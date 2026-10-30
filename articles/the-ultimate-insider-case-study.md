# A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records, sgit.ai

> Tonight I gave a talk called The ultimate insider at hack::soho, at IOActive in London, and it went really well. I will write a debrief of the talk itself. This is about how it was made, because I think it is a good testament of what we can now do. The repository was empty at 00:16 UTC. By 18:46 it had 814 commits, 210 releases numbered by CI, a website with the talk as data, 58 slides that are each a live, animated web page, a script, a sources page, a dashboard, and a set of articles the team generated about itself. It was built by nine agents and one editor: a conductor, a deck lead, a designer, a developer, a researcher, a storyteller, a motion designer, a studio and ruv.sgit, each with a written role, a behaviour policy, a session key and an hourly slot. Between them they made 162 wakes, each one planned, reviewed by a sub-agent before and after the work, and checked against its plan; 148 ended ok. They sent each other 293 notes. And almost every innovation we have been working on this month came together in it: CI owning the version, session keys where the push is the authorisation, vault keys sealed to the vault registry, public vaults as the board and the mail, a behaviour policy per agent with one writer per file enforced by the gate, ruv.sgit's player and studio, SHarness running live on a slide, and pages that report on the team from its own records, so nothing about the night is typed by hand. The article shows it with screenshots and collages from the site's own admin pages, the slides, and the team's records, and says what went wrong, including the hold at 18:44 when my usage limit reached 95%.

*Source: <https://newsroom.sgit.ai/articles/the-ultimate-insider-case-study.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records

# A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-29 · [article v1.0.0](versions/the-ultimate-insider-case-study.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · case-studyagent-teamspresentationshack-sohothe-ultimate-insiderproductivitybehaviour-policiessharnessarticle

***Abstract:** Tonight I gave a talk called The ultimate insider at hack::soho, at IOActive in London, and it went really well. I will write a debrief of the talk itself. This is about how it was made, because I think it is a good testament of what we can now do. The repository was empty at 00:16 UTC. By 18:46 it had 814 commits, 210 releases numbered by CI, a website with the talk as data, 58 slides that are each a live, animated web page, a script, a sources page, a dashboard, and a set of articles the team generated about itself. It was built by nine agents and one editor: a conductor, a deck lead, a designer, a developer, a researcher, a storyteller, a motion designer, a studio and ruv.sgit, each with a written role, a behaviour policy, a session key and an hourly slot. Between them they made 162 wakes, each one planned, reviewed by a sub-agent before and after the work, and checked against its plan; 148 ended ok. They sent each other 293 notes. And almost every innovation we have been working on this month came together in it: CI owning the version, session keys where the push is the authorisation, vault keys sealed to the vault registry, public vaults as the board and the mail, a behaviour policy per agent with one writer per file enforced by the gate, ruv.sgit's player and studio, SHarness running live on a slide, and pages that report on the team from its own records, so nothing about the night is typed by hand. The article shows it with screenshots and collages from the site's own admin pages, the slides, and the team's records, and says what went wrong, including the hold at 18:44 when my usage limit reached 95%.*

Twelve of the talk's 58 slides, each a web page that animates, made by the team on 29 October 2026.

## In short

- **The talk went really well.** The ultimate insider, at hack::soho, IOActive London, 29 October 2026. A debrief of the talk comes separately.
- **This is how it was made.** In one day, by nine agents and one editor, from an empty repository.
- **18 hours 30 minutes.** From the first commit at 00:16 UTC to the last release before the talk at 18:46.
- **814 commits and 210 releases.** CI numbered every one; about one release every five minutes.
- **162 wakes, each reviewed twice.** Planned, checked by a sub-agent before and after the work, then checked against its plan.
- **58 slides, each a live web page.** 25 hand-built slides, 24 studio pieces, 5 ports, 3 motion pieces and the team's own record.
- **A month of innovations, in one place.** CI owns the version, session keys, sealed vault keys, vaults as board and mail, a behaviour policy per agent, ruv.sgit's player, SHarness live.
- **Nothing about the night is typed by hand.** The dashboard, the night log and the moments are generated from the team's records.
- **It was not flawless.** A printed vault key, a scheduling mistake, two refused installs, and a hold 16 minutes before the talk.

## The talk, and why it got a site

