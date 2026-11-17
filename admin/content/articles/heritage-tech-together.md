---
title: HeritageTech, together: how our open-source stack could plug into UAlgTec Heritage, the University of the Algarve's new European centre of excellence for heritage science and technology, mapped from the dig to the museum, with encrypted evidence vaults per site, signed finds, graphs of every excavation, agents with written policies, and what I would write in its "start a conversation" form
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Today I saw a screen with an invitation: "Help build what comes next. Bring a problem. Bring a technology. Bring an idea." It is from UAlgTec Heritage, UTH, the University of the Algarve's new centre of excellence, coordinated through its ICArEHB research centre and led by João Cascalheira. It won about 31.5 million euros, 15 million of it from Horizon Europe's Teaming for Excellence, the first such award in archaeology in Europe, with Kiel University, ERA Arqueologia and Zartis as partners, and it plans to start in January 2027. Its aim is a European HeritageTech sector, like FinTech or HealthTech, built on an AI-first platform for archaeological heritage. That is very close to what we have been building. An AI-first platform for heritage needs what every AI-first platform needs: evidence that cannot be quietly changed, records signed by the person who made them, data from many teams that does not collide, agents that only do what they are allowed to, and claims a reader can trace back to the find. So here is the mapping, stage by stage, from the field to the archive to the public; what UTH brings and what we bring; a first pilot on one site; and the answer I would give in its form.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: heritage, archaeology, algarve, research, provenance, vaults, graphs, partnerships, article
status: published
---

!shot uth-map.webp | images/ | From the dig to the public: what an AI-first heritage platform needs at each stage, and the open piece we already have. | diagram

## In short {#in-short}

- **UTH is a new European centre of excellence** for heritage science and technology, at the University of the Algarve.
- **Its aim is a HeritageTech sector,** on an AI-first platform for archaeological heritage, from January 2027.
- **An AI-first heritage platform needs proof:** evidence, signatures, provenance, agents with limits.
- **That is what our open-source stack does,** already running in our own newsrooms.
- **Six places it plugs in,** from the field record to the public story.
- **A first pilot:** one site, one season's records, in the open.
- **The first step is theirs to invite and ours to take:** a short answer in their form.

## UAlgTec Heritage {#uth}

UAlgTec Heritage, UTH, is the University of the Algarve's new centre of excellence, coordinated through ICArEHB, its Interdisciplinary Center for Archaeology and the Evolution of Human Behaviour, with João Cascalheira as director and project coordinator. Its funding is about 31.5 million euros: 15 million from the European Commission through Horizon Europe's Teaming for Excellence programme, and 16.5 million from national sources, including CCDR Algarve, Património Cultural and FCT. It is reported as the first Teaming for Excellence award in archaeology in Europe, and the first for an Algarve institution. The consortium brings together the University of the Algarve, Kiel University in Germany, ERA Arqueologia and Zartis.

The goal, in its own framing, is a European HeritageTech sector, the way FinTech and HealthTech became sectors, built on an AI-first platform for archaeological heritage. It is expected to start work in January 2027, and it is already asking: its form, "Let's build HeritageTech together", invites companies, researchers, entrepreneurs and organisations "with challenges to solve, technologies to explore or ideas worth developing together", as "an informal first contact, with no commitment."

## Why this fits {#fit}

Heritage is evidence. A find matters because of where it was, what was next to it, who recorded it and when. A report matters because each claim can be traced back to a context, a sample, a photograph. Put AI in the middle of that, agents that read field notes, classify finds, draft reports and answer the public, and the question becomes the one we have been working on all year: when an AI can produce five versions of a site report in a minute, how does anyone know which one to trust, and what it rests on?

Our answer, in our own newsrooms, has been to make every piece carry its own proof: encrypted, versioned vaults ([how a vault works](/articles/how-a-vault-works.html)), a key for every person and signatures on what they publish ([signed by the source](/articles/signed-by-the-source.html)), behaviour policies for agents ([where assist becomes execute](/articles/where-assist-becomes-execute.html)), and graphs that tie claims to their sources. None of it was built for archaeology. All of it is what an AI-first heritage platform will need underneath.

## Six places it plugs in {#map}

1. **An evidence vault per site.** Field notes, photographs, drawings, scans, sample records and permits, in an encrypted vault the project owns, versioned so nothing is quietly overwritten, and opened by a key, never by the host. Sensitive locations, of unexcavated sites or of finds at risk of looting, stay out of the public copy by design, not by policy alone.
2. **Signed field records.** Each archaeologist has a key; each context sheet, find record and photograph is signed by the person who made it, at the time they made it. A QR code on a find bag or a site marker points to its signed record ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).
3. **Many teams, no collisions.** A dig has many hands: university teams, a commercial unit like ERA, specialists, students, volunteers. Append lanes let each write into a project without being able to read or change the rest ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).
4. **A graph of each excavation.** Contexts, finds, samples, dates and interpretations as a graph, each claim linked to its evidence, the way this newsroom keeps a graph for every article ([knowledge graphs in the era of LLMs](/articles/knowledge-graphs-for-kgell.html)). An interpretation can then show what it rests on, and what changes if a date is revised.
5. **Agents with written limits.** The AI-first platform's agents, classifying, transcribing, drafting, answering visitors, each with a written behaviour policy: what it may read, what it may never publish, which claims need a person. And agents that check other agents, against named standards ([agents rating agents](/articles/agents-rating-agents.html)).
6. **The public story, with its proof.** Every site and project with its own small site, made by our site factory from the vault ([the site factory works](/articles/the-site-factory-works.html)), and local news about heritage filed where it happens, the way PrompTugal.news files it ([local trust, certified upwards](/articles/local-trust-certified-upwards.html)). A visitor, a journalist or a funder can follow a claim back to the find.

