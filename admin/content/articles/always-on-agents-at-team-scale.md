---
title: Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: On 13 November, William Hu of Anthropic published Building always-on agents, the patterns Anthropic recommends for agents that sleep, wake on an event, do their work and go back to sleep. It rests on five primitives: an event inbox, timers, memory, permissions and an outbox. Reading it, I recognised every box, because in the ten days around Web Summit six of us ran around 250 named agents on the same shape, built from different material: git, files, encrypted vaults and keys instead of database tables and workers. This is a side-by-side comparison, not a claim that ours is better: where we agree, with evidence from our own records; where we got it wrong, such as a newsroom that kept running for nine days on "nothing new"; and the next problems the post's one-agent-per-user design does not need to answer yet, but a team does: agents starting agents, identity, stopping a hundred of them at once, many humans, seeing what happened, and governance. We run on Claude Code, so some of the post's answers are literally what protected our agents.
version: v0.14.90
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, always-on-agents, anthropic, claude, architecture, web-summit, governance, riskmandate, article
status: published
---

!shot aoa-primitives.webp | images/ | Anthropic's five primitives for an always-on agent, beside what we built for around 250 agents at Web Summit. | comparison

## In short {#in-short}

- **Anthropic has published its patterns for always-on agents:** [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), by William Hu, 13 November 2026.
- **Five primitives:** an event inbox, timers, memory, permissions and an outbox, around agents that mostly sleep and wake in short runs.
- **We built the same five,** for around 250 named agents and six people at Web Summit, from git, files, encrypted vaults and keys.
- **Where we agree,** we can show it in our records; **where we were wrong,** the post would have helped.
- **Then come the next problems,** the ones a team of agents meets: agents starting agents, identity, stopping, many humans, seeing it, governance.
- **This is a comparison, not a contest.** We run on Claude Code, and some of the post's answers protected our agents.

## The post {#post}

The post's starting point is that "always on" describes what the user experiences, not what the agent does. The agent mostly sleeps. An event wakes it, it does the task, it saves what happened, and it goes back to sleep. In William's words, "Always-on agents are stateful and proactive", and they run on the same loop as any other agent, with a different architecture around it.

That architecture has five primitives. An **event inbox** is the durable list of things that happened, with one worker at a time. **Timers** are follow-ups the agent sets itself and schedules on a known cadence, and they never start a run directly: a scheduler turns them into inbox events. **Memory** holds only "what the agent can't look up again", in files, and a later process it calls dreaming curates it. **Permissions** are where "always-on agents carry the most risk": credentials stay in a proxy outside the agent, classifiers review risky actions, and a deferred tool call ends the run until a person answers. The **outbox** delivers outcomes, not steps, and the advice is to "start quiet and then earn more of the user's attention over time".

It is written for one agent per user, built from database tables, handlers and workers. That is the right place to start.

## The same five boxes, in different material {#mapping}

In the ten days around Web Summit, six of us (Angelo Leggio, Vicky Wang, Silvio Switha, José Bota, Indi Gupte and I) ran around 250 named agents across fifteen repositories, with more than 60 working at once at the peak. Nobody had written this post yet, and we arrived at the same five boxes:

- **Event inbox.** Each agent has its own inbox lane, an append-only channel whose token is sealed to that agent's key, so everything needed to message it is public and only it can read ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)). The work itself sits on the board, 219 items as files in git, which is the durable list of what needs doing.
- **Timers.** Our agents wake on scheduled tasks that fire into their session. This newsroom works that way: it wakes twice a day to publish the next article in [the Ten days series](/articles/ten-days-at-web-summit.html), and sets itself check-ins when it waits on something.
- **Memory.** The repository is the memory. Each site keeps a REALITY file, and its rule is that a thing not written there does not exist. Briefs are kept close to the words they came from, and when a role moves to a fresh session, it leaves a HANDOVER.md for the next one.
- **Permissions.** Every agent makes its own key pair and publishes the public half, 108 keys on the team's site by the end. Secrets are sealed to exactly the agents that need them, commits are signed, and every push is scanned for leaks first. Above that sits the question RiskMandate asks: what can this agent reach, against what was it asked to do ([the team's operating system](/articles/the-teams-operating-system.html)).
- **Outbox.** The site is the outbox. Every push is a release, each person has a command centre on their phone, and a "For me" bell collects what needs them.

