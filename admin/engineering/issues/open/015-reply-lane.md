---
id: 015
title: A reply lane from the newsroom to the reader
kind: story
priority: low
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: 
estimated_effort: large
---
# A reply lane from the newsroom to the reader
## What is asked
Today nothing comes back through the lane; replies are versions and notes on the site. If that proves too slow, a lane the other way: the reader's vault accepts the newsroom's replies through an append lane of its own, drained by the pane.

## Scenario
```gherkin
Given the newsroom has answered a note
When I open the pane
Then the reply is shown under the note it answers, read from my own vault's lane
```
