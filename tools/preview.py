#!/usr/bin/env python3
"""Render the Jekyll homepage as a portable, offline HTML preview.

Install once: python -m pip install -r tools/preview-requirements.txt
Run: python tools/preview.py --open
This renders the same Liquid layout/data/CSS as Jekyll; it does not build other pages.
"""
from pathlib import Path
import argparse
import base64
import datetime
import mimetypes
import re
import webbrowser

try:
    import yaml
    from liquid import Environment, StrictUndefined
except ImportError:
    raise SystemExit('Install preview dependencies first:\npython -m pip install -r tools/preview-requirements.txt')

ROOT = Path(__file__).resolve().parent.parent

def render(output=None):
    config = yaml.safe_load((ROOT / '_config.yml').read_text(encoding='utf-8'))
    data = {name: yaml.safe_load((ROOT / '_data' / (name + '.yml')).read_text(encoding='utf-8'))
            for name in ('profile', 'publications', 'news', 'honors', 'experience')}
    # Match Jekyll’s optional-field defaults while keeping other fields strict.
    for paper in data['publications']:
        paper.setdefault('author_note', '')
    config.update(data=data, time=datetime.datetime.now())
    env = Environment(undefined=StrictUndefined)
    html = env.from_string((ROOT / '_layouts/academic.html').read_text(encoding='utf-8')).render(site=config)
    css = (ROOT / 'assets/css/academic.css').read_text(encoding='utf-8')
    html = re.sub(r'<link rel="stylesheet"[^>]+>', lambda _: '<style>\n' + css + '\n</style>', html)
    photo = ROOT / data['profile']['photo'].lstrip('/')
    photo_url = (config.get('baseurl') or '') + data['profile']['photo']
    mime = mimetypes.guess_type(photo)[0] or 'image/jpeg'
    image_uri = 'data:' + mime + ';base64,' + base64.b64encode(photo.read_bytes()).decode('ascii')
    html = html.replace('src="' + photo_url + '"', 'src="' + image_uri + '"')
    # A file:// preview has no website root. Keep the existing public CV link usable.
    origin = config['url'].rstrip('/')
    html = re.sub(r'href="(/[^\"]*)"', lambda m: 'href="' + origin + m[1] + '"', html)
    if '{%' in html or '{{' in html:
        raise ValueError('Unrendered Liquid markup remains')
    path = Path(output) if output else ROOT / '_preview/homepage-preview.html'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
    return path.resolve()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--open', action='store_true', help='Open the generated HTML in your default browser')
    parser.add_argument('--output', help='Optional output path')
    args = parser.parse_args()
    result = render(args.output)
    print('Preview created:', result)
    if args.open:
        webbrowser.open(result.as_uri())
