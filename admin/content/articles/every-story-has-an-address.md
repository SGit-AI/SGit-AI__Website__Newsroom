---
title: Every story has an address: a design proposal for PrompTugal.news as a ground-up newsroom, where news is filed where it happens and climbs to the region and the country with its proof, mocked up from the live data of 19 local editions
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: PrompTugal.news now has an agent for every town in the Algarve, plus the region and the country, and between them they hold real data at every altitude: 116 sourced stories, 182 organisations, 23 events, 16 connections between places and 166 recorded gaps. That made me think about what the site should become. News should start local. National news almost always starts at a regional level, and a regional story starts in a town, so the natural shape of a newsroom is from the ground up: every story filed at an address, a parish, a town, a region, and climbing to the region and the country only through its connections, keeping the link to the source it started from at every step. Here is a design proposal for that, mocked up from the live by-place data rather than invented: the idea and the levels, how a real story climbs, a national front page with no national desk, a regional page with a map of the towns and their connections, a town edition, a story page with its address and proof, an organisation page, and the proof layer behind all of it. Plus three names and positioning directions, six design principles, and what is missing: a locality layer, so a thin town leans on its neighbours.
version: v0.14.112
license: https://creativecommons.org/licenses/by/4.0/
tags: promptugal, local-news, design, provenance, by-place, agents, positioning, article
status: published
---

!shot ptl-idea.webp | images/ | The proposal: news starts local and climbs with its proof, from the parish to Europe, and what the data already holds. | screenshot

## In short {#in-short}

- **News should start local.** National news starts at a regional level, and regional news starts in a town.
- **PrompTugal.news already has the data for it:** 19 editions with an agent each, 116 sourced stories, 182 organisations, 166 recorded gaps.
- **The design: every story has an address,** and climbs to the region and the country through its connections, with its sources.
- **Mocked up from the live data:** front page, region, town, story, organisation and the proof layer.
- **Three names;** the one I would pick keeps the masthead and names the method: ground-up news.
- **What is missing:** a locality layer, so a thin town leans on its neighbours.

## Why from the ground up {#why}

PrompTugal.news started as the newsroom we ran around Web Summit ([PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html)), and in the last few days it went local: one agent per place, for Portugal, the Algarve and each of its towns, each keeping a signed file of what it found, with its sources and dates ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)).

Looking at what those agents have gathered, from weather to local companies, startups and events, I think we have something new. This is a newsroom that goes from local to global and is fact-based all the way, with provenance from the top of the page down to the local source. And the irony is that this is how news should work anyway. Every story starts somewhere. A national story usually begins as a regional one, which began in a town. So why not build the newsroom in that order?

## What is already in the data {#data}

Read from the by-place files on 16 November 2026: 19 editions (the country, the region and 17 towns and cities); 116 stories, each with its publisher, date and the date it was read; 182 organisations on the map, from councils and companies to labs and communities; 23 events; 16 connections between places, found by the detective agent; and 166 gaps, each one a thing an agent looked for and could not find.

Some towns are thin. Vila do Bispo has no AI story yet; Silves and Tavira have two each. That is not a problem if the design treats a thin town as connected: to its neighbours, to its region, and to the stories that link it elsewhere.

## How a story climbs {#climb}

!shot ptl-climb.webp | images/ | How a real story climbs: ALGAR's AI tool, from Almancil to Loulé, the pilot towns, the region and Portugal. | screenshot

A story the Loulé agent published yesterday shows it. ALGAR, the Algarve's waste company, built an AI tool with the startup NILG.AI to choose sites for recycling points ([the story on PrompTugal.news](https://promptugal.news/articles/algar-ai-recycling-points-almancil.html)). The company is headquartered in Almancil, a parish of Loulé, so that is where the story is filed. The pilots ran in Lagoa and São Brás de Alportel; ALGAR serves 16 Algarve municipalities; and NILG.AI and the Sociedade Ponto Verde programme that funded the work are national. Each step up is a sourced connection, and each keeps the link back to Almancil.

## The front page {#front}

!shot ptl-front.webp | images/ | Mockup of the national front page: a live strip, a lead with its address and climb, the region, country and towns. | screenshot

The national front page has no national desk. It is assembled from the local and regional files and the connections between them. Above the reporting sits a live strip: warnings, today's events and the council agenda, so a local reader has a reason to come back every day. The lead carries its address above the headline (Faro, the Algarve) and its climb beneath it; every item shows its publisher, its date, the date it was read and how many steps it is from the beat. Further down, the towns sit side by side, each with its stories, events and gaps, and a thin town says which neighbours it leans on.

## The region {#region}

