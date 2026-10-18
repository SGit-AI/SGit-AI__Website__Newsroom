---
title: Ephemeral town planner services: a better name than serverless, now that serverless includes things that bill you by the hour
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: I have never liked the word serverless, and it has been stretched until it barely means anything. To me it always meant four things: it scales to zero, it costs nothing when you are not using it, it starts fast, and it turns a capability into a commodity. Lambda and Cloud Run are that. But today the word is also on products that bill you every hour whether you use them or not: MSK Serverless at $0.75 a cluster-hour, OpenSearch Serverless's classic collections with a floor of two capacity units, ElastiCache Serverless with a minimum of storage metered every hour. The definitions were clear: the CNCF's whitepaper says "there is no charge when code is not running", and the Berkeley paper warned in 2019 that few so-called elastic services could scale to zero. So I propose a better name, built from three words that each carry part of it: ephemeral, because it comes and goes with use; town planner, Simon Wardley's word for something industrialised and mature; and services, because it is exposed for others to use. Ephemeral town planner services. Lambda is one, sitting on town planner services like S3. And naming things this way shows how much glue sits behind what is sold as a commodity: Lambda itself ran on containers inside EC2 instances for four years, until Firecracker replaced them. The test I would use is simple: if it bills you by the hour when nobody is using it, it is not serverless, and whoever runs it has something running on their side.
version: v0.12.111
license: https://creativecommons.org/licenses/by/4.0/
tags: serverless, cloud, wardley-maps, town-planners, pricing, aws, article
status: published
---

!shot es-scale.webp | images/ | What "serverless" costs when nobody is using it, for products sold under the name, as their own pricing pages read on 18 October 2026, excluding storage. Some scale to zero: Lambda's event functions, Cloud Run, Cosmos DB serverless, Neon, Redshift Serverless, Aurora Serverless v2 since November 2024 and OpenSearch's next-generation collections since May 2026. Some do not: MSK Serverless bills $0.75 a cluster-hour, OpenSearch's classic collections a floor of two capacity units, ElastiCache Serverless a minimum of storage, Neptune Serverless a minimum of one capacity unit. The line between the two groups is the test this article proposes. | comparison

## In short {#in-short}

- **Serverless meant four things.** Scales to zero, costs nothing idle, starts fast, turns a capability into a commodity.
- **The definitions said so.** "There is no charge when code is not running", in the CNCF's own words.
- **The word now covers hourly bills.** MSK Serverless charges by the cluster-hour; others have floors.
- **The test.** If it bills you by the hour when nobody is using it, it is not serverless.
- **A better name: ephemeral town planner services.** Each word carries a part the others do not.
- **Lambda is one, on top of town planner services.** S3 underneath, always there.
- **The name shows the glue.** Lambda ran on containers in EC2 for four years before Firecracker.

## What serverless meant {#meant}

When Lambda launched in November 2014, Jeff Barr's post said: "You pay for compute time in units of 100 milliseconds and you pay for each request." That was the point. No request, no cost. The code was there when needed and gone when not.

