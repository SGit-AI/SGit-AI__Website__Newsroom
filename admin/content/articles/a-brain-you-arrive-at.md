---
title: A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: A friend who has spent almost eleven years in crypto described what he wants for his company: one place where everything is, so nobody wastes time asking what anyone did today, and where a question to an agent comes back with what the team, the market and the competitors did. That is a company brain, and I think the important word is not brain but company. It has to be made for one company, one sector, one division and even one team, and you do not start with it: you start with one person's brain, then a team's, then a division's, and you arrive at the organisation's. Each level has the same three parts, information, decisions and insights, and the same building blocks: agents with their own keys, append-only lanes, a semantic graph, encrypted vaults, and apps on the phone, the tablet and the computer. The six of us already ran one at Web Summit: I could ask my conductor what everybody was doing, and it would ask the other conductors. This article and a working demo show how.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: company-brain, agents, knowledge-graph, vaults, organisation, fractal, demo, article
status: published
---

!shot abr-levels.webp | images/ | A brain you arrive at: a person's, a team's, a division's, then the organisation's, each with the same three parts. | concept

## In short {#in-short}

- **A company brain is one place for information, decisions and insights,** where you ask an agent instead of a colleague what happened today.
- **It is made for one company,** and for one division and one team inside it, not bought as a generic product.
- **You arrive at it.** Start with one person's brain, then a team's, then a division's, and the organisation's grows from them.
- **The building blocks exist:** agents with keys, append-only lanes, a semantic graph, encrypted vaults, and apps.
- **We already ran one,** for six people and around 250 agents at Web Summit.
- **Try it:** [a working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha), with made-up data.

## What my friend asked for {#ask}

I was with a friend who has been in crypto for almost eleven years, and he described two things he wants for his company. The second was a brain. In his words, the point is not to lose time: if everything is in one place, you can see what a competitor has just launched, what other platforms did, and you walk into the office already knowing what happened today. Inside the team, he does not want to ask anyone what they did. He wants to look, or ask an agent, and get the answer.

I agree with every part of that, and I would change one word in how it is usually said. People say "a brain for the company", as if it were one thing you install. I think it has to be a brain made for this company.

## Made for one company, not bought for all {#custom}

A brain is only as useful as its fit. A logistics company cares about routes, depots and fuel; a crypto company about tokens, holders and liquidity; a bank about exposures and approvals. The same company has divisions that care about different things, and teams inside them that care about different things again. A generic brain that fits everyone fits no one.

So what you build is not a brain but the ability to make one: the same building blocks, put together for a particular company, division and team, in its own words and around its own decisions.

## You arrive at the brain {#arrive}

The second change is the order. You do not start with a brain for the whole organisation; you arrive at it.

- **A person.** Their agent reads their inbox, calendar and notes, and keeps their information, their decisions and why, and what it noticed.
- **A team.** Each person's agent appends what it did to its own lane, and the team's conductor reads the lanes it is allowed to and answers for the team.
- **A division.** The division joins its teams' summaries with its own data.
- **The organisation.** The divisions' graphs are joined where they name the same customer, product or place.

Each level has the same three parts and is built the same way. That is the fractal nature of it: what works for one person works for a team, because a team's brain is made of its people's.

!shot dmo-brain.webp | images/ | The demo's first tab: pick a level, see its information, decisions and insights, and ask what everyone did today. | screenshot

## We already ran one {#ran}

This is not a proposal for us. For Web Summit, the six of us, Angelo Leggio, Vicky Wang, Silvio Switha, José Bota, Indi Gupte and I, ran around 250 named agents on one site, [the team's operating system](/articles/the-teams-operating-system.html), and it worked the way my friend described.

- **Ask the agents, not the people.** I could ask my conductor what everybody was doing, and it would tell me, from the agents' own records.
- **Agents asking agents.** One of Vicky's agents would ask whether my conductor could ask something; when we needed every contact from the summit, I sent one message to my conductor, it messaged every other person's conductor, and each one asked its own agents. The answers came back through encrypted vaults.
- **A lane per agent.** Every agent had [an inbox only it could read](/articles/an-inbox-only-your-agents-can-write-to.html), and its own key, so every message and commit says whose agent made it.
- **A view per person.** Each person had a command centre on their phone, iPad or computer, and the team had [four iPhone and iPad apps and an Android tablet app](/articles/ten-days-at-web-summit.html) by the end of the week.

## The building blocks {#blocks}

What we used is what a company brain needs:

- **Agents with keys:** each one named for its person and role, so you always know whose agent did what.
- **Append-only lanes:** each agent writes what it did and never edits the past; the record is the brain's memory.
- **A semantic graph:** the things and links the agents find, so a question can follow a customer across divisions.
- **Encrypted vaults:** where the private parts live, opened only by the people and agents they are sealed to.
- **Apps:** the brain on the phone, the tablet and the computer, because a brain you have to go to a desk for is not used.
- **Policies:** what each agent may reach, and what it was asked to do, written down ([what can your agent reach?](/articles/what-can-your-agent-reach.html)).

## Try the demo {#demo}

I have put [a small working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha). Its first tab is a made-up company: pick a person, a team, a division or the organisation and see each level's information, decisions and insights; ask what everyone did today, or ask the agents to collect every contact from a trade fair. Everything in it is invented to show the pattern, and it runs in your browser.

## What this does not claim {#limits}

- **The demo's company, people and numbers are made up.**
- **The Web Summit examples are ours,** from 3 to 13 November 2026, as described in [ten days at Web Summit](/articles/ten-days-at-web-summit.html).
- **My friend's company is not named,** and nothing here is from it beyond what he described.

## Where this comes from {#sources}

A conversation with a friend in crypto, 15 November 2026, and my own account of how the Web Summit team worked. Earlier on this site: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [the team's operating system](/articles/the-teams-operating-system.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [always-on agents at team scale](/articles/always-on-agents-at-team-scale.html), and the two companion articles, [the new data lake](/articles/the-new-data-lake.html) and [a market for sweets](/articles/a-market-for-sweets.html).
