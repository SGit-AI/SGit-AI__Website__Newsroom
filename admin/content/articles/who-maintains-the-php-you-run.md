---
title: Who maintains the PHP you run? A version signed off by the people who maintain it, buyers who require that signature, and money that flows down the chain: a follow-up to the maintenance deficit
date: 2026-10-23
author: Dinis Cruz
author_url: about/index.html
summary: A follow-up to the maintenance deficit, with evidence, and this time with the solutions first. My proposal is simple to state. Every version of an open source platform that a product depends on should be signed off, cryptographically, by the people who maintain that platform, who help set it up, support it and patch it. Buyers, governments first, should refuse to buy products whose core pieces do not carry that signature. That creates a financial flow all the way down the chain, from the buyer to the product, to the platform, to the maintainers, and a commercial ecosystem of companies that provide the assurance, the maintenance and the ability to patch that php2shell showed we need. It is many small purchases, not one large one: the money spent maintaining the core pieces of an application should be in proportion to the money spent on that project, and it has to add value all the time, not sit there as insurance. And it scales now because of Gen AI, not because Gen AI writes the code, but because it helps people understand code bases, side effects and changes, so customised support can be sold at a price that makes sense. Today the market fails both ways: organisations running PHP have no maintenance of what they run to buy, and PHP's experts have no product to sell. When the flaws landed, the security team wrote the fixes for free and vendors resold them within a day. In Wardley's terms, the maintainers are the town planners: paid to read, maintain and sign off the code, pushing quality downstream, with their certification something insurers can price and regulators can require as a licence to operate. Here is the case I make on open-source.sgit.ai and at RiskMandate, the seven services that should exist now, and how they can be sold.
version: v0.13.57
license: https://creativecommons.org/licenses/by/4.0/
tags: open-source, php2shell, business-models, maintainers, sovereignty, article
status: published
---

> **A follow-up to [the maintenance deficit, with evidence](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html).** That article followed Dion Wiggins' numbers on what governments spend on top of PHP against what reaches PHP itself. This one takes the next step: what each organisation running PHP should be buying, the services that should exist now, and how the money reaches the people who know the code.

!shot mk-both-ways.webp | images/ | A market failing both ways: those who run open source, those in the middle, those who know the code, and a missing step. | concept

## In short: what I am proposing {#in-short}

- **A version signed off by the people who maintain it.** The maintainers of PHP sign, cryptographically, the builds they stand behind, and help set them up, support them and patch them.
- **The maintainers are the town planners.** Paid to read the code, maintain it and sign it off; they push quality downstream, and their certification is what insurers and regulators can rely on.
- **Buyers require the signature.** Governments and companies stop buying products whose core open source pieces do not carry it.
- **The money flows down the chain.** From the buyer to the product, to the platform, to the people who maintain what it depends on.
- **Many small purchases, in proportion.** Maintaining the core is a cost line in every project, sized to the project's own spend, and it adds value all the time. It is not insurance.
- **Gen AI makes it scale.** Not by writing the code, but by helping people understand code bases, side effects and changes, so customised support costs what it should.
- **No signature is a mapped risk.** We now have the data to map what each organisation depends on, and who maintains it.
- **Seven services, and a way to sell them.** Starting with bringing the switched-off sites back: paid to map, paid to engineer, retained to maintain.
- **Why it is needed.** The market fails both ways: no maintenance to buy, none to sell. This week the fix was written for free and resold within a day.

## The case I have been making {#the-case}

Before the PHP details, where I am coming from, because this article is an application of an argument I have been making for a while, and of a business I am building on it.

