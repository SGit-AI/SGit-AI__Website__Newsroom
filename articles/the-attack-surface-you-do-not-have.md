# The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed, sgit.ai

> Every time I see a CVE now, I smile, because it is one less thing to worry about. My server-side attack surface is very small: fundamentally, the SG/Send upload server, and that only ever stores encrypted data. Today two critical PHP vulnerabilities were released, unauthenticated remote code execution in every supported PHP branch. In the month before, CISA's catalogue of exploited vulnerabilities filled with VPN gateways, mail gateways, firewalls, media servers and a help desk, and WordPress shipped a critical fix. None of it runs in my stack. That is the result of a constraint I have been writing about for months: no database, then no back end, everything that can run in the browser running there. It is good engineering, and it is not a limitation. It is giving me speed: 45 static sites in eleven weeks, a newsroom that can take payments, 100+ users and customers, a key register, and accounts and an AWS twin on the way, with nothing to provision or patch. Internal applications are where the risk is going, because they are rarely tested like public ones. The question to ask of every component is the one this article ends with: why does this need to be on the server?

*Source: <https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed

# The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.1.0, 2 versions](versions/the-attack-surface-you-do-not-have.md) · [newsroom v0.13.24](https://newsroom.sgit.ai/admin/versions.html) · securityarchitectureclient-sideattack-surfacearticle

***Abstract:** Every time I see a CVE now, I smile, because it is one less thing to worry about. My server-side attack surface is very small: fundamentally, the SG/Send upload server, and that only ever stores encrypted data. Today two critical PHP vulnerabilities were released, unauthenticated remote code execution in every supported PHP branch. In the month before, CISA's catalogue of exploited vulnerabilities filled with VPN gateways, mail gateways, firewalls, media servers and a help desk, and WordPress shipped a critical fix. None of it runs in my stack. That is the result of a constraint I have been writing about for months: no database, then no back end, everything that can run in the browser running there. It is good engineering, and it is not a limitation. It is giving me speed: 45 static sites in eleven weeks, a newsroom that can take payments, 100+ users and customers, a key register, and accounts and an AWS twin on the way, with nothing to provision or patch. Internal applications are where the risk is going, because they are rarely tested like public ones. The question to ask of every component is the one this article ends with: why does this need to be on the server?*

A month of critical vulnerabilities in server software, from 22 September to 21 October 2026: PHP, Plex Media Server, SiteGuard, Palo Alto PAN-OS, Cisco Secure Email Gateway, Ahsay, Ivanti Connect Secure, Zammad, Fortinet FortiMail, Citrix NetScaler and WordPress. My exposure to each: none.

## In short

- **Every CVE now makes me smile.** One less thing I have to worry about.
- **My server-side attack surface is very small.** The SG/Send upload server, which stores only ciphertext.
- **A month of critical server flaws passed me by.** PHP today; gateways, firewalls and WordPress before it.
- **It came from a constraint.** No database, then no back end; everything possible in the browser.
- **The constraint is speed, not a limit.** Nothing to provision, patch or keep running.
- **Internal apps are where the risk is going.** They are rarely tested like public ones.
- **Ask of every component: why the server?**

## Today, PHP

Today a message in one of my groups flagged two critical PHP vulnerabilities, with the patches due that afternoon. They arrived on time. php.net's advisory says PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 "fix two critical vulnerabilities that can allow unauthenticated remote code execution", CVE-2026-109618 and CVE-2026-109619, and that "There are no complete mitigations, updating is the only safe choice." PHP runs a very large share of the web, so a great many teams spent the afternoon finding every PHP system they have.

My reply in that group was that this is another reason I love that I have moved away not only from server-side databases, but from server-side code. The server-side code I have to maintain, and worry about, is getting very small, while the features in my apps and services keep growing.

## A month I did not have to care about

PHP is not unusual. In the month before it, these were the critical flaws in server software, from the vendors' advisories and CISA's catalogue of known exploited vulnerabilities:

