import json

# ============================================================
# Sub-category definitions
# ============================================================
brand_subs = {
    "brand-identity": "品牌标识",
    "design-thinking": "设计思维",
    "typography": "字体排版",
    "logo-packaging": "标志包装",
    "visual-inspo": "视觉灵感",
    "brand-strategy": "品牌空间策略",
}

platform_subs = {
    "amazon": "Amazon",
    "shopify": "Shopify",
    "tiktok": "TikTok Shop",
    "meta": "Meta / Instagram",
    "google": "Google",
    "shopee": "Shopee / Lazada",
    "other": "其他平台",
}

compliance_subs = {
    "us": "美国",
    "eu": "欧盟",
    "uk": "英国",
    "intl": "国际 / WTO",
    "general": "综合",
}

supply_subs = {
    "ocean": "海运",
    "air": "空运",
    "warehouse": "仓储与履约",
    "index": "运价指数",
    "risk": "风险与合规",
    "general": "综合",
}

media_subs = {
    "cn": "国内媒体",
    "intl": "海外媒体",
}

# ============================================================
# All sources: (id, name, url, desc, tier, category, [sub_category])
# ============================================================
all_sources = [
    # ======================== 平台政策 ========================
    # -- Amazon --
    ("amz-spapi-changelog", "Amazon SP-API Changelog", "https://developer-docs.amazon.com/sp-api/changelog",
     "Amazon 卖家 API 变更日志——直接影响工具开发与自动化运营。", "S", "platform", "amazon"),
    ("seller-central-news", "Amazon Seller Central 公告", "https://sellercentral.amazon.com/help/hub/reference/G200271940",
     "Amazon 卖家中心官方公告：费率变更、FBA 政策、新功能发布。", "S", "platform", "amazon"),
    ("aws-ml-blog", "AWS 机器学习博客", "https://aws.amazon.com/blogs/machine-learning",
     "Amazon AI/ML 产品动态——与 Amazon 广告算法和推荐系统紧密相关。", "A", "platform", "amazon"),

    # -- Shopify --
    ("shopify-changelog", "Shopify Developer Changelog", "https://shopify.dev/changelog",
     "Shopify 平台 API 与开发者功能变更，第一时间知道平台规则调整。", "S", "platform", "shopify"),
    ("shopify-changelog-merchant", "Shopify 商家更新日志", "https://changelog.shopify.com",
     "面向商家的 Shopify 功能更新、费率调整、新工具发布。", "A", "platform", "shopify"),
    ("shopify-retail-blog", "Shopify Retail Blog", "https://www.shopify.com/blog",
     "Shopify 官方博客：电商趋势、卖家案例、营销策略——商家视角一手信息。", "B", "platform", "shopify"),

    # -- TikTok --
    ("tiktokshop-dev", "TikTok Shop Developer", "https://partner.tiktokshop.com/doc",
     "TikTok Shop 开放平台文档与 API 变更，东南亚/欧美站点政策。", "S", "platform", "tiktok"),
    ("tiktok-creative-center", "TikTok Creative Center", "https://ads.tiktok.com/business/creativecenter",
     "TikTok 热门广告素材库——哪些产品/创意正在被大规模投放。", "S", "platform", "tiktok"),
    ("tiktok-business-blog", "TikTok for Business Blog", "https://www.tiktok.com/business/blog",
     "TikTok 商业博客：广告产品更新、电商功能、Shop 政策。", "A", "platform", "tiktok"),

    # -- Meta / Instagram --
    ("meta-graph-changelog", "Meta Graph API Changelog", "https://developers.facebook.com/docs/graph-api/changelog",
     "Facebook/Instagram 图谱 API 变更，影响广告投放与数据获取。", "A", "platform", "meta"),
    ("meta-research", "Meta Research Blog", "https://about.fb.com/news",
     "Meta 官方博客：广告产品、商业工具、AI 功能更新。", "A", "platform", "meta"),
    ("instagram-business", "Instagram Business Blog", "https://business.instagram.com/blog",
     "Instagram 商业功能更新：Shopping、Reels 电商、创作者变现。", "B", "platform", "meta"),

    # -- Google --
    ("google-ads-commerce", "Google Ads & Commerce Blog", "https://blog.google/products/ads-commerce",
     "Google 广告与电商产品官方博客：Shopping/Merchant Center 变动。", "B", "platform", "google"),
    ("google-shopping", "Google Shopping Blog", "https://blog.google/products/shopping",
     "Google Shopping 产品更新与最佳实践——免费与付费列表政策。", "B", "platform", "google"),
    ("google-merchant-blog", "Google Merchant Center 帮助", "https://support.google.com/merchants",
     "Google Merchant Center 政策中心：产品数据规范、 disapprovals 原因。", "A", "platform", "google"),

    # -- Shopee / Lazada --
    ("shopee-open", "Shopee Open Platform", "https://open.shopee.com",
     "Shopee 开放平台公告，东南亚与拉美市场卖家必读。", "A", "platform", "shopee"),
    ("lazada-open", "Lazada Open Platform", "https://open.lazada.com",
     "Lazada 开放平台文档——东南亚六国市场 API 与政策更新。", "A", "platform", "shopee"),
    ("shopee-seller-edu", "Shopee 卖家学习中心", "https://seller.shopee.sg/edu",
     "Shopee 卖家教育中心：政策解读、运营指南、新功能培训。", "B", "platform", "shopee"),

    # -- 其他平台 --
    ("walmart-marketplace", "Walmart Marketplace 公告", "https://marketplace.walmart.com",
     "Walmart 电商平台卖家公告：入驻政策、费率、API 更新。", "A", "platform", "other"),
    ("ebay-announcements", "eBay 卖家公告", "https://www.ebay.com/sellercenter",
     "eBay 卖家中心公告板：品类政策、运费调整、国际销售规则。", "B", "platform", "other"),
    ("mercado-libre-dev", "Mercado Libre Developer", "https://developers.mercadolibre.com",
     "美客多开发者平台——拉美最大电商的 API 与政策更新。", "A", "platform", "other"),
    ("temu-seller-center", "Temu 卖家中心", "https://seller.kuajingmaihuo.com",
     "Temu 跨境卖家后台——拼多多海外版的政策与规则变动。", "A", "platform", "other"),
    ("practical-ecom", "Practical Ecommerce", "https://www.practicalecommerce.com",
     "电商实操指南：多平台运营、SEO、转化优化——实战型内容。", "B", "platform", "other"),
    ("ecommerce-fuel", "Ecommerce Fuel", "https://www.ecommercefuel.com",
     "面向成熟电商卖家的高阶社区与内容，7 位数卖家圈子。", "B", "platform", "other"),
    ("ecommercebytes", "EcommerceBytes", "https://www.ecommercebytes.com",
     "电商行业新闻与卖家社区，覆盖 Amazon/eBay/Etsy/Walmart 多平台。", "B", "platform", "other"),
    ("mp-pulse", "Marketplace Pulse", "https://www.marketplacepulse.com",
     "Amazon/Walmart/eBay 第三方卖家数据与平台趋势深度分析。", "A", "platform", "other"),
    ("baijing", "白鲸出海", "https://www.baijing.cn",
     "中文出海圈活跃资讯社区——泛娱乐与工具类出海应用动态。", "B", "platform", "other"),

    # ======================== 合规与法规 ========================
    # -- 美国 --
    ("us-federal-register", "US Federal Register", "https://www.federalregister.gov",
     "美国联邦公报原文：de minimis、Section 301、关税与贸易政策。", "S", "compliance", "us"),
    ("cpsc-recalls", "US CPSC 产品召回", "https://www.cpsc.gov/Newsroom",
     "美国消费品安全委员会——产品召回通知，直接影响在售品类。", "S", "compliance", "us"),
    ("ustr-press", "USTR 美国贸易代表", "https://ustr.gov",
     "美国贸易代表办公室：301 关税、贸易协定、知识产权保护。", "S", "compliance", "us"),
    ("us-cbp", "US CBP 贸易公告", "https://www.cbp.gov/rss/trade",
     "美国海关边境保护局：清关政策、执法动态、Section 321。", "A", "compliance", "us"),
    ("fda-imports", "FDA 进口警报", "https://www.fda.gov/industry/import-alerts",
     "FDA 进口警报列表——食品、药品、化妆品品类的合规红线。", "S", "compliance", "us"),
    ("epa-chemicals", "EPA 化学品与农药", "https://www.epa.gov/pesticides",
     "美国环保署化学品与农药法规——影响家居、清洁、个护品类。", "A", "compliance", "us"),

    # -- 欧盟 --
    ("eu-eurlex", "EU EUR-Lex 法规数据库", "https://eur-lex.europa.eu",
     "欧盟法律数据库原文：GPSR、EPR、数字产品护照等核心法规。", "S", "compliance", "eu"),
    ("ec-press", "EU 委员会新闻室", "https://ec.europa.eu/commission/presscorner",
     "欧盟委员会官方：数字服务法、产品安全法规、贸易政策。", "A", "compliance", "eu"),
    ("echa-reach", "ECHA / REACH 化学品", "https://echa.europa.eu",
     "欧盟化学品管理局——REACH 法规与 SVHC 清单更新。", "S", "compliance", "eu"),
    ("eu-market-surveillance", "EU Safety Gate (RAPEX)", "https://ec.europa.eu/safety-gate",
     "欧盟非食品产品安全快速预警系统——危险产品通报。", "A", "compliance", "eu"),

    # -- 英国 --
    ("uk-hmrc", "UK HMRC 税务海关", "https://www.gov.uk/government/organisations/hm-revenue-customs",
     "英国税务海关总署：VAT 政策、海关程序、跨境电商税务。", "A", "compliance", "uk"),
    ("uk-opss", "UK OPSS 产品安全", "https://www.gov.uk/government/organisations/office-for-product-safety-and-standards",
     "英国产品安全与标准办公室——GPSR 英国版执行机构。", "A", "compliance", "uk"),

    # -- 国际 / WTO --
    ("wto-eping", "WTO TBT 通知 ePing", "https://epingalert.org",
     "WTO 技术性贸易壁垒通报——各国产品标准变更预警。", "S", "compliance", "intl"),
    ("wto-trade-monitor", "WTO Trade Monitoring", "https://www.wto.org/english/news_e/archive_e/trdev_arc_e.htm",
     "WTO 贸易政策监控——各国关税与非关税措施变动汇总。", "A", "compliance", "intl"),
    ("unctad-trade", "UNCTAD 贸易与物流", "https://unctad.org/topic/transport-and-trade-logistics",
     "联合国贸发会议贸易物流——海运连通性、贸易便利化指数。", "B", "compliance", "intl"),

    # -- 综合 --
    ("scb-reg-compliance", "SupplyChainBrain 法规合规", "https://www.supplychainbrain.com",
     "全球供应链法规追踪：强迫劳动、碳边境、供应链尽职调查。", "S", "compliance", "general"),
    ("scb-supply-risk", "SupplyChainBrain 供应链风险", "https://www.supplychainbrain.com",
     "供应链安全与风险专题：制裁、地缘政治、全球断链。", "A", "compliance", "general"),

    # ======================== 供应链与物流 ========================
    # -- 海运 --
    ("freightwaves", "FreightWaves", "https://www.freightwaves.com",
     "全球货运与供应链媒体——海运运价、运力与航线分析。", "A", "supply", "ocean"),
    ("seatrade-maritime", "Seatrade Maritime", "https://www.seatrade-maritime.com",
     "海事航运权威——船公司动态、新船交付、航线调整。", "A", "supply", "ocean"),
    ("scb-ocean", "SupplyChainBrain 海运", "https://www.supplychainbrain.com",
     "全球海运专题：航运联盟、港口拥堵与费率趋势。", "A", "supply", "ocean"),
    ("loadstar", "The Loadstar", "https://theloadstar.com",
     "全球货运深度报道——集装箱航运、船公司、港口。", "B", "supply", "ocean"),
    ("hellenic-shipping", "Hellenic Shipping News", "https://www.hellenicshippingnews.com",
     "全球航运新闻：散货、油轮、集装箱全品类覆盖。", "B", "supply", "ocean"),
    ("splash247", "Splash247 海运", "https://splash247.com",
     "海运快讯：船公司并购、造船订单、地缘政治影响。", "B", "supply", "ocean"),

    # -- 空运 --
    ("air-cargo-news", "Air Cargo News", "https://www.aircargonews.net",
     "全球空运新闻——跨境电商包裹运力、费率与航司动态。", "A", "supply", "air"),
    ("stat-times", "STAT Times 空运物流", "https://www.stattimes.com",
     "航空货运与物流媒体——Fleet、运力、机场枢纽动态。", "B", "supply", "air"),

    # -- 仓储与履约 --
    ("shipbob-blog", "ShipBob Blog", "https://www.shipbob.com/blog",
     "电商履约实操：3PL 选择、库存布局、退货管理——卖家视角。", "B", "supply", "warehouse"),
    ("dc-velocity", "DC Velocity", "https://www.dcvelocity.com",
     "配送中心与物流运营——仓库管理、自动化、劳动力趋势。", "B", "supply", "warehouse"),
    ("supply-chain-quarterly", "Supply Chain Quarterly", "https://www.supplychainquarterly.com",
     "供应链管理季刊——战略层面深度分析，学术与行业结合。", "A", "supply", "warehouse"),

    # -- 运价指数 --
    ("freightos-fbx", "Freightos FBX 运价指数", "https://fbx.freightos.com",
     "全球集装箱运价指数——中国至欧美主要航线实时运价。", "A", "supply", "index"),
    ("drewry-wci", "Drewry WCI 运价指数", "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index",
     "Drewry 世界集装箱运价指数——海运即期运费的行业基准。", "A", "supply", "index"),
    ("xeneta", "Xeneta 运价情报", "https://www.xeneta.com",
     "海运空运运价基准平台——基于真实货主合同的数据情报。", "A", "supply", "index"),

    # -- 风险与合规 --
    ("scb-global-trade", "SupplyChainBrain 全球贸易", "https://www.supplychainbrain.com",
     "全球贸易经济专题——协定、关税变动、制造业产业转移。", "A", "supply", "risk"),
    ("supply-chain-dive", "Supply Chain Dive", "https://www.supplychaindive.com",
     "供应链深度报道——物流科技、仓储自动化、风险与韧性。", "A", "supply", "risk"),

    # -- 综合 --
    ("supplychain247", "SupplyChain 24/7", "https://www.supplychain247.com",
     "供应链行业新闻聚合——物流、运输、仓储、技术全覆盖。", "B", "supply", "general"),
    ("trade-ready", "Trade Ready 国际贸易", "https://www.tradeready.ca",
     "国际贸易实务：出口流程、融资、市场准入操作指南。", "B", "supply", "general"),

    # ======================== 需求与用户 ========================
    ("voc-reddit", "Reddit 用户原声", "https://www.reddit.com",
     "AmazonSeller/FBA/ecommerce 等子版块——卖家与消费者真实反馈。", "A", "demand"),
    ("voc-amz-reviews", "亚马逊差评聚类", "https://www.amazon.com",
     "通过差评聚类识别品类痛点——反向推断产品改进与新品机会。", "A", "demand"),
    ("voc-amz-movers", "Amazon Movers & Shakers", "https://www.amazon.com/gp/movers-and-shakers",
     "Amazon 24 小时内销量飙升榜——品类动量的直接需求信号。", "B", "demand"),
    ("pinterest-trends", "Pinterest Trends", "https://www.pinterest.com/trends",
     "Pinterest 搜索趋势——提前 6-12 个月的消费需求预测。", "B", "demand"),
    ("google-trends", "Google Trends", "https://trends.google.com/trends",
     "Google 搜索趋势——实时了解全球消费者在搜什么品类/品牌。", "A", "demand"),
    ("signal-linkedin-hiring", "LinkedIn 竞品招聘信号", "https://www.linkedin.com",
     "通过岗位变动追踪竞品扩张方向——组织级领先信号。", "B", "demand"),
    ("exploding-topics", "Exploding Topics", "https://explodingtopics.com",
     "AI 追踪快速增长的话题与品类——月度趋势数据集。", "A", "demand"),
    ("glossy-trends", "Glossy 消费趋势", "https://www.glossy.co",
     "时尚与美妆领域消费者行为分析——DTC 品牌创新风向。", "A", "demand"),

    # ======================== 市场与趋势 ========================
    ("thingtesting", "Thingtesting", "https://thingtesting.com",
     "DTC 品牌评测平台——新品牌发现与真实用户评测。", "A", "market"),
    ("trendhunter-main", "Trend Hunter", "https://www.trendhunter.com",
     "全球消费趋势情报——新品、新品类、新消费行为信号。", "B", "market"),
    ("similarweb-blog", "Similarweb Blog", "https://www.similarweb.com/blog",
     "网站流量与数字市场情报——品类市场份额与竞争格局。", "A", "market"),
    ("statista-dossier", "Statista 行业档案", "https://www.statista.com",
     "横跨消费品类别的统计数据库——市场规模与预测。", "A", "market"),

    # ======================== 行业媒体 ========================
    # -- 国内 --
    ("kr-asia", "氪出海", "https://36kr.com",
     "36氪出海频道——中国公司全球化最新动态与深度报道。", "A", "media", "cn"),
    ("cifnews", "雨果跨境", "https://www.cifnews.com",
     "跨境电商行业门户——平台政策解读、卖家故事、选品指南。", "B", "media", "cn"),
    ("ebrun", "亿邦动力", "https://www.ebrun.com",
     "电商产业信息服务商——品牌数字化、零售创新、跨境电商。", "B", "media", "cn"),
    ("baijing-app", "白鲸出海", "https://www.baijing.cn",
     "中文出海圈活跃社区——应用出海与跨境电商最新资讯。", "B", "media", "cn"),
    ("luxe-co", "华丽志", "https://www.luxe.co",
     "奢侈品与时尚商业媒体——品牌并购、零售创新、消费升级。", "B", "media", "cn"),
    ("36kr-news", "36氪", "https://36kr.com",
     "中国创投与科技商业媒体——消费、出海、AI 赛道全覆盖。", "B", "media", "cn"),
    ("equal-ocean", "EqualOcean 亿欧", "https://equalocean.com",
     "中国品牌全球化智库——出海研究、全球市场分析、行业报告。", "A", "media", "cn"),

    # -- 海外 --
    ("modern-retail", "Modern Retail", "https://www.modernretail.co",
     "现代零售媒体——DTC 品牌、全渠道零售、电商战略深度分析。", "A", "media", "intl"),
    ("digital-commerce-360", "Digital Commerce 360", "https://www.digitalcommerce360.com",
     "数字商业数据与报道——Top 500/1000 电商排名与品类分析。", "A", "media", "intl"),
    ("retail-dive", "Retail Dive", "https://www.retaildive.com",
     "零售行业深度新闻——门店关张、全渠道策略、零售科技。", "A", "media", "intl"),
    ("digiday", "Digiday", "https://digiday.com",
     "数字营销与媒体——广告技术、电商营销、品牌数字化转型。", "A", "media", "intl"),
    ("marketing-dive", "Marketing Dive", "https://www.marketingdive.com",
     "营销行业深度——品牌策略、广告趋势、CMO 洞察。", "A", "media", "intl"),
    ("ecommerce-news-europe", "Ecommerce News Europe", "https://ecommercenews.eu",
     "欧洲电商新闻——各国市场动态、支付物流、法规统一。", "A", "media", "intl"),
    ("channelx", "ChannelX", "https://channelx.world",
     "全球电商市场报道——Amazon/Marketplace/TikTok Shop 全覆盖。", "A", "media", "intl"),
    ("2pm", "2PM", "https://2pml.com",
     "DTC 品牌与电商策略深度简报——每篇都是行业洞察浓缩。", "B", "media", "intl"),
    ("adweek", "Adweek", "https://www.adweek.com",
     "广告与品牌营销权威媒体——创意案例、代理商与品牌策略。", "B", "media", "intl"),
    ("retail-times", "Retail Times", "https://retailtimes.co.uk",
     "英国零售行业新闻——线下零售、电商、品牌动态。", "C", "media", "intl"),
    ("youtube-blog", "YouTube 官方博客", "https://blog.youtube",
     "YouTube 产品生态更新——短视频、直播电商、创作者变现。", "B", "media", "intl"),
    ("retail-gazette-uk", "Retail Gazette UK", "https://www.retailgazette.co.uk",
     "英国零售商业媒体——百货、超市、连锁与电商竞争格局。", "C", "media", "intl"),
    ("ecommerce-germany", "Ecommerce Germany News", "https://ecommercegermany.com",
     "德国电商新闻——欧洲最大电商市场的政策、平台与品牌动态。", "B", "media", "intl"),
    ("business-of-fashion-news", "Business of Fashion 新闻", "https://www.businessoffashion.com",
     "时尚产业权威媒体——品牌战略、零售创新、消费趋势分析。", "A", "media", "intl"),

    # ======================== 品牌与视觉 ========================
    # -- 品牌标识 --
    ("underconsideration", "Under Consideration", "https://www.underconsideration.com",
     "Brand New 母站——全球最权威的品牌标识评论与行业趋势。", "A", "brand", "brand-identity"),
    ("brandnew", "Brand New", "https://www.underconsideration.com/brandnew",
     "品牌标识评审标杆——新 logo 发布后的第一手专业点评。", "A", "brand", "brand-identity"),
    ("bpando", "BP&O", "https://bpando.org",
     "品牌标识与包装深度案例——每篇都是完整的品牌项目复盘。", "A", "brand", "brand-identity"),
    ("identity-designed", "Identity Designed", "https://identitydesigned.com",
     "品牌标识案例深度分析——从概念到落地的完整记录。", "A", "brand", "brand-identity"),
    ("brandingmag", "Branding Mag", "https://www.brandingmag.com",
     "品牌策略与案例分析——定位、命名、视觉系统综合性媒体。", "B", "brand", "brand-identity"),
    # -- 设计思维 --
    ("aiga-eye-on-design", "AIGA Eye on Design", "https://eyeondesign.aiga.org",
     "AIGA 出品设计媒体——设计思维、行业趋势、新兴设计师访谈。", "A", "brand", "design-thinking"),
    ("itsnicethat", "It's Nice That", "https://www.itsnicethat.com",
     "创意产业标杆——品牌、平面设计、数字艺术、插画全覆盖。", "A", "brand", "design-thinking"),
    ("creative-boom", "Creative Boom", "https://www.creativeboom.com",
     "创意产业动态与设计师访谈——关注独立设计师与中小工作室。", "B", "brand", "design-thinking"),
    ("creative-review", "Creative Review", "https://www.creativereview.co.uk",
     "英国老牌创意杂志——品牌、广告、设计行业评论与趋势。", "C", "brand", "design-thinking"),
    # -- 字体排版 --
    ("typewolf", "Typewolf", "https://www.typewolf.com",
     "字体趋势与品牌字体推荐——每天一个真实网站字体拆解。", "A", "brand", "typography"),
    ("fontsinuse", "Fonts In Use", "https://fontsinuse.com",
     "字体使用案例宝库——按行业、品牌、字体分类检索。", "A", "brand", "typography"),
    # -- 标志包装 --
    ("logodesignlove", "Logo Design Love", "https://www.logodesignlove.com",
     "标志设计经典博客——从标志到品牌视觉系统的实战分析。", "B", "brand", "logo-packaging"),
    ("dieline", "The Dieline", "https://thedieline.com",
     "全球包装设计权威——消费品包装策略、材料创新、品牌趋势。", "B", "brand", "logo-packaging"),
    ("packaging-of-world", "Packaging of the World", "https://www.packagingoftheworld.com",
     "全球包装设计案例聚合——按国家、品类浏览，创意面极广。", "C", "brand", "logo-packaging"),
    # -- 视觉灵感 --
    ("awwwards", "Awwwards", "https://www.awwwards.com",
     "全球网页设计奖项——每天评选最佳网站，视觉趋势风向标。", "B", "brand", "visual-inspo"),
    ("swiss-miss", "Swiss Miss", "https://www.swiss-miss.com",
     "Tina Roth Eisenberg 个人策展博客——设计灵感精选，品味独特。", "B", "brand", "visual-inspo"),
    ("mindsparkle", "Mindsparkle Mag", "https://mindsparklemag.com",
     "高质量品牌与网页设计案例——精选全球工作室优秀作品。", "B", "brand", "visual-inspo"),
    ("siteinspire", "SiteInspire", "https://www.siteinspire.com",
     "网页设计灵感库——按风格、行业筛选，收录最精致网站设计。", "B", "brand", "visual-inspo"),
    ("creative-bloq", "Creative Bloq", "https://www.creativebloq.com",
     "设计综合媒体——3D、图形、网页、品牌，教程趋势并重。", "B", "brand", "visual-inspo"),
    ("dribbble", "Dribbble", "https://dribbble.com",
     "全球设计师社区——UI、品牌、插画、动效作品首选发布平台。", "B", "brand", "visual-inspo"),
    ("designboom", "Designboom", "https://www.designboom.com",
     "综合设计媒体——建筑、产品、艺术、品牌的全球性资讯平台。", "C", "brand", "visual-inspo"),
    # -- 品牌空间策略 --
    ("dezeen", "Dezeen", "https://www.dezeen.com",
     "全球最具影响力设计媒体——建筑、室内、品牌空间。跨境开店前必看。", "A", "brand", "brand-strategy"),
    ("robin-report", "The Robin Report", "https://www.therobinreport.com",
     "零售品牌战略深度分析——DTC、百货、电商的模式与策略。", "A", "brand", "brand-strategy"),
    ("bof", "Business of Fashion", "https://www.businessoffashion.com",
     "时尚产业权威——品牌战略、零售创新、消费趋势必读。", "A", "brand", "brand-strategy"),
    ("footwear-news", "Footwear News", "https://footwearnews.com",
     "鞋履与运动品牌——新品发布、品牌合作、零售趋势。", "B", "brand", "brand-strategy"),
    ("producthunt", "Product Hunt", "https://www.producthunt.com",
     "每日新产品发现——科技产品、设计工具、AI 应用创新窗口。", "A", "brand", "brand-strategy"),

    # ======================== 资本与创投 ========================
    ("hacker-news", "Hacker News", "https://news.ycombinator.com",
     "Y Combinator 旗下科技社区——创业者与投资人日常讨论。", "B", "capital"),
    ("indie-hackers", "Indie Hackers", "https://www.indiehackers.com",
     "独立开发者与微型 SaaS 创业社区——收入透明、经验分享。", "A", "capital"),
    ("techcrunch", "TechCrunch", "https://techcrunch.com",
     "科技与创投媒体——消费品牌融资、DTC 并购、电商赛道风投。", "A", "capital"),
    ("pitchbook-news", "PitchBook News", "https://pitchbook.com/news",
     "私募与风投数据——并购交易、IPO 窗口、行业估值趋势。", "A", "capital"),

    # ======================== 众筹与新品 ========================
    ("crowd-kickstarter", "Kickstarter", "https://www.kickstarter.com/discover",
     "全球最大众筹平台——消费电子与设计品类先行信号，提前 6-18 个月。", "A", "crowdfunding"),
    ("crowd-indiegogo", "Indiegogo", "https://www.indiegogo.com/explore",
     "众筹平台——亚洲品牌出海首选测试渠道，创新产品早期发现。", "B", "crowdfunding"),
    ("backerkit", "BackerKit", "https://www.backerkit.com",
     "众筹后市场管理平台——热门众筹项目延伸信号。", "B", "crowdfunding"),

    # ======================== 支付与金融 ========================
    ("stripe-blog", "Stripe Blog", "https://stripe.com/blog",
     "Stripe 官方博客——全球支付基础设施、金融科技趋势。", "A", "payment"),
    ("checkout-blog", "Checkout.com Blog", "https://www.checkout.com/blog",
     "Checkout.com 博客——跨境支付优化、多币种结算策略。", "A", "payment"),
    ("finextra", "Finextra", "https://www.finextra.com",
     "金融科技媒体——支付、银行、监管科技的全球动态。", "A", "payment"),
    ("paypal-newsroom", "PayPal Newsroom", "https://newsroom.paypal-corp.com",
     "PayPal 官方新闻——支付产品更新、跨境结算功能。", "A", "payment"),
    ("pymnts", "PYMNTS", "https://www.pymnts.com",
     "支付与商业媒体——B2B 支付、跨境汇款、嵌入式金融。", "B", "payment"),
    ("payments-journal", "Payments Journal", "https://www.paymentsjournal.com",
     "支付行业媒体——信用卡、ACH、实时支付、数字货币。", "B", "payment"),
    ("payments-dive", "Payments Dive", "https://www.paymentsdive.com",
     "支付行业深度——先买后付、开放银行、支付合规。", "B", "payment"),

    # ======================== AI 品牌工具 ========================
    ("midjourney", "Midjourney", "https://www.midjourney.com",
     "AI 图像生成——品牌视觉探索、概念稿、产品渲染的首选工具。", "A", "ai_tools"),
    ("dall-e", "DALL·E", "https://openai.com/index/dall-e-3",
     "OpenAI 图像生成——与 ChatGPT 深度集成的视觉创意工具。", "A", "ai_tools"),
    ("runway", "Runway", "https://runwayml.com",
     "AI 视频生成与编辑——品牌视频素材、产品演示、动态视觉生产。", "A", "ai_tools"),
    ("comfyui", "ComfyUI", "https://github.com/comfyanonymous/ComfyUI",
     "节点式 AI 图像工作流——Stable Diffusion 最灵活的生产界面。", "A", "ai_tools"),
    ("adobe-firefly", "Adobe Firefly", "https://www.adobe.com/products/firefly.html",
     "Adobe 生成式 AI——与 Photoshop/Illustrator 集成的品牌视觉生产工具。", "A", "ai_tools"),
    ("canva-ai", "Canva AI", "https://www.canva.com/ai-image-generator",
     "Canva AI 设计——品牌模板 + AI 生成，非设计师的快捷品牌工具。", "B", "ai_tools"),
    ("figma-ai", "Figma AI", "https://www.figma.com/ai",
     "Figma AI 功能——UI 与品牌设计的 AI 辅助：自动布局、内容填充。", "A", "ai_tools"),
    ("stable-diffusion", "Stable Diffusion WebUI", "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
     "开源 AI 图像生成——本地部署，品牌素材全流程自主可控。", "A", "ai_tools"),
    ("kaiber", "Kaiber", "https://kaiber.ai",
     "AI 视频与动画——品牌故事视频、动态视觉素材生成。", "B", "ai_tools"),
    ("looka", "Looka", "https://looka.com",
     "AI Logo 与品牌套件生成——快速品牌视觉方案原型。", "B", "ai_tools"),
    ("brandmark", "Brandmark", "https://brandmark.io",
     "AI 品牌标识生成——输入关键词，自动生成品牌视觉方案。", "B", "ai_tools"),
    ("galileo-ai", "Galileo AI", "https://www.usegalileo.ai",
     "AI UI 设计——从文本描述生成完整界面设计稿。", "A", "ai_tools"),
    ("sora-openai", "Sora", "https://openai.com/sora",
     "OpenAI 视频生成——文生视频与图生视频，品牌广告素材新范式。", "A", "ai_tools"),
    ("pika-labs", "Pika", "https://pika.art",
     "AI 视频生成——短平快的视频素材生产工具。", "B", "ai_tools"),
    ("suno-music", "Suno", "https://suno.com",
     "AI 音乐生成——品牌视频配乐与播客背景音乐。", "B", "ai_tools"),
    ("udio", "Udio", "https://www.udio.com",
     "AI 音乐生成——品牌声音标识与广告配乐创作工具。", "B", "ai_tools"),
    ("elevenlabs", "ElevenLabs", "https://elevenlabs.io",
     "AI 语音合成——品牌播客、广告旁白、多语言配音。", "A", "ai_tools"),
    ("replit-ai", "Replit AI", "https://replit.com/ai",
     "AI 编程环境——品牌网站与电商工具快速原型开发。", "B", "ai_tools"),
    ("cursor-ai", "Cursor", "https://cursor.com",
     "AI 编程编辑器——品牌技术部署与自动化脚本的首选开发环境。", "A", "ai_tools"),

    # ======================== AI与开发 ========================
    ("google-ai-blog", "Google AI Blog", "https://blog.google/technology/ai",
     "Google AI 研究与应用——Gemini、AI Agent、多模态。", "A", "ai_dev"),
    ("google-dev-blog", "Google AI Developers Blog", "https://developers.googleblog.com",
     "Google 开发者博客——AI 工具链、API 更新、最佳实践。", "A", "ai_dev"),
    ("openai-news", "OpenAI News", "https://openai.com/news",
     "OpenAI 官方新闻——GPT 系列模型、API、产品发布。", "S", "ai_dev"),
    ("anthropic-release-notes", "Anthropic API Release Notes", "https://docs.anthropic.com/en/release-notes/api",
     "Anthropic Claude 系列模型 API 变更与功能更新。", "S", "ai_dev"),
    ("nvidia-dev-blog", "NVIDIA 开发者博客", "https://developer.nvidia.com/blog",
     "NVIDIA 开发者博客——GPU、CUDA、AI 推理部署。", "B", "ai_dev"),
]

