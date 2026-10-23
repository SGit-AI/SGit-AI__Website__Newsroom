# The maintenance deficit, with evidence: a follow-up to Dion Wiggins on why open source's business model fails the people who maintain it, checked against the PHP story's own data, sgit.ai

> Dion Wiggins has written the piece I wish I had written about php2shell. He puts a number on something I have been arguing for months: Germany spends about €27 million a year on its federal website platform, built on PHP, and contributed about €112,000 a year to PHP's security, a maintenance deficit ratio of 241 to 1. Then he walks the same gap through the rest of the stack governments are migrating onto. This is a follow-up with our evidence. I checked his main figures against their primary sources: the order of magnitude holds under every cut, from 179 to 263 to 1, and a few details differ, which I list. I add what our evidence vault and the PHP story's site show two days on: 751 downstream products in the Dutch inventory, only 109 of them fixed; no named organisation saying it was compromised through these flaws, and the US catalogue of exploited flaws still not listing them; and an independent assessment of the incident, built in a day by a team of agents. Then the argument: this is not a story about generosity. Open source's business model pays the integrator, the host and the platform, and almost never the maintainer or the packager, and AI has just made the discoverers richer than the people who have to fix what they find. The money exists; what is missing is a model that pays for maintenance as the product.

*Source: <https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The maintenance deficit, with evidence: a follow-up to Dion Wiggins on why open source's business model fails the people who maintain it, checked against the PHP story's own data

