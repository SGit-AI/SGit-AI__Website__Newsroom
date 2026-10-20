# Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running, sgit.ai

> Almost every time I buy something, I am buying future value. A subscription, a gym membership, a big security product on a good deal, even a one-off purchase: I am betting that I will use it enough for the price of each use to fall to a number I am comfortable with. Often I lose the bet, and the cost of unsubscribing keeps me paying. The research agrees: gym members on a monthly contract paid more than $17 a visit when they could have paid $10. This newsroom is trying the opposite. You start with £5 of credit, each article you read uses a few pence, you can set the price from free to double or refuse it, and the balance can go below zero and stay there. By the time you are asked to pay, you have the value in front of you: what you read, how much, what you liked. The payment is connected to what you received, not what you hope to receive. That only works where the cost of serving is close to zero, which is true of a static site on a CDN, and where the value adds up in a way the reader can see. Wikipedia is the counter-example: £20 a year asked for at a moment with no value in view, even though it is a few pence an article. Add prices fair by country, the Big Mac index for reading, and a view of where the money goes, and payment becomes a choice people are glad to make. The experiment is live, with written hypotheses and a review in December, and I will report back.

*Source: <https://newsroom.sgit.ai/articles/paying-after-the-value.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running

# Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/paying-after-the-value.md) · [newsroom v0.12.54](https://newsroom.sgit.ai/admin/versions.html) · business-modelspricingpsychologysubscriptionsreading-meterpay-after-you-readwikipedianewsroomarticle

***Abstract:** Almost every time I buy something, I am buying future value. A subscription, a gym membership, a big security product on a good deal, even a one-off purchase: I am betting that I will use it enough for the price of each use to fall to a number I am comfortable with. Often I lose the bet, and the cost of unsubscribing keeps me paying. The research agrees: gym members on a monthly contract paid more than $17 a visit when they could have paid $10. This newsroom is trying the opposite. You start with £5 of credit, each article you read uses a few pence, you can set the price from free to double or refuse it, and the balance can go below zero and stay there. By the time you are asked to pay, you have the value in front of you: what you read, how much, what you liked. The payment is connected to what you received, not what you hope to receive. That only works where the cost of serving is close to zero, which is true of a static site on a CDN, and where the value adds up in a way the reader can see. Wikipedia is the counter-example: £20 a year asked for at a moment with no value in view, even though it is a few pence an article. Add prices fair by country, the Big Mac index for reading, and a view of where the money goes, and payment becomes a choice people are glad to make. The experiment is live, with written hypotheses and a review in December, and I will report back.*

Paying for the future, or paying for what you got. A subscription, a gym or an annual donation asks you to pay at the moment of most doubt, for value that may arrive. A meter that lets the balance go negative turns it round: the value arrives first, piece by piece, and the payment comes when you can see what it bought.

## In short

- **Most purchases are bets on future value.** You pay first and hope to use it enough.
- **Often the bet is lost.** Gym members paid over $17 a visit when $10 was on offer.
- **Pay after the value instead.** Start with credit, use it page by page, let the balance go negative.
- **The payment meets the value.** By the time you pay, you can see what you read and what you liked.
- **It works where serving costs almost nothing.** A static site on a CDN is the extreme case.
- **Wikipedia shows the other way.** A yearly ask with no value in view, for something worth a few pence a page.
- **Fair, visible, chosen.** Prices by country, a view of where the money goes, and verified facts as their own product.
- **The experiment is live.** Seven hypotheses, a review on 6 December 2026.

## Buying the future

Almost every time I buy something, I am buying future value. In cyber security this is especially visible: expensive products, and very good deals, where a deal usually means more of the thing for a lower price per unit. A subscription is the same bet in smaller pieces: I will use this enough that the cost of each use falls to a level I accept. A gym membership, a streaming service, a magazine, even a one-off purchase I expect to use for years. The calculation is always the same, and it is always about the future.

The research says we are bad at it. Stefano DellaVigna and Ulrike Malmendier's [study of three gyms](https://eml.berkeley.edu/~ulrike/Papers/gym.pdf) found that "members who choose a contract with a flat monthly fee of over $70 attend on average 4.3 times per month", so "They pay a price per expected visit of more than $17, even though they could pay $10 per visit using a 10-visit pass." Then the cost of leaving does the rest. Subscriptions are easy to start and tiring to stop, which is why regulators keep trying to make cancelling as easy as signing up: the US Federal Trade Commission's click-to-cancel rule was vacated by a court in July 2025 and the process has started again, and the UK's new subscription rules are due in 2027.

