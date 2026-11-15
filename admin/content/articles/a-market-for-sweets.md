---
title: A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: In 1970 George Akerlof described the market for lemons: when sellers know more than buyers, buyers cannot tell good from bad, and good sellers leave. A friend who has spent almost eleven years in crypto lives in one: by his count, about 61,000 new tokens appear every day, and many are traps, a contract that lets the owner take the money, a few wallets holding almost everything. His team audits tokens to warn people off the bad ones, and wants agents to do more of it. I think the opportunity is the opposite of a market for lemons, a market for sweets: give the buyer a semantic graph for one decision, every piece of evidence with its source, its age and which way it points, checked against their own rules. And I think the clever move is a judo move: do everything apart from the trade. Leave the trade to the platforms that already do it. You avoid holding money and keys, and becoming the single point of failure, and you compete with nobody. The person decides. A working demo shows two decisions: do I buy gold, and is this new token safe.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: decisions, knowledge-graph, agents, finance, crypto, riskmandate, information-asymmetry, demo, article
status: published
---

!shot mfs-lemons.webp | images/ | From a market for lemons, where the seller knows more, to a market for sweets, where the buyer gets the evidence. | comparison

## In short {#in-short}

- **A market for lemons** is one where sellers know more than buyers, so buyers cannot tell good from bad.
- **New token markets are an extreme case:** by my friend's count, about 61,000 new tokens a day, and many are traps.
- **A market for sweets** breaks the asymmetry: a semantic graph for one decision, every piece of evidence with its source.
- **The agent gathers and weighs; it does not trade.** Its reach and mandate are written down.
- **The judo move:** do everything apart from the trade, and leave execution to platforms that already do it.
- **The person decides,** with a record of what they saw. **Try it:** [a working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha).

## A market for lemons {#lemons}

George Akerlof's paper of 1970, The Market for "Lemons", used second-hand cars to show something general. When the seller knows whether a car is good and the buyer does not, the buyer will only pay for an average car. Owners of good cars will not sell at that price, so they leave, the average gets worse, and the market fills with lemons.

My friend described the crypto version. Anyone can launch a token, and by his count about 61,000 new ones appear every day. Many are scams: a contract whose owner can mint more tokens or stop people selling, a pool of money that can be withdrawn at any moment, a handful of wallets holding almost all of it. His team audits tokens and tries to warn people off the bad ones, because, as he put it, they are stealing people's money.

## A market for sweets {#sweets}

The opposite of a market for lemons is a market where the buyer can see what the seller sees. I would call it a market for sweets. Its core is not a recommendation, which is just another thing to trust, but a semantic graph for one decision: the question in the middle, and around it every piece of evidence, each with its source, how old it is, which way it points and how much it weighs.

It is the same idea we used in PrompTugal.news, where every claim had to point at a source opened at its own address ([PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html)), applied to a decision instead of a story.

The graph is checked against the person's own rules: no more than a tenth of savings in one asset, no borrowing to invest, never a token whose owner can stop you selling. When a rule fails, the graph says so. And a decision record keeps what the person saw when they chose, so they can learn from it later.

!shot dmo-sweets.webp | images/ | The demo's third tab: a decision graph for buying gold, the evidence, your rules, the agent's mandate and your choice. | screenshot

## The agent gathers; it does not trade {#agent}

My friend made a sharp point. Ask a general assistant to buy a token for you and it will refuse. He wants agents that can work with his platform, and he sees people using agents to trade while they sleep.

I would draw the line in a different place. Let the agent do everything up to the decision: gather prices, reports and public chain data, read the contract, check the evidence against your rules, weigh it and explain it in words and one picture. Write down what it may reach and what it was asked to do, and that it may not connect a wallet, sign, buy or sell. That gap between reach and mandate is exactly what RiskMandate is for ([what can your agent reach?](/articles/what-can-your-agent-reach.html)).

!shot dmo-token.webp | images/ | The same tab for a token launched yesterday: two of your own rules fail, and the evidence points strongly against. | screenshot

## The judo move: everything but the trade {#judo}

!shot mfs-judo.webp | images/ | Gather, check, weigh, explain, decide, and stop before the trade, which stays with an existing platform. | flow

My advice to my friend, and to anyone building this, is to do everything apart from the trade. There are already platforms that execute trades, and you can integrate with them, but leave execution a little outside.

The moment you do the trade, everything gets bigger and more serious. You hold people's money and keys, you may take on a broker's or custodian's obligations, and you become the single point of failure. Before the trade, you compete with nobody: every platform can use the evidence, and every person can take it to the platform they already trust.

And the person decides. We do not make decisions for you; we give you enough evidence that you can, and if you want to throw the dice a little, that is your call, made with your eyes open.

## Wider than crypto {#wider}

Crypto is a good place to start because it moves fast and the traps are visible on the chain. But the pattern is any decision where one side knows more: do I buy gold this month, do I buy this share, this fund, this insurance, this second-hand car. The demo's first example is deliberately gold, not a token.

## Try the demo {#demo}

[The demo's third tab](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha) has two made-up decisions: should I put part of my savings into gold this month, and is a token that launched yesterday safe to buy. Each has a decision graph, the evidence with sources and ages, your rules applied, the agent's reach and mandate, the balance, and three choices that write a decision record in your browser. Nothing in it is real data, nothing is advice, and nothing is traded.

## What this does not claim {#limits}

- **This is not financial advice,** and the demo's evidence, sources and numbers are made up.
- **"About 61,000 new tokens a day" is my friend's figure,** from his work in the market; I have not checked it.
- **The line at the trade is my recommendation,** not a legal opinion; where it falls for a given business is a question for its lawyers.
- **My friend's company is not named,** and nothing here is from it beyond what he described.

## Where this comes from {#sources}

George A. Akerlof, The Market for "Lemons": Quality Uncertainty and the Market Mechanism, The Quarterly Journal of Economics, 1970. A conversation with a friend in crypto, 15 November 2026. Earlier on this site: [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html), [the grant, not the prompt](/articles/the-grant-not-the-prompt.html), and the two companion articles, [a brain you arrive at](/articles/a-brain-you-arrive-at.html) and [the new data lake](/articles/the-new-data-lake.html).
