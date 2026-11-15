---
title: Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: There is a business in setting up small agentic teams for companies: a brain for a team, a newsroom, a decision. Very few people know how to do it yet, and it took me months to learn; three months ago I would have bought it myself. We could sell what we run today, but a customer would not see it and could not control it, so the missing piece is a control centre: the place where they see their agents and start and stop them. PrompTugal.news is the natural first customer, because it already needs a network of teams of different sizes: an editor and coordinator, regional newsrooms, desks in each city, journalists and local news agencies. RiskMandate's Agent Behaviour Policies are the same offering on steroids: every policy needs a policy agent and a couple of others to help. The offer can be packaged by size, from £500 for one agent to £20,000 for a network, built from small open pieces: our workflow, Ruflo, sgit vaults, files in git instead of databases, and Claude, Codex or Cloudflare to run them.
version: v0.14.96
license: https://creativecommons.org/licenses/by/4.0/
tags: agentic-teams, business-model, control-centre, promptugal, riskmandate, abp, open-source, pricing, article
status: published
---

!shot mat-ladder.webp | images/ | Four sizes of setup, priced by size, from one agent at £500 to a network at £20,000, each with a control centre. | pricing

## In short {#in-short}

- **The business:** set up small agentic teams for companies, for a team's brain, a newsroom, a decision.
- **Why now:** few people know how, and it took me months; three months ago I would have bought it.
- **The missing piece is a control centre:** customers must see their agents and be able to start and stop them.
- **The first customer is PrompTugal.news:** a network of teams of different sizes, already needed.
- **Agent Behaviour Policies are the same offering on steroids,** focused on controlling agents.
- **Packaged by size,** from £500 to £20,000, built from small open pieces.

## A business in setting up agentic teams {#business}

Over the last weeks the six of us ran around 250 named agents for Web Summit, and before that I ran newsrooms and [a talk built in a day](/articles/the-ultimate-insider-case-study.html) with teams of agents. That is now a lot of experience in one specific skill: setting up a small agentic team that does real work, for a person, a team or a company.

Very few people know how to do that yet, and to be fair, it took me a long time to figure out. Three months ago I would have been very interested in buying exactly this: someone to set up the team, show me how it works, and leave me able to run it. I think there is a business there: providing companies with agentic teams, setting them up, and helping them make decisions with agents ([a brain you arrive at](/articles/a-brain-you-arrive-at.html), [a market for sweets](/articles/a-market-for-sweets.html)).

## The missing piece: a control centre {#control}

We could try to sell what we run today. The problem is that a customer would not see it. They would not have control. To buy an agentic team, you have to be able to see it, and you have to be able to start it and stop it.

So the product is not the agents; it is the ability to control their execution. What a customer buys is an agent control centre that lets the workflow happen: who is running, what each one is doing, what it may reach, and a button that stops it. At Web Summit, each of us had a command centre on our phone, and every agent had its own key and its own lane ([the team's operating system](/articles/the-teams-operating-system.html)); that is the seed of it. Command and control is the subject of my next memo, because I think it is what makes all of this possible.

## PrompTugal as the first customer {#promptugal}

!shot mat-network.webp | images/ | An illustration of PrompTugal.news as a network of agentic teams: an editor, regions, city desks, journalists, agencies. | concept

The best way to build this is with a customer who already needs it, and [PrompTugal.news](/articles/promptugal-news-the-newsroom-we-ran.html) does. It already has a distributed set of agents and people, and as it grows, each of them will need to spin up a team of their own.

Picture it. I am the main editor and coordinator. Team members run regional newsrooms: let's say Vicky Wang runs the one in Lisbon and José Bota the one in the Algarve. Under them come the city desks, one per city, and the desks inside each city, then the journalists, and then the local news agencies, which we should be able to sell to or work with.

Every one of those needs a different agentic team, of a different size. A journalist might need one agent; a city desk a few sessions, one per role; a regional newsroom a conductor and its team; the editor a conductor of conductors ([six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html)). And each team can run in a different place: a Claude session, Codex, something on Cloudflare, or a full workflow across several accounts. The work is then to map those teams, monetise them and run their environments.

## Customers we already have {#customers}

Read backwards, we have already delivered this several times. The first was ruv.sgit.ai, the first time I had an agentic team running on a loop; the second was the book, written by a team of agents the way the talk was built; the third was Web Summit. RiskMandate used the open method for its Agent Behaviour Policies, more a partner than a customer, and PrompTugal.news is the first customer ([an agentic console](/articles/an-agentic-console.html)).

## Agent Behaviour Policies, on steroids {#abp}

RiskMandate's Agent Behaviour Policies are a variation of the same thing. Every Agent Behaviour Policy needs an agent that looks after it, and probably a couple of others to help: one to read what an agent can reach, one to check what it was asked to do, one to show the gap ([what can your agent reach?](/articles/what-can-your-agent-reach.html)).

So between RiskMandate and PrompTugal we can sell these mini agentic teams. The generic offering helps a company run agents for its work; the Agent Behaviour Policy offering is that, on steroids, focused on controlling agents and on helping people see and control what their agents can do.

## Small open pieces {#pieces}

I would not sell this as one big system. I would break it into small pieces: guidance, small open source components, and a path that starts with a single Claude session. The pieces exist:

- **Our workflow:** briefs, a board as files, conductors, hand-overs and releases, as this newsroom runs.
- **Ruflo,** rUv's open-source agent orchestration, which ran the hive behind the talk in [Agentics, ready to sell](/articles/agentics-ready-to-sell.html).
- **sgit vaults,** for everything private, encrypted and versioned.
- **No databases:** files in git, vaults and append-only lanes, which turns out to be ridiculously powerful ([the new data lake](/articles/the-new-data-lake.html)).
- **Runtimes:** Claude, Codex or Cloudflare, chosen per team.

## Packaged by size {#packages}

What a customer buys is a setup, and the price follows its size. A first proposal:

- **£500: one agent.** One agent with sub-agents in one runtime, for one workflow, set up in a session.
- **£1,500: a few sessions.** One session per role, each its own runtime, sharing lanes and a vault.
- **£5,000: a team.** A conductor and its agents, a key per agent, a board as files, and a week of setting up.
- **£20,000: a network.** Conductors of conductors across a division or a network, with policies and observability.

Every size comes with the control centre. The same ladder has appeared before, on [ruv.sgit.ai's offers](/articles/agentics-ready-to-sell.html) and in the finite packs of [villager services for explorer coders](/articles/villager-services-for-explorer-coders.html), and it follows [decide, then buy](/articles/decide-then-buy.html): the method stays open, and what we sell is the setup, the time and the trust.

## What to call it {#name}

What do you call a company that sells this? I have not chosen yet. It sets up agentic teams the way an outfitter equips an expedition, or a studio sets up a production: candidates are an agentic team outfitter, a team foundry, or simply agent crews, set up for you. The name matters less than the examples, and those we already have.

## What this does not claim {#limits}

- **The prices are a first proposal,** not published offers.
- **The PrompTugal network is an illustration:** the regions, desks, agencies and who runs what show the shape, not a plan anyone has announced.
- **The names are candidates,** not a company.

## Where this comes from {#sources}

My own thinking, 15 November 2026, after the conversations behind [a brain you arrive at](/articles/a-brain-you-arrive-at.html) and [a market for sweets](/articles/a-market-for-sweets.html). Earlier on this site: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [the team's operating system](/articles/the-teams-operating-system.html), [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [Agentics, ready to sell](/articles/agentics-ready-to-sell.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html), [decide, then buy](/articles/decide-then-buy.html), and the companion article, [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html).
