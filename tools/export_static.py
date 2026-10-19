#!/usr/bin/env python3
"""Export the homepage for direct upload to Netlify/Cloudflare, without GitHub."""
from pathlib import Path
import re
import shutil
import yaml
from preview import ROOT, render

output = ROOT / '_public'
output.mkdir(exist_ok=True)
path = render(output / 'index.html')
html = path.read_text(encoding='utf-8')
config = yaml.safe_load((ROOT / '_config.yml').read_text(encoding='utf-8'))
profile = yaml.safe_load((ROOT / '_data/profile.yml').read_text(encoding='utf-8'))
# No deployment hostname is assumed; add canonical/social URLs after choosing a host.
html = re.sub(r'\s*<link rel="canonical"[^>]*>', '', html)
html = re.sub(r'\s*<meta property="og:(?:url|image)"[^>]*>', '', html)
old_cv = config['url'].rstrip('/') + (config.get('baseurl') or '') + profile['cv']
assert old_cv in html
html = html.replace('href="' + old_cv + '"', 'href="./files/Haikang_Diao_CV.pdf"')
(output / 'files').mkdir(exist_ok=True)
shutil.copyfile(ROOT / profile['cv'].lstrip('/'), output / 'files/Haikang_Diao_CV.pdf')
path.write_text(html, encoding='utf-8')
(output / '_redirects').write_text('/about/ / 301\n/about.html / 301\n', encoding='utf-8')
print('Upload this folder:', output)
