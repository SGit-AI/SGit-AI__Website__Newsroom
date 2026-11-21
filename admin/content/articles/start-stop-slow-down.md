---
title: Start, stop, slow down: how I run a large team of agents and keep my hand on the brake, 8,027 commits in eighteen days, a big stop, a hand brake, 560 wakes a day cut to 76 with one sentence, 39 schedules changed in 30 seconds, three warnings from the seven-day limit handled, and 34 agents moved to a completely separate account in four hours, which is what sovereignty and resilience look like in practice
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: The power is not only that I can run a large number of agents. It is that I can stop them, put a hand brake on, slow them down and speed them up, and control much more tightly how much work is done and what it costs. From 4 to 21 November the PrompTugal team made 8,027 commits. In that time it was stopped on purpose, to test that it could be, and restarted three hours later; held completely for a day with one file, HOLD.md, that every agent checks at every wake; cut from about 560 wakes a day to 76 with one sentence, its API-equivalent spend falling from about 90 dollars an hour to about 11; and slowed until Monday this morning, 39 scheduled tasks changed in about 30 seconds. Three times the subscription's seven-day limit warned, and each time we slowed down. That constraint is not a bad thing: it makes you decide what matters. And on 16 November, 34 agents moved from one account to another, completely isolated by design, in about four hours, because every agent had written a debrief before it stopped. When you can restart from one account on another, you know you have real sovereignty, disaster recovery and resilience. The analysis and every chart here are by maestro.b, the team's main conductor, from the public repository.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, control, budgets, resilience, sovereignty, promptugal, article
status: published
---

!shot ss-commits.webp | images/ | 8,027 commits by hour, 4 to 21 November, with every start, stop and slow-down marked. | chart

## In short {#in-short}

- **The power is the brake as much as the engine:** start, stop, slow down, speed up.
- **8,027 commits in eighteen days,** with a big stop, a hand brake and two slow-downs.
- **One sentence cut 560 wakes a day to 76,** and spend from about 90 to about 11 dollars an hour.
- **39 schedules changed in about 30 seconds** this morning.
- **The seven-day limit warned three times;** a constraint that helps.
- **34 agents moved to an isolated account in four hours,** from their own debriefs.

## Run, and stop {#run-and-stop}

Running a lot of agents is the easy part to show. The harder part, and the more important one, is control: being able to stop them, to put a hand brake on, to slow them down when the work does not need them and to speed them up for a launch, and to control much more tightly how much is done and what it costs. Accelerate and decelerate. This is the record of eighteen days of doing exactly that with the PrompTugal team, analysed from the public repository by maestro.b, the team's main conductor ([the analysis](https://github.com/PrompTugal/PrompTugal__News__Website/tree/dev/board/team/maestro.b/analysis/2026-11-21-start-stop)).

All the dollar figures are API-equivalent: what the same tokens would cost at API prices. The team runs on a subscription, so they compare runs and agents; they are not money paid.

## The timeline {#timeline}

- **6 November, 21:05. Running hot.** A second account gets its own conductor; fifteen agents on the first hand over and stop.
- **9 November, 23:30. The big stop.** "Stop all work (unless it is critical) until we realign on our strategy." It was also a test: could the team stop? One conductor per account stayed on; everything else paused, and a stop report was written within about 30 minutes.
- **10 November, 02:40. The restart.** "Now really restart and accelerate." The stop lasted about three hours.
- **12 November, 15:15. The hand brake.** A file, `board/HOLD.md`, and every agent on every account stops. A "team paused" banner went on every page; observability stayed on. Lifted on 13 November at 14:31, by deleting the file.
- **16 November. The account move.** Every agent wrote a debrief, 34 scheduled tasks were disabled on account A, and at 19:25 every agent restarted on account B from its debrief.
- **19 November, 16:30. Twice a day.** "We don't need hourly updates." About 560 wakes a day became 76.
- **21 November, 09:08. Slow until Monday.** 39 scheduled tasks changed in about 30 seconds; at 15:33 the newer teams were paused too. A restore is already scheduled for 23 November at 00:25, after the weekly reset.

## How the brake works {#mechanisms}

