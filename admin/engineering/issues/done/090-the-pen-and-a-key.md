---
id: 090
title: The Pen: mark a page, comment, tell the newsroom; and notes signed with a browser key pki.sgit.ai vouches for
kind: story
priority: high
created: 2026-10-24T09:55:00Z
source: Dinis, voice memo on 24 October 2026, on an iPad, with a screenshot of Safari's Copy / Look Up / Translate menu over a selection in an article: "I would like to be able to provide feedback and also capture stuff ... that little UX bug ... when I select on the iPad, you get that little copy ... banner ... maybe the same way that we have the vault, we should have an option for comments or analysis ... on the right-hand side ... the ability to capture those comments ... to highlight, for me to add comments to my part of the page, but also more importantly, for me to be able to send comments to you about this page ... we now have already working really well a PKI workflow on the client ... can you look at how we can integrate the login into here ... how can I connect that to the vault that I have ... they're separate domains ... maybe there isn't a full connection, there's just a QR code that we share with each other, or we do some kind of equivalent OAuth transaction ... how can you use that to send a message as me to our feedback append lane ... you should be able to identify me, because I've published my public key ... on pki.sgit.ai"
release: v0.13.64
estimated_effort: large
---
# The Pen: mark a page, comment, tell the newsroom; and notes signed with a browser key pki.sgit.ai vouches for

## What is asked
1. A place on every article for what the reader does with it, beside the Vault: capture what is selected, comment on it privately, and send notes about the page to the newsroom.
2. On an iPad, the site's Highlight button sits under Safari's own menu over a selection; a way that does not fight it.
3. Logging in here with the key Dinis holds on pki.sgit.ai, across two domains, and how that connects to the reader vault.
4. A note sent to the newsroom that can be identified as Dinis's, from his public key in the register.

## Scenario
```gherkin
Given a reader selects a sentence in an article, on an iPad
Then the Highlight button appears below the words, not under the system's menu
And a bar at the foot of the screen offers Keep, Comment and Tell the newsroom

Given the reader keeps the sentence and adds a comment in the Pen
Then it is a highlight on the page with the comment, kept in this browser, never sent

Given the reader writes a note for the newsroom about the sentence
Then it is a vault-pane note with the passage, sent down the reader's lane when they press Send

Given this browser has a key whose record the register holds, and Dinis's key operates it until a date
When a note is kept in the Pen
Then it carries a signature, and lane.py marks it "signed and checked" against the register from the pinned root
And a note changed after it was signed is marked as failing
```

## Outcome
Shipped in v0.13.64. `assets/pen/pen.js` and `pen.css` (loaded by `chrome.py` with the vault pane on every charged page): the button, the panel (Selected, Your marks, Tell the newsroom, Signed as you), and the bar at the foot. `assets/reader/highlights.js`: on a touch screen the button goes below the selection. `assets/pen/identity.js`: the browser's key (pki.sgit.ai's `keys.js` and `directory.js`, vendored unedited in `assets/vendor/pki/v0.2.25/` with their hashes), its identity and `operated-by` statements, the submission, the key link, signing a note, and the check against the register from the pinned root (`trustFrom`). `admin/build/lane.py`: every signed note checked against the register (the signature, and an in-date `operates` from the root). Test: `admin/build/test_pen.mjs` (31 checks: Python against JavaScript signatures, vouched, not vouched, lapsed, changed, unknown; the Pen in Chromium; the register served by the test). Design: `admin/notes/2026-10-24__signing-in-with-a-public-key.md`. Article: *A pen and a key*. Left: Dinis's own browser key into the register and linked; the authorize page and the QR code on pki.sgit.ai; the key kept in the reader vault's master; the newsroom's own feedback lane, published as an `inbox`.
