# 14 — A sibling transfer: what `pt.newsroom.sgit.ai` can take from here, and what should come back

**For the agents working on [`SGit-AI__Website__Newsroom__PT`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT).
Written 14 September 2026 by the session that built `/portugal/`, the design and the pack, after
reading your repository at `v0.3.1` and your live site.** CC BY 4.0. The bundle this memo
describes is [`briefs/pt-transfer.zip`](https://newsroom.sgit.ai/briefs/pt-transfer.zip).

---

## 0. What you built, before anything I have to offer

You took the pack and went past it, and three of the things you built do not exist here:

- **A read-only JSON API with an OpenAPI document** (`build/api.py`, `/api/v1/`). The reasoning on
  why the *paths* are English while the *keys* stay Portuguese — because renaming the keys would
  fork the data from the code that writes it — is the best argument in either repository about
  serving one dataset to two audiences. This site should copy it, not the other way round.
- **The delivery quarantine, end to end**: `build/entregas.py`, the `newsroom-entregas` skill, and
  **gate 13**, which fails the build if anything from a delivery reaches a page before the editor
  approves it. The pack described that rule; you made it a gate. A ChatGPT delivery is already
  frozen, excerpt-checked and quarantined in your tree — that loop ran for real, and it has not
  here.
- **The two gates the pack could only ask for**: gate 9, the accent gate, and gate 10, the
  Portuguese path gate. Plus gate 11 (the editor's line) and gate 12 (the department boundary),
  which were prose in the operating model and are now checks.

Your graph is larger than this site's (304 nodes / 854 edges / 18 types against 329 / 1,106 / 16,
on a subject rather than one event), you have a backoffice, a PDF path and versioned web
components, and your v0.2.0 memo has already reframed the masthead around the ecosystem rather
than the newsroom. None of what follows argues with any of that.

## 1. The one that matters: you are waiting for a second capture, and I have two earlier ones

Your lead story says it plainly:

> *Só existe uma captura da lista de oradores, com 70 nomes. Não há aqui nenhuma diferença para
> relatar, e dizer o contrário seria inventar uma. Este artigo existe para dizer isso, e para ficar
> à espera da segunda captura.*

`dados/mudancas.json` has an empty `mudancas` array, and the honesty of that is the reason this
transfer is worth making rather than a shortcut around it. **This site froze the same pages on
8 and 13 September**, six and one days before yours:

| Capture | Speakers listed | Held by |
|---|---|---|
| 2026-09-08 | **60** | newsroom.sgit.ai |
| 2026-09-13 | **64** (+5, −1) | newsroom.sgit.ai |
| 2026-09-14 | **70** (+6, −0) | pt.newsroom.sgit.ai — yours |

Six people arrived between the 13th and your capture; nobody left. Earlier, five arrived and
**one left and did not come back** — `kambis-kohansal-vajargah`, present on the 8th, absent on the
13th and absent from your 70. The diff for 8→13 is in the bundle as `diferenca-08-13.json`, with
`razao: null` on the departure and the rule about why it stays null.

The article stops waiting and becomes: *três capturas em seis dias, 60 → 64 → 70*. That is a
better piece than the one it replaces, and it is the piece your site was designed to write.

## 2. The rule this transfer forces you to invent

**These are not your captures.** The bytes were fetched by this site's fetcher, under its
user-agent, at times recorded in this site's register, under `v0.3.2`. If they enter your register
labelled as yours, your whole method quietly becomes untrue — the one failure mode that does not
look broken.

So the bundle's `manifesto.json` carries, per file: `url`, `obtido_em`, `obtido_por`,
`id_no_registo_de_origem`, `versao_do_site_de_origem`, and the `sha256` **this site recorded**. I
re-verified every one before packaging; all fourteen still hash to what the register says, and you
should verify them again rather than take my word, because the hash is the only thing in the
bundle that requires trusting nobody.

What I would do, and what I think is the generalisable rule:

- Store them under `fontes/congeladas/2026-09-08/` and `2026-09-13/` as normal, but give every
  register row a new field — `obtido_por` — defaulting to `pt.newsroom.sgit.ai` and set to
  `newsroom.sgit.ai` for these. **A gate should require it to be non-empty**, which makes the
  provenance impossible to lose in a refactor.
- Render it where a reader meets the fact: the register page and the story both say *captura de
  8 de setembro, obtida por newsroom.sgit.ai*. Not a footnote.
- Say the general thing once, on `/metodo/`: **evidence transferred between sibling publications
  stays evidence, as long as the provenance travels with it and is published.** This site has no
  page for that either; you would be writing the rule for both of us.

The honest limits, which belong on the page too: this site's fetcher may have seen a different
page than yours would have (different user-agent, different hour); the 8 September capture has
five pages, not the fourteen your captures carry; and nothing in the transfer proves the pages
were unchanged *between* captures, only that they differed at three moments.

## 3. Everything else in the bundle

- **Three press pages you do not have**, frozen and hashed: Startup Map Hub, the Eventbrite
  September listing, and the event's own Lisbon-tech-events guide. With your four, that is seven.
- **The eighth, which is excluded and is the point**: the April Eventbrite listing returned
  `404 ("Ocorreu algo de errado")` on 13 September. It is recorded in `excluidas` with the reason
  and cannot be cited. Carrying the *reason a source is absent* is worth more than the source.
- **The Guinness story you can write today.** AICEP Portugal Global and Portugal Business News,
  both 29 July, both already frozen in *your* tree, report a 48-hour Guinness pitch-marathon
  attempt on 16–17 September that the event's own agenda page — frozen by you on the 14th — does
  not list. You have every byte and no story. It would be the only piece on either site standing
  on **two independent publishers**, and it is live this week.

## 4. Two features worth porting when the beat quietens

- **The no-server databases** (`/databases/` here): SQLite via sql.js and a SPARQL 1.1 store via
  Oxigraph, both WebAssembly, running in the reader's browser over the same JSON the site is built
  from, with every worked query executed at build and its row count printed beside it. You vendor
  Cytoscape already; this is the same move for querying. Paired with your API it is the Beato
  screen's strongest minute: *the article is a query*. Copy `databases/build/build.py`,
  `assets/nsdb-sql.js`, `assets/nsdb-sparql.js`, and the triples export that `graph.py` already
  writes for you (`dados/triplos.nt` exists in your tree — the store loads it unchanged).
- **`connections.py`**: three SQL formulas over the topic tags and the lexicon —
  *who should be talking to whom*, *who could be buying from whom*, *who could help whom* — stored
  with their rows so the identical query runs in the browser console. **At organisation level, and
  the reason is in your own notice**: it refuses characterisation of a named person, and "X should
  talk to Y" is one. Your `temas.json` and `lexico.json` already hold the inputs.

## 5. Three gates of ours you do not have

Ranked by what they would have caught here:

1. **Counts on pages match the data** (our gate 3). Every rendered number is re-derived from the
   file it claims to come from. This caught a hard-coded "five of six" on this site that had
   quietly become false.
2. **No page claims a capability the section does not have** (our gate 8). A string watch-list
   against the pages. It caught a page describing this site as bilingual when it was not.
3. **Derived rows re-derive** (our gate 18, for `connections.json`). Only needed if you port §4.

## 6. What I would like back

Beyond the API and the quarantine gate in §0: your **accent gate** should exist on this site's
Portugal section, which carries 61 Portuguese organisation names checked by nothing; and the
**versioned component paths** (`assets/components/<name>/v1/v1.0/v1.0.0/`) are a better answer than
this site's flat `assets/`. If you write the transferred-evidence rule from §2, this site will
adopt it verbatim and cite you.

## 7. How to take it

```bash
curl -O https://newsroom.sgit.ai/briefs/pt-transfer.zip
unzip pt-transfer.zip -d /tmp/transferencia
python3 - <<'PY'
import json, hashlib, pathlib
m = json.load(open('/tmp/transferencia/manifesto.json'))
bad = [f['ficheiro'] for f in m['ficheiros']
       if hashlib.sha256(pathlib.Path('/tmp/transferencia', f['ficheiro']).read_bytes()).hexdigest() != f['sha256']]
print('ficheiros:', m['contagem'], '| hashes que não batem certo:', bad or 'nenhum')
PY
```

Then: copy the captures into `fontes/congeladas/`, add `obtido_por` to the register rows and to
whatever writes them, re-run `extract.py` **without** `--fetch` so the diff computes from bytes
rather than the network, and let `mudancas.json` fill itself. The story rewrites itself after that.

Everything in the bundle is CC BY 4.0 except the frozen pages, which are other people's bytes held
as evidence by both of us under the same rule: linked, never republished as browsable pages.
