# A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others, sgit.ai

> In 1970 George Akerlof described the market for lemons: when sellers know more than buyers, buyers cannot tell good from bad, and good sellers leave. A friend who has spent almost eleven years in crypto lives in one: by his count, about 61,000 new tokens appear every day, and many are traps, a contract that lets the owner take the money, a few wallets holding almost everything. His team audits tokens to warn people off the bad ones, and wants agents to do more of it. I think the opportunity is the opposite of a market for lemons, a market for sweets: give the buyer a semantic graph for one decision, every piece of evidence with its source, its age and which way it points, checked against their own rules. And I think the clever move is a judo move: do everything apart from the trade. Leave the trade to the platforms that already do it. You avoid holding money and keys, and becoming the single point of failure, and you compete with nobody. The person decides. A working demo shows two decisions: do I buy gold, and is this new token safe.

*Source: <https://newsroom.sgit.ai/articles/a-market-for-sweets.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others

# A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/a-market-for-sweets.md) · [newsroom v0.14.94](https://newsroom.sgit.ai/admin/versions.html) · decisionsknowledge-graphagentsfinancecryptoriskmandateinformation-asymmetrydemoarticle

***Abstract:** In 1970 George Akerlof described the market for lemons: when sellers know more than buyers, buyers cannot tell good from bad, and good sellers leave. A friend who has spent almost eleven years in crypto lives in one: by his count, about 61,000 new tokens appear every day, and many are traps, a contract that lets the owner take the money, a few wallets holding almost everything. His team audits tokens to warn people off the bad ones, and wants agents to do more of it. I think the opportunity is the opposite of a market for lemons, a market for sweets: give the buyer a semantic graph for one decision, every piece of evidence with its source, its age and which way it points, checked against their own rules. And I think the clever move is a judo move: do everything apart from the trade. Leave the trade to the platforms that already do it. You avoid holding money and keys, and becoming the single point of failure, and you compete with nobody. The person decides. A working demo shows two decisions: do I buy gold, and is this new token safe.*

From a market for lemons, where the seller knows more, to a market for sweets, where the buyer gets the evidence.

## In short

- **A market for lemons** is one where sellers know more than buyers, so buyers cannot tell good from bad.
- **New token markets are an extreme case:** by my friend's count, about 61,000 new tokens a day, and many are traps.
- **A market for sweets** breaks the asymmetry: a semantic graph for one decision, every piece of evidence with its source.
- **The agent gathers and weighs; it does not trade.** Its reach and mandate are written down.
- **The judo move:** do everything apart from the trade, and leave execution to platforms that already do it.
- **The person decides,** with a record of what they saw. **Try it:** [a working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha).

## A market for lemons

George Akerlof's paper of 1970, The Market for "Lemons", used second-hand cars to show something general. When the seller knows whether a car is good and the buyer does not, the buyer will only pay for an average car. Owners of good cars will not sell at that price, so they leave, the average gets worse, and the market fills with lemons.

My friend described the crypto version. Anyone can launch a token, and by his count about 61,000 new ones appear every day. Many are scams: a contract whose owner can mint more tokens or stop people selling, a pool of money that can be withdrawn at any moment, a handful of wallets holding almost all of it. His team audits tokens and tries to warn people off the bad ones, because, as he put it, they are stealing people's money.

## A market for sweets

The opposite of a market for lemons is a market where the buyer can see what the seller sees. I would call it a market for sweets. Its core is not a recommendation, which is just another thing to trust, but a semantic graph for one decision: the question in the middle, and around it every piece of evidence, each with its source, how old it is, which way it points and how much it weighs.

It is the same idea we used in PrompTugal.news, where every claim had to point at a source opened at its own address ([PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md)), applied to a decision instead of a story.

The graph is checked against the person's own rules: no more than a tenth of savings in one asset, no borrowing to invest, never a token whose owner can stop you selling. When a rule fails, the graph says so. And a decision record keeps what the person saw when they chose, so they can learn from it later.

The demo's third tab: a decision graph for buying gold, the evidence, your rules, the agent's mandate and your choice.

## The agent gathers; it does not trade

My friend made a sharp point. Ask a general assistant to buy a token for you and it will refuse. He wants agents that can work with his platform, and he sees people using agents to trade while they sleep.

I would draw the line in a different place. Let the agent do everything up to the decision: gather prices, reports and public chain data, read the contract, check the evidence against your rules, weigh it and explain it in words and one picture. Write down what it may reach and what it was asked to do, and that it may not connect a wallet, sign, buy or sell. That gap between reach and mandate is exactly what RiskMandate is for ([what can your agent reach?](what-can-your-agent-reach.md)).

The same tab for a token launched yesterday: two of your own rules fail, and the evidence points strongly against.

## The judo move: everything but the trade

Gather, check, weigh, explain, decide, and stop before the trade, which stays with an existing platform.

My advice to my friend, and to anyone building this, is to do everything apart from the trade. There are already platforms that execute trades, and you can integrate with them, but leave execution a little outside.

The moment you do the trade, everything gets bigger and more serious. You hold people's money and keys, you may take on a broker's or custodian's obligations, and you become the single point of failure. Before the trade, you compete with nobody: every platform can use the evidence, and every person can take it to the platform they already trust.

And the person decides. We do not make decisions for you; we give you enough evidence that you can, and if you want to throw the dice a little, that is your call, made with your eyes open.

## Wider than crypto

Crypto is a good place to start because it moves fast and the traps are visible on the chain. But the pattern is any decision where one side knows more: do I buy gold this month, do I buy this share, this fund, this insurance, this second-hand car. The demo's first example is deliberately gold, not a token.

## Try the demo

[The demo's third tab](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha) has two made-up decisions: should I put part of my savings into gold this month, and is a token that launched yesterday safe to buy. Each has a decision graph, the evidence with sources and ages, your rules applied, the agent's reach and mandate, the balance, and three choices that write a decision record in your browser. Nothing in it is real data, nothing is advice, and nothing is traded.

## What this does not claim

- **This is not financial advice,** and the demo's evidence, sources and numbers are made up.
- **"About 61,000 new tokens a day" is my friend's figure,** from his work in the market; I have not checked it.
- **The line at the trade is my recommendation,** not a legal opinion; where it falls for a given business is a question for its lawyers.
- **My friend's company is not named,** and nothing here is from it beyond what he described.

## Where this comes from

George A. Akerlof, The Market for "Lemons": Quality Uncertainty and the Market Mechanism, The Quarterly Journal of Economics, 1970. A conversation with a friend in crypto, 15 November 2026. Earlier on this site: [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md), [what can your agent reach?](what-can-your-agent-reach.md), [the grant, not the prompt](the-grant-not-the-prompt.md), and the two companion articles, [a brain you arrive at](a-brain-you-arrive-at.md) and [the new data lake](the-new-data-lake.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#a-market-for-sweets)

### Builds on

- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [The grant, not the prompt: a technical user believed Claude could only read his email when he asked, and in an unrelated chat it listed his inbox, the gap between mandate and reach that RiskMandate is built to close](the-grant-not-the-prompt.md) A technical user believed Claude read his email only when asked; an unrelated chat listed his inbox.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.

### Continued by

- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 404 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=404)

**Posting this article on LinkedIn?** The cover is [a-market-for-sweets.jpg](banners/a-market-for-sweets.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-market-for-sweets.html)*
