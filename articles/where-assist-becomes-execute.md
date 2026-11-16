# Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule, sgit.ai

> Khwaja Naveed, a cybersecurity and AI governance director, asked a precise question under my post about running more than 120 agents at once: how do our behaviour policies handle the line between assisting and executing, when an agent moves from summarising data to changing a system of record, and do we use different policy tiers by level of autonomy? Yes, but we tier by capability, not by agent. In an Agent Behaviour Policy every action is a capability in a small grammar, verb, object and reach, and each has an undo class: undone with no loss, recoverable with effort, or not at all. Assisting sits at the reversible end; executing in a system of record is recoverable only with effort, and sending, publishing and spending cannot be undone. The control tightens along that line: allowed and logged, then signed and reviewable, then plan-then-apply, then drafts only. What matters is what enforces each tier: only a boundary above the agent bounds anything. Our own conductor's policy records the proof: a rule against pushing to main, kept only by the agent, failed once, because the technical boundary was not yet set.

*Source: <https://newsroom.sgit.ai/articles/where-assist-becomes-execute.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule

# Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.2.0, 3 versions](versions/where-assist-becomes-execute.md) · [newsroom v0.14.108](https://newsroom.sgit.ai/admin/versions.html) · abpriskmandateagentsgovernancesecurityautonomyweb-summitarticle

***Abstract:** Khwaja Naveed, a cybersecurity and AI governance director, asked a precise question under my post about running more than 120 agents at once: how do our behaviour policies handle the line between assisting and executing, when an agent moves from summarising data to changing a system of record, and do we use different policy tiers by level of autonomy? Yes, but we tier by capability, not by agent. In an Agent Behaviour Policy every action is a capability in a small grammar, verb, object and reach, and each has an undo class: undone with no loss, recoverable with effort, or not at all. Assisting sits at the reversible end; executing in a system of record is recoverable only with effort, and sending, publishing and spending cannot be undone. The control tightens along that line: allowed and logged, then signed and reviewable, then plan-then-apply, then drafts only. What matters is what enforces each tier: only a boundary above the agent bounds anything. Our own conductor's policy records the proof: a rule against pushing to main, kept only by the agent, failed once, because the technical boundary was not yet set.*

Where assist becomes execute: four tiers by reach and undo class, and the control that tightens at each.

## In short

- **The question:** where is the line between an agent that assists and one that executes, and are there tiers?
- **Yes, tiered by capability, not by agent:** each action has a reach and an undo class.
- **Four tiers:** assist, change its own work, change a system of record, and irreversible actions to the world.
- **The control tightens:** logged, then signed and reviewable, then plan-then-apply, then drafts only.
- **Only a boundary bounds anything:** a rule kept by the agent is not a control.
- **Our own evidence:** a rule against pushing to main failed once, and the policy recorded it.

## The question

Khwaja Naveed's question on LinkedIn, 15 November 2026: the assist-to-execute line, and policy tiers.

Under my post about the visualisations that let us run more than 120 agents at once without losing control of them, Khwaja Naveed, a director of cybersecurity governance, asked a question that goes straight to the heart of it: how do our behaviour policies handle the line from assist to execute, when an agent moves from summarising data to executing changes in a system of record, and do we use different policy tiers based on that level of autonomy?

The short answer is yes. The longer answer is that we tier by what an action can reach and whether it can be undone, rather than by how autonomous an agent is, because the same agent can do both.

## Tier by capability, not by agent

