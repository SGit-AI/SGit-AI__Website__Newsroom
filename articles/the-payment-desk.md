# The payment desk that could not take payment: paying a utility bill took two clerks, a system that half worked and a desk that accepted only one kind of card, and why I think AI's real impact on business is in small failures like this one, finding them and driving the change to fix them, while the money itself stays in plain, auditable code, sgit.ai

> This morning I went to a service desk to pay a utility bill. It took two clerks: the first could find the bill, but her system could not take the payment; the second one's system kind of worked; and the desk accepted only one domestic card network, no Visa, no Mastercard. None of this is about one company or one country; the same small failures happen in England and everywhere else. But it made something clear to me. When people talk about AI and business, they talk about replacing people and systems. I think the real gains are in the little things: the desk that fails, the hand-over nobody records, the card nobody can use. And there is a clean line in where AI belongs. The payment itself, read the invoice number and take the money, is the one job that must keep working with everything else on fire, and it should be plain, reliable, auditable code, not AI. AI belongs around it: noticing the desk fails every week, mapping who has to agree to fix it and what it costs, and following it up until it is done. And yes, we will give agents wallets, as soon as we trust them; a single-use card with a small budget would be more secure than what I carry today.

*Source: <https://newsroom.sgit.ai/articles/the-payment-desk.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The payment desk that could not take payment: paying a utility bill took two clerks, a system that half worked and a desk that accepted only one kind of card, and why I think AI's real impact on business is in small failures like this one, finding them and driving the change to fix them, while the money itself stays in plain, auditable code

# The payment desk that could not take payment: paying a utility bill took two clerks, a system that half worked and a desk that accepted only one kind of card, and why I think AI's real impact on business is in small failures like this one, finding them and driving the change to fix them, while the money itself stays in plain, auditable code

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/the-payment-desk.md) · [newsroom v0.14.138](https://newsroom.sgit.ai/admin/versions.html) · aibusinesspaymentstechnical-debtchangeopinionarticle

***Abstract:** This morning I went to a service desk to pay a utility bill. It took two clerks: the first could find the bill, but her system could not take the payment; the second one's system kind of worked; and the desk accepted only one domestic card network, no Visa, no Mastercard. None of this is about one company or one country; the same small failures happen in England and everywhere else. But it made something clear to me. When people talk about AI and business, they talk about replacing people and systems. I think the real gains are in the little things: the desk that fails, the hand-over nobody records, the card nobody can use. And there is a clean line in where AI belongs. The payment itself, read the invoice number and take the money, is the one job that must keep working with everything else on fire, and it should be plain, reliable, auditable code, not AI. AI belongs around it: noticing the desk fails every week, mapping who has to agree to fix it and what it costs, and following it up until it is done. And yes, we will give agents wallets, as soon as we trust them; a single-use card with a small budget would be more secure than what I carry today.*

Paying one bill in four small failures, and the one job that must always work: code for the payment, AI around it.

## In short

- **Paying one bill took two clerks,** a system that half worked, and a desk that took one kind of card.
- **Not about one company or one country:** the same happens everywhere.
- **AI's real gains are in the little things,** not in grand replacements.
- **The one job that must never fail:** read the invoice number, take the money.
- **Code for the money, AI for the change** around it.
- **Agents will get wallets,** as soon as we trust them.

## Four small failures

This morning I went to a service desk to pay a utility bill.

**The invoice** had everything needed to pay it: who is owed, how much, and a reference. In Portugal a bill like this can usually also be paid at any Multibanco terminal or in home banking.

**The first clerk** found the bill, then could not take the payment: something in her system did not work. You could argue that is the most fundamental thing such a system should be able to do.

**The second clerk** typed the same number in again, and her system was kind of working. Hardware fails and things break; that is normal. The question is what happens next: who is recording this? A machine that works if you shake it, a screen that fails every few days, a hand-over between two desks: each one is a signal, and a source of data, if anyone captures it.

**The card:** the desk accepted only Multibanco cards, no Visa, no Mastercard, nothing from outside the Portuguese network. Multibanco itself is quietly impressive: the same network lets you pay bills, the State and phone top-ups from a cash machine, almost like a mini website, which the UK does not have. But refusing every other card is technical debt or a cost decision, and either way it is bad service for anyone with a foreign card.

## The minimum viable desk

If most people who walk into that office come to pay an invoice, then taking that payment is the one job that must keep working, even with the rest of the system on fire. Read the invoice number, take the money, reconcile later if the link is down. Everything else can wait; that cannot.

It is the idea of a minimum viable company, or a minimum viable system: know the few things that must never fail, and make them never fail.

## Code for the money, AI for the change

I am clear about where AI does not belong. For mission-critical things like this, you want code that is reliable, auditable, that we can check and verify. You should not be using AI for that.

Where AI belongs is everything around it: noticing that a desk fails every week, mapping who has to agree to fix it, what it costs and what it breaks, and following it up until it is done. Driving change in an organisation is hard, and it should be, because there are many moving parts. That is exactly why it is a good place for AI: it maps the parts ([who will fix your mess](who-will-fix-your-mess.md)).

## Agents with wallets

I also do not believe people will refuse to trust agents with money. We will give agents money, and wallets, as soon as we trust them. An agent with a 10, 50 or 100 pound budget, able to create a single-use card for one payment, would be far more secure than what I carry now. The payment underneath is, again, just code; what the agent removes is the friction around it, and what makes it safe is a behaviour policy that says what it may spend and on what ([where assist becomes execute](where-assist-becomes-execute.md)).

## One by one

This newsroom is built the same way: one small problem at a time, each fixed, recorded and checked. The interesting work is not the grand replacement. It is the queue at the desk, the second clerk, and the card that does not work.

## What this does not claim

- **One visit, one desk;** the company is not named, because the point is not about one company.
- **Agents with wallets is my position,** not a product we run.

## Where this comes from

My own visit to pay a utility bill on 17 November 2026, first published by my PrompTugal.news newsroom ([the original](https://promptugal.news/articles/the-payment-desk-that-could-not-take-payment.html)), whose conductor agent wrote it up from my words and drew the infographic (CC BY 4.0). On Multibanco: [Santander Portugal](https://www.santander.pt/empresas/tesouraria/pagamentos-cobrancas/pagamento-servicos) on paying services, and [SIBS](https://www.sibs.com/wp-content/uploads/sites/13/2019/11/2019-11-22_API-Market_MULTIBANCO.pdf) on what the network does. Earlier on this site: [who will fix your mess](who-will-fix-your-mess.md), [where assist becomes execute](where-assist-becomes-execute.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#the-payment-desk)

### Builds on

- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.

### Continued by

- [Who wrote it, who steered it, who signs it: the provenance model PrompTugal.news adopted today, a type label, five axes and a ladder from "published by an agent" to "on the record", applied to seven articles on this site, and what the ladder cannot see yet, how much of the author is in a piece, the brief, the corrections and months of background](who-steered-this.md) PrompTugal.news's provenance model, a label, five axes and a ladder, applied to seven articles here, and the two measures it misses.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 453 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=453)

**Posting this article on LinkedIn?** The cover is [the-payment-desk.jpg](banners/the-payment-desk.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-payment-desk.html)*
