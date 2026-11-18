# Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all, sgit.ai

> The companion to stop copying and pasting between your agents is about cost. People running agentic teams often find the token bill grows faster than the work, and most of it is a design choice, not a law of nature. From our own runs, the levers are clear. Keep state in files, so each run starts from a short read rather than a long conversation: the Storm Charles site handed roles to fresh sessions 106 times, because starting again is cheaper than remembering. Cache what repeats: 98.7% of that site's 3.84 billion tokens were cache reads. Use plain code where you can and a model only where judgement is needed: in our Swarm demo a code step took 398 milliseconds and a single model call cost a fiftieth of a cent. Use the right model for each step: a storm-scale Swarm run cost 0.068 dollars on open models against 1.99 dollars on Sonnet. Stop pasting long context between sessions. Build static outputs, which cost nothing to read. And count it: our newsroom's accountant agent read every role's cost every three hours. Setting up workflows like this is part of what AgentiCCells sells.

*Source: <https://newsroom.sgit.ai/articles/spend-fewer-tokens.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all

# Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/spend-fewer-tokens.md) · [newsroom v0.14.102](https://newsroom.sgit.ai/admin/versions.html) · agentstokenscostworkflowscachingmodelsagenticcellsarticle

***Abstract:** The companion to stop copying and pasting between your agents is about cost. People running agentic teams often find the token bill grows faster than the work, and most of it is a design choice, not a law of nature. From our own runs, the levers are clear. Keep state in files, so each run starts from a short read rather than a long conversation: the Storm Charles site handed roles to fresh sessions 106 times, because starting again is cheaper than remembering. Cache what repeats: 98.7% of that site's 3.84 billion tokens were cache reads. Use plain code where you can and a model only where judgement is needed: in our Swarm demo a code step took 398 milliseconds and a single model call cost a fiftieth of a cent. Use the right model for each step: a storm-scale Swarm run cost 0.068 dollars on open models against 1.99 dollars on Sonnet. Stop pasting long context between sessions. Build static outputs, which cost nothing to read. And count it: our newsroom's accountant agent read every role's cost every three hours. Setting up workflows like this is part of what AgentiCCells sells.*

Where an agentic team's tokens go and how to spend fewer, each lever with the evidence from our own runs.

## In short

- **An agentic team's token bill is mostly a design choice.**
- **Files as memory and caching** do the most: 98.7% of one site's 3.84 billion tokens were cache reads.
- **Code where you can, models where you must,** and the right model for each step.
- **Stop copying and pasting long context** between sessions.
- **Static outputs cost nothing to read,** and an accountant agent makes the cost visible.
- **Setting this up** is part of what AgentiCCells sells.

## The bill is a design choice

In [stop copying and pasting between your agents](stop-copying-and-pasting-between-your-agents.md) the problem was a person's time. This one is about the other cost: tokens. Teams that start running several agents often see the bill grow faster than the work, and assume that is what agents cost. Most of it is design. Here are the levers we have used, each with the evidence from our own runs. Dollar figures are API-equivalent: what the tokens would cost at standard prices, since we run on flat subscriptions.

## Files as memory

A long conversation is an expensive memory: every turn re-reads everything before it. We keep state in files instead, the board, the briefs, the reality file, hand-over notes, so each run starts from a short read. When a session grows long, it writes a hand-over and a fresh session takes over. On the Storm Charles site that happened 106 times, across 147 session keys, because starting again is cheaper than remembering ([Storm Charles](storm-charles-a-newsroom-built-in-a-night.md)).

## Cache what repeats

Every run starts with the same rules and briefs. Kept stable and at the front, they are served from the cache rather than paid for again: 98.7% of the Storm Charles site's 3.84 billion tokens were cache reads. Anthropic's own guidance for always-on agents makes the same point ([always-on agents at team scale](always-on-agents-at-team-scale.md)).

## Code, not models, where you can

Not every step needs a model. In the altitudes we mapped for the Swarm demo, A0 is plain code and A1 is a single model call ([six setups of an agentic system](six-setups-of-an-agentic-system.md)). Reading a storm dataset in code took 398 milliseconds; a single model call on an open model cost about 0.0002 dollars. The rule: write code for what repeats and use a model only where judgement is needed. Over time, agents can turn their own repeated steps into code.

## The right model for each step

Frontier models are for judgement; loops of simple checks do not need them. In the Swarm demo, a storm-scale run on open models through a model router cost 0.068 dollars, against 1.99 dollars for the same tokens on Sonnet. A team that picks the model per step, small for loops and frontier for decisions, spends a fraction of one that uses the best model for everything.

## No copy and paste

Pasting long context from one session to another pays for the same tokens again and again, and each session reads far more than it needs. Agents that pass work through lanes and files send only what is needed, with a pointer to the rest; one message to a conductor reached every team at Web Summit without anyone re-reading the whole thread.

## Static outputs

Every site we build is static: built once by the agents, served as files. Readers cost no tokens at all. Where a model is needed at reading time, it is a deliberate feature, not the default.

## Count it

What is not measured grows. PrompTugal.news had an accountant agent that read every role's cost every three hours and kept a budget per role; its busiest day closed at 924 API-equivalent dollars, and most days after that between 300 and 500 ([PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md)). Knowing which role was expensive is how you know which lever to pull.

## What we sell

Setting up an agentic team with these workflows, files as memory, stable rules for caching, code for what repeats, a model per step, lanes instead of pasting, static outputs and an accountant, is part of what [AgentiCCells](atomic-cells-end-to-end.md) sells. The same setup that saves a person's time also saves the tokens.

## What this does not claim

- **The figures are from our own runs,** in October and November 2026, and other workloads will differ.
- **Dollar figures are API-equivalent,** not money we spent.
- **The Swarm comparison** prices the same tokens at list prices, from the run's own records.

## Where this comes from

Our runs: the Storm Charles site's accounts and agents, the Swarm demo's run records, and PrompTugal.news's accountant reports. Earlier on this site: [stop copying and pasting between your agents](stop-copying-and-pasting-between-your-agents.md), [six setups of an agentic system](six-setups-of-an-agentic-system.md), [always-on agents at team scale](always-on-agents-at-team-scale.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#spend-fewer-tokens)

### Builds on

- [Stop copying and pasting between your agents: if you are the wire between your AI sessions you are the bottleneck, and the fix is agents that talk to each other through channels that keep a record, structure that scales your decisions, and outputs you read instead of everything](stop-copying-and-pasting-between-your-agents.md) If you copy and paste between AI sessions, you are the wire, and the bottleneck. Let agents talk through recorded channels; read outputs, not everything.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder](atomic-cells-end-to-end.md) AgentiCCells' first offering: a £500 website as an atomic cell, steered by the customer from their browser with a key, handed over to their GitHub.

### Continued by

- [From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them](from-a-feed-to-meaning.md) What the Storm Charles site did with public data that our data site does not yet, and three hourly source sites to show it.
- [Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in](newsrooms-on-open-data.md) Turning PrompTugal.news's public data feeds into one data site, then small focused newsrooms on top, each run by an agentic team.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 416 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=416)

**Posting this article on LinkedIn?** The cover is [spend-fewer-tokens.jpg](banners/spend-fewer-tokens.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/spend-fewer-tokens.html)*
