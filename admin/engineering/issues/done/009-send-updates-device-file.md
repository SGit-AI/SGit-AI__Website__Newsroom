---
id: 009
title: A send should update this device's file too, so other devices see the notes as sent
kind: bug
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# A send should update this device's file too, so other devices see the notes as sent
## What happens
Sent marks were only carried by the next Update, so a second device saw notes as unsent after a send, and the note sent after the last update was not in the vault at all.

## Scenario
```gherkin
Given the reader vault is open
When I send notes to the newsroom
Then this device's file in the reader vault is rewritten in the same action
And another device that brings my activity in sees every sent note as sent
```

## Outcome
Shipped in v0.12.1. Checked by test_notes.mjs on device B.
