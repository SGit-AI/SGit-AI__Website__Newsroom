# Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database, sgit.ai

> Francois Vanderseypen, who consults on knowledge graphs, reviewed Neo4j's new Relate and made the point I think matters most in this whole space: the market treats "graph database" as a synonym for "agent memory", and both framings skip the hard part, which is the lifecycle, what gets written, what gets trusted, what gets merged and what should be forgotten. A database cannot answer that; a memory layer has to. I agree, and his list of what turns a graph store into a memory system, ontologies, bitemporal facts, reasoning and git-like graph commits, reads like a description of what we have been building, without a graph database. Our graphs are JSON files in encrypted, versioned sgit vaults. Written: append lanes, where a sender can add and learn nothing, and a curator agent that turns rows into graph, every node pointing back at its rows. Trusted: signed commits naming the agent and the person it works for, provenance on every claim, a reviewer before anything is published. Merged: git-like commits, branches and merges of graph files, and per-world ontologies joined by an edge instead of a migration. Forgotten: a new version instead of an edit, a reality file that lists only what is true now, and superseded facts kept, closed and left out of the briefing. Here is the map, and a nudge: the store can be versioned and private, and the engine can be thrown away after every question.

*Source: <https://newsroom.sgit.ai/articles/memory-is-a-lifecycle.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database

# Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/memory-is-a-lifecycle.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · graphsagent-memoryknowledge-graphsneo4jsgitvaultsontologiesarticle

***Abstract:** Francois Vanderseypen, who consults on knowledge graphs, reviewed Neo4j's new Relate and made the point I think matters most in this whole space: the market treats "graph database" as a synonym for "agent memory", and both framings skip the hard part, which is the lifecycle, what gets written, what gets trusted, what gets merged and what should be forgotten. A database cannot answer that; a memory layer has to. I agree, and his list of what turns a graph store into a memory system, ontologies, bitemporal facts, reasoning and git-like graph commits, reads like a description of what we have been building, without a graph database. Our graphs are JSON files in encrypted, versioned sgit vaults. Written: append lanes, where a sender can add and learn nothing, and a curator agent that turns rows into graph, every node pointing back at its rows. Trusted: signed commits naming the agent and the person it works for, provenance on every claim, a reviewer before anything is published. Merged: git-like commits, branches and merges of graph files, and per-world ontologies joined by an edge instead of a migration. Forgotten: a new version instead of an edit, a reality file that lists only what is true now, and superseded facts kept, closed and left out of the briefing. Here is the map, and a nudge: the store can be versioned and private, and the engine can be thrown away after every question.*

Memory is a lifecycle: written, trusted, merged, forgotten, and where each lives in our stack.

## In short

- **Francois is right:** a graph database is not agent memory; the hard part is the lifecycle.
- **Four questions:** what gets written, trusted, merged and forgotten.
- **We answer them without a graph database,** with JSON graphs in encrypted, versioned vaults.
- **His missing features are ours by construction:** git-like graph commits, record time, per-world ontologies.
- **Forgetting is a new version,** not a delete: the briefing changes, the history stays.
- **The engine can be thrown away** after every question; the memory cannot.

## The post

Francois Vanderseypen, knowledge graph consulting, on Neo4j's Relate and agent memory, LinkedIn, November 2026.

Francois Vanderseypen, who consults on knowledge graphs, spent a lot of time with Neo4j's new Relate and wrote a fair review. Well executed and reliable, he says, embedded and in Rust, with a single-file store, a WebAssembly build, openCypher, MCP and Bolt; but missing innovation and vision. He lists what the open-source scene has produced that Relate mostly ignores, from memory degradation that drops knowledge nobody uses, to multi-graph, to RDF and property graphs together, to explainable decisions in the query language.

Then the line I most agree with: "the market treats 'graph database' as a synonym for 'agent memory', while ingestion is treated as just another agent skill. Both framings skip the hard part, which is the lifecycle: what gets written, what gets trusted, what gets merged, and what should be forgotten. A database can't answer that. A memory layer has to."

I wrote a separate debrief of Relate itself ([Relate, debriefed](relate-debriefed.md)). This is about his four questions, because they are the right ones, and we have had to answer every one of them.

