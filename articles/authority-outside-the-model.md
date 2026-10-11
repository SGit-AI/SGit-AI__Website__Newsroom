# Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan, sgit.ai

> On 10 October Satya Nadella published "Models as Insider Risks in the Super Intelligence Era". His argument is that we cannot trace a frontier model's behaviour the way we traced code, so we should treat models the way we treat any powerful insider: identity, least privilege, logs, containment, and controls that sit outside the thing they control. He proposes seven principles: model diversity, observe everything, verifiability, independent controls, independent auditability, containment and incident disclosure. This site and RiskMandate have been making the same case since The ultimate insider on 30 September, and building pieces of it. This is my answer, principle by principle: what we run today, what we have published as design, what we have only argued, and where I would push. It includes an honest maturity table, three things from this week's work (synthetic users that found real bugs, a safety check that stopped our own agents, and the ratio of hope in the policy of the agent that runs this site), and the five things his list leaves out that I think decide whether the principles work, starting with the mandate: observation tells you what an agent did, and only a written mandate tells you whether it was allowed.

*Source: <https://newsroom.sgit.ai/articles/authority-outside-the-model.html> · sgit.ai v0.7.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan

# Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/authority-outside-the-model.md) · [sgit.ai v0.7.41](https://sgit.ai/admin/versions.md) · riskmandateagent-behaviour-policyinsider-threatcontainmentobservabilitymandatebarrierssecond-readerconnector-twinfootprintincident-disclosurelicence-to-operatesynthetic-usersresponsearticle

***Abstract:** On 10 October Satya Nadella published "Models as Insider Risks in the Super Intelligence Era". His argument is that we cannot trace a frontier model's behaviour the way we traced code, so we should treat models the way we treat any powerful insider: identity, least privilege, logs, containment, and controls that sit outside the thing they control. He proposes seven principles: model diversity, observe everything, verifiability, independent controls, independent auditability, containment and incident disclosure. This site and RiskMandate have been making the same case since The ultimate insider on 30 September, and building pieces of it. This is my answer, principle by principle: what we run today, what we have published as design, what we have only argued, and where I would push. It includes an honest maturity table, three things from this week's work (synthetic users that found real bugs, a safety check that stopped our own agents, and the ratio of hope in the policy of the agent that runs this site), and the five things his list leaves out that I think decide whether the principles work, starting with the mandate: observation tells you what an agent did, and only a written mandate tells you whether it was allowed.*

Nadella's seven principles, and what stands behind each one on this network today. Running means it runs in our own agent team or on this site; published means a vault or page anyone can open; design means written down and not yet built.

