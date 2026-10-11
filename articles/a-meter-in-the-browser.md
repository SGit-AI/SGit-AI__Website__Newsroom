# A meter in the browser: a penny a page, a history you keep, and a site that picks for you, sgit.ai

> Every page on sgit.ai now has a price, a few pence, and a meter in the corner of the screen that debits it from five pounds of starting credit. There is a reading account with a history, a price table, a top-up page with a cart and a checkout that has every step except the payment, and an out-of-credit state that never blocks a page. All of it lives in the reader's browser and nowhere else: no account, no server, no card, nothing sent. Open a private window and the meter starts again at five pounds, which looks like a way to read for free, except that it also starts again with no history, and the history is what the site uses to pick articles for you. That is the trade this experiment puts in front of a reader: pay a little, keep the record of what you read on your own machine, and get a site that knows you back. Whether people would make that trade is the question worth testing, and a meter that charges nothing is the cheapest way to start.

*Source: <https://newsroom.sgit.ai/articles/a-meter-in-the-browser.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A meter in the browser: a penny a page, a history you keep, and a site that picks for you

# A meter in the browser: a penny a page, a history you keep, and a site that picks for you

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.1.0, 2 versions](versions/a-meter-in-the-browser.md) · newsroommicropaymentspersonalisationlocal-firstprivacypricingearly-accessarticle

***Abstract:** Every page on sgit.ai now has a price, a few pence, and a meter in the corner of the screen that debits it from five pounds of starting credit. There is a reading account with a history, a price table, a top-up page with a cart and a checkout that has every step except the payment, and an out-of-credit state that never blocks a page. All of it lives in the reader's browser and nowhere else: no account, no server, no card, nothing sent. Open a private window and the meter starts again at five pounds, which looks like a way to read for free, except that it also starts again with no history, and the history is what the site uses to pick articles for you. That is the trade this experiment puts in front of a reader: pay a little, keep the record of what you read on your own machine, and get a site that knows you back. Whether people would make that trade is the question worth testing, and a meter that charges nothing is the cheapest way to start.*

The reading account, as it looks after ten pages: the balance, what was spent, the articles picked for this reader from what they read, and what they paid to read, by topic. All of it is computed in the browser from a history kept in the browser.

**Updated the same day, v0.7.26: this describes the first version.** The meter has since gone live: it charges by how much of a page you read, your balance can go below zero with nothing blocked and no bar, you can decline to pay for a page with a reason, the badge is now a small balance in the top bar, and topping up is a £5 Stripe payment. Prices rose to 10p and 5p for articles. The plan and the reasoning are in [going live with the reading meter](going-live-with-the-reading-meter.md); the library is [SG Meter](../meter/index.md). What follows is kept as it was written.

## What it does

