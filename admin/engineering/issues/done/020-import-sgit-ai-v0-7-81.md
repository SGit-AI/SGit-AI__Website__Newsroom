---
id: 020
title: Import sgit.ai v0.7.81: two articles, the records ran out and sovereignty is the ability to move
kind: task
priority: normal
created: 2026-10-12T17:30:00Z
source: the owner, in chat, 12 October 2026: "can you do another sync with sgit.ai since we have a couple more articles since"
release: v0.12.3
estimated_effort: small
---
# Import sgit.ai v0.7.81: two articles, the records ran out and sovereignty is the ability to move

## What is asked
Two articles were published on sgit.ai after the import of v0.7.79 (card 019): bring them here with their numbers.

## Scenario
```gherkin
Given sgit.ai is at v0.7.81 and this site last imported v0.7.79
When the sync runs and the articles are numbered
Then the two new articles carry numbers 93 and 94 in the order sgit.ai published them
And every imported page is byte-identical to its source apart from the import's own rules
And the article numbers 1 to 92 are unchanged
And the nine test files and the validator pass
```

## Outcome
Shipped in v0.12.3: 1,724 files and 392 pages imported, 94 articles, 803 files written, none removed. Number 93, The records ran out; number 94, Sovereignty is the ability to move. The gate checked the imports unedited and the numbers held.
