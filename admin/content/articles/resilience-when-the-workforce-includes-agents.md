---
title: Resilience when the workforce includes agents: what Synergy Six Degrees rates with OCRR, recovers with NeuShield and protects with Actifile, and where RiskMandate, sgit and SHarness meet it
date: 2026-11-04
author: Dinis Cruz
author_url: about/index.html
summary: Someone I know who runs Synergy Six Degrees, a London analyst firm in cyber security and data protection, shared a new assessment with me and asked what I thought. It is called OCRR, the Operational Cyber Resilience Rating, and I like its premise: recovery is not only an IT question, so it rates an organisation across four disciplines at once, operational, data, financial and people, in one executive conversation. It starts with a free five-page summary built from industry defaults, refines it with a guided assessment of about 500 fields that takes under two hours of the client's time, and then appraises proposed changes before money is spent. It is consultant-delivered, deploys nothing, and does not use AI. Beside it the firm distributes two products: NeuShield, whose Mirror Shielding keeps the original file intact so ransomware damage can be reverted without a backup, and Actifile, which finds sensitive data, encrypts it and puts a money figure on the exposure. The intersection with my work is the part of the workforce that OCRR's people discipline does not yet count: agents. RiskMandate's behaviour policies say what each agent is for and what it can reach; SHarness holds an agent's processes to a policy the kernel enforces; and sgit keeps data encrypted, immutable and recoverable. Together they could give a resilience rating the agent rows it is missing.
version: v0.14.61
license: https://creativecommons.org/licenses/by/4.0/
tags: resilience, ocrr, ransomware, data-protection, riskmandate, sgit, sharness, agents, insurance, article
status: published
---

!shot rw-layers.webp | images/ | Five questions about resilience, and where each piece answers one: rate, mandate, contain, recover, protect. | architecture

## In short {#in-short}

- **Synergy Six Degrees** is a London analyst firm in cyber security and data protection, with three lines of work: analyst research, go-to-market consultancy, and distribution of NeuShield and Actifile.
- **OCRR rates resilience across four disciplines at once:** operational, data, financial and people.
- **It starts free and grows:** a five-page summary from industry defaults, then a guided assessment, then an appraisal of proposed changes.
- **It is deliberately simple to adopt:** consultant-delivered, nothing to install, no AI.
- **NeuShield recovers; Actifile protects and prices.** One keeps the original file, the other finds and encrypts sensitive data and puts a money figure on it.
- **The intersection is agents.** They are now part of how work gets done, and a resilience rating needs rows for them: what each is for, what it can reach, what contains it, and what it costs.
- **RiskMandate, SHarness and sgit** supply those rows: the mandate, the containment, and data that stays recoverable.

## What Synergy Six Degrees does {#what}

Synergy Six Degrees describes itself as "a specialist analyst firm in the cyber security and data protection sector", based in London. Its site lists three kinds of work:

- **Analyst services:** research, adoption reviews and data analysis, for vendors, for the organisations buying from them, and for investors.
- **Go-to-market consultancy** for security vendors: planning, marketing and positioning, with the objective, in its own words, "to achieve the most appropriate and fastest GTM engagements".
- **Distribution:** it is an "Authorised distributor of NeuShield and Actifile", two data protection products, positioned around resilience outcomes.

And now a fourth piece, which is the one I was asked about: an assessment of its own.

## OCRR: one rating, four disciplines {#ocrr}

OCRR stands for Operational Cyber Resilience Rating. Its premise is the part I like most. When an incident hits, recovery is not only an IT question. Can the services recover? Will the data that comes back actually support them? Can the business afford the disruption? What will the people need? Those questions are usually answered by different teams, in different documents, and OCRR's aim is to bring them "into one executive conversation".

So it rates four disciplines, each with its own question:

- **Operational:** "Can services recover?"
- **Data:** "Will recovery support usable services?"
- **Financial:** "Can the business sustain disruption?"
- **People:** "What will your workforce need?"

The output is an overall rating, the four discipline ratings behind it, financial context "under stated recovery assumptions", and improvement priorities. It does not predict a particular attack, and it says plainly that it "does not itself establish technical control effectiveness": it examines recovery capability and assumptions, against agreed disruption scenarios.

It comes in three stages:

1. **Industry Defaults,** the required first step: a no-cost, five-page executive summary within two days, built from the defaults for the organisation's industry and size. It does not look at the actual environment, and says so.
2. **Guided:** the defaults refined with the organisation's own information, across eight domains and about 500 fields, for less than two hours of the client's time, delivered in seven to fourteen days.
3. **Elevated TTP Options:** proposed changes to policy, process and technology appraised against the assessed position, before resources are committed.

Two design choices stand out. It is consultant-delivered, with "No software, agents or infrastructure to deploy". And the assessment page states "No use of AI/LLM Applications". I think both are right for this buyer: a board will start a conversation that costs nothing and installs nothing.

## NeuShield and Actifile: recover, and protect {#products}

The two products the firm distributes sit at either end of an incident.

**NeuShield Data Sentinel,** from NeuShield in Fremont, California, is built on what it calls Mirror Shielding. Its 2018 announcement describes it as "a protective shield between system files and applications": "If malicious code makes any modifications to a file, the original copy stays intact", so damaged files can be reverted without needing a backup. Later releases added protection against data being taken out of SQL databases. These are the vendor's own descriptions.

