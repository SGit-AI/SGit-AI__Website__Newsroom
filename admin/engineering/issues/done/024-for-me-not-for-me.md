---
id: 024
title: New since the last visit, for me and not for me, with the lens remembered
kind: story
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.6
estimated_effort: medium
---
# New since the last visit, for me and not for me, with the lens remembered
## What is asked
The owner: a way in the newsroom UI to detect the new items, the ones not for me and the ones I should pay attention to.

## Scenario
```gherkin
Given I have opened the wire before in this browser
When I open it in a new tab after the desk added stories
Then the bar says how many stories are new since my last visit
And under my lens, how many of them are for me and how many are not
And every new story carries a New flag, in the stories and in the withheld lists
When I reload the page
Then the same stories are still new
When I open the wire again in a new visit
Then only stories that arrived since are new

Given I chose a lens last time
When I open the wire with no lens in the address
Then it opens under the lens I chose

Given a story was withheld from me under my lens
When I tap Should reach me
Then a note of kind more-like-this is kept with the story's id and the words "should have reached me as" and my lens
```

## Outcome
Shipped in v0.12.6: assets/vault-pane/wire-state.js (seen, the visit, the lens), the bar in wire/wire.js. A visit is the tab's life; New is first seen in this visit, here. Checked by test_notes.mjs.

## Screenshots
![Under the named reader's lens: 40 new, 26 for Dinis and 14 not; a decision with undo; what is only in this browser](../shots/024-for-me.png)
