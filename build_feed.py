# -*- coding: utf-8 -*-
"""近期动态快照生成器
   从 feeds 项目的 briefing.json 抽取 -> nav/feed.js (window.NAV_FEED)
   过期了重跑本脚本即可：  python build_feed.py
"""
import json
from pathlib import Path

SRC = r"C:\Users\延航\Desktop\sequentry-跨境资讯平台\feed-collectors-v2\briefing.json"
OUT = Path(__file__).with_name("feed.js")
N = 5  # 每个模块取几条

# briefing 主题 -> 导航模块 id
THEME2CAT = {
    "平台政策": "platform-channel",
    "AI电商":   "platform-channel",
    "关税合规": "compliance-fulfillment",
    "消费趋势": "market-product",
    "品牌·DTC": "brand-retail",
}

b = json.load(open(SRC, encoding="utf-8"))
by = {}
for it in b.get("items", []):
    cat = THEME2CAT.get(it.get("theme"))
    if not cat:
        continue
    lst = by.setdefault(cat, [])
    if len(lst) >= N:
        continue
    ts = (it.get("ts") or "")[:10]          # YYYY-MM-DD 完整日期
    lst.append({
        "t": it.get("title_cn") or it.get("title_src") or "",
        "s": it.get("source", ""),
        "u": it.get("url", ""),
        "d": ts,
    })

updated = (b.get("generated_at") or "")[:10] or "—"
data = {"updated": updated, "by_cat": by}
out  = "// 近期动态快照 —— build_feed.py 从 feeds 项目 briefing.json 生成；过期重跑该脚本即可。\n"
out += "window.NAV_FEED = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
OUT.write_text(out, encoding="utf-8")

print("updated:", updated)
print("out:", OUT)
for c, l in by.items():
    print(" ", c, len(l))
