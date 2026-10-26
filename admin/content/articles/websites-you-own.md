---
title: Websites you own: a reply to an infographic that sells AI-built websites by the month, section by section, why rent is the wrong model, and the one-off model I propose, where the client owns Claude, GitHub and the domain, and changes their own site by talking to it
date: 2026-10-26
author: Dinis Cruz
author_url: about/index.html
summary: Someone I am helping, who is doing a lot of agentic work now, sent me an infographic for a business selling websites built with Claude: three monthly plans from £39 to £119 with a setup fee, a cap of five or ten pages, half an hour to two hours of edits a month, the seller's Claude subscription as the main cost, and ten clients making about £570 a month. It is a good sign that people see the opportunity. But the temptation is always rent, money while you sleep, and the economics are wrong. On a monthly plan you earn most when your clients use you least, the clients who use you most cost you most, and a few of them will never stop asking. The page caps make no sense either: a static page costs almost nothing, and this newsroom runs about 1,500 of them on GitHub Pages. The model I propose is different. The client owns three accounts, Claude or ChatGPT, GitHub with Pages, and a domain. You charge once, to set them up and wire them together, build the site from the client's own material with designs to choose from, check it, and hand it over with a lesson in changing it by talking to their AI. After that, help is a block of hours, if they want it. Every engagement ends, the client is in control, and delighted clients tell others. Here is the infographic, section by section, and the alternative.
version: v0.13.92
license: https://creativecommons.org/licenses/by/4.0/
tags: business-models, websites, agents, pricing, explorers-villagers, article
status: published
---

!shot kw-info-all.webp | images/ | The infographic as I received it, on 26 October 2026: a pay-monthly website business built with Claude, in five sections: price plans, cost to run, time per five-page build, the numbers, and risks and fixes. Shared without its author's name; nothing in it identifies them. | small | aside

## In short {#in-short}

- **I was sent a plan to sell websites built with Claude, by the month.** A good instinct, the wrong model.
- **Rent pays you when clients do not use you.** The more they use it, the less you earn.
- **A few clients will drive you mad.** For them a monthly fee is permission to keep asking.
- **Page caps make no sense.** A static page costs almost nothing.
- **The client should own the stack:** Claude or ChatGPT, GitHub with Pages, a domain.
- **Charge once, for a finished job.** Setup, build, designs to choose from, QA, handover.
- **After that, blocks of hours, only if wanted.** Every engagement ends.

## What I was sent {#infographic}

Someone I am helping, who is now doing a lot of agentic work, sent me this infographic. I had asked them to look at what I have been writing on this newsroom first. Their agent did, and the plan still came back as a rent business. So either the articles were not found or the argument did not land. This article makes it in one place.

First, a check: the image carries nothing about its author. Its embedded data holds only its resolution and orientation, and the page names no one; the one first-person line, "Code I cannot fix", identifies nobody. I am sharing it without saying who made it.

It is a good piece of work, and a good sign. People are seeing the opportunity to build websites with an agent and sell them. My problem is with the model underneath it, so here it is, section by section.

## 1. The price plans {#plans}

!shot kw-info-plans.webp | images/ | Section 1, price plans: Starter £39 a month and £149 setup, up to five pages, hosting, DNS and SSL, 30 minutes of edits a month; Standard £69 a month and £299 setup, up to ten pages, contact form, analytics, uptime checks, an hour of edits; Plus £119 a month and £499 setup, blog or booking, two hours of edits, a quarterly report; extra work £35 an hour; the client owns the domain and content. | screenshot

Three monthly plans, each with a setup fee, a page cap and a monthly allowance of edits. Two things are wrong here.

**The page caps are spectacularly low.** Five pages, ten pages. With this stack a page costs almost nothing: the agent writes it, and a static host serves it. This newsroom has about 1,500 pages on GitHub Pages, whose [limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) are a published site of up to 1 GB and a soft bandwidth limit of 100 GB a month. The real limit is how many tokens the client wants to spend: with a decent Claude account, hundreds or thousands of pages are practical. A cap of five pages is a pricing device, not a cost.

