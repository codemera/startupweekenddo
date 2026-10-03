# Content model

What the old site stored and how it behaved, taken from
`startupweekenddo/models.py`, `views.py` and the templates at commit `58b8811`.
Use this as the spec for the new site's content types. It is not a schema to
copy field for field.

## Event

One Startup Weekend edition. URL: `/eventos/<slug>/`.

| Field | Notes |
|---|---|
| title, slug | e.g. "Startup Weekend Alpha" → `startup-weekend-alpha` |
| start_date | required |
| end_date | optional in the old model; make it required (see bugs below) |
| city | required, e.g. "Santo Domingo" |
| location | venue name, optional |
| registration_url | required; external sign-up link (the "Inscríbete" button) |
| about | rich text, shown as "¿Qué es {event}?" |
| youtube_video_id | optional |
| banner | optional; cropped to 2000×1200 (5:3); hero background |
| logo | optional; cropped to 400×400 |
| participants | number; adds up to the homepage counter |
| published | draft/published |

Each event also has the related lists below.

### Sponsors

name, logo (cropped 500×400), url (optional), tier. One name per event.

Tiers, in display order: **Diamante, Platino, Oro, Plata, Bronce, Media
Partner**. Empty tiers are hidden.

If you import an old DB dump, note that the stored tier numbers do not follow
display order: Oro = 0, Diamante = 1, Platino = 2, Plata = 3, Bronce = 4,
Media Partner = 5.

### People

Every person has a name, a photo (cropped square 300×300, shown at 225×225), a
`visible` flag and belongs to one event. Roles:

| Role (old model) | Shown as | Extra fields |
|---|---|---|
| Facilitator | Facilitador | bio (≤500 chars), twitter handle (name links to it) |
| Mentor | Coaches | bio, position |
| Judge | Jueces | bio, position |
| Organizer | Organizadores | manual sort order |
| Collaborator | Colaboradores | none |

Bios were shown as a tooltip on the photo.

### Schedule

A list of items per event: date and time, title, description (optional).
Grouped by day in America/Santo_Domingo, one collapsible panel per day; each
item shows its time (12-hour) and title.

## FAQ

Question categories (name, order) → questions (question, rich-text answer,
order). Shown on `/startup-weekend/` grouped by category.

## Blog ("Novedades")

Mezzanine's built-in blog: title, slug, author, publish date, featured image,
rich-text content, categories. URL: `/blog/<slug>/`.

## Press kit

- **Logos:** static files (see `images/press-kit/`).
- **Press photos:** a gallery of images, each with a description.
- **Press releases:** title, downloadable file, date added, published flag.
  Newest first; only published ones are shown.

## Homepage content

Editable fields used when no event is upcoming: header (rich text over the
jumbotron), about (rich text), video ID and video description. Only the newest
record was used.

## Rules

- **Next event:** the published event with the earliest start date that has
  not ended yet (start date ≥ today, or today falls between start and end).
  "Today" is in America/Santo_Domingo.
- **Homepage:** if there is a next event, the homepage becomes that event's
  page: hero with Inscríbete / Más Información, video and about, schedule,
  facilitator, coaches, judges, organizers, collaborators, sponsors, then
  "Otros Eventos". Otherwise it shows the static homepage: header, about, the 3
  latest blog posts, video, counters and the 6 latest events. Both versions end
  with the newsletter form.
- **Counters:** number of published events, sum of participants, number of
  distinct cities.
- **Events list:** two tabs. "Próximos Eventos" holds events that have not
  ended; "Eventos Pasados" holds the rest.
- **Event page:** the registration buttons and the about/video section only
  show while the event has not ended.
- **`/startup-weekend/`:** page text, the 3 latest events, the FAQ, then the
  newsletter form.

## Bugs in the old code (don't port)

- The "cities" counter counted events, not distinct cities.
- Events with no end date never appeared under past events, and the event page
  crashed for them once their start date had passed.
- An event ending today appeared in both the upcoming and past tabs.

## Where the real data is

None of the following is in git. It lives in the old production database and
its `media/` folder:

| Data | DB table(s) | Media folder |
|---|---|---|
| Events | `startupweekenddo_event`, `pages_page` | `media/event/banner/`, `media/event/logo/` |
| Sponsors | `startupweekenddo_sponsor` | `media/sponsors/` |
| People | `startupweekenddo_person` + `_facilitator`, `_mentor`, `_judge`, `_organizer`, `_collaborator` | `media/person/` |
| Schedules | `startupweekenddo_schedule`, `startupweekenddo_scheduleitem` | none |
| FAQ | `startupweekenddo_questioncategory`, `startupweekenddo_question` | none |
| Homepage content | `startupweekenddo_homepagedata` | none |
| Press releases | `startupweekenddo_pressrelease` | `media/press_releases/` |
| Press photos | `galleries_gallery`, `galleries_galleryimage` | `media/galleries/` |
| Blog | `blog_blogpost`, `blog_blogcategory` | `media/uploads/` (featured images) |
| Page text and inline images | `pages_richtextpage` | `media/uploads/` (e.g. `metodologia.png`) |

The old server appears to be gone, so this data can't be exported. What's left
of it is in the Wayback Machine's snapshots of `startupweekend.do`
(`https://web.archive.org/web/*/startupweekend.do/*`). If a copy of the
database or `media/` ever turns up, export it with:

```sh
./manage.py dumpdata startupweekenddo pages blog galleries \
  --natural-foreign --indent 2 > swdo-dump.json
tar czf swdo-media.tgz media/
```
