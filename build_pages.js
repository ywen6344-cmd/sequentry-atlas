/* 序引海图 · 静态 SEO 页生成器
 * 读取 live 数据（links.js 的 NAV_DATA + index.html 的 GLOBAL_STORES）+ guides-src/*.md，
 * 生成 /markets/<slug>/、/categories/<id>/、/guides/<slug>/、三个枢纽页与 sitemap.xml。
 * 不修改 index.html，单一数据源。  运行：node build_pages.js
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = __dirname;
const BASE_URL = 'https://atlas.sequentry.com';
const TODAY = new Date().toISOString().slice(0, 10);

function esc(s){return (s==null?'':String(s)).replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));}

/* ---- 读取 SPA 数据文件里的 window 全局 ---- */
function loadGlobals(file){
  const code = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const sandbox = {}; sandbox.window = sandbox;
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox, {timeout:5000});
  return sandbox;
}
/* ---- 从 index.html 提取 `var NAME=[...]` 数组（括号配对） ---- */
function extractArray(html, name){
  const start = html.indexOf('var ' + name + '=[');
  if (start < 0) throw new Error('找不到 ' + name);
  let i = html.indexOf('[', start), depth = 0, inStr = false, q = '';
  for (; i < html.length; i++){
    const c = html[i];
    if (inStr){ if (c === '\\'){ i++; continue; } if (c === q) inStr = false; continue; }
    if (c === '"' || c === "'"){ inStr = true; q = c; continue; }
    if (c === '[') depth++;
    else if (c === ']'){ depth--; if (depth === 0){ const txt = html.slice(html.indexOf('[', start), i + 1); return vm.runInNewContext('(' + txt + ')'); } }
  }
  throw new Error('数组未闭合: ' + name);
}

const NAV = loadGlobals('links.js').NAV_DATA || {categories:[], links:[]};
const GLOBAL_STORES = extractArray(fs.readFileSync(path.join(ROOT,'index.html'),'utf8'), 'GLOBAL_STORES');
const CATS = NAV.categories || [];

/* ---- 市场分区 slug 与简介 ---- */
const MARKET = {
  '热门':    {slug:'popular',        title:'热门跨境平台',    intro:'跨境出海最常用、生态最成熟的主流平台合集——综合平台、内容电商、独立站与全托管新势力，覆盖大多数品类的起步选择。'},
  '北美':    {slug:'north-america',  title:'北美',            intro:'美国、加拿大市场：平台成熟、广告生态完整、履约与合规标准稳定，是品牌化与规模化的核心战场。'},
  '欧洲':    {slug:'europe',         title:'欧洲',            intro:'德法意西等多国市场：VAT、EPR、CE 等合规密集，本地化要求高，适合长期品牌化经营。'},
  '英国':    {slug:'uk',             title:'英国',            intro:'脱欧后合规独立于欧盟：Amazon UK、独立站、TikTok Shop 与零售媒体并行。'},
  '日韩':    {slug:'japan-korea',    title:'日本 / 韩国',     intro:'消费审美与本地客服要求高，适合精细化品牌与垂直品类，客单与复购表现优。'},
  '东南亚':  {slug:'southeast-asia', title:'东南亚',          intro:'Shopee、Lazada、TikTok Shop 主导：内容电商爆发、本地履约与价格带差异大。'},
  '拉美':    {slug:'latin-america',  title:'拉美',            intro:'Mercado Libre、Amazon、Shopee 等混合市场：支付、物流与本地化是关键变量。'},
  '中东':    {slug:'middle-east',    title:'中东',            intro:'海湾市场客单价高：Noon、Amazon.ae/.sa，本地支付与清关能力重要。'},
  '非洲':    {slug:'africa',         title:'非洲',            intro:'增长型市场：Jumia 等平台与本地支付、物流网络仍在快速演进。'},
  '俄·独联': {slug:'russia-cis',     title:'俄罗斯 / 独联体', intro:'Ozon、Wildberries 主导：本土支付与海外仓体系独立，增长快但合规与汇兑需谨慎。'},
  '南亚':    {slug:'south-asia',     title:'南亚 / 印度',     intro:'规模巨大但本地规则复杂，适合供应链、本地伙伴与价格带精细化。'},
  'B2B':     {slug:'b2b',            title:'B2B / 批发',      intro:'面向工厂、ODM/OEM、批发询盘与渠道型客户的平台与入口。'}
};
function marketInfo(region){return MARKET[region] || {slug:(region.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'region'), title:region, intro:region+'市场的主流跨境电商平台与开店入口。'};}
function marketTitleBySlug(slug){const r=Object.keys(MARKET).find(k=>MARKET[k].slug===slug);return r?MARKET[r].title:slug;}
function catNameById(id){const c=CATS.find(c=>c.id===id);return c?c.name:id;}

