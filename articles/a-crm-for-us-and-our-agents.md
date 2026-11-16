# A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it, sgit.ai

> The next stage of our development is a CRM. I have built several versions of one before, this is the fourth or fifth, but it is now critical. After Web Summit we have a lot of people to follow up, a lot of messages to send, introductions to make ("you should talk to this person", as I heard again in a meeting today), and no single place that connects those dots. And we have most of the pieces: vaults now work in the iOS app, images upload at scale, Apple Intelligence runs on the device, and the app can talk back to its developers through a lane. So I think a CRM is a product in itself, with an iOS app of its own. We researched the field. Among open-source CRMs, Twenty leads clearly on momentum and agent readiness, with its own MCP server and roles per API key; Atomic CRM and Relaticle are small and agent-friendly. Among commercial agentic CRMs, Attio, folk, HubSpot, Day AI and Lightfield all point the same way: agents propose, people approve, drafts are not sent without a person. None meets our constraints, encrypted vaults, a key per agent, no servers of our own, written behaviour policies, so the plan is to build the record ourselves, with a small data model where introductions and drafts are first-class, and to use Twenty as the reference and an optional interface. And the most important idea: we build it by using it first on ourselves. Customer feedback is slow; our own team's and our own agents' communications are not. Managing a fleet of agents is relationship management, almost one to one: an agent is a contact, a team is an organisation, a message on a lane is an interaction, a hand-over is an introduction, the board is the pipeline. So the CRM tracks our own agents and workflows first, synthetic users answer our emails, and then it follows up the many Web Summit leads. It needs two teams, as everything does now: one that develops the CRM, and an agentic team that uses it, with people approving and sending.

*Source: <https://newsroom.sgit.ai/articles/a-crm-for-us-and-our-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it

# A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/a-crm-for-us-and-our-agents.md) · [newsroom v0.14.121](https://newsroom.sgit.ai/admin/versions.html) · crmagentsvaultsiosopen-sourceabpoutreachproductarticle

***Abstract:** The next stage of our development is a CRM. I have built several versions of one before, this is the fourth or fifth, but it is now critical. After Web Summit we have a lot of people to follow up, a lot of messages to send, introductions to make ("you should talk to this person", as I heard again in a meeting today), and no single place that connects those dots. And we have most of the pieces: vaults now work in the iOS app, images upload at scale, Apple Intelligence runs on the device, and the app can talk back to its developers through a lane. So I think a CRM is a product in itself, with an iOS app of its own. We researched the field. Among open-source CRMs, Twenty leads clearly on momentum and agent readiness, with its own MCP server and roles per API key; Atomic CRM and Relaticle are small and agent-friendly. Among commercial agentic CRMs, Attio, folk, HubSpot, Day AI and Lightfield all point the same way: agents propose, people approve, drafts are not sent without a person. None meets our constraints, encrypted vaults, a key per agent, no servers of our own, written behaviour policies, so the plan is to build the record ourselves, with a small data model where introductions and drafts are first-class, and to use Twenty as the reference and an optional interface. And the most important idea: we build it by using it first on ourselves. Customer feedback is slow; our own team's and our own agents' communications are not. Managing a fleet of agents is relationship management, almost one to one: an agent is a contact, a team is an organisation, a message on a lane is an interaction, a hand-over is an introduction, the board is the pipeline. So the CRM tracks our own agents and workflows first, synthetic users answer our emails, and then it follows up the many Web Summit leads. It needs two teams, as everything does now: one that develops the CRM, and an agentic team that uses it, with people approving and sending.*

Two teams: one builds the CRM, one uses it, under behaviour policies where only a person sends.

## In short

