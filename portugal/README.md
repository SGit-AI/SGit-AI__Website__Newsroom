# Portugal Startups — beta

A publication mapping the Portuguese startup ecosystem. **First beat: Startup Summit Lisbon
2026**, 17–18 September 2026 at Beato Innovation District.

Built from [the 12 May 2026 briefs](https://newsroom.sgit.ai/mvps/portugal.html) — the
bilingual publication brief and the newsroom workflow brief — which specified this
publication and were never run. This is the first attempt to run them.

## What is different about this section

It is the **first section on this site whose sources are primary, frozen and hashed.**

[The Governance Wire](../governance/README.md) specifies a `frozen` state — a hashed byte
copy of the source — and carries `blocked: true` against it, because the fetch-freeze-hash
path was never built. Nothing has ever passed that door, which is why every fact there is
`secondary` and nothing is anchored.

Here the path runs:

```
fetch  ->  freeze  ->  hash  ->  extract  ->  diff
```

A claim on this section points at bytes in this repository, not at a URL that may have
moved since anybody looked. `gates.py` re-verifies every SHA-256 on every build.

It also has a **named human editor of record**, Dinis Cruz, who reviews every page before
it publishes — `human_in_the_loop: true`, unlike the fully-agentic sibling. That is
deliberate: this beat is about named people and named companies in a small ecosystem,
where being wrong in public costs somebody other than us. It answers open question 5 of
the original brief, which that brief left unanswered and this site called the question it
should be most uncomfortable about.

## Shape

```
portugal/
  sources/frozen/<date>/*.snapshot   the frozen byte copies — EVIDENCE, not pages
  data/
    event.json       the event as its own site describes it, each field naming its source
    people.json      64 speakers: name, role, org, links. NO biographies
    orgs.json        61 organisations, DERIVED from speaker cards, placeholders flagged
    sources.json     the register: every frozen file with SHA-256, bytes, retrieval time
    changes.json     snapshot-to-snapshot diffs, with the hash of both sides
    checks.json      what re-reading established, and what cannot be verified
    team.json        seven agent roles + the named editor of record
    stories.json     the story index
  content/*.md       story prose
  build/
    extract.py       the ingestion path: fetch, freeze, hash, extract, diff
    build.py         the projection: JSON + markdown -> HTML
    gates.py         ten section checks
```

### Why frozen copies are `.snapshot` and not `.html`

They are unmodified bytes of **another organisation's pages**, held so a claim can be
checked. They are evidence, not content. A non-HTML extension keeps them from being served
or indexed as pages of this site — publishing a browsable mirror of somebody else's whole
website under this domain would contradict the one rule this publication has, which is
that it links rather than reproduces. The bytes are untouched, so the hash still verifies.

The same rule governs speaker biographies: not extracted, not stored, not published. Gate
check 10 fails the build if any node field grows long enough to be one.

## Build

```bash
python3 portugal/build/extract.py --fetch   # take a new dated snapshot, then re-extract
python3 portugal/build/extract.py           # re-extract from the copies already held
python3 portugal/build/build.py             # regenerate the pages
python3 admin/build/chrome.py               # inject site nav + footer
python3 portugal/build/gates.py             # the ten section checks
node admin/build/validate.js                # the whole-site gate
```

Taking a snapshot on a cadence is the whole point. The most valuable copy of the speaker
list will be the one taken the day after it stops being updated.

## The ten gates

1. Every frozen file exists and **still hashes to its registered SHA-256**. If a copy was
   modified, every claim resting on it is unsupported and the build stops.
2. Every speaker and organisation traces to a source that exists.
3. Counts in the data match the lists they describe.
4. **No removal is given a reason**, and no page uses a word that implies one.
5. **No target is reported as a result** — "targeting 2,000+" is a plan, not attendance.
6. Every organisation anchor a speaker row links to actually exists.
7. The posture is stated on every page: beta, the editor of record by name, frozen-and-hashed.
8. No page claims a Portuguese edition that does not exist.
9. Stories trace to registered sources, and their pages match their markdown.
10. No node field is long enough to be a reproduced biography.

## What is real, and what is not

| | |
|---|---|
| Primary sources, frozen and hashed | **Real** |
| Snapshot diffing, with both hashes published | **Real** |
| Named human editor of record | **Real** |
| A closed speaker/organisation graph for one event | **Real** |
| A map of the Portuguese startup ecosystem | **Not yet** — one event is a sample, not a census |
| Corroboration | **None** — every source has the same publisher, the event itself |
| Session-to-speaker joins | **Not built** — the source does not join them either |
| Anything in Portuguese | **Not published** — labels carry `pt`, the switch is not thrown |

## Licence

CC BY 4.0, as the rest of the site. Frozen copies remain the property of their publisher
and are held for verification, not relicensed or republished.
