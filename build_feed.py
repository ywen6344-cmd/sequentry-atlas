# -*- coding: utf-8 -*-
"""近期动态快照生成器
   从 feeds 项目的 briefing.json 抽取 -> nav/feed.js (window.NAV_FEED)
   过期了重跑本脚本即可：  python build_feed.py
"""
import json
import re
import unicodedata
from pathlib import Path

SRC = r"C:\Users\延航\Desktop\sequentry-跨境资讯平台\feed-collectors-v2\briefing.json"
SIGNALS = Path(SRC).with_name("signals.json")
OUT = Path(__file__).with_name("feed.js")
INDEX = Path(__file__).with_name("index.html")
N = 6  # 每个模块最多取几条

# briefing 主题 -> 导航模块 id
THEME2CAT = {
    "平台政策": "platform-channel",
    "AI电商":   "platform-channel",
    "关税合规": "compliance-fulfillment",
    "消费趋势": "market-product",
    "品牌·DTC": "brand-retail",
}

# briefing 的主题由模型归类，偶尔会把宏观人口、人物致辞等内容误放进
# “关税合规”。前台只保留能明确对应法规、履约、物流、支付或贸易风险的条目。
COMPLIANCE_CN_TERMS = (
    "合规", "关税", "税务", "海关", "监管", "法规", "物流", "履约", "支付",
    "清关", "进口", "出口", "港口", "供应链", "贸易", "跨境", "制裁", "认证",
)
COMPLIANCE_EN_TERMS = (
    "compliance", "tariff", "customs", "regulation", "logistics", "fulfillment",
    "payment", "port", "import", "export", "supply chain", "trade", "sanction",
)


def normalized_title(item):
    """Return a stable cross-source key for duplicate story detection."""
    value = item.get("title_src") or item.get("title_cn") or ""
    value = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", value)


def canonical_url(value):
    """Drop tracking/query parameters for stable briefing-to-signal matching."""
    return str(value or "").split("?", 1)[0].rstrip("/")


def relevant_to_category(item, cat):
    if cat != "compliance-fulfillment":
        return True
    haystack = " ".join(
        str(item.get(key) or "")
        for key in ("title_cn", "title_src", "reason")
    ).casefold()
    if any(term in haystack for term in COMPLIANCE_CN_TERMS):
        return True
    return any(
        re.search(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", haystack)
        for term in COMPLIANCE_EN_TERMS
    )

b = json.load(open(SRC, encoding="utf-8"))
signal_by_url = {}
if SIGNALS.exists():
    for signal in json.loads(SIGNALS.read_text(encoding="utf-8")):
        signal_url = canonical_url(signal.get("url"))
        if signal_url:
            signal_by_url[signal_url] = signal

by = {}
seen = set()
for it in b.get("items", []):
    cat = THEME2CAT.get(it.get("theme"))
    title = it.get("title_cn") or it.get("title_src") or ""
    url = it.get("url") or ""
    key = normalized_title(it)
    if not cat or not title or not url or not key or key in seen:
        continue
    if not relevant_to_category(it, cat):
        continue
    signal = signal_by_url.get(canonical_url(url))
    if signal and signal.get("date_known") is False:
        continue
    lst = by.setdefault(cat, [])
    if len(lst) >= N:
        continue
    seen.add(key)
    # 可信时优先使用原始信号的发布日期；briefing.ts 可能是抓取时间。
    ts = ((signal or {}).get("ts") or it.get("ts") or "")[:10]
    lst.append({
        "t": title,
        "s": it.get("source", ""),
        "u": url,
        "d": ts,
        "p": it.get("priority", ""),
        "m": it.get("market", ""),
        "score": it.get("score"),
    })

updated = (b.get("generated_at") or "")[:10] or "—"
data = {"updated": updated, "by_cat": by}
out  = "// 近期动态快照 —— build_feed.py 从 feeds 项目生成；已做发布日期校验、跨来源去重与主题相关性过滤。\n"
out += "window.NAV_FEED = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
OUT.write_text(out, encoding="utf-8")

# 静态站可能长期缓存 feed.js；让每次快照同步刷新脚本版本号。
if INDEX.exists():
    index_html = INDEX.read_text(encoding="utf-8")
    # 同一天内也可能多次修正快照，使用完整生成时间避免继续命中旧缓存。
    version = re.sub(r"\D", "", b.get("generated_at") or "")[:14]
    version = version or updated.replace("-", "")
    refreshed = re.sub(
        r'<script src="feed\.js(?:\?v=[^"]*)?"></script>',
        f'<script src="feed.js?v={version}"></script>',
        index_html,
        count=1,
    )
    if refreshed != index_html:
        INDEX.write_text(refreshed, encoding="utf-8")

print("updated:", updated)
print("out:", OUT)
print("index:", INDEX)
for c, l in by.items():
    print(" ", c, len(l))
