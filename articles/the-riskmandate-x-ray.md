# The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy, sgit.ai

> The X-ray was one of the most spectacular things we built for Web Summit, and it runs in a browser. You type a company's name. An orchestrator sends it to four search agents, Perplexity, OpenAI, Gemini and Claude Haiku with web search, a collector gathers what they find, and a graph grows on screen as the evidence arrives. What comes out is three cards: what the company's AI helpers can reach, what they were asked to do, and the gap between the two, which is where an agent behaviour policy belongs. A model's claim is only a lead: only facts whose sources were read reach the page, each with its link. Thirteen companies were X-rayed on 7 November for about 1.13 dollars in total. Before choosing, the team measured the four search agents on the same questions: Perplexity had 45 of 50 claims confirmed, Haiku 49 of 55, OpenAI 35 of 41, Gemini 16 of 23, and Gemini appeared not to search at all. From 11 November it ran live in the stand's command centre, and from 12 November it could X-ray any company, with Claude Sonnet writing the scenario.

*Source: <https://newsroom.sgit.ai/articles/the-riskmandate-x-ray.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy

# The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-20 · [article v1.0.0](versions/the-riskmandate-x-ray.md) · [newsroom v0.14.181](https://newsroom.sgit.ai/admin/versions.html) · riskmandatex-raybehaviour-policiesweb-summitagentssearcharticle

***Abstract:** The X-ray was one of the most spectacular things we built for Web Summit, and it runs in a browser. You type a company's name. An orchestrator sends it to four search agents, Perplexity, OpenAI, Gemini and Claude Haiku with web search, a collector gathers what they find, and a graph grows on screen as the evidence arrives. What comes out is three cards: what the company's AI helpers can reach, what they were asked to do, and the gap between the two, which is where an agent behaviour policy belongs. A model's claim is only a lead: only facts whose sources were read reach the page, each with its link. Thirteen companies were X-rayed on 7 November for about 1.13 dollars in total. Before choosing, the team measured the four search agents on the same questions: Perplexity had 45 of 50 claims confirmed, Haiku 49 of 55, OpenAI 35 of 41, Gemini 16 of 23, and Gemini appeared not to search at all. From 11 November it ran live in the stand's command centre, and from 12 November it could X-ray any company, with Claude Sonnet writing the scenario.*

The X-ray of our own SGit: what an agent can reach, what it was asked to do, and the gap.

## In short

- **Type a company; see its AI helpers' reach, their mandate and the gap.**
- **Four search agents and a collector,** with a graph that grows as evidence arrives.
- **A model's claim is a lead, not a fact:** only read sources reach the page.
- **Thirteen companies for about 1.13 dollars,** searched on 7 November.
- **The four models measured first:** Perplexity and Haiku held up best; Gemini did not search.
- **Live in the browser from 11 November,** any company from 12 November.

## What it does

