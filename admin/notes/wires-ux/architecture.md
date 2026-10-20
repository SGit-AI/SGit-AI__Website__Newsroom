# The wires: consuming the data, the graphs, the infographics and the cost

*Architecture, 13 October 2026, by the Architect agent, for newsroom.sgit.ai's wires: the Industry, OWASP, AWS and Portugal wires and the overview at `/wire/`. From the owner's voice memo of today. Read against newsroom.sgit.ai v0.12.31 and the four vault clones. Saved by the lead from the agent's hand-back; the agent's own session could not write files.*

## A. The data model across the four wires

Every vault is one contract plus optional sections, and the page already tolerates their absence. Measured today:

| | Industry | OWASP | AWS | Portugal |
|---|---|---|---|---|
| stories / sources / personas | 59 / 55 / 7 | 19 / 28 / 6 | 88 / 24 / 5 | 36 / 45 / 8 |
| editions in the bundle | 2 (10-11, 10-13) | 1 | 1 | 1 |
| releases in releases.json | 3 | 3 | 2 | 2 |
| deliveries (reached / withheld) | 236 / 177 | 66 / 48 | 114 / 326 | 167 / 121 |
| primary_fetched false | 27 | 0 | 0 | 3 |
| stories with changes[] | 13 | 1 | 0 | 4 |
| wire block | none (the fixed six lenses) | yes, weekly | yes, daily items | yes, daily, languages ["en","pt"] |
| extra | none | map, 20 projects | stack, 5 services, 4 deadlines | map, 40 organisations; headline_pt, summary_pt, quote_lang, label_pt, sources lang |
| factcheck | per-story rows (10-11) | prose (10-13) | prose (10-13) | per-story rows, wire-factcheck/v1 |
| entity kinds | orgs people products tech cves | + events, standards | as Industry | + places |

The graphs the data already holds: the desk's GRAPHS.md lists five (provenance per story, the OWASP projects graph, the AWS stack, the persona join, the week as co-occurrence and threads timelines). The bundle holds more, none needing anything from the desks:

6. Sources by day: story.date × primary.publisher × tier; a stacked bar, one colour per tier, dashed for primaries not fetched.
7. Personas reached per story: the reach matrix, stories as rows, personas as columns; filled for reached with the top connection's weight, hollow with the withheld reason. 59×7 to 88×5: small enough to draw whole.
8. Corrections over time: every changes[].at, plus factcheck verdicts per date. The charter says corrections propagate; this shows they happen.
9. The evidence grid: confidence (high, medium, low) × primary state (fetched tier A/B/C/none, not fetched). The honest one-glance quality measure per edition.
10. Beats per edition over time: needs editions kept as history (section D).
11. Release cadence: releases[].at on a time axis with added/updated/withdrawn counts. Across wires, the overview's heartbeat.
12. Coverage independence: coverage count and distinct publishers per story.
13. The map's zero-count signal (OWASP: 8 of 20 projects named by no story): keep it visible.
14. Deadlines timeline (AWS): the dates, today's marker, red inside 30 days, the touched services beneath.
15. Language split (Portugal): sources 39 pt / 6 en; quote_lang per story.
16. Cost per edition, from the ledger (section C), and the month to date.

All computed from one bundle.json and one deliveries.json, so drawable in the browser from the live vault; only 10, 11 across wires and 16 need something the site keeps.

## B. The views: five pages, one code

Rule: a graph that needs only this vault's current files is drawn in the browser, live; one that needs history, another vault's data, or something paid for (an image) is computed by the morning routine into a static file beside the page, which the page reads first and the vault second.

```
/wire/            THE OVERVIEW (new): today across the wires
  industry/       The Industry Wire (moved from /wire/, redirect kept)
  owasp/ aws/ portugal/   each: index (edition as inbox + graphs + infographics), sources, how, reach,
                          snapshot.json, editions/<date>.json, infographics/<edition>/
  days.html, charter.html, desk-brief.html (exist)
```

Every wire page gets the same spine, each section present only when the bundle has what it needs:
1. The hero of the edition: the infographic from infographics/<edition>/hero.webp (built), the editor's note beside it as text; the note alone when no image exists.
2. The bar (exists): since last visit, releases, filters, lens.
3. The edition at a glance (browser): the evidence grid, sources by day for the window, the release cadence. Three small SVGs, text labels only.
4. The wire's own extra as a graph: the projects graph with its zero counts (OWASP), the stack with the deadlines timeline (AWS), the ecosystem map (Portugal). The site draws its own from data, never pasted SVG.
5. Threads as timelines: incidents above the line, responses below.
6. The stories by beat (exist), each card with the provenance strip, its reach chips, and its infographic card at the side when it exists, the headline as alt text.
7. The reach matrix and corrections over time, folded, at the foot, with the cost of this edition and of the month as the last line.

