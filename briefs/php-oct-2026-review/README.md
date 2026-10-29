# php.oct.2026.newsroom.sgit.ai, reviewed against the newsroom's own standard

*22 October 2026. A review of the live site at v0.2.2 (vault commit 200d08971937) for the agent that builds it, from the SGit Newsroom, for Dinis Cruz, the editor of both. Screenshots in Chromium at 1280×800 and 390×844, light theme unless stated; the ones worth keeping are in `shots/`. Requests come as this brief; the newsroom does not edit your repository.*

**Since this review.** The site reached v0.2.4 while it was being written, and these findings were checked against the source at v0.2.4: the table rule in `assets/site.css`, the briefing titles "a analyst" and "a cfo", the Wiz actor page, and "Six briefings" on the front page are all still there. The evidence vault is now **public and read-only**: its read key is at https://newsroom.sgit.ai/admin/php-oct-2026/, with the scan made before it was published. Anything written to the vault from now on is public for good. The newsroom's tracker still sees 2 of 5 checks for the move: `/status.json` is a 404, and the site has 144 of the 184 sources.

## Summary

The site already does the hard part. Every claim carries one of five status words, every number says what it measures, sixteen agencies sit side by side, and the build is deterministic and gated. The numbers page does what the first memo asked: it takes "70% of the internet" apart into a headline, a survey of websites, a host count and a national scan. What holds it back is presentation and the last link in the chain. The first screen shows the vault's counters before what happened or what to do; every table breaks on a phone, and the exploitation table breaks on a laptop too; a claim walks back to a source page but not to the sentence and the hash; the briefings are one long claims table with a different question on top; and the graph is a picture you cannot walk. Five things the memos asked for are missing or thin: blast radius from the assets outwards, exploitation counted over time, who said what first, the fractal graph, and a guide that shows its evidence. Separately, the newsroom cannot retire `/php-flaws/` until `status.json` exists and the 40 missing sources are exported.

## What works, and should be kept

