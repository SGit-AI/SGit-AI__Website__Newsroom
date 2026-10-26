---
title: One researcher for every newsroom: a research site that works as a light, focused Internet Archive for the sources our stories rest on, captured on a schedule into a pack a day, published by licence tier, and shared by the PHP site, the wires and the Web Summit newsroom
date: 2026-10-26
author: Dinis Cruz
author_url: about/index.html
summary: Every newsroom we run has its own researcher. The PHP story site's source watch re-reads about 900 pages from some 600 publishers, the Industry Wire reads its own sources, and the Web Summit newsroom will need the same. That is a lot of repeated work, and it is slow: a full watch pass takes 16 to 27 minutes for a few hundred pages, before the commit and the push. Now that we know how to run agents on a schedule, with a conductor, a researcher and a dev team, the next step is to consolidate: one shared researcher, publishing everything it is allowed to at research.newsroom.sgit.ai, a light and very focused version of the Internet Archive. Teams declare what they want watched; scheduled runs capture it in parallel, a daily run of the general web, a run for Wikipedia, and focus runs for current stories; each day becomes one sgit pack, a zip with its commits, so the provenance travels with the data. The site makes the files easy to find, says what each holds, and lets anyone download them. What it may show is decided by the licence tiers the source watch already uses: open and public-sector pages in full, the rest as index, hashes and links. This is the design, for review before we build it.
version: v0.13.91
license: https://creativecommons.org/licenses/by/4.0/
tags: research, archive, provenance, sgit, vaults, agents, design, article
status: published
---

!shot rz-arch.webp | images/ | research.newsroom.sgit.ai, one researcher shared by every newsroom: a watch list of what to watch, who asked, how often and its licence tier; three kinds of scheduled run, the daily web, Wikipedia, and focus runs for current work; a pack a day in an sgit pack vault, with an index of what is inside; the research site, where tier A is published in full and tiers B and C as index, hashes and links; and the readers, the PHP story site, the Industry Wire, the Web Summit newsroom and anyone outside. Proposed. | process

## In short {#in-short}

- **Every newsroom runs its own researcher.** The same sources, read again and again.
- **It is slow.** A full watch pass is 16 to 27 minutes for a few hundred pages, before the push.
- **Consolidate:** one shared researcher, on a schedule, at research.newsroom.sgit.ai.
- **Three kinds of run, in parallel:** the daily web, Wikipedia, focus runs for current stories.
- **A pack a day.** One zip per day with its commits, so the provenance travels with the data.
- **Published by licence tier.** Open pages in full; the rest as index, hashes and links.
- **Each team then researches only what is not covered.**

## The problem: a researcher in every newsroom {#problem}

We now know how to run agents on a schedule, with a conductor, a researcher, a dev agent and several teams working on one site. The PHP story site does it every day. But look at what each newsroom does for its sources.

