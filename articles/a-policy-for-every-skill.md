# A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less, sgit.ai

> I was with my friend Sean Turner this week, talking about agent behaviour policies, and he described something he built that I think is great. It is a natural-language control policy for agent skills, and a CI pipeline that checks every skill contributed to an organisation-wide repository against it before hundreds of developers pull it down to their machines. Is it safe, secure, well documented, usable, understandable by the model and understandable by people. And the part that makes it more than a linter: it reads the skill in its context. A skill that turns internal documentation into a LinkedIn post has no untrusted input to worry about; a skill that pulls content off the web is handling untrusted text, and should treat it as data, not obey it. It sits beside a security scan, not instead of one: the question is operational, is this the right way to give this skill to our workforce. That is an agent behaviour policy for a skill: the mandate is what the skill is for, the reach is everything it touches, and the gap is the risk. A control written in natural language is hope-based security, better than nothing and not enough on its own. Sean's next step is the one I keep coming back to: use an agent to write deterministic rules that follow the natural-language control, and keep the description, not the code, as the canonical version. Change the description, regenerate the code. Using models to need them less. And in a common ontology, a whole catalogue of skills becomes one graph, where the dangerous combinations are a query.

*Source: <https://newsroom.sgit.ai/articles/a-policy-for-every-skill.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less

# A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.2.0, 3 versions](versions/a-policy-for-every-skill.md) · [newsroom v0.12.36](https://newsroom.sgit.ai/admin/versions.html) · agent-skillsagent-behaviour-policynatural-language-policycipolicy-as-codesupply-chainprompt-injectionfractal-semantic-graphsgovernancearticle

***Abstract:** I was with my friend Sean Turner this week, talking about agent behaviour policies, and he described something he built that I think is great. It is a natural-language control policy for agent skills, and a CI pipeline that checks every skill contributed to an organisation-wide repository against it before hundreds of developers pull it down to their machines. Is it safe, secure, well documented, usable, understandable by the model and understandable by people. And the part that makes it more than a linter: it reads the skill in its context. A skill that turns internal documentation into a LinkedIn post has no untrusted input to worry about; a skill that pulls content off the web is handling untrusted text, and should treat it as data, not obey it. It sits beside a security scan, not instead of one: the question is operational, is this the right way to give this skill to our workforce. That is an agent behaviour policy for a skill: the mandate is what the skill is for, the reach is everything it touches, and the gap is the risk. A control written in natural language is hope-based security, better than nothing and not enough on its own. Sean's next step is the one I keep coming back to: use an agent to write deterministic rules that follow the natural-language control, and keep the description, not the code, as the canonical version. Change the description, regenerate the code. Using models to need them less. And in a common ontology, a whole catalogue of skills becomes one graph, where the dangerous combinations are a query.*

A policy for every skill. The natural-language control at the top is the canonical source; each contributed skill passes deterministic checks, a model that reads it in its context, rules an agent generated from the control, and a human review, before it reaches the organisation's repository and the developers who pull it.

## In short

- **Skills are the new dependency.** A skill is instructions an agent follows with a developer's reach, pulled by hundreds of people from one repository.
- **Sean Turner built a control for them.** A natural-language policy and a CI pipeline: is a contributed skill safe, secure, documented, usable, and understandable by the model and by people.
- **It reads the skill in context.** Internal documents in, a post out: little to worry about. Web pages in: untrusted text, to be treated as data.
- **Beside the security scan, not instead of it.** The question is operational: is this the right way to give this skill to our workforce.
- **It is a behaviour policy for a skill.** Mandate: what it is for. Reach: what it touches. Gap: the risk.
- **Natural language alone is hope-based security.** Better than nothing; it needs deterministic controls around it.
- **Use models to need them less.** An agent writes deterministic rules from the control; the description stays canonical; change it, regenerate the code.
- **A catalogue is a graph.** In a common ontology, "which skills read untrusted content, reach private data and can send it out?" is one query.

## What Sean built

I was with my friend Sean Turner this week, talking about agent behaviour policies, and he described something he had built that I liked a lot. He has a different name for it: a natural-language control policy for agent skills.

