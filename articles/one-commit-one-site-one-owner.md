# One commit, one site, one owner: the small change to the AgentiCCells site factory that unblocked the most, giving a GitHub account access to the repository it creates, so that one commit with a site's details and its owner's account makes the repository, the DNS record in AWS, the address, HTTPS and the owner's access in under a minute, and all that is left is to point Claude at it, sgit.ai

> Some of the things that make the biggest difference are hard to measure, and small. On 17 November, at about 18:20, I said yes to a change in the AgentiCCells site factory, "since it will really make a massive difference": a second domain, a GitHub token per owner, and collaborators. The last one is the detail. The factory could already turn a request file in a commit into a GitHub repository, a DNS record in AWS, a seeded site, its address and HTTPS. Now the same request can name the GitHub accounts that should have access, and the factory invites them at the end. So one commit with the details of a site and its owner's account does everything: when events.promptugal.news was created today, the factory validated the request at 14:28:12, created the repository four seconds later, seeded it, configured it, set the DNS record, enforced HTTPS at 14:29:06 and gave the owner's account access at 14:29:07, 55 seconds in all. The factory has now handled 36 requests. And the hand-over is one sentence: point your Claude at this repository, and start editing. Part two of the series.

*Source: <https://newsroom.sgit.ai/articles/one-commit-one-site-one-owner.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / One commit, one site, one owner: the small change to the AgentiCCells site factory that unblocked the most, giving a GitHub account access to the repository it creates, so that one commit with a site's details and its owner's account makes the repository, the DNS record in AWS, the address, HTTPS and the owner's access in under a minute, and all that is left is to point Claude at it

# One commit, one site, one owner: the small change to the AgentiCCells site factory that unblocked the most, giving a GitHub account access to the repository it creates, so that one commit with a site's details and its owner's account makes the repository, the DNS record in AWS, the address, HTTPS and the owner's access in under a minute, and all that is left is to point Claude at it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/one-commit-one-site-one-owner.md) · [newsroom v0.14.158](https://newsroom.sgit.ai/admin/versions.html) · agenticcellssite-factorygithubawsautomationseriesarticle

***Abstract:** Some of the things that make the biggest difference are hard to measure, and small. On 17 November, at about 18:20, I said yes to a change in the AgentiCCells site factory, "since it will really make a massive difference": a second domain, a GitHub token per owner, and collaborators. The last one is the detail. The factory could already turn a request file in a commit into a GitHub repository, a DNS record in AWS, a seeded site, its address and HTTPS. Now the same request can name the GitHub accounts that should have access, and the factory invites them at the end. So one commit with the details of a site and its owner's account does everything: when events.promptugal.news was created today, the factory validated the request at 14:28:12, created the repository four seconds later, seeded it, configured it, set the DNS record, enforced HTTPS at 14:29:06 and gave the owner's account access at 14:29:07, 55 seconds in all. The factory has now handled 36 requests. And the hand-over is one sentence: point your Claude at this repository, and start editing. Part two of the series.*

One commit to a live site with its owner: validate, repository, seed, settings, DNS, HTTPS, access, in 55 seconds.

## In short

- **The factory already made sites from a commit:** repository, DNS, address, HTTPS.
- **The missing piece was access:** giving the owner's GitHub account the repository.
- **Added on 17 November,** with a token per owner and a second domain.
- **events.promptugal.news: 55 seconds** from request to a live site with its owner's access.
- **36 requests so far.**
- **The hand-over is one sentence:** point Claude at the repository.

Part two of [gaining speed](gaining-speed.md).

## What the factory did already

The AgentiCCells site factory turns a request file in a commit into a site: "a request file in a commit makes a CI pipeline create the GitHub repository, the DNS record and the sgit vault, seed a page, check HTTPS ... so an agent can create sites by committing". The plan runs on the pull request; the work runs on merge ([the site factory works](the-site-factory-works.md)).

What it could not do was hand the site to someone. The repository belonged to the factory's account, and giving another person or agent access meant a person clicking through GitHub's settings.

## The small change

At about 18:20 on 17 November I said yes to three changes, "since it will really make a massive difference", and the factory's agent made them in one commit at 18:25: a second domain, so sites can be created on promptugal.news as well as agenticcells.site; a GitHub token per owner, so each organisation's sites are made with its own credentials; and a collaborators step. After HTTPS, the factory now invites each GitHub account named in the request with push access, up to five, and records whether each was invited or already there. Its own record says the change "worked on their first real run".

