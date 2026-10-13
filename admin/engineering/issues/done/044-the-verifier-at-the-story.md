---
id: 044
title: The verifier's record drawn at the story, and asked for on every run
kind: story
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: one more round, maybe a different model, to check independence, claims, verifications and facts; the mappings should be very factual, the analysis on top
release: v0.12.20
estimated_effort: small
---
# The verifier's record drawn at the story, and asked for on every run
## Scenario
```gherkin
Given the vault carries data/factcheck-<date>.json
When the file has results[] rows with a story id
Then each row is drawn at its story: the date, the quote's state, the verdict and the fix
And the file's own words (who checked, how, what was not checked) are in the edition's header
Given the file has only a prose result, as the first editions do
Then the prose is drawn in the header as it is
```

## Outcome
Shipped in v0.12.20 on this side: `wire/wire.js` reads every `data/factcheck-*.json`; the contract on each how page names it as optional; the charter's third round and the brief's schema (`wire-factcheck/v1`, one row per story) ask the desks for it on every run. The vault side is the desks'.
