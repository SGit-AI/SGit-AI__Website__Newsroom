---
title: Static against the platforms: why a static site in your own repository, edited by Claude and watched by a security agent, is a real alternative to WordPress, Wix and Squarespace, what the numbers say about their reach, their attack surface, their complexity and their lock-in, and a converter that could bring a WordPress or Squarespace site across
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: I think the website cell has a real market, and the place to look for it is the people already running a site on WordPress, Wix or Squarespace. Those platforms are not short of features; they are full of them, and full of complexity. I know people who maintain WordPress sites, and I remember one where changing a banner did not work, and nobody could update it normally. The numbers back that up. WordPress runs 38.5% of all websites; Wix has 6.1 million paying subscriptions; Squarespace had more than 5.2 million when it last said. In 2025, 11,334 new vulnerabilities were found in the WordPress ecosystem, 91% of them in plugins, 46% with no fix when they were disclosed, and the worst ones were mass-exploited a median of five hours after. A third of WordPress sites run an older major version; 60% use a page builder; only 45% pass Core Web Vitals on mobile. Wix's sites cannot be moved off Wix, and Squarespace exports only part of a site; both raised prices this year. Against that, a website cell is static: no server code, no database, no plugins to patch, no cookies unless the owner adds them, served as files. Its editor is Claude, which can do far more than any page editor; and it ships with a security agent that checks what the owner's changes expose. The owner can still shoot themselves in the foot, and that is a service a partner can sell. And because WordPress exports everything, and Squarespace exports in WordPress's format, one converter could bring a large share of those sites across.
version: v0.14.148
license: https://creativecommons.org/licenses/by/4.0/
tags: websites, wordpress, wix, squarespace, security, static-sites, agenticcells, market, article
status: published
---

!shot sap-compare.webp | images/ | A platform site against a website cell: what runs, what can be attacked, who edits, what leaves with you. | comparison

## In short {#in-short}

- **The market is the people already on a platform:** WordPress runs 38.5% of all websites.
- **The platforms are rich and complex,** and much of the complexity is attack surface.
- **11,334 WordPress vulnerabilities in 2025,** 91% in plugins, 46% unfixed when disclosed.
- **Lock-in is real:** Wix sites cannot leave Wix; Squarespace exports part of a site; prices rose.
- **A website cell is static:** no server code, no database, no plugins, no cookies by default.
- **Its editor is Claude,** and it ships with a security agent.
- **A converter** from WordPress, and Squarespace through WordPress's format, could bring sites across.

## Where the market is {#market}

When I asked who would buy a website cell ([the website cell](/articles/the-website-cell.html)), the obvious answer was people without a website. The bigger answer is people who already have one, and are tired of it. W3Techs puts WordPress on 38.5% of all websites, Shopify on 5.4%, Wix on 4.2% and Squarespace on 2.4%. Wix reported 6.11 million premium subscriptions at the end of 2025; Squarespace last reported more than 5.2 million unique subscriptions, in 2024, before it was taken private. Every one of those is a person paying, every month, for a site.

## Rich, and complex {#complex}

These platforms are not short of features. The problem is the opposite: they have so many that running a simple site means running a complicated system. I know people who maintain WordPress sites, and the complexity is remarkable. I remember one site where changing a banner did not work, and nobody could update it the normal way; it was a mess, and not practical at all.

The HTTP Archive's 2025 Web Almanac gives the shape of it. About 60% of WordPress sites use a page builder on top of WordPress, Elementor alone on 43% of them on mobile. On mobile, 45% of WordPress sites pass Core Web Vitals, against 74% of Wix sites; WordPress's median mobile page weighs about 2.9 MB, Squarespace's about 4 MB. And the WordPress.org statistics show about a third of WordPress sites on an older major version, and about one in ten several versions behind. Keeping all of it working is why a London small business typically pays an agency a retainer of £200 to £300 a month for a brochure site.

I looked for a survey of how many of the features people actually use, and did not find one I trust. My guess, from the sites I know, is a small fraction: pages, a contact form, a gallery, a blog that is rarely updated.

## The attack surface {#attack}

!shot sap-attack.webp | images/ | WordPress's attack surface in 2025: 11,334 new vulnerabilities, 91% in plugins, 46% with no fix at disclosure. | chart

Every feature that runs on a server is something that can be attacked. Patchstack, which sells WordPress security, counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, up 42% on the year before: 91% in plugins, 9% in themes, and only six in WordPress itself. 46% had no fix available when they were disclosed, and for the heavily exploited ones, the median time from disclosure to mass exploitation was five hours. Wordfence, which also sells protection, blocked 9.1 billion attacks on its firewall in the last quarter of 2025 alone. Sucuri found that 39% of the sites it cleaned in 2023 were running an outdated system, and half had a backdoor.

The hosted platforms carry less of that for their owners, because the platform patches it, but they are not immune: in July 2024, domains moved from Google Domains to Squarespace were hijacked because multi-factor authentication was not carried over.

The point is not that WordPress is badly built. It is that a site which runs plugins, themes and a database on a server inherits every flaw in all of them, and has to be patched, by someone, within hours.

## Locked in {#lockin}

