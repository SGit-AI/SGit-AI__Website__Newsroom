---
title: The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy
date: 2026-11-20
author: Dinis Cruz
author_url: about/index.html
summary: The X-ray was one of the most spectacular things we built for Web Summit, and it runs in a browser. You type a company's name. An orchestrator sends it to four search agents, Perplexity, OpenAI, Gemini and Claude Haiku with web search, a collector gathers what they find, and a graph grows on screen as the evidence arrives. What comes out is three cards: what the company's AI helpers can reach, what they were asked to do, and the gap between the two, which is where an agent behaviour policy belongs. A model's claim is only a lead: only facts whose sources were read reach the page, each with its link. Thirteen companies were X-rayed on 7 November for about 1.13 dollars in total. Before choosing, the team measured the four search agents on the same questions: Perplexity had 45 of 50 claims confirmed, Haiku 49 of 55, OpenAI 35 of 41, Gemini 16 of 23, and Gemini appeared not to search at all. From 11 November it ran live in the stand's command centre, and from 12 November it could X-ray any company, with Claude Sonnet writing the scenario.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, x-ray, behaviour-policies, web-summit, agents, search, article
status: published
---

!shot wsx-sgit.webp | images/ | The X-ray of our own SGit: what an agent can reach, what it was asked to do, and the gap. | screenshot

## In short {#in-short}

- **Type a company; see its AI helpers' reach, their mandate and the gap.**
- **Four search agents and a collector,** with a graph that grows as evidence arrives.
- **A model's claim is a lead, not a fact:** only read sources reach the page.
- **Thirteen companies for about 1.13 dollars,** searched on 7 November.
- **The four models measured first:** Perplexity and Haiku held up best; Gemini did not search.
- **Live in the browser from 11 November,** any company from 12 November.

## What it does {#what}

At [web-summit.sgit.ai/xray](https://web-summit.sgit.ai/xray/) you type a company's name and press "Show me". The page answers in three cards, one for each of the ideas at the heart of RiskMandate: what the company's AI helpers **can reach**, what they **were asked to do**, and **the gap** between the two. The gap is where an agent behaviour policy belongs ([feature behaviour policies](/articles/feature-behaviour-policies.html)). Under the cards, the use cases it found, the sources, and a button to make a behaviour policy in two minutes.

The screenshot above is the X-ray of our own SGit: an agent that hands over vault keys can reach the keys and who it hands them to; it was asked to seal keys only to the trusted owner; and the gap is that, once delivered, the key sits in plain text. That is exactly the kind of finding a behaviour policy is for.

## How it works {#how}

!shot wsx-start.webp | images/ | The X-ray's start: type a company, or pick one of the thirteen prepared on 7 November. | screenshot

- **Four search agents.** An orchestrator sends the name to Perplexity's sonar, OpenAI with web search, Gemini with web search and Claude Haiku with OpenRouter's web search, all through OpenRouter.
- **A collector** gathers what they find, and the graph grows on screen as the evidence arrives, replayed in the order the agents ran, their timings scaled to a few seconds.
- **A claim is a lead.** The team read the sources; only facts whose sources were read reach the page, each with its link and the date read, and every lead is marked confirmed, not found or unverified.
- **The mandate is an example.** "What they were asked to do" is the team's judgement of what a careful company would allow, not the company's own policy, and the page says so.
- **RiskMandate watches; it does not stop.** It is never in the request path ([the X-ray page](https://web-summit.sgit.ai/xray/)).

From 11 November the X-ray ran live in the stand's command centre, entirely in the browser, calling OpenRouter directly with a disposable key limited by budget, with no server of ours. From 12 November it could X-ray any company, with Claude Sonnet writing a scenario: the mandate, the reach, the gap, with and without a behaviour policy.

## What it cost {#cost}

Thirteen companies were X-rayed on 7 November, from 0.056 to 0.124 dollars each, about 1.13 dollars in all, by the run records in the site's repository. A search costs pennies; the value is in what is read and kept.

## Choosing the models {#models}

Before the stand, the team asked the same question of all four agents about five subjects and checked every claim ([the decision page](https://web-summit.sgit.ai/xray/decide/)):

- **Perplexity:** 45 of 50 claims confirmed, 90%, for about 0.006 dollars a run, with the most sources.
- **Claude Haiku with web search:** 49 of 55, 89%, the most claims that held up, but the slowest, and cut off on the two broad subjects.
- **OpenAI with web search:** 35 of 41, 85%; twice it said RiskMandate "enforces" or alerts in real time, which it does not.
- **Gemini with web search:** 16 of 23, 70%; it appeared not to search the web at all, and four of the links it gave did not exist.

That is the X-ray's own lesson in miniature: what a model says is a lead until someone reads the source.

## What did not get done {#limits}

- **Live results are marked "not reviewed"** and stay on the device that made them.
- **An evidence vault per company,** and most of the further subjects the team proposed, were not done before the stand closed.
- **The companies on the page are the team's examples;** the mandates are the team's judgement, not the companies' policies.

## Where this comes from {#sources}

The X-ray at [web-summit.sgit.ai/xray](https://web-summit.sgit.ai/xray/), its [decision page](https://web-summit.sgit.ai/xray/decide/) and [how it is made](https://web-summit.sgit.ai/xray/how/), and the site's repository, [SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), read on 20 November 2026: its run records in `data/xray`, its versions log and its REALITY file. Related: [the team's operating system](/articles/the-teams-operating-system.html), [feature behaviour policies](/articles/feature-behaviour-policies.html), [a galaxy of agents](/articles/a-galaxy-of-agents.html).
