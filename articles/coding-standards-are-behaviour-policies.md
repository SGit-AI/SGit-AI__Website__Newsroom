# Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit, sgit.ai

> We use Agent Behaviour Policies to say what an agent may do: this database, this table, this field, a positive number. A conversation this week made a point I like: a coding standard is the same thing. "Here is how we write Python" describes a behaviour, and describing behaviour as intent is what makes a policy useful. We already keep detailed markdown standards for JavaScript, Python and the rest, and our sibling site coding.sgit.ai measured them: 31 documented rules, kept well by habit, with no linter in the estate and not one of the 31 held by a passing CI guard. Read as a behaviour policy, that is a mandate with no barrier, and the policy is what makes the gap visible. The bigger idea is what happens across teams. With fractal semantic graphs, a codebase becomes layers you can climb, from the business intent to the stories, the features, the classes and the methods; our worked example on the sgit command-line tool already reads one commit upwards to the stories it can reach. Do that across every language and every department, express the standards as common intents, and a feature that touches the back end, the front end and the data tier can be kept in step by the same intent at every layer. Building those mappings is what language models are good at.

*Source: <https://newsroom.sgit.ai/articles/coding-standards-are-behaviour-policies.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit

# Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-13 · [article v1.0.0](versions/coding-standards-are-behaviour-policies.md) · [newsroom v0.14.79](https://newsroom.sgit.ai/admin/versions.html) · abpcoding-standardsfractal-semantic-graphsagentscode-reviewintentriskmandatearticle

***Abstract:** We use Agent Behaviour Policies to say what an agent may do: this database, this table, this field, a positive number. A conversation this week made a point I like: a coding standard is the same thing. "Here is how we write Python" describes a behaviour, and describing behaviour as intent is what makes a policy useful. We already keep detailed markdown standards for JavaScript, Python and the rest, and our sibling site coding.sgit.ai measured them: 31 documented rules, kept well by habit, with no linter in the estate and not one of the 31 held by a passing CI guard. Read as a behaviour policy, that is a mandate with no barrier, and the policy is what makes the gap visible. The bigger idea is what happens across teams. With fractal semantic graphs, a codebase becomes layers you can climb, from the business intent to the stories, the features, the classes and the methods; our worked example on the sgit command-line tool already reads one commit upwards to the stories it can reach. Do that across every language and every department, express the standards as common intents, and a feature that touches the back end, the front end and the data tier can be kept in step by the same intent at every layer. Building those mappings is what language models are good at.*

One intent for the shopping cart, from the business down to each team's code, kept in every language.

## In short

- **A coding standard is a behaviour policy.** It describes how an agent should behave when it writes code, the same way a policy describes what it may touch.
- **The power is that it describes intent,** not a tool's configuration, so the same intent can be kept in every language.
- **We already have these:** detailed markdown standards per language, which our coding site measured: 31 rules, kept well by habit, none held by a passing CI guard.
- **Read as a policy, that is a mandate with no barrier,** and the policy is the document that shows it.
- **Across teams, fractal semantic graphs connect the layers:** intent, stories, features, classes, methods. Change a method and you know which business requirement it serves.
- **Common intents keep teams in step:** a feature that touches the back end, the front end and the data tier carries the same intent into each.
- **Language models make the mappings affordable;** people and tests confirm them.

## The idea

An Agent Behaviour Policy is how we write down what an agent is for: what it can reach, what the business authorised, the gap between the two, and what holds each row. The examples are usually about data. You may access this database, this table, this field, and only with a positive number.

In a conversation this week someone made the point that a coding standard is the same kind of thing, and I agree. "If you write Python, this is how you write it" is a description of behaviour. It is the agent's behaviour when the job is writing code, instead of its behaviour when the job is reading a customer record.

What makes both work is the same thing: you are describing the intent. Not "set this linter flag", but "money is never a raw number", "every input is validated where it enters", "a class does one thing and has its test". The flag is one way of keeping the intent, in one tool, for one language. The intent is what you actually want, and it survives a change of tool.

## We already write these

Our own house rules, measured by coding.sgit.ai: 31 rules, kept well by habit, none held by a passing CI guard.

For a long time we have kept detailed markdown files that say how we code: how a Python class is laid out, how a web component is built, what a test looks like, what never goes in a file. Agents read them before they write.