Wix's own help page says its sites need to be hosted and operated on Wix's servers and cannot be moved to another host. Squarespace exports a site only as a WordPress-format file, covering pages, one blog and their text and images, and leaving out the store, products, audio and video blocks, other page types and the styles. And this year both raised prices: Squarespace by 18 to 26% on three of its four plans, with an apology for over-charging some renewals; Wix on new subscriptions and renewals, moving legacy plans onto new ones. When you cannot leave, the price is whatever the platform says.

## What a website cell is instead {#static}

A website cell is the opposite design ([you bring the business, we build the site](/articles/you-bring-the-business.html)):

- **Static:** the site is files, built once and served as they are. There is no server code running, no database, no plugin to patch, no login page to brute-force on the site itself.
- **No cookies unless the owner adds them:** nothing to put behind a banner. If the owner wants analytics, they can add Google Analytics, or the encrypted, cookie-free observability we use, which writes visits into a vault through an append-only lane ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).
- **In the owner's repository:** every change is a commit, every version can be restored, and the site deploys to any static host ([the site factory works](/articles/the-site-factory-works.html)).
- **Edited by Claude:** the most capable editor there is. It can add a page, rewrite a section, read a CV and update the experience, connect a feed, or build a feature, in plain words.

The static design removes the category of flaw that makes up almost all of Patchstack's 11,334: code running on a server. I did not find an independent study that measures how much safer static sites are, so I will not claim a number; but the argument is simple, there is very little left to attack.

## You can still shoot yourself in the foot {#foot}

A static site is not automatically safe. An owner's Claude could publish something private, embed a script from somewhere unsafe, or break a page. So every website cell ships with guard rails: a behaviour policy that says what the owner's agent may do ([where assist becomes execute](/articles/where-assist-becomes-execute.html)), CI checks and a leak scan before anything goes live, and a security agent that reviews what each change exposes. And where an owner wants a person to watch over it, that is exactly the service a partner can sell, monthly, at their own price ([partners sell, we build](/articles/partners-sell-we-build.html)).

## A converter {#converter}

!shot sap-convert.webp | images/ | A converter: WordPress and Squarespace export, agents rebuild the content as a website cell, the owner keeps it. | process

Here is the part I find most interesting. WordPress can export everything, as an XML file or through its REST API. Squarespace's only export is in WordPress's format. So one converter, reading WordPress's format, could bring across the content of both: pages, posts, images, menus. The agents rebuild it as a static website cell, with five designs, the old site's words and pictures, and redirects from the old addresses; the owner checks it, and switches. Tools that turn a WordPress site into static files already exist, Simply Static has more than 30,000 active installs; what we add is the redesign, the repository, the policies and Claude as the editor afterwards.

Wix is harder, because it does not export; but the owner can always let an agent read their own public pages and start from there.

This is a proposal; the converter does not exist yet. But it is the shortest path from a platform site to one the owner owns.

## The opportunity {#opportunity}

The numbers are large enough that the share we need is tiny. One site in ten thousand of Wix's paying subscriptions is more than 600 sites. The pitch is simple: a site that looks better, that you own, that nobody can lock you into, that has almost nothing to attack, that costs once instead of every month, and that you change by talking to Claude.

## What this does not claim {#limits}

- **The security figures come from vendors** that sell WordPress security, Patchstack, Wordfence and Sucuri; they are the best data there is, and they have an interest.
- **No study measures static sites' security,** and I found none on how many features site owners use.
- **The number of WordPress sites is not known;** shares, not counts, are what is measured.
- **The converter is a proposal.**

## Where this comes from {#sources}

[W3Techs](https://w3techs.com/technologies/overview/content_management), read on 18 November 2026; [Wix's results for 2025](https://www.sec.gov/Archives/edgar/data/1576789/000162828026014406/fourthquarterandfullyear20.htm); [Squarespace's subscriptions](https://www.stylefactoryproductions.com/blog/squarespace-statistics) (secondary, 2024); the [Web Almanac 2025 CMS chapter](https://almanac.httparchive.org/en/2025/cms); the [WordPress.org version statistics](https://api.wordpress.org/stats/wordpress/1.0/), read on 18 November 2026; [Patchstack, State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/); [Wordfence, Q4 2025](https://www.wordfence.com/blog/2026/02/quarterly-wordpress-threat-intelligence-report-q4-2025/); [Sucuri, 2023](https://blog.sucuri.net/2024/06/2023-hacked-website-malware-threat-report.html); [SecurityWeek](https://www.securityweek.com/hackers-exploit-flaw-in-squarespace-migration-to-hijack-domains/) on the Squarespace domain hijacks; [Wix on exporting](https://support.wix.com/en/article/exporting-or-embedding-your-wix-site-elsewhere); [Squarespace on exporting](https://support.squarespace.com/hc/en-us/articles/206566687-Exporting-your-site); [TechRadar](https://techradar.com/pro/im-paying-for-things-i-sincerely-did-not-ask-for-squarespace-users-arent-happy-with-recent-price-hikes) and [Wix](https://support.wix.com/en/article/upcoming-changes-to-wix-premium-plan-pricing) on prices; a [London agency](https://kolonell.com/en/blog/wordpress-maintenance-retainer-comparison-london-smes-2026) on retainers; [WordPress's REST API](https://developer.wordpress.org/rest-api/). Earlier on this site: [the website cell](/articles/the-website-cell.html), [you bring the business, we build the site](/articles/you-bring-the-business.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [the site factory works](/articles/the-site-factory-works.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [partners sell, we build](/articles/partners-sell-we-build.html).
