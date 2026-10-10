# The newsroom move: phase 0 note, the content audit, and milestone 1

10 October 2026, site v0.6.0. Written by the Claude Code session that maintains newsroom.sgit.ai,
for Dinis Cruz. It answers the brief at
<https://sgit.ai/docs/briefs/newsroom-move-to-newsroom-sgit-ai.html> (its Phase 0 deliverable is
"a short note in the repository listing the plan, collisions, and decisions needed") and records
the content audit asked for on the same day: decide, brutally, what stays as this site's content
and what becomes dated history.

## The ask, in one line

newsroom.sgit.ai becomes a professional site: the newsroom experience first (reading, the reader's
own account, customisation and paying), then the design it came from, then everything needed for
someone else to run one. Everything this site published on the way stays, dated, as history.
Milestone 1: the home page looks like sgit.ai's `/articles/`.

## What was decided

| Brief decision | State |
|---|---|
| 1. Homepage | **Decided by Dinis on 10 October**: the newsroom front page at `/`. Done in v0.6.0. |
| 2. Meter storage key | Not decided. The import keeps `sgit.meter.v1`, because it carries sgit.ai's config unchanged. localStorage is per origin, so nothing collides; a reader's data still does not move without the import page (Phase 3). |
| 3. Stripe Payment Link | Not created, and not this session's to create. When it is, its redirect should be `https://newsroom.sgit.ai/account/topped-up.html?session_id={CHECKOUT_SESSION_ID}`. Until then no money moves, and the site says so on `/shipped/`. |
| 4. SG Meter docs | Moved with the newsroom, at `/meter/`, as the brief recommended. Easy to reverse. |
| 5. Name | "SGit Newsroom", unchanged. |

## How the move works: import first, port later

This is the explorer-to-villager step, done in that order on purpose.

**Now (villager):** the newsroom's pages are *imported*, not rebuilt. sgit.ai still publishes
articles every day, and its newsroom is built by a 680 KB `build_pages.py` that also builds the
rest of sgit.ai. Porting that generator now would mean two generators drifting while one of them
keeps publishing. Importing the built pages makes "each article's text matches sgit.ai" true by
construction, and the brief already says "sync from sgit.ai as needed; do not edit moved content
on the new side".

`admin/build/sync_newsroom.py --from <sgit.ai checkout>` copies the brief's "what moves" tree to
the same paths and changes only this:

1. A relative link resolves to one of three places: a path that moved (stays relative), a path
   this site has its own version of (`index.html`, `llms.txt`: stays relative, now means this
   site's), or anything else, which is sgit.ai's and becomes `https://sgit.ai/<path>`.
2. `https://sgit.ai/<moved path>` becomes `https://newsroom.sgit.ai/<path>`: canonical URLs,
   og:url, og:image, JSON-LD, the feed, the wire.
3. sgit.ai's stylesheet arrives as `assets/newsroom.css` (see collisions).
4. The page loader no longer loads sgit.ai's site chat (see collisions).
5. The front page is written to `/` as well as `/articles/index.html`, re-based one level up, and
   both name `/` as canonical.
6. The site's name in the metadata (tab title, og:title, og:site_name, JSON-LD) becomes the SGit
   Newsroom, and the front page takes the newsroom's own title and description (v0.6.1).

Links are rewritten in real tags only, never in a code sample (v0.6.1 corrects v0.6.0, which
changed SG Meter's install snippet). Checked across all 312 pages: the visible text is identical to
sgit.ai's apart from the edition line, and the meter config is byte-identical on every page.

Scripts, styles, the meter component and `/.well-known/sgit-subscribe.json` are copied **byte for
byte**; the sync refuses to run if any would change. 647 of 1,274 files are identical to source.

The record of the import is `admin/build/newsroom-sync.json`: source commit, sgit.ai version, and
two SHA-256 per file (as sgit.ai serves it; as imported, with this site's nav, footer and version
stamp set aside). **validate.js check 11** recomputes the second for every file, so editing an
imported page here fails the build. The sync also refuses to overwrite any file it did not write
itself, except the pages listed in its `REPLACES`, and only once `archive.py` holds a dated copy.

**At cutover (town planner):** the generator moves here and is extracted as it moves, and this
site becomes the publisher. That is Phase 5 and needs both sessions.

## Collisions found

| Path | What happened |
|---|---|
| `/newsroom/index.html` | The brief's named collision. This site's design page ("roles and operations") is now `archive/2026-08-23-newsroom-roles-and-operations.html`, and sgit.ai's backstage owns `/newsroom/`. The brief suggested `/design/newsroom.html` with a forward; a forward from `/newsroom/` is impossible once the backstage lives there, and the page is a design the backstage overtook, so it went to the archive. |
| `/index.html`, `/index.md` | This site's home page, copied to `archive/2026-08-22-home.*`; the front page took the address. |
| `/shipped/index.html` | Said "nothing on this site is running yet", which stopped being true. The August text is copied to `archive/2026-08-23-what-is-shipped.html`; the address now carries the current line. |
| `assets/site.css` | Both sites have one; this site's is used by 130 pages and their generators. sgit.ai's arrives as `assets/newsroom.css`, and the loader in each imported page is told the new name. |
| `assets/site-chat.js` | Not imported. It is sgit.ai's site chat over sgit.ai's own content index; here it would answer questions about the wrong site. |
| `llms.txt`, `llms-full.txt`, `index.html` | Local equivalents: an imported page's link to them means this site's. |
| `admin/versions.html`, `about/` | Not equivalents: an article's "site v0.7.36" or byline link means sgit.ai's, so it goes to `https://sgit.ai/...`. |
| `sgit_rk1_` | An imported article version quotes a read key in sgit's first key format. sgit.ai's own credential checker classifies the prefix as read-only, so the tripwire names it alongside `sgit_public_read_`. Precise, not looser. |
| The freshness check | Imported pages compare their baked sgit.ai version with `/version.txt` on sgit.ai's host. Left naming sgit.ai, so it is inert here; pointing it at this host would reload every page against the wrong version number. |
| No collision | `account/`, `subscribe/`, `meter/`, `og/`, `assets/components/`. |

## The content audit

Before v0.6.0: **130 pages**. After: **446**. Of the 130:

- **53 stay live** as this site's own content.
- **75 are archived in place**: same address, a dated note at the top saying when, why, and
  what overtook them, out of the main navigation, listed at `/archive/`.
- **2 addresses were taken by the import** (`/` and `/newsroom/`), with dated copies in `archive/`.

The test for each page: does something now run that does what this page argued for? If so, the
running thing is the content and the page is history. If not, the page is still the design and
stays, labelled as design. Nothing was deleted.

### Stays live (53)

| Section | Pages | Why it stays |
|---|---|---|
| `/thesis/` | 1 | The core concept: sell the graph. |
| `/corrections/` | 3 | The concept, its one worked case (10,000 hours), the mechanism. |
| `/provenance/` | 3 | The concept, articles as vaults, the decision graph: still designs, still the argument. |
| `/economics/` | 2 | Paying the fact creator, trust as a service: the argument the meter has only begun to test. |
| `/rights/` | 1 | CC-Signed: a design, and the World News Day licence finding makes the case for it. |
| `/databases/` | 3 | The no-server constraint, with consoles that run. |
| `/shipped/` | 1 | Rewritten: the current line between running and designed. |
| `/world-news-day/` | 33 | A running instance, a published vault, and the place the outreach will send 21 authors. |
| `/mvps/seed-companies.html` | 1 | Business templates published to be copied: on-mission for "replicate". |
| `/about/`, `/network/`, `/admin/` | 5 | The disclosure, the network, how the site is built, release history, comms. |

### Archived (75 in place + 3 copies)

| What | Pages | Written | Overtaken by |
|---|---|---|---|
| The home page, the "what is shipped" page, the newsroom design | 3 copies | Aug 2026 | The front page; the rewritten `/shipped/`; the running backstage |
| The Governance Wire | 19 | 28 Aug | One research run, verification never built; its method runs in World News Day and the newsroom |
| Portugal Startups | 24 | 13 Sep | The event is over; the beat is pt.newsroom.sgit.ai |
| pt.newsroom home-page designs | 2 | 13 Sep | pt.newsroom.sgit.ai exists |
| The MVPs as specified, the Portugal instance as specified | 2 | 25 Aug | Built differently, or not at all |
| Design pages the newsroom overtook: show your work, the £8.40 story, the long economics page, the rails, 242 papers, staleness in the wild, agenda is context | 7 | 23 Aug | The backstage; real article numbers; the reading meter; the concept pages that remain |
| The brief pack and research briefs | 19 | 21 Aug to 14 Sep | It is the origin record; sources stay in `briefs/` |
| The library, micro and nano payments | 2 | 2025 material | The newsroom's articles; the meter |

The table that drives this is `GROUPS` in `admin/build/archive.py`; the archive index is generated
from it, so the two cannot disagree.

### New (3 pages, in the newsroom's look)

- `/design/`: six ideas, each beside what runs and what does not yet. The hub for the
  philosophy and the architecture.
- `/replicate/`: what someone can copy today to run a newsroom like this, where it is, how far each
  piece is packaged, and what is not packaged yet (the generator; payments).
- `/archive/`: the archive index.

### The navigation, in the reader's order

Newsroom · Account · How it runs · Design · Replicate · World News Day · Archive · About.

The brief's order was the newsroom's own items, then "The design", then "The instances". Two
deliberate differences: the reader's account and the backstage are their own groups, because
customisation, paying and "how it runs" are what the ask puts first; and "The instances" became
the Archive plus World News Day, because three of the four instances it names are archived.

## Where the brief's phases stand

| Phase | State after v0.6.0 |
|---|---|
| 0. Inventory | This note. |
| 1. Articles exactly as they are | Done by import: 66 articles at their paths, markdown twins, version history, graphs (`graphs.json` has 66), views, images, cards, banners, OG images. The link checker passes. The build refusals (quote not in article, teaser over 160 characters, missing link target) run where the pages are built, on sgit.ai. |
| 2. The newsroom around them | Done by import: front page (same lead and highlights by construction), desk notes, collections, newsletter, backstage, roles, policies, board, log. The policy checker runs on sgit.ai, where the role files are. |
| 3. The reader account | Partly. SG Meter is at its versioned paths and works on every imported page (balance in the top bar, reader card, module by dynamic import). **Not yet:** the meter on this site's own pages, `/account/import.html`, and a run of `test_meter.mjs` here. |
| 4. Feeds and agents | Partly. feed.xml, wire.json, graphs.json and markdown twins are at their paths with canonical URLs here; llms.txt has a newsroom section; OG images are JPEG. **Not yet:** feed validation and a LinkedIn post-inspector check. |
| 5. Cutover | Both sessions. Not started. |

## What comes next

1. **Restyle the pages that stay** (the design concept pages, World News Day, the site pages) into
   the newsroom's look, so the whole site is one site. Today they keep the earlier look; only the
   newsroom and the three new hubs use the newsroom stylesheet.
2. **Phase 3 remainder**: the meter on this site's own pages, `/account/import.html`,
   `test_meter.mjs`.
3. **A sync routine**: re-run the import whenever sgit.ai publishes, until cutover.
4. **Decisions 2 to 5** above, which are Dinis's.