The definitions that followed said the same. The CNCF's serverless whitepaper describes applications "executed, scaled, and billed in response to the exact demand needed at the moment", scaling down "so that there is never idle capacity", under a heading that reads *No compute cost when idle*: "there is no charge when code is not running." Berkeley's [view on serverless computing](https://arxiv.org/abs/1902.03383), in February 2019, put it as two conditions: a serverless service must "scale automatically with no need for explicit provisioning, and be billed based on usage", paying "in proportion to resources used instead of for resources allocated." It praised Lambda for "scaling all the way down to zero resources, and zero cost, in the absence of demand."

To me, a serverless service always had four properties. It scales to zero. It costs little or nothing when it is not there. It starts fast. And it turns a capability into a commodity: something you use without thinking about how it is built. Lambda and Google's Cloud Run behave like that. There is a scale where they stop being efficient, when they run all the time, but they behave like commodities.

## What it means now {#now}

The word has been stretched. Today it is on products that bill every hour whether anyone uses them or not. From their own pricing pages on 18 October 2026, excluding storage:

| Product | Idle | How it bills |
|---|---|---|
| Lambda event functions | Zero | Per request and per millisecond |
| Cloud Run | Zero | Per 100 ms; idle instances not charged |
| Cosmos DB serverless | Zero | Per request unit, no minimum |
| Neon | Zero | Compute suspends when idle |
| Redshift Serverless | Zero | Per second while running |
| Aurora Serverless v2 | Zero since Nov 2024 | Pauses after a set idle time |
| OpenSearch, next generation | Zero since May 2026 | Scales to zero after 10 idle minutes |
| OpenSearch, classic | About $350 a month | A floor of 2 capacity units |
| MSK Serverless | About $550 a month | $0.75 per cluster-hour |
| Neptune Serverless | About $80 a month | A floor of 1 capacity unit |
| ElastiCache Serverless | From $6 a month | A minimum of storage, metered hourly |

The monthly figures are my arithmetic at 730 hours, at US East rates where the pages give them; they move with region and configuration.

Some of these have moved towards zero over time, which is to their credit. Aurora Serverless v2 had a floor of half a capacity unit, which Corey Quinn [priced in 2022](https://www.lastweekinaws.com/blog/the-aurora-serverless-road-not-taken/) at "just shy of $45" a month, until AWS added [scaling to zero](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-aurora-serverless-v2-scaling-zero-capacity/) in November 2024. OpenSearch Serverless started with a minimum of four units, halved it [in June 2024](https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-opensearch-serverless-entry-cost-half-collection-types/), and reached zero with its next generation in May 2026. Others have not. [MSK Serverless](https://aws.amazon.com/msk/pricing/) says it plainly: you "pay an hourly rate for your serverless clusters."

None of this is new. Jeremy Daly [wrote in 2018](https://www.jeremydaly.com/stop-calling-everything-serverless/) that the promise "used to be 'never pay for idle'", and that many "serverless" offerings "require you to pay for the service whether you're using it or not". The Berkeley paper warned in 2019 that "few so called 'elastic' services" could scale to zero. The word kept spreading anyway.

## The test {#test}

So here is the test I would use. **If it bills you by the hour when nobody is using it, it is not serverless.** Storage is different: data has to live somewhere. But compute that charges by the hour, the day or the month while idle means there is a server on the other side, running for you, whether you call it or not.

And that tells you something about the provider, not just the price. A per-hour bill for a "serverless" product usually means they cannot yet spin the thing up and down fast enough, and safely enough, to bill by use. That is an engineering gap on their side, passed to you as a cost. It is fine to sell that; it should not be sold under a name that promised the opposite.

## A better name {#name}

I would rather replace the word than keep defending it. I tried a few.

*Commodity services* is close: the point is that the capability is a commodity. But a commodity does not have to be on demand. A commodity can sit there running all month.

*Town planner services* is closer. In Simon Wardley's terms, which this site uses as explorers, villagers and town planners, [town planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html) "take something and industrialise it taking advantage of economies of scale." A town planner service is mature, stable, built as a commodity. But a town planner component can also be always on.

*Ephemeral services* has the other half: services that turn up when used and disappear afterwards, provisioned on demand. But on its own it says nothing about maturity; you could have an ephemeral service that is a custom-built, glued-together prototype.

Put together, the three words say what serverless was supposed to say, and each covers a part the others miss:

- **Ephemeral**: it comes and goes with use, and costs nothing when it is gone.
- **Town planner**: it is mature, industrialised, a commodity; not a prototype held together behind the scenes.
- **Services**: it is exposed for others to use, through an interface, usually the web.

*Ephemeral town planner services.* Lambda is a good example: an ephemeral town planner service that sits on top of town planner services, like S3, which are always there. Wardley said something close in 2016, in [why the fuss about serverless?](https://blog.gardeviance.org/2016/11/why-fuss-about-serverless.html): "It's not really 'serverless' but more 'I don't care what a server is'", and "The platform has evolved towards more of a utility service."

## The glue behind the commodity {#glue}

Naming things this way has a useful side effect: it makes you ask whether something is really a town planner service, or only looks like one. Plenty of things are treated as commodities while, behind the scenes, they are a large amount of custom technology glued together. That is what a Wardley map is good at showing.

The hyperscalers do this on purpose. Werner Vogels wrote in [ten lessons from ten years of AWS](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html) that AWS delivers "new services often with a minimal feature set" and lets customers "help drive the roadmap." Lambda is a well-documented case, in its builders' own words, from the [Firecracker paper](https://www.usenix.org/system/files/nsdi20-paper-agache.pdf) in 2020: "When we first built AWS Lambda, we chose to use Linux containers to isolate functions, and virtualization to isolate between customer accounts", with several functions for one customer in the same virtual machine. "We were unsatisfied with this approach", and from 2018 they migrated customers to Firecracker. For its first four years, the service people treated as the definition of serverless was containers inside rented machines, glued together, while it was matured with its customers.

That is not a criticism; it is how services become commodities. But it is a reason to be careful with names. A first version is often a villager's work dressed as a town planner's, and the product pages over the following years, the floors that halve, the scale-to-zero that arrives, the services that are withdrawn, are the record of it maturing in public.

## Why it matters {#matters}

For anyone buying, the name sets the expectation of what an idle month costs, and the gap between the name and the bill is real money.

For anyone building on this site's terms, it is the property we design for. [Cloudflare as Lego blocks](/articles/cloudflare-as-lego-blocks.html) put an sgit vault server in 83 lines on a platform that bills by request; [an agent desktop by the minute](/articles/an-agent-desktop-by-the-minute.html) asked for desktops billed for the minutes they work. Both are asking for ephemeral town planner services. And [the code you do not ship](/articles/the-code-you-do-not-ship.html) argued that the same discipline applies inside the code: nothing running that nobody needs.

## What this does not claim {#limits}

- **The name is a proposal.** I do not expect it to replace serverless; I want a word that says what I mean.
- **The prices are from pricing pages on 18 October 2026**, excluding storage; the monthly figures are my arithmetic at 730 hours and US East rates.
- **Some products in the table do scale to zero.** The test is about compute billed while idle, not about the brand.
- **Billing by the hour is not wrong.** It is a reasonable product; it is just not what the word promised.
- **The Firecracker account is AWS's own.** It describes Lambda's internals as its builders tell it.

If you sell something called serverless that bills by the hour, I would like to understand why: write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. The research, read that day by a research agent: AWS, [serverless](https://aws.amazon.com/serverless/), the [Lambda launch post](https://aws.amazon.com/blogs/aws/run-code-cloud/), 13 November 2014, and the pricing pages for [Lambda](https://aws.amazon.com/lambda/pricing/), [MSK](https://aws.amazon.com/msk/pricing/), [OpenSearch](https://aws.amazon.com/opensearch-service/pricing/), [ElastiCache](https://aws.amazon.com/elasticache/pricing/) and [Redshift](https://aws.amazon.com/redshift/pricing/); [Aurora's scale to zero](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-aurora-serverless-v2-scaling-zero-capacity/) and [OpenSearch's lower floor](https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-opensearch-serverless-entry-cost-half-collection-types/); [Neptune's capacity](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-capacity-scaling.html); Google, [Cloud Run pricing](https://cloud.google.com/run/pricing); Microsoft, [Cosmos DB serverless](https://learn.microsoft.com/en-us/azure/cosmos-db/serverless); [Neon pricing](https://neon.com/pricing); the CNCF [serverless whitepaper](https://github.com/cncf/wg-serverless/tree/master/whitepapers/serverless-overview); Jonas and others, [a Berkeley view on serverless computing](https://arxiv.org/abs/1902.03383), 2019; Simon Wardley, [on pioneers, settlers and town planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html), 2015, and [why the fuss about serverless?](https://blog.gardeviance.org/2016/11/why-fuss-about-serverless.html), 23 November 2016; Corey Quinn, [the Aurora Serverless road not taken](https://www.lastweekinaws.com/blog/the-aurora-serverless-road-not-taken/), 1 June 2022; Jeremy Daly, [stop calling everything serverless](https://www.jeremydaly.com/stop-calling-everything-serverless/), 21 December 2018; Werner Vogels, [ten lessons](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html), 11 March 2016; Agache and others, [Firecracker](https://www.usenix.org/system/files/nsdi20-paper-agache.pdf), NSDI 2020. Related: [cloudflare as Lego blocks](/articles/cloudflare-as-lego-blocks.html), [an agent desktop by the minute](/articles/an-agent-desktop-by-the-minute.html), [the code you do not ship](/articles/the-code-you-do-not-ship.html), [explorer coding](/articles/explorer-coding.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
