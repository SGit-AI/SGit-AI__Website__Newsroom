---
title: Decide, then buy: deciding what to buy and buying it are two different businesses, one for explorers and villagers and one for town planners, and an open path with a better deal beats locking the customer in
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: When someone buys something, there are two distinct moments. The first is the decision: gathering information, checking it against what they care about, and arriving at "I want to buy X, on platform Y, quantity Z". The second is the purchase. I think these are two separate businesses, and mapping them shows why. Helping someone decide is explorer and villager work: custom interfaces, lots of new data seen in new ways, made personal to the user's culture, goals and values, and it gets unique very fast. Buying is town planner work: a commodity, standard, done at volume, where trust and execution matter more than imagination. Amazon joins the two; OpenRouter is the commodity half alone. My strategy, here and in open source, is to keep them apart and not lock the user in: give them the open path, every step mapped, from twenty-five steps down to one, and offer a service that does it for them. What that service sells is time, trust, execution, expertise with the platform, and the better prices that volume brings.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: strategy, wardley-maps, open-source, decisions, commodity, town-planners, business-models, article
status: published
---

!shot dtb-map.webp | images/ | A Wardley map of a purchase: the decision on the custom side, the purchase on the commodity side, the record between. | wardley-map

## In short {#in-short}

- **Two moments:** deciding what to buy, and buying it.
- **Two businesses:** one helps the person decide, and is agnostic about where they buy; the other carries out the purchase.
- **Different kinds of work:** deciding is explorer and villager work, personal and unique; buying is town planner work, a commodity.
- **The hand-over is a decision record:** "I want to buy X, on platform Y, quantity Z".
- **No lock-in:** give the open path, mapped step by step, and a service that does it for you.
- **The service sells** time, trust, execution, expertise with the platform, and volume prices.

## Two moments {#moments}

!shot dtb-moments.webp | images/ | The two moments: deciding, which ends in a decision record, and buying, done by the person or by a service. | concept

Think of anyone about to buy something: a share, gold, a token, a phone, a model for their agents. There are two moments, and they are very different.

The first is the decision. It is about working out what you want: gathering information, collecting evidence, checking it against your own criteria, weighing it, and arriving at a sentence like "I want to buy X, on platform Y, quantity Z". That is everything I described in [a market for sweets](/articles/a-market-for-sweets.html), and it has nothing to do with the purchase itself.

The second is the purchase: creating an account, moving the money, placing the order, getting the thing.

## Two businesses {#businesses}

I think those are two separate businesses, and the reason is clearest on a Wardley map.

**Helping someone decide sits on the left of the map.** It is about custom interfaces, consuming lots of data and a lot of new data, seeing it in different ways, and making it personal: to the user's culture, their goal, their vision, their values, their criteria. It gets very unique, very fast. That is explorer and villager work, and for me it is the power of everything we have been building: agents, [lanes and graphs](/articles/the-new-data-lake.html), vaults, and [a brain made for one company](/articles/a-brain-you-arrive-at.html).

**Carrying out the purchase sits on the right.** It is a commodity and a standard business: buy X for Z on Y. It is town planner work, where what matters is that it works every time, at volume, safely ([town planners for mission-critical code](/articles/town-planners-for-mission-critical-code.html)).

The decision business should be agnostic about the purchase. Its whole point is to bring the person to the moment where they know what they want, wherever they then buy it.

## Amazon joins them; a router does one {#examples}

You can argue that Amazon does both: it helps you find the thing and then fulfils it. But look at where its strength is. When you already know what you want, Amazon is the commodity: it just gets it to you.

OpenRouter is the commodity half on its own. You know which model you want, and it routes the request. Some of the router services I am talking to now say they can offer better prices because they buy at volume, and that is exactly the town planner's advantage.

## The open path, and a better deal {#open}

This is also my open source strategy, and the reason I think open source and open information are so powerful here. You do not lock the user in. You give them a really good path to your commodity service, and an honest alternative to it.

So after the decision, you say: you can do it yourself, and here is how. Here are the twenty-five steps, for someone doing it the first time. Here are the five steps, for someone who has done it before. Here is the one step: go there, create an account, buy this. Or we can do it for you.

What you sell is not just time. You sell time, trust, execution, and expertise: you will be the expert in dealing with that exchange, that platform, that supplier. And you should be able to get better prices, because you buy at volume. Because the open path is always there, your service has to be the better deal, not the only way, and that keeps it honest. It is the same logic as [the shop that sells time](/articles/the-shop-that-sells-time.html), and as the choice between open core and a hub in [where to invest in sgit](/articles/where-to-invest-in-sgit.html).

## Keep them apart {#apart}

The key point is to separate the decision of what to buy from the operation of buying it.

- **The decision business stays trusted** because it does not depend on where you buy: it has no reason to steer you.
- **The purchase business stays simple** because it does one standard thing well, and it can serve every decision business.
- **The person stays free:** they can take the decision anywhere, do it themselves, or pay for the service.

It also keeps the risky part small. Once you carry out the purchase you hold money and keys, and the serious obligations that come with them. Kept apart, the explorer side can move fast and the town planner side can move carefully, which is what each needs.

## What this does not claim {#limits}

- **This is a strategy argument,** not a description of any one company's business.
- **The routers' volume prices are what they told me,** not prices I have checked.
- **Where a decision service ends and regulated advice begins** depends on the market and the country.

## Where this comes from {#sources}

My own thinking, 15 November 2026, after the conversation behind [a market for sweets](/articles/a-market-for-sweets.html). Wardley maps are Simon Wardley's; [pioneers, settlers and town planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html) are his too (2015), and this site calls the first two explorers and villagers. Earlier on this site: [villager services for explorer coders](/articles/villager-services-for-explorer-coders.html), [explorer coding](/articles/explorer-coding.html), [ephemeral town planner services](/articles/ephemeral-town-planner-services.html), [when the customer becomes the commodity](/articles/when-the-customer-becomes-the-commodity.html), [the shop that sells time](/articles/the-shop-that-sells-time.html), [where to invest in sgit](/articles/where-to-invest-in-sgit.html).
