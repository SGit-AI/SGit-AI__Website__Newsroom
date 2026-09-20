# The Startup Summit beat: a consolidated archive

**For the agent consolidating everything this publication did on Startup Summit Lisbon 2026.**
Cut 20 September 2026 from `newsroom.sgit.ai` v0.3.12. **160 files**, every one also live on the
public web and in a public repository — nothing here requires a credential, and nothing here is
the only copy. CC BY 4.0, except the frozen third-party pages, which are evidence (see §7).

| Where | What |
|---|---|
| **Live section** | https://newsroom.sgit.ai/portugal/index.html |
| **Repository** | https://github.com/SGit-AI/SGit-AI__Website__Newsroom (branch `dev`) |
| **This archive** | https://newsroom.sgit.ai/briefs/summit-archive.zip · unpacked under [`/briefs/summit-archive/`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/tree/dev/briefs/summit-archive) |
| **Agent index** | https://newsroom.sgit.ai/llms.txt · whole corpus in one fetch: https://newsroom.sgit.ai/llms-full.txt |

## Read in this order

| # | File | Why |
|---|---|---|
| 1 | this file | What the beat was, what was built, what is true and what is not |
| 2 | [`01__inventario.md`](01__inventario.md) | Every file with its live URL, its GitHub URL and what it is. JSON twin carries the hashes |
| 3 | [`02__o-que-aconteceu.md`](02__o-que-aconteceu.md) | The chronology: six days, two captures, three stories, and what each one cost |
| 4 | [`03__os-numeros.md`](03__os-numeros.md) | Every published number and the file it is derived from. Nothing here was typed twice |
| 5 | [`04__o-metodo.md`](04__o-metodo.md) | fetch → freeze → hash → extract → diff, the eighteen gates, and the four rules that survived contact |

Then the files themselves, in the numbered folders: `10__paginas`, `50__equipa`, `20__dados`,
`30__codigo`, `40__conteudo`, `70__documentos`, `60__fontes-congeladas`.

## 1. What the beat was

**Startup Summit Lisbon 2026** — 17–18 September 2026, Unicorn Factory Lisboa, Beato Innovation
District, Lisbon. This publication covered it from **8 September** (nine days before the doors)
to **13 September**, as the first beat of `/portugal/`, a section whose purpose was to prove a
method rather than to cover an event: *every claim walks back to bytes this publication holds*.

It was never a preview, a listing or a promotional page. The three stories it produced are all of
the same kind — **the record, not the verdict** — and two of the three are about the source
material disagreeing with itself.

## 2. What was built

- **The section**: 14 pages plus 3 stories plus 7 role pages, at `/portugal/`.
- **The evidence**: 88 frozen files across 2 dated captures, every one hashed, the hashes
  re-verified on every build. 89 files are in this archive: the 88 in the register plus one text
  file the register treats separately.
- **The graph**: 329 nodes, 1,106 edges, 16 node types, 19 verbs — each verb with a distinct named
  inverse *and* a Portuguese form, so a path reads as a sentence in either language. Also exported
  as 4,001 N-Triples with the ontology inside it.
- **The derivation layer**: the event's own topic tags for each speaker (23 distinct, read
  verbatim), plus 417 tag edges derived by a **published lexicon** of 57 patterns — each edge
  carrying the words that matched, so a tag says *this page contains these words* and nothing more.
- **The analysis**: three organisation-level queries — who should be talking, who could be buying
  from whom, who could help whom — 90 rows, stored with the SQL that produced them.
- **The consoles**: SQLite and a SPARQL 1.1 store, both WebAssembly, running in the reader's
  browser over the same JSON files, with 29 worked queries executed at build.
- **The gates**: 18 section gates plus 10 whole-site checks. A red gate is not a warning.

## 3. The three stories

