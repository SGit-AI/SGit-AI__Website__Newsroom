# You can feel good engineering: the weight, the speed and the smoothness of it, why agent teams make the gaps show, and how to keep a constant velocity, sgit.ai

> Good engineering has a presence. If you know what good architecture, good code and good practice look like, you can feel it: in the speed, the quality, the effectiveness, and in where the bugs turn up. I now spend most of my time reviewing what agents do, mostly through its side effects, and the lesson is that multiple agent teams behave like multiple human teams: what slows them down is the engineering gaps, the non-functional requirements, the conventions they do not share. The difference is that agents absorb the overhead quietly, so the waste can hide, until you push the limits and things break. The PHP newsroom pushed sgit from vaults that struggled at tens of thousands of files to 228,000, through three releases in five days, and pushed its own repository until every release rewrote about 1,936 files, then split it into six, where a change now touches one to three. This site still rewrites about 1,588 files per release, which is the same gap, in our own house. The answer is to keep architecting, keep asking for evidence, let scheduled agents hold the quality level, and refactor from explorer to villager when the innovation slows down.

*Source: <https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / You can feel good engineering: the weight, the speed and the smoothness of it, why agent teams make the gaps show, and how to keep a constant velocity

# You can feel good engineering: the weight, the speed and the smoothness of it, why agent teams make the gaps show, and how to keep a constant velocity

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-27 · [article v1.0.0](versions/you-can-feel-good-engineering.md) · [newsroom v0.13.110](https://newsroom.sgit.ai/admin/versions.html) · engineeringagentsqualitysgitarchitecturewardley-mapsarticle

***Abstract:** Good engineering has a presence. If you know what good architecture, good code and good practice look like, you can feel it: in the speed, the quality, the effectiveness, and in where the bugs turn up. I now spend most of my time reviewing what agents do, mostly through its side effects, and the lesson is that multiple agent teams behave like multiple human teams: what slows them down is the engineering gaps, the non-functional requirements, the conventions they do not share. The difference is that agents absorb the overhead quietly, so the waste can hide, until you push the limits and things break. The PHP newsroom pushed sgit from vaults that struggled at tens of thousands of files to 228,000, through three releases in five days, and pushed its own repository until every release rewrote about 1,936 files, then split it into six, where a change now touches one to three. This site still rewrites about 1,588 files per release, which is the same gap, in our own house. The answer is to keep architecting, keep asking for evidence, let scheduled agents hold the quality level, and refactor from explorer to villager when the innovation slows down.*

Push the limits, watch what breaks, ask for evidence, fix the engineering, and keep the level with scheduled agents.

## In short

- **Good engineering has a presence.** You can feel it in the speed, the quality and where the bugs occur.
- **I review agents by their side effects,** and read the code to give direction.
- **Many agent teams behave like many human teams.** The engineering gaps are what slow them down.
- **Agents absorb the overhead quietly,** so waste can hide until you push the limits.
- **sgit, pushed by the PHP vaults:** three releases in five days, a pull from 566 s to 31.7 s on 228,000 files.
- **One repository into six:** files touched per change from about 1,936 to one to three.
- **This site has the same gap:** about 1,588 files per release.
- **Scheduled agents hold the level,** and technical debt gets paid in days, not quarters.
- **Explorer, then villager:** refactor when the innovation slows down.

## The feel of it

Good engineering has a kind of presence, a weight, a smoothness. If you know what good architecture, good code, good quality and good practices look like, you can detect it, a bit like an experienced mechanic hears an engine. There is a speed to it, a quality, an effectiveness. Things that should be easy are easy. Bugs turn up where you expect them, at the edges and the new parts, not everywhere.

These days I spend most of my time reviewing what AI does. I look at the code some of the time, mostly to give direction on particular elements; mainly I look at the side effects: what happened, how fast, what broke, what the records say. And the side effects are where you feel it. When the engineering is good, the teams move fast and the fixes are small. When it isn't, every change is expensive, and the cost shows up somewhere you were not looking.

I think what I have now is one of the most effective development environments I have worked in, with more of the non-functional requirements implemented than I usually see, because I can create many agents, give each one a focus, and have them work together. Which is exactly where the lesson came from.

## Many agent teams behave like many human teams

When you put several agent teams on the same repository, they behave like several human teams. Without good engineering, good practices and good workflows, even simple conventions and ways of working, they get in each other's way. One fixes something and another undoes it. They make a mess. In the non-agentic world, that is why things grind to a halt: there is an overhead, and politics, and eventually nobody can move.

I have plenty of examples from this week alone, in this newsroom:

- **Two version races in one day.** Twice a release I was building had its version taken by another agent's release that landed first (the accountant took v0.13.100; newsroom.dev took v0.13.103), and I had to save, reset and re-apply.
- **The same review filed twice.** Two agents put the same ChatGPT review on the record, in different formats.
- **A fix that broke someone else's test.** Correcting an article broke a new test that had assumed the article would never change.

None of these is a bug in an agent. Each is an engineering gap: a shared counter, a shared record without one owner, a test coupled to content. The PHP newsroom found the same before its split: 28 release messages in three days naming a conflict, a collision or a renumbering, and board rows renumbered by hand 11 times.

## The overhead you don't see

Here is the twist. Agents consume that overhead without complaining, and we are still spoiled by how many tokens we can spend. So the inefficiency can be enormous and nobody notices. I was working synchronously, and suddenly saw updates changing thousands of files. Hold on, why is that happening?

Median files changed per release or commit, before and after the PHP newsroom's split, and on this site.

The answer, in both newsrooms, was the same engineering problem. The PHP newsroom's one repository stamped the site's version on every page, so, [in the words of its split proposal](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/), "every release touches every page, whatever it changed": a median of 1,936 files over its last 20 releases, at 44 to 77 releases a day, each waiting on a 42-second build and a 74-second gate. This site does the same thing: over its last 25 releases, a median of 1,588 files changed to publish what was usually one article. Nobody decided that. It is what happens when nobody is looking at the side effects, and when the cost is paid in tokens rather than in people's patience.

## Push the limits, and watch what breaks

The way to find these gaps is to push. The PHP newsroom pushed sgit harder than anything before it: vaults of tens of thousands of files and gigabytes of captures, where not long ago the advice was to avoid lots of little files because vaults could not handle them.

What broke in sgit under the PHP newsroom's vaults, the numbers before and after, and the release that fixed each.

And it broke, in measurable ways. On 23 October the source watch, 29,861 files and 63,662 objects, had outgrown the server's object listing: it timed out after 90.8 seconds, pushes failed, and one pass took 2 hours 42 minutes and 12 attempts. The team [moved it to a pack vault](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/) with sgit 0.24.0: the listing came back in 0.73 seconds, a fresh clone went from 827 to 95 seconds. Then the newsroom [measured and reported](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-26__brief__for-the-sgit-cli-team-0-25-0-in-the-newsroom/) what was still slow; 0.25.0 took the first commit of a pass from 12 minutes 38 seconds to 25 seconds; and [0.26.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__sgit-0-26-0/) took a pull from 566 to 31.7 seconds on 228,000 files, as measured by the CLI team. Three releases in five days, each driven by evidence from the field.

That is what a good development environment lets you do: refactor, change and push to production fast, at the moment a limit shows. And keep a team you can pause: the sgit team is one I run on the most capable model, because it needs that extra level of attention, and I can pause it for a couple of weeks, come back with "here's a bug", and it continues where it left off, as I described in [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html). That is impossible in the real world.

## Constant velocity

The other half is keeping the level once you have it. When a team has members who are experts, in design, communication, engineering, architecture, they can enforce those qualities even when they are not doing the work day to day, because they know when to tell the team to stop and fix something specific. That gives you a constant velocity: not bursts and stalls, but a smooth rate.

Schedules made that real for me. On the PHP newsroom, the librarian, the security agent, the ontologist, the desk and the conductor run at regular intervals, look for anything that needs doing, do it, and stop, as I described in [what an agent is](https://newsroom.sgit.ai/articles/what-an-agent-is.html). Security has raised 43 advisories; the fact-check desk keeps 162 tickets; the correspondent has caught 18 errors in the journalist's work. That is a constant layer of quality, and it is the first place you see drift.

And technical debt changes character. Instead of spending weeks, slowing everything down, to pay it back, you pay it very quickly, or give it to an agent to improve while the work goes on.

## Explorer, then villager

From a Wardley maps point of view, I do this on purpose. While we are innovating, it is [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html): fast, messy, learning. When the innovation slows down and we reach a good point, I move to villager coding, and that is when you do a major refactoring. I work on the architecture, review the mappings, and refactor, then a couple of rounds until it stabilises.

The PHP newsroom just went through one. Its [split into six repositories](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/) was designed on the principle "split along who writes and how often, not along technology", and its [report on the challenges](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__report__one-repository-into-six-the-challenges/) is honest about the cost: two design decisions reversed, nine bugs introduced and caught before release, two old bugs found that had been live all along. The result is in the chart above: a change in the team, site or data repository now touches one to three files. The references site still stamps every page, at about 1,400 files a commit, which is the next round.

And this site is due its own. About 1,588 files a release, a build of about ten minutes for one article, and two version races in a day are the signs. You can feel it.

## What this does not claim

- **"You can feel it" is experience, not a metric.** The numbers here are the evidence that the feeling pointed at something real.
- **The counts are medians from git history,** read on 27 October; the PHP figures are from its own briefs and reports.
- **The sgit timings are the newsroom's and the CLI team's own measurements,** in cloud sessions, on their vaults.
- **The ranking of my own environment is my opinion.**

## Where this comes from

The PHP October 2026 newsroom's briefs: [moving a vault to pack mode](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/), [the field report for the sgit CLI team on 0.25.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-26__brief__for-the-sgit-cli-team-0-25-0-in-the-newsroom/), [the 0.26.0 brief](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__sgit-0-26-0/), [the proposal to split one repository into six](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/) and [its report on the challenges](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__report__one-repository-into-six-the-challenges/); [sgit's 0.26.0 release notes](https://cli.sgit.ai/docs/update-to-0-26-0.html); the git history of newsroom.sgit.ai and the six PHP repositories, counted on 27 October 2026. Related: [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html), [what an agent is](https://newsroom.sgit.ai/articles/what-an-agent-is.html), [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html), [the sidecar repository](https://newsroom.sgit.ai/articles/the-sidecar-repository.html). Written up by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineeringAgents & policy[This article as a graph →](graphs.md#you-can-feel-good-engineering)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 307 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=307)

**Posting this article on LinkedIn?** The cover is [you-can-feel-good-engineering.jpg](banners/you-can-feel-good-engineering.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html)*