That is all it is. But it closes the loop: the request can now say whose site it is.

## 55 seconds

The factory's record for events.promptugal.news, 18 November, from 14:28:12 to 14:29:07.

The factory's record for events.promptugal.news, created today:

- **14:28:12** the request validated
- **14:28:16** the repository created
- **14:28:18** seeded from the template
- **14:28:21** settings: Pages built by Actions
- **14:28:33** the DNS record in AWS, visible in public DNS, and the domain set
- **14:29:06** HTTPS enforced
- **14:29:07** the owner's agent account given write access, which it accepts

Fifty-five seconds from a commit to a live, secure site that its owner can change. The same steps made data.promptugal.news the evening before in 55 seconds too, and the factory has now handled 36 requests, 35 of them live.

## Point Claude at it

This is why the detail matters. With access in the request, the hand-over to a person is one sentence: here is your repository; point your Claude at it, and start editing. Nothing to configure, no settings to click, no account of ours in the middle. It is the last step of the website cell ([the website cell](the-website-cell.md)), and it is what lets a partner sell one without touching GitHub ([partners sell, we build](partners-sell-we-build.md)).

It is also what let PrompTugal.news grow six sites in one afternoon: each new site came with access for the agent that would build it, so the team could start the moment the site existed.

## Small things, big effects

I keep finding that the changes that speed us up most are small and hard to measure: a token per owner, a step that invites an account, a rule that one agent may write one file. Each removes a person from a loop they never needed to be in, and the loop runs as often as we like.

## What this does not claim

- **The owner still accepts the invitation** in GitHub; that step stays with them.
- **The factory creates sites only on domains it controls** today: agenticcells.site and promptugal.news.
- **A Claude first pass that improved each new site was switched off** today to save cost; sites start from the template.

## Where this comes from

The AgentiCCells site factory repository, read on 18 November 2026: its README, REALITY.md, the commit of 17 November at 18:25 and the request records, including `requests/2026-11-18__events-promptugal-news/status.json`. Earlier on this site: [gaining speed](gaining-speed.md), [the site factory works](the-site-factory-works.md), [the website cell](the-website-cell.md), [partners sell, we build](partners-sell-we-build.md).

## Threads

Startups & strategy[This article as a graph →](graphs.md#one-commit-one-site-one-owner)

### Builds on

- [Gaining speed: a series on what happens when you productise the way you build, PrompTugal.news going from a newsroom at Web Summit to a data intelligence platform for Portugal's places in two weeks, a factory that turns one commit into a site with its owner, money that flows back to the sources, sites built on the data in minutes, the librarian, and a team like this for sale](gaining-speed.md) A series on what happens when you productise how you build: PrompTugal.news from a summit newsroom to a data platform in two weeks.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [Partners sell, we build: the AgentiCCells partner programme in full, three kinds of partner, a freelancer, a small consultancy and a larger firm, what each one sells, the agent team behind even the smallest website cell, the rules of engagement, who owns what, who invoices, who gets paid and when, what stays with the partner, and why a partner who takes the open code and does it alone is still a win](partners-sell-we-build.md) The AgentiCCells partner programme: three kinds of partner, the agent team they resell, and the rules of engagement, 50/50.

### Continued by

- [Sites on the data: what happens when a data platform meets a factory that makes a site in minutes, a page that draws IPMA's data six ways, an invented holiday-homes company whose bookings are simulated and whose weather, sea and events are real, demos for weather, events and cyber, and how each experiment, a new industry, a new view, a new idea, is now a site published in ten or twenty minutes](sites-on-the-data.md) When a data platform meets a site factory, every idea becomes a site: IPMA six ways, and holiday homes with real weather and events.
- [Gaining speed: a series on what happens when you productise the way you build, PrompTugal.news going from a newsroom at Web Summit to a data intelligence platform for Portugal's places in two weeks, a factory that turns one commit into a site with its owner, money that flows back to the sources, sites built on the data in minutes, the librarian, and a team like this for sale](gaining-speed.md) A series on what happens when you productise how you build: PrompTugal.news from a summit newsroom to a data platform in two weeks.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 476 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=476)

**Posting this article on LinkedIn?** The cover is [one-commit-one-site-one-owner.jpg](banners/one-commit-one-site-one-owner.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/one-commit-one-site-one-owner.html)*
