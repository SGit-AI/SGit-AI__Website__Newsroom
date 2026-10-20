---
id: 007
title: The three steps, with the next one in bold: enable, update, send
kind: story
priority: normal
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# The three steps, with the next one in bold: enable, update, send
## What is asked
The owner: "guide the user so that anybody who never used this before can follow." The first form of it: the pane says where you are in the loop and what to do next. The full first-time guidance, with the early-access key first, is 012 and 018.

## Scenario
```gherkin
Given I have not enabled the vault on this device
When I open the pane
Then step 1, Enable the vault with your passkey, is in bold with a Go button to the Vault tab
When I enable it
Then step 1 is ticked and step 2, Update the vault, is in bold
When I update
Then step 2 is ticked with the time, and step 3, Send your notes to the newsroom, is in bold
```

## Outcome
Shipped in v0.12.1 at the top of This page. Checked by test_notes.mjs.

## Screenshots
![The three steps](../shots/007-steps.png)
