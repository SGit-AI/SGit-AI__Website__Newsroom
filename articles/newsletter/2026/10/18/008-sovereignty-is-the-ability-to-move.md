# Issue 8: Sovereignty is the ability to move: take away the dot, move the cloud and not the code, and focus on the place of highest leverage, SGit Newsroom

> What does sovereignty mean in practice, for a company, for a small country and for one person choosing what to work on? Seven articles from 12 October, most of them written around a day at a sovereignty event, with Wardley maps underneath. Sovereignty is the ability to move: take each dot you do not control off the map, follow the blast radius, and keep a twin that works for the minimum viable company, tested in QA. Workloads do not move because moving means changing code, so the code must not know, and the reason to move is never sovereignty but value that lands the day you switch. A small country should not enter the race for GPUs; it should build the plumbing, open source, like a road. Open source is a copyright licence whose point is that nobody can lock you in. And the maps themselves: how to read one, where the market is, and how the same rule, the place of highest leverage, chose the work of the week that made all of this possible.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/18/008-sovereignty-is-the-ability-to-move.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 8

SGit Newsroom · Issue 8 · 2026-10-18

# Sovereignty is the ability to move: take away the dot, move the cloud and not the code, and focus on the place of highest leverage

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** What does sovereignty mean in practice, for a company, for a small country and for one person choosing what to work on? Seven articles from 12 October, most of them written around a day at a sovereignty event, with Wardley maps underneath. Sovereignty is the ability to move: take each dot you do not control off the map, follow the blast radius, and keep a twin that works for the minimum viable company, tested in QA. Workloads do not move because moving means changing code, so the code must not know, and the reason to move is never sovereignty but value that lands the day you switch. A small country should not enter the race for GPUs; it should build the plumbing, open source, like a road. Open source is a copyright licence whose point is that nobody can lock you in. And the maps themselves: how to read one, where the market is, and how the same rule, the place of highest leverage, chose the work of the week that made all of this possible.*

