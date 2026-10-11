# The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate, sgit.ai

> On 10 October Satya Nadella published "Models as Insider Risks in the Super Intelligence Era", a short post arguing that because we can no longer trace what a model does back to a code path, we should treat models the way we treat any powerful insider, and keep the authority over them outside them. Reading it, I kept translating. His lost code path is what I have been calling software was the law. His insider that need not be malicious is the ultimate insider. His split between the supply of intelligence and the authority over it is RiskMandate's founding line, the grant is not the mandate. His controls outside the model are the enforcer test. And his last line, that the most trustworthy system is the one that needs to trust the model least, is the irony The ultimate insider ended on: the more you can constrain an agent, the more autonomy you can afford to give it. This article puts the two vocabularies side by side, idea by idea, shows where ours came from, and names the two places where they differ: his unit is the model and ours is one agent in one deployment, and his frame is observation where ours is authority, accepted by a named person for a stated interval. A companion article takes his seven principles one at a time.

*Source: <https://newsroom.sgit.ai/articles/the-same-argument-in-our-words.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate

# The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/the-same-argument-in-our-words.md) · [sgit.ai v0.7.41](https://sgit.ai/admin/versions.md) · riskmandateagent-behaviour-policyinsider-threatmandategrantbarriersenforcer-testrisk-acceptancesoftware-was-the-lawphilosophyresponsearticle

***Abstract:** On 10 October Satya Nadella published "Models as Insider Risks in the Super Intelligence Era", a short post arguing that because we can no longer trace what a model does back to a code path, we should treat models the way we treat any powerful insider, and keep the authority over them outside them. Reading it, I kept translating. His lost code path is what I have been calling software was the law. His insider that need not be malicious is the ultimate insider. His split between the supply of intelligence and the authority over it is RiskMandate's founding line, the grant is not the mandate. His controls outside the model are the enforcer test. And his last line, that the most trustworthy system is the one that needs to trust the model least, is the irony The ultimate insider ended on: the more you can constrain an agent, the more autonomy you can afford to give it. This article puts the two vocabularies side by side, idea by idea, shows where ours came from, and names the two places where they differ: his unit is the model and ours is one agent in one deployment, and his frame is observation where ours is authority, accepted by a named person for a stated interval. A companion article takes his seven principles one at a time.*

His words and ours. Each idea in Satya Nadella's post, paraphrased, beside the word this network has been using for it, and the page where that word is defined and worked through.

