# Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it, sgit.ai

> On 13 October Anthropic described Scion, the system that replaced Git for its monorepo after merges grew from about 2,500 a day in May to more than 30,000 in September, most of them by Claude. Git's offline, full-clone design, its post says, "was actively undermining our ability to scale", because nearly every client is now an always-online agent or job. Scion moves the work to the server, fetches only what a job needs, and serves immutable objects from three tiers of cache. Reading it, I recognised most of the ideas, because sgit, the encrypted version control we build in the open, arrived at many of them from the other direction: immutable objects named by the hash of their ciphertext, which anyone can keep for ever; a server that cannot read what it holds, so reads can come from any static host; clones that take one folder, one commit or only the structure; and, like Scion, no packfiles and no maintenance. Measured on the vault the agents behind this newsroom share every day, 35,000 encrypted objects and 1,295 commits, an agent takes one folder with one commit of history in 13 seconds and 3 MB, however large the vault is. The differences are real too. Scion does history, blame and merges on the server and runs at a scale sgit has never been tested at; sgit does them on the client and has no blame or bisect yet. But Scion is internal and, in Anthropic's words, "by no means a suitable replacement for git for general use". sgit is open source and on PyPI today, and it encrypts everything.

*Source: <https://newsroom.sgit.ai/articles/scion-and-sgit.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it

# Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.3.0, 4 versions](versions/scion-and-sgit.md) · [newsroom v0.12.80](https://newsroom.sgit.ai/admin/versions.html) · sgitscionanthropicversion-controlgitagentsencryptioncachingmonorepoopen-sourcecomparisonarticle

***Abstract:** On 13 October Anthropic described Scion, the system that replaced Git for its monorepo after merges grew from about 2,500 a day in May to more than 30,000 in September, most of them by Claude. Git's offline, full-clone design, its post says, "was actively undermining our ability to scale", because nearly every client is now an always-online agent or job. Scion moves the work to the server, fetches only what a job needs, and serves immutable objects from three tiers of cache. Reading it, I recognised most of the ideas, because sgit, the encrypted version control we build in the open, arrived at many of them from the other direction: immutable objects named by the hash of their ciphertext, which anyone can keep for ever; a server that cannot read what it holds, so reads can come from any static host; clones that take one folder, one commit or only the structure; and, like Scion, no packfiles and no maintenance. Measured on the vault the agents behind this newsroom share every day, 35,000 encrypted objects and 1,295 commits, an agent takes one folder with one commit of history in 13 seconds and 3 MB, however large the vault is. The differences are real too. Scion does history, blame and merges on the server and runs at a scale sgit has never been tested at; sgit does them on the client and has no blame or bisect yet. But Scion is internal and, in Anthropic's words, "by no means a suitable replacement for git for general use". sgit is open source and on PyPI today, and it encrypts everything.*

Two answers to agents at scale: Scion's always-online clients and server, and sgit's encrypting clients and dumb server.

## In short

- **Agents broke Git's assumptions at Anthropic.** 30,000 merges a day, 25 million CI checkouts, always-online clients.
- **Scion moved the work to the server.** History, blame, merges and commits server-side; fetch only what you need.
- **sgit shares the core ideas.** Immutable objects, fetch only what you need, no packfiles, compare-and-swap.
- **It arrived from the other side.** The server is dumb and blind; the client encrypts, merges and verifies.
- **Measured on a real, busy vault.** 35,000 objects: one folder, one commit, in 13 seconds and 3 MB.
- **The gaps are real.** No blame or bisect; long histories need a depth; never tested at Scion's scale.

## What Anthropic built

Anthropic's engineering post, [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control), is unusually concrete. Merges to its monorepo went from about 2,500 a day in May 2026 to over 30,000 in September. The main branch's history is almost 100 GB; there are about 25 million CI checkouts a day, which, fetched naively, the post estimates at over 600 PB of Git traffic a day; and at the peak the company ran several hundred internal Git mirrors.

The diagnosis is the interesting part. Git was designed for people working offline on full copies, and the post says that design "was actively undermining our ability to scale as the repo grew", because nearly all its clients are now agents and jobs that are always online. So Scion inverts it. The server keeps history and does blame, commits, merges and rebases; refs move by a compare-and-swap on one database row; clients fetch only the trees and blobs they need, and many jobs never check out at all, but query an API. Objects are immutable, so three tiers of cache each serve more than 99% of reads. "There is no equivalent of packfiles (git's compressed bundles of objects), so no repository maintenance is needed." Directories can carry their own permissions.

