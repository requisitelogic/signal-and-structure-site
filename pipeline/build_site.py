#!/usr/bin/env python3
from pathlib import Path
import html

BASE = Path('/home/brandon/.openclaw/workspace/business/signal-and-structure')
CONTENT = BASE / 'content' / 'pages'
SITE = BASE / 'site'
SITE.mkdir(parents=True, exist_ok=True)

STYLE = """
body { font-family: Arial, Helvetica, sans-serif; margin: 0; color: #1c1f26; background: #f8fbff; }
.wrap { max-width: 980px; margin: 0 auto; padding: 32px 24px; }
.card { background: #fff; border: 1px solid #dce6f0; border-radius: 16px; padding: 28px; margin: 18px 0; box-shadow: 0 8px 24px rgba(10,25,40,0.04); }
h1,h2,h3 { color: #123b64; }
p, li { line-height: 1.6; }
ul { padding-left: 20px; }
.hero img { max-width: 100%; border-radius: 16px; box-shadow: 0 12px 32px rgba(18,59,100,0.08); }
"""


def md_to_html(md: str) -> str:
    parts = []
    in_list = False
    for raw in md.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            if in_list:
                parts.append('</ul>')
                in_list = False
            continue
        if s.startswith('# '):
            if in_list:
                parts.append('</ul>')
                in_list = False
            parts.append(f'<h1>{html.escape(s[2:].strip())}</h1>')
        elif s.startswith('## '):
            if in_list:
                parts.append('</ul>')
                in_list = False
            parts.append(f'<h2>{html.escape(s[3:].strip())}</h2>')
        elif s.startswith('### '):
            if in_list:
                parts.append('</ul>')
                in_list = False
            parts.append(f'<h3>{html.escape(s[4:].strip())}</h3>')
        elif s.startswith('- '):
            if not in_list:
                parts.append('<ul>')
                in_list = True
            parts.append(f'<li>{html.escape(s[2:].strip())}</li>')
        else:
            if in_list:
                parts.append('</ul>')
                in_list = False
            parts.append(f'<p>{html.escape(s)}</p>')
    if in_list:
        parts.append('</ul>')
    return '\n'.join(parts)


for md_file in CONTENT.glob('*.md'):
    body = md_to_html(md_file.read_text(encoding='utf-8'))
    out = SITE / (md_file.stem + '.html')
    page = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{md_file.stem}</title><style>{STYLE}</style></head><body><div class="wrap"><div class="card">{body}</div></div></body></html>'''
    out.write_text(page, encoding='utf-8')
    print('Built', out)
