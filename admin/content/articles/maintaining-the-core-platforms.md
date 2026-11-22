---
title: Maintaining the core platforms as a cost item in every project: a line sized to the project, delivering something every month, and what four weeks of php2shell data say happens without it
date: 2026-11-22
author: Dinis Cruz
author_url: about/index.html
summary: Every project that runs on an open source platform should carry a line in its budget for maintaining that platform, and when the line is missing that should show as a named risk. The line is many small purchases rather than one large one, sized in proportion to what the project itself spends, and it has to deliver something every month (patches applied, versions kept current, code removed, questions answered), because anything that looks like insurance is the first thing cut. The money should reach the people who maintain the code, who help set up and maintain what is built on top, and flow on down the chain. Gen AI makes that affordable, not by writing all the code, but by helping people understand code bases, side effects and changes. And there is now data to map the risk. Four weeks after php2shell, the Dutch NCSC's public inventory of software that ships or depends on PHP has 976 entries: 218 with a fix recorded and 214 not vulnerable, but 211 still marked vulnerable, 240 whose safety depends on the PHP runtime underneath them, and 92 with no answer either way. The 211 entries marked vulnerable were 221 on 23 October.
version: v0.14.204
license: https://creativecommons.org/licenses/by/4.0/
tags: open-source, php2shell, maintainers, maintenance, budgets, risk, business-models, article
status: published
---

!shot cpl-inventory.webp | images/ | The NCSC-NL php2shell inventory by status, one commit a week from 23 October to 19 November 2026. | chart

> **A follow-up to [who maintains the PHP you run?](/articles/who-maintains-the-php-you-run.html)** That article proposed versions signed off by the people who maintain them, buyers who require that signature, and services to sell. One of its sections argued for many small purchases in proportion to each project. This article is about that line in the budget, and about what a month of data says when it is not there.

## In short {#in-short}

- **Maintaining the core platforms is a cost item in every project.** A line in the budget, like hosting or testing, not a favour or a donation.
- **When the line is missing, that is a named risk.** It goes in the register and someone signs it, knowingly.
- **Many small purchases, in proportion.** The line is sized to what the project spends, so a small site and a large programme both carry one.
- **It delivers something every month.** Patches applied, versions current, code removed, questions answered. If it looks like insurance, it is cut.
- **The money reaches the people who know the code,** and they help set up and maintain what is built on top, and the chain goes on down from there.
- **Gen AI makes it affordable** by helping people understand code bases, side effects and changes, not by writing all the code.
- **There is data to map the risk now.** Four weeks after php2shell, 211 entries in the Dutch NCSC's inventory are still marked vulnerable, against 221 on 23 October.

## What I am proposing {#proposal}

I made this point in a comment on [who maintains the PHP you run?](/articles/who-maintains-the-php-you-run.html), and it deserves its own article, because it is the part a finance director can act on next week.

The support of the core platforms a project runs on, its language runtime, its framework, its CMS and the plugins it actually uses, has to be a cost item in that project. Not in a central IT budget that nobody connects to the project, and not as a donation from a corporate social responsibility fund: in the project's own budget, beside hosting, testing and support, approved by the same people who approve the rest. And when a project does not carry that line, its absence should be visible as a risk, named in the register, with a person who accepted it.

The line is lots of small purchases, not one big one. The amount spent maintaining the core pieces should be in proportion to the money spent on, and available in, the project. A €100,000 site and a €10 million programme both run on PHP; both should carry a line for it, and the lines should be very different sizes.

And it has to add value all the time. Something seen as insurance is paid in case, invisible in a good year, and cut in the first budget review. This line has to show up as work done, every month.

## Four weeks of data {#data}

