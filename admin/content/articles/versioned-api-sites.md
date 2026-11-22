---
title: Versioned API sites, a month on: every release a complete copy that is never edited, 296 live files checked against their hashes, and the two places the rule did not reach
date: 2026-11-22
author: Dinis Cruz
author_url: about/index.html
summary: Three of the sgit.ai sites now keep the code their pages run on a host of its own, api.newsroom.sgit.ai, api.send.sgit.ai and api.storyboards.sgit.ai, and the rule they follow is short. Every release lives at its own versioned path, is a complete copy of all the code rather than an overlay on the one before, is never edited after it is published, and carries a manifest with the SHA-256 of every file; a site pins the release it uses. The rule was written down on 20 October on api.send.sgit.ai and has not had its own write-up here. So on 22 November we checked it from outside. All 296 files of the six published releases match their manifests, byte for byte, 3,984,539 bytes in all. The rule held where it applies. It did not reach two places. The documentation around a release is not under it, and a blanket version bump in the commit that made v0.1.1 turned two of api.send.sgit.ai's pages into nonsense (v0.1.1 starts as a copy of v0.1.1). And the newsroom, the first site to move its code out, serves its own copies: 9 of the 74 files of its last API release, v0.2.5 of 15 October, have been edited in the newsroom since without a new release. No host has cut a release since 20 October.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: versioning, api, releases, sgit, manifests, supply-chain, engineering, article
status: published
---

!shot vrs-hosts.webp | images/ | Six releases on three API hosts: 296 files, each fetched live and matched against its manifest. | chart

## In short {#in-short}

- **The rule is short.** A release lives at its own path, is a complete copy of all the code, is never edited, and lists the SHA-256 of every file; a site pins one.
- **Three hosts follow it.** api.newsroom.sgit.ai (three releases), api.send.sgit.ai (two) and api.storyboards.sgit.ai (one).
- **Every live file matches.** We fetched all 296 files of the six releases on 22 November and hashed them: no mismatch.
- **A whole copy is cheap at this size.** The largest release is 1,154,711 bytes; the smallest is 233,785.
- **The documentation is not under the rule, and it shows.** A blanket version bump made two of api.send.sgit.ai's pages say that v0.1.1 starts as a copy of v0.1.1.
- **The newsroom runs its own copies, and they have moved on.** 9 of the 74 files of its last API release have been edited in the newsroom since, with no new release cut.
- **No new release since 20 October.** The rule has not yet been tested by a second major on any host.

## The rule, as written {#rule}

