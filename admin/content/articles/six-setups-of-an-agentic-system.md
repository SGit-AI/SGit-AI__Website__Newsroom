---
title: Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: When someone says "an agentic team", they could mean six very different things, and the difference decides what it costs, what it can reach and how you control it. At the bottom is a task: one action, one prompt. Then one agent that does the work and spawns nothing; an agent with sub-agents inside one runtime; several sessions, each in its own runtime; a conductor with its team of agents; and at the top, conductors of conductors, the swarm of swarms we ran at Web Summit, which can grow to thousands. The lower setups are a prompt; the higher ones are a setup, with keys, lanes, boards and policies. Inside every one of them sit the altitudes of a run we mapped in the Swarm demo of 12 November: the person, the swarm, the agent, the loop, the LLM call and the code, where the danger is the same privileges at every altitude, and the control is reach: don't hope the agent behaves, make the dangerous thing unreachable. The higher you go, the more you need visibility and command and control.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agentic-teams, altitudes, swarm, conductors, command-and-control, reach, abp, article
status: published
---

!shot ats-setups.webp | images/ | Six setups of an agentic system, from a single task to conductors of conductors, and what each needs to set up. | concept

## In short {#in-short}

- **"An agentic team" can mean six setups,** and the difference decides cost, reach and control.
- **From the bottom:** a task, one agent, an agent with sub-agents, several sessions, a conductor and its team, conductors of conductors.
- **The lower three are a prompt; the upper three are a setup,** with keys, lanes, boards and policies.
- **Inside every setup are the altitudes of a run:** person, swarm, agent, loop, LLM call, code.
- **The danger is the same privileges at every altitude;** the control is reach.
- **The higher you go, the more you need command and control.**

## Six setups {#setups}

These are the six I see, from the bottom up:

1. **A task.** One action: a question, a command, a run. It is just a prompt.
2. **One agent.** A single session that does the work and does not spin anything off.
3. **An agent with sub-agents.** One Claude session managing its own sub-agents inside it, all sharing one runtime environment.
4. **Several sessions.** Different Claude sessions, one per role, each with its own runtime environment.
5. **A conductor and its agents.** One coordinator with a team of agents working together: what each person on the Web Summit team ran, Vicky Wang's team for example.
6. **Conductors of conductors.** A swarm of swarms: my conductor talking to every other person's conductor, each with its own team. This is the setup I ran at Web Summit, and it is the one that can go exponential, to thousands or tens of thousands of agents.

The first three are a prompt, or a prompt and a project. The last three are a setup: sessions, keys per agent, a board, lanes, vaults, and at the top, policies and observability. That is why they cost different amounts to set up ([selling mini agentic teams](/articles/selling-mini-agentic-teams.html)).

## The scale we ran {#scale}

At Web Summit the top setup was real. Around 250 named agents worked for six people, with more than 60 sessions at once at the peak, and 220 of the 224 sessions were started by other sessions ([ten days at Web Summit](/articles/ten-days-at-web-summit.html)). When we needed every contact from the summit, I sent one message to my conductor, it messaged every other conductor, and each asked its own agents ([a brain you arrive at](/articles/a-brain-you-arrive-at.html)).

## Inside every setup: the altitudes of a run {#altitudes}

!shot ats-altitudes.webp | images/ | The altitudes of a run, from the Swarm demo: person, swarm, agent, loop, LLM call, compute, and the control. | concept

During the summit we mapped something else that I think is very powerful: the altitudes of a run. In the Swarm demo of 12 November, every unit of work was given an altitude: the person (P), a swarm that issues work to agents on other accounts (A4), an agent that plans and holds credentials (A3), a loop that reads, asks, checks and retries (A2), a single LLM call (A1), and plain code (A0).

The six setups and the altitudes are two views of the same thing. A setup says how the agents are arranged; the altitudes say what each unit of work is, and every setup contains them. Even a single agent runs loops, calls models and runs code.

## The danger, and the control {#control}

The altitudes showed the danger clearly. Running code with the privileges of a swarm is a massive vulnerability; so is a loop that can start agents, or code with connections to things it should not touch. In the biggest run we drew, 196 units, 48 loops and up to 96 at once, every one of them could have reached what the agent reached.

So the control is not good behaviour; it is reach. Each altitude should get only what it needs. The line we agreed for the demo says it best: don't hope the agent behaves, make the dangerous thing unreachable. That is the idea behind Agent Behaviour Policies ([what can your agent reach?](/articles/what-can-your-agent-reach.html)), and it applies at every setup.

## Command and control {#command}

The higher the setup, the more you need to see and steer it: who is running, what each one can reach, what it is doing, and how to stop them all. At the bottom, the prompt is the control. At the top, you need a control centre, keys, lanes, a stop that reaches every agent, and observability; our stops reached each agent only at its next wake ([always-on agents at team scale](/articles/always-on-agents-at-team-scale.html)).

I think command and control is what makes all of this possible, and it will be the subject of my next memo.

## What this does not claim {#limits}

- **The six setups are a way to describe the options,** not a standard.
- **The altitudes and run figures come from the Swarm demo's records,** 11 and 12 November 2026; the privilege picture on the biggest run was drawn as an illustration.
- **This altitude is about runs and setups;** [approve at altitude](/articles/approve-at-altitude.html) uses the word for levels of decision, which is a related but different idea.

## Where this comes from {#sources}

My own thinking, 15 November 2026; the Swarm repository behind [swarm.promptugal.news](https://swarm.promptugal.news/), its map and the story of 12 November on altitudes and reach, and its runs of 11 November. Earlier on this site: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [always-on agents at team scale](/articles/always-on-agents-at-team-scale.html), [approve at altitude](/articles/approve-at-altitude.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html), and the companion article, [selling mini agentic teams](/articles/selling-mini-agentic-teams.html).
