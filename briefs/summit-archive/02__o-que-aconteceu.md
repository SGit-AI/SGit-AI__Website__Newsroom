# What happened: six days, two captures, three stories

A chronology of the Startup Summit Lisbon 2026 beat, reconstructed from the register, the release
history and the frozen bytes. Every date below is checkable: the captures carry retrieval times,
and every release row is at https://newsroom.sgit.ai/admin/versions.html.

## The timeline

| When | What | Where it is recorded |
|---|---|---|
| **8 Sep 2026** | First capture. Five pages of the event site frozen and hashed. The speaker list carried **60 names** | [`sources.json`](https://newsroom.sgit.ai/portugal/data/sources.json), snapshot `2026-09-08` |
| **13 Sep** | Second capture: fourteen pages plus every speaker's own page, 88 files in all. The list now carried **64 names** — five arrived, one left | [`changes.json`](https://newsroom.sgit.ai/portugal/data/changes.json) |
| 13 Sep | **v0.3.0** — the section ships: the ingestion path, the register, the people and organisation pages, two stories | [release](https://newsroom.sgit.ai/admin/versions.html) |
| 13 Sep | **v0.3.1** — the data-protection notice that should have shipped with v0.3.0, written after a review caught its absence, and recorded on the page as a miss | [`notice.json`](https://newsroom.sgit.ai/portugal/data/notice.json) |
| 13 Sep | **v0.3.2** — the graph, the file explorer, the newspaper front page; seven press pages enter the register and the third story is written | [`coverage.json`](https://newsroom.sgit.ai/portugal/data/coverage.json) |
| 13 Sep | **v0.3.3** — SQLite and a SPARQL store begin running in the reader's browser over the same files | [`/databases/`](https://newsroom.sgit.ai/databases/index.html) |
| 13 Sep | **v0.3.4** — every speaker's own page is frozen; topics and derived tags enter the graph; the connections page answers who should talk to whom | [`topics.json`](https://newsroom.sgit.ai/portugal/data/topics.json) |
| 14–20 Sep | v0.3.5 – v0.3.12 — the design, the menus, the research briefs, the pack, the sibling transfer | [release history](https://newsroom.sgit.ai/admin/versions.html) |
| **17–18 Sep** | **The event itself.** This publication did not attend and holds no capture from during or after it | — |

**The gap that matters.** The register stops on 13 September. Everything this publication says
about the Summit is about a *published list before the doors opened*. It has no attendance figure,
no report from the room, and no capture of what the site said afterwards. That is a boundary, not
an omission, and it is stated on the section's own [about page](https://newsroom.sgit.ai/portugal/about.html).

## What the two captures bought

One capture proves a claim. Two prove a trajectory — and the second is the only reason story 2
exists at all:

```
2026-09-08   speakers.snapshot   60 listed
2026-09-13   speakers.snapshot   64 listed      +5 arrived, −1 left
```

The departure is the part worth reading twice. `kambis-kohansal-vajargah` is present in the 8
September bytes and absent from the 13th. Withdrawal, a scheduling clash, a duplicate record and
an editing error are **indistinguishable from outside**, so `changes.json` carries
`"reason_known": false` and every rendering of it leaves the reason blank. A gate fails the build
if a reason ever appears. Guessing at why a named person left a list would be the single easiest
way for a publication like this one to do real harm.

## The three stories, and what each one cost

**Story 1 — Two names for three stages.** Cost: reading two frozen pages carefully. The agenda and
the AI-summary page, published by the same event on the same site on the same day, name the stages
differently. Recorded in [`checks.json`](https://newsroom.sgit.ai/portugal/data/checks.json) as
`stage_names`, with both sets. Neither is corrected; both are shown.

**Story 2 — Five names arrived and one left.** Cost: the discipline of capturing twice before
there was anything to say. On 8 September the capture looked like housekeeping. It became the
story on the 13th.

**Story 3 — A record attempt the agenda does not mention.** Cost: widening the register to
third-party pages, which meant a new rule. Press pages are frozen and hashed like any other source
*before* they can be cited, summarised in this publication's own words, and never quoted at length
— gate 15 fails the build on a quotation of 60 characters or more. Seven pages entered. An eighth,
an April Eventbrite listing, returned a 404 body and is recorded in `excluded` **with the reason**,
because a source that is absent is itself a fact.

## Three things that went wrong, and what they changed

Kept because a method that only records its successes is a brochure.

1. **v0.3.0 shipped 64 named people without a data-protection notice.** Caught by a review the
   same day. v0.3.1 wrote the notice, added the gates that enforce it at extraction time, and
   recorded the miss on the page rather than quietly fixing it.
2. **A claim on a page said "five of six" and had become false** when the underlying data moved.
   The fix was not to correct the sentence but to add the gate that re-derives every rendered
   count from the file it claims to come from.
3. **The posture on biographies changed under pressure and was nearly changed silently.** The
   original rule was "not extracted". Reading the speakers' own pages for topics and lexicon
   matches meant the honest rule became "not *reproduced*; read by a published formula that keeps
   only the matched words". That is a real change, and it is written into the notice, the method
   page and the release history rather than left as a quiet drift.

## What a successor should do first

- **Capture again.** The register's last word is 13 September. A capture today would show what the
  event's site says about an event that has now happened, and the diff would be the story.
- **Write the fourth piece.** The first three all work by publishing what the record does and does
  not contain. That trick works once per source; by the fourth piece a publication has to say
  something about the subject itself.
- **Do not backfill.** Nothing may be added to the 8 or 13 September captures now. If a page was
  not frozen then, this publication does not know what it said then, and saying otherwise would
  undo the only thing the method is for.
