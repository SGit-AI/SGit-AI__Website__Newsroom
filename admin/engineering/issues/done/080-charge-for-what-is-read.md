---
id: 080
title: The meter charges for what is read: sg-meter v1.5.0
kind: feature
priority: high
created: 2026-10-17T10:00:00Z
source: the owner, in chat, 17 October 2026: "Charge based on what you read, not based on what you scroll ... allow me to reset the timers ... allow the user to pause it ... add a visual clue for what's been marked as read ... 3 or 4 variations or 5 ... hide it completely ... show just like a line of it ... show a small paragraph ... every paragraph that you already captured, you need to have that one-liner ... needs to have a paragraph and needs to have the whole content"
release: v0.12.99
estimated_effort: medium
---
# The meter charges for what is read: sg-meter v1.5.0

## What is asked
The owner's decision on the question left open by *Scrolled is not read*: charge for the share read, not for the share scrolled.

## Scenario
```gherkin
Given an article opened for the first time
Then a tenth of its price is charged
When the reader flicks to the end in seconds
Then the charge stays at a tenth
When every section is read
Then the full price is charged
When the reader resets the page
Then the charge returns to a tenth
Given an article read on an earlier visit
Then reading already done is not charged again
```

## Outcome
`assets/components/sg-meter/v1/v1.5/v1.5.0/` (a new immutable path; the import re-points every page): the core gains `settle(share)`, which can lower a charge; the page view charges from the reading strip's `sgit-reading` event and the `sgit.reading.v1` record, beyond the entry's `readBase`, and a `reset: true` event sets the base to zero. The foot says what was read on this visit and what was read before. The account page's sentence is corrected by a text rule (`account-lead-read`). Test: `admin/build/test_reading.mjs`.