**The edit allowance keeps the client dependent.** Thirty minutes a month means the client cannot change their own site. That is the opposite of what this stack makes possible: the client can change anything, any time, by asking.

What I agree with: "Client owns the domain and content." Yes, and they should own the rest too.

## 2. The cost to run {#cost}

!shot kw-info-cost.webp | images/ | Section 2, cost to run: fixed £95 to £190 a month, Claude Max at $100 or $200 (about £75 to £150), insurance, email and accounts £20 to £40; each extra site £1 to £5 a month, Route 53 $0.50 per site, Amplify hosting free to a few pounds, a domain about $12 a year, passed to the client. | screenshot

The biggest cost in the plan is the seller's own Claude subscription, used to run every client's site. That puts the cost, and the bottleneck, in the wrong place. The client can have their own Claude or ChatGPT account, which they are probably already paying for, and use it for everything else too. Reselling access to someone else's AI service may also have legal ramifications, so I would not build a business on it; I would read the provider's terms first.

The hosting is right in spirit: static, cheap, nearly free. On GitHub Pages it is free, with one caveat worth knowing. GitHub's [terms for Pages](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features) say it is "not intended for or allowed to be used as a free web hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS)". A brochure, a catalogue or a guide library fits; a site that takes orders and payments should go to another static host.

## 3. The time per build {#time}

!shot kw-info-time.webp | images/ | Section 3, time per five-page build: 10 to 15 hours in total, 3 to 5 hours of coding, fast with Claude Code, and 7 to 10 hours of everything else, calls, content, revisions, testing and launch. "Price on the client's time, not Claude's speed." | screenshot

This is the best section, and I agree with it. Most of the time is not the code: it is the calls, the content, the revisions and the launch. And "price on the client's time, not Claude's speed" is right. Which is exactly why the work should be priced as a job: a finite number of hours, delivered and finished.

## 4. The numbers {#numbers}

!shot kw-info-numbers.webp | images/ | Section 4, the numbers: £1,127 from one Standard client in year one (£299 plus 12 times £69); two Standard clients needed to cover fixed costs; £690 a month from ten Standard clients, about £570 after costs, for about ten hours' work. | screenshot

The arithmetic mostly holds, at the optimistic end. £299 plus twelve months at £69 is £1,127. Two Standard clients bring £138 a month, which covers the fixed costs only at their low end of £95; at £190 it takes three. And ten clients bring £690 a month, which leaves about £570 only if the costs are at their lowest; at the top end it is closer to £450.

But the real problem is not the arithmetic, it is the incentive.

!shot kw-incentive.webp | images/ | Who wins when the client uses it more? On a monthly plan the fee is fixed and the cost of serving the client rises with every request, so the margin shrinks as use grows. On a handover the job is priced once, and afterwards the client's own use costs the studio nothing. Illustrative. | chart

