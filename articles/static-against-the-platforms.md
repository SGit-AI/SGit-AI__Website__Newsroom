# Static against the platforms: why a static site in your own repository, edited by Claude and watched by a security agent, is a real alternative to WordPress, Wix and Squarespace, what the numbers say about their reach, their attack surface, their complexity and their lock-in, and a converter that could bring a WordPress or Squarespace site across, sgit.ai

> I think the website cell has a real market, and the place to look for it is the people already running a site on WordPress, Wix or Squarespace. Those platforms are not short of features; they are full of them, and full of complexity. I know people who maintain WordPress sites, and I remember one where changing a banner did not work, and nobody could update it normally. The numbers back that up. WordPress runs 38.5% of all websites; Wix has 6.1 million paying subscriptions; Squarespace had more than 5.2 million when it last said. In 2025, 11,334 new vulnerabilities were found in the WordPress ecosystem, 91% of them in plugins, 46% with no fix when they were disclosed, and the worst ones were mass-exploited a median of five hours after. A third of WordPress sites run an older major version; 60% use a page builder; only 45% pass Core Web Vitals on mobile. Wix's sites cannot be moved off Wix, and Squarespace exports only part of a site; both raised prices this year. Against that, a website cell is static: no server code, no database, no plugins to patch, no cookies unless the owner adds them, served as files. Its editor is Claude, which can do far more than any page editor; and it ships with a security agent that checks what the owner's changes expose. The owner can still shoot themselves in the foot, and that is a service a partner can sell. And because WordPress exports everything, and Squarespace exports in WordPress's format, one converter could bring a large share of those sites across.

*Source: <https://newsroom.sgit.ai/articles/static-against-the-platforms.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Static against the platforms: why a static site in your own repository, edited by Claude and watched by a security agent, is a real alternative to WordPress, Wix and Squarespace, what the numbers say about their reach, their attack surface, their complexity and their lock-in, and a converter that could bring a WordPress or Squarespace site across

