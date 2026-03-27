# Signal & Structure Site

Standalone GitHub-ready repository export for the Signal & Structure website and publishing pipeline.

## Purpose
This repo contains the source content, brand assets, build scripts, and generated site output for the Signal & Structure static site.

## Cloudflare Pages Settings
- Framework preset: None
- Build command: `python3 pipeline/build_site.py && python3 prepare_cloudflare_pages.py`
- Output directory: `site`

## Main folders
- `content/` source markdown
- `assets/` brand assets
- `pipeline/` build/export scripts
- `site/` generated static site output
