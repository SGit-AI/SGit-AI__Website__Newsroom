# Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema, sgit.ai

> The introduction to the term. Four words and only one of them new; the test that decides whether something deserves the word, worked from a risk register to a TCP packet; why every file format is already a graph; the five-rule grammar; the evidence, eleven altitudes across seven live vaults; what is still modelled rather than imported; and why now.

*Source: <https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema

# Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-09-20 · [article v1.1.1, 6 versions](versions/introducing-fractal-semantic-graphs.md) · [sgit.ai v0.2.97](https://sgit.ai/admin/versions.md) · graphsmethodfractal-semantic-graphsarticle

***Abstract:** The introduction to the term. Four words and only one of them new; the test that decides whether something deserves the word, worked from a risk register to a TCP packet; why every file format is already a graph; the five-rule grammar; the evidence, eleven altitudes across seven live vaults; what is still modelled rather than imported; and why now.*

*By Dinis Cruz. This is the canonical copy of the article, with the diagrams and screenshots the LinkedIn version cannot carry. The definition it introduces, the three diagrams and the seven vaults are on [the Fractal Semantic Graphs page](https://sgit.ai/demos/fractal-graphs/index.md); the vault where the idea was first worked is [VoiceDebrief · Fractal Semantic Graphs](https://sgit.ai/demos/vaults/voice-debrief/index.md).*

For about six months I have been calling this "graphs of graphs of graphs", or when I was feeling more precise, "ontologies of ontologies of ontologies". Neither is a name you can put on a page. This week we gave it one, defined it, and published the evidence: seven live graphs you can open in a browser, from the text of a law down to a threat in one line of code on one compute instance, all built with one method.

The name is Fractal Semantic Graph. This article is the introduction.

## Four words, and only one of them is new

Most people reading this already know three of the four.

A graph is nodes and edges. A semantic graph gives the edges meaning: every edge is a verb, and every verb has a named inverse, so a link reads correctly from whichever end you are standing at. A fact `gives_rise_to` a risk; a risk `arises_from` a fact. An ontology is the agreed vocabulary of node types and verbs that a graph is allowed to use.

The fourth word is fractal, and here is what it adds.

A fractal semantic graph has no privileged level and no single schema. Zoom into any node and you enter a new world with its own node types, its own verbs, its own taxonomy, its own centre of gravity. A regulation is a node in a graph of instruments and jurisdictions. Open it and it is a graph of articles, recitals and amendments: a legal ontology. Open an article and it is a graph of paragraphs and points. Open a paragraph and it is a graph of the terms it uses, each one an edge to the article that defines it: a lexical ontology that looks nothing like the one two levels up.

Three zooms, three ontologies. A four-node semantic graph; the Law node opened into a legal ontology of articles, paragraphs and an amendment drawn as an edge; one paragraph opened into a lexical ontology of the terms it uses. The grammar never changes; the ontology does.

Every one of those worlds was defined by whoever owns it, in its own vocabulary, and none of them was made to conform to the others. What connects them is that each one is still a semantic graph. Every edge is a verb with an inverse. Every node knows where it came from. So an edge can be drawn from any node in one world to any node in another, and the walk works.

There is no top and no bottom. There is only the altitude you happen to be looking from, and how much definition you choose to load at it.

The GDPR atlas says it in its own graph view: "You are at the top of the fractal. Each domain is its own ontology that connects up to the GDPR root and down to concepts and articles." The layout is computed from the graph, not drawn.

## The test is what happens at a link

Here is the test I use to decide whether something deserves the word.

Start inside a risk register. A good one is already a rich semantic graph with a large vocabulary of verbs. A fact `gives_rise_to` a risk, a risk `is_owned_by` a role, a person `reports_to` a person, a control `mitigates` a risk, evidence `backs` a fact. Every link that makes sense inside that ontology teaches you something, and a register with ten thousand well named edges is a great deal of knowledge.

Nothing about it is fractal yet. It is one graph, however large and however deeply it nests, in one vocabulary. A system that never lets you leave that vocabulary is a single graph, or a hierarchy. Not a fractal.

The fractal property is that on one of those links you can jump into another universe.

Follow the register's fact node for an incident and you land in the security operations world: alerts, signals, the systems that were touched, ATT&CK techniques, attack trees. Its own verbs, its own taxonomy, none of it borrowed from the register. In that world you meet a DNS entry that looks like command and control. Follow it and you are in the DNS estate: zones, records, parents, values, every request the resolvers logged, a dataset that might be millions of nodes and is quite possibly served from a SQL database or a GraphQL endpoint rather than held as files. Follow one record to the traffic it produced and you are reading network captures, flows, and eventually a single TCP packet, in yet another vocabulary.

Four worlds. Four ontologies. Four taxonomies. One continuous path of named edges between them, and nobody built an adapter.

The jump. Four worlds in a row, each a small graph in its own vocabulary, joined by a jump link on one node each. All four together are one node in a bigger graph that analyses them, and that graph in another.

What makes it fractal rather than merely linked is that in every one of those self contained worlds you find the same building blocks: nodes, edges with verbs and inverses, an ontology, a taxonomy, provenance. The grammar is what lets the jump work, in either direction. And it runs upward as well as down. Everything I just described can itself be one node in a larger graph that analyses it, sitting next to graphs of behaviour, of agent actions, of agendas, of funding.

## Everything is already a graph, including every file format

This is the part that took me longest to see clearly, and once you see it you cannot unsee it.

A regulation is a graph of articles. A PDF of that regulation is a graph of pages, blocks, lines and glyphs. A spreadsheet is a graph of sheets, rows, cells and formulas. A codebase is a graph of packages, classes, methods and tokens. A JSON document is a tree, which is a graph with one verb.

None of them needs to be converted into a graph. Each one only needs its edges named. And once the edges are named, the boundaries between formats stop mattering, and things become possible that no document can do.

A question can cross formats without a join table. "Which method in our code implements the control that the crosswalk maps to the article the amendment changed?" is one traversal, from a word in a law to a control in a standard to an attestation to a method, because each step is an edge somebody named.

A correction propagates instead of being republished. Mark one node superseded and every path that rested on it becomes a query: what did we build on this? A document cannot do that. The correction is a new document, and nothing connects it to the thousand that already cite the error.

The smallest node is whatever your question needs, not what the format offers. For a lawyer it is the defined term. For a threat model it is the method. For a conformance check it is the attestation and its expiry date. For our GDPR atlas it is, literally, the word.

Every unit keeps its own world. The regulation is modelled in the regulator's vocabulary, the register in the risk team's, the threat model in the engineers', and none of them is asked to change. The bridges are edges somebody declares, not a merged schema everybody has to agree on first.

And provenance comes free. When the leaf is a word, and the word is connected to the byte range it came from and the hash of the file that held it, every claim at every altitude above it is traceable to source with no extra machinery.

## The grammar is short, and one rule does most of the work

Each altitude gets its own schema. What none of them gets to change is the grammar, and the grammar is five rules.

Every edge is a verb, stated in both directions, with an inverse a person in the business would actually say. `relates_to` is banned. Properties carry data, never meaning, so two nodes both holding the value 8080 differ only in what they are connected to. Supersede, never delete. And never render the whole graph: render the answer to a question.

The banned verb is the one I get the most pushback on, so let me defend it. Two things always relate. An edge with no verb constrains nothing and cannot narrow a query. The granularity of the verb is the precision of the question you will later be able to ask. Every time somebody reaches for `relates_to` they are deferring the thinking to whoever has to read the graph later, and that person is usually you.

## The evidence: eleven altitudes, seven vaults, one grammar

A definition is cheap. So we published the ladder.

Eleven altitudes, each one a live graph in its own vocabulary, modelled by its own author, and every altitude joined to the next by a named edge. From the top: the law, the standard, the evidence behind the standard, the fact about your estate, the risk it gives rise to, the owner, the acceptance, the insuring policy, the agent, the system, the compute instance.

The ladder: eleven altitudes, eleven ontologies, one grammar. Each altitude names the published vault where that altitude is a live graph, and on the page each name is a link to the vault and its read key.

At the top sits the EU AI Act, parsed from the official XML into 113 articles, 500 paragraphs, 417 points, 180 recitals, 13 annexes and 68 definitions: 1,523 nodes and 1,944 edges, with the SHA-256 of the retrieved bytes at the end of every provenance chain. When something elsewhere says "touches Article 12", this is the graph that can say what Article 12 says and prove the bytes.

The Regulation Graph's landing view: the counts, both instruments with their CELEX identifiers and the hash of the retrieved bytes, and application dates kept as versioned properties rather than bare facts.

One altitude down is the AIUC-1 agent standard as data: 53 controls, 2,788 nodes, 11,610 edges. Its explorer loads two vaults as one graph, and one of the packs it loads is literally the AI Act by article from the vault above. That join is where a crosswalk stops being a string. The standard publishes 1,126 crosswalks as text. 62 of them resolve into node identifiers in the regulation graph. And the traversal returns something neither graph knew on its own: 8 of the 27 articles reached have since been amended, so the crosswalk was written against text that no longer says what it said.

That is the whole argument in one number. Two graphs, built by different people for different purposes in different vocabularies, joined by declared edges, produced a finding that did not exist in either of them.

Two vaults on one canvas. The chip row is the join: the standard, its crosswalks, another vault's articles, the conformance layer, bow ties, acceptances.

At the bottom of the ladder is a threat model that is itself a graph of graphs: eleven linked models zooming from Customer through Business, Application, Component, Package, Class and Method, down to Source Code, Environment, Runtime and Compute. 51 nodes, 179 threats. The demonstration is a single SQL injection traced upward from the method it lives in to the revenue it puts at risk, and then framed four ways, for the board, the CISO, the CTO and the developer, from one fact.

The zoom ladder, counted: 11 layers, 51 nodes, 179 threats. The bottom altitude is a compute instance.

In between are the altitudes that make this useful to people who are not engineers: a register where answers become facts and facts give rise to risks, an org chart with risks flowing up it until every path terminates at the board, and the same exposure read at seven stakeholder altitudes, each owning it in their own words.

The role risk map: what a role holds against what arrives through it because the graph says it must. Nothing stops short of the board.

My favourite single picture in the whole set is Article 45 of the GDPR. The text has not changed a word since 2016. What it permits has flipped four times: Safe Harbour, Schrems I, Privacy Shield, Schrems II, the Data Privacy Framework, and an appeal pending. The atlas draws that as a timeline of ruling nodes over one unchanged article node. The text is a constant. Its meaning is the graph. That is why a static PDF of a law is wrong and a versioned graph is not.

One article, five rulings, twenty-five years. Safe Harbour to a pending CJEU appeal, over an Article 45 that has not changed a word.

## What is still modelled rather than imported

I would rather tell you this than have you find it.

The bottom four altitudes of the threat model, environment through compute, are nodes an author placed, not a live import from a CMDB, an infrastructure repository or a cloud account. The grammar to receive such an import exists. The connector that emits it is not published yet.

Enterprise architecture is a gap. No published graph holds an EA repository joined upward to obligations, and that is the layer between the standard and the system that the ladder cannot yet point at.

The crosswalks resolve at article level only, where the regulation graph has paragraphs. The GDPR atlas is a seed pass from May, and six of its 227 edges use the banned `relates` verb, because the rule was written after that graph was. And the agent altitude is a vocabulary, not yet a join: we have the 23 capability primitives that describe what an agent can do, and no published graph yet imports a real permission set and computes the difference against what the operator intended, at scale.

Named gaps get filled. Unnamed ones do not. That is why they are on the page.

## Why now

Three things changed in the last year that make this practical rather than academic.

Naming edges used to be the expensive part. It is now the cheap part. A language model can propose the verb between two nodes faster than a human can type it, which means the bottleneck moved from authoring the graph to deciding what the graph is for.

Agents act on the world, and when something acts, provenance stops being a nicety. Every consequential claim needs to be traceable to the byte it came from, and a graph whose leaf is the word gives you that without a second system.

And the schema wars are over, because nobody won. Every organisation, division, team and regulator has its own vocabulary and will keep it. The only integration model that survives contact with that fact is one where nobody is asked to conform and everybody is allowed to connect.

## Open them

Everything in this article is a live graph you can open. Every read key is published on purpose, and none of them can write. Start at the law and walk down, or start at the compute instance and walk up. Either direction works, which is rather the point.

- The definition, the ladder and the seven vaults: [sgit.ai/demos/fractal-graphs](https://sgit.ai/demos/fractal-graphs/index.md)
- The vault where the idea was first worked, with its fifteen-principle register: [VoiceDebrief · Fractal Semantic Graphs](https://sgit.ai/demos/vaults/voice-debrief/index.md)
- The grammar in full, with the four situations in which the argument is wrong: [graphs.sgit.ai](https://graphs.sgit.ai/)
- Laws and standards as addressable provisions: [standards.sgit.ai](https://standards.sgit.ai/)
- The Agent Behaviour Policy, where the graph meets a real permission set: [abp.sgit.ai](https://abp.sgit.ai/)

If you build one of your own, the grammar for drawing it is at [graphs.sgit.ai/llms.txt](https://graphs.sgit.ai/llms.txt), and it is written for agents as much as for people. I would like to see what you connect to what.

*This article is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). The diagrams are inline SVG on the Fractal Semantic Graphs page and may be reused under the same terms; the screenshots are of published vaults, taken with their published read keys.*

## Threads

Graphs & knowledge[This article as a graph →](graphs.md#introducing-fractal-semantic-graphs)

### Continued by

- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [The AI governance stack, as a graph: an answer to Hari Kota, built](the-ai-governance-stack-as-a-graph.md) Hari Kota's ten-layer AI governance stack, kept as posted and turned into a fractal semantic graph: the gaps become missing edges, and queries.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [Liquid content needs water: liquefy the journalist's notebook, not the finished product](liquid-content-needs-water.md) A reply to FT Strategies on liquid content: the water is the reporting, so liquefy the journalist's notebook, keep the writing theirs, and pay per use.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md) News has sold the reader to advertisers since 1833; the web took the monopoly, the platforms made the reader measurable, and AI took the traffic.
- [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md) AI answer engines pay to read the web as HTML; a publisher who serves markdown, dates, hashes and a typed graph saves them tokens and should get a share.
- [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md) The food chain is a data problem: one encrypted vault per party, joined by append lanes and a typed graph, could cut the waste that keeps prices high.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 8 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=8)

**Posting this article on LinkedIn?** The cover is [introducing-fractal-semantic-graphs.jpg](banners/introducing-fractal-semantic-graphs.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html)*
