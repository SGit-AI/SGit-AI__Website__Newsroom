---
id: 023
title: The wire as an inbox: filters, decisions that leave the inbox, Follow up
kind: story
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.6
estimated_effort: medium
---
# The wire as an inbox: filters, decisions that leave the inbox, Follow up
## What is asked
The owner: go through the news flagged for me or others, or any of it, and flag each one: read, to do, done, processed, follow up. The brief of The site is an inbox: the inbox is what has not been decided, and the state to return to is empty. The design is [the wire as an inbox](../../admin/notes/2026-10-13__the-wire-as-an-inbox.md).

## Scenario
```gherkin
Given I open the wire with no decisions
Then the bar offers Inbox, New, Read later, Follow up, Done and Everything, each with its count
And every story is in the inbox with six decisions: Done, Read later, Follow up, Not for me, More like this, Wrong
When I tap Done at a story
Then a note of kind done is kept with the story's id
And the story leaves the inbox, and the bar says what I decided, with undo
When I choose Done in the bar
Then the story is listed there, folded to its headline, with undo
When I undo
Then the story is back in the inbox
```

## Mock-up
```
Since your last visit (13 Oct 08:10 UTC): 12 new stories, 7 for Dinis and 5 not for Dinis.
| Morning edition, 13 October · 13 Oct 08:30 UTC
| Twelve new stories, three in cybersecurity on the same advisory...
| Added: sec-09, sec-10, ai-11 · Updated: ai-03
[Inbox (31)] [New (12)] [Read later (2)] [Follow up (1)] [Done (6)] [Everything (40)]
Done: Anthropic cuts live internet access for all internal evals... undo
1 change(s) only in this browser, 1 note: not in your vault until you update it. [Update the vault] [Open the vault]
```

## Outcome
Shipped in v0.12.6 (wire/wire.js, wire.css; Follow up added to assets/vault-pane/notes.js). Checked by test_notes.mjs against the live wire vault.

## Screenshots
![The wire on a first visit: the bar, the filters, every story new](../shots/023-inbox.png)
