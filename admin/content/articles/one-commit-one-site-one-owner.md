---
title: One commit, one site, one owner: the small change to the AgentiCCells site factory that unblocked the most, giving a GitHub account access to the repository it creates, so that one commit with a site's details and its owner's account makes the repository, the DNS record in AWS, the address, HTTPS and the owner's access in under a minute, and all that is left is to point Claude at it
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: Some of the things that make the biggest difference are hard to measure, and small. On 17 November, at about 18:20, I said yes to a change in the AgentiCCells site factory, "since it will really make a massive difference": a second domain, a GitHub token per owner, and collaborators. The last one is the detail. The factory could already turn a request file in a commit into a GitHub repository, a DNS record in AWS, a seeded site, its address and HTTPS. Now the same request can name the GitHub accounts that should have access, and the factory invites them at the end. So one commit with the details of a site and its owner's account does everything: when events.promptugal.news was created today, the factory validated the request at 14:28:12, created the repository four seconds later, seeded it, configured it, set the DNS record, enforced HTTPS at 14:29:06 and gave the owner's account access at 14:29:07, 55 seconds in all. The factory has now handled 36 requests. And the hand-over is one sentence: point your Claude at this repository, and start editing. Part two of the series.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, site-factory, github, aws, automation, series, article
status: published
---

!shot oco-steps.webp | images/ | One commit to a live site with its owner: validate, repository, seed, settings, DNS, HTTPS, access, in 55 seconds. | process

## In short {#in-short}

- **The factory already made sites from a commit:** repository, DNS, address, HTTPS.
- **The missing piece was access:** giving the owner's GitHub account the repository.
- **Added on 17 November,** with a token per owner and a second domain.
- **events.promptugal.news: 55 seconds** from request to a live site with its owner's access.
- **36 requests so far.**
- **The hand-over is one sentence:** point Claude at the repository.

Part two of [gaining speed](/articles/gaining-speed.html).

## What the factory did already {#before}

The AgentiCCells site factory turns a request file in a commit into a site: "a request file in a commit makes a CI pipeline create the GitHub repository, the DNS record and the sgit vault, seed a page, check HTTPS ... so an agent can create sites by committing". The plan runs on the pull request; the work runs on merge ([the site factory works](/articles/the-site-factory-works.html)).

What it could not do was hand the site to someone. The repository belonged to the factory's account, and giving another person or agent access meant a person clicking through GitHub's settings.

## The small change {#change}

At about 18:20 on 17 November I said yes to three changes, "since it will really make a massive difference", and the factory's agent made them in one commit at 18:25: a second domain, so sites can be created on promptugal.news as well as agenticcells.site; a GitHub token per owner, so each organisation's sites are made with its own credentials; and a collaborators step. After HTTPS, the factory now invites each GitHub account named in the request with push access, up to five, and records whether each was invited or already there. Its own record says the change "worked on their first real run".

That is all it is. But it closes the loop: the request can now say whose site it is.

## 55 seconds {#events}

!shot oco-run.webp | images/ | The factory's record for events.promptugal.news, 18 November, from 14:28:12 to 14:29:07. | table

The factory's record for events.promptugal.news, created today:

- **14:28:12** the request validated
- **14:28:16** the repository created
- **14:28:18** seeded from the template
- **14:28:21** settings: Pages built by Actions
- **14:28:33** the DNS record in AWS, visible in public DNS, and the domain set
- **14:29:06** HTTPS enforced
- **14:29:07** the owner's agent account given write access, which it accepts

Fifty-five seconds from a commit to a live, secure site that its owner can change. The same steps made data.promptugal.news the evening before in 55 seconds too, and the factory has now handled 36 requests, 35 of them live.

## Point Claude at it {#handover}

This is why the detail matters. With access in the request, the hand-over to a person is one sentence: here is your repository; point your Claude at it, and start editing. Nothing to configure, no settings to click, no account of ours in the middle. It is the last step of the website cell ([the website cell](/articles/the-website-cell.html)), and it is what lets a partner sell one without touching GitHub ([partners sell, we build](/articles/partners-sell-we-build.html)).

It is also what let PrompTugal.news grow six sites in one afternoon: each new site came with access for the agent that would build it, so the team could start the moment the site existed.

## Small things, big effects {#small}

I keep finding that the changes that speed us up most are small and hard to measure: a token per owner, a step that invites an account, a rule that one agent may write one file. Each removes a person from a loop they never needed to be in, and the loop runs as often as we like.

## What this does not claim {#limits}

- **The owner still accepts the invitation** in GitHub; that step stays with them.
- **The factory creates sites only on domains it controls** today: agenticcells.site and promptugal.news.
- **A Claude first pass that improved each new site was switched off** today to save cost; sites start from the template.

## Where this comes from {#sources}

The AgentiCCells site factory repository, read on 18 November 2026: its README, REALITY.md, the commit of 17 November at 18:25 and the request records, including `requests/2026-11-18__events-promptugal-news/status.json`. Earlier on this site: [gaining speed](/articles/gaining-speed.html), [the site factory works](/articles/the-site-factory-works.html), [the website cell](/articles/the-website-cell.html), [partners sell, we build](/articles/partners-sell-we-build.html).
