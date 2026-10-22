# PHP October 2026, at 8pm: where the php2shell story stands, and a guided tour of the site that tracks it, built in one day by a team of agents from an evidence vault anyone can read, sgit.ai

> At 8pm UK time on 22 October, this is where the php2shell story stands. The fix has been out since 21 October; sixteen agencies say install it; attackers are trying, in large numbers, and Amazon saw an attempt four days before the announcement; no organisation has confirmed a break-in, and the US list of flaws known to be used in attacks still does not include these two. The Dutch inventory of affected software has 724 rows, and only 61 of them have a fix. And behind that update is something I want to show properly: php.oct.2026.newsroom.sgit.ai, a site built today, from 09:27 to 19:04 UTC, in 34 versions, by two people and thirteen agents. It reads an evidence vault of 184 sources and 177 dated captures, now public. It has a front page in plain English and fifteen briefings, 70 claims each graded by a fact-check desk, ten contradictions in a ledger, a graph of 209 nodes, the fix read in the code, the inventory hour by hour, every section versioned, a phone app, synthetic readers and eight vaults. This is a guided tour of it, with the versions of everything, so the next update can say exactly what changed.

*Source: <https://newsroom.sgit.ai/articles/php-october-at-8pm.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / PHP October 2026, at 8pm: where the php2shell story stands, and a guided tour of the site that tracks it, built in one day by a team of agents from an evidence vault anyone can read

