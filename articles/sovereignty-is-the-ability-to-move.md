# Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works, sgit.ai

> I spent today at a sovereignty event, and what struck me most is how much of Europe's sovereignty conversation is about things we do not control and will not control soon: frontier models, giant data centres, GPUs. That is playing where the ball is, not where it is going, and in padel, which I am learning, that is the difference between having all the time in the world and having none. My view is that technology sovereignty is the ability to move, and that it comes from treating every dot in the stack, commodity, product or custom built, as something you can replace. The test is a Wardley map with one question: take away the dot, what happens? If the answer is that the service stops, that is a board-level risk with a name next to it. The fix is not an alternative that is as good as today, which is why most efforts never start. It is a twin of the thing you do not control, running in your QA environment, good enough for the minimum viable company: the priority customers and the services that must not stop, slower, dearer, tested every week. Can it move is the first question; is it cheap and does it scale is the second, and we keep confusing them. Open source is the only kind of control that survives an acquisition. Europe does not lack startups or talent; it lacks the commercial open source model that would let its many small players add up. And now, with models that can read a map and run a simulation on a twin, this analysis can finally be done at scale.

*Source: <https://newsroom.sgit.ai/articles/sovereignty-is-the-ability-to-move.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works

# Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/sovereignty-is-the-ability-to-move.md) · [sgit.ai v0.7.81](https://sgit.ai/admin/versions.md) · sovereigntyresilienceeuropewardley-mapstwinsopen-sourceminimum-viable-companyqatestingdisaster-recoverystrategyarticle

***Abstract:** I spent today at a sovereignty event, and what struck me most is how much of Europe's sovereignty conversation is about things we do not control and will not control soon: frontier models, giant data centres, GPUs. That is playing where the ball is, not where it is going, and in padel, which I am learning, that is the difference between having all the time in the world and having none. My view is that technology sovereignty is the ability to move, and that it comes from treating every dot in the stack, commodity, product or custom built, as something you can replace. The test is a Wardley map with one question: take away the dot, what happens? If the answer is that the service stops, that is a board-level risk with a name next to it. The fix is not an alternative that is as good as today, which is why most efforts never start. It is a twin of the thing you do not control, running in your QA environment, good enough for the minimum viable company: the priority customers and the services that must not stop, slower, dearer, tested every week. Can it move is the first question; is it cheap and does it scale is the second, and we keep confusing them. Open source is the only kind of control that survives an acquisition. Europe does not lack startups or talent; it lacks the commercial open source model that would let its many small players add up. And now, with models that can read a map and run a simulation on a twin, this analysis can finally be done at scale.*

Take away the dot, in three frames. One service as it runs; object storage removed and the blast radius followed up the edges to the customers; a twin of the storage, tested in QA, putting the service back for the priority customers, degraded but running. Use the controls to stop on each frame.

The 3 frames, one image each: [1](images/sv-dot-1.webp) [2](images/sv-dot-2.webp) [3](images/sv-dot-3.webp).

## In short

- **Europe's sovereignty conversation is mostly about things it does not control.** Frontier models, giant data centres and GPUs are where the ball is today. They take years and capital, and they benefit whoever already has them. Most real work does not need a frontier model.
- **Play where the ball is going.** A good padel player always seems to have time, because they read the ball and move to where it will be. If I move after it comes off the glass, there is no hope. Sovereignty is the same game.
- **Sovereignty is the ability to move.** Agility, almost liquidity: the ability to move a workload, and an action, from one provider to another, including inside the same cloud. Very few companies can, because everything was hard-coded, clicked into existence, and never deployed twice.
- **Take away the dot.** Draw the Wardley map, remove one thing you do not control, and follow the edges up. If the service stops, you have found the problem, and it belongs on the risk register, all the way to the top.
- **Do not jump from zero to a hundred.** The alternative does not have to be as good as today. It has to work, for the minimum viable company: the priority customers and the services that must never stop. Slower and dearer is fine. Zero is not.
- **Run it in QA, all the time.** A twin of every dependency you do not control, running in disposable QA environments, is how this stops being theory. If you only do it in an emergency, you will discover every small problem during the emergency.
- **Can it move, then is it cheap.** The first question is whether it is possible. Whether it is cost effective and scalable is a second question, and asking it first is how sovereignty conversations end before they start.
- **Open source, or one acquisition away.** A European supplier today is one acquisition from not being one. Only open source and Creative Commons give control that survives a change of owner, in either direction.

## Where the ball is going

I am learning to play padel, and the thing that is most striking about watching a good player is how much time they have. They are not faster than me. They read the ball, they know where it will be after it comes off the glass, and they are already there. If I do not read the ball, or I move after it has bounced off the back wall, there is no hope; I am always late, and every shot is a scramble. The same idea is usually told with the line attributed to Wayne Gretzky, about skating to where the puck is going rather than where it has been, and it is the best short description I know of what Europe gets wrong in the sovereignty conversation.

