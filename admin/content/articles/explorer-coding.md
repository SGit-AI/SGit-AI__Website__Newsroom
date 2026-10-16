---
title: Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: I would like to propose a better name for what is usually called vibe coding: explorer coding. Vibe coding sounds as if people are just typing and ad-libbing, and I have never liked it, because what they are doing is the best thing to happen to software since the spreadsheet: everyone with a need can now explore it by building, with the fast feedback loop that made spreadsheets win, and what they build is the best brief anyone will ever write. Explorer is Simon Wardley's word for exactly that kind of work. It also makes the limit clear. An explorer-coded app may look and feel like an application, but nobody has read the code or checked the architecture, and it is not ready to be in line: once other people depend on it, it is mission critical, and it needs villagers to maintain it, with agent behaviour policies, data handling and releases that do not break it, and then town planners who own the code in production and are accountable for it, as the Linux kernel, Fedora and GitHub already say the human who ships code must be. The further towards commodity, the fewer agents in line and the more deterministic code. And it suggests a commercial model: every product should have an explorer version, where users reshape it by talking to it, and paid conversions from there to a villager product and a town planner one.
version: v0.12.76
license: https://creativecommons.org/licenses/by/4.0/
tags: explorer-coding, vibe-coding, wardley-maps, explorers, villagers, town-planners, citizen-developer, accountability, business-models, agents, article
status: published
---

!shot ec-handover.webp | images/ | Explorer coding and the handover that makes it last: explorers build by talking to an agent, and what they build is the brief; villagers maintain it, with policies, data handling and tests; town planners own the code in production. From left to right, fewer agents in line and more deterministic code. | architecture

## In short {#in-short}

- **Call it explorer coding.** What people call vibe coding is exploration, and the word should say so.
- **It is the best thing since the spreadsheet.** Everyone with a need can now build, with a fast feedback loop.
- **What it produces is a brief.** The best one there is: it runs.
- **It is not ready to be in line.** Once others depend on it, it is mission critical, and needs more.
- **Villagers maintain it; town planners own it.** Policies, data and releases first; accountable code after.
- **Towards commodity, fewer agents in line.** And more deterministic code.
- **Every product needs an explorer version.** With paid conversions to villager and town planner products.

## Why not vibe coding {#name}