# PHP October 2026, at 8pm: where the php2shell story stands, and a guided tour of the site that tracks it, built in one day by a team of agents from an evidence vault anyone can read

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-22 · [article v1.0.0](versions/php-october-at-8pm.md) · [newsroom v0.13.43](https://newsroom.sgit.ai/admin/versions.html) · php2shellbreaking-newsevidencevaultsversionsarticle

***Abstract:** At 8pm UK time on 22 October, this is where the php2shell story stands. The fix has been out since 21 October; sixteen agencies say install it; attackers are trying, in large numbers, and Amazon saw an attempt four days before the announcement; no organisation has confirmed a break-in, and the US list of flaws known to be used in attacks still does not include these two. The Dutch inventory of affected software has 724 rows, and only 61 of them have a fix. And behind that update is something I want to show properly: php.oct.2026.newsroom.sgit.ai, a site built today, from 09:27 to 19:04 UTC, in 34 versions, by two people and thirteen agents. It reads an evidence vault of 184 sources and 177 dated captures, now public. It has a front page in plain English and fifteen briefings, 70 claims each graded by a fact-check desk, ten contradictions in a ledger, a graph of 209 nodes, the fix read in the code, the inventory hour by hour, every section versioned, a phone app, synthetic readers and eight vaults. This is a guided tour of it, with the versions of everything, so the next update can say exactly what changed.*

A guided tour of php.oct.2026.newsroom.sgit.ai in nine pages: the front page for everyone, the inventory hour by hour, the story as a graph, every section versioned, a source and its captures, the fix read in the code, the team, the eight vaults, and the six synthetic readers.

## In short

- **The fix is out; the advice is unanimous.** Install PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35.
- **Attackers are trying.** Millions of attempts; one seen four days before the announcement.
- **No confirmed break-in yet.** And the US list of exploited flaws does not include these two.
- **724 affected products listed; 61 fixed.** 440 still under investigation.
- **A whole site, built today.** 34 versions, two people, thirteen agents.
- **Everything rests on a vault anyone can read.** 184 sources, 177 dated captures.
- **The versions of everything are recorded.** So the next update can be compared with this one.

## Where the story stands at 8pm

On the morning of 22 October I was reading the BBC's live page about two critical flaws in PHP, the software that WordPress and a large share of the world's websites run on. In [capture first](https://newsroom.sgit.ai/articles/capture-first.html) I described how that page became an evidence vault, a section on this site and then a site of its own, [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/), by lunchtime. This is the evening update, at 8pm UK time, 19:00 UTC.

What the evidence shows:

- **The flaws and the fix.** Two flaws, [CVE-2026-109618 and CVE-2026-109619](https://php.oct.2026.newsroom.sgit.ai/flaws/index.html), both rated 9.2 out of 10, in PHP itself. The fix is in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October. PHP 8.1 and older have no ready-made fix. Those four releases and the advisory were still the latest entries in php.net's news when I checked at 19:00.
- **When it was disclosed.** On 21 October, not 22 October as many reports, and the first version of our own section, said. The primary records date it to the afternoon of 21 October UTC; the site's fact-check desk graded "disclosed on 22 October" as refuted today, and we have corrected our section.
- **What governments say.** [Sixteen agencies](https://php.oct.2026.newsroom.sgit.ai/agencies/index.html) agree on one thing: install the fix now. They disagree on what to do if you cannot: the US says take the website offline, the UK lists that as a last resort, several European agencies say cut it off from the public internet.
- **Exploitation.** Attackers are trying. Cloudflare's chief executive reported millions of attempts; Amazon reported an attempt against one of its decoy servers on 17 October, four days before the announcement. Other security companies report attempts too; one reported seeing none on its partners' systems on the evening of 21 October.
- **Compromise.** No organisation has confirmed it was broken into through these flaws, in anything the vault has captured. At 19:00 the US government's [catalogue of known exploited vulnerabilities](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) still did not list either flaw; its latest edition was released at 14:04 UTC on 21 October.
- **Systems taken offline.** [Ten entries](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) in the site's ledger of organisations that took websites offline as a precaution, from the Dutch government's login service to UK councils and game wikis. Taken offline is not the same as compromised, and the site keeps them in separate ledgers.
- **Affected software.** The Dutch national cyber security centre keeps a public list of software that ships or depends on PHP. At its latest version, 15:28 UTC, it had 724 rows: 61 fixed, 216 vulnerable, 440 still under investigation, 6 not affected.
The Dutch inventory of affected software, at each of its 38 versions from 21 October: 724 rows at 15:28 UTC on 22 October, of which 61 fixed, 216 vulnerable and 440 still under investigation.

## What we still do not know

- **Whether any website was broken into** before it installed the fix.
- **Whether the fix is complete.** A relayed report on 21 October suggested it may not be; the fact-check desk grades that "not shown".
- **How many systems are still unpatched.** One count is open in the [contradiction ledger](https://php.oct.2026.newsroom.sgit.ai/factcheck/index.html), with no second measure to settle it.
- **Who leaked the news on 20 October**, and whether any technical detail leaked with it.
- **Where the "70% of the internet" figure comes from.** It is roughly the share of websites built with PHP, not a measure of how many are at risk.

## A site built in one day

One day, 34 versions of php.oct.2026.newsroom.sgit.ai, from v0.1.0 at 09:27 UTC to v0.5.5 at 19:04 UTC, with two lines of versions running in parallel until the design branch was merged into v0.4.0.

The site's first version went out at 09:27 UTC. The thirty-fourth, v0.5.5, went out at 19:04. In between, 62 commits, two lines of versions developed in parallel and merged, and a team that grew through the day: the [team page](https://php.oct.2026.newsroom.sgit.ai/team/index.html) now lists 17 members, two of them people, a project manager and me as the editor, and 13 agents, each with a role, what it owns, the rules it works by and the work it has shipped. Their tasks are on a board of 89 items, 25 of them done.

I want to be precise about what I did. I read, I sent voice memos, I pointed agents at sources and decided what mattered. The agents captured the evidence, wrote the data, built the pages, checked each other, and released. The site's own [release history](https://php.oct.2026.newsroom.sgit.ai/admin/versions.html) has every version with what it changed.

## The tour

There is a lot here, so this is the route I would take a colleague through.

**1. The front page, for everyone.** The [front page](https://php.oct.2026.newsroom.sgit.ai/) starts in plain English: what happened, what to do, what is not known, every line linked to the sources it rests on. Then it splits by reader. [Start here](https://php.oct.2026.newsroom.sgit.ai/start/index.html) maps fifteen readers, from a curious reader to a CISO, a CFO, a journalist and a PHP engineer, each with a thirty-second answer and a reading path, and each has [a briefing](https://php.oct.2026.newsroom.sgit.ai/briefings/board/index.html). There is a glossary of 40 terms, linked on first use on every page, and [ten questions readers ask](https://php.oct.2026.newsroom.sgit.ai/questions/index.html), each with a short answer to paste back to whoever asked you.

On a phone: the front page, and Now, which answers what to know for the time you have, one, five, ten or thirty minutes, from the data alone or written by a model with the reader's own key.

**2. On a phone.** [Now](https://php.oct.2026.newsroom.sgit.ai/now/index.html) asks how much time you have, one, five, ten or thirty minutes, and gives you what you have not read yet. "From the data" is built from the site alone. "Written for me" uses a model with your own key, kept in your own vault, and every claim it makes must cite an item on the site. Since v0.5.4, every page also has an Ask pane: you talk to the site with your own key, the model can only use the site's read-only tools, every call is shown, every fact is cited to an item, and it changes nothing without your say-so.

**3. The evidence.** Everything rests on the evidence vault. It holds 184 sources and 177 dated captures, each with the page as served, the rendered page, its text, a full-page screenshot, the headers and a sha256 hash, from six writers, from 08:05 to 11:34 UTC. Since this afternoon it is [readable by anyone](https://newsroom.sgit.ai/articles/a-desk-anyone-can-open.html), with a public read key that cannot write, after a scan of all its files. Every [source page](https://php.oct.2026.newsroom.sgit.ai/sources/bbc-live-ckgel5xp2xv9t/index.html) on the site shows its captures, their times and their hashes, and the claims that cite it. A second vault, the [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html), checks the outside sources on a schedule: 328 pages from 175 publishers in 38 countries and 32 languages, with 440 snapshots, and what access each allows, open, behind a bot challenge, down or gone.

**4. The analysis, graded.** The site has [70 claims](https://php.oct.2026.newsroom.sgit.ai/claims/index.html), each with a status and its sources, [68 timeline events](https://php.oct.2026.newsroom.sgit.ai/timeline/index.html), [17 numbers](https://php.oct.2026.newsroom.sgit.ai/numbers/index.html) pinned to what they measure, and an [impact ledger](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) that keeps offline and compromised apart. Tonight the [fact-check desk](https://php.oct.2026.newsroom.sgit.ai/factcheck/index.html) finished its first run: all 70 claims graded against the vault on a scale from A0, unsupported, to A6, with a verdict for each. 39 hold, 28 hold in part, one is not shown and two are refuted: the 10.0 severity score from the leak, and the 22 October disclosure date. It opened 143 tickets and a ledger of ten contradictions, five explained and five open, each with what would settle it.

**5. The story as a graph.** The [graph](https://php.oct.2026.newsroom.sgit.ai/graph/index.html) has 209 nodes and 281 edges: the 70 claims, the 68 events and the 71 sources they cite. It is drawn from the same rows as the pages, so the picture cannot disagree with the text.

**6. The fix, read in the code.** The [code page](https://php.oct.2026.newsroom.sgit.ai/code/index.html) answers the question I asked in the morning, where the flaw actually lives, from a clone of php-src rather than from any article: the fix commit, its parent, the branch it landed on, the backport to an end-of-life branch, and the files it changed, mapped as [layered graphs](https://php.oct.2026.newsroom.sgit.ai/review/index.html).

**7. Patching and the inventory.** [Patching](https://php.oct.2026.newsroom.sgit.ai/patching/index.html) explains who can get a fix for which version of PHP, the six ways a fix reaches a server, and why not every version gets one. [The inventory, hour by hour](https://php.oct.2026.newsroom.sgit.ai/patching/inventory/index.html) reads the Dutch list from its public history, every change of status, and the first recorded fix from each supplier.

**8. Stories, and context.** Research and stories are kept apart, with a strip at the top of every page saying which it is. [Five house stories](https://php.oct.2026.newsroom.sgit.ai/articles/index.html), by the site's journalist, historian and cyber desk, among them [exposed is not exploited](https://php.oct.2026.newsroom.sgit.ai/articles/exposed-is-not-exploited/index.html), and an [interview with me](https://php.oct.2026.newsroom.sgit.ai/interview/index.html). And [in context](https://php.oct.2026.newsroom.sgit.ai/context/index.html), php2shell against earlier flaws from 2008 to 2026.

**9. Versions, of everything.** This is the part I care most about. Every section of the site, every briefing, front-page section and story, is hashed on every build and gets a new version only when its text changes: 110 sections, 207 versions so far, in a [table of release against section](https://php.oct.2026.newsroom.sgit.ai/versions/index.html). Every fact has its own timeline. And the site tracks [341 items a reader can follow](https://php.oct.2026.newsroom.sgit.ai/whatsnew/index.html), so it can say what is new or changed since your last visit, in your browser, with nothing sent anywhere.

**10. The vaults and the team.** [Eight vaults](https://php.oct.2026.newsroom.sgit.ai/vaults/index.html) sit behind the site: the evidence and the source watch, public read-only; the anonymous telemetry and the subscriptions, each written through a lane that can add and cannot read; the coverage of other outlets, private, because it holds other people's pages; and three the team coordinates through, the conductor's, the issues and the mail. Every vault is encrypted in the browser or the agent's session; the server holds ciphertext.

**11. The readers, real and synthetic.** The telemetry lane counted 120 anonymous events from 74 sessions by the afternoon, with no cookie and no IP address. And six [synthetic readers](https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/index.html), a board member, a CTO, a project manager, a security lead, a developer and a designer, each read the live site in a real browser on its own device, follow their own reading path, and say whether they got their answer, each into its own private vault. They are a test instrument, not readers, and the site says so.

The site in numbers at v0.5.5: 34 versions in one day, 144 sources in its export of the vault, 70 claims, 68 events, 16 agencies, 724 inventory rows, 209 graph nodes, 15 readers and briefings, 110 sections with 207 versions, 341 items, 17 team members, 8 vaults, 328 watched pages, 6 synthetic readers, 70 claims graded and 89 board items.

## A map for the next update

A story like this changes by the hour, and so does the site. So with this article I am publishing [a snapshot](https://newsroom.sgit.ai/articles/data/php-october-at-8pm__snapshot.json) of where everything was at 8pm: the site's version and commit, the evidence vault's head and counts, the source watch's head, the inventory's head and counts, the fact-check run, what I checked outside, every count in this tour, and the hash of each of the site's 46 data files. The next update will take the same snapshot, and the difference between the two will be the update: which data changed, which sections got a new version, which claims moved.

## What the day showed

Three things I want to keep from today.

**The machinery outran the evidence.** The vault's last capture is from 11:34 UTC; the source watch last ran at 15:11; the inventory last changed at 15:28. The site gained a new version every twelve minutes or so through the afternoon, but its account of the story is a morning account. The next priority is scheduled capture, which the site's own brief already asks for, so that the evening's reporting enters the vault before it enters a page. Tonight a search finds security vendors' reports of confirmed exploitation that are not yet captured; until they are, they are not facts here.

**Grading finds our own mistakes.** The fact-check desk refuted a date that our own first section had in its description. That is the point of having it, and the correction is in this release.

**Versions make an update possible.** Because every section, fact and file is versioned, "what changed since 8pm" will be a question with an exact answer, not a rewrite.

## What this does not claim

- **The story facts are as captured.** Mostly from the morning; the vault's latest capture is 11:34 UTC.
- **Two checks are mine, at 19:00 UTC.** The exploited-vulnerabilities catalogue and php.net's news, read directly, not yet captured into the vault.
- **The counts are from the site's data files.** At commit 2e0a2bbd, v0.5.5, 19:04 UTC; the site has probably changed since.
- **The fact-check grades are the desk's.** One run, by one agent, against the vault.
- **The synthetic readers are not readers.** Their reviews are prompts for the team, not evidence of readership.

## Where this comes from

The site [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/) at v0.5.5 and its [public repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP), read from a clone at 19:04 UTC; the public evidence vault, cloned with its read key at head 31ccc515c29f; the [NCSC-NL inventory](https://github.com/NCSC-NL/php2shell) at 94b4b16; CISA's known exploited vulnerabilities feed and php.net's 2026 news archive, read at 19:00 UTC; and screenshots of the live site taken at 19:06 UTC. Related: [capture first](https://newsroom.sgit.ai/articles/capture-first.html), [a desk anyone can open](https://newsroom.sgit.ai/articles/a-desk-anyone-can-open.html), [the PHP flaws section](https://newsroom.sgit.ai/php-flaws/index.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

News & evidenceVaults & method[This article as a graph →](graphs.md#php-october-at-8pm)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 261 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=261)

**Posting this article on LinkedIn?** The cover is [php-october-at-8pm.jpg](banners/php-october-at-8pm.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/php-october-at-8pm.html)*
