---
title: The citizen developer is good news: the spreadsheet grown up, the best briefs ever written, and the handover from explorers to villagers and town planners that makes them last
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: At a conference today the phrase "citizen developer" came up as a worry, the new name for people outside IT building things they should not. I think it is one of the best things to happen to software, and a better way to talk about what is usually called vibe coding. It is not only citizens: it is the employee, the business owner, the expert, the person who knows the work. People have always built with what they controlled, and for most of them that was a spreadsheet; spreadsheets are full of errors, and the world runs on them anyway, because they were the only tool people had. Now they can build full applications, and those applications are also the best briefs ever written: what the user actually wants, in a form that runs. The work is the handover, from the explorer who built it to the villagers who harden it and the town planners who make it scale, with all the non-functional requirements the explorer never had to think about. Encrypted, versioned vaults are a natural carrier for that: a mini app with its UI and its data in one place, which is what a spreadsheet always was, with history, keys and a clean handover added. Done well, this lets people, organisations and even countries move from rent-seeking, control-based software to tools that serve them, which is also the direction of the business models this newsroom is testing.
version: v0.12.54
license: https://creativecommons.org/licenses/by/4.0/
tags: citizen-developer, vibe-coding, spreadsheets, wardley-maps, villagers, town-planners, vault-apps, sgit, empowerment, article
status: published
---

!shot cz-path.webp | images/ | From the spreadsheet to the town planners: the citizen developer's path. People built with what they controlled, a spreadsheet; now they build the application they need, which is also the best brief ever written; villagers harden it and town planners make it scale, and an sgit vault carries the app and its data through every handover. | architecture

## In short {#in-short}

- **A worry, turned round.** The citizen developer is not a risk to contain; it is the best thing to happen to software in a long time.
- **Not only citizens.** The employee, the business owner, the expert: the people who know the work.
- **The spreadsheet grown up.** People always built with what they controlled; now they can build applications.
- **The best briefs ever written.** A working app says what the user wants better than any document.
- **The handover is the work.** From explorers to villagers to town planners, with the non-functional requirements added.
- **A vault is a good carrier.** A mini app with its UI and data, versioned, encrypted and distributed.
- **From rent-seeking to empowerment.** Tools that serve people, and business models where people choose to pay.

## A worry, turned round {#worry}

At a conference today, someone mentioned "citizen developers", attributed to an AWS event, with the tone people use for a problem: employees outside IT building applications that IT will have to clean up. I could not trace the exact quote, but AWS's own definition is neutral enough: "Business users with no or little coding experience, often called citizen developers, can build applications themselves." Gartner describes it as a persona rather than a job title.

I think it is a better way to talk about what has become known as vibe coding, the term Andrej Karpathy coined in February 2025 for coding where you "forget that the code even exists". And I think it is very good news. It is not only citizens, either. It is the employee developer, the business owner developer, the expert in a domain that technology has served badly for decades, building the thing they actually need.

## The spreadsheet grown up {#spreadsheet}

People have always built software with whatever they controlled, and for most of them that was a spreadsheet. A spreadsheet is a user interface and a database in one file, and the business world runs on them, errors and all. In Raymond Panko's audits, as The Register reported, "Of 54 spreadsheets audited between 1997 and 2000, no fewer than 49 were found to contain significant errors". JPMorgan's London Whale model "operated through a series of Excel spreadsheets, which had to be completed manually", and at one point "divided by their sum instead of their average". In October 2020, England's test and trace system lost 15,841 positive cases because an old Excel format "limited the number of rows to 65,536".

Those are not arguments against the people who built them. They are a testament to how badly technology served them: the spreadsheet was the only tool they had that they could change themselves. [The SaaS apocalypse](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) put it in one line: "Every department will now have people building software the way they build spreadsheets". Now those same people can build full applications, with a real interface, real data and real logic, because they can.

## The best briefs ever written {#brief}

The most useful thing about an application built by the person who needs it is not the application. It is the brief. Requirements documents have always been the weakest link in software: a description, by someone who knows the work, of something they have never seen, for someone who does not know the work. A working app, built by the user, is a brief that runs. It says exactly what the user wants, what they do first, what they never use, and what matters to them, without anyone having to guess.

