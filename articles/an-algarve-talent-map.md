# An Algarve talent map: how Algarve Evolution can turn its mapping of services, mentors and investors into a public matchmaking site, built by one Claude session, with consent first, sgit.ai

> Algarve Evolution has already done the hard part of something the region needs. With forms, conversations and a lot of legwork, António Guerreiro and the Algarve Evolution team mapped the people in the Algarve who can provide services, who have talent, who could mentor and who could invest. What is missing is the place where that map can be used. Finding the right person is still luck: you post something and hope. I found a consultant who now works with us exactly that way. A founder should be able to say what they need and what they will pay, and find the people who fit; an investor or a mentor should be able to find the founders. Algarve Evolution sits at the centre of the regional ecosystem and has the credibility to publish this. This article maps how, and comes with a working prototype with invented people. The architecture is four things: the spreadsheet they already hold; a dedicated Google Workspace mailbox; a Claude session that builds and runs it; and a GitHub repository with Pages to serve it. No server and no database. The steps are five: build the site with simulated people; send each person a preview of their own listing; publish only those who approve; let visitors search, post needs and pay per contact; and keep going. Consent comes first, because these are people's details: nobody is published until they have seen their listing and said yes, and anyone can withdraw. Nobody pays to be listed, and nobody pays rent; a visitor pays a little per contact, after the value. Our own team will be the first listings.

*Source: <https://newsroom.sgit.ai/articles/an-algarve-talent-map.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An Algarve talent map: how Algarve Evolution can turn its mapping of services, mentors and investors into a public matchmaking site, built by one Claude session, with consent first