- **The PHP story site's source watch** re-reads about 900 pages, 913 in the site's data and 965 in the researcher's own count of 23 October, from some 600 publishers, in 34 languages and 60 country folders. It keeps a snapshot whenever a page changes: 2,946 so far.
- **The Industry Wire** reads its own sources into its own vault, for four wires.
- **The Web Summit newsroom** will need a feed of its own, from public material, [as the plan says](https://newsroom.sgit.ai/articles/web-summit-2026-the-plan.html).

Much of that is the same sources, read again. And it is slow. The researcher's own [proposal for a phased pass](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__phased-source-watch-pass/index.html) measured the watch stage at 16 to 27 minutes for 630 to 860 pages, with a real browser, 12 at a time, before the discovery, the series, the commit and the push; on the old vault format, a push of 5,000 objects took up to 30 minutes.

## A light, focused Internet Archive {#archive}

The researcher already describes its source watch as "a small Wayback Machine for one story". That is the right idea, and it should not be one per story.

So the proposal is research.newsroom.sgit.ai: a site focused on creating and publishing raw data. A light and very focused version of the [Internet Archive](https://web.archive.org/), and a focused news archive that we publish. It makes it easy to find the files, explains what files exist, and lets anyone download them. Underneath, they are just files in storage with encryption on them, in sgit vaults; for what we may share, we publish the read key, and anyone can open them.

What it adds to what the Internet Archive already does is focus and structure: the pages that matter to the stories we follow, captured on a known schedule, with a machine-readable index of what changed, when, with what access, under what licence. Few publishers offer their own history in a form a machine can use.

## How it would work {#design}

- **One watch list.** A registry of what to watch: the page, who asked for it, how often, its licence tier and its access. Set up once, then changed by agents and people: "here are the sites I want to keep an eye on; here are the ones I want an update on." The roughly 900 sources the PHP site follows are the first entries.
- **Runs split so they can go in parallel.** A tree of who is doing what, so that several sessions run at once and each finishes quickly:
  - **The daily web:** a generic run over the sources every story needs, news homepages, CERTs and agencies, feeds, vulnerability catalogues.
  - **Wikipedia:** a run of its own, for chosen articles and their revisions. Wikipedia is huge, changes all the time, and holds a lot of the shadow reporting that [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html) describes; the PHP site already [reads its article as a graph](https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/index.html).
  - **Focus runs:** requests from current work, the PHP story, the wires, Web Summit, each declared in the watch list.
- **A pack a day.** Each run writes a day's captures into an sgit pack vault: one zip per push, holding the commits, so the provenance travels with the data. Next to each pack, an index of what is inside, so nobody has to download a zip to know whether they need it.
- **A daily update.** The agents that consume the data say what is missing: "what about this, what about that." The watch list grows from their asks.
- **Each team keeps its researcher,** but it only looks at what the shared runs do not cover. That makes each one much more efficient, and gives every newsroom the same data source.

## Why pack mode makes it possible {#packs}

!shot rz-pack.webp | images/ | Why pack mode makes this possible: the source watch vault measured by the PHP site's researcher on 23 October 2026, as a normal sgit vault and as a pack vault; a fresh clone took 827 seconds and 95 seconds, listing the vault on the server 91 seconds (a failure, HTTP 504) and 0.73 seconds, a pull with nothing new 34 seconds and 4 seconds; the vault was 1,614 MB as loose objects and 1,184 MB as packs. | chart

The new versions of sgit change what is practical. In pack mode, released in sgit 0.24.0, a push is one zip with its commits, and a clone is the newest snapshot plus the packs since it. The PHP site's researcher measured the difference on the source watch itself, a vault of 29,861 files: a fresh clone went from 827 seconds to 95, listing the vault on the server from a timeout after 91 seconds to 0.73 seconds, and a pull with nothing new from 34 seconds to 4. Packs are also what make "a pack a day" a natural unit to publish: a dated zip, with its own index, that anyone can fetch directly.

## What we may publish {#tiers}

!shot rz-tiers.webp | images/ | What the research site may publish, by tier: tier A, open or public sector, the full capture in a public pack with a published read key, 73 of the source watch's pages, and Wikipedia under its open licence; tier B, at most 25 words and a link, the index, hash and change record in public and the full bytes in a private vault, 523 pages; tier C, link only, 15 pages. And an opt-out: any publisher who asks us to stop, we stop. | concept

We only use public sources. But public is not the same as free to republish, and the research site has to respect that. The source watch already gives every page a licence tier: A, open or public sector, "keep and show"; B, quote up to 25 words and link; C, link only. Its data counts 73 pages at tier A, 523 at B and 15 at C. And the Industry Wire's contract already sets the rule for public vaults: everything in a vault with a published read key is public, including its history, so "frozen tier-B bytes" never go in one.

So the research site publishes by tier:

- **Tier A** in full: the capture itself, in a public pack. Wikipedia, under its open licence and with attribution, belongs here.
- **Tiers B and C** as the record: the link, when we read it, the access we had, the hash of what was served, when it changed and, for B, at most 25 words. The full bytes stay in a private vault, as evidence.
- **An opt-out.** If a publisher asks us to stop, we stop, and the index says so. And we follow each site's own terms and robots.txt, as we did with [Feisty Duck](https://newsroom.sgit.ai/articles/feisty-duck-briefed.html).

That is still a lot. Most of what makes the archive useful, what changed, when, and who said it first, is in the record, not the bytes.

## What happens next {#next}

This is the design, for review. If it holds:

1. **The watch list,** seeded from the PHP site's sources, with each team's asks.
2. **The first runs on a schedule:** the daily web and Wikipedia, as pack vaults.
3. **research.newsroom.sgit.ai,** with the index, the packs and their read keys, built like the other newsroom sites.
4. **The PHP site's researcher moved onto it,** watching only what the shared runs do not cover; then the wires; then Web Summit.

## What this does not claim {#limits}

- **Nothing here is built.** research.newsroom.sgit.ai does not exist yet.
- **The source counts differ by date:** 913 pages in the site's data, 965 in the researcher's count of 23 October; the memo's "800" was an estimate.
- **The pack-mode numbers are from one vault,** measured by one agent on 23 October.
- **The Internet Archive archives far more.** The point is focus, structure and the index, not scale.

## Where this comes from {#sources}

My voice memo of 26 October 2026. The PHP story site's source watch data and its pack-mode measurements of 23 October; the researcher's [proposal for a phased source watch pass](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__phased-source-watch-pass/index.html); the sgit pack-mode specification in the sgit CLI repository; [how the Industry Wire works](https://newsroom.sgit.ai/wire/how.html); all read on 26 October 2026. Related: [Web Summit 2026, the plan](https://newsroom.sgit.ai/articles/web-summit-2026-the-plan.html), [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [who creates the original?](https://newsroom.sgit.ai/articles/who-creates-the-original.html), [Feisty Duck, briefed](https://newsroom.sgit.ai/articles/feisty-duck-briefed.html), [a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
