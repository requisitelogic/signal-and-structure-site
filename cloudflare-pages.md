# Cloudflare Pages Deployment Guide - Signal & Structure

## Recommended Host
- **Cloudflare Pages**

## Source
This site is generated from local markdown/content and exported into:

- `business/signal-and-structure/site`

## Deployment Model
Use a static-site deployment.

## Recommended Cloudflare Pages Settings
### Framework preset
- **None**

### Build command
```bash
python3 business/signal-and-structure/pipeline/build_site.py && python3 business/signal-and-structure/prepare_cloudflare_pages.py
```

### Build output directory
```bash
business/signal-and-structure/site
```

## Current Pages Included
- `/` → homepage
- `/about/` → about page
- `/products/it-project-steering-committee-kit/` → product page

## Static Assets Included
- `brand-logo.png`
- `brand-hero.png`

## Notes
- The current site is intentionally small and static.
- Cloudflare Pages is a good fit because no backend is required yet.
- Gumroad can be layered in later for product checkout and delivery.

## Suggested Next Step After Deployment
- connect a custom domain
- add storefront/payment links
- add analytics
- add a second product page
