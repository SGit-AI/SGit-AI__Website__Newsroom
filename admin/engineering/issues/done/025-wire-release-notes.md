---
id: 025
title: The wire's release notes at the top of the wire: the releases since the last visit
kind: story
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.6
estimated_effort: small
---
# The wire's release notes at the top of the wire: the releases since the last visit
## What is asked
The owner will ask the wire's agent to update the vault and describe what changed, as a release; the newsroom should show it.

## Scenario
```gherkin
Given the wire's vault has data/releases.json with releases newer than my last visit
When I open the wire
Then the bar lists those releases, newest first: title, time, summary, the stories added and updated, each linked to its story
And updated stories carry an Updated flag

Given no release is newer than my last visit
Then the bar shows the latest one

Given the vault has no data/releases.json
Then the bar shows the head commit's message and says the vault publishes no release notes yet, linking the brief
```

## Outcome
Shipped in v0.12.6 on this site's side. The contract is "The release file" in [the brief](../../admin/notes/2026-10-13__the-wire-as-an-inbox.md); the selection is `releasesSince` in wire-state.js, tested in test_sync.mjs. The vault side is card 026.