Two smaller pieces fit too: voice notes on site, transcribed on the phone and offline, where there is often no signal ([build on VoiceDebrief](/articles/build-on-voicedebrief.html)); and the whole stack self-hosted in an EU region, so a European project keeps its data in Europe ([deploy sgit from CI](/articles/deploy-sgit-from-ci.html)).

## What each side brings {#bring}

- **UTH:** the science, the sites, the collections, the funding to build a sector, and a consortium that spans a university, a German research university, a commercial archaeology company and a technology company.
- **Us:** an open-source stack for evidence, signatures, provenance and agent policies, running every day in our own newsrooms, and a team that builds with around 250 agents and has shipped this way all year.
- **Both:** a case that matters beyond heritage: that an AI-first platform can make expert knowledge more trustworthy, not less, if the proof travels with every claim.

## A first pilot {#pilot}

!shot uth-pilot.webp | images/ | A first pilot: one site, one season's records, keys, a vault, signed records, a graph, a public page. | process

Small, real and in the open. One site or one collection the centre chooses, and one season's records, worked over twelve weeks:

- **Weeks 1 to 3:** keys for the team, an evidence vault for the site, and the existing records moved in, with their history.
- **Weeks 4 to 6:** new records signed as they are made, a QR code on each find bag, an append lane for each team.
- **Weeks 7 to 9:** a graph of the site built by agents from the records, every claim linked to its evidence, checked by a person.
- **Weeks 10 to 12:** a public page for the site, with a provenance view, and a review: time per record, errors caught, what the team and visitors make of it.

Everything we add is open source, so whatever the pilot shows belongs to the centre, and to the HeritageTech sector it is trying to start.

## What I would write in the form {#form}

!shot uth-form.webp | images/ | Their form asks what you want to explore; our answer: a technology that could be applied to heritage, and a pilot. | concept

The form asks one real question: what would you like to explore with UTH? Of its six options, ours is "I have a technology or expertise that could be applied to heritage", with a research and innovation collaboration as the natural next step. Under "tell us a little more", I would write something like this:

> We build an open-source stack for trustworthy AI: encrypted, versioned evidence vaults, a key and a signature for every person, graphs that link every claim to its evidence, and written policies for what each AI agent may do. We use it every day in our own newsrooms. An AI-first heritage platform needs exactly this underneath: field records that cannot be quietly changed, finds traceable to who recorded them, and agents with limits. We would like to propose a small, open pilot on one site or collection, and to see where it fits in UTH's plans.

I will send it myself; this article is the longer version.

## What this does not claim {#limits}

- **This is a proposal,** written on the day I saw the invitation; nothing is agreed, and we have not spoken to UTH yet.
- **UTH's figures and plans are as reported** by the University of the Algarve, FCT and regional press, and may change before it starts.
- **None of our stack has been used on an excavation;** the pilot is how to find out.

## Where this comes from {#sources}

UTH's form, [Let's build HeritageTech together](https://tally.so/r/PR9lOV), and its invitation screen, both seen on 17 November 2026. On the centre: [FCT](https://www.fct.pt/en/portugal-assegura-81-milhoes-de-euros-de-financiamento-europeu-para-criar-6-centros-de-investigacao/), [barlavento](https://www.barlavento.pt/ualg-capta-315-milhoes-centro-europeu-inovacao-arqueologica/), [Postal](https://postal.pt/europedirectalgarve/financiamento-historico-coloca-algarve-na-linha-da-frente-da-inovacao-arqueologica/), [Algarve Primeiro](https://www.algarveprimeiro.com/d/financiamento-historico-cria-polo-europeu-de-excelencia-em-patrimonio-no-algarve/66267-1) and [Algarve Notícias](https://www.algarvenoticias.com/pt-pt/noticias/ualg-conquista-primeiro-teaming-excellence-com-financiamento-de-315-milh%C3%B5es-de-euros), all read on 17 November 2026. Earlier on this site: [how a vault works](/articles/how-a-vault-works.html), [signed by the source](/articles/signed-by-the-source.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [knowledge graphs in the era of LLMs](/articles/knowledge-graphs-for-kgell.html), [agents rating agents](/articles/agents-rating-agents.html), [the site factory works](/articles/the-site-factory-works.html), [local trust, certified upwards](/articles/local-trust-certified-upwards.html), [build on VoiceDebrief](/articles/build-on-voicedebrief.html), [deploy sgit from CI](/articles/deploy-sgit-from-ci.html).
