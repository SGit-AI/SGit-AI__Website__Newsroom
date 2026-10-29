# A villager for the agents: a daily agent that does nothing but look for what to refactor and improve, because task-focused agents rarely step back, and why the PHP story's every release now rewrites two thousand files, sgit.ai

> The PHP story now has 23 agents, 12 of them on schedules, each with a good brief and each focused on its own job. That focus is also a blind spot. Agents that do a particular task rarely step back and ask how the whole could be improved, or what should be refactored. The PHP site shows the cost. Its version is stamped on every page, so every release rewrites the whole site: the last 20 releases each changed between 1,950 and 2,227 files, whatever they were for. One repository, one build, one gate and one board file serve every agent, and since 23 October 28 release messages name a conflict, a collision or a renumbering. When I asked, the dev agent proposed splitting the site into six repositories, each with its own writers, version and gate. That is a good engineering problem to have, and it is the kind of thing nobody notices while doing their own task. So I am adding a villager: an agent that runs once a day, reads what changed, asks why problems happened and where things could be better, and leaves recommendations for each agent. It does not have to act straight away. And, beside the security check every agent already does, every agent should do a quality check: a comment, not necessarily a change. The project is not ready for a town planner yet. It is ready for someone to keep an eye on quality.

*Source: <https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A villager for the agents: a daily agent that does nothing but look for what to refactor and improve, because task-focused agents rarely step back, and why the PHP story's every release now rewrites two thousand files