The setting is an organisation with an organisation-wide repository of skills, the packages of instructions and reference material that an agent loads to learn how to do something. Anyone can contribute one, and once it is merged, hundreds of developers can pull it down to their machines and use it. Sean's control is a policy written in plain language about what a skill must be before that happens, and a CI pipeline that checks every contribution against it: is it safe, is it secure, is it well documented, is it usable, is it understandable by the model that will load it, and is it understandable by the people who will review and maintain it. In his words, does it make sense as a reasonable skill.

What makes it more than a linter is that it reads the skill in its context. His example: a skill that publishes an article to LinkedIn, working from internal documentation, has no prompt injection risk to speak of, because nothing it reads was written by an outsider. A skill that goes and pulls content off the internet is a different thing. Everything it reads is untrusted, and the check expects the skill to say so: not to trust that input, to defang it, and to do something meaningful with it as data rather than as instructions.

And it is complementary to a security scan, not a replacement for one. A scanner asks whether a skill contains something malicious. Sean's control asks something more operational: is this the right way to contribute this skill to our workforce, given what it will touch when hundreds of people run it.

I have described it as he described it to me; I have not seen the code, and I could not find it published.

## Skills are the new dependency

This matters because a skill is code that nobody compiles. When an agent loads it, its instructions become part of what the agent does, with whatever the agent can reach: the developer's repositories, their mail, their cloud credentials. In [Attacks rewritten as mandates](attacks-rewritten-as-mandates.md) the same shift showed up from the supply side: Chainguard now publishes hardened agent skills, each with a record of the upstream commit and what was changed. That makes a skill a trustworthy input. It does not say what an agent running it should be allowed to do.

The public tooling for reviewing skills is arriving too, and it shows where the gap is. MongoDB's [guide to reviewing an agent skill](https://www.mongodb.com/docs/meta/tutorials/review-agent-skill/) describes a structural validator that "runs in CI and produces pass/fail results", and a review skill that "optionally uses an LLM judge to score content quality across multiple dimensions": clarity, actionability, token efficiency, scope discipline, directive precision, novelty. That is a good quality bar, and none of those dimensions asks where the skill's inputs come from. The guide says as much about the hardest part: "No automated tool currently reasons across skill boundaries." Sean's control asks the question the quality bar leaves out, which is the one that decides whether a skill is dangerous.

## It is a behaviour policy for a skill

Same check, different context, different verdict. Two illustrative skills described in the columns of an agent behaviour policy: one that turns internal documentation into a post, with trusted inputs and a person pressing publish; one that researches the web, with untrusted inputs and a barrier that must treat fetched text as data.

When Sean described it, I recognised the columns. An [agent behaviour policy](footprint-and-blast-radius.md) describes one agent in one setting by its mandate, what it is for; its reach, everything it can actually touch; the gap between the two, which is the risk; and the barrier in front of each row of the gap. Describe a skill that way and the context question answers itself.

The LinkedIn skill's mandate is to turn internal documentation into a post. Its reach is reading internal documents and posting to one account; its inputs are written by the organisation; the gap is posting anything other than the reviewed draft, and a person pressing publish is the barrier. The web research skill's mandate is to gather and summarise public sources. Its reach is fetching any address and writing into the workspace; its inputs can be written by anyone; the gap is following an instruction found inside a page, and the barrier has to be treating fetched text as data.

Put that next to the rest of what the skill can reach and you have the most useful question in agent security. Simon Willison named [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): "Access to your private data", "Exposure to untrusted content", and "The ability to externally communicate in a way that could be used to steal your data". A skill with untrusted inputs is one leg. Whether the agent loading it has the other two is a property of where it runs, which is why [The policy draws the liability line](the-policy-draws-the-liability-line.md) argued that anything with the trifecta should take a behaviour policy beside its prompt.

## Hope-based security, and why it is still worth writing

A control written in natural language, checked by a model, is what I call hope-based security. You give the model the rule and you hope it follows it. [Hope or enforcement](hope-or-enforcement.md) measured the cost for one customer service agent: built the obvious way, 97% of its rules were kept only by the model's good behaviour.

But I agree with Sean that it is far better than not having it. A written control is the only place the intent exists. It is what a reviewer reads, what a model can check a skill against, and what the deterministic rules are written from. Without it, there is nothing to enforce, only code that nobody can explain. With it, the question becomes how much of it can be wrapped in something that does not hope.