/* ---- 轻量 Markdown（标题/段落/列表/引用/粗斜体/行内码/链接/分隔线/代码块） ---- */
function mdInline(s){
  return esc(s)
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,(m,t,u)=>`<a href="${u}" rel="noopener">${t}</a>`)
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*]+)\*/g,'$1<em>$2</em>')
    .replace(/`([^`]+)`/g,'<code>$1</code>');
}
function mdToHtml(md){
  const lines = md.replace(/\r\n/g,'\n').split('\n');
  let html='', i=0;
  while(i<lines.length){
    const line=lines[i];
    if(/^\s*$/.test(line)){i++;continue;}
    if(/^```/.test(line)){let buf=[];i++;while(i<lines.length&&!/^```/.test(lines[i])){buf.push(esc(lines[i]));i++;}i++;html+=`<pre><code>${buf.join('\n')}</code></pre>`;continue;}
    if(/^###\s+/.test(line)){html+=`<h3>${mdInline(line.replace(/^###\s+/,''))}</h3>`;i++;continue;}
    if(/^##\s+/.test(line)){html+=`<h2>${mdInline(line.replace(/^##\s+/,''))}</h2>`;i++;continue;}
    if(/^---+\s*$/.test(line)){html+='<hr>';i++;continue;}
    if(/^>\s?/.test(line)){let buf=[];while(i<lines.length&&/^>\s?/.test(lines[i])){buf.push(lines[i].replace(/^>\s?/,''));i++;}html+=`<blockquote>${mdInline(buf.join(' '))}</blockquote>`;continue;}
    if(/^[-*]\s+/.test(line)){let buf=[];while(i<lines.length&&/^[-*]\s+/.test(lines[i])){buf.push(`<li>${mdInline(lines[i].replace(/^[-*]\s+/,''))}</li>`);i++;}html+=`<ul>${buf.join('')}</ul>`;continue;}
    if(/^\d+\.\s+/.test(line)){let buf=[];while(i<lines.length&&/^\d+\.\s+/.test(lines[i])){buf.push(`<li>${mdInline(lines[i].replace(/^\d+\.\s+/,''))}</li>`);i++;}html+=`<ol>${buf.join('')}</ol>`;continue;}
    let buf=[];while(i<lines.length&&!/^\s*$/.test(lines[i])&&!/^(#{2,3}\s|>|[-*]\s|\d+\.\s|```|---+\s*$)/.test(lines[i])){buf.push(lines[i]);i++;}
    html+=`<p>${mdInline(buf.join(' '))}</p>`;
  }
  return html;
}
function parseFrontmatter(raw){
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if(!m) return {meta:{}, body:raw};
  const meta={};
  m[1].split('\n').forEach(l=>{const mm=l.match(/^([a-zA-Z0-9_]+):\s*(.*)$/);if(mm)meta[mm[1]]=mm[2].trim();});
  return {meta, body:m[2]};
}
function loadGuides(){
  const dir = path.join(ROOT,'guides-src');
  if(!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f=>f.endsWith('.md')).map(f=>{
    const {meta,body}=parseFrontmatter(fs.readFileSync(path.join(dir,f),'utf8'));
    meta.slug = meta.slug || f.replace(/\.md$/,'');
    meta.bodyHtml = mdToHtml(body);
    return meta;
  }).sort((a,b)=>String(b.date||'').localeCompare(String(a.date||'')));
}

/* ---- HTML 骨架 ---- */
function head(o){
  return `<!DOCTYPE html><html lang="zh-CN"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${esc(o.title)}</title>
<meta name="description" content="${esc(o.desc)}">
<link rel="canonical" href="${BASE_URL}${o.path}">
<meta property="og:title" content="${esc(o.title)}">
<meta property="og:description" content="${esc(o.desc)}">
<meta property="og:type" content="${o.ogType||'website'}">
<meta property="og:url" content="${BASE_URL}${o.path}">
<meta property="og:site_name" content="序引海图 · Sequentry Atlas">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="${BASE_URL}/assets/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="${BASE_URL}/assets/og-cover.png">
<link rel="icon" type="image/svg+xml" href="${o.pre}assets/sequentry-graphite-app-icon-light.svg">
<link rel="stylesheet" href="${o.pre}pages.css">
<script type="application/ld+json">${JSON.stringify(o.jsonld)}</script>
<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","xaaa1cqss1");</script>
</head><body>`;
}
function topbar(pre){
  return `<header class="site-top"><div class="wrap">
<a class="site-brand" href="${pre}index.html"><img src="${pre}assets/sequentry-graphite-mark-primary.svg" alt="" aria-hidden="true"><b>序引海图</b><span>Sequentry&nbsp;Atlas</span></a>
<a class="to-app" href="${pre}index.html">打开导航 →</a>
</div></header>`;
}
function footer(pre){
  return `<footer><div class="wrap">
<div><a href="${pre}index.html">序引海图</a> · 品牌出海的工具海图 · <a href="${pre}guides/">出海指南</a> · <a href="${pre}standards.html">收录与评估标准</a></div>
<div class="cp">© 2026 序引效能（Sequentry）</div>
</div></footer>
<script defer src="${pre}analytics-events.js"></script>
</body></html>`;
}
function relatedGuidesSection(guides){
  if(!guides||!guides.length) return '';
  const items = guides.map(g=>`<a href="../../guides/${esc(g.slug)}/">${esc(g.title)}</a>`).join('');
  return `<section class="related"><div class="sec-h">相关指南</div><div class="chips">${items}</div></section>`;
}
function write(rel, html){
  const fp = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(fp), {recursive:true});
  fs.writeFileSync(fp, html, 'utf8');
}

/* ---- 市场页 ---- */
function platformCard(it){
  const links=(it.links||[]).map(x=>`<a href="${esc(x[1])}" target="_blank" rel="noopener nofollow">${esc(x[0])}</a>`).join('');
  return `<article class="card"><h3>${esc(it.name)}</h3>${it.domain?`<span class="domain">${esc(it.domain)}</span>`:''}${it.note?`<p>${esc(it.note)}</p>`:''}${links?`<div class="links">${links}</div>`:''}</article>`;
}
function buildMarket(region, items, siblings, relGuides){
  const info=marketInfo(region), names=items.map(i=>i.name).slice(0,8).join('、');
  const title=`${info.title}出海开店平台与入口 · 序引海图`;
  const desc=`${info.title}主流跨境电商平台与开店入口：${names}。直达官方入驻与卖家后台，序引海图（Sequentry Atlas）收录整理。`;
  const p=`/markets/${info.slug}/`, pre='../../';
  const jsonld={"@context":"https://schema.org","@graph":[
    {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"序引海图","item":BASE_URL+'/'},
      {"@type":"ListItem","position":2,"name":"全球开店","item":BASE_URL+'/markets/'},
      {"@type":"ListItem","position":3,"name":info.title,"item":BASE_URL+p}]},
    {"@type":"ItemList","name":title,"numberOfItems":items.length,"itemListElement":items.map((it,i)=>({"@type":"ListItem","position":i+1,"name":it.name,"url":(it.links&&it.links[0]&&it.links[0][1])||undefined}))}
  ]};
  const related=siblings.filter(r=>r!==region).map(r=>{const s=marketInfo(r);return `<a href="../${s.slug}/">${esc(s.title)}</a>`;}).join('');
  const html=head({title,desc,path:p,pre,jsonld})+topbar(pre)+
    `<div class="wrap"><nav class="crumb"><a href="${pre}index.html">序引海图</a><span>/</span><a href="../">全球开店</a><span>/</span>${esc(info.title)}</nav>
<main>
<h1>${esc(info.title)}出海开店平台</h1>
<p class="lead">${esc(info.intro)}</p>
<div class="meta-line">${items.length} 个平台 · 官方入驻 / 卖家后台直达</div>
<div class="card-grid">${items.map(platformCard).join('')}</div>
${relatedGuidesSection(relGuides)}
<section class="related"><div class="sec-h">其他市场</div><div class="chips">${related}</div></section>
</main></div>`+footer(pre);
  write(`markets/${info.slug}/index.html`, html);
  return {slug:info.slug, title:info.title, count:items.length, path:p};
}

/* ---- 分类页 ---- */
function linkCard(l){
  return `<article class="card"><h3>${esc(l.name)}${l.tier?`<span class="tier ${esc(l.tier)}">${esc(l.tier)}</span>`:''}</h3>${l.domain?`<span class="domain">${esc(l.domain)}</span>`:''}${l.desc?`<p>${esc(l.desc)}</p>`:''}<a class="visit" href="${esc(l.url)}" target="_blank" rel="noopener nofollow">访问 →</a></article>`;
}
function buildCategory(cat, allCats, relGuides){
  const links=(NAV.links||[]).filter(l=>l.cat===cat.id);
  if(!links.length) return null;
  const names=links.slice(0,8).map(l=>l.name).join('、');
  const title=`${cat.name}工具与信源 · 序引海图`;
  const desc=`${cat.name}：${cat.desc||names}。序引海图（Sequentry Atlas）按收录标准整理的品牌出海工具与信息入口，共 ${links.length} 项。`;
  const p=`/categories/${cat.id}/`, pre='../../';
  const subs=Array.isArray(cat.subs)?cat.subs:[];
  let body='';
  if(subs.length){
    subs.forEach(sb=>{const sl=links.filter(l=>l.sub===sb.id);if(sl.length)body+=`<div class="sec-h">${esc(sb.name)}</div><div class="card-grid">${sl.map(linkCard).join('')}</div>`;});
    const noSub=links.filter(l=>!l.sub||!subs.some(s=>s.id===l.sub));
    if(noSub.length)body+=`<div class="sec-h">其他</div><div class="card-grid">${noSub.map(linkCard).join('')}</div>`;
  } else { body=`<div class="card-grid">${links.map(linkCard).join('')}</div>`; }
  const jsonld={"@context":"https://schema.org","@graph":[
    {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"序引海图","item":BASE_URL+'/'},
      {"@type":"ListItem","position":2,"name":"完整目录","item":BASE_URL+'/categories/'},
      {"@type":"ListItem","position":3,"name":cat.name,"item":BASE_URL+p}]},
    {"@type":"ItemList","name":title,"numberOfItems":links.length,"itemListElement":links.map((l,i)=>({"@type":"ListItem","position":i+1,"name":l.name,"url":l.url}))}
  ]};
  const related=allCats.filter(c=>c.id!==cat.id).map(c=>`<a href="../${c.id}/">${esc(c.name)}</a>`).join('');
  const html=head({title,desc,path:p,pre,jsonld})+topbar(pre)+
    `<div class="wrap"><nav class="crumb"><a href="${pre}index.html">序引海图</a><span>/</span><a href="../">完整目录</a><span>/</span>${esc(cat.name)}</nav>
<main>
<h1>${esc(cat.name)}</h1>
${cat.desc?`<p class="lead">${esc(cat.desc)}</p>`:''}
<div class="meta-line">${links.length} 个入口 · 按序引海图收录标准整理</div>
${body}
${relatedGuidesSection(relGuides)}
<section class="related"><div class="sec-h">其他分类</div><div class="chips">${related}</div></section>
</main></div>`+footer(pre);
  write(`categories/${cat.id}/index.html`, html);
  return {id:cat.id, name:cat.name, count:links.length, path:p};
}

/* ---- 指南文章页 ---- */
function buildGuide(g){
  const p=`/guides/${g.slug}/`, pre='../../';
  const title=`${g.title} · 序引海图`;
  const desc=g.description||g.title;
  const jsonld={"@context":"https://schema.org","@graph":[
    {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"序引海图","item":BASE_URL+'/'},
      {"@type":"ListItem","position":2,"name":"出海指南","item":BASE_URL+'/guides/'},
      {"@type":"ListItem","position":3,"name":g.title,"item":BASE_URL+p}]},
    {"@type":"Article","headline":g.title,"description":desc,"datePublished":g.date||TODAY,"dateModified":g.date||TODAY,
     "author":{"@type":"Organization","name":"序引效能（Sequentry）","url":"https://www.sequentry.com/"},
     "publisher":{"@type":"Organization","name":"序引效能（Sequentry）","logo":BASE_URL+'/assets/sequentry-graphite-app-icon-light.svg'},
     "image":BASE_URL+'/assets/og-cover.png',"mainEntityOfPage":BASE_URL+p,"inLanguage":"zh-CN"}
  ]};
  const rels=[];
  if(g.market) rels.push(`<a href="../../markets/${esc(g.market)}/">${esc(marketTitleBySlug(g.market))}市场</a>`);
  if(g.category) rels.push(`<a href="../../categories/${esc(g.category)}/">${esc(catNameById(g.category))}</a>`);
  const relHtml = rels.length?`<section class="related"><div class="sec-h">相关</div><div class="chips">${rels.join('')}</div></section>`:'';
  const tpl = (g.template==='true')?`<div class="tpl-note">这是示例骨架，用来演示排版与发布流程。请替换为你的正文，并在 frontmatter 删除 <code>template: true</code>。</div>`:'';
  const html=head({title,desc,path:p,pre,jsonld,ogType:'article'})+topbar(pre)+
    `<div class="wrap"><nav class="crumb"><a href="${pre}index.html">序引海图</a><span>/</span><a href="../">出海指南</a><span>/</span>${esc(g.title)}</nav>
<main>
<div class="guide-head"><h1>${esc(g.title)}</h1></div>
<div class="guide-date">${esc(g.date||'')}　·　序引效能（Sequentry）</div>
${tpl}
<article class="prose">${g.bodyHtml}</article>
${relHtml}
</main></div>`+footer(pre);
  write(`guides/${g.slug}/index.html`, html);
  return {slug:g.slug, title:g.title, date:g.date||'', description:desc, path:p};
}