Per wire, what differs is config and data, not code: Portugal's language toggle; AWS's deadlines in the header and "N of M items touched your stack"; OWASP leading with the projects graph; Industry with the most history leading with beats over editions.

The overview at /wire/ needs four things no single vault has:
- Today's releases across wires: every releases[] entry dated today (or the latest per wire) with counts, one row per wire. Built into wire/overview.json each morning; live, the page re-reads each vault's small releases.json and marks what arrived since.
- A best-of: each wire's brief.lead with why_it_leads and its three threads, from the snapshots.
- The infographic of the day: one image across the wires, from the four editor notes and leads as a document.
- "For you" across wires: for the chosen lens, the stories that reached that persona on every wire, newest first, inbox counts summed; lens ids shared where personas share ids (dinis on all four; ai-builder, security-lead, founder on Industry and Portugal); deliveries.json read live, lazily, only when a lens is chosen; the same scoped state (slug:id).
Also: the four evidence grids side by side, the release cadence of all four on one axis, the month's cost per wire. The strip naming the wires becomes the overview's navigation.

## C. The infographic pipeline

Where it runs: the newsroom's morning routine, after the desks publish, the same script runnable by hand at release time. Not the desks: they hold no OpenRouter key; images in a public-read vault are public for ever and cannot be withdrawn, while the site can prune; and the charter puts analysis on top of the record, written by this side and marked as such. The newsroom reads, draws and now illustrates; it never writes to a wire's vault.

```
05:47 to 06:03  desks publish (one commit, one release entry each)
06:56           newsroom routine: clone ×4 → diff against snapshots
                  → snapshots + editions/<date>.json + overview.json
                  → infographics.py (key from OPENROUTER_API_KEY; absent = dry run)
                      per wire: hero (if the edition changed) + cards for added/updated stories
                      ledger.json beside the images; cap checked before every call
                  → wire.py, chrome, sitemap, validate, the tests → push to dev (patch release)
by 08:00        on the site
```

Jobs, one prompt shape each, following the bake-off:

| Job | Input | Model | Cost | Aspect | Style |
|---|---|---|---|---|---|
| Story card | headline, summary (first 60 words), why it matters, up to 5 entity names, date, beat. Never the quote (a tier-B or C quote in an image is a republication). | Nano Banana 2.1 | ~$0.04 | 4:5, 1080×1350 | the wire's style.png attached |
| Edition hero | the brief as a document: editor note, lead and why it leads, thread titles, counts | GPT-5.4 Image 2 | ~$0.20 | 16:9, 1920×1080 | the wire's style.png |
| Overview of the day | the four editor notes and leads as one document | GPT-5.4 Image 2 | ~$0.20 | 16:9 | the site's style.png |

Prompt shape, from a template per job, never hand-written per image: a one-line format ("Concept slide, portrait 4:5"), the wire's name as kicker, the headline as the only title, the facts as a short list, "Use exactly these words and no numbers other than those given", the style sentence without hex codes, and "No other text." Never name a platform. Consistency from attaching the wire's style reference (one slide-1 per wire, generated once and kept at wire/<slug>/infographics/style.png). Portugal's cards draw headline_pt as the title with the English headline as alt; its hero is generated in en and pt.

Avoiding regeneration: the image key is sha256(prompt text), a pure function of the drawn fields, the model, the template version and the style reference's hash; unchanged hash, skipped; a correction changes the hash, the image is redrawn and the old entry stays with superseded_by. Only stories named added or updated in the release note are considered. Hard cap per day: 40 cards and 6 heroes.

Where images live: the repository, WebP, wire/<slug>/infographics/<edition>/<story-id>.webp and hero.webp, ledger.json beside them. A 1080-wide card at quality 80 is 80 to 120 KB, a hero 150 to 200 KB; 20 to 40 images a day is 2 to 5 MB a day, 60 to 150 MB a month; the repository's .git is already 279 MB and the tree holds 225 MB of images; Pages serves up to 1 GB. So: a rolling 90 days in the repository, older editions' images moved with their ledger slice to one newsroom-owned infographics vault (public read key), a moved_to in the ledger. A vault is not the primary home: a plain img, cached by browser and CDN, not decrypted through the vault reader; LFS is not served by Pages.

