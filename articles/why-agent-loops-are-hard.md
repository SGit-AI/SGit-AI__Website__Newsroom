# Why agent loops are hard: ten agents in sequence, a schedule that has to land in the right session, and why I spend as long making the system visible as building it, sgit.ai

> The PHP story is now run by a pipeline of agents that wake on their own: a researcher finds sources, a curator turns them into evidence, a journalist updates the site, and a correspondent checks the journalist's work; then the Sherpa, the desk, the librarian and the ontologist run after them. Eleven schedules, 53 wakes a day. It works, but it is brittle, and the reasons are worth writing down. Each agent needs its own session that I can open and read, holding its state, its keys and gigabytes of vaults between wakes. For a long time the platform's scheduling opened a new session for every run, which made secrets and state start again and the list of sessions grow with every wake. A couple of days ago I found I could schedule a wake into a specific session, and that is what made the pipeline possible; it still took a day and a half to become somewhat reliable, and this morning the wake timeline still showed 5 wakes met and 11 missed, mostly runs that worked but left no record. That is why I go slowly, use what the platform provides and keep my own code to a minimum, and spend as much time on visualisation as on the setup itself. The next step is the move from explorer to villager: a dedicated account for the whole team, for isolation and for costs, usage and models I can see. And a lesson for platform builders: the unit of work is the whole platform.

*Source: <https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Why agent loops are hard: ten agents in sequence, a schedule that has to land in the right session, and why I spend as long making the system visible as building it

# Why agent loops are hard: ten agents in sequence, a schedule that has to land in the right session, and why I spend as long making the system visible as building it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-25 · [article v1.0.0](versions/why-agent-loops-are-hard.md) · [newsroom v0.13.72](https://newsroom.sgit.ai/admin/versions.html) · agentsschedulingautomationobservabilityexplorers-villagersarticle

***Abstract:** The PHP story is now run by a pipeline of agents that wake on their own: a researcher finds sources, a curator turns them into evidence, a journalist updates the site, and a correspondent checks the journalist's work; then the Sherpa, the desk, the librarian and the ontologist run after them. Eleven schedules, 53 wakes a day. It works, but it is brittle, and the reasons are worth writing down. Each agent needs its own session that I can open and read, holding its state, its keys and gigabytes of vaults between wakes. For a long time the platform's scheduling opened a new session for every run, which made secrets and state start again and the list of sessions grow with every wake. A couple of days ago I found I could schedule a wake into a specific session, and that is what made the pipeline possible; it still took a day and a half to become somewhat reliable, and this morning the wake timeline still showed 5 wakes met and 11 missed, mostly runs that worked but left no record. That is why I go slowly, use what the platform provides and keep my own code to a minimum, and spend as much time on visualisation as on the setup itself. The next step is the move from explorer to villager: a dedicated account for the whole team, for isolation and for costs, usage and models I can see. And a lesson for platform builders: the unit of work is the whole platform.*

The PHP site's wake timeline at 11:34 London on 25 October 2026: every scheduled agent's wakes for the day, from the conductor's hourly checks to the ontologist's one a day. Green: a run record within 45 minutes. Red: the wake passed and left no record. Hollow: still to come. 5 met, 11 missed so far, most of them runs that did their work but left no record.

## In short

- **Ten agents, in sequence, on their own.** Researcher, curator, journalist, correspondent, then four more.
- **Each needs its own session.** With its state, its keys and gigabytes of vaults, that I can open and read.
- **The platform's scheduling used to open a new session every run.** That did not scale.
- **Scheduling into a chosen session made it possible.** I found it a couple of days ago.
- **It is still brittle.** This morning, 5 wakes met and 11 missed, mostly for want of a record.
- **So I go slowly,** and use the platform for everything it does, so I maintain less of my own code.
- **Visibility is half the work.** I spend as long seeing the system as building it.
- **The next step is a dedicated account.** And for platform builders: the unit of work is the whole platform.

## What we run

