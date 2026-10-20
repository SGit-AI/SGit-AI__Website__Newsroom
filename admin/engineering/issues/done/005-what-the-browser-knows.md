---
id: 005
title: What this browser knows about the page: reads, how far, cost, rating, the decision
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# What this browser knows about the page: reads, how far, cost, rating, the decision
## What is asked
The owner: the right-hand side is "starting to mirror what do I know about this page and what I have seen about this page." The meter already records every read; the pane showed none of it.

## Scenario
```gherkin
Given I have read this page before in this browser
When the pane's This page tab is drawn
Then it says how many times, when last, how far (opened it, glanced, a third, most, all), what it cost and how I rated it
And the decision at the page, when there is one

Given I have not read this page here
Then it says so, by the meter's records
```

## Outcome
Shipped in v0.12.1 as the block above the chips, from assets/vault-pane/reading.js, which only reads the meter's store. Checked by test_notes.mjs.
