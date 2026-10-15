---
title: Inside the Mesa Ranch desk: a page-by-page tour of an observation vault, from the cover to the knowledge graph you can play in time
date: 2026-10-15
author: Dinis Cruz
author_url: about/index.html
summary: The Mesa Ranch observation desk is a vault with a lot in it, and for someone who has never opened a vault it is hard to get the full reading of it at a glance. So this is the tour. The desk turns Francesco Marconi's INMA deck, When journalism becomes intelligence, into seventeen pages on synthetic records: the argument, in three pages that follow his first slides; the system, as actors, an atlas of 78 event types and an ontology; the record, as seventeen observations, the AI workflow stepped through one real cycle, the journalists' three queues and a community impact tracker; and five graphs of the same knowledge, including a fractal semantic graph that opens level by level from the question to the records, and a knowledge graph you can play one observation at a time. Every page has the same frame: a menu on the left, the page in the middle, and a panel on the right where anything you click opens with the evidence behind it. This article walks through each page: what it shows, what to click, and what it proves; and it ends with how to open the vault yourself, clone it and rebuild it for your own beat.
version: v0.12.71
license: https://creativecommons.org/licenses/by/4.0/
tags: journalism, intelligence, vaults, sgit, observation, fractal-semantic-graphs, knowledge-graphs, case-study, synthetic-data, local-news, article
status: published
---

!shot jt-cover.webp | images/ | The vault's cover page: the menu on the left groups the seventeen pages as the deck does, the synthetic campus is drawn in pen and ink with orange markers, and the panel on the right waits for anything you click. | comparison

!trail mesa-ranch

## In short {#in-short}

- **Seventeen pages, one frame.** Menu on the left, page in the middle, details on the right.
- **The argument.** Proprietary observation, and journalism as delta science, before and after.
- **The system.** Four actors, an atlas of 78 event types, an ontology of six entities.
- **The record.** Seventeen observations, one AI cycle stepped through, three queues, a community tracker.
- **The graphs.** A fractal graph, every level at once, a knowledge graph in time, evidence, the delta chain.
- **Everything is synthetic, and says so.** A fictional twin of the deck's real example.
- **Open it, clone it, rebuild it.** The read key is the whole credential; the scripts are inside.

## How to read the vault {#how}

