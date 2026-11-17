# Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle, sgit.ai

> On 11 November Neo4j released Relate, "the ultimate agent-native database" in the words of its CPO: an open-source, embedded, in-memory graph database written in Rust, Apache 2.0, with openCypher, vector and full-text search in one statement, an MCP server, a CLI built for agents, Bolt and HTTP endpoints, a WebAssembly build and clients in seven languages. I wanted to understand it properly, so this is a debrief from its own documentation, which is unusually honest about where it fits: one application, one agent or one tool, on one machine, with the whole graph in memory and one writing process per store; no TLS, one shared credential, no users or roles. Then the comparison I find most interesting, with our own approach, which gives us much of the power of a graph database without running one. Our graphs are JSON files in sgit vaults: encrypted on the device, content addressed, versioned like git, read with one GET per file, written by many writers through append lanes, and queried by loading only the slice a question needs, then throwing a small engine at it. Relate wins where a graph database should: six hops over a big graph in memory, in under a millisecond. We win on encryption, history, many writers, no server between questions, and size bounded by the answer rather than the machine. And the two fit together: Relate is exactly the shape of the throwaway engine in the Transform step of our cycle.

*Source: <https://newsroom.sgit.ai/articles/relate-debriefed.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle

# Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/relate-debriefed.md) · [newsroom v0.14.135](https://newsroom.sgit.ai/admin/versions.html) · graphsdatabasesneo4jagent-memorysgitvaultsknowledge-graphsarticle

***Abstract:** On 11 November Neo4j released Relate, "the ultimate agent-native database" in the words of its CPO: an open-source, embedded, in-memory graph database written in Rust, Apache 2.0, with openCypher, vector and full-text search in one statement, an MCP server, a CLI built for agents, Bolt and HTTP endpoints, a WebAssembly build and clients in seven languages. I wanted to understand it properly, so this is a debrief from its own documentation, which is unusually honest about where it fits: one application, one agent or one tool, on one machine, with the whole graph in memory and one writing process per store; no TLS, one shared credential, no users or roles. Then the comparison I find most interesting, with our own approach, which gives us much of the power of a graph database without running one. Our graphs are JSON files in sgit vaults: encrypted on the device, content addressed, versioned like git, read with one GET per file, written by many writers through append lanes, and queried by loading only the slice a question needs, then throwing a small engine at it. Relate wins where a graph database should: six hops over a big graph in memory, in under a millisecond. We win on encryption, history, many writers, no server between questions, and size bounded by the answer rather than the machine. And the two fit together: Relate is exactly the shape of the throwaway engine in the Transform step of our cycle.*

Relate and our graph-in-a-vault, side by side: where each lives, writers, size, history, security.

## In short

- **Relate is Neo4j's new embedded graph database for agents,** open source, in Rust, released on 11 November.
- **It is well made for its shape:** one process, one machine, the whole graph in memory, Cypher, vectors and MCP.
- **Its own docs say where it does not fit:** many writers, graphs bigger than memory, multi-user security.
- **We keep graphs as JSON files in sgit vaults:** encrypted, versioned, many writers, nothing running between questions.
- **Each wins on its own ground,** and the comparison is a choice of bills, not a winner.
- **They fit together:** Relate as the throwaway engine in our Load, Extract, Transform, Save cycle.

## What Relate is