# An Algarve talent map: how Algarve Evolution can turn its mapping of services, mentors and investors into a public matchmaking site, built by one Claude session, with consent first

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/an-algarve-talent-map.md) · [newsroom v0.14.24](https://newsroom.sgit.ai/admin/versions.html) · algarvematchmakingtalentopen-sourceconsentclaudegithub-pagesarticle

***Abstract:** Algarve Evolution has already done the hard part of something the region needs. With forms, conversations and a lot of legwork, António Guerreiro and the Algarve Evolution team mapped the people in the Algarve who can provide services, who have talent, who could mentor and who could invest. What is missing is the place where that map can be used. Finding the right person is still luck: you post something and hope. I found a consultant who now works with us exactly that way. A founder should be able to say what they need and what they will pay, and find the people who fit; an investor or a mentor should be able to find the founders. Algarve Evolution sits at the centre of the regional ecosystem and has the credibility to publish this. This article maps how, and comes with a working prototype with invented people. The architecture is four things: the spreadsheet they already hold; a dedicated Google Workspace mailbox; a Claude session that builds and runs it; and a GitHub repository with Pages to serve it. No server and no database. The steps are five: build the site with simulated people; send each person a preview of their own listing; publish only those who approve; let visitors search, post needs and pay per contact; and keep going. Consent comes first, because these are people's details: nobody is published until they have seen their listing and said yes, and anyone can withdraw. Nobody pays to be listed, and nobody pays rent; a visitor pays a little per contact, after the value. Our own team will be the first listings.*

The prototype Algarve Talent Map, with invented people: search, roles, towns and a pay-per-contact credit.

## In short

- **Algarve Evolution has mapped the region's talent:** people who provide services, mentor, or invest.
- **What is missing is a place to use it.** Today, finding the right person is luck.
- **The proposal is a public matchmaking site,** run by Algarve Evolution, with the credibility it already has.
- **Four parts:** the spreadsheet, a dedicated mailbox, a Claude session, and GitHub Pages. No server, no database.
- **Consent first:** each person sees their own listing before anything is published, and can say no.
- **Nobody pays to be listed, and nobody pays rent.** Visitors pay a little per contact, after the value.
- **A prototype with invented people exists,** for Algarve Evolution's team to try and point a session at.

## The hard part is done

António Guerreiro told me about something Algarve Evolution has already done, and I think it is one of the most useful things in the region. With forms, conversations and a lot of legwork, what I would call an old-school exercise, Algarve Evolution mapped the people in the Algarve who can provide services and have talent, the people who could mentor, and the people who could invest. António is happy to be on the record about this project; this article describes it from our conversation, and the words quoted will be António's own, added once they are on the record.

That map is the hard part. It is a first batch of people who are warm, who took part, and who want to be found.

## Matchmaking is still luck

What is missing is the place where the map can be used. I know the problem first-hand. When I found the consultant who now works with us, it was luck: I posted some things, and the right person happened to see them. It would be much better to go to a community and say: I am working with these founders, they need this kind of talent, these are the requirements, and this is what they will pay.

The same is true for investors looking for companies, mentors looking for founders to help, and people with services to offer who do not know where to advertise them. All of them need one place in the middle, and Algarve Evolution is already in the middle: established, credible, and trusted by the people on the map.

## The architecture

A talent map in four parts and five steps: a spreadsheet, a mailbox, a Claude session and GitHub Pages.

None of this is complicated. What is needed is a website that is a web version of the spreadsheet: a page for every person, what they offer or want, a way to search and filter, and a form to post a need. It needs four parts:

- **The spreadsheet** Algarve Evolution already holds. It stays theirs; only approved rows ever leave it.
- **A dedicated mailbox:** a Google Workspace account, about £7 a month, so the map has its own address for previews, approvals and introductions.
- **A dedicated Claude session,** about £20 a month on a team plan, which reads the spreadsheet, builds the site, writes each person's preview and handles the replies.
- **GitHub, with Pages:** a repository for the code and the approved data, served as a site on the map's own domain, at no cost.

No server to run and no database to secure: the approved data is a file, and the site reads it. Everything we would contribute is open source.

## Consent first

The consent step: each person sees their own listing as it would appear, and approves it, changes it or says no.

These are people's names, skills, rates and contact details, so the order matters. Nobody is published until they have approved their own listing:

1. **Build the site with simulated people first,** like the prototype, so everyone can see what it will look like.
2. **Send each person a preview of their own listing,** from the map's mailbox: exactly what would appear, and three answers, approve, change it, or do not list me.
3. **Publish only those who approve,** with the date of their approval kept, and a way to withdraw at any time.

Algarve Evolution collected the data and is responsible for it, and in Europe publishing someone's personal details needs a proper basis. Asking each person, and keeping their yes, is the cleanest one, and it is also good for the map: an approved listing is one the person stands behind. It is in everyone's interest to be listed, so I expect most people to say yes; but the default is not listed, and that is the right default.

We will go first. Our own team will be the first listings, approved by us, so the first preview anyone receives can point at real people who said yes.

## Paying for what is used

It should earn its keep, and in the way I recommend for everything: pay per use, not rent.

- **Being listed is free,** and so is browsing and posting a need.
- **A visitor pays a little per contact,** from credit they top up, after they have seen the profile. In the prototype, a contact costs €0.50 from €5 of starting credit, the way [this newsroom's reader account](paying-after-the-value.md) works.
- **No monthly subscription** for anyone. The value is the introduction, so that is what is paid for.

The prices in the prototype are placeholders; what an introduction is worth is Algarve Evolution's call.

## The prototype

A profile in the prototype, after the visitor has paid €0.50 from their credit to see the contact.

There is a working prototype with fourteen invented people, mentors, investors and people offering services in towns across the Algarve, and four invented needs. It has search and filters, a page per person, a needs board, a form to post a need, the credit meter, and the consent screen each person would receive. It is one static page with the data inside it, which is the point: the real one is the same thing with Algarve Evolution's approved data.

## How Algarve Evolution's team can build it

The brief for their Claude session is short, and this article is part of it:

1. **Set up** a Google Workspace mailbox for the map, a Claude session, and a GitHub repository with Pages on the map's domain.
2. **Give the session this article and the prototype,** and ask it to build the same site with simulated data first.
3. **Give it the spreadsheet,** kept private, and ask it to write a preview for every person, in Portuguese and English, from the map's mailbox.
4. **Publish only approved rows,** each with the date of approval, and handle changes and withdrawals as replies arrive.
5. **Iterate** from what visitors actually search for and the needs they post, the loop of [from a checklist to an app you calibrate](from-a-checklist-to-an-app.md).

If the team wants it done for them, that is what [villager services](villager-services-for-explorer-coders.md) are for. But the point is that they do not need us: everything here is open, and a session with this brief can build it.

## What this does not claim

- **It is a proposal and a prototype.** Nothing is built on Algarve Evolution's data, and every person and need in the prototype is invented.
- **António Guerreiro's words are not quoted.** The project is described from my conversation with António, who is happy to be on the record, and those words will be added.
- **Consent is described, not legal advice.** Algarve Evolution will want its own view on how it publishes the data it holds.
- **The prices are approximate:** the mailbox and model plans at their usual monthly prices, and the contact fee a placeholder.
- **My interest:** The Cyber Boardroom is joining Algarve Evolution, and I build some of the tools this would use.

## Where this comes from

- My voice memo of 31 October 2026, word for word in `admin/notes/2026-10-31__algarve-evolution/memo-03.md` in this site's repository.
- The prototype, built for this article with invented data.
- Related: [joining Algarve Evolution](joining-algarve-evolution.md), [Vibathon Algarve 2026](vibathon-algarve-2026.md), [from a checklist to an app you calibrate](from-a-checklist-to-an-app.md), [villager services for explorer coders](villager-services-for-explorer-coders.md), [paying after the value](paying-after-the-value.md).

## Threads

Startups & strategyVaults & method[This article as a graph →](graphs.md#an-algarve-talent-map)

### Builds on

- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [From a checklist to an app you calibrate: your list is already an information system, so build its smallest version in half an hour, use it, log every run, and let it grow](from-a-checklist-to-an-app.md) From a checklist to an app you calibrate: build the smallest version in half an hour, use it tomorrow, log every run, and let it grow.
- [Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent](villager-services-for-explorer-coders.md) Villager services for explorer coders: founders with ten years of checklists build the apps; we sell everything behind them in finite packs.
- [Joining Algarve Evolution: The Cyber Boardroom takes the startup membership, and what we can share with the region, our workflows and our technology, all of it open source](joining-algarve-evolution.md) Joining Algarve Evolution: The Cyber Boardroom takes the startup membership and shares its workflows and technology, all open source.
- [Vibathon Algarve 2026: a sold-out day of building with AI at the University of the Algarve, and Algarve Evolution, the movement that wants the region to be an innovation hub](vibathon-algarve-2026.md) Vibathon Algarve 2026: a sold-out day of building with AI in Faro, and Algarve Evolution, the movement making the region an innovation hub.

### Continued by

- [Spreadsheet to App: a session programme for Algarve Evolution, with five example spreadsheets, five prompts, a mock event and a public vault, so nobody arrives needing a problem to solve](spreadsheet-to-app-sessions.md) Spreadsheet to App: a session programme for Algarve Evolution, with five examples, five prompts, a mock event and a public vault.
- [Sell to the companies that already have the problem: how Algarve Evolution can match businesses adopting AI with the region's service providers, starting when the business has built its own first app](sell-to-the-companies-that-already-have-the-problem.md) Sell to the companies that already have the problem: matching Algarve businesses that built their own AI apps with the region's providers.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 345 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=345)

**Posting this article on LinkedIn?** The cover is [an-algarve-talent-map.jpg](banners/an-algarve-talent-map.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-algarve-talent-map.html)*
