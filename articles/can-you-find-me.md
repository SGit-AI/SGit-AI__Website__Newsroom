# Can you find me? A service that checks whether an anonymous profile can be traced back to its person before it is published, an agent team of six steps with several models attacking the draft on their own, the truth sealed with the owner and compared only in code, a rewriter that closes what leaked, run in a Claude session or in the browser, and who would use it, sgit.ai

> When we publish an anonymous profile for someone who cannot go public, the most important question is whether it can be reverse-engineered. Can you tell which industry they work in? Which company? Can you zoom in until there is one person left? That is a service we can build, and a good example of why the tools on sovereign websites matter. An agent team works in sequence: one lists everything that could identify the person, one profiles them, one looks at what the vouchers have in common, one estimates how many people could fit. Each step is run by several models on their own, Claude, Mistral, DeepSeek and a local model, and code correlates their answers: when independent models agree, and agree with the truth, the risk is real. The truth itself, the person's real industry, employer, city and years, never goes to a model: it stays sealed with the owner and only code compares the guesses with it. A rewriter then proposes what to generalise, and the check runs again until the risk is low enough. It runs in a Claude session or in the browser with the owner's own keys, and every run is saved. Research shows models can infer personal attributes from text with up to 85% accuracy, and that ordinary anonymisation does not stop them, so this is exactly the check to run before anything is published.

*Source: <https://newsroom.sgit.ai/articles/can-you-find-me.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Can you find me? A service that checks whether an anonymous profile can be traced back to its person before it is published, an agent team of six steps with several models attacking the draft on their own, the truth sealed with the owner and compared only in code, a rewriter that closes what leaked, run in a Claude session or in the browser, and who would use it

# Can you find me? A service that checks whether an anonymous profile can be traced back to its person before it is published, an agent team of six steps with several models attacking the draft on their own, the truth sealed with the owner and compared only in code, a rewriter that closes what leaked, run in a Claude session or in the browser, and who would use it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/can-you-find-me.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · privacyanonymisationagentsevalssovereign-websitepersonasarticle

***Abstract:** When we publish an anonymous profile for someone who cannot go public, the most important question is whether it can be reverse-engineered. Can you tell which industry they work in? Which company? Can you zoom in until there is one person left? That is a service we can build, and a good example of why the tools on sovereign websites matter. An agent team works in sequence: one lists everything that could identify the person, one profiles them, one looks at what the vouchers have in common, one estimates how many people could fit. Each step is run by several models on their own, Claude, Mistral, DeepSeek and a local model, and code correlates their answers: when independent models agree, and agree with the truth, the risk is real. The truth itself, the person's real industry, employer, city and years, never goes to a model: it stays sealed with the owner and only code compares the guesses with it. A rewriter then proposes what to generalise, and the check runs again until the risk is low enough. It runs in a Claude session or in the browser with the owner's own keys, and every run is saved. Research shows models can infer personal attributes from text with up to 85% accuracy, and that ordinary anonymisation does not stop them, so this is exactly the check to run before anything is published.*

An agent team that tries to re-identify a profile; the truth goes only to code.

## In short

- **Before an anonymous profile is published, try to find the person.**
- **Six steps, in sequence:** extract, profile, vouchers, narrow, correlate, rewrite.
- **Several models attack on their own;** code correlates their answers.
- **The truth is sealed with the owner,** and only code compares guesses with it.
- **Run in a Claude session or in the browser,** with every run saved.
- **A service for anyone publishing something anonymous.**

## The question

When we publish an anonymous profile for someone who needs to leave a job without going public ([an anonymous profile, vouched for](an-anonymous-profile-vouched-for.md)), the most important question is: can it be reverse-engineered? Can you say which industry this person worked in? Which kind of company, which size, which city? Can you keep zooming in until only one person fits?

