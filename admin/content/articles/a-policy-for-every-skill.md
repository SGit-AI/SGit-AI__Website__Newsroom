---
title: A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: I was with my friend Sean Turner this week, talking about agent behaviour policies, and he described something he built that I think is great. It is a natural-language control policy for agent skills, and a CI pipeline that checks every skill contributed to an organisation-wide repository against it before hundreds of developers pull it down to their machines. Is it safe, secure, well documented, usable, understandable by the model and understandable by people. And the part that makes it more than a linter: it reads the skill in its context. A skill that turns internal documentation into a LinkedIn post has no untrusted input to worry about; a skill that pulls content off the web is handling untrusted text, and should treat it as data, not obey it. It sits beside a security scan, not instead of one: the question is operational, is this the right way to give this skill to our workforce. That is an agent behaviour policy for a skill: the mandate is what the skill is for, the reach is everything it touches, and the gap is the risk. A control written in natural language is hope-based security, better than nothing and not enough on its own. Sean's next step is the one I keep coming back to: use an agent to write deterministic rules that follow the natural-language control, and keep the description, not the code, as the canonical version. Change the description, regenerate the code. Using models to need them less. And in a common ontology, a whole catalogue of skills becomes one graph, where the dangerous combinations are a query.
version: v0.12.36
license: https://creativecommons.org/licenses/by/4.0/
tags: agent-skills, agent-behaviour-policy, natural-language-policy, ci, policy-as-code, supply-chain, prompt-injection, fractal-semantic-graphs, governance, article
status: published
---

!shot sk-pipeline.webp | images/ | A policy for every skill. The natural-language control at the top is the canonical source; each contributed skill passes deterministic checks, a model that reads it in its context, rules an agent generated from the control, and a human review, before it reaches the organisation's repository and the developers who pull it. | architecture

## In short {#in-short}

- **Skills are the new dependency.** A skill is instructions an agent follows with a developer's reach, pulled by hundreds of people from one repository.
- **Sean Turner built a control for them.** A natural-language policy and a CI pipeline: is a contributed skill safe, secure, documented, usable, and understandable by the model and by people.
- **It reads the skill in context.** Internal documents in, a post out: little to worry about. Web pages in: untrusted text, to be treated as data.
- **Beside the security scan, not instead of it.** The question is operational: is this the right way to give this skill to our workforce.
- **It is a behaviour policy for a skill.** Mandate: what it is for. Reach: what it touches. Gap: the risk.
- **Natural language alone is hope-based security.** Better than nothing; it needs deterministic controls around it.
- **Use models to need them less.** An agent writes deterministic rules from the control; the description stays canonical; change it, regenerate the code.
- **A catalogue is a graph.** In a common ontology, "which skills read untrusted content, reach private data and can send it out?" is one query.

## What Sean built {#built}

I was with my friend Sean Turner this week, talking about agent behaviour policies, and he described something he had built that I liked a lot. He has a different name for it: a natural-language control policy for agent skills.

The setting is an organisation with an organisation-wide repository of skills, the packages of instructions and reference material that an agent loads to learn how to do something. Anyone can contribute one, and once it is merged, hundreds of developers can pull it down to their machines and use it. Sean's control is a policy written in plain language about what a skill must be before that happens, and a CI pipeline that checks every contribution against it: is it safe, is it secure, is it well documented, is it usable, is it understandable by the model that will load it, and is it understandable by the people who will review and maintain it. In his words, does it make sense as a reasonable skill.

What makes it more than a linter is that it reads the skill in its context. His example: a skill that publishes an article to LinkedIn, working from internal documentation, has no prompt injection risk to speak of, because nothing it reads was written by an outsider. A skill that goes and pulls content off the internet is a different thing. Everything it reads is untrusted, and the check expects the skill to say so: not to trust that input, to defang it, and to do something meaningful with it as data rather than as instructions.

And it is complementary to a security scan, not a replacement for one. A scanner asks whether a skill contains something malicious. Sean's control asks something more operational: is this the right way to contribute this skill to our workforce, given what it will touch when hundreds of people run it.

I have described it as he described it to me; I have not seen the code, and I could not find it published.

## Skills are the new dependency {#dependency}

This matters because a skill is code that nobody compiles. When an agent loads it, its instructions become part of what the agent does, with whatever the agent can reach: the developer's repositories, their mail, their cloud credentials. In [Attacks rewritten as mandates](/articles/attacks-rewritten-as-mandates.html) the same shift showed up from the supply side: Chainguard now publishes hardened agent skills, each with a record of the upstream commit and what was changed. That makes a skill a trustworthy input. It does not say what an agent running it should be allowed to do.

The public tooling for reviewing skills is arriving too, and it shows where the gap is. MongoDB's [guide to reviewing an agent skill](https://www.mongodb.com/docs/meta/tutorials/review-agent-skill/) describes a structural validator that "runs in CI and produces pass/fail results", and a review skill that "optionally uses an LLM judge to score content quality across multiple dimensions": clarity, actionability, token efficiency, scope discipline, directive precision, novelty. That is a good quality bar, and none of those dimensions asks where the skill's inputs come from. The guide says as much about the hardest part: "No automated tool currently reasons across skill boundaries." Sean's control asks the question the quality bar leaves out, which is the one that decides whether a skill is dangerous.

## It is a behaviour policy for a skill {#abp}

!shot sk-context.webp | images/ | Same check, different context, different verdict. Two illustrative skills described in the columns of an agent behaviour policy: one that turns internal documentation into a post, with trusted inputs and a person pressing publish; one that researches the web, with untrusted inputs and a barrier that must treat fetched text as data. | comparison

