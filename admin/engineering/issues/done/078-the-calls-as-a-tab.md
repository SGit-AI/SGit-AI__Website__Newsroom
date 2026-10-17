---
id: 078
title: The calls to the vault server, as a tab: what each one is, and what it carried
kind: story
priority: normal
created: 2026-10-16T11:00:00Z
source: the owner, in chat, 16 October 2026, after connecting Firefox to the vault: "the ability to merge those devices ... iPad 1, iPad 2, iPad 3 ... select a couple and merge"; a page to see and browse the vault from the right-hand side; a shared vault viewer made with the vault-in-vault technique and made the default app; the calls to the vault server shown for what they are, expandable to their contents; the selection workflow improved; a debrief as newsroom.vault
release: v0.12.88
estimated_effort: medium
---
# The calls to the vault server, as a tab: what each one is, and what it carried
## What is asked
The pane listed every call ("PUT /api/vault/write/… → 200"). The owner: interesting, but show what they are, a file, a commit, something else, and let me expand one and see its contents; "worth becoming a UI itself".

## Scenario
```gherkin
Given the pane has made calls to the vault server on this page
When I open the Calls tab
Then each call is listed with its time, a badge for what it touched (object, ref, working ref, branch index, append lane), the vault by name (your reader vault, your master vault, your door, your lane), its status, size and time taken
When I open a call
Then what it carried is decrypted here with the key of its vault, when that vault is open in this page, and named: a commit with its message, time, tree and parents; a tree with its entries; a ref with the commit it points at; a file with its text
And the master's and the door's file contents open only behind Reveal
And an append-lane call shows its body with tokens and keys masked
And calls of a vault not open here say they stay sealed
```

## Outcome
Shipped in v0.12.88: `assets/vault-pane/calls.js` (pure: the address named, a batch split into its operations, the plaintext classified, credentials masked) and the Calls tab in `vault-pane.js`, which keeps the bytes of this page's calls in memory and the earlier pages' calls, without bytes, in session storage; Wider widens the pane. Nothing is fetched to decode: the bytes are the call's own. Checked by `test_vault_open.mjs` (a commit, a tree and a ref decoded from the calls of an update).

## Screenshots
![The Calls tab: a batch opened into a file, a tree, a commit and a ref](../shots/078-calls.png)