This is not a hypothetical worry. Researchers gave language models real Reddit profiles and found they could infer location, income, sex and other attributes with up to 85% top-1 and 95% top-3 accuracy, far faster and cheaper than people, and that common text anonymisation did not protect against it ([Staab and others, Beyond Memorization](https://arxiv.org/abs/2310.07298)). If models can do that, the right test for an anonymous profile is to let models try.

## The team

An agent team works in sequence, each step with one job:

1. **Extract.** List every quasi-identifier: dates and durations, team and company sizes, tools and systems, places, awards, rare skills, unusual phrases.
2. **Profile.** From those, guess the industry, the employer or kind of employer, the region, the seniority, the years.
3. **Vouchers.** Look at who vouches for the profile and what they have in common: one company, one city, one period.
4. **Narrow.** Estimate how many people could fit everything found so far: thousands, dozens, or one.
5. **Correlate, in code.** Compare the models' guesses with each other and with the truth.
6. **Rewrite.** Propose what to generalise or remove, and run the check again.

## Several models, each alone

Steps one to four are run by several models independently: for example Claude, Mistral, DeepSeek and a model running locally. Each gives its guesses with a confidence, without seeing the others'. That matters, because one model's guess is a lead, as the X-ray taught us ([the RiskMandate X-ray](the-riskmandate-x-ray.md)); but when independent models converge on the same industry or the same company, the profile is giving it away. It is the same pattern as the Swarm's consensus in code ([the swarm](the-swarm-one-real-run-at-a-time.md)) and the Mistral site's five models on one brief ([one night on Mistral](one-night-on-mistral.md)).

## The truth stays sealed

To know whether a guess is right, something has to know the truth. Here the owner does: before the check, they write down the real industry, employer, city and years, and that record stays with them, in the browser tab or sealed in their vault. It is never sent to a model. Only code reads it, to score each guess: right, close, or wrong.

The draft itself does go to the models, and that is acceptable because it is the text that will be published anyway. Even so, the owner chooses the providers, and should prefer ones that do not train on what they are sent ([DeepSeek in our workflows](deepseek-in-our-workflows.md)).

## The report

Code turns the runs into a report the owner can read:

- **Risk by attribute:** industry, employer, region, seniority, years, each with how many models got it right and how sure they were.
- **What gave it away:** the phrases, numbers and vouchers each model relied on.
- **How narrow:** the estimated number of people who fit.
- **What to change:** the rewriter's suggestions, and the risk after them.

The owner decides what to accept, and the check runs again. Every run is saved, with the models, prompts, outputs and cost, but not the truth, so it can be replayed and audited.

## Where it runs

- **In a Claude session,** as an agent team with a conductor, the way our other teams run ([a website with a team inside](a-website-with-a-team-inside.md)).
- **In the browser,** as a sovereign website tool: the owner's own keys, held in the tab, calls only to the providers they choose, and the truth never leaving the page. The Mistral site already shows this pattern working, with recorded runs that replay with no key.
- **Locally,** with a model on the device, for profiles that must not leave it at all.

## Who would use it

The anonymous profile is the first case, but the need is wider: anyone about to publish something that is meant to be anonymous. A case study about a client, a testimonial, a write-up of an incident, a story with an unnamed source, a dataset released for research. The service can be a free self-check in the browser, and a paid review where the team runs the full set of models and a person reads the report with the owner.

## What this does not claim

- **Nothing is built yet;** this is a design.
- **A pass is not a guarantee:** a determined person with outside knowledge can still find what models miss.
- **The narrowing estimate is a guess,** not a count of real people.

## Where this comes from

My own thinking in writer-10's session on 21 November 2026, following the anonymous profile article of the same day, and the paper cited above, read that day. Related: [an anonymous profile, vouched for](an-anonymous-profile-vouched-for.md), [the RiskMandate X-ray](the-riskmandate-x-ray.md), [the swarm, one real run at a time](the-swarm-one-real-run-at-a-time.md), [one night on Mistral](one-night-on-mistral.md), [DeepSeek in our workflows](deepseek-in-our-workflows.md), [a website with a team inside](a-website-with-a-team-inside.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#can-you-find-me)

### Builds on

- [An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation](an-anonymous-profile-vouched-for.md) An anonymous profile for someone who cannot go public yet, made credible by people who vouch for it in the web of trust.
- [The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy](the-riskmandate-x-ray.md) The RiskMandate X-ray: type a company, see its AI helpers' reach, mandate and gap, built by four search agents for about a dime a company.
- [The swarm, one real run at a time: the Web Summit demo that showed agents, the loops they start and the model calls they make, run for real, signed and replayed, step by step from one person and one agent to 24 loops at once, 216 model calls for 6.8 cents, the same work under a harness with 3 of 12 risky actions still possible instead of 11, and the Story Studio, where a spoken answer became a deck in front of you](the-swarm-one-real-run-at-a-time.md) The Swarm from Web Summit: agents run for real, signed and replayed, 216 model calls for 6.8 cents, a harness test, and a voice-to-deck studio.
- [One night on Mistral: how an agent team turned "a European brain for a sovereign website" into a working site overnight, for the Mistral Vibe Hackathon in London, with 33 demos in the browser, from a shoebox of files to a website and five Mistral models drawn side by side, evals that found which model catches a scam note, the Swarm moved onto Mistral, about 41 cents of Mistral usage, and why this is where I want to start working with Mistral](one-night-on-mistral.md) An agent team turned the European brain article into a working Mistral site overnight: 33 browser demos, evals, the Swarm on Mistral, about 41 cents.
- [DeepSeek in our workflows and on sovereign websites: what DeepSeek offers today, open weights under MIT, an API that answers calls from the browser and speaks both OpenAI's and Anthropic's formats, at a fraction of the price, where its data goes and where else it can run, and a proposal for a sovereign website that loads Wikipedia articles and draws them as graphs, with DeepSeek doing the reading and code doing the checking](deepseek-in-our-workflows.md) Using DeepSeek in our workflows and on sovereign websites, with open eyes, and a proposal: a Wikipedia explorer where DeepSeek reads and code checks.
- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 526 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=526)

**Posting this article on LinkedIn?** The cover is [can-you-find-me.jpg](banners/can-you-find-me.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/can-you-find-me.html)*
