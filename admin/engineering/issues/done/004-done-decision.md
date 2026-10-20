---
id: 004
title: “Done”: I have read it, I am done with it, take it off my lists
kind: story
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# “Done”: I have read it, I am done with it, take it off my lists
## What is asked
The owner's note: "once I've read it it should disappear from my list … I want to say I've done it and done with this." The seven decisions had no way to say that. The newsletter issue the note was kept on is content already processed, not to be seen again.

## Scenario
```gherkin
Given I am on a page I have read
When I tap Done in the pane, or Done at a wire story
Then a note of kind done is kept for that page (or story)
And the page's record in the pane shows Done as its decision
And the page is folded away from the Reading tab
And a decided wire story folds to its headline

Given a page is marked done
When I remove the Done note
Then the page is back on the lists
```

## Mock-up
A first chip, "Done", before Read later; the known block above the chips reads "Done on 2026-10-12 15:49. Read once, last …: you read it all, 9.5p."

## Outcome
Shipped in v0.12.1 as the first of eight chips, and as the first decision at a wire story. The Reading tab (006) folds done pages away. Checked by test_notes.mjs.

## Screenshots
![Done as the page's decision](../shots/004-done.png)
