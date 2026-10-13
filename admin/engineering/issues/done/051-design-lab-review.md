---
id: 051
title: The Newsroom Design Lab, reviewed against v0.12.13
kind: task
priority: normal
created: 2026-10-13T13:20:00Z
source: the owner, in chat, with the lab's handover zip and its vault keys: "review the work and vaults created by another claude agent (based on a version of the site that was a bit older than the current one), and see what we can use and explore from it"
release: v0.12.31
estimated_effort: small
---
# The Newsroom Design Lab, reviewed against v0.12.13

## What is asked
Another Claude session (11 to 13 October) ran a UX review of the site at v0.6.4 and built four SGit vaults of prototypes, three design directions each, with a shared kit. Review the handover, open the vaults, and say what the site can use now that it is at v0.12.13.

## Scenario
```gherkin
Given the handover zip and the vaults' read keys
When the review is done
Then every vault has been cloned by its read key and compared with the zip
And every finding of the UX review has been checked against today's built tree
And the note says what to take, in what order, and what not to do
And no write key is anywhere in the repository
```

## Outcome
The note is `admin/notes/2026-10-13__design-lab-review.md`. The four vaults match the zip and open in the host; the review's asks are mapped against what shipped since v0.7.1 (the pane, the lane, Ask, Search); four of its ten bugs are fixed and five still hold; the order to take things is the data (desks, tags, series, formats), the written words (personas, purpose, masthead), three small live fixes, the reader-primitive patterns, the direction decision, then the kit's escaping template.
