# Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief, sgit.ai

> In a conversation today I tried to put in a few sentences what all the graph work on this site is for, and it came out as knowledge management. Take an organisation's policies and internal information, and build a fractal semantic graph of it: an ontology and a taxonomy for every element, each part kept in its own vocabulary, with named edges between them. Then brief people and agents from the graph, not from the pile of documents. They get the slice they need and the diff since they last read it, so the context is there and the tokens are not wasted. It looks a bit like vector search, but vectors give you similarity, not a reason, and the answer can change with the model and the index; a graph gives the same answer to the same question and the path that led to it. The most important part is that the feedback loop maintains itself. You do not have to get the graph right first; you have to maintain it, and agents are very good at maintaining graphs. When something in the graph looks wrong, you ask why, and the answer is a fix at the right altitude. I measured the briefing on this site: the graphs of its 112 articles hold about an eighth of the articles' text. And the brief has to travel. That is what sgit is for: an encrypted git where I give an agent the key to a vault, it reads and writes there, I can scope it to one folder and encrypt to it with its own key, and the vault itself says, this is what you need to read now.

*Source: <https://newsroom.sgit.ai/articles/knowledge-that-maintains-itself.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief

# Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/knowledge-that-maintains-itself.md) · [newsroom v0.12.40](https://newsroom.sgit.ai/admin/versions.html) · knowledge-managementfractal-semantic-graphsontologiestaxonomiesbriefingagentstokensvectorssgitvaultspoliciesarticle

***Abstract:** In a conversation today I tried to put in a few sentences what all the graph work on this site is for, and it came out as knowledge management. Take an organisation's policies and internal information, and build a fractal semantic graph of it: an ontology and a taxonomy for every element, each part kept in its own vocabulary, with named edges between them. Then brief people and agents from the graph, not from the pile of documents. They get the slice they need and the diff since they last read it, so the context is there and the tokens are not wasted. It looks a bit like vector search, but vectors give you similarity, not a reason, and the answer can change with the model and the index; a graph gives the same answer to the same question and the path that led to it. The most important part is that the feedback loop maintains itself. You do not have to get the graph right first; you have to maintain it, and agents are very good at maintaining graphs. When something in the graph looks wrong, you ask why, and the answer is a fix at the right altitude. I measured the briefing on this site: the graphs of its 112 articles hold about an eighth of the articles' text. And the brief has to travel. That is what sgit is for: an encrypted git where I give an agent the key to a vault, it reads and writes there, I can scope it to one folder and encrypt to it with its own key, and the vault itself says, this is what you need to read now.*

Knowledge that maintains itself. Sources kept in their own vocabularies; agents build and maintain the graph; people and agents are briefed from it; what looks odd is noticed and asked about; the fix lands at the right altitude; and each brief travels as a vault, scoped and encrypted to the one who needs it.

## In short

- **Policies and internal knowledge as a graph.** An ontology and a taxonomy for every element, each part in its own vocabulary, with named edges between them.
- **Brief from the graph, not the pile.** People and agents get the slice they need and the diff since they last read it.
- **Measured here: about an eighth.** The graphs of this site's 112 articles hold 12.4% of the articles' text, roughly 87,000 tokens against 704,000.
- **Graphs are not vectors.** Similarity search is useful for finding a starting point; a graph gives the same answer to the same question, with the path that led to it.
- **You do not have to get it right; you have to maintain it.** Agents are good at maintaining graphs, and a validator checks them.
- **"Why is this happening?"** An odd edge is a question, and the answer is a fix at the right altitude. This site has found several that way.
- **The brief travels in a vault.** sgit gives each agent a key, a scoped folder, its own key pair and a history of every change.

## The idea

In a conversation today I tried to say in a few sentences what all the graph work on this site is for, and it came out as knowledge management.

