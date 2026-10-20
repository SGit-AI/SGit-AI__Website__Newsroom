---
id: 014
title: Marks on a phrase, with kinds: interesting, great phrase, not sure, fact, evidence, question
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: 
estimated_effort: medium
---
# Marks on a phrase, with kinds: interesting, great phrase, not sure, fact, evidence, question
## What is asked
The brief's third item. A mark is a note at a phrase with one of six kinds; today a tap keeps the selected phrase as the note's quote, with the feedback kinds, which is half of it.

## Scenario
```gherkin
Given I select a phrase on an article
When I tap a mark kind
Then a note is kept with the phrase, the kind, the article and its version, and the persona
And the pane shows the marks on this page, and the graph beside the article when the pane about the piece exists (016)
```
