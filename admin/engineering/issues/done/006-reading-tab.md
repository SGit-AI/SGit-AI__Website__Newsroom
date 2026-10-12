---
id: 006
title: A Reading tab: every page read here, newest first, with its decision; done pages folded away
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: medium
---
# A Reading tab: every page read here, newest first, with its decision; done pages folded away
## What is asked
The owner: the pages already opened, which the account page shows, "should also be available on the right-hand side", with the done ones gone from the list.

## Scenario
```gherkin
Given I have read pages in this browser
When I open the Reading tab
Then I see one entry per page, newest first: the title as a link, when, how far, what it cost, its decision
And pages marked done are folded away, with a count and a switch to show them
And each entry has a Done button that folds it away
```

## Mock-up
```
WHAT YOU HAVE READ HERE
5 pages read in this browser, 1 marked done and folded away.
[ ] Show the pages marked done
  The site is an inbox                      [Done]
  2026-10-12 14:49 · you read a third of it, 9.5p
  Two agents, one vault        Read later   [Done]
  2026-10-12 14:30 · you read it all, 19p
```

## Outcome
Shipped in v0.12.1. The list is the meter's records, grouped by page; the decision comes from the notes. Checked by test_notes.mjs. Not done: the list across devices (it needs a merge first) and the account page itself, which is imported.

## Screenshots
![The Reading tab](../shots/006-reading-tab.png)
