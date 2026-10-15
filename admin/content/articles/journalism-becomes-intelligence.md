---
title: When journalism becomes intelligence, built: an observation desk for one data-center buildout, from an atlas of 78 events to a community impact tracker, in a vault you can open
date: 2026-10-15
author: Dinis Cruz
author_url: about/index.html
summary: Francesco Marconi shared the slides of an INMA talk with a line I agree with completely: "As AI makes content production easier, journalism's competitive advantage will increasingly come from how we observe the world." His deck makes it concrete with a data-center buildout in the desert: journalism as delta science, a map of who wants what, an atlas of events each with a definition and an observable signal, a domain ontology, observations that add to what the newsroom knows, a workflow of observe, compare, check, report and update, and a community impact tracker. I wanted to see it working, so this site's agent built it: a vault on this site, an app of seventeen pages that follows the eleven slides, runs each one on real data structures, and adds five graphs of the same knowledge. The atlas has all 12 families and 78 event types; the ontology has six entities and six relationships; sixteen source records produce seventeen observations, each a subject, a change, a time and its evidence; and the tracker turns them into an article and two alerts. The records are synthetic, on purpose: a fictional campus in a fictional county, because fake permits under real agencies' names would be exactly the kind of record a newsroom like this should never publish. The method is the point, and a vault is a natural home for it: the observation history is a versioned record, the evidence travels with every claim, and anyone with the read key can open it, check it, and copy it for their own beat.
version: v0.12.69
license: https://creativecommons.org/licenses/by/4.0/
tags: journalism, intelligence, observation, events, ontology, data-centers, vaults, sgit, provenance, local-news, synthetic-data, article
status: published
---

!shot ji-desk.webp | images/ | The observation desk's cover, in the deck's style: the headline, and a synthetic data-center campus drawn in pen and ink, with orange markers on the power station, the data halls, the water tower, the town and the reservoir. Every marker in the vault opens a record. | comparison

!trail mesa-ranch

## In short {#in-short}

- **The advantage is how you observe.** Marconi's argument, and the reason this site exists.
- **His deck is a design.** An atlas of events, an ontology, an observation history, a workflow, a tracker.
- **So we built it.** A vault that follows the eleven slides, each one working on data.
- **78 event types, 6 entities, 16 records, 17 observations.** Each observation a subject, a change, a time and evidence.
- **Synthetic on purpose.** A fictional campus; no fake records under real agencies' names.
- **Five graphs of one knowledge.** A fractal graph you open level by level, and a knowledge graph you play in time.
- **A vault is the right home.** The history is versioned, the evidence travels, the read key opens it.
- **Copy it for your beat.** Replace the families and records; the app does not change.

## The argument {#argument}

Francesco Marconi, who runs AppliedXL and before that led research and development at The Wall Street Journal, posted the slides of his talk to the International News Media Association with a line I could have written: "As AI makes content production easier, journalism's competitive advantage will increasingly come from how we observe the world." He calls journalism delta science: "identifying what changed, why it matters, and who is affected." And he names what it takes: "an atlas of meaningful events, a map of the actors and relationships within a domain, and a persistent record of observations backed by evidence."

That is very close to how this site works. [The wire is a graph](/articles/the-wire-as-a-graph.html) of stories with their sources; [every claim is checked against the record](/articles/my-memory-checked.html) before it is published; and [every link points back](/articles/every-link-points-back.html) to what came before and what corrected it. What his deck adds is the discipline of defining, in advance, what counts as a change: an event type, with a definition and a signal you can observe.

## From slides to a working desk {#desk}

His example is a data-center buildout in the desert: a campus going up beside a power station, a town, a water tower and a reservoir. The deck is AI-generated and conceptual, and every slide describes a part of a system. So the agent built each part, in the same order, after the cover:

