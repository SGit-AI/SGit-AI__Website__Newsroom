---
title: Agents need direction: how agent roles differ from human ones, why one focused agent can also be a developer, a designer and a data scientist, why that power has to be contained, and teams that send each other pull requests
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: The agents in our newsrooms are different from people in a few important ways, some good and some not. A line that keeps coming back in our own work is that agents can go in all directions, so they need direction. They can do a lot, and when they are not contained they cause damage: the technical debt that made us add a villager is a sign of it. But they have something we never had. Each agent runs on a model that can reason, learn and fetch what it needs, so a role focused on one thing also brings every other skill with it. My brief for the historian asks for a historian, and also a data scientist, a designer, a developer and an architect. That is powerful, and it has to be contained: the historian's role file lists the paths it may write, the shared files it may only append to, and what needs my go. Containing it means agents giving guidance to other agents, which gets complex fast, and that is where people come in: focus, ownership, and sometimes slowing things down. The refactoring we are doing now is cheaper because we did not automate too far. And one principle we can now scale: teams that send each other pull requests, an agent building what it needs as an explorer and handing it to the owning team, for the villagers and later the town planners to refactor or replace.
version: v0.13.78
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, explorers-villagers, engineering, teams, pull-requests, article
status: published
---

!shot dr-many.webp | images/ | One role, many skills, one scope: the historian at the centre, the roles it can also be, and the scope that contains it. | concept

## In short {#in-short}

- **Agents can go in all directions, so they need direction.** Uncontained, they cause damage.
- **But every agent brings every skill.** A focused role is also a developer, a designer, a data scientist.
- **That power has to be contained.** Scope, guidelines, and agents guiding other agents.
- **That is where people come in.** Focus, ownership, and sometimes slowing down.
- **Go slow to go fast.** The refactoring now is cheaper because we did not automate too far.
- **Teams should send each other pull requests.** Explorer code, handed to the owning team.

## Different from people, in good ways and bad {#different}

These agent roles are different from human roles, in some good ways and some not so good. A line from our own workflow puts it well: agents can go in all directions, so they need direction. I wrote it first in [jobs that never scaled](https://newsroom.sgit.ai/articles/jobs-that-never-scaled.html).

Because agents have so many skills, and can do so much, they can also cause a lot of damage, and they need a lot of direction. The reason we now need [a villager](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html) on the PHP story is exactly that: many agents, each working on its own task, and the technical debt that comes from nobody stepping back. Every release rewrites about two thousand files, and 28 release messages since 23 October name a conflict, a collision or a renumbering.

## One role, every skill {#every-skill}

But the agents also have something we never had. Each one runs on a model that can reason, learn and fetch new data. In effect, every agent has access to whatever other skills it needs, and can do much of that work itself.

Take the historian. In [who creates the original?](https://newsroom.sgit.ai/articles/who-creates-the-original.html) I gave it a new job: map where the story's data comes from. But my brief does not stop there. It says: build the visualisations, do the data science, build the pages. So I am asking the historian to be a historian, and also a data scientist, a designer, a developer and an architect. A human team would need five people for that.

That is the power of these agents. I can create an agent focused on one thing, knowing that it also understands Git, and the core primitives of everything we do. That is very useful.

## Contained {#contained}

Of course, it has to be contained. You do not want the historian going to town on the code and ignoring the team's guidelines. On the PHP site, [the historian's role file](https://php.oct.2026.newsroom.sgit.ai/admin/agents/historian/index.html) already draws that line: the paths it may write, exclusively; the shared files it may only append to, in its own block or row; the pages it owns; and what needs the editor's go. When the site is split into six repositories, as [the plan agreed on 25 October](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/index.html) proposes, that line moves from a rule the agent is expected to keep to a boundary GitHub enforces: an agent cannot write a repository it does not hold.

But containing agents means each agent also has to give guidance to the others: the developer's guidelines to the historian, the designer's patterns to the journalist, security's checks to everyone. You can see how complex that gets, very fast.

## Where the people come in {#people}

That is where we need people: to give the work focus and ownership, and sometimes to slow it down.

The fact that I am a bottleneck in some of these workflows is important. It gives us time to think, to find better ways, and to refactor. The big refactoring we are doing right now, one repository into six, is more cost-effective because we did not go too far down the path first, and did not automate too much. Go slow to go fast.

What is new is that we can now iterate very fast, add features very fast, and also think and experiment very fast. There are already tools on these sites that have not been fully used, because I focus on the points of highest leverage. That choice is the human part of the job. It is also why [the call for help](https://newsroom.sgit.ai/articles/a-call-for-help.html) asks for a person in every role.

## Teams that send each other pull requests {#pull-requests}

!shot dr-flow.webp | images/ | Teams that send each other pull requests: an explorer builds, the owner reviews, villagers refactor, planners replace. | process

There is one more property of these focused agents. They can ask other agents for work, and they can also do some of that work themselves. That brings back a principle I have held for a long time: when one team interacts with another, it should send that team pull requests. It should contribute to the other team, not only ask. In corporate environments that never really worked. Open source has some of it, as with [our first pull request into Ruflo](https://newsroom.sgit.ai/articles/our-first-pr-in-ruflo.html), and our own [chapter-by-chapter patches to the book](https://newsroom.sgit.ai/articles/a-pull-request-by-another-name.html). Now we can scale it.

So an agent that needs something from another team should not wait, and should not edit the other team's files. It builds what it needs, as an [explorer](https://newsroom.sgit.ai/articles/explorer-coding.html), in its own space, and sends it to the owning team as a pull request: here is what I needed, and here is a version that works. Then the villagers, agents and people, pick it up and refactor it to the team's guidelines. And when the pattern is clear, the town planners replace it with shared code.

Today the PHP site's agents cannot do this. They write their own paths, append to shared files in their own rows, and send each other messages: 26 so far. Six repositories, with owners, will make pull requests between teams the natural way to work.

## What exists, and what is proposed {#exists}

- **Exists:** focused agents with scope in their role files; messages between agents; the villager proposed; the plan to split the site into six repositories, agreed on 25 October.
- **Proposed:** the historian's brief with data science and pages; pull requests between agent teams; GitHub enforcing each repository's owners.

## What this does not claim {#limits}

- **The skills are the model's, not the agent's own.** Quality still depends on the brief and the review.
- **The release and conflict numbers are from the PHP site's history,** as counted in [a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html).
- **No agent has sent another team a pull request yet.**

## Where this comes from {#sources}

My voice memo of 25 October 2026. The PHP story site at release v0.22.0, read on 25 October 2026: the historian's role file, the agents' messages, and the dev agent's proposal and plan to split the site into six repositories. Related: [who creates the original?](https://newsroom.sgit.ai/articles/who-creates-the-original.html), [a call for help](https://newsroom.sgit.ai/articles/a-call-for-help.html), [a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [jobs that never scaled](https://newsroom.sgit.ai/articles/jobs-that-never-scaled.html), [our first PR in Ruflo](https://newsroom.sgit.ai/articles/our-first-pr-in-ruflo.html), [a pull request by another name](https://newsroom.sgit.ai/articles/a-pull-request-by-another-name.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