An [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) records what an agent can reach, what it was authorised to do, the gap between them, and what actually stands in the way. Its actions are written in a small grammar, [verb, object and reach](https://abp.sgit.ai/model/capabilities/index.html): 23 capabilities such as `read.message.tenant`, `write.repository.project` or `send.message.world`. Each has an [undo class](https://abp.sgit.ai/model/undo/index.html): **yes**, undone by the same actor with no loss; **with-effort**, recoverable from a backup, a history or a revert, at a cost; and **no**, which cannot be undone.

That gives a natural set of tiers:

1. **Assist.** Read, summarise, search. Nothing changes, though a read cannot be unread, which is why the grammar marks reading mail as undo "no": what an agent has read, it can repeat. Allowed, and logged.
2. **Change its own work.** Write to the project or repository it was pointed at; recoverable with a revert. Allowed, with every change signed and reviewable.
3. **Change a system of record.** Push to a shared repository, change a CRM record, a DNS entry, a release to the live site; recoverable, at a cost. Plan, then apply: a reviewed step, enforced above the agent.
4. **Irreversible, to the world.** Send a message, publish under a name, spend money. Drafts only: a person sends, publishes or pays, or the capability is simply not in reach.

Khwaja's line, from summarising to executing in a system of record, is the line between the second and third tiers.

## What actually stands in the way

Only a boundary above the agent bounds anything; and a rule against pushing to main that failed, recorded.

Tiers on paper are not enough. For every capability, a policy records [what stands in the way](https://abp.sgit.ai/model/barriers/index.html), and there are four kinds: nothing; an expectation, a rule in prose enforced by nobody; a setting the agent's own account can flip; and a boundary enforced above the grant, out of the agent's reach. Only the fourth is a control: "a control bounds a grant only if it is enforced by something the grant does not include."

Our own Web Summit team shows why that matters. The policy of my conductor agent, published with every other agent's on [the team's site](https://web-summit.sgit.ai/abp/), says it must never push to the main branch. On 2 November at 23:06, asked for "a major release via main", it pushed directly instead of opening a pull request. The barrier was an expectation, a rule kept by the agent, and the boundary that would have held, branch protection, was not yet set. The policy recorded the failure, in its own gap section, which is exactly what a policy is for. The lesson is the one the model predicts: move every execute capability into the fourth row.

## Three patterns that held

Across more than a hundred agents, three patterns kept the line where it should be:

- **Drafts only for the irreversible.** PrompTugal.news's outreach desk drafted fifty requests to companies and sent none; each waited for a person. Its rule: an agent never sends an email or posts ([PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md)).
- **Plan, then apply, for systems of record.** Changes to shared systems go through a reviewed step: releases that a gate refuses if a check fails, and, for new infrastructure, a plan on a pull request applied only on merge ([from a commit to a live website](from-a-commit-to-a-live-website.md)).
- **Make the dangerous thing unreachable.** The line from our Swarm demo: don't hope the agent behaves. Most agents simply did not hold the credentials to execute in a system of record; secrets were sealed to the few that needed them ([six setups of an agentic system](six-setups-of-an-agentic-system.md)).

## Approve at altitude

No person can approve every action of more than a hundred agents, and should not try. Tiers are approved once, at the right level: a person signs off what each tier may do and what enforces it, and every action inside that tier inherits the decision ([approve at altitude](approve-at-altitude.md)). The approval moves from the action to the policy.

## Gently, with an escape valve

Our Web Summit policies ran in an explorer phase: they observed, recorded and recommended, and blocked nothing, at my word, so the team could move fast while we learned where the real gaps were. Lock-down comes step by step, each with an escape valve. The conductor's failure is what that phase is for: it showed which rule had to become a boundary first.

## What this does not claim

- **The four tiers are a way of reading the grammar,** not a separate standard; the grammar and its undo classes come from abp.sgit.ai.
- **At Web Summit most barriers were rules, not boundaries,** by design, in an explorer phase; the policies record which.
- **"More than 120 agents at once"** is from my post; our published count is around 250 named agents, with more than 60 sessions working at once at the peak.

## Where this comes from

Khwaja Naveed's comment on my LinkedIn post, 15 November 2026. [abp.sgit.ai](https://abp.sgit.ai/): [the capability grammar](https://abp.sgit.ai/model/capabilities/index.html), [the undo class](https://abp.sgit.ai/model/undo/index.html) and [the barrier](https://abp.sgit.ai/model/barriers/index.html). The Web Summit team's [Agent Behaviour Policies](https://web-summit.sgit.ai/abp/), including [the conductor's](https://web-summit.sgit.ai/abp/conductor-web-summit-dinis/index.html). Earlier on this site: [what can your agent reach?](what-can-your-agent-reach.md), [approve at altitude](approve-at-altitude.md), [six setups of an agentic system](six-setups-of-an-agentic-system.md), [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md), [from a commit to a live website](from-a-commit-to-a-live-website.md).

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#where-assist-becomes-execute)

### Builds on

- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [From a commit to a live website: a site factory where a request file in a commit makes a CI pipeline create the GitHub repository, the DNS record and the sgit vault, seed a page, check HTTPS, run a first pass with Claude Code, and record it all, so an agent can create sites by committing](from-a-commit-to-a-live-website.md) A site factory: a request in a commit makes a CI pipeline create the repository, DNS record and vault, seed a page, check HTTPS and record it all.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.

### Continued by

- [Identity for AI agents, layer by layer: how our agent teams answer every row of Maya Dotan's map of 190 projects, with a key per agent, a name that says who it acts for, and a behaviour policy that sets its limits](identity-for-agents-layer-by-layer.md) How our agent teams answer every row of a map of 190 agent identity projects: names, keys, behaviour policies and a signed record.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 421 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=421)

**Posting this article on LinkedIn?** The cover is [where-assist-becomes-execute.jpg](banners/where-assist-becomes-execute.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-assist-becomes-execute.html)*