1. **The advantage moves toward proprietary observation.** What you watch, what you recognize, what you connect: here, 13 registries and sources, 78 event types, and 6 observations that join a new record to an earlier one.
2. **Journalism is delta science.** A before and after of the same landscape; in the after, four documents appear, Permissions, Resources, Ownership and Commitments, and each opens its record.
3. **Who wants what? What depends on what?** The power provider, the developer, the local government and the residents, and what each wants.
4. **An atlas of events.** The deck shows one example in each of twelve families and says the full set is "78 event types in 12 families". The vault has all 78, each with a definition and an observable signal, and shows which ones have been seen.
5. **A domain ontology.** Campus, building, construction work, source record, company, project, and the six verbs between them: contains, modifies, documents, owns, participates in, includes.
6. **Every observation adds to what the newsroom knows.** Seventeen observations, from an air permit application in November 2025 to oversize-load permits in October 2026.
7. **Observations anchor the AI workflow.** Observe, compare, check, report, update, stepped through one real cycle in the vault.
8. **Journalists direct the flow of intelligence.** Monitor, investigate, publish, as three queues.
9. **What is this project changing for the community?** The tracker, and what it produced.
10. **Your advantage is how you observe.** How to make one for your own beat.

!shot ji-ontology.webp | images/ | The ontology slide, working: six entities with their attributes and the six relationships between them, each entity drawn as a pen-and-ink vignette. Clicking an entity lists the observations that changed it. | architecture

## What the observations found {#found}

The synthetic records were written to behave like real ones: they disagree with each other, in small ways that matter. That is where the method earns its keep, because a single record says little, and the change only appears when it is compared with the last one.

- **The permit grew.** The air permit was applied for at up to 5.2 GW and issued at up to 6.1 GW, 17% more.
- **The jobs shrank.** The school-district application promised 140 qualifying jobs; the state tax-program registration commits 120.
- **The schedule slipped.** The developer said in April that the first 1 GW would be online in the second half of 2027; after the acquisition, the new owner's investor presentation says the first half of 2028, while the power station still says 2027.
- **The water question stayed open.** The company says it will cool with non-potable water; the water district deferred a vote on three wells because nobody has said how much water a year the campus will use.

!shot ji-observations.webp | images/ | Every observation adds to what the newsroom knows: four headline observations as folders, January to September 2026, and the full history below, each with time, subject, change, event type and the records it rests on. | comparison

Each of those is an observation with its evidence attached, and two became alerts and one a draft article in the tracker. None of them needed a model to be clever. They needed the atlas to say what a change is, the ontology to say what it changes, and the history to say what was known before.

## The same knowledge, at every level {#graphs}

!shot ji-fractal.webp | images/ | The fractal semantic graph in the vault: the question opens into the actors and the campus, the campus into twelve event families, and here Power and utilities into its seven event types; the breadcrumb leads back up, and every node's details open on the right. | architecture

An atlas, an ontology and an observation history are three views of one graph, and the vault draws it five ways. The [fractal semantic graph](/articles/introducing-fractal-semantic-graphs.html) starts at the question and opens any node into the graph inside it: the campus into its twelve event families, a family into its event types, an event type into the observations that matched it, an observation into its records. Every level has the same shape, which is the point of a fractal graph, and it is the same idea as [reading code as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html): you never need the whole thing at once, only the level you are on and the way down. A radial view puts every level on one page, with the evidence in orange. A bipartite graph joins the sixteen records to the seventeen observations they support. And a delta chain lays the observations on a time axis, with an arc from each one to the earlier observation it was compared with.

!shot ji-knowledge.webp | images/ | The knowledge graph, in time: the ontology instantiated with the campus, its buildings, the projects, the companies, the county, the water district and the residents, played one observation at a time; at the acquisition, the new relationship is orange. | architecture

The one I like most is the knowledge graph played in time. It is the ontology instantiated, the campus, its three buildings, the two projects, four companies and the public bodies, and each relationship carries the observation that created it, and, if one did, the observation that ended it. Press play and it is delta science you can watch: the generation station appears with its permit, the development agreement ties the county to the campus, two buildings appear in August, the developer is bought, and the ownership edge moves from one company to another. That is what a newsroom's memory should look like: not a pile of articles, but a graph whose every edge has a date and a source.

