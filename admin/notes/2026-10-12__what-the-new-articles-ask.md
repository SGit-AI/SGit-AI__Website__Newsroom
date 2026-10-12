# What the new articles ask of this site

*12 October 2026, written for newsroom.sgit.ai v0.11.1, the release that imports sgit.ai v0.7.70. Status: an analysis and a proposed order; nothing in it is built unless a version row says so.*

sgit.ai published five articles on 12 October and revised the passkey article twice. Three of the five are briefs addressed to the session that runs this site. This note reads them against what runs here at v0.11.0, sorts their items into done, ours to build, and sgit.ai's to build, and proposes an order.

## In short

- **The briefs assume v0.11.0.** They are written on top of the vault pane, the reading records in the reader vault, the door per path and the wire read from a vault. Each of those is a property they rely on, and none of them asks for those to change.
- **The next thing is the inbox mode on the wire**: seven one-tap decisions at each story, recorded as edges in local storage and carried by the sync. It is the smallest item, it is first in the brief's own order, and "not for me" is the feedback the wire's desk is waiting for.
- **The second is the pane about the piece**: the right-hand pane becomes about the article in front of the reader, with tabs, and the ways into the article (headlines, facts, relationships, what is new) are computed from files this site already publishes.
- **Several items are not this site's.** The fold under the abstract, the newsletter cut by the reader's default, the Editor placing wire stories on the front page and a pitched wire story becoming an article are sgit.ai's pages and roles; the imported pages are never edited here, so those go to the sgit.ai session as asks.
- **One item is cheap and honest and no brief orders it**: the five counts of *Firing journalists*, run on this site from its own files and published.

## The five articles, and what each one asks

### The vault is live (81)

A description of v0.11.0 as it stands, drawn: the layers, the key chain, the sync model, the tests, the timeline. It asks for nothing new. Its value for the next steps is its list of what is not built, which is the same list as [the activity vault](2026-10-12__the-activity-vault.md) note: pruning local storage once the vault holds it, retiring a device, rotating the master's key, automatic sync, the key pairs for signing, the persona vault, the notes lane to the newsroom. It marks the keys of an unlocked session living in the tab's session storage as a choice to revisit, and that stands.

Its argument matters more than its list: the brief that follows could not be written until the properties of what runs were known. The order below keeps to that. Each step ships a property, the version row and the note record it, and the next brief is written against it.

### Two agents, one vault (80)

The wire as it runs, from both git logs. The next turns it names:

| Turn | Whose | Where it stands |
|---|---|---|
| A pitched wire story becomes an article that inherits the story's frozen sources and provenance graph | sgit.ai's newsroom roles (the Journalist pitches, the Editor places) | Designed in the vault's runbook; not started. The story's sources and graph are in the vault, so the inheritance is a read with the key already on this site. |
| The Editor places up to three wire stories on the front page with a reason per slot | sgit.ai's Editor decides; this site renders | The front page is imported, so a wire slot here would be injected at build from a placement file in the vault, which keeps the imported page unedited. Not built. |
| A weekly newsletter cut from the week's briefs, every quote checked against frozen bytes at build time | sgit.ai's newsletter | Not built. |
| The morning read: more like this, not for me, write about this, wrong, each writing a line to a feedback file; a weekly pass proposes persona edits as a diff | the named reader, on this site, with a private vault | The private vault exists since v0.11.0. The four actions are four of the inbox brief's seven decisions. This is the same build as the inbox mode, below. |

### The site is an inbox (82)

The brief for what a reader does with the vault, with its own order. Read against v0.11.0:

| Item | What exists | What is missing |
|---|---|---|
| 1. The inbox mode on the front page and the wire: read now, read later, not for me, more like this, less like this, comment, move to a persona; one tap at the piece; each clears it; recorded as an edge in local storage; test with the wire first | The wire page lists stories under a lens; the meter records reads, ratings and declines as records; the sync carries records, never totals | The decisions, as a record of their own kind in local storage, in the device file and in the consolidated view; the row of seven at each wire story; the piece leaving the inbox; the front page, which is imported, is the harder surface |
| 2. The pane about the piece: the article's graph, the reader's marks and decisions on it, what it cost; the vault and the meter move to a tab | The pane, on the right, about the vault; every article's graph as JSON beside it; the cost per read in the meter's log | Tabs; the graph drawn in the pane; the decisions and cost for this piece; the meter's card at the end of the article stays, for the rating that sets a price |
| 3. Marks with kinds: interesting, great phrase, not sure, fact, evidence, question; select a phrase, choose a kind, see it in the pane and the graph; the reader can add a kind | Nothing | A mark as a node (phrase, article and version, persona, kind, time), kept like every other record; the selection UI; the link from a phrase to the graph node it belongs to |
| 4. The free signals: depth as "you read this", awake time, from and to | Depth, charged by the meter and kept per read | Awake time, counted only while there is movement, as an experiment; from and to; the account page showing them |
| 5. Persona key pairs in the master, random, one pair per persona | The master vault, holding the reader vault's key and the access key | The pairs, generated on first use, as the passkey design specifies |
| 6. The signed lane: a mark addressed to the newsroom, signed, sent, copied to the vault; the reply as a version | The reading share, encrypted in the browser to the list agent's key, into a write-only lane | The signature; the copy in the reader's vault; the reply as a version is sgit.ai's side |
| 7. The views: vocabulary on demand, the piece classified | The five readers' output for 5 articles, as pages | Both views, starting from that output where it exists |
| 8. An experiment per feature: two variants, a synthetic reader, a measurement | The synthetic-users method, run once on this site | Running it per feature; the first three to test are the inbox decisions, the kinds of mark and the awake-time proxy |

