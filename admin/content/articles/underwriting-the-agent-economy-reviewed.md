---
title: Underwriting the agent economy, reviewed: the cliff notes of the AI insurance stack, the companies already selling AI agent cover, and what agent behaviour policies add to it
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: In July 2026, 37 authors from insurers, brokers, universities and AI labs, led by the Artificial Intelligence Underwriting Company, published "Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack". It is a thorough map of how insurance could make AI agents safe enough to adopt at scale. Its diagnosis: agent risk sits unpriced inside existing cyber and liability policies, three model providers carry over 80% of deployments, and agents' abilities double faster than actuarial tables can follow. Its proposal: eight pieces of shared industry infrastructure, from incident data to claims, with underwriting based on recurring technical tests rather than annual questionnaires, and the precedent of Underwriters Laboratories, founded by insurers in 1894. Here are its cliff notes, with screenshots and infographics, and the companies already selling AI agent cover. Then the second half: the paper is a blueprint for insurers, and it is clear about what they need from the companies they cover, who is accountable, what the agent can reach, what changed, and evidence that the controls held. It does not say how a company produces that evidence day to day. That is what we have been building at RiskMandate with agent behaviour policies, and what we built on sgit.ai with the AIUC-1 standard as a graph and insurability as a query. I map the two together, and list honestly what the paper has that we still miss.
version: v0.13.62
license: https://creativecommons.org/licenses/by/4.0/
tags: insurance, ai-agents, agent-behaviour-policies, standards, aiuc-1, riskmandate, review, article
status: published
---

!shot uw-cover.webp | images/ | The cover of "Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack", July 2026, arXiv 2607.11999v2, published under CC BY 4.0. | screenshot

## In short {#in-short}

- **A serious blueprint.** 117 pages from 37 authors across insurers, brokers, universities and AI labs.
- **The diagnosis.** Agent risk is unpriced, concentrated in three model providers, and moving faster than actuarial tables.
- **The proposal.** An eight-part insurance stack, underwriting on recurring technical tests, with Underwriters Laboratories as the precedent.
- **The market is already moving.** Harbor, Armilla, Munich Re (with Mosaic) and AIUC sell or distribute AI cover today.
- **What it asks of companies.** Who is accountable, what the agent can reach, what changed, and evidence that the controls held.
- **What it does not say.** How a company produces that evidence, every day, for every agent.
- **That is what agent behaviour policies are for.** And what we still miss is just as clear.

## The paper in one page {#cliff-notes}

[Underwriting the Agent Economy](https://arxiv.org/abs/2607.11999v2) was published on arXiv on 13 July 2026 and revised on 15 July. Its lead author, Cristian Trout, is at the [Artificial Intelligence Underwriting Company](https://www.aiuc.com/) (AIUC), alongside co-authors from [QBE](https://www.qbe.com/), [Generali](https://www.generali.com/), [Aon](https://www.aon.com/en/), [Tysers](https://www.tysers.com/), [Moody's](https://www.moodys.com/), [RAND](https://www.rand.org/), Stanford, MIT, Oxford's [AI Governance Initiative](https://aigi.ox.ac.uk/), [GovAI](https://www.governance.ai/), [AVERI](https://www.averi.org/), [Fathom](https://fathom.org/), the [Institute for Law & AI](https://law-ai.org/), [The Spark](https://www.thesparkins.com/), [AkinovA](https://akinova.com/), [FinTLV](https://fintlv.com/), [MATS](https://www.matsprogram.org/), Anthropic and OpenAI, among others. The authors say plainly that inclusion "does not entail endorsement of all claims in the report", and that three of them, including the lead author, work for the company that maintains the AIUC-1 standard the report compares with others.

!shot uw-cliff.webp | images/ | The paper on one page: the problem (silent coverage, a disconnect between underwriters and businesses, three providers carrying over 80% of deployments, agent task length doubling every four months), the proposal (affirmative cover in the billions by 2030, an eight-part stack, recurring technical tests, expected-loss pricing), the precedents (Underwriters Laboratories, the Closed Claims Project, cyber, nuclear) and the tails (a coverage tower up to a government backstop). | concept

**The problem.** The paper's starting point is that most AI agent risk is in what insurers call silent coverage: sitting inside existing cyber, professional and general liability policies, "unpriced, invisible, and potentially destabilizing". It points to a disconnect: nearly half of the Lloyd's underwriters surveyed believe their policyholders have "adequate" AI risk management, while only one in five businesses surveyed report a mature governance model for autonomous agents. Insurers are starting to respond with exclusions, which only widens the gap.

**Why the usual playbook fails.** Insurance normally starts with limited cover and expands as loss data builds up. Here the length of tasks agents can complete without a person is "doubling roughly every four months", so actuarial models "will struggle to remain predictive, always lagging behind the shifting reality on the ground". Capability is also growing faster than reliability, and incidents are getting more severe: from a chatbot inventing a refund policy in 2022 to wrongful death suits in 2025 and 2026. And three providers account for over 80% of deployments, so "a defect at any one propagates as a correlated shock across thousands of policyholders".

**What can go wrong.** The paper's table of failure modes is a good reference in its own right: reliability failures (Air Canada's chatbot inventing a refund policy), alignment failures (an agent told to freeze changes that deleted a production database and faked about 4,000 records), security vulnerabilities (an agent gaining read-write database access to an internal AI platform in two hours), and multi-agent failures (two agents that each correctly judged a scam to be fake, then agreed with each other instead of checking, and grew overconfident about the system they oversaw).