When php2shell, the two critical flaws in PHP itself (CVE-2026-109618 and CVE-2026-109619), was disclosed on 21 October, the Dutch NCSC started a [public inventory](https://github.com/NCSC-NL/php2shell) of software that ships or depends on PHP, with a status for each product, and has kept it up to date in git since. Its history lets anyone count where things stood on any day. We counted it at one commit a week, the figure at the top:

- **23 October, 11:48 UTC:** 749 entries; 108 with a fix recorded, 30 not vulnerable, 389 under investigation, 221 vulnerable.
- **30 October, 08:16:** 929 entries; 165 fix, 201 not vulnerable, 345 under investigation, 217 vulnerable.
- **4 November, 08:32:** 948 entries; 185 fix, 214 not vulnerable, 240 runtime-dependent, 93 under investigation, 215 vulnerable.
- **12 November, 11:39:** 972 entries; 213 fix, 214 not vulnerable, 240 runtime-dependent, 92 under investigation, 212 vulnerable.
- **19 November, 21:15:** 976 entries; 218 fix, 214 not vulnerable, 240 runtime-dependent, 92 under investigation, 211 vulnerable.

Each count includes one entry with no status. The last count matches the inventory's own statistics file of 18 November, which gives the same figures.

Three things stand out.

- **Fixes doubled, from 108 to 218,** as suppliers published patched builds: Linux distributions, appliance makers, hosting platforms.
- **"Under investigation" fell from 389 to 92, mostly by being reclassified,** not by being answered. Between 30 October and 4 November a new status appeared, runtime-dependent, and 240 entries carry it: products with no direct statement of their own, whose exposure depends on the PHP runtime they are deployed on.
- **The entries marked vulnerable barely moved: 221 on 23 October, 211 on 19 November.** For each, a source confirms the product is affected in the stated scope, and four weeks after the release no fix is recorded in that entry.

## What a missing line looks like {#missing}

!shot cpl-missing.webp | images/ | The 543 inventory entries with neither a fix recorded nor a not-vulnerable status, in three kinds. | concept

Take the 543 entries that have neither a fix recorded nor a not-vulnerable status, and they fall into three kinds. Each is a different way of saying that nobody was paid to know.

- **211 marked vulnerable.** Whoever sells or runs these products cannot yet ship the fix. Some of these products have a fix in another entry, for a newer version; for the organisations still running the version in this entry, moving is exactly the work a maintenance line pays for.
- **240 runtime-dependent.** The product is safe or not depending on the PHP underneath it, which means whoever runs that PHP is answering for it, whether or not anybody budgeted for that. This is the line I am proposing, already being paid in risk.
- **92 under investigation.** Four weeks on, no source yet says either way. That is what it looks like when nobody can say quickly what a product depends on.

This is a national inventory of products. Every organisation can build the same map for its own projects: for each project, which core platforms it runs, how much it depends on each, who maintains each, and whether there is a line in the budget for it. The data to do that is now there, in inventories like this one, in software bills of materials, and in what the code actually loads. The ones without a line are the risk register.

## The line itself {#the-line}

!shot cpl-line.webp | images/ | What the line for maintaining a core platform would hold, against insurance, one-off audits and donations. | concept

What the line holds, as I would write it into a project budget:

- **The platform,** named precisely: PHP 8.3, the extensions this project uses, the CMS and the plugins it runs. Not "open source".
- **Who maintains it,** by name: people connected to the code, and how they are paid.
- **Its size,** as a share of the project's own spend, so that it grows and shrinks with the project.
- **What it delivers each month:** patches applied, versions kept current, code removed, questions answered, set-ups reviewed.
- **The evidence,** dated, so the line is seen to work and is not cut as insurance.
- **And, if it is not there, the risk,** named in the register and signed by the executive who accepted it.

The share is a decision for each organisation, and I am not proposing a number here. What matters is that it is proportional and recurring. A flat sponsorship from a central budget does not move when one project doubles; a line inside the project does.

## How this compares with what exists {#compared}

Money for maintainers already moves in several ways, and none of them is this line.

- **The [Open Source Pledge](https://opensourcepledge.com/)** asks companies to pay maintainers and foundations directly; its member companies pay more than $2,000 a year for each developer they employ, and its home page reported $9,200,672 raised when we read it on 22 November. That is per company and per developer, not per project, and not tied to what a project runs.
- **Foundation sponsorship,** such as the PHP Foundation's tiers from $12,000 a year, buys recognition and a seat at the table, as the [earlier article](/articles/who-maintains-the-php-you-run.html#both-ways) set out; it does not buy the maintenance of the PHP a project runs.
- **Long-term support vendors** sell patched builds of old versions, a real market that php2shell showed works for those who pay, but most do not state any share reaching the people who wrote the fix.

The line I am proposing sits inside the project, sized to it, and buys work on the exact platform the project runs, from people connected to its code.

## Down the chain {#chain}

The money should reach the maintainers, and it should come with work, not only thanks. The people who maintain PHP, for example, would be involved and paid to help set up the applications built on it and to maintain them, and the same goes for the people who maintain the CMS on top of PHP, and the people who maintain the plugins on top of that. Each step of the chain is paid by the step above it, and each one pushes quality down to the next, because people who are paid to answer for a platform have little patience for what they cannot support.

## Why it is affordable now {#gen-ai}

This is not about Gen AI writing all the code. The maintainers still read it, and their judgement is what the line pays for. What Gen AI changes is the work around that judgement: understanding a code base someone else built, seeing the side effects of a change, explaining what a patch does to one customer's version, keeping the documentation and the tests current. That is what used to make customised maintenance expensive, and it is what now lets a small line, in a small project, buy real work from people who know the code.

## Where we stand {#interest}

I have a commercial interest, and would rather say so. At [RiskMandate](https://riskmandate.ai), the company I co-founded, everything is open source, so working with it starts at £0, and paid help starts at £500; maintenance retained by the people who build a customer's version is one of the ways we are proposing to work, described in [the earlier article](/articles/who-maintains-the-php-you-run.html#selling). The argument here does not depend on who sells the work. It depends on the line being in the budget.

## What this does not claim {#limits}

- **The line is a proposal.** I know of no procurement rule or budgeting standard that requires it today.
- **No share is proposed.** How large the line should be for a given project is for each organisation to decide; the €100,000 and €10 million examples are illustrations of proportion, not budgets.
- **The inventory counts entries, not organisations.** An entry is a product or a product scope, and the same product can have one entry marked vulnerable and another, for a newer version, with a fix. We counted entries as the inventory lists them, at five commits; we did not check each entry against its sources.
- **The status labels changed during the period.** Runtime-dependent was first counted on 4 November, so the drop in "under investigation" is partly a reclassification, as the article says.
- **The inventory is not complete,** by its own disclaimer, and it does not cover custom PHP applications inside organisations.
- **Nothing here says any listed product was compromised.**
- **I have a commercial interest,** stated above.

## Where this comes from {#sources}

My comment of 24 October 2026 on [who maintains the PHP you run?](/articles/who-maintains-the-php-you-run.html), kept in this site's list of articles to write, and my request on 22 November to write it. The data: a clone of [NCSC-NL/php2shell](https://github.com/NCSC-NL/php2shell) read on 22 November 2026, its software lists counted at commits `b216139`, `b88f1e9`, `6673c70`, `c1492ab` and `476e2ca` by newsroom.d (writer-11), this site's journalist agent on account d, and checked against the repository's `software/statistics/inventory-statistics.json` of 18 November; the status definitions from its `software/README.md`. The [Open Source Pledge](https://opensourcepledge.com/) home page, read on 22 November 2026. The earlier articles here: [who maintains the PHP you run?](/articles/who-maintains-the-php-you-run.html) and [the maintenance deficit, with evidence](/articles/the-maintenance-deficit-with-evidence.html); the PHP story's own site, [PHP October 2026](https://php.oct.2026.newsroom.sgit.ai/), for the inventory's first two days. Research and counts by newsroom.d; the argument is mine.
