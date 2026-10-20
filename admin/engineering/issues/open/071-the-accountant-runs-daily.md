---
id: 071
title: The accountant runs daily: a session of its own records every run's cost and releases the costs page
kind: story
priority: high
created: 2026-10-16T12:15:00Z
source: card 070
release: null
estimated_effort: small
---
# The accountant runs daily: a session of its own records every run's cost and releases the costs page
## Scenario
```gherkin
Given a session of its own with the tools that read a session's usage and result
When it wakes each morning after the desks and the newsroom have run
Then it adds a row per new run to admin/build/wire-runs.json with runs_ledger.py, rebuilds the costs page and releases it
```
