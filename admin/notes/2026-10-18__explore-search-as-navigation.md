# Explore: search as navigation over the newsroom's graph, with no model, and a pane that shows how it works

*18 October 2026, a brief written by newsroom.writer for the agent that builds it. Status: a brief; nothing in it is built. The article that explains why is [search as navigation](https://newsroom.sgit.ai/articles/search-as-navigation.html). It builds on [search in the browser](2026-10-13__search-in-the-browser.md) (the index and BM25 ranking that run today) and on the two engines already vendored for [databases with no server](../../databases/README.md).*

## The ask, in Dinis's words, condensed

Search should be navigation, not question and answer. Typing *Portugal* should show not only the items about Portugal but the graph around it: the articles, their ideas, the sections, the images, the people and things they connect to, and the combinations worth following next. As words are typed, the side of the page should suggest what they could mean and what sits near them, so the reader builds the query by navigating. It should be deterministic: code and graphs, no model, in this version. A model comes later, on top of the graph. And a pane, for Dinis and for power users, that shows exactly what was fetched, how each result arrived, and the load and timing figures.

The point being made with it: the better the taxonomy, the ontology and the graphs, the less a model is needed; and when a model is added, it does better on a clean graph than on vectors. This is graph RAG built in the reader's browser.

## What exists today (measured 18 October 2026)

| Piece | Where | Size or count |
|---|---|---|
| Page index, BM25 in the browser | `admin/build/search_index.py` → `search/docs.json`; `assets/search/search.js` | 576 KB; 930 docs (182 articles, 311 wire stories, 190 engineering, 160 pages, …) |
| Paragraph text, current and earlier versions | `search/text.json` | 6.0 MB |
| Article graphs: core idea, nodes, edges, links, quotes | `articles/graphs/<slug>.json` (source `admin/content/articles/graphs/`) | 182 graphs; 2,289 nodes; 2,326 edges |
| Section summaries: a line and a paragraph per section | `articles/summaries/<slug>.json` | 1,995 sections |
| Article metadata: number, date, topics, personas, teaser | `articles/ids.json` | 182 |
| Figures with captions and kinds | `!shot` lines in the article sources; `articles/images/` | 657 files, 72 MB |
| Trails (series) | `admin/content/trails.json` | 7 |
| Reviews on the record | `reviews/status.json`, `reviews/records/` | new in v0.12.107 |
| Wire stories with entities | `wire/`, `newsroom/wire.json`, the Portugal section | 311 stories |
| Graph drawing | `assets/vendor/cytoscape.min.js` | vendored |
| SPARQL | `assets/vendor/oxigraph/` (used by `/databases/graph.html`) | vendored |
| SQL | `assets/vendor/sql-wasm.js` (used by `/databases/sql.html`) | vendored |

### The taxonomy debt, counted

- **Tags:** 663 distinct tags on 182 articles; 396 are used once. Near-duplicates include `business-model` and `business-models`, `browser` and `browsers`, `brief` and `briefs`, `digital-twin` and `digital-twins`, `llm` and `llms`, `threat-model` and `threat-models`.
- **Ideas:** the graphs have 2,230 distinct node labels; 47 appear in more than one article. Each article's graph is an island: the same idea in two articles has two ids and usually two labels.
- **Topics:** six, used 94, 68, 60, 55, 34 and 33 times. Coarse but clean.

This is the work that makes deterministic search good, and it is part of the brief, not a side task.

## What to build

### 1. The data layer, built at release

A new builder, `admin/build/explore_index.py`, run in the release after `summaries` and `reviews`, writes `explore/`:

- `explore/ontology.json`: the node types and relations below, versioned. Every other file refers to it.
- `explore/nodes.json` and `explore/edges.json`: one graph for the whole site, compact (short keys, ids as integers into a string table), with the articles and everything they connect to.
- `explore/terms.json`: the vocabulary: each term's folded form, stems, aliases, document frequency, and its top co-occurring terms with counts (for suggestions).
- `explore/triples.nt`: the same graph as RDF, for SPARQL.
- `explore/tables.json`: the same graph as tables, for SQL, with the spec shared with the build in the same way `databases/data/tables.json` is.
- `explore/stats.json`: counts per type and relation, sizes, the build time, and the taxonomy report (below).

Node types (canonical ids in brackets):

| Type | From | Id |
|---|---|---|
| article | `ids.json` | `a:<n>` |
| section | `summaries/<slug>.json` and the page's h2 ids | `a:<n>#<section id>` |
| idea | graph nodes | `a:<n>:<node id>`, clustered into `i:<slug>` (below) |
| tag | front matter tags, normalised | `t:<tag>` |
| topic | the six topics | `p:<topic>` |
| trail | `trails.json` | `r:<trail>` |
| figure | `!shot` lines: file, caption, size, kind | `f:<file>` |
| entity | people, organisations, products, places, standards (below) | `e:<slug>` |
| source | external domains linked from articles | `d:<domain>` |
| wire story | wire JSON | `w:<id>` |
| review | `reviews/status.json` | `v:<file>` |

Relations: `has-section`, `has-idea`, idea-to-idea relations as the graphs name them (`leads-to`, `example-of`, `extends`, `answers`, `contrasts`, `depends-on`, `produces`, `compared-with`), `links-to` (article to article, from `links.articles` and from body links, kept apart), `in-trail`, `tagged`, `in-topic`, `has-figure`, `mentions` (article or story to entity), `cites` (article to source domain), `same-as` (idea clusters), `reviewed-by`.

**Idea clusters.** Deterministic only: normalised labels (case, punctuation, plural, a stop list) that match; labels that match an alias in a curated file, `admin/content/explore/aliases.json`; and nothing else. Every cluster lists its members, so a wrong merge is visible and fixable by editing the aliases file. No embeddings.

**Entities.** A curated gazetteer, `admin/content/explore/entities.json`: each entity's id, name, type, aliases and URL (start from the names the wire already gives long-lived ids, the companies in the articles' sources, and the places in the Portugal section). Matching is exact on names and aliases, word-bounded and case-aware, in titles, teasers, headings, section lines and graph labels. A mention records where it was found.