On 10 October Satya Nadella published a short post, [Models as Insider Risks in the Super Intelligence Era](https://snscratchpad.com/posts/models-as-insider-risks/). I read it twice, because it reads like a summary of what this site has been arguing since [The ultimate insider](ultimate-insider-three-collisions.md) on 30 September, written by the CEO of the company that ships Copilot.

That is good news, and it deserves a proper answer rather than a repost. This is the second of two articles. The first, [The same argument, in our words](the-same-argument-in-our-words.md), translates his ideas into our vocabulary at the level of principle. This one is the detailed answer: for each of his seven principles, what I agree with, what we already run, what is only design, and where I think the list needs more. His post is short and worth reading in full first. I paraphrase it here, and quote it once.

## In short

- **The argument is now mainstream.** The CEO of one of the largest AI vendors is saying what this site has been saying: treat a model as an insider, not because it is malicious, but because anything capable with access to important systems can make mistakes or be turned, and build the controls so that they do not depend on the model behaving.
- **His core move is the right one.** Keep the source of the intelligence and the authority over it in different hands. That is the [enforcer test](https://abp.sgit.ai/model/barriers/index.html) in one sentence: a control bounds a grant only if it is enforced by something the grant does not include.
- **Each of his seven principles maps to something we run, publish or plan.** A second reader that fails closed on every draft. A connector twin that journals every call. A hostile mail set run through three designs of one agent. Synthetic users that drive a real browser and found bugs every test had passed over. Agents on dedicated accounts that draft and never send. Our own incidents, written up the day they happened.
- **Most of it is not finished, and I will say so.** The table at the end separates what runs from what is a published design and what is only argued. The honest shape: the pattern is proven on a small, real system; the products around it are early.
- **Five things his list leaves out decide whether the principles work.** The mandate, because observation tells you what happened and not whether it was allowed. The deployment, because risk is a property of one agent in one setup, not of the model. A named owner and an expiry for the risk that is left. Recoverability, because a brake does not undo anything. And speed: decisions made in advance, as envelopes, not quarterly in spreadsheets.
- **The irony holds.** His last line says the most trustworthy system is the one that needs to trust the model least. Ours, from 30 September, is that the more you constrain an agent, the more autonomy you can afford to give it. Same sentence, read from opposite ends.

## His argument, in brief

He starts from a loss. For decades, when software did something, we could follow the behaviour back to a code path. With frontier models we cannot: we cannot tie an output to a particular piece of training data or a particular arrangement of weights. And yet these are the systems we are now connecting to our most sensitive data and allowing to act on our behalf.

From there he makes three moves. Responsibility stays with the deployer, and no assurance from a model provider transfers it. Alignment is a hard and separate problem, so set it aside and start with engineering: wrap a non-deterministic model in deterministic design, human controls and dependable operating procedure. And the right frame for that engineering is insider risk, which enterprises have practised for decades: give the actor an identity, limit its privileges, log what it does, and put it inside boundaries. In his words, we need to **"separate the supply of intelligence from the authority over it."**

He is careful about two of the obvious answers. Transparency of the model's chain of thought should be non-negotiable, he says, but it is not enough, because we cannot yet make a model's account of itself reliably faithful. Using models to test and check each other is good practice, but done naively it stacks opacity on opacity: a black box, orchestrated by a black box, watched by a third. So the controls over what a model can reach and do have to live outside it, in the tradition of the security principle, usually traced to the reference monitor of the early 1970s, that a program must not be able to tamper with or route around whatever enforces its permissions. In practice, that means separating the model from the harness that drives it, and both from the space of actions it can take.

His seven principles follow from that. Let's take them one at a time.

## Seven principles, seven answers

For each one: what he asks for, what we run today, what is published as design, and where I would push.

### 1. Model diversity

**What he asks.** No single model should be the only thing an important outcome depends on, and no model should be the one checking its own work.

**What we run.** On 9 October, two emails drafted by one of my agents went out in my voice. The rule against it existed in four places, and it failed because the agent was the only reader of its own draft. The fix, built the same day, is [a second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md): a hook on the draft tool that runs code checks first, then a fresh model call that sees only the rules, the sources and the draft, and that treats anything other than an explicit PASS as a FAIL. It runs on every draft in our email pipeline, and the checker is a different model from the author: the drafter runs on Opus and the checker on Sonnet, so they do not share every blind spot.

Beyond that: [our agents run in four places](why-my-agents-do-not-run-on-my-laptop.md), one of them a different vendor's model kept for second opinions; the [infographic bake-off](the-infographic-bake-off.md) judged every image model on OpenRouter blind; and every article on this site is read again afterwards by [five readers](one-article-five-readers.md) with different jobs, which is where the flags for the author come from.

**Where I would push.** Diversity of models is half of it. The other half is diversity of *context*. The checker in the second-reader pattern gets less than the author, on purpose: no conversation history, no tools. A second model that has read the same poisoned email as the first is not independent, however different its weights are.

### 2. Observe everything

**What he asks.** Every meaningful action leaves evidence that cannot be tampered with and that a person can read, so that an outcome can be reconstructed without asking the model to vouch for it.

**What we run.** The [agent team](the-agent-team-as-it-runs.md) keeps its memory in encrypted vaults whose history is the record: every change is a commit, every message between agents is a file, and each person's record carries an append-only ledger with every message word for word, its provenance and a hash. [Append lanes](where-the-vault-keys-live.md) let any agent write an entry with one POST to a lane it cannot read back, which is exactly the shape tamper-resistant evidence needs: the writer cannot edit what it wrote. And [re-anchoring](re-anchoring-agent-behaviour-policies.md) adds a canary: a status report computed from the session's transcript rather than written by the model, so that a missing report is itself evidence. The session that runs this site produces one every three answers, and a hook asks for it if it goes missing.

**What is design.** The [connector twin](connector-twin-before-you-deploy-an-agent.md): a journal of every request and response an agent makes through a connector, appended as it happens and replayed later into the inbox and calendar as the agent saw them, with a before and after for each change. It is published as [a vault with a working replay](https://sgit.ai/demos/vaults/connector-twin/index.md) of an invented session, and a business plan; the service is not built. And [footprint](footprint-and-blast-radius.md), what the agent actually did, read afterwards from logs with nobody inline, is a proposal still under review.

**Where I would push.** Two things. Evidence should not be held by the party being observed: the platform that runs the agent is the last place its record should live, which is why ours sits in vaults whose host stores ciphertext and never holds a key. And "observe everything" produces a lot of evidence of nothing in particular unless there is something to compare it with. That is the first of the five gaps below.

### 3. Verifiability

**What he asks.** Test the whole system continuously, including failures, attacks, edge cases and changes, not only the happy path.

**What we run.** [Hope or enforcement](hope-or-enforcement.md) takes one customer service mandate, builds the agent three ways, and runs the same 62 emails through each, sixteen of them hostile. Every rule in each design's policy is marked by what enforces it, and the hostile mail shows which rules a boundary held and which rested on the model: in the first design, all 138 hostile tests rested on the model; in the third, 52 of 85 were held by a boundary. On this site, [a release ends by asking the live site its version](green-does-not-mean-live.md), because two releases once passed every check and never arrived.

And there is a kind of testing his list does not name, which keeps paying for itself: [synthetic users](how-to-run-synthetic-users.md). Five invented people drive a real browser through a site one screenshot at a time. It is meant to find where a page loses a reader, and it does, but its best findings have been bugs. On riskmandate.ai it recorded two JavaScript errors that had shipped and that every existing test had passed over, because the page still rendered and only the browser's console knew. On newsroom.sgit.ai, yesterday, a synthetic researcher hit a missing image in the lead article, and checking it showed 51 of the 527 figures across 10 articles had not survived the move. Neither was a matter of opinion; both came from driving the real thing.

**Honest limit.** Hope or enforcement is a deterministic simulation; no model was called. It tests the design, not a running agent. The second reader and the canary are tested in production, on a small system: ours. And synthetic users are invented people: good at finding where a page loses someone, no evidence at all about how many real people it would lose.

**Where I would push.** Verify the *policy*, not only the system. After every run, our analyst counts how often each rule was exercised, how often hostile input tested it, and whether a boundary or the model held. Rules that are never exercised get listed. That is how a policy gets shorter over time, and a shorter policy is easier to verify.

Nested black boxes, or a gate the agent cannot skip. A model checking a model with the same context and on the same account is opacity on opacity. The second-reader pattern puts code first, gives the checker less than the author, fails closed, and logs every verdict; and whether it is a control depends on who owns its installation.

### 4. Independent controls

**What he asks.** The organisation, not the model or its vendor, decides what a model can reach and what it can do.

**What we ship.** This is the core of [RiskMandate](https://riskmandate.ai/). An [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) writes down four things for one agent in one deployment: the **reach**, what it can actually do, measured; the **mandate**, what the business authorised; the **gap**, reach minus mandate, derived and never written by hand; and the **barriers**, what stands in front of each row of the gap, typed as a boundary, a setting, an expectation or nothing. Only a boundary is a control. The home page puts it in six words: a prompt asks, a policy enforces. The model, sixteen published example policies and the vocabulary are free to read at [abp.sgit.ai](https://abp.sgit.ai/), under CC BY 4.0.

**What the numbers say.** Measuring the reach is where independence starts, because you cannot independently decide what you have not measured. The narrowest Gmail scope that reads one message [reads every message](https://riskmandate.ai/lab-connector-grants.html). In the published policy for Claude Code on the web with one repository attached, the agent can reach fifteen capabilities; six of them were asked for, and seven of the other nine have nothing real in the way.

**What happened to us this week.** When this site's agent set five synthetic readers loose on newsroom.sgit.ai, Claude Code's own safety check stopped the persona agents from driving the live site through a browser. That is his principle working on us: a check in the harness, not in the model, that the agents could not talk their way past. The agent did not try. It served a copy of the site, verified byte for byte against the live one, so that no request could leave the machine, and asked me; I approved one narrow rule for one helper. And by our own test, I have to be honest about what that rule is: it lives in a settings file that the agent's own account can write, so it is a setting with a person's approval on record, not a boundary. Same code, different owner.

**Where I would push.** "Independent" has to include independent of the *agent's own account*. The second reader on our pipeline is today a setting: the agent's own account could switch it off. Installed under managed settings, owned by somebody else, the same code becomes a boundary. Most of what the industry currently calls agent guardrails are, in this vocabulary, settings or expectations. That includes ours: the session that runs this site works under a ten-rule policy that labels each rule by what enforces it, and nine are expectations, one is a setting, and none is a boundary. I am not proud of that ratio, but I know it, and that is the point: you cannot improve a number you have not counted.

RiskMandate itself is [deliberately not inline](https://riskmandate.ai/grant-gap.html): we author the policy and pre-commit what should happen, and the customer's own gateways, proxies, identity and scoped credentials enforce it. An independent control should not be one more vendor in the request path.

### 5. Independent auditability

**What he asks.** Validation must not depend on the intelligence being validated, and no single model should hold both the behaviour and the evidence used to judge it.

**What we run.** The policy and its evidence live in an encrypted vault the customer holds the keys to. A read key is derived one way from the vault key, so a board, an auditor or a broker can be handed exactly what the operator sees and nothing they can change. Every vault on this site is published with its read key, on purpose, so that any claim made here can be checked by somebody who is not us. The [newsroom's run log](https://newsroom.sgit.ai/newsroom/log.html) and every article's version history are public for the same reason.

**Where I would push.** Separating behaviour from evidence is necessary. It is not sufficient if the *mandate* the evidence is judged against is also written by whoever runs the agent, after the fact. The mandate should be locked under change control before the agent runs, so that an auditor compares the footprint with a commitment, not with a story. The same goes for the checker's inputs. Our own second reader has an honest limit, written up in its article: it compares a draft with the sources it is given, and today the drafting agent writes those sources. The log records whether sources were given, so it is auditable; the full fix is sources that come from somewhere the drafter cannot write.

### 6. Containment

**What he asks.** Assume the model is compromised from the start, and make sure an authorised person can always pause or stop it mid-task: an emergency brake, with stronger containment as models get stronger.

**What we run.** Every agent in [our team](the-agent-team-as-it-runs.md) is a session on a dedicated account, so the account is the blast radius. No agent sends: agents create drafts, and a person sends. The one exception is itself a brake: the security agent may send one email, to one address, to put the whole team on hold. [No agent runs on my laptop](why-my-agents-do-not-run-on-my-laptop.md), because a process on my laptop runs as me, and the operating system has no wall between an agent and my keys inside my own account. In the third design in Hope or enforcement, tools take no customer argument, refunds stop at 100 GBP per order, and a 2,000 GBP daily circuit breaker covers every automatic refund: one bad day is bounded before it starts. And the synthetic users above drove a browser that answered from a local copy of the site and refused every request that was not a read, or that went anywhere else: whatever they decided, nothing could be submitted.

**What is design.** The [plug profile](https://riskmandate.ai/plug.html): who can stop this agent, how fast from the decision, what breaks when they do, and what can never be undone, with a named owner and an expiry. The [Licence to Operate](https://riskmandate.ai/licence-to-operate.html), where the business is the authority, the policy is the instrument and the agent is the licensee for a stated interval, exists as a template; automatic revocation is design.

**Where I would push.** A brake is only as good as the answers to four questions that most teams cannot give for a single agent: who holds it, how long it takes, what it breaks, and what it cannot reverse. The last one matters most. Stopping an agent halfway through a refund run does not refund anything. Containment without recoverability is a brake on a car with no reverse gear.

### 7. Incident disclosure

**What he asks.** When these systems fail or are compromised, tell the people affected promptly, and share what failed, which controls did not hold and how to stop it recurring, across the industry, including the details that change how agents behave at runtime.

**What we run.** We disclose our own. The [second reader](a-second-reader-the-agent-cannot-skip.md) article opens with the two emails that went out wrongly in my voice, published the day it happened, with the rule that failed and why. [Green does not mean live](green-does-not-mean-live.md) is a release failure written up. The [GitHub Actions outage](the-investigation-github-owes-its-customers.md) on 5 October took our own release down with it, and that article argues for the aviation model: independent investigators, mandatory reporting of serious incidents, confidential reporting of near misses, and three stories: what happened, why the system allowed it, and why the fix was not paid for.

**What is argued, not built.** [The ultimate insider](ultimate-insider-three-collisions.md) made the case that the main reason we do not see more agent incidents is that almost nobody is required to report them, and that NASA's [Aviation Safety Reporting System](https://en.wikipedia.org/wiki/Aviation_Safety_Reporting_System) shows what changes when it is safe to. A reporting system for agent near misses does not exist on this network, or anywhere we know of. The evidence side does: vaults with one-way read keys, signed and versioned, make it affordable to hand an investigator exactly the record of one incident.

**Where I would push.** Disclose near misses, not only incidents. In our vocabulary a near miss has a precise definition: [footprint in the gap](footprint-and-blast-radius.md). The agent went somewhere it was not asked to go, and nothing stopped it. That is countable, it happens long before anything breaks, and it is the number that would tell the industry where the real risk is.

## Five things the list leaves out

His seven principles are almost all about one column of the problem: evidence and enforcement. Read against our work, five things are missing, and each of them decides whether the seven work in practice.

What observation sees, and what it cannot. The seven principles live mostly in the evidence column. The authority column, the mandate with its gap, barriers, named owner and expiry, is what lets the evidence mean something: footprint compared with the mandate gives a near miss or a dormant mandate, and nothing else does.

**1. The mandate.** Observation tells you what an agent did. It cannot tell you whether the agent was allowed to, unless somebody wrote down what it was for before it ran. Separating the supply of intelligence from the authority over it needs the authority to exist as a document: the mandate, the dozen things the agent is for, with their limits. Compared with the footprint, it produces the two findings that matter: a near miss, where the agent did something outside the mandate and nothing stopped it, and a dormant mandate, where something you relied on never ran.

**2. The deployment, not the model.** His post frames the risk as a property of models. Our evidence says it is a property of one agent in one deployment. The same model is harmless with a read-only tool bound to one customer, and serious with the broadest Gmail scope and a read-write database role; in Hope or enforcement, that difference is one customer against 38,000. Industry standards for "models" will miss most of the risk if they do not describe deployments.

**3. A named owner and an expiry.** [Every risk is already accepted](every-risk-is-already-accepted.md), from the day the exposure exists, by somebody, signed for or not. Containment and observability reduce the gap; they never close it. What is left needs a person who accepts it for a stated interval, and a fact that would end the acceptance. Without that, the residual risk of an agent belongs to nobody, which in practice means it belongs to the board without the board knowing.

**4. Recoverability.** The emergency brake stops the next action. It does nothing for the ones already taken. The connector twin's contribution is to turn "can we undo this?" into a list: for every change, the inverse call, and the plain names of what cannot be undone, such as an email that has been delivered. A policy written against that list is a different kind of document from one written against hope.

**5. Speed.** The decisions behind all seven principles are risk decisions, and in most organisations they are still made in spreadsheets, quarterly. An agent needs them made in advance, as an envelope it can act inside, and in seconds when it asks to step outside. That is what turns containment from a reason to pull the plug into a reason to give the agent more room. It is also where insurers come in: the record that lets an underwriter price an agent is the same record that lets a business approve one.

## What his post has that we do not

Three things, said plainly.

**Chain-of-thought transparency.** We have not worked on it. Our designs assume the model's account of itself is not evidence, which matches his own caveat, but it does not replace the principle.

**Standards.** He calls for industry standards where the existing ones fall short. Our offer is that the vocabulary is open, pinned at [abp.sgit.ai](https://abp.sgit.ai/) under CC BY 4.0, and mapped against [ISO/IEC 42001, the OWASP Agentic Top 10, NIST AI RMF and ISO/IEC 27001](https://riskmandate.ai/insurance.html). But a standard needs more than one small company behind it.

**Continuous adversarial testing of systems in production, at scale.** Ours is a simulation, a small real pipeline and synthetic users on a handful of sites. A vendor with Microsoft's reach can run it where it matters.

## Honest maturity, principle by principle

| Principle | What runs today | Published as design | Planned or argued |
|---|---|---|---|
| **Model diversity** | Second reader on every draft in our email pipeline, failing closed; a second vendor's model kept for review |  | Second reader installed under managed settings, as a boundary |
| **Observe everything** | Vault history, append-only ledgers with hashes, append lanes, the canary | [Connector twin](https://sgit.ai/demos/vaults/connector-twin/index.md) with a working replay | Footprint as part of the policy (under review) |
| **Verifiability** | Policy read after every run; release checks the live site; synthetic users in a real browser | [Hope or enforcement](https://sgit.ai/demos/vaults/hope-or-enforcement/index.md): 62 emails, 16 hostile, simulated | Hostile sets run against live agents |
| **Independent controls** | ABP model, library and [published policies](https://abp.sgit.ai/examples/index.html), free | Four priced levels, live as an on-ramp | Automatic reach recompute wired to pipelines (MVPs) |
| **Independent auditability** | Read keys for every published vault; public run log and article versions |  | Mandate locked under change control as standard practice |
| **Containment** | Dedicated accounts; no agent sends, except one email that puts the team on hold; no agents on the laptop | [Plug profile](https://riskmandate.ai/plug.html); [Licence to Operate](https://riskmandate.ai/licence-to-operate.html) template | Automatic revocation; PKI-delegated authority (MVPs, not wired) |
| **Incident disclosure** | Our own incidents written up the day they happen |  | Near-miss reporting; independent investigation with vault evidence |

## Where to start, if you agree with him

- **Write the mandate before the agent runs**: the dozen things it is for, with their limits, locked under change control.
- **Measure the reach**, not the documentation. Then derive the gap.
- **Mark every rule with what enforces it**: boundary, setting, expectation or nothing. Count the expectations. That count is how much of your policy is hope.
- **Put a second reader on the actions that cannot be undone**, with less context than the author, code checks first, failing closed, installed by someone other than the agent's owner.
- **Journal every connector call** somewhere the agent cannot edit, and write down what cannot be reversed.
- **Name the owner and the expiry** of whatever risk is left.
- **Publish your near misses.** Somebody has to go first.

His last line is that the most trustworthy system will be the one that lets us trust the model least. I agree, and I would add the other half: once you know exactly how little you have to trust it, you can let it do a great deal more.

If you are deploying agents and want to try this on one of yours, from the mandate to the count of expectations, let's talk: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

Satya Nadella's post, [Models as Insider Risks in the Super Intelligence Era](https://snscratchpad.com/posts/models-as-insider-risks/), sn scratchpad, 10 October 2026, read in full; it is paraphrased throughout and quoted once. I asked an agent in a separate Claude session to read it alongside the articles, vaults and pages of this network, check every claim about what runs against the page that owns it, and draft this answer with its figures; this site's agent then rewrote it in the voice of this site and added what happened this week, from its own runs. Every claim about what runs links to the page that owns it; where something is design or only argued, it says so. The argument is mine, and so is the editorial responsibility. On this site: [The same argument, in our words](the-same-argument-in-our-words.md), [The ultimate insider](ultimate-insider-three-collisions.md), [Hope or enforcement](hope-or-enforcement.md), [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md), [Re-anchoring](re-anchoring-agent-behaviour-policies.md), [the connector twin](connector-twin-before-you-deploy-an-agent.md), [Footprint and blast radius](footprint-and-blast-radius.md), [The agent team as it runs](the-agent-team-as-it-runs.md), [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md), [Where the vault keys live](where-the-vault-keys-live.md), [Every risk is already accepted](every-risk-is-already-accepted.md), [The investigation GitHub owes its customers](the-investigation-github-owes-its-customers.md), [Green does not mean live](green-does-not-mean-live.md), [How to run synthetic users](how-to-run-synthetic-users.md) and [Ten hard questions for RiskMandate, answered](riskmandate-ten-questions.md). On RiskMandate: [home](https://riskmandate.ai/), [grant and gap](https://riskmandate.ai/grant-gap.html), [Who can pull the plug?](https://riskmandate.ai/plug.html), [Licence to Operate](https://riskmandate.ai/licence-to-operate.html) and [Insurability](https://riskmandate.ai/insurance.html). The model and vocabulary: [abp.sgit.ai](https://abp.sgit.ai/). And NASA's [Aviation Safety Reporting System](https://en.wikipedia.org/wiki/Aviation_Safety_Reporting_System).

## Threads

Agents & policy[This article as a graph →](graphs.md#authority-outside-the-model)

### Builds on

- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The infographic bake-off: which image model for which job, judged blind on 10 October 2026](the-infographic-bake-off.md) Every image model on OpenRouter, eleven briefs, 101 images judged blind, $10.44: which model for which infographic, and what it costs.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Green does not mean live](green-does-not-mean-live.md) Two releases passed every check and never reached the site because the checks stopped at the git remote; a release now ends by asking the live site its version.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md) A global GitHub Actions outage read the way aviation reads an incident: independent inquiry, near-miss reporting, second and third stories, vaults for the evidence.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.

### Continued by

- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [authority-outside-the-model.jpg](banners/authority-outside-the-model.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/authority-outside-the-model.html)*
