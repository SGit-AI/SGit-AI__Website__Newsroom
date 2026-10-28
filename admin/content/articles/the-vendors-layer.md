---
title: The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product
date: 2026-10-28
author: Dinis Cruz
author_url: about/index.html
summary: The first two articles of this series described insuring an agent row by row from its behaviour policy, and who could carry that risk. This one is about a party I think has to carry some of it: the vendor that sells the agent. When a company buys an agentic workflow, part of what can go wrong is the company's own doing, the access it granted and the data it connected, and part is the vendor's, the model's answer, the guardrail that let something through. Cloud providers settled the same question years ago with a shared responsibility model: AWS calls it security of the cloud and security in the cloud. Agent vendors' published terms put almost all of it on the customer: Anthropic's and Salesforce's both cap liability at the fees paid in the previous twelve months, indemnify intellectual property claims, and leave it to the customer to decide whether outputs are appropriate or use is safe. Some vendors already back their products with money, and the most useful shape is Microsoft's: cover, as long as the customer used the guardrails the product provides. Europe is moving the line from 9 December 2026, when software, AI systems included, becomes a product under the new product liability directive, with no contractual cap against an injured person. So I propose the vendor's layer: in each row of a behaviour policy, a share the vendor carries when its own conditions held. In the worked example, of a £6,720 premium for £80,000 of cover, the vendor carries £1,816, mostly on the rows its product decides; the row the customer decided by granting write access stays the customer's. The formula, the inputs and a calculator are in a vault anyone can open.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: insurance, underwriting, agent-behaviour-policy, riskmandate, vendors, liability, product-liability, shared-responsibility, vaults, article
status: published
---

!shot vl-split.webp | images/ | Each row's premium split between the agent's vendor and the customer's insurer. Illustrative, from the vault. | comparison

## In short {#in-short}

- **Part of an agent's risk belongs to the vendor that sells it.** The model's answer and the guardrail that let something through are the vendor's product; the access granted and the data connected are the customer's.
- **Cloud providers already split it.** AWS calls it security of the cloud and security in the cloud.
- **Agent vendors' terms put most of it on the customer.** Two published contracts cap liability at a year's fees, indemnify IP claims, and leave outputs and safe use to the customer.
- **The right shape already exists.** Microsoft covers copyright claims as long as the customer used the guardrails it built.
- **Europe moves the line on 9 December 2026.** Software, AI systems included, becomes a product, with no contractual cap against an injured person.
- **So each row gets a vendor's layer.** A share the vendor carries when its own conditions held.
- **In the worked example, the vendor carries £1,816 of £6,720.** Mostly on the rows its product decides; the grant the customer gave stays the customer's.
- **The formula is now a vault.** The inputs, a script that reproduces every number, and a calculator anyone can open.

## Two parties in every row {#two-parties}

In [a payout for every row](/articles/a-payout-for-every-row.html) I described an agent behaviour policy read as an insurance policy, each row with its own limit and premium, and in [who carries the risk](/articles/who-carries-the-risk.html) who could carry it. Both articles treated the customer as the only party. That is not how it works when the agent is bought.

Take the support agent from the worked example. If it corrupts customer records, the first question is who gave it write access to the CRM: that is the customer's decision, and the customer's row. If it tells a customer something wrong that the customer acts on, the answer came from the vendor's model, shaped by the vendor's guardrails. And if it leaks data through an output filter the vendor provides and the customer left switched on, part of that is the vendor's too. Every row has two parties in it, and I think the vendor should carry a share of the rows its product decides. In my memo the example was blunter: a vendor saying, if my agent attacks another company, I insure you up to this amount.

## The cloud settled this already {#shared}

Cloud providers had the same question and answered it with a model everyone now knows. In AWS's words, "Security and Compliance is a shared responsibility between AWS and the customer", and "this differentiation of responsibility is commonly referred to as Security 'of' the Cloud versus Security 'in' the Cloud" ([AWS](https://aws.amazon.com/compliance/shared-responsibility-model/)). AWS runs the hardware, software, networking and facilities; the customer configures what it builds on them.

!shot vl-shared.webp | images/ | The cloud's shared responsibility model, and the same split for an agent: of the agent, and in the agent. | diagram

For an agent, the same split holds: the vendor is responsible for the agent itself, its model, guardrails, updates and security; the customer for what it does with it, the grant, the data, the controls around it and where it runs. The difference is where the line falls. In the cloud it runs between two lists of things. In an agent it runs through each row, and it moves with the controls, which is why I would like it written in the behaviour policy rather than in a diagram. It is the same thread as [who signs for this](/articles/who-signs-for-this.html): the parts somebody signs, and the gaps between them.