Every organisation has policies, standards, architecture, decisions, contracts, regulations it answers to, and a long tail of internal documents that explain why things are the way they are. Today the way most of that reaches a person or an agent is a search box and a pile of documents. The proposal is to build a [fractal semantic graph](introducing-fractal-semantic-graphs.md) of it instead: an ontology and a taxonomy for every element, a policy, a system, a team, a control, a regulation, a decision, each part kept in the vocabulary of whoever owns it, and named edges between them, with verbs that read both ways. A policy is `owned_by` a team and `implemented_by` a control; a control `answers` an article of a regulation; a decision `supersedes` an older one.

Then you brief from the graph. A person joining a team, or an agent starting a task, does not need the whole corpus. They need the part of the graph around what they are about to do, and what changed since they last looked.

## Briefing from the graph

Briefing from the graph, measured on this site. The 112 articles in full are about 704,000 tokens; their graphs as JSON with all their structure about 199,000; the graphs' text alone, teaser, core idea, nodes and edges, about 87,000. Below, what a graph gives that similarity search does not: the same answer to the same question, the path behind it, a diff of what changed, and a maintainer.

This site already works this way, so I measured it. Every article here has a graph, 8 to 18 nodes with typed edges, a teaser and a one-paragraph core idea, written with the article and checked by the validator on every release. Across the 112 articles there are 1,435 nodes and 1,538 edges. The articles' text, counted from their markdown, is about 704,000 tokens at four characters a token; the graphs as JSON, with every bracket and field name, about 199,000; the graphs' own words, teaser, core idea, node labels and summaries and the edges between them, about 87,000. That is 12.4% of the text, an eighth, and the median article's graph is 12.8% of the article.