Each is in the archive as rendered HTML (`10__paginas`), as prose (`40__conteudo`), and as a row
in [`stories.json`](https://newsroom.sgit.ai/portugal/data/stories.json) naming the frozen sources
it stands on.

1. **[Two names for three stages](https://newsroom.sgit.ai/portugal/stories/two-names-for-three-stages.html)**
   — the agenda calls them the Unicorn Stage and the Impact Stage; the AI-summary page on the same
   site, the same day, calls them the Main Stage and the Startup Stage. Both frozen. Neither
   corrected by us.
2. **[Five names arrived and one left](https://newsroom.sgit.ai/portugal/stories/five-names-arrived-and-one-left.html)**
   — the published speaker list went from 60 to 64 between the two captures. Both copies held,
   both hashed. **The departure carries no reason, and none may be inferred.**
3. **[A record attempt the agenda does not mention](https://newsroom.sgit.ai/portugal/stories/a-record-attempt-the-agenda-does-not-mention.html)**
   — two Portuguese outlets, both 29 July, report a 48-hour Guinness pitch marathon running
   alongside the summit on 16–17 September. The event's own agenda page, four days out, does not
   list it. Both frozen; neither wrong yet. It is the only story here standing on **two
   independent publishers**.

## 4. What is true, stated precisely

- The counts are of a **published list at a moment**, not of the event. 64 speakers were listed on
  13 September; the event's own pages state a *target* of "150+ speakers planned" and "2,000+"
  attendees. A target is never reported here as a result, and a gate enforces that.
- The 61 organisations are **derived from the speaker cards**, not from a registry. Two are
  placeholders (`Independent`) and are flagged rather than removed.
- No speaker is joined to a session, because **the source joins none**.
- No speaker card carries a country, so the event's "40+ countries" claim is recorded as
  **unverifiable from the source** — not as doubted.
- The `role_class` on a person and every derived tag are **formulas over the listed title or the
  page's own words**, published in full, re-run against the frozen bytes on every build.

## 5. What is not true, and was never claimed

- This is not a complete picture of the Portuguese startup ecosystem. It is one event, from two
  kinds of source — the event's own pages and press pages *about* the event — and **neither is a
  registry or a funding dataset**.
- No biography was reproduced. No contact detail of any natural person exists in any data file;
  it is refused at extraction, not hidden at rendering.
- No assessment, ranking or characterisation of any named person appears anywhere. The connections
  page works at **organisation** level for exactly this reason.
- There was no legal review. The data-protection notice is a posture, not advice.

## 6. If you only take four things

1. **[`extract.py`](https://newsroom.sgit.ai/portugal/build/extract.py)** — the ingestion path. Everything else is downstream of it.
2. **[`gates.py`](https://newsroom.sgit.ai/portugal/build/gates.py)** — eighteen checks that fail the build. The section's conscience, in code.
3. **[`notice.json`](https://newsroom.sgit.ai/portugal/data/notice.json)** — the posture as data: what is held, what is refused, and the unconditional removal.
4. **[`sources.json`](https://newsroom.sgit.ai/portugal/data/sources.json)** — the register. Without it, every page above is a drawing.

## 7. Provenance, licence, and the one thing you may not do

Everything in `60__fontes-congeladas/` is **other organisations' bytes**, held as evidence under
the rule this whole section exists to demonstrate: *link, never republish as browsable pages*.
They carry the `.snapshot` extension so no server serves them as HTML. Keep that rule if you keep
the files. Everything else — the pages, the data, the code, the prose, the briefs — is this
publication's own work under CC BY 4.0 (code under Apache 2.0; see
[`LICENSES.md`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/LICENSES.md)).

Verify any file in this archive against the live site:

```bash
python3 - <<'PY'
import json, hashlib, pathlib, urllib.request
inv = json.load(open('01__inventario.json'))
bad = []
for f in inv['files']:
    local = hashlib.sha256(pathlib.Path(f['archive_path']).read_bytes()).hexdigest()
    if local != f['sha256']: bad.append((f['path'], 'archive differs from manifest'))
    elif f.get('live'):
        live = hashlib.sha256(urllib.request.urlopen(f['live']).read()).hexdigest()
        if live != f['sha256']: bad.append((f['path'], 'live differs — the site moved on'))
print(inv['count'], 'files |', bad or 'every file matches its hash, in the archive and on the live site')
PY
```

A difference is not a failure: the site is alive and may have moved past v0.3.12. Expect it,
in fact, in one specific place — **every archived `.html` page carries the version badge and the
navigation of the release it was cut from**, so each one will differ from the live page after the
next release, while the data files, the code and the frozen sources will not. That is the archive
working: the pages here are what a reader saw at v0.3.12, not what one sees today. The manifest
records what was true when this was cut, which is the whole of what an archive can promise.

The same fact bit the build the first time this archive existed: the site's chrome tool restamped
all 27 archived pages with the current version, and the site validator reported 413 broken links
in them — every report correct, and every one about a copy rather than a page. Both tools now skip
`summit-archive/` by name, with the reason written in the code. **If you keep an archive inside a
live repository, exclude it from anything that rewrites or checks pages**, or the archive quietly
becomes a second copy of the present.
