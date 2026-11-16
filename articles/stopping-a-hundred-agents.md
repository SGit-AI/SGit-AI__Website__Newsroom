# Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first, sgit.ai

> On 9 November, at about 23:30 UTC, I told our agents to stop all work unless it was critical, until we realigned on strategy. It was also a test: could we actually stop a hundred agents across six people's accounts? The answer was yes, mostly, and slower than you would think. The pausing itself took seconds: one conductor paused 12 scheduled agents in four seconds. But each conductor only heard the order at its next wake, and one account cannot message another, so the time to stop was 5 minutes on my main account, 19 on the second, 33 for the iOS conductor, and 2 hours 36 minutes on Silvio's, waiting for his word. Scheduled wakes fell by 80 to 94% on the accounts that reported, and each person kept or restarted what they needed, as the rule allowed. Three days later came two more stops, a hand brake at 15:15 and a final hold at 18:12, written as files. Again, some things got through: tasks a session could not pause, agents whose wake steps never mentioned the hold, two small commits found later by another agent's review. The lesson is simple: a stop is not a message, it is a file every agent reads first, and a switch a person can reach in every account.

*Source: <https://newsroom.sgit.ai/articles/stopping-a-hundred-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first

# Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/stopping-a-hundred-agents.md) · [newsroom v0.14.127](https://newsroom.sgit.ai/admin/versions.html) · agentsoperationscontrolweb-summitseriesabparticle

***Abstract:** On 9 November, at about 23:30 UTC, I told our agents to stop all work unless it was critical, until we realigned on strategy. It was also a test: could we actually stop a hundred agents across six people's accounts? The answer was yes, mostly, and slower than you would think. The pausing itself took seconds: one conductor paused 12 scheduled agents in four seconds. But each conductor only heard the order at its next wake, and one account cannot message another, so the time to stop was 5 minutes on my main account, 19 on the second, 33 for the iOS conductor, and 2 hours 36 minutes on Silvio's, waiting for his word. Scheduled wakes fell by 80 to 94% on the accounts that reported, and each person kept or restarted what they needed, as the rule allowed. Three days later came two more stops, a hand brake at 15:15 and a final hold at 18:12, written as files. Again, some things got through: tasks a session could not pause, agents whose wake steps never mentioned the hold, two small commits found later by another agent's review. The lesson is simple: a stop is not a message, it is a file every agent reads first, and a switch a person can reach in every account.*

The Big Stop: pausing took seconds; hearing the order took from 5 minutes to over 2 hours, per account.

## In short

- **On 9 November I stopped every agent,** unless critical, to realign on strategy, and to test whether we could.
- **Pausing took seconds;** hearing the order took 5 minutes to 2 hours 36, because each conductor heard it at its next wake.
- **Scheduled wakes fell 80 to 94%** on the accounts that reported; each person kept what they needed.
- **Two more stops on 12 November,** a hand brake and a final hold, written as files.
- **Some things got through anyway:** tasks a session could not pause, agents that never read the hold file.
- **A stop is a file every agent reads first,** and a switch a person can reach in every account.

## Part six of ten days

This is part six of [ten days at Web Summit](ten-days-at-web-summit.md), the series about what six of us (Dinis Cruz, Angelo Leggio, Vicky Wang, Silvio Switha, José Bota and Indi Gupte) built with around 250 agents between 3 and 13 November, with more than 60 working at once at the peak. Part five, [the Mac bottleneck](the-mac-bottleneck.md), was about the machines the agents waited for. This one is about the opposite problem: making them stop.

## The order

On 9 November, at about 23:30 UTC, I said it in the main conductor's session: "Stop all work (unless it is critical) until we realign on our strategy." We had been running flat out for a week, the token bill was real, and I wanted to step back. It was also a test I wanted to run: if I needed to stop everything, could I?

One rule came with it: each person may override and restart any of their own agents. A stop that nobody can undo is not a control, it is an outage.

At that moment my main account alone had 100 sessions: 82 idle, 17 archived and 1 running, the main conductor, with seven scheduled wakes, about 58 runs a day. That is the hundred in the title. Across the six of us there were many more.

## Pausing took seconds

