---
id: 070
title: Every run costed: the platform's own cost and tokens for each scheduled run, on the costs page
kind: story
priority: high
created: 2026-10-16T12:10:00Z
source: the owner, 16 October 2026: "every run that happens should be capturing the cost, the tokens, and everything that happens with it"
release: v0.12.74
estimated_effort: small
---
# Every run costed: the platform's own cost and tokens for each scheduled run, on the costs page
## Scenario
```gherkin
Given the scheduled runs of the desks and the newsroom
When the accountant reads each run's session usage and final result
Then admin/build/wire-runs.json holds a row per run: when, the task, the cost and the tokens per model, the turns, the subagents, what the permission check refused (by kind, never the command's arguments) and what it published
And the costs page shows the runs by task, by model and one by one, with the working sessions that built the wires counted apart
```

## Outcome
Shipped in v0.12.74: `admin/build/runs_ledger.py` (adds a run, refuses a row shaped like a key), `admin/build/wire-runs.json` with the runs of 14 to 16 October, and the runs section of `wire/costs.html`. Kept current by the accountant (card 071).
