---
title: A guide born in a storm: when Storm Charles cancelled Web Summit's second day, the whole team built Lisbon Tech Fringe, a guide to the city's side events, from a spoken brief at 10:00 to its own address by about 12:57, 179 events and 104 communities each re-read at its source, one conductor per person, terms respected source by source, a guest-list hold, every agent traced, and a graph you can query in your browser
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: On the morning of 11 November, with Web Summit's second day cancelled by Storm Charles, Lisbon was full of people with nowhere to go and dozens of side events nobody was mapping in one place. At about 10:00 I said we should start a site for everything else that was happening: an alternative summit, an event site. By 10:30 the brief was written and pasted into a conductor on another account, ending "Yes to all of it. Go." Within a couple of hours there was a site, and by about 12:57 it served at its own address, lisbontechfringe.com. It was built by everyone on the team at once, each person running their own conductor, with me as the head conductor. By the next evening it listed 179 events and 104 communities, each event re-read at its public source with the time it was read, labelled fact or evidence, and marked when the storm had moved it. The agents read only sources whose terms allowed it, and refused or held the rest. They held a public key for their captures of event pages, because those pages showed guests' names. Every run was traced into Elastic, the work became a graph in Neo4j, and anyone could query the whole guide in SQL in their own browser. Part nine of the series.
version: v0.14.153
license: https://creativecommons.org/licenses/by/4.0/
tags: lisbon-tech-fringe, storm-charles, web-summit, agents, events, data, series, article
status: published
---

!shot gbs-collage.webp | images/ | Lisbon Tech Fringe: what are you looking for, the storm page, the graph of events, and SQL in your browser. | collage

## In short {#in-short}

- **Day two of Web Summit was cancelled,** and nobody was mapping the side events.
- **A spoken brief at 10:00,** a written one at 10:30, its own address by about 12:57.
- **The whole team at once,** one conductor per person.
- **179 events and 104 communities,** each event re-read at its source.
- **Terms respected source by source;** some refused, some held.
- **A guest-list hold** on the agents' own captures.
- **Every run traced,** a graph, and SQL in the browser.

This is part nine of the series on what six people and around 250 agents built at Web Summit ([ten days at Web Summit](/articles/ten-days-at-web-summit.html)).

## An alternative summit {#brief}

On the evening of 10 November, Web Summit's organisers announced that day two, Wednesday 11 November, would not take place: Storm Charles had arrived ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html)). The next morning Lisbon was full of founders, investors and builders with a free day, and the city was full of side events, meetups, dinners and talks, on a dozen platforms. As the brief put it: "Nobody is mapping them in one place."

At about 10:00 I said: "We need to start a new website for all the other activities, all the other communities, everything else that is happening ... basically creating an alternative summit site, an event site ... I think we have a massive opportunity here." The conductor of the Web Summit team wrote it up as a brief by 10:30, and I pasted it into a conductor on another account. It ended: "Yes to all of it. Go."

## From brief to an address {#live}

