# A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered, sgit.ai

> RiskMandate needs somebody to underwrite agent behaviour policies, and before asking who can, I would like to define what they would be underwriting. An insurer de-risks an action. When I insure the laptops and phones in my house against burglary, the insurer asks about the locks, where I live and where I keep things, sets a limit for any one item and a limit for the policy, leaves out the things it will not cover, and at the claim asks whether the doors were locked. If they were, it pays, up to the limit. Agents need exactly that, and an agent behaviour policy already has the shape: every capability the agent can reach is a row, the mandate says which rows the business authorised, and the delta between them is the reach nobody asked for. So the insurance policy is one-to-one with the behaviour policy: each row it names has its own limit (say £20,000 for corrupted customer records, £50,000 for leaked customer data), each row it does not name is excluded, and every real control on a row, one that something enforces, lowers that row's premium. A line in the prompt is not a control and earns nothing. The formula has to be deterministic, if this, then that, and the runtime the agent runs on is part of it. Start from the maximum: in a worked example, an uncontrolled support agent pays £69,850 a year for £80,000 of cover, insurable but hardly worth buying; with five enforced controls on a certified runtime it pays £6,720 for the same cover. The numbers are illustrative; the shape is the point, and the Licence to Operate vault on sgit.ai already runs a simulated version of it. This is the first of a series: next, who can underwrite this today.

*Source: <https://newsroom.sgit.ai/articles/a-payout-for-every-row.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered

# A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.3.0, 4 versions](versions/a-payout-for-every-row.md) · [newsroom v0.13.124](https://newsroom.sgit.ai/admin/versions.html) · insuranceunderwritingagent-behaviour-policyriskmandatelicence-to-operatecyber-insurancepremiumscontrolsmandatearticle

***Abstract:** RiskMandate needs somebody to underwrite agent behaviour policies, and before asking who can, I would like to define what they would be underwriting. An insurer de-risks an action. When I insure the laptops and phones in my house against burglary, the insurer asks about the locks, where I live and where I keep things, sets a limit for any one item and a limit for the policy, leaves out the things it will not cover, and at the claim asks whether the doors were locked. If they were, it pays, up to the limit. Agents need exactly that, and an agent behaviour policy already has the shape: every capability the agent can reach is a row, the mandate says which rows the business authorised, and the delta between them is the reach nobody asked for. So the insurance policy is one-to-one with the behaviour policy: each row it names has its own limit (say £20,000 for corrupted customer records, £50,000 for leaked customer data), each row it does not name is excluded, and every real control on a row, one that something enforces, lowers that row's premium. A line in the prompt is not a control and earns nothing. The formula has to be deterministic, if this, then that, and the runtime the agent runs on is part of it. Start from the maximum: in a worked example, an uncontrolled support agent pays £69,850 a year for £80,000 of cover, insurable but hardly worth buying; with five enforced controls on a certified runtime it pays £6,720 for the same cover. The numbers are illustrative; the shape is the point, and the Licence to Operate vault on sgit.ai already runs a simulated version of it. This is the first of a series: next, who can underwrite this today.*

One agent's behaviour policy as an insurance policy: a limit, controls and a premium per row. Illustrative.

**What came next.** [Who carries the risk](who-carries-the-risk.md) maps who already insures AI agents and what a company that priced per row would need, starting as a managing agent on someone else's capital.

## In short

- **An insurer de-risks an action, up to a limit, under conditions.** A house policy asks about the locks, caps any one item, leaves some things out, and pays if the conditions held.
- **An agent behaviour policy already has that shape.** Each capability the agent can reach is a row; the mandate says which rows the business authorised.
- **So the insurance is one-to-one with the policy.** Each row it names has its own limit; each row it does not name is excluded.
- **Not everything is insurable, and that is the point.** The bigger the reach, the bigger the delta, and the delta is what no policy covers.
- **The formula is deterministic.** If this control is enforced on this row, the rate falls by this factor; if it was not holding at the time of the loss, the row does not pay.
- **Only enforced controls count.** A hook, a proxy, a capability removed from the grant. A line in the prompt earns nothing.
- **Where the agent runs is part of the price.** A certified runtime lowers it; an uncertified one raises it, or ends the licence to operate.
- **Start from the maximum and come down.** In the worked example, £69,850 a year for £80,000 of cover, uncontrolled; £6,720 with five enforced controls on a certified runtime.
- **The first version already runs.** The Licence to Operate vault on sgit.ai simulates one agent's policy, with a band, a ceiling, a pool and a premium.
- **Next in this series: who can underwrite this today.** And what the vendors of agents should cover themselves.

