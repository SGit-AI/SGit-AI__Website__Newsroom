# Who maintains the PHP you run? A market failing both ways, the services and business models that should exist now, and why the money has to reach the people who know the code, sgit.ai

> php2shell asks every organisation that switched a website off one of two questions. Either the site does not matter, and it can stay off. Or it matters, there is a real cost to it being down, and somebody has to pay to keep it maintained. Today almost nobody is paying, and that is not because the money is missing; it is because the market is failing both ways. The organisations that run PHP have no maintenance of exactly what they run to buy. The people who know PHP best, its core developers and the people around its foundation, have no product to sell them: the foundation sells sponsorship tiers, and its packager for Debian and Ubuntu does it "mostly in my free time". When the flaws landed, the PHP security team wrote the fixes and published source backports for old versions for free, and vendors sold builds of those fixes within a day, with no stated share flowing back. One model shows it can be different: since 2024 the OpenJS Foundation has endorsed a vendor that shares 15% of its revenue with the projects it supports. So here are the services I think should exist now, starting with bringing the switched-off sites back, and the rules that would make the money flow to the people who maintain the code. This is not about leaving open source; it is about fixing its economics, for PHP first, then Node, Python and the rest.

*Source: <https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who maintains the PHP you run? A market failing both ways, the services and business models that should exist now, and why the money has to reach the people who know the code

