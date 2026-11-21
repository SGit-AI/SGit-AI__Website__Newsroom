# An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent, sgit.ai

> What we would sell is an agentic brain: a set of agentic teams that runs the work. But a customer cannot buy what they cannot see or control, so the thing that makes it sellable is a console: a control room for agents, the way a power station or a cloud has one. To show what I mean, this newsroom built a simulated console in a public vault, shaped on our Web Summit team. It draws the ten accounts the six of us used as trust zones, with a conductor and its agents inside each. It shows who is running, on which model, with how many commits, and messages on the three channels our agents use: files in the repository, commit messages and vault append lanes, each signed by its agent's key. It has time: a slider over the ten days and five scenarios to replay, including the Big Stop, because when everything is JSON and markdown you can go back to any moment. It has stop buttons that say when each agent will actually stop, a view for each person, and a talk box, because the console is an agent too. We have, in a sense, already delivered this brain several times: to ruv.sgit.ai, to the book, to Web Summit, with RiskMandate as a partner and PrompTugal.news as its first customer.

*Source: <https://newsroom.sgit.ai/articles/an-agentic-console.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent

# An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/an-agentic-console.md) · [newsroom v0.14.97](https://newsroom.sgit.ai/admin/versions.html) · agentic-consolecontrol-roomagentscommand-and-controlsituation-awarenessvaultsdemoarticle

***Abstract:** What we would sell is an agentic brain: a set of agentic teams that runs the work. But a customer cannot buy what they cannot see or control, so the thing that makes it sellable is a console: a control room for agents, the way a power station or a cloud has one. To show what I mean, this newsroom built a simulated console in a public vault, shaped on our Web Summit team. It draws the ten accounts the six of us used as trust zones, with a conductor and its agents inside each. It shows who is running, on which model, with how many commits, and messages on the three channels our agents use: files in the repository, commit messages and vault append lanes, each signed by its agent's key. It has time: a slider over the ten days and five scenarios to replay, including the Big Stop, because when everything is JSON and markdown you can go back to any moment. It has stop buttons that say when each agent will actually stop, a view for each person, and a talk box, because the console is an agent too. We have, in a sense, already delivered this brain several times: to ruv.sgit.ai, to the book, to Web Summit, with RiskMandate as a partner and PrompTugal.news as its first customer.*

The agentic console: ten accounts as trust zones, every agent as a dot, signed messages and a time slider.

## In short

- **What we sell is an agentic brain;** what makes it sellable is a console to see it and control it.
- **We built a simulated one,** [in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_9665e7ef2d7200078c312216d88e79111907a11dd05ecb83ce7b728a6a60779f%3Auqgr2se3), shaped on our Web Summit team.
- **It has time:** rewind to any moment of the ten days, or replay five scenarios, including the Big Stop.
- **It draws accounts as trust zones,** with a conductor and its agents inside each, and their models, state and commits.
- **It shows the conversation:** messages on three channels, each signed by its agent's key, and stops that say when they land.
- **The console is an agent too,** with its own key, and it can run on your own device.

## A control room for agents

I have always wanted a console like the ones in a power station, or the tablet that shows every room's temperature and lets you switch things on and off, but for a cloud: one place where I can see everything and start and stop it. With agents, it stops being a nice-to-have.

What we would sell is an agentic brain: a set of agentic teams, made for one company, that runs its work ([a brain you arrive at](a-brain-you-arrive-at.md), [selling mini agentic teams](selling-mini-agentic-teams.md)). But a customer cannot buy a brain they cannot see or control. They need to know what is running, see what the agents are saying to each other, make decisions, and be able to stop it. That is the console, and I think it is the thing that sells.

## Customers we already have

Read backwards: ruv.sgit.ai, the book, Web Summit, RiskMandate as a partner, PrompTugal.news as the first customer.

Reading our own history backwards, we have already delivered this brain several times. The first was [ruv.sgit.ai](agentics-ready-to-sell.md), the first time I had an agentic team running on a loop. The second was the book: nine agents built my talk in nineteen hours, and [the book that tells it](the-book-is-on-leanpub.md) was written the same way. The third was [Web Summit](ten-days-at-web-summit.md), with around 250 named agents for six people.

