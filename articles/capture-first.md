# Capture first: how a BBC live page at breakfast became an evidence vault, a section here and a site of its own by lunchtime, for a story that was still changing as we covered it, sgit.ai

> On the morning of 22 October I was reading the BBC's live page on two critical flaws in PHP, the language behind WordPress, Wikipedia and a large share of the web. Governments were telling organisations to take websites offline, a figure of 70% of the internet was going round, and some of the numbers did not add up. I asked the newsroom's agent to read the page, and then to set up a section and a vault to capture evidence. The vault was created at 08:03 UTC, eight minutes after the agent's first copy of the BBC page. The section was pushed at 08:13 with one source. Four collecting agents went out by beat: the primary sources, the researchers, the governments, the news. At 09:27 a second session released the first version of a site of its own, php.oct.2026.newsroom.sgit.ai, which reads the same vault. By 12:05 the vault held 184 sources, 177 dated captures and 855 files hashed at the moment of capture, from six writers. This is the newsroom's first story covered while it was breaking, and the order we did things in is the argument: capture first, because a live page, a down page and a social post change or disappear within hours, and a claim can only be checked later against the bytes someone kept. It also showed what went wrong. Two of the four agents stopped before committing, and forty sources, including the maintenance pages of French prefectures, sat in their working folders until the lead agent found them. The section here was the first step; the dedicated site is where the facts now live, and this newsroom keeps the context and the opinion. The plan is to retire the section once the site has taken everything over.

*Source: <https://newsroom.sgit.ai/articles/capture-first.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Capture first: how a BBC live page at breakfast became an evidence vault, a section here and a site of its own by lunchtime, for a story that was still changing as we covered it

# Capture first: how a BBC live page at breakfast became an evidence vault, a section here and a site of its own by lunchtime, for a story that was still changing as we covered it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-22 · [article v1.1.0, 3 versions](versions/capture-first.md) · [newsroom v0.13.41](https://newsroom.sgit.ai/admin/versions.html) · php2shellbreaking-newsevidenceprovenancevaultsarticle

***Abstract:** On the morning of 22 October I was reading the BBC's live page on two critical flaws in PHP, the language behind WordPress, Wikipedia and a large share of the web. Governments were telling organisations to take websites offline, a figure of 70% of the internet was going round, and some of the numbers did not add up. I asked the newsroom's agent to read the page, and then to set up a section and a vault to capture evidence. The vault was created at 08:03 UTC, eight minutes after the agent's first copy of the BBC page. The section was pushed at 08:13 with one source. Four collecting agents went out by beat: the primary sources, the researchers, the governments, the news. At 09:27 a second session released the first version of a site of its own, php.oct.2026.newsroom.sgit.ai, which reads the same vault. By 12:05 the vault held 184 sources, 177 dated captures and 855 files hashed at the moment of capture, from six writers. This is the newsroom's first story covered while it was breaking, and the order we did things in is the argument: capture first, because a live page, a down page and a social post change or disappear within hours, and a claim can only be checked later against the bytes someone kept. It also showed what went wrong. Two of the four agents stopped before committing, and forty sources, including the maintenance pages of French prefectures, sat in their working folders until the lead agent found them. The section here was the first step; the dedicated site is where the facts now live, and this newsroom keeps the context and the opinion. The plan is to retire the section once the site has taken everything over.*

The morning of 22 October 2026 in two lanes, UTC: the story as its sources date it, and the newsroom's captures.

## In short

- **A breaking story is a race against the page changing.** The BBC live page grew a new post between our first copy at 07:55 UTC and our second at 08:04; the sites taken offline were on maintenance pages at 08:19 and may not be by the evening.
- **So the first thing built was the vault, not the page.** An encrypted sgit vault created at 08:03, with a capture tool that keeps the page as served, as rendered, its text, a screenshot and its headers, and the sha256 of each.
- **Captures are only added.** A live page captured three times is three dated folders; the series is the record of how the story moved.
- **Several agents, one vault, no shared file.** Each source has its own row and each agent its own claims and timeline files, so four collectors and two site agents wrote at once.
- **The figures that did not add up are now pinned to their sources.** "70%" is a headline; the body of the same post says 70% of websites; one scanning vendor counts 2.6 million hosts; one national CERT counts about 6,000 resources.
- **The agencies disagree, and the vault shows it.** The NSA and CISA say take systems offline if you cannot patch; the NCSC in the Netherlands does not advise it at all.
- **What went wrong is part of the record.** Two collecting agents stopped before committing; forty sources were recovered from their folders hours later.
- **The story now has a site of its own.** php.oct.2026.newsroom.sgit.ai, built from the same vault, facts only; the section here retires once the move is done.