- **21 October, PHP.** Two unauthenticated remote code execution flaws in every supported branch.
- **20 October, Plex Media Server.** Four flaws, server-side request forgery and file path control, exploited; with a SiteGuard Server Edition command injection.
- **14 October, Palo Alto PAN-OS, Cisco Secure Email Gateway and Ahsay AhsayCBS.** Code injection, path traversal, authentication bypass and command injection, all exploited.
- **13 October, Ivanti Connect Secure.** In CISA's words, a "zero-day authentication bypass vulnerability, which allows remote, unauthenticated execution of arbitrary commands."
- **1 and 2 October, Fortinet FortiMail and Zammad.** Path traversal; session fixation and privilege management.
- **27 September, Citrix NetScaler ADC and Gateway.** Ten CVEs, and "threat actors are actively exploiting these vulnerabilities globally."
- **22 September, WordPress.** A release for "a critical severity security vulnerability", reported as CVE-2026-87902.

I did not have to patch any of them, because none of them runs anywhere in my stack. That is the best model: not responding faster to these things, but not having to worry about them at all.

## The attack surface you do not have

The attack surface compared. A typical web product runs a web server and runtime, a framework and CMS, a database, admin panels and APIs, VPN and mail gateways, and file processing. These sites run static files, the reader's browser, and one upload server that stores ciphertext.

Look at what a typical web product runs: a web server and a language runtime, a framework or a CMS with its plugins, a database, admin panels and APIs, and, around the company, VPN appliances and mail gateways. Every one of those is something that can appear in that list on any given morning.

Here is what these sites run. Static files, HTML, CSS and JavaScript, served by GitHub Pages, with no server code of ours. The reader's browser, which runs the meter, the vault, the search, the graphs and the link to pay. And one server of our own: the SG/Send upload server, where vaults live. Even that is a small surface, because it only ever stores encrypted data: it never sees the keys or the plaintext. As a measure of how small: its server code was about 9,300 lines of Python in 132 files when I last cloned it, while this newsroom alone runs about 20,000 lines of JavaScript, all of it in the reader's browser.

This is the question in [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html), turned around: an attacker looking for a server flaw has little to find here, because most of the server is not there.

## A constraint I have been writing about

