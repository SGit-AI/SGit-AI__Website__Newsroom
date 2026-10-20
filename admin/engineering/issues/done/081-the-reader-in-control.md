---
id: 081
title: The reader in control: pause, reset, and sections marked by hand
kind: feature
priority: high
created: 2026-10-17T10:00:00Z
source: the owner, in chat, 17 October 2026: "Charge based on what you read, not based on what you scroll ... allow me to reset the timers ... allow the user to pause it ... add a visual clue for what's been marked as read ... 3 or 4 variations or 5 ... hide it completely ... show just like a line of it ... show a small paragraph ... every paragraph that you already captured, you need to have that one-liner ... needs to have a paragraph and needs to have the whole content"
release: v0.12.99
estimated_effort: small
---
# The reader in control: pause, reset, and sections marked by hand

## Scenario
```gherkin
When the reader pauses measuring
Then nothing is measured on any page until they resume, across reloads, and the chip shows it
When the reader resets a page
Then every section is unread again and the meter refunds the page to its minimum
When the reader marks a section read, or unread
Then it counts as read, or its time goes back to zero, and the map says it was marked by hand
```

## Outcome
`assets/reader/strip.js` v3: `sgit.reading.paused`; absolute writes for a reset and a mark, then the `sgit-reading` event; the controls in the map and in the bar at the top. Test: `admin/build/test_reading.mjs`.
