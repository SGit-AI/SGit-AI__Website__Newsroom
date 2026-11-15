---
title: PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: PrompTugal.news is going local. This is the updated strategy, my answer to Vicky Wang's plan for local sites and the brief for the PrompTugal team. One set of agents, stories tagged by place, no agent per town, and every place on its own subdomain from the start, because there will be many and they must be made automatically: promptugal.news is the national site and carries Europe and the world, algarve.promptugal.news is the region, and every one of the Algarve's sixteen municipalities, and the city of Quarteira, gets its own site, faro.promptugal.news, loule.promptugal.news and so on. Each site is a lens on one shared semantic graph: the same stories, read from a different centre, so a Loulé story leads on Loulé's site and is a small item on the national one. Four rules keep it from escalating: the brand is always PrompTugal.news; every story passes the PrompTugal test, it connects to AI, directly or within two or three steps; place decides where a story shows and how big, AI decides whether it is ours at all; and every site opens with its mandate. The first wave is every town in the Algarve at once.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: promptugal, local-news, algarve, knowledge-graph, strategy, newsroom, article
status: published
---

!shot pbp-levels.webp | images/ | PrompTugal.news by place: Portugal, the Algarve and its towns, with news flowing down and local sources rising up. | concept

## In short {#in-short}

- **PrompTugal.news is going local:** Portugal, the Algarve, and every Algarve town.
- **One set of agents, stories tagged by place,** and no agent per town.
- **Every place gets its own subdomain from the start,** made automatically: algarve.promptugal.news, faro.promptugal.news.
- **Each site is a lens on one shared semantic graph:** the same stories, a different centre.
- **One test for every story:** does it connect to AI? Place decides how big; AI decides whether it is ours.
- **The first wave is every town in the Algarve at once,** sixteen municipalities and Quarteira.

## Why local {#why}

[PrompTugal.news](/articles/promptugal-news-the-newsroom-we-ran.html) began as a newsroom for Web Summit: technology and AI, in context, from Portugal for Europe. Vicky Wang wrote a plan for local sites, and this is my answer to it, and the brief for the team. I said yes to her option A, one set of agents with stories tagged by place, with one change: every place gets its own subdomain from the start, because we will make many of them, and it must be automated.

## The north star {#north-star}

Four rules, so this does not escalate:

1. **The brand is PrompTugal.news, always.** A town site is "PrompTugal.news · Faro", a lens on the same publication, never a new brand.
2. **Every story passes the PrompTugal test: is this a PrompTugal story?** A PrompTugal story is always about AI, directly, or within two or three steps in the graph: a council's new data centre and the AI workloads it will run; a startup event and its AI founders. The path to AI is written down with the story. No path to AI, not ours, however local or however big.
3. **Place decides where a story shows and how big. AI decides whether it is ours at all.**
4. **Every site opens with its mandate:** two lines at the top saying what it covers. For example: "PrompTugal.news Faro: AI and technology in Faro, its university and its companies, and what reaches Faro from Portugal and the world. Independent; every fact sourced."

## Three levels of place {#levels}

- **Portugal: promptugal.news,** which also carries the international news, Europe and the world.
- **The Algarve: algarve.promptugal.news,** the region.
- **The towns:** all sixteen municipalities of the Algarve, and the city of Quarteira, each at its own address.

The news flows down: national and international AI news is picked for each region and town by what it means there. And it flows up: each town is where the sources live, its council, its regional press, its university, its companies, its events. They are captured at town level, tagged, and rise to the Algarve and the national site when they matter.

## Each site is a lens {#lens}

!shot pbp-lens.webp | images/ | Each site is a lens on the same stories: how prominent a story is depends on how close it is to the site's place. | chart

Stories, places, companies, people (public and professional only), institutions, events and sources are entities in one graph, with typed links between them: about, located in, part of, organised by, sourced from, uses. A place sits inside the next: Quarteira is part of Loulé, Loulé of the Algarve, the Algarve of Portugal. Each site reads the same graph from its own centre: how close a story is to the site's place sets where it shows and how big; how close it is to AI decides whether it is a PrompTugal story at all.

A story is written once and has one home; every site it concerns lists it and links to it, never a copy. Someone local only needs their town's site: that is where the dots connect ([the new data lake](/articles/the-new-data-lake.html)).

## What every town site shows {#town}

1. Its mandate, at the top.
2. Its centre of gravity: what the place is about, found from sources, never invented. Faro has the University of the Algarve, so innovation and research are a natural focus there.
3. Local AI news, big.
4. Algarve, national and international AI news that matters there, smaller.
5. Events in the area, from their organisers' public pages.
6. Local companies, public facts only, each with its source and the date read.
7. Factual extras, such as the weather from IPMA.
8. Its gaps: what we have no source or feed for yet. A town with no AI news is a finding in itself.

Each town also looks like itself, its own references and landmarks inside the PrompTugal.news frame. And, for fun, each town site gets a clearly labelled toggle that rewrites the page in an exaggerated local voice, with the facts identical: it makes fun with the place, never of its people.

## The first wave {#wave}

Not one town first: all of them, with the Algarve site above them. Faro, Loulé, Quarteira, Silves, Tavira, Vila Real de Santo António, Portimão, Lagos, Olhão, Albufeira, Lagoa, Monchique, Aljezur, Vila do Bispo, Castro Marim, Alcoutim and São Brás de Alportel. The first research for each: its centre of gravity, recent AI stories, each sourced and dated, its local sources and feeds, its events, its companies, and its gaps.

## How it is built {#built}

Everything stays in the PrompTugal.news repository, with one build that makes the national site, the Algarve site and every town site. Making a place is one entry in a list: its name, its parent place, its mandate, its sources; the build does the rest. Addresses are subdomains, never a path, and the DNS for them is set up when the sites are ready to serve, the kind of step the [site factory](/articles/from-a-commit-to-a-live-website.html) is for. The PrompTugal team builds it, from the build and the graph to the towns' sources, their look and their stories, under the usual rules: public sources, a source and a date for every fact, no contact details.

## What this does not claim {#limits}

- **Nothing is built yet:** this is the strategy the team agrees first.
- **Not now:** DNS for the towns, separate repositories, any new brand, or a dedicated local desk, which is Vicky's call when local stories outgrow the Portugal desk.
- **An earlier version** of this brief, published on the Web Summit team's site on 14 November, started with paths under promptugal.news and moved to subdomains later; this version starts with subdomains.

## Where this comes from {#sources}

My brief of 14 November 2026, PrompTugal.news by place, answering Vicky Wang's [plan for local sites](https://web-summit.sgit.ai/people/vicky/local-sites/); the earlier version on the Web Summit team's site: [PrompTugal.news by place](https://web-summit.sgit.ai/articles/promptugal-by-place.html). Earlier on this site: [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [the new data lake](/articles/the-new-data-lake.html), [from a commit to a live website](/articles/from-a-commit-to-a-live-website.html).
