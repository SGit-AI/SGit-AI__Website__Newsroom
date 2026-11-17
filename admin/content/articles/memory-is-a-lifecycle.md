---
title: Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Francois Vanderseypen, who consults on knowledge graphs, reviewed Neo4j's new Relate and made the point I think matters most in this whole space: the market treats "graph database" as a synonym for "agent memory", and both framings skip the hard part, which is the lifecycle, what gets written, what gets trusted, what gets merged and what should be forgotten. A database cannot answer that; a memory layer has to. I agree, and his list of what turns a graph store into a memory system, ontologies, bitemporal facts, reasoning and git-like graph commits, reads like a description of what we have been building, without a graph database. Our graphs are JSON files in encrypted, versioned sgit vaults. Written: append lanes, where a sender can add and learn nothing, and a curator agent that turns rows into graph, every node pointing back at its rows. Trusted: signed commits naming the agent and the person it works for, provenance on every claim, a reviewer before anything is published. Merged: git-like commits, branches and merges of graph files, and per-world ontologies joined by an edge instead of a migration. Forgotten: a new version instead of an edit, a reality file that lists only what is true now, and superseded facts kept, closed and left out of the briefing. Here is the map, and a nudge: the store can be versioned and private, and the engine can be thrown away after every question.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: graphs, agent-memory, knowledge-graphs, neo4j, sgit, vaults, ontologies, article
status: published
---

!shot fv-lifecycle.webp | images/ | Memory is a lifecycle: written, trusted, merged, forgotten, and where each lives in our stack. | concept

## In short {#in-short}

- **Francois is right:** a graph database is not agent memory; the hard part is the lifecycle.
- **Four questions:** what gets written, trusted, merged and forgotten.
- **We answer them without a graph database,** with JSON graphs in encrypted, versioned vaults.
- **His missing features are ours by construction:** git-like graph commits, record time, per-world ontologies.
- **Forgetting is a new version,** not a delete: the briefing changes, the history stays.
- **The engine can be thrown away** after every question; the memory cannot.

## The post {#post}

!shot fv-question.webp | images/ | Francois Vanderseypen, knowledge graph consulting, on Neo4j's Relate and agent memory, LinkedIn, November 2026. | medium | aside

Francois Vanderseypen, who consults on knowledge graphs, spent a lot of time with Neo4j's new Relate and wrote a fair review. Well executed and reliable, he says, embedded and in Rust, with a single-file store, a WebAssembly build, openCypher, MCP and Bolt; but missing innovation and vision. He lists what the open-source scene has produced that Relate mostly ignores, from memory degradation that drops knowledge nobody uses, to multi-graph, to RDF and property graphs together, to explainable decisions in the query language.

Then the line I most agree with: "the market treats 'graph database' as a synonym for 'agent memory', while ingestion is treated as just another agent skill. Both framings skip the hard part, which is the lifecycle: what gets written, what gets trusted, what gets merged, and what should be forgotten. A database can't answer that. A memory layer has to."

I wrote a separate debrief of Relate itself ([Relate, debriefed](/articles/relate-debriefed.html)). This is about his four questions, because they are the right ones, and we have had to answer every one of them.

## Written {#written}

In our stack, writing to memory is not a database insert. Sources append to lanes: a sender holds a write-only token, can add a sealed message to a vault, and learns nothing at all, not even whether anyone else writes there ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)). A curator agent reads the lanes and turns rows into graph: things, links and claims, every node pointing back at the rows it came from ([the new data lake](/articles/the-new-data-lake.html)). Ingestion is not a skill bolted on; it is a role with a policy, and what it writes is a commit.

## Trusted {#trusted}

Trust is the part a database leaves to you. Every commit names the agent that made it and the person it works for, and is signed where the stakes need it ([a key for every person](/articles/a-key-for-every-person.html)). Every claim carries its evidence: a source, an observation, a statement by a party, or our analysis, marked as which. And nothing reaches readers without a reviewer, a separate agent that checks claims against sources ([the wire as a graph](/articles/the-wire-as-a-graph.html)). Trust is then something you can inspect after the fact, not a property of the store.

## Merged {#merged}

Francois lists git-like graph commits among the missing features. In a vault, they are simply how the store works: graph files are committed, branched and merged like code, every version kept. And merging two domains does not need a shared schema. Each world keeps its own ontology, a regulation, its articles, the words they define, and the worlds are joined by an edge, under a grammar where every edge is a verb ([knowledge that maintains itself](/articles/knowledge-that-maintains-itself.html)). That is the multi-graph he wants, without a migration project.

## Forgotten {#forgotten}

Forgetting is the subtlest of the four, and the one I would push back on gently. In memory for agents, I do not think you should delete; you should stop briefing. Our files are immutable, so a change is a new version, never an edit. A reality file lists only what is true now, and is what an agent reads first. Superseded facts are kept, closed, and left out of the briefing, so an agent gets the slice it needs and the diff since it last looked, not the whole pile. That is also the bitemporal model: the commit history is record time, when we believed it; valid time, when it held in the world, is a field in the fact. Memory degradation, in this shape, is a curator's decision about what the briefing includes, not a loss of history.

## A nudge {#nudge}

So my answer to Francois's last line, that products should decide whether they are a database or a memory, is that the memory and the engine can be separate things. The memory is a versioned, private, distributed store of plain files, with its lifecycle in commits, lanes, signatures and reviewers. The engine is whatever answers this question, and can be thrown away after it: SQLite in WebAssembly today, and, I would argue, Relate tomorrow, which is exactly the right shape for it ([Relate, debriefed](/articles/relate-debriefed.html)). It is a different bill from a graph database's: you pay for the bytes a question reads, not for a server holding the graph.

## What this does not claim {#limits}

- **Not a review of the products Francois lists;** I quote only his post.
- **Our approach is slower at deep traversals** over very large graphs, which is a graph database's home ground.
- **Memory degradation as a curator's choice** is my position, not a feature we have measured.
- **Francois's views are his own.**

## Where this comes from {#sources}

Francois Vanderseypen's LinkedIn post on Relate, read on 17 November 2026, and [relatedb.ai](https://relatedb.ai/). Earlier on this site: [Relate, debriefed](/articles/relate-debriefed.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [the new data lake](/articles/the-new-data-lake.html), [a key for every person](/articles/a-key-for-every-person.html), [the wire as a graph](/articles/the-wire-as-a-graph.html), [knowledge that maintains itself](/articles/knowledge-that-maintains-itself.html).