## Paying hurts, and when you pay matters

Behavioural economists have a name for part of this: the pain of paying. Drazen Prelec and George Loewenstein wrote in 1998 that "The pain of paying, we argue, plays an important role in consumer self-regulation, but is hedonically costly." Their model also explains why we like paying up front: "consumption that has already been paid for can be enjoyed as if it were free." The same work shows the cost of it. In a study John Gourville and Dilip Soman reported, people who paid in advance for a season of four plays had "a no-show rate of 21.5 percent", against under one percent for people who bought a ticket for a single play: once the payment is in the past, it stops pulling you to use what you bought.

So paying first feels good at the moment of use and bad at the moment of payment, and it quietly decouples the two. Paying after the value couples them again, on purpose, at the end. The payment comes when the value is in view, and the value is what makes the payment feel fair.

## The newsroom's version

The experiment, as it runs today and what comes next: what the reading meter on this site does now, what is partly built, and what this article proposes, with the five hypotheses it will be reviewed against on 6 December 2026.

This site runs the experiment, and its rules are written down in [Pay after you read](pay-after-you-read.md) and [Going live with the reading meter](going-live-with-the-reading-meter.md). "Everyone starts with £5.00 of credit." Reading uses it: "10p for a new article read to the end, 5p for an older one, less for other pages", and only as far as you read, so the first screen of an article costs a penny. You set the price: a rating moves it from free to double, and you can refuse to pay for a page, with a reason, and the charge comes back. And "Your balance can go below zero and stay there; nothing is blocked and nothing nags." When you want to, you top up with one £5 payment link, which has been live on this site since 11 October, with no account and nothing that renews.

The point of the negative balance is psychological, not financial. By the time you are below zero, you have read dozens of articles, fifty if you read every one of them to the end, you can see which ones, and how far you got. Each one was a small piece of value, and each one, if it was good, felt good. The request to pay arrives after all of that, and it is connected to it. Starting at £5 rather than zero matters too: a reader who tops up again is paying for what they have already consumed, not for what they hope to consume.

## Wikipedia, and the value you never add up