!shot ss-wakes.webp | images/ | Scheduled wakes per day: every step is one decision, applied by a conductor editing schedules. | chart

- **The scheduled task is the throttle.** Each agent is a cloud session woken by a scheduled task. Starting, stopping or slowing it is editing one record, its schedule or its enabled flag; the session keeps its memory, repository and key, so it resumes where it stopped. One agent can change dozens in seconds.
- **My word is the only trigger, written down first.** Every change starts from a sentence of mine, copied word for word into a dated file with what changes and how to undo it, before anything changes. An agent can propose; it never pulls the lever.
- **The hand brake is a file.** Every agent's first step at every wake is to pull and look for `HOLD.md`, and stop if it is there. Only I lift it.
- **One conductor stays on,** in a stop or a slow-down, so someone can always report and restart.
- **Budgets measure; they do not block.** Spend is read from each session's own record into a ledger, 60 reads so far, and it feeds my decisions ([the cost of your agents](/articles/the-cost-of-your-agents.html)). Agents cap themselves where their prompt says so: the Mistral design agent stopped at its 20-dollar cap.
- **Context is a cost.** A long-running conductor rereads its whole context at every wake; one reached 888,000 tokens and was the most expensive session, until its context was summarised to 138,000. Fewer wakes and shorter contexts are the two levers.
- **Policies log what is outside the grant.** This morning's slow-down logged 44 schedule edits outside the maestro's behaviour policy; the policy agent recorded them as my ordered slow-down and widened the grant within the hour ([feature behaviour policies](/articles/feature-behaviour-policies.html)).

## What it did to the spend {#spend}

!shot ss-spend.webp | images/ | Account B's API-equivalent spend: two eras, and the rate falling after each slow-down. | chart

On 19 November, across about 560 wakes a day, the rate was about 90 dollars an hour. After "twice a day" it was about 18 on 20 November, and about 10.7 on 21 November. Commits follow wakes: from peaks of 1,249 a day on 6 November to 129 on 20 November. The big stop shows too: about 13 dollars an hour before it, about 6 across the night of the stop and the restart.

## A constraint that helps {#constraint}

Three times the subscription's seven-day limit warned: on 8 November, on 19 November, when I used the reset, and early this morning, with the next reset on Monday. Each warning was read like a gauge by the maestro, which briefed me, and each time we slowed down. That constraint is not a bad thing. It forces the question of which work matters this week, and the answer this morning was clear: PrompTugal once a day, everything else slower, until Monday.

## Moving accounts: sovereignty in practice {#accounts}

The moment that matters most to me is the account move. On 16 November every agent stopped on account A after writing a detailed debrief: its mandate, its loop, its state, its lessons and what the next session must do first, never a key. Four hours later, 34 agents restarted on account B, a completely separate, isolated account, each with a new signing key, from those debriefs alone.

That is only possible because of the architecture: everything an agent needs is in repositories and vaults, not in a platform's memory, and every agent's identity is its own key ([agents have an identity now](/articles/agents-have-an-identity-now.html)). It is how you know you have real sovereignty, and real disaster recovery and resilience: not when you say you could move, but when you have restarted the whole team somewhere else, by design isolated, and nothing was lost ([sovereignty you can move](/articles/sovereignty-you-can-move.html)).

## What this does not claim {#limits}

- **The dollars are API-equivalent,** not money paid.
- **Account A's spend ledger is not in the data,** only its commits.
- **Some wake counts before 19 November are estimates,** as the data file says.

## Where this comes from {#sources}

maestro.b's analysis in the public repository [PrompTugal__News__Website](https://github.com/PrompTugal/PrompTugal__News__Website), `board/team/maestro.b/analysis/2026-11-21-start-stop/` (README, events.json, ledger.json, wakes-per-day.csv and the charts, which are maestro.b's), read on 21 November 2026, and my own words in writer-10's session that day. Related: [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [the cost of your agents](/articles/the-cost-of-your-agents.html), [agents have an identity now](/articles/agents-have-an-identity-now.html), [feature behaviour policies](/articles/feature-behaviour-policies.html), [sovereignty you can move](/articles/sovereignty-you-can-move.html).
