#!/usr/bin/env python3
"""Export both language pages for static hosting or local QA."""
import re
import shutil
from preview import ROOT, load_site, render_html

output = ROOT / '_public'
output.mkdir(exist_ok=True)
config = load_site()
profile = config['data']['profile']
base = config.get('baseurl') or ''
for lang in ('en', 'zh'):
    html = render_html(lang)
    prefix = './' if lang == 'en' else '../'
    html = re.sub(r'\s*<link rel="(?:canonical|alternate)"[^>]*>', '', html)
    html = re.sub(r'\s*<meta property="og:(?:url|image)"[^>]*>', '', html)
    html = html.replace('href="' + base + profile['cv'] + '"', 'href="' + prefix + 'files/Haikang_Diao_CV.pdf"')
    html = html.replace('href="' + base + '/"', 'href="' + prefix + 'index.html"')
    html = html.replace('href="' + base + '/zh/"', 'href="' + prefix + 'zh/index.html"')
    path = output / ('index.html' if lang == 'en' else 'zh/index.html')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
(output / 'files').mkdir(exist_ok=True)
shutil.copyfile(ROOT / profile['cv'].lstrip('/'), output / 'files/Haikang_Diao_CV.pdf')
(output / '_redirects').write_text('/about/ / 301\n/about.html / 301\n', encoding='utf-8')
print('Upload this folder:', output)