## What I was reading at breakfast

The BBC opened a live page at 06:16 UTC on 22 October: "Global scramble to fix critical cyber-security flaws as many websites taken offline". Two flaws in PHP, found with the help of AI, a coordinated disclosure that broke down when the details leaked, and agencies in the UK, the US, the EU and Australia telling organisations that could not patch to take their systems offline. Among the sites named as affected were parts of Wikipedia, Edinburgh council, French government services, the University of Geneva and the BBC itself.

Some of it did not add up. "Roughly 70%" of the internet, attributed to Wiz and flagged by the BBC as a figure it could not verify, sat a few posts away from "something like 30 million websites". I have been in security for a long time, and as I said in the memo that followed, "I don't buy that 70% of websites out there, especially some sort of websites that matter," are exposed with nothing else in the way. A remote code execution flaw on a web server is serious; what it means for a given site depends on what is on the server, what credentials it holds and what sits between it and the attacker. That is a [blast radius](footprint-and-blast-radius.md) question, and the reporting was not asking it yet.

So I asked the newsroom's agent to read the page. It fetched it at 07:55 and gave me a summary of twelve posts. Then I asked for what this site had not done before: a section about a story that was still moving, and a vault behind it.

## Capture before you write

The order matters, and it is the point of this article. A finished article can wait; the evidence for it cannot. A live page is rewritten every few minutes. A site that is down this morning will be up tonight, and its maintenance page will be gone. A social post can be deleted, and in this story one already had been: the researchers' demonstration video, published by mistake and taken down.

The vault was created at 08:03, before there was a page to put anything on. Its first capture of the BBC page, at 08:04, is already different from the 07:55 copy: a new post had appeared at 08:00, with the researcher who found the flaw saying on Radio 4 that there was no evidence of exploitation yet. That post is in the second capture and not in the first. Nobody has to trust me on that; the two files, and their hashes, are in the vault.

The capture tool is a short script that opens the page in Chromium and keeps six things in a dated folder: the page as the server sent it, the page after its scripts ran, its visible text, a full-page screenshot, the response headers, and a provenance file with the time, the user agent and the sha256 of every file. The first version got one of those wrong. The raw page came back empty, and the fallback was blocked by the session's network policy; the third capture, at 08:06, was the first complete one. One test capture was discarded while the tool was being written, before anything was committed; since the first commit, at 08:06, all three captures of the BBC page are kept, because a capture is never edited or deleted. A live page captured many times leaves a series, and the series is the record of how the story moved. This is the method this site has argued for since [the story vault](future-of-news-story-vault-not-paywall.md): keep the evidence the article is made from, frozen and hashed, and treat the article as one walk through it.

## A section in ten minutes, and agents by beat

