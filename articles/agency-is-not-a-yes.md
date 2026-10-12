# Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source, sgit.ai

> We talk about the human in the loop as if the loop were the point. Most of the time the human, or the agent put in the same place, is asked for a yes or a no, and that is the least interesting part of a decision. This article sets out what agency actually needs, for a person and for an agent: options beyond yes, context in the decider's own terms, the ability to look behind what they are shown, time or tokens, incentives that treat a wrong yes and a wrong no alike, somewhere to escalate, and authority over the system that produced the request. It turns those into a scale of seven levels, from the rubber stamp to the delegator, where the weakest dimension caps the whole decision, and scores fourteen cases from the record and from my own agent team, from a prompt that asks to add label 756-459-3214 to the one email an agent of mine is allowed to send. Below level 3, the decider holds the liability for a decision the system made, and accountability belongs to whoever designed the decision point and up their chain. Above it, the review stops being a sign-off and becomes a QA step: each draft is a chance to validate everything that led to it, to fix the source rather than the output, and to think better. And when a kind of draft keeps going out unchanged, it becomes a rule that runs without review. A vault published with the article holds the scale, the cases and an assessment anyone can run on their own decision points.

*Source: <https://newsroom.sgit.ai/articles/agency-is-not-a-yes.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source

# Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-08 · [article v1.0.0](versions/agency-is-not-a-yes.md) · [sgit.ai v0.7.5](https://sgit.ai/admin/versions.md) · agencyaccountabilityhuman-in-the-loopdecision-makingagentsagent-behaviour-policyprovenancefractal-semantic-graphseu-ai-actmaturity-modelvaultsarticle

***Abstract:** We talk about the human in the loop as if the loop were the point. Most of the time the human, or the agent put in the same place, is asked for a yes or a no, and that is the least interesting part of a decision. This article sets out what agency actually needs, for a person and for an agent: options beyond yes, context in the decider's own terms, the ability to look behind what they are shown, time or tokens, incentives that treat a wrong yes and a wrong no alike, somewhere to escalate, and authority over the system that produced the request. It turns those into a scale of seven levels, from the rubber stamp to the delegator, where the weakest dimension caps the whole decision, and scores fourteen cases from the record and from my own agent team, from a prompt that asks to add label 756-459-3214 to the one email an agent of mine is allowed to send. Below level 3, the decider holds the liability for a decision the system made, and accountability belongs to whoever designed the decision point and up their chain. Above it, the review stops being a sign-off and becomes a QA step: each draft is a chance to validate everything that led to it, to fix the source rather than the output, and to think better. And when a kind of draft keeps going out unchanged, it becomes a rule that runs without review. A vault published with the article holds the scale, the cases and an assessment anyone can run on their own decision points.*

Seven levels of agency for anyone, a person or an agent, asked to make a decision. The weakest of seven dimensions caps the level. Below level 3, accountability belongs to whoever designed the decision point; from level 4, the review improves the system that produced the request.

