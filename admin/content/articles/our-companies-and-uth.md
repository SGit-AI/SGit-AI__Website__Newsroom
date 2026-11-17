---
title: Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Earlier today I mapped how our open-source stack could plug into UAlgTec Heritage, UTH, the University of the Algarve's new European centre of excellence for heritage science and technology. This is the other half of that map, company by company. UTH's aim is not only a platform: it is a HeritageTech sector, the way FinTech and HealthTech became sectors, and a sector is made of companies. We have spent this year building a set of small companies that each do one thing and together go end to end. SGit and SG/Send keep evidence encrypted and versioned; pki.sgit.ai gives every person and agent a key; SHarness puts a kernel-enforced boundary round every process an agent starts; Agent Behaviour Policies, sold by RiskMandate, say what each agent may do; AgentiCCells sets up small agentic teams and, through its site factory, a website per project; GAMMA-Ray rates agents against named standards; VoiceDebrief turns voice notes into records on the phone; PrompTugal.news files news by place; and this newsroom explains all of it. Here is what each could do for a heritage team, with its website, the layer it sits in, and a first use; and why companies like these are what a sector is made of.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: heritage, archaeology, algarve, strategy, sgit, sharness, abp, riskmandate, agenticcells, promptugal, voicedebrief, partnerships, article
status: published
---

!shot uthc-map.webp | images/ | Our companies and websites, each mapped to a need of an AI-first heritage platform, by layer. | table

## In short {#in-short}

- **UTH wants a HeritageTech sector,** and a sector is made of companies.
- **We have built a set of small companies,** each doing one thing, together end to end.
- **Each maps to a heritage need:** evidence, identity, boundaries, policies, teams, ratings, field notes, the public story.
- **All of them run for real** in our own work, with live websites.
- **The open parts are free to adopt;** the companies sell setup, policies and teams.
- **A model for the sector:** small, specialised companies on a shared, open trust layer.

## Why companies {#why}

In [HeritageTech, together](/articles/heritage-tech-together.html) I mapped our stack onto UTH's plans: an AI-first heritage platform needs evidence that cannot be quietly changed, records signed by the person who made them, data from many teams that does not collide, agents with limits, and claims a reader can follow back to the find.

But UTH's stated goal is bigger than a platform. It wants a European HeritageTech sector, the way FinTech and HealthTech became sectors. Sectors are made of companies, usually small ones, each doing one thing well on top of shared infrastructure. That is exactly how we have built ours this year: separate companies, each with its own website and its own customers, that use each other for real ([the intersection](/articles/the-intersection.html)). So here they are, one by one, with what each could do for heritage.

## The foundations {#foundations}

