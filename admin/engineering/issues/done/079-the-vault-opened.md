---
id: 079
title: The vault, opened: a page to browse your vaults, and a viewer every reader vault shares, as its app
kind: story
priority: high
created: 2026-10-16T11:00:00Z
source: the owner, in chat, 16 October 2026, after connecting Firefox to the vault: "the ability to merge those devices ... iPad 1, iPad 2, iPad 3 ... select a couple and merge"; a page to see and browse the vault from the right-hand side; a shared vault viewer made with the vault-in-vault technique and made the default app; the calls to the vault server shown for what they are, expandable to their contents; the selection workflow improved; a debrief as newsroom.vault
release: v0.12.88
estimated_effort: large
---
# The vault, opened: a page to browse your vaults, and a viewer every reader vault shares, as its app
## What is asked
A page, linked from the pane, to see the vault and browse it: its files and what is in them. And a vault viewer shared by everybody: a new vault with the viewer's front end, linked into each reader's data vault with the vault-in-vault technique sgit.ai describes, and made that vault's default app.

## Scenario
```gherkin
Given my vault is open in the pane
When I press Browse your vault
Then a page opens my reader vault, my lane, my master and my door, here, with my keys
And shows each one's files, any file's contents, and its commits, with the files as they were at each
And the master's and the door's files open only behind Reveal
When I press Open it in the SG/Vault app
Then my reader vault opens in the SG/Vault app with its read key, handed over postMessage, never in an address, never stored

Given the newsroom has published its viewer in a vault of its own, with a public read key
When I next update my vault
Then my reader vault links the viewer read-only (a link file, the viewer's read key in .vault/owner/ro-links.json) and makes it the vault's app (.vault/app.json, an entry page that loads the viewer's code through the link)
And opened in the SG/App, my vault shows my account, devices, reading and notes, rendered by the shared viewer from my records
And when the newsroom publishes a new version of the viewer, every vault that links it shows it
```

## Outcome
Shipped in v0.12.88. The page `vault/browse.html` (`assets/vault-pane/browse.js`, built by `admin/build/vault_page.py`), linked from the Vault and Keys tabs. The viewer: source in `vault/vault-app/`, published by `admin/build/viewer_vault.mjs` as vault `lkypj6zq` on dev.send.sgraph.ai, whose public read key is in `admin/content/vaults/vault-viewer.json`; `installViewer` in `assets/newsroom-vault.js` writes the four pieces into a reader vault on the next Update, never replacing an app or an index.html this site did not write. Proven in the live SG/App: a demo reader vault, `eagquvh8`, made with the demo account and linked the same way, opens read-only and renders through the viewer (the screenshot); the browse page opens it on a press. `assets/vault-pane/sg-embed.js` opens a vault in the SG/Vault app by its embed protocol from code, so a key is handed over rather than written into markup; sgit.ai's imported `assets/vault-ui-embed.js` is unchanged. Checked by `test_vault_open.mjs`: the publisher against the mock, the four pieces after an update, the owner record opening the viewer vault on its own, the entry page rendering the account in a stand-in host, the browse page, and the key handed to the SG/Vault app being the read key and nothing else. Not built: the SGit view of a single vault deep-linked in the app (the app has no field for it yet), and a viewer for the lane or the master.

## Screenshots
![The demo reader vault in the SG/App, read-only, through the shared viewer](../shots/079-viewer-in-the-sg-app.png)
![The browse page: files, a merged device's file, the commits](../shots/079-browse.png)
