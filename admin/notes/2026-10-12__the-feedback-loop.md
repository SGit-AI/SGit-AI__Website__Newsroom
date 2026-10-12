# The feedback loop: notes kept as you read, carried by the vault, sent down a lane of their own

*12 October 2026, built in newsroom.sgit.ai v0.12.0. Status: a beta, against dev.send.sgraph.ai, with one reader. The pieces it stands on: [the activity vault](2026-10-12__the-activity-vault.md) (the pane, the device files, the consolidated view) and [one door per passkey path](2026-10-12__one-door-per-passkey-path.md). The brief it answers is the first item of [The site is an inbox](../../articles/the-site-is-an-inbox.html), read in [what the new articles ask](2026-10-12__what-the-new-articles-ask.md), narrowed to what one reader and the agent that runs the site need to learn from each other before anything is automated.*

## In short

- **A note is one tap at a piece**: read later, not for me, more like this, liked, wrong, fix this, idea; with words if the reader adds them and the phrase they had selected on the page. It is a record, like a read in the meter: kept in local storage the moment it is made.
- **The vault carries it, when the reader asks.** Update the vault writes this device's notes in the same file as its reads; another device brings them in, tagged. Nothing new in the sync model.
- **The lane carries what the reader chooses to send.** Send to the newsroom puts the notes not yet sent into a vault of their own, one file per note. The reader keeps the write key in their master; the newsroom gets the read key, once, in the open, and reads with `sgit clone` or `admin/build/lane.py`. Nothing else of the reader's is in the lane, so the reader never shares the reading account to be heard.
- **The keys are the reader's.** A Keys tab lists every vault of the account with its key behind Reveal: the doors, the master, the reader vault, the lane. Any of them opens on its own, in sgit or in the vault app.
- **On the wire, the decision is at the story**: four of the brief's seven at each card; a decided story folds to its headline, with undo. "Not for me" is the signal the wire's desk asked for, and it is a note like any other.

## Why this and not the news automation first

The wire's next turns (a pitched story becoming an article, placement on the front page, the weekly newsletter) are worth building when there are readers to place for. Today the site has one reader who is also its owner, and what is missing is not output but the return path: a way for that reader to say, at the moment of reading, what is wrong, what to do next, what to drop, and for the agent that runs the site to read that without being handed the whole account. The vault was the right kind of experiment: small, real, and it was known to work by the next morning. This is the same kind.

## The record

```
{ id, at, kind, path, title, n, story, text, quote, persona, sent?, device? }
```

| Field | What it is |
|---|---|
| `kind` | `read-later`, `not-for-me`, `more-like-this`, `liked`, `wrong`, `fix`, `idea`; or `note` when there are words alone |
| `path` | the page, as the meter records it (`/articles/the-site-is-an-inbox.html`, `/wire/`) |
| `n` | the article's number from `articles/ids.json` when the page is an article, else null; the number is the contract |
| `story` | a wire story's id when the note is about one, else null |
| `text` | the words the reader added, up to 2,000 characters |
| `quote` | what was selected on the page when the note was made, up to 600 characters |
| `persona` | the meter's active persona at the time |
| `sent` | `{ at, lane }` once it has gone to the lane; set only on this device's own notes |
| `device` | set on notes brought in from another device, never on this device's own |

Kept in `localStorage` under `sgit.notes.v1`, apart from the meter's state, so the meter's own writes never touch it (`assets/vault-pane/notes.js`). In the reader vault: inside `activity/devices/<device>.json`, as `notes[]` beside `reads[]`, written whole by that device and only by it (`assets/vault-pane/sync.js`). In the lane: `notes/<id>.json`, one file per note, with `device` and `sent_at` added; a note sent twice rewrites its file.

## The lane

A vault of its own, made the first time the reader sends, by the pane, with the access key the master holds. Its record in the master, `lane.json`: the vault key, the read key, when and by which device it was made. The read key is the library's own derivation exported in the form the CLI clones with, `sgit_public_read_<64 hex>:<id>`; it opens the vault for reading and carries no write capability, which is a separate derivation it does not hold. The test proves both: the CLI clones the lane with the read key alone and reads every note, and a push from that clone is refused.

What the lane is not: a channel the newsroom can write back on. A reply goes the way replies go on this site, as a new version of an article or a note on a page, and a reply lane is the next thing to design if that proves too slow.

## The loop, step by step

**The reader.**

1. Read. On any page, open the pane (the Vault button beside the balance; it opens on *This page*). Select a phrase if one is the point. Tap a kind. Add words and press *Keep the words* if there is more to say. On the wire, tap the decision at the story.
2. Now and then, in the *Vault* tab, *Update the vault*: the notes travel with the reads to the other devices.
3. When there is something for the newsroom, *Send to the newsroom*. The first send makes the lane and shows its read key; hand that key to the agent once. Later sends go to the same lane and need nothing handed over.
4. In *Keys*, any vault's key, to open it elsewhere.

**The newsroom.**

1. With the read key in the environment, never in a file of the repository:
   ```
   NEWSROOM_LANE_KEY=sgit_public_read_…:… python3 admin/build/lane.py
   ```
   clones the lane the first time and pulls after that, then prints the notes grouped by page, newest first, with the article number, the kind, the quote and the words. `--json` gives the records; `--dir` names the clone. A vault key is refused: the newsroom is not to hold write access to a reader's vault.
2. Act on them in the open: a fix in a release, a version of an article, a line in a note. The version row says which notes it answers, by page and kind, never by quoting a note the reader did not make public.
3. Nothing is sent back through the lane.

## What is not built

- **Three of the seven decisions**: read now, comment (words are a note; a comment addressed to a sentence is a mark, which is item 3 of the brief), move to a persona.
- **The pane about the piece** (item 2 of the brief): the article's graph, the marks and the cost in the pane. The pane now has tabs, which is where that goes.
- **Signing.** A note in the lane is not signed; the lane's existence in the reader's master is what says whose it is. Persona key pairs are item 5 of the brief.
- **A reply lane** from the newsroom to the reader.
- **The front page.** It is imported, so the decisions are on the wire and on article pages, not on the front page's cards.
- **Sent marks reach other devices only with the next Update**, not with the send; a second device sees a note as unsent until the first device updates. A second device does not send another device's notes.
- **Pruning**, as before: local storage keeps every note.

## The experiments

1. **A week of use by one reader**: notes per day, which kinds, how many led to a change in a release. The honest measure is whether the reader keeps doing it.
2. **The morning read on the wire** with the lens set to the named reader: "not for me" and "more like this" at each story, and whether the desk's weekly pass can propose persona edits from the lane alone.
3. **Two devices**: notes made on a phone, updated, brought into a laptop, sent from there; the "sent" marks after the next update.
4. **The agent reading the lane at the start of a session** and acting before anything else is asked: whether that changes what the sessions do.
5. **Which chips are never pressed.** Seven is a guess; the brief said six kinds of mark and seven decisions. The ones not used in a month go.
