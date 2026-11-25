---
title: A repository per agent: why the PrompTugal news site's repository reached 9,080 commits in three weeks, most of them not about the site, and how moving every agent into its own repository and site gives us provenance and explainability we did not have
date: 2026-11-25
author: Dinis Cruz
author_url: about/index.html
summary: PrompTugal__News__Website was meant to hold a news site. In three weeks it took 9,080 commits from about 121 agent identities, 1,249 of them on one day, and when you look at what they touched, two thirds of the commits made by agents changed only coordination files, the agents' notes, runs, briefs, keys and status, and only 9% changed only the site. Everyone, and by everyone I mean every agent, used that repository as the central place to work, because it was the one place they could all write. It worked, and it was also a side effect and a massive bottleneck. Since 24 November each agent gets its own repository: one for the agent itself, its memory, role, keys and restart note, and one for what it works on. That gives each agent its own signed history, its own key published in its own first commit and its own site that others can read. This is what the numbers show, why it happened, and what we gain.
version: v0.14.214
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, provenance, explainability, git, promptugal, sovereign-website, article
status: published
---

!shot rpa-commits.webp | images/ | 9,080 commits to the PrompTugal site's repository in three weeks; orange is coordination-only. | chart

## In short {#in-short}

- **9,080 commits in three weeks** to one repository, from about 121 agent identities.
- **67% of the commits made by agents touched only coordination files;** 9% touched only the site.
- **It was everyone's notebook** because it was the one place every agent could write.
- **Now each agent has two repositories:** one for itself and one for what it works on.
- **The gain is provenance:** each agent's own signed history, key and site, readable by anyone.

## What the numbers show {#numbers}

PrompTugal__News__Website started on 4 November. By 25 November it had 9,080 commits: 1,249 on 6 November, 953 on 11 November, and still 264 to 372 a day from 22 to 24 November. 2,258 were the release bot's version commits. The other 6,822 were made by agents, every one of them signed, under about 121 identities: dev@PrompTugal.dinis with 675, Vicky Wang's reviewer with 419, conductors with hundreds each, a places data scientist with 232, the maestros on accounts B and D.

The folders tell you what the repository really was. Commits touching `board/`: 5,010. The site's build: 2,621. REALITY.md: 2,281. The desks: 1,397. Data: 1,084. Content and articles: about 650. Inside `board/`, the team folder alone had 87 subfolders, one for almost every agent, plus runs and behaviour policies, and the shared keys file held 251 keys. Splitting the agents' commits by path: 4,597 changed only coordination files, 1,352 changed both, and 625 changed only the site.

## Why it happened {#why}

It was not a plan; it was the easiest place. PrompTugal was where the summit team worked, it had the policies and the keys, and every new agent was told to keep its notes there. So the news site's repository became the team's shared board, its message bus and its memory, for agents working on PrompTugal and for many that were not: a maestro's guidance on 19 November said it "works in board/team/maestro.b/… until Dinis gives it a repository of its own."

It worked well enough to run the busiest weeks we have had ([start, stop, slow down](/articles/start-stop-slow-down.html)). It also meant one history for everyone to untangle, one queue for every push, conflicts between agents that had nothing to do with each other, and a site repository whose log was mostly not about the site.

## The decision {#decision}

!shot rpa-before-after.webp | images/ | From one shared board to a repository per agent: the same work, with each agent's own history and key. | figure

On the morning of 24 November I said it at the sync: "the whole idea that each agent has its own repo. So we have a repo for agent and a repo for what they're working on. We're moving away from using the site … which was kind of a side effect of and also massive bottleneck." The brief that came out of it has three lines that matter:

- **Two repositories per agent:** "one for the agent itself: its memory, role, learnings, messages, keys and restart note; one for what it works on: the site or tool."
- **Moving off PrompTugal__News__Website:** "Agents stop using it as the shared board."
- **Done as each agent is onboarded or restarted,** "not as a big-bang move", with the factory first, then the sites and hub keepers, then the librarian.

What made it cheap is the pipeline: an agent's repository and site is one request ([almost a hundred repositories](/articles/almost-a-hundred-repositories.html)). Without that, 32 agents' repositories would have been 32 afternoons of my time.

## What we gain {#gain}

- **Provenance per agent.** Each `Site__Agent__<name>` repository is that agent's history alone. The 32 agent repositories hold 889 commits, all signed, each with `Agent:` and `Claude-Session:` lines, so every change points back to the session that made it.
- **A key that proves itself.** An agent's first commit adds only its public key, and the site's signer check uses it from then on; the factory's keys file is the root.
- **Explainability by reading.** What an agent is, what it is doing and how to restart it are pages on its site ([who runs the agents](/articles/who-runs-the-agents.html)). To understand why something happened, you read one agent's log and pages, not a shared log of 9,000 commits.
- **The site repository is the site again.** Changes to a site come from its keeper, and its history is about the site, which is what an owner who takes it over needs ([the first round trip](/articles/the-first-round-trip.html)).
- **No single queue.** Agents stop waiting on each other's pushes to one branch.

This is the same idea as the sovereign website, applied to the agents themselves: each one owns its files, its history and its address.

## What this does not claim {#limits}

- **The coordination split is by path,** counting board/, desks/, REALITY.md, CLAUDE.md, README and notes as coordination; a different line would give different percentages.
- **The move is partial:** after the decision, maestros on accounts A, C and D still committed to the PrompTugal repository.
- **Identities are counted from commit prefixes and trailers;** some agents used more than one name.

## Where this comes from {#sources}

The git history of [PrompTugal__News__Website](https://github.com/PrompTugal/PrompTugal__News__Website) to 25 November 2026 (its `board/` and `board/keys.json`), and the `Site__Agent__*` repositories of the [SovereignWebsite](https://github.com/SovereignWebsite) organisation: Site__Agent__Maestro's `briefs/2026-11-24-morning-sync.md` and its verbatim note, and SovereignWebsite__IaC's `board/conductor.b/2026-11-24__onboarding-order.md`. The model in full: [how we work](https://strategy.agents.sovereignweb.site/accounts/b/how-we-work/). Related: [who runs the agents](/articles/who-runs-the-agents.html), [almost a hundred repositories](/articles/almost-a-hundred-repositories.html), [start, stop, slow down](/articles/start-stop-slow-down.html), [who steered this](/articles/who-steered-this.html).
