# The homepage is a vault: a fresh edition every morning, every past homepage one commit away, served from plain files, and a brief for the agent that builds it, sgit.ai

> The homepage of this site has to be fresh every day, and today it changes only when someone releases the site. I would like a job that runs every morning at about 05:45, reads the latest articles, the wires and what is happening in the industry, and writes a new edition of the homepage. And that homepage should be a vault. Every edition a commit with a signed tag and its own version line; every edition carrying the links it showed and why, a screenshot of itself and the release note that explains it; any past homepage one commit id away; variants side by side for A/B tests; and anyone who wants their own homepage, in another language or for another audience, forks the vault. The encrypted objects can be served as plain files from S3, a CDN or GitHub Pages, read in the browser with a published read key. I had two facts wrong: this site is not served by a Lambda, it is on GitHub Pages; the Lambda is the vault API the wire reads through, and that is where the time goes, at 317 milliseconds a request against 44 for a static file. This site's agent built the homepage vault locally: three editions, three signed tags, a static export, and a browser that rendered today's edition in four requests, yesterday's in three, and nothing at all inside two minutes. A stats lane took 300 page-load beacons. This is the design, the measurements, and the brief.

*Source: <https://newsroom.sgit.ai/articles/the-homepage-is-a-vault.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The homepage is a vault: a fresh edition every morning, every past homepage one commit away, served from plain files, and a brief for the agent that builds it

# The homepage is a vault: a fresh edition every morning, every past homepage one commit away, served from plain files, and a brief for the agent that builds it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.2.0, 3 versions](versions/the-homepage-is-a-vault.md) · [newsroom v0.12.56](https://newsroom.sgit.ai/admin/versions.html) · homepagevaultssgitstatic-hostingperformanceab-testingappend-lanesscheduled-agentssynthetic-usersversion-controlarchitecturebriefarticle

***Abstract:** The homepage of this site has to be fresh every day, and today it changes only when someone releases the site. I would like a job that runs every morning at about 05:45, reads the latest articles, the wires and what is happening in the industry, and writes a new edition of the homepage. And that homepage should be a vault. Every edition a commit with a signed tag and its own version line; every edition carrying the links it showed and why, a screenshot of itself and the release note that explains it; any past homepage one commit id away; variants side by side for A/B tests; and anyone who wants their own homepage, in another language or for another audience, forks the vault. The encrypted objects can be served as plain files from S3, a CDN or GitHub Pages, read in the browser with a published read key. I had two facts wrong: this site is not served by a Lambda, it is on GitHub Pages; the Lambda is the vault API the wire reads through, and that is where the time goes, at 317 milliseconds a request against 44 for a static file. This site's agent built the homepage vault locally: three editions, three signed tags, a static export, and a browser that rendered today's edition in four requests, yesterday's in three, and nothing at all inside two minutes. A stats lane took 300 page-load beacons. This is the design, the measurements, and the brief.*

The homepage as a vault: the morning job, static hosting, the GitHub Pages shell and the browser reading the edition.

## In short

- **Fresh every morning.** A scheduled job writes a new homepage edition at about 05:45, or every hour if we want.
- **The homepage is a vault.** Every edition a commit, a signed tag and a version of its own.
- **Every past homepage, one commit away.** With its links, its screenshot and its release note.
- **Plain files, not a function.** The encrypted objects can sit on S3, a CDN or GitHub Pages.
- **Where the time goes.** 317 ms a request through the vault API, 44 ms from GitHub Pages.
- **Measured locally.** Today's edition in 4 requests, yesterday's in 3, nothing at all inside two minutes.
- **Variants, stats and synthetic users.** A/B variants in one commit, a stats lane for page loads, a daily run of readers who do not exist.
- **Fork it.** A homepage for another language, culture or publisher is a fork of the vault.

## Why the homepage needs this

The homepage is the page that most needs to be fresh and the one that changes least. Today it is generated when the site is released, so it moves when I publish and stands still when I do not. What I have in mind is an edition: every morning, a job that looks at the latest articles, the wires, and what is happening in the industry we write about, and decides what leads, what follows and what rotates out. The structure, the highlights and the selections are the edition. Parts of the page can stay dynamic: the wire and the full list of articles load live, from their own sources, as they do now.

## Correcting the memo

