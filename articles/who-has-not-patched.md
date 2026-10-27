# Who has not patched? How good the "unpatched" numbers for php2shell are, what makes a website actually vulnerable, and why not patching can be the rational decision, sgit.ai

> Six days after php2shell, the headlines say most websites have not patched, and the subtext is that businesses do not take security seriously. Before accepting that, ask how good the number is. Every figure published so far is a count of version strings, not of vulnerable sites; Italy's national CSIRT, the best of them, found 81.9% of PHP services whose version it could read below the fix, which is 38.5% of all it detected, and a fixed package can keep its old number. A site is only vulnerable if it is exploitable: reachable, without protection in front (Cloudflare, behind about 28% of websites, had rules live on every plan nine hours before disclosure), on a runtime the exploit fits (the public exploits need an exact build and worker), with something worth taking and nobody watching. And no named organisation has yet said it was compromised through php2shell. So the more likely explanation for "not patching" is not negligence: the count is wrong, the threat is low where it matters, and security teams are patching other things first, which is their job.

*Source: <https://newsroom.sgit.ai/articles/who-has-not-patched.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who has not patched? How good the "unpatched" numbers for php2shell are, what makes a website actually vulnerable, and why not patching can be the rational decision

# Who has not patched? How good the "unpatched" numbers for php2shell are, what makes a website actually vulnerable, and why not patching can be the rational decision

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-27 · [article v1.0.0](versions/who-has-not-patched.md) · [newsroom v0.13.108](https://newsroom.sgit.ai/admin/versions.html) · php2shellpatchingriskevidencesecurityarticle

***Abstract:** Six days after php2shell, the headlines say most websites have not patched, and the subtext is that businesses do not take security seriously. Before accepting that, ask how good the number is. Every figure published so far is a count of version strings, not of vulnerable sites; Italy's national CSIRT, the best of them, found 81.9% of PHP services whose version it could read below the fix, which is 38.5% of all it detected, and a fixed package can keep its old number. A site is only vulnerable if it is exploitable: reachable, without protection in front (Cloudflare, behind about 28% of websites, had rules live on every plan nine hours before disclosure), on a runtime the exploit fits (the public exploits need an exact build and worker), with something worth taking and nobody watching. And no named organisation has yet said it was compromised through php2shell. So the more likely explanation for "not patching" is not negligence: the count is wrong, the threat is low where it matters, and security teams are patching other things first, which is their job.*

The layers between "running PHP" and "compromised", and which of them a version count measures.

## In short

- **The headline implies negligence.** "Most sites have not patched" reads as "business doesn't care".
- **Every published number is a version count,** not a test of whether a site can be exploited.
- **Version strings lie both ways.** Backported fixes keep the old number; about a third of hosts hide it.
- **Vulnerable means exploitable.** Reachable, unprotected, the right runtime, something worth taking, nobody watching.
- **The edge moved first.** Cloudflare had rules on every plan nine hours before disclosure.
- **Still no named victim,** six days in, and 34 sites taken offline as a precaution.
- **Security teams prioritise.** 17 flaws went on CISA's exploited list in the same fortnight.
- **The likelier story:** the count is wrong, the threat is low where it matters, and work is going elsewhere.

## The headline and what it implies

The story of day five and six is that websites are not patching: large numbers still unpatched, look at this, people are ignoring it. I asked the newsroom to find the number behind it, and the first finding is that there is no single one. Searching all 614 sources in the PHP story site's evidence, nobody says "90% not patched". The closest are [Italy's national CSIRT](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cybersecitalia-lalert-dellacn-in-italia-a-rischio-vulne/) on 25 October, "only about 18%" of the Italian organisations concerned had updated, and a newsletter headline of "1.5M servers unpatched on day one". The nearest 90% says the opposite: a Berlin hosting firm said 90% of its customers were patched 18 minutes after the release.

What all of them imply is the same, and it is a habit of my own profession. Security has a bad habit of telling the business that it is irresponsible: the sky is falling, you take too many risks, patch, patch, patch. A headline that says most sites have not patched implies negligence. Before accepting that, there are two questions. How good is the number? And what does "vulnerable" actually mean?

## How good is the number?

