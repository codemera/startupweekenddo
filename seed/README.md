# Seed for the new startupweekend.do

Everything worth keeping from the old Django/Mezzanine site (last commit
`58b8811`, October 2017), gathered in one place so the new site can be built
from scratch. The old code is still in the repo and in git history for
reference.

| File | What it holds |
|---|---|
| `site.yml` | Name, domain, timezone, brand colors and fonts, social links, Mailchimp form, old URLs, license |
| `content-model.md` | Content types (events, sponsors, people, schedule, FAQ, blog, press), page rules, old bugs, where the real data lives |
| `text/startup-weekend.md` | The only real page prose in the repo ("¿Qué es Startup Weekend?") |
| `text/ui-strings.yml` | Every hardcoded heading, label and button, by page |
| `images/` | All images from the repo; verdicts below |

## Images

All 16 image files in the old repo are copied here. Whether each one is needed:

**Use as-is**

| File | Notes |
|---|---|
| `favicons/*` (7 files) | Startup Weekend flask icon on teal. No co-branding, so it doesn't go out of date |
| `illustrations/jumbotron.png` | 1349×689 hero art: Santo Domingo skyline and palm trees on teal. The one locally specific image |
| `illustrations/post-default-image.png` | 720×400 flask on teal; fallback for posts without a featured image |

**Needed, but replace before launch**

These say "Powered by Google for Entrepreneurs", a program Google renamed to
Google for Startups in 2018. Get current Startup Weekend / Techstars logos and
swap them in; keep these as the reference for size and placement.

| File | Used for |
|---|---|
| `brand/logo.png` | 500×86 header logo (Startup Weekend + Techstars lockup, gray) |
| `brand/logo-white.png` | 500×86 footer logo (white version) |
| `brand/fb-share-img.png` | 1200×630 social share image |
| `press-kit/sw-negro.png`, `sw-color.png`, `sw-blanco.png` | 600×254 downloadable logos on the press-kit page |

**Optional**

| File | Notes |
|---|---|
| `brand/codemera-logo.png` | 220×22 white "Desarrollado por Codemera" footer credit. Keep only if the credit stays |

**Not copied:** `favicons/manifest.json` and `favicons/browserconfig.xml`.
They're config files with the old `/static/` paths, and any favicon generator
recreates them (theme color `#49bab7`).

## Missing: not in git

The site's real content was entered through the CMS, so it lives in the old
production database and `media/` folder, not in this repo:

- every event (dates, cities, venues, registration links, descriptions, videos,
  participant counts) and its banner and logo
- sponsors and their logos
- facilitators, coaches, judges, organizers and collaborators, with photos and bios
- event schedules
- FAQ questions and answers
- blog posts and their images
- homepage header and about text
- press photos and press-release files
- `metodologia.png`, the methodology graphic on the Startup Weekend page

The old server appears to be gone, which makes the Wayback Machine the only
source left: browse `https://web.archive.org/web/*/startupweekend.do/*` for the
`/eventos/<slug>/`, `/blog/` and `/startup-weekend/` pages. Expect text and
small images; full-size uploads are often missing from the archive. Past
organizers and sponsors may still have photos and logos.

## Building on Lovable

The new site will be built and hosted on Lovable. To use this seed there:

- Start the Lovable prompt with `content-model.md` and `site.yml`: they
  describe the pages, content types, rules, brand and integrations.
- Put the images in the project's `public/` folder and map `brand.colors` and
  `brand.fonts` into the Tailwind theme.
- Events, sponsors, people, schedules and FAQ fit as database tables (Lovable's
  Supabase integration) or, for a start, as static data files.
- The newsletter can stay a plain form that POSTs to `newsletter.form_action`.
- Keep the old URLs (`/eventos/<slug>/` and the rest) as routes or redirects.

The only pages in the old seed data were placeholders ("Content goes here",
lorem ipsum), apart from the Startup Weekend page, so nothing else was worth
copying.
