---
title: Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: The companion to stop copying and pasting between your agents is about cost. People running agentic teams often find the token bill grows faster than the work, and most of it is a design choice, not a law of nature. From our own runs, the levers are clear. Keep state in files, so each run starts from a short read rather than a long conversation: the Storm Charles site handed roles to fresh sessions 106 times, because starting again is cheaper than remembering. Cache what repeats: 98.7% of that site's 3.84 billion tokens were cache reads. Use plain code where you can and a model only where judgement is needed: in our Swarm demo a code step took 398 milliseconds and a single model call cost a fiftieth of a cent. Use the right model for each step: a storm-scale Swarm run cost 0.068 dollars on open models against 1.99 dollars on Sonnet. Stop pasting long context between sessions. Build static outputs, which cost nothing to read. And count it: our newsroom's accountant agent read every role's cost every three hours. Setting up workflows like this is part of what AgentiCCells sells.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, tokens, cost, workflows, caching, models, agenticcells, article
status: published
---

!shot tok-levers.webp | images/ | Where an agentic team's tokens go and how to spend fewer, each lever with the evidence from our own runs. | infographic

## In short {#in-short}

- **An agentic team's token bill is mostly a design choice.**
- **Files as memory and caching** do the most: 98.7% of one site's 3.84 billion tokens were cache reads.
- **Code where you can, models where you must,** and the right model for each step.
- **Stop copying and pasting long context** between sessions.
- **Static outputs cost nothing to read,** and an accountant agent makes the cost visible.
- **Setting this up** is part of what AgentiCCells sells.

## The bill is a design choice {#design}

In [stop copying and pasting between your agents](/articles/stop-copying-and-pasting-between-your-agents.html) the problem was a person's time. This one is about the other cost: tokens. Teams that start running several agents often see the bill grow faster than the work, and assume that is what agents cost. Most of it is design. Here are the levers we have used, each with the evidence from our own runs. Dollar figures are API-equivalent: what the tokens would cost at standard prices, since we run on flat subscriptions.

## Files as memory {#files}

A long conversation is an expensive memory: every turn re-reads everything before it. We keep state in files instead, the board, the briefs, the reality file, hand-over notes, so each run starts from a short read. When a session grows long, it writes a hand-over and a fresh session takes over. On the Storm Charles site that happened 106 times, across 147 session keys, because starting again is cheaper than remembering ([Storm Charles](/articles/storm-charles-a-newsroom-built-in-a-night.html)).

## Cache what repeats {#cache}

Every run starts with the same rules and briefs. Kept stable and at the front, they are served from the cache rather than paid for again: 98.7% of the Storm Charles site's 3.84 billion tokens were cache reads. Anthropic's own guidance for always-on agents makes the same point ([always-on agents at team scale](/articles/always-on-agents-at-team-scale.html)).

## Code, not models, where you can {#code}

Not every step needs a model. In the altitudes we mapped for the Swarm demo, A0 is plain code and A1 is a single model call ([six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html)). Reading a storm dataset in code took 398 milliseconds; a single model call on an open model cost about 0.0002 dollars. The rule: write code for what repeats and use a model only where judgement is needed. Over time, agents can turn their own repeated steps into code.

## The right model for each step {#models}

Frontier models are for judgement; loops of simple checks do not need them. In the Swarm demo, a storm-scale run on open models through a model router cost 0.068 dollars, against 1.99 dollars for the same tokens on Sonnet. A team that picks the model per step, small for loops and frontier for decisions, spends a fraction of one that uses the best model for everything.

## No copy and paste {#paste}

Pasting long context from one session to another pays for the same tokens again and again, and each session reads far more than it needs. Agents that pass work through lanes and files send only what is needed, with a pointer to the rest; one message to a conductor reached every team at Web Summit without anyone re-reading the whole thread.

## Static outputs {#static}

Every site we build is static: built once by the agents, served as files. Readers cost no tokens at all. Where a model is needed at reading time, it is a deliberate feature, not the default.

## Count it {#count}

What is not measured grows. PrompTugal.news had an accountant agent that read every role's cost every three hours and kept a budget per role; its busiest day closed at 924 API-equivalent dollars, and most days after that between 300 and 500 ([PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html)). Knowing which role was expensive is how you know which lever to pull.

## What we sell {#sell}

Setting up an agentic team with these workflows, files as memory, stable rules for caching, code for what repeats, a model per step, lanes instead of pasting, static outputs and an accountant, is part of what [AgentiCCells](/articles/atomic-cells-end-to-end.html) sells. The same setup that saves a person's time also saves the tokens.

## What this does not claim {#limits}

- **The figures are from our own runs,** in October and November 2026, and other workloads will differ.
- **Dollar figures are API-equivalent,** not money we spent.
- **The Swarm comparison** prices the same tokens at list prices, from the run's own records.

## Where this comes from {#sources}

Our runs: the Storm Charles site's accounts and agents, the Swarm demo's run records, and PrompTugal.news's accountant reports. Earlier on this site: [stop copying and pasting between your agents](/articles/stop-copying-and-pasting-between-your-agents.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html), [always-on agents at team scale](/articles/always-on-agents-at-team-scale.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html).
