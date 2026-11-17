---
title: Paid by the read: a proposal to news editors who want more revenue from the journalism they already make, without another subscription, the evidence on micropayments and why it mostly failed, the meter that charges by how much of a page was read and runs in the reader's browser, free for any publisher, a revenue share when PrompTugal.news carries a newsroom's stories with their source, and the associations we should be talking to in the UK and Portugal
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: I agree with Nuno Costa of WizPress: journalism is a business, and right now it is not a good one. In the UK, around 300 local titles have closed since 2005 and the sector's revenue is a quarter of what it was in 2007, after inflation; 37 districts, home to 4.4 million people, have no dedicated local news. In Portugal, 171 of 308 municipalities are news deserts, semi-deserts or at risk. Only 10% of people in the UK and 8% in Portugal pay for online news, and most of the rest say they never will. Local journalism is the heart of it, and it is the part most at risk. Subscriptions are not going to fix that, and the micropayment experiments mostly failed, Blendle above all. But I think the reasons they failed are now fixable, and we have a model that I believe can work. Every reader starts with credit; every page costs a few pence; the reader pays for the share of it they actually read, measured in their own browser; nothing is ever blocked. It runs in this newsroom today, it needs no server and no database, and the code is free for any publisher. On top, a revenue share: when PrompTugal.news carries a newsroom's story, natively and with its source tracked, the newsroom gets its share of what readers pay. What we do not have yet is proof: our revenue is small, because our traffic is small. So this is a proposal to editors with readers, and to the associations that represent them: let us try it together, and see who pays.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: journalism, monetisation, micropayments, local-news, newsrooms, promptugal, wizpress, partnerships, article
status: published
---

!shot mon-models.webp | images/ | Four ways a newsroom earns from the read, not the subscription: the meter, a revenue share, licences, agents. | concept

## In short {#in-short}

- **Journalism is a business,** and local journalism is the part most at risk.
- **Subscriptions have hit a ceiling:** about one in ten people pay for online news in the UK and Portugal.
- **Micropayments mostly failed,** for reasons that are now fixable.
- **Our model: pay by the read,** measured in the reader's browser, nothing ever blocked.
- **The code is free for any publisher;** no server, no database.
- **A revenue share** when PrompTugal.news carries a newsroom's story with its source.
- **Not proven yet:** we need partners with traffic, and the associations that represent them.

## Journalism is a business {#business}

Talking to Nuno Costa of WizPress today, he said something I agree with completely: at the end of the day, journalism is a business ([working with WizPress](/articles/working-with-wizpress.html)). And it is in a hard place. In the UK, around 300 local titles have closed since 2005, the three biggest regional groups employ about 3,000 journalists against about 9,000 in 2007, and the sector's revenue is a quarter of its 2007 size after inflation, according to Press Gazette. The Public Interest News Foundation counts 37 local authority districts with no dedicated local news, home to 4.4 million people. In Portugal, the LabCom study of news deserts at the University of Beira Interior found 45 of 308 municipalities with no local news, and 171, more than half, deserts, semi-deserts or at risk.

Local journalism is the heart of it. It is where a decision about a road, a school or a bridge gets reported, or does not. We have written about exactly that, following one local story to the end ([the bridge, followed to the end](/articles/the-bridge-followed-to-the-end.html)), and about trust that starts local and is certified upwards ([local trust, certified upwards](/articles/local-trust-certified-upwards.html)).

## Why subscriptions are not enough {#subscriptions}

The subscription works for a few large publishers. For everyone else it has hit a ceiling. The Reuters Institute's Digital News Report puts the share of people paying for online news at about 10% in the UK and 8% in Portugal in 2026, and in 2024 found 69% of people in the UK would never pay. Of those not paying, 10% said they would pay £1 or less a month. Piano's own benchmarks put paid-offer conversion at 0.15% of visitors in Europe.

I have felt this as a reader: I wanted one article, I was offered three subscriptions, and I paid nothing ([I just want to buy the article](/articles/i-just-want-to-buy-the-article.html)). Multiply that by every reader who arrives from a link, and that is the revenue a subscription cannot see.

