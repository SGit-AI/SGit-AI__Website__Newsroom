# Knowing when to stop: what experience gives people, and what we have to design into agents, sgit.ai

> The hardest call in most work is not what to do next but when to stop. This article starts with people, because the problem is not new: security champions who had automated away whole classes of bugs and ended up debating whether GUIDs were random enough; development teams that hit every KPI and did not move the business; teams that found more work for themselves as they grew. What stopped them, when something did, was perspective: knowing who the attackers are, which phase the business is in, where the bottleneck is, and what good enough looks like, which is much of what seniority is. Agents have the same problem, worse. Their range is the feature: they can go in any direction, and variability is what makes them useful. But that range means they will keep going, fixing the twenty things they noticed rather than the one that mattered. The answer, for both, is not draconian rules but constraints that carry perspective: direction, a mandate, memory with the bigger picture, graphs that narrow the scope, a stop named before the work begins, one kind of work per step, and shipping often enough that the users tell you whether it mattered.

*Source: <https://newsroom.sgit.ai/articles/knowing-when-to-stop.html> · sgit.ai v0.7.46 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Knowing when to stop: what experience gives people, and what we have to design into agents

# Knowing when to stop: what experience gives people, and what we have to design into agents

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-08 · [article v1.0.0](versions/knowing-when-to-stop.md) · [sgit.ai v0.7.6](https://sgit.ai/admin/versions.md) · agentsknowing-when-to-stopdiminishing-returnssenioritysecuritythreat-modellingkpisgoodhartwardley-mapsconstraintsfireshippingagent-behaviour-policyarticle

***Abstract:** The hardest call in most work is not what to do next but when to stop. This article starts with people, because the problem is not new: security champions who had automated away whole classes of bugs and ended up debating whether GUIDs were random enough; development teams that hit every KPI and did not move the business; teams that found more work for themselves as they grew. What stopped them, when something did, was perspective: knowing who the attackers are, which phase the business is in, where the bottleneck is, and what good enough looks like, which is much of what seniority is. Agents have the same problem, worse. Their range is the feature: they can go in any direction, and variability is what makes them useful. But that range means they will keep going, fixing the twenty things they noticed rather than the one that mattered. The answer, for both, is not draconian rules but constraints that carry perspective: direction, a mandate, memory with the bigger picture, graphs that narrow the scope, a stop named before the work begins, one kind of work per step, and shipping often enough that the users tell you whether it mattered.*

Value rises fast, then flattens. Past the point of diminishing returns, more work is optimising the wrong thing, defending against a movie plot, or hitting a target that no longer moves the business. What tells you to stop is perspective, and for an agent it has to be designed in.

**Where this comes from.** A voice memo recorded after [Agency is not a yes](agency-is-not-a-yes.md), which is the article to read first: knowing when to stop is one of the things agency is for. The examples are from my own career, mostly in application security and as a CISO; the people in them are not named. Several earlier articles on this site meet here, and are linked where they do.

## In short

- **Knowing when to stop is the hard part**, for people and for agents. Past the point of diminishing returns, more work is not more value.
- **For people, perspective is what stops them**: who the attackers are, which phase the business is in, where the bottleneck is, what good enough looks like. Much of what we call seniority is that perspective.
- **Good teams can go too far.** The best security teams ran out of real work and started defending against movie plots; the best delivery teams hit every KPI and did not move the business.
- **Agents have the same problem, by design.** Their range is the feature: they can go in any direction. That also means they will keep going, unless something tells them to stop.
- **The answer is constraints that carry perspective**, not draconian rules: direction, a mandate, the bigger picture in memory, graphs that narrow the scope, a stop named in advance, one kind of work per step, and shipping often enough to see whether it mattered.

## Variability is the feature

I said in [How much of this did I write?](how-much-of-this-did-i-write.md) that a model that can go in every direction needs someone with a direction. That is not a defect to be engineered away. It is what makes these systems special. The ability to try different things, to go in directions nobody asked for, to vary from one run to the next, is close to what we would call creativity in a person. We often call it hallucination, and I think variability is the better name for it; it feels surprising because we do not yet understand it well. But it has a consequence. An entity that can go anywhere has no natural reason to stop anywhere.

People have the same problem, with one difference. Before getting to agents, it is worth looking at how it shows up in human teams, because none of it is new.

## What seniority gives you

When I was doing a lot of application security, a friend told me: when you become a CISO, you will not care about half of what you care about now. He was right. When I became one, although I came from AppSec, I chose to put much of the effort and the budget elsewhere. In the organisations I worked in, the development teams were often very good, and the gaps were in other areas. From the board and the executive table you see the company's strategy, where the business is going, and the whole set of risks it actually carries. Against that picture, some of what had seemed urgent from inside AppSec was not the most important thing to worry about.

That is a large part of what experience is: not only having lived through similar situations, but having the bigger picture, and being able to move between the tactical and the strategic. And the bigger picture is mostly what tells you when to stop.

## When good teams run out of real work

The clearest example I have comes from the time when security stopped being whack-a-mole and became proactive: security champions in the teams, threat modelling, code review, checks running in CI. The best teams treated security, correctly, as an engineering problem, a quality problem, a class of bug. And almost every security issue at that level can be brought down to a practice a good team simply does. Dependency management: of course. Input validation: why would you accept crazy inputs? Authorisation: how can you not know what your code and your users are doing? Injection: use strong schemas, and keep code and data apart.

Those teams ran out of things to do, which was great. Then some of them started to focus too much. I remember being called into a meeting where security champions and developers were debating whether GUIDs were random enough. A version 4 UUID has 122 random bits, around 5.3 × 10^36 possible values. Guessing one is not a realistic attack; repeated guesses can be detected; and there was no plausible path from a predictable GUID to harm in that system. It was a movie plot, in the phrase Bruce Schneier popularised for the dramatic threats we imagine instead of the ordinary ones that happen. Real attacks are mostly much simpler: someone asks someone to run this, install that, or hand over a key.

What I found myself doing, in that meeting and in many others across the business, was giving people permission to take risks. Not common sense, because that implies they did not have it, but perspective: yes, that is technically possible, and it does not matter here, because of who our attackers are, what else is in place and what we are protecting. People new to security tend to worry most, because security can be visceral: you see that something is possible and it feels urgent. The way to bring the perspective back is to map who the attackers actually are, which is what [Who are you protecting against?](who-are-you-protecting-against.md) does, tier by tier.

## Crushing every KPI and not moving the needle

The second example is more relevant to agents. Once a business is mature enough to set objectives and key results and key performance indicators, it can hand them to a team of very good engineers, and very good engineers are excellent at working backwards from a metric. I was in meetings where the development teams were hitting every KPI, delivering everything, and the business was not moving. In a way they should have been more constrained, and told when to stop. When a measure becomes a target, in Marilyn Strathern's well-known phrasing of Goodhart's law, it ceases to be a good measure.

This is where a [Wardley map](https://wardley-maps.sgit.ai/) earns its place. It tells you which phase each part of the business is in. If you are still exploring, still trying to find what makes the business accelerate, polish is waste and the most important skill is knowing when to stop. If something is a commodity being town-planned, the same polish may be exactly right. A map also shows where the bottleneck is, and I have seen teams optimise, beautifully, things that did not need optimising. Somebody has to make the call not to fix this bug, not to build that feature, not to improve the thing that is already good enough. That call is often harder than doing the work, and it belongs to whoever has the context: a person, or an agent that has been given it.

## Art is knowing when to stop

I once heard an artist say that art is knowing when to stop. Knowing what is good enough, and recognising the point of diminishing returns, is the same skill. Teams without vision or direction struggle with it, because they have nothing to measure "enough" against.

The best feedback loop I know for it is shipping, often and early. Are people using it? Does it matter? Did what we just did move anything? If not, stop, and do something else. That is also why observability matters: it is how you find out whether the work changed anything outside the team. I made the same argument for founders in [Every mistake added a rule](every-mistake-added-a-rule.md): ship, then stop, and let the components compound.

## Why it is harder for agents

A person's range is limited. There is only so much one person can think of doing, wants to do, or believes is valuable, and their expertise keeps them in a domain, which, ironically, is what makes them qualified there. An LLM has a far wider set of skills, and it can just keep going. Anyone who uses one has seen this. You ask it to fix a small thing and it fixes a bigger one, because it can. It sees twenty things that are wrong and has a go at all of them. It starts optimising things nobody asked it to touch. At that moment it does not have the perspective to know that nineteen of the twenty do not matter, or matter later, or are someone else's.

There is nothing uniquely agentic about this. Put an entity that can do work into a team without a pile of real tasks and a clear direction, and it will make itself busy. People do the same. C. Northcote Parkinson observed in 1955 that "work expands so as to fill the time available for its completion", and argued that officials make work for each other. In the past we dealt with it through constraints that were often artificial and draconian, like fixed limits on team size, because we had no better control. The real problems were communication and direction, not the number.

## Constraints that carry perspective

The better answer is constraints that carry the bigger picture, rather than rules that only forbid. Dan Ward's FIRE, fast, inexpensive, restrained and elegant, is one name for that attitude, and it is one of the doctrines on [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/): small scope on purpose, so that focus is the default.

Looked at this way, much of what we have been building is machinery for knowing when to stop:

- **Direction**: briefs that explain the thinking and the objective, not only the task, so an agent can judge what matters. The better I explain the why, the better the result.
- **A mandate**: an [Agent Behaviour Policy](https://abp.sgit.ai/) and tools that only reach what the job needs, so the agent's universe of the possible is the size of the job. [Hope or enforcement](hope-or-enforcement.md) shows what that does to a customer service agent.
- **Memory with the bigger picture**: vaults and pages that hold the strategy, the threats and the history, so the perspective a senior person carries in their head is in the agent's context too. That is what [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) argues memory is for.
- **Graphs that narrow the scope**: semantic and flow graphs say what connects to what, and therefore what is in and out of scope for this step.
- **A stop named in advance**: as nfrs.sgit.ai puts it for budgets, "with the stopping point named while it is still cheap to name". For an agent that is a token budget on the step, set before it starts.
- **One kind of work per step**: [the agent team](the-agent-team-as-it-runs.md) runs each agent for one step of up to twelve minutes: read state, do one kind of work, write state, stop.
- **A reviewer with agency**: someone with the context to say "good enough", or "not this, that", which is the scale in [Agency is not a yes](agency-is-not-a-yes.md).
- **Shipping**, so the users answer the question of whether it mattered.

None of these is a rule that says "do less". Each puts the bigger picture where the decision is made, which is what lets a person, or an agent, decide that the next thing is not worth doing.

## Where to start

- **Name the stop before you start**: a time, a token budget, or a result that counts as good enough.
- **Write down which phase you are in**: exploring, settling or town planning. The right amount of polish follows from it.
- **Give the agent the bigger picture**: the objective, the threats, what else is in place, not only the task.
- **Measure the needle, not only the KPI**: ship, watch what people do, and stop when it stops moving.
- **One kind of work per step**, with a budget, and a review by someone who can say "enough".
- **Give explicit permission to leave things undone**, and write down what was left and why.

*Drafted from a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 8 October 2026. The people in the examples are not named. The UUID figures are from the version 4 layout in RFC 9562; Parkinson's sentence is from his essay in The Economist of 19 November 1955; the phrasing of Goodhart's law is Marilyn Strathern's, from 1997; FIRE is the title of Dan Ward's 2014 book.*

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#knowing-when-to-stop)

### Builds on

- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [Who are you protecting against? Draw the security line where the attacker is, not above it](who-are-you-protecting-against.md) Before deciding how secure to be, name the attacker: a six-tier ladder, an air-gapped Mac mini read against it, and eight startups drawing their line.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.

### Continued by

- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Range is the feature, so the stop has to be designed](desk/range-is-the-feature-so-the-stop-is-designed.md) thread, 2026-10-08
- [How agents decide, and when they stop](collections/how-agents-decide.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [knowing-when-to-stop.jpg](banners/knowing-when-to-stop.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/knowing-when-to-stop.html)*