# Static against the platforms: why a static site in your own repository, edited by Claude and watched by a security agent, is a real alternative to WordPress, Wix and Squarespace, what the numbers say about their reach, their attack surface, their complexity and their lock-in, and a converter that could bring a WordPress or Squarespace site across

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/static-against-the-platforms.md) · [newsroom v0.14.148](https://newsroom.sgit.ai/admin/versions.html) · websiteswordpresswixsquarespacesecuritystatic-sitesagenticcellsmarketarticle

***Abstract:** I think the website cell has a real market, and the place to look for it is the people already running a site on WordPress, Wix or Squarespace. Those platforms are not short of features; they are full of them, and full of complexity. I know people who maintain WordPress sites, and I remember one where changing a banner did not work, and nobody could update it normally. The numbers back that up. WordPress runs 38.5% of all websites; Wix has 6.1 million paying subscriptions; Squarespace had more than 5.2 million when it last said. In 2025, 11,334 new vulnerabilities were found in the WordPress ecosystem, 91% of them in plugins, 46% with no fix when they were disclosed, and the worst ones were mass-exploited a median of five hours after. A third of WordPress sites run an older major version; 60% use a page builder; only 45% pass Core Web Vitals on mobile. Wix's sites cannot be moved off Wix, and Squarespace exports only part of a site; both raised prices this year. Against that, a website cell is static: no server code, no database, no plugins to patch, no cookies unless the owner adds them, served as files. Its editor is Claude, which can do far more than any page editor; and it ships with a security agent that checks what the owner's changes expose. The owner can still shoot themselves in the foot, and that is a service a partner can sell. And because WordPress exports everything, and Squarespace exports in WordPress's format, one converter could bring a large share of those sites across.*

A platform site against a website cell: what runs, what can be attacked, who edits, what leaves with you.

## In short

- **The market is the people already on a platform:** WordPress runs 38.5% of all websites.
- **The platforms are rich and complex,** and much of the complexity is attack surface.
- **11,334 WordPress vulnerabilities in 2025,** 91% in plugins, 46% unfixed when disclosed.
- **Lock-in is real:** Wix sites cannot leave Wix; Squarespace exports part of a site; prices rose.
- **A website cell is static:** no server code, no database, no plugins, no cookies by default.
- **Its editor is Claude,** and it ships with a security agent.
- **A converter** from WordPress, and Squarespace through WordPress's format, could bring sites across.

## Where the market is

When I asked who would buy a website cell ([the website cell](the-website-cell.md)), the obvious answer was people without a website. The bigger answer is people who already have one, and are tired of it. W3Techs puts WordPress on 38.5% of all websites, Shopify on 5.4%, Wix on 4.2% and Squarespace on 2.4%. Wix reported 6.11 million premium subscriptions at the end of 2025; Squarespace last reported more than 5.2 million unique subscriptions, in 2024, before it was taken private. Every one of those is a person paying, every month, for a site.

## Rich, and complex

These platforms are not short of features. The problem is the opposite: they have so many that running a simple site means running a complicated system. I know people who maintain WordPress sites, and the complexity is remarkable. I remember one site where changing a banner did not work, and nobody could update it the normal way; it was a mess, and not practical at all.

The HTTP Archive's 2025 Web Almanac gives the shape of it. About 60% of WordPress sites use a page builder on top of WordPress, Elementor alone on 43% of them on mobile. On mobile, 45% of WordPress sites pass Core Web Vitals, against 74% of Wix sites; WordPress's median mobile page weighs about 2.9 MB, Squarespace's about 4 MB. And the WordPress.org statistics show about a third of WordPress sites on an older major version, and about one in ten several versions behind. Keeping all of it working is why a London small business typically pays an agency a retainer of £200 to £300 a month for a brochure site.

I looked for a survey of how many of the features people actually use, and did not find one I trust. My guess, from the sites I know, is a small fraction: pages, a contact form, a gallery, a blog that is rarely updated.

## The attack surface

WordPress's attack surface in 2025: 11,334 new vulnerabilities, 91% in plugins, 46% with no fix at disclosure.

Every feature that runs on a server is something that can be attacked. Patchstack, which sells WordPress security, counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, up 42% on the year before: 91% in plugins, 9% in themes, and only six in WordPress itself. 46% had no fix available when they were disclosed, and for the heavily exploited ones, the median time from disclosure to mass exploitation was five hours. Wordfence, which also sells protection, blocked 9.1 billion attacks on its firewall in the last quarter of 2025 alone. Sucuri found that 39% of the sites it cleaned in 2023 were running an outdated system, and half had a backdoor.

The hosted platforms carry less of that for their owners, because the platform patches it, but they are not immune: in July 2024, domains moved from Google Domains to Squarespace were hijacked because multi-factor authentication was not carried over.

The point is not that WordPress is badly built. It is that a site which runs plugins, themes and a database on a server inherits every flaw in all of them, and has to be patched, by someone, within hours.

## Locked in

Wix's own help page says its sites need to be hosted and operated on Wix's servers and cannot be moved to another host. Squarespace exports a site only as a WordPress-format file, covering pages, one blog and their text and images, and leaving out the store, products, audio and video blocks, other page types and the styles. And this year both raised prices: Squarespace by 18 to 26% on three of its four plans, with an apology for over-charging some renewals; Wix on new subscriptions and renewals, moving legacy plans onto new ones. When you cannot leave, the price is whatever the platform says.

## What a website cell is instead

A website cell is the opposite design ([you bring the business, we build the site](you-bring-the-business.md)):

- **Static:** the site is files, built once and served as they are. There is no server code running, no database, no plugin to patch, no login page to brute-force on the site itself.
- **No cookies unless the owner adds them:** nothing to put behind a banner. If the owner wants analytics, they can add Google Analytics, or the encrypted, cookie-free observability we use, which writes visits into a vault through an append-only lane ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)).
- **In the owner's repository:** every change is a commit, every version can be restored, and the site deploys to any static host ([the site factory works](the-site-factory-works.md)).
- **Edited by Claude:** the most capable editor there is. It can add a page, rewrite a section, read a CV and update the experience, connect a feed, or build a feature, in plain words.

