# A tangent that shipped: how sgit's pack mode went from a slow clone to a release in ten days, and took the PHP story's biggest vault from a 13-minute clone to 95 seconds the day after, sgit.ai

> This is a story about how innovation sometimes happens organically, and why I let myself go on tangents. It started with a bug: a vault that took 59 seconds to clone, measured by this newsroom, and the comms vault that took three and a half minutes. Fixing that led me to ask whether sgit could run a vault from a zip file, partly because I want vaults that live on Google Drive, Dropbox or a USB stick, with no server for us to maintain. The CLI team researched it with no code, designed a pack per push, had it reviewed four times by a second agent, and released sgit-ai 0.24.0 on 22 October. The next day, the PHP story's source watch needed it: 63,662 objects and 1.6 GB, a server that could no longer list it, a clone that took 13 minutes and 47 seconds, and one push that took 12 attempts and 2 hours 42 minutes. As a pack vault, the same history cloned in 95 seconds and pushed in 96. And it shipped without everything: the web UI still cannot open a pack vault. That was fine, because the vault that needed it did not need the UI. Small, incremental changes, done properly, made a very large difference.

*Source: <https://newsroom.sgit.ai/articles/a-tangent-that-shipped.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A tangent that shipped: how sgit's pack mode went from a slow clone to a release in ten days, and took the PHP story's biggest vault from a 13-minute clone to 95 seconds the day after

