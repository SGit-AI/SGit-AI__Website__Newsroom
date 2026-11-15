# Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step, sgit.ai

> When someone says "an agentic team", they could mean six very different things, and the difference decides what it costs, what it can reach and how you control it. At the bottom is a task: one action, one prompt. Then one agent that does the work and spawns nothing; an agent with sub-agents inside one runtime; several sessions, each in its own runtime; a conductor with its team of agents; and at the top, conductors of conductors, the swarm of swarms we ran at Web Summit, which can grow to thousands. The lower setups are a prompt; the higher ones are a setup, with keys, lanes, boards and policies. Inside every one of them sit the altitudes of a run we mapped in the Swarm demo of 12 November: the person, the swarm, the agent, the loop, the LLM call and the code, where the danger is the same privileges at every altitude, and the control is reach: don't hope the agent behaves, make the dangerous thing unreachable. The higher you go, the more you need visibility and command and control.

*Source: <https://newsroom.sgit.ai/articles/six-setups-of-an-agentic-system.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step

# Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/six-setups-of-an-agentic-system.md) · [newsroom v0.14.96](https://newsroom.sgit.ai/admin/versions.html) · agentic-teamsaltitudesswarmconductorscommand-and-controlreachabparticle

***Abstract:** When someone says "an agentic team", they could mean six very different things, and the difference decides what it costs, what it can reach and how you control it. At the bottom is a task: one action, one prompt. Then one agent that does the work and spawns nothing; an agent with sub-agents inside one runtime; several sessions, each in its own runtime; a conductor with its team of agents; and at the top, conductors of conductors, the swarm of swarms we ran at Web Summit, which can grow to thousands. The lower setups are a prompt; the higher ones are a setup, with keys, lanes, boards and policies. Inside every one of them sit the altitudes of a run we mapped in the Swarm demo of 12 November: the person, the swarm, the agent, the loop, the LLM call and the code, where the danger is the same privileges at every altitude, and the control is reach: don't hope the agent behaves, make the dangerous thing unreachable. The higher you go, the more you need visibility and command and control.*

Six setups of an agentic system, from a single task to conductors of conductors, and what each needs to set up.

## In short

- **"An agentic team" can mean six setups,** and the difference decides cost, reach and control.
- **From the bottom:** a task, one agent, an agent with sub-agents, several sessions, a conductor and its team, conductors of conductors.
- **The lower three are a prompt; the upper three are a setup,** with keys, lanes, boards and policies.
- **Inside every setup are the altitudes of a run:** person, swarm, agent, loop, LLM call, code.
- **The danger is the same privileges at every altitude;** the control is reach.
- **The higher you go, the more you need command and control.**

## Six setups

These are the six I see, from the bottom up:

1. **A task.** One action: a question, a command, a run. It is just a prompt.
2. **One agent.** A single session that does the work and does not spin anything off.
3. **An agent with sub-agents.** One Claude session managing its own sub-agents inside it, all sharing one runtime environment.
4. **Several sessions.** Different Claude sessions, one per role, each with its own runtime environment.
5. **A conductor and its agents.** One coordinator with a team of agents working together: what each person on the Web Summit team ran, Vicky Wang's team for example.
6. **Conductors of conductors.** A swarm of swarms: my conductor talking to every other person's conductor, each with its own team. This is the setup I ran at Web Summit, and it is the one that can go exponential, to thousands or tens of thousands of agents.

The first three are a prompt, or a prompt and a project. The last three are a setup: sessions, keys per agent, a board, lanes, vaults, and at the top, policies and observability. That is why they cost different amounts to set up ([selling mini agentic teams](selling-mini-agentic-teams.md)).

## The scale we ran

At Web Summit the top setup was real. Around 250 named agents worked for six people, with more than 60 sessions at once at the peak, and 220 of the 224 sessions were started by other sessions ([ten days at Web Summit](ten-days-at-web-summit.md)). When we needed every contact from the summit, I sent one message to my conductor, it messaged every other conductor, and each asked its own agents ([a brain you arrive at](a-brain-you-arrive-at.md)).