The static design removes the category of flaw that makes up almost all of Patchstack's 11,334: code running on a server. I did not find an independent study that measures how much safer static sites are, so I will not claim a number; but the argument is simple, there is very little left to attack.

## You can still shoot yourself in the foot

A static site is not automatically safe. An owner's Claude could publish something private, embed a script from somewhere unsafe, or break a page. So every website cell ships with guard rails: a behaviour policy that says what the owner's agent may do ([where assist becomes execute](where-assist-becomes-execute.md)), CI checks and a leak scan before anything goes live, and a security agent that reviews what each change exposes. And where an owner wants a person to watch over it, that is exactly the service a partner can sell, monthly, at their own price ([partners sell, we build](partners-sell-we-build.md)).

## A converter

A converter: WordPress and Squarespace export, agents rebuild the content as a website cell, the owner keeps it.

Here is the part I find most interesting. WordPress can export everything, as an XML file or through its REST API. Squarespace's only export is in WordPress's format. So one converter, reading WordPress's format, could bring across the content of both: pages, posts, images, menus. The agents rebuild it as a static website cell, with five designs, the old site's words and pictures, and redirects from the old addresses; the owner checks it, and switches. Tools that turn a WordPress site into static files already exist, Simply Static has more than 30,000 active installs; what we add is the redesign, the repository, the policies and Claude as the editor afterwards.

Wix is harder, because it does not export; but the owner can always let an agent read their own public pages and start from there.

This is a proposal; the converter does not exist yet. But it is the shortest path from a platform site to one the owner owns.

## The opportunity

The numbers are large enough that the share we need is tiny. One site in ten thousand of Wix's paying subscriptions is more than 600 sites. The pitch is simple: a site that looks better, that you own, that nobody can lock you into, that has almost nothing to attack, that costs once instead of every month, and that you change by talking to Claude.

## What this does not claim

- **The security figures come from vendors** that sell WordPress security, Patchstack, Wordfence and Sucuri; they are the best data there is, and they have an interest.
- **No study measures static sites' security,** and I found none on how many features site owners use.
- **The number of WordPress sites is not known;** shares, not counts, are what is measured.
- **The converter is a proposal.**

## Where this comes from

