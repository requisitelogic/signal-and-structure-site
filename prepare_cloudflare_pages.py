#!/usr/bin/env python3
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent
SITE = BASE / 'site'
ASSETS = BASE / 'assets'
SITE.mkdir(parents=True, exist_ok=True)

# Prefer branded root landing page if present
root_index = BASE / 'index.html'
if root_index.exists():
    shutil.copy2(root_index, SITE / 'index.html')
else:
    home = SITE / 'home.html'
    if home.exists():
        shutil.copy2(home, SITE / 'index.html')

for name in ['brand-logo.png', 'brand-hero.png']:
    src = ASSETS / name
    dst = SITE / name
    if src.exists():
        shutil.copy2(src, dst)

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
