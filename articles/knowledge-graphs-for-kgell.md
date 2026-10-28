# Knowledge graphs in the era of LLMs: what the KGELL COST Action is doing, and what 309 graphs built by agents in a working newsroom can bring to its working group on construction, sgit.ai

> I am a member of working group 3 of KGELL, the European COST Action on knowledge graphs in the era of large language models, and I have not contributed yet. This is my first contribution. KGELL runs from October 2025 to October 2029 with one aim, a pipeline that uses LLMs to build and refine knowledge graphs while reducing hallucinations; in its first year it held its first management meeting in Warsaw, published a catalogue of 88 benchmarks, and held its first technical meeting in Málaga. Working group 3 is about building graphs with LLMs, and its stated aim includes "an open library of methods and resources". This site has been building exactly that for two months: 309 knowledge graphs, one per article, written by an LLM agent, 3,487 typed nodes and 3,386 typed edges, each quote checked word for word against its source. I have put them, the method and an RDF export in a public vault for the group, with what the checks catch, what they miss, and five things we offer to do.

*Source: <https://newsroom.sgit.ai/articles/knowledge-graphs-for-kgell.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Knowledge graphs in the era of LLMs: what the KGELL COST Action is doing, and what 309 graphs built by agents in a working newsroom can bring to its working group on construction

