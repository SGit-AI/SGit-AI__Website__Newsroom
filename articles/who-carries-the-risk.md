# Who carries the risk: the companies already insuring AI agents, the parts an insurer for agent behaviour policies would need, and why the first one starts as a managing agent on someone else's capital, sgit.ai

> In the last article I described insuring an agent row by row, from its behaviour policy. We have most of the pieces to put a number on it: the open behaviour policy, a way to map controls to agents and risks, the AIUC-1 standard as a graph on sgit.ai, and a deterministic formula. So the next questions are who sells this today, and what it would take to build a company that does. Today several companies sell AI agent cover: AIUC pairs a standard and audits with insurance, Armilla and Testudo write it as Lloyd's coverholders with limits up to $25 million and $9.25 million, Munich Re prices AI model performance itself, and Harbor distributes cover from surplus lines carriers. We found nobody pricing per row of a behaviour policy yet. The industry already has every part such a company needs: someone to measure, someone to price and bind, someone whose balance sheet pays, and someone who reinsures the tail. I thought it was mostly a capital problem, as I understood it was for neobanks, and asked to be corrected. Partly I was: many early neobanks needed little capital because they could not lend, and their hard part was the licence and the build-out. For an insurance carrier, capital is the business: enough to survive a one-in-two-hundred-year year. But the first company does not need to be a carrier. Coalition and At-Bay started by pricing on other insurers' capital and bought carriers later. So a company built on open behaviour policies could start small, with niche agents, agents in QA, or cover for a few per cent of users, and earn the record that brings capital, then the large providers insuring their own agents. Cover that lapses with an unpatched known vulnerability already exists, which is where this connects to the PHP story.

*Source: <https://newsroom.sgit.ai/articles/who-carries-the-risk.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who carries the risk: the companies already insuring AI agents, the parts an insurer for agent behaviour policies would need, and why the first one starts as a managing agent on someone else's capital

