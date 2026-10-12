---
id: 013
title: Move a piece to a persona: the seventh decision
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: 
estimated_effort: small
---
# Move a piece to a persona: the seventh decision
## What is asked
The brief's seventh decision (The site is an inbox): a piece goes to another of the reader's personas, so the editor persona and the founder persona keep different lists.

## Scenario
```gherkin
Given I have more than one persona in the meter
When I tap Move to a persona at a piece and pick one
Then a note of kind persona is kept with the persona's id
And the Reading tab can be read as that persona
```
