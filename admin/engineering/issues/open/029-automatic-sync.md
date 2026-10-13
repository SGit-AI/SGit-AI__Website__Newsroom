---
id: 029
title: Regular or automatic sync of the reader vault
kind: story
priority: normal
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: 
estimated_effort: medium
---
# Regular or automatic sync of the reader vault
## What is asked
The owner: "first stored locally, and then I'll have a button or a regular sync; but first make it explicit". The button is built (027). A regular sync is the later decision: on a timer, on leaving a page, or when the count passes a threshold, with the pane saying when it last ran.

## Scenario
```gherkin
Given regular sync is switched on for this device
When there are changes only in this browser and the interval has passed
Then the device file is written to the vault as it is by Update the vault
And the pane says when it last ran and what it wrote
```
