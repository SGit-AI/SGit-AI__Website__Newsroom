---
title: Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: At Web Summit two of our demos ran agentic workflows in the browser. The RiskMandate X-ray took a company's name, researched it, proposed where agent behaviour policies would matter, and mapped one in full. Another took a voice note, transcribed it through OpenRouter, fired a storyteller and a deck writer, and came back with a deck and an infographic on how we could work together. This is the same idea for websites, and another step in making it simple. A visitor goes to one page, describes the site they want, types it or says it, puts in their own model key, chooses how many designs, their pictures or generated ones, and a budget, and presses build. Then they watch: the conductor hands out the work, each agent's card shows what it may and may not do, the policy guard refuses what it should and says so on screen, the cost climbs against the budget, and the designs arrive one by one. At the end, a zip, in the browser, with no server of ours involved; a vault if they want one; and a recording of the run to replay. Run the same brief at £1, £3 and £5, on open-weight models, Sonnet and Opus, and you have evals anyone can see. It belongs on sovereignwebsite.org, open source, and it is how I would like to show people what we do.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, agentic, behaviour-policies, evals, browser, demos, article
status: published
---

!shot bwr-ui.webp | images/ | A mock-up: the brief, the team at work with each agent's policy, and the designs as they arrive. | screenshot

## In short {#in-short}

- **The Web Summit demos ran agentic workflows in the browser:** the X-ray, and a voice note that became a deck.
- **Now the same for websites:** describe it, add your key, press build, and watch it being made.
- **Every agent on screen,** with what it may and may not do, and the policy guard refusing in front of you.
- **Every penny shown,** against a budget you set.
- **A zip at the end,** in the browser, with no server of ours.
- **The same brief on several models,** side by side, as evals.

## Where this comes from {#demos}

Two of the demos we showed at Web Summit ran whole agentic workflows on a web page. The RiskMandate X-ray took a company's name, sent it to search agents, and kept only facts whose sources were read; eleven test searches on 7 November cost about 0.94 dollars ([the team's operating system](/articles/the-teams-operating-system.html)). From what it found, it proposed where agent behaviour policies would matter for that company, then took one use case and mapped it in full: what an agent should do, what it should not, and where the gap was. Watching it think was half the point.

The other took a voice note. The browser transcribed it through OpenRouter, mapped what was said, then fired a storyteller and a deck writer, and came back with a deck and an infographic on how that person's company and RiskMandate could work together. Both deserve pieces of their own; what matters here is what they proved. A browser tab can run a team of agents, show them working, and hand back something real.

## The idea {#idea}

So why not the same for a website? Not the whole website cell, but a first pass, built in front of you: the research, the words, five designs or a hundred, the agents firing one after another, all in the browser. It is another step in the direction everything has taken this autumn: make it simple, then simpler ([simple on top of years](/articles/simple-on-top-of-years.html)).

## What the visitor does {#ux}

1. **Goes to one page,** on sovereignwebsite.org.
2. **Says what to build:** types it, says it as a voice note, or picks an example or a template. A website about a company, a topic, themselves, or someone else.
3. **Puts in their own model key:** an OpenRouter key for now, or a key for a partner's own models. It stays in the page.
4. **Chooses:** how many designs, from one to a hundred; their own pictures, or generated ones; a budget and the models, from £1 on open-weight models to Opus; and the checks, a reviewer, the policies, a recording of the run.
5. **Presses build, and watches.**

## What they watch {#watch}

!shot bwr-flow.webp | images/ | The flow in one browser tab: the conductor fans out, every call passes the policy guard. | concept

The page shows the team at work. The conductor plans the run and hands out the work. An interviewer asks the few questions it needs; a researcher reads sources and keeps them; a writer drafts the words; designers make their directions; an image maker makes scenes; a reviewer checks claims and links; a packager zips the site. Each agent has a card that says what it is doing, what it has cost, and its behaviour policy: what it may do, and what it may not.

The important part is that the policies are visible while they work. The writer can draft but cannot change a price or publish. A designer can change styles and images but not the words. The image maker can generate a beach but not a brand's logo, and when it tries, the policy guard refuses, the refusal appears on screen in red, and the agent asks the person instead. That is agent behaviour policies made visible: even with tools we wrote ourselves, agents have more power than they should, and the guard is what narrows it.

There are two layers. The agent's own policy is the set of tools it is given at all. The page's is the guard that checks every call before it runs, the way a secure harness or a proxy would; no agent can switch it off. A browser is a good place to show the difference, because both run where the visitor can see them.

## Cost, and models, side by side {#evals}

!shot bwr-compare.webp | images/ | The same brief, four budgets: compare designs, time and cost, and keep the runs as evals. | concept

The cost climbs on screen against the budget, agent by agent, on the visitor's own key. And because the brief is fixed, the same brief can run on different models: a £1 version on open-weight models, a £3 mixed version, a £5 version on Sonnet, an Opus version, side by side. That is an eval anyone can watch, and a fair one, because the brief, the agents and the policies are the same.

The runs can go into a shared eval vault, so they can be compared later and by anyone. And it is a natural thing for model providers to sponsor: one run on Gemini, one on Bedrock, the same brief on each, published as it happened.

## Sovereign by construction {#sovereign}

- **No server of ours:** the page is static files; the agents run in the tab, calling the model provider with the visitor's key.
- **The key never leaves the page,** and nothing is stored on a server.
- **The result is a zip,** kept in the browser's own storage and downloaded, so no vault is needed; a vault is there for those who want one ([your website, from a vault](/articles/your-website-from-a-vault.html)).
- **The run is recorded,** every step and every refusal, so it can be replayed. There may already be a way to run sgit entirely in the browser, which would make each step a commit; that is to check.
- **The code is open,** at sovereignwebsite.org, so anyone can run it, change it, or point it at their own models ([what is a sovereign website](/articles/what-is-a-sovereign-website.html)).

## Why it matters {#why}

It shows, in a few minutes, everything we have been describing: a team of agents, a [team inside the website](/articles/a-website-with-a-team-inside.html), behaviour policies working, the cost of it, and a site that belongs to the person who asked for it. I would use it to contact the people I want to talk to: here is a link, describe your site, watch it built. And it shows what the paid version adds: the website cell's full team, the review, the hand-over and the hosting.

## A name {#name}

It needs one. My working title is "watch it build". Others to choose from: the build room; build in the open; a live build. Whatever it is called, it should live at an address on sovereignwebsite.org, next to the principles.

## What this does not claim {#limits}

- **None of this is built yet;** the X-ray and the voice-note demo ran at Web Summit, and the mock-ups here are sketches.
- **The costs on the mock-up are invented,** and so are the budget tiers until a real run sets them.
- **Running sgit fully in the browser** is to be confirmed.
- **The policy guard in the browser** is a design, not yet a harness.

## Where this comes from {#sources}

My own thinking, in writer-10's session on 19 November 2026, building on the Web Summit demos described in [the team's operating system](/articles/the-teams-operating-system.html), and on [a website with a team inside](/articles/a-website-with-a-team-inside.html), [your website, from a vault](/articles/your-website-from-a-vault.html), [what is a sovereign website](/articles/what-is-a-sovereign-website.html) and [simple on top of years](/articles/simple-on-top-of-years.html).
