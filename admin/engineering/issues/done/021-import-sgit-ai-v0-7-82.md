---
id: 021
title: Import sgit.ai v0.7.82: one article, not a straight line
kind: task
priority: normal
created: 2026-10-12T18:10:00Z
source: the owner, in chat, 12 October 2026: "can you update it again?"
release: v0.12.4
estimated_effort: small
---
# Import sgit.ai v0.7.82: one article, not a straight line

## What is asked
One article was published on sgit.ai after the import of v0.7.81 (card 020): bring it here with its number.

## Scenario
```gherkin
Given sgit.ai is at v0.7.82 and this site last imported v0.7.81
When the sync runs and the articles are numbered
Then the new article carries number 95
And every imported page is byte-identical to its source apart from the import's own rules
And the article numbers 1 to 94 are unchanged
And the nine test files and the validator pass
```

## Outcome
Shipped in v0.12.4: 1,733 files and 394 pages imported, 95 articles, 799 files written, none removed. Number 95, Not a straight line. The gate checked the imports unedited and the numbers held.
