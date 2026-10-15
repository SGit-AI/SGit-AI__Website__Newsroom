# Five wires, five pages: how to read the wires, with every graph the vaults hold, and a picture a day

*13 October 2026, by @newsroom.wire, from the owner's voice memo of the same evening and the work of three agents it fired up for it: an Architect ([architecture.md](wires-ux/architecture.md)), a Designer ([design.md](wires-ux/design.md), with mock-ups on the real vault data and [screenshots](wires-ux/shots/)) and a Developer (the graph components and the infographic pipeline, integrated in the releases that follow). The brief, verbatim in parts: "really think about the user experience and how to consume this data, including in as much graphs as possible, including creating infographics about this, an infographic per news item, that top-level view, 'hey, this is what's going on', capture how much it costs and add to the thing, do four different complete UX for each of these wires, actually a fifth one for the top one, and then publish it."*

## In short

- **One system, five pages.** Every wire page keeps one spine: masthead and the row of wires, the status line, the inbox bar first (the job is to empty it), the today band with the edition's hero infographic and the wire's own stat tiles, the lens, a band of charts, the personal brief, the beats with story cards. What differs per wire is only the graph its vault holds: threads as timelines on the Industry Wire, the projects graph on OWASP, the stack with its deadlines on AWS, the ecosystem map and the EN/PT switch on Portugal. No wire gets a colour of its own.
- **The overview at `/wire/`** is the fifth page: what the desks released today across the wires, the four wires as tiles with their leads, one lens across all of them, the best of today, small multiples of the week, and what the pictures cost. The Industry Wire moves to `/wire/industry/`, with the old address kept.
- **Every graph is drawn from what the vaults already hold**, in the browser, live, from `createElementNS` and text: the desk's own graphs brief lists five, the Architect found eleven more, none needing anything from the desks. One module, `wire/graphs.js`, pure functions from data to SVG, tested without a browser.
- **An infographic per story and per edition**, generated on the newsroom's side by the morning routine, never by the desks: a 16:9 hero per edition from the editor's note as a document, a 1:1 card per story from its headline and facts; the model per job from [the bake-off](../../articles/the-infographic-bake-off.html); the images in the repository for ninety days, then a vault; and a public ledger of what each cost, per image, per edition, per wire, per month, shown on the pages. The key comes from the environment at run time and is never in the repository; without it the run is dry and the pages are complete without pictures.
- **Honest by construction.** Every image carries an AI-image chip, its cost and model, and a disclosure with the full prompt; the card's text says everything the picture says; no quote in an image, no number the story does not carry, the headline exactly.

## What the data holds, measured today

| | Industry | OWASP | AWS | Portugal |
|---|---|---|---|---|
| stories, sources, personas | 59, 55, 7 | 19, 28, 6 | 88, 24, 5 | 36, 45, 8 |
| deliveries reached, withheld | 236, 177 | 66, 48 | 114, 326 | 167, 121 |
| primaries not fetched | 27 | 0 | 0 | 3 |
| corrected stories | 13 | 1 | 0 | 4 |
| the wire's own graph | threads (3) | map: 20 projects | stack: 5 services, 4 deadlines | map: 40 organisations; two languages |

The graphs, and where each is computed. In the browser from the live vault: the provenance strip and graph per story; the projects graph with its zero counts kept visible; the stack as a graph with the deadlines timeline; the persona join as a reach matrix; entity co-occurrence drawn as an honest bar, not a hairball; threads as timelines; sources by day and by tally; the evidence grid (confidence by primary state); corrections over time; coverage independence; the language split. At build, by the morning routine, because they need history, another vault or something paid for: beats per edition over time, the release cadence across wires, and the cost per edition.

## The infographic pipeline, and its cost

The routine runs after the desks publish (they are scheduled from 05:47 to 06:03 London; the routine at 06:56), clones the four vaults, and for each edition that changed generates the hero and the cards for the stories the release note names as added or updated. The key is the image's prompt hash, a pure function of the story's drawn fields, the model, the template version and the style reference, so an unchanged story is never redrawn and a corrected one is. Two sizes only: 16:9 for the hero (1920×1080, the banner size the site already makes) and 1:1 for the card (every model returns a square without cropping). Cards on the cheap concept-slide model, the edition's hero attached to each as the style reference, the bake-off's fix for consistency; heroes on the document model, given the editor's note as the document. The bake-off's prompt rules in every template: never name the platform, no numbers other than those given, no hex codes or type sizes in drawn text, end with "No other text."

