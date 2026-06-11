// 渠道导航数据 —— 信息架构 v2：按任务模块组织；AI 作为能力层分布到对应模块。
// tier: S 必看 / A 常看 / B 长尾（只影响每类内排序，优质靠前）。
window.NAV_DATA = {
  "updated": "2026-06-11",
  "categories": [
    {
      "id": "platform-channel",
      "group": "research",
      "name": "平台与渠道",
      "desc": "平台规则、API、卖家政策与渠道生态",
      "subs": [
        {
          "id": "amazon",
          "name": "Amazon"
        },
        {
          "id": "shopify",
          "name": "Shopify"
        },
        {
          "id": "tiktok",
          "name": "TikTok Shop"
        },
        {
          "id": "meta",
          "name": "Meta / Instagram"
        },
        {
          "id": "google",
          "name": "Google / Merchant"
        },
        {
          "id": "emerging",
          "name": "新兴市场平台"
        },
        {
          "id": "community",
          "name": "平台实操社区"
        }
      ]
    },
    {
      "id": "market-product",
      "group": "research",
      "name": "市场与选品",
      "desc": "需求信号、消费趋势、品类机会与选品工具",
      "subs": [
        {
          "id": "trend",
          "name": "消费趋势"
        },
        {
          "id": "demand",
          "name": "需求信号"
        },
        {
          "id": "tools",
          "name": "选品工具"
        },
        {
          "id": "data",
          "name": "市场数据"
        },
        {
          "id": "new-products",
          "name": "新品发现"
        }
      ]
    },
    {
      "id": "growth-ads",
      "group": "research",
      "name": "增长与广告",
      "desc": "广告情报、创意库、营销媒体与转化工具",
      "subs": [
        {
          "id": "ad-library",
          "name": "广告库"
        },
        {
          "id": "creative-intel",
          "name": "创意情报"
        },
        {
          "id": "marketing-media",
          "name": "营销媒体"
        },
        {
          "id": "content-conversion",
          "name": "内容与转化"
        }
      ]
    },
    {
      "id": "brand-retail",
      "group": "research",
      "name": "品牌与零售策略",
      "desc": "DTC 品牌、零售策略、定位、资本与新品信号",
      "subs": [
        {
          "id": "dtc-retail",
          "name": "DTC / 零售案例"
        },
        {
          "id": "strategy",
          "name": "定位与品牌理论"
        },
        {
          "id": "capital",
          "name": "资本与并购"
        },
        {
          "id": "brand-space",
          "name": "品牌空间"
        }
      ]
    },
    {
      "id": "visual-production",
      "group": "production",
      "name": "视觉与内容生产",
      "desc": "品牌标识、包装、UI、字体配色、素材与 AI 内容生产",
      "subs": [
        {
          "id": "identity",
          "name": "品牌标识"
        },
        {
          "id": "web-ui",
          "name": "Web / UI 灵感"
        },
        {
          "id": "design-media",
          "name": "设计媒体"
        },
        {
          "id": "type-color",
          "name": "字体与配色"
        },
        {
          "id": "packaging",
          "name": "包装与平面"
        },
        {
          "id": "assets",
          "name": "素材与样机"
        },
        {
          "id": "ai-image",
          "name": "AI 图像"
        },
        {
          "id": "ai-video-audio",
          "name": "AI 视频 / 声音"
        },
        {
          "id": "ai-design",
          "name": "AI 设计 / 建站"
        }
      ]
    },
    {
      "id": "tech-automation",
      "group": "production",
      "name": "技术与自动化",
      "desc": "AI 模型、API、编程原型、自动化与内部工具链",
      "subs": [
        {
          "id": "ai-models",
          "name": "AI 模型与 API"
        },
        {
          "id": "coding",
          "name": "编程与原型"
        },
        {
          "id": "automation",
          "name": "自动化工作流"
        }
      ]
    },
    {
      "id": "compliance-fulfillment",
      "group": "ops",
      "name": "合规与履约",
      "desc": "法规、关税、产品安全、物流、仓储、支付与金融基础设施",
      "subs": [
        {
          "id": "us",
          "name": "美国法规"
        },
        {
          "id": "eu",
          "name": "欧盟法规"
        },
        {
          "id": "uk",
          "name": "英国法规"
        },
        {
          "id": "intl",
          "name": "国际 / WTO"
        },
        {
          "id": "logistics",
          "name": "物流与运价"
        },
        {
          "id": "warehouse",
          "name": "仓储与履约"
        },
        {
          "id": "freight-index",
          "name": "运价指数"
        },
        {
          "id": "payment",
          "name": "支付与金融"
        },
        {
          "id": "general",
          "name": "综合风险"
        }
      ]
    },
    {
      "id": "media-intel",
      "group": "source",
      "name": "媒体与情报源",
      "desc": "中文、英文、行业、报告与 Newsletter 型长期信源",
      "subs": [
        {
          "id": "media-cn",
          "name": "中文出海媒体"
        },
        {
          "id": "media-intl",
          "name": "英文零售媒体"
        },
        {
          "id": "reports",
          "name": "报告 / Newsletter"
        }
      ]
    }
  ],
  "links": [
    {
      "cat": "platform-channel",
      "sub": "amazon",
      "tier": "B",
      "name": "Amazon SP-API Changelog",
      "url": "https://developer-docs.amazon.com/sp-api/changelog",
      "domain": "developer-docs.amazon.com",
      "desc": "Amazon 卖家 API 变更日志——直接影响工具开发与自动化运营。"
    },
    {
      "cat": "platform-channel",
      "sub": "amazon",
      "tier": "B",
      "name": "Amazon Seller Central 公告",
      "url": "https://sellercentral.amazon.com/help/hub/reference/G200271940",
      "domain": "sellercentral.amazon.com",
      "desc": "Amazon 卖家中心官方公告：费率变更、FBA 政策、新功能发布。"
    },
    {
      "cat": "platform-channel",
      "sub": "amazon",
      "tier": "B",
      "name": "AWS 机器学习博客",
      "url": "https://aws.amazon.com/blogs/machine-learning",
      "domain": "aws.amazon.com",
      "desc": "Amazon AI/ML 产品动态——与 Amazon 广告算法和推荐系统紧密相关。"
    },
    {
      "cat": "platform-channel",
      "sub": "shopify",
      "tier": "A",
      "name": "Shopify Developer Changelog",
      "url": "https://shopify.dev/changelog",
      "domain": "shopify.dev",
      "desc": "Shopify 平台 API 与开发者功能变更，第一时间知道平台规则调整。"
    },
    {
      "cat": "platform-channel",
      "sub": "shopify",
      "tier": "A",
      "name": "Shopify 商家更新日志",
      "url": "https://changelog.shopify.com",
      "domain": "changelog.shopify.com",
      "desc": "面向商家的 Shopify 功能更新、费率调整、新工具发布。"
    },
    {
      "cat": "platform-channel",
      "sub": "shopify",
      "tier": "A",
      "name": "Shopify Retail Blog",
      "url": "https://www.shopify.com/blog",
      "domain": "www.shopify.com",
      "desc": "Shopify 官方博客：电商趋势、卖家案例、营销策略——商家视角一手信息。"
    },
    {
      "cat": "platform-channel",
      "sub": "tiktok",
      "tier": "B",
      "name": "TikTok Shop Developer",
      "url": "https://partner.tiktokshop.com/doc",
      "domain": "partner.tiktokshop.com",
      "desc": "TikTok Shop 开放平台文档与 API 变更，东南亚/欧美站点政策。"
    },
    {
      "cat": "growth-ads",
      "sub": "ad-library",
      "tier": "A",
      "name": "TikTok Creative Center",
      "url": "https://ads.tiktok.com/business/creativecenter",
      "domain": "ads.tiktok.com",
      "desc": "TikTok 热门广告素材库——哪些产品/创意正在被大规模投放。"
    },
    {
      "cat": "platform-channel",
      "sub": "tiktok",
      "tier": "B",
      "name": "TikTok for Business Blog",
      "url": "https://www.tiktok.com/business/blog",
      "domain": "www.tiktok.com",
      "desc": "TikTok 商业博客：广告产品更新、电商功能、Shop 政策。"
    },
    {
      "cat": "platform-channel",
      "sub": "meta",
      "tier": "B",
      "name": "Meta Graph API Changelog",
      "url": "https://developers.facebook.com/docs/graph-api/changelog",
      "domain": "developers.facebook.com",
      "desc": "Facebook/Instagram 图谱 API 变更，影响广告投放与数据获取。"
    },
    {
      "cat": "platform-channel",
      "sub": "meta",
      "tier": "B",
      "name": "Meta Research Blog",
      "url": "https://about.fb.com/news",
      "domain": "about.fb.com",
      "desc": "Meta 官方博客：广告产品、商业工具、AI 功能更新。"
    },
    {
      "cat": "platform-channel",
      "sub": "meta",
      "tier": "B",
      "name": "Instagram Business Blog",
      "url": "https://business.instagram.com/blog",
      "domain": "business.instagram.com",
      "desc": "Instagram 商业功能更新：Shopping、Reels 电商、创作者变现。"
    },
    {
      "cat": "platform-channel",
      "sub": "google",
      "tier": "A",
      "name": "Google Ads & Commerce Blog",
      "url": "https://blog.google/products/ads-commerce",
      "domain": "blog.google",
      "desc": "Google 广告与电商产品官方博客：Shopping/Merchant Center 变动。"
    },
    {
      "cat": "platform-channel",
      "sub": "google",
      "tier": "B",
      "name": "Google Shopping Blog",
      "url": "https://blog.google/products/shopping",
      "domain": "blog.google",
      "desc": "Google Shopping 产品更新与最佳实践——免费与付费列表政策。"
    },
    {
      "cat": "platform-channel",
      "sub": "google",
      "tier": "B",
      "name": "Google Merchant Center 帮助",
      "url": "https://support.google.com/merchants",
      "domain": "support.google.com",
      "desc": "Google Merchant Center 政策中心：产品数据规范、 disapprovals 原因。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Shopee Open Platform",
      "url": "https://open.shopee.com",
      "domain": "open.shopee.com",
      "desc": "Shopee 开放平台公告，东南亚与拉美市场卖家必读。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Lazada Open Platform",
      "url": "https://open.lazada.com",
      "domain": "open.lazada.com",
      "desc": "Lazada 开放平台文档——东南亚六国市场 API 与政策更新。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Shopee 卖家学习中心",
      "url": "https://seller.shopee.sg/edu",
      "domain": "seller.shopee.sg",
      "desc": "Shopee 卖家教育中心：政策解读、运营指南、新功能培训。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Walmart Marketplace 公告",
      "url": "https://marketplace.walmart.com",
      "domain": "marketplace.walmart.com",
      "desc": "Walmart 电商平台卖家公告：入驻政策、费率、API 更新。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "eBay 卖家公告",
      "url": "https://www.ebay.com/sellercenter",
      "domain": "www.ebay.com",
      "desc": "eBay 卖家中心公告板：品类政策、运费调整、国际销售规则。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Mercado Libre Developer",
      "url": "https://developers.mercadolibre.com",
      "domain": "developers.mercadolibre.com",
      "desc": "美客多开发者平台——拉美最大电商的 API 与政策更新。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "Temu 卖家中心",
      "url": "https://seller.kuajingmaihuo.com",
      "domain": "seller.kuajingmaihuo.com",
      "desc": "Temu 跨境卖家后台——拼多多海外版的政策与规则变动。"
    },
    {
      "cat": "platform-channel",
      "sub": "community",
      "tier": "A",
      "name": "Practical Ecommerce",
      "url": "https://www.practicalecommerce.com",
      "domain": "www.practicalecommerce.com",
      "desc": "电商实操指南：多平台运营、SEO、转化优化——实战型内容。"
    },
    {
      "cat": "platform-channel",
      "sub": "community",
      "tier": "B",
      "name": "Ecommerce Fuel",
      "url": "https://www.ecommercefuel.com",
      "domain": "www.ecommercefuel.com",
      "desc": "面向成熟电商卖家的高阶社区与内容，7 位数卖家圈子。"
    },
    {
      "cat": "platform-channel",
      "sub": "community",
      "tier": "B",
      "name": "EcommerceBytes",
      "url": "https://www.ecommercebytes.com",
      "domain": "www.ecommercebytes.com",
      "desc": "电商行业新闻与卖家社区，覆盖 Amazon/eBay/Etsy/Walmart 多平台。"
    },
    {
      "cat": "platform-channel",
      "sub": "community",
      "tier": "S",
      "name": "Marketplace Pulse",
      "url": "https://www.marketplacepulse.com",
      "domain": "www.marketplacepulse.com",
      "desc": "Amazon/Walmart/eBay 第三方卖家数据与平台趋势深度分析。"
    },
    {
      "cat": "media-intel",
      "sub": "media-cn",
      "tier": "B",
      "name": "白鲸出海",
      "url": "https://www.baijing.cn",
      "domain": "www.baijing.cn",
      "desc": "中文出海圈活跃资讯社区——泛娱乐与工具类出海应用动态。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "S",
      "name": "US Federal Register",
      "url": "https://www.federalregister.gov",
      "domain": "www.federalregister.gov",
      "desc": "美国联邦公报原文：de minimis、Section 301、关税与贸易政策。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "A",
      "name": "US CPSC 产品召回",
      "url": "https://www.cpsc.gov/Newsroom",
      "domain": "www.cpsc.gov",
      "desc": "美国消费品安全委员会——产品召回通知，直接影响在售品类。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "A",
      "name": "USTR 美国贸易代表",
      "url": "https://ustr.gov",
      "domain": "ustr.gov",
      "desc": "美国贸易代表办公室：301 关税、贸易协定、知识产权保护。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "A",
      "name": "US CBP 贸易公告",
      "url": "https://www.cbp.gov/rss/trade",
      "domain": "www.cbp.gov",
      "desc": "美国海关边境保护局：清关政策、执法动态、Section 321。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "A",
      "name": "FDA 进口警报",
      "url": "https://www.fda.gov/industry/import-alerts",
      "domain": "www.fda.gov",
      "desc": "FDA 进口警报列表——食品、药品、化妆品品类的合规红线。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "B",
      "name": "EPA 化学品与农药",
      "url": "https://www.epa.gov/pesticides",
      "domain": "www.epa.gov",
      "desc": "美国环保署化学品与农药法规——影响家居、清洁、个护品类。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "eu",
      "tier": "A",
      "name": "EU EUR-Lex 法规数据库",
      "url": "https://eur-lex.europa.eu",
      "domain": "eur-lex.europa.eu",
      "desc": "欧盟法律数据库原文：GPSR、EPR、数字产品护照等核心法规。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "eu",
      "tier": "A",
      "name": "EU 委员会新闻室",
      "url": "https://ec.europa.eu/commission/presscorner",
      "domain": "ec.europa.eu",
      "desc": "欧盟委员会官方：数字服务法、产品安全法规、贸易政策。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "eu",
      "tier": "B",
      "name": "ECHA / REACH 化学品",
      "url": "https://echa.europa.eu",
      "domain": "echa.europa.eu",
      "desc": "欧盟化学品管理局——REACH 法规与 SVHC 清单更新。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "eu",
      "tier": "B",
      "name": "EU Safety Gate (RAPEX)",
      "url": "https://ec.europa.eu/safety-gate",
      "domain": "ec.europa.eu",
      "desc": "欧盟非食品产品安全快速预警系统——危险产品通报。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "uk",
      "tier": "A",
      "name": "UK HMRC 税务海关",
      "url": "https://www.gov.uk/government/organisations/hm-revenue-customs",
      "domain": "www.gov.uk",
      "desc": "英国税务海关总署：VAT 政策、海关程序、跨境电商税务。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "uk",
      "tier": "B",
      "name": "UK OPSS 产品安全",
      "url": "https://www.gov.uk/government/organisations/office-for-product-safety-and-standards",
      "domain": "www.gov.uk",
      "desc": "英国产品安全与标准办公室——GPSR 英国版执行机构。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "intl",
      "tier": "B",
      "name": "WTO TBT 通知 ePing",
      "url": "https://epingalert.org",
      "domain": "epingalert.org",
      "desc": "WTO 技术性贸易壁垒通报——各国产品标准变更预警。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "intl",
      "tier": "B",
      "name": "WTO Trade Monitoring",
      "url": "https://www.wto.org/english/news_e/archive_e/trdev_arc_e.htm",
      "domain": "www.wto.org",
      "desc": "WTO 贸易政策监控——各国关税与非关税措施变动汇总。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "intl",
      "tier": "B",
      "name": "UNCTAD 贸易与物流",
      "url": "https://unctad.org/topic/transport-and-trade-logistics",
      "domain": "unctad.org",
      "desc": "联合国贸发会议贸易物流——海运连通性、贸易便利化指数。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "intl",
      "tier": "B",
      "name": "SupplyChainBrain 法规合规",
      "url": "https://www.supplychainbrain.com",
      "domain": "www.supplychainbrain.com",
      "desc": "全球供应链法规追踪：强迫劳动、碳边境、供应链尽职调查。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "general",
      "tier": "A",
      "name": "SupplyChainBrain 供应链风险",
      "url": "https://www.supplychainbrain.com",
      "domain": "www.supplychainbrain.com",
      "desc": "供应链安全与风险专题：制裁、地缘政治、全球断链。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "A",
      "name": "FreightWaves",
      "url": "https://www.freightwaves.com",
      "domain": "www.freightwaves.com",
      "desc": "全球货运与供应链媒体——海运运价、运力与航线分析。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "Seatrade Maritime",
      "url": "https://www.seatrade-maritime.com",
      "domain": "www.seatrade-maritime.com",
      "desc": "海事航运权威——船公司动态、新船交付、航线调整。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "SupplyChainBrain 海运",
      "url": "https://www.supplychainbrain.com",
      "domain": "www.supplychainbrain.com",
      "desc": "全球海运专题：航运联盟、港口拥堵与费率趋势。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "A",
      "name": "The Loadstar",
      "url": "https://theloadstar.com",
      "domain": "theloadstar.com",
      "desc": "全球货运深度报道——集装箱航运、船公司、港口。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "Hellenic Shipping News",
      "url": "https://www.hellenicshippingnews.com",
      "domain": "www.hellenicshippingnews.com",
      "desc": "全球航运新闻：散货、油轮、集装箱全品类覆盖。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "Splash247 海运",
      "url": "https://splash247.com",
      "domain": "splash247.com",
      "desc": "海运快讯：船公司并购、造船订单、地缘政治影响。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "Air Cargo News",
      "url": "https://www.aircargonews.net",
      "domain": "www.aircargonews.net",
      "desc": "全球空运新闻——跨境电商包裹运力、费率与航司动态。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "STAT Times 空运物流",
      "url": "https://www.stattimes.com",
      "domain": "www.stattimes.com",
      "desc": "航空货运与物流媒体——Fleet、运力、机场枢纽动态。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "warehouse",
      "tier": "A",
      "name": "ShipBob Blog",
      "url": "https://www.shipbob.com/blog",
      "domain": "www.shipbob.com",
      "desc": "电商履约实操：3PL 选择、库存布局、退货管理——卖家视角。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "warehouse",
      "tier": "B",
      "name": "DC Velocity",
      "url": "https://www.dcvelocity.com",
      "domain": "www.dcvelocity.com",
      "desc": "配送中心与物流运营——仓库管理、自动化、劳动力趋势。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "warehouse",
      "tier": "B",
      "name": "Supply Chain Quarterly",
      "url": "https://www.supplychainquarterly.com",
      "domain": "www.supplychainquarterly.com",
      "desc": "供应链管理季刊——战略层面深度分析，学术与行业结合。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "freight-index",
      "tier": "A",
      "name": "Freightos FBX 运价指数",
      "url": "https://fbx.freightos.com",
      "domain": "fbx.freightos.com",
      "desc": "全球集装箱运价指数——中国至欧美主要航线实时运价。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "freight-index",
      "tier": "B",
      "name": "Drewry WCI 运价指数",
      "url": "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index",
      "domain": "www.drewry.co.uk",
      "desc": "Drewry 世界集装箱运价指数——海运即期运费的行业基准。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "freight-index",
      "tier": "B",
      "name": "Xeneta 运价情报",
      "url": "https://www.xeneta.com",
      "domain": "www.xeneta.com",
      "desc": "海运空运运价基准平台——基于真实货主合同的数据情报。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "general",
      "tier": "A",
      "name": "SupplyChainBrain 全球贸易",
      "url": "https://www.supplychainbrain.com",
      "domain": "www.supplychainbrain.com",
      "desc": "全球贸易经济专题——协定、关税变动、制造业产业转移。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "A",
      "name": "Supply Chain Dive",
      "url": "https://www.supplychaindive.com",
      "domain": "www.supplychaindive.com",
      "desc": "供应链深度报道——物流科技、仓储自动化、风险与韧性。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "SupplyChain 24/7",
      "url": "https://www.supplychain247.com",
      "domain": "www.supplychain247.com",
      "desc": "供应链行业新闻聚合——物流、运输、仓储、技术全覆盖。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "logistics",
      "tier": "B",
      "name": "Trade Ready 国际贸易",
      "url": "https://www.tradeready.ca",
      "domain": "www.tradeready.ca",
      "desc": "国际贸易实务：出口流程、融资、市场准入操作指南。"
    },
    {
      "cat": "market-product",
      "sub": "demand",
      "tier": "A",
      "name": "Reddit 用户原声",
      "url": "https://www.reddit.com",
      "domain": "www.reddit.com",
      "desc": "AmazonSeller/FBA/ecommerce 等子版块——卖家与消费者真实反馈。"
    },
    {
      "cat": "market-product",
      "sub": "demand",
      "tier": "B",
      "name": "亚马逊差评聚类",
      "url": "https://www.amazon.com",
      "domain": "www.amazon.com",
      "desc": "通过差评聚类识别品类痛点——反向推断产品改进与新品机会。"
    },
    {
      "cat": "market-product",
      "sub": "demand",
      "tier": "A",
      "name": "Amazon Movers & Shakers",
      "url": "https://www.amazon.com/gp/movers-and-shakers",
      "domain": "www.amazon.com",
      "desc": "Amazon 24 小时内销量飙升榜——品类动量的直接需求信号。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "A",
      "name": "Pinterest Trends",
      "url": "https://www.pinterest.com/trends",
      "domain": "www.pinterest.com",
      "desc": "Pinterest 搜索趋势——提前 6-12 个月的消费需求预测。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "S",
      "name": "Google Trends",
      "url": "https://trends.google.com/trends",
      "domain": "trends.google.com",
      "desc": "Google 搜索趋势——实时了解全球消费者在搜什么品类/品牌。"
    },
    {
      "cat": "market-product",
      "sub": "demand",
      "tier": "B",
      "name": "LinkedIn 竞品招聘信号",
      "url": "https://www.linkedin.com",
      "domain": "www.linkedin.com",
      "desc": "通过岗位变动追踪竞品扩张方向——组织级领先信号。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "A",
      "name": "Exploding Topics",
      "url": "https://explodingtopics.com",
      "domain": "explodingtopics.com",
      "desc": "AI 追踪快速增长的话题与品类——月度趋势数据集。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "B",
      "name": "Glossy 消费趋势",
      "url": "https://www.glossy.co",
      "domain": "www.glossy.co",
      "desc": "时尚与美妆领域消费者行为分析——DTC 品牌创新风向。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "S",
      "name": "Thingtesting",
      "url": "https://thingtesting.com",
      "domain": "thingtesting.com",
      "desc": "DTC 品牌评测平台——新品牌发现与真实用户评测。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "B",
      "name": "Trend Hunter",
      "url": "https://www.trendhunter.com",
      "domain": "www.trendhunter.com",
      "desc": "全球消费趋势情报——新品、新品类、新消费行为信号。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Similarweb Blog",
      "url": "https://www.similarweb.com/blog",
      "domain": "www.similarweb.com",
      "desc": "网站流量与数字市场情报——品类市场份额与竞争格局。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Statista 行业档案",
      "url": "https://www.statista.com",
      "domain": "www.statista.com",
      "desc": "横跨消费品类别的统计数据库——市场规模与预测。"
    },
    {
      "cat": "media-intel",
      "sub": "media-cn",
      "tier": "A",
      "name": "氪出海",
      "url": "https://36kr.com",
      "domain": "36kr.com",
      "desc": "36氪出海频道——中国公司全球化最新动态与深度报道。"
    },
    {
      "cat": "media-intel",
      "sub": "media-cn",
      "tier": "A",
      "name": "雨果跨境",
      "url": "https://www.cifnews.com",
      "domain": "www.cifnews.com",
      "desc": "跨境电商行业门户——平台政策解读、卖家故事、选品指南。"
    },
    {
      "cat": "media-intel",
      "sub": "media-cn",
      "tier": "A",
      "name": "亿邦动力",
      "url": "https://www.ebrun.com",
      "domain": "www.ebrun.com",
      "desc": "电商产业信息服务商——品牌数字化、零售创新、跨境电商。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "华丽志",
      "url": "https://www.luxe.co",
      "domain": "www.luxe.co",
      "desc": "奢侈品与时尚商业媒体——品牌并购、零售创新、消费升级。"
    },
    {
      "cat": "media-intel",
      "sub": "media-cn",
      "tier": "B",
      "name": "36氪",
      "url": "https://36kr.com",
      "domain": "36kr.com",
      "desc": "中国创投与科技商业媒体——消费、出海、AI 赛道全覆盖。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "EqualOcean 亿欧",
      "url": "https://equalocean.com",
      "domain": "equalocean.com",
      "desc": "中国品牌全球化智库——出海研究、全球市场分析、行业报告。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "S",
      "name": "Modern Retail",
      "url": "https://www.modernretail.co",
      "domain": "www.modernretail.co",
      "desc": "现代零售媒体——DTC 品牌、全渠道零售、电商战略深度分析。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "Digital Commerce 360",
      "url": "https://www.digitalcommerce360.com",
      "domain": "www.digitalcommerce360.com",
      "desc": "数字商业数据与报道——Top 500/1000 电商排名与品类分析。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "Retail Dive",
      "url": "https://www.retaildive.com",
      "domain": "www.retaildive.com",
      "desc": "零售行业深度新闻——门店关张、全渠道策略、零售科技。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "Digiday",
      "url": "https://digiday.com",
      "domain": "digiday.com",
      "desc": "数字营销与媒体——广告技术、电商营销、品牌数字化转型。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "Marketing Dive",
      "url": "https://www.marketingdive.com",
      "domain": "www.marketingdive.com",
      "desc": "营销行业深度——品牌策略、广告趋势、CMO 洞察。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "B",
      "name": "Ecommerce News Europe",
      "url": "https://ecommercenews.eu",
      "domain": "ecommercenews.eu",
      "desc": "欧洲电商新闻——各国市场动态、支付物流、法规统一。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "A",
      "name": "ChannelX",
      "url": "https://channelx.world",
      "domain": "channelx.world",
      "desc": "全球电商市场报道——Amazon/Marketplace/TikTok Shop 全覆盖。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "S",
      "name": "2PM",
      "url": "https://2pml.com",
      "domain": "2pml.com",
      "desc": "DTC 品牌与电商策略深度简报——每篇都是行业洞察浓缩。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "Adweek",
      "url": "https://www.adweek.com",
      "domain": "www.adweek.com",
      "desc": "广告与品牌营销权威媒体——创意案例、代理商与品牌策略。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "B",
      "name": "Retail Times",
      "url": "https://retailtimes.co.uk",
      "domain": "retailtimes.co.uk",
      "desc": "英国零售行业新闻——线下零售、电商、品牌动态。"
    },
    {
      "cat": "platform-channel",
      "sub": "emerging",
      "tier": "B",
      "name": "YouTube 官方博客",
      "url": "https://blog.youtube",
      "domain": "blog.youtube",
      "desc": "YouTube 产品生态更新——短视频、直播电商、创作者变现。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "B",
      "name": "Retail Gazette UK",
      "url": "https://www.retailgazette.co.uk",
      "domain": "www.retailgazette.co.uk",
      "desc": "英国零售商业媒体——百货、超市、连锁与电商竞争格局。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "B",
      "name": "Ecommerce Germany News",
      "url": "https://ecommercegermany.com",
      "domain": "ecommercegermany.com",
      "desc": "德国电商新闻——欧洲最大电商市场的政策、平台与品牌动态。"
    },
    {
      "cat": "media-intel",
      "sub": "media-intl",
      "tier": "A",
      "name": "Business of Fashion 新闻",
      "url": "https://www.businessoffashion.com",
      "domain": "www.businessoffashion.com",
      "desc": "时尚产业权威媒体——品牌战略、零售创新、消费趋势分析。"
    },
    {
      "cat": "brand-retail",
      "sub": "capital",
      "tier": "B",
      "name": "Hacker News",
      "url": "https://news.ycombinator.com",
      "domain": "news.ycombinator.com",
      "desc": "Y Combinator 旗下科技社区——创业者与投资人日常讨论。"
    },
    {
      "cat": "brand-retail",
      "sub": "capital",
      "tier": "B",
      "name": "Indie Hackers",
      "url": "https://www.indiehackers.com",
      "domain": "www.indiehackers.com",
      "desc": "独立开发者与微型 SaaS 创业社区——收入透明、经验分享。"
    },
    {
      "cat": "brand-retail",
      "sub": "capital",
      "tier": "A",
      "name": "TechCrunch",
      "url": "https://techcrunch.com",
      "domain": "techcrunch.com",
      "desc": "科技与创投媒体——消费品牌融资、DTC 并购、电商赛道风投。"
    },
    {
      "cat": "brand-retail",
      "sub": "capital",
      "tier": "B",
      "name": "PitchBook News",
      "url": "https://pitchbook.com/news",
      "domain": "pitchbook.com",
      "desc": "私募与风投数据——并购交易、IPO 窗口、行业估值趋势。"
    },
    {
      "cat": "market-product",
      "sub": "new-products",
      "tier": "A",
      "name": "Kickstarter",
      "url": "https://www.kickstarter.com/discover",
      "domain": "www.kickstarter.com",
      "desc": "全球最大众筹平台——消费电子与设计品类先行信号，提前 6-18 个月。"
    },
    {
      "cat": "market-product",
      "sub": "new-products",
      "tier": "A",
      "name": "Indiegogo",
      "url": "https://www.indiegogo.com/explore",
      "domain": "www.indiegogo.com",
      "desc": "众筹平台——亚洲品牌出海首选测试渠道，创新产品早期发现。"
    },
    {
      "cat": "market-product",
      "sub": "new-products",
      "tier": "B",
      "name": "BackerKit",
      "url": "https://www.backerkit.com",
      "domain": "www.backerkit.com",
      "desc": "众筹后市场管理平台——热门众筹项目延伸信号。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "A",
      "name": "Stripe Blog",
      "url": "https://stripe.com/blog",
      "domain": "stripe.com",
      "desc": "Stripe 官方博客——全球支付基础设施、金融科技趋势。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "B",
      "name": "Checkout.com Blog",
      "url": "https://www.checkout.com/blog",
      "domain": "www.checkout.com",
      "desc": "Checkout.com 博客——跨境支付优化、多币种结算策略。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "B",
      "name": "Finextra",
      "url": "https://www.finextra.com",
      "domain": "www.finextra.com",
      "desc": "金融科技媒体——支付、银行、监管科技的全球动态。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "B",
      "name": "PayPal Newsroom",
      "url": "https://newsroom.paypal-corp.com",
      "domain": "newsroom.paypal-corp.com",
      "desc": "PayPal 官方新闻——支付产品更新、跨境结算功能。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "B",
      "name": "PYMNTS",
      "url": "https://www.pymnts.com",
      "domain": "www.pymnts.com",
      "desc": "支付与商业媒体——B2B 支付、跨境汇款、嵌入式金融。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "B",
      "name": "Payments Journal",
      "url": "https://www.paymentsjournal.com",
      "domain": "www.paymentsjournal.com",
      "desc": "支付行业媒体——信用卡、ACH、实时支付、数字货币。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "payment",
      "tier": "A",
      "name": "Payments Dive",
      "url": "https://www.paymentsdive.com",
      "domain": "www.paymentsdive.com",
      "desc": "支付行业深度——先买后付、开放银行、支付合规。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "A",
      "name": "Under Consideration",
      "url": "https://www.underconsideration.com",
      "domain": "www.underconsideration.com",
      "desc": "Brand New 母站——全球最权威的品牌标识评论与行业趋势。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "S",
      "name": "Brand New",
      "url": "https://www.underconsideration.com/brandnew",
      "domain": "www.underconsideration.com",
      "desc": "品牌标识评审标杆——新 logo 发布后的第一手专业点评。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "A",
      "name": "BP&O",
      "url": "https://bpando.org",
      "domain": "bpando.org",
      "desc": "品牌标识与包装深度案例——每篇都是完整的品牌项目复盘。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "A",
      "name": "Identity Designed",
      "url": "https://identitydesigned.com",
      "domain": "identitydesigned.com",
      "desc": "品牌标识案例深度分析——从概念到落地的完整记录。"
    },
    {
      "cat": "brand-retail",
      "sub": "strategy",
      "tier": "B",
      "name": "Branding Mag",
      "url": "https://www.brandingmag.com",
      "domain": "www.brandingmag.com",
      "desc": "品牌策略与案例分析——定位、命名、视觉系统综合性媒体。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "A",
      "name": "AIGA Eye on Design",
      "url": "https://eyeondesign.aiga.org",
      "domain": "eyeondesign.aiga.org",
      "desc": "AIGA 出品设计媒体——设计思维、行业趋势、新兴设计师访谈。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "A",
      "name": "It's Nice That",
      "url": "https://www.itsnicethat.com",
      "domain": "www.itsnicethat.com",
      "desc": "创意产业标杆——品牌、平面设计、数字艺术、插画全覆盖。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "B",
      "name": "Creative Boom",
      "url": "https://www.creativeboom.com",
      "domain": "www.creativeboom.com",
      "desc": "创意产业动态与设计师访谈——关注独立设计师与中小工作室。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "B",
      "name": "Creative Review",
      "url": "https://www.creativereview.co.uk",
      "domain": "www.creativereview.co.uk",
      "desc": "英国老牌创意杂志——品牌、广告、设计行业评论与趋势。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "A",
      "name": "Typewolf",
      "url": "https://www.typewolf.com",
      "domain": "www.typewolf.com",
      "desc": "字体趋势与品牌字体推荐——每天一个真实网站字体拆解。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "A",
      "name": "Fonts In Use",
      "url": "https://fontsinuse.com",
      "domain": "fontsinuse.com",
      "desc": "字体使用案例宝库——按行业、品牌、字体分类检索。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "B",
      "name": "Logo Design Love",
      "url": "https://www.logodesignlove.com",
      "domain": "www.logodesignlove.com",
      "desc": "标志设计经典博客——从标志到品牌视觉系统的实战分析。"
    },
    {
      "cat": "visual-production",
      "sub": "packaging",
      "tier": "S",
      "name": "The Dieline",
      "url": "https://thedieline.com",
      "domain": "thedieline.com",
      "desc": "全球包装设计权威——消费品包装策略、材料创新、品牌趋势。"
    },
    {
      "cat": "visual-production",
      "sub": "packaging",
      "tier": "A",
      "name": "Packaging of the World",
      "url": "https://www.packagingoftheworld.com",
      "domain": "www.packagingoftheworld.com",
      "desc": "全球包装设计案例聚合——按国家、品类浏览，创意面极广。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "S",
      "name": "Awwwards",
      "url": "https://www.awwwards.com",
      "domain": "www.awwwards.com",
      "desc": "全球网页设计奖项——每天评选最佳网站，视觉趋势风向标。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "Swiss Miss",
      "url": "https://www.swiss-miss.com",
      "domain": "www.swiss-miss.com",
      "desc": "Tina Roth Eisenberg 个人策展博客——设计灵感精选，品味独特。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "Mindsparkle Mag",
      "url": "https://mindsparklemag.com",
      "domain": "mindsparklemag.com",
      "desc": "高质量品牌与网页设计案例——精选全球工作室优秀作品。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "SiteInspire",
      "url": "https://www.siteinspire.com",
      "domain": "www.siteinspire.com",
      "desc": "网页设计灵感库——按风格、行业筛选，收录最精致网站设计。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "B",
      "name": "Creative Bloq",
      "url": "https://www.creativebloq.com",
      "domain": "www.creativebloq.com",
      "desc": "设计综合媒体——3D、图形、网页、品牌，教程趋势并重。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Dribbble",
      "url": "https://dribbble.com",
      "domain": "dribbble.com",
      "desc": "全球设计师社区——UI、品牌、插画、动效作品首选发布平台。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "B",
      "name": "Designboom",
      "url": "https://www.designboom.com",
      "domain": "www.designboom.com",
      "desc": "综合设计媒体——建筑、产品、艺术、品牌的全球性资讯平台。"
    },
    {
      "cat": "visual-production",
      "sub": "design-media",
      "tier": "A",
      "name": "Dezeen",
      "url": "https://www.dezeen.com",
      "domain": "www.dezeen.com",
      "desc": "全球最具影响力设计媒体——建筑、室内、品牌空间。跨境开店前必看。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "The Robin Report",
      "url": "https://www.therobinreport.com",
      "domain": "www.therobinreport.com",
      "desc": "零售品牌战略深度分析——DTC、百货、电商的模式与策略。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "S",
      "name": "Business of Fashion",
      "url": "https://www.businessoffashion.com",
      "domain": "www.businessoffashion.com",
      "desc": "时尚产业权威媒体——品牌战略、零售创新、消费趋势分析。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "B",
      "name": "Footwear News",
      "url": "https://footwearnews.com",
      "domain": "footwearnews.com",
      "desc": "鞋履与运动品牌——新品发布、品牌合作、零售趋势。"
    },
    {
      "cat": "market-product",
      "sub": "new-products",
      "tier": "A",
      "name": "Product Hunt",
      "url": "https://www.producthunt.com",
      "domain": "www.producthunt.com",
      "desc": "每日新产品发现——科技产品、设计工具、AI 应用创新窗口。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "S",
      "name": "Midjourney",
      "url": "https://www.midjourney.com",
      "domain": "www.midjourney.com",
      "desc": "AI 图像生成——品牌视觉探索、概念稿、产品渲染的首选工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "B",
      "name": "DALL·E",
      "url": "https://openai.com/index/dall-e-3",
      "domain": "openai.com",
      "desc": "OpenAI 图像生成——与 ChatGPT 深度集成的视觉创意工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "A",
      "name": "Runway",
      "url": "https://runwayml.com",
      "domain": "runwayml.com",
      "desc": "AI 视频生成与编辑——品牌视频素材、产品演示、动态视觉生产。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "B",
      "name": "ComfyUI",
      "url": "https://github.com/comfyanonymous/ComfyUI",
      "domain": "github.com",
      "desc": "节点式 AI 图像工作流——Stable Diffusion 最灵活的生产界面。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "A",
      "name": "Adobe Firefly",
      "url": "https://www.adobe.com/products/firefly.html",
      "domain": "www.adobe.com",
      "desc": "Adobe 生成式 AI——与 Photoshop/Illustrator 集成的品牌视觉生产工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "A",
      "name": "Canva AI",
      "url": "https://www.canva.com/ai-image-generator",
      "domain": "www.canva.com",
      "desc": "Canva AI 设计——品牌模板 + AI 生成，非设计师的快捷品牌工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "A",
      "name": "Figma AI",
      "url": "https://www.figma.com/ai",
      "domain": "www.figma.com",
      "desc": "Figma AI 功能——UI 与品牌设计的 AI 辅助：自动布局、内容填充。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "B",
      "name": "Stable Diffusion WebUI",
      "url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
      "domain": "github.com",
      "desc": "开源 AI 图像生成——本地部署，品牌素材全流程自主可控。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "Kaiber",
      "url": "https://kaiber.ai",
      "domain": "kaiber.ai",
      "desc": "AI 视频与动画——品牌故事视频、动态视觉素材生成。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "B",
      "name": "Looka",
      "url": "https://looka.com",
      "domain": "looka.com",
      "desc": "AI Logo 与品牌套件生成——快速品牌视觉方案原型。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "B",
      "name": "Brandmark",
      "url": "https://brandmark.io",
      "domain": "brandmark.io",
      "desc": "AI 品牌标识生成——输入关键词，自动生成品牌视觉方案。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "B",
      "name": "Galileo AI",
      "url": "https://www.usegalileo.ai",
      "domain": "www.usegalileo.ai",
      "desc": "AI UI 设计——从文本描述生成完整界面设计稿。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "A",
      "name": "Sora",
      "url": "https://openai.com/sora",
      "domain": "openai.com",
      "desc": "OpenAI 视频生成——文生视频与图生视频，品牌广告素材新范式。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "Pika",
      "url": "https://pika.art",
      "domain": "pika.art",
      "desc": "AI 视频生成——短平快的视频素材生产工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "A",
      "name": "Suno",
      "url": "https://suno.com",
      "domain": "suno.com",
      "desc": "AI 音乐生成——品牌视频配乐与播客背景音乐。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "Udio",
      "url": "https://www.udio.com",
      "domain": "www.udio.com",
      "desc": "AI 音乐生成——品牌声音标识与广告配乐创作工具。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "A",
      "name": "ElevenLabs",
      "url": "https://elevenlabs.io",
      "domain": "elevenlabs.io",
      "desc": "AI 语音合成——品牌播客、广告旁白、多语言配音。"
    },
    {
      "cat": "tech-automation",
      "sub": "coding",
      "tier": "B",
      "name": "Replit AI",
      "url": "https://replit.com/ai",
      "domain": "replit.com",
      "desc": "AI 编程环境——品牌网站与电商工具快速原型开发。"
    },
    {
      "cat": "tech-automation",
      "sub": "coding",
      "tier": "B",
      "name": "Cursor",
      "url": "https://cursor.com",
      "domain": "cursor.com",
      "desc": "AI 编程编辑器——品牌技术部署与自动化脚本的首选开发环境。"
    },
    {
      "cat": "tech-automation",
      "sub": "ai-models",
      "tier": "B",
      "name": "Google AI Blog",
      "url": "https://blog.google/technology/ai",
      "domain": "blog.google",
      "desc": "Google AI 研究与应用——Gemini、AI Agent、多模态。"
    },
    {
      "cat": "tech-automation",
      "sub": "ai-models",
      "tier": "B",
      "name": "Google AI Developers Blog",
      "url": "https://developers.googleblog.com",
      "domain": "developers.googleblog.com",
      "desc": "Google 开发者博客——AI 工具链、API 更新、最佳实践。"
    },
    {
      "cat": "tech-automation",
      "sub": "ai-models",
      "tier": "B",
      "name": "OpenAI News",
      "url": "https://openai.com/news",
      "domain": "openai.com",
      "desc": "OpenAI 官方新闻——GPT 系列模型、API、产品发布。"
    },
    {
      "cat": "tech-automation",
      "sub": "ai-models",
      "tier": "B",
      "name": "Anthropic API Release Notes",
      "url": "https://docs.anthropic.com/en/release-notes/api",
      "domain": "docs.anthropic.com",
      "desc": "Anthropic Claude 系列模型 API 变更与功能更新。"
    },
    {
      "cat": "tech-automation",
      "sub": "ai-models",
      "tier": "B",
      "name": "NVIDIA 开发者博客",
      "url": "https://developer.nvidia.com/blog",
      "domain": "developer.nvidia.com",
      "desc": "NVIDIA 开发者博客——GPU、CUDA、AI 推理部署。"
    },
    {
      "cat": "compliance-fulfillment",
      "sub": "us",
      "tier": "B",
      "name": "US CBP 贸易公告",
      "url": "https://www.cbp.gov/trade",
      "domain": "www.cbp.gov",
      "desc": "美国海关边境保护局：清关政策、执法动态、Section 321。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "SocialBeta",
      "url": "https://socialbeta.com/",
      "domain": "socialbeta.com",
      "desc": "专注品牌营销实践与趋势研究，案例库丰富，营销人必看。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "数英 Digitaling",
      "url": "https://www.digitaling.com/",
      "domain": "www.digitaling.com",
      "desc": "数字营销综合平台，海量品牌广告案例与行业资讯。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "品牌星球 BrandStar",
      "url": "https://www.brandstar.com.cn/",
      "domain": "www.brandstar.com.cn",
      "desc": "聚焦新消费与 DTC 的品牌创新内容平台，深度报道+榜单。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "Morketing",
      "url": "https://www.morketing.com/",
      "domain": "www.morketing.com",
      "desc": "全球营销商业媒体，覆盖出海、Martech、品牌增长。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "广告门 Adquan",
      "url": "https://www.adquan.com/",
      "domain": "www.adquan.com",
      "desc": "老牌广告行业门户，案例、人事、行业动态。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "梅花网",
      "url": "https://www.meihua.info/",
      "domain": "www.meihua.info",
      "desc": "营销人资源库，案例、数据、创意榜单。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "广告狂人",
      "url": "https://www.mad-men.com/",
      "domain": "www.mad-men.com",
      "desc": "广告营销内容社区，案例拆解与行业观点。"
    },
    {
      "cat": "platform-channel",
      "sub": "community",
      "tier": "B",
      "name": "AMZ123",
      "url": "https://www.amz123.com/",
      "domain": "www.amz123.com",
      "desc": "跨境电商导航与资讯，平台动态、选品、合规一站看。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "B",
      "name": "Foodaily 每日食品",
      "url": "https://www.foodaily.com/",
      "domain": "www.foodaily.com",
      "desc": "食品饮料新消费媒体，新品趋势与品牌创新案例。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "A",
      "name": "Lean Luxe",
      "url": "https://www.leanluxe.com/",
      "domain": "www.leanluxe.com",
      "desc": "现代消费品牌的内参简报，专盯 DTC 与新奢。"
    },
    {
      "cat": "brand-retail",
      "sub": "dtc-retail",
      "tier": "B",
      "name": "RetailWire",
      "url": "https://www.retailwire.com/",
      "domain": "www.retailwire.com",
      "desc": "零售行业讨论社区，专家点评热点零售事件。"
    },
    {
      "cat": "growth-ads",
      "sub": "ad-library",
      "tier": "S",
      "name": "Meta 广告库",
      "url": "https://www.facebook.com/ads/library/",
      "domain": "www.facebook.com",
      "desc": "Meta 全平台在投广告公开库，看竞品到底在投什么。"
    },
    {
      "cat": "growth-ads",
      "sub": "ad-library",
      "tier": "A",
      "name": "Google 广告透明中心",
      "url": "https://adstransparency.google.com/",
      "domain": "adstransparency.google.com",
      "desc": "Google 全渠道广告透明库，查任意广告主的在投素材。"
    },
    {
      "cat": "growth-ads",
      "sub": "creative-intel",
      "tier": "A",
      "name": "Foreplay",
      "url": "https://www.foreplay.co/",
      "domain": "www.foreplay.co",
      "desc": "广告创意收藏与竞品追踪工具，建自己的 swipe file。"
    },
    {
      "cat": "growth-ads",
      "sub": "creative-intel",
      "tier": "B",
      "name": "Atria",
      "url": "https://www.tryatria.com/",
      "domain": "www.tryatria.com",
      "desc": "AI 广告情报，拆解高效广告的钩子与文案框架。"
    },
    {
      "cat": "growth-ads",
      "sub": "creative-intel",
      "tier": "B",
      "name": "Ads of the World",
      "url": "https://www.adsoftheworld.com/",
      "domain": "www.adsoftheworld.com",
      "desc": "全球创意广告档案库，按品类/媒介找平面与影视广告。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "Marketing Brew",
      "url": "https://www.marketingbrew.com/",
      "domain": "www.marketingbrew.com",
      "desc": "轻松好读的营销日报，快速跟上品牌营销动态。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "A",
      "name": "Ad Age",
      "url": "https://adage.com/",
      "domain": "adage.com",
      "desc": "广告业权威大刊，品牌、代理商与营销战略。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "The Drum",
      "url": "https://www.thedrum.com/",
      "domain": "www.thedrum.com",
      "desc": "国际营销与创意媒体，趋势、案例、奖项。"
    },
    {
      "cat": "growth-ads",
      "sub": "marketing-media",
      "tier": "B",
      "name": "Contagious",
      "url": "https://www.contagious.com/",
      "domain": "www.contagious.com",
      "desc": "创意营销情报，深挖最具突破性的品牌战役。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Jungle Scout",
      "url": "https://www.junglescout.com/",
      "domain": "www.junglescout.com",
      "desc": "亚马逊选品与市场数据工具，估销量、查竞品。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Helium 10",
      "url": "https://www.helium10.com/",
      "domain": "www.helium10.com",
      "desc": "亚马逊卖家全能工具集，关键词、选品、运营。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "卖家精灵 SellerSprite",
      "url": "https://www.sellersprite.com/",
      "domain": "www.sellersprite.com",
      "desc": "中文亚马逊选品运营工具，市场分析+关键词+监控。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Keepa",
      "url": "https://keepa.com/",
      "domain": "keepa.com",
      "desc": "亚马逊历史价格与销量排名追踪，选品必备。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "B",
      "name": "SmartScout",
      "url": "https://www.smartscout.com/",
      "domain": "www.smartscout.com",
      "desc": "从品牌、子品类、市场空白切入的亚马逊市场研究工具。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "Semrush",
      "url": "https://www.semrush.com/",
      "domain": "www.semrush.com",
      "desc": "SEO 与数字竞争情报，看竞品流量与关键词。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "A",
      "name": "eMarketer",
      "url": "https://www.emarketer.com/",
      "domain": "www.emarketer.com",
      "desc": "数字经济与电商数据研究，市场规模与预测权威。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "B",
      "name": "Glimpse",
      "url": "https://meetglimpse.com/",
      "domain": "meetglimpse.com",
      "desc": "放大 Google Trends 的趋势发现工具，早期品类信号。"
    },
    {
      "cat": "market-product",
      "sub": "tools",
      "tier": "B",
      "name": "Coresight Research",
      "url": "https://coresight.com/",
      "domain": "coresight.com",
      "desc": "零售与科技研究机构，深度报告与数据。"
    },
    {
      "cat": "market-product",
      "sub": "trend",
      "tier": "A",
      "name": "TrendWatching",
      "url": "https://www.trendwatching.com/",
      "domain": "www.trendwatching.com",
      "desc": "全球消费趋势观察，按区域/主题给趋势框架。"
    },
    {
      "cat": "brand-retail",
      "sub": "capital",
      "tier": "A",
      "name": "a16z",
      "url": "https://a16z.com/",
      "domain": "a16z.com",
      "desc": "顶级风投 a16z 的内容，消费与科技赛道前瞻观点。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "A",
      "name": "The Brand Identity",
      "url": "https://the-brandidentity.com/",
      "domain": "the-brandidentity.com",
      "desc": "品牌设计案例与设计师访谈，更新勤、品味高。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "B",
      "name": "Logobook",
      "url": "https://www.logobook.com/",
      "domain": "www.logobook.com",
      "desc": "经典 logo 与商标设计参考库，按形态检索。"
    },
    {
      "cat": "visual-production",
      "sub": "identity",
      "tier": "B",
      "name": "World Brand Design Society",
      "url": "https://worldbranddesign.com/",
      "domain": "worldbranddesign.com",
      "desc": "全球品牌设计案例库，量大、覆盖广。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Behance",
      "url": "https://www.behance.net/",
      "domain": "www.behance.net",
      "desc": "Adobe 旗下全球设计师作品集，各领域找参考。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Land-book",
      "url": "https://land-book.com/",
      "domain": "land-book.com",
      "desc": "落地页与网站设计灵感库，转化页参考首选。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Godly",
      "url": "https://godly.website/",
      "domain": "godly.website",
      "desc": "极高水准的网页设计精选，看 web 天花板。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "Httpster",
      "url": "https://httpster.net/",
      "domain": "httpster.net",
      "desc": "当代网页设计灵感，偏潮、偏实验。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "Minimal Gallery",
      "url": "https://minimal.gallery/",
      "domain": "minimal.gallery",
      "desc": "极简风网页设计精选。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "One Page Love",
      "url": "https://onepagelove.com/",
      "domain": "onepagelove.com",
      "desc": "单页网站设计灵感与模板。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "B",
      "name": "Lapa Ninja",
      "url": "https://www.lapa.ninja/",
      "domain": "www.lapa.ninja",
      "desc": "2000+ 优秀落地页案例，按品类浏览。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Mobbin",
      "url": "https://mobbin.com/",
      "domain": "mobbin.com",
      "desc": "海量真实 App/网页界面截图库，做 UI 参考。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Refero",
      "url": "https://refero.design/",
      "domain": "refero.design",
      "desc": "UI/UX 设计参考库，按流程/组件检索真实界面。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Cosmos",
      "url": "https://www.cosmos.so/",
      "domain": "www.cosmos.so",
      "desc": "新一代视觉灵感采集，无算法干扰、质量高。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Savee",
      "url": "https://savee.it/",
      "domain": "savee.it",
      "desc": "设计师常用的视觉灵感收藏工具。"
    },
    {
      "cat": "visual-production",
      "sub": "web-ui",
      "tier": "A",
      "name": "Are.na",
      "url": "https://www.are.na/",
      "domain": "www.are.na",
      "desc": "研究式视觉策展工具，做 moodboard 与知识库。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "S",
      "name": "Google Fonts",
      "url": "https://fonts.google.com/",
      "domain": "fonts.google.com",
      "desc": "免费可商用字体库，直接选直接用。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "A",
      "name": "Fontshare",
      "url": "https://www.fontshare.com/",
      "domain": "www.fontshare.com",
      "desc": "高质量免费商用字体库（Indian Type Foundry 出品）。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "A",
      "name": "Coolors",
      "url": "https://coolors.co/",
      "domain": "coolors.co",
      "desc": "秒出配色方案并保存，配色起步首选。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "B",
      "name": "Adobe Color",
      "url": "https://color.adobe.com/",
      "domain": "color.adobe.com",
      "desc": "配色轮与趋势色板，可提取图片配色。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "B",
      "name": "Khroma",
      "url": "https://www.khroma.co/",
      "domain": "www.khroma.co",
      "desc": "AI 配色生成，按你的喜好训练出色板。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "B",
      "name": "Realtime Colors",
      "url": "https://www.realtimecolors.com/",
      "domain": "www.realtimecolors.com",
      "desc": "在真实 UI 上实时预览配色与字体效果。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "B",
      "name": "Fontjoy",
      "url": "https://fontjoy.com/",
      "domain": "fontjoy.com",
      "desc": "AI 字体搭配生成，快速找到字体组合。"
    },
    {
      "cat": "visual-production",
      "sub": "type-color",
      "tier": "B",
      "name": "Velvetyne",
      "url": "https://velvetyne.fr/",
      "domain": "velvetyne.fr",
      "desc": "实验性开源字体厂，找有个性的免费字体。"
    },
    {
      "cat": "visual-production",
      "sub": "packaging",
      "tier": "A",
      "name": "Pentawards",
      "url": "https://www.pentawards.com/",
      "domain": "www.pentawards.com",
      "desc": "全球包装设计大奖，看顶级包装案例。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "S",
      "name": "Unsplash",
      "url": "https://unsplash.com/",
      "domain": "unsplash.com",
      "desc": "高质量免费可商用图片库，量大质优。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "A",
      "name": "Pexels",
      "url": "https://www.pexels.com/",
      "domain": "www.pexels.com",
      "desc": "免费可商用图片与视频素材。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "A",
      "name": "Freepik",
      "url": "https://www.freepik.com/",
      "domain": "www.freepik.com",
      "desc": "矢量、图片、PSD 素材大全（注意授权）。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Pixabay",
      "url": "https://pixabay.com/",
      "domain": "pixabay.com",
      "desc": "免费图片/视频/插画素材。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "A",
      "name": "The Noun Project",
      "url": "https://thenounproject.com/",
      "domain": "thenounproject.com",
      "desc": "海量统一风格图标库，覆盖各类概念。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "A",
      "name": "Lucide",
      "url": "https://lucide.dev/",
      "domain": "lucide.dev",
      "desc": "开源简洁线性图标集，开发友好。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Iconfinder",
      "url": "https://www.iconfinder.com/",
      "domain": "www.iconfinder.com",
      "desc": "图标搜索与购买平台，风格全。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Icons8",
      "url": "https://icons8.com/",
      "domain": "icons8.com",
      "desc": "图标、插画、图片、工具一站式。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Flaticon",
      "url": "https://www.flaticon.com/",
      "domain": "www.flaticon.com",
      "desc": "超大图标库，格式多。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Heroicons",
      "url": "https://heroicons.com/",
      "domain": "heroicons.com",
      "desc": "Tailwind 团队出品的精致开源图标。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Phosphor Icons",
      "url": "https://phosphoricons.com/",
      "domain": "phosphoricons.com",
      "desc": "灵活的开源图标家族，多种字重。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "A",
      "name": "Mockup World",
      "url": "https://www.mockupworld.co/",
      "domain": "www.mockupworld.co",
      "desc": "免费样机大全，产品/包装/UI 展示。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Unblast",
      "url": "https://unblast.com/",
      "domain": "unblast.com",
      "desc": "免费样机、模板与素材精选。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "unDraw",
      "url": "https://undraw.co/",
      "domain": "undraw.co",
      "desc": "可改色的开源扁平插画，配色随站点走。"
    },
    {
      "cat": "visual-production",
      "sub": "assets",
      "tier": "B",
      "name": "Open Peeps",
      "url": "https://www.openpeeps.com/",
      "domain": "www.openpeeps.com",
      "desc": "手绘人物插画库，自由组合。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "A",
      "name": "Ideogram",
      "url": "https://ideogram.ai/",
      "domain": "ideogram.ai",
      "desc": "擅长文字排版的 AI 图像生成，做海报/logo 概念。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "A",
      "name": "Recraft",
      "url": "https://www.recraft.ai/",
      "domain": "www.recraft.ai",
      "desc": "面向设计的 AI 图像与矢量生成，可控品牌风格。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "A",
      "name": "Krea",
      "url": "https://www.krea.ai/",
      "domain": "www.krea.ai",
      "desc": "实时 AI 图像生成与放大，创意探索快。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "A",
      "name": "Photoroom",
      "url": "https://www.photoroom.com/",
      "domain": "www.photoroom.com",
      "desc": "AI 抠图与产品图生成，电商主图利器。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "B",
      "name": "Leonardo AI",
      "url": "https://leonardo.ai/",
      "domain": "leonardo.ai",
      "desc": "可控的 AI 图像生成，模型与风格丰富。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-image",
      "tier": "B",
      "name": "Magnific",
      "url": "https://magnific.ai/",
      "domain": "magnific.ai",
      "desc": "AI 高清放大与重绘，细节增强惊人。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "A",
      "name": "Luma Dream Machine",
      "url": "https://lumalabs.ai/",
      "domain": "lumalabs.ai",
      "desc": "AI 文/图生视频，品牌动态素材新范式。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "HeyGen",
      "url": "https://www.heygen.com/",
      "domain": "www.heygen.com",
      "desc": "AI 数字人与多语配音视频。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "Descript",
      "url": "https://www.descript.com/",
      "domain": "www.descript.com",
      "desc": "像文档一样剪视频/播客，AI 配音。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-video-audio",
      "tier": "B",
      "name": "Captions",
      "url": "https://www.captions.ai/",
      "domain": "www.captions.ai",
      "desc": "AI 短视频字幕与口播生成。"
    },
    {
      "cat": "growth-ads",
      "sub": "content-conversion",
      "tier": "A",
      "name": "Gamma",
      "url": "https://gamma.app/",
      "domain": "gamma.app",
      "desc": "AI 生成演示/网页/文档，做提案快。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "A",
      "name": "Framer",
      "url": "https://www.framer.com/",
      "domain": "www.framer.com",
      "desc": "AI 辅助的高质量建站工具，设计即上线。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "A",
      "name": "Spline",
      "url": "https://spline.design/",
      "domain": "spline.design",
      "desc": "浏览器里做 3D 与交互，落地页酷炫元素。"
    },
    {
      "cat": "visual-production",
      "sub": "ai-design",
      "tier": "B",
      "name": "Uizard",
      "url": "https://uizard.io/",
      "domain": "uizard.io",
      "desc": "文字/手稿一键转 UI 设计稿。"
    },
    {
      "cat": "tech-automation",
      "sub": "coding",
      "tier": "B",
      "name": "v0",
      "url": "https://v0.dev/",
      "domain": "v0.dev",
      "desc": "Vercel 的 AI 生成前端界面，描述即出代码。"
    }
  ]
};