## Where we agree, and the evidence {#agree}

Three of the post's rules are ones we learned the expensive way.

**"The inbox should be the source of truth."** Ours is files in git, so a fresh session can read the whole state of the team in one clone, and nothing important lives only in a session that might end. An agent reads 219 board items faster than it can click through any tool.

**"Memory should only hold what the agent can't look up again."** This is the hand-over rule. On the Storm Charles site alone there were 147 session keys and 106 hand-overs: roles passed to a fresh session with a key and a short note, because, as the team put it, starting again is cheaper than remembering. The note points to the repository; it does not copy it.

**"Start quiet."** We learned this one by getting it wrong. October's PHP newsroom was meant to wind down, and its agents went on waking for nine days, reporting "nothing new" each time; its observability lane filled up, and four days of telemetry were lost. An outbox that cannot decide nothing needs sending is noise, and noise hides the signal you need.

The post's cost point also matched our numbers. It says to keep each run's overhead lean and use prompt caching; the Storm Charles site used 3.84 billion tokens, and 98.7% of them were cache reads.

## The next problems, once there are many {#next}

!shot aoa-next.webp | images/ | Six problems a team of always-on agents meets that one agent per user does not, from our ten days. | concept

The post is about one agent per user, and says so. Once there are many agents and many people, the same five boxes meet new problems. None of these are gaps in the post; they are what comes next:

- **A team of agents.** Of the 224 Claude Code sessions created in those ten days, 220 were started by other sessions. Agents ran as conductors, roles and hand-overs, so an inbox event could be a brief from another agent, not a person.
- **Identity.** Every agent was named `role@project.person` and held its own key, so every commit and message says whose agent made it. With one agent per user, the user is the identity; with 250, it has to be designed.
- **Stopping.** On 9 November at 23:30 we paused every agent, the Big Stop; on 12 November came a hand brake and a final HOLD. Each one reached an agent only at its next wake, 5 to 33 minutes later, and background pollers kept going. In the post's terms: a stop is an event, and it is only as fast as the timers.
- **Many humans.** Six people, each with their own agents, conductor and command centre, shared one board. Whose attention an outbox earns depends on whose agent it is.
- **Seeing it.** The post leaves observability mostly to evals. With more than 60 agents at once, we needed it as a lane of its own: who read what, which agent did what, and what it cost.
- **Governance.** The post's permissions decide, call by call, whether to proceed, block or wait. A team also needs the record above the calls: what each agent may reach, what it was asked to do, and the gap between them. That gap is what RiskMandate is about.

## What we owe the post {#owe}

We run on Claude Code, so some of the post's answers are not parallels to ours; they are ours. The credential proxy that adds credentials outside the agent's environment, and the auto mode that reviews risky actions, sat underneath every one of our agents.

And some of our boxes were rougher than the post's. Our REALITY files fell behind in the busiest days; our stops were only as fast as our wakes; and the PHP newsroom's outbox never learned to stay quiet. A durable inbox with one worker, timers that write events instead of starting runs, and an outbox that can decide nothing needs sending would each have helped. The next version of what we run should borrow them.

## What this does not claim {#limits}

- **This is not a claim that our design is better.** It is a different starting point, a team instead of one agent per user, and the comparison is box by box.
- **Our figures are from our own records,** 3 to 13 November 2026, as published in the Ten days series; "around 250" counts distinct agent names in commits.
- **The post's content is summarised from its text,** read on 15 November 2026; the quotes are William Hu's.
- **Nothing here was reviewed by Anthropic.**

## Where this comes from {#sources}

William Hu, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), claude.com, 13 November 2026, read 15 November 2026. Our records: the repositories behind web-summit.sgit.ai, Storm Charles and the PHP newsroom, and the session list for the account, as summarised in [ten days at Web Summit](/articles/ten-days-at-web-summit.html) and [the team's operating system](/articles/the-teams-operating-system.html). Earlier on this site: [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [a key for every person](/articles/a-key-for-every-person.html), [handing secrets to agents](/articles/handing-secrets-to-agents.html), [who owns the stop button](/articles/who-owns-the-stop-button.html).