# Who carries the risk: the companies already insuring AI agents, the parts an insurer for agent behaviour policies would need, and why the first one starts as a managing agent on someone else's capital

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.2.0, 3 versions](versions/who-carries-the-risk.md) · [newsroom v0.13.124](https://newsroom.sgit.ai/admin/versions.html) · insuranceunderwritingagent-behaviour-policyriskmandatemgacapitalreinsuranceaiucstartupsarticle

***Abstract:** In the last article I described insuring an agent row by row, from its behaviour policy. We have most of the pieces to put a number on it: the open behaviour policy, a way to map controls to agents and risks, the AIUC-1 standard as a graph on sgit.ai, and a deterministic formula. So the next questions are who sells this today, and what it would take to build a company that does. Today several companies sell AI agent cover: AIUC pairs a standard and audits with insurance, Armilla and Testudo write it as Lloyd's coverholders with limits up to $25 million and $9.25 million, Munich Re prices AI model performance itself, and Harbor distributes cover from surplus lines carriers. We found nobody pricing per row of a behaviour policy yet. The industry already has every part such a company needs: someone to measure, someone to price and bind, someone whose balance sheet pays, and someone who reinsures the tail. I thought it was mostly a capital problem, as I understood it was for neobanks, and asked to be corrected. Partly I was: many early neobanks needed little capital because they could not lend, and their hard part was the licence and the build-out. For an insurance carrier, capital is the business: enough to survive a one-in-two-hundred-year year. But the first company does not need to be a carrier. Coalition and At-Bay started by pricing on other insurers' capital and bought carriers later. So a company built on open behaviour policies could start small, with niche agents, agents in QA, or cover for a few per cent of users, and earn the record that brings capital, then the large providers insuring their own agents. Cover that lapses with an unpatched known vulnerability already exists, which is where this connects to the PHP story.*

The four parts of an insurer for agent behaviour policies, and who already does each one today.

**What came next.** [The vendor's layer](the-vendors-layer.md) gives each row a share the agent's vendor carries, and puts the formula and a calculator in a vault.

## In short

- **We have most of the pieces to put a number on an agent.** The open behaviour policy, the controls mapped to risks, AIUC-1 as a graph, and [a deterministic formula](a-payout-for-every-row.md).
- **Several companies already sell AI agent cover.** AIUC, Armilla, Testudo, Munich Re, and Harbor as a distributor; we found nobody pricing per row of a behaviour policy.
- **The industry already has every part such a company needs.** Measure, price and bind, carry the balance sheet, reinsure the tail.
- **I thought it was a capital problem, like neobanks, and was partly wrong.** Many early neobanks could not lend and needed little capital; their hard part was the licence and the build-out.
- **For a carrier, capital is the business.** Enough own funds to survive a one-in-two-hundred-year year, with a floor of £2.4 million in the UK.
- **The first company does not need to be a carrier.** A managing agent prices and sells on a carrier's capital; Coalition and At-Bay started there and bought carriers later.
- **Cover that lapses with a known vulnerability already exists.** Chubb shifts the risk to the policyholder in steps after a 45-day grace period to patch.
- **Start small, then the large providers.** Niche agents, agents in QA, a few per cent of users; then the model providers insuring their own agents, which some have already looked at.

## What we have, and the question it leaves

In [a payout for every row](a-payout-for-every-row.md) I described how an agent behaviour policy could be insured: each row it names with its own limit, each enforced control lowering the premium, and what it does not name excluded. I think we now have most of the pieces of the puzzle to calculate that number. The behaviour policy exists and is open source; [what can your agent reach?](what-can-your-agent-reach.md) explains it. We have a way to map controls to agents and to risks: on sgit.ai we turned the AIUC-1 standard into a graph and asked it what would be insurable, as [underwriting the agent economy, reviewed](underwriting-the-agent-economy-reviewed.md) describes. And we have a formula that says: with this agent, with these controls, the premium is this and the payout is that.

So the next questions are practical. Who sells that today? And if someone, or an investor, wanted to build a company that does, what would it take? I should say first what I am not: this has to be built by people who are experts in insurance and understand the medium, and it needs a lot of capital. What I can do is map the pieces, and ask the questions an expert would have to answer.

## Who sells AI agent cover today

The market is already moving, and the last review of it on this site is four days old. What it found, and what has been checked since:

- **AIUC** combines a standard, audits and insurance. When it came out of stealth, its policies were described as covering "customers and vendors in the event an agent causes harm", with pricing that "reflects how safe the system is" ([Fortune](https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/), 23 July 2025). In September 2026 it raised a Series A to extend its audits, standards and insurance to frontier models, reported as $40 million and given on AIUC's own site as $55 million; the companies certified to AIUC-1 include Cursor, ElevenLabs, Harvey, KPMG, Lovable, UiPath and Intercom's Fin ([FinTech Global](https://fintech.global/2026/09/17/aiuc-raises-40m-to-police-risk-in-frontier-ai-agents/), 17 September 2026).
- **Armilla** is a Lloyd's coverholder whose affirmative AI liability cover is "underwritten by certain underwriters at Lloyd's, including Chaucer" ([Armilla](https://www.armilla.ai/resources/armilla-launches-affirmative-ai-liability-insurance-with-lloyds-underwriter-chaucer), 30 April 2025), now with limits "up to $25 million per organization" and cover for "AI Agent Failures: Claims arising from incorrect decisions, improper tool use, or escalation errors" ([Armilla](https://www.armilla.ai/resources/armilla-ai-raises-lloyds-backed-coverage-to-25m-as-traditional-insurers-retreat-from-ai-risk)).
- **Testudo**, another Lloyd's coverholder, covers third-party claims from "AI-generated outputs", with limits of "$9.25m per insured" since Atrium and QBE joined Apollo on its panel ([FinTech Global](https://fintech.global/2026/03/09/testudo-expands-ai-liability-capacity-to-9-25m/), 9 March 2026).
- **Munich Re** has written AI cover since 2018 as aiSure, and says "The quality of the model and its performance stability determine the premium" ([Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html)).
- **Harbor** takes a company from discovering its agents to insuring them, and its policies "are issued by surplus lines insurance carriers", as the last review recorded.

Each of these is a real step. None, as far as we found, prices an agent per row of its behaviour policy, with a limit per named risk and a factor per enforced control. AIUC comes nearest, because it pairs a standard and its audits with the cover. That is the gap, and since the behaviour policy is open, the company that fills it does not have to be RiskMandate: anyone can build on the policies, and sponsor the mapping for the agents they insure.

## The parts of an insurer

The insurance industry has spent a long time separating the jobs, and it helps to name them, because a new company does not have to do them all.

1. **The policy and the evidence.** What the agent can reach, what it may do, and the logs that show each control held. This is the behaviour policy's job, and where RiskMandate works; AIUC's audits are another form of it.
2. **Pricing and binding.** A managing general agent, which Lloyd's calls a coverholder, prices and sells policies on an insurer's behalf. In Lloyd's words, it "is a company that has been authorised" "by a Lloyd's Managing Agent to enter into insurance contracts on behalf of a Lloyd's syndicate", and "This authority is granted through a formal Binding Authority agreement" ([Lloyd's](https://www.lloyds.com/market-resources/delegated-authorities/compliance-and-operations/about-coverholders)). It does not carry the risk on its own balance sheet; the insurer does.
3. **The balance sheet.** The carrier pays the claim and holds the capital for it. At Lloyd's, "A Lloyd's syndicate is formed by one or more members joining together to provide capital and accept insurance risks on a several liability basis" ([Lloyd's](https://www.lloyds.com/market-resources/member-services/about/what-is-a-member)). A fronting carrier lends its licence and balance sheet to business an MGA places and passes most of the risk on: in the US in 2025, fronting carriers wrote "more than $22 billion in gross premiums" and ceded "nearly $19 billion to nonaffiliated reinsurers" ([Insurance Business](https://www.insurancebusinessmag.com/us/news/breaking-news/conning-fronting-sectors-easy-growth-phase-is-ending-587956.aspx), 31 August 2026, citing a Conning study).
4. **Reinsurance.** "Reinsurance, often referred to as "insurance for insurance companies," is a contract between a reinsurer and an insurer" ([NAIC](https://content.naic.org/insurance-topics/reinsurance)). It takes the tail and the correlated loss: the day one model's flaw hits every agent built on it.

Around them sit distribution, brokers and platforms, and the claim. For agents, the claim could be the simplest part. Swiss Re describes parametric insurance as "a type of insurance that covers the probability of a predefined event happening", paid on an index rather than on a loss adjuster's assessment ([Swiss Re](https://corporatesolutions.swissre.com/en/japan/insights/knowledge/parametric-solutions-srij/what-is-parametric.html)). A row of a behaviour policy is close to that: the event maps to a row, and the log says whether the conditions held.

## Is it a capital problem?

My understanding going in was that this is like the fintech revolution in banking. When the neobanks arrived, they did not give much credit to new accounts, so they carried little risk, and I thought the main gap was having enough capital to cover the balances if something major went wrong. I asked to be corrected if that was wrong, and partly it was.

What an e-money firm, a new bank, an insurance carrier and a managing agent must hold, and the hard part of each.

Many early neobanks were e-money institutions. Those need initial capital "of not less than EUR 350 000" ([EMD2, article 4](https://www.legislation.gov.uk/eudr/2009/110/article/4)), and customer money is safeguarded: credit may be granted only "provided that such credit is not granted from funds safeguarded" ([EMR 2011, regulation 32](https://www.legislation.gov.uk/uksi/2011/99/regulation/32)). A full bank holds capital mostly against its lending: in the EU at the end of 2025, credit risk was 77.9% of banks' risk-weighted assets, operational risk 13.4% and market risk 3.7% ([EBA Risk Dashboard, Q4 2025](https://eba.europa.eu/sites/default/files/2026-03/f99324ee-6d5c-451f-9cfa-5b58a908c18d/EBA%20Risk%20Dashboard%20-%20Q4%202025.pdf)). A new UK bank goes through mobilisation, which "typically lasts no longer than 12 months", while "the bank's deposit-taking permission is restricted to a total of £50,000" ([Bank of England](https://www.bankofengland.co.uk/prudential-regulation/new-bank-start-up-unit)). Revolut was granted its licence with restrictions in July 2024 and left mobilisation on 11 March 2026 ([tech.eu](https://tech.eu/2026/03/11/revolut-wins-full-uk-banking-licence-as-finally-exits-mobilisation-phase/)). So for the neobanks, the hard part was the licence and the build-out as much as the capital.

For an insurer, I was closer to right. The risk is the product, so capital is the business. Under Solvency II, the capital requirement corresponds to the value at risk of the insurer's own funds "subject to a confidence level of 99,5 % over a one-year period" ([Solvency II, article 101](https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-2188_en)): enough to survive a year that comes once in two hundred. Below that there is a minimum, which in the UK "must neither fall below 25% nor exceed 45% of the firm's SCR", with a floor of £2,400,000 for a general insurer ([PRA Rulebook](https://www.prarulebook.co.uk/pra-rules/minimum-capital-requirement/03-06-2026)). In the US, risk-based capital sets "a statutory minimum level of capital" by size and by "the inherent riskiness of its financial assets and operations" ([NAIC](https://content.naic.org/cipr-topics/risk-based-capital)).

And this is where the deterministic formula matters most. Capital is held against what could go wrong at once. A policy that excludes what it does not name, caps every row, and holds a reserve for the catastrophe layer makes the worst year easier to bound, and a bounded worst year needs less capital per pound of cover. It is still a question of how many policies, how much risk accumulates, and how much the balance sheet can hold; but it is a question with numbers.

## Start as a managing agent, carry the risk later

So the first company does not need to be a carrier. It can price and sell on someone else's capital, prove its loss record, and then carry the risk. Two cyber insurers bought carriers of their own once they had a book.

From a managing agent on someone else's capital to a carrier that reinsures the tail, with two cyber precedents.

Coalition "completed the acquisition of Digital Affect Insurance Company from Munich Re Digital Partners US Holding Corporation" on 15 August 2022, a carrier "licensed in all 50 states" ([Coalition](https://www.coalitioninc.com/announcements/Coalition-completes-acquisition-of-insurance-carrier-with-licenses-in-all-50-states)). At-Bay followed on 24 January 2023: "Taking on balance sheet risk and owning our own insurance carrier are crucial steps on our journey" ([At-Bay](https://www.at-bay.com/articles/introducing-at-bay-specialty-insurance-company/)). And a full carrier still cedes part of its risk: Lemonade "expects to cede approximately 18% of premium to reinsurers" under the agreements it renewed in June 2026 ([Lemonade](https://www.lemonade.com/investor/news/lemonade-renews-reinsurance-program-improving-costs-coverage-and-capital-efficiency)).

That answers whether one company or several are needed: at the start, several, with the new company as the managing agent and established carriers and reinsurers behind it; later, possibly one group that does most of it. I would also expect the large insurers to build exactly these divisions themselves, once the market matures and they trust their models. The open behaviour policy makes collaboration easy either way: whoever prices the risk works from the same rows.

## Start small

The way in is small. Insure smaller agents first, or agents while they are in QA, or agents that serve only a small share of users, 1% or 5%, with low limits per row. Each of those gives a carrier a bounded exposure and gives the new company a loss record against named rows and logged controls. Once that works, it can go to the large providers.

There are signs the industry is ready to fund the attempt. Lloyd's Lab's sixteenth cohort includes Exona Lab, a "Risk engine quantifying advanced and systemic AI risks" ([FinTech Global](https://fintech.global/2026/03/20/lloyds-lab-unveils-cohort-16-insurtech-innovators/), 20 March 2026). Deloitte projected in May 2024 that "by 2032, insurers can potentially write around US$4.7 billion" of AI insurance premiums, "at a compounded annual growth rate of around 80%" ([Deloitte](https://www.deloitte.com/us/en/insights/industry/financial-services/risk-insurance-for-ai.html)).

## Fractal, not top-down

This is not about selling one large policy to a company. A top-down policy is what you sell when you already have fifty, five hundred or a thousand small ones: one per agent, each tied to where it runs, the software under it, and the ecosystem around it. The company-wide policy is the aggregate, and its limit is the sum of rows the insurer is willing to hold together.

That also means the cover moves with the software. Take [a PHP website with an application behaviour policy](application-behaviour-policies.md), insured as long as no known vulnerability in it is left unpatched. When a vulnerability like [php2shell](who-maintains-the-php-you-run.md) is published, you either fix it or take the site offline, because otherwise you are running outside the policy, and uninsured. That already exists in cyber insurance. Chubb's neglected software endorsement gives policyholders "a 45-day grace period to patch software vulnerabilities that are published as Common Vulnerabilities and Exposures (CVEs)", after which the risk shifts towards the policyholder "at the 46-, 90-, 180-, and 365-day points" ([Chubb](https://chubb.com/content/dam/chubb-sites/chubb-com/nordic-en/_assets/documents/Chubb_DK_EN043_Cyber_Endorsement_202202.pdf), 2022). Coalition reports another insurer that "excludes losses arising from CVEs with a Common Vulnerability Scoring System (CVSS) severity score greater than 8.0" when the patch was not applied within three weeks, and counts "As of July 2025, 61,764 vulnerabilities would qualify" ([Coalition](https://www.coalitioninc.com/blog/cyber-insurance/taking-responsibility-in-the-age-of-non-stop-cves), 31 July 2025). A behaviour policy makes that rule precise: which row the vulnerability touches, and which control would have to hold for the row to stay in cover.

## The providers insuring their own agents

There is an opportunity at both ends: enterprise and personal cover, and the providers of agentic workflows insuring their own agents. Imagine a provider saying: I provide this service, and if my agent attacks another company, I insure you up to this amount. I think the large providers will play, once they see it working, even if they do not fully do it now.

They have already looked at the problem from the other side. Insurance Journal, reporting the Financial Times on 8 October 2025, wrote that "OpenAI has considered "self-insurance" by setting aside investor funding", that it "has secured coverage of up to $300 million for emerging AI risks", and that Anthropic is "partly using its own funds to cover potential settlements" ([Insurance Journal](https://amp.insurancejournal.com/news/national/2025/10/08/843087.htm)). A provider that can show, row by row, what its agents may do and what stops them, has a better chance of getting cover, and of selling it on.

And some of this may become required. Everyone who drives on a road needs insurance: the Road Traffic Act says "a person must not use a motor vehicle on a road or other public place unless there is in force" a policy that complies with it ([section 143](https://www.legislation.gov.uk/ukpga/1988/52/section/143)). In October 2020 the European Parliament asked that operators of high-risk AI "should take out liability insurance similar to that for motor vehicles" ([European Parliament](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1636987)), in a resolution that does not bind; the Commission withdrew its AI liability directive in February 2025. As agents get more powerful, I believe agents with real reach will need insurance in the same way.

## The questions for the people who would build it

This is a research brief as much as an article, so here are the questions I would like answered by people who know insurance:

1. **Which carrier or Lloyd's syndicate would give a binding authority to a managing agent that prices per row of a behaviour policy?** And what loss record would it want first?
2. **How much capital does a book of capped, deterministic rows actually need?** Compared with a cyber book of the same premium.
3. **How do correlated losses work when many agents share one model?** Which rows aggregate across a fleet, and what does the reinsurer need to see?
4. **What does the claim look like?** Close to parametric, or with a loss adjuster, and who reads the logs?
5. **Who certifies the runtime and the enforcing software?** And is that a condition of cover or a factor in the price?
6. **Where do the providers' own warranties sit?** Beside the customer's cover, or under it?
7. **Which market goes first: enterprise agents, personal agents, or the providers?**

## What this does not claim

- **I am not an insurance expert.** This maps the parts as published; building it needs underwriters, actuaries, lawyers and regulators.
- **The landscape is what we found.** Companies may price agents in ways not visible from their public pages; "nobody prices per row" means nobody we found.
- **The capital comparison is simplified.** Real capital requirements depend on the risk model, the lines written and the regulator; the floors quoted are minimums, not what a carrier holds.
- **The path is a precedent, not a plan.** Coalition and At-Bay are cyber insurers; agents may need a different route.
- **The market forecast is Deloitte's, from 2024.** It is a projection, and other figures in circulation were not used because they could not be checked.
- **The compulsory insurance point is a view.** No UK or US law requires insurance for AI agents today, as far as we found.

If you underwrite specialty risk and would like to price an agent row by row, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 28 October 2026, the second of this series, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The neobank comparison is mine and was checked; the correction in the capital section is the research's, not my memo's.

Every outside source is linked where it is used and was read on 28 October 2026 by a research agent of this site, which fetched each page quoted. A few quotes are fragments of longer sentences, joined with quotation marks where the fetch tool cut them. The research notes, with what could and could not be verified, are `admin/notes/2026-10-28__underwriting-abp/research-01.md` and `research-02.md` in this site's repository. Two facts come from secondary sources and are marked so there: Coalition's own carrier launch in January 2023, and Lemonade's earlier share of premium ceded. Neither is used above.

On this site: [a payout for every row](a-payout-for-every-row.md), the first article of this series; [underwriting the agent economy, reviewed](underwriting-the-agent-economy-reviewed.md), for Harbor and the AIUC-1 work; [what can your agent reach?](what-can-your-agent-reach.md); [application behaviour policies](application-behaviour-policies.md) and [who maintains the PHP you run?](who-maintains-the-php-you-run.md) for the PHP story.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#who-carries-the-risk)

### Builds on

- [The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product](the-vendors-layer.md) Each row of an agent behaviour policy gets a vendor's share, carried when the vendor's conditions held; contracts cap at a year's fees, Europe moves the line.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Underwriting the agent economy, reviewed: the cliff notes of the AI insurance stack, the companies already selling AI agent cover, and what agent behaviour policies add to it](underwriting-the-agent-economy-reviewed.md) A review of the AI insurance stack blueprint, the companies selling agent cover, and what agent behaviour policies add to it.
- [Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius](application-behaviour-policies.md) Map an application the way we map an agent, so a site switched off for php2shell can come back with a known blast radius.
- [Who maintains the PHP you run? A version signed off by the people who maintain it, buyers who require that signature, and money that flows down the chain: a follow-up to the maintenance deficit](who-maintains-the-php-you-run.md) Versions signed off by their maintainers, buyers who require it, and money that flows down the chain, scaled by Gen AI.

### Continued by

- [The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product](the-vendors-layer.md) Each row of an agent behaviour policy gets a vendor's share, carried when the vendor's conditions held; contracts cap at a year's fees, Europe moves the line.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 316 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=316)

**Posting this article on LinkedIn?** The cover is [who-carries-the-risk.jpg](banners/who-carries-the-risk.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-carries-the-risk.html)*
