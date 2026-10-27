# What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it, sgit.ai

> I have moved from many Claude sessions to agent teams that run on schedules. The PHP October 2026 newsroom is the furthest along: a pipeline of researcher, curator, journalist and correspondent runs in order five times a day, a desk twice, a conductor every hour, and eight more agents keep the house, all on their own schedule cards. For two days it has run in sequence with no content commit from me. Then there is a second way to run the same agents: in one session, as subagents, which is how the newsroom carried CISA's listing of php2shell to readers in 5 hours 21 minutes. Writing this up against the team's own record corrected me in several places: the conductor does not start the breaking run, the agents' keys seal secrets but do not yet sign their work, and nothing has run on anything but Claude. What it confirmed is the main point: an agent is a session plus a card, a role, a loop, a key and memory kept in repositories and vaults, and only the first part is the model.

*Source: <https://newsroom.sgit.ai/articles/what-an-agent-is.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it

# What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-27 · [article v1.0.0](versions/what-an-agent-is.md) · [newsroom v0.13.108](https://newsroom.sgit.ai/admin/versions.html) · agentsagentic-workflowsphp2shellnewsroomschedulespkivaultsarticle

***Abstract:** I have moved from many Claude sessions to agent teams that run on schedules. The PHP October 2026 newsroom is the furthest along: a pipeline of researcher, curator, journalist and correspondent runs in order five times a day, a desk twice, a conductor every hour, and eight more agents keep the house, all on their own schedule cards. For two days it has run in sequence with no content commit from me. Then there is a second way to run the same agents: in one session, as subagents, which is how the newsroom carried CISA's listing of php2shell to readers in 5 hours 21 minutes. Writing this up against the team's own record corrected me in several places: the conductor does not start the breaking run, the agents' keys seal secrets but do not yet sign their work, and nothing has run on anything but Claude. What it confirmed is the main point: an agent is a session plus a card, a role, a loop, a key and memory kept in repositories and vaults, and only the first part is the model.*

Every scheduled wake of the PHP newsroom's agents in one day, London time.

## In short

- **From sessions to teams on schedules.** Once something works, you use it everywhere.
- **The pipeline runs itself.** Researcher, curator, journalist, correspondent: five times a day, in order.
- **No content commit from me.** Agents and CI write everything; I give the "go"s.
- **A second way to run them:** one session, every step as a subagent. CISA's listing reached readers in 5 h 21 min.
- **The record corrected me.** The conductor doesn't start breaking runs; keys seal secrets, they don't sign yet.
- **An agent is six parts,** and only one of them is the model.
- **The memory is the repository,** which is why an agent can move session, account, and in principle vendor.
- **Today the newsroom is moving account,** and that is the test of all of this.

## From sessions to teams

This follows [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html), and it is a Wardley story: as soon as something stops being a novelty and you understand it, you use it left, right and centre. I went from running many Claude sessions to running agent teams, and the step that changed the most was the schedule. A schedule means a follow-up: the agent comes back, picks up where it was, and does the next thing without me asking. It also changes how you think. Which tasks can run on a loop? Which can't be automated? Where does a person have to come in, and why?

