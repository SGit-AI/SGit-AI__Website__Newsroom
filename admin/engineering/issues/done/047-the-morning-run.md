---
id: 047
title: The newsroom's morning run: a routine that refreshes the wires every day at seven
kind: task
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: put these on a schedule, something that runs every day at seven in the morning
release: v0.12.20
estimated_effort: small
---
# The newsroom's morning run: a routine that refreshes the wires every day at seven
## What is asked
The desks' runs are theirs to schedule (the brief asks for seven, London). This side's run: every morning, clone every wire's vault, compare with the snapshots, refresh them, rebuild, test, and release when something changed; read the brief for the desks for anything that is this side's.

## Scenario
```gherkin
Given a routine fires a fresh session every day at seven (London)
When a wire's vault has a new commit since the last snapshot
Then the snapshots are refreshed, the site rebuilt and validated, the wire test run against the real vaults, and a patch release pushed to dev
And when nothing changed, nothing is pushed and the run says so
```

## Outcome
Shipped in v0.12.20 outside the repository: a routine on the owner's account, created by the newsroom's agent in the session that built this release, firing a fresh session in the same environment every day at seven (London, a few minutes early), with the steps above as its prompt: routine `trig_01H41yFnc3ZmuahVDLaPkCYr`, cron `CRON_TZ=Europe/London 56 6 * * *`, first run 14 October 2026 at 06:56 London. The owner can pause or edit it from the routines list. It holds no connectors and needs none: git and the vault server are all it reaches. The desks' own runs are theirs to schedule; the brief asks them for seven.