Relate was announced by Neo4j on 11 November 2026 as an "AI-native, open source, in-memory and in-process embedded database built in Rust for AI Agents and Agentic Systems" ([press release](https://neo4j.com/press-releases/announcing-relate-by-neo4j/)). Its site, [relatedb.ai](https://relatedb.ai/), puts it more simply: "Give your agents an open-source embedded database to keep their data. No signup. No server to deploy."

From the documentation, verified against version 1.0.1:

- **Embedded:** a library inside your application, with clients for Rust, Python, Node.js, Java, Go and Swift, a C ABI, and a WebAssembly build that runs in a browser.
- **Stores:** in memory, a directory, or one `.rl` file, with a write-ahead log; under the default durability mode a crash loses no acknowledged write.
- **Query:** openCypher, which the press release calls fully compliant, and more than 97% of GQL; one statement can combine vector similarity with graph traversal, and there is full-text and hybrid search.
- **Built for agents:** a CLI with JSON envelopes and typed errors with retryable flags, a row cap with an in-band truncation marker to protect an agent's context, a safe mode, an agent skill, and an MCP server exposing `read_cypher`, `get_schema` and `write_cypher`.
- **Servers when you want them:** `relate serve` puts Bolt, the HTTP Query API and MCP in front of one store.
- **Memory patterns as guides:** modelling agent memory as entities, episodes and bi-temporal facts with provenance; storing an ontology spec; and keeping a "diffable memory in the repo", a directory store whose checkpoint writes the whole graph as one readable JSON file you commit to git.

It is clearly well executed, and someone thought hard about agent ergonomics, as Francois Vanderseypen said when he reviewed it ([memory is a lifecycle](memory-is-a-lifecycle.md)).

## Where it fits, in its own words

What I like most is the "Where relate fits" page and a limitations reference that lists every limit with the error it causes. Relate fits "when the graph belongs to one application, one agent or one tool, lives on one machine, and fits in that machine's memory." The rest follows:

- **One writer:** one process at a time opens a persistent store for writing; a second writer is refused.
- **Memory-bound:** the whole graph and its indexes are held in memory, with no paging and no spill to disk.
- **One graph per statement,** in three fixed namespaces; no composite databases.
- **Security:** no served surface has TLS, everything binds to localhost by default, and one Basic-auth credential is shared by every surface, with no users or roles.
- **Testing:** the site says it is tested against the openCypher compatibility kit; the limitations page adds that no current pass count is published.

That is an honest shape: an excellent local engine for one agent, a sandbox, a notebook or a device.

## How we keep graphs

We have been building graphs for months, for this newsroom (every article has one), for regulations, risk toolkits and governance stacks on [graphs.sgit.ai](https://graphs.sgit.ai/), and for agent memory. And we run with no graph database at all.

A graph, for us, is a set of JSON files in an sgit vault: nodes, edges and an ontology per world, joined by a grammar in which every edge is a verb. The vault does the rest. Every file is encrypted on the device; its address is derived from the read key, so reading one item is one GET with no authentication; content-addressed objects never change, so every cache is correct forever; history is git-like, with commits, branches, merges and signed tags; and writes can come from many places through append lanes that never touch a branch or block a read ([how a vault works](how-a-vault-works.md)).

The trick is the question, not the engine. sgit.ai's own measurements, from 21 September, are worth reading in full ([performance, cost and running everywhere](https://sgit.ai/demos/fractal-graphs/performance.html)): on a 1,051-node graph, cloning everything took 65 seconds, but answering one question took one 59 KB file in under half a second; decrypting a megabyte took 0.35 milliseconds, a tenth of parsing its JSON. The rule is a budget: under 100 KB is an answer; gigabytes is a design error.

So in a way we have the power of a graph database without running one. The storage is ordinary object storage, the format is JSON, the engine is JavaScript or Python in whatever process asks, and it scales with the number of questions, not the size of the graph. It does not need to be sgit, but sgit is what gives it encryption, distribution and history.

## Side by side

Where Relate wins, clearly:

- **Traversals:** six hops over a large graph in memory, in under a millisecond. Nothing in our approach competes there, and sgit.ai says so.
- **A real query language:** Cypher, with vector and full-text search in one statement, and drivers for everything.
- **Transactions,** with conflict detection inside one process.
- **Agent ergonomics out of the box:** typed errors, row caps, a skill and an MCP server.

Where our approach wins:

- **Encryption:** the storage provider never sees content, keys or names.
- **Many writers:** people and agents on different machines, through commits, branches and append lanes.
- **History:** every version kept and signed; the "git-like graph commits" Francois asks for are simply how the store works.
- **Nothing running:** no process between questions, no instance hours; you pay for bytes read.
- **Size:** bounded by the answer, not by one machine's memory.
- **Many worlds:** each with its own ontology, joined by an edge, not a migration.

## Better together

Relate as the throwaway engine in LETS: load a slice from the vault, transform it with Relate, save back.

Our cycle is called LETS: Load, Extract, Transform, Save. Load the bytes a question needs from the vault; extract the slice and its ontology; transform it with a throwaway engine built for this one question; save the answer back as new immutable files, shaped for the next question. Today the throwaway engine is SQLite compiled to WebAssembly, an RDF store, or plain in-memory structures.

Relate is exactly the right shape for that Transform step: embedded, in WebAssembly, starting in milliseconds, with Cypher and vector search. Load a slice from a vault into a `:memory:` Relate, ask the six-hop question there, and save the answer back to the vault with its provenance. The vault keeps what a database should not have to: encryption, history and many writers. The database does what it is good at, for as long as the question lasts.

## What this does not claim

- **I have not benchmarked Relate;** this debrief is from its documentation and press release, read on 17 November 2026.
- **Our numbers are sgit.ai's own measurements** of September 2026, on specific vaults.
- **The two do different work;** a fair comparison is about which bill you want, not which is faster.
- **Relate as our Transform engine is a proposal,** not something we have built.

## Where this comes from

Neo4j's [press release](https://neo4j.com/press-releases/announcing-relate-by-neo4j/) of 11 November 2026; [relatedb.ai](https://relatedb.ai/) and its documentation (verified against 1.0.1): "Where relate fits", "Limitations", "Model agent memory", "Keep a diffable memory in the repo" and "Use an ontology", read on 17 November 2026. sgit.ai's [performance, cost and running everywhere](https://sgit.ai/demos/fractal-graphs/performance.html). Earlier on this site: [how a vault works](how-a-vault-works.md), [knowledge that maintains itself](knowledge-that-maintains-itself.md), [the new data lake](the-new-data-lake.md), [memory is a lifecycle](memory-is-a-lifecycle.md).

## Threads

Site & engineeringAgents & policy[This article as a graph →](graphs.md#relate-debriefed)

### Builds on

- [Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database](memory-is-a-lifecycle.md) A reply to Francois Vanderseypen: agent memory is a lifecycle, written, trusted, merged, forgotten, and how we answer each without a graph database.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief](knowledge-that-maintains-itself.md) Fractal semantic graphs for policies and internal knowledge: brief people and agents from the graph, maintain it in a loop, carry the brief in a vault.
- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.

### Continued by

- [Memory is a lifecycle: a reply to Francois Vanderseypen on Neo4j's Relate, agreeing that a graph database is not agent memory, and showing how we answer his four questions, what gets written, trusted, merged and forgotten, with append lanes, signed commits, git-like graph merges and new versions instead of edits, all in encrypted vaults rather than a database](memory-is-a-lifecycle.md) A reply to Francois Vanderseypen: agent memory is a lifecycle, written, trusted, merged, forgotten, and how we answer each without a graph database.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 447 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=447)

**Posting this article on LinkedIn?** The cover is [relate-debriefed.jpg](banners/relate-debriefed.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/relate-debriefed.html)*