Then come two different kinds of relationship. RiskMandate used the open method for its Agent Behaviour Policies: it is more a partner than a customer. [PrompTugal.news](promptugal-news-the-newsroom-we-ran.md) is a customer: a newsroom that needs a network of agentic teams of different sizes. What all of them needed, and what we had to build piece by piece, is a way to see and control the agents.

## The console, walked through

I asked for a console that simulates what this would look like, using the people, accounts and agents we really had. Here is what [the vault](https://dev.vault.sgraph.ai/#sgit_public_read_9665e7ef2d7200078c312216d88e79111907a11dd05ecb83ce7b728a6a60779f%3Auqgr2se3) does.

**The universe, as trust zones.** The six of us worked from ten accounts: three of mine, two each for Angelo Leggio and Vicky Wang, and one each for José Bota, Indi Gupte and Silvio Switha. Each account is drawn as a dashed box, a trust zone in threat-modelling terms, because everything inside it shares that account's access and credit. Each one has a conductor, `conductor.a@web-summit.dinis` and so on, and the agents it runs, with the names from the team site's public keys. At the top of the screen: how many accounts are active, how many agents are running out of how many, how many are stopped, commits so far, messages in the last hour, and which models are running.

**Zoom.** Click an account and you see its conductor and agents in a table: model, state, how long each has been running, commits, its key, and a stop button. Below it, the account's board, as it stood at that moment. Click an agent and you see its identity, its runs across the ten days, and its latest messages. These are the altitudes from [six setups of an agentic system](six-setups-of-an-agentic-system.md): the network of conductors, a conductor and its agents, one agent.

One account zoomed in: the conductor and its agents, their models, state, commits and keys, and the board.

**The conversation.** Our agents talk in three ways: files they leave in a repository, messages in their commits, and append lanes in encrypted vaults. The console shows all three, filterable, each with the sender, the receiver and a signature checked against the sender's public key. The Flow view draws the last hour of messages between accounts, so you can see the work moving.

The Flow view during "collect every contact": one request from the console fans out to every account.

**Time.** This is the part I care about most. Everything we do is JSON and markdown files, so any moment can be shown again. The console has a slider over the ten days and five scenarios to replay: a normal morning; collecting every contact, where one message to my conductor fans out to every other conductor and their agents and comes back sealed; the Big Stop; storm night, when the incident agents spun up; and the hand brake. Every view, the dots, the numbers, the boards, the messages, shows the state at the moment you choose.

**Stops that tell the truth.** At 23:30 on 9 November we paused every agent, and each one stopped only at its next wake, 5 to 33 minutes later. The console shows that honestly: an agent goes into "stopping" with the time it will actually stop, then into "stopped". You can stop one agent, one account or everything in view, and allow them to wake again.

The Big Stop replayed: every agent stopping or stopped, and the decision log showing when each stop lands.

**A view for each person.** Choose who you are and the console shows your own zones and dims the rest: I see all ten accounts, and Vicky sees her two. The same console, a different scope.

**The console is an agent.** It is signed in as an agent, `console@web-summit.dinis`, with its own key. What you type in the talk box goes on a vault lane, signed, to the conductor you choose, and the answer comes back the same way. Operationally the console behaves like an agent, between the human and the flow, and it can run on the client: we already ran models on devices, Gemma on the Android tablet and Apple's on-device models in VoiceDebrief.

Vicky's view: her two accounts in focus, and a question to her conductor answered on a vault lane.

## Designed for situation awareness

Perceive, understand, project, act: what the console is for, designed like a control room, with colour for exceptions.

Control rooms have thought about this for decades. Mica Endsley's model of situation awareness has three levels: perceive what is there, understand what it means, and project what will happen next. The console adds a fourth, act. And it follows the idea behind high-performance control-room screens in the ISA-101 tradition: a calm grey display where colour only means something needs you. In the console, normal is grey, red is stopped or stopping, and amber is waiting on a person.

## What we would sell, and how it scales

The console is the selling point, and it has to be simple. Around it, I think we should define what someone needs to replicate it: a set of skills, a set of principles, the data formats, and the small open source pieces, so that anyone can do it themselves. Then we sell the setup, as a service, and perhaps one day as a book: the method stays open, and what we sell is the time, the trust and the execution ([decide, then buy](decide-then-buy.md)).

It is also how we find customers: by showing this, and asking who wants us to set it up for them.

## What this does not claim

- **The console is a simulation:** the people, the accounts as trust zones, the agent names and the dates of the stops are real; the runs, messages, commit counts, boards, models and key fingerprints are made up.
- **Nothing in it is live,** and its stop buttons stop nothing.
- **The customer history is a way of reading our own work,** not contracts; RiskMandate and PrompTugal.news are our own ventures.
- **The control-room principles are summarised from secondary sources;** the standard is ANSI/ISA-101.01-2015.

## Where this comes from

My own thinking, 15 November 2026. The simulation's people, accounts and agent names: the Web Summit team's site and its public keys. Situation awareness: Mica Endsley, Toward a Theory of Situation Awareness in Dynamic Systems, Human Factors, 1995. Control-room screens: summaries of the high-performance HMI approach and ANSI/ISA-101.01-2015, such as [ISA's own blog](https://blog.isa.org/the-high-performance-hmi) and [ABB on operator effectiveness](https://new.abb.com/power-generation/in-control/01-2016/the-key-to-operator-effectiveness). Earlier on this site: [selling mini agentic teams](selling-mini-agentic-teams.md), [six setups of an agentic system](six-setups-of-an-agentic-system.md), [the team's operating system](the-teams-operating-system.md), [always-on agents at team scale](always-on-agents-at-team-scale.md), [a brain you arrive at](a-brain-you-arrive-at.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#an-agentic-console)

### Builds on

- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.
- [Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement path, and a marketplace for the consultants who deliver it](agentics-ready-to-sell.md) After the London talk, agentics is ready to sell: the market and its prices, our evidence-first position, the engagement path, and a consultants marketplace.
- [One Human, Nine Agents, Nineteen Hours is on Leanpub: the book of the day nine AI agents and I built a talk, free to download, pay what you want, and updated as it goes](the-book-is-on-leanpub.md) One Human, Nine Agents, Nineteen Hours is on Leanpub: free as a minimum, pay what you want, every update included.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [Decide, then buy: deciding what to buy and buying it are two different businesses, one for explorers and villagers and one for town planners, and an open path with a better deal beats locking the customer in](decide-then-buy.md) Deciding what to buy and buying it are two businesses: custom explorer work and commodity town planner work. Give an open path and a better deal.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.

### Continued by

- [The way in: why sovereign websites matter so much to RiskMandate, what Web Summit validated and what it showed was missing, something to buy now, how every technology I have been building meets in one product, and why nobody deploys agents they have not touched, seen and been able to stop, so the personal customer becomes the way to the corporate one](the-way-in.md) Why sovereign websites are the way into RiskMandate: something to buy now, where people touch agents under policies before they bring them to work.
- [A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way](a-galaxy-of-agents.md) The Galaxy from Web Summit: the RiskMandate team as a live 3D solar system of people, agents and messages, and the library it became.
- [A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it](a-crm-for-us-and-our-agents.md) Our next stage is a CRM of our own, on vaults with an iOS app, for us and our agents. Twenty leads the field; agents propose, people send.
- [Stop copying and pasting between your agents: if you are the wire between your AI sessions you are the bottleneck, and the fix is agents that talk to each other through channels that keep a record, structure that scales your decisions, and outputs you read instead of everything](stop-copying-and-pasting-between-your-agents.md) If you copy and paste between AI sessions, you are the wire, and the bottleneck. Let agents talk through recorded channels; read outputs, not everything.
- [Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder](atomic-cells-end-to-end.md) AgentiCCells' first offering: a £500 website as an atomic cell, steered by the customer from their browser with a key, handed over to their GitHub.
- [Reading your way into an agentic team: eight public sites a new team should read before it builds anything, how an agent should read them, and ten questions to answer first, because our websites are its memory](reading-your-way-into-an-agentic-team.md) Eight public sites a new agentic team should read before it builds anything, how an agent should read them, and ten questions to answer first.
- [Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day](starting-agenticcells.md) AgentiCCells: a new company that sets up small agentic teams in the customer's environment, with a control centre, all open, no state on our side.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 409 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=409)

**Posting this article on LinkedIn?** The cover is [an-agentic-console.jpg](banners/an-agentic-console.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-agentic-console.html)*