- **A CRM is now critical:** after Web Summit, many people to follow up, messages to send and introductions to track.
- **Most pieces exist:** vaults in the iOS app, image uploads, Apple Intelligence, a lane back to the developers.
- **Use it on ourselves first:** our own team and our own agents, where the feedback loop is minutes, not weeks.
- **A fleet of agents is a CRM:** agents are contacts, lanes are interactions, hand-overs are introductions, the board is the pipeline.
- **The field, researched:** Twenty leads the open-source CRMs; the commercial agentic CRMs agree that agents propose and people approve.
- **None fits our constraints,** so we build the record ourselves, on vaults, and use Twenty as reference and optional interface.
- **Introductions and drafts are first-class records;** agents never send.
- **Two teams:** one develops the CRM, one uses it.

## Why now

I have built several CRMs before; this is about the fourth or fifth. Each was useful and none became the place where everything is. Now it has to be. After Web Summit we have a long list of people to follow up, a lot of messages to prepare, and a constant stream of introductions: I came out of a meeting today with exactly that, "you should talk to this person". Without one place that connects those dots, they get lost.

What we need is a pipeline. When we meet someone at the summit, what happens next, what the status is, who has to contact whom, and what was said. The contacts, the history and the follow-ups exist in pieces across our teams' repositories and lanes ([the team's operating system](the-teams-operating-system.md)). They need to come together.

## The pieces we already have

In the last couple of days, the iOS app proved most of what a CRM app needs. Vaults work in the app, and the upload of images scales, so a photo of a card or a badge can become a record. Apple Intelligence runs on the device. The app can talk directly back to its developers, and signed comments now travel from the app to the conductor through a lane ([native apps by agents](native-apps-by-agents.md)). Every person and agent has a key ([a key for every person](a-key-for-every-person.md)), and our agents already draft outreach that a person sends ([PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md)).

So I think a CRM is a product in itself, and it should have an iOS app of its own: the place where I capture a contact in the corridor, see who needs a follow-up, read the draft an agent prepared, and send it.

## Use it on ourselves first

Managing a fleet of agents is relationship management: the same records, almost one to one, and what we have.

The most important part of the plan is not the technology. When you develop something, you need a fierce focus on usability and live examples, which is why Web Summit was so powerful for us: it gave us a real workflow to build our technology on, and to show it working. A CRM built only for customer interactions would have a slow feedback loop: you send a message, they reply days later, you update the record. Too slow to learn what hurts.

So I always look for ways to use what we are building on ourselves, even when it is a bit of a stretch, because what comes out is much better. Here it is not a stretch at all. Customer relationship management is really relationship management, and we already have a lot of relationships to manage: our own team, and our own agents.

Managing a fleet of agents maps onto a CRM almost one to one. How many agents exist at any moment, who they are, what their identity and key are, who they work for, what they are doing: that is a contact list, and I already have the problem of keeping it. A team or a repository is an organisation. A message one agent sends another on a lane is an interaction, and should be tracked as one. A hand-over to a fresh session, or a new agent joining a team, is an introduction. An ask waiting on someone is a follow-up. A pull request or a planned change is a draft. And our Kanban boards are the pipeline. That holds from the smallest group of five agents to the most powerful workflows we run.

We can also close the loop on the outreach side before real people are involved: synthetic users can answer our emails, push back on a proposal, ask for an infographic, so the whole cycle runs many times a day ([synthetic users for your website](synthetic-users-for-your-website.md)).

And this is what we sell anyway. When we sell an agentic team, we sell an environment where you have maximum visibility of what is happening ([an agentic console](an-agentic-console.md)). A CRM of your agents and your people is that visibility, written down. Then the same CRM follows up the many Web Summit leads, the custom proposals and the infographics each of them needs.

## What the field looks like

The CRM landscape through an agent's eyes: licence, agents or MCP, writes as proposals, drafts rather than sends.

We researched the open-source and agentic CRMs on 16 November 2026:

