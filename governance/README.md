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
    team.json         the seven agent roles
  content/        markdown — the source of truth for prose
    <slug>.md
  team/<role>/role.md   what it owns, what it refuses, how to tell when it is wrong
  build/
    build.py      the projection: JSON + markdown -> HTML
    gates.py      the section's six checks
  *.html          generated; do not edit by hand
  stories/*.html  generated; do not edit by hand
```

## Build

```bash
python3 governance/build/build.py     # regenerate the pages
python3 admin/build/chrome.py         # inject site nav + footer
python3 governance/build/gates.py     # the six section checks
node admin/build/validate.js          # the whole-site gate
```

`build.py` renders markdown **at build time** rather than in the browser — a deliberate
departure from the sibling convention, because this site lists crawler-invisibility of
client-assembled pages as an existential risk and a story whose text is not in the HTML is a
story an agent cannot read. Gate check 5 re-derives every story page from its markdown, so
the no-drift guarantee is kept anyway.

## The six gates

1. Every node's source resolves to a register entry, or its origin is declared.
2. Every edge verb exists in the ontology; no banned verb appears; no edge is its own inverse.
3. Every story's cited node ids exist and its markdown is present.
4. No page claims a verified anchor while no node carries one.
5. Every story page matches its markdown.
6. Beta notice, no-human-review statement and secondary-source statement on every page.

Plus: the register's own claims (every source resolved when checked), and every role having
a `role.md` with its owns / refuses / wrong-when sections.

## What is real, and what is not

| | |
|---|---|
| Typed graph, published vocabulary, gate | **Real** |
| Links back to every source, all re-checked | **Real** |
| Ingestion from primary regulator texts | **Not built** — every fact is `secondary` |
| Freeze / hash / anchor to byte offsets | **Not built** — nothing is anchored |
| Staleness detection | **Not built** — it depends on the above |
| Human editorial review | **Deliberately absent** |
| Legal review | **None** — so no named organisation is assessed |

## Licence

CC BY 4.0, as the rest of the site. Linked sources belong to their publishers and are
cited, never relicensed.
