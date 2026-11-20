---
title: The swarm, one real run at a time: the Web Summit demo that showed agents, the loops they start and the model calls they make, run for real, signed and replayed, step by step from one person and one agent to 24 loops at once, 216 model calls for 6.8 cents, the same work under a harness with 3 of 12 risky actions still possible instead of 11, and the Story Studio, where a spoken answer became a deck in front of you
date: 2026-11-20
author: Dinis Cruz
author_url: about/index.html
summary: The Swarm was one of the sections of the stand's command centre at Web Summit, and has its own site, swarm.promptugal.news. Its idea is simple: show agents, the loops they start and the model calls they make, run for real and recorded, so that anyone can see what each was asked to do, what it could reach, and how to close the gap. It climbs one step at a time, from me asking one agent for one task, to one model call, to four models at once, to loops, to a swarm of 24 loops and a consensus in code, each step a real run on the storm site's public data, saved as a file and replayable. Fifteen signed requests became fifteen jobs on GitHub's compute, twelve at once, making 216 model calls on open-weight models for 6.8 cents; the same tokens on Claude Sonnet would have cost 1.99 dollars. Model text is never stored, only its length and hash. Under a harness, the same work produced the same output, while 3 of 12 risky actions remained possible instead of 11. And the Story Studio is the demo I remember most: someone answers a question out loud, the browser transcribes it, and a coordinator builds a deck in front of them, drawing every step of how it was made, with its time and its cost.
version: v0.14.182
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, swarm, agents, behaviour-policies, harness, promptugal, article
status: published
---

!shot swm-home.webp | images/ | The Swarm at swarm.promptugal.news: every run real, signed and replayable; model text never stored. | screenshot

## In short {#in-short}

- **Agents, loops and model calls, run for real and recorded,** at [swarm.promptugal.news](https://swarm.promptugal.news/).
- **One step at a time,** from one person and one agent to 24 loops at once.
- **216 model calls for 6.8 cents** on open-weight models; 1.99 dollars for the same tokens on Sonnet.
- **Model text never stored:** only its length and hash.
- **Under a harness,** 3 of 12 risky actions still possible instead of 11, with the same output.
- **The Story Studio:** a spoken answer becomes a deck in front of you, with how it was made.

## The idea {#idea}

Everything an agent starts runs with the agent's keys: every loop, every model call, every line of code it runs. That is the gap between what an agent was asked to do and what it can reach, the idea at the heart of RiskMandate. The Swarm makes it visible by running agents for real and recording everything: what each was asked to do, what it could actually reach, and how to close the gap. It was one of the sections of the stand's command centre at Web Summit, beside [the Galaxy](/articles/a-galaxy-of-agents.html) and [the X-ray](/articles/the-riskmandate-x-ray.html), and it has its own site.

## One step at a time {#steps}

!shot swm-flow.webp | images/ | The execution flow: 15 signed requests, 15 jobs, 216 model calls, every run replayable. | screenshot

The brief was to start small and go one by one. The workload is real: the storm site refreshes 51 datasets from public sources, and each refresh is a small unit any runner can do. Each step adds one thing, and each step is a real run, saved as one file and replayable on the site ([the map](https://github.com/PrompTugal/PrompTugal__News__Swarm/blob/dev/MAP.md)):

1. **Me, Claude, a task.**
2. **Compute:** read one storm dataset.
3. **One model call,** for 0.02 cents.
4. **Many models:** one question to four open-weight models at once, for 0.11 cents.
5. **Loops:** six storm tasks, each read, asked, checked and retried, for 0.26 cents.
6. **A swarm of loops:** six tasks on four models, 24 loops at once, 40 calls, a consensus per task in code, for 1.1 cents; the same tokens on Sonnet, 33 cents.

The next steps were planned and need credentials: other people's sessions running the same signed packets, then the clouds, then everyone's conductor.

## Signed, budgeted, replayable {#signed}

Work moves through GitHub: a signed request is pushed, a GitHub Action runs it inside a budget written before it starts, and the signed result comes back with an attestation. Fifteen requests went through that way, as fifteen jobs, twelve at the same time, making 216 model calls, 79.6% of them valid, on four open-weight models, about 631,000 tokens, for 6.8 cents; the same tokens on Claude Sonnet would have cost 1.99 dollars. Model text is never stored, only its length and hash, so the record proves what ran without keeping what was said. And every run can be seen six ways, flat, blueprint, heat, neon, orbit and in 3D, with every unit clickable: what it is, what it holds, what it did.

## The harness {#harness}

The Swarm's own agents were then run under SHarness, an early secure harness: the same work, first with no policy, then with one. The output was identical, the same hash. Of twelve risky attempts, reading keys, writing outside the workspace, opening a shell, reaching the network and the rest, eleven succeeded without the harness and three with it: two inside the workspace, which is allowed, and one through the environment the process inherited, which is the gap to close. The findings are published as they are, including what did not hold yet ([the harness findings](https://github.com/PrompTugal/PrompTugal__News__Swarm/blob/dev/harness/SUMMARY.md)).

## The Story Studio {#studio}

!shot swm-studio.webp | images/ | The Story Studio: record an answer, and watch a deck being made from it, with its cost. | screenshot

This is the demo I remember most. At the stand, you ask someone a question and let them answer out loud. The browser records it and sends it to an audio model through OpenRouter to transcribe; a coordinator, Claude Sonnet by default, turns the words into a short deck, using only StoryKit's building blocks, with the person's own words quoted exactly and never polished; and, if asked, it makes infographics too. Beside the deck, the making-of draws itself: every hop, who did it, which model, how long and what it cost, with the day's spend at the top.

It is honest about what it is: the page is marked as a simulation, run in the browser, with real times and costs but no compute of our own and no behaviour policy enforced; the stories made with the full swarm say which of their steps ran under a policy and on GitHub's compute, and which did not. It is the same pattern as [watch your website being built](/articles/watch-your-website-being-built.html), a week earlier, and the reason that page is possible.

## An appliance, before the appliance {#appliance}

One more thing in the Swarm surprised me on rereading: a story from 12 November called "An appliance, not an app", and a summit offer of a tablet set up with the larger packages. The idea behind [the sovereign website appliance](/articles/launching-the-sovereign-website-appliance.html) was already on the stand.

## What this does not claim {#limits}

- **The runs are small,** on public data, and the costs are those recorded on the site.
- **The Studio is a simulation:** real model calls in the browser, no enforcement.
- **The harness is early beta,** and its findings include gaps not yet closed.

## Where this comes from {#sources}

[swarm.promptugal.news](https://swarm.promptugal.news/), read and captured on 20 November 2026, and its repositories, [PrompTugal__News__Swarm](https://github.com/PrompTugal/PrompTugal__News__Swarm) (its map, runs, harness summary and the Studio page) and [PrompTugal__News__Swarm__Runs](https://github.com/PrompTugal/PrompTugal__News__Swarm__Runs). Related: [a galaxy of agents](/articles/a-galaxy-of-agents.html), [the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html), [watch your website being built](/articles/watch-your-website-being-built.html), [launching the sovereign website appliance](/articles/launching-the-sovereign-website-appliance.html).