None of this happened by accident, and you can follow it in what we have published. First I retired the database, then the back end, in [no server, by design](https://newsroom.sgit.ai/articles/no-server-by-design.html). [The no-server startup](the-no-server-startup.md) made it a blueprint, and [the no-server studio](inside-the-no-server-studio.md) built one. [The code you do not ship](the-code-you-do-not-ship.md) and [the minimum code below](the-minimum-code-below.md) argued for less code in general. And this week the pattern reached things that are usually server-side by definition: billing, in [the user keeps the meter](the-user-keeps-the-meter.md); messaging, in [Messaging-FS](messaging-fs.md); and AWS management, in [AWS from the vault](aws-from-the-vault.md).

I think this is good engineering. The constraint of not having anything on the server side gives me a lot of security for free, and it forces simpler designs.

## The constraint is speed

The constraint gives speed: 45 live sgit.ai sites, all static, in eleven weeks; 1,306 pages on this newsroom, with a meter and payments; 100+ users and customers across our vaults, sgit.ai and riskmandate.ai; and one server of our own, SG/Send, which stores only ciphertext.

I also want to make the business case, because the usual reading is that no server is a limitation. It is the opposite. There is nothing to provision, patch, scale or keep running, so a new site is a repository and a session, and the innovation shows it:

- **45 live sites in eleven weeks**, all static, as counted in [the sgit.ai sites in numbers](the-sgit-ai-sites-in-numbers.md).
- **This newsroom**, a full publication of over 1,300 pages, with a reading meter and payments, and able to earn revenue, entirely on the client.
- **100+ users and customers**, across our vaults, sgit.ai and riskmandate.ai, including [customers.riskmandate.ai](https://customers.riskmandate.ai/), the early-customer programme.
- **[pki.sgit.ai](https://pki.sgit.ai/)**, the key register, now accelerating.
- **On the way, the same pattern**: users.sgit.ai, accounts and billing on vaults, and aws.twin.sgit.ai, an AWS twin on a vault, both built today and not yet serving.

The architecture is leaner, with fewer moving parts, so it is easier to maintain and the workflows are simpler. And it scales well, because the heavy lifting is done on the client: every reader brings their own compute.

## Where the risk is going

None of this means the problem is solved for everyone. Internal applications are still very vulnerable, and they are rarely tested the way public ones are: the admin tool, the internal dashboard, the script with a database password that everyone forgot. I think that is where a lot of the problems will be in the future, all the more as agents start building internal tools at speed. That is a strong reason to build internal tools the same way: client side, with the data in vaults, and the server reduced to storage that cannot read what it stores.

It also connects to [the SaaS apocalypse](https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html): as more people brief the software they want instead of buying it, the question of where that software runs, and what it exposes, becomes theirs to answer.

## The question to ask

So here is the question I would ask of every component, in every design review: why does this need to be done on the server, and why can it not be done on the client? Sometimes there is a good answer: shared state, a secret that must stay off the device, an operation that must not be trusted to the user. Most of the time, in my experience, the honest answer is habit. And each habit you drop is one less line on that list.

## What this does not claim

- **The client side has its own risks.** Cross-site scripting, the JavaScript supply chain and the browser itself; the risk moves, it does not disappear.
- **There are servers underneath.** GitHub Pages and the browser vendors patch theirs; I depend on them.
- **The SG/Send server is still a server.** Small, and holding ciphertext, but real.
- **The CVE list is a month, not a census.** The critical and exploited flaws in the advisories I read.
- **The code sizes are approximate.** The SG/Send figure is from a clone of 9 September 2026.

## Where this comes from

A voice memo of 21 October 2026, and my reply in a messaging group that day. php.net's [security advisory of 21 October 2026](https://www.php.net/). CISA's alerts of [27 September](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway), [1 October](https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog), [2 October](https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog), [13 October](https://www.cisa.gov/news-events/alerts/2026/10/13/cisa-urges-patching-newly-exploited-vulnerability-ivanti-connect-secure), [14 October](https://www.cisa.gov/news-events/alerts/2026/10/14/cisa-adds-four-known-exploited-vulnerabilities-catalog) and [20 October](https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog). WordPress's [release of 22 September](https://wordpress.org/news/category/releases/). The repositories and live sites of sgit.ai, read the same day. Related: [no server, by design](https://newsroom.sgit.ai/articles/no-server-by-design.html), [the no-server startup](the-no-server-startup.md), [the code you do not ship](the-code-you-do-not-ship.md), [the user keeps the meter](the-user-keeps-the-meter.md), [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html), [the SaaS apocalypse](https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#the-attack-surface-you-do-not-have)

### Builds on

- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.
- [Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault](inside-the-no-server-studio.md) An infographic studio built to the no-server blueprint, mostly simulated, in a vault: what is real, the business plan, and a bug found live.
- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line](messaging-fs.md) A proposed encrypted messenger between vaults: append lanes for transport, PKI for trust, and Messaging-FS as the schema.
- [AWS from the vault: a proposed aws.twin.sgit.ai, where a temporary AWS session lives in the user's vault, the browser does the work, and AWS data finally has a place to go](aws-from-the-vault.md) A proposed aws.twin.sgit.ai: an AWS twin on a vault first, then a temporary AWS session from the user's vault.
- [The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says](the-sgit-ai-sites-in-numbers.md) All 53 sgit.ai site repositories counted: 45 live sites, 1,679 commits, 5,419 pages, growth in bursts and a long tail.

### Continued by

- [The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent](the-key-is-not-the-risk.md) Credential injection for AI agents is a good pattern; the first question is still what an attacker can make the agent do.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 243 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=243)

**Posting this article on LinkedIn?** The cover is [the-attack-surface-you-do-not-have.jpg](banners/the-attack-surface-you-do-not-have.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html)*
