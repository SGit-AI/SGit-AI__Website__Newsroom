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


---

# v0.6.2: the synthetic-readers study, finding by finding

Five invented readers drove a browser through v0.6.1 on 10 October 2026 and found 31 things. The study
is a vault, <https://newsroom.sgit.ai/demos/vaults/newsroom-synthetic-users/index.html>, opened with its
published read key; its headline numbers (62 steps, 51 questions, 56 confusions, 31 findings, 6 blocking,
and every row of the per-reader table) were re-counted from its own run records and hold. The readers are
model-written and it is not user research.

**Verdicts.** FIXED: this repo's, done in v0.6.2. PARTLY: the part that was this repo's is fixed, the rest
is not. SGIT.AI: the page is imported and is fixed there, then re-synced. DECISION: needs a person, not
a fix. NOT A DEFECT: checked. Page paths are as the reader saw them.

| # | Severity | Finding | Verdict | Detail |
|---|---|---|---|---|
| 1 | blocking | No way to contact anyone about a pilot (`/replicate/`) | DECISION | The article invites sites to test the meter. The only address published anywhere (`agent@riskmandate.ai`) is described on the subscribe page as the agent that runs the mailing list. Who takes pilot enquiries is Dinis's. |
| 2 | blocking | Nothing shows real money moving (article) | SGIT.AI | True: no payment link is set, and `/shipped/` says so. The article could say the same. |
| 3 | blocking | Install assumes a developer (`/meter/`) | SGIT.AI | Five file paths, ES modules, no download or hosted-platform note. A product and writing decision. |
| 4 | blocking | No paragraph a writer could give readers (`/meter/`) | SGIT.AI | |
| 5 | blocking | How the writer gets paid is not clear (`/meter/`) | SGIT.AI | Balances live in the reader's browser; the page does not say what the writer sees. |
| 6 | blocking | Top-up says simulated while asking for money (`/account/top-up.html`) | SGIT.AI | Follows from brief decision 3: the Stripe link is not created. |
| 7 | worth fixing | Balance £4.97 in the top bar, £4.49 on the card | NOT A DEFECT | The card is a picture, `pv-card.webp`, with the author's balance baked in. Chip and card agree at every depth in a fresh browser and under the study's reopen-and-jump pattern, here and on sgit.ai. A picture of the card is still indistinguishable from the card: label it or crop the balance. The drift £4.99 to £4.92 is the meter charging by scroll depth, by design. |
| 8 | worth fixing | Three version numbers for one site | PARTLY | Fixed: the edition line is this site's release; a byline says "sgit.ai v0.7.36"; the markdown twins say the same. The article's own sentence "v0.7.39 today" is sgit.ai's. |
| 9 | worth fixing | The practical answer sits behind the story (article) | SGIT.AI | |
| 10 | worth fixing | First phone screen does not say what the site is or that the £5 is free (`/`) | SGIT.AI | The front page and the meter chip. The chip is a published component version that does not change; a label would be a new version. |
| 11 | worth fixing | Balance drops silently as the reader scrolls | SGIT.AI | By design; explained on the account page, two taps away. |
| 12 | worth fixing | Article opens as a tag cloud and a wall of italics; hero unreadable on a phone | SGIT.AI | |
| 13 | worth fixing | Insider terms: personas, streaks, roles, "edition from sgit v0.7.39" | PARTLY | The edition wording was added here in v0.6.0 and is gone. Personas and streaks are the meter's. |
| 14 | worth fixing | No route from the front page to the meter's install steps | PARTLY | Every page's nav has Replicate, then SG Meter, since v0.6.0. The front page is sgit.ai's. |
| 15 | worth fixing | Balance chip disappears on `/replicate/` | FIXED | Every page this site writes carries the chip, as a free page. |
| 16 | worth fixing | Byline names one human; the AI authorship is in the footer | SGIT.AI | `/shipped/` now says who is who; the byline is sgit.ai's template. |
| 17 | worth fixing | No approval step, and an unclear Editor (`/newsroom/`) | PARTLY | `/shipped/` now says the Editor is an agent role and Dinis Cruz holds editorial responsibility. The how-it-runs page is sgit.ai's. |
| 18 | worth fixing | The corrections page is an argument, not a policy; no way to report an error | PARTLY | `/shipped/` says plainly there is no published route. The route itself is a DECISION. |
| 19 | worth fixing | Pages contradict each other on what runs (`/about/participant.html`) | FIXED | The card said "Nothing here runs". The "v0.7.4" is the byline of the lead article, the sgit.ai release it was published in; it read "site v0.7.4" and now reads "sgit.ai v0.7.4" (see 8). |
| 20 | worth fixing | Evidence image fails; "real" against "fictional" (lead article) | PARTLY | The image is fixed. The caption's wording is the article's. |
| 21 | worth fixing | 51 of 527 figures missing | FIXED | Larger than measured: 117 figures and 2 thumbnails on 13 pages, 0 now. |
| 22 | worth fixing | Top-bar balance is not labelled as credit | SGIT.AI | Same as 10. |
| 23 | worth fixing | "Credit can go below zero" reads as a debt (`/account/`) | SGIT.AI | |
| 24 | worth fixing | "How it works" leads to a developer manual | SGIT.AI | |
| 25 | worth fixing | A penny is taken on opening a page with no notice | SGIT.AI | By design; no notice at the point it happens. |
| 26 | minor | The account page explains the meter clearly | n/a | A positive finding: the reassurance is two taps from where the worry starts. |
| 27 | minor | Eleven views, no "start here" subset (`/meter/`) | SGIT.AI | |
| 28 | minor | Balance falls while reading; the rating card looks pre-answered | SGIT.AI | |
| 29 | minor | Blank white page after Back | NOT A DEFECT | Reproduced as the loader's fade-in: blank for about 0.3 seconds, not a lasting blank. |
| 30 | helper artefact | The page jumps backwards while scrolling | NOT A DEFECT | As the study labelled it. |
| 31 | helper artefact | Taps on Latest open the wrong article | NOT A DEFECT | As the study labelled it. |

