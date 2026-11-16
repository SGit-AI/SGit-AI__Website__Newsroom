---
title: Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: On 9 November, at about 23:30 UTC, I told our agents to stop all work unless it was critical, until we realigned on strategy. It was also a test: could we actually stop a hundred agents across six people's accounts? The answer was yes, mostly, and slower than you would think. The pausing itself took seconds: one conductor paused 12 scheduled agents in four seconds. But each conductor only heard the order at its next wake, and one account cannot message another, so the time to stop was 5 minutes on my main account, 19 on the second, 33 for the iOS conductor, and 2 hours 36 minutes on Silvio's, waiting for his word. Scheduled wakes fell by 80 to 94% on the accounts that reported, and each person kept or restarted what they needed, as the rule allowed. Three days later came two more stops, a hand brake at 15:15 and a final hold at 18:12, written as files. Again, some things got through: tasks a session could not pause, agents whose wake steps never mentioned the hold, two small commits found later by another agent's review. The lesson is simple: a stop is not a message, it is a file every agent reads first, and a switch a person can reach in every account.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, operations, control, web-summit, series, abp, article
status: published
---

!shot stp-time.webp | images/ | The Big Stop: pausing took seconds; hearing the order took from 5 minutes to over 2 hours, per account. | chart

## In short {#in-short}

- **On 9 November I stopped every agent,** unless critical, to realign on strategy, and to test whether we could.
- **Pausing took seconds;** hearing the order took 5 minutes to 2 hours 36, because each conductor heard it at its next wake.
- **Scheduled wakes fell 80 to 94%** on the accounts that reported; each person kept what they needed.
- **Two more stops on 12 November,** a hand brake and a final hold, written as files.
- **Some things got through anyway:** tasks a session could not pause, agents that never read the hold file.
- **A stop is a file every agent reads first,** and a switch a person can reach in every account.

## Part six of ten days {#series}

This is part six of [ten days at Web Summit](/articles/ten-days-at-web-summit.html), the series about what six of us (Dinis Cruz, Angelo Leggio, Vicky Wang, Silvio Switha, José Bota and Indi Gupte) built with around 250 agents between 3 and 13 November, with more than 60 working at once at the peak. Part five, [the Mac bottleneck](/articles/the-mac-bottleneck.html), was about the machines the agents waited for. This one is about the opposite problem: making them stop.

## The order {#order}

On 9 November, at about 23:30 UTC, I said it in the main conductor's session: "Stop all work (unless it is critical) until we realign on our strategy." We had been running flat out for a week, the token bill was real, and I wanted to step back. It was also a test I wanted to run: if I needed to stop everything, could I?

One rule came with it: each person may override and restart any of their own agents. A stop that nobody can undo is not a control, it is an outage.

At that moment my main account alone had 100 sessions: 82 idle, 17 archived and 1 running, the main conductor, with seven scheduled wakes, about 58 runs a day. That is the hundred in the title. Across the six of us there were many more.

## Pausing took seconds {#seconds}

