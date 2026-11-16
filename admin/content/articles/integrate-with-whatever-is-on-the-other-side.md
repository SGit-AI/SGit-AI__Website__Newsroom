---
title: Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: Today I showed an MVP of an AgentiCCells cell to an organisation that liked it, said it fits their explorer mode, and then said, fairly: we use Odoo. That is exactly the point. They are already committed to Odoo, their data and workflows already live in it, and many of those workflows are manual and can be improved. So our strategy is to integrate with whatever is on the other side. We do not start by asking a customer to move to our technology. We use what they have, Odoo 12 or Odoo 20, Salesforce, a spreadsheet, and build around it: agents, behaviour policies, signed approvals, a lasting record, better interfaces and prototypes. That is the open source model: leverage what exists, make it better, and when the underlying technology is upgraded, use the new features. It puts the burden of keeping pace on the underlying technology. Then one of two things happens. Most likely, their system gets better, ships what we built, and we retire our code, which means less to maintain. Or what we built becomes the better place, and the data and work move to it over time, until the old system is no longer needed, the way some web application firewalls once sat in front of the existing firewalls because they understood HTTP. You do not start with replacement. And because we build only on commodity parts, no database of our own, no servers, either way we carry very little code.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: strategy, integration, open-source, odoo, agenticcells, wardley-maps, positioning, article
status: published
---

!shot iwt-path.webp | images/ | Integrate, build around it, and let time decide: their system gets better, or ours becomes the better place. | concept

## In short {#in-short}

- **Today's MVP met the real world:** the organisation liked it, and said they use Odoo. That is the point.
- **We integrate with whatever is on the other side:** Odoo 12 or 20, Salesforce, a spreadsheet.
- **We build around it:** agents, policies, a lasting record, better interfaces and prototypes, starting with the manual workflows.
- **The open source model:** leverage what exists, make it better, use the upgrades when they come.
- **Then one of two things:** their system gets better and we retire our code, or ours becomes the better place.
- **Only commodity parts underneath,** so either way we carry very little code.

## What happened today {#today}

Today I showed an MVP of an [AgentiCCells](/articles/the-intersection.html) cell to an organisation I am working with. They liked it, and said it fits what they call their explorer mode, which is exactly where it should sit ([explorer coding](/articles/explorer-coding.html)). And then they said, fairly: we use Odoo.

That is not an objection. It is the point. They are already committed to Odoo. Their data is in it, their workflows are in it, and many of those workflows are still manual and can be improved. The worst thing we could do is ask them to move. The best thing we can do is go to where they already are.

## Integrate with whatever is on the other side {#integrate}

That is the strategy, and it applies far beyond Odoo. We integrate with whatever the customer has. If it is Odoo 20, we use its agents and its MCP server. If it is Odoo 15, we use its API, which every version since at least 12 has; in this session an agent brought up Odoo 12, 15, 18 and 19 and ran the same workflow on all four, each from nothing to customised in under a minute ([Odoo and our stack](/articles/odoo-and-our-stack.html)). If it is Salesforce, a spreadsheet or a shared drive, the same idea holds. We can even integrate when they do not have a system for something yet: then the vault and the agents are the system.

So customers do not have to wait to be upgraded to use the future. We bring agents, behaviour policies, signed approvals, a lasting record and better interfaces to what they run now.

## Build around it {#around}

Building around a system means leaving its core alone and adding what it does not do well yet. With agents, that is a lot: the work between people and systems, the record of who did what, the policies that say what an agent may change, and interfaces and prototypes that fit a team better than a general-purpose screen. Odoo, for example, is a strong platform to prototype on: we can build a better interface or an MVP on top of it and leave the customer's records where they are.

Starting with the manual workflows matters. They are where the value is most visible, and where the risk is lowest: an agent that drafts what a person used to type, under a policy, with the person still approving.

## The open source model {#open-source}

This is how open source has always worked. You leverage the most of what exists today, you make it better, and when what exists moves to the next level, you take advantage of it. The burden of keeping pace sits with the underlying technology, not with you.

I do this myself. I build on top of Claude, and I have not replaced Claude, because Claude is still the best at what it does and has excellent workflows of its own. There is no reason to rebuild that. I build what it does not do, and when it gets better, my work gets better for free ([open source, so you keep it](/articles/open-source-so-you-keep-it.html)).

## Two ways it ends {#ends}

Over time, one of two things happens.

**Their system gets better.** This is the most likely. Odoo, Salesforce or whatever is underneath ships what we built: agents, approvals, a better screen. Then we use theirs, and retire our code. That is a good outcome: we have less to maintain, and the customer has the same capability from the vendor they already pay.

**Ours becomes the better place.** Sometimes what we build around a system becomes so useful that the data and the work move to it, and the old system holds less and less, until it is no longer needed. If a customer has Salesforce, we integrate with it; over time, a CRM built from their vaults and agents may need less and less from it. There is a path where you replace the underlying technology, but you never start there.

There is an old pattern for this. Some web application firewalls were sold by saying: do not replace your firewalls, put us in front of them, because we understand HTTP and they do not. Some of them later took over; others never needed to. Which way it went depended on what was best for the customer, and that is the right test.

## Only commodity parts underneath {#commodity}

The reason this works for us is how we build. We do not run databases of our own, or servers we have to maintain. We build on commodity parts: vaults, keys, static sites, CI, a model ([no tech stack to maintain](/articles/no-tech-stack-to-maintain.html), [the minimum code below](/articles/the-minimum-code-below.html)). That is the whole idea of removing moving parts and using only commoditised pieces, and it is what makes making a website a commit ([the site factory works](/articles/the-site-factory-works.html)).

So whichever way it goes, we carry very little code of our own. When the system underneath improves, we delete code. When ours wins, there is not much to scale.

## What this does not claim {#limits}

- **The organisation from today is not named,** and the MVP is not linked, until they have reviewed it.
- **The Odoo versions were tested in this session** with Community images and an example partner, not on a customer's data.
- **"Most likely" is my judgement,** from how platforms usually evolve; it is not measured.
- **The firewall story is a pattern,** told from memory, not a claim about any one vendor.

## Where this comes from {#sources}

A demo and conversation today, 16 November 2026, and my own thinking. Earlier on this site: [Odoo and our stack](/articles/odoo-and-our-stack.html), [the intersection](/articles/the-intersection.html), [the site factory works](/articles/the-site-factory-works.html), [explorer coding](/articles/explorer-coding.html), [open source, so you keep it](/articles/open-source-so-you-keep-it.html), [no tech stack to maintain](/articles/no-tech-stack-to-maintain.html), [the minimum code below](/articles/the-minimum-code-below.html).
