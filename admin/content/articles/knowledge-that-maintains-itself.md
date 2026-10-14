---
title: Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: In a conversation today I tried to put in a few sentences what all the graph work on this site is for, and it came out as knowledge management. Take an organisation's policies and internal information, and build a fractal semantic graph of it: an ontology and a taxonomy for every element, each part kept in its own vocabulary, with named edges between them. Then brief people and agents from the graph, not from the pile of documents. They get the slice they need and the diff since they last read it, so the context is there and the tokens are not wasted. It looks a bit like vector search, but vectors give you similarity, not a reason, and the answer can change with the model and the index; a graph gives the same answer to the same question and the path that led to it. The most important part is that the feedback loop maintains itself. You do not have to get the graph right first; you have to maintain it, and agents are very good at maintaining graphs. When something in the graph looks wrong, you ask why, and the answer is a fix at the right altitude. I measured the briefing on this site: the graphs of its 112 articles hold about an eighth of the articles' text. And the brief has to travel. That is what sgit is for: an encrypted git where I give an agent the key to a vault, it reads and writes there, I can scope it to one folder and encrypt to it with its own key, and the vault itself says, this is what you need to read now.
version: v0.12.40
license: https://creativecommons.org/licenses/by/4.0/
tags: knowledge-management, fractal-semantic-graphs, ontologies, taxonomies, briefing, agents, tokens, vectors, sgit, vaults, policies, article
status: published
---

!shot kq-loop.webp | images/ | Knowledge that maintains itself. Sources kept in their own vocabularies; agents build and maintain the graph; people and agents are briefed from it; what looks odd is noticed and asked about; the fix lands at the right altitude; and each brief travels as a vault, scoped and encrypted to the one who needs it. | architecture

## In short {#in-short}

- **Policies and internal knowledge as a graph.** An ontology and a taxonomy for every element, each part in its own vocabulary, with named edges between them.
- **Brief from the graph, not the pile.** People and agents get the slice they need and the diff since they last read it.
- **Measured here: about an eighth.** The graphs of this site's 112 articles hold 12.4% of the articles' text, roughly 87,000 tokens against 704,000.
- **Graphs are not vectors.** Similarity search is useful for finding a starting point; a graph gives the same answer to the same question, with the path that led to it.
- **You do not have to get it right; you have to maintain it.** Agents are good at maintaining graphs, and a validator checks them.
- **"Why is this happening?"** An odd edge is a question, and the answer is a fix at the right altitude. This site has found several that way.
- **The brief travels in a vault.** sgit gives each agent a key, a scoped folder, its own key pair and a history of every change.

## The idea {#idea}

In a conversation today I tried to say in a few sentences what all the graph work on this site is for, and it came out as knowledge management.

Every organisation has policies, standards, architecture, decisions, contracts, regulations it answers to, and a long tail of internal documents that explain why things are the way they are. Today the way most of that reaches a person or an agent is a search box and a pile of documents. The proposal is to build a [fractal semantic graph](/articles/introducing-fractal-semantic-graphs.html) of it instead: an ontology and a taxonomy for every element, a policy, a system, a team, a control, a regulation, a decision, each part kept in the vocabulary of whoever owns it, and named edges between them, with verbs that read both ways. A policy is `owned_by` a team and `implemented_by` a control; a control `answers` an article of a regulation; a decision `supersedes` an older one.

Then you brief from the graph. A person joining a team, or an agent starting a task, does not need the whole corpus. They need the part of the graph around what they are about to do, and what changed since they last looked.

## Briefing from the graph {#briefing}

!shot kq-briefing.webp | images/ | Briefing from the graph, measured on this site. The 112 articles in full are about 704,000 tokens; their graphs as JSON with all their structure about 199,000; the graphs' text alone, teaser, core idea, nodes and edges, about 87,000. Below, what a graph gives that similarity search does not: the same answer to the same question, the path behind it, a diff of what changed, and a maintainer. | comparison

This site already works this way, so I measured it. Every article here has a graph, 8 to 18 nodes with typed edges, a teaser and a one-paragraph core idea, written with the article and checked by the validator on every release. Across the 112 articles there are 1,435 nodes and 1,538 edges. The articles' text, counted from their markdown, is about 704,000 tokens at four characters a token; the graphs as JSON, with every bracket and field name, about 199,000; the graphs' own words, teaser, core idea, node labels and summaries and the edges between them, about 87,000. That is 12.4% of the text, an eighth, and the median article's graph is 12.8% of the article.

