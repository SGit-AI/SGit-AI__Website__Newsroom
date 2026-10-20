# The numbers, and the file each one comes from

Every number this publication printed about the Summit, with the file it is derived from. **None
was typed twice**: the pages read these files, and a gate re-derives the rendered counts. If a
number here disagrees with a page, the file is right and the page is a bug.

## The event, as its own pages describe it

| Fact | Value | From |
|---|---|---|
| Name | Startup Summit Lisbon 2026 | [`event.json`](https://newsroom.sgit.ai/portugal/data/event.json) |
| Main dates | 17–18 September 2026 | `event.json` → `dates.main` |
| Pre-event | 16 September, Welcome Drinks, 19:00 | `event.json` → `dates.pre_event` |
| Venue | Unicorn Factory Lisboa, Beato Innovation District | `event.json` → `venue` |
| Organiser | StartUp Events | `event.json` → `organiser` |
| Stages | 3, and **named two different ways on two pages** | `event.json` → `stages` |

## What was counted

| Count | Value | From | Note |
|---|---|---|---|
| Speakers listed, 13 Sep | **64** | [`people.json`](https://newsroom.sgit.ai/portugal/data/people.json) | On the published list at that moment |
| Speakers listed, 8 Sep | **60** | [`changes.json`](https://newsroom.sgit.ai/portugal/data/changes.json) | |
| Arrived / left between | **+5 / −1** | `changes.json` | The departure carries no reason |
| With a LinkedIn link | 61 of 64 | `people.json` | A property of the list, not a judgement |
| Organisations | **61** | [`orgs.json`](https://newsroom.sgit.ai/portugal/data/orgs.json) | Derived from the cards, never typed |
| — of which placeholders | 2 | `orgs.json` | `Independent`; flagged, not removed |
| — with more than one speaker | 3 | `orgs.json` | |
| Sessions | **16** on 3 stages | [`sessions.json`](https://newsroom.sgit.ai/portugal/data/sessions.json) | Every title verbatim in the frozen agenda |
| Press pages in the register | **7** | [`coverage.json`](https://newsroom.sgit.ai/portugal/data/coverage.json) | Frozen before cited |
| — excluded, with reason | 1 | `coverage.json` → `excluded` | Returned 404 |
| Frozen files | **88** across 2 captures | [`sources.json`](https://newsroom.sgit.ai/portugal/data/sources.json) | Every hash re-verified per build |
| Files in the manifest | 111 | [`manifest.json`](https://newsroom.sgit.ai/portugal/data/manifest.json) | Everything the section is built from |
| Stories | 3 | [`stories.json`](https://newsroom.sgit.ai/portugal/data/stories.json) | |

## The graph

| Count | Value | From |
|---|---|---|
| Nodes | **329** | [`graph.json`](https://newsroom.sgit.ai/portugal/data/graph.json) → `counts` |
| Edges | **1,106** | `graph.json` |
| Node types | 16, each with a Portuguese label | [`ontology.json`](https://newsroom.sgit.ai/portugal/data/ontology.json) |
| Verbs | 19, each with a **distinct named inverse** and a Portuguese form | `ontology.json` |
| Banned verbs | 4 — `related_to`, `mentions`, `associated_with`, `works_at` | `ontology.json` → `banned` |
| Packs | 10, switched on block by block | `graph.json` → `packs` |
| Triples | **4,001** | [`triples.nt`](https://newsroom.sgit.ai/portugal/data/triples.nt) |

Nodes by pack: event 3 · orgs 61 · people 64 · sessions 19 · sources 90 · changes 2 · coverage 14
· stories 3 · topics 23 · tags 50.

## The derivation layer

| Count | Value | From |
|---|---|---|
| Distinct topics (the **event's own** words) | **23** | [`topics.json`](https://newsroom.sgit.ai/portugal/data/topics.json) |
| Speaker pages carrying a topic list | 60 of 64 | `topics.json` |
| Lexicon patterns (the published formula) | **57** | [`lexicon.json`](https://newsroom.sgit.ai/portugal/data/lexicon.json) |
| Derived tag edges | **417**, each carrying the words it matched | `topics.json` → `person_tags` |
| Distinct tags used | 50 | `topics.json` |
| Connection rows | **90** across 3 queries | [`connections.json`](https://newsroom.sgit.ai/portugal/data/connections.json) |

## The consoles

| Count | Value | From |
|---|---|---|
| Tables built in the browser | 15 | [`tables.json`](https://newsroom.sgit.ai/databases/data/tables.json) |
| Rows loaded | 2,454 | the loader, at run time |
| Worked SQL queries | **16**, each executed at build | [`queries-sql.json`](https://newsroom.sgit.ai/databases/data/queries-sql.json) |
| Worked SPARQL queries | **13**, each beside its Cypher equivalent | [`queries-sparql.json`](https://newsroom.sgit.ai/databases/data/queries-sparql.json) |

Every worked query stores the count it returned at build, printed next to it on the page, so a
reader's run can agree or differ **in the open**.

## The numbers this publication refused to print

- **Attendance.** The event's pages state a target of "2,000+"; no source gives a result, and a
  gate fails the build if a target is rendered as a count.
- **Speaker total as a fact about the event.** "150+ speakers planned" is the event's wording. 64
  is what its own list named on 13 September. The two are different claims and are never merged.
- **Countries.** "40+ countries" appears on the event's pages. No speaker card carries a country,
  so this is recorded as **unverifiable from the source** in
  [`checks.json`](https://newsroom.sgit.ai/portugal/data/checks.json) — not as doubted.
- **Any count about what happened at the event.** There is no capture from during or after it.