## An insurer de-risks an action

The question behind this series is simple to ask. RiskMandate writes agent behaviour policies, and the end of [the roadmap](the-riskmandate-roadmap.md) is agents an insurer can cover. So who would underwrite an agent behaviour policy, today, and what would they be underwriting? Before the first question, I would like to answer the second, because I think the answer is simpler than it usually gets made.

Take a house. I have laptops and phones in it, and some jewellery, and I would like to be covered against burglary. The insurer asks where the house is, what kind of locks it has, and where I keep things. It sets a limit for the policy and a limit for any one item, and it asks me to list anything valuable above a certain value. It does not cover everything: a laptop worth £20,000 or a data centre in the spare room is not something a contents policy is built for. Then, when something is stolen, it asks the questions again: were the doors locked, was the phone left in plain view? If the conditions held, it pays, up to the limit.

None of that is my invention. A broker's guide puts the limit for any one item "usually between £1,000 to £2,500" and tells you to "declare any expensive items to your insurer" ([Howden](https://www.howdeninsurance.co.uk/personal/home/home-insurance/guides/single-article-limit/), 9 January 2025). A comparison site says "You may need BS3621 standard five-lever mortice deadlocks on all your external doors in order to get home insurance", and that "you are unlikely to be able to claim on your home insurance if you leave your doors unlocked" ([MoneySuperMarket](https://moneysupermarket.com/home-insurance/house-locks), updated 3 September 2026). Conditions, limits per item, exclusions, and a check at the claim.

A home contents policy and an agent behaviour policy, question by question.

That is a very simple proposition, and it is what agents need. Not a policy for "AI", and not a questionnaire about the company's security programme, but a policy for one agent, in one deployment, that names what is at risk, the conditions, the limits, and what is left out.

## Not every action is insurable, and that is the point

An agent behaviour policy starts from the same place as the house: an inventory. [What can your agent reach?](what-can-your-agent-reach.md) explains it for the person who has to decide. The grant is everything the agent can technically do. The mandate is what the business actually asked it to do. The delta is the gap: inside the agent's reach, outside its authority.