The results, by the company's own figures: about 200 times less CPU and memory than the Git mirrors it replaced, checkouts in seconds instead of minutes, a quarter of CI's CPU given back, and a migration done in five months by seven engineers. The post is equally clear about what Scion is not: "by no means a suitable replacement for git for general use".

## Why I recognised it

[sgit](https://sgit.ai/) started from the same instruction Anthropic arrived at: Git solved most of the hard problems, so [copy Git](from-send-to-sgit.md#git). Commits, trees, blobs, refs and branches, with encryption underneath, and a server that, in the words of the March brief, is "a dumb key-value blob store" while "All intelligence lives in the client." Reading Scion's post, the overlap is not in the centre of gravity, which is the opposite, but in the properties that make agents fast.

Scion, sgit and Git side by side, from who does the work to proven scale and availability.

**Fetch only what you need, the same way.** Scion's post: "Scion's negotiation doesn't tell the server what the client already has; instead, it operates exclusively on trees and blobs the client wants. Starting from a root tree, the client checks its local store for missing trees and requests them recursively, then repeats the process for blobs." That is sgit's clone and pull walk: level by level over the trees, then the blobs in batches of 50 with 16 requests in flight. A scoped clone asks only for the spine down to its folders, and an unchanged folder keeps its tree id across commits, so it is never fetched twice.

**Immutable objects, kept by whoever fetched them.** Scion: "Every request is for a specific object that never changes, so any cache can answer it." Every sgit object is named by the SHA-256 of its ciphertext, and the client checks each one against its name. The name also says what it is: immutable objects carry `-imm-`, the two mutable pointers carry `-muw-`. So a browser, a proxy, a CI cache or a folder can keep an object for ever by looking at its name, without reading it. That is how sgit.ai's own documentation pages, which are a vault read in the browser, load: 18 objects cold, then one 69-byte ref, then nothing inside a two-minute window. The server also sends a one-year `immutable` cache header, though the CDN in front of the hosted API does not yet serve object reads from its cache; browsers, clients and static hosts do. The trade is deliberate: no deltas between versions, so a changed file is a new object.

**No packfiles, no maintenance.** Neither system packs objects on the server, and both treat that as a feature.

**Compare-and-swap.** Scion moves a ref with a compare-and-swap on one row; sgit moves the ref and the branch index the same way.

**Where they differ, sharply.** Scion protects directories with permissions on a server that holds plaintext. sgit protects them with keys: one vault per trust domain, a read key that cannot be turned into a write key, and append lanes that can write without reading. Files, names, trees, commit messages and refs are all encrypted on the client, so the server has nothing to protect and nothing to compute, and it can be anyone's. More on that in [sgit is a standard, not a server](sgit-is-a-standard.md).

## Measured on a real, busy vault

The measurements now: the 83-file vault and the 35,000-object vault, in full, with history and for one folder.

An 83-file vault says little about Scion's question: what happens when the repository is big and the clients are many. The right vault is the agents behind this newsroom share every day, with their mail, briefs, runs and analysis. On 16 October it had 1,295 commits, 5,281 files and about 35,000 encrypted objects, 527 MB with all its history, which is the size of a real application's source repository.

A full clone is the worst case: three and a half minutes for 35,423 objects. But no agent takes one. With one commit of history, the whole tree is 57 seconds; one 130-file folder with one commit is **13 seconds and 3 MB**, 137 objects, however large the vault is. A file fetched on demand is under 3 seconds; an up-to-date pull is 2.5. The full picture, with the honest edges, is in [One vault, ten agents, measured](one-vault-ten-agents.md).

On a small vault the client's own edges show instead: an 83-file vault took 59 seconds to clone with sgit 0.22.0, because two batches of objects were over the size limit of the Lambda that serves the API and the client fell back to reading one object at a time; the CLI's development branch splits a refused batch in two, and the same clone takes about 11 seconds.

And the time is the distance to the storage, not sgit. The same objects on local disk: the one-folder clone takes 0.8 seconds against a local API server, the full clone 69. On the small vault, the same encrypted files served by Python's built-in file server, with no sgit server at all, cloned in 1.6 seconds, identical file for file.

## Where Scion is ahead

Scion does blame, bisect and merges on the server and builds history indexes as derived data; sgit's server cannot read a commit, so those run on the client. Today sgit has path history, signed authorship, signed tags and verification, but no blame and no bisect. Where it is behind on its own terms: a partial clone of a long history still walks the commits one request at a time, so a folder with all 1,295 commits takes nearly four minutes, and a depth avoids it; `history log` for one file over that history takes minutes of CPU; one server process queues concurrent full clones; and the largest vault it has been proven on is 35,000 objects and ten agents, not 100 GB and 30,000 merges a day. Being designed for something is not the same as being proven at it.

Git and sgit also live side by side rather than in sync. A vault can sit in the same folder as a Git repository, and a vault can be committed into one and attached with its key on the other side; but there is no bridge that turns Git history into sgit history or back.

## What it means

I find it fascinating to watch the same idea arrive twice. Agents change what source control is for: the clients are always online, the volume is machine-scale, and the expensive thing is moving bytes nobody needs. Anthropic answered inside one trusted company, with a powerful server that does the work. sgit answers for everyone else, where the server should not be trusted at all: encrypt everything on the client, name every object by its ciphertext, let anyone keep the objects they fetched, and keep the server dumb enough that anyone can run it. The two designs meet in the middle on immutable objects, fetching only what is needed, no packfiles and compare-and-swap.

Scion's post concedes one point from the other side: it could not keep a merge queue at its rate, so "concurrent changes can conflict, but Claude can typically fix these conflicts". The merge went back to the agent. That is where sgit keeps it: a merge is a workflow step, made where the context and the policy are.

The practical difference is availability. Scion is a blog post. sgit is `pip install sgit-ai` today, with its code in the open, and it already carries [the vaults this site publishes](what-sgit-is.md) and the one its agents work in. The useful next steps are on the client: a small encrypted record of the commit chain so a partial clone does not walk history, blame as a fold over path history, and testing at a much larger scale.

## What this does not claim

- **sgit is not proven at Scion's scale.** Its largest vault in daily use is about 35,000 objects and ten agents.
- **The measurements are one run each, from cloud sandboxes.** A plain connection does better.
- **The fix for the small vault is not released yet.** It is on the CLI's development branch.
- **Scion's figures are Anthropic's.** From its post; not independently verified.
- **I have a stake.** sgit is ours.

If you run agents against a large repository and want to try an encrypted, cacheable alternative, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Anthropic, [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control), 13 October 2026, read again on 16 October. The measurements of the newsroom's shared vault are the sgit CLI team's, from 14 and 16 October, from the hosted service and from local disk; this site's agent checked the cache headers, re-ran the small vault's clone with the released CLI and the development branch, and checked the quotes and the code. sgit's facts are from the [sgit-ai](https://pypi.org/project/sgit-ai/) package and the [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) code and changelog; the documentation pages' loading numbers are from sgit.ai's live-vault case study.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#scion-and-sgit)

### Builds on

- [From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults](from-send-to-sgit.md) Eight months of SG/Send, checked against its own briefs and commits: how file sharing became sgit and vaults, the pace, and what the market said.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom](one-vault-ten-agents.md) The vault behind this newsroom, 35,000 objects and ten agents, measured eight ways: one folder in 13 seconds, history as the edge, storage as the bottleneck.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.

### Continued by

- [Where to invest in sgit: the tool, a hub for vaults, or open core, with the history of developer platforms, the evidence of use, three business plans, and the investor deck as a vault](where-to-invest-in-sgit.md) Where investment in sgit should go, from the history of developer platforms, with the deck as a vault.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom](one-vault-ten-agents.md) The vault behind this newsroom, 35,000 objects and ten agents, measured eight ways: one folder in 13 seconds, history as the edge, storage as the bottleneck.
- [The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think](the-value-of-constraints.md) sgit's encryption and open source matter less as features than as constraints: they remove the temptations that lead to server code, lock-in and bad decisions.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 141 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=141)

**Posting this article on LinkedIn?** The cover is [scion-and-sgit.jpg](banners/scion-and-sgit.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/scion-and-sgit.html)*
