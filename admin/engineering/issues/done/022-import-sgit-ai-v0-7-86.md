---
id: 022
title: Import sgit.ai v0.7.86: two articles, and the owner's correction to Who owns the words
kind: task
priority: normal
created: 2026-10-13T09:00:00Z
source: the owner, in chat, 13 October 2026: "can you import the last document?", after asking for one sentence of Who owns the words to change ("I have not stopped thinking about" was over the top and not what happened)
release: v0.12.5
estimated_effort: small
---
# Import sgit.ai v0.7.86: two articles, and the owner's correction to Who owns the words

## What is asked
Bring the articles published on sgit.ai after v0.7.82 (card 021) here. The owner had asked the sgit.ai session to change one sentence of Who owns the words; that change was made on sgit.ai, where the article lives, and arrives here with the import. The owner also said this should be among the last imports: a brief is being written so that articles are written in the newsroom directly.

## Scenario
```gherkin
Given sgit.ai is at v0.7.86 and this site last imported v0.7.82
When the sync runs and the articles are numbered
Then What open source is, and is not carries number 96 and Who owns the words number 97
And Who owns the words is at its third version, without "I have not stopped thinking about"
And every imported page is byte-identical to its source apart from the import's own rules
And the article numbers 1 to 95 are unchanged
And the nine test files and the validator pass
```

## Outcome
Shipped in v0.12.5: 1,756 files and 400 pages imported, 97 articles, 817 files written, none removed. Number 96, What open source is, and is not; number 97, Who owns the words, at v1.2.0: the sentence now reads "a digression that deserves a proper answer" (sgit.ai v0.7.85), and the section on addressing the agents directly is rewritten (v0.7.86). Its earlier versions are on its version page. The gate checked the imports unedited and the numbers held.
