# newsroom.sgit.ai: the SGit Newsroom

The SGit Newsroom: one page, one argument, with the figures, the data and the links to check
it. Since v0.6.0 (10 October 2026) this site is the newsroom first: the articles and the
reader's own account, then the design the newsroom came from, then everything needed to run
one like it. What it published before the newsroom ran is in `/archive/`, dated and kept at
its original addresses.

Live site: https://newsroom.sgit.ai (GitHub Pages, deployed from `dev`).

## Since v0.6.0

- `/` and `articles/`: **the newsroom**, imported from sgit.ai's built pages at the same
  paths by `admin/build/sync_newsroom.py` until cutover. Never edit these by hand: fix them on
  sgit.ai and re-sync. `validate.js` check 11 fails the build if an imported file changes.
- `admin/content/articles/`: **articles written here** (since v0.12.10), with their graphs in
  `graphs/` and figures in `images/`, in sgit.ai's authoring contract. `admin/build/publish.py`
  publishes them: it renders them with sgit.ai's generator in a temporary clone of a read-only
  checkout (nothing is pushed to sgit.ai), validates, and imports the result with the sync. Edit
  these sources, never the generated pages. The generator itself moves here in a later step. The guide to writing one, the voice, the shape and the run, is `admin/content/articles/README.md`.
- `admin/content/newsletter/`: **newsletter issues written here** (since v0.12.18), `NNN-YYYY-MM-DD.md`,
  in the format of sgit.ai's newsroom README, published by the same `publish.py` to
  `articles/newsletter/YYYY/MM/DD/NNN-<slug>.html` with a 1920x1080 cover. Issue numbers continue from
  sgit.ai's 001 to 005; `publish.py` refuses a number sgit.ai already has.
  An issue's LinkedIn post ends with its subscribe paragraph, which names newsroom.sgit.ai (sync
  item 15); the cover is the only image to upload, because the body's images copy and paste.
- `account/`, `subscribe/`, `meter/`: the reader's account, subscribe, and the SG Meter
  library (imported with the newsroom).