# A villager for the agents: a daily agent that does nothing but look for what to refactor and improve, because task-focused agents rarely step back, and why the PHP story's every release now rewrites two thousand files

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-25 · [article v1.1.0, 2 versions](versions/a-villager-for-the-agents.md) · [newsroom v0.13.75](https://newsroom.sgit.ai/admin/versions.html) · agentsrefactoringqualityexplorers-villagersengineeringarticle

***Abstract:** The PHP story now has 23 agents, 12 of them on schedules, each with a good brief and each focused on its own job. That focus is also a blind spot. Agents that do a particular task rarely step back and ask how the whole could be improved, or what should be refactored. The PHP site shows the cost. Its version is stamped on every page, so every release rewrites the whole site: the last 20 releases each changed between 1,950 and 2,227 files, whatever they were for. One repository, one build, one gate and one board file serve every agent, and since 23 October 28 release messages name a conflict, a collision or a renumbering. When I asked, the dev agent proposed splitting the site into six repositories, each with its own writers, version and gate. That is a good engineering problem to have, and it is the kind of thing nobody notices while doing their own task. So I am adding a villager: an agent that runs once a day, reads what changed, asks why problems happened and where things could be better, and leaves recommendations for each agent. It does not have to act straight away. And, beside the security check every agent already does, every agent should do a quality check: a comment, not necessarily a change. The project is not ready for a town planner yet. It is ready for someone to keep an eye on quality.*

A villager beside the explorers: task agents, security, the villager and, later, the town planner.

## In short

- **23 agents, 12 on schedules,** each with a good brief and each focused on its own task.
- **That focus is a blind spot.** Task-focused agents rarely step back and ask what should be refactored.
- **The cost is visible.** Every release now rewrites about two thousand files, whatever it changed.
- **The dev agent saw it when asked.** It proposed splitting one repository into six.
- **So: a villager.** One agent, once a day, that only looks for what to improve, and why.
- **And a quality check on every wake,** beside the security check. A comment, not necessarily a change.
- **Not yet a town planner.** The project is not ready for one. It is ready for someone to watch quality.

## A team of explorers

The PHP story's team is now large. Its status data lists 23 agents; 12 have schedule cards and wake on their own, about 53 times a day: the conductor every hour, the Sherpa every two hours, the researcher, curator, journalist and correspondent five times each, the fact-check desk four, and, since 25 October, the security agent once a day at 22:35 London. Each has a brief, and the latest briefs are good. They are working, and some of them have started refactoring their own parts.

But each of them is focused on a particular task. That is what makes them effective, and it is also the blind spot of a lot of AI models and AI workflows: because they focus on the task in front of them, they do not take a step back and ask how the system could be improved, or what should be refactored. A researcher captures. A journalist publishes. Nobody's job is to notice that the way they all publish has become expensive. In the language of [explorers, villagers and town planners](https://newsroom.sgit.ai/articles/explorer-coding.html), they are explorers, and good ones.

## What it costs: every release rewrites the site

Every release rewrites the whole site: files changed by the PHP site's last 20 releases, against the repository's total.

Here is the kind of thing nobody notices while doing their own task. The PHP site stamps its version on every page. So every release, whether it is a redesign or one agent's run record, rewrites every page. Across the last 20 releases, each one changed between 1,950 and 2,227 files, with a median of 2,140, in a repository of about 3,300 files. A change of a few lines becomes a commit that touches two thousand. That is a good engineering problem to have: it means the site is busy and growing. But it is a problem.

It is not the only one. One repository, one build, one gate and one board file serve every agent. The board file, which records what every agent is waiting on, was touched by 70 commits in three days. Since 23 October, 28 release messages name a conflict, a collision or a renumbering, and board rows have been renumbered by hand 11 times. Every release, whatever its size, takes in everything every other agent released, rebuilds over a thousand pages and passes the whole gate, 42 seconds to build and 74 to prove the build is deterministic. And the researcher's and the curator's wakes of 24 and 25 October did their work but left nothing in the repository, partly because a wake that touches the repository pays for all of it.

## What the dev agent saw, when asked

The dev agent's proposal on the PHP site, 25 October 2026: one repository into six, and what one costs today.

When I asked the dev agent to look at the whole, it saw all of this at once, and wrote [a proposal](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/index.html): split the site into six repositories, kit, data, references, updates, the main site and the team, each with one group of writers, its own version, its own gate and its own site, meeting only through published, versioned addresses. Its principle is a good one: "Split along who writes and how often, not along technology." And its diagnosis is exactly right: "The cause is not the number of agents. It is that one version, one build, one gate, one board file and one output tree serve everything." It also proposes the obvious first fix: no version stamp on every page.

Nothing has moved yet; the decisions are mine. But notice how it happened. The insight came because I asked an agent to step back. Nothing in the agents' normal work would have produced it. That is the gap.

## The villager

So I am adding a villager to the team. An agent that runs every day, and is focused exclusively on recommendations: what to refactor, what to improve, and guidance for each of the other agents.

It reads what changed since its last run: the releases, the commits, the run records, the conflicts, the gate's timings, the board. And it asks the villager's questions. Not only "what is wrong?", but why did it happen? What is the bug? Where is the problem? Where is the place where a change would improve the most? Then it writes recommendations, addressed to the agent that owns each part, in the place the team already uses to talk to each other: the notes in their commits and the board.

It does not need to act straight away, and mostly it should not. Its job is to make the team aware: we need to do some refactoring here, this is why, and this is what it would buy. The agents that own the code decide, with me, when.

## A quality check on every wake

The villager runs once a day. But there is a smaller version of the same idea that every agent can do on every wake.

The PHP team already does a security check on every release: on 25 October the gate became stricter, and it now fails on inline event handlers, pages without a safe Content-Security-Policy, forged message headers and more. A security pass runs once a day on top of that. In the same way, every agent should do a quality check when it runs: a short comment on what it noticed. Was this slower than it should be? Did I fight a conflict? Did I copy something that should be shared? Did I touch two thousand files to change ten lines? A comment, not a change. The villager reads them all, and turns them into recommendations.

That is the villager's habit, spread across the team: doing the work, and also noticing how the work could be better.

## Not yet a town planner

I do not think this project is ready for a town planner, someone who sets the standards, builds the shared components and runs the platform the others build on. Eventually it will be, and the six-repository proposal already points that way, with a kit that every site uses. But a town planner too early freezes things that are still changing. What the project needs now is someone keeping an eye on quality, understanding why things happen, and making the team aware. That is the villager.

## What this does not claim

- **The villager does not exist yet.** This is the plan; its brief and schedule card come next.
- **The proposal is not decided.** Nothing has moved; the six repositories are the dev agent's recommendation.
- **The file counts are from the git history** of the last 20 releases to v0.21.6; the dev agent's own figure, at v0.20.0, is a median of 1,936 generated files.
- **Some agents already refactor their own parts.** The villager is for what no single agent sees.

## Where this comes from

My voice memo of 25 October 2026. The PHP story site at release v0.21.6, read on 25 October: the dev agent's [proposal, one repository into six](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/index.html), published at 12:33 UTC; its git history (files changed by the last 20 releases); its team status data (23 agents) and schedule cards (12 active, including security's daily pass); the release v0.20.3 that made the security gate stricter; its screenshots under its Apache-2.0 licence. Related: [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#a-villager-for-the-agents)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 282 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=282)

**Posting this article on LinkedIn?** The cover is [a-villager-for-the-agents.jpg](banners/a-villager-for-the-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html)*