When Sean described it, I recognised the columns. An [agent behaviour policy](/articles/footprint-and-blast-radius.html) describes one agent in one setting by its mandate, what it is for; its reach, everything it can actually touch; the gap between the two, which is the risk; and the barrier in front of each row of the gap. Describe a skill that way and the context question answers itself.

The LinkedIn skill's mandate is to turn internal documentation into a post. Its reach is reading internal documents and posting to one account; its inputs are written by the organisation; the gap is posting anything other than the reviewed draft, and a person pressing publish is the barrier. The web research skill's mandate is to gather and summarise public sources. Its reach is fetching any address and writing into the workspace; its inputs can be written by anyone; the gap is following an instruction found inside a page, and the barrier has to be treating fetched text as data.

Put that next to the rest of what the skill can reach and you have the most useful question in agent security. Simon Willison named [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): "Access to your private data", "Exposure to untrusted content", and "The ability to externally communicate in a way that could be used to steal your data". A skill with untrusted inputs is one leg. Whether the agent loading it has the other two is a property of where it runs, which is why [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html) argued that anything with the trifecta should take a behaviour policy beside its prompt.

## Hope-based security, and why it is still worth writing {#hope}

A control written in natural language, checked by a model, is what I call hope-based security. You give the model the rule and you hope it follows it. [Hope or enforcement](/articles/hope-or-enforcement.html) measured the cost for one customer service agent: built the obvious way, 97% of its rules were kept only by the model's good behaviour.

But I agree with Sean that it is far better than not having it. A written control is the only place the intent exists. It is what a reviewer reads, what a model can check a skill against, and what the deterministic rules are written from. Without it, there is nothing to enforce, only code that nobody can explain. With it, the question becomes how much of it can be wrapped in something that does not hope.

## Use models to need them less {#codify}

That is where Sean's next step comes in, and it is the part of the conversation I liked most. Use an agent to write deterministic rules that follow the natural-language control. For example, a skill that declares it reads the web gets a rule that checks it routes fetched content through a step that treats it as data. A skill that can post externally gets a rule that it has a human step before it does. The model reads the control once and writes code; from then on, the code runs, the same way every time, at no model cost per run.

I usually put that as using models to not use models. The model is the author of the deterministic part, not the judge of every case. And the natural-language control is, in effect, the requirements document for those rules.

Then the rule that makes it work: the description stays the canonical version, not the code. If the control changes, you change the description and regenerate the code. That is the same round trip [Policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html) ran this week with Open Policy Agent: rows of a behaviour policy generated into Rego, the requests decided, and the code parsed back to find the rows with no code and the code with no row. AWS has built a version of it into a product: its agent [policy service](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) lets developers "describe rules in plain English instead of writing formal policy code in Cedar", generates candidate policies, and checks them for being "overly permissive, overly restrictive, or contain conditions that can never be satisfied". The direction is the same everywhere: people write intent, models write enforcement, and the intent stays the source.

## A catalogue is a graph {#graph}

The last piece is what happens at the scale Sean is working at: not one skill, but hundreds, contributed by different people, describing themselves in different words. My approach to that is to bring them to a common ontology, the way [fractal semantic graphs](/articles/introducing-fractal-semantic-graphs.html) do: every skill described by the same columns, mandate, reach, inputs and their trust, barriers, as nodes with named edges, while each skill keeps its own text.

Then the questions that matter across a catalogue are queries, not reviews. Which skills read untrusted content, and which of those can also reach private data and send something out? Which skills changed their reach since they were approved? Which declared a barrier that no generated rule enforces? MongoDB's guide is right that no tool reasons across skill boundaries today. A graph of skills in a common vocabulary is how one could.

## From policy to licence to insurance {#licence}

All of this is open source on our side, and it follows the line I keep drawing at [RiskMandate](https://riskmandate.ai): describe the behaviour in a policy; from the policy, grant a [licence to operate](https://riskmandate.ai/licence-to-operate.html) that can be checked and revoked; and from a policy with a record behind it, make the agent insurable. To be clear about where that stands, as [Ten hard questions for RiskMandate](/articles/riskmandate-ten-questions.html) put it: "we make agents insurable. We do not insure them." The licence to operate and the insurability index are designs.

A skill with a policy, checked at contribution and enforced where it runs, is the smallest version of that whole chain. Sean has built the first link.

## What this does not claim {#limits}

- **Sean's tool is described from a conversation.** I have not seen its code, and I could not find it published; the details are his, as he told them, and any errors are mine.
- **The two skills in the figure are illustrations.** They follow his examples; they are not skills from his repository.
- **Generated rules are only as good as the control.** A model can write a rule that checks the wrong thing; the rules need tests and review like any code.
- **A barrier written as "treat it as data" is still an expectation** until something outside the skill enforces it.
- **Licence to operate and insurability are designs,** not products a customer runs today.

If you are running an organisation-wide skills repository, or you have built something like Sean's, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A conversation with Sean Turner on 14 October 2026, recorded as a voice memo of mine, and written up by this site's agent in the voice of this site; the argument and the editorial responsibility are mine, and Sean's work is credited to him. Sean read the article on 14 October 2026 and agreed to be named. MongoDB, [How to Review an Agent Skill](https://www.mongodb.com/docs/meta/tutorials/review-agent-skill/); AWS, [Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html); Simon Willison, [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), 16 June 2025. All read on 14 October 2026.
