# The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together, sgit.ai

> On 11 October this site published a design for a reader's account with no server: a passkey computes the address of a small door vault, the door holds the key of a master vault, the master holds everything else. By 02:22 UTC on 12 October it was running on newsroom.sgit.ai. Not as a demo: a Vault button beside the balance on every page opens a pane that enables the account with a passkey, creates three real sgit vaults on the vault server with an access key pasted once, writes this device's reading records as one file in one commit, lists every device of yours, and brings their activity into this browser so the meter shows one balance. In between came a lab with every step as a card, a finding that put the door layer back into the design, the vault library that runs dev.vault.sgraph.ai vendored unedited with every hash checked, a mock of the vault server for the tests, a round trip through the sgit command line in CI, and a live check on an iPad that made three vaults from an iCloud Keychain passkey and opened them again after a refresh. This article is the architecture as it stands, drawn: the layers in the browser, the key chain and the files in each vault, the sync model that has no conflicts by construction, the tests, and what is not yet built. It is also the point of the whole exercise, which is that I could not have written the next brief until this one existed, because the properties of what runs are the constraints I think with.

*Source: <https://newsroom.sgit.ai/articles/the-vault-is-live.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together

# The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/the-vault-is-live.md) · [sgit.ai v0.7.66](https://sgit.ai/admin/versions.md) · vaultspasskeysnewsroomarchitectureclient-sidesynclocal-firstsgittestingreleasearticle

***Abstract:** On 11 October this site published a design for a reader's account with no server: a passkey computes the address of a small door vault, the door holds the key of a master vault, the master holds everything else. By 02:22 UTC on 12 October it was running on newsroom.sgit.ai. Not as a demo: a Vault button beside the balance on every page opens a pane that enables the account with a passkey, creates three real sgit vaults on the vault server with an access key pasted once, writes this device's reading records as one file in one commit, lists every device of yours, and brings their activity into this browser so the meter shows one balance. In between came a lab with every step as a card, a finding that put the door layer back into the design, the vault library that runs dev.vault.sgraph.ai vendored unedited with every hash checked, a mock of the vault server for the tests, a round trip through the sgit command line in CI, and a live check on an iPad that made three vaults from an iCloud Keychain passkey and opened them again after a refresh. This article is the architecture as it stands, drawn: the layers in the browser, the key chain and the files in each vault, the sync model that has no conflicts by construction, the tests, and what is not yet built. It is also the point of the whole exercise, which is that I could not have written the next brief until this one existed, because the properties of what runs are the constraints I think with.*

What is running on newsroom.sgit.ai at v0.11.0: the meter and local storage as before; the vault pane and one module over the vendored vault library, new; the vault server holding ciphertext. On the right, the three vaults, what each holds, and how one gesture opens all three.

Yesterday morning the reader's vault was [a design](the-passkey-opens-the-vault.md). This morning it runs. Open any article on [newsroom.sgit.ai](https://newsroom.sgit.ai/), and beside the balance there is a button that says Vault. It opens a pane on the right, and the page moves over to make room. Enable with your passkey, and the pane says what it is doing in one line at a time: deriving the door from the bytes, opening the door, the master and the reader vault. On a first device there is no door yet, so you paste an access key and press Create the account, and the pane makes three vaults and shows you a recovery code once. Read some articles. Press Update the vault, and this device's records go into the reader vault as one file, one commit. On another device, the same passkey opens the same vaults, a table lists the first device with its reads and its spend, and one press brings its activity here, so the meter shows one balance.

That is the feature I said I missed in [I miss it, so it is working](i-miss-it.md), two days ago. This article is the architecture of what was built, drawn so that the next person, or the next agent, can see how all of it fits: the layers in the browser, the chain of vaults and the files in each, the sync model, the tests, the timeline, and the honest list of what is not there. And then one paragraph on why I think this matters beyond the feature.

## In short

