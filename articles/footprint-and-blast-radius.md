# Footprint and blast radius: what the agent actually did, and what it would have cost, sgit.ai

> RiskMandate's Agent Behaviour Policy is written before an agent runs, in four words: reach, mandate, gap and barriers. This article proposes two more. The footprint is what the agent actually did, read afterwards from logs, traffic and vault history, with nobody inline and no production access needed. Compared with the mandate it gives two kinds of finding: footprint in the gap, which is a near miss, and dormant mandate, which is a check that never ran or a mandate that asked for too much. Read on its own it gives the mandate as practised, a policy reverse-engineered from evidence. Blast radius is the measure that goes with any of them: what it would cost the business if a row of the reach were used in full, today. The same footprint can carry a different blast radius on different days, which is why a near miss on an empty table and an incident on a full one are the same row in the record. One figure carries the whole argument: the gap as a map, each row shaded by what it would cost and marked if there is no way back.

*Source: <https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Footprint and blast radius: what the agent actually did, and what it would have cost

# Footprint and blast radius: what the agent actually did, and what it would have cost

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-02 · updated 2026-10-02 · [article v1.1.1, 3 versions](versions/footprint-and-blast-radius.md) · [sgit.ai v0.6.36](https://sgit.ai/admin/versions.md) · agentsagent-behaviour-policyriskmandatefootprintblast-radiusrisk-managementlogsconnector-twinvaultsarticle

***Abstract:** RiskMandate's Agent Behaviour Policy is written before an agent runs, in four words: reach, mandate, gap and barriers. This article proposes two more. The footprint is what the agent actually did, read afterwards from logs, traffic and vault history, with nobody inline and no production access needed. Compared with the mandate it gives two kinds of finding: footprint in the gap, which is a near miss, and dormant mandate, which is a check that never ran or a mandate that asked for too much. Read on its own it gives the mandate as practised, a policy reverse-engineered from evidence. Blast radius is the measure that goes with any of them: what it would cost the business if a row of the reach were used in full, today. The same footprint can carry a different blast radius on different days, which is why a near miss on an empty table and an incident on a full one are the same row in the record. One figure carries the whole argument: the gap as a map, each row shaded by what it would cost and marked if there is no way back.*

The gap as a map, for an illustrative inbox agent. Every row is something the agent can reach. The bands say whether a row is in the mandate, and whether the footprint has touched it. The barrier column is RiskMandate's four kinds. The shading is blast radius, what it would cost if the row were used in full today, hatched where there is no way back. The red dots are footprint in the gap, which is a near miss. The row to fix first is high blast radius, irreversible, with nothing but an expectation in front of it, whether or not the footprint has reached it yet. Placeholder capabilities and counts.

**A note on what this is.** A proposal to extend the vocabulary of [RiskMandate's Agent Behaviour Policy](https://riskmandate.ai/abp.html), written on sgit.ai because the evidence for it lives here: the connector twin, the vaults' own history, and a team of agents whose policies we can hold up against what they did. RiskMandate's four words are reach, mandate, gap and barriers. Earlier pages on both sites, including the [ultimate insider](ultimate-insider-three-collisions.md) talk proposal, called the reach the grant and the gap the delta; they are the same things. The two words proposed here are new to the policy, not to the industry. A companion [brief to the RiskMandate team](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.md) carries the schema changes. **Status, 2 October 2026:** the founders are still reviewing this proposal, and the best way to make it happen will be decided with the RiskMandate team. Until then it is an idea published on sgit.ai, where the vaults and the evidence live, not a change to the policy.

## In short

- **The policy is written before the agent runs.** Reach is what it can do, measured. Mandate is what you asked it to do. The gap is the difference, in both directions. Barriers are what stands in the way of each row of the gap, typed as a boundary, a setting, an expectation or nothing, and only a boundary is a control.
- **Footprint is what it actually did, read afterwards.** From the connector's audit log, the model's tool-call log, the vault's commit history, the append lane's record, or a connector twin's replay. Nothing sits inline. Nobody needs production access. It accumulates, so some of what it shows only appears over weeks.
- **Footprint in the gap is a near miss.** The agent went somewhere you did not ask it to go and nothing stopped it. Each one resolves one of two ways: add the row to the mandate, because the mandate was incomplete, or put a boundary in front of it.
- **Dormant mandate is a finding too.** A row you asked for that the footprint never shows. The mandate asked for too much, or a check you were relying on never ran, or the agent cannot do it and the reach inventory missed the shortfall.
- **Read alone, the footprint is the mandate as practised.** For an agent that has no written policy, it is the fastest honest way to write one: here is what your agent does, now tell me which rows you meant.
- **Blast radius is the measure, not another set.** It is what it would cost the business if a row were used in full, today. It is defined over the reach, because whoever takes the agent over inherits its reach and ignores its mandate. It changes with context while the row does not. And it has a second axis the industry usually leaves out: whether there is a way back.
- **The gap plus blast radius is the risk.** The gap is exposure. Blast radius is impact. The person who accepts a gap is accepting its blast radius, and until now the policy did not say what that was.

## Four words, written before anything happens

RiskMandate's policy starts from a simple observation that keeps proving true: what an agent can do and what it was asked to do are different lists, and almost nobody has written down either. So the method measures the **reach** from the deployment itself, the account, the connectors, the credentials, the tools. It elicits the **mandate** from the owner, in minutes, in their words. It derives the **gap**, which runs in both directions: excess, where the agent can and you did not ask, and shortfall, where you asked and it cannot. And for every row of the excess it records the **barrier**, typed honestly. A boundary is enforced above the agent's reach, so it cannot flip it. A setting is a switch the agent's own account could flip. An expectation is a rule in prose, enforced by nobody. None is none. Only the boundary is a control, and most of what organisations call controls turn out to be expectations once they are typed. The [Kit Bag](https://sgit.ai/demos/vaults/kit-bag/index.md) plan did this for a browser extension before any code was written and found thirteen rows in the gap, four of them stopped by the platform and the rest by nothing but the code as written.

All four of those words describe the agent before it runs. That is deliberate and it is the method's strength: the point is to decide in advance, so that the decision exists before the incident does. But it leaves out the one thing that an incident review always asks for first, which is what actually happened.

## The fifth set: footprint

The footprint is the set of things the agent actually did, in a period, read from the record afterwards. It is the same kind of thing as the reach and the mandate, a list of rows, which is what makes the comparisons below possible. It is different in one way that matters: it is evidence, not a decision.

Where does it come from? From wherever the agent's actions leave a trace, and there are more of those than people expect:

- The connector's own audit log. Google Workspace, Microsoft 365 and the rest record what an account did, and an agent runs as an account.
- The model provider's record of tool calls, where the deployment keeps it.
- A [connector twin](connector-twin-before-you-deploy-an-agent.md), which records what the agent saw and asked for at the connector and can replay it. It was argued for as a deployment requirement; it is also the cleanest footprint recorder there is, because it sits exactly where the actions cross the line.
- A vault's commit history. Every agent on this site that works in a vault leaves a signed, versioned record of every file it touched, and the [append lanes](https://sgit.ai/api/append-lanes.md) record every message that went down them.
- The agent's own messages. Agents here talk to each other in files, and a file is a trace.

Three properties follow from reading rather than intercepting. It is **passive**: nothing sits inline, nothing adds latency, nothing can break the agent by being there. It needs **no production access**: a copy of the logs, or a read key to the vault, is enough, which is why an outside reviewer can do it. And it **accumulates over time**: the first week's footprint says little, the twelfth week's says a great deal, and some findings only exist at the twelfth week.

## What the footprint reveals

Put the footprint beside the mandate and the reach, and four things fall out.

**Footprint in the gap.** The agent did something that is within its reach and outside its mandate, and whatever barrier was there did not stop it, because it was an expectation or nothing. In the safety disciplines this is a near miss, and it is the most valuable kind of finding there is, because it arrives before the damage. It resolves one of two ways, and the owner decides which. Either the mandate was incomplete, which is normal for a new agent, and the row joins the mandate. Or the agent should not have gone there, and the row gets a boundary. Either way the gap shrinks, and the policy is more honest than it was.

**Dormant mandate.** A row the owner asked for that the footprint never shows. This one has three possible causes, and telling them apart is the review. The mandate may be over-stated: the owner asked for things the job does not need, which is how permissions creep in the first place, and the row should go. Or a check the owner was relying on never ran: the mandate said "escalate to a human when a payment is mentioned", fourteen payment threads went past, and the escalation row is empty. That is a control that exists on paper only, and finding it from the logs is better than finding it from the incident. Or the agent cannot do it at all, and the shortfall side of the gap missed it. One caveat that the method has to carry: some rows are supposed to be dormant. "May escalate" should rarely fire. So each mandate row wants a hint of how often the owner expects to see it, always, sometimes, rarely, hopefully never, and the comparison is against that.

**Footprint outside the reach.** This should be impossible by construction, so when it appears, the reach inventory is wrong, and that is a finding about the measurement rather than the agent.

**Barrier hits.** Attempts that a boundary stopped are also in the record, and they are the footprint of the barriers. A boundary that stops something every week has earned its place. An expectation, by definition, has no hits, because nothing was there to record the stop.

The mandate as written beside the mandate as practised, for the same illustrative agent. Four rows used, two dormant, two excursions into the gap. The left side is a set of decisions made in advance. The right side is evidence. The owner decides what each difference means.

## The mandate as practised

Turn the comparison round and it becomes a way to write a policy for an agent that has none, which is most agents. Read the footprint for a month and you have the mandate as practised: the rows the agent actually uses, in order of frequency, with the near misses marked. Put that in front of the owner and the conversation is a different one from the usual elicitation. Not "what do you want this agent to do?", which produces a wish list, but "here is what your agent does; which of these did you mean, and which of these worries you?" The written mandate that comes out of that is grounded in evidence from the first draft.

This matters most for agents at the genesis end of the strip, built in an afternoon and running for months, where nobody wrote anything down because the thing was an experiment until it was not. The [Custom UIs](custom-uis-are-not-the-exception.md) article described a team of ten agents that grew that way in eight days. Six of them have a written policy; the footprint is how the other four get one without anyone having to remember what they were for.

## Blast radius: the measure, not a sixth set

Reach, mandate, gap, barriers and footprint are all lists of rows. Blast radius is not. It is a measure that attaches to a row, or to a set of rows: what it would cost the business if that row were used in full, today.

The term comes from explosives and the cloud operators made it ordinary. AWS uses it for the scope of a failure, the chaos engineering people for the scope of an experiment, and the identity vendors for the scope of a credential. It needs no definition fight, which is why it is the right word. In the policy it should mean one narrow thing: the impact if the agent's reach were exercised, by the agent or by whoever controls it.

That last clause is the reason to define blast radius over the reach and not over the mandate. An attacker who takes an agent over, through a prompt injection, a poisoned document, a compromised skill, inherits the agent's reach and ignores its mandate entirely. The [ultimate insider](ultimate-insider-three-collisions.md) has a blast radius, and it is the reach. The mandate tells you what you hoped for. The reach tells you what you are exposed to.

Three things make the measure useful rather than decorative.

**It is about the business, not the system.** "Can delete the database" is a row of the reach. Its blast radius is not "the database"; it is what the business loses when the database is gone, which depends entirely on what is in it, who depends on it, and whether there is a copy. The same row on a staging database full of test data and on the production ledger the week before the audit has the same name and a completely different blast radius. This is why blast radius connects the policy to the risk register rather than to the infrastructure diagram: it is the impact column, and the person who owns the impact is the person who fills it in.

**It has a before reading and an after reading.** Potential blast radius is computed from the reach, before the agent runs: the worst the deployment could do. Realised blast radius is what the footprint actually touched, read against the context at the time. The first is what you accept when you deploy. The second is what you learn when you review. They should converge as the policy matures, and when they do not, the gap is where the surprises are.

**It has a second axis: whether there is a way back.** The industry's blast radius is usually a scope, how far the damage spreads. For agents the more useful second question is whether the damage can be undone. Sending an email as the owner cannot be unsent. Permanently deleting a message is, as the platform's own documentation says, permanent. Forwarding mail to an outside address is quietly reversible for the mailbox and not at all for the mail that already left. Writing to an append-only vault with history can be rolled back in a minute. Two rows with the same scope and different reversibility are not the same risk, and the policy should say so.

## Same footprint, different blast radius

The property that took longest to see is that the footprint is fixed and the blast radius is not. An action, once taken, is a row in the record and stays there. What it would have cost depends on the moment.

Same footprint, different blast radius. An agent drops a staging table three times over two months. The row in the footprint is identical each time. On day three the table was empty and nobody noticed. On day twenty-two it held a week of test data and somebody shrugged. On day forty-one it held six weeks of real records and it was the incident. The footprint lets the review say: this is not the first time. Illustrative.

Picture an agent with a cleanup step that drops a staging table. The first time it runs, the table is nearly empty, and nobody notices. The second time, there is a week of test data in it, and somebody shrugs. The third time, six weeks of real records have been landing in that table because another process changed, and it is the incident. The action is the same row, three times. If the footprint was being read, the review on day forty-one can say something that is otherwise impossible to say: this is not the first time. The same row is in the footprint on day three and day twenty-two. It was a near miss twice before the table had anything in it.

That sentence is worth the whole method. It turns the incident from a surprise into the third occurrence of a known pattern, and it means the near miss could have been caught at the first occurrence, when it cost nothing, if anyone had been looking at the footprint against the gap. The safety disciplines learned this a long time ago: the incidents and the near misses are the same events with different luck, and the organisations that get safer are the ones that review the near misses. The footprint is how you get near misses for agents without waiting for the luck to run out.

## What the cloud already does, and what it cannot

None of the comparison idea is new, and the article would be dishonest to pretend otherwise. The cloud identity tooling has been comparing permissions granted with permissions used for years. [AWS IAM Access Analyzer](https://aws.amazon.com/about-aws/whats-new/2023/11/iam-access-analyzer-inspecting-unused-access) added unused-access findings in November 2023 and, from [June 2024](https://aws.amazon.com/about-aws/whats-new/2024/06/aws-iam-access-analyzer-refine-unused-access/), recommends a refined policy from the access activity. Google Cloud's [role recommendations](https://cloud.google.com/iam/docs/recommender-overview) compare a principal's permissions with those used in the last ninety days and will not recommend removing one that was used. Microsoft Entra's [Permission Creep Index](https://learn.microsoft.com/en-us/entra/permissions-management/overview) scores the difference between permissions granted and permissions exercised, weighted by how much damage the permissions could do, which is a blast radius over the grant, and Microsoft's own [report](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/2023-state-of-cloud-permissions-risks-report-now-published/1061397) on it found workload identities using under five per cent of what they were granted. These are the footprint against the reach, done at scale, and anyone deploying agents on a cloud should turn them on.

What they cannot do is the other half, because a permission set carries no statement of intent. There is no mandate in an IAM policy, so there is no such thing as a dormant mandate, no "you asked for a check and it never ran", no near miss in the sense of "the agent went where you did not mean it to", only "the identity used a permission". The owner's intent is the thing the Agent Behaviour Policy adds, and once it exists the footprint can be read against it. That is the whole proposal: take a comparison the cloud already makes and give it the one input it never had.

## What vaults change

This site is about encrypted vaults, so it is fair to ask what they have to do with any of this. Two things, and they are different.

The first is that a vault is a footprint recorder by construction. Every commit is signed, versioned and append-only; every message down an append lane is recorded with its token and its time; a read key lets a reviewer read all of that without touching anything. An agent that works in a vault leaves a footprint whether or not anyone intended to collect one, and a reviewer can read it from outside production with a key that cannot write. The connector twin does the same for the connectors, which is where most agents' reach actually lives.

The second is reversibility, which is the axis the industry's blast radius leaves out. Barriers shrink the reach. Containment and reversibility shrink the blast radius, and they are different levers. A read key caps the blast radius of a row at disclosure. A lane token caps it at queue pollution. Only a vault key reaches the integrity of the record, and even then the history is there to roll back to. Most of what sgit does for agents, once you look at it through this lens, is shrink the irreversible part of the blast radius: the agent can do a great deal, and almost none of it is permanent.

Before, during, after. Reach, mandate, gap and barriers are written before the agent runs. Barriers act during. The footprint is read after, from logs, traffic and vault history, with nothing inline and no production access. Blast radius has a potential reading, from the reach, and a realised reading, from the footprint. Findings go back into the policy.

## Reading our own footprint

The honest status is that this is a proposal with the pieces in place and the worked example still to do. We have ten agents, six with a written policy, all working in vaults, all talking in files, with eight days of commit history and several hundred messages between them. The next step is to read that footprint against the six policies and publish the result: which rows were used, which were dormant, where the footprint went into the gap, and what each finding resolved into. We are building that now, and it will be the second article. The counts will come from the vaults' history and nothing in it will name a contact or quote a message.

What we expect to find, from having watched it happen, is that the near misses are mostly mandate gaps rather than misbehaviour, because the mandates were written quickly for agents that were still changing, and that at least one check we wrote into a policy has never fired. We would rather publish that than claim the method and leave the evidence to the reader's imagination.

## What to add to the policy

The brief to the RiskMandate team asks for five things, in this order of usefulness:

1. **Footprint as a section of the policy**, with a period, a source for each row, and the four derived findings: footprint in the gap, dormant mandate, footprint outside reach, barrier hits.
2. **An expected-use hint on every mandate row**: always, sometimes, rarely, hopefully never. Without it, a dormant row cannot be told from a contingency that was never needed.
3. **Blast radius on every row of the gap**, on a short scale the owner fills in against the business, with the reversible-or-not flag beside it. Five steps is plenty. The figure at the top uses none, low, a bad day, serious, the business.
4. **The mandate as practised** as a view the tooling can produce from a footprint alone, for agents with no written policy yet.
5. **A review cadence**, because the footprint accumulates and the blast radius moves. Monthly for a new agent, quarterly once the potential and the realised readings have converged.

With those, the policy says what the agent can do, what you asked, what stands in the way, what it actually did, and what each of those would cost. That is the risk, written down, in a form a risk owner can accept or refuse, and in a form an auditor can check against the logs without asking anyone for access.

## Threads woven here

- [The ultimate insider](ultimate-insider-three-collisions.md): why an agent's reach, not its mandate, is what an attacker inherits.
- [Every risk is already accepted](every-risk-is-already-accepted.md): the person who accepts the gap is accepting its blast radius, and the policy should say what that is.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md): the footprint recorder at the line where the reach is exercised.
- [Six agents, one inbox](six-agents-one-inbox.md): the first policy on this site, written before the near misses.
- [Custom UIs are not the exception](custom-uis-are-not-the-exception.md): the ten agents whose footprint we will read next.
- Vaults: [Kit Bag](https://sgit.ai/demos/vaults/kit-bag/index.md), a policy written before the code; [Connector Twin](https://sgit.ai/demos/vaults/connector-twin/index.md); [RiskMandate](https://sgit.ai/demos/vaults/risk-mandate/index.md); [Risk acceptance](https://sgit.ai/demos/vaults/risk-acceptance/index.md).
- [RiskMandate.ai](https://riskmandate.ai/) for the policy itself, and the [brief](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.md) that carries this proposal to its team.

*Drafted from a conversation with Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session. The four figures are illustrative: an inbox agent with placeholder capabilities and counts, and a staging table that nobody owns. The industry references were checked against the vendors' own pages on 2 October 2026.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#footprint-and-blast-radius)

### Builds on

- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.

### Continued by

- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [The records ran out: a fresh agent found the shared contract in two MCP calls, and where sgit and RiskMandate fit at the edges](the-records-ran-out.md) A fresh agent found a shared contract in two MCP calls from build records; where the records stopped is exactly where evidence labels and sgit vaults fit.
- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md) A global GitHub Actions outage read the way aviation reads an incident: independent inquiry, near-miss reporting, second and third stories, vaults for the evidence.
- [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](send-an-agent-not-a-spreadsheet.md) Due diligence never scaled because it was a form; a buyer can now send an agent into a vendor's environment and read what the code and the practices are.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 20 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=20)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [footprint-and-blast-radius.jpg](banners/footprint-and-blast-radius.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html)*