## What the contracts say today {#terms}

I read two published contracts to see where the line falls now. Anthropic's commercial terms, effective 17 June 2025, limit liability to "Fees paid by Customer for the Services in the previous 12 months", exclude consequential damages, indemnify third-party intellectual property claims, and say "It is Customer's responsibility to evaluate whether Outputs are appropriate for Customer's use case, including where human review is appropriate" ([Anthropic](https://www.anthropic.com/legal/commercial-terms)). Salesforce's main services agreement, updated 15 October 2026, caps each party's liability at the amount paid "IN THE TWELVE MONTHS PRECEDING THE FIRST INCIDENT OUT OF WHICH THE LIABILITY AROSE", and indemnifies intellectual property claims ([Salesforce](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/salesforce_MSA.pdf)); its AI acceptable use policy adds "Customer is responsible for determining if its use of these technologies is safe." We found no warranty, indemnity or insurance for what an Agentforce agent does.

!shot vl-terms.webp | images/ | Two AI vendors' published terms beside the EU's product liability directive and AI Act. | comparison

These are standard software terms, and they make sense for software that does what it is told. An agent decides some of what it does, and that is the part the terms leave with the customer. A year's fees is also small beside the limits in the worked example: a support agent priced at a few thousand pounds a year, against £80,000 of rows.

## The vendors who have started {#started}

Some vendors already put money behind their products, and the conditions are the most useful part. Microsoft's commitment says "we will defend the customer and pay the amount of any adverse judgments or settlements", "as long as the customer used the guardrails and content filters we have built into our products" ([Microsoft](https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/), 7 September 2023). That is exactly the vendor's layer, for one row: the vendor carries the risk, on the condition that the customer kept the vendor's controls on. Google, Anthropic and OpenAI made similar commitments in 2023, and like Microsoft's they cover copyright claims.

