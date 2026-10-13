# Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks, sgit.ai

> The reading meter on sgit.ai stops being a demonstration. A page now costs what you read of it: scroll a tenth of the way down a new article and you pay a tenth of 10p. Your balance can go below zero and stay there; nothing is blocked and nothing nags, there is only a small balance in the top bar. If a page was not worth it you can say so, with a reason, and it is not charged. Topping up is one £5 payment on Stripe, with no account and nothing that renews, and the page you come back to adds the credit without being able to check it, on purpose. The meter is also packaged as a library any website can add. This article is the plan and the reasoning, written down before the results: the business case, what we expect, the numbers that would prove us wrong, and the date we look.

*Source: <https://newsroom.sgit.ai/articles/going-live-with-the-reading-meter.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks

# Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · updated 2026-10-11 · [article v1.3.0, 4 versions](versions/going-live-with-the-reading-meter.md) · newsroommicropaymentspricingpersonalisationlocal-firstbusiness-casehypothesesstripearticle

***Abstract:** The reading meter on sgit.ai stops being a demonstration. A page now costs what you read of it: scroll a tenth of the way down a new article and you pay a tenth of 10p. Your balance can go below zero and stay there; nothing is blocked and nothing nags, there is only a small balance in the top bar. If a page was not worth it you can say so, with a reason, and it is not charged. Topping up is one £5 payment on Stripe, with no account and nothing that renews, and the page you come back to adds the credit without being able to check it, on purpose. The meter is also packaged as a library any website can add. This article is the plan and the reasoning, written down before the results: the business case, what we expect, the numbers that would prove us wrong, and the date we look.*

The plan on one page: six changes, and the five hypotheses written down before the first payment, each with what we expect and what would prove us wrong.

**You are paying for this page, by how much of it you read.** It was published this week, so reading it to the end costs 10p. Your balance is in the top bar; if it is below zero, nothing happens. At the foot of the page you can see what you have paid, and decline to pay at all.

## In short

- **The meter goes live.** It charges by how far down a page you scroll, it lets your balance go below zero forever, it shows only a small balance in the top bar, and it lets you refuse to pay for a page, with a reason.
- **Paying is one £5 payment on Stripe.** No account, no subscription, nothing renews. The page you come back to adds the credit without checking it, because a site with no server cannot, and we say so.
- **The price is a hypothesis.** 10p for a new article read to the end, 5p for an older one, less for other pages. It could be wrong either way.
- **The bet** is that people pay for reading when nothing forces them to, if what they get back is a site that knows what they read, with the history kept on their own machine.
- **The anchors.** Five numbers we expect, the ones that would prove us wrong, and a review date: eight weeks after the payment link goes live.
- **It is a library now.** [SG Meter](../meter/index.md) is one web component another site can add, with its config, events, storage and [security model](../meter/security.md) written down.

## What changes today

[A meter in the browser](a-meter-in-the-browser.md) described the first version: every page debited from £5.00 of credit kept in the browser, a badge in the corner, a bar when credit ran out, a cart with every step but the payment. It was a demonstration and said so. Six things change.

1. **You pay for what you read.** A page's price is what it costs read to the end. You pay that times the share you scrolled through, never less than a tenth. Open a new article, read the first screen and leave: 1p. Read half: 5p. Reading further later in the same visit tops the same charge up.
2. **Your balance can go below zero, and stay there.** Nothing is blocked. Nothing pops up. There is no bar, no count of articles read, no request.
3. **One small number in the top bar.** The balance, as a link to your account. Below zero it changes colour, and its tooltip says nothing is blocked.
4. **"Not worth it? Don't charge me."** At the foot of an article, four reasons: the headline promised more than the page gave, not relevant to me, I did not really read it, another reason. The charge is refunded, and the reason is kept in your history as a signal. "Not relevant" counts against that page's topics when the site picks articles for you.
5. **A real payment.** The top-up becomes one £5 Stripe payment. The simulated cart stays only for a site with no payment link configured.
6. **A library.** The meter is rebuilt as [SG Meter](../meter/index.md), a web component that follows the estate's [JavaScript guidance](https://coding.sgit.ai/javascript/index.html), so another site can add it with a script tag and a config.
The foot of an article: what it has cost so far, for how much of it was read, the price to the end, and the choice not to pay, with four reasons. Kept in the reader's browser, nowhere else.The reading account below zero. This test account read sixteen articles to different depths and declined two; we then set its balance below zero in the browser's storage, the way any reader can. The balance in the top bar turns a warmer colour, and the account says nothing is blocked.