Wikipedia is the clearest counter-example, and I say that as someone who values it enormously. Its fundraising raised [US$184.5 million](https://meta.wikimedia.org/wiki/Fundraising/2024-25_Report) in 2024 to 2025, from 7.7 million donors, an average of about US$10. But the ask arrives as a lump sum, at a moment when the value is not in view. Whatever the number, a once-a-year request feels heavy, because the value is thousands of small moments that nobody adds up: the answers found, the time saved, the roads not taken because you knew better. It is the tragedy of the commons applied to your own reading: each benefit is too small to feel, so the total never gets felt either.

Imagine the same ask with your year in front of you: the articles you read, how many, which ones you came back to. A penny an article for four hundred articles is £4, and it is easier to give when you can see the four hundred.

## Where it works

This model has a condition, and it is worth being plain about it. It only works where there is a very large gap between the cost of serving and what you can charge. Software has always had that gap, and a static website has it in the extreme: this site has no back end, pages are served from a CDN, and the cost of one more reader reading one more article is close to nothing. Even at 10p, the margin is very high. A business with a real cost per unit cannot let balances run negative for ever.

It also needs value that adds up in a way the reader can see. That is why I keep wanting the reading history for myself: which pages I read, which I skimmed, which I meant to come back to, which I liked, across every device I use. The billing is a side effect of that tracking, and the tracking is valuable on its own. [Pay to keep your persona](pay-to-keep-your-persona.md) made it a hypothesis: that readers will pay more for a history that follows them between devices than for reading alone. The reader can always delete it; it is theirs.

And it still works for readers who never pay. What they read, and what they rate, tells us which articles are worth writing.

## Fair, visible, chosen

Three more things would make it fairer and, I think, more successful.

**Fair by country.** 10p in the UK is not 10p everywhere. Prices should follow local purchasing power or wages, the way The Economist's Big Mac index is "an informal way of measuring the purchasing power parity" between currencies. Streaming services already do it; reading can too.

**Visible.** A reader should be able to see what the money pays for: better articles, fact checks, follow-ups. There is good evidence that this changes behaviour. In a [field experiment](https://newsroom.haas.berkeley.edu/name-your-price-pricing-strategy-aimed-achieving-corporate-social-responsibility-and/) at an amusement park, letting people pay what they wanted for a photo meant many bought one but "paid only about 92 cents each"; when half of what they paid went to charity, fewer bought, but they paid an average of $5.33.

**Chosen, at more than one level.** Verified facts are worth more than unverified ones, and to some readers, especially commercial ones, a lot more. A follow-up on a story they care about, a certified fact, a briefing with every claim checked: those are things people choose to pay for, separately, because they need them.

## The experiment

The good news is that this is not a thought experiment. The meter is live, real money can move, and the hypotheses were written before the first payment, in [Going live with the reading meter](going-live-with-the-reading-meter.md): H1, a first real payment within 14 days; H2, at least 10 payers by the review; H3, at least three who pay twice; H4, no disputes; H5, below zero is normal and not a reason to leave. Two more, about a persona that follows the reader between devices, are in Pay to keep your persona. The review is on 6 December 2026. I will come back in a few weeks, and again then, with what happened, including if nobody paid.

## What this does not claim

- **No results yet.** The meter has no analytics and the review is in December; nothing here says it works.
- **The balance is notional until you top up.** No debt is ever collected; a negative balance is a number on your screen.
- **The studies are about other things.** Gyms, theatre tickets and photos, not reading; they explain the psychology, not our results.
- **Regional prices, a view of where the money goes and the year-in-reading view are proposals.** Not built yet.
- **Wikipedia's figures are its own.** From its fundraising report for 2024 to 2025.

If you run a site, a product or a service where the cost of serving is close to zero and want to try paying after the value, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The meter's rules are from its code and the articles that set it live; a research agent gathered the evidence, and the quotes were checked on the pages themselves. DellaVigna and Malmendier, [Paying Not to Go to the Gym](https://eml.berkeley.edu/~ulrike/Papers/gym.pdf), American Economic Review, 2006; Prelec and Loewenstein, [The Red and the Black](https://ideas.repec.org/a/inm/ormksc/v17y1998i1p4-28.html), Marketing Science, 1998; Gourville and Soman as reported by [the Wilson Quarterly](https://www.wilsonquarterly.com/quarterly/_/feel-pain/); Gneezy and others as summarised by [Berkeley Haas](https://newsroom.haas.berkeley.edu/name-your-price-pricing-strategy-aimed-achieving-corporate-social-responsibility-and/); Wikimedia, [Fundraising 2024-25 report](https://meta.wikimedia.org/wiki/Fundraising/2024-25_Report); Wikipedia, [Big Mac Index](https://en.wikipedia.org/wiki/Big_Mac_Index); Latham and Watkins on [the FTC rule](https://www.lw.com/en/insights/eighth-circuit-vacates-ftc-click-to-cancel-rule). All read on 14 October 2026.

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#paying-after-the-value)

### Builds on

- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.

### Continued by

- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.
- [Can you sell it? Start selling what you have, however rough it is, because the point is not to sell, it is to learn](can-you-sell-it.md) Start selling what you have, however rough. The point is not the sale but what you learn trying, and a payment is the best signal there is.
- [Two years in, the opposite: an essay about burning out on AI that I could not buy, and why my two years of AI have been the most productive of my career](two-years-in-the-opposite.md) An essay about burning out on AI that I could not buy, three paragraphs and a subscription; and why my two years of AI were the opposite.
- [A book for one reader: a personalised edition of Generation Z Developers, assembled by an agent for one person, and paid for as it is read](a-book-for-one-reader.md) A personalised edition of Generation Z Developers, assembled by an agent for one person from a private brief, and paid for as it is read.
- [I just want to buy the article: what happened when I tried to pay Harvard Business Review for one piece I wanted to answer, the arithmetic of a subscription, and ten things HBR could sell a reader like me, most of them already running on this newsroom](i-just-want-to-buy-the-article.md) I tried to pay HBR for one article and was offered a subscription. The arithmetic says 24p to 55p; and ten things HBR could sell a reader like me.
- [Sell, don't issue: a funding model for founders who have already won, where the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest](sell-dont-issue.md) For founders who have already won: the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [The citizen developer is good news: the spreadsheet grown up, the best briefs ever written, and the handover from explorers to villagers and town planners that makes them last](the-citizen-developer.md) The citizen developer is the spreadsheet grown up: the best briefs ever written, handed to villagers and town planners, carried in versioned vaults.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 126 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=126)

**Posting this article on LinkedIn?** The cover is [paying-after-the-value.jpg](banners/paying-after-the-value.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/paying-after-the-value.html)*
