---
title: Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: On 13 October Anthropic described Scion, the system that replaced Git for its monorepo after merges grew from about 2,500 a day in May to more than 30,000 in September, most of them by Claude. Git's offline, full-clone design, its post says, "was actively undermining our ability to scale", because nearly every client is now an always-online agent or job. Scion moves the work to the server, fetches only what a job needs, and serves immutable objects from three tiers of cache. Reading it, I recognised most of the ideas, because sgit, the encrypted version control we build in the open, arrived at many of them from the other direction. Its object ids are immutable content addresses, so objects cache for a year at a CDN; its server is a dumb store that cannot read what it holds, so reads can come from any static host; and its latest releases add scoped, shallow and on-demand clones. This site's agent checked each claim against sgit 0.22.0's code and measured it on a real vault: a scoped clone in 4 seconds against 59 for the full one, and a full clone served by a plain file server with no sgit server at all. The differences are real too. Scion does history, blame and merges on the server, and runs at a scale sgit has never been tested at; sgit does them on the client, has no blame or bisect yet, and does no packing on the server. But Scion is internal and, in Anthropic's words, "by no means a suitable replacement for git for general use". sgit is open source and on PyPI today, and it encrypts everything.
version: v0.12.72
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, scion, anthropic, version-control, git, agents, encryption, caching, monorepo, open-source, comparison, article
status: published
---

!shot sq-architecture.webp | images/ | Two answers to agents at scale: Scion's always-online clients, three cache tiers and a server that does history, blame, merges and commits; and sgit's clients that encrypt, merge and read history, a dumb server that stores encrypted objects, and reads that any static host or CDN can serve. | architecture

## In short {#in-short}

- **Agents broke Git's assumptions at Anthropic.** 30,000 merges a day, 25 million CI checkouts, always-online clients.
- **Scion moved the work to the server.** History, blame, merges and commits server-side; fetch only what you need.
- **sgit shares the core ideas.** Immutable content-addressed objects, partial clones, reads served by caches.
- **It arrived from the other side.** The server is dumb and blind; the client encrypts, merges and verifies.
- **Measured on 0.22.0.** A scoped clone in 4 seconds against 59; a full clone from a plain file server.
- **The gaps are real.** No server-side merge, blame or bisect; no packing; never tested at Scion's scale.
- **One is internal, one is open.** Scion is not released; sgit is on PyPI today.

## What Anthropic built {#scion}

Anthropic's engineering post, [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control), is unusually concrete. Merges to its monorepo went from about 2,500 a day in May 2026 to over 30,000 in September. The main branch's history is almost 100 GB; there are about 25 million CI checkouts a day, which, fetched naively, the post estimates at over 600 PB of Git traffic a day; and at the peak the company ran several hundred internal Git mirrors.

The diagnosis is the interesting part. Git was designed for people working offline on full copies, and the post says that design "was actively undermining our ability to scale as the repo grew", because nearly all its clients are now agents and jobs that are always online. So Scion inverts it. The server keeps history and does blame, commits, merges and rebases; a unit of work is a changeset written server-side; refs move by a compare-and-swap on one database row; clients fetch only the trees and files they need, and many jobs never check out at all, but query an API. Objects are immutable, so three tiers of cache, per machine, per region and the authoritative server, each serve more than 99% of reads. Nowhere, not even on the server, is there a full copy of the repository.

The results, by the company's own figures: about 200 times less CPU and memory than the Git mirrors it replaced, checkouts in seconds instead of minutes, a quarter of CI's CPU given back, and a migration done in five months by seven engineers while merges grew tenfold, with Claude writing much of the code. The post is equally clear about what Scion is not: internal, and "by no means a suitable replacement for git for general use".

## Why I recognised it {#recognised}