**Where this comes from.** Two voice memos, recorded one after the other, about agency: what it is, how to tell when someone has it, and how it changes when the someone is an agent. They draw on the agent team that helps me run my work and write this site, and on cases this site has already written up. The scale, the cases and an assessment you can run on your own decisions are in a vault published with the article, [The agency scale](https://sgit.ai/demos/vaults/agency-scale/index.md).

## In short

- **A yes or no is not agency.** It is the least interesting part of a decision, and when a no stalls the work with no way back, it is not even a choice.
- **Agency has seven dimensions**: options, context, depth, time, incentives, escalation and authority. Each can be observed. The weakest one caps the decision.
- **Below level 3 it is liability, not agency.** A decider without the information, time or authority to decide well should not carry the decision. Accountability belongs to whoever designed the decision point, and their boss, and their boss's boss.
- **Above level 3, a review is a QA step, not a sign-off.** Every draft is a chance to validate everything that produced it, to fix the source instead of the output, and to think better.
- **The top of the scale is delegation.** The cases you keep approving unchanged become rules that run without you, as code under a behaviour policy, so the final yes is a decision tree that can be explained.
- **It applies to agents in the same way.** An agent asked "is this OK?" with no context is a rubber stamp too.

## The least interesting part of a decision

I am a human in the loop now. Every day, the agents I work with prepare emails for me to review, and every day I send some of them. No agent sends email on its own, with one exception: a security agent may send one email, to one address, to put the team on hold. So I am the process. And what I have noticed, here as when I was coding and every time I work with an agent, is that the go or no-go is the most boring part. When you get there, you mostly see what you expected to see.

The problem is what a yes-or-no does to the person holding it. If you say no to an agent asking for permission, somebody now has a problem. Either you have to work out what to do differently, or the agent has to find another way, or the work stops. That is why it is always tempting to say yes: get on with it. A decider whose only realistic answer is yes has, in practice, no agency at all. This site has covered how that looks: a prompt that asked to add a repository and said nothing about why, a vendor reporting that its users approve 93% of permission prompts, and a sign-in push accepted after enough repetitions. Those are all in [Where is the why?](where-is-the-why.md).

My favourite example is a prompt that asked to add a label, and named it: label 756-459-3214. Which message? Which label? Why? I could not tell what I was authorising. There was no way for that decision to be a good one, and no way for it to be a bad one either; it was a click.

## The incentive to say no, or to say yes

Turn it around. If the person in the loop is punished for getting a yes wrong, and nothing happens when a no is wrong, they will say no, and find every reason to. If they are punished for delay, or for a no, they will say yes. Whatever you punish, you teach the other answer. The behaviour is well studied: people tend to judge harm caused by acting more harshly than equal harm caused by not acting, which Ritov and Baron called omission bias in 1990, though how strong the effect is has been debated since. A reviewer who is only ever blamed for approvals is not deciding; they are protecting themselves, and the organisation has designed them to.

So agency needs incentives that treat a wrong yes and a wrong no alike, and a margin for honest error. It needs time: a decision made in seconds, mid-task, in a queue, is a decision to trust. And it needs somewhere to escalate. Without those, we can predict that a certain number of mistakes will be made, and whoever makes them cannot fairly be held accountable, because they were never in a position to decide well.

## Everything you are shown is a compression

The next question is whether the decider has what they need to decide. Every time we look at something, we are looking at a compression of reality: a summary of a situation, a description of an action, a draft of a reply. That is fine until there is a question. Then you need to expand it, to see the data it came from, the steps that were taken, the decisions made along the way.

That is why provenance and [fractal semantic graphs](introducing-fractal-semantic-graphs.md) matter here. Provenance is the ability to answer: why did this happen, how was this decided, how did we get here? A graph that can be zoomed is what lets a decider go from the summary to the claim to the source in a few steps. If the answer to "why?" is not available, there is no explainability, and the decision is a guess dressed as a decision.

## Accountability without agency is liability

When the decider has no options, no context, no time or no authority, what they are carrying is not agency but liability. We have done this with cars: a person supervises an automated vehicle for hours, not engaged, and is then expected to take over the moment the system reaches its limits. In a simulator study by Eriksson and Stanton, drivers took between 1.9 and 25.7 seconds to take back control in non-critical conditions. Lisanne Bainbridge called this out in 1983, in a paper titled *Ironies of Automation*: "the more advanced a control system is, so the more crucial may be the contribution of the human operator." The irony is that the more we automate, the harder the human part becomes, and the less ready the human is for it.

The record of who gets blamed is in [Where is the why?](where-is-the-why.md): the moral crumple zone, where the nearest person absorbs the blame for a system's failure, and the Post Office's sub-postmasters, held to shortfalls they had no way of disputing. European guidance on automated decisions already says that sign-off must be "meaningful, rather than just a token gesture".

So here is how I would slice it. When a person in the loop has no agency, the responsibility should not sit with that person. It should sit with whoever designed the decision point, and their boss, and their boss's boss: they are authorising a decision system that will statistically make mistakes, because it has put an entity that cannot decide well at the point of decision.

## The scale

The seven levels in the vault: what the decider can do at each, what agency it gives, and who is accountable.

Put those together and agency becomes measurable. The vault defines seven dimensions, each a question you can answer by looking at the decision point:

| Dimension | The question |
|---|---|
| Options | What can the decider actually do: only yes, yes or no, change the outcome, fix the source, delegate? |
| Context | Do they see what is being decided, and why, in their own terms, or an identifier? |
| Depth | Can they look behind what they are shown: ask, or zoom into the sources and steps? |
| Time | Is there time, or for an agent tokens, to look properly? |
| Incentives | Is a wrong yes treated like a wrong no, with room for honest error? |
| Escalation | Is there somewhere to take a decision they cannot make? |
| Authority | Can they change the system that produced the request? |

Each answer caps the level, and the level is the lowest cap: one weak dimension caps the whole decision, the way one weak link caps a chain. Context without time is still a guess; time without authority is still a sign-off. The seven levels that come out are:

- **0 · Rubber stamp.** Only yes is realistic, or the decider cannot tell what they are deciding.
- **1 · Informed yes or no.** They see what and why, and can accept or refuse.
- **2 · Can look behind it.** They can ask why and follow the provenance, but lack the time, the incentives or the escalation to use it.
- **3 · Resourced.** Time or tokens, symmetric incentives, room for honest error, somewhere to escalate. A good yes-or-no decision is now possible.
- **4 · Editor.** They can change the outcome: edit, ask back, redirect.
- **5 · Owner of the source.** They fix what produced the result: the record, the graph, the brief, the tool.
- **6 · Delegator.** They turn proven cases into rules that run without them, and the final yes is code.
Fourteen decision points scored by the same rule, from the label prompt at level 0 to the one email an agent may send at level 6.

The vault scores fourteen cases with the same rule. Eight of them sit at level 0, including the label prompt, the repository prompt, the sign-in push before it was fixed, the token sign-off and the driver asked to take over. The same push after the fix, with the application, the location and a number to match, reaches level 1, which is exactly what a sign-in decision needs. A senior clinician at the end of an escalation chain, with the record, colleagues and time, is at level 4: the model the others should copy, because the person who decides is the most senior and has everything they need. My own draft review is at level 5, and the one email my security agent may send is at level 6.

## Agents are deciders too

The scale does not care whether the decider is a person. An agent asked "is this fine to send?", with the draft and nothing else, no tools to check the record, no budget and nowhere to escalate, is a rubber stamp. The controller in [Hope or enforcement](hope-or-enforcement.md), which checks every reply against the ledger and the customer record before a second model reviews the tone, with a token budget and a path to a person, is at level 3. We should hold agents to the same standard we hold people: if an agent cannot follow up each of the data points behind its decision and say why it is there, it does not have agency either.

And the final decision should not be an agent's at all. It should be code: a decision tree in which the yes is reached through a sequence of checks, five or twenty-five of them, each of which can be followed and questioned on its own. Then it is easy to see who did what, and why. Models prepare and propose; rules decide; people own the rules.

## The review is a QA step, not a sign-off

The review as a loop: read it as the person who will sign it, question each statement, trace where it came from, classify the gap, fix the source, think better, record the outcome, and promote what is proven.

Everything so far has been about saying no well. The more interesting part is positive. When I review a draft I am not signing off. I would like to stop calling it a draft: it is QA, the stage before production, the question of whether this is ready to ship. And as in software, when the output is not what I wanted, the useful question is not how to fix this output but how we got here.

Every piece of text an agent writes is a statement, a move: based on what I know, here is the conclusion. The person who will live with that statement, who will sign it, or is the expert in that area, or is affected by it, is the one who can see the bigger picture and say: this is not right. A doctor, a project manager, a board member, an operator, a nurse, or the person at the end who signs the bottom line. When I read an email the agents have prepared, I am asking: is this a tweak to the brief, a mistake in the data, or a bigger problem? Often the answer is that the CRM record for that person is missing something, so the email cannot take it into account. The right fix is not to the email. It is to the record, the graph, the connection, so that every future email has it. Sometimes the answer is that the objectives have changed: we are trying something else now. Then the fix is to the objectives, written down where the agents will read them.

This is where the self-correction comes from that lets the whole thing scale. Every time someone with the context reviews a result and fixes the source, they validate a great many decisions and actions that came before it, and the graph gets more granular and more correct. This brief is an example. It is far more complex than what I would have given an agent six months ago, because I have learned that the better I explain the thinking behind an idea, the better the result, and because I read everything that comes back. People sometimes look at the volume and assume it is unread slop. It is not: I read it all, and it is how I learn which workflows work. [How much of this did I write?](how-much-of-this-did-i-write.md) has the numbers.

Ownership is what makes this happen. When I had a security policy I wanted adopted, I learned not to ask stakeholders to review it; I told them it would be published under their name, and the level of engagement changed completely. The same with risk: until someone has to [accept a risk](every-risk-is-already-accepted.md) in writing, they do not really engage. An email that goes out under my name gets that attention from me. And because I have the mandate, the capability and the authority to change the system, I can act on what I find.

The workflow itself keeps improving. [The agent team](the-agent-team-as-it-runs.md) labels each draft, for review or ready to send. If I want major changes, I type them into the draft, save it and change the label, and the agent picks it up on its next run. Sometimes the agent writes a draft with no recipient, so it cannot be sent by mistake, puts its questions about next steps in it, and I answer in the draft: a small interface, made of an email, that the agent then replaces with the real one. That is agency over my own environment.

## From review to rule

The top of the scale is where this goes. As the drafts of one kind keep coming back correct, exactly what I wanted, I become comfortable letting that kind go automatically, and the behaviour policy changes to allow that agent, in that setup, to send that kind of email, and nothing else. The more use cases are defined and proven, the more can be trimmed to the ones that are safe to automate, the less expertise is needed to review the rest, and the cheaper the agents doing it can be. In my experience the smaller models, Anthropic's Sonnet and even Haiku in their 5.5 versions, now reason well enough for tasks that are well defined.

It also tells you who should review what remains. The person who underwrites an agent's decision should be the most senior, the most time-pressed and the most optimised: the doctor at the end of the escalation chain, given everything needed to decide, and interrupted only for what is genuinely new.

## The law already asks for most of this

The EU AI Act's human oversight requirements and the guidance on automated decisions, mapped to the seven dimensions. Read together, they put the floor at level 3.

The EU AI Act asks for this in its own words. Article 14(4) says people overseeing a high-risk system must be enabled "to properly understand the relevant capacities and limitations" of the system, "to remain aware of the possible tendency of automatically relying or over-relying on the output", "to decide, in any particular situation, not to use" it "or to otherwise disregard, override or reverse the output", and to stop it. Article 26(2) says deployers "shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support." Read against the scale, that is a floor at level 3. Below it, the oversight is on paper only, and I would argue that for some decisions, taking them that way should not be allowed.

In the end this has very little to do with AI. People have always made decisions they could not explain; we called it judgement, and sometimes it was the same thing we now call a hallucination. What is new is that we are automating the flow, and automating a flow without explainability makes the old problem bigger. The scale is about how decisions are made, whoever makes them.

## Where to start

- **List the decision points** in a workflow, human and agent, and run each through the [assessment](https://sgit.ai/demos/vaults/agency-scale/index.md).
- **Find the weakest dimension** of each. That is the only one worth fixing first.
- **Replace identifiers with things**: every prompt shows what, which and why, in the decider's terms.
- **Make "why?" answerable**: link every draft to the sources, steps and decisions behind it.
- **Check the incentives** for a wrong yes and a wrong no, and make them match.
- **Move accountability** to whoever owns a decision point below level 3, until it is fixed.
- **Treat every review as QA**: fix the source, then record what you fixed.
- **Count the clean passes**, and turn the proven ones into rules under a behaviour policy.

*Drafted from two voice memos by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 8 October 2026. The quoted law is from Regulation (EU) 2024/1689; the cases from the public record are summarised and sourced in the vault and in Where is the why?; Bainbridge is quoted from Ironies of Automation (1983); the takeover times are from Eriksson and Stanton (2017); omission bias from Ritov and Baron (1990). Two cases are from the author's own agent team.*

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#agency-is-not-a-yes)

### Builds on

- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.

### Continued by

- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [How I work with Claude: one session per topic, agents with names, and memory you curate](how-i-work-with-claude.md) A practical guide from a year of daily use: one Claude session per topic, named agents with a role.md, curated memory, vaults, and policy before connectors.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 46 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=46)

## From the desk

- [Range is the feature, so the stop has to be designed](desk/range-is-the-feature-so-the-stop-is-designed.md) thread, 2026-10-08
- [How agents decide, and when they stop](collections/how-agents-decide.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [agency-is-not-a-yes.jpg](banners/agency-is-not-a-yes.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agency-is-not-a-yes.html)*
