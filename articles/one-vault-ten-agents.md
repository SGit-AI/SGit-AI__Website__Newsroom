# One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom, sgit.ai

> Anthropic's post on Scion makes one observation that holds for any version control system: when the clients are agents, they are always online, there are many of them, and the expensive thing is moving bytes nobody needs. So the question for sgit is not how fast it clones a small vault, but what it does with a big one that many agents use every day. We have one. The vault the agents behind this newsroom share, with their mail, briefs, runs and analysis, had 1,295 commits, 5,281 files and about 35,000 encrypted objects on 16 October, 527 MB with all its history: the size of a real application's source repository, and about the size of our own SG/Send application's git repository. The sgit CLI team measured it eight ways from the hosted service and again from local disk. A full clone takes three and a half minutes; nobody needs one. One folder with one commit of history takes 13 seconds and 3 MB, however large the vault is; a file on demand under 3 seconds; an up-to-date pull 2.5. The honest edge is history: without a depth, a partial clone walks the commits one request at a time, nearly four minutes for one folder, and the fix is designed but not shipped. And with the same objects on local disk, the one-folder clone is 0.8 seconds: the time is the distance to the storage, not sgit. Which is why I think vaults this size are where sgit becomes useful for more than agents' memory, including source code.

*Source: <https://newsroom.sgit.ai/articles/one-vault-ten-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom

# One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.3.0, 4 versions](versions/one-vault-ten-agents.md) · [newsroom v0.12.80](https://newsroom.sgit.ai/admin/versions.html) · sgitvaultsagentsperformancemeasurementpartial-clonesscionversion-controlsource-codearticle

***Abstract:** Anthropic's post on Scion makes one observation that holds for any version control system: when the clients are agents, they are always online, there are many of them, and the expensive thing is moving bytes nobody needs. So the question for sgit is not how fast it clones a small vault, but what it does with a big one that many agents use every day. We have one. The vault the agents behind this newsroom share, with their mail, briefs, runs and analysis, had 1,295 commits, 5,281 files and about 35,000 encrypted objects on 16 October, 527 MB with all its history: the size of a real application's source repository, and about the size of our own SG/Send application's git repository. The sgit CLI team measured it eight ways from the hosted service and again from local disk. A full clone takes three and a half minutes; nobody needs one. One folder with one commit of history takes 13 seconds and 3 MB, however large the vault is; a file on demand under 3 seconds; an up-to-date pull 2.5. The honest edge is history: without a depth, a partial clone walks the commits one request at a time, nearly four minutes for one folder, and the fix is designed but not shipped. And with the same objects on local disk, the one-folder clone is 0.8 seconds: the time is the distance to the storage, not sgit. Which is why I think vaults this size are where sgit becomes useful for more than agents' memory, including source code.*

The newsroom's vault against two of our own git repositories: the SG/Send application and the sgit CLI.

## In short

- **The vault behind this newsroom.** Ten agents, one person, every day.
- **35,000 objects, 1,295 commits, 5,281 files.** The size of a real application's source code.
- **Nobody clones all of it.** Three and a half minutes, and nobody needs to.
- **One folder, one commit: 13 seconds, 3 MB.** However large the vault grows.
- **History is the edge.** Without a depth, one request per commit; a fix is designed.
- **The time is the storage.** The same clone from local disk: 0.8 seconds.
- **Big enough for source code.** That is the next use worth testing.

## The vault

The agents that write, check and publish this newsroom, ten of them, and I, share one vault. It holds our mail between agents, briefs, runs and analysis. Its contents are private; its shape is not, and it is the best test we have, because it is big by sgit's standards and busy every day: 68 of its commits arrived in the two days before these measurements.

On 16 October it had 1,295 commits, 5,281 files, 16,315 blobs and 16,391 trees: about 35,000 encrypted objects, and 527 MB when every one of them is on disk (measured with the full clone of 14 October). The latest version of its files is 139 MB. The biggest folder has 3,275 files and 69 MB; the smallest have a dozen. It lives on the hosted service, S3 behind CloudFront with a small API in front, and the agents reach it through the CLI.

The comparison in the figure above is why I think this matters beyond agents. The SG/Send application's git repository has 5,584 files, 4,399 commits and 42,434 objects; the sgit CLI's has 1,811 files, 1,603 commits and 13,985. The vault is in the same range as real application source code. If sgit handles this vault well, it handles a code base of that size, encrypted, with every version signed.

## What an agent fetches

What an agent fetches from the 35,000-object vault and what it costs, in seconds, on a log scale.

Nobody working in this vault needs all of it, and the point of the design is that they do not have to take it. The sgit CLI team measured each way of asking, from a cloud sandbox, on 14 and 16 October:

| What was asked for | Time | Objects | On disk |
|---|---|---|---|
| Everything, the full clone | 3½ min | 35,423 | 527 MB |
| The whole tree, one commit of history (`--depth 1`) | 57 s | 6,248 | 142 MB |
| One 130-file folder, one commit (`--path … --depth 1`) | 13 s | 137 | 3 MB |
| Structure only, one commit (`--sparse --depth 1`) | 27 s | 967 | 6 MB |
| One file on demand, in that sparse clone | 2.9 s | 1 |  |
| Widening a clone by a 130-file folder (`fetch`) | 7.8 s | 135 | 2 MB |
| A pull when nothing changed | 2.5 s | 0 |  |
| One 130-file folder, all its history | 227 s | 3,364 | 64 MB |
| The biggest folder, all its history | 264 s | 25,110 | 274 MB |

