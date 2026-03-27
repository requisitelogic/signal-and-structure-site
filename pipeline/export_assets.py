#!/usr/bin/env python3
from pathlib import Path
import shutil

BASE = Path('/home/brandon/.openclaw/workspace/business/signal-and-structure')
EXPORTS = BASE / 'exports'
(EXPORTS / 'storefront').mkdir(parents=True, exist_ok=True)
(EXPORTS / 'email').mkdir(parents=True, exist_ok=True)
(EXPORTS / 'social').mkdir(parents=True, exist_ok=True)
(EXPORTS / 'downloads').mkdir(parents=True, exist_ok=True)

copies = [
    (BASE / 'storefront-product-copy.md', EXPORTS / 'storefront' / 'it-project-steering-committee-kit-pro.md'),
    (BASE / 'sales' / 'outreach-email.md', EXPORTS / 'email' / 'outreach-email.md'),
    (BASE / 'launch-posts' / 'linkedin-post-01.md', EXPORTS / 'social' / 'linkedin-post-01.md'),
    (BASE / 'launch-posts' / 'linkedin-post-02.md', EXPORTS / 'social' / 'linkedin-post-02.md'),
    (BASE / 'products' / 'it-project-steering-committee-kit' / 'it-project-steering-committee-kit-pro.zip', EXPORTS / 'downloads' / 'it-project-steering-committee-kit-pro.zip'),
]

for src, dst in copies:
    if src.exists():
        shutil.copy2(src, dst)
        print('Exported', dst)