Every figure published so far counts version strings. None tests whether a site can be exploited. And the units are all different: [Censys counted](https://refs.php.oct.2026.newsroom.sgit.ai/sources/securityweek-exploitation-days-before/) 2.58 million hosts seen on release day, 1.57 million announcing a version below the fix; its dashboard was quoted at 36.7 million "services"; Palo Alto at 22.6 million "instances"; Italy at 741,523 services. As we found [checking Jeremiah Grossman's post](https://newsroom.sgit.ai/articles/the-evidence-behind-four-days.html), those are different things, and no one measurer has published a series over the days.

The best of them, Italy's, shows the problem. CSIRT Italia detected 741,523 PHP services; it could read the version of 348,130, 47%; and 285,149 of those, 81.9%, were below the fixed release. So the 81.9% is of the readable half. Of everything detected, it is 38.5%. And "below the fixed release" is not "unpatched": Fortinet, quoting Censys, says these "are service counts, not unique servers or organizations, and version-based estimates may include installations already patched through vendor backports". Ubuntu, Debian and Red Hat fix PHP in the version they shipped, without changing its number. The PHP story site's [patching tracker](https://php.oct.2026.newsroom.sgit.ai/patching/) lists fixes from Ubuntu, Debian, Red Hat, cPanel and CloudLinux that a version scan would count as unpatched.

The error runs the other way too. The CVE records list only PHP 8.2 to 8.5, so a scanner that reads them reports 7.4 to 8.1 as not affected. And one French count put 6.62 million of 11 million PHP services in France, which turned out to be a fingerprinting error about home routers. A version count is a starting point, not a finding.

## What makes a site vulnerable

This is the simple logic: a site that cannot be exploited is not vulnerable, whatever its version says. For a php2shell compromise, five things have to be true, and a version count measures none of them.

1. **Reachable.** The PHP server answers the attacker directly. Sites taken offline, or behind a login, or only on an internal network, are not.
2. **Nothing in front.** No web application firewall or edge rule blocking the attack. [Cloudflare's rules](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cloudflare-blog-php2shell-waf/) were live on every plan, including the free one, from 03:02 UTC on 21 October, about nine hours before disclosure. [Akamai](https://refs.php.oct.2026.newsroom.sgit.ai/sources/akamai-blog-php-core-rce/) and [Imperva](https://refs.php.oct.2026.newsroom.sgit.ai/sources/imperva-blog-php2shell/) followed the same day, Fortinet the next. According to W3Techs on 27 October, 32.7% of websites sit behind a reverse proxy it monitors, and Cloudflare alone 28.1%. A rule is a stopgap, every vendor says so, and an origin reachable directly goes round it. But a scan that reaches the edge often cannot see the PHP version at all.
3. **A runtime the exploit fits.** The advisories say complete remote code execution was demonstrated against Apache with mod_php; for PHP-FPM, "no complete FPM exploit has been demonstrated" for the first flaw. [Fastly](https://refs.php.oct.2026.newsroom.sgit.ai/sources/fastly-blog-php2shell/) says the public exploits "require knowledge of the specific, running PHP binary and address space layout on the server". The public bounty win needed an exact build and worked about seven times in ten in its author's own lab, as [we checked](https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html). CISA's own assessment on the CVE records said "Automatable: no".
4. **Something worth taking.** Code execution on a brochure site with nothing behind it is a defacement risk; on a server holding tokens, customer data or a route into the network, it is a breach. Not all websites are the same.
5. **Nobody watching.** Can the attack be detected? The PHP story site's defence notes are frank that standard logs show little of this attack. That cuts both ways, and I come back to it below.

Multiply those together and the population that is vulnerable, valuable and unwatched is much smaller than "not patched". Nobody has measured it, which is the honest answer, and also why the headline number tells us so little.

## What the record shows

Six days in, the PHP story site's [compromise record](https://php.oct.2026.newsroom.sgit.ai/compromise/), at 14:41 UTC on 27 October, still reads: "No named organisation has said it was compromised through php2shell." Vendors report attempts, in millions; two vendors retracted earlier claims of success; eight national CERTs, among them Latvia, Austria, Belgium, Switzerland, Germany, the Netherlands, Japan and Luxembourg, report no successful attacks in their countries; watchTowr's answer to whether reliable indiscriminate exploitation is happening was "for now, the answer is a firm No".

The site also counts 34 services taken offline, all as precautions: councils, ministries, banks, airlines, Wikimedia. That raises its own question, which I think deserves measuring: how many sites were taken off the internet that did not need to be, and what did that cost? A site taken offline shows in a version scan as "not seen", or as "unpatched" if it was scanned before it went down. Neither is "not patching".

## The call the team had to answer

Think about the conversation that actually happens. An executive has seen it on the news and asks: are we vulnerable, yes or no? What's the impact? Can they get in? And then the questions executives always ask, because they make risk decisions every day: how many companies have been hit? What is the threat?

If the answer is "none, so far", the executive concludes, correctly, that the threat is low. You can only stop everything for a clear and present danger, and you only have that when it is actually happening. Imagine someone on a high street saying the whole street is about to catch fire, and you look up and down the street and no shop is on fire. You might still act, but you would not stop trading.

And the business is paying the security team to do exactly that: to put its limited time where the real threats are. In the same fortnight, CISA added 17 flaws to its list of known exploited vulnerabilities, among them PAN-OS, Cisco's email gateway, BeyondTrust, Fortinet, Plex, Arista and Collabora, each with a deadline. php2shell went on it on 26 October.

CISA's exploited-vulnerability additions from 14 to 26 October 2026, and php2shell's EPSS score.

A model-driven queue would not have put php2shell at the top for most of the week either: its EPSS score was 0.05 to 0.12 until 25 October, then jumped above 0.999. Choosing not to patch this server today usually means patching another one first. That is not negligence. It is the job.

## The secondary stories

So when the headline says sites are not patching, I think the more likely explanations, in order, are:

1. **The count is wrong,** or at least much smaller than it looks: version strings, backports, unreadable versions and different units.
2. **The threat is not there yet** for most sites: hard exploits, no named victim, CERTs reporting none.
3. **Protection was put in front,** especially of the sites worth attacking: the edge, configuration changes such as switching off upload progress, and sites taken offline.
4. **Teams are patching what is being exploited first,** which is what they are paid to do.

Against that, "they don't care" is the least likely explanation, and it is the one the headline chooses.

## The part I can't rule out

I do think some companies may have been compromised and have not said so. Detection is hard: JPCERT warned that a lack of traces does not prove there was no compromise. GMO Internet Group found malicious programs on 26,739 servers of one of its services and has not stated the cause. And disclosure rules do not require a public statement: GDPR and NIS2 reports go to regulators, not the public, and US listed companies report only material incidents. But given how high-profile this is, I would be surprised if many such cases stay hidden for long. One regulator's notice naming the flaw would end the "no named victim" line, and the PHP story site is watching for it.

## What this does not claim

- **That patching is unnecessary.** Patch: every vendor says the rules and settings are stopgaps, and a third flaw affects fully patched releases.
- **That no site was compromised.** The record is a dated absence, as of 14:41 UTC on 27 October.
- **A measured number of exploitable sites.** Nobody has published one; the layers above are the argument for measuring it.
- **Some figures are relayed.** Italy's 81.9% comes through two Italian outlets; CSIRT Italia's alert itself is not captured. Censys's figures are relayed by others.
- **"90% not patched" was not found** as a headline; if you have the link, we will add it.

## Where this comes from

The PHP story site's data, read on 27 October 2026 (data version 0.1.85): [the compromise record](https://php.oct.2026.newsroom.sgit.ai/compromise/) and [compromise.json](https://data.php.oct.2026.newsroom.sgit.ai/latest/compromise.json), [the patching tracker](https://php.oct.2026.newsroom.sgit.ai/patching/) and [patching.json](https://data.php.oct.2026.newsroom.sgit.ai/latest/patching.json), [defence.json](https://data.php.oct.2026.newsroom.sgit.ai/latest/defence.json), [numbers.json](https://data.php.oct.2026.newsroom.sgit.ai/latest/numbers.json), with the captured sources: [CyberSecItalia on ACN's alert](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cybersecitalia-lalert-dellacn-in-italia-a-rischio-vulne/), [SecurityWeek on Censys](https://refs.php.oct.2026.newsroom.sgit.ai/sources/securityweek-exploitation-days-before/), [Cryptoast on the French miscount](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cryptoast-failles-critiques-php-php2shell-france-f/), [php.net's advisory](https://refs.php.oct.2026.newsroom.sgit.ai/sources/php-net-advisory/), [Cloudflare](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cloudflare-blog-php2shell-waf/), [Akamai](https://refs.php.oct.2026.newsroom.sgit.ai/sources/akamai-blog-php-core-rce/), [Fastly](https://refs.php.oct.2026.newsroom.sgit.ai/sources/fastly-blog-php2shell/), [Imperva](https://refs.php.oct.2026.newsroom.sgit.ai/sources/imperva-blog-php2shell/). Read live on 27 October: [Fortinet's post](https://www.fortinet.com/blog/industry-trends/understanding-php2shell-vulnerabilities-and-reducing-risk-while-you-patch), [W3Techs' reverse proxy survey](https://w3techs.com/technologies/overview/proxy), [CISA's KEV catalogue](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) and [FIRST's EPSS API](https://api.first.org/data/v1/epss?cve=CVE-2026-109618,CVE-2026-109619&amp;scope=time-series). Related: [the evidence behind four days](https://newsroom.sgit.ai/articles/the-evidence-behind-four-days.html), [what the bitcoin bounty actually proves](https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [translate the assumption](https://newsroom.sgit.ai/articles/translate-the-assumption.html). Researched by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

News & evidence[This article as a graph →](graphs.md#who-has-not-patched)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 305 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=305)

**Posting this article on LinkedIn?** The cover is [who-has-not-patched.jpg](banners/who-has-not-patched.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-has-not-patched.html)*