What not to build, and what it changes here: no decision placed at the end of a page, so the seven decisions go at the piece, in the inbox and at the top of an open article, and the meter's rating card at the end stays what it is, a price; no signal sent anywhere without a press, which the pane already keeps to; no mark the reader cannot see in their records, which the device file and the consolidated view already give; no server of ours.

### Ways to read one article (84)

The modes in the pane about the piece, on top of item 2 above. The ones that can be computed today, from files this site already publishes:

| Mode | Computed from | Exists for |
|---|---|---|
| Headlines | the title, the In short, one sentence per section | every article |
| The infographic | the figures in order, with captions | every article with figures |
| The facts, the relationships, the vocabulary | the article's graph JSON | every article |
| Two minutes, the slides, the arc | the five readers' pages | 5 articles; the mode says so and offers the nearest for the rest |
| What is new | the Historian's arc crossed with the reader's reading records | 5 articles; the records exist since v0.11.0 |
| At my level, through my persona, a question | a model in the tab, through the Prompt API | not here; the page says so plainly |

The brief's other items: a default mode per persona, kept with the persona; the mode in the address, so a reading list can say "the slides of this one"; on the phone the pane as a sheet from the bottom, where today it overlays; the email cut by default is sgit.ai's newsletter; a figure drawn for this reader, later. The fold under the abstract on the article pages is sgit.ai's to remove, since those pages are imported unedited.

One wording change: the finished article is not "prose". This site's own pages use the word about the World News Day op-eds' text and in two build notes about rendered pages, not about an article's standing beside its graph, so nothing here needs to change; the article pages are sgit.ai's wording.

### Firing journalists (83)

An argument about publishers, with five counts that read one from outside: original share, sourcing, corrections, roles, the metric reported. The article says this site has the data to run them on itself and would publish the result. It does: the articles and their graphs for the first two, with a check that the source links still resolve; the corrections page and the version pages for the third; the newsroom's roles for the fourth; the meter for the fifth. A page built from those files at release time, with the honest line the article predicts (original share high, sourcing high, corrections kept but not yet propagating, roles all agents and one person, a metric that measures value to the reader with almost no readers yet), is a day's work and costs nothing to keep current.

### The passkey opens the vault, v1.4.0

Revised twice after this site's lab. Its brief for this site, read against v0.11.0: "no door here yet" is what the pane says (done); the reading account in the reader vault (done); a door added with no key typed, which the lab does and the pane does not; the pane showing the master's entries and its doors, with a lock, where the pane has "Forget on this device" and no list of doors; retiring a door (not built); several passkeys giving several masters (not tested); the tests repeating the four runs (the lab's and the pane's tests cover the platform path and the recovery code; the hybrid path is covered by the note, not by a test); the report to Apple and Google, which is the owner's.

## What belongs to sgit.ai, not here

These are in the briefs and are changes to pages this site imports unedited, or to roles that run there. They go to the sgit.ai session as asks, with a link to this note:

- the fold under the abstract on the article pages, which the modes replace;
- the newsletter cut by the reader's default mode;
- the Editor placing wire stories on the front page, with a reason per slot, and the placement file this site would read;
- a pitched wire story becoming an article with the story's provenance;
- the reply to a signed mark as a new version of the article;
- the word "prose" on the article pages.

## The order proposed

1. **The inbox decisions on the wire** (brief item 1 and the morning read). A decision is a record, kept in local storage beside reads and ratings, in the device file and in the consolidated view; the wire page shows the seven at each story and clears it; the account page lists them. Test with the wire. Measured by: the named reader's decisions over a week, and whether "not for me" reaches the desk, which is a read key to that slice when the reader chooses to give it.
2. **The pane about the piece** (brief item 2 and the computed modes). Tabs in the pane: the piece, the vault. On an article: its graph drawn, the decisions and the cost, and the modes row, computed first: headlines, the facts, the relationships, the vocabulary, the infographic, with two minutes, the slides and the arc where the five readers' pages exist, and what is new from the reader's own records. The phone gets the sheet.
3. **Marks with kinds, and the free signals** (items 3 and 4), with the experiment the brief asks for on the awake-time proxy.
4. **The five counts, run on this site**, as a page built at release from the files.
5. **The passkey follow-ups in the pane**: the master's doors listed, a door added from the pane with no key typed, a door retired.
6. **Persona key pairs and the signed lane** (items 5 and 6), after the passkey follow-ups, since both live in the master.

Each step is one release with a version row, and each ships with its test file. The open items from earlier notes stand beside this order and are not displaced by it: a fresh wire vault, the daily wire run scheduled, deploys gated on green tests, the access key in CI for the live check, the upstream issue for creating a vault at a chosen address, and the report of the PRF difference by path.