The [PHP October 2026 newsroom](https://php.oct.2026.newsroom.sgit.ai/), the team covering php2shell, is the furthest along. Its record is public, on [the team site](https://team.php.oct.2026.newsroom.sgit.ai/), and everything below comes from it.

## The pipeline, on a schedule

Four agents run one after another, five times a day, each [on its own card](https://team.php.oct.2026.newsroom.sgit.ai/team/schedule/wiring/):

- **The researcher** probes every watched source, captures what changed into the source watch's vault and reports what moved (07:00, then every two and a half hours).
- **The curator** promotes what the researcher captured into the evidence vault, a bounded batch a wake, each capture read first (an hour later).
- **The journalist** takes that evidence through to the site by fixed rules, one release a wake (40 minutes after the curator, because the curator takes 12 to 21 minutes to push).
- **The correspondent** reviews what the journalist published, corrects it in the open and counts the catches (45 minutes after the journalist).

The desk, which keeps the story's line and the front page true to the evidence, follows the correspondent twice a day. The conductor wakes every hour to keep everyone in step. And eight more agents keep the house: [the fact-check desk](https://team.php.oct.2026.newsroom.sgit.ai/team/schedule/factcheck/), Pulse, which tracks other vulnerabilities in the news, the ontologist, the sherpa, which reads the readers' feedback, observability, dev, the librarian and security, which reviews each day's changes for injection, leaks and vulnerabilities every night.

On 27 October the commit history shows four full cycles running in order, on time. In the first: the researcher woke at 07:00 and released at 07:55; the curator at 08:00, released at 08:37 with "580 sources, 304 claims"; the journalist at 08:40, "11 claim verdicts for batch 19"; the correspondent at 09:25, reviewing batches 18 and 19; the desk at 10:40. Each batch number passes downstream. There are 157 run records, none failed. And I wrote none of the content: the team repository has 237 commits by Claude, 99 by the build, 12 by the curator's own identity, and one by me, the initial commit.

That is supervised, not unattended. The cards' notes quote my "go" on most changes, and the move to standing sessions, the timings and the models were decisions I made. But the work runs without me.

## One session each, and why

What makes schedules work today is a dedicated session per agent that the schedule wakes again. It continues the same conversation, so it has its context: the same as going back to a session and saying "continue". The journalist and the correspondent started differently, as a fresh session each wake, and were moved to standing sessions on 26 October because, in the card's words, "a fresh session could not always attach the repository". Dev still runs fresh each morning.

There is a practical reason too. Each session holds clones of the vaults and the keys to open them, and those are expensive to set up: the source watch's vault takes 232 to 316 seconds and 4.3 to 4.8 GB to clone, and the curator's pull takes 30 to 40 minutes. A standing session sets that up once.

And there is one limit worth knowing: one session cannot wake another agent's session. When the conductor tried to start the curator with a trigger, it "started a fresh, empty session … no repositories … no vault key. That session stopped in 9 seconds", at a cost of about $0.08. Which is why the second way of running exists.

## The second way: one session, every step

Three ways to run the same agent: a standing session on a schedule, subagents in one session, or a fresh session.

For breaking news I start one session, [the breaking desk](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__the-breaking-news-desk/), and give it a link: "breaking: this has happened". It runs the four steps of the pipeline in order, "each as a subagent given that role's card and runbook", and checks each step's output before the next starts. The subagents have no memory of a session, but they have the memory of the repository, which is the one that matters.

The first real run was CISA's listing of both php2shell flaws on 26 October. [The report](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__report__the-kev-listing-run/): CISA released its catalogue at 22:24 UTC, and the newsroom's readers' pages carried it 5 h 21 min later, against about 11 h 36 min on the schedule. From my "breaking:" to the last deploy took 45.8 minutes: researcher 271 seconds, curator 482, journalist 447, the correspondent's review 756, 642,456 tokens and 186 tool calls in all, with three catches in the review. It also said where the time really went: 86% of the delay was before the run started, because the capture had not been queued for the curator. That is now fixed in the researcher's card.

The same pattern runs [projects](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__projects-and-the-projects-desk/): an Opus coordinator, Sonnet subagents for each member's step, the ontologist, the sherpa, the design agent, the journalist. And the fresh-session option is always there: start a new session, tell it who it is, let it pull the team repository and read its card. Because the repository is the memory, that is how an agent moves when its context is too long, or to another account.

Models follow the work. On 27 October I decided: Opus for the conductor, the correspondent and security, the agents where judgement and review matter most; Sonnet for everyone else. The record shows two drifts from that decision (dev's card still says Opus), which is the kind of thing a record is for.

## What an agent is

The six parts of an agent on the PHP newsroom: session, card, role and policy, memory, loop and key.

Here is the definition this work has led me to. An agent is not the model. It is six things:

- **A session:** Claude or ChatGPT or another, with tools and skills. Today every agent here is Claude Code on the web.
- **A card:** [its schedule card](https://team.php.oct.2026.newsroom.sgit.ai/team/schedule/conductor/), with its objective, its wakes, its model, what it reads and writes, and what it must never do.
- **A role and a policy:** [ROLE.md and an agent behaviour policy](https://team.php.oct.2026.newsroom.sgit.ai/admin/agents/researcher/), in RiskMandate's terms a grant, a mandate, a delta and a barrier. All 29 policies are still drafts, which is honest: they are written, not yet agreed.
- **Memory:** the repositories and the vaults. Briefs, board rows, run records, debriefs, messages. Not the session.
- **A loop:** one shared file, WAKE.md, that every wake follows: a start banner, read the inbox and the board, do the work, leave a run record, an end banner. The scheduled prompt is as short as possible and points there.
- **A key:** a key pair, made in its session.

Only the first is the model. The other five are files and keys. That is why the same agent can be a standing session on a schedule, a step inside someone else's session, or a fresh session on another account, and why, in principle, it could run on ChatGPT or another tool that can clone a repository and open a vault.

## Where the record corrected me

I dictated the first version of this from memory. Checked against the team's record, I had several things wrong, and they are worth stating:

- **The conductor doesn't start the breaking run.** I start a separate session, and it runs the steps. The conductor wrote its brief and runbook, after its own attempt to wake another session failed.
- **The breaking run has four steps, not five.** There is no desk step.
- **The keys don't sign anything yet.** Each agent can have a key pair, and they are used to seal vault keys sent to them, carried by me as QR codes and checked five ways on opening. But nothing the agents write is signed with their own keys. [Security's advisory SA-2026-024](https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/) is open: "Nothing is signed, although every agent can have a key". Every agent commit is signed by one shared platform key, and the agent is named only in a trailer. Signing is the next step.
- **"About two days" is the newest part.** The researcher and curator have been on schedules since 23 October; the full pipeline across six repositories since 25 and 26 October.
- **Nothing has run on anything but Claude.** The portability is in the design, not yet in the record.
- **The vaults are real and large.** The researcher writes the source watch, 1,330 pages, 988 publishers and 15,953 snapshots by midday on 27 October; the curator writes [the evidence vault](https://team.php.oct.2026.newsroom.sgit.ai/team/vaults/), 614 sources and 679 captures, of which only the hashes are public.

## Today's test

At 16:51 UTC today, every scheduled task except the conductor's, security's and observability's was paused: the account was at 78% of its usage, and the newsroom is moving to a new one. The move brief lists what does not carry over: each agent's session and scratchpad, its clones, its key pair, the vault keys sealed to it, the scheduled tasks. And what does: everything in the repositories. "That is why the move is simple: a new session is told who it is, pulls team, and reads its card."

That sentence is the whole argument. If the memory is in the session, moving is a disaster. If it is in the repository and the vaults, moving is a setup cost: a new key, sealed vault keys, clones and a card. We will know in a day or two how small that cost is.

## What this does not claim

- **Supervised, not autonomous.** The pipeline runs on schedules, but its design, timings, models and fixes are my decisions, on the record.
- **Counts are from the record on 27 October:** commit times, run records and cards, read by an agent of this newsroom.
- **Signing is planned, not built.** Agents seal secrets with their keys; they do not sign their work yet.
- **Portability is a design property,** not yet tested: every agent so far has run on Claude.
- **Costs in dollars are not recorded** in the run records, except one empty session's $0.08.

## Where this comes from

The PHP October 2026 team site and repository, read on 27 October 2026: [the schedule wiring](https://team.php.oct.2026.newsroom.sgit.ai/team/schedule/wiring/) and each agent's card under records/schedule/, the agents' roles and policies under [admin/agents](https://team.php.oct.2026.newsroom.sgit.ai/admin/agents/researcher/), records/WAKE.md, [the breaking-desk brief](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__the-breaking-news-desk/), [the projects brief](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__projects-and-the-projects-desk/), [the KEV listing run report](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__report__the-kev-listing-run/), the move brief of 27 October, [the vaults](https://team.php.oct.2026.newsroom.sgit.ai/team/vaults/), [security advisories](https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/), and the commit history of the six repositories. Related: [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html), [agents need direction](https://newsroom.sgit.ai/articles/agents-need-direction.html), [one vault, ten agents](https://newsroom.sgit.ai/articles/one-vault-ten-agents.html), [agent workflows on ephemeral vaults](https://newsroom.sgit.ai/articles/agent-workflows-on-ephemeral-vaults.html), [what if an agent loses its workspace](https://newsroom.sgit.ai/articles/what-if-an-agent-loses-its-workspace.html), [process behaviour policies](https://newsroom.sgit.ai/articles/process-behaviour-policies.html). Checked against the record by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#what-an-agent-is)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 304 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=304)

**Posting this article on LinkedIn?** The cover is [what-an-agent-is.jpg](banners/what-an-agent-is.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-an-agent-is.html)*
