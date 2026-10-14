---
id: 057
title: The overview at /wire/: the four wires as tiles, one lens across them, the week as small multiples; the Industry Wire moves to /wire/industry/
kind: story
priority: high
created: 2026-10-14T16:05:00Z
source: the owner's voice memo of 13 October 2026 ("when I go to the wires main one, I should see the four wires or a nice overview of them"); the design note
release: null
estimated_effort: large
blocked_on: the owner's yes to moving the Industry Wire to /wire/industry/ (the old address keeps a line saying where it went; the inbox state and the notes carry over)
---
# The overview at /wire/: the four wires as tiles, one lens across them, the week as small multiples; the Industry Wire moves to /wire/industry/
## Scenario
```gherkin
Given four wires each with its own page
When I open /wire/
Then I see what the desks released today across the wires, the four wires as tiles with their leads and counts, one lens across all of them, the best of today, the week as small multiples per wire, and what the pictures cost
And the Industry Wire is at /wire/industry/, its old address saying so, nothing of the reader's state lost
```