At [web-summit.sgit.ai/xray](https://web-summit.sgit.ai/xray/) you type a company's name and press "Show me". The page answers in three cards, one for each of the ideas at the heart of RiskMandate: what the company's AI helpers **can reach**, what they **were asked to do**, and **the gap** between the two. The gap is where an agent behaviour policy belongs ([feature behaviour policies](feature-behaviour-policies.md)). Under the cards, the use cases it found, the sources, and a button to make a behaviour policy in two minutes.

The screenshot above is the X-ray of our own SGit: an agent that hands over vault keys can reach the keys and who it hands them to; it was asked to seal keys only to the trusted owner; and the gap is that, once delivered, the key sits in plain text. That is exactly the kind of finding a behaviour policy is for.

## How it works

The X-ray's start: type a company, or pick one of the thirteen prepared on 7 November.

- **Four search agents.** An orchestrator sends the name to Perplexity's sonar, OpenAI with web search, Gemini with web search and Claude Haiku with OpenRouter's web search, all through OpenRouter.
- **A collector** gathers what they find, and the graph grows on screen as the evidence arrives, replayed in the order the agents ran, their timings scaled to a few seconds.
- **A claim is a lead.** The team read the sources; only facts whose sources were read reach the page, each with its link and the date read, and every lead is marked confirmed, not found or unverified.
- **The mandate is an example.** "What they were asked to do" is the team's judgement of what a careful company would allow, not the company's own policy, and the page says so.
- **RiskMandate watches; it does not stop.** It is never in the request path ([the X-ray page](https://web-summit.sgit.ai/xray/)).

From 11 November the X-ray ran live in the stand's command centre, entirely in the browser, calling OpenRouter directly with a disposable key limited by budget, with no server of ours. From 12 November it could X-ray any company, with Claude Sonnet writing a scenario: the mandate, the reach, the gap, with and without a behaviour policy.

## What it cost

Thirteen companies were X-rayed on 7 November, from 0.056 to 0.124 dollars each, about 1.13 dollars in all, by the run records in the site's repository. A search costs pennies; the value is in what is read and kept.

## Choosing the models

Before the stand, the team asked the same question of all four agents about five subjects and checked every claim ([the decision page](https://web-summit.sgit.ai/xray/decide/)):

- **Perplexity:** 45 of 50 claims confirmed, 90%, for about 0.006 dollars a run, with the most sources.
- **Claude Haiku with web search:** 49 of 55, 89%, the most claims that held up, but the slowest, and cut off on the two broad subjects.
- **OpenAI with web search:** 35 of 41, 85%; twice it said RiskMandate "enforces" or alerts in real time, which it does not.
- **Gemini with web search:** 16 of 23, 70%; it appeared not to search the web at all, and four of the links it gave did not exist.

That is the X-ray's own lesson in miniature: what a model says is a lead until someone reads the source.

## What did not get done

- **Live results are marked "not reviewed"** and stay on the device that made them.
- **An evidence vault per company,** and most of the further subjects the team proposed, were not done before the stand closed.
- **The companies on the page are the team's examples;** the mandates are the team's judgement, not the companies' policies.

## Where this comes from

The X-ray at [web-summit.sgit.ai/xray](https://web-summit.sgit.ai/xray/), its [decision page](https://web-summit.sgit.ai/xray/decide/) and [how it is made](https://web-summit.sgit.ai/xray/how/), and the site's repository, [SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), read on 20 November 2026: its run records in `data/xray`, its versions log and its REALITY file. Related: [the team's operating system](the-teams-operating-system.md), [feature behaviour policies](feature-behaviour-policies.md), [a galaxy of agents](a-galaxy-of-agents.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#the-riskmandate-x-ray)

### Builds on

- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way](a-galaxy-of-agents.md) The Galaxy from Web Summit: the RiskMandate team as a live 3D solar system of people, agents and messages, and the library it became.

### Continued by

- [The way in: why sovereign websites matter so much to RiskMandate, what Web Summit validated and what it showed was missing, something to buy now, how every technology I have been building meets in one product, and why nobody deploys agents they have not touched, seen and been able to stop, so the personal customer becomes the way to the corporate one](the-way-in.md) Why sovereign websites are the way into RiskMandate: something to buy now, where people touch agents under policies before they bring them to work.
- [The swarm, one real run at a time: the Web Summit demo that showed agents, the loops they start and the model calls they make, run for real, signed and replayed, step by step from one person and one agent to 24 loops at once, 216 model calls for 6.8 cents, the same work under a harness with 3 of 12 risky actions still possible instead of 11, and the Story Studio, where a spoken answer became a deck in front of you](the-swarm-one-real-run-at-a-time.md) The Swarm from Web Summit: agents run for real, signed and replayed, 216 model calls for 6.8 cents, a harness test, and a voice-to-deck studio.
- [A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way](a-galaxy-of-agents.md) The Galaxy from Web Summit: the RiskMandate team as a live 3D solar system of people, agents and messages, and the library it became.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 512 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=512)

**Posting this article on LinkedIn?** The cover is [the-riskmandate-x-ray.jpg](banners/the-riskmandate-x-ray.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-riskmandate-x-ray.html)*
