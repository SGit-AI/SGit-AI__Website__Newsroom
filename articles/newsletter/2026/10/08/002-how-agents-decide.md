# Issue 2: How agents decide, when they stop, and a local story kept as evidence, SGit Newsroom

> A day of articles on deciding: what a real decision needs, why an agent that can go anywhere has no reason to stop, what happens when every mistake adds a rule, and one customer service agent built three ways to count which rules are only hoped for. Alongside, a live local story, a hospital outage nobody could check from home, kept as evidence while it was happening.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/08/002-how-agents-decide.html> · sgit.ai v0.7.70 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 2

SGit Newsroom · Issue 2 · 2026-10-08

# How agents decide, when they stop, and a local story kept as evidence

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md) · [read it on LinkedIn ↗](https://www.linkedin.com/pulse/how-agents-decide-when-stop-local-story-kept-evidence-dinis-cruz-reune/)

***Abstract:** A day of articles on deciding: what a real decision needs, why an agent that can go anywhere has no reason to stop, what happens when every mistake adds a rule, and one customer service agent built three ways to count which rules are only hoped for. Alongside, a live local story, a hospital outage nobody could check from home, kept as evidence while it was happening.*

What does an agent need to decide well, and what makes it stop? Most of 8 October's articles answer one of those two questions, from the person's side and from the agent's. Alongside them, a live local story, kept as evidence while it was still happening.

The day in six pictures, one from each article

## A decision is more than a yes

[Agency is not a yes](https://newsroom.sgit.ai/articles/agency-is-not-a-yes.html) sets out what anyone asked to decide actually needs, a person or an agent: options beyond yes, context in their own terms, time, somewhere to escalate, authority over the system that produced the request, and incentives that treat a wrong yes and a wrong no alike. The scale it builds has seven levels, the weakest dimension caps the whole decision, and its vault holds the scale. One line from it is worth keeping:

>

Whatever you punish, you teach the other answer.

Inside the agency scale vault: the levels, the decisions scored against them, and the law

## Knowing when to stop

[Knowing when to stop](https://newsroom.sgit.ai/articles/knowing-when-to-stop.html) starts with people, security champions who had automated away whole classes of bug and then debated whether GUIDs were random enough, and comes to agents, who have the same problem by design:

>

An entity that can go anywhere has no natural reason to stop anywhere.

Value rises fast, then flattens. Past the point of diminishing returns, more work is optimising the wrong thing.

[Every mistake added a rule](https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html) is what happens when the answer is more instructions: long sessions, prompts that grow to 100 KB, and each new rule causing the next mistake. The way back it maps is to turn each piece of the process into a small, shipped component:

>

If a session needs 100 KB of rules to be productive, the rules are doing the job that structure should do.

The same process mapped twice: as it runs, and with each piece made a small shipped component

And [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html) gives security a place to stop: name the attacker first, on a six-tier ladder, and draw the line where the attacker is.

>

The question is who, not how much.

Six tiers of attacker, from your own mistakes to elevated threats, with what stops each.

## Hope or enforcement

The day's lead on the site is [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html): one customer service agent, one mandate, built three ways, from a single capable model connected to everything to a team of narrow agents behind a deterministic gateway. Each design gets an Agent Behaviour Policy, and the published vault counts how much of each policy is a boundary and how much is hope:

>

Every design has a policy for every behaviour. The difference is who enforces it.

Inside the vault: the three designs, and one hostile email run through each

[Encrypted memory for agents that run somewhere else](https://newsroom.sgit.ai/articles/encrypted-memory-for-isolated-agents.html) is the infrastructure underneath: five ways to give isolated, short-lived agents a memory that outlives them, with only ciphertext on the server.

The compute is disposable and the memory is not: each run starts from a scoped clone of the vault and ends with a push.

## A local story, kept as evidence

[The waiting room knew first](https://newsroom.sgit.ai/articles/the-waiting-room-knew-first.html) was written on the afternoon it happened. Staff at two London hospitals told patients the IT systems were down; nothing a local person could check before leaving home showed it. The article is about that gap, where local information comes from now, and the evidence behind it is kept in a vault, with care over what it does not claim:

>

Blocked is a limit of our access, never evidence about the hospital.

The local evidence log: the gap, the claims, and where a local could have looked

One correction from the day before: in [the bridge, followed to the end](https://newsroom.sgit.ai/articles/the-bridge-followed-to-the-end.html), the reporter's base salary had been counted as both her income and her cost. Her row now shows pay, salary plus commission, and every other figure is unchanged.

## Everything published on 8 October

Seven articles were published on 2026-10-08, grouped below by what they are about.

### Deciding and stopping

What a decision needs, and what lets a person or an agent stop.

- [**Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source**](../../../../agency-is-not-a-yes.md). A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [**Knowing when to stop: what experience gives people, and what we have to design into agents**](../../../../knowing-when-to-stop.md). Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.
- [**Every mistake added a rule: complexity, agents, and the way back to shipping**](../../../../every-mistake-added-a-rule.md). When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [**Who are you protecting against? Draw the security line where the attacker is, not above it**](../../../../who-are-you-protecting-against.md). Before deciding how secure to be, name the attacker: a six-tier ladder, an air-gapped Mac mini read against it, and eight startups drawing their line.

### Policy that holds

Which rules an agent keeps because it is told, and which because it cannot do otherwise, and the memory that outlives a run.

- [**Hope or enforcement: one customer service agent, three designs, and who keeps each promise**](../../../../hope-or-enforcement.md). One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [**Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes**](../../../../encrypted-memory-for-isolated-agents.md). Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.

### Local, live

A story written while it was happening, with its evidence kept.

- [**The waiting room knew first: a live local story, and the gap where local information used to be**](../../../../the-waiting-room-knew-first.md). Staff at two London hospitals said the IT was down; nothing a local could check showed it. A live local story about where local information comes from now.

*This is issue 2 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [002-how-agents-decide.jpg](../../../../banners/002-how-agents-decide.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. LinkedIn drops images from a paste, so add these where they appear, in this order, with the caption under each:

1. [002-2026-10-08-week.jpg](../../../../banners/collages/002-2026-10-08-week.jpg) The day in six pictures, one from each article
2. [002-2026-10-08-agency-vault.jpg](../../../../banners/collages/002-2026-10-08-agency-vault.jpg) Inside the agency scale vault: the levels, the decisions scored against them, and the law
3. [st-stop.webp](../../../../images/st-stop.webp) Value rises fast, then flattens. Past the point of diminishing returns, more work is optimising the wrong thing.
4. [002-2026-10-08-maps.jpg](../../../../banners/collages/002-2026-10-08-maps.jpg) The same process mapped twice: as it runs, and with each piece made a small shipped component
5. [ts-ladder.webp](../../../../images/ts-ladder.webp) Six tiers of attacker, from your own mistakes to elevated threats, with what stops each.
6. [002-2026-10-08-designs.jpg](../../../../banners/collages/002-2026-10-08-designs.jpg) Inside the vault: the three designs, and one hostile email run through each
7. [dp-run.webp](../../../../images/dp-run.webp) The compute is disposable and the memory is not: each run starts from a scoped clone of the vault and ends with a push.
8. [002-2026-10-08-evidence.jpg](../../../../banners/collages/002-2026-10-08-evidence.jpg) The local evidence log: the gap, the claims, and where a local could have looked

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/08/002-how-agents-decide.html)*
