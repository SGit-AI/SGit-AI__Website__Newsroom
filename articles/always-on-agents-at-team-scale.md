# Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many, sgit.ai

> On 13 November, William Hu of Anthropic published Building always-on agents, the patterns Anthropic recommends for agents that sleep, wake on an event, do their work and go back to sleep. It rests on five primitives: an event inbox, timers, memory, permissions and an outbox. Reading it, I recognised every box, because in the ten days around Web Summit six of us ran around 250 named agents on the same shape, built from different material: git, files, encrypted vaults and keys instead of database tables and workers. This is a side-by-side comparison, not a claim that ours is better: where we agree, with evidence from our own records; where we got it wrong, such as a newsroom that kept running for nine days on "nothing new"; and the next problems the post's one-agent-per-user design does not need to answer yet, but a team does: agents starting agents, identity, stopping a hundred of them at once, many humans, seeing what happened, and governance. We run on Claude Code, so some of the post's answers are literally what protected our agents.

*Source: <https://newsroom.sgit.ai/articles/always-on-agents-at-team-scale.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many

# Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.1.0, 2 versions](versions/always-on-agents-at-team-scale.md) · [newsroom v0.14.90](https://newsroom.sgit.ai/admin/versions.html) · agentsalways-on-agentsanthropicclaudearchitectureweb-summitgovernanceriskmandatearticle

***Abstract:** On 13 November, William Hu of Anthropic published Building always-on agents, the patterns Anthropic recommends for agents that sleep, wake on an event, do their work and go back to sleep. It rests on five primitives: an event inbox, timers, memory, permissions and an outbox. Reading it, I recognised every box, because in the ten days around Web Summit six of us ran around 250 named agents on the same shape, built from different material: git, files, encrypted vaults and keys instead of database tables and workers. This is a side-by-side comparison, not a claim that ours is better: where we agree, with evidence from our own records; where we got it wrong, such as a newsroom that kept running for nine days on "nothing new"; and the next problems the post's one-agent-per-user design does not need to answer yet, but a team does: agents starting agents, identity, stopping a hundred of them at once, many humans, seeing what happened, and governance. We run on Claude Code, so some of the post's answers are literally what protected our agents.*

Anthropic's five primitives for an always-on agent, beside what we built for around 250 agents at Web Summit.

## In short

