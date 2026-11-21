---
title: Learning from Wikipedia, with DeepSeek, a plan: a sovereign website built around a tool made of many small tools, a site for each topic from atoms to dinosaurs to maths, every one its own repository, made from Wikipedia with DeepSeek doing the reading, an agent team that verifies, checks quality and reviews for the right age under behaviour policies, a person approving every publish, and a project to build with a friend in the open
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: A friend and I are going to build this together. It is a sovereign website around a tool, and the tool is made of many small tools: a graph, a timeline, a glossary, a quiz, a map, a comparison. With them we make learning materials, one site per topic: someone learning about atoms, someone about maths, someone about dinosaurs. Everything is made from Wikipedia, with DeepSeek doing the reading, and with code checking everything that can be checked: every quote word for word against the article, every entity anchored to Wikidata. An agent team does the whole loop: research, writing, fact checking with a second model, quality control, a review that the language and the content suit the age of the reader, licence and attribution, and accessibility, each agent under a behaviour policy, and a person approving every publish. The age is a question for the legal team: 16 and up, or 18 and up, and the plan holds until they answer. There is no account, no tracking and no data about learners, so nothing about a reader ever goes to a model. Each site has its own repository, like the tools we already publish, and the whole thing is a good example of how we can collaborate with someone from outside.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: learning, wikipedia, deepseek, sovereign-website, behaviour-policies, collaboration, plan, article
status: published
---

!shot learn-plan.webp | images/ | One area, many small sites: a hub, the tools, a site per topic, and the same loop for each. | concept

## In short {#in-short}

- **A website around a tool made of small tools,** and a site for every topic.
- **Made from Wikipedia, with DeepSeek reading** and code checking.
- **An agent team does the loop:** verify, quality control, age review, licence, approval.
- **The age is for the legal team to decide:** 16 and up, or 18 and up.
- **No accounts, no tracking, nothing about readers sent to a model.**
- **Every site its own repository,** built with a friend in the open.

## The idea {#idea}

Can we make good learning materials, and good visualisations, from Wikipedia? Someone learning about atoms, someone about maths, someone about dinosaurs: each should find a site that explains the topic well, shows how its ideas connect, lets them test themselves, and always leads back to the articles it came from. A friend and I will build it together, as a sovereign website around a tool, and the tool will be made of many small tools.

It builds directly on the Wikipedia explorer I proposed this morning ([DeepSeek in our workflows](/articles/deepseek-in-our-workflows.html)): code loads, DeepSeek reads, code checks.

## One area, many small sites {#shape}

- **The hub.** The area's own site: what it is, how it is made, every tool and every topic.
- **The tools.** Each does one thing and is its own site and repository: a graph of how ideas connect, a timeline, a glossary, a quiz, a map, a comparison of two things. The same pattern as every tool its own website ([every tool its own website](/articles/every-tool-its-own-website.html)).
- **The topics.** A site per topic, atoms, dinosaurs, fractions, volcanoes, made with the tools from a set of Wikipedia articles.

Every site has its own repository, its own history and its own address, so each can be worked on, reviewed and handed on separately.

## The loop for every topic {#loop}

1. **Load, in code.** The topic's Wikipedia articles, each pinned to its revision, so every page can say exactly what it was made from.
2. **Read, with DeepSeek.** Facts, terms, people, dates and relations, each with the sentence it came from. Wikipedia is public, so DeepSeek's own API suits this step.
3. **Check, in code.** Every quote must be in the article word for word; entities anchored to Wikidata, so topics join up instead of repeating.
4. **Make.** Explanations at the right level, a glossary, a timeline, a graph, quiz questions with their answers and sources.
5. **Review.** Facts, age, safety, licence and accessibility, by the team below.
6. **Approve.** A person reads what changed and publishes, or sends it back.

## The team, under policies {#team}

Each agent has one job and a behaviour policy that says what it may touch ([feature behaviour policies](/articles/feature-behaviour-policies.html)):

- **A researcher** chooses and loads the articles for a topic.
- **A writer** turns checked facts into explanations and quizzes.
- **A fact checker on a second model,** for example Mistral or Claude, independently confirms each claim against the source; disagreement sends it back.
- **An age reviewer** checks the language and the content suit the agreed audience.
- **A safety reviewer** checks for anything harmful, misleading or unsuitable.
- **A licence reviewer** checks attribution under CC BY-SA 4.0 on every page, with links to the articles and a note of what changed ([reusing Wikipedia content](https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content)).
- **An accessibility reviewer** checks contrast, structure and reading order.
- **A conductor** runs the loop and keeps the record, and no agent can publish.

## The age question {#age}

I went back and forth on this: 8 to 15, then 16 and up, then 18 and up. It is a legal question as much as an editorial one, so the legal team decides it. Until they answer, the plan assumes an audience of 16 and up, with language and content reviewed for that, and nothing published for younger readers. Two things make it simpler whatever they decide: the sites collect nothing about their readers, and every page is reviewed by an agent and a person before it goes out.

## Nothing about the reader {#privacy}

The sites are static: no accounts, no cookies, no tracking, no chat box that sends a reader's words to a model. All the model work happens when the materials are made, on public Wikipedia text, never when someone reads them. A quiz scores itself in the browser and forgets. That matters for any audience, and more for a young one.

## Working together {#collaborate}

This is also a good example of how we collaborate with someone outside the team. My friend gets their own repositories, and edits through their own AI, the path we learnt on [the first round trip](/articles/the-first-round-trip.html). Requests and ideas go through a board and an inbox lane, and every change by either of us, or by an agent, is a commit with its author.

## First steps {#steps}

1. **The hub and one topic,** atoms, with two tools, the graph and the glossary.
2. **The full review loop** on that topic, with a person approving.
3. **The legal team's answer on age,** written into the age reviewer's policy.
4. **More tools and more topics,** dinosaurs and maths next.

## What this does not claim {#limits}

- **This is a plan;** nothing is built yet.
- **The audience age is not decided;** the legal team will set it.
- **Reviews reduce mistakes, they do not remove them;** every page links to its sources so readers can check.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026, following the DeepSeek article of the same day. My collaborator is not named here until they choose to be. Related: [DeepSeek in our workflows](/articles/deepseek-in-our-workflows.html), [every tool its own website](/articles/every-tool-its-own-website.html), [feature behaviour policies](/articles/feature-behaviour-policies.html), [the first round trip](/articles/the-first-round-trip.html), [the showroom](/articles/the-showroom.html).
