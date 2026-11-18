---
title: Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: At Web Summit we measured what our agents cost, and the numbers tell one story from two ends. At one end, the swarm: on the night of 11 November, 15 signed requests, each started by a push, ran 216 model calls on four open-weight models through OpenRouter, up to 12 at once, in about ten minutes, for 6.8 cents; the same tokens at a frontier model's list price would have cost about two dollars. At the other end, the newsroom: its accountant agent reported days of 375 to 924 API-equivalent dollars, money we did not spend, because the team runs on a subscription, but a true measure of the work, and on the busiest day 98% of every token was a session re-reading its own history. The storm site said the same: 3.84 billion tokens, 98.7% of them cache reads, against about 2.50 dollars of actual model calls in a day. So the cost of an agent is set less by what it writes than by how long it has been remembering. The lessons: put the repeating work in code and cheap models, check them against each other, keep the frontier model for judgement, and start a fresh session from written notes rather than dragging a long one along. Part ten of the series.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: costs, models, open-weight, agents, tokens, swarm, series, article
status: published
---

!shot pad-collage.webp | images/ | The swarm, one real run at a time; the GitHub flow; the stage; and the storm site's accounts. | collage

## In short {#in-short}

- **The swarm:** 216 model calls on four open-weight models for 6.8 cents.
- **The same tokens on a frontier model:** about two dollars.
- **The newsroom:** days of 375 to 924 API-equivalent dollars.
- **98% of those tokens** were sessions re-reading their own history.
- **Context is the cost.**
- **Starting again is cheaper than remembering.**

This is part ten of the series on what six people and around 250 agents built at Web Summit ([ten days at Web Summit](/articles/ten-days-at-web-summit.html)).

## Two ends of one story {#ends}

We ran two very different kinds of agent work at the summit, and we measured both. The newsroom and the storm site ran on long Claude sessions, conductors and specialists that kept working for hours. The swarm ran small, signed tasks on cheap open-weight models, each one a few calls. Put their numbers side by side and the difference is not ten percent. It is pennies against dollars.

## The swarm {#swarm}

The swarm is "one real run at a time: packets issued here, run by runners on any account, results signed and replayed on the site" ([swarm.promptugal.news](https://swarm.promptugal.news/)). A packet says what to do, what it may reach and what it may spend: one of them, for the storm, gave a mandate to "answer each task's question, checked, on each named model. Nothing else", a grant to read the storm site's data and call one model service, and a budget of at most 12 calls, two cents and five minutes. A push starts a GitHub workflow that checks the packet's signature, runs it within its budget, and commits the signed result with GitHub's provenance attestation. "One run is one commit, one workflow run and one result."

On the night of 11 November it climbed a ladder, step by step. One call cost $0.0002. Four open-weight models at once, $0.0011. Six tasks on four models, 24 loops with the consensus decided in code: 40 calls for 1.1 cents, where the same tokens on Sonnet would have cost 33 cents.

Then the scale run. Between 23:50 and 00:01, 15 requests ran 216 model calls on four open-weight models, DeepSeek, Llama, Mistral and Qwen, up to 12 jobs at once: 539,722 tokens in, 91,248 out, 172 answers valid. The bill: **$0.068**. The same tokens at list price would have cost about ten cents on Haiku, **$1.99** on Sonnet and $3.98 on Opus. Those are what the same tokens would cost, not runs on those models, and the swarm's own reviewer warned not to read them as more than that.

## The newsroom {#newsroom}

!shot pad-cost.webp | images/ | The same work, priced: the swarm's 6.8 cents against the same tokens at frontier list prices, and a newsroom day. | chart

The newsroom's accountant agent kept the books every day, with one rule stated at the top: "Read every dollar here as API-equivalent ... the team runs on a Claude subscription; these figures compare runs and agents at API prices and are not money spent." Its daily closes: $923.72 on 6 November, the busiest; $375.05 on 9 November; $449.70 on 11 November, the storm day. The only real money was the model credit for the open-weight calls.

And the shape of it was the same every day. On 6 November: "Cache reads are 98% of all tokens processed (325 M of 331 M); fresh input is 63 k." The accountant's conclusion: "Context is the cost. About 98% of the tokens were sessions re-reading their own history." The Sonnet workers were the cheap work, three to sixteen dollars a day each; the Opus conductors cost 26 to 104.

## The storm site {#storm}

The storm site's books say it again ([after the storm](/articles/after-the-storm.html)): 3,835,812,875 tokens, 98.7% of them cache reads, against about $2.50 of actual model calls in a day, 8,796 of them. Its journal put it in one sentence: "about 99 in every 100 are an agent reading its own session again. What an agent costs is set less by what it writes than by how long it has been remembering." Its conductor alone read 327 million tokens, 99.4% of them its own history; a fresh conductor session every hour would, it estimated, have used 176 million, 46% less.

## What the cheap models were good for {#good}

Cheap models were not trusted on their own. The storm site's router ran every task on two open-weight models with a frontier model for comparison, and reported agreement, not success: the sources task agreed with the parser 35 times in 35; media summaries 41 in 60; transport summaries 14 in 23. Labelling agreed with ours on 126 of 138 over three runs, "so labelling stays a second reader, not a labeller". And when a model was given too little room, it said so: with 300 output tokens, 3 answers in 32 were valid; with 1,500, 12 in 12.

## The lessons {#lessons}

- **Context is the cost.** An agent's bill is mostly its memory; shorter sessions are cheaper sessions ([spend fewer tokens](/articles/spend-fewer-tokens.html)).
- **Starting again is cheaper than remembering.** The storm site's agents measured a fresh session reading 53% to 84% less per call; and, as its journal says, "a team that writes down what matters, and starts again from that, is not guessing".
- **Code first, cheap models second, the frontier model for judgement.** The consensus was decided in code; the open-weight models were second readers; the expensive model was kept for what needs it.
- **Give every task a budget.** A packet that carries its own limit cannot run away.

## What this does not claim {#limits}

- **API-equivalent dollars are not money spent;** the team ran on subscriptions, and only the open-weight calls were paid.
- **The frontier figures are the same tokens at list price,** not runs on those models.
- **The agents' own session tokens were not measured** in the swarm's figures.

## Where this comes from {#sources}

The swarm repositories, PrompTugal__News__Swarm (README.md, MAP.md, RUNNER.md, the packets and reviews) and PrompTugal__News__Swarm__Runs (runs/summary.json, updated 00:01 UTC on 12 November); the PrompTugal.news accountant's reports of 6 to 16 November and board/budgets.json; the Storm Charles repository's accounts, journal and agents/models/HANDOVER.md; all re-read on 18 November 2026. The live sites: [swarm.promptugal.news](https://swarm.promptugal.news/) and the [storm site's accounts](https://storm-charles.promptugal.news/accounts/). Earlier in the series: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [after the storm](/articles/after-the-storm.html), [spend fewer tokens](/articles/spend-fewer-tokens.html).
