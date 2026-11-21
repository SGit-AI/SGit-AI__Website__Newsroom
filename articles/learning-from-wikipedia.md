# Learning from Wikipedia, with DeepSeek, a plan: a sovereign website built around a tool made of many small tools, a site for each topic from atoms to dinosaurs to maths, every one its own repository, made from Wikipedia with DeepSeek doing the reading, an agent team that verifies, checks quality and reviews for the right age under behaviour policies, a person approving every publish, and the natural next step for sovereign websites, into education, sgit.ai

> This is the natural progression of what we have been building: the next step, into education. It is a sovereign website around a tool, and the tool is made of many small tools: a graph, a timeline, a glossary, a quiz, a map, a comparison. With them we make learning materials, one site per topic: someone learning about atoms, someone about maths, someone about dinosaurs. Everything is made from Wikipedia, with DeepSeek doing the reading, and with code checking everything that can be checked: every quote word for word against the article, every entity anchored to Wikidata. An agent team does the whole loop: research, writing, fact checking with a second model, quality control, a review that the language and the content suit the age of the reader, licence and attribution, and accessibility, each agent under a behaviour policy, and a person approving every publish. The age is a question for the legal team: 16 and up, or 18 and up, and the plan holds until they answer. There is no account, no tracking and no data about learners, so nothing about a reader ever goes to a model. Each site has its own repository, like the tools we already publish, and I want to bring in people I know who work in education.

*Source: <https://newsroom.sgit.ai/articles/learning-from-wikipedia.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Learning from Wikipedia, with DeepSeek, a plan: a sovereign website built around a tool made of many small tools, a site for each topic from atoms to dinosaurs to maths, every one its own repository, made from Wikipedia with DeepSeek doing the reading, an agent team that verifies, checks quality and reviews for the right age under behaviour policies, a person approving every publish, and the natural next step for sovereign websites, into education