- **Twenty** is the clear leader among open-source CRMs: very active, with releases every few days, GraphQL and REST, objects defined as code, and, since version 2.0 in April, agents, chat and its own MCP server, where a connection inherits the permissions of the user or of the role assigned to the API key ([Twenty's MCP documentation](https://docs.twenty.com/developers/extend/mcp)). Its examples include agents that draft and send follow-ups, which is exactly what we would turn off.
- **Atomic CRM** (MIT, on Supabase) and **Relaticle** (AGPL) are small and agent-friendly; Relaticle's assistant proposes writes for a person to approve.
- **EspoCRM and SuiteCRM** are mature and conservative, with no agent story yet; **Monica**, the personal CRM, has effectively stalled.
- **Commercial agentic CRMs** point the same way. Attio's assistant proposes changes that do nothing until you confirm, and does not send email without approval; folk's documented recipe is to read, draft for a person to send, then log; HubSpot's prospecting agent has a switch between review and send; Day AI and Lightfield queue drafts for approval. Almost all of these claims are the vendors' own.

What none of them documents is a record of what each agent did, as opposed to each user; acting as the user hides which agent did what.

## Build the record, borrow the ideas

A small data model: people, organisations, interactions, introductions, follow-ups, drafts and plays.

None of the products meets our constraints: encrypted vaults, a key for every agent, no servers of our own, and written behaviour policies. Every open-source option needs a database and a running server; every commercial one keeps the data on the vendor's side and logs per user. The data model we need is small, and the mechanics, proposals, signatures and history, already exist in vaults, lanes and git ([how a vault works](how-a-vault-works.md)).

So the plan is to build the record ourselves and borrow the best ideas:

- **Proposals, not changes** (Attio, Relaticle): agents append proposed records to a lane; a person, or a policy-checked step, accepts them.
- **Drafts, never sends** (HubSpot, folk, Lightfield): a draft has a status; a person sends it; the sent message is logged back as an interaction.
- **A key per agent** (Twenty's roles per API key, done our way): every change says which agent made it.
- **A source on every value** (Day AI): why the CRM believes what it believes.
- **Introductions as first-class records:** who suggested it, between whom, why, and whether it happened. None of the products we looked at treats them that way, and for us they are the heart of it.
- **Twenty as reference and interface:** a sync from our vault records to a Twenty workspace gives anyone who wants a classic CRM screen one, without making it the source of truth; customers' CRMs are reached through their own APIs, the way we use whatever is on the other side ([integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md)).

## Two teams

Like everything now, the CRM needs two teams. A team of agents that develops it: the record format, the iOS app, a web view for the desk, an MCP adapter, and the syncs. And an agentic team that uses it: an agent that captures contacts from the summit, meetings and introductions, with sources; one that proposes merges of duplicates and, separately, enriches with provenance; one that plans who to follow up and by when; and one that drafts the emails in our voice for a person to read, change and send. A specialist agent for behaviour policies writes their policies ([specialist agents for every team](specialist-agents-for-every-team.md)).

The policies are simple and strict: a key per agent; writes as proposals; every value with its source; and no agent ever sends an email or posts. A person does.

## The next steps

1. **Our own fleet first:** our agents, teams, lanes, hand-overs and boards as records, so the CRM is used every hour.
2. **The record format and the import:** the summit contacts, the introductions and the follow-ups we already have, into vaults, deduplicated by proposal.
3. **The follow-up pipeline:** statuses, owners and next steps, and drafts for the first batch of follow-ups.
4. **The iOS CRM app:** capture, the list of who needs what, read and send a draft.
5. **The sync to Twenty,** for a classic interface, and the MCP adapter for agents.
6. **Then the product:** a CRM for teams like ours, on the AgentiCCells ladder.

## What this does not claim

- **This is a plan;** the CRM does not exist yet in this form.
- **The research is a snapshot** of 16 November 2026; star counts were rounded and some release dates had no year.
- **Most approval and audit claims are the vendors' own,** not independently confirmed.

## Where this comes from

My own thinking, 16 November 2026, and a research agent's review of the field the same day: [Twenty](https://github.com/twentyhq/twenty) and [its AI documentation](https://docs.twenty.com/getting-started/core-concepts/ai), [Heise on Twenty 2.0](https://www.heise.de/en/news/Twenty-2-0-The-open-source-CRM-follows-up-11268835.html), [Atomic CRM's MCP server](https://marmelab.com/atomic-crm/doc/users/mcp-server/), [Relaticle's comparison](https://relaticle.com/blog/relaticle-vs-twenty-an-honest-comparison), [EspoCRM](https://github.com/espocrm/espocrm), [SuiteCRM](https://github.com/SuiteCRM/SuiteCRM-Core), [Monica](https://github.com/monicahq/monica), [Attio's assistant](https://attio.com/help/reference/attio-ai/ask-attio/chat-with-ask-attio), [folk's MCP recipe](https://help.folk.app/en/articles/15533142-draft-and-log-a-personalized-follow-up-with-folk-mcp), [HubSpot's prospecting agent](https://knowledge.hubspot.com/prospecting/use-the-prospecting-agent), [Day AI](https://day.ai/guides/best-ai-native-crm), [Lightfield](https://lightfield.com), [Contrary Research on Lightfield](https://research.contrary.com/company/lightfield). Earlier on this site: [an agentic console](an-agentic-console.md), [synthetic users for your website](synthetic-users-for-your-website.md), [integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md), [specialist agents for every team](specialist-agents-for-every-team.md), [native apps by agents](native-apps-by-agents.md), [the team's operating system](the-teams-operating-system.md), [a key for every person](a-key-for-every-person.md), [how a vault works](how-a-vault-works.md), [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#a-crm-for-us-and-our-agents)

### Builds on

- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Synthetic users for your website: how to set up five invented visitors who read your site one screenshot at a time, with Claude, a sub-agent per persona, and an encrypted vault you can publish anywhere](synthetic-users-for-your-website.md) Onboarding for synthetic users: invented personas, a sub-agent each, a real browser one screenshot at a time, all in a vault you publish.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place](integrate-with-whatever-is-on-the-other-side.md) We never start by asking a customer to move. We integrate with what they run, build around it, and either retire our code or become the better place.
- [Specialist agents for every team: long-lived agents that keep one skill, design, UX, code, security, behaviour policies or writing, with a person who owns it, so that new teams start from our best work instead of from scratch, and why that makes expertise that never scaled into something you can hire, even from another company](specialist-agents-for-every-team.md) Specialist agents for design, UX, code, security, ABP and writing serve every team, so new ones start from our best work. Expertise you can hire.

### Continued by

- [VoiceDebrief, relaunched: what the iPhone and iPad app already does, from recording without loss to an on-device transcript, a debrief and an encrypted vault, why the agent workflows move to the CRM app, and the list that takes it to the App Store properly, under its own name and its own accounts](voicedebrief-relaunch.md) VoiceDebrief is ready for market: record, transcribe and debrief on the device, save to a vault. A simpler relaunch, under its own name and accounts.
- [The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with one gateway agent that alone touches Gmail, a digital twin of the mailbox in a vault that people and agents work on together, signed proposals, approvals and even reads on append lanes, and behaviour policies at five altitudes](the-email-agentic-cell.md) Our own email connector: one gateway agent touches Gmail, everyone else works on a signed twin of the mailbox in a vault, with policies at five altitudes.
- [PrompTugal.news, the next phase: a roadmap for the team that ran it at Web Summit and the people who want to join, from outreach and contributors to local news partners, a subscribe box on every page, regional updates and a verification layer that says who has checked each story, with twelve task cards to point an agentic team at](promptugal-news-the-next-phase.md) The PrompTugal.news team wants to continue. A roadmap: outreach by agentic teams, local partners, a subscribe box, a verification layer, twelve cards.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 430 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=430)

**Posting this article on LinkedIn?** The cover is [a-crm-for-us-and-our-agents.jpg](banners/a-crm-for-us-and-our-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-crm-for-us-and-our-agents.html)*
