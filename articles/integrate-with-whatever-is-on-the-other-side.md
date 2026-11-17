# Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place, sgit.ai

> Today I showed an MVP of an AgentiCCells cell to an organisation that liked it, said it fits their explorer mode, and then said, fairly: we use Odoo. That is exactly the point. They are already committed to Odoo, their data and workflows already live in it, and many of those workflows are manual and can be improved. So our strategy is to integrate with whatever is on the other side. We do not start by asking a customer to move to our technology. We use what they have, Odoo 12 or Odoo 20, Salesforce, a spreadsheet, and build around it: agents, behaviour policies, signed approvals, a lasting record, better interfaces and prototypes. That is the open source model: leverage what exists, make it better, and when the underlying technology is upgraded, use the new features. It puts the burden of keeping pace on the underlying technology. Then one of two things happens. Most likely, their system gets better, ships what we built, and we retire our code, which means less to maintain. Or what we built becomes the better place, and the data and work move to it over time, until the old system is no longer needed, the way some web application firewalls once sat in front of the existing firewalls because they understood HTTP. You do not start with replacement. And because we build only on commodity parts, no database of our own, no servers, either way we carry very little code.

*Source: <https://newsroom.sgit.ai/articles/integrate-with-whatever-is-on-the-other-side.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place

# Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/integrate-with-whatever-is-on-the-other-side.md) · [newsroom v0.14.120](https://newsroom.sgit.ai/admin/versions.html) · strategyintegrationopen-sourceodooagenticcellswardley-mapspositioningarticle

***Abstract:** Today I showed an MVP of an AgentiCCells cell to an organisation that liked it, said it fits their explorer mode, and then said, fairly: we use Odoo. That is exactly the point. They are already committed to Odoo, their data and workflows already live in it, and many of those workflows are manual and can be improved. So our strategy is to integrate with whatever is on the other side. We do not start by asking a customer to move to our technology. We use what they have, Odoo 12 or Odoo 20, Salesforce, a spreadsheet, and build around it: agents, behaviour policies, signed approvals, a lasting record, better interfaces and prototypes. That is the open source model: leverage what exists, make it better, and when the underlying technology is upgraded, use the new features. It puts the burden of keeping pace on the underlying technology. Then one of two things happens. Most likely, their system gets better, ships what we built, and we retire our code, which means less to maintain. Or what we built becomes the better place, and the data and work move to it over time, until the old system is no longer needed, the way some web application firewalls once sat in front of the existing firewalls because they understood HTTP. You do not start with replacement. And because we build only on commodity parts, no database of our own, no servers, either way we carry very little code.*

Integrate, build around it, and let time decide: their system gets better, or ours becomes the better place.

## In short

- **Today's MVP met the real world:** the organisation liked it, and said they use Odoo. That is the point.
- **We integrate with whatever is on the other side:** Odoo 12 or 20, Salesforce, a spreadsheet.
- **We build around it:** agents, policies, a lasting record, better interfaces and prototypes, starting with the manual workflows.
- **The open source model:** leverage what exists, make it better, use the upgrades when they come.
- **Then one of two things:** their system gets better and we retire our code, or ours becomes the better place.
- **Only commodity parts underneath,** so either way we carry very little code.

## What happened today

Today I showed an MVP of an [AgentiCCells](the-intersection.md) cell to an organisation I am working with. They liked it, and said it fits what they call their explorer mode, which is exactly where it should sit ([explorer coding](explorer-coding.md)). And then they said, fairly: we use Odoo.

That is not an objection. It is the point. They are already committed to Odoo. Their data is in it, their workflows are in it, and many of those workflows are still manual and can be improved. The worst thing we could do is ask them to move. The best thing we can do is go to where they already are.

## Integrate with whatever is on the other side

That is the strategy, and it applies far beyond Odoo. We integrate with whatever the customer has. If it is Odoo 20, we use its agents and its MCP server. If it is Odoo 15, we use its API, which every version since at least 12 has; in this session an agent brought up Odoo 12, 15, 18 and 19 and ran the same workflow on all four, each from nothing to customised in under a minute ([Odoo and our stack](odoo-and-our-stack.md)). If it is Salesforce, a spreadsheet or a shared drive, the same idea holds. We can even integrate when they do not have a system for something yet: then the vault and the agents are the system.

So customers do not have to wait to be upgraded to use the future. We bring agents, behaviour policies, signed approvals, a lasting record and better interfaces to what they run now.

## Build around it

Building around a system means leaving its core alone and adding what it does not do well yet. With agents, that is a lot: the work between people and systems, the record of who did what, the policies that say what an agent may change, and interfaces and prototypes that fit a team better than a general-purpose screen. Odoo, for example, is a strong platform to prototype on: we can build a better interface or an MVP on top of it and leave the customer's records where they are.

Starting with the manual workflows matters. They are where the value is most visible, and where the risk is lowest: an agent that drafts what a person used to type, under a policy, with the person still approving.

## The open source model

This is how open source has always worked. You leverage the most of what exists today, you make it better, and when what exists moves to the next level, you take advantage of it. The burden of keeping pace sits with the underlying technology, not with you.