# ============================================================
# Build structured data
# ============================================================
cat_order = ["platform", "compliance", "supply", "demand", "market", "media", "capital", "crowdfunding", "payment", "brand", "ai_tools", "ai_dev"]
cat_meta = {
    "platform": ("平台政策", "按平台分类的规则、API 与费率变动"),
    "compliance": ("合规与法规", "按管辖区的关税、产品安全与贸易政策"),
    "supply": ("供应链与物流", "海运、空运、仓储、运价指数与供应链风险"),
    "demand": ("需求与用户", "用户原声、搜索趋势、消费需求信号"),
    "market": ("市场与趋势", "行业数据、消费趋势、竞争格局"),
    "media": ("行业媒体", "国内与海外跨境资讯渠道"),
    "brand": ("品牌与视觉", "品牌策略、标识设计、包装、视觉灵感"),
    "capital": ("资本与创投", "融资、并购、出海赛道资本动态"),
    "crowdfunding": ("众筹与新品", "Kickstarter、Indiegogo 等先行信号"),
    "payment": ("支付与金融", "跨境支付、金融科技、汇率"),
    "ai_tools": ("AI 品牌工具", "AI 视觉、视频、语音、音乐与品牌设计工具"),
    "ai_dev": ("AI 开发动态", "AI 模型发布、API 变更、开发者生态"),
}

