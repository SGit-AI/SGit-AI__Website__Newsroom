---
title: A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way
date: 2026-11-20
author: Dinis Cruz
author_url: about/index.html
summary: The Galaxy is the view I kept coming back to at Web Summit. It is the Universe of the RiskMandate team, drawn as a solar system in the browser: the team at the centre, each person a sun, their agents in orbit, and the messages between agents travelling as arcs of light. It is not a mock-up. It reads the team's repositories live, every person's list of agents, every behaviour policy and each agent's latest commit, and counts a commit that names another agent as a message; tonight it showed 117 agents around six people, 222 messages and 50 pairs in conversation, and how many agents have no policy yet. Click an agent and you see its behaviour policy. It was built for the stand by Silvio Switha's dashboard agent, became the default view on 12 November, and has a calmer Simple view beside it. And it became a library, Gravity, versioned with a latest and a pinned folder, that can draw any system the same way: venues and events, or workloads across clouds.
version: v0.14.181
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, visualisation, agents, behaviour-policies, riskmandate, gravity, article
status: published
---

!shot wsg-galaxy.webp | images/ | The Galaxy, read live on 20 November: 117 agents around six people, 222 messages between them. | screenshot

## In short {#in-short}

- **The RiskMandate team as a solar system:** people as suns, agents in orbit, messages as light.
- **Live, not a mock-up:** read from the repositories every few minutes.
- **Each agent's behaviour policy is one click away,** and agents without one are counted.
- **Built for the stand,** the default view from 12 November, with a calm Simple view beside it.
- **It became Gravity,** a library that can draw any system as a universe.

## What it is {#what}

In the stand's command centre, the first tab is the Universe, and its default view is the Galaxy. At the centre is the team. Around it, each person is a sun; around each person, their agents are planets; and between the agents, the messages they send travel as arcs of light. Labels say how many agents each person runs and how many have no behaviour policy yet. Along the side, a timeline; along the bottom, the totals, and a box to ask Claude about what you see: who needs a policy?

When I captured it, early on 20 November, it showed 117 agents around six people, 222 messages and 50 pairs of agents in conversation.

## Live, not a mock-up {#live}

The Galaxy reads the team's repositories as they are: every person's list of agents, every behaviour policy, and each agent's latest commit from GitHub. A commit that names another agent counts as a message, so the arcs are the real traffic between agents, and the view refreshes every five minutes, falling back to a saved snapshot if it cannot read. The details of each agent's gaps are sealed to its developer's own key, so the public view shows the shape of the team without exposing what needs fixing.

Click an agent and its behaviour policy opens: what it may reach, what it was asked to do, and the gap ([feature behaviour policies](/articles/feature-behaviour-policies.html)). Beside the Galaxy, tabs bring in other views: the team, the messages, the deliveries, the X-ray ([the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html)), and a replay of 300 enforcement runs from 11 November, marked as synthetic data.

## Built for the stand {#stand}

The Galaxy was built for the stand by Silvio Switha's dashboard agent, in three.js with a bloom effect, inside the browser. It went through the usual week of a demo: light mode was dropped because it only worked dark; a loss of quality was found and fixed; a calmer Simple view was added for people who wanted it explained in a sentence; and on 12 November the Galaxy became the default again, with a switch between the two on the stand.

## It became Gravity {#gravity}

What started as one view became a library: [Gravity](https://web-summit.sgit.ai/lib/gravity/). It draws any system as a universe: a core, centres of gravity around it, the nodes that belong to each centre, and the flows between nodes. You fly into a centre, see it through a lens, then open one node's detail, in Portuguese or English, full screen, with extra views as plugins. The same library can draw the Lisbon Tech Fringe, its venues, sessions and events, or workloads spread across clouds and environments.

It is versioned the way we now want everything versioned: a `latest/` folder, always the newest, and pinned folders such as `v0/v0.1/v0.1.0/` that never change ([every tool its own website](/articles/every-tool-its-own-website.html)).

## Why it matters {#why}

A team of agents is hard to see. The Galaxy makes it visible in one look: who runs how many agents, who talks to whom, and where a policy is missing. That is what a customer of an agentic team wants on the wall ([an agentic console](/articles/an-agentic-console.html)), and it is a strong way to show behaviour policies at work.

## What this does not claim {#limits}

- **The counts are one reading,** early on 20 November; they change as the repositories do.
- **The enforcement replay is synthetic data,** as its own panel says.
- **Gravity is at version 0.1.0.**

## Where this comes from {#sources}

The command centre at [web-summit.sgit.ai](https://web-summit.sgit.ai/), captured on 20 November 2026, the [Gravity page](https://web-summit.sgit.ai/lib/gravity/), and the site's repository, [SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit): `assets/cc/stand.js`, `lib/gravity` and its versions log. Related: [the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html), [the team's operating system](/articles/the-teams-operating-system.html), [an agentic console](/articles/an-agentic-console.html).
