---
title: Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent
date: 2026-10-31
author: Dinis Cruz
author_url: about/index.html
summary: At the Vibathon in Faro two participants, an engineer and a designer, showed me a checklist they have refined for ten years and wanted to turn into an app: what to do when you leave a house and when you arrive at another. I wrote up the advice I gave them. This is the next step: the business. Their checklist is the brief, battle-hardened and valuable, and they are what I would call the ultimate product managers: clever, experienced, and close to the problem. They will never need to learn GitHub, CI pipelines or testing, and they should not have to. But they will hit every non-functional requirement, because building with an AI is addictive and every feature asks for the next. So the proposal is villager services for explorer coders. We take what they built and release it without changing what it does: in a repository, deployed properly, locked down, reviewed, tested, with private data opened by a passkey and kept in a vault, and agents running on a schedule inside a harness. It breaks less, more people can use it, and then it becomes a business. Users pay for use, a few pounds of credit at first and more after the value; the explorers buy finite packs, around £500, £2,000 or £5,000, and can share the revenue; and they sell it, because the people around them trust them more than they trust us. The market is Generation X founders with a running business, a folder of spreadsheets, time, money and a need. The work is finite and handed over, never rent; our own agents make each pack faster than the last; and the last step is to town-plan the villager service itself, into a commodity with a buy-now page.
version: v0.14.22
license: https://creativecommons.org/licenses/by/4.0/
tags: villagers, explorer-coding, business-model, consulting, lovable, vaults, pki, article
status: published
---

!shot vx-roles.webp | images/ | Villager services for explorer coders: the explorers keep the brief and the features, and we build the rest. | concept

## In short {#in-short}

- **The checklist is the brief.** Ten years of getting it right and wrong; that is the valuable part.
- **The explorers are the ultimate product managers.** They should never need to learn GitHub, CI or testing.
- **They will hit every non-functional requirement,** because building with an AI is addictive.
- **Villager services release what they built without changing what it does:** deployed, locked down, tested, private where needed.
- **Users pay for use; explorers buy finite packs,** and can share the revenue. Nobody pays rent.
- **The explorers sell it,** to people who trust them more than us.
- **Our own agents make each pack faster,** and the villager service becomes a commodity.

## The brief they already have {#brief}

In [from a checklist to an app you calibrate](/articles/from-a-checklist-to-an-app.html) I wrote up the advice I gave two participants at the Vibathon in Faro. They have a document they have refined for about ten years: what to do when you leave a house and what to do when you arrive at another. It is a standard operating procedure: turn the gas off, set this, do that, if this then that, with the important steps in bold. My advice was to start turning it into an app with Lovable that afternoon.

The good news is that they already have the brief. Ten years of getting it right, getting it wrong and adding what was forgotten have made it battle-hardened, and that is the valuable part. Writing the code is now the cheap part.

## The ultimate product managers {#explorers}

People like them, one an engineer and the other a designer, with a career and a life behind them, are what I would call the ultimate product managers. They know the problem better than anyone who would build it for them, and they can say what good looks like.

What they will never need to understand is GitHub, CI pipelines or testing. And they should not have to. That is not their job, and asking them to learn it is how good ideas die. This is [explorer coding](/articles/explorer-coding.html): exploring what to build by building it, with an AI writing the code.

And they will hit every non-functional requirement. Not because they make mistakes, but because it is addictive: you build this, then you want that, then this, and the feedback loop is so powerful that you keep adding features. It is even stronger for someone who never had the ability to go from an idea to a working app in an afternoon. I know, because I have felt it, including the moment it tips into [burning out a bit](/articles/two-years-in-the-opposite.html). Somewhere in all those features, the app needs to stay up, keep data safe, work for a second person and not break when it changes.

## What villager services do {#villagers}

So the proposal is a partnership. We give them the villager side: the environment and the code that a product needs and an explorer should never see. We take what they built and we release it, without changing the functionality. That is the rule. Everything we do is behind the scenes:

- **A repository and a proper deployment,** with every version kept.
- **Locked down and reviewed,** with the obvious holes closed before anyone else uses it.
- **Tests and a CI pipeline,** so a change that breaks something is caught before it ships.
- **Private data where it is needed,** opened with the user's passkey and kept in a vault, so it is private everywhere and still needs no server of ours.
- **Agents on a schedule, inside a harness,** for the jobs that should run on their own, contained by a policy so they can be let loose safely.

What the explorers notice is not any of that. They notice that it breaks less, and that more people can use it. That is the moment it can become a business.

