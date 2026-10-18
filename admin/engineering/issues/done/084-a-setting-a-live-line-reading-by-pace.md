---
id: 084
title: The view of what was read as a setting, a live margin line, reading by pace, and no jump when scrolling back up
kind: feature
priority: high
created: 2026-10-18T01:00:00Z
source: Dinis, in chat, 18 October 2026, after a day of use: "Don't put that top banner with the multiple options in the top ... that should be a general top level setting, and it should be also overwritten by article ... on the UX on the right ... make it a little bit bigger ... add a config section there"; "when I have ... the ones that collapse things ... the screen moves ... as soon as I scroll up a little bit ... where am I moved ... that's very confusing"; "that little bar on the left ... Can you change its color automatically in real time? ... from that light color to the current color ... that's the only one that should change"; "the faded ... shouldn't fade ... or else it fades halfway through I'm reading"; "if the user is scrolling up slowly, that indicates the article's been read ... if I scroll up a certain speed, you can assume that it's not ... by the time I got to the end ... I got that 100% mapping, and it's okay to give me that visual clue"
release: v0.12.110
estimated_effort: medium
---
# The view of what was read as a setting, a live margin line, reading by pace, and no jump when scrolling back up

## What is asked
Five changes to card 082's views and card 081's strip, after a day of use:

1. No bar at the top. The view is a setting made once: one for every article, which any article can override, in the panel on the right, larger, with a settings section.
2. The folding views (Paragraph, Line, Hidden) must never move the page under the reader. Scrolling back up a little threw the reader elsewhere.
3. The margin line changes colour as the reader reads, smoothly, from a light tint to the solid colour. It is the only view that changes live.
4. Faded must not fade a section the reader is part way through.
5. A slow scroll, either way, is a signal of reading; a fast one is not. Reaching the end at a reading pace gives 100%, and that is shown.

## Scenario
```gherkin
Given a reader with Line chosen, part way down an article, the first sections read
When they scroll back up with a trackpad or a phone, the scroll still moving
Then nothing on the page changes while it moves
And once the page has been still for 0.7 seconds, the sections read above fold
And the words on screen do not move

Given a reader in Margin
When they read a section
Then the line beside it goes from pale to solid in steps of 5%, slowly
And a tick appears beside its heading when it is read in full

Given a reader who scrolls through an article at about 320 words a minute
Then every section counts as read by pace, the page reaches 100%, and the chip's dot becomes a tick
But the same scroll at four times the speed counts by pace only its first few seconds

Given the chip's panel
When the reader opens Settings
Then they see the six views for every article, each with what it does, a choice for this article alone, and Pause
And the choices are kept in this browser
```

## Outcome
- `assets/reader/folds.js` rewritten. LIVE: the margin, from `R.sections()` every second, `--rf-p` in steps of 5% and `rf-done` with a tick on the first node; drawn as `::before`, a colour only. PASSES: fade, fold or hide change the page only in a pass: on arriving with something read, after a scroll back up of half a window (from the deepest point since the last pass), or when the reader asks. STILLNESS: a pass waits until there has been no scroll, wheel or touch for 700 ms and no finger down (scroll events and a 250 ms poll of `scrollY`; the page's own correction is not counted as the reader moving). The pass decides which sections are on screen for all of them first, then notes the first element on screen, changes the page, corrects the scroll by what that element moved, with `overflow-anchor: none` for that frame. Only sections read in full fade or fold. No bar. Settings: `sgit.reading.view` (every article) and `sgit.reading.views` (by path, at most 400).
- `assets/reader/strip.js` v4: PACE. The reading line runs from the top of the page at scroll 0 to its foot at the end; text passing it is credited from a budget earned at 450 words a minute while attended, capped at 60 words; a movement that passes more than the budget counts nothing and spends it; a move of more than a window counts nothing. A section passed for 95% of its words at pace is passed. A section's read is the larger of time and pace (`pw` in `sgit.reading.v1`). Reset and marks set it. The chip shows ✓ at 100%. The panel has two tabs, This page and Settings, and is larger (520 by 720 pixels at most).
- `assets/reader/strip.css`: the live line (`color-mix` in oklab between `--line2` and `--accent`, a 1.6 s transition, none with reduced motion), the tick clear of the line, the tabs and the settings list; the bar's styles gone; tokens only.
- The cause of the jump, measured: a smooth scroll of 1,400 pixels back up in Line moved the heading more than 3,500 pixels in one frame. Two causes: sections asked one by one whether they were on screen while the ones above folded (the one in view moved up, was folded too, and took the anchor with it), and a correction made under a scroll still in motion.

Tests: `admin/build/test_reading.mjs` (the real-time smooth-scroll test in Line and Hidden; nothing while moving; Settings for every article and for one; Faded only read in full; the live margin; pace: a slow scroll to 100% with the tick, four times the speed, a jump, paused); `admin/build/test_pane.mjs` (the new keys). The article *Your reading, your controls* has an update section.