**The taxonomy report.** `stats.json` lists: tags used once; near-duplicate tags; ideas that cluster across articles and labels that almost do; entities never mentioned; articles with fewer than N connections. It is printed by the builder and shown on a page, so Dinis can see the debt shrink release by release. Merging duplicate tags in the sources is in scope; each merge is a line in the release notes.

**Budget.** The core files (`ontology`, `nodes`, `edges`, `terms`) under 1.5 MB uncompressed in total, loaded once and cached; `text.json` and the RDF only when a view needs them. Measure and print the sizes at build.

### 2. The page: `/explore/`

A new page, linked from the nav's Search and from `/search/`, which keeps working as it is. One layout, three areas:

- **The query bar** builds a query out of chips. Typed words resolve, deterministically, to things: *Portugal* is offered as the entity Portugal, the Portugal wire, the tag `portugal`, and the words. Choosing one makes it a chip; a chip can be an entity, a tag, a topic, a trail, an idea cluster, an article, a date range or free words. Chips combine with AND by default; a chip can be negated.
- **The side: suggestions.** As the reader types, and after every chip, the side lists, with counts that are exact: what the words could mean (the resolutions above); what sits nearest (the top neighbours of the current chips in the graph, by relation); and combinations worth following (pairs and triples of the current chips with co-occurring tags, entities and ideas, ranked by how many articles have both and by lift over chance). Every suggestion is one click to add as a chip. Nothing is suggested that would return nothing.
- **The views of the result**, as tabs over the same result set:
  1. **Graph.** Cytoscape: the chips at the centre, the matching articles, their ideas and the entities around them; click to expand a node's neighbourhood; select two nodes to show the shortest paths between them ("how is Portugal connected to vaults?"). Limit what is drawn (about 300 nodes) and say what was left out.
  2. **Sections.** The matching sections, each as its one-line summary, grouped by article, expanding to the paragraph and linking to the section. This is the "mini sections" view.
  3. **Figures.** A collage of the figures from the matching articles, at thumbnail size, with captions on hover or tap; a click opens the article at the figure.
  4. **Timeline.** The matching articles and stories by date, with trails drawn as lines.
  5. **List.** The ranked list, using today's BM25 over the matching set, so nothing that works today is lost.
