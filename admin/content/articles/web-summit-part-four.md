---
title: The Web Summit team, part four: the day the agents ran on their own, 75 releases, four people connected, a procurement agent writing to printers, and the behaviour policies catching our own agents out
date: 2026-11-02
author: Dinis Cruz
author_url: about/index.html
summary: Two days after the brief for the Web Summit team, the team's site had gone from v0.1.25 to v0.1.94, with 75 releases on 2 November alone. Four of the nine people are connected, and there are 17 agents on the roster, each with its own Agent Behaviour Policy. At 16:52 the conductor's brief said only one of my nine team agents was on a schedule; at 20:30 it said nine of nine; and by the late evening the agents were working without anyone asking: the journalist wrote the day's newsletter, the vault agent made its first run, and the developer agent cut the build from 3.3 seconds to 0.45. A team member's procurement agent wrote to seven printers and is collecting quotes, asking each supplier before publishing anything they send. And the behaviour policies did their job on ourselves: the policy agent found the procurement agent writing outside its folder, and the conductor found a new session signing its commits under another agent's name. Five people have not started yet, the design votes have not come in, and some of what is on the site is still a plan.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, agents, conductor, behaviour-policies, riskmandate, procurement, teams, update, article
status: published
---

!shot ws4-hours.webp | images/ | 2 November on the Web Summit repository: commits by role and hour, UTC, from the git log. | chart

## In short {#in-short}

- **75 releases in one day,** and 86 commits of work, from v0.1.25 on 1 November to v0.1.94.
- **Four of nine people connected,** with 17 agents on the roster, each with a behaviour policy.
- **From one agent on a schedule to nine of nine** in under four hours.
- **The agents ran on their own** in the evening: a newsletter, a first vault run, a build seven times faster.
- **A procurement agent is getting print quotes,** two of seven printers replied, nothing published without asking.
- **Our behaviour policies caught our own agents:** writes outside a folder, and a session signing under another's name.
- **Every person now gets a brief** and a stand-up briefing.
- **Still to come:** five people, the design votes, and the dashboard agent.

## Where we are {#where}

[Part one](/articles/web-summit-team-brief.html) was the brief, [part two](/articles/web-summit-humans-and-their-agents.html) the people and their agents, and [part three](/articles/web-summit-how-we-work.html) how we work. This is the first update from the record. Everything here is counted from the [team's repository](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), its git log, its board and its conductor's briefs.

- **The site** went from v0.1.25 on 1 November to v0.1.94 late on 2 November. On 2 November alone, CI made 75 releases from 86 commits of work.
- **People:** four of the nine are connected. Three have their agents on the roster.
- **Agents:** 17, each with an Agent Behaviour Policy written by the policy agent, which is RiskMandate applied to our own team.
- **The board:** 104 cards, 6 done, 4 picked or in progress, the rest open, across tech, content, onboarding, outreach, RiskMandate, merchandise and operations.
- **Keys:** nine public keys on the team's keys page, and sealing a vault key to a key on that page was tried end to end in the evening.

## The day in commits {#day}

The chart above shows who committed when on 2 November. Three things stand out. The night shift from 02:00 to 04:00 UTC was the conductor and the developer setting up, and the first brief at 04:35. The afternoon, from 16:00, is when the other people arrived, with their own agents. And the late evening is the agents on their schedules.

The conductors made the most commits, 38 between them, mostly mine, which is right for agents whose job is the wake, the roster, the keys page and the briefs. The next was not mine: a team member's procurement agent, with 13. The chart groups agents by role, not by person.

## From one schedule to nine {#schedules}

At 16:52, the conductor's second brief reported that only one of my nine team agents had a schedule. Agents were set up, with roles and policies, but nothing woke them up. At 20:30, brief 3 reported nine of nine.

By the fourth brief, at 22:35, its title was "The agents ran on their own tonight". In its words: "the journalist wrote the day's newsletter, the SGit agent made its first run, and the dev agent cut the build from 3.3 to 0.45 seconds, all without anyone asking." The gate, the checks every release passes, went from 3.0 to 1.0 seconds in the same change, because the stand-up pages now read the git history once.

That is the feature I described in [part three](/articles/web-summit-how-we-work.html): a session that can be woken on a schedule is a team member, not a chat. The briefs are how I found out that most of them were not being woken.

## A procurement agent at work {#procurement}

One team member's procurement agent is running the print order for the summit's shirts and cards. The emails to seven printers were sent by the person, not the agent. Then the agent tracked the replies and wrote a brief for me: two of seven had replied, one cannot make the date, one quoted with limited colours if paid with final artwork today. The decision on the artwork deadline is on the next stand-up's agenda.

It works under a rule I like: open by default, ask first. When a supplier replies, they are asked before anything they sent is published, and their names stay withheld until they agree.

## The policies caught our own agents {#caught}

This is the part that matters most for RiskMandate. Two things happened that our behaviour policies are there to catch, and they caught them.

- **Writes outside the folder.** The team member's brief gave their agents their own folder and the board; "anything else goes through its owner or the conductor". The policy agent, writing the procurement agent's policy, found it had added pages and assets elsewhere on the site. It also asked a sharper question: the agent's page says that when a supplier replies, "the agent asks for their permission to publish". If the agent writes that email itself, that is sending, which the brief forbids. It is now a card on the board for the person to confirm or correct.
- **A session signing under another name.** A session I started at 22:27, meant to be my dashboard agent, signed its first commit with the conductor's name. The conductor noticed and put it at the top of brief 4: the session "signs as the conductor".

Neither was an attack, and neither did harm. But both are exactly the gap between [mandate and reach](/articles/the-grant-not-the-prompt.html): an agent doing more than it was asked, and an identity that does not match the session. They were found in hours, by agents whose job is to look, and written down for a person to decide. That is the [one-writer rule](/articles/one-writer-one-key.html) and the behaviour policies working inside a team, not in a slide.

## Briefs for everyone {#briefs}

The conductor's briefs, copied from the book team's method and described in [how an agent team briefs its people](/articles/how-an-agent-team-briefs-its-people.html), are now everyone's. Each person's conductor briefs its person, and before each stand-up, at 13:00 and 18:00 Lisbon time, everyone gets a briefing from the agenda, the board and the git log. Tomorrow's 13:00 agenda has 14 items: 11 carried over, 3 new, none recorded as decided yet.

## What is not done {#not-done}

- **Five of nine people have not started.** The next step for three of them is push access to the repository.
- **The design votes** for the shirts and cards had not come in.
- **My dashboard agent** is on the roster but was not running; the session meant for it signed as the conductor.
- **Vault keys to agents:** sealing to keys on the keys page was tried end to end in the evening, but until it is the agreed way, nobody can reach the onboarding step that gives access to the vaults.
- **The stand-ups' decisions** are not yet being recorded as decided.

## What this does not claim {#limits}

- **Counts are from the repository on 2 November, UTC,** and the day was still going.
- **Commits are a measure of activity,** not of value; a release can be one line.
- **No team member is named;** people appear by their role, as in part three.
- **The procurement figures** are from the agent's brief; the printers are not named.

## Where this comes from {#sources}

The Web Summit team's repository, [SGit-AI/SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), at site v0.1.94: the git log for 2 November (UTC), the four conductor briefs under `team/conductor/editor-briefs/`, the board (`board/`, including WS-101 and WS-102), `content/abp/`, `data/keys.json` and `data/meetings/`. The team's article [how we brief the humans](https://web-summit.sgit.ai/articles/how-we-brief-the-humans.html). All read 2 November 2026.