# A tangent that shipped: how sgit's pack mode went from a slow clone to a release in ten days, and took the PHP story's biggest vault from a 13-minute clone to 95 seconds the day after

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-24 · [article v1.0.0](versions/a-tangent-that-shipped.md) · [newsroom v0.13.65](https://newsroom.sgit.ai/admin/versions.html) · sgitpack-modeperformanceagentsvaultsinnovationarticle

***Abstract:** This is a story about how innovation sometimes happens organically, and why I let myself go on tangents. It started with a bug: a vault that took 59 seconds to clone, measured by this newsroom, and the comms vault that took three and a half minutes. Fixing that led me to ask whether sgit could run a vault from a zip file, partly because I want vaults that live on Google Drive, Dropbox or a USB stick, with no server for us to maintain. The CLI team researched it with no code, designed a pack per push, had it reviewed four times by a second agent, and released sgit-ai 0.24.0 on 22 October. The next day, the PHP story's source watch needed it: 63,662 objects and 1.6 GB, a server that could no longer list it, a clone that took 13 minutes and 47 seconds, and one push that took 12 attempts and 2 hours 42 minutes. As a pack vault, the same history cloned in 95 seconds and pushed in 96. And it shipped without everything: the web UI still cannot open a pack vault. That was fine, because the vault that needed it did not need the UI. Small, incremental changes, done properly, made a very large difference.*

The PHP site's pack-mode page, 23 October 2026: the source watch, 63,662 objects and 1,614.4 MB, cloned in 95 seconds as a pack vault against 13 minutes 47 seconds as a normal vault, its whole history pushed in 96 seconds, in 4 requests, 1.36 times smaller on the server.

## In short

- **It started with a bug.** A 59-second clone of a small vault, and a 3½-minute clone of a big one.
- **Then a tangent.** Could sgit run a vault from a zip, so a vault can live on Drive, Dropbox or a USB stick?
- **Research before code.** No code until the idea was measured, designed, specified and reviewed.
- **Ten days to a release.** sgit-ai 0.24.0, pack mode, on 22 October, after four review rounds by a second agent.
- **A real vault needed it the next day.** The PHP story's source watch: 13 minutes 47 seconds to clone, then 95.
- **It shipped without everything.** No web view yet, and that was the right call.
- **Battle-hardened.** Agents using it in anger, on a story that was still breaking.

## A bug, then a tangent

I want to capture this one because it is a great example of why I sometimes allow myself to go on tangents.

It started with performance. On 16 October this newsroom's own article on [Scion and sgit](https://newsroom.sgit.ai/articles/scion-and-sgit.html) measured an 83-file vault taking 59 seconds to clone. The CLI agent reproduced it and found the cause: batches of objects over the size limit of the Lambda that serves the API, retried instead of split. sgit-ai 0.23.0 fixed it the same day. The same work measured the comms vault we use to manage a lot of this: 35,423 objects and 527 MB, and a full clone of about three and a half minutes. That was the real problem.

While looking at that, I started exploring an idea I had wanted for a while: running a vault directly from a zip file. Not only for speed. I want vaults that can live where there is no vault server at all: Google Drive, Dropbox, a single object on S3, a USB stick, an email attachment. Other projects of ours need exactly that, and it fits the drive behind everything we do: not having infrastructure that we have to maintain. The CLI team wrote that research up as [a vault in one file](https://cli.sgit.ai/articles/a-vault-in-one-file.html) and [a vault you can carry](https://cli.sgit.ai/articles/a-vault-you-can-carry.html): nearly all of a vault is immutable objects named by their hash, which can live in any container, and only a handful of small files ever change. So the whole vault can be one file.

## Research, then a design, then four reviews

What I like most about what happened next is the order. I asked for research with no code changes, and got it, with live measurements: what the server's API already allowed, a 430 MB bundle downloaded in 3 seconds, zip files verified to 70,000 members. A brief for a server-side change was written, and then parked, because a design appeared that needed no server change at all: [a pack per push](https://cli.sgit.ai/articles/a-pack-per-push.html). Every push writes one zip; a snapshot pack holds the head; the server's existing routes do the rest.

Then a spec, reviewed before anything was built ([pack mode, read closely](https://cli.sgit.ai/articles/pack-mode-read-closely.html), with five decisions). Then the build, with tests that count requests and bytes on a simulated host, so "how many requests" is a measurement, not a guess. Then a live trial on the comms vault's history: a full clone in 25 seconds against three and a half minutes. Then [four review rounds](https://cli.sgit.ai/articles/pack-mode-four-rounds.html) by a second agent with its own reproducing scripts: 8 findings, then 4, then 4 (one of them caused by a fix from the round before), then 3 nits and no blockers. sgit-ai 0.24.0 went up on PyPI at 19:53 UTC on 22 October. The CLI team's own account of the [whole path](https://cli.sgit.ai/research/pack-mode-idea-to-release.html) lists every document it left behind.

Ten days from a slow clone to a vault that clones in 95 seconds: the comms vault's 3½-minute clone (14 October), a 59-second clone measured by this newsroom and fixed in 0.23.0 (16 October), research with no code and the tangent about a vault in one file (16 to 20 October), a pack per push designed and specified (21 October), four review rounds (21 to 22 October), sgit-ai 0.24.0 (22 October), and the source watch moved to pack mode (23 October).

## The vault that needed it

Meanwhile, the [PHP story](https://php.oct.2026.newsroom.sgit.ai/) was running. Its researcher agent built a source watch that captures every page it follows, with screenshots, every pass. It was doing exactly what we asked. It was also growing by about 5,000 objects a pass, and by 23 October it held 29,861 files, 63,662 objects and 1.6 GB. The agents just got on with it, and they struggled.

The limit we hit was not storage. In my memo I said we hit a limit of S3 at around 64,000 objects; the measurements say something more precise. A normal vault stores every object as its own file, and several operations start by asking the server for the list. At 63,662 objects the server's gateway gave up first: listing the vault returned HTTP 504 after 91 seconds. So a fresh clone walked the history instead and fetched 34,453 file objects one by one: 13 minutes and 47 seconds. Pushing one pass of 6,161 objects took 11 failed attempts, connection resets, timeouts and 504s, and a twelfth that worked: 2 hours and 42 minutes from commit to server. That is a good example of a massive inefficiency that agents will cheerfully work around until it breaks.

One pass of the source watch, pushed to the normal vault on 23 October: 11 failed attempts from 16:32 UTC, connection resets, a 25-minute cap and 504 timeouts listing the vault, and a twelfth that pushed 6,161 objects at 19:09 UTC. From the PHP site's pack-mode page.

On 23 October, the day after the release, the researcher imported the watch into a pack vault with `sgit pack import`, pushed it, cloned it fresh and checked it file for file. The PHP site [measured both](https://php.oct.2026.newsroom.sgit.ai/admin/pack-mode/index.html):

- **A fresh clone:** 13 minutes 47 seconds as a normal vault; 95 seconds as a pack vault, one 1,221.7 MB snapshot in 4 requests.
- **Listing the vault on the server:** a 504 after 91 seconds; 0.73 seconds.
- **A pull with nothing new:** 34 seconds; 4 seconds.
- **Pushing the whole history:** 96 seconds, in one go, against 2 hours 42 minutes for one pass.
- **On the server:** 1,614.4 MB down to 1,184.2 MB, because files are compressed before they are encrypted.
The same operations, side by side, on the same vault, server and sandbox: a fresh clone in 13 minutes 47 seconds against 95 seconds; listing the vault, an HTTP 504 against 0.73 seconds; a pull with nothing new, 34 seconds against 4. From the PHP site's pack-mode page.

That evening the scheduled curator followed the watch into its pack copy, and two agents wrote to it in turn, the scheduled session and the researcher, with no merge needed. A 1.6 GB set of files we can download in about a minute and a half, where it used to take nearly a quarter of an hour, is the difference between an agent that can start work and one that cannot. These are battle-hardened examples of the sgit CLI in action: not a benchmark, but agents using it on a story that was still breaking.

One request per object, or one zip per push: the normal vault's 63,662 objects, a listing that times out and a 13-minute clone, against the pack vault's one snapshot in 4 requests, a 95-second clone and 1.36 times less on the server. The server did not change.

## Not everything at once

Pack mode also shows that you do not have to do everything at once. It shipped with real gaps, stated in [the release notes](https://cli.sgit.ai/docs/update-to-0-24-0.html). The biggest: the web UI cannot open a pack vault yet. vault.sgraph.ai and the vault apps show it as empty, so a vault that must be browsable stays a normal vault for now. A thread is now looking at it. Scoped and shallow clones take the packs whole. Compaction is manual. And the local side still walks the whole working tree: on 29,861 files, pushing four objects took 77 seconds.

None of that mattered for the vault that needed it, which is read by agents, not in a browser. So it did not block it. Each change on the way was small, incremental and properly reviewed, and together they made a very large difference. That is how I want us to work: find the real constraint, fix it properly for the case that needs it, write down what it does not do yet, and come back for the rest.

Not everything at once: what sgit-ai 0.24.0 shipped (the pack commands, clones in a handful of requests, compression before encryption, older clients refused by name, a round trip back, the full test suite and four review rounds) and what it left for later (the web view, scoped and shallow clones, automatic compaction, slow local walks).

## Why the tangent mattered

If I had not gone down the zip tangent, we would have fixed the batch bug and moved on, and the source watch would have kept failing to push until someone noticed. Instead, by the time the PHP story's biggest vault hit the wall, the fix had been researched, built, reviewed four times and released the day before. That is not luck. It is what happens when a tangent is treated as research, measured and written down, rather than as a distraction. And the original goal is still there: a vault that is one file can live on Drive, Dropbox or a USB stick, with no server for anyone to maintain. Pack mode is the first half of that.

## What this does not claim

- **One run of each, not a median.** The PHP site's numbers come from one timed run each, from a cloud sandbox; the CLI team's medians are in its release notes.
- **The S3 limit in my memo was the server's listing.** At 63,662 objects, the list call timed out; storage itself did not fail.
- **Pack mode is opt-in.** Normal vaults behave as before.
- **No web view yet.** A pack vault opens as empty in the browser in this version.
- **Running a vault from Drive or Dropbox is research.** Range reads there are reported, not yet verified by the CLI.

## Where this comes from

My voice memo of 24 October 2026; the PHP story site's [pack-mode page](https://php.oct.2026.newsroom.sgit.ai/admin/pack-mode/index.html) and its data, measured by researcher@php.newsroom on 23 October; on [cli.sgit.ai](https://cli.sgit.ai/): the [0.24.0 release notes](https://cli.sgit.ai/docs/update-to-0-24-0.html), [a pack per push](https://cli.sgit.ai/articles/a-pack-per-push.html), [pack mode, read closely](https://cli.sgit.ai/articles/pack-mode-read-closely.html), [four rounds to no blockers](https://cli.sgit.ai/articles/pack-mode-four-rounds.html), [a vault in one file](https://cli.sgit.ai/articles/a-vault-in-one-file.html), [a vault you can carry](https://cli.sgit.ai/articles/a-vault-you-can-carry.html), [how pack mode went from an article to a release](https://cli.sgit.ai/research/pack-mode-idea-to-release.html), [the comms-vault report](https://cli.sgit.ai/research/sgit-issues-2026-10-14.html) and the [playbook for agents](https://cli.sgit.ai/docs/pack-mode-for-agents.html); PyPI's release times for sgit-ai 0.23.0 and 0.24.0. Related: [Scion and sgit](https://newsroom.sgit.ai/articles/scion-and-sgit.html), [almost working](https://newsroom.sgit.ai/articles/almost-working.html), [PHP October 2026, day three](https://newsroom.sgit.ai/articles/php-daily-2026-10-23.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#a-tangent-that-shipped)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 272 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=272)

**Posting this article on LinkedIn?** The cover is [a-tangent-that-shipped.jpg](banners/a-tangent-that-shipped.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-tangent-that-shipped.html)*
