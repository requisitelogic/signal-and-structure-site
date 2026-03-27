# Signal & Structure Publishing Pipeline

## Purpose
Create a repeatable local publishing workflow for product pages, site pages, launch posts, and storefront exports.

## Workflow
1. Author content in markdown under `content/`
2. Store brand/media assets under `assets/`
3. Generate publishable HTML under `site/`
4. Generate storefront/email/social export files under `exports/`
5. Publish manually or connect later to a host/storefront

## Folder Roles
- `content/pages/` → website pages
- `content/products/` → product descriptions and product-page source
- `content/posts/` → social/blog/newsletter source
- `content/emails/` → launch and outreach emails
- `assets/brand/` → logos and hero graphics
- `assets/downloads/` → downloadable product zips and packaged assets
- `site/` → generated website pages
- `exports/storefront/` → Gumroad/Lemon Squeezy-ready copy
- `exports/email/` → launch email exports
- `exports/social/` → post-ready exports

## Suggested Next Evolution
Later, connect `site/` to a static host like Netlify, Cloudflare Pages, or Vercel.