cat_subs = {
    "platform": platform_subs,
    "compliance": compliance_subs,
    "supply": supply_subs,
    "media": media_subs,
    "brand": brand_subs,
}

data = {}
for cat in cat_order:
    data[cat] = {
        "name": cat_meta[cat][0],
        "desc": cat_meta[cat][1],
        "sources": [],
        "subs": None,
    }
    if cat in cat_subs:
        data[cat]["subs"] = {}
        for sk, sv in cat_subs[cat].items():
            data[cat]["subs"][sk] = {"name": sv, "sources": []}

for s in all_sources:
    sid, name, url, desc, tier, cat = s[0], s[1], s[2], s[3], s[4], s[5]
    entry = {"id": sid, "name": name, "url": url, "desc": desc, "tier": tier}
    if len(s) > 6:
        sub = s[6]
        if data[cat]["subs"] and sub in data[cat]["subs"]:
            data[cat]["subs"][sub]["sources"].append(entry)
        else:
            data[cat]["sources"].append(entry)
    else:
        data[cat]["sources"].append(entry)

# Remove empty subs
for cat in cat_order:
    if data[cat]["subs"]:
        data[cat]["subs"] = {k: v for k, v in data[cat]["subs"].items() if v["sources"]}

# Count
def cat_count(info):
    n = len(info["sources"])
    if info["subs"]:
        n += sum(len(v["sources"]) for v in info["subs"].values())
    return n

total = sum(cat_count(data[cat]) for cat in cat_order)
print(f"Total: {total} sources\n")
for cat in cat_order:
    info = data[cat]
    n = cat_count(info)
    s = ""
    if info["subs"]:
        s = " [" + ", ".join(f"{k}({len(v['sources'])})" for k, v in info["subs"].items()) + "]"
    print(f"  {info['name']:16s}: {n:3d}{s}")

with open("nav_data.json", "w", encoding="utf-8") as f:
    json.dump({"total": total, "categories": data, "cat_order": cat_order, "brand_subs": brand_subs}, f, ensure_ascii=False, indent=2)
print(f"\nWritten nav_data.json ({total} sources, {len(cat_order)} categories)")

# Auto-build links.js for atlas.sequentry.com JS-rendered page
import subprocess, sys
subprocess.run([sys.executable, "build_links_js.py"], check=True)
