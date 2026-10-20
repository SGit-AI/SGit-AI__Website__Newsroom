---
id: 077
title: Merge devices, and a chooser that says where a browser goes
kind: story
priority: high
created: 2026-10-16T11:00:00Z
source: the owner, in chat, 16 October 2026, after connecting Firefox to the vault: "the ability to merge those devices ... iPad 1, iPad 2, iPad 3 ... select a couple and merge"; a page to see and browse the vault from the right-hand side; a shared vault viewer made with the vault-in-vault technique and made the default app; the calls to the vault server shown for what they are, expandable to their contents; the selection workflow improved; a debrief as newsroom.vault
release: v0.12.88
estimated_effort: medium
---
# Merge devices, and a chooser that says where a browser goes
## What is asked
The owner's vault had iPad 1, iPad 2 and iPad 3: one device, three rows. "Select a couple and merge", without losing the per-device view or deleting a payment. And the device chooser, which worked, should make the choice easier.

## Scenario
```gherkin
Given my vault knows three devices that are one iPad
When I tick two or more of them in Across your devices
Then a bar offers to merge them into one of them, under a name I can change, and says nothing is deleted
When I press Merge
Then one device file holds every read, note, top-up and story seen of all of them, re-tagged with that device
And the account's totals are the same as before
And the merged ids are recorded as aliases, so a browser still using one is filed under the merged device the next time it opens the vault, or sends through the inbox

Given my vault knows devices and this browser is none of them
When the pane asks which device this is
Then the device whose name this browser used, or the one device on the same platform, is offered first and already picked
And the button says where the browser goes: "Continue as iPad", "Continue as a new device: Firefox"
And I can change it later with Change beside Device, which moves what this browser wrote into the device chosen
```

## Outcome
Shipped in v0.12.88. `mergeDevices`, `resolveAlias` and `applyAliases` in `assets/vault-pane/sync.js` (nothing dropped: `refile` then `combine`; a merged device written again later folds into its target); the bar under the table, `activity/aliases.json` with the merges recorded, the merged files removed from the current tree (they stay in the vault's history); `readAll` and `writeDevice` follow the aliases, the inbox drain files under them. The chooser: cards, a suggestion, a button that names the destination, and Change, which merges this browser's device into the one chosen. Checked by `test_sync.mjs` (three iPads into one, totals unchanged, an old file folded) and `test_vault_open.mjs` (the suggestion, the merge in the pane, the browser filed as the merged device). Not built: splitting a device back out.

## Screenshots
![The chooser: the device on the same platform offered first](../shots/077-chooser.png)
![Two devices ticked, the merge bar](../shots/077-merge.png)
