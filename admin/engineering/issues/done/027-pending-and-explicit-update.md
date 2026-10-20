---
id: 027
title: What only this browser holds: the count on the Vault button, the strip, Update the vault from anywhere
kind: story
priority: urgent
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.6
estimated_effort: medium
---
# What only this browser holds: the count on the Vault button, the strip, Update the vault from anywhere
## What is asked
The owner: stored locally first, then an explicit push to the vault; and the principle that if I do not update the master, I have something to lose because it is not synchronised.

## Scenario
```gherkin
Given I have kept notes or read pages since this device last updated the vault
Then the Vault button shows how many, with an amber dot
And the pane shows a strip above its tabs naming them, with Update the vault
And the wire's bar shows the same line, with Update the vault and Open the vault
When I press Update the vault from the strip or the wire
Then this device's file is written to the reader vault, one commit
And the count goes to zero, and the wire says everything I decided here is in the vault

Given the vault is not enabled on this device
Then the strip's button says Enable the vault to keep them and opens the Vault tab
```

## Outcome
Shipped in v0.12.6: assets/vault-pane/pending.js, the strip and the badge in vault-pane.js, two window events (sgit-vault-open, sgit-vault-update) and the answer (sgit-vault-updated). Stories seen are named in the strip and carried by the update, but are not in the number on the button, which counts what the reader did. Checked by test_notes.mjs.

## Screenshots
![The strip above the pane's tabs, and the count on the Vault button](../shots/027-strip.png)