# Learning from Wikipedia, with DeepSeek, a plan: a sovereign website built around a tool made of many small tools, a site for each topic from atoms to dinosaurs to maths, every one its own repository, made from Wikipedia with DeepSeek doing the reading, an agent team that verifies, checks quality and reviews for the right age under behaviour policies, a person approving every publish, and the natural next step for sovereign websites, into education

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/learning-from-wikipedia.md) · [newsroom v0.14.196](https://newsroom.sgit.ai/admin/versions.html) · learningwikipediadeepseeksovereign-websitebehaviour-policieseducationplanarticle

***Abstract:** This is the natural progression of what we have been building: the next step, into education. It is a sovereign website around a tool, and the tool is made of many small tools: a graph, a timeline, a glossary, a quiz, a map, a comparison. With them we make learning materials, one site per topic: someone learning about atoms, someone about maths, someone about dinosaurs. Everything is made from Wikipedia, with DeepSeek doing the reading, and with code checking everything that can be checked: every quote word for word against the article, every entity anchored to Wikidata. An agent team does the whole loop: research, writing, fact checking with a second model, quality control, a review that the language and the content suit the age of the reader, licence and attribution, and accessibility, each agent under a behaviour policy, and a person approving every publish. The age is a question for the legal team: 16 and up, or 18 and up, and the plan holds until they answer. There is no account, no tracking and no data about learners, so nothing about a reader ever goes to a model. Each site has its own repository, like the tools we already publish, and I want to bring in people I know who work in education.*

One area, many small sites: a hub, the tools, a site per topic, and the same loop for each.

## In short

- **A website around a tool made of small tools,** and a site for every topic.
- **Made from Wikipedia, with DeepSeek reading** and code checking.
- **An agent team does the loop:** verify, quality control, age review, licence, approval.
- **The age is for the legal team to decide:** 16 and up, or 18 and up.
- **No accounts, no tracking, nothing about readers sent to a model.**
- **Every site its own repository,** with people from education involved.

## The idea

Can we make good learning materials, and good visualisations, from Wikipedia? Someone learning about atoms, someone about maths, someone about dinosaurs: each should find a site that explains the topic well, shows how its ideas connect, lets them test themselves, and always leads back to the articles it came from. It is a natural next step for sovereign websites, into education, and I will build it as a sovereign website around a tool, and the tool will be made of many small tools.

It builds directly on the Wikipedia explorer I proposed this morning ([DeepSeek in our workflows](deepseek-in-our-workflows.md)): code loads, DeepSeek reads, code checks.

## One area, many small sites

- **The hub.** The area's own site: what it is, how it is made, every tool and every topic.
- **The tools.** Each does one thing and is its own site and repository: a graph of how ideas connect, a timeline, a glossary, a quiz, a map, a comparison of two things. The same pattern as every tool its own website ([every tool its own website](every-tool-its-own-website.md)).
- **The topics.** A site per topic, atoms, dinosaurs, fractions, volcanoes, made with the tools from a set of Wikipedia articles.

Every site has its own repository, its own history and its own address, so each can be worked on, reviewed and handed on separately.

## The loop for every topic

1. **Load, in code.** The topic's Wikipedia articles, each pinned to its revision, so every page can say exactly what it was made from.
2. **Read, with DeepSeek.** Facts, terms, people, dates and relations, each with the sentence it came from. Wikipedia is public, so DeepSeek's own API suits this step.
3. **Check, in code.** Every quote must be in the article word for word; entities anchored to Wikidata, so topics join up instead of repeating.
4. **Make.** Explanations at the right level, a glossary, a timeline, a graph, quiz questions with their answers and sources.
5. **Review.** Facts, age, safety, licence and accessibility, by the team below.
6. **Approve.** A person reads what changed and publishes, or sends it back.

## The team, under policies

Each agent has one job and a behaviour policy that says what it may touch ([feature behaviour policies](feature-behaviour-policies.md)):

- **A researcher** chooses and loads the articles for a topic.
- **A writer** turns checked facts into explanations and quizzes.
- **A fact checker on a second model,** for example Mistral or Claude, independently confirms each claim against the source; disagreement sends it back.
- **An age reviewer** checks the language and the content suit the agreed audience.
- **A safety reviewer** checks for anything harmful, misleading or unsuitable.
- **A licence reviewer** checks attribution under CC BY-SA 4.0 on every page, with links to the articles and a note of what changed ([reusing Wikipedia content](https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content)).
- **An accessibility reviewer** checks contrast, structure and reading order.
- **A conductor** runs the loop and keeps the record, and no agent can publish.

## The age question

I went back and forth on this: 8 to 15, then 16 and up, then 18 and up. It is a legal question as much as an editorial one, so the legal team decides it. Until they answer, the plan assumes an audience of 16 and up, with language and content reviewed for that, and nothing published for younger readers. Two things make it simpler whatever they decide: the sites collect nothing about their readers, and every page is reviewed by an agent and a person before it goes out.

## Nothing about the reader

The sites are static: no accounts, no cookies, no tracking, no chat box that sends a reader's words to a model. All the model work happens when the materials are made, on public Wikipedia text, never when someone reads them. A quiz scores itself in the browser and forgets. That matters for any audience, and more for a young one.

## People from education

The agents make it scale; people who teach make it right. I want to involve people I know in education to shape the topics, the level and the reviews. Each gets their own repositories and edits through their own AI, the path we learnt on [the first round trip](the-first-round-trip.md). Requests and ideas go through a board and an inbox lane, and every change, by a person or an agent, is a commit with its author.

## First steps

1. **The hub and one topic,** atoms, with two tools, the graph and the glossary.
2. **The full review loop** on that topic, with a person approving.
3. **The legal team's answer on age,** written into the age reviewer's policy.
4. **More tools and more topics,** dinosaurs and maths next.

## What this does not claim

- **This is a plan;** nothing is built yet.
- **The audience age is not decided;** the legal team will set it.
- **Reviews reduce mistakes, they do not remove them;** every page links to its sources so readers can check.

## Where this comes from

My own thinking in writer-10's session on 21 November 2026, following the DeepSeek article of the same day. Related: [DeepSeek in our workflows](deepseek-in-our-workflows.md), [every tool its own website](every-tool-its-own-website.md), [feature behaviour policies](feature-behaviour-policies.md), [the first round trip](the-first-round-trip.md), [the showroom](the-showroom.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#learning-from-wikipedia)

### Builds on

- [DeepSeek in our workflows and on sovereign websites: what DeepSeek offers today, open weights under MIT, an API that answers calls from the browser and speaks both OpenAI's and Anthropic's formats, at a fraction of the price, where its data goes and where else it can run, and a proposal for a sovereign website that loads Wikipedia articles and draws them as graphs, with DeepSeek doing the reading and code doing the checking](deepseek-in-our-workflows.md) Using DeepSeek in our workflows and on sovereign websites, with open eyes, and a proposal: a Wikipedia explorer where DeepSeek reads and code checks.
- [Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving](every-tool-its-own-website.md) Turning the 49 tools of tools.sgraph.ai into sovereign websites: one site each, simple first, pinned versions, signed hashes, a team of teams.
- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [The first round trip: a sovereign website made for Kate Curtis-Evans during our call, five designs from a design agent of its own, then handed over so she edits it herself from her own Claude, the friction that took multiple rounds to get through, what it says about over-privilege, and the next step, a signed and sealed channel from her site straight to the agent](the-first-round-trip.md) The first round trip of Sovereign Website with someone from outside: a site made during a call, handed over, and edited by its owner's own Claude.
- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, independent brochures for our startups, a provider guide, tools that run on the owner's own key, made-up businesses, a family of news sites, and the theme that is emerging across all of them, a site that is yours, says how it was made and can be worked on by your own AI](the-showroom.md) The Sovereign Website hub after its first days: 33 live sites from one pipeline, and the shared bones that are becoming the product.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 527 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=527)

**Posting this article on LinkedIn?** The cover is [learning-from-wikipedia.jpg](banners/learning-from-wikipedia.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/learning-from-wikipedia.html)*