I had two facts wrong. This site is not served by a Lambda function: newsroom.sgit.ai is on GitHub Pages, whose responses say `server: GitHub.com`. The Lambda is the vault API, behind CloudFront, that the [Industry Wire](https://newsroom.sgit.ai/wire/index.html) reads its vaults through. And the wire is half of what I described: it does read encrypted vaults in the browser with a published read key, as [Two agents, one vault](two-agents-one-vault.md) explained, but through that API, not from plain files.

That is where the time goes. On one cold load of the wire from this sandbox, the browser made eight requests to the API, one after the other, each taking between 360 and 810 milliseconds, and the last one ended 3.9 seconds after the page itself had loaded. On a warm connection, one request to the vault API took a median of 317 milliseconds; one request to GitHub Pages for a small file took 44. The API also sent no cache header for an immutable object, which sgit.ai's [own measurements](https://sgit.ai/demos/fractal-graphs/performance.html) noted in September: "the read endpoint returned **no `Cache-Control` header at all** for an immutable object".

## Plain files are enough

The good news is that sgit already reads from plain files. sgit.ai's update [Take the API out of the path](https://sgit.ai/updates/index.html#take-the-api-out-of-the-path) cloned the same vault in 65.4 seconds through the serverless API and in 2.63 seconds from plain GETs: "Twenty five times faster, with nothing about the vault changed." It was honest that the static host was on the same machine, so a real CDN adds its own latency. Its conclusion is the one that matters: the API is "a convenience over a store, not a requirement of it".

The browser side is documented in [Static hosting](https://sgit.ai/docs/vault/static-hosting.html): the same reader runs against the API or a folder of files laid out as `api/vault/read/<vault id>/bare/`, where content-addressed objects can be cached for ever and the one ref, the pointer to the latest commit, must never be. It also names the limit: "Read-only and frozen." A static copy changes only when it is exported again, which is not a problem for a homepage that is released once a day. It is exactly the model.

## The demo

Three editions of the demo homepage vault, each a commit with a signed tag.

This site's agent built the homepage vault on a local vault server with sgit 0.21.0. A small script, the edition job, reads the articles and their graphs and writes one edition: `index.html` with the structure, `edition.json` with the lead, the picks, the topics and every link shown with the reason it was chosen, `variants/a.html` and `variants/b.html`, a release note in `releases/`, and a screenshot in `shots/`. It ran three times, for 13 October, the morning of 14 October and the evening of 14 October, and each run was committed, pushed and tagged: `home-v0.1.0`, `home-v0.1.1`, `home-v0.1.2`, each "signed by this clone". The homepage now has its own version line, separate from the site's.

Then the agent exported the vault as plain files with `sgit publish`, put the objects in the documented layout, and served them from a plain static server with the cache headers S3 or a CDN would send. A reader cloned it with `--transport static` in 0.38 seconds, against 0.33 through the local API: on one machine, the network costs nothing either way. In a browser, using the same reader the wire uses, the results were these.

- **Today's edition, cold.** 4 requests and 4.7 KB: the ref, the commit, the tree and the page.
- **The same reader inside two minutes.** No requests at all: the ref is reused for 120 seconds and the objects come from the browser's cache.
- **Yesterday's edition.** 3 requests, by commit id; no ref is needed, because history is just another object.
- **The other variant.** 2 requests, for the variants folder and the page.

Those are counts, not network times. With 44 milliseconds a request, four chained requests are about 0.2 seconds from static files; at 317, about 1.3 seconds through the API. The [live vault docs](https://sgit.ai/case-studies/live-vault-docs.html) on sgit.ai found the same shape in production: a cold load of 18 objects, then "one 69-byte request per reader per two minutes".

## Who loads what

One page load: the shell from GitHub Pages, four chained requests to the static host, and a beacon to the stats lane.

The order matters because each step needs the one before it. The shell comes from GitHub Pages, with the read key and the reader. The ref says which commit is today's edition; the commit names the tree; the tree names the page. Only the ref can change, so it is never cached; everything else is named by its own hash and can be cached by every layer in between for ever. The browser decrypts with the read key, renders, and records which variant it showed. The read key is public on purpose: [sgit.ai's credentials page](https://sgit.ai/docs/credentials.html) says it is "derived from the vault key by a one-way function, so a read key can never be turned back into write access."

## History, variants and forks

Version control of the homepage is the feature I like most. Every edition is a commit, so any day's homepage can be opened again exactly as it was, with the links it showed, the screenshot of how it looked, and the release note that says why it changed. That also means we can rotate: the job can see every link that has led the page and give the rest a turn.

Variants sit in the same commit, so an A/B test is a choice the page makes, not a second deployment. And a fork is a whole homepage: another language, another culture, another publisher, or one reader who wants their own front page, takes the vault, changes the edition rules and publishes their own.

## Stats, and the readers who do not exist

The measurements: live numbers from this sandbox to newsroom.sgit.ai, and vault numbers from local servers.

For the test to mean anything, we need to know what happened. An [append lane](https://sgit.ai/api/append-lanes.html) is "A write-only channel attached to a vault, gated by a token the writer holds and nothing else", and sgit.ai already has a [brief for telemetry](https://sgit.ai/docs/briefs/vault-telemetry-append-lanes.html) through one. The agent configured a lane on the homepage vault and sent it 300 synthetic page-load beacons, each with the edition, the variant, a load time and whether a link was clicked: 2.6 milliseconds each on the local server, and all 300 read back with the enum key. The click rates in that test were invented by the script, so they show the plumbing, not a result. Two limits apply. A static host cannot take writes, so the beacons still go to the API; and the cap is "**1000 pending files per token → 507**", so the morning job has to collect and clear the lane every day, writing the totals into a stats vault.

The other daily input is the synthetic readers. [How to run synthetic users](how-to-run-synthetic-users.md) describes five to ten invented readers who drive a real browser and report what they saw; run every morning against the live page, with their findings and timings in their own vault, they tell us when something has broken or slowed down before a reader does.

## What has to be handled

**Search engines.** sgit.ai's case study is plain about it: "Search engines and agents see an empty shell." The shell on GitHub Pages should therefore carry a plain snapshot of today's edition, generated from the same commit and naming it. [Surfaces](https://sgit.ai/docs/surfaces.html) gives the rule for that: "What must never be duplicated is the content itself"; the snapshot is a projection of the edition, not a second copy to edit.

**Revocation.** `sgit publish` warns that bytes deployed into a git repository "stay in its history after any later deletion, so rotation cannot revoke access to what you publish now", and suggests object storage when that matters. For a public homepage it does not, but it is a reason to put the static objects on S3 rather than in this repository.

**A mirror needs a reader.** sgit.ai learnt this the hard way when it [removed its own vault mirror](https://sgit.ai/updates/index.html#the-mirror-is-gone): "give a mirror a reader before giving it a remote". The homepage vault has a reader from the first day: the homepage.

## A brief for the agent

1. **Start on a separate page.** Build `/front/` from the homepage vault and leave the homepage alone until the numbers say it is better.
2. **The edition job.** Every morning at 05:45 UK time, read the articles, the wires and the stats, write one edition, commit it, tag it `home-vX.Y.Z` and add its screenshot and release note.
3. **Plain files.** Export each edition to S3 behind a CDN, with immutable objects cached for a year and the ref never cached; keep the vault API as the writer's path only.
4. **A shell with a snapshot.** A small page on GitHub Pages with the read key, the reader, and a plain snapshot of the edition for search engines, naming its commit.
5. **Every edition reachable.** A "this page on another day" link that opens any tag by its commit id.
6. **Variants and stats.** Two variants per edition, assigned in the browser; a beacon per load to a stats lane; the morning job collects, totals and clears it, and writes the totals to a stats vault.
7. **Synthetic users daily.** Five readers against `/front/` and the homepage, findings and timings in their own vault.
8. **Prove it.** Time the live cold and warm loads of `/front/` against the current homepage, every day for two weeks, and report; move the homepage only if `/front/` is at least as fast and the variants show which works better.
9. **Move the wire too.** The same export for the wire's vaults would take its eight API requests off the reader's path.

## What this does not claim

- **The demo is local.** A local vault server and a local static server; the vault numbers count requests and bytes, not network time.
- **The live timings are from this sandbox.** One location, medians of ten requests; readers elsewhere will see other numbers.
- **The beacons and clicks were synthetic.** They show the lane works, not which variant is better.
- **Nothing is scheduled yet.** The morning job, the S3 export and `/front/` are proposed.
- **A/B tests need readers.** With this site's traffic, a difference between variants may take weeks to show.

If you want your own homepage to be a vault, or want to fork ours, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The demo and the timings were run by this site's agent on 14 October 2026; a research agent read sgit.ai's documentation, and the quotes were checked against it. From sgit.ai: [Take the API out of the path](https://sgit.ai/updates/index.html#take-the-api-out-of-the-path), [Static hosting](https://sgit.ai/docs/vault/static-hosting.html), [Live vault docs](https://sgit.ai/case-studies/live-vault-docs.html), [Fractal graphs performance](https://sgit.ai/demos/fractal-graphs/performance.html), [Surfaces](https://sgit.ai/docs/surfaces.html), [Credentials](https://sgit.ai/docs/credentials.html), [Append lanes](https://sgit.ai/api/append-lanes.html), [Vault telemetry through append lanes](https://sgit.ai/docs/briefs/vault-telemetry-append-lanes.html) and [The mirror is gone](https://sgit.ai/updates/index.html#the-mirror-is-gone).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-homepage-is-a-vault)

### Builds on

- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.

### Continued by

- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 129 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=129)

**Posting this article on LinkedIn?** The cover is [the-homepage-is-a-vault.jpg](banners/the-homepage-is-a-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-homepage-is-a-vault.html)*
