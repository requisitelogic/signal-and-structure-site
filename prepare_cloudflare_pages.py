#!/usr/bin/env python3
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent
SITE = BASE / 'site'
SITE.mkdir(parents=True, exist_ok=True)

# Ensure index.html exists from home.html
home = SITE / 'home.html'
index = SITE / 'index.html'
if home.exists():
    shutil.copy2(home, index)

# Copy brand assets into site root for static deployment
for name in ['brand-logo.png', 'brand-hero.png']:
    src = BASE / name
    dst = SITE / name
    if src.exists():
        shutil.copy2(src, dst)

# Basic redirects/helper page for convenience
about_src = SITE / 'about.html'
product_src = SITE / 'product-it-project-steering-committee-kit.html'

about_dir = SITE / 'about'
product_dir = SITE / 'products' / 'it-project-steering-committee-kit'
about_dir.mkdir(parents=True, exist_ok=True)
product_dir.mkdir(parents=True, exist_ok=True)

if about_src.exists():
    shutil.copy2(about_src, about_dir / 'index.html')
if product_src.exists():
    shutil.copy2(product_src, product_dir / 'index.html')

headers = SITE / '_headers'
headers.write_text('''/*\n  X-Frame-Options: SAMEORIGIN\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n''', encoding='utf-8')

print(f'Prepared {SITE}')
