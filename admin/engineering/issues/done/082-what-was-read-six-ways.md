---
id: 082
title: What was read, shown six ways, and never while reading forward
kind: feature
priority: high
created: 2026-10-17T10:00:00Z
source: the owner, in chat, 17 October 2026: "Charge based on what you read, not based on what you scroll ... allow me to reset the timers ... allow the user to pause it ... add a visual clue for what's been marked as read ... 3 or 4 variations or 5 ... hide it completely ... show just like a line of it ... show a small paragraph ... every paragraph that you already captured, you need to have that one-liner ... needs to have a paragraph and needs to have the whole content"
release: v0.12.99
estimated_effort: medium
---
# What was read, shown six ways, and never while reading forward

## What is asked
A visual clue for what has been read, in three to five variations to compare; only after the reader scrolls back up, or comes back; including hiding what was read, showing a line, and showing a paragraph.

## Scenario
```gherkin
Given a reader going down an article
Then nothing on the page changes
When they scroll back up by more than half a window, or come back to an article they had read some of
Then the sections they read are shown in the view they chose: Full, Margin, Faded, Paragraph, Line or Hidden
And a section on screen is never folded by the clock
And Show opens a folded section where it is
And the choice is kept in the browser
```

## Outcome
`assets/reader/folds.js` and its styles in `strip.css`: margin lines as `::before`, folds as a class and an inserted block, runs of hidden sections under one marker, the scroll corrected so the words in view stay; the bar at the top with the six views, Pause and Reset. Test: `admin/build/test_reading.mjs`.
