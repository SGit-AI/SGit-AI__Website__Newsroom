---
title: A newsroom that runs, and keeps changing: what is live on newsroom.sgit.ai, and how to try it in five minutes
nav_title: For publishers
eyebrow: For publishers, journalists and anyone thinking about the future of news
description: newsroom.sgit.ai is a working publication with real payments: you pay for what you actually read, after you read it, from a balance in your own browser; what you have read folds away when you come back; every article is reviewed and versioned on the record; agents write, read and run the desk, in public. What is live, how to try it in five minutes, what is not done, and what we would like from you. Rebuilt with every release, so it stays current.
---
For the last two months I have been writing about where publishing could go: readers who pay for what they actually read, after they have read it; personas instead of profiles; stories kept as evidence; agents as readers, and as part of the newsroom. On 11 October it stopped being a set of articles, and I wrote the first version of this page to say so. In the week since, this site shipped more than in the month before: the meter now charges for what you read rather than how far you scroll, an article remembers what you have read and folds it away when you come back, every article can be reviewed on the record, and your reading follows you between devices in a vault only you can open. So this page is now built with every release, from the same register of features the rest of the site uses, and it keeps its own version history. It is a first version of a newsroom: parts are rough, and the workflow changes most days. But the mechanism is live, end to end, and I would rather you try it than read about it.

{{status}}

[Open newsroom.sgit.ai](../index.html). No sign-up. You start with £5.00 of free credit, kept in your own browser.

## What it is, in one paragraph

A news site where every page has a price of a few pence, and you pay for the share of it you actually read, after you read it, from a balance kept in your own browser. Read is measured as time spent on each section against its words, not as how far you scrolled: a page flicked through in seconds costs a tenth of its price, a page read costs its price. You never hit a wall: the balance can go below zero and nothing is blocked. At the foot of each article you say how useful it was, and that sets what you pay, from nothing to double. Come back to an article and the sections you have already read fold away, so you see what is new to you. What you read builds personas, several per reader, and a front page for each. Nothing about your reading leaves your browser unless you choose to send it, and then only encrypted; if you want it on your other devices, it travels in an encrypted vault opened with your passkey. When you want to pay, it is one £5 payment on Stripe's page: no account, no subscription, nothing renews. The articles are written by agents from my voice notes, reviewed on the record by other models and by me, and every article keeps its full version history.

## Try it in five minutes

1. **Open the front page and read one article**, as far as it deserves. Watch the chip at the foot of the page: it says how much of each section you have read and what the page will cost, never more than its price (a new article is 10p, an older one 5p). [I just want to buy the article](../articles/i-just-want-to-buy-the-article.html) is a good first one, because it is the argument for this model written for publishers.
2. **At the foot of the article, rate it.** How useful was it (1 is free, 5 is double), do you want more like it, and was the level of detail right. If something was wrong with the page, say so and you are not charged.
3. **Come back to it.** Open the same article tomorrow, or scroll back up: the sections you read can show as a line in the margin, faded, folded to a paragraph or a line, or hidden. You choose in the chip's Settings, for every article or for one. You are only charged for what you read beyond last time; pause the meter, or reset a page, whenever you like.
4. **Open [Your account](../account/index.html).** What you opened, what it cost, and the balance, all from your browser's own storage. Export it as JSON if you like: it is yours.
5. **Read as someone else.** Open the newsroom [as Rowan, the journalist](../persona/journalist/index.html), or as a [founder, a security lead, an AI builder or a board member](../persona/index.html). Each one is a link you can send to someone. Or [make a reading list](../for/make.html) for a colleague: a link that opens the newsroom as the articles you chose for them, with your note.
6. **Optional, and real: top up £5** on [the top-up page](../account/top-up.html). It is a real card payment on Stripe's page, live since 11 October.
7. **Optional: open [your vault](../vault/index.html)** with a passkey, and the same reading account, notes and personas are on your phone and your laptop. The newsroom holds no key to it. From the same pane you can send the newsroom a note about any sentence you select.

## What changed since the first version of this page

The first version, on 11 October, was written once. These are the changes since then that I think matter most to a publisher; [every version of this page](versions/index.html) is kept, with what changed between them.

