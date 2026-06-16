/* ============================================================
 * market_meta.js — 全球开店板块的「可审核编辑层」
 * ------------------------------------------------------------
 * 这里放的是需要人工判断、会随时间变化、需要定期复核的内容：
 *   - cn:      各平台对「中国卖家」的入口可达性（入驻/后台是否开放）
 *   - regions: 各地区的「主流平台总数 / 已收录 / 未收录原因」（下一步填充）
 *   - global:  全球总览（主流平台共多少 / 类型 / 分布 / 未收录原因）（下一步填充）
 *
 * 审核约定（重要）：
 *   - 每条都带 status 和 reviewed。
 *       status:"draft"    = 由助手起草、尚【待核实】（UI 上会标注）
 *       status:"verified" = 你已人工确认；确认时把 status 改成 verified 并更新 reviewed 日期
 *   - 历史留痕：本文件纳入 git，每次审核改动 commit 一次即为历史记录。
 *   - 缺省即「对中国开放」：cn 里没有列出的平台，默认入驻/后台都对中国卖家开放。
 *
 * cn 条目字段：
 *   closed: 数组，列出【未对中国卖家开放】的入口角色，取值 "signup"(入驻) / "admin"(后台)
 *   note:   悬停时补充说明（为什么不开放 / 门槛）
 * ============================================================ */
window.MARKET_META = {
  reviewedAt: "2026-06-16",
  source: "助手起草，截至 2026-01 知识；均为 draft，待你核实。平台政策变动频繁，以官方为准。",

  // 按平台名（需与 GLOBAL_STORES 里的 name 完全一致）键入。缺省=对中国开放。
  cn: {
    "Target Plus":        { closed: ["signup", "admin"], note: "邀请制，仅面向美国本土品牌/有美国实体", status: "draft", reviewed: "2026-06-16" },
    "Otto":               { closed: ["signup", "admin"], note: "Otto Market 以欧盟卖家为主，需德国/欧盟实体（待核）", status: "draft", reviewed: "2026-06-16" },
    "Bol":                { closed: ["signup", "admin"], note: "比荷卢市场，需欧盟实体与本地账户", status: "draft", reviewed: "2026-06-16" },
    "Notonthehighstreet": { closed: ["signup", "admin"], note: "仅面向英国本土创作者/品牌", status: "draft", reviewed: "2026-06-16" },
    "Rakuten":            { closed: ["signup", "admin"], note: "乐天日本以日本法人为主，跨境支持有限", status: "draft", reviewed: "2026-06-16" },
    "ZOZOTOWN":           { closed: ["signup", "admin"], note: "日本时尚寄售，需日本法人", status: "draft", reviewed: "2026-06-16" },
    "Naver Smart Store":  { closed: ["signup", "admin"], note: "需韩国营业执照与本地结算", status: "draft", reviewed: "2026-06-16" },
    "Tiki":               { closed: ["signup", "admin"], note: "越南本土平台，需越南实体", status: "draft", reviewed: "2026-06-16" },
    "Sendo":              { closed: ["signup", "admin"], note: "越南本土平台，需越南实体", status: "draft", reviewed: "2026-06-16" },
    "Magazine Luiza":     { closed: ["signup", "admin"], note: "巴西本土零售，需当地 CNPJ", status: "draft", reviewed: "2026-06-16" },
    "Amazon India":       { closed: ["signup"], note: "在 .in 销售需印度本地实体/GST", status: "draft", reviewed: "2026-06-16" },
    "Flipkart":           { closed: ["signup", "admin"], note: "印度 FDI 限制，需本地实体", status: "draft", reviewed: "2026-06-16" },
    "Meesho":             { closed: ["signup", "admin"], note: "印度供应商需 GST 等本地资质", status: "draft", reviewed: "2026-06-16" },
    "Myntra":             { closed: ["signup", "admin"], note: "印度时尚平台，需本地实体", status: "draft", reviewed: "2026-06-16" },
    "Yandex Market":      { closed: ["signup", "admin"], note: "俄罗斯本土，跨境通道有限（Ozon/Wildberries 更适合跨境）", status: "draft", reviewed: "2026-06-16" }
  },

  // 各地区汇总：universe=该区主流平台估数（待核）；omitted=未收录的取舍原因。
  // 已收录数 = 该区实际平台卡数，由代码自动统计，不写在这里。键名须与地图区域名一致。
  regions: {
    "北美":            { universe: 12, omitted: "邀请制(如 Target+)与纯本土小平台未全收", status: "draft", reviewed: "2026-06-16" },
    "欧洲":            { universe: 22, omitted: "各国本地小平台众多，仅收主力与可跨境者", status: "draft", reviewed: "2026-06-16" },
    "英国":            { universe: 8,  omitted: "本土手作/小众平台从略", status: "draft", reviewed: "2026-06-16" },
    "东南亚":          { universe: 10, omitted: "各国本土小平台从略", status: "draft", reviewed: "2026-06-16" },
    "日本 / 韩国":     { universe: 12, omitted: "需本地法人的平台仅列出、不深收", status: "draft", reviewed: "2026-06-16" },
    "拉美":            { universe: 10, omitted: "本地小平台与需当地实体者从略", status: "draft", reviewed: "2026-06-16" },
    "中东":            { universe: 8,  omitted: "本地垂直小平台从略", status: "draft", reviewed: "2026-06-16" },
    "南亚 / 印度":     { universe: 8,  omitted: "印度 FDI 限制，多数需本地实体", status: "draft", reviewed: "2026-06-16" },
    "澳新":            { universe: 6,  omitted: "市场较小，仅收主力综合平台", status: "draft", reviewed: "2026-06-16" },
    "非洲":            { universe: 6,  omitted: "市场早期、平台更替快，仅收稳定主力", status: "draft", reviewed: "2026-06-16" },
    "俄罗斯 / 独联体": { universe: 6,  omitted: "受合规/汇兑影响，仅收主力跨境平台", status: "draft", reviewed: "2026-06-16" }
  },

  // 全球总览：universe=全球主流跨境电商平台估数（待核）；collected 由代码自动统计。
  global: {
    universe: 60,
    types: "综合平台 · 内容电商 · 独立站 · 垂直零售 · 全托管/新势力 · B2B 批发",
    distribution: "北美、欧洲、英国最成熟；东南亚、拉美增长快；日韩、中东重本地化；南亚、俄独联、非洲为新兴或政策市场",
    omitted: "已衰退、纯本地小平台、需当地实体且无跨境通道的暂未全收；优先收录中国卖家可触达的主流平台",
    status: "draft", reviewed: "2026-06-16"
  }
};