## Inside every setup: the altitudes of a run

The altitudes of a run, from the Swarm demo: person, swarm, agent, loop, LLM call, compute, and the control.

During the summit we mapped something else that I think is very powerful: the altitudes of a run. In the Swarm demo of 12 November, every unit of work was given an altitude: the person (P), a swarm that issues work to agents on other accounts (A4), an agent that plans and holds credentials (A3), a loop that reads, asks, checks and retries (A2), a single LLM call (A1), and plain code (A0).

The six setups and the altitudes are two views of the same thing. A setup says how the agents are arranged; the altitudes say what each unit of work is, and every setup contains them. Even a single agent runs loops, calls models and runs code.

## The danger, and the control

The altitudes showed the danger clearly. Running code with the privileges of a swarm is a massive vulnerability; so is a loop that can start agents, or code with connections to things it should not touch. In the biggest run we drew, 196 units, 48 loops and up to 96 at once, every one of them could have reached what the agent reached.

So the control is not good behaviour; it is reach. Each altitude should get only what it needs. The line we agreed for the demo says it best: don't hope the agent behaves, make the dangerous thing unreachable. That is the idea behind Agent Behaviour Policies ([what can your agent reach?](what-can-your-agent-reach.md)), and it applies at every setup.

## Command and control

The higher the setup, the more you need to see and steer it: who is running, what each one can reach, what it is doing, and how to stop them all. At the bottom, the prompt is the control. At the top, you need a control centre, keys, lanes, a stop that reaches every agent, and observability; our stops reached each agent only at its next wake ([always-on agents at team scale](always-on-agents-at-team-scale.md)).

I think command and control is what makes all of this possible, and it will be the subject of my next memo.

## What this does not claim

- **The six setups are a way to describe the options,** not a standard.
- **The altitudes and run figures come from the Swarm demo's records,** 11 and 12 November 2026; the privilege picture on the biggest run was drawn as an illustration.
- **This altitude is about runs and setups;** [approve at altitude](approve-at-altitude.md) uses the word for levels of decision, which is a related but different idea.

## Where this comes from

My own thinking, 15 November 2026; the Swarm repository behind [swarm.promptugal.news](https://swarm.promptugal.news/), its map and the story of 12 November on altitudes and reach, and its runs of 11 November. Earlier on this site: [ten days at Web Summit](ten-days-at-web-summit.md), [always-on agents at team scale](always-on-agents-at-team-scale.md), [approve at altitude](approve-at-altitude.md), [what can your agent reach?](what-can-your-agent-reach.md), and the companion article, [selling mini agentic teams](selling-mini-agentic-teams.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#six-setups-of-an-agentic-system)

### Builds on

- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.

### Continued by

- [Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all](spend-fewer-tokens.md) An agentic team's token bill is mostly a design choice: files as memory, caching, code where you can, the right model per step, static outputs, counting.
- [Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder](atomic-cells-end-to-end.md) AgentiCCells' first offering: a £500 website as an atomic cell, steered by the customer from their browser with a key, handed over to their GitHub.
- [Reading your way into an agentic team: eight public sites a new team should read before it builds anything, how an agent should read them, and ten questions to answer first, because our websites are its memory](reading-your-way-into-an-agentic-team.md) Eight public sites a new agentic team should read before it builds anything, how an agent should read them, and ten questions to answer first.
- [Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day](starting-agenticcells.md) AgentiCCells: a new company that sets up small agentic teams in the customer's environment, with a control centre, all open, no state on our side.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 408 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=408)

**Posting this article on LinkedIn?** The cover is [six-setups-of-an-agentic-system.jpg](banners/six-setups-of-an-agentic-system.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/six-setups-of-an-agentic-system.html)*