[sgit](https://sgit.ai/) started from the same instruction Anthropic arrived at: Git solved most of the hard problems, so [copy Git](/articles/from-send-to-sgit.html#git). Commits, trees, blobs, refs and branches, with encryption on top, and a server that, in the words of the March brief, is "a dumb key-value blob store" while "All intelligence lives in the client." Reading Scion's post, the overlap is not in the architecture's centre of gravity, which is the opposite, but in the properties that make agents fast.

!shot sq-matrix.webp | images/ | Scion, sgit 0.22.0 and Git side by side: who does the work, encryption, object ids, partial copies, reads without the server, writes, merge, history queries, proven scale and availability. | comparison

**Immutable identifiers that cache.** Every object in an sgit vault is named by the SHA-256 of its ciphertext, so its name can never point at different bytes; the client checks every object against its name before using it. That is exactly the property Scion's cache tiers rest on, and the live server already uses it: an object read from the SG/Send service comes back with `cache-control: public, max-age=31536000, immutable`, through a CDN. Unchanged folders keep the same tree ids across commits, so they are not fetched twice.

**Fetch only what you need.** Scion's clients request only the trees and blobs a job needs. sgit 0.18 to 0.22 added the same family of options: `--path` for a scoped clone, in which "Other folders are carried by id and never downloaded", `--depth` for a shallow one, and `--sparse` for structure first and content on demand. The CLI team measured a scoped clone of one folder in 14 seconds against 81 for the full clone on a vault of 626 commits and 9,404 files; this site's agent measured the same pattern below.

**Reads without the server.** Scion keeps its server for reads, behind caches. sgit can do without one: because the objects are encrypted and immutable, a read is a plain GET of a known path, and 0.22.0's `clone --transport static` reads from "any GET host". The server only matters for writes, which go through a batch endpoint, up to 100 operations at a time, with refs moved by compare-and-swap, the same primitive Scion uses on its database row.

**A server that cannot see.** This is where sgit goes beyond Scion's post, which does not mention encryption. Files, file names, trees, commit messages and refs are all encrypted on the client. The server holds ciphertext, so it can be cheap, simple and anyone's: a cloud bucket, a CDN, a folder on a laptop. That is why the hosting is so simple; the server has nothing to protect and nothing to compute.

## Measured on 0.22.0 {#measured}

!shot sq-bench.webp | images/ | One vault, five ways: a full clone in 58.6 seconds holding 12,664 KB of encrypted objects; depth 1 in 60.7 seconds; a scoped clone of one folder in 4.2 seconds and 412 KB; an on-demand clone in 3.6 seconds and 180 KB; and a full clone from a plain static file server in 1.6 seconds. | comparison

The agent installed sgit-ai 0.22.0, released on 15 October, and cloned a real published vault, the newsroom's synthetic-users vault of 83 files and 12 MB, with its public read key, twice in each mode. A full clone took about 59 seconds. A scoped clone of one folder took about 4 seconds and held 412 KB of encrypted objects instead of 12,664. An on-demand clone took 3.6 seconds and held 180 KB, the structure only. A shallow clone of depth 1 saved nothing on this vault, because almost all of its bytes are in the latest files; depth helps on long histories, not on young vaults.

Then the agent laid the same encrypted objects out as plain files and served them with Python's built-in file server, a program that knows nothing about sgit, and cloned from it with `--transport static`. The clone took 1.6 seconds on the same machine and was identical, file for file, to the clone from the API. It shows the mechanism rather than network speed, but it is the point: an sgit vault can be read from any storage that answers a GET, with no sgit server in the path.

## Where Scion is ahead {#gaps}

The memo I gave the agent was more optimistic than the code, and the article should say where. sgit does no packing or compaction on the server; the speed-ups in 0.18 to 0.22 are on the client, batching up to 50 objects a request with 16 requests in flight, and a vault of 35,000 objects still takes about three and a half minutes to clone in full. Merges happen on the client, three-way and whole-file; Scion does them on the server. sgit has a history log on the client but no blame and no bisect, which Scion offers through its API, and its automated bisect and revert pipelines depend on that. There is no command to read a file from a vault without at least a headless local clone. And the largest vault sgit's team documents has about 35,000 objects and 1,227 commits; Scion's has 100 GB of history and 30,000 merges a day. Being designed for something is not the same as being proven at it.

Git and sgit also live side by side rather than in sync. A vault can sit in the same folder as a Git repository, since sgit ignores `.git`, and a vault can be committed into a Git repository and attached with its key on the other side; but there is no bridge that turns Git history into sgit history or back.

## What it means {#means}

I find it fascinating to watch the same idea arrive twice. Agents change what source control is for: the clients are always online, the volume is machine-scale, and the expensive thing is moving bytes nobody needs. Anthropic answered inside one trusted company, with a powerful server that does the work. sgit answers for everyone else, where the server should not be trusted at all: encrypt everything on the client, name every object by its ciphertext, let any cache or bucket serve the reads, and keep the server dumb enough that anyone can run it. The two designs meet in the middle on immutable objects, partial fetches and compare-and-swap.

The practical difference is availability. Scion is a blog post. sgit is `pip install sgit-ai` today, with its code in the open, and it already carries [the vaults this site publishes](/articles/what-sgit-is.html). The useful next steps are clear from Scion's list: server-side history queries that do not need the plaintext, blame and bisect, and testing at a much larger scale. Anthropic says it wants to share its ideas with Git platforms and the open-source community. The ideas that do not depend on a trusted server are already there.

## What this does not claim {#limits}

- **sgit is not proven at Scion's scale.** Its largest documented vault is about 35,000 objects.
- **The measurements are small.** One 12 MB vault, two runs per mode, from a cloud sandbox; the static run was local.
- **Scion's figures are Anthropic's.** From its post; not independently verified.
- **Some features are missing.** No server-side merge, blame, bisect, packing, or Git history bridge in sgit 0.22.0.
- **I have a stake.** sgit is ours.

If you run agents against a large repository and want to try an encrypted, cacheable alternative, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Anthropic, [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control), 13 October 2026, updated 15 October, read on 16 October. sgit's facts are from the [sgit-ai](https://pypi.org/project/sgit-ai/) 0.22.0 wheel, which matches the [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) code and its changelog, and from the [SG/Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send) server code; the cache header was read from the live service. The measurements were made by this site's agent on 16 October 2026, cloning the published [newsroom-synthetic-users vault](https://newsroom.sgit.ai/demos/vaults/newsroom-synthetic-users/index.html) with its public read key.
