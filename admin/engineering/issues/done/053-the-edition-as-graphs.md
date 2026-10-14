---
id: 053
title: The edition as graphs: a provenance strip per story, the week by beat, the threads on a date axis, who is named twice
kind: story
priority: high
created: 2026-10-13T20:40:00Z
source: the owner's voice memo of 13 October 2026 ("as much graphs as possible"), the desks' docs/GRAPHS.md in every vault, the developer agent's module
release: v0.12.42
estimated_effort: medium
---
# The edition as graphs: a provenance strip per story, the week by beat, the threads on a date axis, who is named twice
## Scenario
```gherkin
Given a wire whose vault holds stories with dates, beats, sources and entities
When I open the edition
Then under every headline a strip of dots shows the primary and each covering source, by licence tier, the quote's source ringed
And the header folds three graphs: the stories per day of the last fortnight by beat, the threads as rows on one date axis, the entities two or more stories name
And every graph is drawn in the browser from the bundle, as SVG made of text nodes, every colour a theme token, so the five themes reach it
And a fault in a drawing is one line of text, never a broken edition
```

## Outcome
Shipped in v0.12.42: `wire/graphs.js` (seven drawings and their six pure tables: provenance strip and graph, co-occurrence, threads timeline, stories by day, sources tally, deliveries matrix), placed in `wire/wire.js` (the strip at the head of each story's meta line; `details#wire-byday`, `#wire-threads`, `#wire-entities` folded in the header), sizes in `wire/wire.css`. Test `admin/build/test_graphs.mjs` (source rules, the tables on a fixture with hostile and malformed shapes, the drawings in Chromium under the Night theme, the four real bundles) in CI, and two checks in `test_wire.mjs` on every wire. The sources tally and the deliveries matrix are exported and tested, placed by the next stage (the overview). Design: `admin/notes/2026-10-13__five-wires-five-pages.md`.
