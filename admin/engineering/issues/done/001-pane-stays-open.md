---
id: 001
title: The pane closes on every navigation
kind: bug
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# The pane closes on every navigation
## What happens
The reader opens the pane, reads, follows a link, and the pane is gone. Every page starts closed. The owner's note: "we lose the right hand side of the vault every time I navigate and it should be there so once I click I should continue to see it."

## Scenario
```gherkin
Given the pane is open on the This page tab
When I follow a link to another page of the site
Then the pane is open on that page, on the same tab
And it shows that page's own record and notes

Given the pane is open
When I press Close and follow a link
Then the pane is closed on the next page
```

## Mock-up
No new element. The state "open, on tab X" lives for the tab's life in session storage and is read on arrival, after every declaration the pane needs; Close clears it. `#vault`, `#notes` and `#reading` in the address still win.

## Outcome
Shipped in v0.12.1. Open stays open from page to page, on the same tab; Close closes it for good. Checked by test_notes.mjs: a note kept, a navigation, the pane open on the same tab showing the next page's record.

## Screenshots
![The pane open on the next page, on the same tab](../shots/001-pane-stays-open.png)
