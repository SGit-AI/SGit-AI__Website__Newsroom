---
title: The false positives are the next incident: Jeremiah Grossman's warning about php2shell scanners, checked against what the evidence holds a day later
date: 2026-10-23
author: Dinis Cruz
author_url: about/index.html
summary: On the evening of 22 October, Jeremiah Grossman wrote on LinkedIn that "the false-positives for php2shell from makeshift scanners is what's going to be apocalyptic". I replied that, as of the night before, there was no public record of a company being hit. Both things are true, and the data the PHP story's source watch captured by midday on 23 October shows why they belong together. One scanner maker says most scanners in circulation read the version string, and a version string cannot see a distribution's backported fix: one user has already reported a check script calling Ubuntu's patched PHP vulnerable. One account opened 53 templated "heads up" issues, each saying it may itself be a false positive. A detection guide withdrew its own ModSecurity rule because it never fired. Against that, the compromise map holds millions of attempts and no named organisation saying php2shell was the way in. When the noise is this loud and the confirmed signal this quiet, the false positives are not a side effect: they are what organisations act on, and switching a patched site off because a makeshift scanner said so is an incident of its own.
version: v0.13.55
license: https://creativecommons.org/licenses/by/4.0/
tags: php2shell, scanners, false-positives, detection, evidence, article
status: published
---

!shot qn-grossman-post.webp | images/ | Jeremiah Grossman's LinkedIn post on php2shell false positives, as captured on 23 October 2026. | screenshot

## In short {#in-short}

- **Jeremiah Grossman's warning is right.** The evidence a day later already shows the pattern.
- **Most scanners read the version string.** That is what one scanner maker says, and a version string cannot see a backported fix.
- **The predicted error has been reported.** A community check script called Ubuntu's patched PHP vulnerable.
- **The noise is already in bulk.** 53 templated issues from one account, 62 issues for php2shell "false positive".
- **Detection rules fail too, in both directions.** One guide withdrew a ModSecurity rule that never fired.
- **The signal is quiet.** Millions of attempts, and no named organisation saying php2shell was the way in.
- **Ask how a scanner decides.** Then check the package, not the banner, before switching anything off.

## The post, and my reply {#the-post}

On the evening of 22 October (UTC), Jeremiah Grossman, chief executive of Root Evidence, [posted on LinkedIn](https://www.linkedin.com/posts/grossmanjeremiah_the-false-positives-for-php2shell-from-makeshift-share-7519173707991433217-Qh3E/): "The false-positives for php2shell from makeshift scanners is what's going to be apocalyptic." It is a short, cheeky line, and an important one. I replied under it with a pointer to the [PHP story site](https://php.oct.2026.newsroom.sgit.ai/): as of the night before, there was no public record of a company being hit.

The two statements are not in tension. They describe the same situation from two sides. When the confirmed damage is small and the fear is large, what organisations act on is whatever their tools tell them. If the tools are wrong, the action is wrong too. So I asked the PHP story's researcher to make it a research angle: how good the scanners and detection rules are, who reports them getting it wrong, and how the noise flows. The [brief is public](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/), and by 12:40 UTC on 23 October the source watch (vault `oq9gflln`) had twelve captured pages in it, each with its snapshot and hash.

!shot qn-twelve.webp | images/ | The twelve pieces of evidence in the scanner-noise angle, captured 12:38 to 12:40 UTC on 23 October 2026. | concept

## Why a version check gets it wrong {#version-strings}

There are two ways a scanner can decide that a server is vulnerable. It can read the version the server advertises, in a banner, a header or the output of `php -v`, and compare it with the fixed release. Or it can try to produce the fault, harmlessly, and see whether it appears.

The first is quick to write and wrong in a predictable way. Linux distributions backport fixes into their own packages without changing the upstream version number. Ubuntu's patched PHP 8.5 package is `8.5.4-0ubuntu1.5`, listed as fixed (the [Konfirmity advisory](https://www.konfirmity.com/advisories/php2shell-php-remote-code-execution) collects the distributions' fixed packages and says it plainly: "Distributions often backport the fix without changing the PHP version number"). The upstream number in that package is still 8.5.4, below the fixed upstream release, 8.5.12. A scanner that reads 8.5.4 says vulnerable. The server is fixed.

That is not a hypothetical. In the watch:

- **Searchlight Cyber**, which released an open-source scanner, is quoted by Help Net Security saying that most of the scanners in circulation "rely on version checks, or do not accurately depict vulnerable conditions for both mod_php and php-fpm". Its own scanner tries to produce the fault first and reads the version only as a last resort.
- **An issue on a community check script, `php2shell-check`,** reports that the script calls Ubuntu's patched `8.5.4-0ubuntu1.5` vulnerable, because the version string is older than the fixed upstream release. Exactly the error the method predicts.

!shot qn-two-checks.webp | images/ | Two ways a scanner decides on the same patched Ubuntu server: reading the version string, or trying the fault. | diagram

## The noise is already in bulk {#bulk}

A false positive in one scanner is a bug. A false positive sent to many people at once is noise, and it scales.

- **53 templated issues, from one account.** Titled "Heads up: this repo pins a PHP version affected by PHP2Shell", at 12:38 UTC. The repositories they landed on include training repositories and an intentionally vulnerable challenge set, which are meant to be vulnerable. To its credit, the template itself says it may be a false positive, or that the image may already carry a distribution backport. Every one of those notices still asks a maintainer, often an unpaid one, to stop and check.
- **62 GitHub issues** match a search for `php2shell "false positive"`, the templated notices among them.
- **10 issues on nuclei-templates** name php2shell, and two merged pull requests are in the watch's series: the scanner templates are being fixed as people report them.