/* ---- 枢纽页 ---- */
function buildHub(kind, items){
  const map={markets:['全球开店 · 各地区主流平台','按地区查看全球主流跨境电商平台分布，直达各平台官方入驻与卖家后台入口。','全球开店'],
             categories:['完整目录 · 品牌出海工具分类','按分类浏览品牌出海全流程的工具与信息入口，每一项按序引海图收录标准整理。','完整目录']};
  const [h1,lead,crumb]=map[kind];
  const title=h1+' · 序引海图';
  const desc=kind==='markets'?'按地区浏览全球主流跨境电商平台与开店入口：北美、欧洲、英国、东南亚、日韩、拉美、中东等。序引海图整理。':'按分类浏览品牌出海工具与信息入口：平台政策、市场选品、广告投放、支付物流、合规与信源库等。序引海图整理。';
  const p=`/${kind}/`, pre='../';
  const jsonld={"@context":"https://schema.org","@type":"CollectionPage","name":title,"url":BASE_URL+p,"isPartOf":{"@type":"WebSite","name":"序引海图 Sequentry Atlas","url":BASE_URL+'/'}};
  const cards=items.map(it=>`<a class="hub-card" href="${it.slug||it.id}/"><strong>${esc(it.title||it.name)}</strong><span>${it.count} 个${kind==='markets'?'平台':'入口'} →</span></a>`).join('');
  const html=head({title,desc,path:p,pre,jsonld})+topbar(pre)+
    `<div class="wrap"><nav class="crumb"><a href="${pre}index.html">序引海图</a><span>/</span>${crumb}</nav>
<main><h1>${h1}</h1><p class="lead">${esc(lead)}</p><div class="hub-grid">${cards}</div></main></div>`+footer(pre);
  write(`${kind}/index.html`, html);
}
function buildGuidesHub(guides){
  const p='/guides/', pre='../';
  const title='出海指南 · 品牌出海怎么做 · 序引海图';
  const desc='序引海图的出海指南：分市场、分环节的实操与判断——平台怎么选、合规怎么过、坑在哪。序引效能（Sequentry）出品。';
  const jsonld={"@context":"https://schema.org","@type":"CollectionPage","name":title,"url":BASE_URL+p,"isPartOf":{"@type":"WebSite","name":"序引海图 Sequentry Atlas","url":BASE_URL+'/'}};
  const list = guides.length
    ? `<div class="guide-list">${guides.map(g=>`<a class="guide-item" href="${esc(g.slug)}/"><strong>${esc(g.title)}</strong><p>${esc(g.description)}</p><div class="d">${esc(g.date)}</div></a>`).join('')}</div>`
    : `<div class="empty-state">指南正在路上——分市场、分环节的实操与判断陆续上线。</div>`;
  const html=head({title,desc,path:p,pre,jsonld})+topbar(pre)+
    `<div class="wrap"><nav class="crumb"><a href="${pre}index.html">序引海图</a><span>/</span>出海指南</nav>
<main><h1>出海指南</h1><p class="lead">分市场、分环节的实操与判断——平台怎么选、合规怎么过、坑在哪。不是链接堆，是带观点的怎么做。</p>${list}</main></div>`+footer(pre);
  write('guides/index.html', html);
}