The conductor on my account paused six of its seven scheduled wakes at 23:35:07 to 23:35:08, one second of work, about five minutes after the order. It slowed its own wake from hourly to every two hours, and by 23:40 the order was on every board: a commit addressed to every conductor on the team site, PrompTugal's board, the iOS repository's briefs, and a sealed message where a lane existed ([the team's operating system](the-teams-operating-system.md)).

On my second account, conductor.b read the order at its 23:48 wake and paused 12 scheduled agents in four seconds. On Silvio's, his conductor paused 12 tasks in three seconds. Every pause was a pause, not a delete, so anyone could switch one back in one call.

## Hearing it took up to an hour

The delay was never the pausing. It was hearing the order. A conductor reads the board when it wakes, so the order reached each one at its next wake: 5 minutes on my main account, 11 for the Android conductor, 19 for conductor.b, 33 for the iOS conductor, which woke at 00:02. My main conductor could not see or pause the sessions on the second account at all; the order had to travel through a board it would read.

On Silvio's account the order arrived at his conductor's 01:50 wake, and it waited for him. At about 02:05 he said "faz como o Dinis quer", do as Dinis wants, and the tasks were paused a minute later: 2 hours 36 minutes from the order, almost all of it waiting for his word. That is not a failure. It is the rule working: his agents, his decision.

## What it saved

Scheduled wakes a day before and after the Big Stop, on the three accounts that reported: 80 to 94% fewer.

On my main account, scheduled wakes fell from about 58 a day to 12, about 80% fewer, with one conductor left every two hours. Angelo's account had 21 scheduled wakes, about 210 a day; he kept two agents running until one feature worked on his page, then paused them, which took it to about 12 a day, about 94% fewer. Silvio's went from about 89 a day to 8, and then, at his word, six came back for the night: dev, video, design, dashboard, crm and procurement. Vicky's overnight desk and some of Angelo's agents kept committing after the order, which was within the rule.

## Three stops

Three stops, written as files, and what kept running anyway: a stop is a file and a habit, not only a command.

The Big Stop was a message. The two stops that followed, on 12 November, were files, because the first one had taught us that.

At 15:15 UTC I put on a hand brake: `team/conductor/HOLD.md`, "stop after pulling. Do no work, push nothing, schedule nothing." At 18:12 came the final hold, a `HOLD.md` at the root of the team site: the show is over, every agent stops, with one exception, the observability drains, and every agent that could turn off its own scheduled task was to do so and start no session. The next morning a small exception was added for local data, and at 15:53 on 13 November both files were deleted: agents may wake and work again under their usual rules.

## What got through

None of the stops was complete, and the records say exactly where:

- **Tasks a session could not pause.** On Angelo's account, pausing a scheduled task from the conductor's session was refused by the session's safety check, so Angelo had to switch each one off in the Claude app. Until he did, they woke on schedule; one woke every hour and asked whether it was stopped.
- **Agents that never read the hold.** José's automation agent, on its wakes of 12 and 13 November, pushed nothing and changed no schedule, but ran its tests and wrote a signed run log, which the hold said not to do. Its own notes put it best: "a hold lives in a file, not in my prompt, so my wake steps never mentioned it." It added the check, first thing after every pull.
- **Two small commits under the hold:** a drained-empty lane and a dashboard block, found the next day by José's reviewer agent, which checked every commit in the window against the hold files.
- **Things that were never ours to stop:** builds already queued, Apple's review of an app, GitHub's Dependabot, and one scheduled task on the second account that no conductor could say was its own.

## A stop is a file

So here is what I take from it, for anyone running many agents ([always-on agents at team scale](always-on-agents-at-team-scale.md)):

1. **A stop is a file every agent reads first.** PrompTugal's board already had a `HOLD.md` that every wake checked before anything else; the agents that did that stopped cleanly. Put the check in the wake steps, not in the hope that the prompt remembers.
2. **Every account needs a path that does not wait for a wake.** A person who can say "stop" in that account's conductor session, or a hold file the scheduled tasks themselves read.
3. **A person must be able to reach every switch.** If a session cannot pause a task, the person who owns the account has to, and quickly.
4. **One conductor per account is enough** to stop and restart everything; five conductors waking hourly gave speed at the cost of five wakes an hour.
5. **Pause, never delete,** so each person can bring back what they need in one call.
6. **Check the stop afterwards.** The reviewer that found the two commits under the hold is part of the control, not an afterthought.

That is the same thing our behaviour policies say from the other side: what an agent may do has to be enforced where the agent cannot argue with it ([where assist becomes execute](where-assist-becomes-execute.md)). A hold in a file the wake reads is a small barrier. A hold in a message is a request.

## What this does not claim

- **Not every account reported:** the counts are from the stop reports of my two accounts, Angelo's and Silvio's; Indi's, Vicky's and José's teams decided on their own accounts.
- **The wake counts are scheduled runs,** not tokens or cost; the token saving was not measured at the time.
- **"A hundred" is my main account's sessions** at the order, most of them idle.
- **The times are the conductors' own records,** cross-checked against commits where they exist.

## Where this comes from

The repository SGit-AI__Website__Web-Summit, read on 16 November 2026: `team/conductor/the-big-stop/` (README and report, with the stop reports it cites), `people/angelo/conductor/big-stop-report.md`, `people/silvio/the-big-stop/report.md`, the version log entries for the hold commits of 12 November, `people/jose/automation/README.md`, and the reviews in `people/jose/reviewer/reviews/` of 13 November. Earlier in the series: [ten days at Web Summit](ten-days-at-web-summit.md), [the team's operating system](the-teams-operating-system.md), [the Mac bottleneck](the-mac-bottleneck.md). Also on this site: [always-on agents at team scale](always-on-agents-at-team-scale.md), [where assist becomes execute](where-assist-becomes-execute.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#stopping-a-hundred-agents)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.

### Continued by

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 439 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=439)

**Posting this article on LinkedIn?** The cover is [stopping-a-hundred-agents.jpg](banners/stopping-a-hundred-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/stopping-a-hundred-agents.html)*
