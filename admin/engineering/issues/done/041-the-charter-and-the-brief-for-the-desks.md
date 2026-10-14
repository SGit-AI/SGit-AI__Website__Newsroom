---
id: 041
title: The charter of the wires, and a standing brief for the desks
kind: story
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026, transcribed: publish a charter and guidelines with the checks and balances and the principles, for this side and for the agent that writes the vaults; a way to pass notes to the other side
release: v0.12.20
estimated_effort: medium
---
# The charter of the wires, and a standing brief for the desks
## What is asked
A published charter: facts first and analysis on top, corrections that propagate, the rounds of agents and what each enforces, what is never done, public by default. And a channel from the owner, through the newsroom, to the desks that write the vaults: a brief the desk reads at the start of every run, since the newsroom holds no write key to any vault.

## Scenario
```gherkin
Given the owner asks for something of the desks
When the newsroom releases
Then wire/desk-brief.md carries it, dated, newest first, at a URL a runbook can read
And wire/charter.html says what every round enforces, and the pages link both
```

## Outcome
Shipped in v0.12.20: `admin/notes/2026-10-13__the-wires-charter.md` rendered at `wire/charter.html`; `wire/desk-brief.md` rendered at `wire/desk-brief.html`, with the items of 13 October: the schedule, the reader's lane, the verifier on every run (`wire-factcheck/v1`), one list per wire, a Portugal wire, who should know, the release note. The strip on every wire page links both.