## What micropayments taught us {#lessons}

This has been tried, and the lessons matter:

- **Blendle,** in the Netherlands, had more than a million registered users, but only about 150,000 had made a micropayment by 2017; it moved to subscriptions in 2019 and was sold in 2020.
- **Coil,** paying sites by the second through Web Monetization, shut down in March 2023.
- **Axate,** in the UK, runs a pay-as-you-go wallet across sites at around 20p to 30p an article, with a cap; it works, at a modest scale.
- **Google's Offerwall,** with Supertab, now lets a reader pay a little for a short pass; Google reports a 9% average revenue uplift for the publishers that tested it, and Supertab says over 10% of its pay-as-you-go readers subscribe within months.

What sank the early ones, as I read it, was friction: an account first, a decision at every click, and a wallet nobody else accepted. What is changing is that the friction can go, and that a new reader has arrived: AI agents, which already make one visit for every 31 human ones, according to TollBit, and send almost no clicks back.

## Our model: pay by the read {#model}

!shot mon-meter.webp | images/ | The meter: £5 of credit, a few pence a page, charged by the share read, in the reader's browser, nothing blocked. | process

This newsroom has run it since October ([the reading account, as built](/articles/the-reading-account-as-built.html)):

1. **Every new reader starts with £5 of credit,** and no account.
2. **Every page has a price of a few pence,** 10p for a new article and 5p for an older one, and the reader pays for the share of it they actually read, measured section by section in their own browser. A page they only scroll through costs a tenth of its price. A page that was not worth it can be marked so, and is not charged ([every link a gift link](/articles/every-link-a-gift-link.html)).
3. **Nothing is ever blocked:** credit can go below zero.
4. **Top-ups through Stripe,** £5 at a time.
5. **The reading account lives in the reader's own encrypted vault,** opened with a passkey; the server only ever sees ciphertext.

The important part for a publisher: it is all client side. The meter keeps its count in the reader's browser and sends nothing anywhere; there is no reader database to run and no personal data to hold. The reader's side is open source, Apache 2.0, at api.newsroom.sgit.ai, as a custom element, `<sg-meter>`, that a page adds in a few lines, so any publisher can use it for free. PrompTugal.news already runs the same meter.

## Four ways to earn from it {#ways}

- **The meter on your own site,** in place of, or beside, a paywall: free code, your prices, your revenue.
- **A revenue share through PrompTugal.news.** When PrompTugal.news carries a newsroom's story, natively, in its own pages, with the original source tracked and rated, the newsroom earns a share of what readers pay for it. Because every story carries its provenance, we can see what the original source of a piece of news is, and pay it ([who wrote it, who steered it, who signs it](/articles/who-steered-this.html)).
- **Licences to quote,** paid per use: another writer quotes your piece in their work and you share in what their readers pay, the way we proposed to Harvard Business Review.
- **Agents that pay at the source:** an AI agent reading your story pays per use, the way Cloudflare's pay per crawl and ProRata's 50% revenue share point to, but with the price and the evidence on your page ([free to copy, paid at the source](/articles/free-to-copy-paid-at-the-source.html)).

## A workflow for one newsroom {#workflow}

!shot mon-flow.webp | images/ | A newsroom's story, read on its own site and on PrompTugal.news, with the source tracked and a share paid back. | process

A regional newsroom publishes a story about a council decision. On its own site, the meter charges readers a few pence by the share they read. PrompTugal.news's town agent picks the story up, with its source, and carries it, linked, in the town's page, where its readers pay the same way. The provenance record says whose story it is; the share goes back. If WizPress produced the story, its provenance record travels with it from the draft, and the journalist signs it. The newsroom has not built anything, has not run a server, and has not asked anyone for a subscription.

## What we do not have yet {#proof}

I should be clear: this is not proven. Our own revenue is small, because our traffic is small; the meter works, the APIs work, the top-ups work, and what is missing is readers in numbers. That is why we need partners: newsrooms with traffic that want to experiment with this angle, and see who actually pays, and how much.

## Who we should talk to {#associations}

