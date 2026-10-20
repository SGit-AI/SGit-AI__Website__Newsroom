# The activity vault: the reading account, carried between devices

**Date:** 12 October 2026. **Status:** the design, and a first build (the vault pane, v0.11.0); what the pane gained since is at the end, before the experiments. The experiments it calls for are listed at the end; the design will move as they are run.

**Related:** [The passkey opens the vault](../../articles/the-passkey-opens-the-vault.html) (the account with no server), [one door per passkey path](2026-10-12__one-door-per-passkey-path.md) (why the doors are per path), [the passkey lab](../../passkey/index.html) (every piece, as a thing you can press), [the vault pane](../../vault/index.html) (where this runs), `assets/vault-pane/sync.js` (the logic, as pure functions), `admin/build/test_sync.mjs` and `test_pane.mjs` (what is checked).

## What this is for

The reading account lives in one browser's local storage: what was read and how far, what it cost, what was declined and why, the top-ups, the personas and their lists. It is updated as the reader reads, and it goes nowhere. The vault gives it a second home that the reader owns and that every device of theirs can reach through a passkey. The loop to close is short to state: enable the account on one device, read, press **Update the vault**; open another device, enable it, and see the same reads, the same spend, the same balance.

## The principles

1. **Local storage stays primary.** It is written in real time by the meter, as today, and nothing about the meter changes. The vault is a copy that the reader keeps current.
2. **The reader chooses when to sync.** One button. Nothing commits on its own, so the number of commits is the number of times a person pressed the button, and the cost of a sync (a few key derivations, one commit, one publish) is paid when they want it. A timer or a quiet-moment sync can come later, as a setting, once the shape of a sync is understood.
3. **The vault holds records, never totals.** Reads, top-ups and personas go in raw. Reads, spend, declined, credit and balance are recomputed from the records every time they are shown, with one starting credit for the account. A total copied from a device would be wrong the moment a second device existed.
4. **One file per device, written only by that device.** Each device is fingerprinted once (the id it already uses as its clone branch, `nr-` and eight characters, kept in local storage) and writes everything it originated to its own file, whole, on every sync. Two devices never write the same file, so there is nothing to merge at the file level and no conflict by construction; the compare-and-swap on publish still guards the ref, and a race there is merged by the library at file level, which keeps both files.
5. **The consolidated view is computed, not stored.** Opening the vault reads every device's file and builds one view: per device, and in total. Bringing other devices' activity into a browser adds their records to its local storage, tagged with the device they came from, and recomputes the totals; the next sync from that browser writes only its own records back, so a record has exactly one author for ever.
6. **Keys never leave the device unencrypted and nothing is typed twice.** The passkey derives the door; the door holds the master's key; the master holds the reader vault's key and the access key. The access key is pasted once, on the first device, and lives in the master from then on; a second device gets it by opening the master, which it can do with its passkey once it has a door, or with the recovery code once.

## The data

In the reader vault:

```
activity/
  account.json                  written once: { v, start, symbol, created, created_by }
  devices/
    nr-3f9a1c2b.json            one per device, rewritten whole on each sync
    nr-77e0b4d1.json
```

A device file:

```
{ "v": 1,
  "device":   { "id": "nr-3f9a1c2b", "label": "DC New iPad", "agent": "iPad", "first_sync": "…", "last_sync": "…", "syncs": 4 },
  "created":  "…",                       the local account's creation time
  "reads":    [ { id, at, path, title, kind, topics, price, depth, cost, persona, autoKept?, rating?, declined?, device } ],
  "topups":   [ { ref, at, credit, source, device } ],
  "personas": [ { id, preset?, name, created, on[], off[], visitor?, list?, theme?, device } ],
  "notes":    [ { id, at, kind, path, title, n, story, text, quote, persona, sent?, device } ],      since v0.12.0: the feedback loop
  "wire":     { "seen": { "<story id>": { at } } },                                                  since v0.12.6: what the wire drew for this reader
  "active":   "me" }
```

Every record is the meter's own, unchanged, plus the `device` that originated it (the notes are `assets/vault-pane/notes.js`'s own records, kept apart from the meter's state, and travel in the same file; the stories seen are `assets/vault-pane/wire-state.js`'s). A read's id is made on one device and only that device's meter changes it afterwards (its depth grows while the page is read; a rating or a decline is added), so the device's next sync carries the latest version and the rule "the version that knows most wins" (declined over rated over deeper) is a safety net, not the mechanism.

The totals, recomputed:

| Figure | From the records |
|---|---|
| reads | the number of distinct read ids across every device |
| spent | the sum of `cost` over those reads (a declined read's cost is 0) |
| declined | the sum of `declined.refunded` |
| credit | the sum of `credit` over top-ups, one per payment reference |
| balance | `start` + credit − spent |

`start` is the account's one starting credit, written to `account.json` by the device that created the account; every device's meter begins with the same starting credit locally, and the vault counts it once. Payment references make top-ups unique across devices, which matters because a merged top-up is also added to the device's list of credited references, so a return page opened again on another device cannot credit the same payment twice.

## The flow

1. **First device.** Open the pane, **Enable with your passkey**. The passkey gives the bytes, the bytes give the door, the door is not there: *no door here for this path yet*. Paste the access key, **Create the account**: the door, the master and the reader vault are made; the access key goes into the master; a recovery code is shown once and its door is added. Read some pages. **Update the vault**: this device's file is written, one commit, published.
2. **Second device.** Open the pane, **Enable with your passkey**. The door is there; the master opens and brings the access key; the reader vault opens. *Across your devices* lists the first device with its reads and spend. **Bring that device's activity here**: the records are added to this browser's local storage and the meter now shows the consolidated balance. Read, **Update the vault**: the second file is written. The first device, on its next open, sees two.
3. **A device whose passkey cannot be a door**, or a path that gives other bytes: *no door here for this path yet*, then **Add this device with the code**: the recovery door opens the master, the access key comes with it, and this path gets a door of its own; the code is not needed on that device again.
4. **Forget on this device** clears the session; the vault is unchanged.

The keys for an unlocked session are kept in memory and, for the life of the tab, in session storage, so that moving from page to page does not ask for the passkey each time. This is a choice for the beta, written here so it can be revisited: the article's final shape may keep them in memory only and ask again on each page, or hold them behind a lock screen in the pane.

## What is not synced, and why

- **The active persona and the reading position** are a device's own.
- **Shares** (what the reader sent to the newsroom) are not in the vault yet; they are a record of something that already left the browser.
- **The simulated cart** is unused with a live payment link.
- **Local pruning.** The intent is that local storage holds what the vault does not have yet, and no more. That is not done in this build: the meter keeps its own window of 500 reads regardless, and the vault keeps everything. Pruning needs the meter to read from the consolidated view rather than from its own log, which is phase five of the article's plan.
- **Retiring a device and rotating the master's key** are designed, not built, as before.

## What is built in v0.11.0

- `assets/vault-pane/vault-pane.js` and `.css`: the pane on the right of every page that carries the meter, opened by the **Vault** button beside the balance; the page moves left while it is open and the pane overlays at phone width. Enable, create, join with the code, update the vault, the table across devices, bring their activity here, forget on this device, and every call to the vault server listed.
- `assets/vault-pane/sync.js`: `extract`, `consolidate`, `mergeInto`, `accountFile`, as pure functions, checked by `admin/build/test_sync.mjs` with two devices' states.
- `assets/door.js`: the door derivation, moved out of the lab so the pane and the lab derive the same door from the same bytes; the lab re-exports it.
- `admin/build/test_pane.mjs`: the loop in Chromium against the mock of the vault API, with a virtual authenticator standing in for one synced passkey: device A reads, enables, creates, updates; device B (the same passkey, a cleared browser) enables, sees A, brings A's activity in and shows the consolidated balance, reads, updates; a third opens with the recovery code.
- `/vault/index.html`: the page that explains this and opens the pane.

## What the pane gained after v0.11.0

- **v0.12.0**: a *This page* tab before the vault's, with the notes and the lane to the newsroom, and a *Keys* tab with every vault's key behind Reveal ([the feedback loop](2026-10-12__the-feedback-loop.md)). A device's file carries its notes beside its reads.
- **v0.12.1**: the pane stays open from page to page (the open state and the tab in session storage); a *Reading* tab, every page read here with its decision and the done ones folded away; what the browser knows about the page above the chips; the three steps with the next one in bold; an account made without an access key in its master asks for it once; a send rewrites the device's file (cards 001 to 009).
- **v0.12.6**: what only this browser holds, counted on the Vault button and named in a strip above the tabs with *Update the vault* one press away (`assets/vault-pane/pending.js`); the wire's seen stories in the device file as `wire.seen`, so *New* is right on every device; two window events, `sgit-vault-open` and `sgit-vault-update`, so the wire can ask for the pane and for an update (cards 027, 028).
- **v0.12.8**: *Write to the newsroom*, with *Save and send* (card 034).
- **v0.12.14**: more than one wire, so a seen story's id carries the wire's scope in the device file (`owasp:sec-01`); the Industry Wire's stay bare.
- **v0.12.26**: the inbox, an append lane on the reader vault that a browser without the passkey writes into with a link; what arrives is written as that browser's device file (`combine()` in `sync.js` when it already has one) and brought in by the same merge ([send to my vault from any browser](2026-10-13__send-to-my-vault-from-any-browser.md), card 049).
- **v0.12.58**: two ways in, *Open with your passkey* and *Connect with a link*, nothing named first; after an explicit open the pane asks which device this browser is when the vault knows devices (an existing one is adopted with its records) and brings in what the vault holds on its own; both directions counted above the tabs; every write `combine(prev, extract(local))`, so two browsers may share a device; a sent batch filed under a device of the reader's choosing ([open, or connect](2026-10-13__open-or-connect-a-vault.md), card 059). Principle 4 above now reads: one file per device, and a device is a bucket the reader names.

## The experiments to run next

1. **Two real devices, your own.** iPad and laptop with the same iCloud Keychain passkey: the loop above, watching the number of calls per sync and per open in the pane's log. The question is whether a sync is one commit (it should be: one file) and whether an open is cheap enough to do on every page.
2. **A page read on both devices.** Open the same article on both after a merge: two read ids for one page, charged twice, which is the meter's rule today (a page is charged once per session per device). Decide whether the consolidated view should show it once.
3. **Ratings and declines after a merge.** Rate a page on the device that read it after the other device has merged it; sync both; check the other device's copy updates on its next bring-in (it should: the author's version wins).
4. **A top-up on one device, a return page on the other.** The merged payment reference should stop a second credit.
5. **Pruning.** Once the meter can read the consolidated view, drop local records that a device's file already holds, and measure what the meter loses (nothing, if the view is complete).
6. **Automatic sync.** A timer, or a sync when the tab goes to the background, as a setting the reader turns on, once the per-sync cost is known from experiment 1.
