#!/usr/bin/env python3
"""Build the standalone Sequentry signal center from local snapshots."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AIHOT_PATH = ROOT / "data" / "aihot.json"
COMMERCE_PATH = ROOT / "data" / "commerce.json"
OUT = ROOT / "briefs" / "index.html"


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def script_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def build_payload() -> dict:
    aihot = read_json(AIHOT_PATH)
    commerce = read_json(COMMERCE_PATH)
    items = []

    for item in aihot.get("items", []):
        if not isinstance(item, dict):
            continue
        items.append({
            "id": item.get("id", ""),
            "channel": "aihot",
            "title": item.get("title", ""),
            "summary": item.get("summary", ""),
            "source": item.get("source", "AI 资讯"),
            "published_at": item.get("published_at", ""),
            "category": item.get("category", "AI 动态"),
            "raw_category": "ai",
            "source_score": item.get("source_score"),
            "permalink": item.get("permalink", ""),
            "original_url": item.get("original_url", ""),
        })

    for item in commerce.get("items", []):
        if not isinstance(item, dict):
            continue
        items.append({
            "id": item.get("id", ""),
            "channel": "commerce",
            "title": item.get("title", ""),
            "summary": item.get("summary", ""),
            "source": item.get("source", ""),
            "published_at": item.get("published_at", ""),
            "category": item.get("category", "跨境信号"),
            "raw_category": item.get("raw_category", ""),
            "theme": item.get("theme", ""),
            "market": item.get("market", ""),
            "priority": item.get("priority", ""),
            "internal_score": item.get("internal_score"),
            "tier": item.get("tier", ""),
            "source_id": item.get("source_id", ""),
            "featured": bool(item.get("featured")),
            "original_title": item.get("original_title", ""),
            "confirmations": item.get("confirmations", 0),
            "original_url": item.get("original_url", ""),
        })

    items.sort(
        key=lambda item: (
            str(item.get("published_at") or ""),
            item.get("channel") == "commerce",
            int(item.get("internal_score") or item.get("source_score") or 0),
        ),
        reverse=True,
    )
    return {
        "generated_at": aihot.get("fetched_at") or commerce.get("generated_at") or "",
        "aihot_updated_at": aihot.get("fetched_at", ""),
        "commerce_updated_at": commerce.get("generated_at", ""),
        "aihot_stale": bool(aihot.get("stale")),
        "hot_topics": aihot.get("hot_topics", []),
        "commerce_total": commerce.get("count", 0),
        "source_count": commerce.get("source_count", 0),
        "score_min": commerce.get("score_min", 60),
        "editorial_overview": commerce.get("overview", ""),
        "items": items,
    }


def build_html(payload: dict) -> str:
    data = script_json(payload)
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="序引信号中心：AI 动态、跨境政策与市场信号的每日聚合。">
  <title>信号中心｜序引 SEQUENTRY</title>
  <style>
    :root{{--ink:#0B0C0E;--graphite:#596579;--muted:#7A8494;--line:#D8DEE7;--panel:#EEF2F6;--bg:#F5F7FA;--paper:#FFF;--blue:#2859FF;--red:#C43B32;--cat-platform:#2F4B6E;--cat-brand:#2F6E5B;--cat-market:#8A5A25;--cat-compliance:#B0341F;--cat-ops:#5D6A2C;--header:64px}}
    *{{box-sizing:border-box}}
    html{{scroll-behavior:smooth}}
    body{{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,"SF Pro Display","Noto Sans SC","Microsoft YaHei",sans-serif;-webkit-font-smoothing:antialiased}}
    a{{color:inherit}}
    button,input,select{{font:inherit}}
    .mono{{font-family:"SFMono-Regular",Consolas,"Liberation Mono",monospace}}
    .topbar{{height:var(--header);display:flex;align-items:center;border-bottom:1px solid var(--line);background:rgba(245,247,250,.96);position:sticky;top:0;z-index:20}}
    .topbar-inner{{width:min(1480px,calc(100% - 40px));margin:auto;display:flex;align-items:center;gap:24px}}
    .brand{{display:flex;align-items:center;gap:10px;text-decoration:none;min-width:max-content}}
    .brand img{{width:28px;height:28px}}
    .brand-copy{{display:flex;align-items:baseline;gap:7px;font-weight:780;letter-spacing:-.02em}}
    .brand-copy small{{font-size:9px;letter-spacing:.14em;color:var(--graphite)}}
    .topnav{{margin-left:auto;display:flex;gap:6px;align-items:center}}
    .topnav a{{text-decoration:none;color:var(--graphite);font-size:13px;padding:8px 10px;border:1px solid transparent}}
    .topnav a[aria-current="page"],.topnav a:hover{{color:var(--blue);border-color:var(--line);background:var(--paper)}}
    .layout{{width:min(1480px,calc(100% - 40px));margin:0 auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:32px;padding:32px 0 72px}}
    .rail{{position:sticky;top:96px;align-self:start}}
    .eyebrow{{font-size:10px;letter-spacing:.16em;color:var(--graphite);font-weight:750;text-transform:uppercase}}
    .rail-title{{font-size:12px;margin:0 0 12px;color:var(--graphite)}}
    .filter-list{{display:grid;border-top:1px solid var(--line)}}
    .filter{{appearance:none;border:0;border-bottom:1px solid var(--line);background:transparent;text-align:left;padding:12px 8px;display:flex;justify-content:space-between;gap:12px;cursor:pointer;color:var(--graphite)}}
    .filter:hover,.filter.active{{color:var(--blue);background:var(--paper)}}
    .filter b{{font-size:12px}}.filter span{{font-size:10px}}
    .rail-block{{margin-top:28px;padding-top:16px;border-top:2px solid var(--ink)}}
    .topic-list{{margin:10px 0 0;padding:0;list-style:none}}
    .topic-list li{{font-size:11px;line-height:1.55;color:var(--graphite);padding:7px 0;border-bottom:1px solid var(--line)}}
    .source-note{{font-size:10px;line-height:1.65;color:var(--muted);margin:12px 0 0}}
    .hero{{border-top:4px solid var(--ink);padding:24px 0 22px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:24px;border-bottom:1px solid var(--line)}}
    .hero h1{{font-size:clamp(34px,5vw,68px);line-height:.96;letter-spacing:-.055em;margin:8px 0 14px;max-width:780px}}
    .hero p{{margin:0;max-width:690px;color:var(--graphite);font-size:14px;line-height:1.7}}
    .hero-stats{{display:grid;grid-template-columns:repeat(2,120px);align-content:end}}
    .stat{{border-left:1px solid var(--line);padding:8px 0 8px 14px}}
    .stat b{{display:block;font-size:26px;line-height:1;letter-spacing:-.04em}}
    .stat span{{display:block;margin-top:6px;font-size:9px;letter-spacing:.1em;color:var(--graphite)}}
    .status{{display:flex;align-items:center;gap:8px;margin-top:18px;font-size:10px;color:var(--graphite)}}
    .status-dot{{width:7px;height:7px;border:1px solid var(--graphite);background:var(--paper)}}
    .status-dot.live{{background:var(--blue);border-color:var(--blue)}}
    .facets{{border-bottom:1px solid var(--line);padding:14px 0 12px;display:grid;gap:9px}}
    .facet-row{{display:grid;grid-template-columns:62px minmax(0,1fr);gap:10px;align-items:start}}
    .facet-label{{font-size:9px;letter-spacing:.1em;color:var(--graphite);padding-top:7px}}
    .facet-options{{display:flex;flex-wrap:wrap;gap:5px}}
    .facet{{appearance:none;border:1px solid var(--line);background:var(--paper);color:var(--graphite);padding:6px 9px;font-size:10px;cursor:pointer}}
    .facet:hover{{border-color:var(--graphite);color:var(--ink)}}
    .facet.active{{background:var(--ink);border-color:var(--ink);color:var(--paper)}}
    .date-system{{display:inline-flex;align-items:center;gap:7px;margin-left:4px}}
    .date-select{{height:29px;min-width:214px;border:1px solid var(--line);background:var(--paper);color:var(--graphite);padding:0 28px 0 9px;font-size:10px;cursor:pointer;outline:0}}
    .date-select:hover,.date-select:focus{{border-color:var(--blue);color:var(--ink)}}
    .date-availability{{font-size:9px;color:var(--muted);white-space:nowrap}}
    .toolbar{{min-height:66px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--line)}}
    .search{{flex:1;display:flex;align-items:center;gap:10px;background:var(--paper);border:1px solid var(--line);height:38px;padding:0 12px}}
    .search:focus-within{{border-color:var(--blue)}}
    .search span{{color:var(--graphite);font-size:12px}}
    .search input{{width:100%;border:0;outline:0;background:transparent;color:var(--ink);font-size:12px}}
    .result-count{{font-size:10px;color:var(--graphite);white-space:nowrap}}
    .viewbar{{min-height:44px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--line)}}
    .viewbar-label{{font-size:9px;letter-spacing:.1em;color:var(--graphite);white-space:nowrap}}
    .view-options{{display:flex;gap:5px}}
    .view-hint{{margin-left:auto;color:var(--muted);font-size:9px;text-align:right}}
    .core-brief{{display:grid;grid-template-columns:150px minmax(0,1fr);gap:18px;padding:20px 18px 18px;border-bottom:1px solid var(--line);background:var(--panel)}}
    .core-brief-label{{padding:2px 14px 0 0;color:var(--graphite);font-size:9px;line-height:1.65;letter-spacing:.12em;text-transform:uppercase}}
    .core-brief-label b{{display:block;color:var(--ink);font-size:11px;letter-spacing:.04em;margin-bottom:4px}}
    .core-brief-body h2{{margin:0 0 8px;font-size:17px;letter-spacing:-.025em}}
    .core-brief-body p{{margin:0;max-width:980px;color:var(--graphite);font-size:12px;line-height:1.85}}
    .core-brief-meta{{margin-top:8px;color:var(--muted);font-size:9px;line-height:1.55}}
    .feed-head{{display:grid;grid-template-columns:118px minmax(0,1fr) 130px;gap:18px;padding:14px 0 9px;color:var(--graphite);font-size:9px;letter-spacing:.12em;border-bottom:2px solid var(--ink)}}
    .feed-head-tools{{display:flex;justify-content:flex-end;gap:10px;letter-spacing:0}}
    .feed-head-tools button{{appearance:none;border:0;background:transparent;color:var(--graphite);padding:0;cursor:pointer;font-size:9px}}
    .feed-head-tools button:hover{{color:var(--blue);text-decoration:underline;text-underline-offset:3px}}
    .day{{padding-top:26px}}
    .day-label{{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:8px}}
    .day-label h2{{margin:0;font-size:17px;letter-spacing:-.025em}}
    .day-label span{{font-size:9px;color:var(--graphite)}}
    .category-group{{border-top:1px solid var(--ink);margin-top:14px}}
    .category-toggle{{appearance:none;width:100%;border:0;background:var(--paper);color:var(--ink);display:grid;grid-template-columns:minmax(0,1fr) auto auto;align-items:center;gap:16px;padding:12px 4px;text-align:left;cursor:pointer}}
    .category-toggle:hover{{color:var(--blue)}}
    .category-toggle-name{{display:flex;align-items:center;gap:9px;font-size:14px;font-weight:780;letter-spacing:-.01em}}
    .category-dot{{width:7px;height:7px;border-radius:50%;background:var(--graphite);flex:0 0 auto}}
    .category-dot.platform-channel{{background:var(--cat-platform)}}
    .category-dot.compliance-fulfillment{{background:var(--cat-compliance)}}
    .category-dot.market-product{{background:var(--cat-market)}}
    .category-dot.brand-retail{{background:var(--cat-brand)}}
    .category-dot.supply-ops{{background:var(--cat-ops)}}
    .category-toggle-meta{{font-size:9px;color:var(--graphite);white-space:nowrap}}
    .category-toggle-state{{font-size:9px;color:var(--blue);min-width:26px;text-align:right}}
    .category-sources[hidden]{{display:none}}
    .category-sources{{padding-left:14px;border-left:1px solid var(--line)}}
    .source-group{{border-top:1px solid var(--line)}}
    .source-group+.source-group{{margin-top:6px}}
    .source-toggle{{appearance:none;width:100%;border:0;background:var(--panel);color:var(--ink);display:grid;grid-template-columns:minmax(0,1fr) auto auto;align-items:center;gap:16px;padding:10px 12px;text-align:left;cursor:pointer}}
    .source-toggle:hover{{background:var(--paper);color:var(--blue)}}
    .source-toggle-name{{font-size:11px;font-weight:780;letter-spacing:.02em}}
    .source-toggle-meta{{font-size:9px;color:var(--graphite);white-space:nowrap}}
    .source-toggle-state{{font-size:9px;color:var(--blue);min-width:26px;text-align:right}}
    .source-items[hidden]{{display:none}}
    .source-items .signal:first-child{{border-top:0}}
    .timeline-group{{border-top:1px solid var(--ink);margin-top:18px}}
    .timeline-group:first-child{{margin-top:14px}}
    .timeline-track[hidden]{{display:none}}
    .timeline-track{{padding-left:18px;border-left:1px solid var(--line)}}
    .timeline-day{{display:grid;grid-template-columns:92px minmax(0,1fr);gap:14px;position:relative}}
    .timeline-day+.timeline-day{{border-top:1px solid var(--line)}}
    .timeline-marker{{padding:18px 0;color:var(--graphite);font-size:9px}}
    .timeline-marker::before{{content:"";position:absolute;left:-22px;top:23px;width:7px;height:7px;border:2px solid var(--paper);background:var(--graphite);border-radius:50%}}
    .timeline-day-items .signal{{grid-template-columns:104px minmax(0,1fr) 110px}}
    .timeline-day-items .signal:first-child{{border-top:0}}
    .signal{{display:grid;grid-template-columns:118px minmax(0,1fr) 130px;gap:18px;padding:18px 0;border-top:1px solid var(--line);transition:background .16s ease}}
    .signal:hover{{background:var(--paper)}}
    .meta{{font-size:9px;color:var(--graphite);line-height:1.65;padding-left:4px}}
    .channel{{display:inline-flex;align-items:center;min-height:19px;padding:2px 6px;border:1px solid var(--line);color:var(--ink);font-size:9px;font-weight:780;letter-spacing:.06em;margin-bottom:7px;background:var(--paper)}}
    .channel.ai{{border-color:var(--line);color:var(--graphite)}}
    .source-name{{display:block;font-size:10px;line-height:1.4;color:var(--ink);margin-bottom:6px}}
    .signal-main h3{{font-size:16px;line-height:1.45;letter-spacing:-.018em;margin:0}}
    .signal-main h3 a{{text-decoration:none}}
    .signal-main h3 a:hover{{color:var(--blue);text-decoration:underline;text-underline-offset:3px}}
    .summary{{font-size:12px;line-height:1.7;color:var(--graphite);margin:8px 0 0;max-width:840px;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;overflow:hidden}}
    .summary.expanded{{display:block;-webkit-line-clamp:unset;overflow:visible}}
    .summary-toggle{{appearance:none;border:0;background:transparent;color:var(--blue);padding:4px 0 0;font-size:9px;cursor:pointer}}
    .summary-toggle:hover{{text-decoration:underline;text-underline-offset:3px}}
    .source-row{{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:10px;font-size:9px;color:var(--muted)}}
    .source-row a{{color:var(--blue);text-decoration:none}}
    .source-row a:hover{{text-decoration:underline}}
    .strength{{margin-top:8px}}
    .strength-label{{font-size:8px;color:var(--graphite);margin-bottom:4px}}
    .strength-bar{{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;width:72px}}
    .strength-bar i{{display:block;height:3px;background:var(--line)}}
    .strength-bar i.on{{background:var(--ink)}}
    .source-score{{font-size:9px;color:var(--graphite);margin-top:7px}}
    .action{{display:flex;justify-content:flex-end;align-items:flex-start}}
    .action a{{display:inline-flex;align-items:center;justify-content:center;width:76px;height:28px;border:1px solid var(--line);font-size:10px;text-decoration:none;color:var(--graphite);background:var(--paper)}}
    .action a:hover{{border-color:var(--blue);color:var(--blue)}}
    .empty{{padding:64px 0;border-bottom:1px solid var(--line);color:var(--graphite);font-size:13px}}
    .load-wrap{{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:24px 0;border-top:1px solid var(--line)}}
    .load-note{{font-size:10px;color:var(--graphite)}}
    .load-more{{border:1px solid var(--line);background:var(--paper);color:var(--blue);padding:9px 14px;font-size:11px;cursor:pointer}}
    .load-more:hover{{border-color:var(--blue)}}
    footer{{border-top:1px solid var(--line);padding:20px 0 0;margin-top:40px;display:flex;justify-content:space-between;gap:20px;color:var(--muted);font-size:9px;line-height:1.6}}
    @media(max-width:920px){{.layout{{grid-template-columns:1fr;gap:20px}}.rail{{position:static}}.filter-list{{grid-template-columns:repeat(3,1fr)}}.filter{{border-right:1px solid var(--line)}}.rail-block{{display:none}}.hero{{grid-template-columns:1fr}}.hero-stats{{grid-template-columns:repeat(2,1fr)}}}}
    @media(max-width:620px){{.topbar-inner,.layout{{width:calc(100% - 24px)}}.brand-copy small{{display:none}}.topnav a{{font-size:11px;padding:7px 6px}}.hero h1{{font-size:42px}}.facet-row{{grid-template-columns:1fr;gap:5px}}.facet-label{{padding-top:0}}.date-system{{width:100%;margin:3px 0 0;align-items:flex-start;flex-direction:column}}.date-select{{width:100%}}.viewbar{{align-items:flex-start;flex-direction:column;padding:10px 0;gap:7px}}.view-hint{{margin-left:0;text-align:left}}.core-brief{{grid-template-columns:1fr;background:var(--panel);padding:16px 14px;gap:8px}}.core-brief-label{{padding:0}}.feed-head{{display:none}}.category-toggle,.source-toggle{{grid-template-columns:minmax(0,1fr) auto;padding:10px 8px}}.category-toggle-meta,.source-toggle-meta{{grid-column:1}}.category-toggle-state,.source-toggle-state{{grid-column:2;grid-row:1 / span 2}}.category-sources{{padding-left:7px}}.timeline-track{{padding-left:10px}}.timeline-day{{grid-template-columns:1fr;gap:0}}.timeline-marker{{padding:12px 0 0}}.timeline-marker::before{{display:none}}.timeline-day-items .signal,.signal{{grid-template-columns:72px minmax(0,1fr);gap:12px}}.action{{grid-column:2;justify-content:flex-start}}.signal-main h3{{font-size:15px}}footer{{display:block}}}}
    @media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;transition:none!important}}}}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="../" aria-label="返回序引导航首页">
        <img src="../assets/sequentry-graphite-mark-primary.svg" alt="">
        <span class="brand-copy">序引 <small>SEQUENTRY</small></span>
      </a>
      <nav class="topnav" aria-label="主导航">
        <a href="../">导航</a>
        <a href="./" aria-current="page">信号</a>
        <a href="../brand.html">品牌研究</a>
      </nav>
    </div>
  </header>
  <main class="layout">
    <aside class="rail" aria-label="信号筛选">
      <p class="rail-title eyebrow">Signal desk</p>
      <div class="filter-list" id="channelFilters"></div>
      <div class="rail-block">
        <div class="eyebrow">今日 AI 资讯</div>
        <ul class="topic-list" id="hotTopics"></ul>
        <p class="source-note">AI 资讯汇集公开来源，优先展示原始信源与原文链接。部分摘要经智能整理，仅供信息参考。</p>
      </div>
    </aside>
    <section>
      <div class="hero">
        <div>
          <div class="eyebrow">Sequentry intelligence</div>
          <h1>信号中心</h1>
          <p>汇集全球平台政策、合规、市场、品牌、供应链与 AI 动态，帮助出海团队更快识别变化、风险与机会。</p>
          <div class="status"><span class="status-dot" id="statusDot"></span><span id="updatedAt">读取本地快照</span></div>
        </div>
        <div class="hero-stats">
          <div class="stat"><b id="commerceCount">0</b><span>跨境信号</span></div>
          <div class="stat"><b id="aiCount">0</b><span>AI 资讯</span></div>
        </div>
      </div>
      <div class="facets" aria-label="日期与分类筛选">
        <div class="facet-row"><span class="facet-label mono">日期</span><div class="facet-options" id="dateFilters"></div></div>
        <div class="facet-row"><span class="facet-label mono">分类</span><div class="facet-options" id="categoryFilters"></div></div>
      </div>
      <div class="toolbar">
        <label class="search"><span>⌕</span><input id="searchInput" type="search" placeholder="搜索标题、摘要、来源、市场" autocomplete="off"></label>
        <div class="result-count mono" id="resultCount">0 SIGNALS</div>
      </div>
      <div class="viewbar" aria-label="信息组织方式">
        <span class="viewbar-label mono">组织方式</span>
        <div class="view-options" id="viewFilters"></div>
        <span class="view-hint" id="viewHint">按日期查看分类与信源</span>
      </div>
      <section class="core-brief" aria-labelledby="coreBriefTitle">
        <div class="core-brief-label mono"><b>核心摘要</b>Core brief</div>
        <div class="core-brief-body">
          <h2 id="coreBriefTitle">当前信息主线</h2>
          <p id="coreBriefText">正在归纳当前范围内的信息主题、重点来源与高强度事件。</p>
          <div class="core-brief-meta mono" id="coreBriefMeta">依据当前信息整理 · 重要信息请以原始来源为准</div>
        </div>
      </section>
      <div class="feed-head mono"><span>来源 / 时间</span><span id="feedStructureLabel">按日期、分类与信源归并</span><span class="feed-head-tools"><button id="expandAllGroups" type="button">展开全部</button><button id="collapseAllGroups" type="button">折叠全部</button></span></div>
      <div id="feed"></div>
      <div class="load-wrap" id="loadWrap"><span class="load-note mono" id="loadNote"></span><button class="load-more" id="loadMore" type="button">继续加载</button></div>
      <footer><span>© Sequentry · 序引信号中心</span><span>信息来自公开来源，版权归原作者及发布机构所有。内容仅供行业研究，不构成商业、投资或法律建议。</span></footer>
    </section>
  </main>
  <script>
    const DATA={data};
    const state={{channel:'all',date:'1',exactDate:'',category:'all',query:'',view:'date',limit:120,groupOverrides:new Map()}};
    const labels={{all:'全部信号',commerce:'跨境资讯',aihot:'AI 资讯'}};
    const dateOptions=[['1','今日'],['3','近 3 天'],['7','近 7 天'],['30','近 30 天'],['all','全部日期']];
    const categoryOptions=[['all','全部分类'],['platform-channel','平台政策'],['compliance-fulfillment','合规履约'],['market-product','市场需求'],['brand-retail','品牌媒体'],['supply-ops','供应链物流'],['ai','AI 资讯']];
    const categoryLabels=Object.fromEntries(categoryOptions);
    const viewOptions=[['date','日期视图'],['category','分类时间线'],['source','信源时间线']];
    const viewHints={{date:'按日期查看大分类与信源',category:'按模块查看跨日期变化',source:'按媒体查看跨日期报道'}};
    const categoryInterpretations={{
      'platform-channel':'平台政策与产品能力更新较集中，卖家运营流程、流量入口和平台依赖关系可能发生调整。',
      'compliance-fulfillment':'合规与政策变化正在提高进入门槛，应优先核查税务、认证、关务和平台执行节点。',
      'market-product':'市场需求与消费变化较多，选品和区域机会需要结合趋势、竞争与转化数据继续验证。',
      'brand-retail':'品牌与媒体动作集中，内容、渠道组合和品牌表达正成为主要竞争信号。',
      'supply-ops':'供应链与物流信号密集，成本、时效和运输稳定性是当前最直接的经营变量。',
      'ai':'AI 资讯以产品与工具更新为主，更适合作为自动化、研发和内容效率的补充观察。'
    }};
    const esc=value=>String(value??'').replace(/[&<>"']/g,char=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[char]));
    const safeUrl=value=>/^https?:\/\//i.test(String(value||''))?String(value):'#';
    const day=value=>String(value||'').slice(0,10)||'日期待核验';
    const fmtUpdated=value=>{{if(!value)return '暂无更新时间';const d=new Date(value);return Number.isNaN(d.getTime())?String(value):new Intl.DateTimeFormat('zh-CN',{{month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false,timeZone:'Asia/Shanghai'}}).format(d)+' 更新';}};
    const strength=score=>{{const n=Number(score);if(!Number.isFinite(n))return 0;if(n>=90)return 4;if(n>=80)return 3;if(n>=70)return 2;return 1;}};
    const latestDay=DATA.items.map(item=>day(item.published_at)).filter(value=>/^\d{{4}}-\d{{2}}-\d{{2}}$/.test(value)).sort().reverse()[0]||day(new Date().toISOString());
    function itemText(item){{return [item.title,item.original_title,item.summary,item.source,item.category,item.theme,item.market].join(' ').toLowerCase();}}
    function itemCategory(item){{return item.channel==='aihot'?'ai':(item.category||item.raw_category||'other');}}
    function matchesChannelAndQuery(item){{const q=state.query.trim().toLowerCase();return (state.channel==='all'||item.channel===state.channel)&&(!q||itemText(item).includes(q));}}
    function matchesNonDate(item){{return matchesChannelAndQuery(item)&&(state.category==='all'||itemCategory(item)===state.category);}}
    function matchesDate(item){{if(state.exactDate)return day(item.published_at)===state.exactDate;if(state.date==='all')return true;const a=new Date(latestDay+'T00:00:00Z');const b=new Date(day(item.published_at)+'T00:00:00Z');const delta=(a-b)/86400000;return Number.isFinite(delta)&&delta>=0&&delta<Number(state.date);}}
    function availableDateCounts(){{return DATA.items.filter(matchesNonDate).reduce((acc,item)=>{{const value=day(item.published_at);if(/^\d{{4}}-\d{{2}}-\d{{2}}$/.test(value))acc[value]=(acc[value]||0)+1;return acc;}},{{}});}}
    function filtered(){{return DATA.items.filter(item=>matchesNonDate(item)&&matchesDate(item)).sort((a,b)=>{{const dateOrder=day(b.published_at).localeCompare(day(a.published_at));if(dateOrder)return dateOrder;const channelOrder=(b.channel==='commerce')-(a.channel==='commerce');if(channelOrder)return channelOrder;return Number(b.internal_score||0)-Number(a.internal_score||0);}});}}
    function signalMarkup(item){{
      const isAI=item.channel==='aihot';
      const label=isAI?'AI资讯':(categoryLabels[item.category]||item.theme||'跨境信号');
      const primary=safeUrl(item.original_url||item.permalink);
      const sourceLink=safeUrl(item.original_url);
      const meter=!isAI&&item.internal_score!=null?`<div class="strength"><div class="strength-label mono">序引信号强度</div><div class="strength-bar">${{[1,2,3,4].map(n=>`<i class="${{n<=strength(item.internal_score)?'on':''}}"></i>`).join('')}}</div></div>`:'';
      const sourceAction=sourceLink!=='#'?`<a href="${{sourceLink}}" target="_blank" rel="noopener noreferrer">访问原始来源 ↗</a>`:'';
      const attribution=isAI?'<span>摘要经智能整理 · 请以原文为准</span>':'';
      const tier=!isAI&&item.tier?`<span>信源 ${{esc(item.tier)}} 级</span>`:'';
      const hasLongSummary=String(item.summary||'').length>150;
      const summaryMarkup=item.summary?`<p class="summary">${{esc(item.summary)}}</p>${{hasLongSummary?'<button class="summary-toggle" type="button" data-summary-toggle aria-expanded="false">展开摘要</button>':''}}`:'';
      return `<article class="signal">
        <div class="meta mono"><strong class="source-name">${{esc(item.source||'来源信息待补充')}}</strong><span class="channel ${{isAI?'ai':''}}">${{esc(label)}}</span><br>${{esc(day(item.published_at))}}${{meter}}</div>
        <div class="signal-main"><h3><a href="${{primary}}" target="_blank" rel="noopener noreferrer">${{esc(item.title)}}</a></h3>${{summaryMarkup}}<div class="source-row">${{sourceAction}}${{attribution}}${{tier}}${{item.market?`<span>${{esc(item.market)}}</span>`:''}}</div></div>
        <div class="action"><a href="${{primary}}" target="_blank" rel="noopener noreferrer">查看详情</a></div>
      </article>`;
    }}
    function renderFilters(){{
      const counts={{all:DATA.items.length,aihot:DATA.items.filter(x=>x.channel==='aihot').length,commerce:DATA.items.filter(x=>x.channel==='commerce').length}};
      document.getElementById('channelFilters').innerHTML=Object.keys(labels).map(key=>`<button class="filter ${{state.channel===key?'active':''}}" type="button" data-channel="${{key}}"><b>${{labels[key]}}</b><span class="mono">${{counts[key]}}</span></button>`).join('');
      document.querySelectorAll('[data-channel]').forEach(button=>button.addEventListener('click',()=>{{state.channel=button.dataset.channel;state.category='all';state.limit=120;render();}}));
      document.getElementById('aiCount').textContent=counts.aihot;document.getElementById('commerceCount').textContent=counts.commerce;
    }}
    function renderFacets(){{
      const dateCounts=availableDateCounts();
      const availableDates=Object.keys(dateCounts).sort().reverse();
      if(state.exactDate&&!dateCounts[state.exactDate]){{state.exactDate='';state.date='1';}}
      const categoryScope=DATA.items.filter(item=>matchesChannelAndQuery(item)&&matchesDate(item));
      const quickDates=dateOptions.map(option=>`<button class="facet ${{!state.exactDate&&state.date===option[0]?'active':''}}" type="button" data-date="${{option[0]}}">${{option[1]}}</button>`).join('');
      const exactOptions=availableDates.map(value=>`<option value="${{value}}" ${{state.exactDate===value?'selected':''}}>${{value}} · ${{dateCounts[value]}} 条</option>`).join('');
      const availability=availableDates.length?`可选 ${{availableDates.length}} 天 · ${{availableDates.at(-1)}}—${{availableDates[0]}}`:'当前条件无可选日期';
      document.getElementById('dateFilters').innerHTML=quickDates+`<span class="date-system"><select class="date-select" id="exactDateSelect" aria-label="选择有信号的具体日期"><option value="">选择具体日期（仅列有数据日期）</option>${{exactOptions}}</select><span class="date-availability mono">${{availability}}</span></span>`;
      document.getElementById('categoryFilters').innerHTML=categoryOptions.map(option=>{{const count=option[0]==='all'?categoryScope.length:categoryScope.filter(item=>itemCategory(item)===option[0]).length;return `<button class="facet ${{state.category===option[0]?'active':''}}" type="button" data-category="${{option[0]}}">${{option[1]}} <span class="mono">${{count}}</span></button>`;}}).join('');
      document.querySelectorAll('[data-date]').forEach(button=>button.addEventListener('click',()=>{{state.date=button.dataset.date;state.exactDate='';state.limit=120;render();}}));
      document.getElementById('exactDateSelect').addEventListener('change',event=>{{if(!event.target.value)return;state.exactDate=event.target.value;state.date='exact';state.limit=120;render();}});
      document.querySelectorAll('[data-category]').forEach(button=>button.addEventListener('click',()=>{{state.category=button.dataset.category;state.limit=120;render();}}));
    }}
    function renderTopics(){{
      const topics=Array.isArray(DATA.hot_topics)?DATA.hot_topics.slice(0,5):[];
      document.getElementById('hotTopics').innerHTML=topics.length?topics.map(topic=>`<li>${{esc(typeof topic==='string'?topic:(topic.title||topic.topic||topic.name||JSON.stringify(topic)))}}</li>`).join(''):'<li>等待下一次热点快照</li>';
    }}
    function ranked(items,keyFn){{
      const counts={{}};
      items.forEach(item=>{{const key=String(keyFn(item)||'').trim();if(key)counts[key]=(counts[key]||0)+1;}});
      return Object.entries(counts).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
    }}
    function compactTitle(value,limit=38){{const text=String(value||'').trim();return text.length>limit?text.slice(0,limit).trim()+'…':text;}}
    function scopeLabel(){{
      const relative=(dateOptions.find(option=>option[0]===state.date)||[])[1]||'当前日期';
      const parts=[state.exactDate||relative];
      if(state.channel!=='all')parts.push(labels[state.channel]);
      if(state.category!=='all')parts.push(categoryLabels[state.category]||state.category);
      if(state.query.trim())parts.push(`搜索“${{compactTitle(state.query.trim(),14)}}”`);
      return parts.join(' / ');
    }}
    function renderCoreBrief(items){{
      const title=document.getElementById('coreBriefTitle');
      const text=document.getElementById('coreBriefText');
      const meta=document.getElementById('coreBriefMeta');
      title.textContent=scopeLabel()+' · 信息主线';
      if(!items.length){{text.textContent='当前条件下暂无可汇总的信息，请调整日期、来源、分类或搜索条件。';meta.textContent='当前范围暂无信息';return;}}
      const commerce=items.filter(item=>item.channel==='commerce');
      const ai=items.length-commerce.length;
      const categories=ranked(items,item=>itemCategory(item)).filter(entry=>categoryLabels[entry[0]]).slice(0,3);
      const sources=ranked(items,item=>item.source).slice(0,3);
      const strong=commerce.filter(item=>Number(item.internal_score||0)>=80).sort((a,b)=>Number(b.internal_score||0)-Number(a.internal_score||0)).slice(0,2);
      const parts=[];
      const useEditorial=Boolean(DATA.editorial_overview)&&!state.exactDate&&state.date==='1'&&state.channel==='all'&&state.category==='all'&&!state.query.trim();
      if(useEditorial)parts.push(`今日精选研判：${{String(DATA.editorial_overview).trim()}}`);
      parts.push(`当前范围共收录 ${{items.length}} 条信号，其中跨境资讯 ${{commerce.length}} 条、AI 资讯 ${{ai}} 条。`);
      if(categories.length)parts.push(`信息主要集中在${{categories.map(entry=>`${{categoryLabels[entry[0]]}}（${{entry[1]}}）`).join('、')}}。`);
      if(sources.length)parts.push(`高频来源包括${{sources.map(entry=>`${{entry[0]}}（${{entry[1]}}）`).join('、')}}。`);
      if(strong.length)parts.push(`高强度事件优先指向${{strong.map(item=>`「${{compactTitle(item.title)}}」`).join('与')}}。`);
      const leadCategory=categories[0]?.[0];
      if(leadCategory&&categoryInterpretations[leadCategory])parts.push(`整体解读：${{categoryInterpretations[leadCategory]}}`);
      text.textContent=parts.join('');
      meta.textContent=`依据当前筛选结果整理 · ${{sources.length?`涉及至少 ${{ranked(items,item=>item.source).length}} 个公开来源 · `:''}}重要信息请以原始来源为准`;
    }}
    function maxGroupScore(items){{return items.reduce((max,item)=>Math.max(max,Number(item.internal_score||0)),0);}}
    function sourceGroups(items){{
      const groups={{}};
      items.forEach(item=>{{const source=String(item.source||'来源信息待补充').trim()||'来源信息待补充';(groups[source]??=[]).push(item);}});
      return Object.entries(groups).sort((a,b)=>{{
        const aiOrder=Number(a[1].every(item=>item.channel==='aihot'))-Number(b[1].every(item=>item.channel==='aihot'));
        if(aiOrder)return aiOrder;
        const scoreOrder=maxGroupScore(b[1])-maxGroupScore(a[1]);
        if(scoreOrder)return scoreOrder;
        return b[1].length-a[1].length||a[0].localeCompare(b[0]);
      }});
    }}
    function categoryGroups(items){{
      const groups={{}};
      items.forEach(item=>{{const category=itemCategory(item);(groups[category]??=[]).push(item);}});
      return Object.entries(groups).sort((a,b)=>{{
        const aiOrder=Number(a[0]==='ai')-Number(b[0]==='ai');
        if(aiOrder)return aiOrder;
        const scoreOrder=maxGroupScore(b[1])-maxGroupScore(a[1]);
        if(scoreOrder)return scoreOrder;
        return b[1].length-a[1].length||a[0].localeCompare(b[0]);
      }});
    }}
    function categoryIsOpen(date,category,dateIndex,categoryIndex){{
      if(state.query.trim()||state.category!=='all'||state.channel!=='all')return true;
      const key=`category::${{date}}::${{category}}`;
      if(state.groupOverrides.has(key))return state.groupOverrides.get(key);
      return dateIndex===0&&categoryIndex<2;
    }}
    function sourceIsOpen(date,category,source,dateIndex,sourceIndex){{
      if(state.query.trim())return true;
      const key=`source::${{date}}::${{category}}::${{source}}`;
      if(state.groupOverrides.has(key))return state.groupOverrides.get(key);
      return dateIndex===0&&sourceIndex<2;
    }}
    function sourceGroupMarkup(date,category,items,dateIndex){{
      return sourceGroups(items).map((entry,sourceIndex)=>{{
        const [source,sourceItems]=entry;
        const key=`source::${{date}}::${{category}}::${{source}}`;
        const panelId=`source-${{date.replace(/[^a-z0-9-]/gi,'-')}}-${{category.replace(/[^a-z0-9-]/gi,'-')}}-${{sourceIndex}}`;
        const open=sourceIsOpen(date,category,source,dateIndex,sourceIndex);
        const strongCount=sourceItems.filter(item=>Number(item.internal_score||0)>=80).length;
        const meta=[`${{sourceItems.length}} 条`,strongCount?`${{strongCount}} 条高强度`:'' ].filter(Boolean).join(' · ');
        return `<section class="source-group" data-source-group="${{esc(key)}}">
          <button class="source-toggle" type="button" data-group-toggle data-group-key="${{esc(key)}}" aria-expanded="${{open}}" aria-controls="${{panelId}}">
            <span class="source-toggle-name">${{esc(source)}}</span><span class="source-toggle-meta mono">${{esc(meta)}}</span><span class="source-toggle-state group-toggle-state">${{open?'收起':'展开'}}</span>
          </button>
          <div class="source-items" id="${{panelId}}" ${{open?'':'hidden'}}>${{sourceItems.map(signalMarkup).join('')}}</div>
        </section>`;
      }}).join('');
    }}
    function categoryGroupMarkup(date,items,dateIndex){{
      return categoryGroups(items).map((entry,categoryIndex)=>{{
        const [category,categoryItems]=entry;
        const key=`category::${{date}}::${{category}}`;
        const panelId=`category-${{date.replace(/[^a-z0-9-]/gi,'-')}}-${{categoryIndex}}`;
        const open=categoryIsOpen(date,category,dateIndex,categoryIndex);
        const strongCount=categoryItems.filter(item=>Number(item.internal_score||0)>=80).length;
        const meta=[`${{categoryItems.length}} 条`,`${{sourceGroups(categoryItems).length}} 个信源`,strongCount?`${{strongCount}} 条高强度`:'' ].filter(Boolean).join(' · ');
        return `<section class="category-group" data-category-group="${{esc(key)}}">
          <button class="category-toggle" type="button" data-group-toggle data-group-key="${{esc(key)}}" aria-expanded="${{open}}" aria-controls="${{panelId}}">
            <span class="category-toggle-name"><i class="category-dot ${{esc(category)}}"></i>${{esc(categoryLabels[category]||'其它信号')}}</span><span class="category-toggle-meta mono">${{esc(meta)}}</span><span class="category-toggle-state group-toggle-state">${{open?'收起':'展开'}}</span>
          </button>
          <div class="category-sources" id="${{panelId}}" ${{open?'':'hidden'}}>${{sourceGroupMarkup(date,category,categoryItems,dateIndex)}}</div>
        </section>`;
      }}).join('');
    }}
    function timelineDaysMarkup(items){{
      const groups={{}};
      items.forEach(item=>{{(groups[day(item.published_at)]??=[]).push(item);}});
      return Object.keys(groups).sort().reverse().map(date=>`<section class="timeline-day"><div class="timeline-marker mono">${{esc(date)}}</div><div class="timeline-day-items">${{groups[date].sort((a,b)=>Number(b.internal_score||0)-Number(a.internal_score||0)).map(signalMarkup).join('')}}</div></section>`).join('');
    }}
    function timelineGroupIsOpen(mode,key,groupIndex){{
      if(state.query.trim()||state.category!=='all'||state.channel!=='all')return true;
      const overrideKey=`timeline::${{mode}}::${{key}}`;
      if(state.groupOverrides.has(overrideKey))return state.groupOverrides.get(overrideKey);
      return groupIndex<2;
    }}
    function timelineGroupMarkup(mode,key,items,groupIndex){{
      const overrideKey=`timeline::${{mode}}::${{key}}`;
      const panelId=`timeline-${{mode}}-${{groupIndex}}`;
      const open=timelineGroupIsOpen(mode,key,groupIndex);
      const dates=new Set(items.map(item=>day(item.published_at))).size;
      const relatedCount=mode==='category'?sourceGroups(items).length:categoryGroups(items).length;
      const relatedLabel=mode==='category'?'个信源':'个分类';
      const meta=`${{items.length}} 条 · ${{dates}} 个日期 · ${{relatedCount}} ${{relatedLabel}}`;
      const name=mode==='category'?(categoryLabels[key]||'其它信号'):key;
      const dot=mode==='category'?`<i class="category-dot ${{esc(key)}}"></i>`:'';
      return `<section class="timeline-group">
        <button class="category-toggle" type="button" data-group-toggle data-group-key="${{esc(overrideKey)}}" aria-expanded="${{open}}" aria-controls="${{panelId}}">
          <span class="category-toggle-name">${{dot}}${{esc(name)}}</span><span class="category-toggle-meta mono">${{esc(meta)}}</span><span class="category-toggle-state group-toggle-state">${{open?'收起':'展开'}}</span>
        </button>
        <div class="timeline-track" id="${{panelId}}" ${{open?'':'hidden'}}>${{timelineDaysMarkup(items)}}</div>
      </section>`;
    }}
    function renderTimeline(mode,items){{
      const groups=mode==='category'?categoryGroups(items):sourceGroups(items);
      return groups.map((entry,index)=>timelineGroupMarkup(mode,entry[0],entry[1],index)).join('');
    }}
    function renderViewFilters(){{
      document.getElementById('viewFilters').innerHTML=viewOptions.map(option=>`<button class="facet ${{state.view===option[0]?'active':''}}" type="button" data-view="${{option[0]}}" aria-pressed="${{state.view===option[0]}}">${{option[1]}}</button>`).join('');
      document.getElementById('viewHint').textContent=viewHints[state.view];
      document.getElementById('feedStructureLabel').textContent=state.view==='date'?'按日期、分类与信源归并':state.view==='category'?'按分类查看跨日期时间线':'按信源查看跨日期时间线';
      document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>{{state.view=button.dataset.view;state.limit=120;render();}}));
    }}
    function setVisibleGroups(open){{
      document.querySelectorAll('[data-group-toggle]').forEach(button=>{{
        state.groupOverrides.set(button.dataset.groupKey,open);
        button.setAttribute('aria-expanded',String(open));
        const panel=document.getElementById(button.getAttribute('aria-controls'));
        if(panel)panel.hidden=!open;
        const label=button.querySelector('.group-toggle-state');
        if(label)label.textContent=open?'收起':'展开';
      }});
    }}
    function renderFeed(){{
      const matched=filtered();const items=state.view==='date'?matched.slice(0,state.limit):matched;document.getElementById('resultCount').textContent=`共 ${{matched.length}} 条 · 当前显示 ${{items.length}} 条`;
      renderCoreBrief(matched);
      let feedMarkup='';
      if(items.length&&state.view==='date'){{
        const groups={{}};items.forEach(item=>{{(groups[day(item.published_at)]??=[]).push(item);}});
        feedMarkup=Object.keys(groups).sort().reverse().map((date,dateIndex)=>`<section class="day"><div class="day-label"><h2>${{esc(date)}}</h2><span class="mono">${{groups[date].length}} 条信号 · ${{categoryGroups(groups[date]).length}} 个分类 · ${{sourceGroups(groups[date]).length}} 个信源</span></div>${{categoryGroupMarkup(date,groups[date],dateIndex)}}</section>`).join('');
      }}else if(items.length){{feedMarkup=renderTimeline(state.view,items);}}
      document.getElementById('feed').innerHTML=feedMarkup||'<div class="empty">当前条件下暂无相关信号，请调整日期、来源、分类或搜索词。</div>';
      document.getElementById('loadWrap').style.display=state.view==='date'&&matched.length?'flex':'none';document.getElementById('loadMore').style.display=matched.length>items.length?'inline-flex':'none';document.getElementById('loadNote').textContent=`已显示 ${{items.length}} / ${{matched.length}} 条`;
    }}
    function render(){{renderFilters();renderFacets();renderViewFilters();renderFeed();}}
    document.getElementById('searchInput').addEventListener('input',event=>{{state.query=event.target.value;state.limit=120;render();}});
    document.getElementById('loadMore').addEventListener('click',()=>{{state.limit+=120;renderFeed();}});
    document.getElementById('expandAllGroups').addEventListener('click',()=>setVisibleGroups(true));
    document.getElementById('collapseAllGroups').addEventListener('click',()=>setVisibleGroups(false));
    document.addEventListener('click',event=>{{
      const groupButton=event.target.closest('[data-group-toggle]');
      if(groupButton){{
        const open=groupButton.getAttribute('aria-expanded')!=='true';
        state.groupOverrides.set(groupButton.dataset.groupKey,open);
        groupButton.setAttribute('aria-expanded',String(open));
        const panel=document.getElementById(groupButton.getAttribute('aria-controls'));
        if(panel)panel.hidden=!open;
        const label=groupButton.querySelector('.group-toggle-state');
        if(label)label.textContent=open?'收起':'展开';
        return;
      }}
      const button=event.target.closest('[data-summary-toggle]');
      if(!button)return;
      const summary=button.closest('.signal-main')?.querySelector('.summary');
      if(!summary)return;
      const expanded=summary.classList.toggle('expanded');
      button.setAttribute('aria-expanded',String(expanded));
      button.textContent=expanded?'收起摘要':'展开摘要';
    }});
    document.getElementById('updatedAt').textContent=fmtUpdated(DATA.generated_at)+(DATA.aihot_stale?' · 当前使用缓存':'');
    document.getElementById('statusDot').classList.toggle('live',!DATA.aihot_stale&&DATA.items.length>0);
    renderTopics();render();
  </script>
</body>
</html>
'''


def main() -> int:
    payload = build_payload()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_html(payload), encoding="utf-8")
    print(f"briefs: {OUT}")
    print(f"signals: {len(payload['items'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
