---
id: 002
title: A stray “null” is printed under Send to the newsroom
kind: bug
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# A stray “null” is printed under Send to the newsroom
## What happens
Below the warning under Send to the newsroom the word "null" is printed (second screenshot). The lane block is drawn with `replaceChildren(null)` when there is no lane, and a null becomes the text "null".

## Scenario
```gherkin
Given the account has no lane yet
When I press Send to the newsroom and it cannot send
Then the warning is shown and nothing else is printed under it
```

## Outcome
Shipped in v0.12.1. Every place the pane fills an element now drops nulls. Checked by test_notes.mjs on the no-access-key path.
