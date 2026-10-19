---
title: You are a developer, you just do not call it that: what every GenAI founder I know does all day, the sausage factory they never saw, and why the book may be called Generation ZX Founders
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: Every GenAI founder I know is a developer, and none of them think so. When I tell them, they look at me as if I were joking: they just tell the model to do things. But look at what they do all day. They write requirements, they own the product, they design, they engineer, they deploy continuously, they run a development team. Some of it is crude, but much of the industry does it worse: underfunded teams, ridiculous deadlines, ship it anyway, which is where so many vulnerabilities come from, because a vulnerability is a sign of an engineering gap. The founders do not know that because they never saw the sausage factory. They grew up on polished, second- and third-generation products. They did not see the iPhone launched on a golden path of taps that kept the prototype from crashing, or developers giving a mock-up a hand-drawn theme so the business would not think it was finished. Now, building things themselves, they complain about versioning, stability and security, the non-functional requirements nobody used to fund. They are developers. Which brings me to the book: it is very hard to tell someone what they are in a word they do not relate to, so my hypothesis is that it should be called Generation ZX Founders, with "you are a developer" kept for the end, as the reveal.
version: v0.12.130
license: https://creativecommons.org/licenses/by/4.0/
tags: founders, developers, explorer-coding, books, gen-z-book, article
status: published
---

!shot yd-roles.webp | images/ | One GenAI founder, many roles. In the middle, the founder who says "I am not a developer, I just tell the model what to do". Around them, what they actually do every day: senior stakeholder and business owner (decides what matters and pays for it), product owner (writes the requirements), designer, developer and engineer (builds, with agents), release manager (continuous deployment), and the head of a development team (the agents). Each of those is a job title in a technology company. | concept

## In short {#in-short}

- **Every GenAI founder I know is a developer.** None of them think so.
- **Look at what they do.** Product owner, designer, engineer, continuous deployment: a whole team's roles.
- **Crude, compared to what?** Much of the industry does it worse, and gets away with it.
- **They never saw the sausage factory.** Only the polished products, generations later.
- **Now they meet the non-functional requirements.** Versioning, stability, security.
- **Programming is not just writing code.** It never was.
- **So call the book what they are.** Generation ZX Founders, with "you are a developer" at the end.

## The look they give me {#look}

Every GenAI founder I know is a developer. The challenge is that they do not consider themselves one. I have tried to make the case to friends who are building companies, that they are developers, and senior product managers, and the people running the infrastructure, the senior stakeholder, the product owner, the designer. And they all look at me as if I must be joking. No way. I do not know what I am doing. I just tell the model to do some stuff.

But look at what they do. They literally work like a developer. They work like a product manager and like a business owner. They do engineering. They do continuous deployment. They write the brief, which is the requirement; they check what came back, which is testing; they push it live, which is a release; and they direct a team of agents, which is running a development team. They might not think they are doing any of it, but they are.

In the terms of Simon Wardley's explorers, villagers and town planners, most of them are developers in the explorer phase, which is what [explorer coding](/articles/explorer-coding.html) names. Some work at other phases too: building on components that are already commodities, they are doing the town planner's job of assembling them.

## Crude, compared to what? {#crude}

Yes, some of what they build is a bit crude. But let us be clear about the comparison. A lot of companies, especially older ones and ones outside the technology sector, do this much worse. They barely invest in technology. They hire the lowest common denominator, or outsource whole parts of it. When they do set up development teams, the teams are not properly funded, and they get ridiculous deadlines, ridiculous requirements, and the instruction to just ship it.

That is why there are so many ridiculous vulnerabilities, even in the internal products of big technology companies. A vulnerability is a sign of bad engineering, or at least of an engineering gap. Lack of validation, of authentication, of authorisation, of input handling, of resilience: those are all engineering properties, most of them non-functional requirements. Internal products got away with it because they never had the healthy beating a product gets in the market, the moment when somebody says we need to build this with better engineering. That is where I think [the SaaS apocalypse](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) will be felt first: in the internal tools that were never good enough, now that the people who use them can build their own.