# Knowledge graphs in the era of LLMs: what the KGELL COST Action is doing, and what 309 graphs built by agents in a working newsroom can bring to its working group on construction

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.0.0](versions/knowledge-graphs-for-kgell.md) · [newsroom v0.13.121](https://newsroom.sgit.ai/admin/versions.html) · knowledge-graphsllmkgellcost-actionresearchsemantic-graphsvaultsarticle

***Abstract:** I am a member of working group 3 of KGELL, the European COST Action on knowledge graphs in the era of large language models, and I have not contributed yet. This is my first contribution. KGELL runs from October 2025 to October 2029 with one aim, a pipeline that uses LLMs to build and refine knowledge graphs while reducing hallucinations; in its first year it held its first management meeting in Warsaw, published a catalogue of 88 benchmarks, and held its first technical meeting in Málaga. Working group 3 is about building graphs with LLMs, and its stated aim includes "an open library of methods and resources". This site has been building exactly that for two months: 309 knowledge graphs, one per article, written by an LLM agent, 3,487 typed nodes and 3,386 typed edges, each quote checked word for word against its source. I have put them, the method and an RDF export in a public vault for the group, with what the checks catch, what they miss, and five things we offer to do.*

KGELL, COST Action CA24121: four years, six working groups, and what its first year produced.

## In short

- **KGELL is a European research network** (COST Action CA24121) on knowledge graphs and LLMs, running from October 2025 to October 2029.
- **Its aim:** a pipeline that uses LLMs to build and refine knowledge graphs, "reducing hallucinations and increasing factual accuracy".
- **Year one:** a management meeting in Warsaw, a catalogue of 88 LLM benchmarks, and a technical meeting in Málaga.
- **Working group 3 is about building graphs with LLMs,** including "an open library of methods and resources".
- **This newsroom has built 309 such graphs,** one per article, by an LLM agent, with every quote checked against its source.
- **They are now in a public vault for the group:** JSON, RDF with SPARQL, the method, and what the checks miss.
- **Five offers:** a case study, the dataset, a faithfulness experiment, linking to Wikidata, and vaults as infrastructure.

## What KGELL is

[KGELL](https://kgell-cost.eu/) is COST Action CA24121, *Knowledge Graphs in the Era of Large Language Models*, funded by COST, the European Cooperation in Science and Technology. Its [COST page](https://www.cost.eu/actions/CA24121/) gives a start date of 23 October 2025 and an end of 22 October 2029. The chair is Prof Diego Reforgiato Recupero, of the University of Cagliari, and the vice-chair Prof Michael Cochez, of the Vrije Universiteit Amsterdam.

The problem it states is the one everyone working with LLMs knows: models trained on general data do worse in specialist domains and in languages with fewer resources, reflect the biases of their training data, and "sometimes produce inaccurate or made-up information", which the field calls hallucinations. Its answer is to put the two technologies together, because knowledge graphs "can provide factual information and the ability to perform reasoning", and LLMs can help build and refresh the graphs. The main objective, from its [about page](https://kgell-cost.eu/about/), is "to develop and evaluate an automated pipeline that uses LLMs to generate and refine Knowledge Graph content from domain-specific textual datasets", focused on "reducing hallucinations and increasing factual accuracy".

The work is split into [six working groups](https://kgell-cost.eu/research/working-groups/): augmenting LLMs with knowledge graphs; tasks in specific domains; graph construction assisted by LLMs; many languages; bias and ethics; and evaluation.

## What it has done in its first year

- **20 April 2026: the first management committee meeting,** in Warsaw, hosted by NASK.
- **July 2026: the first deliverable.** D1.1, from working group 1, is "Benchmarking Large Language Model Quality, Reliability, and Trustworthiness: A Review and Catalogue": [88 benchmarks](https://kgell-cost.eu/resources/deliverables/), each tagged with eight features, from hallucination and factfulness to the quality of structured output. It calls itself "an exploratory, community-driven collection rather than a systematic literature review".
- **24 and 25 September 2026: the first technical meeting,** in [Málaga](https://kgell-cost.eu/1st-kgell-technical-meeting/), with status updates from every working group, parallel working sessions and a report from each. The keynote closest to graph construction, by Mélida López of Kanzo Tech, compared LLM-based and semantic NLP approaches to building a graph from text, and ended on "the criteria required to evaluate LLM-assisted knowledge graph construction".
- **A speaker series.** The next talk, on 24 November 2026, is Claire Gardent of CNRS and LORIA on "Verbalising Knowledge Graphs into Multiple Languages"; the [series](https://kgell-cost.eu/events/speaker-series/) runs into July 2027.

## Working group 3: building graphs with LLMs

Working group 3, "KG Construction assisted by LLMs", is led by Dr Ana-Maria Ghiran, with Prof Robert Buchmann as vice-leader, both of Babeș-Bolyai University. Its aim is "to analyze and develop new methodologies for generating KGs, focusing on semi-automated information extraction methods and creating an open library of methods and resources". Its tasks:

- best practices for ontology engineering and reuse of schemas;
- using LLMs to extract entities and relations;
- publishing, storing and querying graphs;
- linking new graphs to public ones such as Wikidata and DBpedia.

The Action's plan (its [Memorandum of Understanding](https://e-services.cost.eu/files/domain_files/CA/Action_CA24121/mou/CA24121-e.pdf)) gives it three chapters: guidelines and best practices for generating graphs, the role of LLMs in generating them, and the tools and resources for generating, refining and linking them.

## Where my work fits

I joined working group 3 and have not contributed yet. Reading its aims, the overlap is direct, because the graph work on this site is graph construction with LLMs, in production.

- **Fractal semantic graphs.** The idea I [introduced](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html) is that each domain keeps its own vocabulary, and the domains connect through named edges, at every altitude. That is schema reuse without forcing one ontology on everything, which is working group 3's first task. It is also, by a wide margin, the most-linked article in this site's graphs: 39 other articles point to it.
- **Knowledge that maintains itself.** The [aim of all of it](https://newsroom.sgit.ai/articles/knowledge-that-maintains-itself.html) is knowledge management: an organisation's policies and information as a graph that agents keep current and brief people from.
- **A graph per article, built by an agent.** Every article here has a semantic graph beside it, written by the same LLM agent that writes the article, and checked before it is saved.
Working group 3's four tasks, and what the newsroom's graphs and vault bring to each.

## 309 graphs, and what the checks catch

On 28 October 2026 the site has 309 graphs: 3,487 nodes of six kinds (claims, methods, examples, concepts, artefacts and questions), 3,386 edges of eight relations (leads to, depends on, produces, extends, example of, answers, contrasts, compared with), 774 quotes, and six topics. A graph has 7 to 18 nodes, typically 11. You can see them all at [the graphs page](https://newsroom.sgit.ai/articles/graphs.html).

The method is simple, and that is the point: a small vocabulary an LLM applies consistently, and checks at write time. The writer refuses a graph whose node kinds, relations or topics are not in the vocabulary, a link to an article that does not exist, or a quote that is not word for word in the article. In the terms of KGELL's own D1.1, that is **ontology conformance** and a **hallucination check on the quotes**. What the checks do not do is the interesting part for working group 3: they do not test whether each node's label and summary is faithful to the article, whether each edge is the right relation, or whether the graph covers the article's main ideas. That is a faithfulness test per triple, and here the source is always one link away.

## The vault

I have put all of it in a public [sgit vault](https://sgit.ai), encrypted, versioned, and readable by anyone with its public read key, which is published on this site. It holds:

- the 309 graphs as JSON, and the site's index of them;
- all of them as RDF in Turtle, 21,840 triples, each node a fragment of its article's address, with the vocabulary as RDFS;
- `METHOD.md`: how the graphs are written and checked, and what the checks miss;
- `WG3.md`: how it maps to the group's tasks and chapters, and the offers below;
- `stats.json`, and a SPARQL example that runs as written.
The KGELL WG3 vault: 309 graphs as JSON and RDF, the vocabulary, the method and the offers.

Open it in the [vault browser](https://dev.vault.sgraph.ai/#sgit_public_read_fa820a5b828288c4b1f32369fa16eaded3bf18a47c8a87ae05139205ad488927%3Ax7hcpg5l), or clone it with `pip install sgit-ai` and `sgit clone sgit_public_read_fa820a5b828288c4b1f32369fa16eaded3bf18a47c8a87ae05139205ad488927:x7hcpg5l kgell-wg3`. The same graphs are on the site's [graphs page](https://newsroom.sgit.ai/articles/graphs.html).

## What we offer

If they are useful to working group 3:

1. **A case study for the chapter on the role of LLMs:** how an agent builds a graph per document in a live publication, what the write-time checks catch, and what they miss.
2. **The dataset for the library of resources,** under CC BY 4.0, refreshed as the site publishes.
3. **A faithfulness experiment:** score each triple against its source article, and compare methods on a set where the source is always there.
4. **Linking to Wikidata:** link node labels, and measure what an LLM gets right.
5. **Vaults as infrastructure for the library:** versioned, signed, readable with a public key, from any static host, which matters for a library that should outlive any one server.

The next step is the conversation with the group, starting with working group 3's leads.

## What this does not claim

- **Everything about KGELL here is from its public pages,** the COST page and its Memorandum of Understanding, read on 27 and 28 October 2026. Nothing speaks for KGELL or its working groups.
- **The graphs are one agent's work, in one style,** and their faithfulness is not measured yet; that is offer 3.
- **No links to Wikidata or DBpedia yet;** node labels are free text.
- **The counts are this site's own,** from its published graphs on 28 October 2026.

## Where this comes from

KGELL's site: [home](https://kgell-cost.eu/), [about](https://kgell-cost.eu/about/), [working groups](https://kgell-cost.eu/research/working-groups/), [deliverables](https://kgell-cost.eu/resources/deliverables/), [the Málaga meeting](https://kgell-cost.eu/1st-kgell-technical-meeting/) and [the speaker series](https://kgell-cost.eu/events/speaker-series/); [the COST page for CA24121](https://www.cost.eu/actions/CA24121/) and its [Memorandum of Understanding](https://e-services.cost.eu/files/domain_files/CA/Action_CA24121/mou/CA24121-e.pdf); D1.1, read in full. This site's graphs, counted from `articles/graphs/` on 28 October 2026. Related: [introducing fractal semantic graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html), [knowledge that maintains itself](https://newsroom.sgit.ai/articles/knowledge-that-maintains-itself.html), [search as navigation](https://newsroom.sgit.ai/articles/search-as-navigation.html). Written up by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Graphs & knowledgeNews & evidence[This article as a graph →](graphs.md#knowledge-graphs-for-kgell)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 310 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=310)

**Posting this article on LinkedIn?** The cover is [knowledge-graphs-for-kgell.jpg](banners/knowledge-graphs-for-kgell.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/knowledge-graphs-for-kgell.html)*
