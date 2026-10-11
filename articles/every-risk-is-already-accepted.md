# Every risk is already accepted. The only question is by whom, and for how long., sgit.ai

> A foundation article on risk acceptance, for readers who have never met the idea. A risk exists the moment the exposure does, so an organisation is always carrying it; the only open questions are who has accepted it, and until when. There is no deny button, only three doors (accept for a stated interval, fund the work, or fix it), and silence escalates. The interval is the decision, from four hours, which is an incident, to six months, which is a named decision to wait. Accepted is not the same as acceptable, which matters because the EU AI Act requires providers of high-risk AI systems to have residual risk judged acceptable, and never defines the word. Every risk has a holder, every holder has a boss, and every path ends at the board. Every risk is established by facts and ended by facts, from the board down to the configuration file, which is what closes the gap between a register and reality. The article walks one invented risk through six weeks, argues that each material risk deserves a vault of its own as its evidence pack, explains why executives resist the model, and shows why it fits alongside every GRC platform rather than replacing one. A business plan for a company that runs this loop is published with it.

*Source: <https://newsroom.sgit.ai/articles/every-risk-is-already-accepted.html> · sgit.ai v0.7.61 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Every risk is already accepted. The only question is by whom, and for how long.

# Every risk is already accepted. The only question is by whom, and for how long.

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-09-24 · [article v1.1.1, 3 versions](versions/every-risk-is-already-accepted.md) · [sgit.ai v0.6.5](https://sgit.ai/admin/versions.md) · riskrisk-acceptancegovernancegrcfractal-semantic-graphseu-ai-actarticle

***Abstract:** A foundation article on risk acceptance, for readers who have never met the idea. A risk exists the moment the exposure does, so an organisation is always carrying it; the only open questions are who has accepted it, and until when. There is no deny button, only three doors (accept for a stated interval, fund the work, or fix it), and silence escalates. The interval is the decision, from four hours, which is an incident, to six months, which is a named decision to wait. Accepted is not the same as acceptable, which matters because the EU AI Act requires providers of high-risk AI systems to have residual risk judged acceptable, and never defines the word. Every risk has a holder, every holder has a boss, and every path ends at the board. Every risk is established by facts and ended by facts, from the board down to the configuration file, which is what closes the gap between a register and reality. The article walks one invented risk through six weeks, argues that each material risk deserves a vault of its own as its evidence pack, explains why executives resist the model, and shows why it fits alongside every GRC platform rather than replacing one. A business plan for a company that runs this loop is published with it.*

The acceptance loop. Establish the risk on facts, place it with a holder and the chain above them, have the holder accept it for an interval with an action, and when the interval ends, accept again, fund or fix. Silence is not a door: it escalates to the holder's boss.

Here is the claim, stated so it can be wrong. **Every risk your organisation has is already accepted. Somebody is carrying it, today, whether or not anybody signed for it. The only questions worth asking are who has accepted it, and until when.** Most risk management avoids those two questions. This article is about what happens when you stop avoiding them, and it assumes you have never heard any of this before.

## In short

- **A risk exists the moment the exposure does.** Nobody decides whether to accept it. The organisation is carrying it from the start, signed for or not.
- **There is no deny button.** You cannot vote a fact out of existence, and a register that lets you reject a risk lets you pretend.
- **There are three doors: accept it for a stated interval, fund the work that reduces it, or fix it.** Silence is not a fourth door. A risk nobody accepts is treated as critical and rolls up to the holder's boss.
- **The interval is the decision.** Accepting for four hours is declaring an incident. Accepting for a month is funding work. Accepting for six months is a named decision to wait.
- **Accepted is not the same as acceptable.** One is an act by a named person on a date. The other is a threshold. The EU AI Act asks for residual risk to be "judged to be acceptable" and never defines the word.
- **Every risk has a boss.** Every risk has a holder, every holder has a boss, and every path ends at the board, computed rather than reported.
- **Risks are fractal.** A board line such as "loss of customer funds" opens into business, operational and technical risks, each with its own holder, down to the configuration file that makes it true.
- **Established by facts, ended by facts.** Every risk names the facts that make it true, and the facts that would end it. That is what closes the gap between a register and reality.
- **Each material risk deserves a vault of its own**: the evidence pack of governance, with its facts, decisions and history, readable by each audience with its own key.
- **Executives resist this, and they are right that it is disruptive.** That resistance is the work, and it is why this is a governance change, not a product feature.
- **It fits alongside every GRC platform.** It works in the gaps they leave. A [business plan for a company that does exactly this](https://sgit.ai/demos/vaults/risk-acceptance/index.md) is published with this article.

## A risk you are already carrying

Take one ordinary example. A company lets an AI agent run database changes in production, because it makes deployments faster. The agent's database role can write to the ledger. Some ledger migrations cannot be rolled back.

From the moment that role was created, the company has been carrying a risk: the agent can change production in ways nobody can undo. Nobody decided to accept it. Nobody decided not to. It is simply there, and it will stay there until somebody changes one of the facts that make it true.

Now look at how most organisations record it, if they record it at all: a row in a register. "Change risk in automated deployment. Owner: Technology. Rating: Medium. Status: Open. Next review: the risk committee in December. Evidence: none attached." Every field is reasonable. None of them says who has accepted the risk, until when, or what will happen if nothing changes.

## There is no deny button

The first principle sounds obvious and changes everything: **you cannot deny a risk.** As [risks.sgit.ai](https://risks.sgit.ai/) puts it, "You cannot vote a fact out of existence." If the agent's role can write to the ledger, no meeting can decide otherwise. You can change the role, or accept that it can.

So the only real choices are three, each with a name against it:

1. **Accept it**, personally, for a stated interval.
2. **Fund** the work that will reduce it.
3. **Fix** it, so that the facts that make it true stop holding.

Deferral is not a fourth door. "Revisit next quarter" is not a decision, and silence is not a decision anybody can underwrite. In this model, **unaccepted is critical**: a risk nobody has accepted rests on whoever is nearest, and it rolls upward to their boss, and then to theirs, until somebody signs.

## The interval is the decision

Accepting a risk is never open-ended. Every acceptance is for an interval, and the interval is not a detail of the decision. It *is* the decision, because each length names a different response. This is the ladder as published on risks.sgit.ai:

| Interval | What it means |
|---|---|
| 1 hour | "I need more data." Go and get it, then decide again. |
| 4 hours | A priority-one incident. Trigger incident response. |
| 1 to 2 days | A smaller incident. |
| 1 to 2 weeks | A funded project for a team that already exists. |
| 1 month | Assemble and fund. The default, set deliberately just above the incident line. |
| 6 months | Do nothing, and review it then. It costs nothing, and it is legitimate, with a name on it. |

Two things follow. First, **a short acceptance is an incident.** If the honest answer to "how long can we live with this?" is four hours, the organisation is not managing a risk any more; it is responding to one. Second, **a funded acceptance has a natural length**: the length of the project that will end it.

When the interval ends, nothing silently continues. The same decision comes back to the same desk, with whatever evidence has arrived since. Accept again, fund or fix. If nobody does anything, the risk goes one level up, where the choice is the same.

## Accepted is not acceptable

Most registers blur two different questions.

Two questions, four states. Accepted is an act by a named person at a dated moment. Acceptable is a threshold. The dangerous state is a risk over the line that nobody has signed for.

**Accepted** is an act: a named person, on a date, for an interval. **Acceptable** is a threshold: in [RiskMandate.ai](https://riskmandate.ai/acceptable.html)'s words, "the moment that the business is happy to stop funding remediation activities". A risk can be accepted and not yet acceptable: somebody has signed for it, for a short interval, while the fix is funded. A risk can be acceptable and not accepted: probably harmless, and exactly where a register quietly goes stale. And a risk can be neither, which is the dangerous one.

This distinction is now written into law for one class of organisation. Article 9(5) of the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) requires providers of high-risk AI systems to adopt risk management measures "such that the relevant residual risk associated with each hazard, as well as the overall residual risk of the high-risk AI systems is judged to be acceptable" ([text of Article 9](https://artificialintelligenceact.eu/article/9/)). The Act never defines "acceptable". The duty to make the judgement is imposed, and the standard for making it is not supplied. An organisation has to draw its own line, and be able to show that it did.

Our position is that this is not the end of the question but the beginning. Being over or under the line does not remove the need for somebody to accept what is actually being carried. **Acceptance has to happen every time a risk exists. The only debate is for how long, and for what action.**

## Every risk has a boss

Every risk has a holder: the person whose job it is to accept, fund or fix it. Every holder has a boss, and that boss has a boss, up to the board. So every risk has a chain, and every chain ends at the board.

The role risk map in the Risk Graph Explorer vault. Every risk is assigned to somebody, and every risk reaches the board. The CTO holds 4 and sees 25 pass through; the board has 37 arrive.

The [Risk Graph Explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/views/index.md) vault computes this today. Each role shows what it is **assigned**, meaning its own to deal with, and what arrives **through** it, meaning what the risk graph says must reach it. In the tool's own words: "It arrives because the risk graph says so, not because anybody reports here." No risk is orphaned, and nobody at the top is surprised by something nobody carried up.

The other rule of the chain is that **nobody can accept on anybody else's behalf.** A holder's boss sees the risk arrive, and sees whether it was accepted, until when, and on what evidence. But the acceptance belongs to the person who holds it. When somebody refuses, that is visible too, and it is a finding rather than a failure. As I said in one of the recorded walkthroughs of that vault, "everybody that is going to accept it is going to push back". That pushback is the point.

## From the board to the bytes

A risk at the board is written in the board's language: loss of customer funds, regulatory penalty, loss of licence. That line is real, but it is not something anybody can fix. Underneath it are risks in other languages: the business risk that payments can be corrupted, the operational risk that an agent can change production irreversibly, and the technical risk that the agent's role has write access to the ledger with no approval step.

One risk from the board to the bytes. Each altitude has its own holder and its own words, joined by "leads to" edges, and every altitude points at the facts and evidence beneath it. A register row in a spreadsheet is the top box on its own.

This is what we call a **fractal risk register**, described on [graphs.sgit.ai](https://graphs.sgit.ai/v1/docs/fractal-risk-registers.html): "wherever there is a stakeholder accepting a risk, that entity needs a register." A database administrator's risk translates into the CISO's, the CFO's, the CEO's and the board's, each in that person's own words, joined by named edges rather than retyped. The vocabulary changes at every altitude. The grammar does not: a holder, an interval, the facts that establish it and the facts that end it.

Risk chains in the Risk Graph Explorer vault. Inherent risks on the left rise by causal depth to the corporate register on the right. Click any entry to see what produced it and what it produces.

This is also where [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md) stop being an abstraction. The fractal property is that on one of the links you can jump into another universe with its own rules: from the board's register into security operations, into the database estate, into one configuration file. A vulnerability at the bottom and a revenue obligation at the top are no longer in different tools with a spreadsheet between them.

## Established by facts, ended by facts

The single change that closes the gap between a register and reality is this: **every risk names the facts that make it true, and the facts that would end it.**

In the Risk Graph Explorer, a risk is established by one cited fact, F-5, that the agent can change the production estate. Then, unusually, it carries its own end condition: "Ceases when any of these hold: F-4 reads-only-from, or F-3 absent-from." The risk ships with its own falsification condition. It is not a judgement to be argued down; it is a claim about facts, and when the facts change, the risk ends, with the evidence attached.

That is also what makes disagreement productive. When a holder says "I don't buy that", the conversation becomes which fact is wrong, not whose opinion is louder. And it is what the usual register cannot do: a row typed by a person, reviewed quarterly, connected to nothing, is a record that can be perfectly maintained and entirely wrong.

## One risk, six weeks

Here is the whole loop on the example above, as an invented company, replayed in the [Risk Acceptance Office vault](https://sgit.ai/demos/vaults/risk-acceptance/index.md).

The risk is established on day 0 on two facts, each with its source, and placed with the SRE lead. The platform owner, the CTO, the CEO and the board see it arrive through the chain. On day 1 the SRE lead accepts it for two weeks, with an action: add an approval step to the agent's production writes. On day 15 the acceptance expires. The approval step was not built, because the team was moved onto a release. Nobody renewed it, so it escalates.

Day 15. The two-week acceptance expired with its action undone, so the risk rolled up to the platform owner, who must now accept, fund or fix.

The platform owner funds a four-week project and accepts the risk for a month. On day 24 the risk materialises: the agent applies a migration that cannot be rolled back, and settlement stalls. The platform owner accepts for four hours, which is an incident response by definition, suspends the agent and reconciles the ledger. The incident's timeline becomes a new fact in the risk's own record. On day 41 the approval step is merged, one of the facts that the risk named as ending it now holds, and on day 42 it ceases, on evidence.

Day 42. The fact that ends the risk holds, with its source, and the risk ceases. The facts that established it are still true; the one that ends it is now true as well.

Now look at the register row at the same moment.

The same day, two views. The register row still says "Open until the committee on 12 December", with no evidence attached. The risk's own record says who accepted it, until when, what happened, and why it ended.

That difference is the air gap. Nothing in the row is wrong. It just never learned that the risk was accepted twice, expired once, escalated, funded, materialised as an incident, and ended.

## A vault per risk

Every material risk deserves a place to keep its own story: the facts and where they came from, the controls and their states, every acceptance with its interval and action, every escalation, every incident, and the evidence that ended it. That is the evidence pack of governance, and today it is scattered across emails, spreadsheets, screenshots and meetings nobody minuted.

A vault is a natural home for it. It keeps every version of every fact and decision, proves the record was not altered afterwards, travels as one read key, and stays readable if the organisation changes its tools. The holder writes to it. Their chain up to the board gets a read key. The auditor and the insurer get their own keys when they need them, and nothing else. A corporate risk's vault can link to the vaults of the business, operational and technical risks beneath it, which makes the register fractal in storage as well as in meaning.

This is a proposal, not yet a practice: the published method describes fractal registers and a chain to the board, and the idea of a vault per material risk is new here.

## Twins, and where this goes

On [twins.sgit.ai](https://twins.sgit.ai/actors/index.html), every action that changes the risk graph, including accepting a risk, is performed by a twin acting for a person, connected either to that person or to an agent working for them. That makes acceptance "the most evidenced act rather than the least". Twins also make risk testable: an organisation's risks, controls and decisions modelled well enough to simulate what happens when one of them changes. And risks.sgit.ai names the air gap honestly: "A twin not connected to reality is a tracked air gap."

Both ideas are designs, and the twins site says so plainly: "None of this is built." I include them because they show where the model leads. Risk systems that stay at the level of a register row will always be disconnected from events. A model in which risks are established on facts, facts come from twins of the real systems, and acceptances are recorded as events, is one where the register and reality can finally be the same thing.

## Why this is hard, and why people resist

I want to be honest about what happened when we took this to market. With [RiskMandate.ai](https://riskmandate.ai/) we approached risk acceptance from the angle of AI agents and insurability, and it was hard for two reasons.

The first is ownership. Risk acceptance is a governance matter. It has to come from the people who own governance, risk and compliance, and from the board. Sold as a feature of a security or AI product, it lands with people who do not own it.

The second is resistance, and it is rational. Some of the people we worked with did not want to give their risk owners an acceptance workflow at all, because they understood, instinctively or explicitly, that it would be a very disruptive change. Today many executives accept very little, or accept only what has already been judged acceptable. Asking them to accept, personally and for a stated interval, everything they actually hold changes their job. risks.sgit.ai names the same tension: "No-deny is the strongest idea here and the hardest to sell. Removing the deny button removes the thing most executives use a register for." It also names how the model can be defeated without anybody arguing with it: "interval inflation, where everything is accepted for six months".

None of that makes the model wrong. It makes it a change programme, and change programmes are run by people, one business unit at a time.

## It fits alongside every GRC platform

Nothing here replaces the platforms organisations already use for governance, risk and compliance. They solve real problems: the register, the workflow, the frameworks, the reporting. What they leave are gaps: between the row and the facts, between "accepted" and a clock, between a function and a named person, between one coarse row and the forty things underneath it.

This model operates in those gaps. It reads the register from the platform, and writes back what the platform lacks: who accepted, until when, what happens at expiry, and a link to the evidence. Which is why I think the GRC vendors should be sponsoring and integrating with this work rather than competing with it: it makes their platforms more valuable and harder to leave.

## What exists today, and what does not

**Exists and runs:** the published model on [risks.sgit.ai](https://risks.sgit.ai/), the acceptance and licence-to-operate work on [RiskMandate.ai](https://riskmandate.ai/), fractal risk registers on [graphs.sgit.ai](https://graphs.sgit.ai/v1/docs/fractal-risk-registers.html), the [Risk Graph Explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/index.md) vault, which computes the chain to the board, and the [Risk Acceptance Office](https://sgit.ai/demos/vaults/risk-acceptance/index.md) vault, which replays one risk's acceptance loop with a hash-chained decision record verified in your browser.

**Does not exist yet:** an engine that records acceptances, runs the clocks and fires at expiry. risks.sgit.ai states plainly, in capitals, that essentially none of its model is implemented in code. The published material also leaves open exactly what happens at expiry, whether an unaccepted risk rolls up automatically or waits, and which of two published ladders is canonical. The business plan takes a position on each, and says so.

## For somebody to build

I think this should be a company, and possibly several. Its work is the hard part: establishing risks on facts, connecting them to the people who hold them, running the clocks, keeping the evidence, and helping executives through the change. The [Risk Acceptance Office](https://sgit.ai/demos/vaults/risk-acceptance/index.md) vault holds a business plan for it: the operating model, working in the gaps of the GRC platform, services and prices as hypotheses, a calculator, go-to-market that starts from the resistance rather than around it, the first ninety days, the risks and the open questions. It sits with the other [business plans published for founders](https://sgit.ai/startups/business-plans.md).

The pitch is two questions, asked of any register: **who has accepted this, and until when?**

## Sources

- [risks.sgit.ai, the model, the ladder and the inventory of what is built](https://risks.sgit.ai/)
- [risks.sgit.ai, Accepted is not acceptable](https://risks.sgit.ai/acceptable/)
- [RiskMandate.ai, Accepted is not acceptable](https://riskmandate.ai/acceptable.html)
- [graphs.sgit.ai, Fractal Risk Registers](https://graphs.sgit.ai/v1/docs/fractal-risk-registers.html)
- [twins.sgit.ai, twins as actors](https://twins.sgit.ai/actors/index.html)
- [Regulation (EU) 2024/1689, the AI Act, on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Article 9 of the AI Act, risk management system](https://artificialintelligenceact.eu/article/9/)
- [The Risk Graph Explorer, the seven views](https://sgit.ai/demos/vaults/risk-graph-explorer/views/index.md)
- [The Risk Acceptance Office vault](https://sgit.ai/demos/vaults/risk-acceptance/index.md)

*© 2026 Dinis Cruz. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#every-risk-is-already-accepted)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.

### Continued by

- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [Who are you protecting against? Draw the security line where the attacker is, not above it](who-are-you-protecting-against.md) Before deciding how secure to be, name the attacker: a six-tier ladder, an air-gapped Mac mini read against it, and eight startups drawing their line.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md) A global GitHub Actions outage read the way aviation reads an incident: independent inquiry, near-miss reporting, second and third stories, vaults for the evidence.
- [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](send-an-agent-not-a-spreadsheet.md) Due diligence never scaled because it was a form; a buyer can now send an agent into a vendor's environment and read what the code and the practices are.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 13 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=13)

**Posting this article on LinkedIn?** The cover is [every-risk-is-already-accepted.jpg](banners/every-risk-is-already-accepted.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/every-risk-is-already-accepted.html)*
