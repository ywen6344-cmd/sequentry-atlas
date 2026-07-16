# -*- coding: utf-8 -*-
"""近期动态快照生成器
   从 feeds 项目的 briefing.json 抽取 -> feed.js + data/commerce.json
   过期了重跑本脚本即可：  python build_feed.py
"""
import json
import html
import re
import unicodedata
from pathlib import Path

SRC = r"C:\Users\延航\Desktop\sequentry-跨境资讯平台\feed-collectors-v2\briefing.json"
SIGNALS = Path(SRC).with_name("signals.json")
TITLE_CACHE = Path(SRC).with_name("title_cache.json")
BRIEF_CACHE = Path(SRC).with_name("briefing_cache.json")
OUT = Path(__file__).with_name("feed.js")
INDEX = Path(__file__).with_name("index.html")
COMMERCE_OUT = Path(__file__).with_name("data") / "commerce.json"
N = 6  # 每个模块最多取几条
FULL_SCORE_MIN = 60
SUMMARY_MAX_CHARS = 680

# briefing 主题 -> 导航模块 id
THEME2CAT = {
    "平台政策": "platform-channel",
    "AI电商":   "platform-channel",
    "关税合规": "compliance-fulfillment",
    "消费趋势": "market-product",
    "品牌·DTC": "brand-retail",
}

RAW2CAT = {
    "platform": "platform-channel",
    "compliance": "compliance-fulfillment",
    "market": "market-product",
    "demand": "market-product",
    "media": "brand-retail",
    "supply": "supply-ops",
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


def clean_summary(value, max_chars=SUMMARY_MAX_CHARS):
    """Turn scraped page fragments into compact, list-safe plain text."""
    text = str(value or "")
    for _ in range(2):
        text = html.unescape(text)
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    clipped = text[: max_chars + 1]
    # Prefer a natural sentence boundary without collapsing to an unhelpfully short fragment.
    boundaries = [clipped.rfind(mark) for mark in ("。", "！", "？", ". ", "! ", "? ", "; ")]
    boundary = max(boundaries)
    if boundary >= int(max_chars * 0.58):
        clipped = clipped[: boundary + 1]
    else:
        clipped = clipped[:max_chars].rstrip(" ,，;；:：")
    return clipped.rstrip() + "…"


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
signals_data = []
if SIGNALS.exists():
    signals_data = json.loads(SIGNALS.read_text(encoding="utf-8"))
    for signal in signals_data:
        signal_url = canonical_url(signal.get("url"))
        if signal_url:
            signal_by_url[signal_url] = signal

by = {}
featured_items = []
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
    seen.add(key)
    # 可信时优先使用原始信号的发布日期；briefing.ts 可能是抓取时间。
    ts = ((signal or {}).get("ts") or it.get("ts") or "")[:10]
    compact_item = {
        "t": title,
        "s": it.get("source", ""),
        "u": url,
        "d": ts,
        "p": it.get("priority", ""),
        "m": it.get("market", ""),
        "score": it.get("score"),
    }
    lst = by.setdefault(cat, [])
    if len(lst) < N:
        lst.append(compact_item)
    featured_items.append({
        "id": canonical_url(url) or key,
        "channel": "commerce",
        "title": title,
        "original_title": it.get("title_src", ""),
        "summary": clean_summary(it.get("reason", "")),
        "source": it.get("source", ""),
        "published_at": ts,
        "category": cat,
        "theme": it.get("theme", ""),
        "market": it.get("market", ""),
        "priority": it.get("priority", ""),
        "internal_score": it.get("score"),
        "original_url": url,
        "verified_date": not bool(signal) or signal.get("date_known") is not False,
    })

# 信号中心读取完整合格库存，而不是只读取 briefing.json 的 30 条精选。
# 低于 60 分和日期不可信的条目仍保留在采集器，但不进入公开信号流。
title_cache = json.loads(TITLE_CACHE.read_text(encoding="utf-8")) if TITLE_CACHE.exists() else {}
brief_cache = json.loads(BRIEF_CACHE.read_text(encoding="utf-8")) if BRIEF_CACHE.exists() else {}
featured_urls = {canonical_url(item.get("original_url")) for item in featured_items}
commerce_items = []
full_seen = set()
for signal in signals_data:
    if signal.get("date_known") is False:
        continue
    try:
        score = int(signal.get("score") or 0)
    except (TypeError, ValueError):
        score = 0
    if score < FULL_SCORE_MIN:
        continue
    url = signal.get("url") or ""
    original_title = signal.get("title") or ""
    key = canonical_url(url) or normalized_title({"title_src": original_title})
    if not key or not original_title or key in full_seen:
        continue
    full_seen.add(key)
    signal_id = str(signal.get("id") or key)
    cached_title = title_cache.get(signal_id)
    cached_brief = brief_cache.get(signal_id) if isinstance(brief_cache.get(signal_id), dict) else {}
    title = cached_title if isinstance(cached_title, str) and cached_title.strip() else original_title
    summary = clean_summary(cached_brief.get("reason") or signal.get("summary") or "")
    raw_category = str(signal.get("category") or "")
    commerce_items.append({
        "id": signal_id,
        "channel": "commerce",
        "title": title,
        "original_title": original_title if original_title != title else "",
        "summary": summary,
        "source": signal.get("source_name", ""),
        "source_id": signal.get("source_id", ""),
        "published_at": str(signal.get("ts") or "")[:10],
        "category": RAW2CAT.get(raw_category, raw_category or "other"),
        "raw_category": raw_category,
        "theme": cached_brief.get("theme", ""),
        "market": signal.get("market", ""),
        "priority": signal.get("priority", ""),
        "internal_score": score,
        "tier": signal.get("tier", ""),
        "confirmations": signal.get("confirmations", 0),
        "escalated": bool(signal.get("escalated")),
        "original_url": url,
        "verified_date": True,
        "featured": canonical_url(url) in featured_urls,
    })

commerce_items.sort(
    key=lambda item: (str(item.get("published_at") or ""), int(item.get("internal_score") or 0)),
    reverse=True,
)

updated = (b.get("generated_at") or "")[:10] or "—"
data = {
    "updated": updated,
    "total": len(commerce_items),
    "source_count": len({item.get("source_id") for item in commerce_items if item.get("source_id")}),
    "score_min": FULL_SCORE_MIN,
    "by_cat": by,
}
out  = "// 近期动态快照 —— build_feed.py 从 feeds 项目生成；已做发布日期校验、跨来源去重与主题相关性过滤。\n"
out += "window.NAV_FEED = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
OUT.write_text(out, encoding="utf-8")

COMMERCE_OUT.parent.mkdir(parents=True, exist_ok=True)
commerce_snapshot = {
    "schema_version": 1,
    "provider": "Sequentry Feed Collectors",
    "generated_at": b.get("generated_at") or updated,
    "count": len(commerce_items),
    "featured_count": len(featured_items),
    "source_count": len({item.get("source_id") for item in commerce_items if item.get("source_id")}),
    "score_min": FULL_SCORE_MIN,
    "overview": clean_summary(b.get("overview") or "", max_chars=520),
    "items": commerce_items,
}
COMMERCE_OUT.write_text(
    json.dumps(commerce_snapshot, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

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
print("commerce:", COMMERCE_OUT, len(commerce_items))
print("index:", INDEX)
for c, l in by.items():
    print(" ", c, len(l))