## Why below zero, and why no nagging

Most reader-funded sites do the opposite, and do it well. The Guardian counts what you read in your browser's own storage, the same place this meter keeps its history. Its open-source code keeps a weekly count under `gu.history.weeklyArticleCount`, with a count per tag, starting each week on a Monday, ignoring repeat visits to the same article and dropping weeks older than a year. The count is used to ask you for support.

It works. Press Gazette reported in September 2025 that the Guardian's digital reader revenue rose 22%, "from £88m in 2023/2024 to £107m in the year to the end of March 2025". Its tiers are £4 a month to support, £12 a month to "avoid intrusive pop-up supporter messages" and read without ads, and £27 a month with the print weekly. Its app, Press Gazette added, "sits within a paywall (free users can only read 20 articles per month)".

Two things in that are worth noticing. The middle tier sells, in part, the absence of the ask. And every tier is a subscription: £4 a month is £48 a year, £12 a month is £144 a year, a commitment decided once, in advance, for reading that has not happened yet. A one-off payment is the other door, and it is awkward in its own way: how much is fair, for what, and when?

This meter tries a third door. The ask is never made, because the balance is always visible and the price of each page is stated where you read it. The commitment is never asked for, because you pay for pages after you have read them, as much of them as you read, and you can refuse. And going below zero is not a failure state. It is information you have, about what you have read, kept where only you can see it.

The hypothesis is that a reader who can see an honest running total, and who is never shamed for it, is more willing to settle it than one who is counted and asked. More so as the site gives something back for the history: curation, picks, and in time a front page that is entirely personal to the reader, computed in their browser from what they read and what they declined. The first version of that front page is live the same day: [your newsroom](../account/newsroom.md), one per persona, and why personas are what a reader would pay to keep is in [pay to keep your persona](pay-to-keep-your-persona.md).

**Added later the same day, v0.7.34: the reader sets part of the price.** At the foot of every article there is now a reader card with three scales, each starting in the middle. *How useful was this?* changes what you pay: 1 is free, 3 is the price, 5 is double. *More like this?* changes how often you see pages like it. *Level of detail* tells your persona whether you want it lighter or deeper. "Don't charge me" is still there, at the end, as the exception. A page is now charged only as much as you read it *and* only as much as you say it was worth. Paying more for an excellent page is a signal we did not have before; it is in what you can [send us](../account/share.md).

## Why by depth

Because a page is not one thing. A reader who opens an article, sees in the first paragraph that it is not for them and leaves has not had the same page as one who read it to the end. Charging them the same is a small unfairness repeated many times, and it rewards exactly the wrong writing: a headline that gets the click, followed by a page nobody finishes.

Depth is measured on the page's main column, rounded to 5%, at most once every 400 milliseconds while you scroll and once more as you leave. It is not reading time and it is not attention; a reader can scroll to the bottom without reading. That is fine. The point is not to measure reading precisely. It is to make the price follow the reader's own choice to keep going, and to give them the refusal for the cases where it did not.

## Why "don't charge me" is the most useful button

A charge tells us nothing; everyone who scrolled was charged. A refusal, with a reason, is the first thing this site has ever been told by a reader about a page without asking them to write anything. "The headline promised more than the page gave" is a verdict on the writing. "Not relevant to me" is a verdict on the placement, and on the picks. "I did not really read it" is a correction to the depth.

They are kept in the reader's history, in their browser, like everything else, and used there: a page declined as not relevant pushes its topics down the reader's picks. We do not see them. If that changes, it will be because a reader chose to send their history, not because the meter sent it. Rating a page, classifying it and keeping a note on it are the obvious next steps, in the same local history. Not yet.

## The price is the hypothesis

| A page read to the end | Price | What £5 buys, read to the end |
|---|---|---|
| An article published in the last seven days | 10p | 50 |
| An older article | 5p | 100 |
| A newsletter issue | 3p | 166 |
| A desk note or a collection | 2p | 250 |
| Any other page: docs, vaults, the network | 1p | 500 |
| The homepage, subscribe, your account | free |  |

