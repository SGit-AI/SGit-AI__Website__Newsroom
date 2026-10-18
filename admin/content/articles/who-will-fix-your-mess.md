---
title: Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: Harvard Business Review published "Turn Vibe-Coded Prototypes Into Tools Your Company Can Actually Use" on 16 October 2026, by José Parra Moyano and Karl Schmedders of IMD, Olivier Laplace of Vi Partners and Benjamin Torben-Nielsen of Roche. Its argument, as its summary and Olivier's post put it: AI has made building software feel almost free, so the prototype is the easy part and turning it into a tool people rely on is the hard part, which they call the deployment gap; nobody in-house knows how an AI-designed tool is built; build where you are different and partner where specialists live the problem. I agree with almost all of it, and I think this site has already answered the question in a set of articles, with Simon Wardley's explorers, villagers and town planners as the frame. The gap is not a place to stop; it is a handover between people with different skills. The prototype is not the mess; it is a better brief than any document. The architecture an agent designed can be known, if the agents leave a record: a mandate, a memory and a graph. Their bonus test is the town planner's accountability by another name. And the answer to "who will fix your mess?" should never depend on one partner: if the code is open, anyone can. I have read the public summary and Olivier's post, not the full article, which is behind a paywall.
version: v0.12.102
license: https://creativecommons.org/licenses/by/4.0/
tags: explorer-coding, vibe-coding, wardley-maps, build-or-buy, deployment-gap, open-source, agents, startups, hbr, article
status: published
---

!shot hb-map.webp | images/ | The points in the HBR article's public summary and in Olivier Laplace's post, on the left, and the article on this site that answers each one, on the right: explorer coding, the citizen developer, knowledge that maintains itself, how cheap it is to undo, the expert founders, software vendors as villagers and the fork next door. | comparison

## In short {#in-short}

- **The diagnosis is right.** The prototype is easy; the tool people rely on every day is hard.
- **The gap is a handover.** From explorers, to villagers who maintain it, to town planners who run it.
- **The prototype is not the mess.** It is a better brief than any document.
- **"Nobody knows how it is built" is fixable.** Make the agents leave a record: a mandate, a memory, a graph.
- **The bonus test is accountability.** Whoever ships it answers for it, as the Linux kernel already says.
- **Build the explorer version; partner for the villagers.** And choose partners whose code you could fix without them.
- **"Who will fix your mess?"** Anyone, if it is open source. That is the answer that does not depend on one partner.

## What they argue {#argument}