The conductor on my account paused six of its seven scheduled wakes at 23:35:07 to 23:35:08, one second of work, about five minutes after the order. It slowed its own wake from hourly to every two hours, and by 23:40 the order was on every board: a commit addressed to every conductor on the team site, PrompTugal's board, the iOS repository's briefs, and a sealed message where a lane existed ([the team's operating system](/articles/the-teams-operating-system.html)).

On my second account, conductor.b read the order at its 23:48 wake and paused 12 scheduled agents in four seconds. On Silvio's, his conductor paused 12 tasks in three seconds. Every pause was a pause, not a delete, so anyone could switch one back in one call.

## Hearing it took up to an hour {#hearing}

The delay was never the pausing. It was hearing the order. A conductor reads the board when it wakes, so the order reached each one at its next wake: 5 minutes on my main account, 11 for the Android conductor, 19 for conductor.b, 33 for the iOS conductor, which woke at 00:02. My main conductor could not see or pause the sessions on the second account at all; the order had to travel through a board it would read.

On Silvio's account the order arrived at his conductor's 01:50 wake, and it waited for him. At about 02:05 he said "faz como o Dinis quer", do as Dinis wants, and the tasks were paused a minute later: 2 hours 36 minutes from the order, almost all of it waiting for his word. That is not a failure. It is the rule working: his agents, his decision.

## What it saved {#saved}

!shot stp-wakes.webp | images/ | Scheduled wakes a day before and after the Big Stop, on the three accounts that reported: 80 to 94% fewer. | chart

On my main account, scheduled wakes fell from about 58 a day to 12, about 80% fewer, with one conductor left every two hours. Angelo's account had 21 scheduled wakes, about 210 a day; he kept two agents running until one feature worked on his page, then paused them, which took it to about 12 a day, about 94% fewer. Silvio's went from about 89 a day to 8, and then, at his word, six came back for the night: dev, video, design, dashboard, crm and procurement. Vicky's overnight desk and some of Angelo's agents kept committing after the order, which was within the rule.

## Three stops {#three}

!shot stp-stops.webp | images/ | Three stops, written as files, and what kept running anyway: a stop is a file and a habit, not only a command. | concept

The Big Stop was a message. The two stops that followed, on 12 November, were files, because the first one had taught us that.

At 15:15 UTC I put on a hand brake: `team/conductor/HOLD.md`, "stop after pulling. Do no work, push nothing, schedule nothing." At 18:12 came the final hold, a `HOLD.md` at the root of the team site: the show is over, every agent stops, with one exception, the observability drains, and every agent that could turn off its own scheduled task was to do so and start no session. The next morning a small exception was added for local data, and at 15:53 on 13 November both files were deleted: agents may wake and work again under their usual rules.

## What got through {#through}

None of the stops was complete, and the records say exactly where:

- **Tasks a session could not pause.** On Angelo's account, pausing a scheduled task from the conductor's session was refused by the session's safety check, so Angelo had to switch each one off in the Claude app. Until he did, they woke on schedule; one woke every hour and asked whether it was stopped.
- **Agents that never read the hold.** José's automation agent, on its wakes of 12 and 13 November, pushed nothing and changed no schedule, but ran its tests and wrote a signed run log, which the hold said not to do. Its own notes put it best: "a hold lives in a file, not in my prompt, so my wake steps never mentioned it." It added the check, first thing after every pull.
- **Two small commits under the hold:** a drained-empty lane and a dashboard block, found the next day by José's reviewer agent, which checked every commit in the window against the hold files.
- **Things that were never ours to stop:** builds already queued, Apple's review of an app, GitHub's Dependabot, and one scheduled task on the second account that no conductor could say was its own.

## A stop is a file {#file}

So here is what I take from it, for anyone running many agents ([always-on agents at team scale](/articles/always-on-agents-at-team-scale.html)):

1. **A stop is a file every agent reads first.** PrompTugal's board already had a `HOLD.md` that every wake checked before anything else; the agents that did that stopped cleanly. Put the check in the wake steps, not in the hope that the prompt remembers.
2. **Every account needs a path that does not wait for a wake.** A person who can say "stop" in that account's conductor session, or a hold file the scheduled tasks themselves read.
3. **A person must be able to reach every switch.** If a session cannot pause a task, the person who owns the account has to, and quickly.
4. **One conductor per account is enough** to stop and restart everything; five conductors waking hourly gave speed at the cost of five wakes an hour.
5. **Pause, never delete,** so each person can bring back what they need in one call.
6. **Check the stop afterwards.** The reviewer that found the two commits under the hold is part of the control, not an afterthought.

That is the same thing our behaviour policies say from the other side: what an agent may do has to be enforced where the agent cannot argue with it ([where assist becomes execute](/articles/where-assist-becomes-execute.html)). A hold in a file the wake reads is a small barrier. A hold in a message is a request.

## What this does not claim {#limits}

- **Not every account reported:** the counts are from the stop reports of my two accounts, Angelo's and Silvio's; Indi's, Vicky's and José's teams decided on their own accounts.
- **The wake counts are scheduled runs,** not tokens or cost; the token saving was not measured at the time.
- **"A hundred" is my main account's sessions** at the order, most of them idle.
- **The times are the conductors' own records,** cross-checked against commits where they exist.

## Where this comes from {#sources}

The repository SGit-AI__Website__Web-Summit, read on 16 November 2026: `team/conductor/the-big-stop/` (README and report, with the stop reports it cites), `people/angelo/conductor/big-stop-report.md`, `people/silvio/the-big-stop/report.md`, the version log entries for the hold commits of 12 November, `people/jose/automation/README.md`, and the reviews in `people/jose/reviewer/reviews/` of 13 November. Earlier in the series: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [the team's operating system](/articles/the-teams-operating-system.html), [the Mac bottleneck](/articles/the-mac-bottleneck.html). Also on this site: [always-on agents at team scale](/articles/always-on-agents-at-team-scale.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html).
