---
title: PHP October 2026, at 8pm: where the php2shell story stands, and a guided tour of the site that tracks it, built in one day by a team of agents from an evidence vault anyone can read
date: 2026-10-22
author: Dinis Cruz
author_url: about/index.html
summary: At 8pm UK time on 22 October, this is where the php2shell story stands. The fix has been out since 21 October; sixteen agencies say install it; attackers are trying, in large numbers, and Amazon saw an attempt four days before the announcement; no named organisation has said it was broken into through these flaws, and the US list of flaws known to be used in attacks still does not include these two. The Dutch inventory of affected software has 724 rows, and only 61 of them have a fix. And behind that update is something I want to show properly: php.oct.2026.newsroom.sgit.ai, a site built today, from 09:27 to 19:04 UTC, in 34 versions, by two people and thirteen agents. It reads an evidence vault of 184 sources and 177 dated captures, now public. It has a front page in plain English and fifteen briefings, 70 claims each graded by a fact-check desk, ten contradictions in a ledger, a graph of 209 nodes, the fix read in the code, the inventory hour by hour, every section versioned, a phone app, synthetic readers and eight vaults. This is a guided tour of it, with the versions of everything, so the next update can say exactly what changed.
version: v0.13.49
license: https://creativecommons.org/licenses/by/4.0/
tags: php2shell, breaking-news, evidence, vaults, versions, article
status: published
---