- **The status words, defined once and used everywhere,** with the primary count `p/n` beside each claim: the [evidence, not truth](https://newsroom.sgit.ai/thesis/index.html) position made visible.
- **The numbers page:** six figures across four orders of magnitude, each with who said it and what it measures, then "Why they differ".
- **The agencies page:** the offline advice as a short label, the sentence quoted, the BBC's framing checked against each agency's own page, translations marked.
- **The impact page's two ledgers,** taken offline against compromised, with the gap stated: the cost so far is the cost of precaution.
- **The timeline's honesty about time:** stated, inferred and disputed, with conversions named.
- **"What is not" on the front page:** open questions and what would close each, the [corrections ethos](https://newsroom.sgit.ai/corrections/index.html) applied early.
- **Markdown twins, `llms.txt` and `data/*.json`:** the page API [Fix the page yourself](https://newsroom.sgit.ai/articles/fix-the-page-yourself.html) asks for, and what [The agent is the reader](https://newsroom.sgit.ai/articles/the-agent-is-the-reader.html) says agents will pay for.
- **REALITY.md and BRIEF-CORRECTIONS.md** say what is not built, including the fractal graph and the second model.
- **Weight and contrast:** 112 to 174 KB a page, eight requests, no page errors; dim text 6.1:1, links 6.2:1, status pills 6.4:1 to 8.4:1; one h1 per page.
- **The voice:** no first person, plain words, British spelling, contradictions left visible.

## The top 10 changes, ranked by impact

### 1. The first screen: what happened and what to do, before the vault's counters

- **Element:** front page, `header.hero` (`shots/01-front-first-screen-1280.webp`, `shots/02-front-first-screen-390.webp`).
- **Problem:** At 1280×800 the fold holds the title, a 110-word lead and seven counter tiles, five of which describe the vault (sources, captures, claims, events, inventory). The fixed versions and the playbook are not on the first screen; the playbook is linked only from the menu. On a phone, three rows of chrome (about 155 px) and the lead fill the screen.
- **Standard:** "News first, record second, plumbing last", from the newsroom's front page spec (`admin/notes/wires-ux/first-screen.md`); [Ways to read one article](https://newsroom.sgit.ai/articles/ways-to-read-one-article.html): the reader picks the way in, phone first.
- **Change:** Under the title, three lines with status words: what it is (two RCE flaws, CVSS 9.2); what to do (patch to 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or apply the mitigations); where it stands (attempts at scale, no confirmed compromise, agencies split on taking systems offline). Then two buttons, **If you run PHP** and **Read it for your job**. The counters become one quiet linked line; the method sentence moves into the caveat.
- **Acceptance check:** At 1280×800 and 390×844 the fixed versions, the exploitation state and a link to the playbook are visible without scrolling.

### 2. Tables that keep their words whole

- **Element:** every table; worst on the exploitation page at 1280 (`shots/03-exploitation-table-1280.webp`) and every table at 390 (`shots/04-numbers-table-390.webp`).
- **Problem:** `assets/site.css` sets `td{overflow-wrap:anywhere}`, so the browser shrinks text columns to almost nothing while the `nowrap` status pill holds its width. On the exploitation page at 1280 the "What" column is about 100 px and words break mid-word ("attem pt", "Cloudfla re"). At 390 a single note runs to 40 lines of fragments; the claims page is 67,000 px tall, the CISO briefing 45,000 px.
- **Standard:** the reading list design review (`admin/notes/2026-10-21__the-reading-list-design-review.md`): no overflow at 390, checked with a screenshot. [Scrolled is not read](https://newsroom.sgit.ai/articles/scrolled-is-not-read.html): 45,000 px scrolled has not been read.
- **Change:** Use `overflow-wrap:break-word` on `td` (keep `anywhere` for hashes, URLs and code); fix the widths of the status and time columns; under 700 px draw each row as a card (claim in bold, then status, who, `p/n` and chips, then the note). Add a screenshot check at 390 to the gate.
- **Acceptance check:** No word broken inside itself in any table at 1280 or 390; the claims page at 390 under 25,000 px.

### 3. Every claim walks back to the sentence and the hash, in two clicks

- **Element:** claims page, briefings, source pages, `data/claims.json`.
- **Problem:** Claims link to source pages, which show collectors' notes and, folded, the hashes. Claim rows have no ids, so briefings link to the claims page as a whole. No claim carries its quoted sentence or the capture and file it is in. The source page says "the hashes above"; they are below, folded.
- **Standard:** [Provenance is the product](https://newsroom.sgit.ai/provenance/index.html): a citation the reader can actually follow. [The wire as a graph](https://newsroom.sgit.ai/articles/the-wire-as-a-graph.html): every sentence a claim pointing at its evidence, with a long-lived ID. [The story vault](https://newsroom.sgit.ai/articles/future-of-news-story-vault-not-paywall.html): a chain from claim to frozen bytes with a hash.
- **Change:** `id="c-<claim id>"` on every claim row, used by briefings and graph nodes. Per citation, a word-for-word `quote`, the `capture` id and the file, shown as "Wiz, 22 Oct 08:10 UTC capture: '...' sha256 32408c9f...". The gate checks each quote occurs in the capture's text. Source pages list their claims with the sentences first and show the hashes unfolded.
- **Acceptance check:** From any claim, two clicks reach the quoted sentence, the capture time and the file's sha256; `claims/index.html#c-two-cves-9.2` resolves.

### 4. The transition: `status.json` and the 40 missing sources

- **Element:** site root, `data/sources.json`, footer.
- **Problem:** `/status.json` answers 404, and the site lists 144 sources where the vault held 184 by 12:05 UTC: checks 2 and 3 of `briefs/php-oct-2026/01__the-transition.md`. The footer's "here" links to the section that is about to become a pointer.
- **Standard:** `briefs/php-oct-2026/02__status-json.md` and `04__what-the-newsroom-keeps.md`; [Capture first](https://newsroom.sgit.ai/articles/capture-first.html): two places with the same facts is one too many.
- **Change:** Re-export from the vault head; build `status.json` in the shape in `02`, with `data_as_of` from the latest capture and up to three `headline_facts` already on the site. Point the footer at the article `capture-first`, and keep the link to the newsroom's front page.
- **Acceptance check:** `track.py` reports checks 1 to 4 passing against the live site.

### 5. Exploitation counted over time, drawn

- **Element:** exploitation page; the front page.
- **Problem:** Twenty signals sit in a table. The memo asked to track exploitation over time, because volume across hours is the evidence of how weaponised a flaw is. Nothing draws it, and the count that matters, zero confirmed compromises, is a clause in a lead.
- **Standard:** the first memo; [When journalism becomes intelligence](https://newsroom.sgit.ai/articles/journalism-becomes-intelligence.html): each observation a subject, a change, a time and evidence, played in time.
- **Change:** An SVG strip chart built from `data/exploitation.json`, UTC from 17 October, one lane per kind (honeypot or sensor hit, attempts at a CDN, national CERT, negative finding, confirmed compromise). Each mark links to its row; sized by a stated count where one exists, hollow where none is given; the compromise lane shows zero. Add `count` and `count_basis` to each signal so the chart never invents a number. A small copy on the front page.
- **Acceptance check:** The chart is on both pages, every mark links to a row, and the caption says attempts are not compromises.

### 6. Who said what first, and what was recycled

- **Element:** journalist briefing, actor pages, numbers page, `data/claims.json`, `data/actors.json`.
- **Problem:** The journalist briefing promises "who said what first"; only the discovery page answers it. For the claims that travelled (70%, 30 million, "take systems offline") there is no first appearance and no relay chain. The actor join is broken: the Wiz page says "No claim row names this party" (`shots/06-actor-wiz-1280.webp`), because `by` is free text ("Wiz (headline, X post)").
- **Standard:** the first memo ("who's bringing it in ... what's new, what's being recycled"); [The wire as a graph](https://newsroom.sgit.ai/articles/the-wire-as-a-graph.html): every name a link with an ID; the newsroom's rule to name parties, dated.
- **Change:** Add `by_ids` and, per source on a claim, `first_seen` and a role (`origin`, `relay`, `independent`). Show the chain on each claim ("Wiz on X, 21 Oct (origin) → BBC live page, 22 Oct (relay, flagged unverified) → ..."). Actor pages list what the party said first, relayed, and got wrong.
- **Acceptance check:** The Wiz page lists the 70% claim; each headline number shows its origin with a time and its relays.

### 7. Briefings a person in that role can read in two minutes

- **Element:** the twelve pages under `/briefings/` (`shots/08-board-briefing-1280.webp`).
- **Problem:** Each is a question, five decisions (good), then 30 to 40 claims in a table. The board briefing is 31,000 px on a phone, with no bottom line. Titles read "Briefing for a analyst", "a cfo", "a ciso", "a cto", "a php or platform engineer". The front page says "Six briefings" over twelve cards.
- **Standard:** [A briefing for the WestCap CISO Summit](https://newsroom.sgit.ai/articles/a-briefing-for-the-ciso-summit.html): the idea said for each kind of person, with what to read next. [Research, delivered as a vault](https://newsroom.sgit.ai/articles/research-delivered-as-a-vault.html): briefings per reader from one graph.
- **Change:** Open with three sentences in the role's words, each ending in a claim link and status; then the decisions; then five to eight claims as cards; then the full table folded; then "read next" for that role. Fix the grammar, the capitals and "Six".
- **Acceptance check:** At 390 the bottom line and decisions sit within two screens; each briefing under 6,000 px with the table folded.

### 8. Blast radius, from the assets outwards

- **Element:** the flaws page's blast radius section; a new page.
- **Problem:** Six good questions in prose. The memo asked to start from the assets: what is behind each server, what credentials it holds, what stands in front, and what compromise would mean for each kind of site. No map, no worked case.
- **Standard:** [Footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html): cost if the reach is used in full, and whether there is a way back. [Ten questions, one graph](https://newsroom.sgit.ai/articles/ten-questions-one-graph.html).
- **Change:** `/blast-radius/`: per asset type (brochure site, shop with payments, intranet with single sign-on, admin or hosting panel, vendor appliance, shared hosting) what the PHP worker reaches, the barriers in front, the way back, and the sources; marked as the site's analysis. Link it from playbook step 0 and the board and CISO briefings.
- **Acceptance check:** Five or more asset types, each row sourced, linked from the playbook and two briefings.

### 9. The playbook, with its evidence shown and offline at the end

- **Element:** "If you run PHP" (`shots/09-playbook-1280.webp`).
- **Problem:** The intro promises "the sentence each step comes from", but steps show only chips. "Isolate or take offline" is step 4, before "Look for compromise" and "Verify". The detection and defence page is not linked. No before, during and after.
- **Standard:** the second memo: a guide "backed with evidence", with offline "at the end of a long sequence of events", and the ability to pull the plug quickly. [Provenance is the product](https://newsroom.sgit.ai/provenance/index.html).
- **Change:** Three phases. *Now:* inventory, patch, mitigate, shield, watch (linking `/defence/` for WAF rules, Sigma, Suricata, Falco and host signals). *If none of that is possible in time:* isolate, then take offline, naming the agencies that say so and those that do not. *After:* look for compromise from 17 October, verify the running version, rehearse pulling the plug and record the time. Each step opens to the agency's sentence, word for word, linked to its claim.
- **Acceptance check:** Every step opens to a quoted sentence; taking offline is the last action; `/defence/` is linked twice.

### 10. A graph you can walk, and its first fractal layer

- **Element:** "The story as a graph", and the small graphs on source and actor pages (`shots/05-graph-390.webp`).
- **Problem:** A static two-column drawing: 70 truncated claims, 71 sources, 281 edges, all `cites`. No node is a link. One party appears as several nodes (CISA three times, oss-security four). At 390 labels are about 3 px tall.
- **Standard:** [Fractal Semantic Graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html): the test is what happens at a link. [Search as navigation](https://newsroom.sgit.ai/articles/search-as-navigation.html): walk into the graph around a word. [Inside the Mesa Ranch desk](https://newsroom.sgit.ai/articles/inside-the-mesa-ranch-desk.html): a fractal graph opened level by level.
- **Change:** Every node a link; parties as nodes; typed edges (`states`, `relays`, `contradicts`, `supersedes`, `quotes`). Then one fractal layer: a source opens into its captures and hashes, an actor into its statements over time, an agency into its advice. On a phone, the selected node and its neighbours as a list.
- **Acceptance check:** Every node is a link; four or more edge types in `data/graph.json`; one click from a claim reaches a graph in another vocabulary; labels at least 12 px at 390.

## The rest, by area

**Navigation and findability.** The menu has 47 items; the playbook is eleventh under "The story". Put "If you run PHP" and "Briefings" in the bar. Add a client-side filter over claims and sources by party, status and topic. On a phone, move the version and data time to the footer. Replace the footer's "here" with what it names.

**Reading and typography.** Show "Thursday 22 October 2026, 11:34 UTC" with the ISO value in `datetime`, as the front page spec does. The impact page repeats its opening paragraph; keep one. The front page's claim counts omit the 33 reported; the caveat defines four of the five status words, missing *contradicted*. On the agencies page "yes" (take offline) is green like *confirmed*: give advice labels their own neutral style. A log-scale bar beside each headline number would show the four orders of magnitude at a glance. The markdown twins join claim and note with no space ("initiativeAll three").

**Provenance.** Give each claim a status history; on a developing story this is the "Corrected by" and "Status since" that [Every link points back](https://newsroom.sgit.ai/articles/every-link-points-back.html) proposes. Say on the method page that hashes are not yet anchored to an outside time.

**Mobile.** Group the timeline (41,787 px at 390) by day, the latest open.

**Accessibility.** Under each SVG graph, the same data as a linked list. In dark mode the reading meter's rating buttons are pale on pale, about 1.3:1 (`shots/07-meter-dark-1280.webp`): move from SG Meter v1.3.1 to v1.5.0, which the newsroom runs and whose colours are tokens.

**Performance.** Fine. The meter is about 90 KB of a 120 KB page; load it after the content if weight matters later.

**Themes and tokens.** The site defines its own tokens (`--ok-*`, `--bad-*`, `--mute-ink`), a blue accent, and follows the system's dark setting with no choice. The newsroom's rule is one set of named tokens defined in every theme ([Dark mode, and four more](https://newsroom.sgit.ai/articles/dark-mode-and-four-more.html), `assets/themes/README.md`). Use the newsroom's names (`--text`, `--dim2`, `--danger-bg`, `--danger-ink`, `--warn-line`, `--tint`, `--on-accent`), honour `data-theme` with at least Newsprint and Night, and add a picker. The accent can stay the site's own.

**Voice and wording.** The gate's em-dash check skips `sources/` and `actors/` to allow third-party titles, so 23 em-dashes in collectors' notes reach the page (the Wiz source page has one in its first note). Exempt only `<q>` and `title`, and rewrite the notes. Absolutes: "Nobody has published a count of successful exploitation" should be "no captured source gives a count"; "a statistic that nobody on this beat sources" should be "none of the captured sources names". "That gap is the most important finding on this site" claims more than a page can show; "That gap is the finding this page is for". Add the byline mark from [Who is speaking](https://newsroom.sgit.ai/articles/who-is-speaking.html) where the site gives its own analysis.

**Testing.** Run five synthetic readers on screenshots (a board member on a phone, a PHP engineer, a journalist, a sceptic, a comms lead), as in [How to run synthetic users](https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html), and record the findings in BRIEF-CORRECTIONS.md.

## What the memos asked for, and where the site stands

| Asked for | Where it stands | Next |
|---|---|---|
| Provenance and accuracy; the statistics explained | Strong: numbers page, status words | Sentence-level citations (3) |
| The vulnerability, attack vector, exploits | Done: flaws and code pages, read from php-src | Keep current on the 8.5.12 question |
| Blast radius from the assets | Six questions in prose | A worked map by asset type (8) |
| Exploitation signals, objectively | Twenty signals; the impact ledgers | Counted over time, drawn (5) |
| How many sites actually exploited | None confirmed, stated | Keep the zero on the front page |
| Detection: logs, signatures, WAF, IDS | The defence page | Linked from the playbook (9) |
| An evidence-backed guide, offline at the end | Seven steps with chips; offline fourth | Phases, quotes, offline last (9) |
| How fast can you pull the plug | A paragraph | A rehearsal step with a time (9) |
| Briefings for each role | Twelve, each a selection of claims | Bottom line, short form (7) |
| Who says what, new or recycled | The discovery page only | Origin and relay chains (6) |
| Exploitation and patch numbers over time | One-off counts | A series per figure as captures accumulate |
| Which systems are vulnerable | NCSC-NL inventory at one commit | Recount per commit, show the change |
| The semantic fractal graph | One graph, one edge type; recorded as not built | Walkable and typed, one fractal layer (10) |
| ChatGPT and Claude both reading the data | Not done; recorded | A second model, its disagreements published |
| How the story changes over time | Captures kept as series | Status history per claim |

## How to work with the newsroom

The split is the one the second memo set. **This site keeps the facts:** claims with a status, sources, timeline, numbers, agencies, inventory, playbook and briefings, with no first person and analysis marked as such. **The newsroom keeps the context and the opinion:** what the story means, how it was covered, what it says about disclosure and AI-found flaws, in Dinis's voice. The newsroom links to your pages for every fact and never copies them, so keep URLs stable, give every claim a stable anchor (change 3), and leave a pointer if a page moves.

The move off `newsroom.sgit.ai/php-flaws/` is in `briefs/php-oct-2026/01__the-transition.md`. The tracker runs five checks against your live site: live (passing); `status.json` (not yet); every section source in your `data/sources.json` (144 of 184); the newsroom's front page linking to you (passing); then the newsroom's own step, turning `/php-flaws/` into a pointer to your front and sources pages. Change 4 unblocks it. Once checks 1 to 4 pass and Dinis confirms, the section becomes the pointer, and the front-page strip reads your `status.json` while the story is `developing`.

If this brief gets something about your site wrong, open an issue on `SGit-AI/SGit-AI__Website__Newsroom` or tell Dinis, and it gets a new version.

## Where this comes from

Reviewed on 22 October 2026 against the live site at v0.2.2 and its repository at commit f545cc9, after reading its README, REALITY.md, BRIEF-CORRECTIONS.md, the brief and the two memo transcripts. Fourteen pages were screenshotted at both widths with a Playwright script that recorded weight, requests, headings and scroll width; the front and numbers pages again in dark mode. Contrast was computed from the token values in `assets/site.css`; the em-dash, absolute and title findings from a scan of the built pages and twins. The standard is the newsroom's: `admin/content/articles/README.md`, `assets/themes/README.md`, the design notes in `admin/notes/`, the provenance, corrections and thesis hubs, and the articles linked above. Written by the newsroom's agent; the editorial responsibility is Dinis's.
