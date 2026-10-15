# Open, or connect: the two ways into a reader's vault, which device a browser is, and what comes back

*13 October 2026, built in newsroom.sgit.ai v0.12.58. Card 059. The ask, in chat with two screenshots: the aggregation is the point, so a browser that opens the vault should show the account's balance, recomputed from what it received; the workflow is open a vault or connect a vault, not name a device first; and a browser that sends should be able to file what it sent under a device the reader already has. The pieces it stands on: [the activity vault](2026-10-12__the-activity-vault.md) (the device files, the consolidated view, the merge) and [send to my vault from any browser](2026-10-13__send-to-my-vault-from-any-browser.md) (the inbox).*

## In short

- **Two ways in, nothing to name first.** *Open your vault* with the passkey: the browser reads and writes. *Connect with a link*: the browser only sends, into the vault's inbox. The locked pane offers both, and asks for no label before either.
- **Which device is this, asked once, after the open.** When the vault already knows devices and this browser is none of them, the pane lists them and offers a new one. Two browsers may share a device.
- **What the vault holds comes here.** After an explicit open, the other devices' records are merged into this browser on their own, and the meter shows the account's balance. Both directions are counted above the tabs: what is only here, and what is in the vault and not here.
- **A sent batch is filed where the reader says.** Where the vault is open, each sending browser's batch has a choice: a device of its own, or one the reader already has, this browser included. The choice is remembered.
- **Every write is combined with the file as it is**, so a shared device never loses one browser's records to the other's.

## The two workflows

| | Open your vault | Connect with a link |
|---|---|---|
| needs | the passkey (or the recovery code, once) | the link from a browser where the vault is open: a URL, text or a QR code |
| reads the vault | yes | no, nothing, not even what it sent |
| writes | its own device file, one commit per update | one sealed message per send, into the inbox lane |
| the meter shows | the whole account, once what the vault holds is brought in | this browser alone |
| which device | asked after the open: one the vault knows, or a new one | the name the browser gives itself; where the vault is open, the reader files the batch under a device of their choosing |
| when it is right for | a browser you keep: a laptop, a Chrome profile, the iPad's Safari | a browser that cannot reach the passkey: a web view an app opened, a browser signed in to nothing, an old iPad |

Opening is the full membership; connecting is the push-only one, and the site is not personalised there. That is the trade the ask accepts: what matters in that browser is that the reads, the decisions and the notes are captured, because they are the reader's own intelligence and the reason they come back. The reader's example: an iPad kept light for reading, no tabs, no distractions; read the article, decide, note, and have that count.

## The states of a browser

1. **Nothing.** The pane's Vault tab offers *Open with your passkey* and *Connect with a link*, and *I have a recovery code* beside the first. A passkey is only offered for making when none answers: soft enforcement, the way in is never a form.
2. **Connected.** A link is kept in local storage (`sgit.inbox.link`). The Vault tab says which vault it sends to, takes *Send as* (the name of this browser, or of a device the reader already has), and offers *Send to my vault* and *Forget the link*; the strip above the tabs offers the send on any page.
3. **Open, device unknown.** The passkey opened the door, the master and the reader vault; the vault knows devices; this browser has never written and is none of them. The pane asks *Which device is this?*
4. **Open, device known.** The unlocked view: this device, what is not yet in the vault, what is not yet here, the devices across, the inbox. From a saved session (a page change) the pane returns straight here.

The reader moves 1 to 2 by pasting or opening a link; 1 to 3 by the passkey or the code; 3 to 4 by choosing; 4 to 1 by *Forget on this device*; 2 to 1 by *Forget the link*. A connected browser that later reaches the passkey moves 2 to 3 like any other.

## Which device is this

The device id is what a browser writes its file under, and the author on every record it originates. Until now a browser made its own id on first use and showed a label field before the passkey; a second browser on the same iPad, or a second Chrome profile, became a second device whether the reader wanted one or not, and the label had to be typed before anything opened.