# The maintenance deficit, with evidence: a follow-up to Dion Wiggins on why open source's business model fails the people who maintain it, checked against the PHP story's own data

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-23 · [article v1.0.0](versions/the-maintenance-deficit-with-evidence.md) · [newsroom v0.13.52](https://newsroom.sgit.ai/admin/versions.html) · php2shellopen-sourcesovereigntyfundingmaintainersarticle

***Abstract:** Dion Wiggins has written the piece I wish I had written about php2shell. He puts a number on something I have been arguing for months: Germany spends about €27 million a year on its federal website platform, built on PHP, and contributed about €112,000 a year to PHP's security, a maintenance deficit ratio of 241 to 1. Then he walks the same gap through the rest of the stack governments are migrating onto. This is a follow-up with our evidence. I checked his main figures against their primary sources: the order of magnitude holds under every cut, from 179 to 263 to 1, and a few details differ, which I list. I add what our evidence vault and the PHP story's site show two days on: 751 downstream products in the Dutch inventory, only 109 of them fixed; no named organisation saying it was compromised through these flaws, and the US catalogue of exploited flaws still not listing them; and an independent assessment of the incident, built in a day by a team of agents. Then the argument: this is not a story about generosity. Open source's business model pays the integrator, the host and the platform, and almost never the maintainer or the packager, and AI has just made the discoverers richer than the people who have to fix what they find. The money exists; what is missing is a model that pays for maintenance as the product.*

"Built on volunteers: €108 million for the building, €112,000 for the foundation." Dion Wiggins' illustration for his article: a building labelled Digital Sovereignty, lifted by a crane carrying the €108 million contract, resting on a cracked column of PHP, OpenSSL, curl, FFmpeg, libxml2, core-js and pgBackRest, held up by volunteers, beside a jar of $730,534 from 536 donors and a sign saying 11 part-time engineers on duty, while an official with binoculars holds a €2 billion, seven-year sovereignty package. Reused from his public post, with credit.

## In short

- **Dion Wiggins measured the gap.** A maintenance deficit ratio: 241 to 1, for Germany and PHP.
- **The number holds.** Every cut of the sources gives two orders of magnitude.
- **Two days on, most downstream software is not fixed.** 109 of 751 rows in the Dutch inventory.
- **No named compromise yet.** The shutdowns were decisions under uncertainty.
- **An independent assessment took a day.** Built by agents, from an evidence vault anyone can read.
- **The business model pays the wrong layer.** Integrators and hosts, not maintainers and packagers.
- **AI made finding cheap and fixing scarce.** The discoverer now has more resources than the maintainer.

## The piece

Dion Wiggins published [a post](https://lnkd.in/p/eYFQfRRn) and [a long-form article](https://www.linkedin.com/pulse/maintenance-deficit-governments-building-digital-nobody-dion-wiggins-zv7pf/) on 23 October that I think everyone working on digital sovereignty should read. His metric is simple: divide what a government spends migrating onto open source by what it contributes to maintaining that open source. For Germany and PHP he gets €27 million a year against €112,000 a year: 241 to 1. His line for it: "Any government whose ratio exceeds 10:1 does not have a sovereignty strategy. It has a procurement preference with no supply chain behind it."

He then walks the rest of the stack: LibreOffice, Nextcloud, FFmpeg, curl, OpenSSL, Kubernetes Ingress-NGINX, pgBackRest, libxml2, core-js, each with a funding gap, a staffing gap, or both. And he points at a post the PHP Foundation published seven weeks before php2shell, ["Digital Sovereignty Is Written in PHP"](https://thephp.foundation/blog/2026/09/02/digital-sovereignty-is-written-in-php), whose author, Sebastian Bergmann, named the problem in advance: "the institutions most dependent on PHP have no established mechanism" to turn that dependency into maintenance funding.

This is very much what we have been talking about here, with numbers attached. So this is a follow-up, with the evidence we have.

## The numbers, checked

The maintenance deficit ratio, checked: with Dion Wiggins' figures, 241 to 1; with the whole contract and the Sovereign Tech Agency's own page, 263 to 1; with the migration share alone, 179 to 1. Two orders of magnitude in every case.

I checked the main figures against their primary sources on 23 October:

- **The contract.** €108 million over four years, from Bergmann's post. Of that, €73.2 million is migration and relaunch, €26.88 million product development and support, and €8 million operations. So €27 million a year is the whole contract, and the migration alone is about €18.3 million a year.
- **The investment in PHP.** The Sovereign Tech Agency's [own page for PHP](https://www.sovereign.tech/tech/php) lists €205,000, for 2023 and 2024: an extension distribution overhaul, a security audit, documentation and a testing tool. Dion's €112,000 a year comes from a figure of about €223,000 for 2025 and 2026. Either way, about €100,000 a year.
- **The ratio.** 241 to 1 on his figures, 263 to 1 on the agency's page, 179 to 1 on the migration share alone. Two orders of magnitude, however you cut it.
- **The PHP Foundation.** Its [report for 2025](https://thephp.foundation/blog/2026/05/27/impact-and-transparency-report-2025/): $730,534 donated by 536 organisations and individuals, expenses of $784,376, a deficit of about $139,000 taken on purpose, and "11 contracted developers who worked part- and full-time". Bergmann's post gives thirteen by September.
- **The shutdowns.** The PHP story's [impact ledger](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) records them on 21 October, as Dion says. Two details are narrower than his summary: Finland's Valtori restricted incoming public traffic from 12:45 local time, as a precaution, with internal networks unaffected; and the UK figure is a minister saying that 32 central government services were unavailable and four partially, at one moment, which the site's fact-check desk keeps as an open question.
- **UK councils.** Bergmann counts "over 58 councils" sharing LocalGov Drupal; Dion has Drupal at 100 councils. Possibly different measures; I could not reconcile them.
- **Not checked.** The 50,000 warnings, DigiD's 17 million users, Datadog's 3.10 seconds, and Sansec's update of 22 October, which I could not find.

None of that changes the argument. It sharpens it: the migration share alone is nearly 180 times the investment in the language underneath it.

## Two days on, from our evidence

The Dutch NCSC's inventory of software that ships or depends on PHP: on 22 October at 15:28 UTC, 724 rows, 61 fixed, 216 vulnerable, 440 under investigation; on 23 October at 12:50 UTC, 751 rows, 109 fixed, 222 vulnerable, 389 under investigation, 30 not affected.

Dion writes that "every government in every country waited for the same patch from the same" small team. The patch itself came fast: PHP's four fixed releases were all out by 21 October. What followed is the part his article calls the packaging and distribution layer, and our data shows how slow that layer is.

The Dutch national cyber security centre keeps a [public inventory](https://github.com/NCSC-NL/php2shell) of software that ships or depends on PHP. Read from its history, at 12:50 UTC today, about two days after the fix, it has 751 rows: 109 fixed, 222 vulnerable, 389 still under investigation, 30 not affected. That is 15% fixed. The patch was the easy part. Getting it through every vendor, distribution and appliance is where the time goes, and that work belongs to nobody in particular.

And the risk itself? The PHP story's [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html), as of 20:50 UTC on 22 October, lays out 33 statements behind one claim: no named organisation has said it was compromised through php2shell. Millions of attempts; three vendors reporting exploitation without naming a victim; one university saying an attack was stopped. At 14:41 UTC today, the US catalogue of known exploited vulnerabilities still did not list either flaw. As I wrote in [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), that silence lowers the likelihood; it does nothing to the blast radius. The shutdowns were decisions under uncertainty, made without a map of what each site could reach.

## An assessment in a day

Dion makes a point I want to take one step further: no government had "the independent capability" to assess the flaw before shutting down its services. That was true on 21 October. It no longer needs to be.

The [PHP story's own site](https://php.oct.2026.newsroom.sgit.ai/), as I described in [PHP October 2026, at 8pm](https://newsroom.sgit.ai/articles/php-october-at-8pm.html), was built in one day by two people and a team of agents, from an [evidence vault anyone can read](https://newsroom.sgit.ai/articles/a-desk-anyone-can-open.html): 184 sources and 177 dated captures, 70 claims graded by a fact-check desk, the fix read in PHP's own code, the inventory hour by hour, the compromise map. None of it needed the PHP Foundation's time. That is the kind of independent assessment a government could commission, or run itself, in the first hours of the next incident. The capacity to understand an incident has become cheap. The capacity to fix the code has not.

## Why this is a business model failure

Where the money flows: Germany's €108 million contract over four years, Acquia sold for $1 billion, Automattic's reported revenue of over $700 million in 2024, the EU's €2 billion seven-year open source strategy and its €264 billion a year on proprietary IT; against the PHP Foundation's $730,534 from 536 donors, 11 to 13 developers, one security engineer for six months, €205,000 from the Sovereign Tech Agency, and one person packaging PHP for Debian and Ubuntu.

I want to be careful about the framing. This is not a story about governments or companies being mean. It is a business model that pays the wrong layer.

Look at where the money in Dion's article goes. The integrator wins a €108 million contract to build on TYPO3. The platform company is sold for a billion. The host charges every month. All of them sell something a customer can buy: a project, a product, a service with a contract and a phone number. The maintainer of the language underneath, and the person who packages it for most Debian and Ubuntu servers, sell nothing a procurement process can buy. They take donations. That is not a funding gap; it is a missing product.

And AI has just made the imbalance worse. In [the eyeballs get cheap](https://newsroom.sgit.ai/articles/the-eyeballs-get-cheap.html) I argued that models make deep security review abundant for open source, which is good news. php2shell shows the other side. As Dion describes it, the flaws had been glimpsed by two audits that could not exploit them; two teams with frontier models turned them into working exploits within days. Dion's line for FFmpeg applies to all of it: "The discoverer had more resources than the maintainer." Finding is now cheap and well funded; deciding, fixing, back-porting and packaging are not. In the Foundation's own words after the incident, quoted by Dion, the delay was "a structural failure" of its decision process and its resources.

## What would work

Three ideas, which fit together.

**Pay for maintenance as the product.** In [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html) I argued that the specialist who knows a component best should be paid to maintain the version their customers actually run: the smallest one that does the job, with its behaviour, decision and workflow policies. That is something a procurement process can buy, because it has a scope, an owner and a service level. Tiffany Farriss's proposal, which Dion cites, of a maintainer line item in public contracts is the obvious way to buy it: 1% of the German contract is more than the PHP Foundation's whole year.

**Pay at the source.** In [free to copy, paid at the source](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html) I argued that open code can be free to copy and still paid for where it is trusted: the official source, reviewed and signed. A patched PHP build from the people who maintain it, signed and on time, is worth paying for, per server or per use, even though anyone may rebuild it.

**Measure it, everywhere.** Dion's ratio should be on every sovereignty plan, and the same idea works inside companies: what you spend on what you build on top, against what you spend on what you build on. And with the method in [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), every organisation can know, before the next incident, what each of its sites can reach and what it would lose, so the next shutdown is a decision with a map rather than a reflex.

The money exists, as Dion shows. What is missing is a product that lets it reach the people doing the maintenance.

## What this does not claim

- **The ratios are illustrative.** Contracts and grants cover different periods and scopes.
- **Some of Dion's figures I have not checked.** Listed above; they are his, with his sources.
- **The inventory counts rows, not servers.** And "under investigation" means nobody has said.
- **The compromise map is a time-bounded absence.** As of 20:50 UTC on 22 October; one statement would end it.
- **The proposals are mine.** Not Dion's, though his article points the same way.

## Where this comes from

Dion Wiggins' [post](https://lnkd.in/p/eYFQfRRn) and [article](https://www.linkedin.com/pulse/maintenance-deficit-governments-building-digital-nobody-dion-wiggins-zv7pf/) of 23 October 2026, and his illustration, reused from his public post with credit; Sebastian Bergmann's ["Digital Sovereignty Is Written in PHP"](https://thephp.foundation/blog/2026/09/02/digital-sovereignty-is-written-in-php); the PHP Foundation's [report for 2025](https://thephp.foundation/blog/2026/05/27/impact-and-transparency-report-2025/); the Sovereign Tech Agency's [page for PHP](https://www.sovereign.tech/tech/php); Materna's press release of 22 May 2025; the NCSC-NL inventory at 2fdc314, parsed with the PHP story site's own tool; CISA's catalogue feed, read at 14:41 UTC on 23 October; and the [PHP story's site](https://php.oct.2026.newsroom.sgit.ai/) at v0.10.3. Related: [the eyeballs get cheap](https://newsroom.sgit.ai/articles/the-eyeballs-get-cheap.html), [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html), [free to copy, paid at the source](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html), [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), [PHP October 2026, at 8pm](https://newsroom.sgit.ai/articles/php-october-at-8pm.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Startups & strategyNews & evidence[This article as a graph →](graphs.md#the-maintenance-deficit-with-evidence)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 264 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=264)

**Posting this article on LinkedIn?** The cover is [the-maintenance-deficit-with-evidence.jpg](banners/the-maintenance-deficit-with-evidence.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html)*