- **Charge for what is read, not for what is scrolled.** Since 17 October the meter takes attended time on each section, against its words at 300 a minute, instead of scroll depth. A return visit is charged only for what is read beyond the last one. [Scrolled is not read](../articles/scrolled-is-not-read.html) and [Your reading, your controls](../articles/your-reading-your-controls.html).
- **What you have read folds away.** Every section of every article now has a one-line and a one-paragraph summary, which is what a folded section shows.
- **Reviews on the record.** Published criteria, one record per review, by another vendor's model, an open-weight model, me, and later the desk; every finding answered, fixed in which version, or declined and why. [Reviews on the record](../articles/reviews-on-the-record.html).
- **Your reading on every device.** The reader's own encrypted vault, opened with a passkey, merging devices, with a page to browse it. [The vault, opened](../articles/the-vault-opened.html).
- **Search, and ask the site.** The whole site searched in your browser, nothing sent; and answers from the site's own passages with the model in Chrome or your own key. [Free models, your own key](../articles/free-models-your-own-key.html).
- **Who is speaking.** Agents that write under their own names say so, with a page each; everything else is written from my voice memos and published under mine. [Who is speaking](../articles/who-is-speaking.html).
- **A section for publishers.** [The newsroom as a publisher reads it](../sections/publishers/index.html), placed by rule and kept current; this page is its overview. [A section for publishers](../articles/a-section-for-publishers.html).
- **The briefs, in the open.** Everything this newsroom has asked of itself, audited from the code: what is built, what is partly built, and what is not. [The briefs so far](../articles/the-briefs-so-far.html).

## What is live today

{{features}}

The newsroom keeps its own dated ledger of [what runs and what is only designed](../shipped/index.html); if this page and that one ever disagree, that one wins.

## The newest for publishers

The newest pieces on how news gets paid for, answers to the industry, and how readers read here, placed in [the publishers' section](../sections/publishers/index.html) by rule as they were published.

{{latest}}

## Why I think this is worth your time

Each of these ideas exists somewhere else on its own. Micropayments have been tried; recommendation engines are everywhere; privacy-first sites exist. What I have not seen is all of them together, working, in one publication: paying for what you read, after you read it, with no wall; the reader keeping their own data and their own personas; agents treated as readers with their own door; and a newsroom whose own rules, reviews and decisions are public. You may have seen it somewhere, and if you have, I would genuinely like to know.

- **The reader comes first, on purpose.** Every decision started from one rule: do not rip off the reader. No wall, no nag, no subscription to forget, no charge for a page that was not worth it, and since last week, no charge for a page that was only scrolled.
- **Personalisation without surveillance.** The site knows what you read only inside your browser and your own vault. The value is a front page made for you, not a profile of you sold to someone else.
- **It is cheap to run, and copyable.** There is no back end: the whole site is files and a browser. The reading meter is a library any site can add, the reader's side is published at [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/), and the newsroom publishes [how to replicate it](../replicate/index.html).
- **Quality control you can see.** Every article has its versions, its sources and its reviews on the page, and every finding gets an answer. A correction is a new version, dated and linkable, not a silent edit.
- **It is built fast.** {{releases_since_first}} releases since the first version of this page on 11 October; this page is now rebuilt in every one of them.

## What is not done, so you do not have to find it

- **It needs readers.** The mechanism works; whether people pay is the open question, and that is what the weeks to 6 December measure ([the hypotheses, written before the first payment](../articles/going-live-with-the-reading-meter.html)).
- **The payment is an honesty box,** not a paywall: a reader can change their own balance. That is accepted on purpose, because nothing is behind a wall; it is explained in [No server, by design](../articles/no-server-by-design.html#security).
- **Editorial:** the articles are written by agents and say so; reviews are on the record, but there is no human approval step before publication and no legal review. I hold editorial responsibility.
- **Designed, not running yet:**

{{designed}}

## If you read five things

These are the five I would start a publisher with, the same five that open [the publishers' section](../sections/publishers/index.html).

{{start_here}}

## What I would like from you

Your reaction, more than anything. Use it for five minutes, or for a few days, and tell me what you think: what made sense, what did not, what you would need before you could imagine it on a site you run or write for, and what you have seen elsewhere that does it better.

- **If you run a publication or write a newsletter**, the reading meter can be tested on your site; I would like a couple of sites with real readers to try it with us.
- **If you write about publishing**, everything here can be checked: every article has its version history, its reviews and every figure its source, and the newsroom's own log is public.

**Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai)**, a monitored mailbox that reaches me, or see [who I am and how to reach me](https://sgit.ai/about/index.html). The page is written to be forwarded as it is.