That is also where the mistake people make is. The SaaS article called it "treating the brief as if it were already a product". A working app is not yet maintained, secured, documented, tested, versioned or able to scale, and the person who built it usually does not want to do any of that. They want to build it and hand it over.

## The handover is the work {#handover}

This is where [Wardley maps](/articles/why-i-love-wardley-maps.html) help, and why I keep coming back to them. Simon Wardley describes three kinds of people for three stages of anything: explorers, villagers and town planners. The citizen developer is an explorer, and that is exactly what an explorer should be doing: finding what is needed, quickly, by building it. Then the villagers take the brief and stabilise it, harden it and put it into production, and the town planners make it scale, with the non-functional requirements the explorer never had to think about: security, reliability, observability, cost, documentation, support.

The newsroom went through exactly that move: [Explorer to villager](/articles/explorer-to-villager-newsroom.html) described slowing down to take what had been built quickly and make it something that can be maintained. With agents, the handover itself becomes cheap and visible: a move from one folder to another and a version bump, logged and reviewable. And the security of the result is now within reach of everyone, as [The eyeballs get cheap](/articles/the-eyeballs-get-cheap.html) argued: deep review is no longer only for teams that can pay for it.

## A vault is a good carrier {#vaults}

The piece of the puzzle I think is underrated is where these mini apps live. A spreadsheet is a UI with data behind it, in one file, emailed around, never versioned. An sgit vault can hold the same thing, a small application with its interface and its data, and add what the spreadsheet never had: history, so every change is a commit; keys, so a reader can see without being able to change; encryption, so it can live anywhere; and a clean handover, because the villager clones exactly what the explorer committed.

I already work this way: small applications with a UI and the data behind them, in vaults, as [Custom UIs are not the exception](/articles/custom-uis-are-not-the-exception.html) described ("A custom interface per message or moment is not an exception"), and as the wires on this site show, with research desks writing vaults that the site reads. [What sgit is](/articles/what-sgit-is.html) is the longer version of why. A vault is a distributed, versioned spreadsheet that can be a whole application, and that is exactly the carrier the citizen developer's work needs on its way to the town planners.

## From rent-seeking to empowerment {#empowerment}

The bigger point is what this enables. Industries, practices and people that technology served badly, or served by renting them software they could not change, can now build what they need. That applies to individuals, to teams, to companies, and to countries: [sovereignty is the ability to move](/articles/sovereignty-is-the-ability-to-move.html), and the ability to build your own tools is the first step to it. It lets people be creative and scale what they do in ways that were not possible before.

And it changes the business models around it. When the user can build, the business is no longer locking them in; it is serving them well enough that they choose to pay. That is what this newsroom is testing with its reading meter, where readers pay after they have read, and only for what they valued: [Pay after you read](/articles/pay-after-you-read.html) is the experiment, and [Paying after the value](/articles/paying-after-the-value.html), published alongside this one, is the psychology behind it.

## What this does not claim {#limits}

- **The conference quote is untraced.** The AWS attribution came from a speaker; AWS's own definition is quoted instead.
- **Spreadsheet errors are old evidence.** Panko's audits are from 1997 to 2000; the London Whale and test and trace cases are well documented.
- **Not every app should be scaled.** Most citizen-built apps will stay small, and should; the handover is for the ones that matter.
- **Vaults are one carrier.** They are the one I use and build; the argument does not depend on them.

If you have people building their own applications and want help turning the best ones into something that lasts, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, after a conference, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. A research agent gathered the evidence and the quotes were checked on the pages themselves. AWS, [What is low-code?](https://aws.amazon.com/what-is/low-code/); Gartner, [citizen developer](https://www.gartner.com/en/information-technology/glossary/citizen-developer); Wikipedia, [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding); The Register on [Panko's spreadsheet audits](https://www.theregister.com/2006/05/03/buggy_spreadsheet) and on [the test and trace error](https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/); James Kwak on [the London Whale's spreadsheets](https://baselinescenario.com/2013/02/09/the-importance-of-excel); Simon Wardley, [How to organise yourself](https://blog.gardeviance.org/2023/12/how-to-organise-yourself-dangerous-path.html). All read on 14 October 2026.
