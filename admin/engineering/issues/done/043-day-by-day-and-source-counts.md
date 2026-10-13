---
id: 043
title: Every wire day by day, and how many stories each source gave
kind: story
priority: normal
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: a page with sources, visualised as what updated, what happened on each day
release: v0.12.20
estimated_effort: small
---
# Every wire day by day, and how many stories each source gave
## Scenario
```gherkin
Given the wires' vaults date every story and every release
When I open wire/days.html
Then every wire's releases and stories are listed by the day they are dated, newest first, each story by its source and tier, linked to its wire page
And each wire's sources page says how many stories each source gave this edition
```

## Outcome
Shipped in v0.12.20: `wire/days.html` reads every vault (the config carries the wires); the sources pages gain a Stories column. Checked in `test_wire.mjs`.
