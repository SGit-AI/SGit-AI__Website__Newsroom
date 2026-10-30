# A brief for the Web Summit team: an event site run by an ephemeral agent team, built from this week's template, with a map of every company we should meet, sgit.ai

> Web Summit runs in Lisbon from 9 to 12 November, and seven of us are now going. The plan I published on 26 October called for a newsroom of our own for the summit. This is the brief to build it, now that we have a template that works. In the last two days three teams were stood up from nothing in a few hours each: the talk's, the cold read's and the book's. Each had a repository, a written brief, a role file and a behaviour policy per member, a key for every session, an hourly slot, a five-step wake, a hold any member can pull, a board and a mailroom in git, and a gate with CI owning the version. The Web Summit team gets the same, on an event site that consolidates everything about our participation: the graph of companies and people, the events and sessions, the materials, and a countdown with observability, so we can see what is used. Its centre is a map of the companies going, built from public material only: who they are, what they do, why they matter to us, and whether we should meet them, interview them or write about them, each with an owner on our team. Each person's email stays in their own account, run by their own email agent, and each of those agents gets a key, so that what it sends can be verified; that is a separate brief. The design track, T-shirts, hoodies, a banner, cards for everyone and flyers, gets its own brief and its own design member. This article sets out the site, the template, the roles, the company map, the schedule to 12 November, and what I need to decide.

*Source: <https://newsroom.sgit.ai/articles/web-summit-team-brief.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A brief for the Web Summit team: an event site run by an ephemeral agent team, built from this week's template, with a map of every company we should meet

