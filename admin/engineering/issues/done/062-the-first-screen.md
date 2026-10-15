---
id: 062
title: The wire's first screen: a front page for a first-time visitor and a screenshot to send
kind: story
priority: high
created: 2026-10-14T22:50:00Z
source: the owner, 14 October 2026: "clean up that industry wire homepage... a user that arrives here for the first time... make it look as professional and as powerful as possible... send screenshots... including on emails"; the designer agent's spec
release: v0.12.70
estimated_effort: medium
---
# The wire's first screen: a front page for a first-time visitor and a screenshot to send
## Scenario
```gherkin
Given a reader who arrives at a wire for the first time
When the page opens
Then the first screen is a masthead and today's edition: the strip of wires, the wire's name, the dateline with the day and "beta", one line with the counts and "ai-generated, unreviewed", then the hero picture beside the editor's note, the threads folded to a line each with their story counts, and the lead's headline
And the desk's record (this edition, corrections, the verifier, the graphs) is one folded row under it
And the inbox bar is one quiet line with the desk's note folded on a first visit, and its full self once the reader has state
And the vault id, the commit, the fetch counts, the re-check button and what the pictures cost are one quiet line at the foot, linked from the dateline
And ?share on the address reduces the page to the masthead and the band for a 1200 by 630 screenshot
And every vault value is still drawn as text, and the AI-image chip with its model and cost stays under every picture
```

## Outcome
Shipped in v0.12.70 for all four wires: `wire.py` (the strip as the eyebrow, no blurb, the status line after the mount), `wire.js` (the dateline, the status line, the today band, the folded record, the bar's first-visit state, the share flag), `wire.css` (the designer's CSS as written). The spec: `admin/notes/wires-ux/first-screen.md`; the screenshots beside it. Checked in `test_wire.mjs` on every wire.