- **It runs.** At newsroom.sgit.ai v0.11.0 a reader can enable a vault with a passkey, create the account once with an access key, update the vault from each device, and bring every device's activity into the browser they are holding. Three real sgit vaults, opened with one gesture.
- **The design held, with one change the lab forced.** The passkey computes the door's address and key; the door holds the master's key; the master holds the reader vault's key, the access key and the list of doors. The change: a door per path, because a passkey reached by a phone over QR gives different bytes from the same passkey on the device.
- **One code base, vendored.** The browser does not have a vault writer of its own. It uses the twelve files of the vault UI library that runs dev.vault.sgraph.ai, unedited, each SHA-256 recorded, with a build check that fails if one changes, and one local patch pending upstream: create a vault at a chosen id.
- **Local storage stays primary.** The meter is unchanged. The vault is a second home the reader keeps current, by pressing a button; the number of commits is the number of presses.
- **Records, never totals; one file per device.** Each device writes what it originated to its own file, whole. Totals are recomputed from the records on every open. Two devices never write the same file, so there is nothing to merge.
- **Tested against a mock, then for real.** Eight test files in CI, including the account, the sync logic, two devices in Chromium with a virtual authenticator, and a round trip through the sgit command line. Then an iPad with an iCloud Keychain passkey against the real server: three vaults made, a note written and read back, all three opened again after a refresh.
- **Not built:** pruning local storage, retiring a device, rotating the master's key, automatic sync, the key pairs, the persona vault, the notes lane to the newsroom. Each is designed; the experiments to run first are listed.
- **The point.** I could not think about the next brief until this existed. The properties of what runs are the constraints I think with, and shipping is how I get them.

## The layers

Everything on the reader's side runs in the browser, on static pages, with [no server of ours](no-server-by-design.md). From the bottom up:

