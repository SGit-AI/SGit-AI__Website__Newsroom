---
id: 073
title: Scrolled is not read: two measures per section, and a chip that holds still
kind: feature
priority: high
created: 2026-10-16T09:00:00Z
source: the owner, in chat, 16 October 2026: "on the bottom little pane that you added... you shouldn't show the total... It flickers... the percentage that you scroll and the percentage that you read... think of the page as a graph... which articles I read, which I don't read, which articles I highlight... a separate section for articles that are written by agents"
release: v0.12.85
estimated_effort: medium
---
# Scrolled is not read: two measures per section, and a chip that holds still

## What is asked
The chip at the foot of every article (card 066) repeated the balance the bar shows, flickered as the page scrolled, and showed the window's position on the page, which fell when the reader scrolled back up. Show what the reader did, not where they are: how much was scrolled and how much was read, kept per section, in the browser.

## Scenario
```gherkin
Given an article the reader flicks to the bottom in a few seconds
Then it is nearly all scrolled and nearly none of it read
Given a section kept in the middle of the window while the reader is active and the tab in front
Then its time grows, and read grows with it, against its words at 300 a minute
Given a reader who stops for more than a minute, or a hidden tab
Then no time is counted
When the reader scrolls back up
Then scrolled does not go down
And the chip shows scrolled, read and the page's cost, no balance, and does not move
And tapping it opens the page as its sections
```

## Outcome
`assets/reader/strip.js` v2: sections from the article's headings; a one-second clock shares attended time among the sections in the reading band (15% to 85% of the window, the whole window at the foot); scrolled kept as a maximum per section; both word-weighted; kept under `sgit.reading.v1` (at most 400 pages), merged across tabs. The chip is a button with values in fixed-width boxes and tabular figures, written only when they change: 20 positions in 30 scroll steps before, one after. The hairline shows scrolled pale and read solid. The meter's charging is unchanged. Test: `admin/build/test_reading.mjs`. Design and plan: the article *Scrolled is not read*.
