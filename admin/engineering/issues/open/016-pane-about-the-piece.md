---
id: 016
title: The pane about the piece: the article's graph, the marks and the cost in the pane
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: 
estimated_effort: large
---
# The pane about the piece: the article's graph, the marks and the cost in the pane
## What is asked
The brief's second item (The site is an inbox) and the modes of Ways to read one article: on an article, the pane shows its graph, the reader's marks and decisions, and what it cost; the ways in (headlines, facts, relationships, what is new) computed from the files this site already publishes.

## Scenario
```gherkin
Given I am on an article
When I open the pane
Then a Piece tab shows the article's graph drawn from articles/graphs/<slug>.json, my marks on it, and the cost so far
And a row of modes: headlines, facts, relationships, vocabulary, and the five readers' views where they exist
```
