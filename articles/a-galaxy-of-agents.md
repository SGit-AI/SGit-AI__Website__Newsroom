# A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way, sgit.ai

> The Galaxy is the view I kept coming back to at Web Summit. It is the Universe of the RiskMandate team, drawn as a solar system in the browser: the team at the centre, each person a sun, their agents in orbit, and the messages between agents travelling as arcs of light. It is not a mock-up. It reads the team's repositories live, every person's list of agents, every behaviour policy and each agent's latest commit, and counts a commit that names another agent as a message; tonight it showed 117 agents around six people, 222 messages and 50 pairs in conversation, and how many agents have no policy yet. Click an agent and you see its behaviour policy. It was built for the stand by Silvio Switha's dashboard agent, became the default view on 12 November, and has a calmer Simple view beside it. And it became a library, Gravity, versioned with a latest and a pinned folder, that can draw any system the same way: venues and events, or workloads across clouds.

*Source: <https://newsroom.sgit.ai/articles/a-galaxy-of-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way

# A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-20 · [article v1.0.0](versions/a-galaxy-of-agents.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · web-summitvisualisationagentsbehaviour-policiesriskmandategravityarticle

***Abstract:** The Galaxy is the view I kept coming back to at Web Summit. It is the Universe of the RiskMandate team, drawn as a solar system in the browser: the team at the centre, each person a sun, their agents in orbit, and the messages between agents travelling as arcs of light. It is not a mock-up. It reads the team's repositories live, every person's list of agents, every behaviour policy and each agent's latest commit, and counts a commit that names another agent as a message; tonight it showed 117 agents around six people, 222 messages and 50 pairs in conversation, and how many agents have no policy yet. Click an agent and you see its behaviour policy. It was built for the stand by Silvio Switha's dashboard agent, became the default view on 12 November, and has a calmer Simple view beside it. And it became a library, Gravity, versioned with a latest and a pinned folder, that can draw any system the same way: venues and events, or workloads across clouds.*

The Galaxy, read live on 20 November: 117 agents around six people, 222 messages between them.

## In short

- **The RiskMandate team as a solar system:** people as suns, agents in orbit, messages as light.
- **Live, not a mock-up:** read from the repositories every few minutes.
- **Each agent's behaviour policy is one click away,** and agents without one are counted.
- **Built for the stand,** the default view from 12 November, with a calm Simple view beside it.
- **It became Gravity,** a library that can draw any system as a universe.

## What it is

In the stand's command centre, the first tab is the Universe, and its default view is the Galaxy. At the centre is the team. Around it, each person is a sun; around each person, their agents are planets; and between the agents, the messages they send travel as arcs of light. Labels say how many agents each person runs and how many have no behaviour policy yet. Along the side, a timeline; along the bottom, the totals, and a box to ask Claude about what you see: who needs a policy?

When I captured it, early on 20 November, it showed 117 agents around six people, 222 messages and 50 pairs of agents in conversation.

## Live, not a mock-up

The Galaxy reads the team's repositories as they are: every person's list of agents, every behaviour policy, and each agent's latest commit from GitHub. A commit that names another agent counts as a message, so the arcs are the real traffic between agents, and the view refreshes every five minutes, falling back to a saved snapshot if it cannot read. The details of each agent's gaps are sealed to its developer's own key, so the public view shows the shape of the team without exposing what needs fixing.

Click an agent and its behaviour policy opens: what it may reach, what it was asked to do, and the gap ([feature behaviour policies](feature-behaviour-policies.md)). Beside the Galaxy, tabs bring in other views: the team, the messages, the deliveries, the X-ray ([the RiskMandate X-ray](the-riskmandate-x-ray.md)), and a replay of 300 enforcement runs from 11 November, marked as synthetic data.

## Built for the stand

The Galaxy was built for the stand by Silvio Switha's dashboard agent, in three.js with a bloom effect, inside the browser. It went through the usual week of a demo: light mode was dropped because it only worked dark; a loss of quality was found and fixed; a calmer Simple view was added for people who wanted it explained in a sentence; and on 12 November the Galaxy became the default again, with a switch between the two on the stand.

## It became Gravity

What started as one view became a library: [Gravity](https://web-summit.sgit.ai/lib/gravity/). It draws any system as a universe: a core, centres of gravity around it, the nodes that belong to each centre, and the flows between nodes. You fly into a centre, see it through a lens, then open one node's detail, in Portuguese or English, full screen, with extra views as plugins. The same library can draw the Lisbon Tech Fringe, its venues, sessions and events, or workloads spread across clouds and environments.

It is versioned the way we now want everything versioned: a `latest/` folder, always the newest, and pinned folders such as `v0/v0.1/v0.1.0/` that never change ([every tool its own website](every-tool-its-own-website.md)).

## Why it matters

A team of agents is hard to see. The Galaxy makes it visible in one look: who runs how many agents, who talks to whom, and where a policy is missing. That is what a customer of an agentic team wants on the wall ([an agentic console](an-agentic-console.md)), and it is a strong way to show behaviour policies at work.

## What this does not claim

- **The counts are one reading,** early on 20 November; they change as the repositories do.
- **The enforcement replay is synthetic data,** as its own panel says.
- **Gravity is at version 0.1.0.**

## Where this comes from

The command centre at [web-summit.sgit.ai](https://web-summit.sgit.ai/), captured on 20 November 2026, the [Gravity page](https://web-summit.sgit.ai/lib/gravity/), and the site's repository, [SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit): `assets/cc/stand.js`, `lib/gravity` and its versions log. Related: [the RiskMandate X-ray](the-riskmandate-x-ray.md), [the team's operating system](the-teams-operating-system.md), [an agentic console](an-agentic-console.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#a-galaxy-of-agents)

### Builds on

- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy](the-riskmandate-x-ray.md) The RiskMandate X-ray: type a company, see its AI helpers' reach, mandate and gap, built by four search agents for about a dime a company.
- [Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving](every-tool-its-own-website.md) Turning the 49 tools of tools.sgraph.ai into sovereign websites: one site each, simple first, pinned versions, signed hashes, a team of teams.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.

### Continued by

- [The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy](the-riskmandate-x-ray.md) The RiskMandate X-ray: type a company, see its AI helpers' reach, mandate and gap, built by four search agents for about a dime a company.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 511 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=511)

**Posting this article on LinkedIn?** The cover is [a-galaxy-of-agents.jpg](banners/a-galaxy-of-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-galaxy-of-agents.html)*
