---
id: 003
title: An account made in the lab holds no access key, and the pane offers no way out
kind: bug
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: small
---
# An account made in the lab holds no access key, and the pane offers no way out
## What happens
The owner's account was made in the passkey lab at v0.10.x, before the pane wrote the access key into the master. The pane unlocks it and says "Access key: none: writes will fail"; Update the vault is disabled; Send says "The master holds no access key, so nothing can be written; create the account again with one." A dead end, for the first real account.

## Scenario
```gherkin
Given my passkey opens an account whose master holds no access key
When the Vault tab is drawn
Then it says the master holds no access key and offers a field to add it
When I paste a valid access key and press Add the access key
Then it is written into the master, once
And Update the vault is enabled
And my other devices get the key from the master from then on

Given I paste a key the vault server refuses
Then the pane says so and nothing is written
```

## Mock-up
Under the Access key row: a highlighted block, "This account was made without an access key in its master, so nothing can be written yet. Paste the key once …", a password field, a button "Add the access key".

## Outcome
Shipped in v0.12.1. Checked by test_notes.mjs: the master's key file emptied, the pane reloaded from the session, the block shown with Update off, the key added, Update on.

## Screenshots
![The Vault tab offering to add the access key](../shots/003-add-key.png)