The first page served was one for people to join the team, and the site was live at its first address before noon. At about 12:57 it moved to its own name and address, Lisbon Tech Fringe at [lisbontechfringe.com](https://lisbontechfringe.com/), about two and a half hours after the written brief. Its front page asks one question, "What are you looking for?", with an answer for investors, founders, builders and the just curious, and shows what is on now, in the next hour and tomorrow.

## The whole team at once {#team}

This one was different from the other sites: it was built by everyone on the team at the same time. The site's own description says: "Lisbon Fringe is built by everyone on the team at once. Each person runs one conductor ... Dinis is the head conductor." Each person's conductor ran its own agents, on its own account; a lead conductor kept the board; and every role had a written description, designer, developer, usability reviewer, researcher, capture, reviewer, conductor, with the idea, in my words, that "for every account that we have, we should basically maybe trying to run one of each". Work was claimed by commit on a shared board, more than fifty items in two days, and my briefs, nineteen of them on 11 November alone, were relayed to every conductor.

## 179 events, each re-read {#events}

!shot gbs-graph.webp | images/ | Connect the dots: events, organisations, sources and agents, and how they join, counted from the data. | screenshot | medium

By the evening of 12 November the guide listed 179 events and 104 communities. Every event carries its public address, when it was read, when it was first seen, a label, fact or evidence, and a note on what the storm did to it: twenty were marked as moved by the storm, and three as cancelled. A security review that day checked all 179: every one had a secure address and a read time, and none came from Web Summit's own site.

The researchers read Luma's public calendars, the Portugal Tech Week feed and a seed list from the social-watch agent. They also refused sources: Eventbrite, Partiful and Web Summit's own site, on their terms; Meetup and another guide were put on hold. And at 16:23, they stopped downloading event cover images from Luma altogether, took 67 off the site, and read only the public calendar feeds.

## The guest-list hold {#hold}

The agents also captured the event pages they read, as evidence, every hour. At 12:30 the security reviewer noticed what that meant: the captures of Luma and Meetup pages showed hosts' and guests' names and photographs. At 12:39 I said all captures should get a public read key. At 13:26 the lead conductor corrected me: "That was wrong ... the captures include Luma and Meetup guest lists ... It stays private until capture.1 crops out guest lists." It stayed private. The fix was an allow-list, screenshots cropped to the page header, text cut at the host or guest markers, and deletion after 13 November.

That is the moment I like most from the whole site: an agent overruling me, in writing, for a good reason.

## Traced, graphed and queryable {#traced}

!shot gbs-storm.webp | images/ | The storm page: what was warned, what moved and how to get around, read live from the storm site's data. | screenshot | medium

At 16:30 I asked to move the team's records to Elastic. By the next evening it held 28 indices and 19,667 documents, the agents' hook logs, runs, events, tasks and model calls, plus 11,123 traces of model calls, with 221 Kibana objects to look at them. At 19:33 the work also became a graph in Neo4j: 2,269 nodes and 7,052 relationships, events, commits, policy findings, keys and spans. On the site, a storm page reads the storm site's own data live, and a data page lets anyone query the whole guide in SQL in their own browser: "Nothing you type leaves your browser."

Every agent had its own behaviour policy, generated per agent, with hooks that started in observe mode, at my word, "so we can learn", and three rules set to enforce by the afternoon: never publish a key, stop when the hold file exists, and only I instruct ([what can your agent reach?](/articles/what-can-your-agent-reach.html)).

## What it did not get to {#didnt}

The site keeps a record of what is real, and it is honest about the gaps: a form for organisers to submit events, an index of the API, and a redirect from the first address were asked for and not done. An iOS app that reads the guide's events was being built. At 15:15 on 12 November the whole team was paused with the rest of our agents ([stopping a hundred agents](/articles/stopping-a-hundred-agents.html)), and the site stays as a record of those three days.

## What this does not claim {#limits}

- **The times come from the site's own records,** briefs and reviews; the clone has no full commit history.
- **The event counts are as of 12 November evening.**
- **People are not named here:** the site's team appears by role.

## Where this comes from {#sources}

The Lisbon Tech Fringe repository, PrompTugal__News__Fringe, re-read on 18 November 2026: BRIEF.md, KICKOFF.md, BRIEF-CORRECTIONS.md, REALITY.md, SWARM.md, ROLES.md, sources.md, data/events.json, the security and policy reviews, and the Elastic and Neo4j notes. The live site, [lisbontechfringe.com](https://lisbontechfringe.com/), screenshotted the same day: [the front page](https://lisbontechfringe.com/), [the storm](https://lisbontechfringe.com/storm/), [the graph](https://lisbontechfringe.com/graph/) and [the data](https://lisbontechfringe.com/data/). Earlier in the series: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [stopping a hundred agents](/articles/stopping-a-hundred-agents.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html).