On [open-source.sgit.ai](https://open-source.sgit.ai/) I make the case that open source is a strategy, not a charity, and that its real value is in highly customised, maintainable and, in a way, smaller versions of the applications and packages people run. Most organisations use a fraction of what they install. As I put it there: "a company might only need 10% of them. So we create a version with only 10% of the features. It has much less attack surface, it is much cheaper to run". Customisation is not only addition, it is subtraction. And the people best placed to build and maintain those versions are the people who maintain the code: "A consultancy can study the package. The maintainer is the package." What is missing today is the connection between them and the people who use the software: "The relationship is missing because the platform is missing."

At [RiskMandate](https://riskmandate.ai), the company I co-founded, we are turning that into a commercial model: every customer version is built on the open-source base, the customer decides what stays private, and the revenue comes from the work customers ask us to own, mapping, engineering and above all maintaining, not from access to closed code. So I have a commercial interest in what follows, and I would rather say so up front.

php2shell is that argument with the market already in place. The PHP story's source watch tracks 295 sites that somebody named as taken offline this week, each run by an organisation that has just discovered, in the worst way, that it runs software nobody is maintaining for it. The need for these services is not hypothetical; it is the list of sites switched off this week. What has to be managed and mapped is that direct connection: who maintains each piece of what an organisation runs, and how they are paid.

## A version signed off by the people who maintain it {#signed-off}

!shot mk-signed-chain.webp | images/ | The signature chain that makes the money flow: signed-off versions go up to maintainers, money comes down. | concept

This is the idea I think makes the rest work. A version of an open source platform, the one a product actually ships with, should be signed off by the key authors of that technology. Not a logo, not a sponsorship: a cryptographic signature on a specific build, saying the people who maintain this code know this version, stand behind it for this use, and will help maintain it and patch it when something like php2shell lands. Those maintainers are involved in the set-up and the maintainability of the application built on top, and they provide a level of support for it.

The pieces already exist. PHP's release managers have signed the project's release tags in Git since April 2012, so the source can already be proven to come from them. What does not exist is the next step: a signature on the version a customer runs, from the people who know the code, with a commercial relationship behind it.

Then comes the part that turns it into a market. Governments first, and then any organisation that buys software, should say: we will not buy your product unless its core platforms are signed off by the people who maintain them. That single procurement line creates a financial flow all the way down. The supplier of a council's portal pays for the sign-off of the CMS it builds on; the CMS's maintainers pay for, or provide, the sign-off of the PHP underneath. And it creates a commercial ecosystem for the companies that provide that assurance, that signature, that maintenance, and the ability to patch quickly that we needed this week.

## The maintainers are the town planners {#town-planners}

In the language I used for [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), there are three kinds of work on any piece of software. Explorers build by talking to an agent, and what they build is the brief. Villagers maintain what other people have started to depend on. Town planners own the code in production. PHP, the runtime under a large share of the web, is about as far towards commodity as software gets, and the people who maintain it are its town planners. That is the role they should be paid for: to read the code, to maintain it, and to sign it off.

Signing off is already how the most mature projects work. The Linux kernel's [rules for AI coding assistants](https://docs.kernel.org/process/coding-assistants.html) say "AI agents MUST NOT add Signed-off-by tags" and "Only humans can legally certify the Developer Certificate of Origin". A signature means a person has read it and answers for it. What I am proposing extends that from the code a project accepts to the versions its users run.

Because they sign, town planners will have no patience for what they do not support, and that is a feature. It pushes quality downstream. If a product does too much that is unsafe on top of PHP, an unsupported extension, a private fork nobody can patch, a version left far behind, the people who maintain PHP will not sign it off, and the buyer of that product will see that they did not.

That signature also connects to insurance. A certified application is a risk an insurer can price: the people who know the platform have said what they stand behind. An uncertified one is on its own. And for the services that matter most, a government login, a bank's portal, a hospital's records, it becomes a question of a licence to operate: should a service like that run on a platform nobody who maintains it has signed off? That is where regulators can come in, and where the money becomes non-negotiable.

## Why it scales now {#gen-ai}

First, the caveat: this is not about Gen AI magically writing all the code, or Gen AI as a massive thing in the middle. The maintainers still read the code; that is the point of their signature. What Gen AI changes is everything around it. It helps people understand code bases, the side effects of a change, the architecture and the changes between versions. It scales the non-functional work: the maintenance, the support, the testing, the documentation, the explanation of what a patch does to a particular customer's version. That is what makes mass-customised support possible at a price that makes sense, and that is what was missing. Before, signing off thousands of customer versions would have needed thousands of experts. Now the right experts can cover far more of them, with the tools doing much of the reading and checking around them.

## Many small purchases, in proportion {#proportional}

This is not about charging a large amount for one thing. It is about lots and lots of small purchases, aligned with the money each organisation already spends. The amount spent maintaining the core pieces of software an application depends on should be in direct proportion to the money spent on, and available in, that project. A €100,000 site and a €10 million programme should both carry a maintenance line for their platform, sized accordingly.

And it has to add value all the time. If it is seen as insurance, it is the first thing cut. It should show up as patches applied, versions kept current, code removed, questions answered, set-ups reviewed, every month. Maintaining the core platforms has to become a cost item in every project; when it is not there, that should be visible as a risk. That is a place where we now have data: for PHP alone, the Dutch NCSC's inventory lists 751 products that ship or depend on it, and the PHP story's source watch tracks 295 sites named as switched off. The same mapping can show, for any organisation, what it depends on, how much it uses, and whether anyone is maintaining it.

## Two questions {#two-questions}

When the flaws in PHP landed on 21 October, organisations across Europe and beyond switched websites off as a precaution: government login services, councils, universities, wikis. In the article this one follows, I followed Dion Wiggins' numbers on what governments spend on top of PHP against what they spend on PHP itself. Here I follow the other thread: what each of those organisations should be buying.

Every site that was switched off asks two questions. The first: does it matter? If it does not, it can stay off, and that is a decision worth making on purpose. If it does, there is a real cost to it being down, for real people, and the second question follows: who is paying to keep it maintained? The honest answer, for most of these sites, is nobody. They were built, launched and left. They went offline because nobody could say quickly whether they were safe, and nobody could say because nobody was paid to know.

That cost should be measured. I could not find a single estimate, from any named source, of what the php2shell shutdowns cost. The nearest comparison is Log4Shell: the US Cyber Safety Review Board reported that "one federal cabinet department reported dedicating 33,000 hours to Log4j vulnerability response", and that the responses "resulted in high costs and delayed other mission-critical work". Every organisation that switched a site off this week could count its own: hours offline, people who could not use the service, staff time spent on the response. That number is the budget the maintenance should have had.

## A market failing both ways {#both-ways}

The money is not missing. The market is failing on both sides.

On one side are the people who run PHP in production. They budget for building, for migrating, for hosting. They have nowhere to buy the maintenance of exactly what they run: their version of PHP, their extensions, their CMS and its plugins, kept patched by people who know that code. So when something breaks, the safest thing they can do is switch it off.

On the other side are the people who know PHP best. The [PHP Foundation's sponsorship page](https://thephp.foundation/sponsor/) sells tiers from $12,000 a year: a logo on the website, mentions on social media and in the newsletter, an advisory board seat; $100,000 a year adds a co-authored case study. What it does not sell, on that page or its home page, is support, a maintained build, a custom build or a security service level. And [deb.sury.org](https://deb.sury.org/), how most Debian and Ubuntu servers get their PHP, says plainly: "The PHP packaging is time consuming and I do this mostly in my free time."

In between, the money that does move stops with the integrators, the consultancies and the platforms, who sell projects with contracts and phone numbers. Paying more of them, when none of that money reaches the people who maintain the code, is exactly what we should not do.

## What happened to the old versions {#old-versions}

!shot mk-vendors.webp | images/ | Who sold the fix for old PHP, and what flows back to the PHP Foundation, from the PHP security team to Freexian. | comparison

This week shows the market half exists already. [php.net's advisory](https://www.php.net/) is clear that "PHP 8.1 and older no longer receive updates from the PHP project", and then: "Given the severity of these vulnerabilities, the PHP security team provided minimal source-backports for PHP 7.4, PHP 8.0, and PHP 8.1 to help people building from source or without access to an LTS vendor." Branches, not releases; free, for anyone who can build from source.

And the vendors sold ready-made builds of those fixes almost at once. [Zend by Perforce](https://www.zend.com/blog/php2shell-patches-now-available) published patched builds for PHP 7.2 to 8.1 alongside the upstream release, thanking "the PHP Ecosystem Security Team, the PHP Foundation, and release managers" for coordinating. Ubuntu lists fixes for the PHP in its older releases under Ubuntu Pro. TuxCare and HeroDevs sold the fix for end-of-life versions under their extended support. [Freexian](https://www.freexian.com/lts/php/) sells PHP long-term support for Debian, from €1,200 to €18,000 a year, "with the help of" the packager.

That is a market. It works, for the customers who can pay. What it does not do is pay the people who wrote the fix. Of these vendors, Zend is the only one shown among the Foundation's sponsors, at the $12,000 Silver tier; none of them states a share of its revenue going back to PHP. The patches were written by a small team, mostly funded by donations, and resold.

## The best that exists today {#openjs}

The closest thing to a working model today is in JavaScript. In May 2024 the OpenJS Foundation, home of Node.js and much of the JavaScript world, [announced an Ecosystem Sustainability Program](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner) with HeroDevs as the first partner. Partners sell commercial security fixes for end-of-life versions; they must be endorsed by the project's own core team; and HeroDevs is "contributing a 15% revenue share to all OpenJS Foundation projects participating in the program."

It is the best that can happen right now, and it is not what I think should happen. The maintainers stay at one remove: a vendor sells the fixes and the project receives a share. What I am proposing is more direct: a commercial decision by everyone who depends on the code, with the maintainers' own signature on the version they support. Other models point the same way from different angles: Tidelift says it pays maintainers "income based on a number of factors, including customer usage"; the Open Source Pledge asks companies for $2,000 a year per developer they employ; GitHub Sponsors passes on 100% of personal sponsorships. None of them is yet the default way an organisation running PHP buys maintenance.

## Why the experts {#experts}

Who is best placed to maintain a PHP deployment? The people who write PHP: its core developers, the people the Foundation hires, the companies directly connected to it. They know which fix is safe, which version can be back-ported, which extension is the risk. The problem is that the workflow does not exist. There is no route for a council, a ministry or a company to buy, from those people, the maintenance of the PHP it actually runs.

I have done this commercially, and I am doing it again at RiskMandate; I have seen what happens when it does exist. When the company that maintains a piece of software is directly connected to its source code, and is responsible for maintaining it at scale for many customers, it invests in exactly the things that make maintenance cheaper: the scalability of the process, the tooling for customised versions, the tests that make a back-port safe. That investment goes back into the code everyone uses. A consultancy that patches one site and moves on has no reason to make that investment, and no way to.

## The services that should exist now {#services}

!shot mk-services.webp | images/ | The services that should exist now, from bringing it back to the endorsed partner, and the foundation's share. | comparison

So here are the services I think should appear now, each sold to the people who run the code and delivered by, or with, the people who maintain it, with a stated share flowing upstream:

1. **Bring it back.** The market that exists this week: restore the sites switched off as a precaution. Map what each site can reach, cut what it does not need, patch, name the signals to watch, restore. That is the workflow in [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), priced per site.
2. **A maintained build.** PHP as the customer runs it: only the extensions they use, fixes back-ported to the versions they cannot leave yet, signed, on time, by people connected to the code.
3. **Patch on behalf.** The same for everything on top: the CMS, its modules and plugins, fixed and tested on the customer's own copy. Every piece of software people depend on should have someone paid to apply its fixes.
4. **Remove what is not used.** The most important question in any of these sites is why the code is there at all. PHP makes this easier than most: it is interpreted, so you can see which files and functions a site actually runs, and build PHP with only the extensions it needs. In [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html) a real tool went from 1,500 files to 428 for one use case. The cheapest patch is the code that is not there.
5. **The dependency register.** For each piece of software an organisation runs: how much it depends on it, how much it uses it, and how well it is maintained. The maintenance deficit ratio, per dependency. A risk the executive signs, knowingly.
6. **The incident desk.** An independent assessment in hours, from captured evidence, as the [PHP story's own site](https://php.oct.2026.newsroom.sgit.ai/) did in a day, so the next shutdown is a decision with a map.
7. **The signed-off version.** A build signed by the people who maintain the code, with their involvement in its set-up and support, and a stated share of every sale flowing to them; the line a procurement can require.

## How we are thinking of selling it {#selling}

!shot mk-options.webp | images/ | Ways to make money selling open source software, as RiskMandate is mapping them: from paid mapping to maintenance. | concept

Here is how we are mapping the ways to make money selling open source software at RiskMandate, in the words of our current proposal. They are directly applicable here, and they are still proposals, not proven revenue.

- **Paid to map.** One workflow, one accountable owner, what the system can actually reach against what the business approved, the gap, the control options and a decision. For a switched-off PHP site: what does it run, what does it reach, what does it need, and what would make it safe to bring back. Proposed as a bounded engagement (£5,000 in the current proposal).
- **Paid to engineer.** Deeper mapping, implementation design, integration or a proof of concept, acceptance tests and a handover (£25,000 in the current proposal).
- **A scoped custom version.** Built on the open-source base, with private adapters and configuration, deployment hardening and a supported release. For PHP, this is the smaller build: only the extensions and code the site uses.
- **Retained to maintain.** Compatibility, change review, regression tests, evidence refresh, response and continuity. Priced by what is at stake: standard (supported releases, quarterly review, dependency compatibility), operational (monthly change review, a regression suite, an incident response target), and critical (reserved capacity, rapid response, a continuity drill, current evidence).
- **Small public products** as a lightweight on-ramp, from £10 to £1,500.

What ties these options together is simple. Nobody pays for access to the code: it is all open. What a customer pays for is work: understanding what they run, changing it to fit, and keeping it maintained. That is the opposite of the usual software model, where the code is locked away and you pay for a licence to use it. Here the code is free, and the commitment is what you buy. The price follows how much is at stake: a council's citizen login and a university's archive wiki both run PHP, but they should not buy the same maintenance, and today neither can buy any. Over time the maintenance can be worth more than the first project, as long as the work it takes is measured and priced. And the smaller and less unusual a customer's version is, the easier it is to maintain, check, replace and hand over; where the customer allows it, the improvements made for them go back into the open code everyone uses. That is how paying for the maintenance of one organisation's version also improves the code for everyone else.

## Towards regulation {#regulation}

The path I would like to see is that this becomes easy first, and then required. Easy: the PHP Foundation, or any foundation, publishes how a company becomes an endorsed maintenance partner, and the share it pays; buyers can find one. Required: public procurement asks, for every open source dependency a contract relies on, whether its version is signed off by the people who maintain it, who maintains it and how they are paid, with a maintainer line item in the budget, as Tiffany Farriss of the Drupal Association has proposed, according to Dion Wiggins; and regulation such as the EU's Cyber Resilience Act, which makes manufacturers answer for the open source in their products, recognises endorsed maintenance as a way to meet that duty.

## Not only PHP {#beyond}

PHP is the example this week. The same is true of Node, of Python, of every open source runtime and library that organisations run without paying for its upkeep. JavaScript has the first revenue-sharing model; Python's foundation has had a security developer-in-residence, supported by an OpenSSF security programme; most projects have neither. The questions are the same everywhere: what do we depend on, how much do we use it, who maintains it, and how are they paid?

This is not about moving away from open source. Open source is how we got here, and it is how sovereignty is possible at all. It is about fixing an economic model in which the value flows everywhere except to the people who keep the code safe. As I argued in [open source is not free](https://newsroom.sgit.ai/articles/open-source-is-not-free.html): somebody is always paying; the question is whether the people who get the value have an easy way to pay the people who create it.

## What this does not claim {#limits}

- **The services are proposals.** Pieces exist: vendor LTS builds, and OpenJS's partner programme.
- **The signed-off version is a proposal.** Signed release tags exist; I found no offer of signed customer versions with the maintainers' support behind them.
- **Gen AI scales the work around the code.** It does not replace the maintainers reading it.
- **Insurance and a licence to operate are proposed links.** They describe what could follow, not what insurers or regulators require today.
- **RiskMandate's options are a proposal too.** The prices are anchors in a current proposal, not published pricing (the public site lists £10 to £1,500), and the commercial proof is still being built.
- **I have a commercial interest.** RiskMandate sells this kind of work.
- **"Not shown as a sponsor" is about the Foundation's home page.** Companies may give in other ways not listed there.
- **No vendor states a revenue share to PHP.** That is not the same as none being paid.
- **Some vendor fix dates are not confirmed.** Notably TuxCare's for 8.0 and 8.1, and Ubuntu's for older releases.
- **No cost estimate for the shutdowns exists yet.** The Log4Shell figure is a comparison, not a measure.

## Where this comes from {#sources}

My voice memo of 23 October 2026; a research pass on PHP's commercial support, checked against the sources: [php.net](https://www.php.net/)'s advisory of 21 October; the [PHP Foundation](https://thephp.foundation/) and its [sponsorship tiers](https://thephp.foundation/sponsor/); [Zend's post of 22 October](https://www.zend.com/blog/php2shell-patches-now-available); Ubuntu's security pages for CVE-2026-109618; TuxCare's and HeroDevs' php2shell posts; [Freexian's PHP LTS](https://www.freexian.com/lts/php/); [deb.sury.org](https://deb.sury.org/); the [OpenJS programme announcement](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner); Tidelift, the Open Source Pledge and GitHub Sponsors; [open-source.sgit.ai](https://open-source.sgit.ai/)'s pages on [open core or packaging](https://open-source.sgit.ai/views/open-core.html), [funding](https://open-source.sgit.ai/funding/index.html) and [somebody has to be the villagers](https://open-source.sgit.ai/views/villagers.html); RiskMandate's current commercial proposal (October 2026); and the [Cyber Safety Review Board's Log4j report](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf). Related: [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [software vendors as villagers](https://newsroom.sgit.ai/articles/software-vendors-as-villagers.html), [the maintenance deficit, with evidence](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html), [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html), [the eyeballs get cheap](https://newsroom.sgit.ai/articles/the-eyeballs-get-cheap.html), [open source is not free](https://newsroom.sgit.ai/articles/open-source-is-not-free.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
