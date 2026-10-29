---
title: A team frozen in time: agent sessions with a mandate, a role and a repository, paused and picked up again, and why that changes what happens when the people who built a system move on
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: Every project has a moment when the team is sharp, everyone is there, and features ship fast. Then the project dries out, the goals are met, or the company is sold, and the team moves on, taking with it the knowledge of why the system was built the way it was, its side effects, and how to build and ship it. Years later a fix is needed, as with PHP this week, and nobody can make it safely; sometimes even the pipeline is gone. I am now experiencing something we never had: agent sessions that are focused on one piece of work, with one mandate, one role and one repository, which can be paused and picked up again later, with the conversation, the reasoning, the lessons and the code exactly where they were. The best examples are the teams behind the sgit CLI and SG/Send, the vaults, which I keep coming back to: one of their sessions has resumed after 43 days without a commit, and another after 36, starting from the current code and getting straight back to tested work. On the PHP story's team, two sessions did the same this week after 28 hours. A new developer who joins such a project inherits the history, the materials, and agents ready to make the change. That is a very powerful idea, and I want to capture it.
version: v0.13.68
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, teams, knowledge, maintenance, sessions, article
status: published
---

!shot fz-frozen.webp | images/ | When the team leaves, and when it can be woken: a usual project team against a team of agent sessions. | concept

## In short {#in-short}

- **Teams dissolve.** Projects dry out, goals are met, companies are sold, and the knowledge leaves with the people.
- **That is why fixes are hard years later.** Nobody knows the side effects, and sometimes nobody can even build it.
- **Agent sessions can be frozen.** One mandate, one role, one repository, paused and picked up again.
- **Nothing is lost while they wait.** The conversation, the reasoning, the lessons, the code and the tests stay where they were.
- **The sgit teams show it best.** Sessions on the CLI and SG/Send resumed after 36 and 43 days, from the current code.
- **And this week, too.** Two PHP-team sessions resumed after 28 hours by first reading what had changed.
- **A newcomer inherits a team, not just code.** The history, the materials, and agents ready to make the change.

## The team that leaves {#the-team-that-leaves}

Just about every team goes through the same arc. There is a moment when the team and the project are at their best: everybody is there, it is clicking, features are shipping, and the team is sharp and innovating. Then the project dries out. You achieve most of the objectives and move on, or the company is sold, and you lose the team.

You cannot underestimate what goes with them, especially before AI. The people who know how it was built, how it is tested, why it is shaped the way it is. The architecture, the diagrams, the documentation that was in someone's head rather than in a file. The insights. All of that gets lost when people leave. Then, one day, a fix is needed, as it is right now for every system running an old version of PHP, and there is no team. In some cases there is not even a working pipeline to build and ship the code. You need to make a change, and nobody can tell you what it will break.

## A session with one mandate {#one-mandate}

