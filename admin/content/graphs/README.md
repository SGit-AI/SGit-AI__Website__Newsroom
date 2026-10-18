# The graph of meaning: the standing brief

The brief for whoever runs the next pass over the newsroom's articles, a person or an agent. It was written on
18 October 2026 for the first run and is kept current by each run after it. The article that set the expectations
is [The graph of meaning: a brief](../../../articles/the-graph-of-meaning-a-brief.md); what the first run found is
[The graph of meaning, drawn](../../../articles/the-graph-of-meaning-drawn.md). `admin/build/fsg.py` checks every
file here and derives the layers; its docstring is the short form of this page.

## What this is for

Every article already has a graph beside it, `admin/content/articles/graphs/<slug>.json`: ten to fifteen nodes, the
argument's shape, two quotes. Those graphs are maps of one argument each, and they barely touch: of 2,286 node labels
across 187 articles, 48 appear in more than one article. The vocabulary is loose too: 401 of 672 tags are used once.
The site says meaning is connectivity, and its own graphs are islands.

This brief adds a second reading of every article, from the bottom up, that is made to connect. Each article is read
as the things in it that can be checked, named and joined: its **facts**, **data points**, **hypotheses**,
**proposals**, **questions**, **limits**, **definitions** and **decisions**; the **names** it uses (people,
organisations, products, models, standards, laws, places, events, sites, publications, repositories, vaults,
roles); the **concepts** of the newsroom's own vocabulary it uses or defines; the outside **sources** it cites, dated;
and the **dates** it turns on. Every claim is anchored to the section it comes from and to a quote, word for word, so a
script can check the anchor and a reader can find the sentence.