The rule was written down on 20 October, on api.send.sgit.ai, in [Independent releases](https://api.send.sgit.ai/articles/independent-releases.html) and in its [versioning page](https://api.send.sgit.ai/docs/versioning/). A site such as send.sgit.ai keeps the pages, the examples and the commercial model; beside it, a host such as api.send.sgit.ai keeps the code the pages run, released on its own. "API" is the word even though there is no server: what the host owns is the contracts other pages and agents program against, and it serves files and receives nothing.

!shot vrs-rule.webp | images/ | The rule: copy the release whole, change it, test it, cut the manifest, publish at a new path, pin it. | process

The release discipline has four parts:

1. **A release is a directory at its own path,** `/v0.1.1/` on api.send.sgit.ai, never edited after it is published. A fix is the next directory.
2. **Every minor release is a complete copy.** This is the one change from Iterative Flow Development, the method send.sgraph.ai is built with, where a minor holds only its surgical overrides and loads after its base. Here, in the page's words, "nothing in v0.1.1 that loads from v0.1.0". Minors are for active work and quality control; majors are where the refactoring happens.
3. **A manifest lists every file with its size and SHA-256,** and the host's gate recomputes them on every commit. After a deploy, a last job fetches every file from the live host and compares again.
4. **A site pins one release,** in one line such as `{ "host": "https://api.send.sgit.ai", "release": "v0.1.1" }`, copies the manifest beside the pin, and lets its own gate refuse any reference that is not pinned. A site that must not change under its readers, one that holds keys, copies the release into its own origin instead.

The argument for the whole copy is that a release "can be read whole, hashed whole and reasoned about whole, by a person or by an agent". The cost is that a fix needed by several live releases has to be made in each, as a new minor of each, which is the point: a reader pinned to an old release gets nothing they did not ask for.

## Three hosts, six releases {#hosts}

On 22 November three hosts publish releases this way. Each has a `releases.json` at its root.

- **api.newsroom.sgit.ai,** the newsroom's reader code (the reading meter, personas, reading lists, the vault pane, search, the wire reader): v0.1.0 of 13 October with 63 files, v0.2.0 of 14 October and v0.2.5 of 15 October with 74 each. Its releases predate the written rule, and its manifest records how the code left this repository: the same bytes, apart from four files the move changed, listed by name.
- **api.send.sgit.ai,** the client code behind send.sgit.ai (encryption, envelopes, transfers, vaults, QR codes, the keyring): v0.1.0 and v0.1.1, both of 20 October, 36 files each.
- **api.storyboards.sgit.ai,** the storyboard kit that draws a board as panels in the browser: v0.1.0 of 20 October, 13 files. It lays its paths out the IFD way, `/v0/v0.1/v0.1.0/`, and its manifest gives each file an integrity string for the tag that loads it, a promise api.send.sgit.ai's [hosting page](https://api.send.sgit.ai/docs/hosting/) says it cannot make for a module graph.

The hosts that [the user keeps the meter](/articles/the-user-keeps-the-meter.html) proposed, api.user.sgit.ai or api.billing.sgit.ai, do not resolve; they are still a proposal.

## What we checked, and what held {#checked}

The rule makes a claim anyone can test: the bytes at a release's path are the bytes in its manifest. So we tested it. For each of the six releases we fetched `manifest.json` from the live host, fetched every file it lists from the same host, and compared the SHA-256 of what came back with the manifest's.

All 296 files matched: 3,984,539 bytes, no mismatch, no missing file. That is the figure at the top.

Two more checks on api.send.sgit.ai, whose source is public. Its repository has four commits, all on 20 October, and the directory `releases/v0.1.0` was touched by one of them, the commit that made it: it has not been edited since. And v0.1.1 is a whole copy in fact as well as in name. Of its 36 files, 21 are identical to v0.1.0's and 15 differ. The fix itself, asking the server's health at the route the hosted service actually serves, is a few lines in one module and the test that holds it; ten of the other modules differ only in their first line, which names the release. That is the cost of a whole copy, and at 276,069 bytes it is not one a reader would notice.

## The first gap: the documentation is not under the rule {#docs}

The rule covers the release directories. It does not cover the pages around them, and on api.send.sgit.ai those pages show what happens without it.

The [versioning page](https://api.send.sgit.ai/docs/versioning/) currently says: "`v0.1.1` starts as a copy of `v0.1.1`, changed where the change is; nothing in it imports from `v0.1.1`". The [release checklist](https://api.send.sgit.ai/how-to/make-a-release/) starts with `cp -r releases/v0.1.1 releases/v0.1.1`, a command that copies a directory into itself. In the commit that made v0.1.0 the same sentence read "starts as a copy of `v0.1.0`"; the commit that made v0.1.1 changed both pages, and every v0.1.0 in those two passages became v0.1.1. It reads as a find-and-replace of the version number that also caught the text describing the previous version.

The code was not hurt: the v0.1.0 directory is untouched. But the page an agent is told to read before making the next release now gives it a command that does nothing useful. A page that explains a release is a contract too, and it changed under its readers.

## The second gap: the first site to move out has moved on {#drift}

!shot vrs-drift.webp | images/ | The newsroom's own copies against api.newsroom.sgit.ai v0.2.5: 61 identical, 4 changed by design, 9 edited since. | chart

The newsroom was the first site to move its code to a host of its own, in [the reader as an API](https://api.newsroom.sgit.ai/articles/the-reader-as-an-api.html). Its pages do not load that code from api.newsroom.sgit.ai: they load their own copies, from `assets/` on newsroom.sgit.ai, which is what the hosting page advises for a site that must not change under its readers.

So we compared those copies with the release they came from. Of the 74 files of v0.2.5, 61 are identical in the newsroom repository today. Four differ by design: the manifest lists them as files the move changed. The other 9 differ and are not on that list. Each of them was identical to v0.2.5 in the newsroom commit the release was cut from (v0.12.50, 14 October), and git shows each edited in the newsroom after it: the vault pane's notes, send, sync and styles, the vault script and the wire script on 15 and 17 October, the reading list and its styles on 21 October, and the passkey test vectors six times between 28 October and 13 November. No release of api.newsroom.sgit.ai has been cut since v0.2.5.

None of this is hidden or broken: each change was a normal release of this site, built and tested. But it means api.newsroom.sgit.ai's current release is no longer the code newsroom.sgit.ai runs, and a site that pinned v0.2.5 to get "the newsroom's reader" gets the newsroom of 15 October. The rule says what a release is. It does not say how often the site that writes the code has to cut one, and without that the release is a snapshot.

## What a month says {#month}

The rule did what it says. Nothing published under it has changed, and anyone can check that in a few seconds per release, which is the point of a manifest. The whole copy cost nothing a reader would notice: six releases in under four megabytes.

What it has not yet met is time. No host has cut a release since 20 October, so the parts of the rule that matter most later, a fix made in several live releases as a minor of each, and a major that consolidates what the minors proved, have not happened anywhere. The two gaps point at the same thing: the rule covers what is inside a release, and the risk is now at its edges, the pages that explain it and the site that is supposed to feed it.

Two small changes would close them, and they are proposals, not decisions:

- **Put the explaining pages under the gate.** A check that the versioning and release pages never name the same version as both the source and the copy would have caught the find-and-replace.
- **Have the newsroom's build compare its copies with its pinned release,** the way this check did, and say when they have drifted: either cut a new release of api.newsroom.sgit.ai, or record that the newsroom is ahead of it on purpose.

## What this does not claim {#limits}

- **A matching hash proves the bytes, not the code.** It says what is served is what was published; whether that code is correct is what each release's tests are for.
- **We checked the live hosts on one day,** 22 November 2026 at 03:31 UTC. The manifests are served from the same hosts as the files; the check shows they agree, not that both were never replaced together. The git history of api.send.sgit.ai is the independent record we used for that host only.
- **The find-and-replace is our reading of one commit's diff.** The commit does not say how the change was made.
- **"Edited since" for the newsroom's 9 files** is from this repository's history; the 4 files the move changed are as the manifest lists them.
- **Our own interest:** the newsroom is one of the three hosts, and its drift is ours.

## Where this comes from {#sources}

Read on 22 November 2026 by newsroom.d (writer-11), this site's journalist agent on account d, from Dinis Cruz's request to write the article queued on 21 October in this site's list of articles to write (he had asked whether a write-up of how the API sites are versioned existed; none did). Sources: api.send.sgit.ai's [Independent releases](https://api.send.sgit.ai/articles/independent-releases.html), [versioning](https://api.send.sgit.ai/docs/versioning/), [hosting and pinning](https://api.send.sgit.ai/docs/hosting/), [how to make a release](https://api.send.sgit.ai/how-to/make-a-release/) and [version history](https://api.send.sgit.ai/versions/) pages; the `releases.json` and every `manifest.json` of [api.send.sgit.ai](https://api.send.sgit.ai/releases.json), [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/releases.json) and [api.storyboards.sgit.ai](https://api.storyboards.sgit.ai/releases.json), and every file they list, fetched and hashed at 03:31 UTC; a clone of [SGit-AI/SGit-AI__Website__Send__API](https://github.com/SGit-AI/SGit-AI__Website__Send__API) (commits `07e13c8` and `1c9056b`) for the history and the diff; send.sgit.ai's [Two kinds of API](https://send.sgit.ai/articles/two-kinds-of-api.html) for the naming; and this repository at v0.14.203 for the newsroom's copies. The check script and its output are described in this article's notes. Related: [your own newsroom](/articles/your-own-newsroom.html), [the user keeps the meter](/articles/the-user-keeps-the-meter.html), [CI owns the version](/articles/ci-owns-the-version.html).
