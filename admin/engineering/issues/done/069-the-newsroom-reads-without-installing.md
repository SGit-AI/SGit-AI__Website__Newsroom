---
id: 069
title: The newsroom's morning run reads the vaults without installing anything
kind: story
priority: high
created: 2026-10-16T12:05:00Z
source: the newsroom's morning runs of 14, 15 and 16 October 2026, each refused at `pip3 install sgit-ai` as "Code from External"
release: v0.12.74
estimated_effort: small
---
# The newsroom's morning run reads the vaults without installing anything
## Scenario
```gherkin
Given a fresh container where installing the sgit client is refused
When the morning run needs the wires' vaults
Then admin/build/vault_fetch.mjs reads each one with the site's own reader (wire/vault-reader.js) and its published read key into a folder shaped like a clone, with the commit it read
And wire.py builds the pages and the snapshots from those folders as from a clone
```

## Outcome
Shipped in v0.12.74: `admin/build/vault_fetch.mjs` (Node's fetch and Web Crypto, no package); the four vaults in 28 seconds; the morning run's prompt uses it, installs nothing, and runs on Sonnet.