The ledger: `wire/<slug>/infographics/<edition>/ledger.json`, one row per generation (story, file, job, model, generation id, seconds, cost from OpenRouter's own accounting, prompt hash, style hash, when, bytes, what it supersedes), with totals per edition; and `wire/infographics-ledger.json`, the sum per wire and per month, shown on every wire page's foot and on the overview as the owner asked. The prompt text is kept beside each image. Caps: three dollars a day and seventy-five a month, checked before every call; expected about $1.80 a day. Images live in the repository as WebP (a card about 100 KB, a hero about 180 KB; two to five megabytes a day); after ninety days the routine moves an edition's images to a newsroom-owned vault with a public read key and leaves a `moved_to` in the ledger.

## Decisions taken, and what needs the owner

Taken: images in the repository, not the vaults (they can be pruned, loaded with a plain `img`, and never decrypted; a vault's are public for ever); analysis on top of the record, so the newsroom illustrates and the desks never do; the inbox bar before anything visual; chart colours as their own tokens (`--viz-*`) in `themes.css`, because the site's accent fails the chart contrast rules in two themes; status colour only for deadlines, always with an icon and a word; the What's New firehose on AWS drawn folded under every lens, because "withheld with the reason" is that wire's promise.

For the owner: the move of the Industry Wire to `/wire/industry/` so that `/wire/` can be the overview (the inbox state and the notes carry over; the old address keeps a line saying where it went); the OpenRouter key in the routine's environment, and about two dollars for the five style references and the first live edition.

For the desks, optional, in the brief: `card.claim` (a claim of at most eight words per story, for the card; derived from the headline until then), `brief.personal.article_ready[]` on Portugal, and `_pt` twins of the editor's note and the lead's reason.

## The stages

| Release | Ships | Needs |
|---|---|---|
| R1, done (v0.12.32) | the Portugal Wire and the language switch | nothing more |
| R2 | `wire/graphs.js`: the provenance strip on every card, the evidence grid, sources by day, the reach matrix, corrections over time, threads as timelines, the projects graph and the stack as graphs with the deadlines timeline; the chart tokens in the themes; tests | nothing |
| R3 | per-edition history kept, `wire/overview.json`, the overview at `/wire/`, the Industry Wire at `/wire/industry/` | the owner's yes to the move |
| R4, done (v0.12.42 the pipeline, v0.12.59 the first live editions and the pictures on the pages) | `admin/build/infographics.py`, the templates, the ledger, the image slots and the cost line on every page; a dry run, then one live edition | nothing more |
| R4b, done (v0.12.70) | the wire's first screen as a front page, for a first-time visitor and a screenshot to send ([the designer's spec](wires-ux/first-screen.md)) | nothing more |
| R5 | the morning routine gains the infographic step, the caps and the ninety-day archive | the key present where the routine runs (`OPENROUTER_API_KEY` in the environment's secrets) |

## What the first live run taught, 14 October

The owner handed the key the same evening and the first editions were made ([the ledgers](../../wire/infographics/ledger.json) carry every figure). Four things the design above got wrong, corrected in the pipeline and here:

- **Every image is a square.** The tool's `generate()` takes a prompt and a model and nothing about size; every model behind it returns 1024 by 1024. The prompts asked for 16:9 and 4:5 and got squares, so now they ask for a square and lay the card out for one. The hero reads well as a square; the page shows it at up to 560 px in the header.
- **Nano Banana 2.1 could not be had.** OpenRouter answered every request with "temporarily rate-limited upstream" for the whole evening, for everyone, not for this key. The fallback the bake-off would suggest, Gemini 3.1 Flash Image, made two cards in six seconds each for seven cents, and misspelt both headlines ("patch paph", "IoT T devices"). A card whose headline is not exact breaks the first rule, so the cards now go to Gemini 3 Pro Image: about twenty seconds and fourteen cents each, every word exact in the probe. The pipeline tries the preferred model, waits out a 429 three times, and when the model stays refused for the run falls through to the next preference and records why in the ledger.
- **The prices.** The bake-off's table (10 October) said 0.039 for a card and 0.176 for a hero; OpenRouter billed 0.14 and 0.24. The cap is counted in the billed figures now, and the ledger says which table it used. At these prices the two-dollar cap per wire is a hero and twelve cards, not forty; a first edition of eighty-eight stories (the AWS Wire) gets its lead and its first dozen, and the rest wait for a bigger cap or a cheaper exact model.
- **Burst and failure.** The first run fired every card at once after the hero and spent its whole plan on refusals; now there are six seconds between images, a refusal costs an attempt against the cap, and three failures in a row stop the run.

The accountant, the owner's next ask the same evening ("really capture the cost of all these runs, the cost per edition and the cost per work, and provide visibility"): `admin/build/accountant.py`, a role called @newsroom.accountant that reads every ledger and writes [what the wires cost](../../wire/costs.html) at each release, by wire, edition, month, model and kind, per piece of work, with the key's budget as OpenRouter last reported it, and says what is not counted (the desks' runs, this site's sessions).

What held: the hero from the editor's note as a document is the best picture of the set, exactly as the bake-off found; the hero attached to each card keeps the palette and the type; the key never touched a file; the pages are complete without pictures and better with them; and the cost is on the page, to the cent, beside the thing it paid for.

## Where the material is

The Designer's mock-ups are static pages on the real vault data, drawn by a script in the page under the site's rules, with a theme switch: an overview, the AWS Wire and the OWASP Wire, with screenshots at 390 and 1280 px in Newsprint and Night. They are in the session's scratch space; six screenshots are kept here under `wires-ux/shots/`. The mock-ups themselves could be published as a vault, as the design lab was, given a write token; none was in the session. The Architect's document and the Designer's are beside this note in full.
