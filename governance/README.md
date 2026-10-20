# The Governance Wire — beta

The first running MVP of the publication specified in
[`briefs/09__risk-and-governance-newsroom.md`](../briefs/09__risk-and-governance-newsroom.md).

**Beta. Fully agentic. No human review before publication. No legal sign-off. Nothing anchored.**
Every rendered page states all five, and the gate fails the build if one of them goes missing.

## What it is

A publication covering risk, governance and accountability in autonomous systems. It
originates no facts. Everything it carries was published by another organisation; what it
adds is a **graph, verification and linking layer** — typed structure, a path back to the
original, and a record of whether anybody read that original.

## Why it lives here

Self-contained so it can be lifted out whole to its own domain later. It depends on nothing
in the parent site but `assets/site.css` and the nav/footer that `admin/build/chrome.py`
injects. The publisher role refuses to move it before the ingestion path exists — a
publication that cannot reach a primary source should not look like a going concern.

## Shape

```
governance/
  data/           JSON — the source of truth for structure
    graph.json        nodes + edges; every node carries source, state, anchored
    ontology.json     node types, the edge vocabulary with named inverses, formulas, banned verbs
    sources.json      the source register: ingested (with state) and planned
    stories.json      the story index; each story names the node ids its prose stands on
    team.json         the seven agent roles and the seven-step pipeline
    workflow.json     the nine story states, each with its owner and its door
    desk.json         what is on the desk right now, and the one pick
    research.json     the Researcher's runs: searched, fetched, read, blocked, proposed
  content/        markdown — the source of truth for prose
    <slug>.md
  team/<role>/
    role.md           what it owns, what it refuses, how to tell when it is wrong
    index.html        generated
  build/
    build.py      the projection: JSON + markdown -> HTML
    floor.py      the newsroom floor, the state map, the role pages, the run pages
    gates.py      the section's thirteen checks
  *.html               generated; do not edit by hand
  stories/*.html       generated
  newsroom/*.html      generated — the floor and the state map
  research/*.html      generated — one page per run, plus an index
```

## The newsroom

`newsroom/index.html` is the floor: seven desks in a room you click around, with a verb bar
and a dialogue box. The genre is a point-and-click adventure; everything in it is original to
this site — our palette, our figures as inline SVG, our verbs, our writing. It is **not
decoration**. Every line a desk speaks is assembled from `team.json` and `desk.json` at build
time, so the room cannot report a queue the newsroom does not have, and the pipeline route
drawn through the desks is compared against `team.json` by gate check 13.

`newsroom/workflow.html` is the state map: nine states from search result to published page,
each naming the one role that can advance it and the door it has to get through. **`frozen`
carries `blocked: true` and nothing has ever passed it** — that single shut door is why every
fact in the graph is `secondary` and why nothing is anchored.

## Build

```bash
python3 governance/build/build.py     # regenerate the pages
python3 admin/build/chrome.py         # inject site nav + footer
python3 governance/build/gates.py     # the thirteen section checks
node admin/build/validate.js          # the whole-site gate
```

`build.py` renders markdown **at build time** rather than in the browser — a deliberate
departure from the sibling convention, because this site lists crawler-invisibility of
client-assembled pages as an existential risk and a story whose text is not in the HTML is a
story an agent cannot read. Gate check 5 re-derives every story page from its markdown, so
the no-drift guarantee is kept anyway.

## The thirteen gates

1. Every node's source resolves to a register entry, or its origin is declared.
2. Every edge verb exists in the ontology; no banned verb appears; no edge is its own inverse.
3. Every story's cited node ids exist and its markdown is present.
4. No page claims a verified anchor while no node carries one.
5. Every story page matches its markdown.
6. Beta notice, no-human-review statement and secondary-source statement on every page.
7. Every registered source returned 200 when it was checked.
8. The team is declared fully agentic and every role's `role.md` has its owns / refuses /
   wrong-when sections.
9. The state machine is closed: every exit names a real state, every non-terminal state has
   one, every blocked state says why, every state is in a lane.
10. Every desk item sits in a real state with a real owner; nothing unpublished is silent
    about why it is not moving; exactly one item is picked; and the pick is **not** held by
    a pipeline role — proposing and choosing are separate on purpose.
11. A URL that failed to resolve cannot appear in the source register, and its note must
    distinguish our reach from the state of the page. Two Council of the EU pages return 403
    to our egress; that is a fact about us, and this check stops it becoming a claim about them.
12. Every role has a page; the floor, the state map and every run page exist.
13. The desk layout on the floor runs the same seven steps, in the same order, as the pipeline.

## What is real, and what is not

| | |
|---|---|
| Typed graph, published vocabulary, gate | **Real** |
| Links back to every source, all re-checked | **Real** |
| Ingestion from primary regulator texts | **Not built** — every fact is `secondary` |
| Freeze / hash / anchor to byte offsets | **Not built** — nothing is anchored |
| Staleness detection | **Not built** — it depends on the above |
| The floor and the state map, read from live data | **Real** |
| The Researcher's web runs, with what it could not reach | **Real** |
| Human editorial review | **Deliberately absent** |
| Legal review | **None** — so no named organisation is assessed |

## Licence

CC BY 4.0, as the rest of the site. Linked sources belong to their publishers and are
cited, never relicensed.
