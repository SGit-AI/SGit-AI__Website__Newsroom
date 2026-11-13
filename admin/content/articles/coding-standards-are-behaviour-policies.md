---
title: Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit
date: 2026-11-13
author: Dinis Cruz
author_url: about/index.html
summary: We use Agent Behaviour Policies to say what an agent may do: this database, this table, this field, a positive number. A conversation this week made a point I like: a coding standard is the same thing. "Here is how we write Python" describes a behaviour, and describing behaviour as intent is what makes a policy useful. We already keep detailed markdown standards for JavaScript, Python and the rest, and our sibling site coding.sgit.ai measured them: 31 documented rules, kept well by habit, with no linter in the estate and not one of the 31 held by a passing CI guard. Read as a behaviour policy, that is a mandate with no barrier, and the policy is what makes the gap visible. The bigger idea is what happens across teams. With fractal semantic graphs, a codebase becomes layers you can climb, from the business intent to the stories, the features, the classes and the methods; our worked example on the sgit command-line tool already reads one commit upwards to the stories it can reach. Do that across every language and every department, express the standards as common intents, and a feature that touches the back end, the front end and the data tier can be kept in step by the same intent at every layer. Building those mappings is what language models are good at.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: abp, coding-standards, fractal-semantic-graphs, agents, code-review, intent, riskmandate, article
status: published
---

!shot cbp-ladder.webp | images/ | One intent for the shopping cart, from the business down to each team's code, kept in every language. | concept

## In short {#in-short}

- **A coding standard is a behaviour policy.** It describes how an agent should behave when it writes code, the same way a policy describes what it may touch.
- **The power is that it describes intent,** not a tool's configuration, so the same intent can be kept in every language.
- **We already have these:** detailed markdown standards per language, which our coding site measured: 31 rules, kept well by habit, none held by a passing CI guard.
- **Read as a policy, that is a mandate with no barrier,** and the policy is the document that shows it.
- **Across teams, fractal semantic graphs connect the layers:** intent, stories, features, classes, methods. Change a method and you know which business requirement it serves.
- **Common intents keep teams in step:** a feature that touches the back end, the front end and the data tier carries the same intent into each.
- **Language models make the mappings affordable;** people and tests confirm them.

## The idea {#idea}

An Agent Behaviour Policy is how we write down what an agent is for: what it can reach, what the business authorised, the gap between the two, and what holds each row. The examples are usually about data. You may access this database, this table, this field, and only with a positive number.

In a conversation this week someone made the point that a coding standard is the same kind of thing, and I agree. "If you write Python, this is how you write it" is a description of behaviour. It is the agent's behaviour when the job is writing code, instead of its behaviour when the job is reading a customer record.

What makes both work is the same thing: you are describing the intent. Not "set this linter flag", but "money is never a raw number", "every input is validated where it enters", "a class does one thing and has its test". The flag is one way of keeping the intent, in one tool, for one language. The intent is what you actually want, and it survives a change of tool.

## We already write these {#ours}

!shot cbp-measured.webp | images/ | Our own house rules, measured by coding.sgit.ai: 31 rules, kept well by habit, none held by a passing CI guard. | chart

For a long time we have kept detailed markdown files that say how we code: how a Python class is laid out, how a web component is built, what a test looks like, what never goes in a file. Agents read them before they write.