On 10 October Satya Nadella published [Models as Insider Risks in the Super Intelligence Era](https://snscratchpad.com/posts/models-as-insider-risks/). It is short and careful, and as I read it I kept doing the same thing: translating it, line by line, into the words we have been using on this site and on [RiskMandate](https://riskmandate.ai/) for the last few weeks, and in some cases for much longer.

This is a big deal, and not for the reason you might think. It is not about who said it first. When the CEO of one of the largest AI vendors arrives at the same conclusions from the other side of the market, from the side that builds the models rather than the side that has to live with them, that is evidence the conclusions are right. Two very different starting points, one set of answers. So this is not a rebuttal. It is a translation, because the most useful thing I can do with his post is show how the two vocabularies map onto each other, and where they do not.

This is the first of two articles. The second, [Authority outside the model](authority-outside-the-model.md), takes his seven principles one at a time and says, for each, what we run, what we have only designed, and what we have only argued. His post is worth reading in full first. I paraphrase it here, and quote it once.

## In short

- **We are describing the same thing.** He starts from what we lost when models replaced code; I called it [software was the law](the-behaviour-policy-is-the-business-logic.md). He treats models as insiders that need not be malicious; I called that [the ultimate insider](ultimate-insider-three-collisions.md). He separates the supply of intelligence from the authority over it; RiskMandate's first line is that [the grant is not the mandate](https://riskmandate.ai/grant-gap.html).
- **His most important idea is our enforcer test.** Controls have to sit outside the thing they control. In [the ABP's words](https://abp.sgit.ai/model/barriers/index.html), a control bounds a grant only if it is enforced by something the grant does not include. Everything else in his post follows from that, and so does everything in ours.
- **We got here from risk, not from models.** Twenty-five years of security work, much of it in application security and as a CISO, taught me that most damage is not malice, that [every risk is already accepted](every-risk-is-already-accepted.md) by somebody, and that the interesting number is the gap between what a credential allows and what its holder was meant to do. Agents made that gap the whole problem.
- **Two differences are worth naming.** His unit is the model; ours is one agent in one deployment, because the same model is harmless in one setup and serious in another. His frame is observation; ours is authority: a mandate written before the agent runs, and the risk that is left accepted by a named person for a stated interval.
- **The ending is the same sentence, read from opposite ends.** His: the most trustworthy system is the one that needs to trust the model least. Ours: the more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it.

## Where our words came from

It helps to say where our vocabulary comes from, because it was not built for models. It was built for risk.

Most of the worst damage I have seen in twenty-five years of security work was not an attack. It was a bug, a misconfiguration, a script run against the wrong environment, a person doing something that was allowed and should not have been. So when I say threat, I mean anything that causes business impact, malicious or not. And underneath the damage, the same thing kept turning up: what somebody *could* do was much larger than what they were *meant* to do, the difference was rarely written down, and so it was rarely accepted by anyone.

That became the research behind [risks.sgit.ai](https://risks.sgit.ai/), which starts from an inversion: you cannot deny a risk, you can only say how long you accept it. A risk with a real exposure under it exists whether or not anyone signs for it. Take away the deny button, ask a named person to underwrite the exposure for a stated interval, and risk management stops being a gate and becomes a forcing function, because whoever has to sign starts asking for evidence.

Then agents arrived, and every part of that problem got worse at once. An agent is given a credential whose reach has rarely been measured, a job that is usually clear but rarely written down, and a set of rules it is asked to keep itself. RiskMandate exists to answer one narrow question about that arrangement: what can this agent we just connected actually do, and who said it could? The answer is a document, the [Agent Behaviour Policy](https://abp.sgit.ai/), and its four words are the vocabulary the rest of this article translates into:

- **Reach**: what the agent can do, measured.
- **Mandate**: what the business authorised, written down.
- **Gap**: reach minus mandate, derived, never written by hand.
- **Barriers**: what stands in the way of each row of the gap: nothing, an expectation, a setting, or a boundary.
How the vocabulary was built, in dated public work. Most of it was written in the three weeks before Nadella's post, on top of risk and identity research going back to 2025. The convergence is the point: two very different starting places, one set of conclusions.

## His words, translated

### The code path we lost, or software was the law

He opens with a loss. For decades, when software did something, we could follow the behaviour back to a code path. With frontier models we cannot, and yet these are the systems we are connecting to sensitive data and letting act for us.

I described the same loss from the business side, in [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md). For decades, the rules of a business lived in its systems. A clerk could not send an unapproved invoice, because the finance system had no button for it until the approval was recorded. Those rules were enforced by omission, by the screen that did not show the button. An agent works through APIs, not screens: it can call the endpoint the button would have called. So the rule is no longer enforced, unless somebody writes it down and something outside the agent enforces it.

The translation adds one thing to his version. What we lost was not only traceability. It was the place where the business kept its rules. Many organisations have never written those rules down, because their software was the law. The behaviour policy is where they get written down, and that is why, a few layers in, an agent's policy stops being about security and starts being about how the company actually works.

### An insider that need not be malicious, or the ultimate insider

His frame is insider risk: treat a frontier model, closed or open, as an insider, not because it means harm, but because anything capable with access to important systems can make mistakes or be compromised.

That is the argument of [The ultimate insider](ultimate-insider-three-collisions.md), from 30 September. Insider threat was always real and always hard to scale, because the insider was either a person, bounded by hours, skills and conscience, or code, which did exactly what it was written to do. An agent is neither. It is a reasoning engine in a loop with tools, fluent in every language and every schema, able to write the connector it lacks and try again. Three of the five public incidents in that article were not attacks at all, just agents being agents. The way I put it then: the distance between the benign case and the hostile one is a prompt.

[Knowing when to stop](knowing-when-to-stop.md) adds the part that is easy to miss. The variability that makes an agent dangerous is also what makes it useful; in a person, we would call it creativity. You cannot engineer it away without losing the point of the agent. A model that can go in every direction needs someone with a direction, and something that stops it.

### Responsibility cannot be outsourced, or every risk is already accepted

He is clear that responsibility for what intelligence does on our behalf stays with us, and that a model provider's assurances do not move it.

In our words: [every risk is already accepted](every-risk-is-already-accepted.md). The day an agent is connected, the exposure exists, and somebody is carrying it, signed for or not. There is no deny button, only the question of who holds it and until when. A risk that nobody accepted has not gone away. It has come to rest on whoever is nearest, and it rolls upward to the board without anyone choosing to escalate it.

The vendor point has a sharper edge in our vocabulary. On [nhi.sgit.ai](https://nhi.sgit.ai/) we separate agents you run from agents you rent. Almost every agent a business can name today is rented: it runs on somebody else's infrastructure, and the only thing the business controls is the credential it hands over. For those, the honest current workflow is to hand over a broad credential and hope. Hope is not a control, and it does not change who is accountable.

### Supply and authority, or the grant is not the mandate

This is the centre of his post, and of ours. In his words, we need to **"separate the supply of intelligence from the authority over it."**

RiskMandate's [first page](https://riskmandate.ai/grant-gap.html) says the same thing in five words: the grant is not the mandate. A grant is what the credential technically permits. A mandate is what the holder is authorised and expected to do. In practice the first is much larger than the second, and the difference is where the exposure lives. The supply of intelligence arrives with a grant attached. The authority is the mandate, and it only exists if somebody writes it down.

Our vocabulary is stricter about what counts as authority. A mandate has an issuer, a subject, a scope, an interval and a way to revoke it; an instruction in a chat has none of these. And a mandate with no clock is just a grant. That last line is the one I would most like to see in an industry standard, because an authority that never expires is not separated from the supply. It has quietly become part of it.

Supply and authority, in RiskMandate's terms. The supply arrives with a grant; the authority is a mandate with an issuer, a scope and a clock. The gap between them is derived, and each row of it has a barrier. Only one kind of barrier is a control.

### Controls outside the model, or the enforcer test

He grounds the separation in an old security principle: a program must not be able to bypass or tamper with whatever enforces its permissions. So the controls over what a model can reach and do have to sit outside it, which means pulling apart the model, the harness that drives it, and the space of actions it can take.

The ABP turns that principle into a test you can run on any rule: [a control bounds a grant only if it is enforced by something the grant does not include](https://abp.sgit.ai/model/barriers/index.html). Four kinds of barrier follow from it:

- **Nothing.**
- **An expectation**: a rule in prose, enforced by nobody.
- **A setting**: a switch the agent's own account could flip.
- **A boundary**: enforced above the grant, out of the agent's reach.

Only the last one is a control. RiskMandate's home page says it shorter: a prompt asks, a policy enforces.

His worry about models checking models, an opaque system watched by another opaque system, is the same test applied to verification. [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md) starts from the line that a rule kept by the agent it governs is hope, and ends on this: the same checking code is a setting when the agent's own account installed it, and a boundary when somebody else did. Same code, different owner. Independence is not a property of the checker. It is a property of who controls it.

### Deterministic design around a non-deterministic model, or moving knowledge into code

He asks for engineering before alignment: wrap the non-deterministic model in deterministic system design, human controls and dependable procedure.

[Hope or enforcement](hope-or-enforcement.md) measured what that does. One customer service agent, built three ways, with the same rules each time. With one model and broad connectors, 97% of the policy was hope. Behind a harness of business tools, 73%. As a team of narrow agents behind a deterministic gateway, with tools that take no customer argument and limits written into the tools, 23%, and one run could reach one customer instead of 38,000. The phrase that came out of it is my translation of his: granularity moves knowledge out of the prompt and into code. And there is a finding he does not mention: as the reach falls, the policy gets shorter, because it no longer has to forbid what the agent has no way to do.

### Observe everything, or reality is the calibrator

He wants every meaningful action to leave evidence that cannot be tampered with and that a person can read, so that an outcome can be reconstructed without relying on the model's account of it.

We arrived at the same rule by being wrong. I wrote a policy for an agent from the vendor's documentation, which said the connector could not send attachments. The agent found a way, proved it with a signed PDF, and wrote it up; that story is in [Six agents, one inbox](six-agents-one-inbox.md). Since then the rule has been that the grant is measured on the thing itself, and calibrated against what the logs show it did: the [footprint](footprint-and-blast-radius.md). Reality is the calibrator. The [connector twin](connector-twin-before-you-deploy-an-agent.md) is the same idea for actions: journal every call, replay it as the agent saw it, and turn "can we undo this?" into a list.

Our version adds two conditions. First, the evidence should not be held by whoever is being observed, which is why ours lives in vaults whose host stores ciphertext and never holds a key. Second, observation needs something to compare against. A footprint read against a written mandate produces findings: a near miss, where the agent went somewhere it was not asked and nothing stopped it, or a dormant mandate, where something you relied on never ran. A footprint read against nothing produces logs. That is why RiskMandate's order is to instrument before you enforce: the measurement is what tells you where enforcement is worth its cost.

### Containment and the brake, or the account is the blast radius

He asks us to assume the model is compromised from the start, and to make sure an authorised person can always pause or stop it mid-task.

Our first containment rule came from running agents, not from theory: [the account is the blast radius](six-agents-one-inbox.md). Every session an agent opens runs as the account that authorised it, so the first real control is a dedicated account per agent. The brake, in RiskMandate's language, is the question a board asks in one sentence: [who can pull the plug?](https://riskmandate.ai/plug.html) The plug always exists. What is missing is its profile: who holds it, how fast it works from the decision, what breaks when it is pulled, and what can never be undone. The last of those matters most, because a brake stops the next action and does nothing for the ones already taken.

### Incident disclosure, or near misses are incidents

He asks for timely disclosure to the people affected, and for the industry to share what failed and how to prevent it.

The ultimate insider argued that the main reason we do not see more agent incidents is that almost nobody is required to report them, and pointed at aviation, where confidential near-miss reporting, about 100,000 reports a year, helped make a complex system safe. Our own practice is to write up our incidents the day they happen: the second reader article opens with two emails that went out wrongly in my voice. And our vocabulary gives disclosure something precise to count. A near miss is footprint in the gap: the agent went somewhere it was not asked to go, and nothing stopped it. It happens long before anything breaks.

### Trust the model least, or brakes are what let a car go fast

His last line is that the most trustworthy system will not be the one with the most trusted model, but the one that needs to trust the model least.

Ours, from the end of The ultimate insider: the more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it. Once you know the universe of what an agent can do, and that universe fits inside your risk appetite, you can let it act freely within it, and every human decision becomes an exception worth making rather than one alarm among thousands. We put brakes on cars so that we can go faster.

They are the same sentence. His is written from the point of view of the system that has to be trusted. Ours is written from the point of view of the business that wants to use it.

## Where the two languages differ

A translation is most useful where it is not one to one. There are two differences, and both matter.

**The unit.** His post is about models. Ours is about one agent in one deployment. The same model, connected to a mailbox with the broadest scope and a read-write database, can reach 38,000 customers; behind a gateway with bound tools, one. RiskMandate's home page says it in a heading: not a model property, a property of this deployment. Standards written for models will miss most of the risk if they do not describe deployments.

**The frame.** His principles are mostly about seeing: observability, verification, audit, disclosure. Ours start one step earlier, with deciding. A mandate written before the agent runs. A gap derived from it. And the risk that is left, accepted by a named person for a stated interval, where the interval is the decision: accepting for four hours is declaring an incident, for a month is funding the work, for six months is a named decision to wait. Observation tells you what happened. Authority tells you whether it was allowed, and acceptance tells you who carries it if it was not.

Neither difference is a disagreement. They are the two halves a business needs: the vendor's half, which makes the system observable and containable, and the deployer's half, which says what it is for and who answers for it.

## A shared language is the next step

For me, the most useful thing about his post is that it names principles at the level where an industry can agree on them. The next step is a vocabulary precise enough to write them down for a real agent, and to test them.

Ours is open. The [ABP model](https://abp.sgit.ai/), its four objects, its barrier kinds and the enforcer test are published under CC BY 4.0, with sixteen example policies anyone can read. It is not the only possible language, but it is a working one, and it already says, row by row, how much of a given agent's policy is a control and how much is hope. If you are working on agent standards, or deploying agents and want to try writing the mandate down, let's compare notes: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

For the detail, [Authority outside the model](authority-outside-the-model.md) takes his seven principles one at a time, says what we run, what is published as design and what is only argued, and lists the five things I think the principles need in order to work.

## Where this comes from

Satya Nadella's post, [Models as Insider Risks in the Super Intelligence Era](https://snscratchpad.com/posts/models-as-insider-risks/), sn scratchpad, 10 October 2026, read in full; it is paraphrased throughout and quoted once. I asked an agent in a separate Claude session to read it alongside the articles, vaults and sites of this network, check every claim against the page that owns it, and draft this answer with its figures; this site's agent then rewrote it in the voice of this site. The argument is mine, and so is the editorial responsibility. The pages it translates into: on this site, [The ultimate insider](ultimate-insider-three-collisions.md), [the business logic](the-behaviour-policy-is-the-business-logic.md), [Every risk is already accepted](every-risk-is-already-accepted.md), [Knowing when to stop](knowing-when-to-stop.md), [Six agents, one inbox](six-agents-one-inbox.md), [Hope or enforcement](hope-or-enforcement.md), [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md), [Footprint and blast radius](footprint-and-blast-radius.md) and [the connector twin](connector-twin-before-you-deploy-an-agent.md); on RiskMandate, [the grant is not the mandate](https://riskmandate.ai/grant-gap.html), [Who can pull the plug?](https://riskmandate.ai/plug.html) and [the home page](https://riskmandate.ai/); the model and vocabulary at [abp.sgit.ai](https://abp.sgit.ai/) and [the barrier and the enforcer test](https://abp.sgit.ai/model/barriers/index.html); and the research sites [risks.sgit.ai](https://risks.sgit.ai/) and [nhi.sgit.ai](https://nhi.sgit.ai/).

## Threads

Agents & policy[This article as a graph →](graphs.md#the-same-argument-in-our-words)

### Builds on

- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.

### Continued by

- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 69 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=69)

**Posting this article on LinkedIn?** The cover is [the-same-argument-in-our-words.jpg](banners/the-same-argument-in-our-words.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-same-argument-in-our-words.html)*