Now the question is asked once, after the open, and only when there is a choice: the devices the vault knows, with their reads, notes and last update, and *A new device* with a name. Choosing an existing one makes this browser that device: the id and the label are taken, and the merge that follows brings that device's records in as this browser's own (`mergeInto`, `mergeNotes`, `mergeWire` with `own`), so the Reading tab, the notes and the meter are what that device had. A new device needs no name; the label can be set in the unlocked view later.

Two browsers sharing a device write the same file, so **every write is now `combine(prev, extract(local))`** rather than a plain overwrite: every record of either, the one that knows more where both have it. The file can no longer shrink; a note removed in one browser stays in the vault file. The activity vault's rule, one author per record, holds: the author is the device, and the device is now a bucket the reader names.

## What comes back, and when

The pane counted one direction: what was only in this browser, with *Update the vault* one press away. The other direction was a button under the table across devices, and the screenshot that started this showed the result: a vault with four devices, a browser that had brought in none of them, "the vault has everything of this device" in the Vault tab, and a meter £0.18 off the account.

Now `inbound()` (sync.js) counts what a merge would add, without writing: reads, top-ups, personas, notes and stories seen, from how many other devices. It is shown as *Not yet here* in the Vault tab, beside *Not yet in the vault*, with *Bring them here* beside *Update the vault*; and in the strip above the tabs, on every page, with the same button.

After an **explicit** open (the passkey, the code, the account just made, the device just chosen) the merge runs on its own: the reader asked for the vault, and the vault is the account. The page reloads once so the meter reads the merged state, and the Vault tab says what arrived. On a **page change** the saved session opens the vault silently and nothing is merged: a reload under a reader who is reading is not acceptable, so the strip says what is not here and waits for the press.

## Where a sent batch is filed

A browser that connects cannot see the vault's devices, and the link carries no list of them on purpose (it carries where to write and the key to encrypt to, nothing else). So the choice is made where the information is: in the Vault tab, when the batch is listed before it is brought in. Each sending browser gets a *File under* choice: a device of its own (new, or the row it already has), or any device the vault knows, this browser included, which is always offered even before it has a file.

What is chosen first: what was chosen for that browser last time (`aliases` in the master's `inbox.json`, sender id to device id, written only when it changes); else a device whose label matches the name the browser gave itself; else the browser as its own device. Filing under another device re-tags every record with that device and keeps the sender's id as `from` (`refile()`), and the file is combined with the target's as every write is. Filing under this browser brings the records in as its own.

Soft enforcement throughout: the name on the sending side is free text and only a hint; the reader confirms in the pane; nothing is refused for a name.

## Not built

- **Consolidating two devices the vault already has** into one row (merge files, retire the id). The alias machinery is most of it; the ask was "we might need to", so it waits for the need. Nothing is deleted meanwhile, which is the rule the ask set for payment records.
- **Automatic sync on a timer or on leaving a page** (card 029); the inbound side now runs on an explicit open, the outbound side is still a press.
- **A choice of device on the sending side.** The link would have to carry the devices; it stays minimal.
- **The table's pennies.** Each device's spend is rounded to a tenth of a penny before it is shown at two decimals, so the column can add to a penny less than the total. Top-ups now show a dash in the total when there are none, as the rows do.

## Tests

`admin/build/test_sync.mjs`: `inbound()` before and after a merge; a cleared browser taking a device as its own; `refile()`; a write combined with the file as it is. `test_pane.mjs`: nothing to name before opening; device B asked which device it is, choosing a new one, and the vault's records coming in on their own with the account's balance; device C opening with the recovery code and taking device B as its own: B's read is its own there, A's is tagged A, the id and label are B's, the balance is the account's, nothing left to bring in. `test_inbox.mjs`: the *File under* choice before anything is brought in, B's batch filed under A itself, A's own notes and one row across the devices, the choice remembered in the master. `test_notes.mjs`: device B through the chooser.