For what an agent does, the examples are about performance. Intercom offers "up to $1M of your money back" for its Fin agent, under stated conditions ([Intercom](https://intercom.help/fin4all/en/articles/11645601-what-is-the-fin-guarantee), 24 June 2025). Sierra and Zendesk charge for outcomes: at Zendesk "customers will only incur costs for issues that are resolved autonomously by AI" ([Zendesk](https://www.zendesk.com/newsroom/articles/zendesk-outcome-based-pricing/), 28 August 2024), which ties the price to the work, though it does not pay for a mistake. ElevenLabs is the one vendor we found with insurance backed by AIUC-1 for its agents, announced on 12 February 2026 ([ElevenLabs](https://elevenlabs.io/blog/aiuc-announcement)); AIUC-1 has since certified Cursor, KPMG's aIQ Capture and Sierra, among others, and Munich Re offers vendors "performance warranties" that "enable you to indemnify your clients for their financial losses" ([Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai.html)).

## Europe moves the line {#europe}

The law is about to move part of this, at least in Europe. The new product liability directive, (EU) 2024/2853, says a product "includes electricity, digital manufacturing files, raw materials and software", and its recital adds that "A developer or producer of software, including AI system providers within the meaning of Regulation (EU) 2024/1689 ... should be treated as a manufacturer" ([EUR-Lex](https://eur-lex.europa.eu/eli/dir/2024/2853/oj)). The maker cannot point to a defect that arose later when it comes from "software, including software updates or upgrades" or "a lack of software updates or upgrades necessary to maintain safety", "provided that it is within the manufacturer's control" (article 11), and "A product can also be found to be defective on account of its cybersecurity vulnerability" (recital 32). Article 15 is the one that meets the contracts above: liability "is not, in relation to the injured person, limited or excluded by a contractual provision or by national law." Member states must apply it by 9 December 2026, to products placed on the market after that date.

It has limits worth stating. Only natural persons can claim under it, so a business customer's loss stays under its contract. But it sets a direction: the maker of software that keeps updating it, and keeps control of it, keeps responsibility for it. The AI Act already divides the work the same way: providers of high-risk systems must make them compliant (article 16), and deployers must use them "in accordance with the instructions for use" and "assign human oversight to natural persons who have the necessary competence, training and authority" (article 26) ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)). A deployer that makes "a substantial modification" becomes a provider itself (article 25). Those are the two parties of every row, in law.

## The vendor's layer {#layer}

So here is the proposal, as one more step in [the formula](/articles/a-payout-for-every-row.html#formula): **each row of the behaviour policy carries a vendor's share, which the vendor pays when its own conditions held**. The vendor prices that layer into what it sells, and insures it if it likes; the customer's insurer prices the rest.

In the worked example, I gave the three covered rows these shares:

- **Customer records corrupted: 0%.** The agent could corrupt records because the customer gave it `crm:write`. The vendor's product did what it was allowed to do.
- **Customer data leaked: 20%.** A leak through the vendor's own output filter, with the filter switched on, is partly the vendor's.
- **A wrong answer acted on: 50%.** The answer is the vendor's product.

With five enforced controls on a certified runtime, the premium is £6,720 for £80,000 of cover, and the vendor's layer is £1,816 of it: £816 on the leak row and £1,000 on the answer row. The customer's insurer prices £4,904. The vendor's condition is its guardrails and filters left on, the Microsoft condition: switch them off and the vendor carries nothing, and the customer's insurer carries every row. The shell row is excluded for both, because nobody named a limit for it.

The shares are mine and illustrative; who carries what is the negotiation, and the point is that it becomes a negotiation about named rows, rather than a liability cap set against a year's fees.

## The formula, as a vault {#vault}

The formula, its inputs and the worked example are now a vault, so they can be argued with in numbers rather than words.

It is vault `m1wbrefr`, published with its read key so anyone can open it: [open the calculator in the vault viewer](https://dev.vault.sgraph.ai/#sgit_public_read_54a5d5d39863f124c6a304b20874e53436d77df42945ba15c74712a680b22991%3Am1wbrefr), or clone it with `sgit clone sgit_public_read_54a5d5d39863f124c6a304b20874e53436d77df42945ba15c74712a680b22991:m1wbrefr agent-underwriting` and run `python3 premium.py`.

It holds `formula.md`, the seven steps in words; `policy.json`, every input, the four rows, the seven controls, the runtime factors, the vendor's share per row; `premium.py`, which reproduces every number in this series with Python's standard library; and a calculator. In the calculator you switch controls on and off, choose the runtime, change any row's limit or the vendor's share, and test a claim against a row with its conditions held or not. A control nothing enforces, such as a line in the prompt, can be ticked and moves nothing.

## Where this leaves the series {#next}

Three articles in, the series has a definition, a market and a split. What I would like next is to take this to the people who would carry it:

1. **To vendors of agents:** which rows would you carry, at what share, and under which conditions?
2. **To insurers and managing agents:** would you price the customer's layer from these rows, and the vendor's layer as a separate book?
3. **To the people who write behaviour policies:** a field for the vendor's share and its conditions, beside each row.

## What this does not claim {#limits}

- **The shares and numbers are illustrative.** They are mine, chosen to show the shape; nobody has negotiated them.
- **Two contracts are not the market.** Anthropic's and Salesforce's published terms were read; other vendors' terms differ, and enterprise contracts are often negotiated.
- **This is not legal advice.** The directive's articles are quoted as written; how each member state applies them from December 2026 is open, and only natural persons can claim under it.
- **"We found no" means what it says.** No Agentforce cover and no AIUC-1-backed insurance beyond ElevenLabs were found in public sources on 28 October 2026.
- **The copyright commitments cover copyright.** They are cited for their shape, cover on a condition, not as cover for agent actions.

If you sell an agent and would carry a share of its rows, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 28 October 2026, the first of this series, which asked for "the insurance that I also believe that the vendors have to start giving when they provide an agentic workflow", and the second, which imagined a provider insuring what its agent does; written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine.

Every outside source is linked where it is used. They were read on 28 October 2026 by research agents of this site, which fetched each page quoted. The EU texts were read through the EU Publications Office's copy of EUR-Lex. OpenAI's copyright commitment is described from press coverage of 6 November 2023, because its own page could not be fetched, and is not quoted. The research notes, with what could and could not be verified, are `admin/notes/2026-10-28__underwriting-abp/research-01.md` and `research-03.md` in this site's repository.

The worked example and the vault: `premium.py` and `policy.json` in the vault, whose sources are also kept in this site's repository under `admin/notes/2026-10-28__underwriting-abp/vault-agent-underwriting/`; the numbers match [a payout for every row](/articles/a-payout-for-every-row.html), and the vendor's layer is new here. On this site: [who carries the risk](/articles/who-carries-the-risk.html), [who signs for this](/articles/who-signs-for-this.html).