Harvard Business Review published [Turn Vibe-Coded Prototypes Into Tools Your Company Can Actually Use](https://hbr.org/2026/10/turn-vibe-coded-prototypes-into-tools-your-company-can-actually-use) on 16 October 2026, by José Parra Moyano and Karl Schmedders, professors at IMD, Olivier Laplace, a partner at Vi Partners, and Benjamin Torben-Nielsen, an AI expert at Roche. It opens: "Generative AI has made building software feel almost free." A product manager describes what she wants, an AI model writes the code, "and a working tool appears in an afternoon, impressing everyone who sees it."

The rest is behind a paywall, so I am working from the public summary and from Olivier's LinkedIn post about it, which sets out the argument in his own words. His opening: "'Build or buy in the age of AI?' Wrong question. The real one is: 'Who will fix your mess?'"

The post makes six points. The prototype is the easy part: "Turning it into a tool people rely on every day is much harder. We call this the #DeploymentGap." A European bank piloted a Swiss AI startup's tool, decided to build its own, had a basic prototype six months later that could not handle "regulation, data management and daily use", and went back to the startup after a year. What the C-level rarely sees when signing the budget, in his words: "the AI designs the architecture, not your team. So nobody in-house knows how the tool is built." A test for any chief executive: "would your team accept a bonus tied to how this tool performs in production? If yes, build. If they hesitate, look for a partner." Build where you are different, for narrow internal tools, or to prototype; partner where specialists live the problem every day. And a specialist works on one problem across many clients: "Every edge case one client hits makes the product better for all the others."

The trend behind it is real. McKinsey's [State of AI in 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) found that 32 percent of respondents had decided against buying at least one software product or feature because they could build it in-house with coding agents.

I agree with almost all of it. What I want to add is that this site has been working on the same question for months, from the other side, and I think the answer is already written down. Here it is, article by article.

## The prototype is not the mess {#brief}

!shot ec-handover.webp | images/ | Explorer coding and the handover that makes it last: explorers build by talking to an agent, and what they build is the brief; villagers maintain it, with policies, data handling and tests; town planners own the code in production. From Explorer coding. | architecture

The word "vibe" is part of the problem. In [Explorer coding](/articles/explorer-coding.html) I proposed a better name for it, from Simon Wardley's explorers, villagers and town planners. What people are doing when they build an app by talking to an agent is exploring, with the fast feedback loop that made spreadsheets win. And what they build is a better brief than any document: what the user actually wants, in a form that runs. [The citizen developer](/articles/the-citizen-developer.html) makes the same case for the people outside IT who are now building: it is the spreadsheet grown up, and spreadsheets ran the world for decades despite their errors.

So I would not start from "who will fix your mess?". The prototype is not a mess. It is the most precise requirement the company has ever had. The mistake is to put it in line, so that other people depend on it, before anyone has done the work that makes software dependable.

## The gap is a handover {#handover}

!shot hb-wardley.webp | images/ | The deployment gap on a Wardley map: the prototype in genesis, built by explorers; the tool people rely on, made reliable by villagers; the platform it runs on, owned by town planners. The gap is the handover from explorer to villager. | architecture

On a Wardley map, the deployment gap has a place. It is the move from genesis to custom built and product, and it is a change of people, not only of code. Explorers are good at finding what is needed. Villagers are good at making it reliable: tests, data handling, releases that do not break it, and now [behaviour policies](https://abp.sgit.ai/what-is-an-abp/index.html) for the agents that work on it. Town planners are good at running it at scale, and they own it in production.

!shot cz-path.webp | images/ | From the spreadsheet to the town planners: the citizen developer's path, from what people built with what they controlled, to the application they need, to the villagers and town planners who make it last. From The citizen developer. | architecture

That is why the bank's story went the way it did. It is not that the internal team was weak, or that building is always wrong. An explorer team was asked to be villagers and town planners as well, on a regulated, data-heavy, daily-use tool, and those are different jobs. The startup had already done the villager and town planner work, many times, for many clients.

## "Nobody knows how it is built" can be fixed {#record}

This is the point in the post I most want to answer, because I think it is the one that most needs to change: "the AI designs the architecture, not your team. So nobody in-house knows how the tool is built." That is true of most agent-built software today. It does not have to be.

!shot kq-loop.webp | images/ | Knowledge that maintains itself: sources kept in their own vocabularies, agents that keep a semantic graph of them up to date, and people and agents briefed from the graph. From Knowledge that maintains itself. | architecture

If the agents work under a written mandate, keep their memory in a versioned store the company owns, and describe what they built as a graph, then the architecture is not a mystery. It is a record the next team can read. [Knowledge that maintains itself](/articles/knowledge-that-maintains-itself.html) is about exactly that: a graph of what an organisation knows, kept up to date by agents and used to brief people and agents. Each article on this site carries one, and you can [read them all as graphs](/articles/graphs.html).

!shot hb-graph.webp | images/ | One article as a graph, as this site publishes it for every article: Explorer coding's twelve nodes, from "vibe coding, the word" to "town planners own it", with the edges between them and the quotes that carry them. A screenshot of the graphs page on newsroom.sgit.ai. | comparison

!shot rf-board.webp | images/ | A prototype that is ready for the villagers: Mondweep Chakravorty's SGit × Ruflo run, twelve steps, five worked, three safeguards refused as intended, recall by meaning marked as not tested. From What if an agent loses its workspace? | comparison

For what a prototype ready for the handover looks like, Mondweep Chakravorty's [SGit × Ruflo proof of concept](/articles/what-if-an-agent-loses-its-workspace.html) is a good example: built with agents, but with its versions pinned, sixteen tests, a folder of evidence, a written behaviour policy, and a README that says plainly what it does not do yet. A villager can pick that up. The pieces after it, [when the vault is actually used](/articles/when-is-the-vault-actually-used.html) and [the path the policy does not guard](/articles/the-policy-guards-the-door.html), are what a villager's first review of it reads like.

## The bonus test is accountability {#bonus}

I like the bonus test a lot: would your team accept a bonus tied to how the tool performs in production? It is the right question, and it has a name in the Wardley frame. It is the moment the town planners take the code and answer for it.

[Explorer coding](/articles/explorer-coding.html#handover) makes the same point from the other end: more of the industry already says that whoever ships code is responsible for it, however it was written. The Linux kernel's rules for AI coding assistants say so. If nobody will put their name, or their bonus, on a tool in production, it is not ready to be in line, whoever wrote it.

## Build where it is cheap to undo {#undo}

!shot cu-spectrum.webp | images/ | The spectrum: across, how much it costs to undo, from a two-way door to a one-way door; up, how mature the controls and the record are, from explorer to town planner. Where an output sits decides how much a person needs to be in the loop. From How cheap is it to undo? | comparison

"Build where you are different, for narrow internal tools, or to prototype what you need." I agree, and I would add the test I use for how far to let something go. In [How cheap is it to undo?](/articles/how-cheap-is-it-to-undo.html), the question is not build or buy, but how much it costs to reverse a mistake and how mature the controls are. A narrow internal tool that a few people use and that can be switched off is a two-way door: build it, explore, learn. A tool that touches regulated data every day is a one-way door until the controls are mature: that is where the villagers have to be in place first, yours or a partner's.

## Partner with the specialist, and the specialist may be the founder {#specialist}

!shot ef-playbooks.webp | images/ | Two playbooks: the outsider who finds a gap, raises first and hires the experts; and the expert who lives the problem and builds it with agents. From The expert founders. | comparison

"Partner where specialists live the problem every day." Yes, and the specialist is changing. In [The expert founders](/articles/the-expert-founders.html) I argued that agents let the people who know a problem best build the product themselves, without the millions that used to come first. That is good news for the buyer: more of the startups worth partnering with will be run by people who have lived the problem, not by outsiders who hired them.

## The specialist should be the villager underneath you {#villagers}

!shot vt-map.webp | images/ | A product as explorers, villagers and town planners: users explore on top, talking to the app and writing the best brief the vendor will get; the vendor maintains the customisations, and runs the platform. From Software vendors should become villagers and town planners. | architecture

"Every edge case one client hits makes the product better for all the others." That is the strongest argument for a partner, and it is also why I think vendors should change what they sell. In [Software vendors should become villagers and town planners](/articles/software-vendors-as-villagers.html) I argued that a software company should stop being the only explorer and let its users explore on top of the product, by talking to it, while it sells them the maintenance of what they built, and learns from every one of them. That keeps the network effect Olivier describes, and it closes the deployment gap from the vendor's side: the client's explorers keep exploring, and the vendor is the villager. [A custom Firefox of my own](/articles/a-custom-firefox-of-my-own.html) is the worked example, for a product I use every day.

## And who will fix your mess? {#fix}

The last point is the one I would change in the question itself. "Who will fix your mess?" should not have a single answer. If the only people who can fix a tool are one partner's engineers, the company has swapped a deployment gap for a dependency.

That is why I keep arguing for open source, all of it. [The value of constraints](/articles/the-value-of-constraints.html) explains what it takes away: the temptation to lock customers in, and the startup curse of building every customer's integration. [The fork next door](/articles/the-fork-next-door.html) explains what it protects: if the partner stops executing, the customer, or another partner, can take the code and carry on. With the code open and the record kept, "who will fix it?" has many answers: your team, the partner, another partner, or the agents, under a mandate, reading the record.

## What this does not claim {#limits}

- **I have not read the full article.** It is behind a paywall; I quote its public summary and Olivier Laplace's post.
- **Not that every company should build.** The post's bank example is a good warning.
- **The record is a proposal, not a standard.** This site runs it; few organisations do yet.
- **I have a stake.** My companies sell open source and the kind of record described here.

If you are one of the authors and would like to discuss it, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 17 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The article: José Parra Moyano, Karl Schmedders, Olivier Laplace and Benjamin Torben-Nielsen, [Turn Vibe-Coded Prototypes Into Tools Your Company Can Actually Use](https://hbr.org/2026/10/turn-vibe-coded-prototypes-into-tools-your-company-can-actually-use), Harvard Business Review, 16 October 2026, read in its public summary and opening; Olivier Laplace's public LinkedIn post about it, quoted from the post. McKinsey, [The State of AI in 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), August 2026. This site: [Explorer coding](/articles/explorer-coding.html), [The citizen developer](/articles/the-citizen-developer.html), [Knowledge that maintains itself](/articles/knowledge-that-maintains-itself.html), [How cheap is it to undo?](/articles/how-cheap-is-it-to-undo.html), [The expert founders](/articles/the-expert-founders.html), [Software vendors should become villagers and town planners](/articles/software-vendors-as-villagers.html), [A custom Firefox of my own](/articles/a-custom-firefox-of-my-own.html), [The value of constraints](/articles/the-value-of-constraints.html), [The fork next door](/articles/the-fork-next-door.html), [What if an agent loses its workspace?](/articles/what-if-an-agent-loses-its-workspace.html), [The SaaS apocalypse will be decided by inertia, not by AI](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html), and [the articles as graphs](/articles/graphs.html).