Two things stand out. A clone that carries a depth costs seconds and megabytes however large the vault is, because it asks for the spine of trees down to its folder and the blobs under it, and nothing else. That is the pattern the documentation gives agents, and the one ours use. And a clone that carries the whole history of a folder pays for the history, not the folder: 227 seconds for 130 files, almost all of it walking 1,295 commits one request at a time. A full clone avoids that by listing the store once and fetching everything in bulk; a partial clone cannot, because it must not hold objects it does not track.

That is the one real edge in the numbers, and the fix is designed: a small encrypted record of the commit chain, written on every push, so a clone can fetch the chain in about 26 batched requests instead of discovering it. Until it ships, the answer is the depth flag.

## What an agent does every session

The command an agent runs most is not clone but pull: come back, take what changed, carry on. Until 14 October that was the slow path on this vault, one request per commit and one per blob, and an agent a day behind waited the best part of an hour. The CLI team fixed it on the vault where the agents reported it: blobs now come in batches of 50 with 16 requests in flight, and past a long gap the client lists the store and sweeps what is missing, so fetching the whole head into an empty store takes about three minutes, down from about 53. A pull a few commits behind takes the few requests it needs; one with nothing new, 2.5 seconds.

## Where the time goes

The same vault and client with the objects in three places: hosted, a plain file server and a local API server.

The CLI team then copied the same 35,000 objects to local disk and served them two ways: a plain file server, and the same API server the hosted service runs, as one local process. The one-folder, one-commit clone fell from 13 seconds to 2.3 and 0.8. The history walk that costs three minutes hosted took 7 seconds, because it is the same 1,227 requests at about a millisecond each instead of 150. With no network at all, what is left of a full clone's 69 seconds is the client decrypting 16,000 trees.

So sgit is not the bottleneck; the distance to the storage is. Each request to the hosted service pays a round trip through a CDN, a Lambda and S3 before a byte moves, and the client's own work per object, checking its hash and decrypting it, is microseconds. The ruv.sgit hive runs say the same from the other side: on a local server, every sgit operation in fifteen recorded runs took between 0.4 and 1.5 seconds, including starting Python and deriving the key, and a 142-file, 6.9 MB vault cloned in 0.74 seconds. [sgit is a standard, not a server](sgit-is-a-standard.md) explains why that follows from the design.

## Many clients at once

The question Scion's post is really about is many clients. Earlier measurements on this site, on a single local server process, put a number on it: ten clones of one folder at once took 1.9 seconds with the server mostly idle; ten full clones queued to 21 seconds, which is the single process, not the protocol ([Agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md)). The more clients there are, the more it matters that each takes only what it needs.

## From agents' memory to source code

I started this vault as memory for agents, and the numbers say it is now a repository of real size: about as many files and objects as our application's source repository, every version encrypted and signed, read by ten clients that each take only what they need. That is where sgit starts to be useful for more than notes and mail. A code base of this size, kept in a vault, would let each agent clone the one package it works on, with one commit of history, in seconds; keep large files in the repository without every client paying for them; and live on a server, or a static host, that cannot read a line of it. The next test I would like to run is exactly that: a real code base, moved into a vault, with agents working on it.

## What this does not claim

- **Not proven at Scion's scale.** 35,000 objects, 1,295 commits and ten agents is the largest vault we run; Scion's monorepo has 100 GB of history and 30,000 merges a day.
- **No blame or bisect.** Path history, signed commits, signed tags and verification exist; blame is not written yet.
- **A partial clone of a long history is slow without a depth, today.** The fix is designed, not shipped.
- **One run each, from sandboxes that send every request through a proxy.** A plain connection does better.
- **The source-code use is a proposal.** The vault holds notes, mail and analysis, not code.

If you want to try a code base in a vault, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, a companion to [Scion and sgit](scion-and-sgit.md); written by this site's agent in the voice of this site; the editorial responsibility is mine. The vault's measurements are the CLI team's, from 14 and 16 October, with sgit 0.22.0 and the 14 October fixes; the vault's id and contents are not published. The git repositories were counted by this site's agent with `git ls-files`, `git rev-list --count` and `git count-objects`. The hive runs are from ruv.sgit.ai's published ledger of 16 October.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#one-vault-ten-agents)

### Builds on

- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.
- [Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it](scion-and-sgit.md) Anthropic's Scion replaced Git for agents inside one company; sgit, open source and encrypted, shares its core ideas, measured on a 35,000-object vault.

### Continued by

- [Where to invest in sgit: the tool, a hub for vaults, or open core, with the history of developer platforms, the evidence of use, three business plans, and the investor deck as a vault](where-to-invest-in-sgit.md) Where investment in sgit should go, from the history of developer platforms, with the deck as a vault.
- [Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open](three-linkedin-pages.md) Three companies, no LinkedIn pages: the decisions, every drafted field with its count, thirty first posts already written, and a new profile, in the open.
- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it](scion-and-sgit.md) Anthropic's Scion replaced Git for agents inside one company; sgit, open source and encrypted, shares its core ideas, measured on a 35,000-object vault.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 153 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=153)

**Posting this article on LinkedIn?** The cover is [one-vault-ten-agents.jpg](banners/one-vault-ten-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/one-vault-ten-agents.html)*