# A brief for the Web Summit team: an event site run by an ephemeral agent team, built from this week's template, with a map of every company we should meet

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-30 · [article v1.0.0](versions/web-summit-team-brief.md) · [newsroom v0.14.7](https://newsroom.sgit.ai/admin/versions.html) · web-summitagent-teamsbriefseventspkistartupsarticle

***Abstract:** Web Summit runs in Lisbon from 9 to 12 November, and seven of us are now going. The plan I published on 26 October called for a newsroom of our own for the summit. This is the brief to build it, now that we have a template that works. In the last two days three teams were stood up from nothing in a few hours each: the talk's, the cold read's and the book's. Each had a repository, a written brief, a role file and a behaviour policy per member, a key for every session, an hourly slot, a five-step wake, a hold any member can pull, a board and a mailroom in git, and a gate with CI owning the version. The Web Summit team gets the same, on an event site that consolidates everything about our participation: the graph of companies and people, the events and sessions, the materials, and a countdown with observability, so we can see what is used. Its centre is a map of the companies going, built from public material only: who they are, what they do, why they matter to us, and whether we should meet them, interview them or write about them, each with an owner on our team. Each person's email stays in their own account, run by their own email agent, and each of those agents gets a key, so that what it sends can be verified; that is a separate brief. The design track, T-shirts, hoodies, a banner, cards for everyone and flyers, gets its own brief and its own design member. This article sets out the site, the template, the roles, the company map, the schedule to 12 November, and what I need to decide.*

The Web Summit team: seven people, and the agent roles that work for them on an hourly schedule.

## In short

- **Seven of us go to Web Summit,** from 9 to 12 November in Lisbon, and we need one place to run it from.
- **An event site, run by an agent team,** consolidates the graph of companies and people, the events, the materials and a countdown.
- **The template is proven.** The talk's, the cold read's and the book's teams were each stood up in hours with the same setup.
- **Every member has a role, a policy, a key and a slot,** and every wake is planned, reviewed and checked.
- **The centre is a map of companies:** who is going, what they do, and whether we meet, interview or write about them, each with an owner.
- **Email stays in our own accounts,** each run by its own agent with its own key; that is the next brief.
- **Design gets its own brief and member:** T-shirts, hoodies, a banner, cards and flyers for seven people.

## What changed since the plan

On 26 October I published [the plan](web-summit-2026-the-plan.md): usage first and the sale after, three parallel tracks of intelligence, outreach and content, the method of an asset, a page and a link, and a newsroom of our own for the summit, built like the PHP story site but simpler. Two things have changed since.

There are now seven of us going, not five. And in the last two days we found out how to stand up an agent team in a few hours, three times: the [talk's team](the-ultimate-insider-case-study.md), and then overnight the book's team and a cold read of the talk by a second team, both described in [the book of the talk](the-book-of-the-talk-and-its-companion.md). Together with the PHP story site's newsroom and the email workflow behind RiskMandate, that is a template. This brief applies it.

## The site

The site is an event site for our participation in Web Summit. I would call it something like an sgit event site for Web Summit; the exact address is for the developers to settle with me. It consolidates what is now scattered:

- **The graph.** Companies, people, sessions and our own products, and the connections between them, each with its public source.
- **The events and the materials.** The programme, the sessions we go to, the meetings we book, and every asset we make for someone, with its link.
- **The synchronisation.** What each of us did today, and what is next, so seven people work as one team.
- **A countdown and observability.** Days to Lisbon on the front page, and numbers that show activity: pages made, links sent, pages opened, meetings booked. If we cannot see what is used, we cannot tell where we add value.

Web Summit's own website is hard to find things on. We can do better for ourselves, and some of what we build, a clear map of who is there and what they do, may be useful to others too.

## The template

What every ephemeral team gets from day one, as set up for the talk, the cold read and the book this week.

Every member of the team gets the same setup the last three teams had:

- **A repository, a brief and a reality file.** The brief says what the team is for; `REALITY.md` says what exists, and anything not in it does not exist, whatever a brief says.
- **A role file and a behaviour policy** per member, with the paths it may write; the gate fails if two members claim the same file.
- **A key for every session,** made by the session, its public half published beside its role. The push is the authorisation.
- **An hourly slot,** fifteen minutes apart, in the order the work flows, and a scheduled task each member creates in its own session.
- **The five-step wake:** a plan, a review of the plan, at most 45 minutes of work, a review of the work, and a check against the plan, each recorded.
- **A hold** any member can pull, which stops every wake until I lift it.
- **A board and a mailroom in git,** as the cold read used: issues and letters as files, one writer per file, public by design, so nothing private goes there.
- **A gate, and CI that owns the version,** so a release is checked, numbered and live within minutes.
- **A list of what done means** for each member. An event team is ephemeral: when its work is done, each member pauses its own task.

## The roles

Seven people, and the agents that work for them. Each person owns one agent's output and reviews it daily, as the plan said.

- **Conductor.** Routes requests, keeps the schedule, the keys and the site true, and writes the daily debrief.
- **Researcher.** Builds the company map from public material only: the exhibitor and speaker lists, the startups, their own sites and news, each fact with its source and date.
- **Cartographer.** Keeps the graph: companies, people, sessions and our products, and the links between them; flags the companies worth a meeting.
- **Writer.** Makes the assets: a page for one company, an interview's questions, an article that brings traffic, in the newsroom's voice.
- **Curator.** Runs the feed: the programme, the sessions, the news about the summit, each item with its source.
- **Analyst.** The observability: the countdown and the numbers of what was made, sent, opened and booked.
- **Designer.** The design track, with its own brief.
- **Security.** Reviews every wake's plan and work, as in the five steps, and owns the hold.
- **The email agents.** Each of us has their own email, in their own account, run by their own agent, which reads the site and drafts what goes out; a person sends every email.

## The company map

One company on the map: what we know from public sources, why it matters, the decision, the owner, the assets.

The heart of the site is the map of companies going to Web Summit. For each one:

- **Who they are and what they do,** from their own public material, with the source and the date read.
- **Why they matter to us,** in one line: a customer, a partner, a story, an investor, or none.
- **The decision:** meet them, interview them, write about them, or describe what they do on the site.
- **An owner** among the seven of us, and the status: to contact, contacted, meeting booked, met, followed up.
- **The assets made for them,** each a page with a link, because behind every email there is an asset.

It is built from public material only, as the plan says. Nothing private about a person goes on the site or in the board; a person's contact details stay in their owner's email account.

## Email, and a key for each email agent

I thought at first of using a vault for the team's email, as Email-FS does at RiskMandate. We should not: each of us has our own email account. So the site integrates with the email agents each of us already runs, the way [the inbox team as a recipe](the-inbox-team-as-a-recipe.md) set mine up, and each agent stays in its owner's account.

That opens something I want to do next: a key for each email agent. If the agent that runs my email has its own key, vouched for by mine on pki.sgit.ai, every email it drafts can carry a signature and a QR code that lets the recipient check it is really from me. I should have one official email agent, so that anything sent on my behalf can be proved. That is the next brief.

## Design

With seven of us going, we should look like a team. I would like branded T-shirts and hoodies, a banner, cards for everyone and small flyers to hand out. This is money well spent, and it gets its own brief, with a designer on our side and a design member on the team to prepare the files, the variants and the print-ready versions. The designs, like everything else, will be versioned on the site.

## The schedule

- **31 October to 2 November.** The site and the team up from the template: repository, brief, roles, keys, slots, the first release. The company map started.
- **3 to 8 November.** The map filled and prioritised; assets made for the first companies; meetings booked; the design files sent to print; the countdown live.
- **9 to 12 November, Lisbon.** Seven people, one board, a daily debrief on the site, and the map updated after every meeting.
- **The week after.** Follow-up with everyone we met, from the map; the team's debrief; then each member pauses its own task.

## What I need to decide

- **The site's name and address,** and which repository it lives in.
- **Who owns which agent** among the seven of us.
- **The design budget,** and the designer we work with.
- **Which email accounts** join first, and when each email agent gets its key.

## What this does not claim

- **It is a brief.** None of the site exists yet; the template does, in three repositories that ran this week.
- **The company map will be public material only,** and its judgements ours.
- **The schedule is a plan,** written eleven days before the summit.

## Where this comes from

- My voice memo of 30 October 2026, word for word in `admin/notes/2026-10-30__web-summit-team/memo-01.md`.
- [Web Summit 2026, the plan](web-summit-2026-the-plan.md), 26 October 2026.
- The template, as it ran this week: the talk's repository, [SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider); the cold read's, [SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider) (`team/conductor/WAKE.md`, `schedule.json`, `comms/`); and the book's, [SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider).
- Related: [the talk built in a day](the-ultimate-insider-case-study.md), [the book of the talk](the-book-of-the-talk-and-its-companion.md), [the inbox team as a recipe](the-inbox-team-as-a-recipe.md), [agents have an identity now](agents-have-an-identity-now.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#web-summit-team-brief)

### Builds on

- [Web Summit 2026, the plan: a briefing for the team on usage first and the sale after, intelligence from public material, an asset, a page and a link for every person we want to reach, a newsroom of our own for the summit, and the two agentic workflows the team will learn on](web-summit-2026-the-plan.md) Web Summit 2026, the plan: usage first, an asset, a page and a link for every person, a summit newsroom, and two agentic workflows.
- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.
- [The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes](the-book-of-the-talk-and-its-companion.md) Two agent teams, one night: RC1 of the book of The Ultimate Insider, a cold read by a team that knew only the record, and a companion PDF of tick boxes.
- [The inbox team as a recipe: how the RiskMandate agents run my email and CRM, written down by one of them so a second team can copy it](the-inbox-team-as-a-recipe.md) The RiskMandate inbox team, written down by its own agent so a second team can copy it.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.

### Continued by

- [Signed by the agent, vouched for by the person: a brief to give every email agent its own key, so each email carries a QR code that proves it is authentic](signed-email-from-the-agent.md) A brief to give every email agent its own key, vouched for by its person, so each email carries a QR code that proves it is authentic.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 332 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=332)

**Posting this article on LinkedIn?** The cover is [web-summit-team-brief.jpg](banners/web-summit-team-brief.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/web-summit-team-brief.html)*
