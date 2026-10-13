---
id: 026
title: The wire's vault publishes data/releases.json on every publish
kind: task
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: 
estimated_effort: small
blocked_on: the wire's agent, which holds the vault's write key; the owner relays the message at the end of the brief
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