Our sibling site [coding.sgit.ai](https://coding.sgit.ai/) went further and measured them against the code, across 217,266 lines in five languages, deriving every convention by counting rather than from documentation. What it found reads exactly like a behaviour policy with its gap column filled in:

- **31 documented rules,** plus 4 testing non-negotiables. That is the mandate.
- **0 linters, formatters or type-checkers** anywhere in the estate.
- **4 working CI guards,** and each one encodes an incident rather than a rule. A fifth guard has never worked: its pattern cannot match the real package name.
- **None of the 31 rules carries a passing CI guard.** In the site's own words, "the written rule set and the tested rule set do not currently overlap at all."

And yet the rules are mostly kept: banners on 100% of class-defining files, no docstrings on 99.7%, empty `__init__.py` on 99%, one class per file on 90%. They are kept by habit, by agents and people who read the standard, not by a barrier. The site also ships the configurations that would turn some of them into barriers (ruff, eslint, stylelint, a house-style test), with an honest table of what those tools cannot express.

That is the value of reading a standard as a policy. A markdown standard tells you the mandate. A policy also asks, for every rule, what holds it, and shows the rows where the answer is "nothing yet".

## From a method to the business requirement {#graph}

The second half of the idea is where it gets powerful. In [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html) I described source code as layers within layers, each a graph with its own vocabulary: what the user is trying to do, the features and flows, the components, the classes, the methods and their calls, the syntax tree.

The worked example was the sgit command-line tool: 427 files, 377 classes, 1,111 methods, 2,592 resolved calls, 72 commands and eleven stories. One commit, a bug fix of 75 lines added and 7 removed, read upwards: one method in a transport class and six command handlers changed, and the climb through the call graph reaches nine of the 72 commands and six of the eleven stories. So when you change a function, you know which stories, and so which business requirements, sit above it.

The same example ran ten of the project's house rules as queries over the graph. "No raw primitives as fields of typed classes": 19 exceptions in 755 fields. "A mirrored test file for every domain class": missing for 143 of 253. A rule becomes a shape, and a violation is a node where the shape is missing. That is a coding standard enforced as a graph query, which works the same way whatever language the graph was read from.

## Common intents across teams {#common}

Now put the two together, across a company.

Say several teams are adding a feature to the shopping cart: a returning customer can save a cart and come back to it. It needs changes in the back end, the front end and the data tier, each in its own language, each team with its own standard. Today those standards are separate documents that happen to agree, or not.

If each team's standard is written as a behaviour policy, and the policies share common intents, the picture changes:

- **The intent is written once:** money is never a raw number; every input is validated where it enters; no secrets in code; every class has its test.
- **Each language keeps it its own way:** a constrained type in Python, a validated attribute in a web component, a check constraint in SQL.
- **The graph connects the layers:** the feature, its stories, and the classes and methods each team changes, so a reviewer can see that the whole change serves the same intent at every layer, and which row in which language has no barrier yet.

That is how you keep teams in step without asking them to use the same tools. You found the common language, and it is the intent, not the syntax.

## Why language models change this {#models}

None of this was new as an idea. What made it expensive was the mapping: naming which story a method serves, which intent a rule protects, how "money is never a raw number" looks in four languages. Those were acts of human attention, and there were never enough of them.

A language model can now propose those mappings, across languages and across teams, cheaply. The proposals will be partly wrong, which is why the graph keeps them marked as proposed until something confirms them: users confirm the stories, experts confirm their layer, and tests confirm execution. Every correction is a commit to the graph files. The standards stay in markdown, readable by people and agents; the policy says what holds each one; the graph says where each one applies.

## What this does not claim {#limits}

- **The cart example is invented,** to show the shape of a shared intent; nothing here has been built for it.
- **The figures for our own rules are coding.sgit.ai's,** from its measurement published on 25 August 2026, read on 12 November.
- **The graph figures are from the worked example** in the code review article: one Python project, with hand-written stories.
- **Mapping across many languages and teams is a proposal.** The single-project graph and the measured standards exist today.

## Where this comes from {#sources}

A conversation on 12 November 2026, in my words. [coding.sgit.ai](https://coding.sgit.ai/) and [its llms.txt](https://coding.sgit.ai/llms.txt), read 12 November 2026. Earlier on this site: [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html), [introducing fractal semantic graphs](/articles/introducing-fractal-semantic-graphs.html), [behaviour policies from the checks](/articles/behaviour-policies-from-the-checks.html), [a policy for every skill](/articles/a-policy-for-every-skill.html), [governs, enforces, attests](/articles/governs-enforces-attests.html), [RiskMandate and Lovable](/articles/riskmandate-and-lovable.html).
