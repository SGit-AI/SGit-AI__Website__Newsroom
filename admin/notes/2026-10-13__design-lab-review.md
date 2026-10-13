# The Newsroom Design Lab, reviewed against v0.12.13

*13 October 2026, by newsroom.ux. A review of the handover from the Claude session that ran the Newsroom Design Lab on 11 October (the UX review, the kit, four published vaults, 162 screenshots), judged against the site as it is today, not the v0.6.4 to v0.7.1 it was built on. What is there, what has already been overtaken, what to take, and in what order.*

## What the lab is

Another agent session, 11 to 13 October, did three things in order: a UX review of newsroom.sgit.ai from the point of view of a contact arriving from a link (six roles, measured on the live site at v0.6.4); a brief for prototypes in SGit vaults, three design directions of everything, explored before anything touched the live site; and the prototypes themselves, built with a shared kit by a dev and an architect, each gated and published with a read key.

| Vault | Id | What it tries | Clone matches the zip |
|---|---|---|---|
| The lab (hub) | `3bf2p46v` | brief, directions, the map from review to prototype, seven decisions, the reviews | yes, v0.1.1 |
| Front page & personas | `m1m66ace` | the front page as the neutral persona, the first phone screen, the persona picker and mini-site, purpose, masthead, the split menu | yes, v0.1.1 |
| Article & reader primitives | `vdcj8hpl` | the article reordered, a short version first, Semaform blocks, the side column, highlights and notes, feedback that starts empty, ask the article, the reading board, the reader's record | yes, v0.1.1 |
| Findability | `xvq3z35u` | five desks by audience, 42 controlled tags, 11 series, linkable search, reading time and format on cards, the Librarian's audit | yes, v0.1.1 |

