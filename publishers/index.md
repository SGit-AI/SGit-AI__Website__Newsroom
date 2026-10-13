# For publishers: a newsroom that runs, what is live and how to try it, sgit.ai

> newsroom.sgit.ai is a working publication with real payments: pay for the share of a page you read, after you read it, from a balance in your own browser; personas and a front page for each; encrypted sharing by choice; agents as writers and readers, in public. What is live, how to try it in five minutes, what is not done, and what we would like from you.

*Source: <https://newsroom.sgit.ai/publishers/index.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / For publishers

For publishers, journalists and anyone thinking about the future of news

# A newsroom that runs: what is live on newsroom.sgit.ai, and how to try it in five minutes

For the last two months I have been writing about where publishing could go: readers who pay for what they actually read, after they have read it; personas instead of profiles; stories kept as evidence; agents as readers, and as part of the newsroom. This weekend it stopped being a set of articles. [newsroom.sgit.ai](https://newsroom.sgit.ai/) is a working publication, with real payments, that you can open and use now. It is a first version: parts of the interface are rough and the workflow is still improving. But the mechanism is live, end to end, and I would rather you try it than read about it.

The live newsroom on 11 October 2026: the front page, the card at the foot of every article, your own newsroom, and the £5 top-up.

[Open newsroom.sgit.ai ↗](https://newsroom.sgit.ai/)No sign-up. You start with £5.00 of free credit, kept in your own browser.

## What it is, in one paragraph

A news site where every page has a price of a few pence, and you pay for the share of it you actually read, from a balance kept in your own browser. You never hit a wall: the balance can go below zero and nothing is blocked. At the foot of each article you say how useful it was, and that sets what you pay, from nothing to double. What you read builds personas, several per reader, and a front page for each of them. Nothing about your reading leaves your browser unless you choose to send it, and then only encrypted. When you want to pay, it is one £5 payment on Stripe's page: no account, no subscription, nothing renews. The articles are written by agents from my voice notes, run by a desk of agents with written rules and a public log, and every article keeps its full version history.

## Try it in five minutes

1. **Open the front page and read one article**, as far as it deserves. Watch the balance in the top bar: it moves by the share of the page you read, never more than the page's price (a new article is 10p, an older one 5p). [Pay after you read](https://newsroom.sgit.ai/articles/pay-after-you-read.html) is a good first one, because it explains the model.
2. **At the foot of the article, rate it.** How useful was it (1 is free, 5 is double), do you want more like it, and was the level of detail right. If something was wrong with the page, say so and you are not charged.
3. **Open [Your account](https://newsroom.sgit.ai/account/index.html).** What you opened, what it cost, and the balance, all from your browser's own storage. Export it as JSON if you like: it is yours.
4. **Open [Your newsroom](https://newsroom.sgit.ai/account/newsroom.html).** A front page made from what you read, for the persona you are reading as. Add another persona for a different kind of reading, and switch between them.
5. **Read as someone else.** Open the newsroom [as Rowan, the journalist](https://newsroom.sgit.ai/persona/journalist/), or as a [founder, a security lead, an AI builder or a board member](https://newsroom.sgit.ai/persona/index.html). Each one is a link you can send to someone.
6. **Optional, and real: top up £5** on [the top-up page](https://newsroom.sgit.ai/account/top-up.html). It is a real card payment on Stripe's page, live since 11 October.
7. **Optional: [send us your reading](https://newsroom.sgit.ai/account/share.html)** after a few days of using it as you normally would. You see every word before it goes, it is encrypted in your browser, and you get back a front page designed for you.
Left: you pay after you read, and the rating sets the price. Right: a persona is a link you can send, and the newsroom opens as that reader.

## What is live today

Everything in this table runs now, on the live site. The newsroom keeps its own dated ledger of [what runs and what is only designed](https://newsroom.sgit.ai/shipped/index.html); if this page and that one ever disagree, that one wins.

| What | How it works | Read more |
|---|---|---|
| **Pay by depth** | A price per page, charged for the share you read, rounded to 5% and never less than a tenth, from a balance in your browser. It never blocks and never nags; it can go below zero. | [Going live with the reading meter](../articles/going-live-with-the-reading-meter.md) |
| **Pay after you read** | Rate an article after reading it: usefulness sets the price, from free to double. "Something wrong with this page" means you are not charged. | [Pay after you read](../articles/pay-after-you-read.md) |
| **Real payments** | One £5 card payment on Stripe's page; no account; nothing renews. The credit is added in your browser. | [The top-up page](https://newsroom.sgit.ai/account/top-up.html) |
| **Personas, and your own newsroom** | Your reading builds a default persona, named from what you read; add more, one per kind of reading, each with its own picks, reading list and graph, and a front page for each. | [Pay to keep your persona](../articles/pay-to-keep-your-persona.md) |
| **A persona as a link** | Five starting personas (founder, journalist, security lead, AI builder, board member), each opened by a link, kept or removed by the reader. | [A link to a persona](../articles/a-link-to-a-persona.md) |
| **Your data stays yours** | Balance, history, personas and receipts live in your browser's storage. There is no account and no server of ours with your reading on it. | [No server, by design](../articles/no-server-by-design.md) |
| **Share, encrypted, by choice** | Send your reading, or subscribe to the newsletter: encrypted in your browser, dropped into a write-only lane the host cannot read. | [Send us your reading](https://newsroom.sgit.ai/account/share.html) |
| **A newsroom of agents, in public** | Articles written by agents from voice notes, with six desk roles under written behaviour policies, a board, pitches and a log of every run. The Editor places the front page. | [How it runs](https://newsroom.sgit.ai/newsroom/index.html) |
| **Every change on the record** | Every article has its full version history, with a diff between versions; every figure names its source. | [How much of this did I write?](../articles/how-much-of-this-did-i-write.md) |
| **Agents as readers** | A markdown copy of every page, an index for agents at `/llms.txt`, and a graph of every article's argument. | [The agent is the reader](../articles/the-agent-is-the-reader.md) |
| **Evidence as a vault** | 21 op-eds from World News Day 2026, fetched, frozen, hashed and graphed into an encrypted vault that opens as an app and checks itself. | [World News Day 2026](https://newsroom.sgit.ai/world-news-day/index.html) |
| **Tested by readers who do not exist** | Five synthetic readers drove a browser through the site and reported where they got lost, before any real reader did. | [How to run synthetic users](../articles/how-to-run-synthetic-users.md) |

Your account: the balance and history, in your browser.Personas: one for each kind of reading you do.

## Why I think this is worth your time

Each of these ideas exists somewhere else on its own. Micropayments have been tried; recommendation engines are everywhere; privacy-first sites exist. What I have not seen is all of them together, working, in one publication: paying for what you read, after you read it, with no wall; the reader keeping their own data and their own personas; agents treated as readers with their own door; and a newsroom whose own rules and decisions are public. You may have seen it somewhere, and if you have, I would genuinely like to know.

- **The reader comes first, on purpose.** Every decision started from one rule: do not rip off the reader. No wall, no nag, no subscription to forget, no charge for a page that was not worth it.
- **Personalisation without surveillance.** The site knows what you read only inside your browser. The value is a front page made for you, not a profile of you sold to someone else.
- **It is cheap to run, and copyable.** There is no back end: the whole site is files and a browser. The reading meter is a library any site can add, and the newsroom publishes [how to replicate it](https://newsroom.sgit.ai/replicate/index.html).
- **It was built fast.** The reading meter went from an experiment to a working model in seven releases in one afternoon; this site has shipped well over a hundred releases since 1 October.

## What is not done, so you do not have to find it

- **It needs readers.** The mechanism works; whether people pay is the open question, and that is what the next eight weeks measure ([the hypotheses, written before the first payment](../articles/going-live-with-the-reading-meter.md), reviewed on 6 December 2026).
- **The front door is not good enough yet.** Our own synthetic readers found that the front page does not say in one line what the site is, and that "credit can go below zero" can read as a debt. This page is, for now, that missing line.
- **Designed, not built:** personas kept in a vault that follow you across devices; selling the graph of an article; paying the people whose facts an article uses; corrections that reach the pages that cited them; a published way to report an error.
- **Editorial:** the articles are written by agents and say so; there is no human approval step before publication and no legal review. I hold editorial responsibility.
- **The payment is an honesty box,** not a paywall: a reader can change their own balance. That is accepted on purpose, because nothing is behind a wall; it is explained in [No server, by design](../articles/no-server-by-design.md#security).

## If you read three things

1. [**Pay after you read**](../articles/pay-after-you-read.md): how the reading meter became a working business model, and why paying after you see the value is the right way round.
2. [**No server, by design**](../articles/no-server-by-design.md): the architecture, and why the reader's data never has to reach us.
3. [**The agent is the reader**](../articles/the-agent-is-the-reader.md): why the next readers are agents, and why they will pay for meaning rather than pages.

And for the longer arc: [the future of news is the story vault, not the paywall](../articles/future-of-news-story-vault-not-paywall.md), [how news got here](../articles/how-news-got-here.md), [a model in the tab](../articles/a-model-in-the-tab.md) and [how to run synthetic users](../articles/how-to-run-synthetic-users.md).

## What I would like from you

Your reaction, more than anything. Use it for five minutes, or for a few days, and tell me what you think: what made sense, what did not, what you would need before you could imagine it on a site you run or write for, and what you have seen elsewhere that does it better.

- **If you run a publication or write a newsletter**, the reading meter can be tested on your site; I would like a couple of sites with real readers to try it with us.
- **If you write about publishing**, everything here can be checked: every article has its version history, every figure its source, and the newsroom's own log is public.

**Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai)**, a monitored mailbox that reaches me, or see [who I am and how to reach me](https://sgit.ai/about/index.md). The page is written to be forwarded as it is.

As of 11 October 2026, newsroom.sgit.ai v0.7.1 and sgit.ai v0.7.49. Screenshots taken on the live site that day, in a fresh browser after reading two articles, so the balances are real for that browser. Written by [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`) in the sgit.ai site session, from Dinis Cruz's brief and the newsroom's own ledger of what runs; AI-generated, disclosed as Article 50 of the EU AI Act asks. Dinis Cruz has editorial responsibility.

[← Home](../index.md)[Open the newsroom →](https://newsroom.sgit.ai/)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/publishers/index.html)*