The ledger, wire/<slug>/infographics/<edition>/ledger.json, one row per generation: schema wire-infographics/v1, edition, wire, images[] (story, file, job, model, generationId, duration_s, cost_usd, prompt_sha256, style_sha256, at, bytes, supersedes), totals (images, cost_usd, skipped_unchanged, dry_run). Also wire/infographics-ledger.json, the sum per edition, per wire and per month, shown at every wire page's foot and per wire on the overview. The prompt text kept at prompts/<story-id>.txt beside the images.

## D. The release flow with daily editions

Without a site release: everything read live reaches the pages within ref_ttl_s (120 s): stories, releases, corrections, factcheck rows, map and stack, and every browser-computed graph. A reader at 07:00 sees the 06:00 edition drawn in full before the routine has run.

Needing the routine: the snapshots; per-edition history wire/<slug>/editions/<date>.json (the snapshot's shape, kept rather than overwritten: graphs 10 and 11, and "editions as history" on this side); wire/overview.json; the infographics and the ledger; the search index. The routine releases only when a clone changed; the infographic step is one more builder in that run, and a step in the README's release order.

One codebase: wire.js keeps one entry point and data-wire kinds: edition, sources, how, reach, days, and overview. The graphs go in one module, wire/graphs.js, pure functions from data to SVG via createElementNS, text nodes only, no innerHTML, tested in Node. Optional sections stay optional by presence, now also a fetched infographics/<edition>/ledger.json (a 404 means no images). Per-wire differences stay in wire-vault.<slug>.json, gaining infographics: {cards, hero, languages}. wire.py writes the same pages for every config plus the overview; test_wire.mjs grows one block per graph and one for the overview.

Moving the Industry Wire from /wire/ to /wire/industry/ is the one migration: the inbox state is scoped by slug ('' today) and notes by path (/wire/). wire.js reads both the old and the new scope for the Industry Wire and writes the new; /wire/ keeps a canonical to the overview and a line saying the Industry Wire moved.

## E. Risks and limits

- Web access from the session: the infographic step needs dev.tools.sgraph.ai and openrouter.ai through the proxy, Chromium given the proxy explicitly. If refused, the step logs it, writes the ledger with dry_run and a reason, and the release proceeds without images. Never a failed release for a missing picture.
- The key: from OPENROUTER_API_KEY in the environment, never a file; the key-leak tripwire gains the sk-or-v1- prefix. Absent: dry run writes every prompt, the ledger shows 0, the page says "no infographic yet", alt text carries the headline.
- Cost caps: $3 a day and $75 a month, read from the ledger before every call; the routine stops at the cap and says so in the release note. Expected about $1.80 a day, about $55 a month.
- The vault host's CSP does not touch this site; the desks' apps can show the images with a plain img from newsroom.sgit.ai.
- Image sizes: 120 KB per card, 200 KB per hero, loading="lazy", width and height set, cards folded by default on phones.
- What an image may say: analysis on top of the record, labelled "AI-generated infographic, from the story's text". No quote; no number the story does not carry; the headline exactly. A wrong image is fixed by a `wrong` decision from the reader, turned into a regeneration with the correction in the ledger.
- Repository growth bounded by the 90-day rule and the vault archive.

## F. A staged plan

| Release | Ships | Needs |
|---|---|---|
| R1: the Portugal Wire | the config, /wire/portugal/, the language toggle, quote_lang, the ecosystem map; the days page gains the fourth vault | the read key (received) |
| R2: the graphs | wire/graphs.js: the provenance strip on every card, the evidence grid, sources by day, release cadence, the reach matrix, corrections over time, threads as timelines; the projects graph with zero counts; the stack and deadlines timeline; tests | nothing |
| R3: history and the overview | editions/<date>.json kept; wire/overview.json; /wire/ becomes the overview; the Industry Wire moves to /wire/industry/ with the scope migration | the owner's yes to the move |
| R4: infographics, dry run first | infographics.py, the templates, the ledger, the slots on every page and the overview, the cost line, the style references; once dry, then once live | the OpenRouter key in the environment; about $2 for the style references and the first live edition |
| R5: the morning run with pictures | the routine's prompt extended with the infographic step, caps, the 90-day archive, the monthly cost on the overview | the key present in that environment |

R1 and R2 in either order, R3 before R4, R4 before R5. From the desks: nothing beyond the Portugal key; every graph and image is drawn from what the contract already gives.