- `newsroom/`: how the newsroom runs: roles, behaviour policies, board, log (imported).
- `design/`: the ideas, each beside what runs and what does not yet (`admin/build/hubs.py`).
- `replicate/`: what someone can copy today to run a newsroom like this (`hubs.py`).
- `shipped/`: what runs, what is designed, dated (`hubs.py`).
- `persona/`: a link that opens the newsroom as a persona, one page each, and `links.json` (`admin/build/personas.py`).
- `wire/`: the Industry Wire, industry news read live in the browser from a public-read sgit vault that agents write to (`admin/build/wire.py`, `wire-vault.json`; code `wire/vault-reader.js`, `wire/wire.js`; test `admin/build/test_wire.mjs`, against the real vault). Read as an inbox (`admin/notes/2026-10-13__the-wire-as-an-inbox.md`): the desk writes a release note on every publish (`data/releases.json` in the vault, since 13 October 2026) and the bar shows the ones since the reader's last visit; a story the desk corrected carries its `changes`, dated, under its text. `wire/snapshot.json` is the vault at the last release, for agents without a browser; refresh it with `--from <clone>`. Since v0.12.14 there is more than one wire: `wire/owasp/` (the OWASP Wire, with a projects graph) and `wire/aws/` (the AWS Wire, filtered by a declared stack with its deadlines), and since v0.12.32 `wire/portugal/` (the Portugal Wire, in English and Portuguese with a switch, `wire.languages`), each with its own config `admin/build/wire-vault.<slug>.json` under the same contract and the same code, and its own snapshot (`--from <slug>=<clone>`); `admin/notes/2026-10-13__more-than-one-wire.md`. Since v0.12.20: `wire/charter.html` (from `admin/notes/2026-10-13__the-wires-charter.md`), `wire/desk-brief.md` (the standing brief for the desks, rendered too), `wire/days.html` (every wire by date), `wire/<slug>/reach.html` (who should know, by organisation route, from `admin/build/wire-reach.json` and the vault), `wire/subscribe.js` (one list per wire), and the verifier's `data/factcheck-*.json` drawn at the story. Since v0.12.42 the edition is also drawn as graphs: `wire/graphs.js` (SVG by `createElementNS`, text nodes only, every colour a theme token; a provenance strip under each headline, and folded in the header the stories per day by beat, the threads on a date axis, the entities two or more stories share; test `admin/build/test_graphs.mjs`), and `admin/build/infographics.py` makes one card per story and one hero per edition through dev.tools.sgraph.ai with a cost ledger (`OPENROUTER_API_KEY` from the environment only; without it, a dry run that writes the prompts and the plan); since v0.12.59 the images live under `wire/<slug>/infographics/<edition>/` with their ledger, and `wire/wire.js` draws the hero in the edition's header and a card beside its story, each with an AI-image chip, its model, its cost and the prompt on request; `admin/build/accountant.py` (@newsroom.accountant, called by `wire.py`) sums every ledger into `wire/costs.html` and `wire/costs.json`: by wire, edition, month, model and kind, per piece of work, and the key's budget as OpenRouter last reported it; since v0.12.74 every scheduled run is costed too (`admin/build/wire-runs.json`, written with `admin/build/runs_ledger.py`, shown on `wire/costs.html`), the newsroom's morning run reads the vaults with `admin/build/vault_fetch.mjs` (the site's own reader in Node, nothing to install), and the charter has rules for a wire about a person; since v0.12.70 the page opens as a front page (the masthead, the hero beside the editor's note, the threads folded, the lead; the desk's record folded; the plumbing at the foot; `?share` for a 1200 by 630 screenshot), the designer's spec in `admin/notes/wires-ux/first-screen.md`; the UX for the five pages is in `admin/notes/2026-10-13__five-wires-five-pages.md` and `admin/notes/wires-ux/`.
- `passkey/`: the passkey lab, proofs of concept for the passkey-opens-the-vault design (`admin/build/passkey_lab.py`, `passkey_vectors.py`; code `passkey/lab.js`; test `admin/build/test_passkey.mjs`). Its card 6 makes real vaults through `assets/newsroom-vault.js`, the newsroom's one module over the vault library that runs dev.vault.sgraph.ai, vendored unedited at `assets/vendor/sg-vault/v0.2.3/` (`VENDOR.md` records the upstream commit and every hash; the validator checks them) with one local extension in `assets/vendor/sg-vault/local/`. `admin/build/test_vault.mjs` runs that library against a mock of the vault API (`admin/build/vault-mock.mjs`) and through an `sgit clone`, `commit` and `push` round trip with sgit-ai 0.21.0.
- `newsroom-api/`: the map and review of everything a reader runs, regenerated by `admin/build/api_map.py`; its findings are pinned by `admin/build/test_review.mjs`.
- `for/`: a reading list in a link, and the page that makes and previews one (`admin/build/lists.py`; the code is `for/reading-list.js` and `for/make.js`). `articles/ids.json`: a stable number for every article (`admin/build/ids.py`).
- `vault/`: your vault, in four tabs: the notes you keep as you read and the lane that carries the ones you send to the newsroom; every page read in this browser, with its decision; the reading account carried between devices; every key of the account (`admin/build/vault_page.py`). The pane itself is `assets/vault-pane/` (`vault-pane.js` the UI, `notes.js` the notes as records, `reading.js` what the meter's records say about a page, `pending.js` what is only in this browser, `wire-state.js` what was seen on the wire, `sync.js` the sync logic as pure functions), injected on every page with the meter by `chrome.py`; the door derivation is `assets/door.js`; the lane in `assets/newsroom-vault.js`. The newsroom reads a lane with `NEWSROOM_LANE_KEY=<read key> python3 admin/build/lane.py` (the key from the environment, never a file). Open with the passkey, or connect with a link and only send; which device a browser is, asked after the open; what the vault holds brought in on its own: `admin/notes/2026-10-13__open-or-connect-a-vault.md` (card 059). The inbox (card 049): `assets/vault-pane/inbox.js` (the key pair, the link, the envelope, the append routes, the QR code with the vendored `assets/vendor/qrcode-generator/`), `assets/vault-pane/send.js` and `vault/send.html` (the sending side, for a browser without the passkey); the design is `admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md` and the test `admin/build/test_inbox.mjs`. Designs: `admin/notes/2026-10-12__the-activity-vault.md`, `admin/notes/2026-10-12__the-feedback-loop.md`. Tests: `admin/build/test_sync.mjs` (Node), `test_pane.mjs` (two devices in Chromium against the mock) and `test_notes.mjs` (the feedback loop end to end, including the sgit CLI reading the lane).
- `search/`: search in the browser. `admin/build/search_index.py` writes `search/docs.json` and `search/text.json` from every page in the sitemap, the article graphs and versions, the wire's snapshot and the notes; `assets/search/search.js` ranks them in the page (BM25 over fields and paragraphs); the nav links it from every page. Run it after the first `gen_sitemap.py`. *Ask* (`assets/search/ask.js`) gives the top passages to Chrome's built-in model, or to openrouter.ai with the reader's own key, to answer from and cite. Design: `admin/notes/2026-10-13__search-in-the-browser.md`. Tests: `admin/build/test_search.mjs`, `admin/build/test_ask.mjs`.
- `assets/themes/`: **the five themes** (since v0.12.12): `themes.css` defines every colour token in every theme (Newsprint, the default; Night; Paper; Blueprint; Ember) and shadows the imported stylesheet's literal colours; `themes.js` sets `data-theme` on `<html>` before the first paint and draws the picker in the bar; `README.md` is the design guidance (a stylesheet names a colour through a token, defined there in all five). `assets/site-nav.css` is the bar's layout in both looks. `chrome.py` loads all three first in the nav block of every page. Test: `admin/build/test_themes.mjs` (every token in every theme, no literal colour outside the themes file, the picker and its memory, 4.5:1 contrast in every theme, the bar on one row at 1280 and up). Pictures: `admin/build/shots_themes.mjs`. Design: `admin/notes/2026-10-13__five-themes-and-the-bar.md`.
- `about/newsroom-ux.html`: the page of the agent that writes here under its own name (`admin/build/agents.py`); an article's `author_url` points at it.
- `engineering/`: the issues and the releases, rendered by `admin/build/engineering.py` from `admin/engineering/` (the Issues-FS-lite layout: `issues/open|blocked|done/NNN-slug.md` cards with front matter, a Gherkin scenario, a mock-up and an outcome; `releases/vX.Y.Z.md`; the convention in `admin/engineering/README.md`). Every change is connected to a card; version rows name the ids. Every push is a patch release.
- `archive/`: the index of everything archived (`admin/build/archive.py`, whose `GROUPS`
  table decides what is archived and why).
- `world-news-day/`: a running instance, built by its own `world-news-day/build/`.

The plan, the collisions with sgit.ai, and the content audit behind all of this are in
[`admin/notes/2026-10-10__newsroom-move-and-content-audit.md`](admin/notes/2026-10-10__newsroom-move-and-content-audit.md).
The other notes are the reader API's map and review (`2026-10-11__newsroom-api-map-and-review.md`, generated) and the passkey
finding that a door is per path, not per passkey (`2026-10-12__one-door-per-passkey-path.md`).
The structure list below is the site as it was built in August and September; most of
those sections are now archived.

## Structure

- `index.html` — **the front page, this site's own since v0.12.60, in three views** (`admin/build/front.py`): Broadsheet, Briefing and Your desk are all in the page; `data-view` on `<html>` shows one, set by `assets/front/front.js` before the first paint from what the browser remembers (`newsroom.view`; `?view=briefing` opens one directly, which is how an A/B test sends readers to a view). The views are the Newsroom Design Lab's three directions on this site's tokens (`assets/front/front.css`, tokens only). The editor's words are `admin/content/front/` (the masthead: "Pay for what you read."; the door lines, the publishers' door, the lead when the editor names one; otherwise the newest article leads). Your desk is filled from the meter's and the pane's local records: the balance, the spend, a status per pick, the progress bar, the board; the chooser changes the meter's active persona. `index.md` is the twin; `articles/front.json` the data. `about/index.html`, "Why this exists", comes from `admin/content/front/purpose.json`. Test: `admin/build/test_front.mjs`.
- `desks/` — the five desks, each an audience (`admin/build/desks.py`), from `articles/find.json`, which `admin/build/find.py` derives from the wire, the articles' markdown twins and the editor's `admin/content/find/find-editorial.json`: a primary and secondary desk, controlled tags, series in order, a format and a reading time for every article. A raw tag the editor has not mapped is listed under `unmapped`, never fatal.
- `assets/reader/` — the reading strip (`strip.css`, `strip.js`), injected by `chrome.py` on every page with the meter and running where the page is charged: a hairline that fills as the reader goes down the page, and a chip with how far, what this page cost and what is left, from the meter's records.
- `admin/notes/sgit-ai-dependencies.md` — what the site still takes from sgit.ai, by kind (`admin/build/deps.py`); the rule is that the newsroom is self-contained and the one link it keeps outside itself is to a vault.
- `thesis/` — the thesis: sell the graph, evidence not truth, the author is the oracle
- `corrections/` — **corrections must propagate**, the site's most distinctive argument:
  the 10,000-hours case, the 242-paper citation network, how a graph answers it, the
  self-critique on agenda ("the graph has an agenda too"), and a live staleness example
- `provenance/` — provenance is the product: fifteen departments, the £8.40 worked
  story, the decision graph, articles as vaults
- `library/` — the published record, chronological, 2025 → present: ten core articles
  and three adjacent pieces, 68,846 words, every entry carrying a provenance block
- `economics/` — paying the fact creator: the 60/25/10/5 split, Trust-as-a-Service, the
  x402 payment rail, and the 2025 micropayments argument republished and paired with it
- `rights/` — content rights: CC-Signed, a licence family with an enforceable stick
- `newsroom/` — operations: roles, the daily clock, departments, the craft doctrine
- `mvps/` — the publication instances: the newsroom specified as a series of small,
  separately launchable publications rather than one platform. The programme index, the
  flagship bilingual country publication and its eleven-role agentic newsroom, and the
  seven Creative Commons seed companies. Designed April–May 2026; none of it was built
- `governance/` — **The Governance Wire (beta)** — the first running MVP of the
  risk-and-governance publication, self-contained so it can move to its own domain. JSON is
  the source of truth for structure (`data/*.json`), markdown for prose (`content/*.md`), and
  the HTML is a projection built by `governance/build/build.py` and checked by
  `governance/build/gates.py`. Fully agentic: seven roles under `governance/team/`, one page
  each; no human review before publication, no legal sign-off, nothing anchored — every page
  says so. `governance/newsroom/` is the room itself: a clickable floor whose dialogue is
  assembled from live data, and a state map whose `frozen` door is shut, which is why nothing
  in the graph is anchored. `governance/research/` publishes the Researcher's runs, including
  the URLs our own egress could not reach
- `briefs/10__the-newsroom-floor.md` — a **debrief**, published for the other `*.sgit.ai`
  sites: how the agentic team was rendered as a point-and-click room, the rule that keeps
  it from being a mock-up, the defects it shipped into, and a porting recipe. Rendered at
  `documents/newsroom-floor.html`
- `shipped/` — what runs vs what is argued. Non-negotiable
- `network/` — sibling boundaries, the Risk Mandate inversion, open questions
- `documents/` — the brief pack this site was built from, published verbatim in `briefs/`,
  plus one **v1.1 addendum** that looks forward instead of back:
  `09__risk-and-governance-newsroom.md`, a commissioning brief for a risk-and-governance
  publication assembled from this network, with `riskmandate.ai` as its named customer
- `about/participant.html` — participant disclosure; two years of disclosed model
  co-authorship, stated as an asset rather than an awkwardness
- `admin/` — engineering: comms (open requests, in public), versions, build tooling
  - `admin/build/chrome.py` — the single definition of nav and footer, applied across every page
  - `admin/build/validate.js` — the pre-release gate, including the provenance-contract
    and redaction-watch-list checks specific to this site
- `assets/site.css` + `assets/nav.js` — the shared `sgit.ai` design language

## The provenance contract

Every page that republishes or derives from previously published material carries a
visible block: the **original** publication date (never the republication date), a link
to the original, the original authors including any AI co-authorship, and an honest
curation label (verbatim / edited / excerpted / synthesised). Full contract in
[`briefs/02__source-provenance-and-attribution.md`](briefs/02__source-provenance-and-attribution.md) —
the load-bearing file in this site's own brief pack. This site's central argument is
that most articles do not provide evidence and the link is never followed; losing its
own provenance chain would refute the site on page one.

## Release process

1. Bump `admin/build/version.txt` (vX.Y.Z, exactly once per release) and add a row to
   `admin/versions.html`.
2. `python3 admin/build/publish.py --from <checkout of SGit-AI/SGit-AI__Website> --node-modules <dir with sharp and playwright>`:
   publish the articles written here and import everything (it runs the sync below). Or, with no articles of our own changed,
   `python3 admin/build/sync_newsroom.py --from <checkout of SGit-AI/SGit-AI__Website>`:
   re-import the newsroom (only when sgit.ai has published since the last sync). It numbers any new article first
   (`admin/build/ids.py`, `articles/ids.json`) and prints each article's number at its foot.
3. Section builders, if their data or prose changed: `governance/build/build.py`,
   `world-news-day/build/build.py`, and so on, each followed by its own `gates.py`.
4. `python3 admin/build/find.py`: the findability data (`articles/find.json`); then `python3 admin/build/front.py`: the front page in three views, `index.md`, `about/index.html` and `articles/front.json`; `python3 admin/build/desks.py`: the desk pages; `python3 admin/build/deps.py`: the sgit.ai dependency report. `python3 admin/build/ids.py`: refresh `articles/ids.json` (the numbers never change). `python3 admin/build/hubs.py`:
   the design, replicate and shipped pages. `python3 admin/build/agents.py`: the agents' pages under `about/`. `python3 admin/build/personas.py`: the persona pages and
   `persona/links.json`. `python3 admin/build/lists.py`: the reading list pages (`for/`). `python3 admin/build/passkey_lab.py`: the passkey lab
   and its vectors. `python3 admin/build/wire.py [--from <clone of the wire's vault>]`: the wire pages, and the snapshot. `python3 admin/build/api_map.py`: the reader API map (`newsroom-api/`), last, so it hashes what the other builders wrote.
5. `python3 admin/build/archive.py`: the archive notes and the archive index; `python3 admin/build/engineering.py`: the engineering pages from the cards.
6. `python3 admin/build/chrome.py`: nav, footer and version on every page, plus `llms.txt`
   and `index.md`.
7. `python3 admin/build/gen_sitemap.py` and `python3 admin/build/gen_llms_full.py`.
8. `node admin/build/validate.js`, and, when the meter, the persona pages or the reading lists changed, `node admin/build/test_meter.mjs` and
   `node admin/build/test_lists.mjs` `node admin/build/test_review.mjs`, `node admin/build/test_passkey.mjs`, `node admin/build/test_wire.mjs`, `node admin/build/test_graphs.mjs`, `node admin/build/test_vault.mjs`, `node admin/build/test_sync.mjs`, `node admin/build/test_pane.mjs`, `node admin/build/test_notes.mjs`, `node admin/build/test_search.mjs`, `node admin/build/test_ask.mjs`, `node admin/build/test_themes.mjs`, `node admin/build/test_inbox.mjs` and `node admin/build/test_front.mjs`
   (browser tests; they need Playwright and skip without it; the wire test reads the real vault). CI runs all fifteen before it tags a release; the inbox test also needs jsqr (`npm install jsqr@1.4.0`) to read the QR code back.
9. `git commit -am "site vX.Y.Z: ..." && git push origin dev`

Running steps 4 to 7 twice changes nothing; if a second run writes files, something is wrong.

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate → auto-tag
(`vX.Y.Z`, verified against `version.txt` and the commit subject, next-minor enforced) →
deploy to GitHub Pages. Pull requests run validation only. Same pipeline as
[SGit-AI__Website](https://github.com/SGit-AI/SGit-AI__Website),
[SGit-AI__Website__PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI),
[SGit-AI__Website__Graphs](https://github.com/SGit-AI/SGit-AI__Website__Graphs) and
[SGit-AI__Website__Issues-FS](https://github.com/SGit-AI/SGit-AI__Website__Issues-FS).

### What the gate checks

The shared core (version agreement, links, canonical, agent surface, key-leak, block
balance, agent block) plus two checks specific to this site: **the provenance
contract** — every `class="provenance"` block must state a first-published date and a
working source link — and **the redaction watch-list** — a fixed set of Tier 3 strings
from the brief pack's own source manifest may never appear in the published tree.

## v0.2.0 — what shipped, and what is honestly still open

v0.1.0 shipped before a brief pack existed for this site and built on a wrong premise
(the site reporting on the `*.sgit.ai` network's own activity). v0.2.0 replaces that
content in full against the real, commissioned brief — *newsroom.sgit.ai, The Future of
News* — and follows its build order for the first five steps. Three sections
(`rights/`, `newsroom/`, `thesis/`) ship as single comprehensive hub pages rather than
the full multi-page trees the brief specifies, tracked as open task T1 on
`admin/comms.html`. Full detail on `admin/versions.html`.

## Licence

Two licences — see [`LICENSES.md`](LICENSES.md). Code Apache 2.0; this site's own
content CC BY 4.0. Republished library material is CC0 1.0 Universal at source
(`docs.diniscruz.ai`) — stated per page, never silently relicensed.