- **The walk.** Every step (a chip added, a node expanded, a path asked for) is kept as a breadcrumb trail above the views, and the address keeps the whole query, so a walk can be linked to and continued.

### 3. The inspector pane

A pane that opens from the side, for Dinis and power users. It shows, live:

- **What was fetched**: every file, its size, whether it came from the cache, and the time to fetch and to parse.
- **The query plan**: the chips, the node ids they resolved to and why (which alias, which rule), and each traversal step with how many nodes it touched.
- **Why each result is there**: the path or the fields that brought it in, and its score broken down.
- **The same query as SQL and as SPARQL**, generated from the chips, with an editor to change and run either over the loaded data (sql.js and Oxigraph, already vendored, loaded only when the tab is opened).
- **Stats**: nodes and edges loaded, memory used where the browser reports it, time per stage (load, index, resolve, traverse, rank, draw), and the build's `stats.json`.
- **Export**: the whole state as JSON, to attach to feedback.

The pane publishes `window.__tools.explore` after a `tool:ready` event, as the SQL console does, so Playwright and agents use the same surface as people.

### 4. Feedback, and the queries that define "good"

- On every suggestion and result: *expected*, *not expected*, *missing something*, sent as notes through the existing lane, with the query and the inspector's export attached.
- `admin/content/explore/queries.json`: a set of queries written by Dinis, starting with about twenty, each with the articles, sections or entities he expects to see. `explore_index.py` runs them at build and prints recall at 10 for each; the release notes carry the numbers, and a query that gets worse is called out. This is how Dinis's feedback becomes a test, and how the taxonomy work shows its effect.

### 5. Later, not in this version

- **A model on top.** The graph as the retrieval: the chips and the subgraph they select, serialised, go to the model with the question; the inspector shows exactly what it was given. Chrome's built-in model or the reader's own key, as Ask does today.
- **A comparison with vectors.** The same golden queries answered with an embedding index over the same text, recall side by side, published as an article. The hypothesis to test: on this corpus, a clean graph with deterministic resolution matches or beats vectors, and a model on top of the graph beats a model on top of vectors.
- **Infographics** generated from a walk.

## Constraints

- Everything runs in the reader's browser; nothing is sent anywhere, except feedback the reader chooses to send.
- No model, no embeddings, no remote calls in this version.
- Works at 390px wide: the side becomes a drawer, the views stay usable, the graph is pannable and the page does not scroll sideways.
- Every count shown is exact, and comes from the loaded data, not from an estimate.
- Wording on the page follows the article README (no em-dashes; British English; no superlatives).

## Tests

- `admin/build/test_explore.mjs` (Playwright): typing *Portugal* offers the entity, the wire and the tag, each with a count that matches the data; choosing the entity draws the graph with the Portugal articles and stories; adding a second chip narrows the result and the counts agree; the sections view shows one-liners that link to real anchors; the figures view shows only figures from the result; the inspector lists every fetched file with a size and a time, and its SQL and SPARQL return the same article set as the page; nothing overflows at 390px; `window.__tools.explore` answers the same query with the same ids.
- The build fails if an edge points at a missing node, if an alias maps to two entities, or if a golden query's recall falls below the floor recorded beside it.

## Order

1. The data layer, the ontology and the taxonomy report, with the tag merges that are obvious.
2. The query bar, the suggestions and the list and sections views.
3. The graph view, the walk, and the figures collage.
4. The inspector, with SQL and SPARQL.
5. Feedback, and the golden queries with recall at build.

## Questions for Dinis

- The first twenty golden queries: which searches should work, and what should each find?
- Should `/explore/` replace `/search/` in the nav, or sit beside it until it has proved itself?
- Which entities matter most to start the gazetteer: people, companies, standards, places?