Read by depth, a fiver goes further than the table says, because most pages are not read to the end. These prices were raised from the first version's 5p and 3p for articles on purpose: a price that is too low teaches nothing, because nobody would ever notice paying it, and we would rather find out that 10p is too much than never find out whether anyone would pay 10p. It could be more. It could be less. The account page prints the current table, and the build prints it from the same `METER` rules the meter charges by, so the published price and the charged price cannot differ.

## The business case, honestly

The money first, because it is small and it should be said plainly. Stripe's listed UK fee for a standard UK card is 1.5% + 20p. On £5 that is 27.5p, so £4.72 reaches the site, about 94.5%. Premium UK cards are 2.8% + 20p (34p), European cards 2.5% + 20p (32.5p), international cards 3.15% + 20p (about 36p), plus 2% where the currency is converted. The fixed 20p is why the top-up is £5 and not £1: on £1, a standard card would cost 21.5p, more than a fifth.

| Payers in eight weeks | Gross | After a standard UK card fee |
|---|---|---|
| 10 | £50 | £47.25 |
| 50 | £250 | £236.25 |
| 200 | £1,000 | £945 |

None of those rows pays for anything that matters. That is not the case for doing this. The case is three things the money cannot buy.

- **Evidence.** Whether anyone pays for reading on a site that does not make them is the question in [the question is whether they miss it](the-question-is-whether-they-miss-it.md). A meter that charges nothing could only answer half of it. A payment is the only signal on this site that cannot be produced by curiosity.
- **A shape to test the personalisation against.** The history is the product, as the first article put it. If readers who pay are readers who read more, and who come back, that is the case for building the personal front page, and it costs nothing to collect because the reader collects it.
- **A library.** If it works here it works on any site that can add a script tag, which is a different and larger question about [how news got here](how-news-got-here.md) and whether a penny a page was ever the problem, or only the machinery around it. The same idea, from the other side, is [price it, then give it away](price-it-then-give-it-away.md): put a real price on the thing, then let people decide.

## Why an honesty box can work

There is evidence that people pay when nothing forces them to, and evidence of how much less they pay. Both belong here.

- **Paul Feldman's bagels.** For years he left bagels and an unwatched cash box in offices. *Freakonomics*, writing about him in the *New York Times Magazine* in June 2004, reported that about 87% of bagels were paid for by 2001, rising by about two points after September 11. He had set 90% as the rate he would call honest, and in his earlier, basket years, about 95%.
- **Radiohead's *In Rainbows*** was released in 2007 for whatever buyers chose to pay. comScore estimated that 38% of downloaders paid something (48% in the UK), that those who paid averaged about $6, and that the average across everyone who downloaded was $2.26.
- **Pay what you want, measured.** In a field experiment published in *Science* in 2010, Gneezy and colleagues sold photos at a theme park. At a fixed $12.95, 0.5% of riders bought. When riders could pay what they wanted, 8.39% bought, paying 92 cents on average. When half of what they paid went to charity, 4.49% bought, paying $5.33.

The pattern is the one this meter is built around. Remove the force and many more people take part, while the average payment falls. A small, stated price per page sits between the two: the reader is told what is fair, and left to decide.

## The anchors: what we expect, and what would prove us wrong

Written now, before there is a single payment, so that we cannot move the goalposts later. The clock starts when the Stripe link goes live; the review is eight weeks after that. If the link goes live today, that is **5 December 2026**. *Update, 11 October 2026: the link went live on newsroom.sgit.ai today, so the review is on **6 December 2026**.*

| # | Hypothesis | We expect | Proved wrong if |
|---|---|---|---|
| H1 | Someone pays when nothing forces them to | A first real payment within 14 days | No payment in 14 days |
| H2 | Enough pay for it to be a signal, not an accident | At least 10 different payers by the review | Fewer than 5 |
| H3 | Paying is a habit, not a gesture | At least 3 payers pay a second time | No repeat payment |
| H4 | Making cheating easy costs nothing that reaches us | No disputes or chargebacks | Any dispute that is not plain card fraud |
| H5 | Below zero is normal, not a reason to leave | Readers who send us their history mostly have a negative balance, and still read | We cannot test this without readers sending their history; it is written here so that we notice if we start to believe it without evidence |