**Actifile,** from an Israeli company listed in company directories as based in Herzliya, works before the incident. As the firm's page describes it, it will "locate and secure sensitive data", encrypt it, and "calculate potential financial penalties and liabilities", which is what OCRR's financial discipline needs as an input.

So the firm has a rating at the top, and products under two of its disciplines. That is a sensible shape.

## Where my work meets it: the agents {#intersection}

Here is where it gets interesting for me. Look at OCRR's people discipline: "What will your workforce need?" In many organisations, part of the work is now done by agents. They triage tickets, draft replies, move data, run scheduled jobs. They are a new kind of insider: they have access, they act at volume, and, as I said in a recent talk, the difference is that the agent does not stop. A resilience rating that counts the people and not the agents is missing rows, and those rows are exactly what my work produces.

**1. The mandate: RiskMandate.** An [Agent Behaviour Policy](/articles/what-can-your-agent-reach.html) writes down, for one agent, what it is for, what it can actually reach, the gap between the two, and what stands in the way of each capability. That is resilience data. It answers questions OCRR's guided stage could ask: which services depend on agents, which agents can touch the data that recovery depends on, and which of them can be stopped, by whom. Who owns that stop is [a question I have written about](/articles/who-owns-the-stop-button.html), and it belongs in an operational rating.

**2. The money: agents have a cost line.** OCRR puts financial context on recovery. Agents add two lines to it. One is the run cost: [the cost of your agents](/articles/the-cost-of-your-agents.html) shows how a behaviour policy tells waste from work in a token bill. The other is the risk cost: in [insuring agents](/articles/insuring-agents-the-whole-story.html) I argued that a behaviour policy can be read as an insurance policy, priced row by row, with each enforced control lowering that row's premium. A rating that already speaks in money is the natural place for both.

**3. Containment: SHarness.** NeuShield answers "can we recover the file?". The question before it is "could the process have changed it?". [SHarness](/articles/introducing-sharness.html) holds every process an agent starts to a Process Behaviour Policy, what it may read, write, run and connect to, enforced by the Linux kernel, so a tricked agent cannot widen it. An agent that has been steered into behaving like ransomware, writing over files it should not touch, is refused before NeuShield is needed. The kernel locks run today; the launcher that binds a whole agent is still a design.

**4. Recovery and data: sgit.** Mirror Shielding and [an sgit vault](/articles/how-a-vault-works.html) share an instinct I like: never overwrite the original. In a vault every object is immutable and named by the hash of its own ciphertext, so a change is a new object, and the history keeps every earlier version. Everything is encrypted on the client before it reaches the server, so a server that is fully compromised leaks nothing readable. NeuShield does this for the files on a machine; sgit does it for data that moves between people, agents and devices. Actifile and sgit share the other instinct: encrypt the data itself, not only the place it sits.

**5. Delivery: the assessment as a vault.** OCRR keeps its process simple and deploys nothing. Its results could travel the same way: the executive summary, the ratings and the evidence behind them in an encrypted vault, readable by the board with a read key, kept by the client, with every revision of the rating in its history. That is how we already deliver [research](/articles/research-delivered-as-a-vault.html), and it fits a product that promises not to install anything.

## A layered picture {#layers}

Put together, the pieces answer five different questions, and none of them answers all five:

- **How resilient are we?** OCRR rates it, across operations, data, finances and people.
- **What is each agent for?** RiskMandate writes it down, as a behaviour policy.
- **What can an agent's process actually do?** SHarness holds it to its policy, in the kernel.
- **Can we get it back?** NeuShield for the files on a machine; sgit's history for data in vaults.
- **Is the data itself protected?** Actifile, and sgit's client-side encryption.

What I would explore with the firm is small and concrete: whether agents could be an option in OCRR's elevated stage, appraised the way it appraises any proposed change, with a behaviour policy per agent as the input. That is a proposal, not something either of us has built.

## What this does not claim {#limits}

- **OCRR's scale and scoring method are not published;** the ratings on its pages are marked illustrative. I have not run an assessment.
- **NeuShield's and Actifile's descriptions are their vendors' and the distributor's;** I have not tested either product.
- **The intersection is my reading,** not a partnership or an agreed integration.
- **The firm's site is mid-redesign;** what is quoted here was read on 4 November 2026 and may change.
- **SHarness's launcher for a whole agent is still a design;** its kernel locks run today.

## Where this comes from {#sources}

A conversation of 4 November 2026 with the person who runs the firm, who asked what I thought of OCRR, and my own reading of the site. Synergy Six Degrees: [home](https://www.synergysixd.com/), [OCRR](https://www.synergysixd.com/ocrr), [the OCRR assessment](https://www.synergysixd.com/ocrr-assessment-redesign-draft), [services](https://www.synergysixd.com/our-services), [NeuShield Data Sentinel](https://www.synergysixd.com/neushield-data-sentinel), [Actifile](https://www.synergysixd.com/actifile-data-security-platform). [NeuShield's Mirror Shielding announcement, 2018](https://www.prweb.com/releases/2018/06/prweb15596796.htm). On this site: [what can your agent reach](/articles/what-can-your-agent-reach.html), [the cost of your agents](/articles/the-cost-of-your-agents.html), [insuring agents](/articles/insuring-agents-the-whole-story.html), [introducing SHarness](/articles/introducing-sharness.html), [how a vault works](/articles/how-a-vault-works.html). All read 4 November 2026.