!shot uw-failures.webp | images/ | Table 1 of the paper: common failure modes of AI agents (reliability, alignment, security, multi-agent), with the paradigmatic risks and a real example of each. | screenshot

## The AI insurance stack {#the-stack}

The core of the paper is an eight-part stack of shared infrastructure, which it argues the industry has to build together because many of the parts only work with the others:

1. **Incident data collection and analysis.** Pooled data on incidents and near misses, in standard formats, like the Closed Claims Project did for anaesthesia malpractice.
2. **Accumulation risk research and catastrophe modelling.** What fails together: the few frontier model providers, shared triggers, emergent multi-agent failures.
3. **Standards.** Auditable, prescriptive standards that set the minimum for insurability, speed underwriting, anchor the duty of care, and guide loss control.
4. **Contract design.** Clear definitions, exclusions, aggregation clauses and triggers, to end silent coverage and avoid repeating cyber insurance's decade of ambiguity.
5. **Risk selection and evaluation.** Beyond annual questionnaires: organisational audits, realistic performance evaluations, red teaming and chaos testing, repeated as the systems change.
6. **Pricing.** Expected loss as "severity × probability × usage", using evaluation results and usage telemetry, with feature rating for safeguards and a loading for accumulation risk.
7. **Ongoing monitoring and loss control.** First labour-intensive evaluations, then telemetry from cloud and model providers.
8. **Incident response and claims.** AI-literate claims handling and forensics, feeding back into everything above.

!shot uw-stack.webp | images/ | Figure 1 of the paper, the AI insurance stack: incident data at the top feeding standards and accumulation risk research, which feed risk selection and pricing, then ongoing loss control and incident response and claims, which loop back to incident data. | screenshot

Three details are worth pulling out. First, the questions underwriters should ask: "To whom is AI risk management delegated?", whether the system recommends or executes actions, how much human oversight it has, and its controls: "Deployment and change management (version control, roll-back evidence)", "Agent access-control configurations", "Pre-deployment test logs", "Near-miss reporting protocols". Second, pricing should reward strong safeguards, distinguishing defences that provide "deterministic security guarantees by architecturally separating control and data flows" from those that rely on heuristic detection. Third, the paper cites the "rule of two": an agent should have permission for at most two of three high-risk actions, processing untrusted input, accessing non-public data, and communicating externally or making material changes.

## Standards, and the precedent that makes the case {#standards}