An agent that needs to know what this site has said about agent behaviour policies can read every graph in the `agents-and-policy` topic, follow the edges to the articles that matter, and only then read those in full. The site publishes all of it for exactly that: one [file of every graph](https://newsroom.sgit.ai/articles/graphs.json), a [page that draws them](https://newsroom.sgit.ai/articles/graphs.html), an [llms.txt](https://newsroom.sgit.ai/llms.txt) index, and a markdown twin of every page.

The other half of a brief is the diff. Every article here has a version page and a word-by-word diff between versions, and [Every link points back](every-link-points-back.md) argued that a reader should be told what changed, what corrected what, and what has happened since. In a graph, that is cheap: a node superseded, an edge added, a claim marked out of date. "What changed since you last read this?" becomes a list of nodes, not a re-read.

## Graphs and vectors

It looks a bit like vector search, and in practice the two work well together. Embedding search is good at finding a starting point when you do not know the words the organisation uses. But it gives you similarity, not a reason. The result depends on the embedding model, the index and its settings; re-index with a newer model and the neighbours move. And it cannot tell you why two things are related, only that they are close.

A graph is the other kind of thing. The same question gives the same answer, because it is a walk over named edges. The answer comes with its path: this control is here because it answers that article, which this policy cites. A change is a diff of nodes and edges, not a re-embedding. For policies, where the question is often "why are we required to do this, and by whom?", the path is the answer.

## You do not have to get it right; you have to maintain it

This is the part that matters most. Nobody builds a correct graph of an organisation on the first try, and the projects that try spend a year on the ontology and never ship. The graph does not have to be right. It has to be maintained, and the loop maintains it.

Agents are very good at that work. They read a new document and propose its nodes and edges. They notice that a policy changed and mark what rested on it. They keep the graph's own rules: every edge a verb with an inverse, properties for data and edges for meaning, supersede and never delete. And the rules can be checked by something that is not an agent. On this site every article's graph is checked on every release: its quotes must be word for word in the article, its links must be links the article makes, its sizes within limits. The maintenance is done by models and verified by code.

Then the loop does the rest. When something in the graph looks wrong, an edge that should not exist, a node nobody cites, a claim with no source, you ask: why is this happening? The answer is a fix at the right altitude, in the source or in the graph, and the next brief carries it. This site has done that several times:

- **The link graph.** Walking the links between articles found that 551 of 566 point back in time, and that an earlier article described a plan a later one said had not happened. That became [Every link points back](every-link-points-back.md) and the "What came next" notes.
- **A spreadsheet of controls.** When the [AI Baseline Control Framework](ai-baseline-control-framework.md) was turned from its CSV into a graph joined to the EU AI Act's text, the graph surfaced "the six things the graph found that the CSV does not say".
- **A governance stack.** [The AI governance stack as a graph](the-ai-governance-stack-as-a-graph.md) made every cell of a ten-layer table a node, 329 edges in all, 119 of them added, each citing the fact it rests on.
- **Policies and their code.** In [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md), comparing a behaviour policy with the code that enforces it found a rule with no code and code with no rule.
- **Code review.** In [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) and its [vault](https://sgit.ai/demos/vaults/code-review-graphs/index.html), a change is read at every layer from the method to the story.

The [fractal semantic graphs page](https://sgit.ai/demos/fractal-graphs/index.html) and the [regulation graph vault](https://sgit.ai/demos/vaults/regulation-graph/index.html) are the open examples to start from.

## The brief has to travel

A brief is only useful if it gets to the person or agent who needs it, and only them. That is what sgit is for, and why I built it. [sgit](what-sgit-is.md) is an encrypted git: the files are encrypted before they leave, and the server holds only ciphertext. To brief an agent, I give it the key to a vault. It can read what is there, write what it finds, and every change is a commit, so the history is the diff.

The pieces line up with the graph. A scoped clone takes only one folder of a vault, so an agent can hold its slice and nothing else, as [sgit in a CI pipeline](sgit-in-a-ci-pipeline.md) measured. A key pair per agent means a brief can be encrypted to the one agent that should read it. An append lane lets an agent send its findings back without being able to read anything. And the vault can say, in its own index, this is what you need to read now. This site's agents already work like that: [two agents share one vault](two-agents-one-vault.md) with only the read key on the public side; agents that run [somewhere else](encrypted-memory-for-isolated-agents.md) keep their memory in one; and the policy this site's own agent works under is a brief, [restored after every summary](re-anchoring-agent-behaviour-policies.md). [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) is the longer version of why the memory has to be something the owner keeps.

## What this does not claim

- **Tokens are estimated.** Characters divided by four, on this site's 112 articles and their graphs at v0.12.39.
- **A graph is a map, not the territory.** An eighth of the text is enough to choose what to read, not a replacement for reading it.
- **Vectors still help.** For finding a starting point in unfamiliar words, similarity search is useful; the graph is what makes the answer repeatable and explainable.
- **This site's graphs have a contract.** Their size and checks are why they compress well; an organisation's graph needs the same discipline.
- **Maintenance is still work.** Agents do most of it and a validator checks it, but someone has to own the ontology at each altitude.

If you are drowning in policies and internal documents and want to see them as a graph, or you want to brief your agents from one, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, from a conversation about knowledge management, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The briefing figures were counted for this article from this site's article markdown and its graph files at v0.12.39. The examples are this site's own articles and the open vaults linked above.

## Threads

Graphs & knowledgeVaults & method[This article as a graph →](graphs.md#knowledge-that-maintains-itself)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.
- [The AI governance stack, as a graph: an answer to Hari Kota, built](the-ai-governance-stack-as-a-graph.md) Hari Kota's ten-layer AI governance stack, kept as posted and turned into a fractal semantic graph: the gaps become missing edges, and queries.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.

### Continued by

- [AWS from the vault: a proposed aws.twin.sgit.ai, where a temporary AWS session lives in the user's vault, the browser does the work, and AWS data finally has a place to go](aws-from-the-vault.md) A proposed aws.twin.sgit.ai: an AWS twin on a vault first, then a temporary AWS session from the user's vault.
- [Bringing my past work back: a daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles, and why every team needs one](bringing-my-past-work-back.md) A daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles: then and now, connected, two or three a day.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it](the-agents-write-too.md) The newsroom's agents get their own bylines: lessons every agent loads, debriefs as source material, a page for every agent, and a conductor.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 113 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=113)

**Posting this article on LinkedIn?** The cover is [knowledge-that-maintains-itself.jpg](banners/knowledge-that-maintains-itself.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/knowledge-that-maintains-itself.html)*
