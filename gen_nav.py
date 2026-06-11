import json

with open("nav_data.json", "r", encoding="utf-8") as f:
    D = json.load(f)

cat_order = D["cat_order"]
categories = D["categories"]

# Card HTML
def card(s):
    domain = s["url"].replace("https://", "").replace("http://", "").split("/")[0]
    favicon = f'https://www.google.com/s2/favicons?domain={domain}&sz=32'
    return f'''<a href="{s["url"]}" target="_blank" rel="noopener" class="card">
  <span class="card-icon"><img src="{favicon}" alt="" width="16" height="16" loading="lazy" onerror="this.style.display='none'"></span>
  <span class="card-name">{s["name"]}</span>
  <span class="card-desc">{s["desc"]}</span>
  <span class="card-domain">{domain}</span>
</a>'''

# Sidebar
sidebar_links = []
for i, cat in enumerate(cat_order, 1):
    info = categories[cat]
    sidebar_links.append(f'<a href="#cat-{cat}" class="sb-link">{info["name"]}</a>')

# Sections
sections = []
for i, cat in enumerate(cat_order, 1):
    info = categories[cat]
    subs = info.get("subs")
    section_html = f'''<section class="cat-section" id="cat-{cat}">
  <div class="cat-head">
    <span class="cat-index">{i:02d}</span>
    <h2>{info["name"]}</h2>
    <span class="cat-desc">{info["desc"]}</span>
  </div>'''

    if subs:
        sub_ids = list(subs.keys())
        # Tab bar
        tabs = '<button class="stab on" data-sub="all">全部</button>\n'
        for sk in sub_ids:
            tabs += f'<button class="stab" data-sub="{sk}">{subs[sk]["name"]}</button>\n'
        section_html += f'\n  <div class="sub-tabs">{tabs}</div>\n'

        # All pane
        all_sources = []
        for sk in sub_ids:
            all_sources.extend(subs[sk]["sources"])
        if info.get("sources"):
            all_sources.extend(info["sources"])
        section_html += '  <div class="card-grid sub-pane" data-sub="all">\n'
        section_html += "\n".join(card(s) for s in all_sources)
        section_html += '\n  </div>\n'

        # Individual sub panes
        for sk in sub_ids:
            section_html += f'  <div class="card-grid sub-pane" data-sub="{sk}" style="display:none">\n'
            section_html += "\n".join(card(s) for s in subs[sk]["sources"])
            section_html += '\n  </div>\n'
    else:
        srcs = info.get("sources", [])
        section_html += '\n  <div class="card-grid">\n'
        section_html += "\n".join(card(s) for s in srcs)
        section_html += '\n  </div>\n'

    section_html += '</section>'
    sections.append(section_html)

sections_html = "\n\n".join(sections)
sidebar_html = "\n".join(sidebar_links)

# Read template and fill
with open("nav_template_v2.html", "r", encoding="utf-8") as f:
    template = f.read()

html = template.replace("{{TOTAL}}", str(D["total"])).replace("{{SIDEBAR}}", sidebar_html).replace("{{SECTIONS}}", sections_html)

with open("../sequentry-site/nav/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated nav/index.html: {D['total']} sources, {len(cat_order)} categories")
