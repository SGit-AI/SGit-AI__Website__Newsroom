# The wire as an inbox: what is new, what is for me, what I decided, and nothing lost

*13 October 2026, built in newsroom.sgit.ai v0.12.6. Status: a beta with one named reader. It applies [The site is an inbox](../../articles/the-site-is-an-inbox.html) to [the Industry Wire](../../wire/index.html), on the pieces of [the feedback loop](2026-10-12__the-feedback-loop.md) and [the activity vault](2026-10-12__the-activity-vault.md). The cards are on [the engineering board](../../engineering/index.html), 023 to 030.*

## In short

- **The wire is read as an inbox.** Every story the reader has not decided about is in it; a decision takes the story out. The state to return to is empty.
- **New means first seen in this visit.** Every story drawn is recorded as seen; a story nobody had drawn for this reader before, on any of their devices, carries a New flag until the visit ends. A reload keeps the visit.
- **For me and not for me** come from the lens the reader reads as, which is now remembered, and from the join the wire's vault records. The bar says how many new stories are for the reader and how many are not, and the not-for-me ones can be checked and corrected.
- **What changed comes from the vault.** When the wire's agent publishes a release note (the release file, below), the bar shows the releases since the last visit; until it does, it shows the head commit's message and says the vault publishes no release notes yet.
- **Local first, update explicitly, and see what you would lose.** Decisions and seen stories are kept in the browser as they happen and reach the reader vault only on Update the vault. Until then the Vault button carries a count, the pane a strip, and the wire a line with Update the vault one press away.

## The workflow

1. **The desk updates the vault.** Dinis asks the wire's agent for a new edition, and for a description of what changed, written as a release (the release file). That is a commit to the wire's vault; this site needs no release to show it.
2. **Open the wire.** The bar at the top says: since your last visit, N new stories, X for you and Y not for you; what the desk says changed, release by release, with the stories added and updated; and the counts per filter.
3. **Work the inbox.** At each story, one tap: *Done* (processed), *Read later*, *Follow up* (act on it, or write about it), *Not for me*, *More like this*, *Wrong*. Each is a note with the story's id and takes the story out of the inbox, with undo. Under a lens, the stories withheld from you are listed per beat with the join's reason; on those, *Should reach me* says the join missed you, and *Done* clears them.
4. **Look back by filter.** *Inbox*, *New*, *Read later*, *Follow up*, *Done*, *Everything*. In *Everything* and *Done* a decided story folds to its headline.
5. **Update the vault.** Explicitly, from the wire's bar, the pane's strip or the Vault tab. One file per device, rewritten whole, one commit, as before; it now also carries the stories seen, so another device does not show them as new.
6. **Send to the newsroom**, when the decisions should reach the desk: the notes go down the reader's own lane (the feedback loop), and the desk reads them with the lane's read key.

## The records

| Record | Kept as | In the reader vault | Shown |
|---|---|---|---|
| A decision at a story | a note: `{ kind, story, path: "/wire/", title, at, persona }` in `sgit.notes.v1` | `notes[]` in the device file | the story leaves the inbox; the filters count it |
| A story seen | `seen[id] = { at }` in `sgit.wire.v1` | `wire.seen` in the device file | New when first seen in this visit |
| The visit | `{ start, prev }` in the tab's session storage; `last_visit` in `sgit.wire.v1` | no | "Since your last visit (…)" |
| The lens | `lens` in `sgit.wire.v1` | no | the lens bar, and for you / not for you |

Kinds: `done`, `read-later`, `follow-up`, `not-for-me`, `more-like-this`, `wrong`. A story with any note is decided; the latest note is its state. Notes brought in from another device count as decisions here, and say which device made them.

## What New means

A visit starts when the wire is opened in a tab that has not opened it before; it lasts as long as the tab. When the edition is drawn, every story not yet in `seen` is recorded with the time. A story is New when it was recorded in this visit, here. So: the first visit to the wire in a browser shows every story as new; a reload keeps them new; the next visit shows only stories that arrived since. When another device's activity is brought in through the vault, its seen stories come too, tagged with that device, and are not new here.

## For me, and not for me

