---
id: 018
title: Guide a first-time reader through the whole loop, from the early-access key to the first note sent
kind: story
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.2
estimated_effort: medium
---
# Guide a first-time reader through the whole loop, from the early-access key to the first note sent
## What is asked
The owner: "we need to guide the user so that anybody who never used this before can follow up … we need to create a better experience." The three steps (007) are the start; this card is the whole first run: what to do, in order, on the page where it happens, with what each step makes and why.

## Scenario
```gherkin
Given I arrive with nothing
When I open the pane
Then it tells me the loop in three lines and what the first step is
And every step says what it makes (a passkey, three vaults, a file, a lane) and what leaves the browser
And at the end I can see what I made, in the Keys tab, and what I sent
```

## Mock-up
A first-run card at the top of This page, dismissible, that follows the steps; the vault page's "The feedback loop" section as the long form.