[W3Techs](https://w3techs.com/technologies/overview/content_management), read on 18 November 2026; [Wix's results for 2025](https://www.sec.gov/Archives/edgar/data/1576789/000162828026014406/fourthquarterandfullyear20.htm); [Squarespace's subscriptions](https://www.stylefactoryproductions.com/blog/squarespace-statistics) (secondary, 2024); the [Web Almanac 2025 CMS chapter](https://almanac.httparchive.org/en/2025/cms); the [WordPress.org version statistics](https://api.wordpress.org/stats/wordpress/1.0/), read on 18 November 2026; [Patchstack, State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/); [Wordfence, Q4 2025](https://www.wordfence.com/blog/2026/02/quarterly-wordpress-threat-intelligence-report-q4-2025/); [Sucuri, 2023](https://blog.sucuri.net/2024/06/2023-hacked-website-malware-threat-report.html); [SecurityWeek](https://www.securityweek.com/hackers-exploit-flaw-in-squarespace-migration-to-hijack-domains/) on the Squarespace domain hijacks; [Wix on exporting](https://support.wix.com/en/article/exporting-or-embedding-your-wix-site-elsewhere); [Squarespace on exporting](https://support.squarespace.com/hc/en-us/articles/206566687-Exporting-your-site); [TechRadar](https://techradar.com/pro/im-paying-for-things-i-sincerely-did-not-ask-for-squarespace-users-arent-happy-with-recent-price-hikes) and [Wix](https://support.wix.com/en/article/upcoming-changes-to-wix-premium-plan-pricing) on prices; a [London agency](https://kolonell.com/en/blog/wordpress-maintenance-retainer-comparison-london-smes-2026) on retainers; [WordPress's REST API](https://developer.wordpress.org/rest-api/). Earlier on this site: [the website cell](the-website-cell.md), [you bring the business, we build the site](you-bring-the-business.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [the site factory works](the-site-factory-works.md), [where assist becomes execute](where-assist-becomes-execute.md), [partners sell, we build](partners-sell-we-build.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#static-against-the-platforms)

### Builds on

- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [You bring the business, we build the site: the AgentiCCells partner programme as it now stands on agenticcells.ai, one page per kind of partner, each with four figures, the fit, the flow, who does what and the money, a launch price of £250 with free evaluations every day, partner terms published, five designs on every page and ten languages from day one, all built in a night by the site's own agent team from two newsroom articles](you-bring-the-business.md) The AgentiCCells partner programme as built overnight: one page per partner, four figures each, £250 launch, free evaluations, ten languages.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [Partners sell, we build: the AgentiCCells partner programme in full, three kinds of partner, a freelancer, a small consultancy and a larger firm, what each one sells, the agent team behind even the smallest website cell, the rules of engagement, who owns what, who invoices, who gets paid and when, what stays with the partner, and why a partner who takes the open code and does it alone is still a win](partners-sell-we-build.md) The AgentiCCells partner programme: three kinds of partner, the agent team they resell, and the rules of engagement, 50/50.

### Continued by

- [The sovereign website: a pivot brief for agenticcells.ai, what the site says today and what it should say next, sovereignty as the headline, a website you own, control, change and can run anywhere, the deliverables explained, the infographics to draw, five homepage designs to choose from, and the partner programme and examples that already prove it](the-sovereign-website.md) A pivot brief for agenticcells.ai: lead with sovereignty, show the deliverables, draw the infographics, and make five homepage designs.
- [Sovereignty you can move: why where your data is hosted is not sovereignty, why being able to move the site, the data and the schema is, why that makes the website cell a direct competitor to Wix, Squarespace and Fliplet with a proper sovereign offer, European-aligned, multilingual and privacy-first, and the business that other companies can build on it](sovereignty-you-can-move.md) Sovereignty is being able to move your site, data and schema, not where it is hosted; the website cell as a sovereign competitor.
- [No lock-in: why the one thing that most separates the website cell from Wix, Squarespace, Fliplet and the rest is that the customer can leave, what the platforms' own terms and export pages say, how large the market of people paying monthly for sites they cannot take with them is, and what a site that promises to move into its owner's hands should say on its front page](no-lock-in.md) The website cell's biggest difference is that the customer can leave; the platforms' own terms show why that matters.
- [Rent or own: Fliplet, an AI software builder advertised on the London Underground, against the AgentiCCells website cell, both building from a plain-language description and changing by talking to an AI, one a monthly platform paid in credits, the other a one-off build handed over into the customer's own repository, and why we should promise to move every site into its owner's hands within three months](fliplet-and-the-website-cell.md) Fliplet, an AI software builder you rent, against the website cell, a one-off build its owner keeps, and a three-month ownership promise.
- [Start with an interview: how someone goes from "I want to try it" to editing their own site with Claude, by being interviewed by Claude first, about what they want, the sections, their materials and the sites they like, then sending their material in whichever way suits them, getting five designs inspired by what they like, or a better version of the site they already have, and reaching the one milestone that matters](start-with-an-interview.md) Onboarding by interview: Claude asks what you want and which sites you like, material comes any way, and you end up editing with Claude.
- [The pitch: a site that looks better, that you own, that nobody can lock you into, that has almost nothing to attack, that costs once instead of every month, and that you change by talking to Claude, six promises, the proof behind each, and three designs for a site built on nothing else, "six promises", "just say it" and "stop renting your website"](the-pitch.md) A site that looks better, that you own, that nobody can lock you into: six promises, their proof, and three designs built on the pitch.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 466 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=466)

**Posting this article on LinkedIn?** The cover is [static-against-the-platforms.jpg](banners/static-against-the-platforms.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/static-against-the-platforms.html)*