> **Update 1.** This is the first update on the php2shell story and the newsroom covering it. [Update 2](https://newsroom.sgit.ai/articles/php-daily-2026-10-23.html) follows, as of 23:30 UTC on 23 October.

!shot po-collage.webp | images/ | A guided tour of php.oct.2026.newsroom.sgit.ai in nine pages: the front page for everyone, the inventory hour by hour, the story as a graph, every section versioned, a source and its captures, the fix read in the code, the team, the eight vaults, and the six synthetic readers. | wide | screenshot

> **Updated at 22:15 UTC.** The story's site has moved from v0.5.5 to v0.6.0 since 8pm. What changed is in [since 8pm](#since): a map of the evidence on compromise, a second fact-check run that answers the incomplete-fix report, and a new risk and compliance section. Two lines below are corrected to match: no *named* organisation has said it was compromised through these flaws, and the incomplete-fix report was answered that morning. At 22:45 UTC, a third correction: the source watch did not stop at 15:11, and the vendor reports were captured; see [what the day showed](#lessons).

## In short {#in-short}

- **The fix is out; the advice is unanimous.** Install PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35.
- **Attackers are trying.** Millions of attempts; one seen four days before the announcement.
- **No named compromise yet.** And the US list of exploited flaws does not include these two.
- **724 affected products listed; 61 fixed.** 440 still under investigation.
- **A whole site, built today.** 34 versions, two people, thirteen agents.
- **Everything rests on a vault anyone can read.** 184 sources, 177 dated captures.
- **The versions of everything are recorded.** So the next update can be compared with this one.

## Where the story stands at 8pm {#stands}

On the morning of 22 October I was reading the BBC's live page about two critical flaws in PHP, the software that WordPress and a large share of the world's websites run on. In [capture first](https://newsroom.sgit.ai/articles/capture-first.html) I described how that page became an evidence vault, a section on this site and then a site of its own, [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/), by lunchtime. This is the evening update, at 8pm UK time, 19:00 UTC.

What the evidence shows:

- **The flaws and the fix.** Two flaws, [CVE-2026-109618 and CVE-2026-109619](https://php.oct.2026.newsroom.sgit.ai/flaws/index.html), both rated 9.2 out of 10, in PHP itself. The fix is in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October. PHP 8.1 and older have no ready-made fix. Those four releases and the advisory were still the latest entries in php.net's news when I checked at 19:00.
- **When it was disclosed.** On 21 October, not 22 October as many reports, and the first version of our own section, said. The primary records date it to the afternoon of 21 October UTC; the site's fact-check desk graded "disclosed on 22 October" as refuted today, and we have corrected our section.
- **What governments say.** [Sixteen agencies](https://php.oct.2026.newsroom.sgit.ai/agencies/index.html) agree on one thing: install the fix now. They disagree on what to do if you cannot: the US says take the website offline, the UK lists that as a last resort, several European agencies say cut it off from the public internet.
- **Exploitation.** Attackers are trying. Cloudflare's chief executive reported millions of attempts; Amazon reported an attempt against one of its decoy servers on 17 October, four days before the announcement. Other security companies report attempts too; one reported seeing none on its partners' systems on the evening of 21 October.
- **Compromise.** No named organisation had said it was broken into through these flaws, in anything the vault had captured. At 19:00 the US government's [catalogue of known exploited vulnerabilities](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) still did not list either flaw; its latest edition was released at 14:04 UTC on 21 October.
- **Systems taken offline.** [Ten entries](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) in the site's ledger of organisations that took websites offline as a precaution, from the Dutch government's login service to UK councils and game wikis. Taken offline is not the same as compromised, and the site keeps them in separate ledgers.
- **Affected software.** The Dutch national cyber security centre keeps a public list of software that ships or depends on PHP. At its latest version, 15:28 UTC, it had 724 rows: 61 fixed, 216 vulnerable, 440 still under investigation, 6 not affected.

!shot po-inventory.webp | images/ | The Dutch inventory of affected software, at each of its 38 versions from 21 October: 724 rows at 15:28 UTC on 22 October, of which 61 fixed, 216 vulnerable and 440 still under investigation. | comparison

## What we still do not know {#unknown}

- **Whether any website was broken into** before it installed the fix.
- **Whether the fix is complete: since answered.** A relayed report on 21 October suggested it may not be. At 8pm the fact-check desk graded it "not shown"; its second run found that PHP's security team had answered it publicly at 09:11 UTC that morning: an unrelated crash bug, nothing to do with the remote code execution. I should have caught that at 8pm.
- **How many systems are still unpatched.** One count is open in the [contradiction ledger](https://php.oct.2026.newsroom.sgit.ai/factcheck/index.html), with no second measure to settle it.
- **Who leaked the news on 20 October**, and whether any technical detail leaked with it.
- **Where the "70% of the internet" figure comes from.** It is roughly the share of websites built with PHP, not a measure of how many are at risk.

## A site built in one day {#day}

!shot po-releases.webp | images/ | One day, 34 versions of php.oct.2026.newsroom.sgit.ai, from v0.1.0 at 09:27 UTC to v0.5.5 at 19:04 UTC, with two lines of versions running in parallel until the design branch was merged into v0.4.0. | comparison

The site's first version went out at 09:27 UTC. The thirty-fourth, v0.5.5, went out at 19:04. In between, 62 commits, two lines of versions developed in parallel and merged, and a team that grew through the day: the [team page](https://php.oct.2026.newsroom.sgit.ai/team/index.html) now lists 17 members, two of them people, a project manager and me as the editor, and 13 agents, each with a role, what it owns, the rules it works by and the work it has shipped. Their tasks are on a board of 89 items, 25 of them done.

I want to be precise about what I did. I read, I sent voice memos, I pointed agents at sources and decided what mattered. The agents captured the evidence, wrote the data, built the pages, checked each other, and released. The site's own [release history](https://php.oct.2026.newsroom.sgit.ai/admin/versions.html) has every version with what it changed.

## The tour {#tour}

There is a lot here, so this is the route I would take a colleague through.

**1. The front page, for everyone.** The [front page](https://php.oct.2026.newsroom.sgit.ai/) starts in plain English: what happened, what to do, what is not known, every line linked to the sources it rests on. Then it splits by reader. [Start here](https://php.oct.2026.newsroom.sgit.ai/start/index.html) maps fifteen readers, from a curious reader to a CISO, a CFO, a journalist and a PHP engineer, each with a thirty-second answer and a reading path, and each has [a briefing](https://php.oct.2026.newsroom.sgit.ai/briefings/board/index.html). There is a glossary of 40 terms, linked on first use on every page, and [ten questions readers ask](https://php.oct.2026.newsroom.sgit.ai/questions/index.html), each with a short answer to paste back to whoever asked you.

!shot po-phone.webp | images/ | On a phone: the front page, and Now, which answers what to know for the time you have, one, five, ten or thirty minutes, from the data alone or written by a model with the reader's own key. | comparison | screenshot

**2. On a phone.** [Now](https://php.oct.2026.newsroom.sgit.ai/now/index.html) asks how much time you have, one, five, ten or thirty minutes, and gives you what you have not read yet. "From the data" is built from the site alone. "Written for me" uses a model with your own key, kept in your own vault, and every claim it makes must cite an item on the site. Since v0.5.4, every page also has an Ask pane: you talk to the site with your own key, the model can only use the site's read-only tools, every call is shown, every fact is cited to an item, and it changes nothing without your say-so.

**3. The evidence.** Everything rests on the evidence vault. It holds 184 sources and 177 dated captures, each with the page as served, the rendered page, its text, a full-page screenshot, the headers and a sha256 hash, from six writers, from 08:05 to 11:34 UTC. Since this afternoon it is [readable by anyone](https://newsroom.sgit.ai/articles/a-desk-anyone-can-open.html), with a public read key that cannot write, after a scan of all its files. Every [source page](https://php.oct.2026.newsroom.sgit.ai/sources/bbc-live-ckgel5xp2xv9t/index.html) on the site shows its captures, their times and their hashes, and the claims that cite it. A second vault, the [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html), checks the outside sources on a schedule: by 21:08 UTC, 773 pages from 474 publishers in 57 countries and 34 languages, with 1,851 dated snapshots, and what access each allows, open, behind a bot challenge, down or gone.

**4. The analysis, graded.** The site has [70 claims](https://php.oct.2026.newsroom.sgit.ai/claims/index.html), each with a status and its sources, [68 timeline events](https://php.oct.2026.newsroom.sgit.ai/timeline/index.html), [17 numbers](https://php.oct.2026.newsroom.sgit.ai/numbers/index.html) pinned to what they measure, and an [impact ledger](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) that keeps offline and compromised apart. Tonight the [fact-check desk](https://php.oct.2026.newsroom.sgit.ai/factcheck/index.html) finished its first run: all 70 claims graded against the vault on a scale from A0, unsupported, to A6, with a verdict for each. 39 hold, 28 hold in part, one is not shown and two are refuted: the 10.0 severity score from the leak, and the 22 October disclosure date. It opened 143 tickets and a ledger of ten contradictions, five explained and five open, each with what would settle it.

**5. The story as a graph.** The [graph](https://php.oct.2026.newsroom.sgit.ai/graph/index.html) has 209 nodes and 281 edges: the 70 claims, the 68 events and the 71 sources they cite. It is drawn from the same rows as the pages, so the picture cannot disagree with the text.

**6. The fix, read in the code.** The [code page](https://php.oct.2026.newsroom.sgit.ai/code/index.html) answers the question I asked in the morning, where the flaw actually lives, from a clone of php-src rather than from any article: the fix commit, its parent, the branch it landed on, the backport to an end-of-life branch, and the files it changed, mapped as [layered graphs](https://php.oct.2026.newsroom.sgit.ai/review/index.html).

**7. Patching and the inventory.** [Patching](https://php.oct.2026.newsroom.sgit.ai/patching/index.html) explains who can get a fix for which version of PHP, the six ways a fix reaches a server, and why not every version gets one. [The inventory, hour by hour](https://php.oct.2026.newsroom.sgit.ai/patching/inventory/index.html) reads the Dutch list from its public history, every change of status, and the first recorded fix from each supplier.

**8. Stories, and context.** Research and stories are kept apart, with a strip at the top of every page saying which it is. [Five house stories](https://php.oct.2026.newsroom.sgit.ai/articles/index.html), by the site's journalist, historian and cyber desk, among them [exposed is not exploited](https://php.oct.2026.newsroom.sgit.ai/articles/exposed-is-not-exploited/index.html), and an [interview with me](https://php.oct.2026.newsroom.sgit.ai/interview/index.html). And [in context](https://php.oct.2026.newsroom.sgit.ai/context/index.html), php2shell against earlier flaws from 2008 to 2026.

**9. Versions, of everything.** This is the part I care most about. Every section of the site, every briefing, front-page section and story, is hashed on every build and gets a new version only when its text changes: 110 sections, 207 versions so far, in a [table of release against section](https://php.oct.2026.newsroom.sgit.ai/versions/index.html). Every fact has its own timeline. And the site tracks [341 items a reader can follow](https://php.oct.2026.newsroom.sgit.ai/whatsnew/index.html), so it can say what is new or changed since your last visit, in your browser, with nothing sent anywhere.

**10. The vaults and the team.** [Eight vaults](https://php.oct.2026.newsroom.sgit.ai/vaults/index.html) sit behind the site: the evidence and the source watch, public read-only; the anonymous telemetry and the subscriptions, each written through a lane that can add and cannot read; the coverage of other outlets, private, because it holds other people's pages; and three the team coordinates through, the conductor's, the issues and the mail. Every vault is encrypted in the browser or the agent's session; the server holds ciphertext.

**11. The readers, real and synthetic.** The telemetry lane counted 120 anonymous events from 74 sessions by the afternoon, with no cookie and no IP address. And six [synthetic readers](https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/index.html), a board member, a CTO, a project manager, a security lead, a developer and a designer, each read the live site in a real browser on its own device, follow their own reading path, and say whether they got their answer, each into its own private vault. They are a test instrument, not readers, and the site says so.

!shot po-numbers.webp | images/ | The site in numbers at v0.5.5: 34 versions in one day, 144 sources in its export of the vault, 70 claims, 68 events, 16 agencies, 724 inventory rows, 209 graph nodes, 15 readers and briefings, 110 sections with 207 versions, 341 items, 17 team members, 8 vaults, 328 pages in the site's export of the source watch, 6 synthetic readers, 70 claims graded and 89 board items. | comparison

## Since 8pm {#since}

!shot ay-layers.webp | images/ | From attempts to a named compromise, as of 20:50 UTC on 22 October: millions of attempts; three security vendors reporting exploitation without naming a victim; one named organisation saying it was attacked, with the attack stopped; and none saying php2shell was the way in. | comparison

By 22:00 the story's site had gone from v0.5.5 to [v0.6.0](https://php.oct.2026.newsroom.sgit.ai/admin/versions.html), in five more versions. The ones that change the story:

- **The compromise map (v0.5.9, 21:06 UTC).** A [page of its own](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html) for one statement: "No named organisation has said it was compromised through php2shell", as of 20:50 UTC. It searched the evidence vault's 184 sources, 773 pages watched hourly from 474 publishers in 57 countries, 3,444 news items and 295 named sites probed every 30 minutes. It found millions of attempts; three vendors, Hadrian, Patchstack and Amazon, reporting exploitation without naming a victim; one named organisation, the Czech Technical University, saying it faced an attack that was stopped; one Japanese company reporting a break-in without a cause; another that blamed the PHP flaw and then corrected itself; and none saying php2shell was the way in. The site moved its own claim from "confirmed" to "reported", because it is "a time-bounded absence, not a confirmed fact". I take this further, with three readings of the silence, in [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html).
- **The second fact-check run (v0.5.8, 20:58 UTC).** It found the PHP security team's public answer to the incomplete-fix report, opened an eleventh contradiction, and recorded that the US catalogue still lists neither flaw. When I checked at 22:09 UTC, its latest edition was still the one released at 14:04 UTC on 21 October.
- **Risk and compliance (v0.6.0, 21:44 UTC).** A new [section](https://php.oct.2026.newsroom.sgit.ai/grc/index.html) with risk registers for php2shell: 34 risks assigned to 53 stakeholders, each joined to its weakness, CVE, fix and code, and mapped to 95 controls in 20 frameworks, from GDPR and NIS2 to ISO 27001. A data protection officer joins the readers, with a briefing on the GDPR 72-hour clock.
- **Readers.** The telemetry lane counted 235 anonymous events from 161 sessions by 20:35 UTC, against 120 from 74 in the afternoon.

The snapshot below stays as it was at 8pm; the next update will compare against it.

## A map for the next update {#map}

A story like this changes by the hour, and so does the site. So with this article I am publishing [a snapshot](https://newsroom.sgit.ai/articles/data/php-october-at-8pm__snapshot.json) of where everything was at 8pm: the site's version and commit, the evidence vault's head and counts, the source watch's head, the inventory's head and counts, the fact-check run, what I checked outside, every count in this tour, and the hash of each of the site's 46 data files. The next update will take the same snapshot, and the difference between the two will be the update: which data changed, which sections got a new version, which claims moved.

## What the day showed {#lessons}

Three things I want to keep from today.

**The pages lag the evidence.** At 8pm I wrote that the machinery had outrun the evidence. Checked again at 22:45 UTC, after the researcher's latest pass, that was wrong, and how it was wrong is the lesson. The evidence vault's last capture is still from 11:34 UTC, and the site's own copies of its vaults are older still. But capture never stopped. The source watch, the second vault, ran at 17:15, 18:16, 19:15 and 20:34 UTC, chased the compromise leads, read 339 pages in their own language, and probed 295 named sites every 30 minutes until 21:08: by then 773 pages and 1,851 dated snapshots. I read the site's export of the watch, not the watch, and reported its last run as 15:11. The Dutch inventory's rows did last change at 15:28 UTC; its later commits only reformat its changelog. And the vendor reports of exploitation that I said were not captured were: Patchstack's, through Recorded Future, and Hadrian's, through SecurityWeek, have been in the evidence vault since about 11:30 UTC, and the compromise map cites them. So the gap is not between the story and the capture; it is between the capture and the pages. The next priority is to close it: move the watch's snapshots into the evidence vault, and refresh the site's copies, as often as the watch runs.

**Grading finds our own mistakes.** The fact-check desk refuted a date that our own first section had in its description. That is the point of having it, and the correction is in this release.

**Versions make an update possible.** Because every section, fact and file is versioned, "what changed since 8pm" will be a question with an exact answer, not a rewrite.

## What this does not claim {#limits}

- **The story facts are as captured.** The evidence vault's latest capture is 11:34 UTC; the source watch's runs continued into the evening.
- **Two checks are mine, at 19:00 UTC.** The exploited-vulnerabilities catalogue and php.net's news, read directly, not yet captured into the vault.
- **The counts are from the site's data files.** At commit 2e0a2bbd, v0.5.5, 19:04 UTC; the site has probably changed since.
- **The fact-check grades are the desk's.** One run, by one agent, against the vault.
- **The synthetic readers are not readers.** Their reviews are prompts for the team, not evidence of readership.

## Where this comes from {#sources}

The site [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/) at v0.5.5 and its [public repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP), read from a clone at 19:04 UTC; the public evidence vault, cloned with its read key at head 31ccc515c29f; the [NCSC-NL inventory](https://github.com/NCSC-NL/php2shell) at 94b4b16; CISA's known exploited vulnerabilities feed and php.net's 2026 news archive, read at 19:00 UTC; and screenshots of the live site taken at 19:06 UTC. Related: [capture first](https://newsroom.sgit.ai/articles/capture-first.html), [a desk anyone can open](https://newsroom.sgit.ai/articles/a-desk-anyone-can-open.html), [the PHP flaws section](https://newsroom.sgit.ai/php-flaws/index.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