!shot ptl-region.webp | images/ | Mockup of the regional page: a map of the towns from their real positions, their borders, and the sourced connections. | screenshot

The regional page is a map before it is a list. Each town is a dot sized by what its file holds; a pale dot is a thin file; grey lines are shared borders and red arcs are the connections the detective agent has sourced. Next to it: the connections in words, the region's events, and how to start a company here, from the region's own file.

## A town edition {#town}

!shot ptl-phone.webp | images/ | A story page on a phone: the address, the climb, the signature and the distance to the beat. | aside

Every town gets an edition with its own voice. The place agents write their ledes with local character, and the design should let that show: Faro's opens with the storks on the bell tower and the university teaching the region to talk to machines. Under it: the town's live strip, its stories, its map of organisations by type, what is useful to know (where to start a company), its neighbours, its connections, the sources the agent read, and what it could not find.

That last block matters. Gaps are journalism: they tell the reader what we looked for and where we could not see, and they tell the next agent where to look.

!shot ptl-town.webp | images/ | Mockup of a town edition, Faro: lede, live strip, stories, the town's map, useful facts and what we could not find. | screenshot

## The story page {#story}

!shot ptl-story.webp | images/ | Mockup of a story page: the published text, and a rail with the address, how it climbed, and its sources. | screenshot

The story page keeps the article as the agent published it and adds a rail: the address, why it is filed there, how it climbed, its sources with the date each was read, and the entities it links to. The byline is the agent that wrote it, with the key it signed with.

## The proof layer {#proof}

!shot ptl-proof.webp | images/ | Mockup of the proof layer: the chain from a local source to the front page, who keeps each page, and the gaps. | screenshot

Behind every page is a chain of custody: a local source, captured with the date read; the place agent that keeps the town's file and signs it; the data agents that index and capture every cited page (647 indexed and 532 captured at their last run), so a link that dies keeps its copy; the detective that finds the links between places; and the regional and national pages, built from all of that rather than written separately. This is the part no other newsroom shows, and it should be designed in, not hidden in a footnote ([signed by the source](/articles/signed-by-the-source.html)).

## Names and positioning {#names}

!shot ptl-names.webp | images/ | Three directions for the name: local first, proven up; PrompTugal Raiz; and The Address. | screenshot

- **Local first, proven up.** Keep the PrompTugal.news masthead and name the method: ground-up news, with the line "every story has an address". It explains itself in one sentence, and it suits readers who distrust national news. This is the one I would pick.
- **PrompTugal Raiz.** Raiz is Portuguese for root: "notícias com raiz", news with roots, as a name for the local editions (Raiz Faro, Raiz Olhão). Warm in Portugal; needs explaining abroad.
- **The Address.** A standalone name for the format, so it can travel: an open method and stack that any region can run, with PrompTugal.news as the first edition. That is also a capability [AgentiCCells](/articles/starting-agenticcells.html) could sell.

## Six design principles {#principles}

- **An address on every story,** shown above the headline, with the climb beneath it.
- **Proof one tap away:** every claim with its source and the date read, every page signed.
- **Gaps are journalism:** each place says what it could not find, so no page is empty.
- **Altitude before sections:** navigation goes up and down (parish, town, region, country, Europe) before it goes across topics.
- **Now, then depth:** a live strip above the slower reporting.
- **Distance to the beat:** each story says how many steps it is from the subject, so readers see why it is there.

## What is missing: the locality layer {#locality}

The mockups draw the Algarve from real town positions and shared borders, which I added by hand. To make this work for real, the site needs a locality layer of its own: parishes inside municipalities, municipalities inside regions, and each place's neighbours. With that, a thin town automatically draws on the towns around it and on its region, and a story filed in a parish appears, with its address, in every edition above it.

## What this does not claim {#limits}

- **These are mockups,** images of a design proposal; the live site does not look like this yet.
- **The content is real,** from the place agents' files on 16 November 2026; only the weather values in the live strip are samples.
- **The map is schematic,** from town positions and borders added by hand, not from the site's own data yet.
- **The names are proposals,** and none is decided.

## Where this comes from {#sources}

My own thinking, 16 November 2026, after reading the by-place work. The PrompTugal.news repository: `data/by-place/` (19 place files and `connections.json`) and the article by place.loule@, [Almancil waste firm uses AI to site recycling points](https://promptugal.news/articles/algar-ai-recycling-points-almancil.html). Earlier on this site: [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [selling capabilities, not content](/articles/selling-capabilities-not-content.html), [signed by the source](/articles/signed-by-the-source.html), [starting AgentiCCells](/articles/starting-agenticcells.html).
