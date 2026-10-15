---
id: 059
title: Open a vault, or connect one: which device this browser is, what the vault holds brought in, and a sent batch filed under a device you have
kind: story
priority: high
created: 2026-10-13T21:30:00Z
source: the owner, in chat, 13 October 2026, with two screenshots: a Vault tab showing four devices, a balance of £4.57 across them and £4.75 in the meter, "the aggregation is the point"; a browser with sixteen changes and a label asked for before the passkey; "the workflow is open a vault or connect a vault"; "I want to reuse one of the devices I already have"
release: v0.12.58
estimated_effort: large
---
# Open a vault, or connect one: which device this browser is, what the vault holds brought in, and a sent batch filed under a device you have
## What happens
Three things in the two screenshots. The vault held four devices and the account's balance was £4.57, and the browser that had opened it showed £4.75 and "nothing: the vault has everything of this device": the pane counted what was only in the browser and never what was in the vault and not in the browser, and the one way to bring it in was a button under the table. The locked pane asked for a device label before the passkey, so opening a vault read as naming a device. And a browser that could only send (the iPad's second browser, sixteen changes) could only ever become a new device in the table, when the owner wanted its reads filed under the iPad they already had.

## Scenario
```gherkin
Given a browser that has never opened the vault
When I open the Vault tab
Then it offers Open with your passkey and Connect with a link, and asks for no name

Given my passkey opens a vault that knows three devices and this browser is none of them
Then the pane asks which device this is: one of the three, with its reads and last update, or a new one
When I choose one I already have
Then this browser takes its id and label, and that device's records come in as this browser's own
When I choose a new one
Then the other devices' records come in, tagged with their device
And in both cases the meter shows the account's balance, recomputed, with nothing pressed

Given the vault holds records this browser does not
When I open the pane on any page
Then the strip above the tabs says what is in the vault and not here, with Bring them here
And the Vault tab says it beside what is not yet in the vault

Given a browser that holds the link and cannot reach my passkey
When I open the Vault tab there
Then it says which vault it sends to, takes a name, and offers Send to my vault
When what it sent is listed where the vault is open
Then I choose where to file it: as a device of its own, or under a device I already have, this one included
And the choice is remembered for that browser's next batch
```

## Mock-up
Locked: *Open your vault* [Open with your passkey] [I have a recovery code]; *Or connect with a link* [Connect with a link]. After the open, when there is a choice: *Which device is this?* ( ) DC on iPad old · 6 read(s), 0 note(s), last update 2026-10-13 20:12 · nr-… ( ) DC on iphone … (•) A new device [name] [Continue]. Unlocked: *Not yet in the vault* nothing; *Not yet here* 17 reads and 7 notes from 3 other devices; [Update the vault] [Bring them here] [Check the vault] [Forget on this device]. The drain: "iPhone, in WhatsApp (iPhone), sent 2026-10-13 20:01: 3 read(s), 16 note(s)…" then "File what iPhone, in WhatsApp sent under [iPhone, in WhatsApp: a device of its own (new) ▾ | DC on iPad old · 6 read(s) | DC on Athena session (here) …]".

## Outcome
Shipped in v0.12.58. The locked view offers the two ways in and names nothing first; the passkey is offered for making only when none answers. After an explicit open the pane reads the devices' files, asks which device this is when there is a choice (`drawChooser`; `adopt` takes the id and label; `NV.setDeviceBranch`), then merges what the vault holds on its own (`afterUnlock`; `inbound()` in sync.js counts it; `mergeInto`, `mergeNotes` and `mergeWire` take `own` so an adopted device's records come in as this browser's). The strip above the tabs and the Vault tab show both directions. Every device-file write is `combine(prev, extract(local))`, so two browsers may share a device. At the drain, a *File under* choice per sending browser (this browser always offered; the last choice, then a label match, first), `refile()` re-tags a batch, and the choice is kept as `aliases` in the master's `inbox.json`. The note of what arrived now travels with the redraw instead of being wiped by it. Top-ups show a dash in the total when there are none. Design: `admin/notes/2026-10-13__open-or-connect-a-vault.md`. Not built: consolidating two existing devices into one, automatic sync on a timer (029), a device choice on the sending side.
