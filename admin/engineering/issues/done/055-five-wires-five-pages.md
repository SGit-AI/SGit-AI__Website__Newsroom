---
id: 055
title: Five wires, five pages: the design note and the staged plan for the wires' UX
kind: design
priority: high
created: 2026-10-13T20:30:00Z
source: the owner's voice memo of 13 October 2026 ("take a step back... fire up a designer agent and a developer agent and an architect agent... four different complete UX for each of these wires, actually a fifth one for the top one")
release: v0.12.42
estimated_effort: medium
---
# Five wires, five pages: the design note and the staged plan for the wires' UX
## Scenario
```gherkin
Given four wires on one code and the owner's ask for a complete UX per wire and an overview above them
When the architect, the designer and the developer have each answered the brief
Then one note synthesises them: what the data holds, measured; every graph it can carry and where each is computed; the infographic pipeline and its cost; the decisions taken and the ones that need the owner; the stages
And the designer's mock-ups and screenshots on the real vault data sit beside it
```

## Outcome
Published in v0.12.42: `admin/notes/2026-10-13__five-wires-five-pages.md`, with `admin/notes/wires-ux/architecture.md`, `design.md` and six screenshots. Stage one (the module and the first placements) ships with this release; stage two, the overview at `/wire/` with the Industry Wire moving to `/wire/industry/`, waits on the owner's yes (card 057); stage three, the pictures, on the key (card 056).