!shot mon-who.webp | images/ | Who to talk to: the associations representing publishers in the UK, Portugal and Europe. | table

Nuno's other point was the associations: they represent the newsrooms, and they have the connections. So we should map them and talk to them, in the UK and in Portugal first:

- **UK:** the News Media Association, for national, regional and local publishers; the Independent Community News Network, for independent and hyperlocal publishers; the Public Interest News Foundation, which maps local news; the Society of Editors.
- **Portugal:** the Associação Portuguesa de Imprensa, for the press; the regional press associations, among them the Associação de Imprensa de Inspiração Cristã and APMEDIO, for digital local media; and ERC, the regulator, to understand the rules.
- **Europe:** News Media Europe, the European Newspaper Publishers' Association, European Independent Media Publishers and WAN-IFRA.

What we would bring them: a model their members can try for free, the evidence of what happens when they do, and a way for local journalism to earn from the reach it already has.

## What this does not claim {#limits}

- **The model is not proven at scale;** our revenue today is small.
- **The revenue share through PrompTugal.news is a proposal,** not yet running.
- **Figures about others are as reported** in the sources below; some are vendors' own claims.
- **We have not spoken to the associations;** this is the map, not the meetings.

## Where this comes from {#sources}

My conversation with Nuno Costa of WizPress on 17 November 2026. On local news: [Press Gazette](https://pressgazette.co.uk/publishers/regional-newspapers/local-newspaper-closures-uk-2022-to-2024/) on UK closures; the [Public Interest News Foundation](https://www.publicinterestnews.org.uk/blog/local-news-launches-closures-and-the-state-of-play-in-2025/), December 2025; LabCom, [Desertos de Notícias Europa 2025: Portugal](https://labcom.ubi.pt/wp-content/uploads/2025/10/DNE_relatorio-2025.pdf). On paying for news: the Reuters Institute's Digital News Report for the [UK](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/united-kingdom) and [Portugal](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/portugal), and 2026 figures as reported by [ECO](https://eco.sapo.pt/2026/06/16/51-dos-portugueses-confia-nas-noticias/); [Press Gazette](https://pressgazette.co.uk/paywalls/online-news-subscriptions-stagnate-amid-jump-in-numbers-saying-they-would-never-pay/) on 2024; [Piano's benchmarks](https://piano.io/resources/benchmark-update-growing-revenue-with-declining-traffic). On micropayments: [Press Gazette](https://pressgazette.co.uk/paywalls/micropayments-for-news/) on Blendle and Axate; [Interledger](https://community.interledger.org/interledger/changes-to-the-web-monetization-ecosystem-discussion-post-1emc) on Coil; [Press Gazette](https://pressgazette.co.uk/paywalls/google-offerwall-monetisation-adverts-publishers/) on Google's Offerwall and Supertab. On AI: [TollBit](https://tollbit.com/analytics), [Nieman Lab](https://www.niemanlab.org/2025/07/cloudflare-will-block-ai-scraping-by-default-and-launches-new-pay-per-crawl-marketplace/) on Cloudflare, [Business Wire](https://www.businesswire.com/news/home/20250606852177/en/) on ProRata. The associations' own sites: [News Media Association](https://newsmediauk.org), [ICNN](https://www.communityjournalism.co.uk), [News Media Europe](https://www.newsmediaeurope.eu), [ENPA](https://www.enpa.eu), [EIMP](https://mediapublishers.eu), [ERC](https://www.erc.pt). All read on 17 November 2026. Earlier on this site: [the reading account, as built](/articles/the-reading-account-as-built.html), [every link a gift link](/articles/every-link-a-gift-link.html), [I just want to buy the article](/articles/i-just-want-to-buy-the-article.html), [free to copy, paid at the source](/articles/free-to-copy-paid-at-the-source.html), [the bridge, followed to the end](/articles/the-bridge-followed-to-the-end.html), [local trust, certified upwards](/articles/local-trust-certified-upwards.html), [working with WizPress](/articles/working-with-wizpress.html), [who wrote it, who steered it, who signs it](/articles/who-steered-this.html).
