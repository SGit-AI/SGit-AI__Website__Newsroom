---
title: Can you find me? A service that checks whether an anonymous profile can be traced back to its person before it is published, an agent team of six steps with several models attacking the draft on their own, the truth sealed with the owner and compared only in code, a rewriter that closes what leaked, run in a Claude session or in the browser, and who would use it
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: When we publish an anonymous profile for someone who cannot go public, the most important question is whether it can be reverse-engineered. Can you tell which industry they work in? Which company? Can you zoom in until there is one person left? That is a service we can build, and a good example of why the tools on sovereign websites matter. An agent team works in sequence: one lists everything that could identify the person, one profiles them, one looks at what the vouchers have in common, one estimates how many people could fit. Each step is run by several models on their own, Claude, Mistral, DeepSeek and a local model, and code correlates their answers: when independent models agree, and agree with the truth, the risk is real. The truth itself, the person's real industry, employer, city and years, never goes to a model: it stays sealed with the owner and only code compares the guesses with it. A rewriter then proposes what to generalise, and the check runs again until the risk is low enough. It runs in a Claude session or in the browser with the owner's own keys, and every run is saved. Research shows models can infer personal attributes from text with up to 85% accuracy, and that ordinary anonymisation does not stop them, so this is exactly the check to run before anything is published.
version: v0.14.195
license: https://creativecommons.org/licenses/by/4.0/
tags: privacy, anonymisation, agents, evals, sovereign-website, personas, article
status: published
---

!shot rid-team.webp | images/ | An agent team that tries to re-identify a profile; the truth goes only to code. | concept

## In short {#in-short}

- **Before an anonymous profile is published, try to find the person.**
- **Six steps, in sequence:** extract, profile, vouchers, narrow, correlate, rewrite.
- **Several models attack on their own;** code correlates their answers.
- **The truth is sealed with the owner,** and only code compares guesses with it.
- **Run in a Claude session or in the browser,** with every run saved.
- **A service for anyone publishing something anonymous.**

## The question {#question}

When we publish an anonymous profile for someone who needs to leave a job without going public ([an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html)), the most important question is: can it be reverse-engineered? Can you say which industry this person worked in? Which kind of company, which size, which city? Can you keep zooming in until only one person fits?

This is not a hypothetical worry. Researchers gave language models real Reddit profiles and found they could infer location, income, sex and other attributes with up to 85% top-1 and 95% top-3 accuracy, far faster and cheaper than people, and that common text anonymisation did not protect against it ([Staab and others, Beyond Memorization](https://arxiv.org/abs/2310.07298)). If models can do that, the right test for an anonymous profile is to let models try.

## The team {#team}

An agent team works in sequence, each step with one job:

1. **Extract.** List every quasi-identifier: dates and durations, team and company sizes, tools and systems, places, awards, rare skills, unusual phrases.
2. **Profile.** From those, guess the industry, the employer or kind of employer, the region, the seniority, the years.
3. **Vouchers.** Look at who vouches for the profile and what they have in common: one company, one city, one period.
4. **Narrow.** Estimate how many people could fit everything found so far: thousands, dozens, or one.
5. **Correlate, in code.** Compare the models' guesses with each other and with the truth.
6. **Rewrite.** Propose what to generalise or remove, and run the check again.

## Several models, each alone {#models}

Steps one to four are run by several models independently: for example Claude, Mistral, DeepSeek and a model running locally. Each gives its guesses with a confidence, without seeing the others'. That matters, because one model's guess is a lead, as the X-ray taught us ([the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html)); but when independent models converge on the same industry or the same company, the profile is giving it away. It is the same pattern as the Swarm's consensus in code ([the swarm](/articles/the-swarm-one-real-run-at-a-time.html)) and the Mistral site's five models on one brief ([one night on Mistral](/articles/one-night-on-mistral.html)).

## The truth stays sealed {#truth}

To know whether a guess is right, something has to know the truth. Here the owner does: before the check, they write down the real industry, employer, city and years, and that record stays with them, in the browser tab or sealed in their vault. It is never sent to a model. Only code reads it, to score each guess: right, close, or wrong.

The draft itself does go to the models, and that is acceptable because it is the text that will be published anyway. Even so, the owner chooses the providers, and should prefer ones that do not train on what they are sent ([DeepSeek in our workflows](/articles/deepseek-in-our-workflows.html)).

## The report {#report}

Code turns the runs into a report the owner can read:

- **Risk by attribute:** industry, employer, region, seniority, years, each with how many models got it right and how sure they were.
- **What gave it away:** the phrases, numbers and vouchers each model relied on.
- **How narrow:** the estimated number of people who fit.
- **What to change:** the rewriter's suggestions, and the risk after them.

The owner decides what to accept, and the check runs again. Every run is saved, with the models, prompts, outputs and cost, but not the truth, so it can be replayed and audited.

## Where it runs {#where}

- **In a Claude session,** as an agent team with a conductor, the way our other teams run ([a website with a team inside](/articles/a-website-with-a-team-inside.html)).
- **In the browser,** as a sovereign website tool: the owner's own keys, held in the tab, calls only to the providers they choose, and the truth never leaving the page. The Mistral site already shows this pattern working, with recorded runs that replay with no key.
- **Locally,** with a model on the device, for profiles that must not leave it at all.

## Who would use it {#who}

The anonymous profile is the first case, but the need is wider: anyone about to publish something that is meant to be anonymous. A case study about a client, a testimonial, a write-up of an incident, a story with an unnamed source, a dataset released for research. The service can be a free self-check in the browser, and a paid review where the team runs the full set of models and a person reads the report with the owner.

## What this does not claim {#limits}

- **Nothing is built yet;** this is a design.
- **A pass is not a guarantee:** a determined person with outside knowledge can still find what models miss.
- **The narrowing estimate is a guess,** not a count of real people.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026, following the anonymous profile article of the same day, and the paper cited above, read that day. Related: [an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html), [the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html), [the swarm, one real run at a time](/articles/the-swarm-one-real-run-at-a-time.html), [one night on Mistral](/articles/one-night-on-mistral.html), [DeepSeek in our workflows](/articles/deepseek-in-our-workflows.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html).