The ball today is the frontier model, the giant data centre and the GPU. Those are real, and they matter, and they are where the ball is now. Building them takes years and a scale of capital that only benefits the players who already have the infrastructure and can leverage it. You cannot compete with that, and trying to is moving after the ball has hit the glass. [Judo for small countries](judo-for-small-countries.md), written this afternoon, makes the same point for a single country: the capital race is the wrong end of the map, and most real work does not need a frontier model anyway. The models are becoming a commodity. Very few use cases need the frontier, and for the ones that do not, a frontier model is too expensive, too powerful and more dangerous than the job needs.

Where the ball is going is the ability to move: workloads, data and the actions agents take, from one provider to another, when you decide, and not on the day a supplier decides for you.

## Sovereignty is the ability to move

The way I think about it now is that sovereignty is mostly agility, almost liquidity: the ability to move a workload and keep operating. And the honest test of most organisations is that they cannot do it, not between clouds and often not even within the same hyperscaler. The infrastructure was hard-coded, created by clicks, built up over generations of changes, and never deployed in a second place. That is fragility, whatever the contract says about where the data lives.

That is an engineering gap, not a policy gap, in the same way that [agentic cost is an engineering problem](agentic-cost-is-an-engineering-problem.md). And "critical" is a word that gets abused. For a company, a disruption at a supplier, a technology partner or a platform that stops the business is a critical problem whether or not it is national critical infrastructure: you are losing money, losing customers, and not providing what people are paying for. The question for every organisation is the same: can you move the workloads, and are you focusing on what you can control?

## Take away the dot

The tool for this is the one I keep coming back to, a [Wardley map](why-i-love-wardley-maps.md). Put the customer at the top, the service they pay for, your application and your data, and under them the products and commodities you buy. Then ask one question of each dot you do not control: take it away, what happens?

The figure at the top does it in three frames for an illustrative service. Remove the object storage. Follow the edges up: the data has nowhere to live, the application cannot start, the service stops, the customers have nothing. That is the blast radius, the same measure [Footprint and blast radius](footprint-and-blast-radius.md) uses for an agent's reach, applied to a dependency. If the blast radius is the whole chain, you know where the problem is, and then you keep asking: what happens when the service stops, and what happens after that. That is the analysis every organisation should be able to do, and the one it should take to the board: by the way, you have a dependency here, and in this scenario you do not have a business.

The important correction to my own first framing is that this applies across the whole stack. It is tempting to say only the products and commodities you buy need an alternative, because custom-built things are yours. But custom-built things stand on commodities, and a custom-built system that only one person can deploy is as much a single point of failure as a supplier. The rule is: you must be able to treat every dot as replaceable, at least to the level of a product, whether you built it or bought it.

## Do not jump from zero to a hundred

A maturity model for every dot you do not control. From 0, it stops, through the data can leave, it runs somewhere once, it runs for the minimum viable company, to 4, it moves when you decide. Each level carries a cost and a population it serves, and each is only real if it was tested.

The reason most sovereignty efforts never start is that they set the bar at "an alternative that works just like today, as efficient and as optimised as today". That is a hundred, and nobody gets from zero to a hundred. The bar should be: it works. Unoptimised, maybe not for every customer, maybe not for every feature, but it works.

This is where the minimum viable company comes in, an idea from the resilience and incident-response world: the smallest version of the business that can keep serving customers while the rest recovers. From a disaster recovery and resilience point of view, you should have infrastructure that runs that minimum viable company: the priority customers, the services you must provide, the users who should never go without. Emergency services are the clean example: they should never lose network capability, whatever else fails, so there are backups of backups.