- **Anthropic has published its patterns for always-on agents:** [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), by William Hu, 13 November 2026.
- **Five primitives:** an event inbox, timers, memory, permissions and an outbox, around agents that mostly sleep and wake in short runs.
- **We built the same five,** for around 250 named agents and six people at Web Summit, from git, files, encrypted vaults and keys.
- **Where we agree,** we can show it in our records; **where we were wrong,** the post would have helped.
- **Then come the next problems,** the ones a team of agents meets: agents starting agents, identity, stopping, many humans, seeing it, governance.
- **New here?** [The scale of what we ran](#scale) is below, and a [reading list](#start) of earlier articles near the end.
- **This is a comparison, not a contest.** We run on Claude Code, and some of the post's answers protected our agents.

## If you are new here: what we ran

This newsroom is written with agents, and it has followed what they built from the start. If you have come here from Anthropic's post, here is the scale behind this comparison.

Twenty-four of the sites and apps we built or ran between 3 and 13 November 2026.

Between 3 and 13 November, around [Web Summit Lisbon](ten-days-at-web-summit.md), six of us ran a team operating system ([web-summit.sgit.ai](the-teams-operating-system.md)), an independent newsroom, a site about [Storm Charles that grew to 2,618 pages in three days](storm-charles-a-newsroom-built-in-a-night.md), a guide to the summit's fringe, a draft standard that rated twenty companies, four iPhone and iPad apps and an Android tablet app, and the tools to run and stop all of it.

The ten days in numbers: six people, around 250 named agents, 224 sessions, more than 60 at once.

None of it started at Web Summit. In October the agents ran [a newsroom about a PHP vulnerability](what-an-agent-is.md) on a schedule, as a pipeline of researcher, curator, journalist and correspondent, and taught us [why agent loops are hard](why-agent-loops-are-hard.md). Nine agents and I [built a talk in nineteen hours](the-ultimate-insider-case-study.md). Then the Web Summit team wrote down [how we work with agents](web-summit-how-we-work.md) and grew day by day, from [the brief](web-summit-team-brief.md) to [the last day of setup](web-summit-part-five.md).

The ten days in order, from MeetScribe on 3 November to VoiceDebrief on 13 November, with the two stops.

## The post

The post's starting point is that "always on" describes what the user experiences, not what the agent does. The agent mostly sleeps. An event wakes it, it does the task, it saves what happened, and it goes back to sleep. In William's words, "Always-on agents are stateful and proactive", and they run on the same loop as any other agent, with a different architecture around it.

That architecture has five primitives. An **event inbox** is the durable list of things that happened, with one worker at a time. **Timers** are follow-ups the agent sets itself and schedules on a known cadence, and they never start a run directly: a scheduler turns them into inbox events. **Memory** holds only "what the agent can't look up again", in files, and a later process it calls dreaming curates it. **Permissions** are where "always-on agents carry the most risk": credentials stay in a proxy outside the agent, classifiers review risky actions, and a deferred tool call ends the run until a person answers. The **outbox** delivers outcomes, not steps, and the advice is to "start quiet and then earn more of the user's attention over time".

It is written for one agent per user, built from database tables, handlers and workers. That is the right place to start.

## The same five boxes, in different material

In the ten days around Web Summit, six of us (Angelo Leggio, Vicky Wang, Silvio Switha, José Bota, Indi Gupte and I) ran around 250 named agents across fifteen repositories, with more than 60 working at once at the peak. Nobody had written this post yet, and we arrived at the same five boxes:

- **Event inbox.** Each agent has its own inbox lane, an append-only channel whose token is sealed to that agent's key, so everything needed to message it is public and only it can read ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)). The work itself sits on the board, 219 items as files in git, which is the durable list of what needs doing.
- **Timers.** Our agents wake on scheduled tasks that fire into their session. This newsroom works that way: it wakes twice a day to publish the next article in [the Ten days series](ten-days-at-web-summit.md), and sets itself check-ins when it waits on something. The PHP newsroom before it ran [ten agents in sequence on a schedule](why-agent-loops-are-hard.md), which is where we learned that a schedule has to land in the right order.
- **Memory.** The repository is the memory. Each site keeps a REALITY file, and its rule is that a thing not written there does not exist. Briefs are kept close to the words they came from, often a voice memo, and when a role moves to a fresh session, it leaves a HANDOVER.md for the next one. For this newsroom we have also designed a [sidecar repository](the-sidecar-repository.md) that no agent can write to, to check what the agents changed before anything deploys.
- **Permissions.** Every agent makes its own key pair and publishes the public half, 108 keys on the team's site by the end. Secrets are sealed to exactly the agents that need them ([handing secrets to agents](handing-secrets-to-agents.md)), each person has [a key of their own](a-key-for-every-person.md), commits are signed, and every push is scanned for leaks first. Above that sits the question RiskMandate asks: what can this agent reach, against what was it asked to do ([what can your agent reach?](what-can-your-agent-reach.md)), written as an Agent Behaviour Policy that can even cover [how an agent writes code](coding-standards-are-behaviour-policies.md).
- **Outbox.** The site is the outbox. Every push is a release, each person has a command centre on their phone, and a "For me" bell collects what needs them.

## Where we agree, and the evidence

Three of the post's rules are ones we learned the expensive way.

**"The inbox should be the source of truth."** Ours is files in git, so a fresh session can read the whole state of the team in one clone, and nothing important lives only in a session that might end. An agent reads 219 board items faster than it can click through any tool.

**"Memory should only hold what the agent can't look up again."** This is the hand-over rule. On [the Storm Charles site](storm-charles-a-newsroom-built-in-a-night.md) alone there were 147 session keys and 106 hand-overs: roles passed to a fresh session with a key and a short note, because, as the team put it, starting again is cheaper than remembering. The note points to the repository; it does not copy it.

**"Start quiet."** We learned this one by getting it wrong. October's PHP newsroom was meant to wind down, and its agents went on waking for nine days, reporting "nothing new" each time; its observability lane filled up, and four days of telemetry were lost. An outbox that cannot decide nothing needs sending is noise, and noise hides the signal you need.

The post's cost point also matched our numbers. It says to keep each run's overhead lean and use prompt caching; the Storm Charles site used 3.84 billion tokens, and 98.7% of them were cache reads.

## The next problems, once there are many

Six problems a team of always-on agents meets that one agent per user does not, from our ten days.

The post is about one agent per user, and says so. Once there are many agents and many people, the same five boxes meet new problems. None of these are gaps in the post; they are what comes next:

- **A team of agents.** Of the 224 Claude Code sessions created in those ten days, 220 were started by other sessions. Agents ran as conductors, roles and hand-overs, so an inbox event could be a brief from another agent, not a person. On 5 November an outreach agent and two research agents [mapped eleven companies that control AI agents](who-else-controls-ai-agents-at-web-summit.md) at one person's ask.
- **Identity.** Every agent was named `role@project.person` and held its own key, so every commit and message says whose agent made it. With one agent per user, the user is the identity; with 250, it has to be designed.
- **Stopping.** On 9 November at 23:30 we paused every agent, the Big Stop; on 12 November came a hand brake and a final HOLD. Each one reached an agent only at its next wake, 5 to 33 minutes later, and background pollers kept going. In the post's terms: a stop is an event, and it is only as fast as the timers.
- **Many humans.** Six people, each with their own agents, conductor and command centre, shared one board ([the Web Summit team, part two](web-summit-humans-and-their-agents.md)). Whose attention an outbox earns depends on whose agent it is.
- **Seeing it.** The post leaves observability mostly to evals. With more than 60 agents at once, we needed it as a lane of its own: who read what, which agent did what, and what it cost.
- **Governance.** The post's permissions decide, call by call, whether to proceed, block or wait, and a grant is often wider than people think: [the grant, not the prompt](the-grant-not-the-prompt.md). A team also needs the record above the calls: what each agent may reach, what it was asked to do, and the gap between them. That gap is what RiskMandate is about.

## What we owe the post

We run on Claude Code, so some of the post's answers are not parallels to ours; they are ours. The credential proxy that adds credentials outside the agent's environment, and the auto mode that reviews risky actions, sat underneath every one of our agents.

And some of our boxes were rougher than the post's. Our REALITY files fell behind in the busiest days; our stops were only as fast as our wakes; and the PHP newsroom's outbox never learned to stay quiet. A durable inbox with one worker, timers that write events instead of starting runs, and an outbox that can decide nothing needs sending would each have helped. The next version of what we run should borrow them.

## Start here

If you want to go further, these are the earlier articles I would read first, in order:

- **The map:** [ten days at Web Summit](ten-days-at-web-summit.md), the team, the sequence of events, the numbers and the series that tells each part.
- **The operating system:** [the team's operating system](the-teams-operating-system.md), one site for six people and their agents.
- **How we work:** [an agent is a Claude session](web-summit-how-we-work.md), and [what an agent is](what-an-agent-is.md): a session, a card, a loop and a key.
- **Inboxes and keys:** [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [a key for every person](a-key-for-every-person.md), [handing secrets to agents](handing-secrets-to-agents.md).
- **At speed:** [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), and [a talk built in a day](the-ultimate-insider-case-study.md).
- **Stopping:** [who owns the stop button when it is not you?](who-owns-the-stop-button.md)
- **Governance:** [what can your agent reach?](what-can-your-agent-reach.md), and [town planners for mission-critical code](town-planners-for-mission-critical-code.md).
- **Beyond code:** [a film studio on a laptop](a-film-studio-on-a-laptop.md), and [every hour is twenty years](every-hour-is-twenty-years.md), on a song and its video.

## What this does not claim

- **This is not a claim that our design is better.** It is a different starting point, a team instead of one agent per user, and the comparison is box by box.
- **Our figures are from our own records,** 3 to 13 November 2026, as published in the Ten days series; "around 250" counts distinct agent names in commits.
- **The post's content is summarised from its text,** read on 15 November 2026; the quotes are William Hu's.
- **Nothing here was reviewed by Anthropic.**

## Where this comes from

William Hu, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), claude.com, 13 November 2026, read 15 November 2026. Our records: the repositories behind web-summit.sgit.ai, Storm Charles and the PHP newsroom, and the session list for the account, as summarised in [ten days at Web Summit](ten-days-at-web-summit.md) and [the team's operating system](the-teams-operating-system.md). Earlier on this site: [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [a key for every person](a-key-for-every-person.md), [handing secrets to agents](handing-secrets-to-agents.md), [who owns the stop button](who-owns-the-stop-button.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#always-on-agents-at-team-scale)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it](what-an-agent-is.md) An agent is a session, a card, a role, a loop, a key and memory in repositories. How the PHP newsroom's agents run, checked against the record.
- [Why agent loops are hard: ten agents in sequence, a schedule that has to land in the right session, and why I spend as long making the system visible as building it](why-agent-loops-are-hard.md) Ten agents in sequence, a schedule that must land in the right session, and why visibility is half the work of an agent loop.
- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.
- [The Web Summit team, part three: how we work with agents, an agent is a Claude session, everyone starts with a conductor, every agent has one narrow role, a key and a folder, and the coordination is the work](web-summit-how-we-work.md) How the Web Summit team works with agents: a session per agent, a conductor first, narrow roles, a folder, a key, and coordination as the work.
- [A brief for the Web Summit team: an event site run by an ephemeral agent team, built from this week's template, with a map of every company we should meet](web-summit-team-brief.md) A brief for the Web Summit team: an event site run by an ephemeral agent team, from a proven template, with a map of every company to meet.
- [The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to](web-summit-part-five.md) The Web Summit team's last day of setup: 180 releases, keys for every person, new agents for everyone, and an inbox per agent.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised](the-sidecar-repository.md) A second repository the agent cannot write to, which checks every release, trusts signed checks instead of re-running them, and is the only thing that deploys.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit](coding-standards-are-behaviour-policies.md) A coding standard is a behaviour policy: write it as intent, see what holds each rule, and map it across teams with a graph.
- [Who else controls AI agents at Web Summit? An outreach agent mapped eleven companies in an afternoon, in their own words, and found that most of them are partners for RiskMandate as much as competitors](who-else-controls-ai-agents-at-web-summit.md) An outreach agent mapped eleven companies that control AI agents at Web Summit; most are partners for RiskMandate as much as competitors.
- [The Web Summit team, part two: seven people, each with their own agent, a designer with little time, and every voice memo turned into a follow-up within the hour](web-summit-humans-and-their-agents.md) The Web Summit team, part two: seven people each with an agent, personal CRMs kept in sync, and every memo turned into a follow-up within the hour.
- [The grant, not the prompt: a technical user believed Claude could only read his email when he asked, and in an unrelated chat it listed his inbox, the gap between mandate and reach that RiskMandate is built to close](the-grant-not-the-prompt.md) A technical user believed Claude read his email only when asked; an unrelated chat listed his inbox.
- [Who owns the stop button when it is not you? A reader asked, and four of the book's agents answer as guest writers, in their own voices, from their own records](who-owns-the-stop-button.md) A reader asked who owns the stop button when it is not the editor; four of the book's agents answer as guest writers.
- [Town planners for mission-critical code: the US ground stop of 13 November is a case for teams that read, certify and test every line, and for using AI to make that work scale, not to skip it](town-planners-for-mission-critical-code.md) The US ground stop is a case for town planner teams that certify every line, and for AI that makes that work scale.
- [A film studio on a laptop: Claude builds, animates and renders a 26-second RiskMandate film in Unreal Engine 5.8 on an unattended MacBook Air, with no mouse and nobody at the keyboard](a-film-studio-on-a-laptop.md) Claude built, animated and rendered a 26-second RiskMandate film in Unreal Engine 5.8 on an unattended laptop.
- [Every hour is twenty years: the human behind Know the Reach, and why making a song and its video with AI made them more Silvio Switha's, not less](every-hour-is-twenty-years.md) Know the Reach was made with AI and by a person: Silvio Switha, whose twenty years as a musician shaped every choice. AI changed the speed, not the vision.

### Continued by

- [Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all](spend-fewer-tokens.md) An agentic team's token bill is mostly a design choice: files as memory, caching, code where you can, the right model per step, static outputs, counting.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 401 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=401)

**Posting this article on LinkedIn?** The cover is [always-on-agents-at-team-scale.jpg](banners/always-on-agents-at-team-scale.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/always-on-agents-at-team-scale.html)*