- **[SGit](https://sgit.ai/)** is git for encrypted vaults: a vault is a unit of work, its data, history and sources, versioned and handed over with a single read key ([how a vault works](/articles/how-a-vault-works.html)). **For heritage:** an evidence vault per site or collection, owned by the project, opened by a key, never by the host; sensitive locations kept out of the public copy.
- **SG/Send** is the server the vaults live on, with append lanes that accept writes and return nothing, and it can be self-hosted ([deploy sgit from CI](/articles/deploy-sgit-from-ci.html)). **For heritage:** each team on a dig writes into the project without reading or changing the rest; a European project runs it in an EU region.
- **[pki.sgit.ai](https://pki.sgit.ai/)** gives every person and every agent a key, made in the browser, and passes keys and sealed links as QR codes ([a key for every person](/articles/a-key-for-every-person.html)). **For heritage:** a signature on every context sheet and find record, and a QR code on every find bag.
- **[SHarness](https://sharness.ai/)** puts a Process Behaviour Policy round every process an AI agent starts, enforced by the Linux kernel ([introducing SHarness](/articles/introducing-sharness.html)). **For heritage:** the platform's agents can only touch the records they are meant to, whatever a prompt says.

## The standard and its seller {#abp}

- **[Agent Behaviour Policies](https://abp.sgit.ai/)** describe, for one agent, what it can reach, what it was asked to do, the gap, and what stands in the way ([where assist becomes execute](/articles/where-assist-becomes-execute.html)). **For heritage:** a written policy for each agent of the AI-first platform, the one that classifies finds, the one that drafts reports, the one that answers visitors, readable by a director, a funder or an ethics board.
- **[RiskMandate](https://riskmandate.ai/)** sells those policies, from a downloadable pack to one corrected for your situation and signed by a professional ([know the reach](/articles/know-the-reach.html)). **For heritage:** the policies for a European-funded platform, reviewed before it goes live, the kind of evidence a Horizon Europe project is asked for.

## Teams and sites {#teams}

- **[AgentiCCells](https://agenticcells.ai/)** sets up small teams of AI agents as fixed-price cells, each agent with a key and a policy ([the cell is the unit](/articles/the-cell-is-the-unit.html)). **For heritage:** an agentic cell per research group or per startup in the centre's programme, set up in days, seen and stoppable.
- **The site factory** at agenticcells.site makes a repository, an address and a website from one commit, in minutes ([the site factory works](/articles/the-site-factory-works.html)), and a person's own vault can feed it ([your own agentic cell](/articles/your-own-agentic-cell.html)). **For heritage:** a site for every excavation, project and researcher, made from the vault, kept up by its owner's own agent.

## Checking and recording {#checking}

- **[GAMMA-Ray](https://gamma-ray.sgit.ai/)** rates agents and companies against named standards, with every rating carrying its evidence ([agents rating agents](/articles/agents-rating-agents.html)). **For heritage:** the platform's agents and partners checked against the heritage and data standards they must follow, with the gaps listed, not hidden.
- **[VoiceDebrief](https://voicedebrief.ai/)** turns a voice note into a transcript and a debrief on the phone, offline, kept in a vault the user owns ([build on VoiceDebrief](/articles/build-on-voicedebrief.html)). **For heritage:** field notes spoken on site, where there is often no signal, recorded and signed the same day.

## The public story {#public}

- **[PrompTugal.news](https://promptugal.news/)** files news where it happens, with an agent for every town in the Algarve, and shows who wrote, checked and signs each piece ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)). **For heritage:** heritage news by place, from every town that has a site, with the proof attached, and local outlets certifying national stories about their patch.
- **This newsroom, newsroom.sgit.ai,** explains every piece of the stack, every release signed. **For heritage:** the public, readable record of how the platform is built, the way this one records ours.
- **Native apps,** built by agents for iPhone, iPad and Android ([native apps by agents](/articles/native-apps-by-agents.html)). **For heritage:** a visitor app for a site or a museum, made from the same vault.

## How they fit together {#together}

!shot uthc-flow.webp | images/ | One find, through our companies: spoken, signed, stored, checked, explained, published. | process

Take one find. An archaeologist speaks a note on site, and VoiceDebrief transcribes it on the phone. They sign the record with their key from pki.sgit.ai, and a QR code goes on the find bag. The record lands in the site's SGit vault through their team's lane on SG/Send. The platform's agents, each under a behaviour policy from RiskMandate and a SHarness boundary, classify it and add it to the site's graph. GAMMA-Ray checks those agents against the standards. And the find reaches the public through the site's own website from the factory, and through PrompTugal.news, with its proof.

## A model for the sector {#model}

What UTH could take from this is not only the tools but the shape: small, specialised companies, each with one job and one website, on a shared, open trust layer that none of them owns. That is how a sector forms around a centre of excellence. The open parts, SGit, SG/Send, pki.sgit.ai, SHarness and the policy standard, are free to adopt; the companies sell setup, policies, teams and checks. A HeritageTech startup in UTH's programme could start on the same layer on its first day.

## What this does not claim {#limits}

- **This is a proposal;** we have not spoken to UTH, and nothing is agreed.
- **None of these companies has worked on heritage yet;** every "for heritage" is a proposed use.
- **"Separate companies" is how I think about them;** their legal structure is not described here.

## Where this comes from {#sources}

Our own sites: [sgit.ai](https://sgit.ai/), [pki.sgit.ai](https://pki.sgit.ai/), [sharness.ai](https://sharness.ai/), [abp.sgit.ai](https://abp.sgit.ai/), [riskmandate.ai](https://riskmandate.ai/), [agenticcells.ai](https://agenticcells.ai/), [gamma-ray.sgit.ai](https://gamma-ray.sgit.ai/), [voicedebrief.ai](https://voicedebrief.ai/) and [promptugal.news](https://promptugal.news/). UTH's form, [Let's build HeritageTech together](https://tally.so/r/PR9lOV), and the reporting in [HeritageTech, together](/articles/heritage-tech-together.html), 17 November 2026. Earlier on this site: [the intersection](/articles/the-intersection.html), [how a vault works](/articles/how-a-vault-works.html), [deploy sgit from CI](/articles/deploy-sgit-from-ci.html), [a key for every person](/articles/a-key-for-every-person.html), [introducing SHarness](/articles/introducing-sharness.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [know the reach](/articles/know-the-reach.html), [the cell is the unit](/articles/the-cell-is-the-unit.html), [the site factory works](/articles/the-site-factory-works.html), [your own agentic cell](/articles/your-own-agentic-cell.html), [agents rating agents](/articles/agents-rating-agents.html), [build on VoiceDebrief](/articles/build-on-voicedebrief.html), [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [native apps by agents](/articles/native-apps-by-agents.html).
