---
title: The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: What we have now is a ridiculously powerful workflow, and it runs across what are really several companies. SGit, encrypted vaults and lanes, is one foundation; SHarness, kernel-enforced Process Behaviour Policies, is another; a key for every person and agent is the third. On top sit Agent Behaviour Policies, the standard that underpins all of it, housed at RiskMandate for now. RiskMandate sells those policies. And AgentiCCells sells agentic teams built on all of it, which is what was missing: RiskMandate had a strong idea and a hard first step, because people asked how to start, and a £500 cell is a way to start. With the site factory, the last manual piece, creating repositories and making DNS and AWS changes, is now a commit, so delivery can scale. Above them are the customers and uses: PrompTugal.news going local town by town, the Web Summit team, the sites the factory makes, five apps, VoiceDebrief, and this newsroom. Money is not changing hands between them, but each uses the others, and that is real usage I can point to. So every site should now sell something on the same ladder of one-off prices, £500, £1,500, £5,000 and £20,000, show its examples, link to the others and to the content here, and say where it sits in the stack. This is the map, and the plan to align them.
version: v0.14.117
license: https://creativecommons.org/licenses/by/4.0/
tags: strategy, sgit, sharness, abp, riskmandate, agenticcells, promptugal, voicedebrief, positioning, article
status: published
---

!shot int-stack.webp | images/ | One stack, several companies: foundations, the ABP standard, RiskMandate, AgentiCCells, and the customers and uses. | architecture

## In short {#in-short}

- **A powerful workflow, across several companies:** SGit, SHarness and PKI underneath; Agent Behaviour Policies as the standard; RiskMandate and AgentiCCells on top.
- **AgentiCCells is the missing first step:** a fixed-price cell, using RiskMandate's policies and SGit's vaults, is how a customer starts.
- **The factory removed the last manual piece:** repositories, DNS and cloud changes are now a commit.
- **Real usage, cross-referenced:** PrompTugal.news, the Web Summit team, the factory's sites, five apps, VoiceDebrief and this newsroom each use the layers below.
- **One ladder on every site:** £500, £1,500, £5,000 and £20,000, each company selling its own thing at each step.
- **Next:** align every site to the same pattern, and give SHarness its first showcase.

## Why now {#why}

Until a few weeks ago, these were ideas with demos. Now we have real customers, real usage and real examples. Six of us, with around 250 agents, ran a team operating system, a newsroom, a storm site, a fringe guide and native apps around Web Summit, all on this stack ([ten days at Web Summit](/articles/ten-days-at-web-summit.html)). PrompTugal.news has gone local, with an agent for every town in the Algarve ([every story has an address](/articles/every-story-has-an-address.html)). And last night the AgentiCCells site factory made a website from a commit in two and a half minutes ([the site factory works](/articles/the-site-factory-works.html)), which removed one of the last pieces that was still manual and painful.

What that shows is an intersection: a set of companies that each do one thing, and that, together, go end to end. It is time to map it, and to make every site say so.

## The foundations {#foundations}

