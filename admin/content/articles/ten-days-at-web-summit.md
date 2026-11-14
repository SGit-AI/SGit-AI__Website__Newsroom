---
title: Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part
date: 2026-11-14
author: Dinis Cruz
author_url: about/index.html
summary: Between 3 and 13 November 2026, six of us, with our agents, built more than I can fit in one article. A team operating system, an independent newsroom for Web Summit Lisbon, a site about Storm Charles that grew to more than 2,600 pages in three days, a guide to the summit's fringe that went live two and a half hours after its brief, a draft standard that rated twenty companies, four iPhone and iPad apps, an Android tablet app, and the tools to run all of it. About 20,000 commits across fifteen repositories, 224 Claude Code sessions, around 250 named agents, and more than 60 sessions working at the same time at the peak. This article is the map: the team, the sequence of events, the numbers, a collage of what we made, and the list of articles that will tell each part. I will update it as each one goes live.
version: v0.14.82
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, agents, promptugal, storm-charles, team, series, collage, article
status: published
---

!shot tdw-collage.webp | images/ | Twenty-four of the sites and apps we built or ran between 3 and 13 November 2026. | collage

## In short {#in-short}

- **Six people and around 250 agents,** in ten days around Web Summit Lisbon.
- **What we built:** a team operating system, a newsroom, a storm site, a fringe guide, a rating standard, native apps on two platforms, and the tools to run and stop it all.
- **The scale:** about 20,000 commits, 224 Claude Code sessions, more than 60 working at once at the peak.
- **This is the map.** Each part gets its own article; the list below links them as they go live.

## The team {#team}

There were six of us. Each person had their own agents, their own conductor and their own lane:

- **Dinis Cruz,** head conductor.
- **Angelo Leggio,** the graphs and live views.
- **Vicky Wang,** the editorial check, and the reviewer who kept the newsroom honest.
- **Silvio Switha,** on the ground, video, and competitive research.
- **José Bota,** the channels.
- **Indi Gupte,** communities and organisers.

The agents carried our names in theirs (`role@project.person`), so every commit says whose agent made it. On the Web Summit team's site alone, Angelo's agents made 895 commits, mine 853, Vicky's 767, Silvio's 320, José's 277 and Indi's 277, beside about 2,100 automatic release commits.

## What happened, in order {#timeline}

| When | What happened |
|---|---|
| 3 Nov | MeetScribe, a Google Meet transcriber, built in a day; the book of my talk pushed to its second draft |
| 4 Nov | PrompTugal.news starts; every person gets a key for the team's site; agents get inboxes only they can write to |
| 5 Nov | The book printed as two review copies |
| 6 Nov | PrompTugal.news's busiest day: 1,249 commits |
| 7 Nov | The iPhone app grows from a 1,164-line start; the team's site has its busiest day, 699 commits |
| 8 Nov | Three iOS apps; the first App Store submission at 23:20 UTC; the Android app's first commit at 20:33 |
| 9 Nov | A signed Android build on a tablet at 00:50, four hours after the first commit; at 23:30, the Big Stop: every agent paused |
| 10 Nov | Restart at 02:40; GAMMA-Ray starts; Storm Charles reaches Lisbon and Web Summit calls off its second day at 19:09; the storm site's first commit at 21:14 |
| 11 Nov | The storm swarm: 134 sessions created in one day; Lisbon Tech Fringe live at 12:57; the Fringe iPhone app on TestFlight at 21:11; flights, transport, cloud and model-router desks; Swarm |
| 12 Nov | Shutdown at about 00:50; GAMMA-Ray stops; the hand brake at 15:15; the final hold at 18:12: "the show is over" |
| 13 Nov | The VoiceDebrief iPhone app reaches TestFlight an hour after its first commit |

## The numbers {#numbers}