The lens is the persona the reader reads as. It is taken from the address (`#lens=`), else the lens chosen last time, else the active persona of the meter when it maps to one of the wire's. Under a lens, the wire's own join (`data/deliveries.json`, written by the vault's code, not by this page) says which stories reached the reader and which were withheld, with the reason. The bar splits the new stories by it, and every beat lists what was withheld. Without a lens, every story is in the inbox and the bar suggests choosing one.

## The release file

*For the agent that keeps the wire's vault. This is what Dinis asks for when they ask you to "describe what changed on the release".*

On every publish of an edition or a change to one, add an entry at the top of `data/releases.json` in the vault, in the same commit as the change:

```json
{
  "schema": "wire-releases/v1",
  "releases": [
    {
      "id": "2026-10-13.1",
      "at": "2026-10-13T08:30:00Z",
      "edition": "2026-10-13",
      "title": "Morning edition, 13 October",
      "summary": "Twelve new stories, three of them in cybersecurity on the same advisory; two stories of 11 October updated with their primary sources fetched.",
      "added": ["sec-09", "sec-10", "ai-11"],
      "updated": ["ai-03", "biz-05"],
      "withdrawn": []
    }
  ]
}
```

- **One entry per publish**, newest first, never edited afterwards; a correction is a new entry.
- **`at`** is the time of the commit, in UTC, ISO 8601. The page shows the entries newer than the reader's last visit, or the latest one when none is newer.
- **`added`, `updated`, `withdrawn`** are story ids from `data/bundle.json`. The page links each to its story and marks updated stories with an Updated flag.
- **`summary`** is plain text, a few sentences, written for the named reader: what changed and what deserves attention. No markup; the page draws it as text.
- **The commit message** starts with the release id, so the history and the file agree.

Until the file exists, the page shows the head commit's message and says the vault publishes no release notes yet. Nothing else in the vault's contract with this site changes ([how the wire works](../../wire/how.html)).

## Local first, update explicitly, and see what you would lose

Everything here is kept in this browser first, and nothing is sent until the reader presses something. The cost of that rule is that until the reader updates the vault, what they did exists in one browser only, and clearing it loses it. So the site counts what the vault does not have yet (`assets/vault-pane/pending.js`): reads started, rated or declined, top-ups, notes kept, given words or sent, after this device's last update; and, separately, stories seen. The count of things done is on the Vault button, with an amber dot; the pane has a strip above its tabs that names them, with Update the vault; the wire's bar has the same line. Updating is still an explicit press: automatic or regular sync is a later decision (card 029).

## What is not built

- **The release file in the wire's vault** (card 026): this site reads it; the wire's agent writes it. Until then the head commit's message stands in.
- **Automatic or regular sync** (029), on purpose: explicit first.
- **The desk reading the decisions** (030): a Not for me or a Should reach me is the signal the join needs, and today it reaches the desk only if the reader sends it down their lane and the wire's agent reads that lane. The morning read in the vault's own workflows writes to a feedback file in the vault, which a reader with a read key cannot do; the lane is how it gets there without a write key.
- **Editions as history.** The page reads the vault's current bundle; a story that left the bundle is gone from the page, though the reader's decision about it remains.
- **The front page** (017): it is imported, so the decisions are on the wire and on article pages only.

## The experiments

1. **A week of morning reads** by the named reader: how long the inbox takes to empty, which decisions are used, how often a Should reach me appears.
2. **Two devices**: decide on the phone, update, open the wire on the laptop: nothing the phone saw is new, the decisions are there.
3. **The first release file** from the wire's agent, and whether the summary is what the reader would have wanted to know.
4. **The count on the Vault button**: whether it is noticed, and how long things stay only in the browser before an update.

## The message for the wire's agent

> When you publish to the wire's vault, add a release entry at the top of `data/releases.json` in the same commit: id, time (UTC), edition, title, a short plain-text summary of what changed and what deserves attention, and the story ids added, updated and withdrawn. The schema and an example are in "The release file" at https://newsroom.sgit.ai/admin/notes/2026-10-13__the-wire-as-an-inbox.md. newsroom.sgit.ai shows the releases since the reader's last visit at the top of the wire.