- **[SGit](https://sgit.ai/):** git for encrypted vaults. A vault is a unit of work, data, app, history and sources, versioned and handed over with a single read key; lanes in a vault are how our agents message each other with a record. It sits under almost everything here.
- **[SHarness](https://sharness.ai/):** a Process Behaviour Policy for every process an AI agent starts, what it may read, write, run and connect to, enforced by the Linux kernel. It is the boundary layer: the kind of control that holds because the agent cannot reach it.
- **PKI:** a key for every person and every agent, made in the browser or the session, with the public half in a registry ([a key for every person](/articles/a-key-for-every-person.html)). It is how we know who did what, and who it was for ([identity for agents, layer by layer](/articles/identity-for-agents-layer-by-layer.html)).

## The standard: Agent Behaviour Policies {#abp}

[Agent Behaviour Policies](https://abp.sgit.ai/) are the underpinning of all of this: for one agent, the grant (what it can reach), the mandate (what it was asked to do), the gap between them, and the barrier that actually stands in the way. The Web Summit team published policies for its agents, PrompTugal.news keeps 45 roles in one policy file, and the same grammar now describes a CI pipeline ([CI behaviour policies](/articles/ci-behaviour-policies.html)). For now the standard is housed at RiskMandate; its open home will come later, with the open security community.

## RiskMandate, and what it was missing {#riskmandate}

[RiskMandate](https://riskmandate.ai/) sells Agent Behaviour Policies for real agents: from a downloaded pack at £10 to a policy corrected for your situation at £500, and two sessions with a professional's signature at £1,500. Its use case is the summit: the team's agents, the stand, and the film ([know the reach](/articles/know-the-reach.html)).

What it was missing was a sale that is easy to start. A policy is valuable, but people asked: how do I start? What do I do on day one? That is the gap AgentiCCells fills.

## AgentiCCells: the first step {#agenticcells}

[AgentiCCells](https://agenticcells.ai/) sets up small teams of AI agents, in the customer's accounts or ours, as fixed-price cells: one agent or a website at £500, a few sessions handed over at £1,500, a team with a conductor, keys and a board at £5,000, and a network of teams at £20,000 ([six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html)). Every cell runs on SGit's vaults and lanes, gives each agent a key, and puts each agent under a behaviour policy: AgentiCCells uses RiskMandate, and sells it, as part of something a customer can buy today. With the site factory, delivery is now a commit away ([atomic cells, end to end](/articles/atomic-cells-end-to-end.html)).

## The customers and uses {#uses}

!shot int-uses.webp | images/ | Who uses whom, with evidence: each tick is something in a repository or on a live site. | table

- **PrompTugal.news** is the customer that uses everything: vault lanes, agent and person keys, behaviour policies for 45 roles, and the AgentiCCells way of running agentic teams, now one agent per town ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)).
- **The Web Summit team** ran on vaults, lanes, keys and published policies, and RiskMandate was its use case ([the team's operating system](/articles/the-teams-operating-system.html)).
- **The sites the factory makes,** starting with RiskMandate at Web Summit and my brother's site: AgentiCCells customers, in practice if not yet in money.
- **Five apps:** the PrompTugal news app, the Team app, the RiskMandate app on iPad and an Android tablet, the Lisbon Tech Fringe guide, and VoiceDebrief ([native apps by agents](/articles/native-apps-by-agents.html)).
- **VoiceDebrief** deserves its own line. With the new iPhone and iPad app, a voice note becomes a transcript and a debrief on the device, kept in a vault the user owns. It is now genuinely usable, and it adds a lot of value: a product of its own, built on SGit.
- **This newsroom:** media and demo vaults, every release signed by a writer key, and more than 420 articles that explain every piece of this. Every site should use them.

Money is not changing hands between these companies, but each uses the others for real, and that is evidence a customer can check.

## One ladder on every site {#ladder}

!shot int-ladder.webp | images/ | One ladder on every site: £500, £1,500, £5,000 and £20,000, each company selling its own thing at each step. | comparison

Every site should have something for sale, and the pattern is the same: £500 for one workflow, done in a session; £1,500 for two sessions and a handover; £5,000 for a few days and a team; £20,000 for a bespoke engagement. Each company sells its own thing at each step: a cell, a policy, a vault, a process policy, a set of debriefs, a town page. AgentiCCells and RiskMandate already show prices; the others are proposals in the figure.

## Separate companies, one map {#companies}

I see each of these as a separate company, with its own investment, its own flows and its own go-to-market:

- **SGit** sells to developers and teams who share data with agents and with each other.
- **SHarness** sells to platform and security engineers who need a boundary agents cannot cross.
- **RiskMandate** sells to the people who answer for agents: the CISO, the CTO, the board, and the consultants who advise them.
- **AgentiCCells** sells to small teams and businesses that want agentic teams set up, seen and stoppable, starting with a website.
- **VoiceDebrief** sells to professionals and teams who meet, talk and need the record.
- **PrompTugal.news** serves readers and local businesses, town by town, and shows what all of the above can do.

## The plan: align every site {#plan}

Each site should carry the same few things, in its own words:

1. **One line on what it is,** and where it sits in the stack, with the stack figure and its own layer highlighted.
2. **The ladder,** with what it sells at each step, and a way to buy or start.
3. **Real examples and customers,** with links: the summit, PrompTugal.news, the factory's sites, the apps.
4. **Links to the others,** above and below it in the stack.
5. **Links to the newsroom's articles** that explain it.
6. **A contact and an outreach path,** so a reader who arrives on one site can find the one that fits.

And one gap to close: SHarness has no user in the map yet. It is the foundation with the most to show, and the next showcase should be a team of agents whose processes run under it.

## What this does not claim {#limits}

- **No money has changed hands between these companies;** the uses are real, the transactions are not.
- **Only AgentiCCells and RiskMandate show prices today,** and AgentiCCells calls its prices first proposals; the rest of the ladder is a proposal.
- **The ticks are only what I could evidence** on 16 November 2026; an empty cell is not a no.
- **"Separate companies" is how I think about them;** their legal structure is not described here.

## Where this comes from {#sources}

My own thinking, 16 November 2026. The live sites: [sgit.ai](https://sgit.ai/), [sharness.ai](https://sharness.ai/), [abp.sgit.ai](https://abp.sgit.ai/), [riskmandate.ai](https://riskmandate.ai/), [agenticcells.ai](https://agenticcells.ai/), [promptugal.news](https://promptugal.news/), [voicedebrief.ai](https://voicedebrief.ai/) and [its iOS app](https://ios.app.voicedebrief.ai/), read on 16 November 2026; the PrompTugal.news, AgentiCCells and PrompTugal iOS repositories. Earlier on this site: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [the site factory works](/articles/the-site-factory-works.html), [CI behaviour policies](/articles/ci-behaviour-policies.html), [every story has an address](/articles/every-story-has-an-address.html), [identity for agents, layer by layer](/articles/identity-for-agents-layer-by-layer.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html), [atomic cells, end to end](/articles/atomic-cells-end-to-end.html), [native apps by agents](/articles/native-apps-by-agents.html), [know the reach](/articles/know-the-reach.html).
