---
id: 046
title: A Portugal wire: the same beats, Portuguese sources and stories, under the same contract
kind: story
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: one more news feed, for Portugal, same topics, AI governance and so on; a source of material for the Portuguese publication
release: 
estimated_effort: medium
blocked_on: the desk building the vault and publishing its read key to the owner; the newsroom adds it with one config file (the brief for the desks, 13 October)
---
# A Portugal wire: the same beats, Portuguese sources and stories, under the same contract
## Scenario
```gherkin
Given a vault for the Portugal wire exists under the contract, with wire.id "portugal"
When its read key reaches the owner
Then admin/build/wire-vault.portugal.json records it and the named reader's agreement
And /wire/portugal/ reads it with no other change
```