- **Every page has a price.** An article published in the last seven days costs 5p, an older one 3p, a newsletter issue, a desk note or a collection 2p, any other page 1p. The homepage, the subscribe page and your own account are free. The full table is on [the account page](../account/index.md#prices).
- **You start with £5.00** of credit, and each page you open is debited once per visit. Going back to a page you opened in the same browser session costs nothing.
- **A badge in the corner** shows your balance and what this page cost, and links to your account.
- **Out of credit, nothing is blocked.** The page is shown, the read is recorded as unpaid, and a bar offers a top-up.
- **Topping up** has every step of a real shop except the payment: four packs, a cart you can adjust, a review step, a confirm button and a receipt. The credit lands at once.
- **Your account** has the history, the receipts, a pause button, an export of everything as JSON, and a button to start again.
An article as a reader sees it: the badge in the bottom-left corner shows the balance and what this page cost. It links to the account.

## The history is the product

The balance is the obvious part. The less obvious part is the list of what you read, with the topics each article belongs to, which the meter keeps because a ledger has to. That list is enough to personalise the site. Your account picks unread articles from the topics you have read most, and so does the front page, in a band called *Picked for you* that only appears once there is a history to pick from.

The front page after a handful of reads: a Picked for you band, filled from this browser's history and nowhere else.

None of this needs an account, a cookie banner or a server. The articles and their topics are already published as one file, `articles/graphs.json`, the data behind [the articles as graphs](graphs.md), and the browser does the arithmetic. The history never leaves the machine it was made on.

Which means there is an obvious way to cheat. Open a private window, or a different browser, and the meter starts again at £5.00. You can read for free forever. What you cannot do is take your history with you, so you start again with no picks, a front page that knows nothing about you, and an account with nothing in it. **The meter can be escaped; the personalisation cannot be copied.** That is the experiment: does a site that knows what you read, without anybody else knowing, make a few pence a page feel like a fair price? Or do people open the private window?

## Why a meter that charges nothing

Because it is the cheapest honest way to ask the question. [The question is whether they miss it](the-question-is-whether-they-miss-it.md) argues for shipping something usable, giving it away, and watching whether anybody notices when it goes. [Price it, then give it away](price-it-then-give-it-away.md) adds the step before: define the product, put a price on it, and offer it free to people who know you, because the price is a statement of what you think it is worth. A meter that shows the price on every page, and charges nothing, is that step made visible. The reader sees what a page would cost, what they have spent, and what it bought them, without anybody's money moving.

The idea is old. [How news got here](how-news-got-here.md) tells the story of a payment code reserved in the web's own protocol in 1997, 402 Payment Required, still waiting for a payment system to use it. This meter does not answer how a penny should move. It asks something that comes before it: whether the interesting part is the payment at all, or what the reader gets back for the record of having paid.

## Where it came from

The first version of this was on [pt.newsroom.sgit.ai](https://pt.newsroom.sgit.ai/carteira/), the Portuguese newsroom: one cent a page, a five-euro wallet that refills itself when it empties, and a ledger with a page of its own. Its rules were right and are kept here: say first that it is a demonstration, never block a page, charge once per page per visit so the back button is not a purchase, and let the page work if the browser refuses to store anything.

This version adds three things. Prices that depend on what a page is and how new it is, set in one place in the site's build so the published table and the meter cannot disagree. A top-up you choose, through a cart, instead of a refill that happens to you. And the personalisation, which is the reason to keep a history at all.

Topping up: two packs in the cart, and the review step where a card form or a wallet button would go. None is shown and nothing is charged.

## What it does not do, yet

- **It holds no money.** Anybody can edit their own balance in the browser's developer tools. For a demonstration that is fine; for real money the balance needs a server, or receipts signed by one.
- **It does not follow you between devices.** The history stays where it was made. A version that syncs could keep the ledger in an encrypted vault that only the reader holds the key to, which is the kind of thing this site is built on; that is a proposal, not something built.
- **It does not meter agents.** Reading a page's markdown twin, or the newsroom's [wire](../newsroom/index.md#agents), costs nothing. The other side of that question is in [the token bill nobody is sending](token-bill-nobody-is-sending.md).
- **It charges the same for every reader.** The obvious next prices are not per page but per question: a query over the reporting behind a story, the kind of thing [the bridge, followed to the end](the-bridge-followed-to-the-end.md) imagines readers and agents paying for in small amounts.
Out of credit: the page is still shown, the read is noted as unpaid, and the bar offers a top-up.

## Try it

Your meter has been running since you arrived. [Your account](../account/index.md) shows what it has recorded; [top up](../account/top-up.md) to walk through the cart; and open this page in a private window to see what starting again costs you.

*Drafted from a voice note by Dinis Cruz, who is the author of the idea and has editorial responsibility, by a Claude Code session working as the sgit.ai newsroom, on 10 October 2026. The meter is `assets/meter.js`; its prices are `METER` in `admin/build/build_pages.py`; the screenshots were taken from this site with the meter running.*

## Threads

Startups & strategyNews & evidence[This article as a graph →](graphs.md#a-meter-in-the-browser)

### Builds on

- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [For a startup, the most important question is whether they miss it](the-question-is-whether-they-miss-it.md) Ship something usable, give it away briefly, take it away and see whether anybody misses it; charge at a profit before you talk to investors.
- [Price it, then give it away: the early access programme as the next step after "do they miss it"](price-it-then-give-it-away.md) Define the product, price it, deliver it at a cost that grows a step at a time, then offer it free to people who know you and measure what it costs them.
- [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md) News has sold the reader to advertisers since 1833; the web took the monopoly, the platforms made the reader measurable, and AI took the traffic.
- [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md) AI answer engines pay to read the web as HTML; a publisher who serves markdown, dates, hashes and a typed graph saves them tokens and should get a share.
- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.

### Continued by

- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [Open source is not free: who pays to keep the long tail working?](open-source-is-not-free.md) An old iMac, the long tail of old versions that projects are not paid to support, measured from public data, and five ways to pay for it, simulated.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 57 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=57)

**Posting this article on LinkedIn?** The cover is [a-meter-in-the-browser.jpg](banners/a-meter-in-the-browser.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-meter-in-the-browser.html)*
