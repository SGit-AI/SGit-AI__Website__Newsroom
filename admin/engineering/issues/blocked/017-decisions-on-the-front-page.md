---
id: 017
title: The decisions at each piece on the front page
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: 
estimated_effort: medium
blocked_on: the front page is imported from sgit.ai unedited; the cards' markup is theirs. Either sgit.ai adds a hook for a per-card slot, or this site injects the row at build from the imported page's structure, which the import gate would have to allow
---
# The decisions at each piece on the front page
## What is asked
The brief's first item names the front page and the wire. The wire has the decisions since v0.12.0; the front page does not.

## Scenario
```gherkin
Given I am on the front page
When I look at a piece
Then the decisions are at it, as on the wire, and a decided piece folds
```