The term is [Andrej Karpathy's](https://en.wikipedia.org/wiki/Vibe_coding), from a post in February 2025: "There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." He was describing throwaway weekend projects, and by November it was Collins Dictionary's word of the year. In [an article in September](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) I wrote that I did not love it, but that the word had won. I want to go further now, because the word is doing harm. It sounds as if people are just typing, ad-libbing, going with a feeling; it is a little demeaning to the people doing it, and it hides what is actually happening. I am not alone in this: Andrew Ng [said in May 2025](https://www.aol.com/andrew-ng-says-vibe-coding-065832544.html) "It's unfortunate that that's called vibe coding", and that coding with AI is "a deeply intellectual exercise".

So I would like to propose **explorer coding**. I considered spreadsheet coding, because of where this comes from, and brief coding, because of what it produces. But if you think in [Wardley maps](https://blog.gardeviance.org/2023/12/how-to-organise-yourself-dangerous-path.html), the right word is already there. Explorers "explore never-before-discovered concepts, the uncharted land"; "They show you wonder but they fail a lot." That is exactly what someone does when they build the tool they need with an agent. I could not find anyone using explorer coding as a term. The nearest is *exploratory programming*, the [research term](https://dblp.org/rec/conf/vl/KeryM17.html) for programming while the requirements are still being discovered, which is a good ancestor to have.

## The best thing since the spreadsheet {#spreadsheet}

People have always built software with whatever they controlled, and for most of them it was a spreadsheet. Spreadsheets won because of the feedback loop: change a cell and see the result, a read-evaluate-print loop for people who would never call it that. Everybody was already exploring; it was just very slow, because anything beyond a spreadsheet meant writing a document and waiting for someone else to build it. What has changed is that the loop is now fast for anything: an app, a workflow, a customisation of a product, a change to the [interface of a single moment](/articles/custom-uis-are-not-the-exception.html).

That is why I think it is the best thing to happen to software since the spreadsheet, and why [the citizen developer is good news](/articles/the-citizen-developer.html). It is an explosion of empowerment. I was talking to someone who works in HR this week, and once we started to explore what her team will be doing, the apps, the customisations and the workflows they will build, and the agents they will have to manage, her answer was: "Amazing! When can I start?"

And what explorers produce is the best brief there is. A working app says what its user wants better than any document, because it runs.

## Not ready to be in line {#in-line}

This is the part the new word makes easier to say, and the part that matters most. An explorer-coded app may look like an application and feel like an application, but it is a brief. Nobody has read the code. Nobody has validated the architecture. It does not meet any internal standard, and it is not ready to be run in production, or, the better way to say it, not ready to be *in line*: in the path of work that other people depend on.

The trap is that dependence comes quickly. Once something gets used, it is mission critical, because people depend on it; even for one person, if it replaced how they work, it is mission critical to them. From then on it has to be maintained, checked and kept working, and new versions cannot break it.

## Villagers and town planners {#handover}

That is the villagers' work. They take what the explorer built and make it safe for others to depend on: maintenance, tests around what people rely on, releases that do not break it, and, because these apps now run agents, [agent behaviour policies](/articles/your-own-newsroom.html#policy) and rules for the data the agents touch. In Wardley's words, they "turn the prototype into a product, make it manufacturable, listen to customers".

When it matures, the town planners take it, and they own the code. Here the accountability is not new: more and more of the industry already says that whoever ships code is responsible for it, however it was written. The Linux kernel's [rules for AI coding assistants](https://docs.kernel.org/process/coding-assistants.html) say "AI agents MUST NOT add Signed-off-by tags" and "Only humans can legally certify the Developer Certificate of Origin", and make the submitter responsible for "Taking full responsibility for the contribution". Fedora's [policy proposal](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/) says "The contributor is always the author and is fully accountable for their contributions." We cannot make an explorer accountable for code they never read. We can make the team the work is handed to accountable, and the town planners above all.

They can use agents, of course. But the direction is set by where the code sits on the map: the further towards commodity, the fewer agents in line, and the more deterministic code. I have argued it for [code review](/articles/if-somebody-built-a-company-on-code-review.html), where "A model has no place in line on a mission-critical path", and for [cost](/articles/agentic-cost-is-an-engineering-problem.html): explorer-style code running in a commodity place is an engineering problem.

## An explorer version of every product {#products}

!shot ec-tiers.webp | images/ | An explorer version of every product, and paid conversions from it: the explorer version where users reshape the product by talking to it; the submission, which is the brief; the villager product, maintained; and the town planner product, built properly or as a maintained fork. Proposed. | comparison

The name also suggests a commercial model, and it follows from [the previous article](/articles/software-vendors-as-villagers.html). Products need to become explorer-friendly; more than that, they need an explorer version. In it, users can talk to the product with a model, reshape it, move things around and keep their own version; the product is treated as primitives. When the user has something they want to keep, they submit it, and pay to convert it into a villager product, maintained across releases, and, if it matters enough, into a town planner product, built properly or kept as a maintained fork. Each step is a revenue stream, and each submission tells the vendor exactly what its users want.

The same path should exist inside companies, between a department and its engineers, and around open-source projects, between their users and their maintainers. [The custom Firefox plan](/articles/a-custom-firefox-of-my-own.html) walks through what it would look like for one product.

## What this does not claim {#limits}

- **Explorer coding is a proposal.** I found no established use of the term; exploratory programming is its ancestor.
- **Not that explorer-coded apps are good code.** The point is that they are briefs, not products.
- **The HR conversation is one conversation.** An illustration, not a survey.
- **The explorer version of a product is a proposal.** I know of no vendor selling it.

If you want to set up the handover from explorers to villagers and town planners in your company, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Andrej Karpathy's post of 2 February 2025, quoted from [Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding); Andrew Ng, reported by [Business Insider via AOL](https://www.aol.com/andrew-ng-says-vibe-coding-065832544.html); Simon Wardley, [How to organise yourself: the dangerous path to Explorer, Villager and Town Planners](https://blog.gardeviance.org/2023/12/how-to-organise-yourself-dangerous-path.html), 7 December 2023; Kery and Myers, [Exploring Exploratory Programming](https://dblp.org/rec/conf/vl/KeryM17.html), VL/HCC 2017; the Linux kernel, [AI Coding Assistants](https://docs.kernel.org/process/coding-assistants.html); Fedora Council, [policy proposal on AI-assisted contributions](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/), 25 September 2025. Read on 16 October 2026. The HR conversation was mine, and the person is not named.