The three directions, in every vault: **A Broadsheet** (a serious paper, serif, warm), **B Briefing** (answers first, labelled blocks, phone-first), **C Your desk** (the reader's own newsroom: persona, board, notes). A top-bar switch and a Compare view at phone width. All four vaults open read-only in the SG/App host today (`https://dev.vault.sgraph.ai/#<read key with %3A>`), and `sgit clone <read key>` works with sgit-ai 0.21.0. The write keys were delivered separately and must not enter this repository; the gate's key-leak tripwire would refuse them.

## The quality of the work

High, and honest about itself. Every vault carries a REALITY file checked by a test, a BRIEF-CORRECTIONS file naming each deviation and deferral, and a sources file with the SHA-256 of the newsroom data it was built on. Nothing is lorem ipsum: it runs on the real `wire.json`, `persona/links.json` and the markdown twins, and everything the site does not have yet is labelled *Proposal* in the interface and kept in `data/proposals/*.json` so an editor can change it without code. The kit has an escaping template that refuses raw HTML, a gate that renders every route in every direction at 390 and 1280 with zero page errors and no sideways scroll, a contrast test over every theme block, and a budget on the bundle. The architect's review of the kit (`lab/reviews/architect-kit.md`) is a real review: 22 checks, defects reproduced before and after, and the open risks named.

Three things it measured that this repository should know and not re-discover:

- The vault host's CSP is `connect-src blob: data:`: `fetch()` to newsroom.sgit.ai is refused inside a vault app even though the newsroom sends `access-control-allow-origin: *`. Images and classic scripts from other origins do load. So a vault app carries a byte-faithful snapshot and reads live only when opened standalone.
- `localStorage` throws in the app frame; `sg.state` works and survives reload.
- Never assign `location.hash` in the host; the srcdoc frame re-navigates. Routes live in a variable, filters in the route path.

## What the site has done since, without the lab

The lab was built on v0.7.1. The site is at v0.12.13 and several of the review's asks arrived by another road, which changes what to take:

| The review asked for | What shipped since (release) | Gap left |
|---|---|---|
| Reader primitives on the article: status, notes, highlights, a board | The vault pane on every page: notes as you read, read later, not for me, more like this, Done; the reading tab; carried between devices by the reader's vault (v0.11.0 to v0.12.8) | No highlights of a selected passage; no board with four columns; no side column, the pane is a drawer |
| Feedback that reaches the newsroom | The lane: every note and decision is sent, encrypted, to the newsroom's append lane and read by `lane.py`; *Write to the newsroom* with Save and send (v0.12.0, v0.12.8) | Ratings themselves still live in the meter and are not sent one-tap; the lab's receipt and consent wording is better than the pane's |
| Ask the article | *Ask* the site: top passages to Chrome's built-in model or openrouter with the reader's key, cited (v0.12.9) | Per-article ask, with the Explainer's short version as context, is not built |
| Search over bodies, linkable filters | Search in the browser over every page, article, graph and the wire, BM25 (v0.12.7) | Filters are not in the address; no tag pages, no desks, no series; cards show no reading time or format |
| Persona links | `/persona/<id>` pages and `persona/links.json` (v0.7.0) | Only the founder, security and newsroom stories are written in the lab; the live persona pages are the meter's landing view, not a mini-site |
| The wire as an inbox, seen and decided | Shipped (v0.12.6, v0.12.8) | Not in the lab's scope |
| A theme | Five themes (v0.12.12) | The lab's two themes per direction are a different axis: direction is layout and type, theme is colour. Both can coexist |

Of the review's ten bugs, checked today on the built tree:

| Bug | Today |
|---|---|
| Articles on two domains, both canonical | Fixed: sgit.ai's copy of *Hope or enforcement* now declares the newsroom canonical |
| Stale edition label | Still true: the front page says *Edition of 2026-10-08* above articles dated 13 October. It is imported from sgit.ai, so the fix is upstream, or the sync's text rules |
| Version shown three times | Still true, now four occurrences on the front page (badge, agent chip, edition line, footer), all the same number since chrome.py unified them |
| £5 chip unlabelled | Still true: the balance pill has no title or label saying it is free credit |
| Ratings preselected on 3 | Fixed in the meter (v1.3.1 marks an untouched scale) |
| Unbranded 404 | Still true: no 404.html |
| Body hidden until JavaScript | Still true on imported pages (sgit.ai's opacity bootstrap) |
| Author tooling at the article foot | Fixed |
| Feed titled for the old site | Still true: `articles/feed.xml` is titled *sgit.ai articles* (imported) |
| Count drift | llms.txt and the front page now agree at 100 |

## What to take, in order

**1. The data, this week, not the code.** This is the lab's own advice and it is right. Four files in the findability vault are editorial work that does not exist anywhere else and would take the Librarian days to redo:

- `desks.json`: five desks by audience with a scoring rule, a start-here list of five per desk, and every one of 73 articles assigned (one primary, at most one secondary). Today one topic holds 38 of 73; the largest desk holds 18.
- `tags.json`: 339 raw tags reduced to 42 controlled ones in five groups, each with a scope sentence and the raw tags it absorbs; 40 rejected with a reason (format, product, too broad, one-off). Median tags per article from 11 to 4.
- `series.json`: 11 series found from *Builds on* chains and the desk notes, each with its order and dek (the reading meter in five, behaviour policy from argument to gate in four, where agents run in four).
- `formats.json`: a format label per article (field report, explainer, analysis, RFC, answer, how-to) with the rule that derived it.

Where they go: the newsroom's authoring side is sgit.ai's generator, so the honest target is `admin/content/` on sgit.ai (the catalogue and the wire are built there), or, until the generator moves here, a derived index this site builds and renders as pages: `/desks/`, `/tags/<id>.html`, `/series/<id>.html`, reading time and format on the cards in `search/`. The lab's `find/tools/derive_find.py` already does the derivation and its tests pin it. Each file should gain a `status` and a `target` field, as the architect proposed, so acceptance is a move and not a retype.

**2. The three persona stories and the purpose page.** `front/data/proposals/personas/{founder,security,newsroom}.json` are written in full (story, Dinis's note, start here, sections mapped to real slugs). `purpose.json` is the *Why this exists* page the site does not have: agenda and disclosure, licences, method, who it is for, the ask. `masthead.json` holds three heart lines; the current tagline describes a method and no subject. These are words, and words move for free.

**3. Three small live fixes from the review's bug list** that are this site's to make: a `404.html` with search and the doors; a label on the balance chip (*£5 free reading credit*, in the meter's balance view, v1.4.2); the feed title and the edition label are sgit.ai's and belong in the sync's text rules or upstream.

**4. The reader primitives the pane does not have yet**, taken from the article vault as patterns, not code: highlights kept as exact text and re-marked on render (`ar-reader.js`), a four-column board with keyboard and swipe, and the feedback block's consent and receipt wording (`feedback.json`). The pane already has the lane the lab only simulated, so this is the one place the live site is ahead and the lab's design is the better face for it.

**5. Decide the direction before porting any layout.** The hub's `#decisions` page holds seven decisions with options (direction, masthead line, doors, article top, feedback, desks, board), kept in the browser and downloadable as JSON. Nothing in the vaults should become the live front page until those are picked, and the lab says so itself. My reading of the screenshots, for what it is worth: Broadsheet is the most finished and closest to the site's existing voice; Briefing's *The news, Our view, The evidence, Room for disagreement* blocks are the strongest single idea because every block is sourced from something that already exists (the Explainer's short version, the article's *In short*, the vault links, the Historian's contradictions); Your desk is what the vault pane is becoming. The lab's own *Mix* option (A for the publication, C for a signed-in reader) is the one that matches where the site has gone since.

**6. The kit, selectively.** `nr-html.js` (the escaping template, `NR.url`, the safe markdown subset) has tests behind it and is worth adopting as a shared primitive; this site's `wire.js`, `vault-pane.js` and `search.js` each render with their own escaping. `NrBase` and the gate's render-every-route check are good patterns for any future vault app this site ships. The shell, the direction switcher and the compare view are lab furniture and should not move. The kit's two-theme-per-direction colour blocks are a separate axis from the five themes shipped in v0.12.12 and can be left where they are.

## What not to do

- Do not re-run the UX review's measurements as if they were current. Six of its ten bugs and three of its five "fix this week" items have moved. A fourth synthetic-user run against v0.12.13, which the review itself asks for, would be the right way to re-baseline.
- Do not port prototype code into the site before the decisions. The vaults are the place to decide and the evidence; the architect's path-to-live section says what moves (components served from the versioned path, tokens, the reader store) and what stays.
- Do not copy the vaults into this repository. They are published with read keys and clone in seconds; `admin/notes` should link them, which this note does.

## Where the material is

- The zip, extracted to the session's scratch space: `HANDOVER.md`, `lab/BRIEF.md`, `lab/reviews/architect-kit.md`, `lab/context/newsroom-ux-review.md` (6,200 words), the kit at v0.1.3, the four vault sources, 162 screenshots named `<route>__<direction>__<width>.webp`.
- The vaults, live: read keys in the hub's `data/vaults.json` and in the handover.
- The decisions: hub `#decisions`; the review map: hub `#map` (26 items, 22 prototyped, 4 partial, 2 not in scope).