On a monthly plan you make money when your clients do not use you. The more they use what you sell, the less profitable they are. And in my experience something like 10 or 15 per cent of clients will drive you absolutely mad: endless requests, a lot of noise, never content, because to them a monthly fee is permission to keep asking. That is fair from their side; they are getting what they can for the money. But it is a perverse position to build a business in. I have written about the other side of it: "A subscription is a discount for committing to regular use. It is not rent on something you have the right to ignore", in [stop the bleeding, then ask for it back](https://newsroom.sgit.ai/articles/stop-the-bleeding-then-ask-for-it-back.html), and why paying after the value feels different, in [paying after the value](https://newsroom.sgit.ai/articles/paying-after-the-value.html).

## 5. The risks {#risks}

!shot kw-info-risks.webp | images/ | Section 5, risks and fixes: code I cannot fix, keep sites simple and static, read what Claude writes; Claude usage caps, never promise same-hour fixes in the contract. | screenshot

"Keep sites simple and static. Read what Claude writes." Agreed. The second risk, Claude's usage caps, only exists because the seller holds one AI account for every client. When each client has their own, a cap is theirs, and nobody has promised anyone a same-hour fix.

## The model I propose {#model}

!shot kw-models.webp | images/ | Two ways to sell a website made with an agent: rent, a monthly plan where the seller holds the AI account, the hosting and the edits, with caps on pages and edits; and handover, a finished job where the client owns Claude or ChatGPT, GitHub with Pages and the domain, the studio charges once for setup, build, designs, QA and handover, and help afterwards is a block of hours. | comparison

The tech stack for someone to maintain a website today is an AI account, GitHub Pages and a DNS account, the recipe in [your own newsroom](https://newsroom.sgit.ai/articles/your-own-newsroom.html). So package that, and sell the work, not the rent.

- **Setup, one-off.** The client creates a Claude account (or ChatGPT, or a team plan), a GitHub account and, if they need one, a domain. You guide them, plug them together, and give them the prompts and modes that make it work. If they have no idea how to register a domain, sell them a domain and its DNS for a year, as a one-off.
- **The build, one-off.** A couple of sessions and briefs to extract their ideas. They give you fifty documents, pages or notes; the agent builds the site; you show them five designs and they pick one; you run a couple of rounds of QA.
- **The handover.** You teach them to change their site by talking to their AI. Clients who were happy to change a paragraph can now change anything, and they will never have experienced anything like it.
- **After that, blocks of time.** If they want help, they buy a block of hours. Nothing monthly.
- **Prices from the market.** £500 for a site, £1,000 for a bigger one, or a family-and-friends discount on what is £500 worth of effort. For a site you can edit and maintain, that looks good, with five designs to choose from and a content management system that is a conversation, it is a very good deal. The only question is the market economics: how much time you have, and how many clients you can onboard.
- **Lift and shift.** Most business websites are static by design, glued together by someone who has since left. "Do you have a website? Can you edit it? Do you want to talk to it?" A conversion is £200, £500 or £1,000, depending on its back end.

Every engagement is finite, which is what [jobs that never scaled](https://newsroom.sgit.ai/articles/jobs-that-never-scaled.html) describes: a piece of expert work, delivered end to end, and finished. The client is empowered and in control, and delighted clients tell others. For someone who is not very technical, I think finite work is especially important. You could call these explorer services, in the language of [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html): someone without an engineering background, selling what they can now build, on top of powerful open-source technology like ours, with villager and town planner services for what needs more.

## What it looks like {#mockup}

To make this concrete, I asked the agents to build a mock-up: Kitewing Websites, a made-up studio selling exactly this offer, and three made-up client sites in three industries, a potter's catalogue, a community garden and a local plumber with a guides library. Each is a vault app, a site in an encrypted folder. The tour is in [inside Kitewing Websites](https://newsroom.sgit.ai/articles/inside-kitewing-websites.html).

## What this does not claim {#limits}

- **The infographic is shared without its author,** and its figures are theirs; I checked the arithmetic, not the costs.
- **The 10 to 15 per cent is my experience,** not a measurement.
- **The prices in my model are hypotheses,** to be set by the market.
- **Reselling AI access may be fine under some terms;** I have not checked any provider's, which is why I would not depend on it.

## Where this comes from {#sources}

The infographic sent to me on 26 October 2026, and my voice memo of the same day. GitHub Docs, [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), and GitHub's [terms for additional products and features](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features), on Pages, read on 26 October 2026. Related: [inside Kitewing Websites](https://newsroom.sgit.ai/articles/inside-kitewing-websites.html), [your own newsroom](https://newsroom.sgit.ai/articles/your-own-newsroom.html), [stop the bleeding, then ask for it back](https://newsroom.sgit.ai/articles/stop-the-bleeding-then-ask-for-it-back.html), [paying after the value](https://newsroom.sgit.ai/articles/paying-after-the-value.html), [jobs that never scaled](https://newsroom.sgit.ai/articles/jobs-that-never-scaled.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [the no-server startup](https://newsroom.sgit.ai/articles/the-no-server-startup.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