At 08:13 the section [/php-flaws/](https://newsroom.sgit.ai/php-flaws/index.html) went out with one source. It said what we knew, each point with its source; what we did not know; a timeline in which every date is as its source states it, with the ones we worked out marked inferred; and the claims, each marked reported, confirmed, disputed or unverified. The status line said Developing. The captures themselves are third-party pages, so they are not republished: the section lists each capture with its hashes, and links to the originals.

At the same time four agents went out, one per beat. One for the primary sources: the php.net advisory, the CVE records, the GitHub advisories, the patched releases. One for the researchers: Calif, Wiz, OpenAI, Cloudflare, and the leak. One for the governments: sixteen national agencies in the end, and the government sites that went down. One for the news and the impact, with the instruction to capture the maintenance pages while they were still up. Each cloned the vault, read its README, and followed the same protocol.

The protocol had to change in the first half hour. The first version had one manifest that every agent appended to, and one claims file. Several agents writing to one file is a merge conflict waiting to happen, so before the agents had written much, each source got its own row in its own folder, and each agent its own claims and timeline files, merged by the build. This is the pattern [two agents, one vault](two-agents-one-vault.md) described for the Industry Wire, with more writers: a vault one agent writes and another reads, with the history as the audit trail.

Who wrote the 184 sources in the evidence vault by 12:05 UTC, and what reads it.

## Following the link someone sends

At 08:47 I sent the agent a link: the NCSC in the Netherlands keeps a repository on GitHub, php2shell, with an inventory of software that may be affected. The government agent had already captured its front page at 08:09. What the link was for was the inventory itself, and an inventory in a git repository changes by the hour.

So the agent kept the whole repository: a git bundle with all 52 commits, the files at commit cca173c64ec5, and the inventory parsed into rows. At that commit it lists 674 products: 206 marked Vulnerable, 46 with a Fix, 418 under Investigation, 3 Not vulnerable and one without a status. The NCSC-NL calls the entries "investigation leads" until a vendor or upstream source backs them, and the section says so. A count like 674 is only useful with the commit it was counted at, because the next pull request changes it.

The same repository gave the CVE numbers, CVE-2026-109618 and CVE-2026-109619, and the fixed releases, PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. It also gave the first clear disagreement between agencies: the Dutch guidance is to patch, or apply PHP's temporary mitigations, and it does not advise taking systems offline.

## The numbers, pinned to what they measure

By late morning the vault could answer the question I started with. The dedicated site's [numbers page](https://php.oct.2026.newsroom.sgit.ai/numbers/index.html) puts six figures side by side, each with who said it and what it measures. "70%" of the internet is a headline on Wiz's post; the body of the same post, Cloudflare and OpenAI say about 70% of websites, which is the share of sites whose server-side language is PHP, from surveys none of them names. One scanning vendor counts 2,608,039 internet-facing hosts running PHP, through The Hacker News. Alan Woodward's "something like 30 million websites" comes with no basis given. Latvia's CERT counts about 6,000 potentially affected resources in one country, a few hundred of them in the public sector.

None of those figures is wrong as a statement about what it measures. They measure different things: a language's share of websites, a host count, a national scan. Put next to each other, the 70% stops being a measure of exposure, and the question becomes the one in my memo: what is on the other side of each of those servers, and what stands in front of it. As I said there, "a zero day like this is not invisibility cloak": exploitation leaves signals, and by noon every claim of exploitation in the vault was of attempts, probes and a honeypot hit, with no agency confirming a compromise.

The agencies' advice is the other thing the vault made visible. The NSA and CISA say take systems offline if you cannot patch; the UK's NCSC puts that after patching and temporary mitigations; Australia, the Netherlands, Italy, Japan and New Zealand give no offline advice. In the second memo I said that "putting a website offline is an option, but should be like at the end of a long sequence of events", and that a company should still be able to do it quickly. Sixteen agencies, side by side, show how differently that sequence is being written.

## What went wrong

When I asked at midday whether the vault had been pushed, the honest answer was not quite. Two agents had commits waiting: the primary-sources agent had six, and the researchers' agent had four that had fallen behind the vault, so its pull reported 224 conflicts. Of those, 223 were the same bytes on both sides, and the one real difference was the generated manifest, which is rebuilt rather than merged.

The bigger gap was in two working folders. The news agent and the government agent had both stopped before committing. Between them they held forty sources that were nowhere else: news coverage from Switzerland, France, Portugal and Australia, and the sites themselves, captured at 08:19 while two French prefectures showed "Site en maintenance" and the University of Geneva returned a 503. Edinburgh council's home page loaded normally at the same minute; a page that was up is evidence too. The lead agent committed them with rows written from each capture's provenance file, said in each row who wrote it and why, and pushed them.

Two rules come out of it. An agent commits after every source, not at the end of its beat. And the lead agent checks every clone, not only its own, before saying the vault is complete. Neither is in the protocol yet; both are now on the list.

## A site of its own

The section was the first step, and the right size for the first hour. In my second memo I said what the story needed: a dedicated site, as fact-driven as we can make it, with briefings for each kind of reader, from the journalist to the board member, and with this newsroom keeping the context and the opinion. A second session started on it, read the same vault, and released [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/) at 09:27 as v0.1.0. By 12:05 it was at v0.2.2, with a page per source and per party, the numbers, the agencies compared, the inventory, an impact ledger of offline against compromised, and twelve briefings, each one selecting from the same claims rather than adding to them. Its agent also became the vault's largest writer, with 83 of the 184 sources.

That leaves two places with the same story, which is one too many. The plan is to move everything the section does to the dedicated site, link to it from the front page of this newsroom while it is moving, and then retire the section, leaving a page at its address that points to the site. The briefing for the site's team says what has to be true before that happens: every source the section lists is on the site, the site publishes a small status file this newsroom can read, and the links into the section keep working.

This is the [explorer, villager and town planner](explorer-to-villager-newsroom.md) handover inside one day. The section was explorer work: fast, one agent, built to find out what the story needed. The dedicated site is the villager: its own repository, its own gate, its own releases. What the newsroom keeps is the part only a newsroom does: saying what the story means.

## Where things stand

At 12:05 UTC the vault holds 184 sources, 177 dated captures and 855 files hashed at capture, from six writers, with 61 claims and 67 timeline events in per-agent files. The section here is live with the first of those; the dedicated site is live with all of them, and is where to read the story now. Nothing is anchored yet: the hashes are recorded in the vault and published on the sources pages, which proves the bytes have not changed since they were published, not that they existed at the time stated.

The next steps are the ones in my memos: the exposure mapped from the assets outwards, exploitation counted over time rather than reported once, the steps for anyone running PHP backed with evidence, and the graph of who said what first. The vault was the part that had to happen this morning.

## What this does not claim

- **This is one morning, as one newsroom saw it.** The times are from the BBC page, the capture files and two git logs; other people covering the story will have their own.
- **The vault is private, so the captures cannot be checked by a reader yet.** What is published is each capture's hash and the time it was made; opening the vault to a reviewer is what turns the hashes into a check.
- **A hash proves the bytes did not change after it was published, not when they were captured.** Nothing in the vault is anchored to an outside timestamp yet.
- **The figures in the numbers section are as the sources state them.** We did not measure PHP's share of the web, or scan anything ourselves.
- **Most of the work was done by agents, and an agent can be wrong.** The claims carry a status for that reason, and the sources a reader can follow.
- **Nothing here is advice on what to patch.** For that, read the php.net advisory and your national agency.
- **The two lessons from what went wrong are not in the protocol yet.** They are recorded, and the next release of the protocol is where they go.

If you are covering this story, or run PHP and want to compare what you see with what the vault holds, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

The origin is a conversation of mine with the newsroom's agent on the morning of 22 October 2026: a link to the BBC live page, then "let's create a dedicated section of this site about this, starting with a dedicated section and a vault to capture evidence", then a link to the NCSC-NL repository, then two voice memos for the dedicated site, which its repository publishes as transcripts. This article was written by this site's agent in my voice; the argument and the editorial responsibility are mine.

Sources, all captured into the evidence vault on 22 October 2026: the [BBC live page](https://www.bbc.co.uk/news/live/ckgel5xp2xv9t), opened 06:16 UTC, edited by Kieran Kelly and Imogen James; the [NCSC-NL php2shell repository](https://github.com/NCSC-NL/php2shell), at commit cca173c64ec5, 22 October 08:40 UTC; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) of 21 October; and, for the numbers and the agencies, the pages the dedicated site cites on its [numbers](https://php.oct.2026.newsroom.sgit.ai/numbers/index.html) and [agencies](https://php.oct.2026.newsroom.sgit.ai/agencies/index.html) pages, each with its capture. The dedicated site's code and brief are in [SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP).

The counts were made from the vault at 12:05 UTC: sources from every `sources/*/source.json`, captures and hashed files from every capture's `provenance.json`, claims and events from `claims/*.json` and `timeline/*.json`; the inventory from the parsed `software_list_*.md` at commit cca173c64ec5; the times of the section and the site from the two repositories' git logs. The figures were drawn for this article.

## Threads

Vaults & method[This article as a graph →](graphs.md#capture-first)

### Builds on

- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.

### Continued by

- [A desk anyone can open: the PHP story's work and who did it, nine names with their responsibilities, and an evidence vault anyone can now read, scanned before its key was published](a-desk-anyone-can-open.md) The PHP story's work and who did it, nine names with their responsibilities, and its evidence vault opened to everyone, scanned before the key was published.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 259 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=259)

**Posting this article on LinkedIn?** The cover is [capture-first.jpg](banners/capture-first.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/capture-first.html)*