## They never saw the sausage factory {#sausage}

The problem is that most new GenAI founders never worked in a technology company. They never saw the sausage factory, how messy it is, how tight it is. They have been the consumers of very polished products, usually the second, third or fourth generation of them, or the commodity version, by which time they are very good.

They did not see how those products looked when they were new. When Steve Jobs launched the iPhone in January 2007, the prototype could not reliably play a whole song or video without crashing. The engineers had worked out what they called "the golden path", "a specific set of tasks, performed in a specific way and order, that made the phone look as if it worked". The phone's display was "preprogrammed to always show five bars of signal strength", and Jobs had several phones on stage to swap when one ran low on memory ([Fred Vogelstein, New York Times Magazine, October 2013](https://www.nytimes.com/2013/10/06/magazine/and-then-steve-said-let-there-be-an-iphone.html)). In my memory this was a Bill Gates story; it is not. Gates's own famous demo went the other way: at COMDEX in April 1998, Windows 98 crashed to a blue screen on stage beside him, and he said "That must be why we're not shipping Windows 98 yet" ([the Associated Press report at the time](https://lists.tlug.jp/ML/9804/msg00419.html)).

Even Apple's interfaces began as mock-ups. Bas Ording, the designer behind Mac OS X's Dock, built his prototypes in Macromedia Director, and an engineer's job was to "take his prototypes built in Macromind Director and turn them into working code" ([James Thomson, who built the Dock](https://tla.systems/blog/2025/01/04/i-live-my-life-a-quarter-century-at-a-time/)). Those were internal prototypes, not demos shown as real software; but they looked real, and they were pictures and animation.

This is what "the demo gods" means. The demo gods are not real. A demo that fails on stage is usually explorer technology, hanging by a thread, collapsing at the first unexpected step. It is also why so many products are announced and then take months or years to ship, or never do: in the hands of real users the whole thing breaks, or the production pipeline is not good enough. Fake it until you make it is common in technology, and a lot of the time they do not make it.

## The pilot who is relieved to land {#relieved}

I remember noticing an interesting dynamic when I demoed to a user or a customer, and I think it is very common. The people doing the demo are always happy, and relieved, when it works. And the customer looks a bit shocked: hold on, was it not supposed to go well?

It is like a plane landing and the pilot and crew being ridiculously happy that it landed safely. Or a car that drove you there without falling apart, and the driver celebrating. You start to wonder: is this thing safe? How is it actually built?

## Make it look unfinished {#unfinished}

There is a funny example of the other side. In the early days of the new generation of web applications, engineers would build a mock-up that looked quite good, especially compared with the applications before it. The business would look at it and say: great, let us ship it. And the developers would say: there is no back end, nothing works. Fine, ship it in two weeks instead of one. No, there is no back end.

So some teams started making their mock-ups look rough on purpose, with themes that look hand-drawn and slightly misaligned, so that the business would see something still being worked on. Bootstrap has one, [Sketchy](https://bootswatch.com/sketchy/), "a hand-drawn look suitable for mockups". The idea is older. In 2002 Joel Spolsky wrote, in [The Iceberg Secret, Revealed](https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/): "If you show a nonprogrammer a screen which has a user interface which is 100% beautiful, they will think the program is almost done." His advice was to build the interface "in such a way that unfinished parts *look* unfinished", and around 2004 [Napkin Look & Feel](https://napkinlaf.sourceforge.net/) did exactly that for Java applications.

!shot yd-iceberg.webp | images/ | The iceberg they never saw. Above the waterline, what a user of polished products sees: the interface and the demo, about 10% of the work in Joel Spolsky's 2002 estimate. Below it, what was there when those products were new: the back end and the data; versioning; validation, authentication and authorisation; resilience; the release pipeline and real users. On the left, what founders saw, such as the iPhone launched on a golden path of taps; on the right, what they meet now that they build: versioning, stability and security. | concept

It is a bit of a joke, but it was common. The business made decisions without the visibility, and it was not their fault: how could they know? They had never been inside.

## Now they understand {#understand}

It is only now, with explorer coding, that they do. I find it fascinating to hear business owners, product managers and people who would never call themselves developers complain about versioning, about something breaking over there when they change something here, about design alignment, shipping, stability and security. Those are the non-functional requirements that were never really funded. Now that they build, they understand them, and they would understand them even better if they had seen what happens inside a technology company. They would realise how good they already are.

## Programming is not writing code {#programming}

I used to make the same case to people who were not founders, even engineers, who would say: I am not a developer, I do not program. And then you saw what they had built in Excel, or how they used a professional tool, a graphic design tool, a production tool, a tool specific to their field, and you thought: you are programming. That is what programming is. Writing code is a small part of development, and [the citizen developer](/articles/the-citizen-developer.html) made the case that this is good news.

## Call the book what they are {#book}

All of this keeps arriving at the book. The problem is that you have to convince people, and it is very hard to communicate with someone using a word they do not relate to. If the founders who are already doing all of this look at me as if I were joking when I call them developers, a book that calls its readers developers will lose exactly the people it is for. Many people who would benefit will not pick it up, because they are not developers. Even if you hand it to them, they will say: but I am not a developer. It is very hard to explain to someone that they will become a developer by doing this, when even the ones already doing it do not buy it at first.

So my hypothesis, and it is my thinking at the moment, is to change the title from *Generation ZX Developers* to *Generation ZX Founders*. That is what they are, and what they would recognise. It also gives the book a better target: a founder, or someone who would like to be one, has already qualified themselves.

And "you are a developer" moves to the end. By then the reader has founded something, shipped it and sold it, and the book can say: by the way, if you have done all this, you have been a developer, a product manager, a designer and a release manager, and you have been running a development team. Today that argument is chapter 8, *Everyone who can brief an agent is a developer*, early in the book. As the reveal at the end, it is something the reader can check against what they have just done.

The title is decided on the book's site, where [decision 014](https://gen-z-developers.sgit.ai/decisions/index.html#the-title-is-generation-zx-developers-genai-startup-edition) chose *Generation ZX Developers (GenAI Startup Edition)* and decision 017 made it a new book rather than a second edition. This is the next question for it.

## What this does not claim {#limits}

- **"Every founder I know" is my experience.** Not a survey.
- **The title is a hypothesis.** Decision 014 stands until a new decision replaces it.
- **The iPhone story is from one reporter's account.** Vogelstein's, from the engineers he interviewed.
- **The Director prototypes were internal.** Apple did not show them as working software.
- **Some founders' work is fragile.** Being a developer is not the same as the work being ready for users; [who will fix your mess?](/articles/who-will-fix-your-mess.html) is about that gap.

## Where this comes from {#sources}

A voice memo from me on 19 October 2026. Fred Vogelstein, [And Then Steve Said, 'Let There Be an iPhone'](https://www.nytimes.com/2013/10/06/magazine/and-then-steve-said-let-there-be-an-iphone.html), New York Times Magazine, 4 October 2013. The Associated Press on COMDEX, 20 April 1998, [archived copy](https://lists.tlug.jp/ML/9804/msg00419.html). James Thomson, [I live my life a quarter century at a time](https://tla.systems/blog/2025/01/04/i-live-my-life-a-quarter-century-at-a-time/), January 2025. Joel Spolsky, [The Iceberg Secret, Revealed](https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/), 13 February 2002. [Bootswatch Sketchy](https://bootswatch.com/sketchy/); [Napkin Look & Feel](https://napkinlaf.sourceforge.net/). The book's [decisions](https://gen-z-developers.sgit.ai/decisions/index.html). Related: [explorer coding](/articles/explorer-coding.html), [the citizen developer](/articles/the-citizen-developer.html), [the SaaS apocalypse](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html), [who will fix your mess?](/articles/who-will-fix-your-mess.html), [Generation Z Developers (AI edition)](/articles/generation-z-developers-again.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
