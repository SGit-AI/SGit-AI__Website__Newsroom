---
id: 026
title: The wire's vault publishes data/releases.json on every publish
kind: task
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.14
estimated_effort: small
---
# The wire's vault publishes data/releases.json on every publish
## What is asked
On every publish, the wire's agent adds a release entry at the top of `data/releases.json`, in the same commit: id, time, edition, title, a plain-text summary, and the story ids added, updated and withdrawn. The schema, an example and the message to pass on are in [the brief](../../admin/notes/2026-10-13__the-wire-as-an-inbox.md).

## Scenario
```gherkin
Given the wire's agent publishes a new edition to the vault
Then data/releases.json has a new first entry with the same id as the commit message
And newsroom.sgit.ai shows it at the top of the wire within two minutes, with no release of the site
```

## Outcome
Done on the vault's side on 13 October 2026, in the wire's commit `2026-10-13.1 update edition: 19 new stories, 13 updated after primary sources were fetched; releases.json added` (head `8a56ece9fe58`): `data/releases.json` is `wire-releases/v1` with two entries, `2026-10-13.1` (19 added, 13 updated, none withdrawn, a summary written for the named reader) and `2026-10-11.1`, written the same day for the first edition and saying so. The commit message starts with the release id, and the vault's runbook now carries the step (its step 11), so every run writes one. The site had read the file since v0.12.6 and showed it with no change; v0.12.14 pins it: `test_wire.mjs` checks the bar shows the releases with each added or updated id linked to its story, and that every story a release names as updated is flagged. The summary also told the reader something the site could not: that the desk could not read their lane, so their decisions are not reflected yet (card 030).