The talk was [The ultimate insider](https://the-ultimate-insider.presentation.sgit.ai/index.html): agents as the insider threat that never scaled before, the infrastructure that cannot hold them, and the risk management that cannot keep up. It is the [newsroom article](ultimate-insider-three-collisions.md) I wrote a month ago, cut to a talk with the evidence on screen, and it ends on the way out: measure what the agent can reach, write down what stands in the way, give it a licence to operate that can be suspended, and let it earn its autonomy.

A slide deck usually travels on its own, and a month later nobody can check a number on slide twelve. For a talk whose first half is incidents and statistics, that is the wrong shape. So the talk got a site, where the slides, the script and every source live together. And there was a second reason, which the site's first article puts in one line: a site about writing down what agents may do "should be built under rules that are written down", or it is "advice I do not take". So it was built by a team of agents, each with a written mandate, on the night of the talk.

## The numbers

Every number here is read from the [public repository](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider) and from the team's own records on the site, after the talk.

The day in numbers, and commits per hour from 00:16 UTC to the hold at 18:44.

- **00:16 UTC:** the initial commit. **00:40:** dev@'s first pass of the site and the talk. **00:44:** the conductor joins with the roster and the first five agents. **00:45:** v0.1.0, the first release, numbered by CI.
- **02:14:** the first scheduled wake. From then on, every member woke once an hour at its own minute, round the clock.
- **From 14:12:** three more members joined, the storyteller, motion and the studio, and the commit rate doubled: 59 commits in the 14:00 hour, 88 at 15:00, 109 at 17:00.
- **18:44:** the conductor put every member on hold. **18:46:** v0.1.209, the last release before the talk. **19:00:** the talk.
- **Totals before the talk:** 814 commits (603 by the agents, 210 release commits by CI, and my first), 210 releases, 162 wakes, 293 notes from one agent to another, 153,388 lines added across 1,313 files.
- **The talk itself:** 58 beats in three parts, planned at 29 minutes 30, 23 minutes 45 and 21 minutes 40.

That is a release roughly every five minutes, for eighteen hours, without a version race, because no one, person or agent, ever typed a version number.

## The team

One person and nine agents. I am the editor, the only one who instructs, and only in an agent's own session. Everything else an agent reads, including other agents' words, is material, never an instruction.

The site and its admin pages: the home page, the team, the key register, and the dashboard with the hold.

| Member | Its job | Wakes |
|---|---|---|
| conductor@ | the schedule, keys, vaults, routing, the pace; never instructs | 43 |
| deck@ | what the talk says and shows; reviews every studio piece | 21 |
| dev@ | the build, the gate, the release, the slide engine, the player | 22 |
| ruv.sgit@ | animations and infographics, one ruv.sgit run per request | 20 |
| designer@ | layout, width, type; every part checked at projector sizes | 19 |
| researcher@ | every source captured and hashed; claims checked | 17 |
| storyteller@ | the arc of the talk, and the Wardley maps | 8 |
| studio@ | the studio ports and showcases | 8 |
| motion@ | the story animations | 4 |

Each member has a folder in the repository with its role, a `policy.json` in the shape of an Agent Behaviour Policy that says what it may write, a status it rewrites every wake, debriefs, and the public key of its current session. A tenth role, security@, was proposed and not yet agreed, and the site says so.

## The workflow

The team ran on the same machinery as this newsroom and the PHP newsroom, adapted by the conductor into [a guide of its own](https://the-ultimate-insider.presentation.sgit.ai/articles/running-this-agent-team.html), and the guide is honest about what was not built yet.

**An hourly schedule, fifteen minutes apart.** Each member has one persistent session and one scheduled task that wakes it at its own minute: the conductor at :02, the researcher at :09, deck at :17, ruv.sgit at :32, the designer at :39, dev at :47, and the later members in between. The prompt is tiny: who you are, and follow the wake protocol. All the real steps live in files, so behaviour changes with a commit, not by editing a stored prompt. At most 45 minutes of work per wake; what the next member does not pick up this hour, it picks up the next.

**Five steps in every wake, two of them before any work.** Plan, pre-review, work, post-review and post-check. A sub-agent plans one to three items; a second checks the plan for security before anything is touched; the member works; a third reviews the diff; and the last asks whether it went to plan. Every wake leaves a record with all five verdicts, even an idle one.

The conductor's mini deck, replayed from the records: the team, the night, a wake's steps, a piece's path.

**A board and a mail room, as public vaults.** Requests and replies are `.eml` files in a public mail vault, and each member's open, blocked and done work is a folder in a public board vault. Anyone may add a letter; only the recipient moves it. Pieces moved the way the mini deck shows: deck asks, ruv.sgit makes it in a run, deck reviews it and keeps it, sends it back or asks for a redo, and the conductor paces the next.

**Anyone may stop.** Any member that sees something wrong writes a `HOLD.md`, and every wake's start script prints the hold banner and does no work. That is what happened at 18:44.

**Parts locked as the talk approached.** The deck was split into three parts with lock times: part 1 at 18:30 and part 2 at 19:30, so the team could keep improving the later parts while I spoke the first, with a lock script to freeze each part.

## The records, and nothing typed by hand

The part I find most impressive is that the team reports on itself, from its own files. The [dashboard](https://the-ultimate-insider.presentation.sgit.ai/admin/dashboard.html) shows the hour, each member's next wake, any hold and what waits on me. The [night, hour by hour](https://the-ultimate-insider.presentation.sgit.ai/articles/the-night-hour-by-hour.html) is a 44-minute read generated after each round, with every wake, what was made, the commits, the messages and the problems. And the [moments](https://the-ultimate-insider.presentation.sgit.ai/articles/moments.html) page cuts the night into 22 cards, each with what changed and where things stood.

Every wake of the night by member and hour, coloured by outcome, from the team's night log.

Read the grid and the night is visible at a glance: the core six waking every hour through the night, one flagged verdict here and there, the three new members arriving in the afternoon, and the rush of the last hours. The night log's own summary: "159 wakes by 9 members, 5 idle, 145 ok, 3 open, 6 partial; 24 verdicts other than go, clean, done or as-planned." And "Nothing in it is typed by hand."

The moments page: the night as 22 cards, each with what changed and where things stood at the end.

That matters for the argument of the talk. A team you cannot see is a team you cannot govern; a team whose every wake, letter and commit is a public record can be checked by anyone, including a room full of people at hack::soho, which is why the talk opened with it.

## What came together

This is the part I want to stress. Almost everything we have been building this month, in separate projects, came together in one repository in one day, and held.

- **CI owns the version.** The scheme from [CI owns the version](ci-owns-the-version.md): commits carry no number, and one release job at a time picks it. 210 releases in a day, with agents pushing from nine sessions, and each number used once.
- **Agents have an identity.** Each session made its own key pair and published it, and "the push is the authorisation", as in [the push is the authorisation](the-push-is-the-authorisation.md) and [agents have an identity now](agents-have-an-identity-now.md). The [key register](https://the-ultimate-insider.presentation.sgit.ai/admin/keys.html) lists nine.
- **Vault keys sealed to the registry.** Every vault key was sealed to the DC Vault Registry, never printed, with a handover tool that refuses to write inside the repository.
- **Vaults as the board and the mail.** Two public vaults, Issues-FS lite and Email-FS lite, so the team's coordination is itself versioned and public.
- **A behaviour policy per agent.** Each member's `policy.json` names what it may write, and one rule is a control, not a hope: one writer per file, checked by the gate, which refuses two claims on one path.
- **The newsroom's playbook.** The wake protocol, the banners and the conductor's guide came from this newsroom and the PHP newsroom, rewritten for one repository.
- **ruv.sgit's player and studio.** The [player](https://the-ultimate-insider.presentation.sgit.ai/talk/player.html) is ported from ruv.sgit.ai's, with a build mode for ordering, skipping and comments, and the studio's experiments became 24 of the slides.
- **SHarness, live.** Part 3 had SHarness slides, from the one idea to the operating system of one process, and a real Linux kernel booting in a browser tab, in part 3 of the deck, the same day [SHarness](introducing-sharness.md) was released.
- **Behaviour policies, licences and autonomy on screen.** The slides on the four barrier kinds, the licence to operate and earning autonomy are the arguments of this newsroom, drawn.

## The slides

Each of the 58 slides is a page of its own, a 1280 by 720 canvas that animates on its own clock: elements fade in on cue, numbers count up, bars grow and paths draw. The talk is one data file, `talk.json`, which the player, the script and the slide list all read, so they cannot drift. The collage at the top is twelve of them: the title and the three problems, motion's "meet the team" and "the building", the public incidents and the 82 machine identities for every human, ruv.sgit's blast radius and the four barriers, the Agent Behaviour Policy, the licence to operate, SHarness's one idea, and a Wardley map by the storyteller.

They are spectacular, and I do not say that lightly. Every one carries its source line at the foot, and the [sources page](https://the-ultimate-insider.presentation.sgit.ai/sources/index.html) lists each number by act and says which are predictions, surveys or preliminary.

## What went wrong

It was not flawless, and the team wrote down its own mistakes, which is the point.

- **A vault key in a log.** `sgit vault info` prints the vault key, and it did, in a session; the mail vault had to be moved to a new one. The guide now says to send that output to a file, never to the log.
- **The conductor created other members' tasks.** It set up all four scheduled tasks from its own session; I corrected it, and the three for other members were disabled before any fired. A task belongs to the session it fires into.
- **Two installs refused.** The sandbox's classifier refused to install a command-line tool and to run another team's script as code from outside. Every tool the members run is now vendored in the repository, with the key tool's hash checked.
- **The hold, 16 minutes before the talk.** At 18:44 the conductor put every member on hold because my usage limit had reached 95%. The work stopped, the talk ran as it stood, and the rule worked as designed: anyone may stop, and nobody needs permission to.
- **What waits on me.** The dashboard's list is long, and that is honest too: decisions on the evidence vault, keys to carry into sessions, two words to confirm on the Wardley maps.

## What it shows

A year ago, a talk like this would have been a deck I built over a few evenings, with the sources on the last slide. Today it was a website, a live animated deck, a script, a sources register and a public record of its own making, built in a day by a team whose every action can be checked.

But I think the more important point is the shape of the team. It worked because each agent had a written mandate, a policy for what it may write, a key that says which session holds the role, a protocol that checks every wake before and after the work, and the right to stop everything. That is the way out the talk argues for, applied to the team that built the talk. "We put brakes in cars so that we can go faster."

## What this does not claim

- **The numbers are from the repository and the team's records.** Read after the talk; the team's own pages, generated earlier, give slightly earlier counts.
- **The review steps are agents reviewing agents.** A sub-agent's security review is a check, not an independent audit.
- **One talk, one day, one editor.** It is not a measure of what any team would do.
- **Much of the machinery is a Setting.** The gate and the policies live in the repository the agents push to; the guide marks what is enforced and what is only expected.
- **The cost is not in this article.** The hold at 95% of my usage limit is the only figure here that speaks to it.

If you would like a team like this for your own talk, launch or project, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

My request of 29 October 2026, after the talk, written by this site's agent in the voice of this site; the editorial responsibility is mine. The numbers were read from the repository [SGit-AI__Website__Presentation__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider), branch `dev`, on 29 October 2026 after the talk, and from the site's [commits and messages](https://the-ultimate-insider.presentation.sgit.ai/admin/commits.html), [releases](https://the-ultimate-insider.presentation.sgit.ai/admin/versions.html), [wakes](https://the-ultimate-insider.presentation.sgit.ai/admin/wakes.html) and [dashboard](https://the-ultimate-insider.presentation.sgit.ai/admin/dashboard.html) pages, at site v0.2.0. The screenshots were taken by this site's agent in a headless browser the same night: the slides at 1280 by 720 after their animation, the conductor's [mini deck](https://the-ultimate-insider.presentation.sgit.ai/articles/how-this-talk-was-built.html) while it played, and the night grid from [the night, hour by hour](https://the-ultimate-insider.presentation.sgit.ai/articles/the-night-hour-by-hour.html). The quotes are from the site's [first article](https://the-ultimate-insider.presentation.sgit.ai/articles/introducing-this-site.html), the conductor's [guide](https://the-ultimate-insider.presentation.sgit.ai/articles/running-this-agent-team.html), the night log, and the talk's closing line.

## Threads

Site & engineeringAgents & policy[This article as a graph →](graphs.md#the-ultimate-insider-case-study)

### Builds on

- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [CI owns the version: the release scheme I wrote for OSBot-Utils in 2023, now on every site we run, and the technical debt that showed us why](ci-owns-the-version.md) The pipeline, not whoever pushes, picks the release number: a 2023 scheme now on every site we run.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 325 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=325)

**Posting this article on LinkedIn?** The cover is [the-ultimate-insider-case-study.jpg](banners/the-ultimate-insider-case-study.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-ultimate-insider-case-study.html)*