## Use models to need them less

That is where Sean's next step comes in, and it is the part of the conversation I liked most. Use an agent to write deterministic rules that follow the natural-language control. For example, a skill that declares it reads the web gets a rule that checks it routes fetched content through a step that treats it as data. A skill that can post externally gets a rule that it has a human step before it does. The model reads the control once and writes code; from then on, the code runs, the same way every time, at no model cost per run.

I usually put that as using models to not use models. The model is the author of the deterministic part, not the judge of every case. And the natural-language control is, in effect, the requirements document for those rules.

Then the rule that makes it work: the description stays the canonical version, not the code. If the control changes, you change the description and regenerate the code. That is the same round trip [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) ran this week with Open Policy Agent: rows of a behaviour policy generated into Rego, the requests decided, and the code parsed back to find the rows with no code and the code with no row. AWS has built a version of it into a product: its agent [policy service](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) lets developers "describe rules in plain English instead of writing formal policy code in Cedar", generates candidate policies, and checks them for being "overly permissive, overly restrictive, or contain conditions that can never be satisfied". The direction is the same everywhere: people write intent, models write enforcement, and the intent stays the source.

## A catalogue is a graph

The last piece is what happens at the scale Sean is working at: not one skill, but hundreds, contributed by different people, describing themselves in different words. My approach to that is to bring them to a common ontology, the way [fractal semantic graphs](introducing-fractal-semantic-graphs.md) do: every skill described by the same columns, mandate, reach, inputs and their trust, barriers, as nodes with named edges, while each skill keeps its own text.

Then the questions that matter across a catalogue are queries, not reviews. Which skills read untrusted content, and which of those can also reach private data and send something out? Which skills changed their reach since they were approved? Which declared a barrier that no generated rule enforces? MongoDB's guide is right that no tool reasons across skill boundaries today. A graph of skills in a common vocabulary is how one could.

## From policy to licence to insurance

All of this is open source on our side, and it follows the line I keep drawing at [RiskMandate](https://riskmandate.ai): describe the behaviour in a policy; from the policy, grant a [licence to operate](https://riskmandate.ai/licence-to-operate.html) that can be checked and revoked; and from a policy with a record behind it, make the agent insurable. To be clear about where that stands, as [Ten hard questions for RiskMandate](riskmandate-ten-questions.md) put it: "we make agents insurable. We do not insure them." The licence to operate and the insurability index are designs.

A skill with a policy, checked at contribution and enforced where it runs, is the smallest version of that whole chain. Sean has built the first link.

## What this does not claim

- **Sean's tool is described from a conversation.** I have not seen its code, and I could not find it published; the details are his, as he told them, and any errors are mine.
- **The two skills in the figure are illustrations.** They follow his examples; they are not skills from his repository.
- **Generated rules are only as good as the control.** A model can write a rule that checks the wrong thing; the rules need tests and review like any code.
- **A barrier written as "treat it as data" is still an expectation** until something outside the skill enforces it.
- **Licence to operate and insurability are designs,** not products a customer runs today.

If you are running an organisation-wide skills repository, or you have built something like Sean's, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A conversation with Sean Turner on 14 October 2026, recorded as a voice memo of mine, and written up by this site's agent in the voice of this site; the argument and the editorial responsibility are mine, and Sean's work is credited to him. Sean read the article on 14 October 2026 and agreed to be named. MongoDB, [How to Review an Agent Skill](https://www.mongodb.com/docs/meta/tutorials/review-agent-skill/); AWS, [Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html); Simon Willison, [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), 16 June 2025. All read on 14 October 2026.

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#a-policy-for-every-skill)

### Builds on

- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](attacks-rewritten-as-mandates.md) 28 supply-chain attacks read as reach beyond mandate: what a hardened registry stops, what only a written mandate can, and why agents change it.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.

### Continued by

- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in](chainguard-mapped.md) Chainguard mapped from OS to agents, its public feeds counted, and the context layer above the package where an open policy and a vault fit.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 111 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=111)

**Posting this article on LinkedIn?** The cover is [a-policy-for-every-skill.jpg](banners/a-policy-for-every-skill.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-policy-for-every-skill.html)*