## Why the images were missing, and what reads them now

sgit.ai's authoring contract forbids a declarative `<img src>`. A figure is
`<figure class="shot" data-shot="x.webp" data-dir="../demos/vaults/v/images/">`, and `assets/shots.js` sets
`img.src = data-dir + data-shot` when the page opens; a card thumbnail is `data-trail-img`. The import treated
`href`, `src` and `data-src` as addresses and not these, and so did the gate. Two things followed. The 51 vault
images were never copied. And the front page copied to `/` kept `data-dir="cards/"`, which resolved to `/cards/`.
The import now treats `data-dir` and `data-trail-img` as addresses, copies every file the moved pages point at
that is outside the moved tree (52 files, each recorded with the pages that need it), and gate checks 2b (every
figure and thumbnail exists) and 2c (every script loaded at run time exists) read what check 2 could not.
Measured in a browser with every figure forced to load: v0.6.1 had 117 figures and 2 thumbnails not rendered
on 13 pages; v0.6.2 has 0 of 625.

## 11 October, v0.7.0: the live newsroom, tightened, and links to a persona

The newsroom is taking readers now, so the pieces of the meter that did not suit a live product came out and the
site was read as a stranger would read it.

- **Imported again** from sgit.ai v0.7.45 (v0.7.40 before): five articles (72 in all, 328 pages), among them
  *No server, by design*, which now carries the design page's "no server" row and the top-up page's data note.
- **The meter is this site's own build, v1.4.0**, a copy of v1.3.1 at its own immutable path
  (`assets/components/sg-meter/v1/v1.4/v1.4.0/`) with three changes: no Pause the meter, no Start again, and the
  landing view. Imported pages load it through a recorded import rule (item 11 in `sync_newsroom.py`), which stops
  the import if sgit.ai moves the component, so the fork cannot drift quietly. sgit.ai still runs v1.3.1.