These are search counts, and they move as GitHub's index updates. The watch tracks them as what the page showed, every pass. The direction matters more than the exact number, and I will report it as it moves.

## Detection rules fail in both directions {#detection}

Scanners look at servers; detection rules look at traffic. They have the same problem from the other side.

- **A rule that never fired.** A community detection guide (a GitHub gist) withdrew its own earlier ModSecurity rule: "ModSecurity leaves REQUEST_BODY empty for multipart requests, so that rule never fires." That is a false negative, found and admitted by the author, which is exactly what should happen. How many copies of the first rule are still deployed is a question nobody can answer from the outside.
- **A claim to test.** The same guide says its replacement rule "has zero false positives by construction". It may be right. It is a claim, and claims like that are what a lab test is for.
- **The request alone is not enough.** Cloudflare's write-up on its protections says the request does not always separate an exploit from legitimate traffic, and that the origin's response "adds context, helping identify whether an exploit succeeded while reducing the risk of false positives".
- **Host detections need a baseline.** Equixly, citing Huntress, says host detections need a baseline first, "because both can produce false positives".
- **Coverage is still being asked for.** The OWASP Core Rule Set has an open request for more PHP2Shell signatures.

None of this is a criticism of the people doing the work. It is what the first days of a new class of flaw look like: tools written fast, corrected in public. The problem is that the people downstream act on the first version.

## A quiet signal under a loud alarm {#signal}

Put the noise next to the PHP story's [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/), as it stood at 20:50 UTC on 22 October. Millions of attempts against sensors, honeypots and edges. Exploitation reported by three vendors, none naming a victim. One named organisation saying it was attacked, with success not stated. Zero named organisations saying php2shell was the way in. That is a time-bounded absence, not proof that nothing happened, and one statement from one organisation would end it.

!shot qn-signal-noise.webp | images/ | The compromise map's layers on 22 October next to the scanner noise by 12:38 UTC on 23 October. | comparison

This is where Jeremiah Grossman's word, apocalyptic, earns its place. Organisations across Europe switched websites off as a precaution on 21 and 22 October. When nobody can say quickly whether a site is safe, a scanner's red line is the deciding fact. A false positive on a patched Ubuntu server becomes a ticket, then an escalation, then a site taken offline, for real people who needed it. Multiply that by every makeshift scanner and every bulk notice, and the cost of the noise can exceed the cost of the attacks we can see. It is an incident of its own, and it is not in anyone's breach count.

It also feeds the problem I wrote about in [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html). A site with somebody paid to know it can answer "is this a false positive?" in an hour. A site that was built, launched and left cannot, so it gets switched off.

## What to do with a scanner's answer {#what-to-do}

- **Ask how the scanner decides.** If it reads the version, its "vulnerable" means "an old upstream number", nothing more. Treat it as a question, not a finding.
- **Check the package, not the banner.** On a distribution install, look at the package version and its changelog for the CVE numbers (CVE-2026-109618 and CVE-2026-109619), and check the PHP that serves web requests, not only the command line.
- **Prefer evidence over inference.** A check that produces the fault, in a lab or with permission, beats a version comparison. Cloudflare's point applies to people too: the response tells you more than the request.
- **Before switching off, write down why.** "A scanner said so" is a reason to look, not a reason to take a service away from the people who use it.
- **If you make a scanner, say its method.** One line on the result, "version check" or "fault reproduced", would remove most of the damage.

## What would settle it {#lab}

The PHP story's board has a lab test on it, owned by its cyber desk and waiting for my go: run the public scanners against a distribution-patched PHP (for example Ubuntu's `8.5.4-0ubuntu1.5`) and an unpatched one, in an isolated lab, and record which ones get each right. It tests the tools, never anyone's systems. That would turn this angle from reports into measurements, and I think it is the most useful thing the newsroom can do about this next. The watch, meanwhile, measures the noise every pass: the issue searches, the templated notices, the nuclei-templates issues, and Hacker News comments on php2shell scanners. The places where people complain most about their tools, Reddit, X, Bluesky and LinkedIn, give the watch a sign-in page, so an external collector covers them.

## What this does not claim {#limits}

- **A false-positive report is one person's account.** It is recorded as what they said, not as a verdict on the tool.
- **Search counts are rough.** They are what the page showed at 12:38 UTC, and they move.
- **No private people are named.** Repositories and tools are named as places; the people who opened the issues are not.
- **It maps evidence, not risk.** It does not say whether scanners make the internet safer or less safe.
- **The absence of a named victim is time-bounded.** True as of the last check; one statement would end it.
- **No cost of the noise has been measured.** "Can exceed the cost of the attacks we can see" is my argument, not a number.

## Where this comes from {#sources}

Jeremiah Grossman's [LinkedIn post](https://www.linkedin.com/posts/grossmanjeremiah_the-false-positives-for-php2shell-from-makeshift-share-7519173707991433217-Qh3E/) of 22 October 2026, and the screenshot I took of it on 23 October; the PHP story's [scanner-noise brief](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/) and its twelve captured pages in the source watch (vault `oq9gflln`, `index/angles/scanner-noise.json`), from Help Net Security, Digital Today, GitHub, a community detection gist, Cloudflare, Equixly, the OWASP Core Rule Set and nuclei-templates; the [Konfirmity advisory](https://www.konfirmity.com/advisories/php2shell-php-remote-code-execution) for Ubuntu's fixed package; and the PHP story's [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/). Related: [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [the maintenance deficit, with evidence](https://newsroom.sgit.ai/articles/the-maintenance-deficit-with-evidence.html), [PHP October 2026, at 8pm](https://newsroom.sgit.ai/articles/php-october-at-8pm.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
