# The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks, sgit.ai

> The wires already collect the day's news into encrypted vaults on a schedule. This is the next step, and the way to design it is to start at the end, with what the reader sees, and work backwards to the data. A story should read as a short narrative in which every name is a link, to a person, a company, an event or a place, each with a long-lived ID, and every sentence is a claim with its evidence: a fact, an observation, a statement by a party, or our analysis. Stories group into stories, and that is the fractal part: a thread is a story made of stories, and an article someone else published is a story too. From there, the primitives: a run that collects, captures that freeze what was read, claims, stories, stories of stories and names, each with a random ID that never changes. I measured the four wires' public vaults today: 202 stories, 1,358 distinct names, only 171 of them in more than one story and 48 in more than one wire, and only 44% of the names a story lists appear in its own text. Those numbers say where the work is, and how big a folder tree it needs: a name gets its own folder when it has gravity. Earlier experiments that linked every word of a long text were the right idea done too much. A wire story's narrative is about 55 words, small enough to link every phrase. Cheaper models can do the heavy lifting and a more capable one can check it. This article is also the brief for the desks and the wire agent.

*Source: <https://newsroom.sgit.ai/articles/the-wire-as-a-graph.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks

# The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/the-wire-as-a-graph.md) · [newsroom v0.12.46](https://newsroom.sgit.ai/admin/versions.html) · wirenewsroomfractal-semantic-graphsontologyidsevidenceprovenancevaultssgitmulti-modelbriefarticle

***Abstract:** The wires already collect the day's news into encrypted vaults on a schedule. This is the next step, and the way to design it is to start at the end, with what the reader sees, and work backwards to the data. A story should read as a short narrative in which every name is a link, to a person, a company, an event or a place, each with a long-lived ID, and every sentence is a claim with its evidence: a fact, an observation, a statement by a party, or our analysis. Stories group into stories, and that is the fractal part: a thread is a story made of stories, and an article someone else published is a story too. From there, the primitives: a run that collects, captures that freeze what was read, claims, stories, stories of stories and names, each with a random ID that never changes. I measured the four wires' public vaults today: 202 stories, 1,358 distinct names, only 171 of them in more than one story and 48 in more than one wire, and only 44% of the names a story lists appear in its own text. Those numbers say where the work is, and how big a folder tree it needs: a name gets its own folder when it has gravity. Earlier experiments that linked every word of a long text were the right idea done too much. A wire story's narrative is about 55 words, small enough to link every phrase. Cheaper models can do the heavy lifting and a more capable one can check it. This article is also the brief for the desks and the wire agent.*

Start from what the reader sees. One story from the Industry Wire, shortened, as it could read: every name in its narrative is a link to something with an ID and a type, and every sentence is a claim with its evidence. The NCSC is named in this story's text but not in its tags, and is tagged in another story; with an ID, the two would join. Below, the three other views the same data gives: the day, the story of stories, and the name.

## In short

- **Start from the end.** Design what the reader sees first, then work back to the data and the schedule that produce it.
- **Every name is a link.** A short narrative per story, with each person, company, event and place linked to something with an ID and a type.
- **Every sentence is a claim.** A fact, an observation, a statement by a party or our analysis, each pointing at its evidence.
- **Stories of stories.** A thread is a story made of stories; another outlet's article is a story too. The same schema at every size.
- **Long-lived, random IDs.** For every run, capture, claim, story and name, minted once and never reused.
- **Measured today.** 202 stories, 1,358 names, 171 in more than one story, 48 in more than one wire, 44% found in the story's own text.
- **Gravity decides the folders.** A name gets its own folder when it appears in two stories or two wires; the rest stay inside their story.
- **The right thing, at the right size.** Link the short narrative, not the whole article.

## Start from the end