/* ---- 运行 ---- */
const guides = loadGuides();
const guidesByMarket={}, guidesByCat={};
guides.forEach(g=>{ if(g.market)(guidesByMarket[g.market]=guidesByMarket[g.market]||[]).push(g); if(g.category)(guidesByCat[g.category]=guidesByCat[g.category]||[]).push(g); });

const guidePages = guides.map(buildGuide);
const regions = GLOBAL_STORES.map(r=>r.region);
const marketPages = GLOBAL_STORES.map(r=>buildMarket(r.region, r.items||[], regions, guidesByMarket[marketInfo(r.region).slug]));
const catPages = CATS.map(c=>buildCategory(c, CATS, guidesByCat[c.id])).filter(Boolean);
buildHub('markets', marketPages);
buildHub('categories', catPages);
buildGuidesHub(guidePages);

/* ---- sitemap ---- */
const urls = [
  {loc:'/', freq:'daily', pri:'1.0'},
  {loc:'/standards.html', freq:'monthly', pri:'0.6'},
  {loc:'/markets/', freq:'weekly', pri:'0.8'},
  {loc:'/categories/', freq:'weekly', pri:'0.8'},
  {loc:'/guides/', freq:'weekly', pri:'0.8'},
  ...marketPages.map(m=>({loc:m.path, freq:'weekly', pri:'0.7'})),
  ...catPages.map(c=>({loc:c.path, freq:'weekly', pri:'0.7'})),
  ...guidePages.map(g=>({loc:g.path, freq:'monthly', pri:'0.7'}))
];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  urls.map(u=>`  <url>\n    <loc>${BASE_URL}${u.loc}</loc>\n    <lastmod>${TODAY}</lastmod>\n    <changefreq>${u.freq}</changefreq>\n    <priority>${u.pri}</priority>\n  </url>`).join('\n') +
  `\n</urlset>\n`;
fs.writeFileSync(path.join(ROOT,'sitemap.xml'), sitemap, 'utf8');

console.log(`市场页 ${marketPages.length}，分类页 ${catPages.length}，指南页 ${guidePages.length}`);
console.log(`指南：`, guidePages.map(g=>g.slug).join(', ')||'(无)');
console.log(`sitemap.xml：${urls.length} 条 URL`);