What does sovereignty mean in practice? On 12 October I spent the day at a digital sovereignty event, and most of the conversation was about things Europe does not control and will not control soon: frontier models, giant data centres, GPUs. These seven articles, written that day and the next, argue for the other end of the map, and they use the same tool throughout, the Wardley map, to say where to stand. It follows [issue 7, who answers for an agent](https://newsroom.sgit.ai/articles/newsletter/2026/10/18/007-who-answers-for-an-agent.html).

Sovereignty is the ability to move, in six pictures, one from each of six of the articles

## Take away the dot

[Sovereignty is the ability to move](https://newsroom.sgit.ai/articles/sovereignty-is-the-ability-to-move.html) starts on a padel court. A good player always seems to have time, because they read the ball and move to where it will be; frontier models and GPUs are where the ball is today. Where it is going is the ability to move a workload when you decide, and very few companies can, because everything was clicked into existence and never deployed twice. The test is a Wardley map and one question: take away the dot, what happens? The fix is not an alternative as good as today, which is why most efforts never start. It is a twin that works for the minimum viable company, run in QA every week:

>

The bar should be: it works.

A maturity model for every dot you do not control, from "it stops" to "it moves when you decide", each level real only if it was tested.

## The code must not know

[Move the cloud, not the code](https://newsroom.sgit.ai/articles/move-the-cloud-not-the-code.html) comes from a conversation at the same event with the chief executive of an infrastructure company with a large footprint in Romania. What stops workloads moving is not policy or price but code: every call to S3, EC2 and IAM is written into applications nobody wants to touch. So the application must not know it has moved; its calls land on a twin, an open source service the client cannot tell from the real one. The S3 twin exists; the others do not yet. A hyperscaler's own sovereign region is a real step, and it makes the point:

>

Sovereignty that depends on one company's API is sovereignty by permission.

The part I think matters most is the reason to move, which is never sovereignty or cost, because both are important and never urgent. It is value that lands the day you switch and gives the person signing it cover: backups that exist, versions, encryption with the key held elsewhere, a journal of every call. And no new features during the move.

What signs a migration and what does not: value that lands the day you switch, against returns that depend on a future event.

## Judo for small countries

[Judo for small countries](https://newsroom.sgit.ai/articles/judo-for-small-countries.html) is written for the people from Romania I met that day and the people in Portugal I talk to every week. The race for GPUs is the commodity end of the map, and a small country should not enter it. The opportunity is the plumbing a talented person in Braga or Cluj needs to sell a service to the world: forming a company, hiring across a border, being paid across Europe, working in every language. Estonia built that road, with X-Road released as open source, and the article's line on why the road has to be open is the one I would put on a ministry's wall:

>

A road with a toll gate owned by one company is not infrastructure; it is lock-in with tarmac.

The judo playbook in five moves: map the attrition, commoditise the plumbing, create the demand, put the money where the market is still genesis, regulate what settled.

[What open source is, and what it is not](https://newsroom.sgit.ai/articles/what-open-source-is-and-is-not.html) answers misconceptions heard at the event. Open source is a copyright licence, which began as copyleft; a few maintainers decide what goes in, so the control is real and visible; security is about whether somebody had the time to review it; open weights are a compiled binary; and no licence means all rights reserved. Above all, it is not free:

>

Somebody is always paying.

## A map, read as a story

[Why I love Wardley maps](https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html) collects the best of the maps drawn on this site, and the reasons the technique matters: what is moving the needle, the altitude you are optimising at, build or buy, and whether a market exists at all, read for sgit and for RiskMandate. A map is a story, read one frame at a time, and every node is a map of its own. And every dot on a map is a claim:

>

A map you cannot be wrong about is a diagram.

## Where to stand

[Places of highest leverage](https://newsroom.sgit.ai/articles/places-of-highest-leverage.html) is the same rule for one person with a team of agents that can build in every direction: work where you can add the most value now, are not blocked, and can start. Three days of real steps show it, from the reading meter to the vault, with two walked back and one branch parked. The path looks obvious backwards and was five choices at every step forwards, as long as each step was shipped and used before the next was chosen:

>

That is the discipline that replaces foresight.

[Not a straight line](https://newsroom.sgit.ai/articles/not-a-straight-line.html) is the case. A day spent improving the newsroom's workflow was, I would argue, a day of work for RiskMandate, because the newsroom had the momentum to solve RiskMandate's oldest problem, where to keep a master vault's key, in two days after six months of attempts. The Cyber Boardroom and MyFeeds paused, and what they taught is in everything the newsroom does, because it was written down and open:

>

Focus, for me, is undivided attention on the place of highest leverage.

## The seven articles

### Sovereignty, in practice

Every dot replaceable, and the twin that lets the code stay where it is.

- [**Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works**](../../../../sovereignty-is-the-ability-to-move.md). Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [**Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch**](../../../../move-the-cloud-not-the-code.md). Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.

### For a small country

The plumbing built like a road, and what open source is for.

- [**Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it**](../../../../judo-for-small-countries.md). A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [**What open source is, and what it is not: six misconceptions, a little history, and why the point is that nobody can lock you in**](../../../../what-open-source-is-and-is-not.md). Open source is a copyright licence, not a free-for-all: six misconceptions corrected, and why the point is that nobody can lock you in.

### Maps, and where to stand

How to read a map, and the rule that chooses the work.

- [**Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map**](../../../../why-i-love-wardley-maps.md). The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [**Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps**](../../../../places-of-highest-leverage.md). Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [**Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted**](../../../../not-a-straight-line.md). Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.

*This is issue 8 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [newsroom.sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at newsroom.sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [008-sovereignty-is-the-ability-to-move.jpg](../../../../banners/008-sovereignty-is-the-ability-to-move.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. Its images copy with it.

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/18/008-sovereignty-is-the-ability-to-move.html)*