Because names and concepts carry one id across the whole newsroom, the files join. From the join the build derives the
layers above: which concepts and names have gravity (two or more articles, the wire's rule); how concepts cluster
when the articles that share them are counted; which clusters hold together as one vocabulary and which split; where
the peaks are, the natural places of arrival (a company, a standard, an idea, an area); and how the shape compares with
the layers the editor drew by hand (six topics, five desks, eleven series, the sections, the personas).

## The grammar, which never changes

The grammar is [graphs.sgit.ai](https://graphs.sgit.ai/v1/grammar/index.html)'s, and every layer keeps it while
choosing its own types and verbs:

1. **Every edge is a verb with a named inverse.** `backs` and `backed_by`; `gives_rise_to` and `arises_from`.
   A path must read as a sentence from either end.
2. **The generic association edge is banned.** No `relates_to`. Two things always relate; an edge with no verb
   constrains nothing. The validator refuses it.
3. **Properties carry data, never meaning.** A claim's `kind` and a name's `type` are the only typed words; what a
   thing *is* comes from what it is connected to.
4. **Supersede, never delete.** A correction is a new claim with a `supersedes` edge to the old one; an id, once
   published, stays, as an alias if it is merged.
5. **Render the answer to a question, never the whole graph.** Every page the build writes answers one question
   (which names have gravity; what this article states; what a concept rests on).

A layer is a new **dimension** when it needs its own types and verbs. The claims of one article are one dimension
(types: the eight claim kinds; verbs: the seven below). The names across the newsroom are another (types: the
thirteen entity types; verbs: `names`, `named_in`, and whatever a later run finds between names). A layer whose
types and verbs are the layer below's is not a new dimension, it is the same one at less resolution, and the build
says so rather than inventing a level. The same rule, in graphs.sgit.ai's words: same types and verbs all the way
down is a hierarchy, not a fractal.

## The file, one per article

`admin/content/graphs/articles/<slug>.json`, written from the article's markdown twin `articles/<slug>.md` and its
page `articles/<slug>.html` (for the section anchors: `python3 admin/build/fsg.py --sections <slug>` prints them).

```json
{
  "slug": "<slug>",
  "by": "newsroom.cartographer",
  "run": "YYYY-MM-DD",
  "claims": [
    {"id": "c01", "kind": "data-point",
     "text": "551 of the 566 links between articles point to an earlier article.",
     "section": "counts",
     "quote": "551 of 566 point to an earlier article",
     "about": ["concept:corrections-propagate", "entity:newsroom-sgit-ai"],
     "value": {"n": 551, "of": 566, "unit": "links", "as_of": "2026-10-13"},
     "refs": []}
  ],
  "edges": [{"from": "c01", "verb": "backs", "to": "c02"}],
  "entities": [{"id": "newsroom-sgit-ai", "role": "the site whose links were counted"},
               {"id": "some-new-name", "new": true, "name": "Some New Name", "type": "organisation", "role": "..."}],
  "concepts": [{"id": "corrections-propagate", "defined_here": false},
               {"id": "a-new-idea", "new": true, "label": "A new idea", "means": "<one line>", "defined_here": true}],
  "references": [{"id": "r01", "url": "https://...", "title": "...", "by": "...", "date": "2026-10-13", "kind": "post"}],
  "dates": [{"date": "2026-10-13", "what": "Four articles written in a row, each linking only to the one before"}]
}
```

**Claims.** Twelve to thirty-five per article (the file must have 8 to 45). Kinds: `fact` (something the article
states as so, checkable), `data-point` (a number, with `value`), `hypothesis` (the owner's "I think", "my hypothesis"),
`proposal` (something to build or do), `question` (left open), `limit` (from What this does not claim, and anywhere
else the article bounds itself), `definition` (the article defines a term), `decision` (the owner or the newsroom
decided or did something). `text` is the claim in plain words, one sentence, under 45 words, in the article's own
terms. `section` is the page's h2 anchor, or `top` for the opening. `quote` is 5 to 40 words copied from the article,
word for word: the validator looks for it in the twin and fails the file if it is not there. `about` lists the
concepts and entities the claim is about, each as `concept:<id>` or `entity:<id>`, and each listed in the file.
`refs` names the references the claim rests on. A data point's `value` has `n` (a number), and when the article gives
them `of`, `unit` and `as_of`.

**Edges** are between claims of the same article, and only where the article makes the connection: `backs` (a data
point or fact backs a claim), `gives_rise_to` (a fact gives rise to a hypothesis, proposal or question), `answers`
(a claim answers a question), `limits` (a limit bounds a claim), `contradicts`, `supersedes` (a later claim replaces
an earlier one), `specifies` (a part specifies a proposal). Five to fifteen is usual. Every other edge (article states
claim, claim names entity, claim uses concept, claim cites reference, article defines concept, article builds on
article, claim happened on date) is derived by the build from the fields, with its inverse.

**Entities and concepts** are ids from the registries, `registry/entities.json` and `registry/concepts.json`
(`python3 admin/build/fsg.py --registry` prints both). An id not in the registry is added to the file with
`new: true` and, for an entity, its `name` and `type`; for a concept, its `label` and a one-line `means`. The next
run folds new ids into the registries and merges duplicates, keeping the old id as an alias, so write the id you would
expect to find (`anthropic`, not `anthropic-pbc`) and check the registry first. A private person named nowhere in the
article is not an entity. Our own products are entities, never concepts. A concept is an idea the newsroom argues
with; an entity is a thing in the world with a name.

**References** are the outside sources the article cites, with the date it gives; `undated` when it gives none.
Articles on this site are not references, they are `builds_on` edges the build derives from the links in the text.

**Dates** are the dates the article turns on, with what happened, YYYY-MM-DD where the article gives the day.

## The rules of the file

- Word for word. A quote is copied, with its punctuation; the validator normalises only quote marks and spaces. It
  compares against the twin with its markdown marks stripped, so a quote carries no backticks, asterisks or hash signs
  (`#4239` reads as `4239`): quote the words, not the marks.
- The section anchor is the page's. Some imported pages carry h2 headings without ids; a claim from such a page sits on
  `top`, and the build says how many pages that is. Do not invent an anchor.
- Nothing the article does not say. A claim is the article's, in its words; the Cartographer adds no claim of its own.
- Plain words, British spelling, no em-dash, and the ladder word (a step of a ladder) is banned here as everywhere:
  say layer, level, altitude or tier. The validator refuses both.
- A number is a data point, with its `value`, so it can be drawn and checked.
- The limits are claims too: every article has a What this does not claim section, and each bullet of it is a `limit`.
- Count what you can: the `data-point` kind is for numbers the article gives; the build counts the rest.

## The run

1. `python3 admin/build/fsg.py --sections <slug>` for the anchors; read `articles/<slug>.md` in full.
2. Write `admin/content/graphs/articles/<slug>.json`; `python3 admin/build/fsg.py --check <slug>` until it passes.
3. When every article has a file: `python3 admin/build/fsg.py --report` for the emergence report (the counts, the
   shared nodes, the gravity, the clusters against the editor's layers), then `python3 admin/build/fsg.py` to fold the
   new ids into the registries, derive the layers and write `graphs/` (the hub, one page per dimension, the peaks, the
   maps, one facts page per article, and a JSON twin for each).
4. In the release process, `fsg.py` runs after `sections.py` and before `chrome.py`.
5. Each run writes its article: what the expectations were, what came of them, counted. The expectations for the next
   run go at the end of it, and into this file.

## What a run should expect to find, and say when it does not

The first run's predictions are in its brief article, numbered, so the next run can score them. A run that finds the
same clusters as the last one has found a stable layer; a run that finds different ones should say which articles
moved them. A cluster that matches a desk or a topic the editor drew is a confirmation of the editor's layer, not a
discovery; a cluster that cuts across them is the finding. A concept with gravity in the claims but no controlled
subject in `articles/find.json` is a candidate for the Librarian. A name with gravity and no page is a candidate peak.