What we can see, so that nobody has to take these on trust: the Stripe dashboard (payments, amounts, payers, repeat payers, disputes), and the views LinkedIn reports on the articles cross-posted there, which is the nearest thing to a denominator we have. What we cannot see: anything the meter records. There is no analytics on this site, and the meter sends nothing. The depth you read, the pages you declined and why, your balance: all of it is in your browser. If you want to help, the account page exports it as JSON, and you can send it to us. Nobody has to.

*Added the same day, before any payment:* two more hypotheses, H6 and H7, about what readers would pay for beyond reading, are in [pay to keep your persona](pay-to-keep-your-persona.md). The five above are unchanged.

We will publish the review on the review date, whatever it says, with the numbers from the Stripe dashboard. A hypothesis that fails is a result. The one outcome that would be a failure of the method is not looking.

## What would make us change course

- **If nobody pays (H1, H2),** the price is not the first suspect. The first suspect is that the trade is invisible: the balance is small, the payment is one click away from nowhere, and the personalisation is too thin to want. We would make the picks better before we made the meter louder.
- **If people pay once and not again (H3),** the history is not worth enough to them yet. That points at the personal front page, not at the price.
- **If cheating shows up somewhere we can see (H4),** the balance has started to unlock something, or someone is testing stolen cards. The first would need a server and a signed receipt; the second is Stripe's to stop, and the payment link can be switched off in a minute.
- **If the reasons readers send are mostly "the headline promised more than the page gave",** that is about the writing, and the newsroom's [behaviour policies](../newsroom/policies.md) are where it gets fixed.

## Who could cheat, and why we let them

Anyone, in several easy ways: edit the balance in developer tools, open a private window, or open the page a payment returns to with a made-up reference and get £5 of credit. Each of those changes a number only the cheater can see, and costs the site a payment it was never going to receive. Who would actually do it, how many of them there are, and which risks are real is the subject of the companion piece, [who will game the reading meter](who-will-game-the-reading-meter.md).

## Try it

Your meter has been running since you arrived. Scroll to the foot of this page to see what it has cost, and the choice not to pay. [Your account](../account/index.md) shows your balance, your history and the depth you read each page; [top up](../account/top-up.md) to settle it, or don't. If you run a site and want the same thing, [SG Meter](../meter/index.md) is the library.

*Written from a voice note by Dinis Cruz, who is the author of the idea and the plan and has editorial responsibility, by a Claude Code session working as the sgit.ai newsroom, on 10 October 2026. The Guardian figures are from Press Gazette's report of 12 September 2025 and the Guardian's open-source [support-dotcom-components](https://github.com/guardian/support-dotcom-components/blob/main/src/shared/lib/history.ts); the Stripe fees are Stripe's published UK prices on the day of writing; the bagel, Radiohead and theme-park figures are from the sources named beside them. The meter is [SG Meter v1.0.0](../meter/index.md); its prices are `METER` in `admin/build/build_pages.py`; the screenshots were taken from this site with the meter running.*

## Threads

Startups & strategyNews & evidence[This article as a graph →](graphs.md#going-live-with-the-reading-meter)

### Builds on

- [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md) Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [For a startup, the most important question is whether they miss it](the-question-is-whether-they-miss-it.md) Ship something usable, give it away briefly, take it away and see whether anybody misses it; charge at a profit before you talk to investors.
- [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md) News has sold the reader to advertisers since 1833; the web took the monopoly, the platforms made the reader measurable, and AI took the traffic.
- [Price it, then give it away: the early access programme as the next step after "do they miss it"](price-it-then-give-it-away.md) Define the product, price it, deliver it at a cost that grows a step at a time, then offer it free to people who know you and measure what it costs them.
- [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](who-will-game-the-reading-meter.md) Eight kinds of reader, none of them attackers, nine ways to cheat a browser meter, and the quieter risks that will actually happen.

### Continued by

- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](who-will-game-the-reading-meter.md) Eight kinds of reader, none of them attackers, nine ways to cheat a browser meter, and the quieter risks that will actually happen.
- [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md) Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 60 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=60)

**Posting this article on LinkedIn?** The cover is [going-live-with-the-reading-meter.jpg](banners/going-live-with-the-reading-meter.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/going-live-with-the-reading-meter.html)*
