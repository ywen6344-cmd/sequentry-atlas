# -*- coding: utf-8 -*-
"""
本地图标包构建器。
扫描 links.js / ai.js / index.html 里所有 domain / iconDomain，
逐个下载 favicon 到 assets/icons/{domain}.png，并生成 icons.js 清单
(window.NAV_ICONS = {"amazon.com":1, ...})。
网页端优先用本地图标，缺失再回落远程/首字母——一次构建、全站本地调取。
重跑即增量补齐(已存在的文件跳过)。
"""
import os, re, sys, json, ssl, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(ROOT, "assets", "icons")
os.makedirs(ICON_DIR, exist_ok=True)

# ---- 收集域名 ----
def read(p):
    try:
        with open(os.path.join(ROOT, p), encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("读不到", p, e); return ""

text = read("links.js") + "\n" + read("ai.js") + "\n" + read("index.html")
domains = set()
for m in re.finditer(r'(?:icon)?[Dd]omain"?\s*:\s*"([^"]+)"', text):
    d = m.group(1).strip().lower()
    if d and "." in d and " " not in d:
        domains.add(d)
domains = sorted(domains)
print("发现域名:", len(domains))

# ---- 下载 ----
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) icon-fetch"}

def sources(d):
    return [
        "https://www.google.com/s2/favicons?domain=%s&sz=64" % d,
        "https://icon.horse/icon/%s" % d,
        "https://icons.duckduckgo.com/ip3/%s.ico" % d,
    ]

def fetch(d):
    path = os.path.join(ICON_DIR, d + ".png")
    if os.path.exists(path) and os.path.getsize(path) > 100:
        return (d, True, "skip")
    for url in sources(d):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
                data = r.read()
            if data and len(data) > 100:
                with open(path, "wb") as f:
                    f.write(data)
                return (d, True, url.split("/")[2])
        except Exception:
            continue
    return (d, False, "")

ok, fail = [], []
with ThreadPoolExecutor(max_workers=12) as ex:
    for d, good, src in ex.map(fetch, domains):
        (ok if good else fail).append(d)

print("成功:", len(ok), "| 失败:", len(fail))
if fail:
    print("失败域名:", ", ".join(fail))

# ---- 写清单 icons.js ----
manifest = {d: 1 for d in sorted(ok)}
with open(os.path.join(ROOT, "icons.js"), "w", encoding="utf-8") as f:
    f.write("// 本地图标清单——build_icons.py 自动生成。值为 1 表示 assets/icons/<domain>.png 存在。\n")
    f.write("window.NAV_ICONS = " + json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("已写 icons.js（%d 个本地图标）" % len(manifest))