I do this myself. I build on top of Claude, and I have not replaced Claude, because Claude is still the best at what it does and has excellent workflows of its own. There is no reason to rebuild that. I build what it does not do, and when it gets better, my work gets better for free ([open source, so you keep it](open-source-so-you-keep-it.md)).

## Two ways it ends

Over time, one of two things happens.

**Their system gets better.** This is the most likely. Odoo, Salesforce or whatever is underneath ships what we built: agents, approvals, a better screen. Then we use theirs, and retire our code. That is a good outcome: we have less to maintain, and the customer has the same capability from the vendor they already pay.

**Ours becomes the better place.** Sometimes what we build around a system becomes so useful that the data and the work move to it, and the old system holds less and less, until it is no longer needed. If a customer has Salesforce, we integrate with it; over time, a CRM built from their vaults and agents may need less and less from it. There is a path where you replace the underlying technology, but you never start there.

There is an old pattern for this. Some web application firewalls were sold by saying: do not replace your firewalls, put us in front of them, because we understand HTTP and they do not. Some of them later took over; others never needed to. Which way it went depended on what was best for the customer, and that is the right test.

## Only commodity parts underneath

The reason this works for us is how we build. We do not run databases of our own, or servers we have to maintain. We build on commodity parts: vaults, keys, static sites, CI, a model ([no tech stack to maintain](no-tech-stack-to-maintain.md), [the minimum code below](the-minimum-code-below.md)). That is the whole idea of removing moving parts and using only commoditised pieces, and it is what makes making a website a commit ([the site factory works](the-site-factory-works.md)).

So whichever way it goes, we carry very little code of our own. When the system underneath improves, we delete code. When ours wins, there is not much to scale.

## What this does not claim

- **The organisation from today is not named,** and the MVP is not linked, until they have reviewed it.
- **The Odoo versions were tested in this session** with Community images and an example partner, not on a customer's data.
- **"Most likely" is my judgement,** from how platforms usually evolve; it is not measured.
- **The firewall story is a pattern,** told from memory, not a claim about any one vendor.

## Where this comes from

A demo and conversation today, 16 November 2026, and my own thinking. Earlier on this site: [Odoo and our stack](odoo-and-our-stack.md), [the intersection](the-intersection.md), [the site factory works](the-site-factory-works.md), [explorer coding](explorer-coding.md), [open source, so you keep it](open-source-so-you-keep-it.md), [no tech stack to maintain](no-tech-stack-to-maintain.md), [the minimum code below](the-minimum-code-below.md).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#integrate-with-whatever-is-on-the-other-side)

### Builds on

- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [Odoo's agents can now write to the system of record: how our stack fits around Odoo, from version 12 to 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, an ephemeral proof of concept that went from nothing to customised in under a minute on four versions, and why we use whatever version is on the other side](odoo-and-our-stack.md) Odoo's agents can write to the system of record. Our stack fits every Odoo from 12 to 20: a proof of concept ran on four versions in under a minute each.
- [Open source what you build, even while you are employed: nobody copies it, and it is the only way you get to keep using it](open-source-so-you-keep-it.md) Nobody copies your open source ideas; the real advantage is that you keep using your own work from job to job, and a rough public history protects you.
- [No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitive rented as a commodity or run in the user's browser over encrypted vaults](no-tech-stack-to-maintain.md) Not no backend: no tech stack of your own. Only HTML, CSS and JavaScript; every other primitive rented or run in the browser over vaults.
- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.

### Continued by

- [Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells](any-data-with-any-data.md) Why we can now connect any data source with any other: nine steps, owners keep control, a person approves every key, sold as cells.
- [Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team](fork-it.md) Forking as the way people adopt our cells: fork a template, point Claude at it, and it is yours. Five ways, fork-ready repositories, and a hub.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [Our workflow on Odoo 20, built and measured: a bills agent with no Odoo credential, a policy check that allowed two proposals and stopped three, a signed approval, a narrow broker, a grant measured from Odoo itself by a new module, and what Odoo's default user role quietly allows](our-workflow-on-odoo-20.md) Our workflow on Odoo 20, built in 98 seconds: a keyless agent, a policy check, a signed approval, a narrow broker and a grant measured from Odoo.
- [A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it](a-crm-for-us-and-our-agents.md) Our next stage is a CRM of our own, on vaults with an iOS app, for us and our agents. Twenty leads the field; agents propose, people send.
- [Odoo's agents can now write to the system of record: how our stack fits around Odoo, from version 12 to 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, an ephemeral proof of concept that went from nothing to customised in under a minute on four versions, and why we use whatever version is on the other side](odoo-and-our-stack.md) Odoo's agents can write to the system of record. Our stack fits every Odoo from 12 to 20: a proof of concept ran on four versions in under a minute each.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 429 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=429)

**Posting this article on LinkedIn?** The cover is [integrate-with-whatever-is-on-the-other-side.jpg](banners/integrate-with-whatever-is-on-the-other-side.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/integrate-with-whatever-is-on-the-other-side.html)*
