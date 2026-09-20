# Inventory — every file, with where it lives now

**160 files.** Machine-readable twin: [`01__inventario.json`](01__inventario.json), which carries the SHA-256, the byte count, the live HTTP status and the archive path for every row. Every live URL below returned **200** and was **byte-identical to the repository** when this archive was cut.

| Column | Meaning |
|---|---|
| Live | The page or file on `newsroom.sgit.ai`, as it is today |
| Repo | The same file on GitHub, on the `dev` branch |
| Archive | Where it sits inside this bundle |

## Pages, as served — 20 files, 573 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `index.html` | The front page of the section: the lead, the wire, the programme by day, what the press says, the room as a graph, who made it | [portugal/index.html](https://newsroom.sgit.ai/portugal/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/index.html) |
| `graph.html` | The graph, drawn: 329 nodes, 1,106 edges, packs switched on block by block, paths read aloud in English or Portuguese | [portugal/graph.html](https://newsroom.sgit.ai/portugal/graph.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/graph.html) |
| `explorer.html` | The files: every file the section is built from, with its SHA-256, rendered / as a graph / raw | [portugal/explorer.html](https://newsroom.sgit.ai/portugal/explorer.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/explorer.html) |
| `connections.html` | Who should be talking to whom, who could be buying from whom, who could help whom — three SQL queries at organisation level | [portugal/connections.html](https://newsroom.sgit.ai/portugal/connections.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/connections.html) |
| `index.html` | The event as it describes itself, with targets distinguished from counts | [portugal/summit/index.html](https://newsroom.sgit.ai/portugal/summit/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/summit/index.html) |
| `people.html` | All 64 published speakers with role, organisation, the event’s own topics, and a link to each speaker’s own page | [portugal/summit/people.html](https://newsroom.sgit.ai/portugal/summit/people.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/summit/people.html) |
| `orgs.html` | 61 organisations derived from the speaker cards; 2 placeholders flagged rather than removed | [portugal/summit/orgs.html](https://newsroom.sgit.ai/portugal/summit/orgs.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/summit/orgs.html) |
| `changes.html` | The same pages frozen twice and diffed: 5 speakers added, 1 removed, between 8 and 13 September | [portugal/summit/changes.html](https://newsroom.sgit.ai/portugal/summit/changes.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/summit/changes.html) |
| `sources.html` | The register: every frozen file with its SHA-256, byte count and retrieval time | [portugal/sources.html](https://newsroom.sgit.ai/portugal/sources.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/sources.html) |
| `checks.html` | What re-reading the frozen copies established, including two different sets of stage names on the same site | [portugal/checks.html](https://newsroom.sgit.ai/portugal/checks.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/checks.html) |
| `method.html` | fetch → freeze → hash → extract → diff, and the gates that enforce it | [portugal/method.html](https://newsroom.sgit.ai/portugal/method.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/method.html) |
| `team.html` | Seven agent roles plus the named editor of record | [portugal/team.html](https://newsroom.sgit.ai/portugal/team.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team.html) |
| `notice.html` | The data-protection notice: what is held, why it is lawful, how to be removed without giving a reason | [portugal/notice.html](https://newsroom.sgit.ai/portugal/notice.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/notice.html) |
| `about.html` | Beta, one beat, two kinds of source, no legal review, nothing in Portuguese | [portugal/about.html](https://newsroom.sgit.ai/portugal/about.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/about.html) |
| `a-record-attempt-the-agenda-does-not-mention.html` | STORY 3 — two Portuguese outlets report a 48-hour Guinness pitch marathon the event’s own agenda does not list | [portugal/stories/a-record-attempt-the-agenda-does-not-mention.html](https://newsroom.sgit.ai/portugal/stories/a-record-attempt-the-agenda-does-not-mention.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/stories/a-record-attempt-the-agenda-does-not-mention.html) |
| `five-names-arrived-and-one-left.html` | STORY 2 — the speaker list went 60 → 64 between 8 and 13 September; both copies held and hashed | [portugal/stories/five-names-arrived-and-one-left.html](https://newsroom.sgit.ai/portugal/stories/five-names-arrived-and-one-left.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/stories/five-names-arrived-and-one-left.html) |
| `two-names-for-three-stages.html` | STORY 1 — the agenda and the AI-summary page name the same stages differently, on the same site, on the same day | [portugal/stories/two-names-for-three-stages.html](https://newsroom.sgit.ai/portugal/stories/two-names-for-three-stages.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/stories/two-names-for-three-stages.html) |
| `index.html` | Databases with no server: the argument — the files are the database, the engines are readers | [databases/index.html](https://newsroom.sgit.ai/databases/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/index.html) |
| `sql.html` | The SQL console: SQLite via sql.js over the section’s JSON, 16 worked queries with their build-time row counts | [databases/sql.html](https://newsroom.sgit.ai/databases/sql.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/sql.html) |
| `graph.html` | The graph console: Oxigraph (SPARQL 1.1) over the same graph as triples, 13 worked queries beside their Cypher equivalents | [databases/graph.html](https://newsroom.sgit.ai/databases/graph.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/graph.html) |

## Role pages — 7 files, 110 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `index.html` | Role page — cartographer: keeps the graph and its vocabulary | [portugal/team/cartographer/index.html](https://newsroom.sgit.ai/portugal/team/cartographer/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/cartographer/index.html) |
| `index.html` | Role page — diffwatch: compares one snapshot to the next | [portugal/team/diffwatch/index.html](https://newsroom.sgit.ai/portugal/team/diffwatch/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/diffwatch/index.html) |
| `index.html` | Role page — editor: the named human of record, reads before publication | [portugal/team/editor/index.html](https://newsroom.sgit.ai/portugal/team/editor/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/editor/index.html) |
| `index.html` | Role page — extractor: reads the frozen bytes into data | [portugal/team/extractor/index.html](https://newsroom.sgit.ai/portugal/team/extractor/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/extractor/index.html) |
| `index.html` | Role page — publisher: runs the build, the gates and the release | [portugal/team/publisher/index.html](https://newsroom.sgit.ai/portugal/team/publisher/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/publisher/index.html) |
| `index.html` | Role page — researcher: finds the source and freezes it | [portugal/team/researcher/index.html](https://newsroom.sgit.ai/portugal/team/researcher/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/researcher/index.html) |
| `index.html` | Role page — writer: writes from the data and nothing else | [portugal/team/writer/index.html](https://newsroom.sgit.ai/portugal/team/writer/index.html) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/team/writer/index.html) |

## Data files — 22 files, 1397 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `changes.json` | The diff between the two snapshots: who arrived, who left, and no reason for the departure | [portugal/data/changes.json](https://newsroom.sgit.ai/portugal/data/changes.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/changes.json) |
| `checks.json` | What re-reading established: speaker counts, the two sets of stage names, the unverifiable countries claim | [portugal/data/checks.json](https://newsroom.sgit.ai/portugal/data/checks.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/checks.json) |
| `connections.json` | The three organisation-level queries with their SQL and the rows each returned at build | [portugal/data/connections.json](https://newsroom.sgit.ai/portugal/data/connections.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/connections.json) |
| `coverage-notes.json` | The editorial notes behind coverage.json, plus the excluded page and why | [portugal/data/coverage-notes.json](https://newsroom.sgit.ai/portugal/data/coverage-notes.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/coverage-notes.json) |
| `coverage.json` | 7 press pages about the event, frozen and hashed before citation, summarised never quoted | [portugal/data/coverage.json](https://newsroom.sgit.ai/portugal/data/coverage.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/coverage.json) |
| `event.json` | The event as its own pages describe it: dates, venue, organiser, stages, targets — targets kept separate from counts | [portugal/data/event.json](https://newsroom.sgit.ai/portugal/data/event.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/event.json) |
| `graph.json` | The whole section as one graph: 329 nodes, 1,106 edges, in 10 packs | [portugal/data/graph.json](https://newsroom.sgit.ai/portugal/data/graph.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/graph.json) |
| `lexicon.json` | The published formula: 57 regular expressions for industries, technologies, ideas, services and products | [portugal/data/lexicon.json](https://newsroom.sgit.ai/portugal/data/lexicon.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/lexicon.json) |
| `manifest.json` | Every file the section is built from, with size and SHA-256 | [portugal/data/manifest.json](https://newsroom.sgit.ai/portugal/data/manifest.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/manifest.json) |
| `notice.json` | The data-protection notice as data: controller, categories held and refused, the three-limb test | [portugal/data/notice.json](https://newsroom.sgit.ai/portugal/data/notice.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/notice.json) |
| `ontology.json` | 16 node types and 19 verbs, each with its Portuguese, the banned verbs, the taxonomy, the formulas | [portugal/data/ontology.json](https://newsroom.sgit.ai/portugal/data/ontology.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/ontology.json) |
| `orgs.json` | 61 organisations derived from the speaker cards, placeholders flagged | [portugal/data/orgs.json](https://newsroom.sgit.ai/portugal/data/orgs.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/orgs.json) |
| `people.json` | 64 speakers: name, listed role, listed organisation, links. No biographies, no contact details | [portugal/data/people.json](https://newsroom.sgit.ai/portugal/data/people.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/people.json) |
| `sessions.json` | 16 sessions on 3 stages, each title verbatim from the frozen agenda | [portugal/data/sessions.json](https://newsroom.sgit.ai/portugal/data/sessions.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/sessions.json) |
| `sources.json` | The register: 88 frozen files across 2 snapshots, each with SHA-256, bytes and retrieval time | [portugal/data/sources.json](https://newsroom.sgit.ai/portugal/data/sources.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/sources.json) |
| `stories.json` | The three stories, each with the frozen sources it stands on | [portugal/data/stories.json](https://newsroom.sgit.ai/portugal/data/stories.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/stories.json) |
| `team.json` | The seven agent roles and the named human editor of record | [portugal/data/team.json](https://newsroom.sgit.ai/portugal/data/team.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/team.json) |
| `topics.json` | Per speaker: the event’s own Topics list verbatim, and the lexicon matches with the matched words | [portugal/data/topics.json](https://newsroom.sgit.ai/portugal/data/topics.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/topics.json) |
| `triples.nt` | The same graph as 4,001 N-Triples with the ontology inside and owl:inverseOf on every verb | [portugal/data/triples.nt](https://newsroom.sgit.ai/portugal/data/triples.nt) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/data/triples.nt) |
| `queries-sparql.json` | The 13 worked SPARQL queries with their Cypher equivalents and build-time counts | [databases/data/queries-sparql.json](https://newsroom.sgit.ai/databases/data/queries-sparql.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/data/queries-sparql.json) |
| `queries-sql.json` | The 16 worked SQL queries with the row count each returned at build | [databases/data/queries-sql.json](https://newsroom.sgit.ai/databases/data/queries-sql.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/data/queries-sql.json) |
| `tables.json` | The loader spec: which file and which field each SQL column comes from | [databases/data/tables.json](https://newsroom.sgit.ai/databases/data/tables.json) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/data/tables.json) |

## Code — 12 files, 322 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `build.py` | Every other page, from the data files and the story markdown | [portugal/build/build.py](https://newsroom.sgit.ai/portugal/build/build.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/build.py) |
| `connections.py` | The three connection formulas as SQL, executed at build and stored with their rows | [portugal/build/connections.py](https://newsroom.sgit.ai/portugal/build/connections.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/connections.py) |
| `extract.py` | The ingestion path: fetch, freeze, hash, register, extract, diff. The one thing to copy before anything else | [portugal/build/extract.py](https://newsroom.sgit.ai/portugal/build/extract.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/extract.py) |
| `gates.py` | Eighteen gates that fail the build — the section’s conscience, in code | [portugal/build/gates.py](https://newsroom.sgit.ai/portugal/build/gates.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/gates.py) |
| `graph.py` | The ontology and the graph builder, including the N-Triples export | [portugal/build/graph.py](https://newsroom.sgit.ai/portugal/build/graph.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/graph.py) |
| `pages.py` | The front page, the graph page, the explorer and the connections page | [portugal/build/pages.py](https://newsroom.sgit.ai/portugal/build/pages.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/build/pages.py) |
| `build.py` | The databases section: the loader spec, the worked queries, and their execution at build | [databases/build/build.py](https://newsroom.sgit.ai/databases/build/build.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/build/build.py) |
| `validate.js` | The site gate: 10 whole-site checks that must pass before any release | [admin/build/validate.js](https://newsroom.sgit.ai/admin/build/validate.js) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/admin/build/validate.js) |
| `chrome.py` | Nav, footer and the version badge that the validator requires to agree everywhere | [admin/build/chrome.py](https://newsroom.sgit.ai/admin/build/chrome.py) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/admin/build/chrome.py) |
| `portugal-graph.js` | The graph viewer: Cytoscape, packs, radius, path-as-sentence, the window.__graph API | [assets/portugal-graph.js](https://newsroom.sgit.ai/assets/portugal-graph.js) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/assets/portugal-graph.js) |
| `nsdb-sql.js` | The SQL console: builds the tables in the browser from the loader spec, publishes window.__tools.sql | [assets/nsdb-sql.js](https://newsroom.sgit.ai/assets/nsdb-sql.js) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/assets/nsdb-sql.js) |
| `nsdb-sparql.js` | The SPARQL console: loads the triples into Oxigraph in the browser, publishes window.__tools.sparql | [assets/nsdb-sparql.js](https://newsroom.sgit.ai/assets/nsdb-sparql.js) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/assets/nsdb-sparql.js) |

## Story prose (markdown) — 3 files, 11 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `a-record-attempt-the-agenda-does-not-mention.md` |  | [portugal/content/a-record-attempt-the-agenda-does-not-mention.md](https://newsroom.sgit.ai/portugal/content/a-record-attempt-the-agenda-does-not-mention.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/content/a-record-attempt-the-agenda-does-not-mention.md) |
| `five-names-arrived-and-one-left.md` |  | [portugal/content/five-names-arrived-and-one-left.md](https://newsroom.sgit.ai/portugal/content/five-names-arrived-and-one-left.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/content/five-names-arrived-and-one-left.md) |
| `two-names-for-three-stages.md` |  | [portugal/content/two-names-for-three-stages.md](https://newsroom.sgit.ai/portugal/content/two-names-for-three-stages.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/content/two-names-for-three-stages.md) |

## Documents and briefs — 7 files, 83 KB

| File | What it is | Live | Repo |
|---|---|---|---|
| `README.md` |  | [portugal/README.md](https://newsroom.sgit.ai/portugal/README.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/portugal/README.md) |
| `11__pt-newsroom-commissioning-brief.md` |  | [briefs/11__pt-newsroom-commissioning-brief.md](https://newsroom.sgit.ai/briefs/11__pt-newsroom-commissioning-brief.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/briefs/11__pt-newsroom-commissioning-brief.md) |
| `14__what-pt-newsroom-can-take-from-here.md` |  | [briefs/14__what-pt-newsroom-can-take-from-here.md](https://newsroom.sgit.ai/briefs/14__what-pt-newsroom-can-take-from-here.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/briefs/14__what-pt-newsroom-can-take-from-here.md) |
| `12__research-brief-for-chatgpt.md` |  | [briefs/12__research-brief-for-chatgpt.md](https://newsroom.sgit.ai/briefs/12__research-brief-for-chatgpt.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/briefs/12__research-brief-for-chatgpt.md) |
| `13__research-brief-for-perplexity.md` |  | [briefs/13__research-brief-for-perplexity.md](https://newsroom.sgit.ai/briefs/13__research-brief-for-perplexity.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/briefs/13__research-brief-for-perplexity.md) |
| `README.md` |  | [databases/README.md](https://newsroom.sgit.ai/databases/README.md) | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/databases/README.md) |
| `LICENSES.md` |  | — | [GitHub](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/LICENSES.md) |

## Frozen sources (evidence) — 89 files, 3877 KB

Third-party bytes, held as evidence by this publication and never republished as browsable pages.
Listed in full in the JSON; summarised here by folder.

| Folder | Files | What |
|---|---|---|
| `portugal/sources/frozen/2026-09-08/agenda.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-08/ai-summary.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-08/index.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-08/speakers.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-08/sponsors.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/agenda.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/ai-summary.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/coverage/` | 8 | Seven press pages about the event, frozen before citation |
| `portugal/sources/frozen/2026-09-13/faq.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/index.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/llms.txt/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/location.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/speakers/` | 64 | Every speaker’s own page on the event site, frozen |
| `portugal/sources/frozen/2026-09-13/speakers.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/sponsors.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/startup-booths.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/tickets.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/what-to-expect.snapshot/` | 1 |  |
| `portugal/sources/frozen/2026-09-13/why-attend.snapshot/` | 1 |  |

Register with every hash: [`portugal/data/sources.json`](https://newsroom.sgit.ai/portugal/data/sources.json)