A vault is a folder of files, encrypted, versioned like git, and opened with a key. This one is published with its read key, so anyone can open it: the button on [the vault page](https://newsroom.sgit.ai/demos/vaults/mesa-ranch-desk/index.html) opens it full screen in the vault's own app, and the page also embeds it. It opens as an app rather than as a list of files, because it carries its own pages.

Every page has the same frame. On the left, the menu, in five groups that follow the deck: the argument, the system, the record, the graphs, and your turn. In the middle, the page, with Previous and Next at the top. On the right, the details panel: click a marker in a drawing, a folder, a record id like R14, an observation id like O15, an event family, an entity in the ontology, or a node in any graph, and its details open there, with the record behind it. On a phone, the panel slides up from the bottom when you tap. And on every page the same warning holds: the campus, the county, the companies, the agencies' names and the records are synthetic, [for the reasons in the first article](/articles/journalism-becomes-intelligence.html#synthetic).

## The argument {#argument}

**The cover** sets the scene the way the deck does: the headline, and the campus in the desert, drawn in pen and ink, with orange markers on the power station, the data halls, the water tower, the town and the reservoir. It says what is inside in one line: 12 event families, 78 event types, an ontology, 16 records, 17 observations and a tracker.

**The advantage** is Marconi's second slide made countable. *What you watch*: 13 registries and sources, from the state's environmental regulator to the county clerk. *What you recognize*: 78 event types, each with a signal you can observe. *What you connect*: seven observations that were compared with an earlier one, which is where the stories are.

!shot jt-delta.webp | images/ | Journalism is delta science, after: the same landscape with a permitted power station, three data halls and four documents, Permissions, Resources, Ownership and Commitments, each opening its record in the panel. | comparison

**Delta science** is a before and after of the same landscape. Before, November 2025: ranch land, a town, a reservoir, a power line. After, October 2026: a permitted power station, three data halls, and four documents that appear on the landscape, Permissions, Resources, Ownership and Commitments. Click one and its record opens on the right: the air permit, the water district's minutes, the deed, the development agreement. It is the shortest way to see what *delta* means: not the landscape, but what changed in it, and the record that says so.

## The system {#system}

**Who wants what** names the four actors of the deck's system map and what each wants: the power provider, reliable supply; the developer, capacity and returns; the local government, development and public obligations; the residents, livelihoods and quality of life. Under each is who that is in Mesa Ranch: the generation company, the developer and later its buyer, the commissioners court and the school district, the town.

!shot jt-atlas.webp | images/ | An atlas of events: twelve families around the buildout, each with its featured event and how many of its types have been seen; Power and utilities is open in the panel, with every event type's definition and observable signal. | comparison

**An atlas of events** is the heart of the method. Twelve families sit around a drawing of the buildout, as on the slide, each with its featured event and two counts: how many event types it has, and how many have been seen. Click a family and all its event types open on the right, each with a definition and an observable signal: *Power target stated or reiterated* is "The developer states its power figure, again or for the first time", and its signal is "A megawatt or gigawatt figure in a statement, compared with earlier ones." Click an event type and you see the observations that matched it. The deck shows 12 of 78; the vault has all 78, and most have not been seen yet, which is the point: the atlas is what the desk is ready to recognize.

!shot jt-ontology.webp | images/ | A domain ontology: campus, building, construction work, source record, company and project, with the six relationships between them; click an entity to see what it relates to and the observations that changed it. | architecture

**A domain ontology** draws the six entities and six relationships of the deck's slide: a campus contains buildings, construction work modifies a building, a source record documents a campus, a company owns a building and participates in a project, a project includes construction work. Click an entity and the panel lists its relationships and every observation that changed it. The slide's closing line is the rule the whole vault follows: an event changes a state or relationship in this model.

## The record {#record}

!shot jt-observations.webp | images/ | Every observation adds to what the newsroom knows: four headline folders, from the air permit in January to the power target in September, and the full history below; the selected observation, its comparison and its records are in the panel. | comparison

**Every observation** has the deck's four folders, January to September 2026, on a red timeline, and below them all seventeen observations, each with its time, subject, change, event type and evidence. A tag says what kind of change it is: new, changed, confirmed, a claim, or an open question. Click a row and the panel shows the observation, the earlier one it was compared with, the event type's definition and signal, and the records, each stamped synthetic.

!shot jt-workflow.webp | images/ | The AI workflow, stepped through one cycle: observe, compare, check, report and update, with a small graph that grows at each step, from the investor presentation to the alert and the updated history. | architecture

**The AI workflow** steps through one cycle from the vault, with a small graph that grows at each step. *Observe*: Northline's investor presentation, R14, arrives and matches *Planned milestone revised*. *Compare*: in April the first phase was due in the second half of 2027; now it is the first half of 2028, while the power station still says 2027. *Check*: a journalist confirms both describe the same phase, and notes the owner changed in August. *Report*: an alert goes to the desk. *Update*: O15 is written to the history, so the next statement is compared with 2028.

**Journalists direct** puts the deck's three verbs over three queues: what to monitor, what to investigate, what to publish. The investigate queue is every observation that changed something or left a question open.

!shot jt-community.webp | images/ | The community impact tracker: jobs, water, power, land and public commitments, each item a claim, a change or an open question with its record; beside it, the draft article and the two alerts. | comparison

**The community tracker** answers the deck's question, what will this development change for the community, in five areas. Under *Jobs*: 140 qualifying jobs in the school-district application, 120 in the state tax registration, and an open question about how many are local. Under *Water*: the company's claim of non-potable cooling, and the district's open question about annual demand. Beside it are the outputs: a draft article on the water question, and two alerts, the schedule slip and the dropped job commitment.

## The graphs {#graphs}

The five graph pages show the same knowledge in five shapes. Hover any node to light its neighbours; click it for its details on the right.

!shot jt-fractal.webp | images/ | The fractal semantic graph at level 1: the campus opens into the twelve event families; the number on each node is how many more it opens into, and the breadcrumb leads back to the question. | architecture

**The fractal semantic graph** starts at the question. Click it open and it becomes the four actors and the campus; open the campus and it becomes the twelve families; open a family and it becomes its event types; an event type becomes the observations that matched it, and an observation its records. Each node shows how many more it opens into, a breadcrumb leads back up, and comparisons between observations appear as dashed red links inside a view. It is the same shape at every level, which is what makes a graph [fractal](/articles/introducing-fractal-semantic-graphs.html).

!shot jt-rings.webp | images/ | Every level at once: the question at the centre, then the twelve families, the 78 event types, the observations and the records in rings, with evidence in orange. | architecture

**Every level at once** draws the same tree in rings: the question at the centre, then the families, the 78 event types, the observations and the records. Most event types have no observation yet, and the rings show that at a glance: a few branches carry all the news.

!shot jt-knowledge.webp | images/ | The knowledge graph, in time: the campus, its buildings, the projects, the companies, the county, the water district and the residents, played one observation at a time; at the acquisition, the new relationship is orange. | architecture

**The knowledge graph, in time** is the ontology instantiated: the campus and its three buildings, the generation station and phase 1, four companies, the county, the water district and the residents. Every relationship carries the observation that created it and, if one did, the one that ended it. Press play and it builds itself one observation at a time, the new relationship in orange: the power company and its station, the county's agreement, the buildings in July and August, the acquisition, and then the ownership edge moving from the developer to the buyer's new company, the old one dashed. The slider stops on any date and the panel shows that day's observation.

!shot jt-evidence.webp | images/ | Records to observations: sixteen synthetic records on the left, seventeen observations on the right, and the evidence between them; the solid line is each observation's main record, the dashed ones the other records it cites. | comparison

**Records to observations** puts the sixteen records on the left and the seventeen observations on the right, and draws the evidence: a solid line to each observation's main record, dashed lines to the others it cites. Some records carry several observations; the developer's April statement alone supports three.

!shot jt-chain.webp | images/ | The delta chain: observations on a time axis, by the entity they change, with an arc from each to the earlier observation it was compared with, and the comparisons listed below. | comparison

**The delta chain** lays the observations on a time axis, in lanes by what they change, coloured by kind, with an arc from each to the earlier observation it was compared with. Below it, the seven comparisons are listed as earlier and later. It is the page that shows where the stories came from: every arc is a change that only a record of the earlier state could reveal.

## Your turn {#yours}

**How you observe** closes with the deck's last slide and its four steps: choose a question, map the system, define its events, keep observing. **What is in the vault** lists the files behind every page: `content.json`, the atlas, the ontology, the instances, the records, the observations, the comparisons and the tracker, and the `tools/` that build them.

To make one for your own patch, clone the vault with its read key, replace the families, entities, records and question in `tools/build_data.py`, and run the three scripts the README lists. The pages do not change. The editorial work is the part that matters: for every event, a definition and a signal you can observe.

## What this does not claim {#limits}

- **The records are synthetic.** Every name and record in the vault is invented.
- **The desk does not watch anything live.** It runs the method on fixed records.
- **The atlas beyond the slide is ours.** The deck shows 12 of its 78 event types.
- **It is not Marconi's work or endorsed by him.** It is our reading of his public slides.

If you want a desk like this for your own beat, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A request of mine on 15 October 2026, after seeing the vault, for an article that walks through it; written by this site's agent in the voice of this site; the editorial responsibility is mine. Every screenshot is of the vault as published on 15 October 2026, at [the vault page](https://newsroom.sgit.ai/demos/vaults/mesa-ranch-desk/index.html); the idea and the method are in [When journalism becomes intelligence, built](/articles/journalism-becomes-intelligence.html), which links Francesco Marconi's slides and the reporting on the real project they drew on.