## Where AI fits {#ai}

This is also where I think the deck is right about AI, and where it matters for newsrooms. Observing and comparing used to be the expensive part: reading every registry, every agenda, every filing, every week. Models make that cheap. What they do not replace is the definition of what matters, the check before anything is published, and the judgement about what to report, which is exactly the part the deck gives to journalists, in three labels: "Direct attention", "Investigate significance" and "Exercise editorial judgment". The workflow slide in the vault walks one cycle through it: the investor presentation arrives, is matched to *Planned milestone revised*, is compared with April's statement, is checked by a person, becomes an alert, and updates the history so the next statement is compared with 2028, not 2027.

!shot ji-tracker.webp | images/ | What is this project changing for the community: the impact tracker by jobs, water, power, land and public commitments, each item a claim, a change or an open question with its record, and the article and alerts it produced. | comparison

## Why it is synthetic {#synthetic}

The deck's example is real. Pacifico Energy's GW Ranch, north of Fort Stockton in Pecos County, Texas, received an air permit from the Texas Commission on Environmental Quality for [7.65 GW of gas-fired power generation](https://bigbendsentinel.com/2026/02/04/massive-ai-data-center-coming-to-pecos-county/), and the local paper's reporting already asks the water question the tracker asks. The deck's own footnote says its observations are "Source summaries from the supplied GW Ranch reporting".

I chose not to put synthetic permits, deeds and minutes under the names of a real company and real agencies. A newsroom whose argument is evidence should not publish invented records that could be mistaken for real ones, even in a demonstration. So the vault has a twin: Mesa Ranch, in Caliche County, with its own developer, buyer, power company, water district and agencies, and the word *synthetic* on every record and on the first screen. The shape is the deck's; the facts are fiction, and the vault says so first.

## Why a vault {#vault}

A vault is a natural home for an observation desk. The observation history is a versioned record: every update is a commit, so what the newsroom knew on any date can be recovered and compared, which is delta science applied to the newsroom itself. The evidence travels with every claim: the records sit beside the observations that cite them. And the read key is the whole credential: anyone can [open the desk](https://newsroom.sgit.ai/demos/vaults/mesa-ranch-desk/index.html), clone it with `sgit`, check every observation against its record, and rebuild it with the scripts inside.

## Make one for your beat {#yours}

The slide that closes the deck is the brief: "Choose a question. Map the system. Define its events. Keep observing." In the vault, that is one script, `tools/build_data.py`, with the families, the entities, the records and the question in it. Replace them with a hospital trust, a school district, a port, a river; the app does not change. The harder part is the one the deck insists on and the vault makes visible: writing, for every event, a definition and a signal you can actually observe. That is editorial work, and it is where a newsroom's knowledge of its own patch becomes an advantage nobody else has.

## What this does not claim {#limits}

- **The records are synthetic.** Mesa Ranch, Caliche County and every name in the vault are invented.
- **The atlas is ours.** The deck names 12 families and 12 examples; the other 66 event types were written for this vault.
- **It does not watch anything.** The desk shows the method on fixed records; it does not read live registries.
- **It is not Marconi's work or endorsed by him.** It is our reading of his public slides.
- **Updated on 15 October.** The vault became seventeen pages with a menu and a details panel, and gained the five graph pages.

If you run a local desk and want an observation vault for your own patch, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A request of mine on 15 October 2026, after reading Francesco Marconi's post and slides, *When journalism becomes intelligence*, from his INMA talk; written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The vault was built by this site's agent the same day and is published at [/demos/vaults/mesa-ranch-desk/](https://newsroom.sgit.ai/demos/vaults/mesa-ranch-desk/index.html). Rob D'Amico, [Massive AI data center coming to Pecos County](https://bigbendsentinel.com/2026/02/04/massive-ai-data-center-coming-to-pecos-county/), Big Bend Sentinel, 4 February 2026; TechCrunch on [AppliedXL and its founders](https://techcrunch.com/?p=2142211). Read on 15 October 2026.