| What | How many | Where it is counted |
|---|---|---|
| Commits, main projects | about 20,000 | git history of each repository |
| Claude Code sessions created, 3 to 13 Nov | 224, 220 of them started by other sessions | the session list |
| Sessions created on 11 November alone | 134 | the session list |
| Sessions working at once, at the peak | more than 60 (64 to 67, on 11 November) | session start and last-activity times |
| Named agents | around 250 | distinct agent names in the commits |
| Storm Charles site | 2,618 pages, 1,434 versions, 3.84 billion tokens | its own accounts page |
| Native apps | 4 iOS apps (about 48,000 lines of Swift), 1 Android tablet app (about 33,000 lines of Kotlin) | the app repositories |
| Companies mapped and rated | 110 on the team's map; 20 GAMMA-Ray reports | the team's site; gamma-ray.sgit.ai |

A word on money. The dollar figures in these articles are API-equivalent: what the tokens would have cost at standard prices. We ran on flat Claude subscriptions, so they are a measure of work, not money spent.

## The series {#series}

I will publish these one at a time, and link each one here as it goes live.

1. **Ten days at Web Summit** (this article): the map.
2. **The team's operating system:** web-summit.sgit.ai, with its board, briefs, keys, inbox lanes, vaults, company map and X-ray.
3. **PrompTugal.news, the newsroom we ran at Web Summit:** the desks, the reviewers, the outreach drafts and the costs.
4. **Native apps by agents:** four iOS apps from one workspace, an Android build on a tablet in four hours, the App Store and TestFlight.
5. **The Mac bottleneck:** agents waiting three times longer than they ran.
6. **Stopping a hundred agents:** the Big Stop, the hand brake, the final hold, and what kept running anyway.
7. **Agents rating agents:** GAMMA-Ray, a draft standard and twenty company reports in thirty hours.
8. **After the storm:** Storm Charles, part two: flights, transport, the cloud and the model router.
9. **A guide born in a storm:** Lisbon Tech Fringe, live two and a half hours after its brief.
10. **Pennies against dollars:** open-weight swarms against frontier models, and the cost of memory.
11. **Agents that retire themselves:** 147 sessions and 106 hand-overs.
12. **The agents that didn't get the memo:** a newsroom that ran nine days on "nothing new".
13. **One hour to TestFlight:** VoiceDebrief, when there is something to install.

Already published, from the same ten days: [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [who else controls AI agents at Web Summit](/articles/who-else-controls-ai-agents-at-web-summit.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [a key for every person](/articles/a-key-for-every-person.html), [the Web Summit team, part five](/articles/web-summit-part-five.html) and [MeetScribe](/articles/meetscribe.html).

## What this does not claim {#limits}

- **Counts depend on how you count.** "Around 250 agents" is the number of distinct agent names in the commits; it includes some renamed agents. Sessions are not agents: many roles handed over to a fresh session several times.
- **"More than 60 at once" is an upper bound** from each session's start and last activity; a session can sit idle between turns.
- **The commit total is approximate,** summed across the main repositories.
- **Dollar figures are API-equivalent,** not money spent.

## Where this comes from {#sources}

The repositories behind each site, read on 13 November 2026: the Web Summit team's site, PrompTugal.news, Storm Charles, Lisbon Tech Fringe, Swarm, GAMMA-Ray, the iOS and Android apps, VoiceDebrief and MeetScribe; and the list of Claude Code sessions for the account. The sites: [web-summit.sgit.ai](https://web-summit.sgit.ai/), [promptugal.news](https://promptugal.news/), [storm-charles.promptugal.news](https://storm-charles.promptugal.news/), [lisbontechfringe.com](https://lisbontechfringe.com/), [swarm.promptugal.news](https://swarm.promptugal.news/), [gamma-ray.sgit.ai](https://gamma-ray.sgit.ai/), [ios.app.promptugal.news](https://ios.app.promptugal.news/), [ios.app.voicedebrief.ai](https://ios.app.voicedebrief.ai/).