## Written

In our stack, writing to memory is not a database insert. Sources append to lanes: a sender holds a write-only token, can add a sealed message to a vault, and learns nothing at all, not even whether anyone else writes there ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)). A curator agent reads the lanes and turns rows into graph: things, links and claims, every node pointing back at the rows it came from ([the new data lake](the-new-data-lake.md)). Ingestion is not a skill bolted on; it is a role with a policy, and what it writes is a commit.

## Trusted

Trust is the part a database leaves to you. Every commit names the agent that made it and the person it works for, and is signed where the stakes need it ([a key for every person](a-key-for-every-person.md)). Every claim carries its evidence: a source, an observation, a statement by a party, or our analysis, marked as which. And nothing reaches readers without a reviewer, a separate agent that checks claims against sources ([the wire as a graph](the-wire-as-a-graph.md)). Trust is then something you can inspect after the fact, not a property of the store.

## Merged

Francois lists git-like graph commits among the missing features. In a vault, they are simply how the store works: graph files are committed, branched and merged like code, every version kept. And merging two domains does not need a shared schema. Each world keeps its own ontology, a regulation, its articles, the words they define, and the worlds are joined by an edge, under a grammar where every edge is a verb ([knowledge that maintains itself](knowledge-that-maintains-itself.md)). That is the multi-graph he wants, without a migration project.

## Forgotten

Forgetting is the subtlest of the four, and the one I would push back on gently. In memory for agents, I do not think you should delete; you should stop briefing. Our files are immutable, so a change is a new version, never an edit. A reality file lists only what is true now, and is what an agent reads first. Superseded facts are kept, closed, and left out of the briefing, so an agent gets the slice it needs and the diff since it last looked, not the whole pile. That is also the bitemporal model: the commit history is record time, when we believed it; valid time, when it held in the world, is a field in the fact. Memory degradation, in this shape, is a curator's decision about what the briefing includes, not a loss of history.

## A nudge

So my answer to Francois's last line, that products should decide whether they are a database or a memory, is that the memory and the engine can be separate things. The memory is a versioned, private, distributed store of plain files, with its lifecycle in commits, lanes, signatures and reviewers. The engine is whatever answers this question, and can be thrown away after it: SQLite in WebAssembly today, and, I would argue, Relate tomorrow, which is exactly the right shape for it ([Relate, debriefed](relate-debriefed.md)). It is a different bill from a graph database's: you pay for the bytes a question reads, not for a server holding the graph.

## What this does not claim

- **Not a review of the products Francois lists;** I quote only his post.
- **Our approach is slower at deep traversals** over very large graphs, which is a graph database's home ground.
- **Memory degradation as a curator's choice** is my position, not a feature we have measured.
- **Francois's views are his own.**

## Where this comes from

Francois Vanderseypen's LinkedIn post on Relate, read on 17 November 2026, and [relatedb.ai](https://relatedb.ai/). Earlier on this site: [Relate, debriefed](relate-debriefed.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [the new data lake](the-new-data-lake.md), [a key for every person](a-key-for-every-person.md), [the wire as a graph](the-wire-as-a-graph.md), [knowledge that maintains itself](knowledge-that-maintains-itself.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#memory-is-a-lifecycle)

### Builds on

- [Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle](relate-debriefed.md) A debrief of Neo4j's Relate, and how it compares with keeping graphs as JSON in encrypted, versioned sgit vaults, and why they fit together.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks](the-wire-as-a-graph.md) Design the wire from what the reader sees: every name a link with a long-lived ID, every sentence a claim, stories of stories, folders by gravity.
- [Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief](knowledge-that-maintains-itself.md) Fractal semantic graphs for policies and internal knowledge: brief people and agents from the graph, maintain it in a loop, carry the brief in a vault.

### Continued by

- [Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle](relate-debriefed.md) A debrief of Neo4j's Relate, and how it compares with keeping graphs as JSON in encrypted, versioned sgit vaults, and why they fit together.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 446 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=446)

**Posting this article on LinkedIn?** The cover is [memory-is-a-lifecycle.jpg](banners/memory-is-a-lifecycle.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/memory-is-a-lifecycle.html)*