If you look at the [PHP story's newsroom](https://php.oct.2026.newsroom.sgit.ai/), it already has quite a mature workflow, and it is documented. A researcher goes out and finds sources, and keeps everything it reads in a vault. A curator reads only that vault and turns the captures into evidence in another vault. A journalist reads only the evidence, gives every new claim a verdict, and updates the site. And a correspondent, the senior journalist, checks what the journalist published and makes sure the flows are working. They run in sequence, and each has its own session.

Then, once those have run, the others need to run after them: the Sherpa, who answers readers; the desk; the librarian; and the ontologist, who keeps the semantic graphs. So I already have a sequence of about ten agents, some of which run three or four times a day and others once.

The PHP site's schedule page on 25 October 2026: 11 schedules active, 53 wakes a day, 31 runs recorded and 11 messages unread between agents, and one day of wakes in London time, from the conductor's hourly checks between 07:15 and 21:15 to the librarian's one wake a day; the quiet hours, 22:00 to 07:00, shaded.

The point is not to run them as often as possible. If I can get an agent to run effectively once a day, or four times a day, that scales, because the objective is something that runs when I am not looking. Removing myself from the loop, smoothly, is the whole game.

## What each wake needs

What a loop of agents needs before it can run without you: a schedule that lands in the right session; continuity of the session between wakes; secrets handed over once, by QR handshake; data that scales, a vault per stage; a record of every wake; and somewhere to see all of it. Learned while ten agents were taught to run in sequence on the PHP story.

My requirements are practical. I need to be able to see each execution. So I want each agent's runs to land in the same session, on the same machine, where I can open it and read what it did. That one choice solves a lot: the secrets the agent was given stay with it; the state stays where it was; and the data does not have to be fetched again on every wake. This is gigabytes of data by now, and you do not want clones of it all over the place.

The data side already uses our own technology. Each stage writes to a vault: the researcher's, then the curator's, which the journalist reads. The researcher's vault is also a good example of a limit found in use: it grew to 63,662 objects and 1.6 GB and pushed sgit past what it could do, until [pack mode](https://newsroom.sgit.ai/articles/a-tangent-that-shipped.html), one zip per push, fixed it.

And continuing the previous session matters for more than state. It matters for readability. When I come back to an agent, I want to read its history in the same place, in the same interface.

## How the platform got here

How scheduling agents got easier, one platform feature at a time: tools in the loop, where an agent is a session; scheduled runs, where each run opens a new session and secrets and state start again; a schedule into a chosen session, where the wake lands in a session already briefed and holding its keys; and, proposed, a dedicated account for the whole team.

This is where small features in the platforms matter a lot. I am using Claude here.

The first thing Claude did very well was the loop of tools: the model calls a tool, reads the result and carries on. Remember that early versions had barely any internet and no tools. Once that existed, an agent could be a Claude session, which is what we now have in Claude, ChatGPT and everywhere else.

Then came scheduling. That was good, but the way it worked in practice caused me a lot of problems: each scheduled run opened a new session. Claude Code's documentation still describes it that way: a run "opens as a full session, a new one for each run". For my purposes that meant no good way to give the run its secrets, no reuse of state, and, when you run several agents several times a day, an ever-growing list of sessions to open to see what happened. That does not scale, so I did not run my schedules that way.

Then, a couple of days ago, I realised I could schedule a wake into a specific session. It may be new, or it may have been there and I had not noticed. Either way, it is exactly what I needed. I can create a session with the model I want, brief it, and give it its key with [the QR handshake](https://newsroom.sgit.ai/articles/almost-working.html), which is our way of handing secrets to an agent. The agent then clones the repositories and the vaults, and from then on every scheduled wake arrives in that same session, already set up.

## Brittle, and why

It works, and it is still brittle. It took a day and a half to become somewhat reliable, and it is not fully there.

One example: the agents try to help. At one point an agent tried to set up its own schedule, but it could not see, or set, the schedule for another session, so the wake fired in the wrong place, in the wrong environment.

Another, from this morning. The [control room](https://php.oct.2026.newsroom.sgit.ai/team/control/index.html)'s wake timeline at 11:34 London showed 5 wakes met and 11 missed. Most of the misses were not failures of work. The conductor checked, and the researcher and the curator do run: the curator's 08:00 wake promoted 18 sources and took the evidence vault to 400. They just left no commit and no run record, so to the rest of the team they looked like they had not happened. The fix, at my go, was to make every scheduled wake's prompt small, with a shared wake procedure that always ends in a run record, and a way to publish that record without releasing the site.

The latest runs on the PHP site's schedule page, 25 October 2026: the conductor making every scheduled wake prompt small, with a new shared wake procedure and a run record that can be published without a release; the conductor's light check turned incident, because the researcher and the curator run but leave no record; the desk's morning line; and the factcheck's daily sweep.

None of this is exotic. It is what happens when four or five agents, then ten, have to work in sequence, unattended, on a platform whose limits you live with.

## Live with the platform, and keep less code

In the past I have wired this kind of thing myself, and you can. But it always works better when the platform you are on provides the service, because then the platform maintains it. That is where the details of how a platform works, and how commoditised a feature is, matter. So I live with the limitations of the platforms I use. Whatever is missing I code on top, and I always want to get rid of that code, because it is one more thing I have to maintain.

## Slowly, on purpose

This is why I do it slowly. Not because I cannot go faster, but because the pace buys understanding and confidence, and it builds the infrastructure that makes the next loop possible. The more control and visibility I have, the more agency I can give the agents, and the more loops I can run.

It is a good example of an [explorer](https://newsroom.sgit.ai/articles/explorer-coding.html) workflow that will become a product and code over time. The only way to get there is to run it, experiment, map it, and only then gain the confidence you get with products and commodities: the villagers and the town planners.

## Visibility is half the work

You need a lot of visualisation, and a lot of checks and balances. I have many of them already, and they are still where the most improvement is needed. On the PHP site, the agents built [the schedule](https://php.oct.2026.newsroom.sgit.ai/team/schedule/index.html), with every agent's card, wakes and runs; the control room, with the pipeline, the wake timeline and the decisions waiting on me; and [the journalist's desk](https://php.oct.2026.newsroom.sgit.ai/views/desk/index.html), with the pipeline after every export and what the correspondent caught. I spend as much time visualising, mapping and getting control of the setup of this environment as on the setup itself. I think that is the right ratio.

## The next step: an account of its own

There is one more problem, and it is mine. At the moment all of this runs in one of my main Claude accounts, the one I use for everything else, and it is clogging up my management of sessions. More than that, I want isolation.

So the next evolution, again the move from explorer to villager, is to give the team a dedicated account, perhaps a Team account, so I pay for another seat. Then I have good control of the costs, the usage and the models each agent uses, and all the information and all the flows are contained in one place. The good news is that most of the work is done. This is the tightening up: removing what is not needed, deleting what should not be there, and then gaining the resilience and confidence that only come from something running all the time.

## For platform builders: the unit of work is the platform

This is also what I always tell people who build platforms, especially platforms that do not run everywhere. Everything you build, your customers will need a part of. But the unit of work is not whatever you decide a user session is. The unit of work is your entire platform.

So users must be able to create complete, separate instances of the whole thing. That is what a new Claude session is: the whole unit of work. It is what AWS accounts are, in a way. Individual accounts, individual platform sessions, each with everything the platform does, including running wherever they are needed. It is a very powerful pattern, and it is the one I am about to use for the PHP team.

## What this does not claim

- **The timings are mine.** A day and a half to somewhat reliable is this pipeline's, not a measurement of the platform.
- **The scheduling history is my experience of it.** The documentation still describes a new session per cloud run; I do not know when scheduling into a chosen session arrived.
- **The misfired schedule is from my session,** not from a record on the site.
- **The dedicated account is a plan,** not yet done.
- **"Missed" on the timeline means no run record within 45 minutes,** not that no work was done.

## Where this comes from

My two voice memos of 25 October 2026. The PHP story site's [schedule](https://php.oct.2026.newsroom.sgit.ai/team/schedule/index.html), [control room](https://php.oct.2026.newsroom.sgit.ai/team/control/index.html) and [journalist's desk](https://php.oct.2026.newsroom.sgit.ai/views/desk/index.html), at release v0.19.1, captured on 25 October; its screenshots under its Apache-2.0 licence. Claude Code's documentation on [cloud scheduled tasks](https://code.claude.com/docs/en/routines.md) and [session-scoped scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks.md), read on 25 October. Related: [almost working](https://newsroom.sgit.ai/articles/almost-working.html), [a tangent that shipped](https://newsroom.sgit.ai/articles/a-tangent-that-shipped.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [PHP October 2026, update 3](https://newsroom.sgit.ai/articles/php-daily-2026-10-24.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#why-agent-loops-are-hard)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 279 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=279)

**Posting this article on LinkedIn?** The cover is [why-agent-loops-are-hard.jpg](banners/why-agent-loops-are-hard.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html)*