- **Persona links** (`admin/build/personas.py`): `/persona/`, `/persona/<id>/` for the five starting personas,
  `/persona/#<id>`, and `/persona/links.json` for whoever writes the email. The first step of
  [a link to a persona](../../articles/a-link-to-a-persona.html), with no vault. The persona is added as a visitor
  the reader can keep or remove; nothing is charged for opening it.
- **Wording that named the removed buttons**, as recorded text rules: the personas page, the security model's shared
  computer row, the component documentation's account row. Also the account page's "Every page on sgit.ai" and its
  price table, which named sgit.ai's docs and vaults.
- **Test**: `admin/build/test_meter.mjs`, sgit.ai's meter test extended for all of the above (Playwright;
  skips when it is not installed).

## 11 October, v0.8.0: reading lists in a link

Part one of [From me to you, in a link](../../articles/a-reading-list-in-a-link.html), built as the brief says.

- **A number for every article** (`articles/ids.json`, `admin/build/ids.py`): assigned once, in publication order, never
  changed or reused, with a gate (check 12). The import prints the number at the foot of each article through a
  recorded rule (item 12 in `sync_newsroom.py`).
- **`/for/`** opens a list from the part of the link after the `#`; **`/for/make.html`** makes and previews one, reading
  its own link back through the recipient's parser. The code is `for/reading-list.js` and `for/make.js`, tested by
  `admin/build/test_lists.mjs`. A list opens as a visitor persona (named "Steve's list, from Dinis") using the meter's
  existing public calls, so there is no new meter version.
- **Not done**: the synthetic recipient the brief asks for, which needs a model and a browser run together; signed
  lists; paying for someone else's reading. The agent brief (part two) belongs to the RiskMandate agent: it needs
  `articles/ids.json` and the link format on `/for/`.

## 11 October, v0.8.1 to v0.8.3: the sync, the map, the lab

- **v0.8.1**: sgit.ai v0.7.61 imported (five articles, 75 to 79) and sgit.ai's page for publishers at `/publishers/`.
- **v0.8.2**: phase 0 of [Go slow to go fast](../../articles/explorer-to-villager-newsroom.html): `/newsroom-api/`,
  the map of the reader code with before-hashes, controls, inputs, outputs and contracts, and the review with 18
  findings, each bug pinned by `admin/build/test_review.mjs`; the generated note is
  `2026-10-11__newsroom-api-map-and-review.md`. CI runs the browser tests before a tag (the one change).
- **v0.8.3**: `/passkey/`, the lab for [The passkey opens the vault](../../articles/the-passkey-opens-the-vault.html):
  a passkey with PRF, the door derivation written out, sgit's keys, a recovery code, test vectors against sgit's
  Python, and the door created on a vault server with an access key. Not a feature; what-runs says so.

## Things for Dinis

1. **A contact for pilots** (finding 1). It needs an address and a commitment, and I would rather not choose
   either.
2. **Model identifiers.** The brief says "model identifiers must not appear on the site" and also that each
   imported article's text must match sgit.ai's. 76 imported pages name a model version, almost always in the
   AI-disclosure line (one model's full identifier and display name on 48 of them, another's on 28), including the
   study page. To list them: search the imported pages for a model identifier. Both rules
   cannot hold. Either sgit.ai changes its disclosure line and the pages are re-synced, or the brief's rule is
   about the byline only. I have not carried sgit.ai's house-style gates into this site's gate for the same reason:
   this one would fail on 76 pages as published.
3. **An article that names the removed button.** *Who will game the reading meter* says "Start again" on the account
   page clears a shared browser. The article is as published on sgit.ai and an article's text is not edited here, so
   it is left. The fix is a line in sgit.ai's article (and sgit.ai's own v1.3.1 meter still has the button), or a
   decision that this newsroom may carry a correction note.
4. **sgit.ai and this site now run different meters.** v1.4.0 here, v1.3.1 there. If sgit.ai should follow, v1.4.0 is
   a small diff against v1.3.1 and can be published there at the same path.