Our sibling site [coding.sgit.ai](https://coding.sgit.ai/) went further and measured them against the code, across 217,266 lines in five languages, deriving every convention by counting rather than from documentation. What it found reads exactly like a behaviour policy with its gap column filled in:

- **31 documented rules,** plus 4 testing non-negotiables. That is the mandate.
- **0 linters, formatters or type-checkers** anywhere in the estate.
- **4 working CI guards,** and each one encodes an incident rather than a rule. A fifth guard has never worked: its pattern cannot match the real package name.
- **None of the 31 rules carries a passing CI guard.** In the site's own words, "the written rule set and the tested rule set do not currently overlap at all."

And yet the rules are mostly kept: banners on 100% of class-defining files, no docstrings on 99.7%, empty `__init__.py` on 99%, one class per file on 90%. They are kept by habit, by agents and people who read the standard, not by a barrier. The site also ships the configurations that would turn some of them into barriers (ruff, eslint, stylelint, a house-style test), with an honest table of what those tools cannot express.

That is the value of reading a standard as a policy. A markdown standard tells you the mandate. A policy also asks, for every rule, what holds it, and shows the rows where the answer is "nothing yet".

## From a method to the business requirement

The second half of the idea is where it gets powerful. In [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) I described source code as layers within layers, each a graph with its own vocabulary: what the user is trying to do, the features and flows, the components, the classes, the methods and their calls, the syntax tree.

The worked example was the sgit command-line tool: 427 files, 377 classes, 1,111 methods, 2,592 resolved calls, 72 commands and eleven stories. One commit, a bug fix of 75 lines added and 7 removed, read upwards: one method in a transport class and six command handlers changed, and the climb through the call graph reaches nine of the 72 commands and six of the eleven stories. So when you change a function, you know which stories, and so which business requirements, sit above it.

The same example ran ten of the project's house rules as queries over the graph. "No raw primitives as fields of typed classes": 19 exceptions in 755 fields. "A mirrored test file for every domain class": missing for 143 of 253. A rule becomes a shape, and a violation is a node where the shape is missing. That is a coding standard enforced as a graph query, which works the same way whatever language the graph was read from.

## Common intents across teams

Now put the two together, across a company.

Say several teams are adding a feature to the shopping cart: a returning customer can save a cart and come back to it. It needs changes in the back end, the front end and the data tier, each in its own language, each team with its own standard. Today those standards are separate documents that happen to agree, or not.

If each team's standard is written as a behaviour policy, and the policies share common intents, the picture changes:

- **The intent is written once:** money is never a raw number; every input is validated where it enters; no secrets in code; every class has its test.
- **Each language keeps it its own way:** a constrained type in Python, a validated attribute in a web component, a check constraint in SQL.
- **The graph connects the layers:** the feature, its stories, and the classes and methods each team changes, so a reviewer can see that the whole change serves the same intent at every layer, and which row in which language has no barrier yet.

That is how you keep teams in step without asking them to use the same tools. You found the common language, and it is the intent, not the syntax.

## Why language models change this

None of this was new as an idea. What made it expensive was the mapping: naming which story a method serves, which intent a rule protects, how "money is never a raw number" looks in four languages. Those were acts of human attention, and there were never enough of them.

A language model can now propose those mappings, across languages and across teams, cheaply. The proposals will be partly wrong, which is why the graph keeps them marked as proposed until something confirms them: users confirm the stories, experts confirm their layer, and tests confirm execution. Every correction is a commit to the graph files. The standards stay in markdown, readable by people and agents; the policy says what holds each one; the graph says where each one applies.

## What this does not claim

- **The cart example is invented,** to show the shape of a shared intent; nothing here has been built for it.
- **The figures for our own rules are coding.sgit.ai's,** from its measurement published on 25 August 2026, read on 12 November.
- **The graph figures are from the worked example** in the code review article: one Python project, with hand-written stories.
- **Mapping across many languages and teams is a proposal.** The single-project graph and the measured standards exist today.

## Where this comes from

A conversation on 12 November 2026, in my words. [coding.sgit.ai](https://coding.sgit.ai/) and [its llms.txt](https://coding.sgit.ai/llms.txt), read 12 November 2026. Earlier on this site: [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md), [introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [a policy for every skill](a-policy-for-every-skill.md), [governs, enforces, attests](governs-enforces-attests.md), [RiskMandate and Lovable](riskmandate-and-lovable.md).

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#coding-standards-are-behaviour-policies)

### Builds on

- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [RiskMandate and Lovable: mapping an Agent Behaviour Policy onto an app builder whose agent writes the code, changes the live database, connects your other systems and publishes, with the controls Lovable already gives and their defaults](riskmandate-and-lovable.md) Lovable's agent can change production; its controls are real, its defaults open, and a policy says what each project's agent may do.

### Continued by

- [A film studio on a laptop: Claude builds, animates and renders a 26-second RiskMandate film in Unreal Engine 5.8 on an unattended MacBook Air, with no mouse and nobody at the keyboard](a-film-studio-on-a-laptop.md) Claude built, animated and rendered a 26-second RiskMandate film in Unreal Engine 5.8 on an unattended laptop.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 393 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=393)

**Posting this article on LinkedIn?** The cover is [coding-standards-are-behaviour-policies.jpg](banners/coding-standards-are-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/coding-standards-are-behaviour-policies.html)*