And it is a backup of operations, not only of data. Having the data is necessary and not sufficient. If you do not have the software, the schema and the ability to load and move it, you do not have data mobility; you have an archive. What you need, for every dot you do not control, is the equivalent of a [twin](https://twins.sgit.ai/what-is-a-twin/index.html): something compatible enough that your application cannot tell, running on infrastructure you can run, perhaps not as efficient, but working. [Move the cloud, not the code](move-the-cloud-not-the-code.md) describes the S3 twin that exists today and why the code must not know it has moved.

Usage and side effects should be a spectrum, not a cliff. When a technology is not available, the service should degrade, not stop. And a point made at the event that I agree with: if customers understood why, understood the disruption and its side effects, many would happily pay for the slower, dearer version that keeps running.

## Run it in QA, all the time

All of this is theoretical until you do it, and if you do it you have to do it all the time. The place to do it is QA and testing. A QA environment should be disposable, created from nothing, and it does not need the scale of production; it needs to work. Run it on the twins: the storage twin, the identity twin, the model you can host yourself. Every time QA is created, you have proved, again, that the business can run without the dots you do not control, for at least a test load. Every time something breaks, you have found it on a Tuesday, not during an outage.

That is also why the alternatives get better. You will discover lots of small problems the first time, and you should solve them when you have time to solve them rather than when there is an emergency. Run it every week and the gap between level 2 and level 3 on the maturity model closes without a migration project anybody had to sign.

## Can it move, then is it cheap

When people ask how much technology sovereignty is possible, the question is already loaded, because it mixes two questions. The first is: is it possible? Can this dot be replaced at all, and has anyone tried? The second is: is it cost effective and does it scale? We keep asking the second before the first, and the answer to the second is almost always "not yet", so the conversation ends.

Ask them in order. Possible first, with a cost matrix and a scale matrix written down for each dot: yes, it can run, for this number of customers, this number of users, this set of services, and we tested it last week. Then cost. My expectation is that the engineering benefits of being able to move, deployments that are reproducible, environments that are disposable, dependencies that are understood, end up paying for much of it, even if the main path stays optimised on the incumbent and the alternative runs a little more expensively. And focus on what can move. Do not spend the effort on things you are clearly never going to control, for physical, political, technical or cost reasons. Spend it on the dots where today there is no alternative, or no efficient market, because that is where the ball is going.

## Open source, or one acquisition away

I have written many times that you cannot have sovereignty unless it is open source, or Creative Commons for content, and the reason is simple. Even if a supplier is European today, you are one acquisition away from losing that. It works both ways: a European company can buy an American one, and the American customers are then in the same position. If you are the underdog, you should be the one playing this game, because you have more to gain and very little to lose. Control that survives a change of owner is the only control that counts, and open source is how you get it: you can read it, run it, fix it and move it. [open-source.sgit.ai](https://open-source.sgit.ai/) is my longer argument that open source is a strategy, not a charity.

This is also where Europe's real gap is. It is not startups and it is not talent. Prosus and Dealroom's [State of AI in Europe](https://www.prosus.com/news-insights/2026/europe-is-ais-invisible-giant), published in March 2026, says "Europe creates as many new AI startups each year as the US", with roughly the same number of AI professionals, "but it converts them into breakout companies at a third of the rate." And the United States is very good at capturing European talent: Stanford's analysis of the founders behind 500 American unicorns, [reported by Crunchbase](https://news.crunchbase.com/venture/foreign-born-entrepreneurs-drive-americas-unicorn-boom-strebulaev-stanford/), found that 44% were born outside the US, with the United Kingdom, Germany and France leading the European countries of birth. The gap is positioning, and it is a commercial open source model that Europe never quite developed: many small and medium players that should be connected and aggregated into a bigger play, each leveraging the others and letting the others scale, which is what an open source ecosystem is.

## Provided centrally, like a road

It is not realistic to expect every company in a country, or every company in a group or a sector, to build a twin of every dependency on its own. Some of this should be provided centrally, by governments, by industry bodies, by the larger organisations in a supply chain, as infrastructure, in the sense of a road: built once, open, used by everyone, and not a central project that becomes another dependency. [Judo for small countries](judo-for-small-countries.md) makes the road argument in full, and [Move the cloud, not the code](move-the-cloud-not-the-code.md) describes the business a European infrastructure operator could build by selling the twin layer. The demand, in both cases, comes from the same question asked of every dot.

## Why now

This analysis was always the right one, and it was always too expensive to do properly: drawing a map of every service, removing each dot, following the blast radius, running the simulation, writing it down for the board. That has changed. With today's models the mapping and the simulations can finally be done at scale, and they are much better done on top of twins than in a spreadsheet, because a twin can actually be switched off and the result observed rather than guessed. Map it, take away the dot, run the twin in QA, and put the level-0 dependencies on the register with a name next to them. That is how Europe gets technology sovereignty: by making every part of the stack replaceable, one dot at a time, starting where the ball is going.

## What this does not claim

- **The map in the figure is illustrative.** It is a typical service, not a measured one; the point is the method.
- **The maturity levels are a proposal.** They are how I would score a dependency; they have not been calibrated across organisations.
- **The startup and founder figures are other people's.** Prosus and Dealroom report parity in the number of AI startups, not that Europe has more; the Stanford founder study covers unicorns up to 2021 and is not specific to AI.
- **The minimum viable company is not my term.** It comes from the resilience and incident-response world; what is mine here is running it on twins in QA.
- **Twins beyond storage are not built.** The S3 twin exists; most of the others in this argument are the work to do.

If you are running a sovereignty programme and want to take away the dots in your own map, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, after a day at a sovereignty event, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. Figures: Prosus and Dealroom, [State of AI in Europe: the invisible giant](https://www.prosus.com/news-insights/2026/europe-is-ais-invisible-giant), 16 March 2026; Ilya Strebulaev's unicorn founder study as [reported by Crunchbase News](https://news.crunchbase.com/venture/foreign-born-entrepreneurs-drive-americas-unicorn-boom-strebulaev-stanford/), 13 May 2025. Twins: [twins.sgit.ai](https://twins.sgit.ai/what-is-a-twin/index.html). Open source as strategy: [open-source.sgit.ai](https://open-source.sgit.ai/).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#sovereignty-is-the-ability-to-move)

### Builds on

- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.

### Continued by

- [What open source is, and what it is not: six misconceptions, a little history, and why the point is that nobody can lock you in](what-open-source-is-and-is-not.md) Open source is a copyright licence, not a free-for-all: six misconceptions corrected, and why the point is that nobody can lock you in.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 94 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=94)

**Posting this article on LinkedIn?** The cover is [sovereignty-is-the-ability-to-move.jpg](banners/sovereignty-is-the-ability-to-move.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/sovereignty-is-the-ability-to-move.html)*
