# The method, and the eighteen gates that enforce it

What made this beat different from a listing page. All of it is in
[`extract.py`](https://newsroom.sgit.ai/portugal/build/extract.py) and
[`gates.py`](https://newsroom.sgit.ai/portugal/build/gates.py), both in `30__codigo/`, both
runnable from a clone of the repository.

## The path

```
fetch  →  freeze  →  hash  →  extract  →  diff
```

- **fetch** — one dated capture at a time, with a user-agent naming this publication and a contact.
- **freeze** — the bytes land at `portugal/sources/frozen/<date>/<page>.snapshot`. The `.snapshot`
  extension is not cosmetic: it stops any server treating another organisation's page as a page of
  this site. Publishing a browsable mirror of somebody else's site would contradict the one rule
  this publication has, which is to link rather than reproduce.
- **hash** — SHA-256 into [`sources.json`](https://newsroom.sgit.ai/portugal/data/sources.json)
  with the byte count and the retrieval time. **Re-verified on every build**, so a frozen file
  that changed on disk fails the build rather than quietly changing what a story stands on.
- **extract** — the data files are read *from the frozen copy*, never from the live network. This
  is what makes a rebuild from a clone, years later, produce the same pages.
- **diff** — one capture against the next. On this beat the diff **was** the story.

Re-running `extract.py` **without** `--fetch` rebuilds everything from bytes already held and
touches no network. That is the test of whether a publication is really anchored.

## The four rules that survived contact

1. **A claim points at bytes, not at a URL.** A URL is a promise about the future; a hash is a
   statement about the past. Every story here names frozen source ids, and the register turns each
   into a file you can open.
2. **Link, never reproduce.** Biographies, session descriptions, sponsor copy and press pages are
   other people's writing. They are summarised in this publication's words and linked. Reading
   them by a **published formula** that keeps only the matched words is allowed, and is how the
   tags are made — that distinction is the whole of the difference between structuring and
   republishing.
3. **A removal has no reason.** A name present in one capture and absent from the next is recorded
   as exactly that, and nothing more.
4. **Classification is a formula or it does not happen.** `role_class` on a person and every
   derived tag are regular expressions, published in full, re-run against the frozen bytes on
   every build. A reader can argue with a formula. A judgement they must trust is worse.

## The eighteen gates

From `gates.py`, in order. A failure exits non-zero: no build, no release.

| # | What it fails on |
|---|---|
| 1 | A frozen file missing, or no longer hashing to what the register says |
| 2 | A person or organisation that traces to a source not in the register |
| 3 | A count rendered on a page that disagrees with the data file it claims to come from |
| 4 | A removal that has been given a reason |
| 5 | A target reported as a result |
| 6 | A speaker row linking to an organisation anchor that does not exist |
| 7 | The stated posture not matching the data |
| 8 | A page claiming a capability the section does not have |
| 9 | A story whose page has drifted from its markdown, or whose sources are unregistered |
| 10 | Any field long enough to be a reproduced biography |
| 11 | An email, telephone or personal postal address **anywhere in the data** — checked at extraction, not at rendering |
| 12 | A page naming individuals that does not link to the notice |
| 13 | The graph disagreeing with its ontology: a verb without a distinct inverse, a missing Portuguese form, a banned verb, a node with no source, an edge outside its domain and range |
| 14 | A session title not appearing **verbatim** in the frozen agenda |
| 15 | Coverage cited before it was frozen, or quoted at 60 characters or more |
| 16 | A topic that is not on the speaker's frozen page verbatim, or a topic on the page missing from the graph |
| 17 | A derived tag that does not re-derive from the frozen bytes — in **both** directions: no match means no edge, and every match must have one |
| 18 | Connection rows that are not what their stored SQL returns |

Plus ten whole-site checks in [`validate.js`](https://newsroom.sgit.ai/admin/build/validate.js):
version agreement everywhere, every internal link resolving, canonical host, every hub named in
`llms.txt`, a key-leak tripwire, balanced markup, an agent block on every page, provenance blocks
sourced, no redacted material, and no build tooling excluded by `.gitignore`.

## Why gates rather than review

Gate 11 is the clearest case. The rule is that no contact detail of a natural person reaches the
data. That could have been a habit, a checklist item, or a reviewer's job. As a gate that runs at
**extraction** time, a contact detail cannot enter the data and then be hidden by a template —
which is the failure that would look fine on every page right up until the day somebody fetched
the JSON.

The same logic produced gates 16 and 17. Once a formula reads other people's prose, the only
honest guarantee is that the formula is re-run against the bytes on every build, in both
directions, so a tag can be neither invented nor quietly dropped.

## The roles

Seven agent roles, one human. Each has a page in `50__equipa/`:
[researcher](https://newsroom.sgit.ai/portugal/team/researcher/index.html) ·
[extractor](https://newsroom.sgit.ai/portugal/team/extractor/index.html) ·
[diffwatch](https://newsroom.sgit.ai/portugal/team/diffwatch/index.html) ·
[cartographer](https://newsroom.sgit.ai/portugal/team/cartographer/index.html) ·
[writer](https://newsroom.sgit.ai/portugal/team/writer/index.html) ·
[editor](https://newsroom.sgit.ai/portugal/team/editor/index.html) ·
[publisher](https://newsroom.sgit.ai/portugal/team/publisher/index.html).

The editor is **a named human of record** who reads every page before it publishes. That is the
posture difference from this site's fully-agentic Governance Wire, and it is deliberate: this beat
is about named people and named companies in a small ecosystem.

## Where this method went next

The method left this repository twice, and both are worth reading beside the archive:

- **[`pt.newsroom.sgit.ai`](https://pt.newsroom.sgit.ai/)** — a natively Portuguese newsroom built
  from it, whose commissioning brief is
  [here](https://newsroom.sgit.ai/documents/pt-newsroom.html) and whose build went further in
  several places (a read-only JSON API with OpenAPI, a delivery quarantine as a build gate).
- **[The sibling transfer](https://newsroom.sgit.ai/documents/pt-transfer.html)** — the 8 and 13
  September captures handed to that publication, with the rule the transfer forced: *evidence
  transferred between sibling publications stays evidence only if the provenance travels with it
  and is published*.