An agent that needs to know what this site has said about agent behaviour policies can read every graph in the `agents-and-policy` topic, follow the edges to the articles that matter, and only then read those in full. The site publishes all of it for exactly that: one [file of every graph](https://newsroom.sgit.ai/articles/graphs.json), a [page that draws them](https://newsroom.sgit.ai/articles/graphs.html), an [llms.txt](https://newsroom.sgit.ai/llms.txt) index, and a markdown twin of every page.

The other half of a brief is the diff. Every article here has a version page and a word-by-word diff between versions, and [Every link points back](/articles/every-link-points-back.html) argued that a reader should be told what changed, what corrected what, and what has happened since. In a graph, that is cheap: a node superseded, an edge added, a claim marked out of date. "What changed since you last read this?" becomes a list of nodes, not a re-read.

## Graphs and vectors {#vectors}

It looks a bit like vector search, and in practice the two work well together. Embedding search is good at finding a starting point when you do not know the words the organisation uses. But it gives you similarity, not a reason. The result depends on the embedding model, the index and its settings; re-index with a newer model and the neighbours move. And it cannot tell you why two things are related, only that they are close.

A graph is the other kind of thing. The same question gives the same answer, because it is a walk over named edges. The answer comes with its path: this control is here because it answers that article, which this policy cites. A change is a diff of nodes and edges, not a re-embedding. For policies, where the question is often "why are we required to do this, and by whom?", the path is the answer.

## You do not have to get it right; you have to maintain it {#maintain}

This is the part that matters most. Nobody builds a correct graph of an organisation on the first try, and the projects that try spend a year on the ontology and never ship. The graph does not have to be right. It has to be maintained, and the loop maintains it.

Agents are very good at that work. They read a new document and propose its nodes and edges. They notice that a policy changed and mark what rested on it. They keep the graph's own rules: every edge a verb with an inverse, properties for data and edges for meaning, supersede and never delete. And the rules can be checked by something that is not an agent. On this site every article's graph is checked on every release: its quotes must be word for word in the article, its links must be links the article makes, its sizes within limits. The maintenance is done by models and verified by code.

Then the loop does the rest. When something in the graph looks wrong, an edge that should not exist, a node nobody cites, a claim with no source, you ask: why is this happening? The answer is a fix at the right altitude, in the source or in the graph, and the next brief carries it. This site has done that several times:

- **The link graph.** Walking the links between articles found that 551 of 566 point back in time, and that an earlier article described a plan a later one said had not happened. That became [Every link points back](/articles/every-link-points-back.html) and the "What came next" notes.
- **A spreadsheet of controls.** When the [AI Baseline Control Framework](/articles/ai-baseline-control-framework.html) was turned from its CSV into a graph joined to the EU AI Act's text, the graph surfaced "the six things the graph found that the CSV does not say".
- **A governance stack.** [The AI governance stack as a graph](/articles/the-ai-governance-stack-as-a-graph.html) made every cell of a ten-layer table a node, 329 edges in all, 119 of them added, each citing the fact it rests on.
- **Policies and their code.** In [Policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html), comparing a behaviour policy with the code that enforces it found a rule with no code and code with no rule.
- **Code review.** In [Code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html) and its [vault](https://sgit.ai/demos/vaults/code-review-graphs/index.html), a change is read at every layer from the method to the story.

The [fractal semantic graphs page](https://sgit.ai/demos/fractal-graphs/index.html) and the [regulation graph vault](https://sgit.ai/demos/vaults/regulation-graph/index.html) are the open examples to start from.

## The brief has to travel {#vaults}

A brief is only useful if it gets to the person or agent who needs it, and only them. That is what sgit is for, and why I built it. [sgit](/articles/what-sgit-is.html) is an encrypted git: the files are encrypted before they leave, and the server holds only ciphertext. To brief an agent, I give it the key to a vault. It can read what is there, write what it finds, and every change is a commit, so the history is the diff.

The pieces line up with the graph. A scoped clone takes only one folder of a vault, so an agent can hold its slice and nothing else, as [sgit in a CI pipeline](/articles/sgit-in-a-ci-pipeline.html) measured. A key pair per agent means a brief can be encrypted to the one agent that should read it. An append lane lets an agent send its findings back without being able to read anything. And the vault can say, in its own index, this is what you need to read now. This site's agents already work like that: [two agents share one vault](/articles/two-agents-one-vault.html) with only the read key on the public side; agents that run [somewhere else](/articles/encrypted-memory-for-isolated-agents.html) keep their memory in one; and the policy this site's own agent works under is a brief, [restored after every summary](/articles/re-anchoring-agent-behaviour-policies.html). [Memory is not a spectator sport](/articles/memory-is-not-a-spectator-sport.html) is the longer version of why the memory has to be something the owner keeps.

## What this does not claim {#limits}

- **Tokens are estimated.** Characters divided by four, on this site's 112 articles and their graphs at v0.12.39.
- **A graph is a map, not the territory.** An eighth of the text is enough to choose what to read, not a replacement for reading it.
- **Vectors still help.** For finding a starting point in unfamiliar words, similarity search is useful; the graph is what makes the answer repeatable and explainable.
- **This site's graphs have a contract.** Their size and checks are why they compress well; an organisation's graph needs the same discipline.
- **Maintenance is still work.** Agents do most of it and a validator checks it, but someone has to own the ontology at each altitude.

If you are drowning in policies and internal documents and want to see them as a graph, or you want to brief your agents from one, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, from a conversation about knowledge management, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The briefing figures were counted for this article from this site's article markdown and its graph files at v0.12.39. The examples are this site's own articles and the open vaults linked above.