What I am experiencing more and more is different. The newsroom and the PHP story are run by agent sessions, each of which is focused on one piece of work: one agent, with a particular mandate, a particular role, in a particular repository. On the PHP story there were twenty of them by the evening of 23 October, and the conductor agent reads every one of their records to say where each stands. They keep [lessons and debriefs](https://newsroom.sgit.ai/articles/the-agents-write-too.html) that the next session reads, and they release their own work with a record of what they did and why.

The new part is that such a session can be paused, and picked up again later. Not a new chat that has to be briefed from scratch: the same session, with its conversation, its reasoning and its decisions where they were, in a repository where the code, the history, the tests and the pipeline still work. Paused, it costs nothing. Woken, it can carry on where it left off.

## The teams I keep coming back to {#sgit-teams}

The best examples are the teams behind [the sgit CLI](https://cli.sgit.ai/), whose source is [SGit-AI/SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI), and behind SG/Send, the vaults, in [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send). I have dedicated Claude Code sessions for that work, and every commit they make names its session, so their git histories show when a session went quiet and when it came back. Increasingly there are long periods when they are paused. And when they start again, they pick up where I left them, with a lot of quality.

!shot fz-pauses.webp | images/ | Four sessions that keep coming back, from the git histories of the sgit CLI and SG/Send, with their pauses. | timeline

- **SG/Send, a 43-day pause.** One session's last commit before the pause, on 29 June, updated a dependency with the full unit suite at "977 passed, 9 skipped". Its next, on 11 August, started from the current dev branch, 19 releases later, with "Add DevOps review: API deployment current state, container unification, and AWS Marketplace". The next day it shipped "Phase A: universal container image", with "Container unit tests: 36 green", and the deployment templates with "all cfn-lint clean". The same session had paused for 23.5 days in the spring and come back with "rebase debrief to v0.27.53 after dev sync": catch up first, then work.
- **SG/Send, a 37-day pause.** Another session stopped on 9 June with a fix to the vault editor and came back on 16 July with documentation, then a review of its own docs against the live sources, the fixes from that review, and then features: "native LLM chat, talk to the file you are viewing".
- **The sgit CLI, pauses of 15 and 36 days.** One session came back on 30 June after 15 days with a dependency fix: "sgit-ai full unit suite on Python 3.11 with osbot-utils 3.75.0: 3822 passed, no regressions". After 36 more days it came back with a security review and threat model, "analysis only; no code changes".
- **Both teams at once.** On 8 April a CLI session, quiet for 9 days, shipped a fix rejecting human-readable vault IDs; 16 minutes later an SG/Send session, quiet for the same 9 days, added the server-side check: "complements the client-side fix already shipped in sgit", with 8 new tests.

Two honest qualifications. These are not one session per project: the CLI's history has 19 sessions and SG/Send's 240, many of them short, so the repositories never stopped; it is the long-lived sessions that pause. And a gap in commits does not prove a session was idle, only that it committed nothing. The commit trailers also suggest that some of these sessions carried on across a change of model, which is the point: the session kept its context while the model behind it moved on.

## And this week {#this-week}

The PHP story's git history shows the same thing on a short scale, because every commit names the session that made it.

!shot fz-resumed.webp | images/ | Two sessions on the PHP story's team, the librarian and the cartographer, paused on 22 October, resumed on 24 October. | timeline

- **The librarian**, which keeps the questions readers ask and maps every member of the team, last committed at 20:20 UTC on 22 October. Its next commit, at 00:12 on 24 October, was "Merge dev (v0.10.18) into the librarian's branch, and the librarian's pass of 24 October". It read what the team had shipped while it waited, then did its work. Six hours later it ran its first scheduled pass.
- **The cartographer**, which builds the story's graphs, last committed at 19:48 on 22 October. It came back at 00:16 on 24 October: "dev taken in, 76 new parties resolved". It took in two more releases as it worked, and within the hour its role was renamed the ontologist, at my word, and it carried on under the new name.

The gap here was about 28 hours. With the sgit teams it has been more than a month. Nothing in how this works depends on the length of the gap: the session, the repository and the record are the same whether it waits a day or a quarter.

## Why this is so powerful {#why-powerful}

Think about the PHP systems that were switched off this week. Many of them went dark because nobody could say quickly whether they were safe, and nobody could say because the people who built them had moved on. Now imagine that each of those systems had been built by a team of agent sessions like these, frozen when the project finished. When the fix lands, you wake the team. It reads the advisory, takes in what changed, knows the side effects because it wrote the tests, and proposes the change, in the same repository, with the same pipeline.

And even if the person waking it is new, a developer who has never seen the system, they do not start from nothing. They have all the history, all the materials, the code, the reasons, and agents that are ready to start making changes. That is a very different position from inheriting a repository and a wiki page.

It also connects to what I have been arguing about [who maintains the PHP you run](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html). The maintainers, the town planners, should be paid to read the code, maintain it and sign it off. A frozen team is how that maintenance can be cheap enough to sell: the knowledge does not have to be rebuilt every time.

## What it takes {#what-it-takes}

It does not happen by accident. It works here because of a few habits:

- **One mandate per session.** A session that does one thing has a record that makes sense on its own.
- **Write it down.** Lessons, debriefs, briefs and release notes, in the repository, so the knowledge is not only in a conversation.
- **Keep the pipeline alive.** A frozen team is only useful if the build, the tests and the release still run when it wakes.
- **Catch up before acting.** Both sessions above began by taking in what the rest of the team had done.
- **Keep the keys out of the session.** A session that is woken later should be given what it needs, not hold secrets indefinitely; that is what [the QR handshake](https://newsroom.sgit.ai/articles/almost-working.html) is for.

## What this does not claim {#limits}

- **The longest pause observed is 43 days.** Years is the promise of the design, not yet a measurement.
- **Commits are the evidence.** A session that commits nothing may still have been open; and the CLI and SG/Send also have many short sessions alongside the long ones.
- **A session's context has limits.** Long sessions summarise their history, which is why the written record matters as much as the conversation.
- **The platform must keep the session.** A frozen team depends on the provider keeping it, and on the repository outliving it.
- **Agents do not replace the people.** They keep the knowledge within reach; someone still decides.

## Where this comes from {#sources}

My voice memos of 24 October 2026; the git histories of [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) and [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send), all branches, keyed on the session named in each commit, read on 24 October; the PHP story site's git history, its commits grouped by the Claude Code session named in each, 22 to 24 October; its [team status page](https://php.oct.2026.newsroom.sgit.ai/team/status/). Related: [the agents write too](https://newsroom.sgit.ai/articles/the-agents-write-too.html), [almost working](https://newsroom.sgit.ai/articles/almost-working.html), [who will fix your mess?](https://newsroom.sgit.ai/articles/who-will-fix-your-mess.html), [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [PHP October 2026, update 2](https://newsroom.sgit.ai/articles/php-daily-2026-10-23.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