# Who maintains the PHP you run? A market failing both ways, the services and business models that should exist now, and why the money has to reach the people who know the code

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-23 · [article v1.0.0](versions/who-maintains-the-php-you-run.md) · [newsroom v0.13.54](https://newsroom.sgit.ai/admin/versions.html) · open-sourcephp2shellbusiness-modelsmaintainerssovereigntyarticle

***Abstract:** php2shell asks every organisation that switched a website off one of two questions. Either the site does not matter, and it can stay off. Or it matters, there is a real cost to it being down, and somebody has to pay to keep it maintained. Today almost nobody is paying, and that is not because the money is missing; it is because the market is failing both ways. The organisations that run PHP have no maintenance of exactly what they run to buy. The people who know PHP best, its core developers and the people around its foundation, have no product to sell them: the foundation sells sponsorship tiers, and its packager for Debian and Ubuntu does it "mostly in my free time". When the flaws landed, the PHP security team wrote the fixes and published source backports for old versions for free, and vendors sold builds of those fixes within a day, with no stated share flowing back. One model shows it can be different: since 2024 the OpenJS Foundation has endorsed a vendor that shares 15% of its revenue with the projects it supports. So here are the services I think should exist now, starting with bringing the switched-off sites back, and the rules that would make the money flow to the people who maintain the code. This is not about leaving open source; it is about fixing its economics, for PHP first, then Node, Python and the rest.*

A market failing both ways: those who run open source budget for building and migrating and have no maintenance to buy; those in the middle, integrators, consultancies and platforms, win the contracts; those who know the code take donations and have no product to sell. The missing piece is a workflow for the first to buy maintenance from the last.

## In short

- **Two questions for every site switched off.** Does it matter? Then who pays to keep it maintained?
- **The market is failing both ways.** No maintenance to buy, no maintenance to sell.
- **The fix was written for free.** And sold within a day by vendors, with no stated share flowing back.
- **The best maintainers are the experts.** The workflow to hire them for what you run does not exist.
- **It can work.** OpenJS has had a 15% revenue-sharing partner since 2024.
- **Seven services should exist now.** Starting with bringing the switched-off sites back.
- **Not leaving open source.** Fixing its economics, for every ecosystem.

## Two questions

When the flaws in PHP landed on 21 October, organisations across Europe and beyond switched websites off as a precaution: government login services, councils, universities, wikis. In [the maintenance deficit, with evidence](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html) I followed Dion Wiggins' numbers on what governments spend on top of PHP against what they spend on PHP itself. Here I want to follow the other thread: what each of those organisations should be buying.

Every site that was switched off asks two questions. The first: does it matter? If it does not, it can stay off, and that is a decision worth making on purpose. If it does, there is a real cost to it being down, for real people, and the second question follows: who is paying to keep it maintained? The honest answer, for most of these sites, is nobody. They were built, launched and left. They went offline because nobody could say quickly whether they were safe, and nobody could say because nobody was paid to know.

That cost should be measured. I could not find a single estimate, from any named source, of what the php2shell shutdowns cost. The nearest comparison is Log4Shell: the US Cyber Safety Review Board reported that "one federal cabinet department reported dedicating 33,000 hours to Log4j vulnerability response", and that the responses "resulted in high costs and delayed other mission-critical work". Every organisation that switched a site off this week could count its own: hours offline, people who could not use the service, staff time spent on the response. That number is the budget the maintenance should have had.

## A market failing both ways

The money is not missing. The market is failing on both sides.

On one side are the people who run PHP in production. They budget for building, for migrating, for hosting. They have nowhere to buy the maintenance of exactly what they run: their version of PHP, their extensions, their CMS and its plugins, kept patched by people who know that code. So when something breaks, the safest thing they can do is switch it off.

On the other side are the people who know PHP best. The [PHP Foundation's sponsorship page](https://thephp.foundation/sponsor/) sells tiers from $12,000 a year: a logo on the website, mentions on social media and in the newsletter, an advisory board seat; $100,000 a year adds a co-authored case study. What it does not sell, on that page or its home page, is support, a maintained build, a custom build or a security service level. And [deb.sury.org](https://deb.sury.org/), how most Debian and Ubuntu servers get their PHP, says plainly: "The PHP packaging is time consuming and I do this mostly in my free time."

In between, the money that does move stops with the integrators, the consultancies and the platforms, who sell projects with contracts and phone numbers. Paying more of them, when none of that money reaches the people who maintain the code, is exactly what we should not do.

## What happened to the old versions

Who sold the fix for old PHP, and what flows back: the PHP security team published source backports for 7.4, 8.0 and 8.1 free; Zend by Perforce sold PHP LTS for 7.2 to 8.1 and is a Silver sponsor of the Foundation, with no revenue share stated; Canonical's Ubuntu Pro, TuxCare and HeroDevs sold subscriptions and are not shown as Foundation sponsors; Freexian sells PHP LTS for Debian with the packager's help.

This week shows the market half exists already. [php.net's advisory](https://www.php.net/) is clear that "PHP 8.1 and older no longer receive updates from the PHP project", and then: "Given the severity of these vulnerabilities, the PHP security team provided minimal source-backports for PHP 7.4, PHP 8.0, and PHP 8.1 to help people building from source or without access to an LTS vendor." Branches, not releases; free, for anyone who can build from source.

And the vendors sold ready-made builds of those fixes almost at once. [Zend by Perforce](https://www.zend.com/blog/php2shell-patches-now-available) published patched builds for PHP 7.2 to 8.1 alongside the upstream release, thanking "the PHP Ecosystem Security Team, the PHP Foundation, and release managers" for coordinating. Ubuntu lists fixes for the PHP in its older releases under Ubuntu Pro. TuxCare and HeroDevs sold the fix for end-of-life versions under their extended support. [Freexian](https://www.freexian.com/lts/php/) sells PHP long-term support for Debian, from €1,200 to €18,000 a year, "with the help of" the packager.

That is a market. It works, for the customers who can pay. What it does not do is pay the people who wrote the fix. Of these vendors, Zend is the only one shown among the Foundation's sponsors, at the $12,000 Silver tier; none of them states a share of its revenue going back to PHP. The patches were written by a small team, mostly funded by donations, and resold.

## It can work: the OpenJS model

There is a model that shows how. In May 2024 the OpenJS Foundation, home of Node.js and much of the JavaScript world, [announced an Ecosystem Sustainability Program](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner) with HeroDevs as the first partner. Partners sell commercial security fixes for end-of-life versions; they must be endorsed by the project's own core team; and HeroDevs is "contributing a 15% revenue share to all OpenJS Foundation projects participating in the program."

That is the shape I want for PHP: the people who maintain the code endorse who may sell its long-term maintenance, and a stated share of every sale flows back to them. Other models point the same way from different angles: Tidelift says it pays maintainers "income based on a number of factors, including customer usage"; the Open Source Pledge asks companies for $2,000 a year per developer they employ; GitHub Sponsors passes on 100% of personal sponsorships. None of them is yet the default way an organisation running PHP buys maintenance.

## Why the experts

Who is best placed to maintain a PHP deployment? The people who write PHP: its core developers, the people the Foundation hires, the companies directly connected to it. They know which fix is safe, which version can be back-ported, which extension is the risk. The problem is that the workflow does not exist. There is no route for a council, a ministry or a company to buy, from those people, the maintenance of the PHP it actually runs.

I have done this commercially, and I have seen what happens when it does exist. When the company that maintains a piece of software is directly connected to its source code, and is responsible for maintaining it at scale for many customers, it invests in exactly the things that make maintenance cheaper: the scalability of the process, the tooling for customised versions, the tests that make a back-port safe. That investment goes back into the code everyone uses. A consultancy that patches one site and moves on has no reason to make that investment, and no way to.

## The services that should exist now

The services that should exist now: bring it back; a maintained build; patch on behalf; remove what is not used; the dependency register; the incident desk; and the endorsed partner, with a stated share of revenue flowing to the foundation, the line procurement can require.

So here are the services I think should appear now, each sold to the people who run the code and delivered by, or with, the people who maintain it, with a stated share flowing upstream:

1. **Bring it back.** The market that exists this week: restore the sites switched off as a precaution. Map what each site can reach, cut what it does not need, patch, name the signals to watch, restore. That is the workflow in [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), priced per site.
2. **A maintained build.** PHP as the customer runs it: only the extensions they use, fixes back-ported to the versions they cannot leave yet, signed, on time, by people connected to the code.
3. **Patch on behalf.** The same for everything on top: the CMS, its modules and plugins, fixed and tested on the customer's own copy. Every piece of software people depend on should have someone paid to apply its fixes.
4. **Remove what is not used.** The most important question in any of these sites is why the code is there at all. PHP makes this easier than most: it is interpreted, so you can see which files and functions a site actually runs, and build PHP with only the extensions it needs. In [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html) a real tool went from 1,500 files to 428 for one use case. The cheapest patch is the code that is not there.
5. **The dependency register.** For each piece of software an organisation runs: how much it depends on it, how much it uses it, and how well it is maintained. The maintenance deficit ratio, per dependency. A risk the executive signs, knowingly.
6. **The incident desk.** An independent assessment in hours, from captured evidence, as the [PHP story's own site](https://php.oct.2026.newsroom.sgit.ai/) did in a day, so the next shutdown is a decision with a map.
7. **The endorsed partner.** Partners endorsed by the foundation that maintains the code, with a stated revenue share, as OpenJS does; and the line a procurement can require.

## Towards regulation

The path I would like to see is that this becomes easy first, and then required. Easy: the PHP Foundation, or any foundation, publishes how a company becomes an endorsed maintenance partner, and the share it pays; buyers can find one. Required: public procurement asks, for every open source dependency a contract relies on, who maintains it and how they are paid, with a maintainer line item in the budget, as Tiffany Farriss of the Drupal Association has proposed, according to Dion Wiggins; and regulation such as the EU's Cyber Resilience Act, which makes manufacturers answer for the open source in their products, recognises endorsed maintenance as a way to meet that duty.

## Not only PHP

PHP is the example this week. The same is true of Node, of Python, of every open source runtime and library that organisations run without paying for its upkeep. JavaScript has the first revenue-sharing model; Python's foundation has had a security developer-in-residence, supported by an OpenSSF security programme; most projects have neither. The questions are the same everywhere: what do we depend on, how much do we use it, who maintains it, and how are they paid?

This is not about moving away from open source. Open source is how we got here, and it is how sovereignty is possible at all. It is about fixing an economic model in which the value flows everywhere except to the people who keep the code safe. As I argued in [open source is not free](https://newsroom.sgit.ai/articles/open-source-is-not-free.html): somebody is always paying; the question is whether the people who get the value have an easy way to pay the people who create it.

## What this does not claim

- **The services are proposals.** Pieces exist: vendor LTS builds, and OpenJS's partner programme.
- **"Not shown as a sponsor" is about the Foundation's home page.** Companies may give in other ways not listed there.
- **No vendor states a revenue share to PHP.** That is not the same as none being paid.
- **Some vendor fix dates are not confirmed.** Notably TuxCare's for 8.0 and 8.1, and Ubuntu's for older releases.
- **No cost estimate for the shutdowns exists yet.** The Log4Shell figure is a comparison, not a measure.

## Where this comes from

My voice memo of 23 October 2026; a research pass on PHP's commercial support, checked against the sources: [php.net](https://www.php.net/)'s advisory of 21 October; the [PHP Foundation](https://thephp.foundation/) and its [sponsorship tiers](https://thephp.foundation/sponsor/); [Zend's post of 22 October](https://www.zend.com/blog/php2shell-patches-now-available); Ubuntu's security pages for CVE-2026-109618; TuxCare's and HeroDevs' php2shell posts; [Freexian's PHP LTS](https://www.freexian.com/lts/php/); [deb.sury.org](https://deb.sury.org/); the [OpenJS programme announcement](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner); Tidelift, the Open Source Pledge and GitHub Sponsors; and the [Cyber Safety Review Board's Log4j report](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf). Related: [the maintenance deficit, with evidence](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html), [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html), [the eyeballs get cheap](https://newsroom.sgit.ai/articles/the-eyeballs-get-cheap.html), [open source is not free](https://newsroom.sgit.ai/articles/open-source-is-not-free.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Startups & strategyNews & evidence[This article as a graph →](graphs.md#who-maintains-the-php-you-run)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 265 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=265)

**Posting this article on LinkedIn?** The cover is [who-maintains-the-php-you-run.jpg](banners/who-maintains-the-php-you-run.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html)*