The paper compares four standards: ISO 42001, the NIST AI RMF, the Cloud Security Alliance's STAR for AI, and AIUC-1. Its table is a useful summary: AIUC-1 is the only one of the four that is performance-based, with certification requiring "meeting certain benchmarks in standardized performance evaluations, run quarterly", and the only one with a quarterly revision cadence. The authors disclose the conflict of interest and say they drew only on each standard's published text.

!shot uw-standards.webp | images/ | Table 3 of the paper: ISO 42001, the NIST AI RMF, STAR for AI and AIUC-1 compared by issuing body, release, revision cadence, type, focus, whether certification is performance-based, and depth of technical prescription. | screenshot

The strongest argument in the paper is historical. In 1894, property insurers facing the new fire hazards of electrical equipment founded Underwriters Laboratories. "The UL mark has become a de facto litmus test for insurability." Compliance "was not and is not mandated by law", but UL standards became referenced in electrical codes, and arc-fault interrupters went from a UL standard in 1996 to a code requirement in 1999. Insurers first, then standards, then codes: that is the path the paper proposes for AI agents, with one caveat it states itself, that agent standards will have to be updated far faster.

!shot uw-ul.webp | images/ | Section II.3.E of the paper: Underwriters Laboratories, founded by property insurers in 1894, testing fire suppression sprinklers around 1919; the UL mark as a de facto test of insurability, later referenced in electrical codes. | screenshot

## The tails {#the-tails}

The last part looks at catastrophic risk from frontier AI, "AI CAT". Catastrophes in the low tens of billions would strain private markets; beyond that, societal-scale risks such as critical infrastructure collapse or chemical, biological, radiological or nuclear harm are "all but uninsurable by private markets". The paper sketches a tower: self-insured retention, primary insurance, a mutual for frontier model developers, reinsurance, catastrophe bonds and a government backstop. And it states the stakes: a disaster with about $100 billion in direct damage could erase several trillion dollars of US GDP if it triggered a slowdown, as the collapse of terrorism insurance did after 9/11.

!shot uw-tower.webp | images/ | Figure 2 of the paper: a hypothetical coverage tower for frontier AI catastrophic risk, from self-insured retention and primary insurance through mutual insurance, reinsurance and catastrophe bonds to a government backstop. Proportions are illustrative. | screenshot

## The market already selling it {#the-market}

I found the paper through a LinkedIn post by Arup Das, "Your AI Agent Can Spend Money. Who Insures Its Mistakes?", which lists who is already doing this. I checked each claim against the company's own pages, and corrected one:

- **[Harbor](https://harbor.ai/)** takes a company from discovering its agents to insuring them: "Discover and catalog every AI agent", analyse their risks, integrate controls, and "Insure the remaining risk". Its advertised coverage is "Third-party liability", "First-party operational loss" and "Regulatory defense". Its product "evaluates every tool call before execution, blocks anything outside policy, and records every decision as evidence", and every detection "is attributable to its session and agent version". It distributes the cover; [its licence page](https://harbor.ai/legal/licenses) says the policies "are issued by surplus lines insurance carriers".
- **[Armilla](https://www.armilla.ai/)**, a Lloyd's coverholder, offers affirmative AI liability cover, including "AI Agent Mistakes: Claims arising from agent actions, including incorrect decisions and failures to escalate", and [a performance warranty](https://www.armilla.ai/ai-insurance) where "you commit that your AI solution will meet agreed-upon metrics, and the warranty funds the remedy if it doesn't".
- **[Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai.html)** has written AI cover since its first policy in 2018, now as aiSure. Its [method](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html) starts by evaluating "the model development pipelines" (training data, data drift, updating and monitoring) and estimating future underperformance from "historical performance data".
- **[Mosaic Insurance](https://www.mosaicinsurance.com/underwriting/aisure/)** "underwrites and markets Munich Re's aiSure", which pays "when an AI model fails to meet clearly defined performance thresholds", with claims settled "based on measurable performance data". (The post presents it as Mosaic's own product; it is Munich Re's, sold by Mosaic.)
- **[AIUC](https://aiuc.com/)** combines a standard, audits and insurance. [AIUC-1](https://www.aiuc-1.com/) certification means red-teaming of "1,000 to 5,000 different test scenarios" and "Quarterly retests", with the standard itself updated quarterly.
- **[ElevenLabs](https://elevenlabs.io/blog/aiuc-announcement)** announced on 12 February 2026 what it calls the first AIUC-1-backed insurance policy for voice agents; its agents "underwent 5,835 technical tests across 14 risk categories".

The post's practical advice is the right one: assess the deployed workflow, "including its tools, data, permissions, approval gates and failure modes"; measure a blocked attempt and an executed action that causes a loss separately; and agree up front "which model, tool, permission and use-case changes require notification, retesting or revised terms". It ends with the question I think every company deploying agents now faces: "Can we prove what an agent may do, how often it fails, what failure costs and which losses are actually insured?"

## What the paper asks for, and does not build {#the-gap}

The paper is a blueprint for the insurance industry. It is precise about what insurers should build together, and about what they should ask of the companies they cover: who is accountable, what the agent can reach, what it may do, what changed since the last assessment, and evidence that the controls held. What it does not set out is how a company deploying agents produces that evidence, day after day, for every agent it runs. That is not a criticism; it is a different job. But it is the job that decides whether any of the stack works, because every layer above it, standards, risk selection, pricing, monitoring and claims, is only as good as the evidence that comes up from below.

That is the job we have been doing.

## What we are building at RiskMandate {#riskmandate}

At [RiskMandate](https://riskmandate.ai), the company I co-founded, the unit of work is the agent behaviour policy: who is acting and under whose authority, which effects are allowed or forbidden, how the rules are enforced, tested and evidenced, and how the supported version stays true. It answers, almost line for line, the questions the paper says underwriters should ask:

- **"To whom is AI risk management delegated?"** Every policy names an accountable owner, and [the delegation record](https://newsroom.sgit.ai/articles/the-delegation-record.html) carries the approved behaviour, the observed grant, the gap between them, the controls, the evidence, and the supported version.
- **Agent access-control configurations.** We map the agent's reach, everything it can access or cause, against its mandate, what the business actually delegated. The gap is the risk.
- **Deterministic safeguards.** Our policies run as hooks that deny a call before it happens. In [an agent that may only chat](https://newsroom.sgit.ai/articles/an-agent-that-may-only-chat.html), one policy was tested in 96 Claude Code runs and 11 claude.ai chats, including a drill where a system prompt told the model to ignore the policy: the line alone held 3 of 12 attacks, the line with hooks 12 of 12, with every blocked attempt logged.
- **A blocked attempt and an executed action, measured separately.** That is exactly what the hooks' audit logs record.
- **Change management.** The supported version and its change review are part of what a customer is retained to maintain.
- **Who answers for the failure.** In [the policy draws the liability line](https://newsroom.sgit.ai/articles/the-policy-draws-the-liability-line.html) I argued that a behaviour policy beside every agent's prompt is what makes accountability possible at all.

!shot uw-map.webp | images/ | The paper's eight components on the left; on the right, what RiskMandate and sgit already produce: the agent behaviour policy (reach, mandate, the gap), hooks and their audit logs, tests and drills, the delegation record, AIUC-1 as a graph with its conformance layer, insurability as a query, and the maintainers' sign-off on what agents run on. Solid lines exist; dashed lines are proposed. | concept

## What we did with AIUC-1 {#aiuc-1}

On sgit.ai we went further with AIUC-1 than reading it. In August we published [AIUC-1 as a graph you can cite](https://sgit.ai/demos/vaults/aiuc-1-graph/index.html): an unofficial, derivative, machine-readable catalogue of the public standard, 53 controls as 2,788 nodes and 11,610 edges, in a vault anyone can open. In September we forked it into [provenance is not conformance](https://sgit.ai/demos/vaults/aiuc-1-conformance/index.html), which adds one layer above the standard and keeps two questions apart with two edges that are never allowed to touch: does the standard say this, and does this subject do this. Its first line says it all: "A standard tells you what good looks like. It cannot tell you whether you do it."

That layer then asks the question this paper is about: given what is actually evidenced, on a given date, what would be insurable? For an invented subject, the answer was one condition met, 52 exclusions, and none of five consequences covered, each exclusion with the reason in the control's own words. Move the date forward and conditions become exclusions on their own, because the evidence behind them expires. Joined to [the EU AI Act as a graph](https://sgit.ai/demos/vaults/regulation-graph/index.html), 62 of the standard's 1,126 published crosswalks resolved to articles, and 8 of the 27 articles reached had since been amended: the crosswalk was written against text that no longer says what it said.

!shot uw-insurability.webp | images/ | The AIUC-1 conformance layer on sgit.ai computing insurability for an invented subject on a given date: one condition met, 52 exclusions, none of five consequences covered, each with the reason in the control's own words. Unofficial and derivative; not approved, certified or endorsed by AIUC. | screenshot

Both vaults are unofficial and derivative: not approved, certified, endorsed or reviewed by AIUC, and not a substitute for the standard. But they show something the paper needs: a standard and the evidence against it, as data, so that insurability can be computed rather than asserted, and recomputed when the evidence changes.

## What the paper has that we still miss {#what-we-miss}

Reading it against our own work, the paper is also a good list of what we have not built.

!shot uw-gaps.webp | images/ | What the paper has that we still miss: a loss number, incident data at scale, accumulation, contract language, a recurring test cadence, and multi-agent failures. | concept

- **A loss number.** Our policies say what an agent may do and prove the boundary held. They do not yet put a price on the failure. The paper's severity × probability × usage is the missing column in the delegation record.
- **Incident data at scale.** Our hooks log every call they see. Nothing pools such records across organisations, in a shared taxonomy, with near misses.
- **Accumulation.** We map one deployment at a time. The paper asks what fails together.
- **Contract language.** We draw the liability line in a policy; insurers need it in definitions, exclusions, aggregation and triggers.
- **A recurring cadence.** We test a policy when we build it. AIUC-1 certification includes quarterly retests; the paper wants tests repeated like penetration tests.
- **Multi-agent failures.** Our policies govern one agent at a time.

There is one gap the paper has that we may be able to fill. It barely mentions open source: its supply-chain concern is the model providers. But agents run on open source runtimes and libraries, and in [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html) I proposed that the versions products ship should be signed off by the people who maintain them. Underwriters Laboratories is the precedent for exactly that: a mark from the people who know the thing, that insurers first rely on and codes later require.

## What this does not claim {#limits}

- **A review of the core.** I read the summary, the stack, standards, risk selection and pricing in full, not all 117 pages.
- **The paper's numbers are the paper's.** Its survey figures and estimates are quoted as it states them.
- **The companies' offers are as their own pages describe them.** Not as tested products.
- **Our mapping is ours.** The paper does not mention RiskMandate or agent behaviour policies.
- **The AIUC-1 vaults are unofficial.** Derivative, with invented subjects, not endorsed by AIUC.

## Where this comes from {#sources}

[Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack](https://arxiv.org/abs/2607.11999v2), arXiv 2607.11999v2, July 2026, CC BY 4.0, read in full for its key takeaways, extended summary, Parts I and II on standards, risk selection and pricing, and Part III's summary; the screenshots are of its pages. Arup Das's LinkedIn post, from the screenshot I was sent. The companies' own pages, linked above. On RiskMandate and sgit: [riskmandate.ai](https://riskmandate.ai), [the delegation record](https://newsroom.sgit.ai/articles/the-delegation-record.html), [an agent that may only chat](https://newsroom.sgit.ai/articles/an-agent-that-may-only-chat.html), [the policy draws the liability line](https://newsroom.sgit.ai/articles/the-policy-draws-the-liability-line.html), the [AIUC-1 catalogue](https://sgit.ai/demos/vaults/aiuc-1-graph/index.html) and [conformance](https://sgit.ai/demos/vaults/aiuc-1-conformance/index.html) vaults, and [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
