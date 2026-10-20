#!/usr/bin/env python3
"""Render a portable bilingual preview from the production Liquid template.

Install once: python -m pip install -r tools/preview-requirements.txt
Run: python tools/preview.py --open
The preview switch works offline; published language pages work without JavaScript.
"""
from pathlib import Path
import argparse
import base64
import datetime
import json
import mimetypes
import re
import webbrowser
try:
    import yaml
    from liquid import Environment, StrictUndefined
except ImportError:
    raise SystemExit('Install preview dependencies first:\npython -m pip install -r tools/preview-requirements.txt')

ROOT = Path(__file__).resolve().parent.parent

def load_site():
    config = yaml.safe_load((ROOT / '_config.yml').read_text(encoding='utf-8'))
    data = {name: yaml.safe_load((ROOT / '_data' / (name + '.yml')).read_text(encoding='utf-8'))
            for name in ('profile', 'publications', 'news', 'honors', 'experience', 'i18n')}
    data['zh'] = {name: yaml.safe_load((ROOT / '_data/zh' / (name + '.yml')).read_text(encoding='utf-8'))
                  for name in ('profile', 'news', 'honors', 'experience')}
    for paper in data['publications']:
        paper.setdefault('author_note', '')
    config.update(data=data, time=datetime.datetime.now())
    return config

def render_html(lang='en', inline_assets=True):
    if lang not in ('en', 'zh'):
        raise ValueError('Language must be en or zh')
    config = load_site()
    env = Environment(undefined=StrictUndefined)
    html = env.from_string((ROOT / '_layouts/academic.html').read_text(encoding='utf-8')).render(site=config, page={'lang': lang})
    if inline_assets:
        css = (ROOT / 'assets/css/academic.css').read_text(encoding='utf-8')
        html = re.sub(r'<link rel="stylesheet"[^>]+>', lambda _: '<style>\n' + css + '\n</style>', html)
        photo_path = config['data']['profile']['photo']
        photo = ROOT / photo_path.lstrip('/')
        photo_url = (config.get('baseurl') or '') + photo_path
        mime = mimetypes.guess_type(photo)[0] or 'image/jpeg'
        image_uri = 'data:' + mime + ';base64,' + base64.b64encode(photo.read_bytes()).decode('ascii')
        html = html.replace('src="' + photo_url + '"', 'src="' + image_uri + '"')
    if '{%' in html or '{{' in html:
        raise ValueError('Unrendered Liquid markup remains')
    return html.lstrip()

def render(output=None, lang='en'):
    config = load_site()
    documents = {}
    for language in ('en', 'zh'):
        html = render_html(language)
        # Only the downloadable preview uses JS. Production uses two static URLs.
        html = re.sub(r'href="(/[^\"]*)"', lambda m: 'href="' + config['url'].rstrip('/') + m[1] + '"', html)
        documents[language] = {
            'body': re.search(r'<body>(.*?)</body>', html, re.S).group(1),
            'title': config['data']['i18n'][language]['title'],
            'description': re.search(r'<meta name="description" content="([^"]*)"', html).group(1),
        }
        if language == lang:
            initial_html = html
    payload = json.dumps(documents, ensure_ascii=False).replace('<', '\\u003c')
    script = '''<script id="preview-languages" type="application/json">PAYLOAD</script>
<script>
(function () {
  const pages = JSON.parse(document.getElementById('preview-languages').textContent);
  document.addEventListener('click', function (event) {
    const link = event.target.closest('a[data-language]');
    if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const language = link.dataset.language;
    const page = pages[language];
    const scrollY = window.scrollY;
    document.body.innerHTML = page.body;
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    document.title = page.title;
    const decoder = document.createElement('textarea');
    decoder.innerHTML = page.description;
    document.querySelector('meta[name="description"]').content = decoder.value;
    const section = window.location.hash && document.getElementById(window.location.hash.slice(1));
    if (section) section.scrollIntoView(); else window.scrollTo(0, scrollY);
    document.querySelector('a[data-language="' + language + '"]').focus({preventScroll:true});
  });
})();
</script>'''.replace('PAYLOAD', payload)
    html = initial_html.replace('</body>', script + '\n</body>')
    path = Path(output) if output else ROOT / '_preview/homepage-preview.html'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
    return path.resolve()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--open', action='store_true', help='Open the generated HTML in your default browser')
    parser.add_argument('--output', help='Optional output path')
    parser.add_argument('--lang', choices=('en', 'zh'), default='en', help='Initial preview language')
    args = parser.parse_args()
    result = render(args.output, args.lang)
    print('Preview created:', result)
    if args.open:
        webbrowser.open(result.as_uri())