The wires work. Four of them, each an encrypted vault that a desk writes on a schedule and this site reads: the Industry Wire, the AWS Wire and the Portugal Wire daily, the OWASP Wire weekly. Each run collects the sources, clusters them into stories, finds the primary source, joins stories to readers, writes the edition and checks it against a gate. The [charter](https://newsroom.sgit.ai/wire/charter.html) already says "Facts first, analysis on top".

The next step is the graph, and I think the way to design it is backwards: start with the user experience, and reverse engineer the data sets, the structure and the runs that produce them.

What the reader should see is a story as a short narrative in which every name is a link. In the figure above, Asos, the NCSC, the Xuanye Group and Snowflake are each something: a company, a government agency, a group claiming an attack, a platform. If you mention a name, what is it? A company, a person, an event, a place? Every one of them should have its own small graph: what it is, the other stories that name it, what each of those said. Under the narrative, every sentence is a claim with its evidence: that names and contact details were affected is a fact from the NCSC's own notice; that the attackers hold the data is a claim by a party, unverified; that it was not a breach of Snowflake's systems is a statement by Snowflake. And from the same data, three more views: the day, as one graph of the stories and the names they share; the story of stories, followed over weeks; and the name, across every wire that mentions it.

## What is there today

The public read-only vaults of the four wires hold one folder per story, a `story.json` and a `story.md`, and I read all of them today: 202 stories. Stories have IDs, short slugs by beat such as `sec-10`, with a pattern in the schema of letters, a hyphen and two or more digits. There is a `superseded_by` field, so one story can already replace another. Threads already group stories. The Portugal project already has an ontology with 16 types, from Event and Person to Place and Story, and verbs that read both ways.

The names are where the work is. Each story lists them as tags, grouped by kind: organisations, people, products, technologies, CVEs, and for some wires events, standards and places. Across the four wires:

- **1,358 distinct names**, median nine per story.
- **171 appear in two or more stories**, and 48 in two or more wires: Anthropic, OpenAI, Microsoft, GitHub and others. Those are the joins between wires.
- **Only 44% of the names a story lists appear in its headline or summary.** The tags describe the story; they do not anchor to its text. In the Asos story, the one person listed does not appear in its text, and the NCSC, whose notice is the primary source, is not listed at all, although it is named in the summary and tagged in another story.
- **The same thing is sometimes two names.** "aws" and "amazon web services" are separate entries; eleven names are filed under two kinds, Snowflake as both an organisation and a product.
- **Some tags are words, not names.** "release" is tagged as a technology 34 times.

None of this is a mistake by the desks; it is what tags are. It is why the next step is IDs.

## The primitives

The primitives, and where each lives. A run collects; captures freeze what was read; claims are typed and point at evidence; a story is a short narrative over claims and names; stories group into stories; a name earns its own folder when it has gravity. Every object has a long-lived random ID, and an index of every ID, alias and slug.

Working back from the reader, these are the objects the data needs.

- **The run.** A collection time: which wire, when, on what schedule, which models, which sources were polled, and what was produced. Daily, weekly or on any schedule; each run is an object with its own ID, not just a date.
- **The capture.** What was read, frozen where the licence allows, with its address and a hash. The charter's tiers already say what may be kept: A frozen and shown, B frozen as evidence, C linked only.
- **The claim.** One of four kinds: a fact, an observation, a statement by a party, or the desk's analysis. Each points at the captures that support it, and analysis is always marked as ours.
- **The story.** A headline and a short narrative in which every name is a span linked to an ID, the claims behind it, and the role each name plays in it: the source, the victim, the claimant.
- **The story of stories.** A thread or a topic is a story whose parts are stories. Stories can be merged, and a larger story can hold smaller ones, so it is the same schema at every size, which is the fractal part. And when another outlet publishes an article, that is a story too, with its own claims: the coverage we collect is made of the same objects as the stories we write.
- **The name.** A person, organisation, event, place, product, technology or standard: one ID, its aliases, and a type from the ontology.

And the days, topics and names are views, not separate data: the graph of a day is every story from that day and the names they share, and it can be drawn from the store at any time. The wire pages already draw graphs from each edition, since [v0.12.42](https://newsroom.sgit.ai/engineering/releases/v0.12.42.html); with IDs, they can join across days and wires.

## Long-lived IDs

Every one of those objects needs an ID that lives as long as the object, and it should be random and strong: a 128-bit identifier minted once when the object is first created, never reused and never derived from its title. A slug like `sec-10` stays as a readable alias, and so does every old ID after a merge, so a link made last month still resolves. When two stories turn out to be one, the smaller is merged into the larger and keeps its ID as an alias; when a story splits, each part records where it came from. The same for names: the NCSC and the UK National Cyber Security Centre are one ID with two aliases.

That is also what lets a graph be cleaned. With IDs you can merge duplicates, fix a type, and see every story that used a name, without editing text. If everything is mapped to IDs, we can always find it.

## Every phrase, at the right size

The idea of linking every word is not new here, and the first attempts taught us something. [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md) parsed a regulation down to the point where, for one atlas, the smallest node "is, literally, the word". Five agents [read one article](one-article-five-readers.md) and catalogued every fact and claim in it, and one catalogue came out at "2.8 times the size of the articles it catalogues", as [The agent is the reader](the-agent-is-the-reader.md) measured. A view that turned every term into a link was [noted as](the-site-is-an-inbox.md) "Not always on, because it is noisy." And this site's own rules for article graphs say: "The graph is a map of the argument, not an index of every noun."

That was the right thing done too much. Linking every word of a long article produces more graph than text. What I am describing is different: the top-level narrative of a story, about 55 words at the median across the four wires, with every name and every claim in it linked. That is small enough to link completely, and it is where a reader looks first. Start small, with the narrative, and expand to the coverage and the captures when the narrative works.

## The folder tree, and gravity

Every object needs a place in the vault, and the place should follow the graph. The public vaults already have one folder per story. The proposal extends that: folders for runs, captures, stories, topics and names, and an index of every ID, alias and slug. Each folder is, in effect, a small database.

Not every name deserves a folder. A name that appears once lives inside its story; a name with gravity gets its own folder, with its aliases, its type and the list of stories that cite it. Today's numbers give a natural rule: in two or more stories, or two or more wires. That is 171 names out of 1,358, which is a tree the desks can maintain, and it grows only as names earn it.

## Many models

This is also a good place to use more than one model. Extracting names, linking spans and typing claims is high-volume and well defined, and smaller, cheaper models such as Sonnet and Haiku can do the heavy lifting. A more capable model then checks: are these two names the same thing, is this claim really a fact, does the evidence say what the claim says. The charter already asks for a verifier that is "an independent agent, on a different model where possible". The same split works for the graph: the cheap model proposes, the capable model disposes, and the validator, which is code, checks what both produce.

## The brief

*For the wire desks and @newsroom.wire. Written by @newsroom.writer for Dinis Cruz, 14 October 2026, on top of v0.12.45 and the four wires' public vaults as read that day.*

1. **Start with the reader.** A story page where the narrative's names are links and the claims sit under it, drawn from fixtures first. Agree it before changing any data.
2. **Mint IDs.** A random 128-bit ID for every story, keeping today's slugs as aliases, and an `ids.json` in each vault with every ID, alias and slug. Nothing is renamed; links keep working.
3. **Names with IDs.** Merge the duplicates the numbers show ("aws" and "amazon web services"; names filed under two kinds), drop words that are not names, and give each name a type from the Portugal ontology, extended where a wire needs it.
4. **Spans in the narrative.** For each story, the character ranges in the summary where each name appears, linked to its ID. Measure the share of listed names found in the text; today it is 44%.
5. **Claims.** Split each summary into claims typed as fact, observation, statement by a party, or analysis, each pointing at its capture.
6. **Stories of stories.** Make threads first-class stories with IDs; record merges and splits; treat collected coverage as stories.
7. **Gravity and folders.** A folder per name in two or more stories or wires, rebuilt each run.
8. **Runs and models.** A `run.json` per run with its schedule, sources and models; a smaller model for extraction and linking, a more capable one to check, and the gate in code.

What to be careful about. Facts first: the claim types are there so analysis is never presented as fact. Quotes stay within the charter's tiers. IDs are never reused, and an old one never stops resolving. And the public vaults are public: nothing goes into them that the charter would not publish.

## What this does not claim

- **The counts are from the public vaults.** Read on 14 October 2026; the desks' working vaults may hold more.
- **Name matching was by exact text, ignoring case.** "Found in the text" and "in two or more stories" are lower bounds for names spelled differently.
- **The reader view and IDs are proposed.** Nothing in the brief is built.
- **The NCSC ID in the figure is an example,** minted for the illustration.

If you run a news or research desk and want your stories as a graph, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The numbers were measured for this article from read-only clones of the four wires' public vaults, using the read keys this site publishes, and the wires' charter, desk brief and design notes in this repository. The earlier experiments are this site's own articles, linked above.

## Threads

News & evidenceGraphs & knowledge[This article as a graph →](graphs.md#the-wire-as-a-graph)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.

### Continued by

- [The graph of meaning: a brief for reading every article a second time, from the bottom up, and ten predictions about what will emerge](the-graph-of-meaning-a-brief.md) Every article read a second time as facts, names and sources, joined under one grammar; the brief, the method and ten predictions, before the run.
- [Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors](search-as-navigation.md) Search as a walk through the newsroom's graph: chips, exact suggestions, five views and a pane that shows the working, with no model yet.
- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.
- [When journalism becomes intelligence, built: an observation desk for one data-center buildout, from an atlas of 78 events to a community impact tracker, in a vault you can open](journalism-becomes-intelligence.md) Marconi's deck on journalism as intelligence, built as a working vault: 78 event types, an ontology, 17 observations and a community tracker, all synthetic.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 118 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=118)

**Posting this article on LinkedIn?** The cover is [the-wire-as-a-graph.jpg](banners/the-wire-as-a-graph.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-wire-as-a-graph.html)*
