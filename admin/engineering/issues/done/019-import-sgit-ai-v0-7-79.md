---
id: 019
title: Import sgit.ai v0.7.79: eight articles, two decks, and the figures in every article's graph
kind: task
priority: high
created: 2026-10-12T16:40:00Z
source: the owner, in chat, 12 October 2026: "do another migration from sgit.ai, since we have quite a good number of articles and I want to do a bunch of follow-ups that should be sending links from there"
release: v0.12.2
estimated_effort: small
---
# Import sgit.ai v0.7.79: eight articles, two decks, and the figures in every article's graph

## What is asked
Bring sgit.ai's newsroom up to date on this site, so that follow-ups can send links to the new articles here. sgit.ai went from v0.7.70 to v0.7.79 in the afternoon of 12 October: eight new articles, two decks under articles/decks/, and the figures added to every article's graph (v0.7.77), which touches most article pages.

## Scenario
```gherkin
Given sgit.ai is at v0.7.79 and this site last imported v0.7.70
When the sync runs and the articles are numbered
Then the eight new articles carry numbers 85 to 92 in the order sgit.ai published them
And every imported page is byte-identical to its source apart from the import's own rules
And the article numbers 1 to 84 are unchanged
And the nine test files and the validator pass
```

## Outcome
Shipped in v0.12.2: 1,703 files and 388 pages imported, 92 articles, 930 files written, none removed. Numbers 85 to 92: the key is the billing system; from a spreadsheet to a folder per person; how the voice works; agentic cost is an engineering problem; places of highest leverage; why I love Wardley maps; judo for small countries; move the cloud, not the code. The decks (reading one map; why I love Wardley maps) came with the articles folder. The gate checked the imports unedited and the numbers held.