This is the model of [software vendors as villagers](/articles/software-vendors-as-villagers.html) and of [who will fix your mess](/articles/who-will-fix-your-mess.html): explorers build, villagers make it dependable, town planners make it a commodity. What has changed is that the primitives now exist, built over the last weeks: everything on the client side and no server of ours to run; keys and passkeys for anything private; vaults for the data; a [harness](/articles/introducing-sharness.html) to contain agents. And the brain does not have to be ours either: a £20 a month model account, Claude, ChatGPT or Mistral, can be it. For many small businesses, a Google Workspace account at about £7 a month and a model account at about £20 already make an email workflow that is secure and theirs, for less than they spend on coffee.

## How it makes money {#money}

!shot vx-offer.webp | images/ | The offer: users pay for use, explorers buy finite packs, and nobody pays rent. | table

**Users pay for use.** Imagine they share the app with someone. That person opens it and sees a small counter: a few pounds or dollars of credit to start. It is useful, so they use it, the credit runs down, and at that moment, having already had the value, they will probably pay £5 or £10. It is [paying after the value](/articles/paying-after-the-value.html), and the meter is the user's, as in [the user keeps the meter](/articles/the-user-keeps-the-meter.html). If they want to save their own data, they need a vault, and they pay for that too. How much it is worth depends far more on the use case than on the workflow.

**Explorers buy finite packs.** Once they are hooked, and they will not want to go back to the document, there is a commercial offer for them: a pack at around £500, £2,000 or £5,000 that productises what they built, integrates it with the way they work, or makes it something others can buy. With a share of the revenue for them where it is sold on.

**And they sell it.** The best people to sell this are the explorers, because they are in the community. When we say it is good, people say of course you can use it. When they say: I had a document with no history that never connected anything, hard to maintain, hard to share, on my phone, and look at this now, an app, with if this then that, and the day I almost forgot the gas it reminded me, that is what sells. The small features they are proud of are the ones they promote.

This is not about millions. It is about thousands and tens of thousands, and I think that is a good business, because the real value, the gold, is in the spreadsheets and workflows they already have.

## Finite, never rent {#finite}

It is critical that everything we do is finite. We deliver a pack, we hand it over, and that is the work. That moves us out of the rent business, the same argument as [websites you own](/articles/websites-you-own.html): nobody should be paying us every month, and nobody should be calling us at two in the morning.

And the more packs we deliver, the faster each one gets, because we use the same tools on ourselves: our own team of agents maintaining the estate. That is how it scales. If a pack costs £500 and takes a couple of hours, or a day, it makes commercial sense, and it is what I think consulting becomes.

## Who it is for, and how it spreads {#market}

The market, I think, is Generation X founders with a running business: they have the spreadsheets, the time, the money and the need, and the app already adds value to them on the day it works.

It spreads one person at a time. Get one person to build something that works for them. Then get a second person to use what the first created, which matters because they are two different people. If it adds value to both, it can go on the internet, ideally in public, which makes everything easier. That is why shipping is so critical: when the second person uses it, we want to be there with the offer.

And it does not stop at one app. A session with twenty people like these produces twenty apps. I told the two in Faro that once they had done this, they would go to every spreadsheet in their working life and make it an app, and they agreed. They will not want to maintain any of them.

## Town-plan the villager service {#town}

The last step is ours. The brief comes free, from the explorers; the packaging is what we sell, and it has to be packaged: clear packs, clear prices, a buy-now page and a cart. That means doing to the villager service what town planners do to everything else: turning it into a commodity, repeatable, priced and quick, so it can be bought without a conversation.

## What this does not claim {#limits}

- **It is a proposal.** No pack has been sold and no price is final; the figures are the ones in my memo.
- **The participants are not named,** and their app is theirs; the example stands for many like it.
- **The primitives run, in part.** The vaults and the reader meter run on this newsroom; the passkey vault and the harness are early, as their own articles say.
- **My interest:** I build the tools this proposal would use, and I would sell the packs.

## Where this comes from {#sources}

- My voice memo of 31 October 2026, word for word in `admin/notes/2026-10-31__checklist-to-app/memo-02.md` in this site's repository, after the conversation in memo 01.
- Related: [from a checklist to an app you calibrate](/articles/from-a-checklist-to-an-app.html), [explorer coding](/articles/explorer-coding.html), [software vendors as villagers](/articles/software-vendors-as-villagers.html), [who will fix your mess](/articles/who-will-fix-your-mess.html), [websites you own](/articles/websites-you-own.html), [paying after the value](/articles/paying-after-the-value.html), [the user keeps the meter](/articles/the-user-keeps-the-meter.html), [Vibathon Algarve 2026](/articles/vibathon-algarve-2026.html).
