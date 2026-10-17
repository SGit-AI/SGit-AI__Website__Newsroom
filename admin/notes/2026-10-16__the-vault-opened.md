# The vault, opened: merging devices, reading the calls, browsing your vaults, and a viewer every reader vault shares

*16 October 2026, built in newsroom.sgit.ai v0.12.88 by newsroom.vault. Cards 077, 078 and 079. The ask, in chat, after the owner connected Firefox to the vault: merge devices; a page to browse the vault, linked from the pane; a shared viewer made with the vault-in-vault technique and made the default app; the calls to the vault server shown for what they are; a better chooser. It stands on [open, or connect](2026-10-13__open-or-connect-a-vault.md), [send to my vault from any browser](2026-10-13__send-to-my-vault-from-any-browser.md) and [the activity vault](2026-10-12__the-activity-vault.md).*

## In short

- **Merge devices.** Tick two or more in *Across your devices*, pick the one they go into and its name, press Merge. Every record of each is kept, re-tagged with that device; the account's totals do not move; the merged ids become aliases in `activity/aliases.json`, so a browser still using one is filed under the merged device next time, and so is anything it sends.
- **The chooser says where a browser goes.** The device whose name this browser used, or the one device on the same platform, is offered first; the button names the destination; *Change* beside *Device* moves this browser into another device later, as a merge.
- **The Calls tab.** Every call to the vault server, named from its address (an object, a ref, a working ref, the branch index, an append lane) and from what is inside once decrypted with the key of its vault (a commit with its message, a tree with its entries, a ref with its commit, a file with its text).
- **The browse page.** `vault/browse.html` opens the reader vault, the lane, the master and the door with the session the pane keeps, and shows the files, any file, the commits and the tree at each. It writes nothing.
- **The shared viewer.** An app in a vault of its own, `lkypj6zq`, published with a public read key. Each reader vault links it read-only and opens with it, so the vault in the SG/App shows the reader's account. Proven in the live SG/App on a demo vault, `eagquvh8`.

## The vault-in-vault technique, as built

sgit.ai describes sub-vaults as a convention ([Sub-vaults](https://sgit.ai/docs/vault/sub-vaults.html)): a file named `*.link.json` points at another vault and carries no key; `.vault/owner/ro-links.json` holds the child's read key; the vault UI splices the child in as a folder, read-only, and an app's `sg.vfs` reads under that folder are served from the child. The live UI's code says the same: `VaultLinks` reads the link and the record (`{vault_id, read_key (base64), ref_file_id}`), and in App Mode a `CompositeDataSource` routes reads under a link's path to the child, opened with `SGVault.openReadOnly`.

So the reader vault holds four things, written by `installViewer` in `assets/newsroom-vault.js` on the next Update:

| File | What it is |
|---|---|
| `newsroom-viewer.link.json` | the pointer: `{vault_id, ref_id: "lk-newsroom-viewer", type: "vault", label, pin: {mode: "latest"}}`; no key |
| `.vault/owner/ro-links.json` | the record under that `ref_id`: the viewer's read key (base64) and its ref file id, derived from the read key alone |
| `.vault/app.json` | `{entry: "index.html", present: true, hud: {mode: "minimal"}, permissions: {fs: {read: true}}, newsroom: {...}}`: the vault opens as an app |
| `index.html` | the entry: `sg.loadJs("newsroom-viewer/viewer.js")`, then `NewsroomViewer.render(...)`; a plain summary of the device files if the viewer cannot be read |

The entry is in the reader vault, not in the viewer vault, on purpose: whether App Mode would launch an entry that lives inside a linked vault is not documented, and a read across the link is. The entry is a dozen lines and does not change; the viewer's code lives in one place and every reader vault gets a new version when the newsroom publishes one, because the link is pinned to the latest.

What the viewer can see: the reader's records, through `sg.vfs`, in the reader's browser. What the viewer vault can see: nothing; nobody writes to it but the newsroom, and the reader vault only reads it. The reader's records never go into it.

`installViewer` writes only what differs, and never replaces an `app.json` or an `index.html` this site did not write; it says so instead.

## Publishing the viewer

`admin/build/viewer_vault.mjs` writes `vault/vault-app/` (the viewer, its own entry, a README, a demo account, and `vault-app.json` as the viewer vault's `.vault/app.json`) into the viewer vault as one publish, and records the vault id and its public read key in `admin/content/vaults/vault-viewer.json`, which the pane reads. The access key and the vault key come from the environment, never a file; on the first run the new vault key is printed once to stderr. A second run with `NEWSROOM_VIEWER_VAULT_KEY` publishes a new version to the same vault and the same key; the first run made `lkypj6zq` and the second wrote two changed files to it.

## Merging, the rules

- **Nothing is dropped.** `mergeDevices` re-files each source into the target (`refile`) and combines (`combine`): every read, note, top-up and story seen, the one that knows more where two copies exist. A payment record is moved, never deleted.
- **The files go; the history stays.** The merged devices' files are removed from the current tree, so no record is counted twice; every earlier version is in the vault's commits, and the browse page shows them.
- **Aliases, not tombstones.** `activity/aliases.json` maps each merged id to the device it went into, with the merge recorded (when, into what, from what, by which device). `readAll` and `writeDevice` follow it, so a browser that was a merged device becomes the merged one before it writes; `applyAliases` folds a merged device's file written again by an old browser into its target; the inbox drain files a batch through it.
- **Change is a merge.** Choosing another device from the Vault tab merges this browser's device into it, then makes this browser that device.

## The calls

`assets/vault-pane/calls.js` names a call from its address alone, then, on a press, from its bytes: the pane keeps each call's request and response bytes in memory (this page only, up to 2 MB a call), decrypts them with `SGSendCrypto.decrypt` and the vault's read key when that vault is open, and classifies the plaintext by its schema (`commit_v2`, `tree_v1`, `{commit_id}`), decrypting a commit's message and a tree's names, which are encrypted again inside. Nothing is fetched to decode. Earlier pages' calls are kept in session storage without their bytes, so the tab shows the whole visit.

## The browse page and the SG/Vault app

`vault/browse.html` unlocks the vaults itself, with the session record the pane keeps for the tab, and lists, reads and walks the history with the library's `listFolder`, `getFile`, `logCommits`, `listTreeAt` and `readFileAt`. On a press it opens the reader vault in the SG/Vault app with `assets/vault-pane/sg-embed.js`, this site's own copy of the embed handshake (sgit.ai's `assets/vault-ui-embed.js` is imported here and must not be edited): the read key is handed to the app over its embed protocol and is never written into the page's markup. The test checks that what the app receives is `sgit_rk1_<read key>:<id>` and nothing else.

## Not built

- Splitting a merged device back out (the history has it; there is no button).
- A deep link to the SGit view of a vault in the app: the embed message has no field for a view yet, as sgit.ai's own briefing says.
- A viewer for the lane or the master; the browse page covers them.
- Purging processed inbox files, as before.

## Tests

`admin/build/test_sync.mjs` (merging three devices, aliases, a folded file), `admin/build/test_vault_open.mjs` (the publisher against the mock; the four pieces after an update; the owner record opening the viewer on its own; the entry page rendering the account in a stand-in host; the Calls tab decoding a commit, a tree and a ref; the chooser's suggestion; a merge in the pane; the browse page; the key handed to the app). The live proof is the screenshot on card 079: the demo vault in the SG/App.