The [Licence to Operate vault](https://sgit.ai/demos/vaults/licence-to-operate/index.html) on sgit.ai makes it countable. Its support agent has a grant of 12 capabilities and a mandate of 4: read the customer record, search the help centre, generate an answer, draft a reply. The other 8, including `crm:write`, `crm:export`, `mail:send` and `shell:exec`, are in its reach and in nobody's mandate, and the vault says it plainly: no policy covers them.

That is not a weakness of the idea. It is the idea. You are not going to insure every action of an agent, and the bigger its reach, the more of it will be uninsurable. What insurance can do is cover the rows you want covered, one by one, and leave the rest visibly outside. The vault even has a number for it: customer records are marked uninsurable above 20 per action.

## One row, one limit

So the insurance policy has the same rows as the behaviour policy. Take an agent connected to the customer database. It can make changes, so it can corrupt records or delete users; it can read them, so it can leak them; it answers customers, so it can tell them something wrong that they act on. Each of those is a row, and each row gets its own limit: up to £20,000 for customer records corrupted, up to £50,000 for customer data leaked, up to £10,000 for a wrong answer acted on.

The lead figure is that policy, row by row. The last row is the one that matters most: `shell:exec` is in the agent's reach and there is no limit beside it, so it is excluded, at any price. If the business wants it covered, it has to name it, decide who accepts it, and put a control on it.

This one-to-one mapping is what makes the rest work. A claim maps to a row; a row has a capability, a limit and the controls that stand in its way; each control has something that enforces it and a log that says whether it held. That is a graph, and it is the kind of graph we now build every day: [governs, enforces, attests](governs-enforces-attests.md) set out the three levels at which a rule is kept, and [approved business mandates](approved-business-mandates.md) why most companies already have the policies and need them turned into tested controls. With generative AI to read the systems and keep the graph current, a mapping at this level of detail is something that can be maintained at scale, and I think that is what will make this kind of insurance scale too.

## The formula has to be deterministic

The underwriter's part is a formula, and it has to be exact: if this, then that. Here is the shape I have in mind, written down so it can be argued with:

1. **A row with no limit is excluded.** If a capability is reachable and the policy names no limit for it, it is not covered.
2. **Each row starts at a base rate.** The share of the limit that an uncontrolled agent would pay for that row in a year.
3. **Each enforced control on a row multiplies its rate by a factor below one.** Write removed from the grant, a proxy that caps records per action, drafts only, an egress allow list, a hook that holds a reply for a person.
4. **Where the agent runs multiplies every row.** Below one for a certified runtime, above one for an uncertified one.
5. **The premium for a row is its limit times its rate.** The policy's premium is the sum.
6. **A claim pays if the event maps to a row and every condition on that row held at the time, up to the row's limit.** If a condition was not holding, the row does not pay: the door was not locked.

The rule that does the most work is in step 3: only an enforced control counts. RiskMandate's [licence to operate](https://riskmandate.ai/licence-to-operate.html) puts it as "A condition with nothing enforcing it is an expectation". We measured the difference in [an agent that may only chat](an-agent-that-may-only-chat.md): when a system prompt told the model to ignore it, the policy as a line in the prompt held 3 of 12 attacks; with a deny-all hook, 12 of 12. So in the formula, a line in the prompt gets a factor of 1. It may be good practice; it is not a control an insurer can price.

The worked example is [in a data file](https://newsroom.sgit.ai/articles/data/a-payout-for-every-row__worked-example.json), computed by a short script, with every input in it. The factors are mine and illustrative; fitting them is what an underwriter does with loss data, and that is the part we do not have.

## Start from the maximum and come down

The formula makes one thing visible that I think matters commercially. You can still insure an uncontrolled agent; it is just expensive. In the worked example, a support agent with no enforced controls, on an uncertified runtime, pays £69,850 a year for £80,000 of cover, 87% of it. That is insurable and close to not worth buying, and it is not far from what I have seen in cyber insurance, where the premium can come near the payout. There is still a reason to pay it: when you need cover to operate at all, a contract or a regulator asking for it, the price of the cover is a cost of doing business.

The annual premium for £80,000 of cover as enforced controls are added, one at a time. Illustrative.

Then each real control brings it down. A certified runtime takes it to £50,800. Removing `crm:write` from the grant, to £39,280. Drafts only, with `mail:send` removed, to £22,280. At most 20 records per action, enforced by a proxy, to £11,440. Outbound traffic only to an allow list, to £8,720. Refunds and legal points held for a person, to £6,720: 8% of the cover. The line in the prompt, second in the figure, moves nothing.

That is how I think cyber insurance should have worked. Much of it has priced on a questionnaire about the company, filled in once a year, rather than on the detail of what a given system could do and what stopped it. RiskMandate's [insurability page](https://riskmandate.ai/insurance.html) says the same thing more sharply: "Questionnaires describe. Evidence prices."

## Insurers already price what they can measure

None of this is new to insurance. Wherever insurers can measure, they price on the measurement.

**Young drivers.** A black box in the car measures how it is driven, and the price follows. One insurer says "We'll collect data on your speed, acceleration, braking and cornering", and that the data helps "work out your renewal price" ([ingenie](https://www.ingenie.com/how-it-works)). A broker adds that many such policies restrict night driving, "usually between 10pm and 6am", and that poor driving may "increase your premium" ([Howden](https://www.howdeninsurance.co.uk/personal/motor/young-driver/guides/black-box-insurance-myths/), 1 September 2025). That is a licence to operate with conditions, measured, and priced on the measurement.

**Health.** UK private medical insurance is underwritten on what you bring to it. Under a moratorium, a condition you had in the five years before joining is not covered until you have gone two years without it; under full medical underwriting, you disclose your history and the exclusions are set before the policy starts, as AXA Health and Bupa describe their own policies. The cover goes up or down with the preconditions.

**Cyber, where it measures.** Some cyber insurers have moved from the form to the scan. Coalition wrote in 2021 that "Traditional cyber insurers will typically ask insureds to fill out long applications", and that it uses "scanning technology that collects and correlates data from internet accessible devices" instead ([Coalition](https://www.coalitioninc.com/blog/risk-engineering-at-coalition-collaboration-to), 3 August 2021). And for AI itself, Munich Re says of its aiSure cover that "The quality of the model and its performance stability determine the premium" ([Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html)). The founder of AIUC, which insures agents, put the idea in one line: "Just like consumers get a better car insurance rate for having airbags and anti-lock brakes" ([Fortune](https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/), 23 July 2025).

My argument is that the more mature an insurance line is, and the more data its insurers can measure, the more precisely it prices, and the more of the risk it is willing to take. Agents are unusual in how much can be measured: every tool call, every record read, every hook decision is logged by the systems that run them. The data an underwriter would need is already being produced. What is missing is the mapping from that data to a row and a limit.

## Where the agent runs

Some of the conditions are not about the agent at all, but about where it runs, the way a house policy asks for the postcode. There will be places where certification is needed: of the runtime, of the hooks and proxies that enforce the controls, down to the software they run on. If an agent runs somewhere that is not certified, either the premium goes up or the row is not covered.

This is also where the licence to operate comes in. RiskMandate describes it as four facts and a date: the organisation as the authority, one agent in one deployment as the licensee, the behaviour policy as the instrument, and an interval after which it has to be renewed, with each condition beside the thing that enforces it. An insurer could reasonably make a current licence a condition of cover, and a change of runtime a reason to look again.

## The licence to operate, simulated

We already have a working version of this, simulated. In the Licence to Operate vault, the policy is a rate table: a normal band, a threshold above which the agent has to ask, a ceiling per action, a pool with an untouchable reserve, and a premium per interval. A simulated support conversation offers three replies at every turn, one inside the band, one that draws on the pool, one outside cover, each with its cost before you choose: 1,400 tokens and 1 record for looking up the customer, 4,800 tokens and 3 records for reading two linked accounts as well, and `mail:send`, outside the mandate entirely. You can let the policy lapse, reinstate it, or trigger a repricing.

The terms are files in the vault, and they read like the formula above. The simulated policy for the support agent, `concierge-sim-2026-09-03`, has a normal band of 2,000 tokens and 5 customer records per action, asks a person above 6,000 tokens or 12 records, sets a ceiling of 8,000 tokens and 20 records per action, refills a pool of 12,000 tokens and 40 records per conversation, and holds back a reserve of 10% that no decision may draw on. Above 20 records the action is not a bigger draw but an exclusion, and the policy gives the reason in one line: "a record once read by an agent is exposure that cannot be unread". Its rating rule is the experience rating an underwriter would recognise: if the pool is drawn on most days, the normal band is wrong, "and the response is to raise the band and shrink the pool, never to enlarge the pool".

At the top it asserts four things: licence held, mandate in force, policy paid, inside cover. All four can be lost. That is the top-up and the payout I had in mind, run in a browser. It is in credits, not money, and the vault says so on its surface: "Simulated. The terms are real files in this vault; the replies are scripted; the numbers are made up."

## The vendors' share

There is one more party I think has to carry some of this: the vendor that provides the agentic workflow. When a company buys an agent from a vendor, part of what goes wrong will be the vendor's, and I believe vendors will have to start backing their agents with cover of their own.

Some vendors have started, and the most interesting part is the conditions. Microsoft's commitment for Copilot says "we will defend the customer and pay the amount of any adverse judgments or settlements", but only "as long as the customer used the guardrails and content filters we have built into our products" ([Microsoft](https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/), 7 September 2023). That is the locked door again: cover, conditional on a control. Google and Anthropic made similar commitments in late 2023, and like Microsoft's they cover copyright claims, not what an agent does.

The closer examples are about performance. Intercom offers "up to $1M of your money back" for its Fin agent under stated conditions, and a programme that pays if Fin does not reach "at least a resolution rate of 65%" ([Intercom](https://intercom.help/fin4all/en/articles/11645601-what-is-the-fin-guarantee), 24 June 2025). ElevenLabs announced on 12 February 2026 a policy backed by the AIUC-1 standard, so that "these AI voice agents - and their actions - can now be insured, just like any other employee" ([ElevenLabs](https://elevenlabs.io/blog/aiuc-announcement)). Munich Re offers vendors "performance warranties" that "enable you to indemnify your clients for their financial losses". None of these is yet a payout per row of a behaviour policy. Each is a step towards one, and the third article in this series is about what the vendor's share of a row should be.

## What comes next

This article defines what would be underwritten. The series continues with the questions it leaves:

1. **Who can underwrite an agent behaviour policy today, and what does that look like?** A research brief, starting from the companies in [underwriting the agent economy, reviewed](underwriting-the-agent-economy-reviewed.md), which already sell AI agent cover, and asking each what it would need to price per row.
2. **What should the vendors of agents cover themselves?** What exists, and what a vendor's share of a row would look like.
3. **The formula as a vault.** The rows, the limits, the factors and the claim rule as data, with a page that computes the premium for your own agent, so the formula can be argued with in numbers rather than in words. It is now [vault m1wbrefr](the-vendors-layer.md#vault), with a calculator.

## What this does not claim

- **The numbers are illustrative.** Every limit, base rate and factor in the worked example is mine, chosen to show the shape; none is fitted to loss data, and an underwriter would set them differently.
- **No insurer has agreed to this.** It is a definition of what we would like to have underwritten, not a product anyone sells.
- **The formula is a sketch.** Real controls interact, losses correlate across agents that share a model, and a fleet needs an aggregate limit; a multiplier per control is the simplest form, not the right one.
- **Certification of runtimes does not exist yet in this form.** Which body would certify a runtime, and against what, is open.
- **The Licence to Operate vault is a simulation.** Its replies are scripted and its numbers are in credits; it shows the mechanism, not a price.
- **The comparisons with other insurance are by analogy.** The sources for how motor, health and home insurers price are below, and each works under its own rules and regulators.

If you underwrite, or would like to underwrite, the risk of one agent at a time, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 28 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine.

The insurance framing, the one-to-one mapping, the deterministic formula, starting from the maximum, the runtime and the vendors' share are from the memo. The six-step formula, the worked example and its numbers are this site's agent's, written to make the memo's argument checkable; the factors are illustrative.

On this site and its neighbours:

- The worked example: [the data file](https://newsroom.sgit.ai/articles/data/a-payout-for-every-row__worked-example.json), computed by `admin/notes/2026-10-28__underwriting-abp/premium.py` in this site's repository; every figure in this article's tables and its premium walk comes from it.
- The [Licence to Operate vault](https://sgit.ai/demos/vaults/licence-to-operate/index.html) on sgit.ai, vault `posrhzp3`, read from its published page on 28 October 2026 for the 12, 4 and 8 capabilities, the three replies and their costs and the quoted banner, and cloned with sgit 0.26.11 the same day for the policy file `policies/concierge/concierge-sim-2026-09-03.json`: the bands, the ceiling, the pool, the 10% reserve, the 20-record exclusion and the two quoted lines.
- RiskMandate's [licence to operate](https://riskmandate.ai/licence-to-operate.html) and [insurable](https://riskmandate.ai/insurance.html) pages, read on 28 October 2026 (site v1.39.0), for the four facts of a licence and the two quoted lines.
- [An agent that may only chat](an-agent-that-may-only-chat.md) for the 3 of 12 and 12 of 12; [what can your agent reach?](what-can-your-agent-reach.md), [governs, enforces, attests](governs-enforces-attests.md), [approved business mandates](approved-business-mandates.md), [the RiskMandate roadmap](the-riskmandate-roadmap.md) and [underwriting the agent economy, reviewed](underwriting-the-agent-economy-reviewed.md).

Outside sources, each linked where it is used and read on 28 October 2026 by a research agent of this site, which fetched every page quoted: Howden on single-article limits (9 January 2025) and on black boxes (1 September 2025); MoneySuperMarket on locks (updated 3 September 2026); ingenie's own page; Coalition (3 August 2021); Munich Re's aiSure pages (undated); Fortune on AIUC (23 July 2025); Microsoft (7 September 2023); Intercom (24 June 2025); ElevenLabs (12 February 2026). The health insurance paragraph is a paraphrase of AXA Health's and Bupa's descriptions of their underwriting, which could not be fetched directly, and quotes neither. The research notes, with what could and could not be verified, are `admin/notes/2026-10-28__underwriting-abp/research-01.md`.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#a-payout-for-every-row)

### Builds on

- [Who carries the risk: the companies already insuring AI agents, the parts an insurer for agent behaviour policies would need, and why the first one starts as a managing agent on someone else's capital](who-carries-the-risk.md) Who already insures AI agents, the four parts an insurer for behaviour policies needs, why capital matters, and why the first one starts as a managing agent.
- [A proposed roadmap for RiskMandate: policies, understand, risk acceptance, contain, manage and insure, a spectrum of trust we would walk with each customer](the-riskmandate-roadmap.md) A proposed strategy for RiskMandate, a spectrum of trust: policies, understand, risk acceptance, contain, manage, insure.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Approved business mandates: companies already have behaviour policies, and RiskMandate's job is to turn them into tested controls and keep them true as the deployment changes](approved-business-mandates.md) Companies already have behaviour policies: RiskMandate's job is to turn approved business mandates into tested controls and keep them true.
- [An agent that may only chat: RM-CHAT-ONLY, the smallest behaviour policy, tested in 96 Claude Code runs and 11 claude.ai chats by an agent on my computer at home, driven from my phone](an-agent-that-may-only-chat.md) RM-CHAT-ONLY, the smallest behaviour policy, tested in 96 Claude Code runs and 11 claude.ai chats, and the fallback drill that shows what a hook is for.
- [Underwriting the agent economy, reviewed: the cliff notes of the AI insurance stack, the companies already selling AI agent cover, and what agent behaviour policies add to it](underwriting-the-agent-economy-reviewed.md) A review of the AI insurance stack blueprint, the companies selling agent cover, and what agent behaviour policies add to it.
- [The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product](the-vendors-layer.md) Each row of an agent behaviour policy gets a vendor's share, carried when the vendor's conditions held; contracts cap at a year's fees, Europe moves the line.

### Continued by

- [Where to build the agent insurer: underwrite in London, sell into the US, carry the risk in Bermuda, raise capital in the Gulf, and about £4 million to start, with the capital following from the limits sold](where-to-build-the-agent-insurer.md) Underwrite in London, sell into the US and EU, carry the risk in Bermuda, raise capital in the Gulf; about £4 million to start.
- [The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product](the-vendors-layer.md) Each row of an agent behaviour policy gets a vendor's share, carried when the vendor's conditions held; contracts cap at a year's fees, Europe moves the line.
- [Who carries the risk: the companies already insuring AI agents, the parts an insurer for agent behaviour policies would need, and why the first one starts as a managing agent on someone else's capital](who-carries-the-risk.md) Who already insures AI agents, the four parts an insurer for behaviour policies needs, why capital matters, and why the first one starts as a managing agent.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 315 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=315)

**Posting this article on LinkedIn?** The cover is [a-payout-for-every-row.jpg](banners/a-payout-for-every-row.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-payout-for-every-row.html)*
