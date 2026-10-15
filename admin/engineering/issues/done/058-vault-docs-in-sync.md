---
id: 058
title: The vault's documentation says what the pane does
kind: task
priority: normal
created: 2026-10-13T11:05:00Z
source: the owner, in chat, 13 October 2026: take a good look at how the newsroom works, then the vault pane; review its documentation and make sure it is in sync with reality
release: v0.12.58
estimated_effort: small
---
# The vault's documentation says what the pane does
## What happens
The pane gained a Reading tab (006), Done and Follow up (004, 023), the strip and the count of what only this browser holds (027), the wire's seen stories in the device file (028), a send that rewrites the device file (009) Write to the newsroom (034), more than one wire (040) and the inbox (049), and the writing about it did not keep up. The vault page, the README, the design and shipped hubs, the reader API map, llms.txt and the pane's own header all said three tabs; the chips were listed without Follow up, and in places without Done; the device file was described as reads, top-ups and personas; the feedback loop's note still said sent marks reach other devices only with the next update, and told the reader to press *Keep the words*; the lane's README named seven kinds.

## Scenario
```gherkin
Given a reader opens /vault/ beside the pane
Then every tab the pane has is named, in order, and nothing the page names is missing from the pane
And the one-tap kinds on the page are the pane's nine, and the wire's six are said to be six
And what an update carries is what the device file holds: reads, top-ups, personas, notes and the stories seen
And where the keys live, what local storage holds, and which buttons only read are said

Given an agent reads llms.txt, the vault page's agent block or the reader API map
Then it finds the same four tabs and the same record

Given the design notes are read for the record
Then the device file's layout shows notes and wire.seen with the version each arrived in
And what changed after the first build is listed, dated, before the experiments
```

## Outcome
Shipped in v0.12.58, with no change to what the pane does. Written against v0.12.9, then carried onto v0.12.27, so it also names the inbox where the pane now has it. Brought into line: `admin/build/vault_page.py` (four tabs; the nine kinds and the wire's six; Update from the strip, the tab or the wire; a send rewrites the device file; the passkey made on the spot, the recovery code's two uses, Check the vault and Forget; the read key shown with Copy; where the keys live and what local storage holds; the agent block, the inbox in the intro, in what leaves the browser and in the agent block), `README.md`, `admin/build/hubs.py` (the two hub entries), `admin/build/api_map.py` (two rows), `llms.txt`, the headers of `assets/vault-pane/vault-pane.js` and `notes.js`, the README written into a new lane (`assets/newsroom-vault.js`), and the two design notes (the record and the device file as they are, a dated list of what the pane gained after v0.11.0 up to the inbox, the sent-marks bullet corrected). Found and left as it is, for a card of its own if wanted: `vault-pane.js` falls back to the meter library's default storage key (`sg.meter.v1`) where `notes.js`, `pending.js` and `reading.js` fall back to `sgit.meter.v1`; every page sets the key, so neither default is reached.