- **The vault server.** dev.send.sgraph.ai, the development instance. It holds ciphertext, sizes, times and ids that look random. A write needs the access key as a request header; a read needs nothing, because the key that decrypts is the credential. The head pointer of each vault is guarded by compare-and-swap. For the tests there is a mock of this API in Node, with the same shapes: read, write, batch with write-if-match and the conflict response, list, the first writer's write key fixed, a token on every write, and the same CORS as the real server.
- **The vault library.** The vault UI library v0.2.3 from the SGraph send repository, twelve files, vendored into the newsroom under `assets/vendor/sg-vault/` and loaded from the newsroom's own origin the first time a page needs it. A VENDOR file records the upstream commit and the SHA-256 of every file, and check 13 of the site's validator fails the build if any of them changes. One local patch sits beside it, a static method that creates a vault at a chosen id and refuses if the address is taken; the upstream issue for it is written and listed on [the page about writing a vault from JavaScript](https://sgit.ai/docs/vault/vault-from-javascript.md).
- **One module over the library.** `newsroom-vault.js`, 197 lines: create a vault, create one at a chosen id, open one (with a named error when there is no vault there), load a folder, write a file, publish, read, and one clone branch per device. On top of those, the account: `createAccount`, `unlock`, `addDoor`, `writeNote`. That is the whole of the design from the article, as code.
- **The door derivation.** `door.js`, 139 lines, moved out of the lab so that the pane and the lab derive the same door from the same bytes; the lab re-exports it.
- **The vault pane.** `vault-pane.js` and its stylesheet, 359 lines, injected by the site's chrome on every page that carries the meter. And `sync.js`, 125 lines of pure functions that decide what goes into a device's file and what the consolidated view is; nothing in it touches storage or the network, which is why it can be tested in Node with two devices' states.
- **The meter and local storage.** [SG Meter](pay-after-you-read.md) v1.4.0, unchanged. It writes local storage in real time, as it has since 10 October.
The pane, on an article, before it is enabled: the device's id, a label for it, the two ways in, one paragraph that says what the passkey does, and the list where every call to the vault server will appear.

## The key chain, and what is in each vault

The chain is the one in [The passkey opens the vault](the-passkey-opens-the-vault.md), as revised after the lab, and now it is three vaults on a server rather than three boxes in a figure.

1. **The door**, at the address derived from the passkey's bytes. Two files: `master-key.json`, the master's key, and `door.json`, where this door came from: the kind (a passkey or the recovery code), the provider as the browser named it, the path (platform or cross-platform), the credential id, a device label and the date. One door per path to the same master; the recovery code has a door of its own. A door is retired by deleting its files, never by destroying its address, because a destroyed vault id can never be used again and a door's is derived.
2. **The master**, at a random id. Two files: `reader.json`, the reader vault's key, and `doors.json`, every door with its own key, so that from any open door the page can read, rewrite or delete every other. The access key lives here, pasted once on the first device and brought to every other by the unlock.
3. **The reader vault**, at a random id. `activity/account.json`, written once: the one starting credit, the currency symbol, when and by which device. `activity/devices/<id>.json`, one per device, rewritten whole on each sync. And `notes/`, where the lab wrote its first note.

Creating the account on a first device is six key derivations and three first commits; the pane says so while it works. Unlocking on any other device is one gesture, then the door, the master and the reader vault in sequence, each a read-only open with the key the previous one held, and the access key arriving with the master so that this device can write too.

Cards 3 and 4 of the passkey lab: the derivation from the bytes to the door, timed on the device, and the recovery code that derives a second door. Card 6, where the account was first built as three real vaults, appears on a browser with a platform authenticator; this headless one has none.

## The sync model

The part of the design that was only a sketch two days ago is now the most carefully stated, in the newsroom's [activity vault note](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md). Six principles, each with a reason:

Two devices, one passkey, one view. Each device writes its own file, whole, when its reader presses Update; the vault holds records, never totals; opening the vault computes one view from every file; brought-in records keep their author.

- **Local storage stays primary.** The meter writes it in real time and nothing about the meter changes. The vault is a copy the reader keeps current.
- **The reader chooses when to sync.** One button. Nothing commits on its own, so the number of commits is the number of presses, and the cost of a sync, a few derivations, one commit, one publish, is paid when the reader wants it. A timer can come later, as a setting, once the shape of a sync is understood.
- **The vault holds records, never totals.** Reads, top-ups and personas go in raw. Reads, spend, declined, credit and balance are recomputed from the records every time they are shown, with one starting credit for the account. A total copied from a device would be wrong the moment a second device existed.
- **One file per device, written only by that device.** Each device has an id it already used as its clone branch, and writes everything it originated to its own file, whole, on every sync. Two devices never write the same file, so there is nothing to merge and no conflict by construction. The compare-and-swap on publish still guards the pointer, and the library merges at file level if a race happens, which keeps both files.
- **The consolidated view is computed, not stored.** Opening the vault reads every device's file and builds one view, per device and in total. Bringing other devices' activity into a browser adds their records to its local storage tagged with the device they came from; the next sync from that browser writes only its own records back, so a record has exactly one author for ever.
- **Nothing is typed twice.** The access key is pasted once and lives in the master. A second device gets it by opening the master with its passkey once it has a door, or with the recovery code once.

Top-ups are counted once by payment reference, so a payment's return page opened on a second device cannot credit it twice. The active persona and the reading position stay on the device. The keys of an unlocked session are kept in memory and in the tab's session storage, for the life of the tab, so that moving from page to page does not ask for the passkey each time; the note marks that as a choice for the beta, to be revisited.

## The tests

The newsroom's CI now runs eight test files, and the ones for the vault are worth listing because they are the reason the live check was a check and not a hope.

- **The account against the mock**: the library loaded as the page loads it, the account created, the unlock, the lazy-folder trap, a publish race, a second door, the shapes of the keys. Twenty-seven checks.
- **The round trip through the command line**: sgit-ai 0.21.0 installed in CI, a clone from the door's key in sgit's own form, a commit, a push, and the file read back in the browser. The first deploy of v0.10.0 failed exactly here, because the test ran sgit with a temporary home directory and the runner had installed the package under the real one; v0.10.1 is the fix, and the versions page says so.
- **The lab's card 6** driven against the mock: thirty-three checks.
- **The sync logic** in Node with two devices' states: nineteen checks.
- **The pane in Chromium**, with a virtual authenticator standing in for one synced passkey: device A reads, enables, creates, updates; device B, the same passkey in a cleared browser, enables, sees A, brings A's activity in and shows the consolidated balance in the meter, reads, updates only its own; device C opens with the recovery code. Twenty-eight checks.

Then the live check, run by hand on 12 October on a current iPad in Safari with an iCloud Keychain passkey and an access key, against the real server: the account made as three vaults, a note written into the reader vault and read back, the vault opened in dev.vault.sgraph.ai showing the note, and after a refresh, with nothing stored, the passkey unlocking all three again. The three vault ids are in the newsroom's versions row, as the brief asked; no key is.

The page that explains the vault and opens the pane on arrival: the loop in five steps, the principles, what leaves the browser, and a block for an agent.

## The timeline

From the two git logs, so that the speed is a measurement and not a feeling.

| When (UTC) | Where | What |
|---|---|---|
| 11 Oct, morning | sgit.ai | The design: [The passkey opens the vault](the-passkey-opens-the-vault.md), v1.0.0 |
| 11 Oct, day | sgit.ai | Two reviews: the door removed as a layer too many, the key pairs made random, sign-in taken out |
| 11 Oct 22:56 | newsroom | v0.8.3, the passkey lab: every step as a card |
| 12 Oct 00:15 | newsroom | v0.9.1, the finding: a door per path, with the Apple forum threads behind it |
| 12 Oct 01:33 | newsroom | v0.10.0, real vaults from the browser through the vendored library, the mock, the tests |
| 12 Oct 01:38 | newsroom | v0.10.1, the CLI round trip runs in CI |
| 12 Oct 01:57 | newsroom | v0.10.2, the live check on an iPad recorded |
| 12 Oct 02:22 | newsroom | v0.11.0, the vault pane: the reading account carried between devices |
| 12 Oct, morning | sgit.ai | The design revised to match what ran, v1.4.0, and this article |

Two sites, two agents, and me reading on an iPad in between. The design went to the lab, the lab corrected the design, the corrected design was built, and the build was checked on a real device before the pane that readers see was written over it. None of those steps was skipped, and none took more than two hours.

## Why this matters more than the feature

I wrote in [Pay after you read](pay-after-you-read.md) that the more you have, the faster you go, and this night is the cleanest case of it I have: the meter existed, so the vault had something to carry; the lab existed, so the vault could be built on tested pieces; the library existed, so no vault writer had to be written; the mock existed, so two devices could be tested without a server.

But there is a second thing, which I only noticed this morning, when I sat down to write the next brief. I could not have written it yesterday. Not because I lacked time, and not because the idea was hard to predict. Because I did not have the constraints. I did not know that the passkey works and the sign-in is not needed. I did not know that a door is per path. I did not know that the sync is one file per device and that the view is computed. Each of those is a property of what runs, and each one closes off a dozen things I might otherwise have had to think about, and opens the two or three that are worth thinking about next. The constraints limit the scope of what I write, and that is what lets me write it.

So the feedback loop is not only use it, miss it, build it. It is also: build it, learn its properties, and only then think the next thought. The vault pane is live. The next brief is about what a reader does with it, and it is next.

## What this does not claim

- **A beta, on the development server.** The vaults are on dev.send.sgraph.ai. The access key is handed out by me for now. The passkey path that works everywhere is the platform one; a phone over QR gets a door of its own.
- **The live check is one device and one day.** An iPad, one iCloud Keychain passkey, one afternoon. The experiments the note lists, two real devices, a page read on both, a rating after a merge, a top-up on one and the return page on the other, pruning, automatic sync, have not run.
- **Not built**, and said so on the page: pruning local storage once the vault holds it, retiring a device, rotating the master's key, automatic sync, the key pairs for signing, the persona vault, the notes lane to the newsroom.
- **The session keys live for the tab.** Kept in memory and session storage so that pages do not ask for the passkey each time. The note marks it as a choice to revisit.

If you build sites that keep a reader's data without a server, or you want to try the vault with your own passkey and tell us what breaks, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on the morning of 12 October 2026, after reading the newsroom's overnight releases, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The facts are from the newsroom repository's commits v0.8.3 to v0.11.0 of 11 and 12 October 2026, their messages and files; the newsroom's [activity vault note](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md), [vault page](https://newsroom.sgit.ai/vault/) and [passkey lab](https://newsroom.sgit.ai/passkey/); the source of `newsroom-vault.js`, `sync.js`, `door.js` and `vault-pane.js`; and the versions row for v0.10.2, which records the live check. The line counts are from the files at v0.11.0. The screenshots are of newsroom.sgit.ai at v0.11.0 on 12 October 2026; the figures were drawn for this article from the note and the code. Related: [The passkey opens the vault](the-passkey-opens-the-vault.md), [I miss it, so it is working](i-miss-it.md), [No server, by design](no-server-by-design.md), [Pay after you read](pay-after-you-read.md), [Two agents, one vault](two-agents-one-vault.md) and [Creating, opening and writing a vault from JavaScript](https://sgit.ai/docs/vault/vault-from-javascript.md).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-vault-is-live)

### Builds on

- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.

### Continued by

- [Four frameworks, one agent: iason's comparison of the OECD classification, the NIST AI RMF, Japan's guidelines and the EU AI Act, read against what runs here, with the evidence and the graphs](four-frameworks-one-agent.md) iason's comparison of four AI risk frameworks, mapped to the behaviour policy, the footprint and the graphs that run here, with the status of each row.
- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it](the-vault-crosses-chrome-profiles.md) The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.
- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it](the-key-is-the-billing-system.md) VoiceDebrief runs with no server on the user's own key; the one thing it cannot sell is a capped key, and this maps who could allow it and what to ask them.
- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 81 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=81)

**Posting this article on LinkedIn?** The cover is [the-vault-is-live.jpg](banners/the-vault-is-live.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-vault-is-live.html)*
