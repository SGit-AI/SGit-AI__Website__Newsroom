---
title: sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: Git won not because of GitHub but because it is a standard: a way of laying out objects that any tool, any host and any person can read, and that GitHub, GitLab and a folder on a laptop all implement. sgit is the same kind of thing, and I think that is the most important thing to understand about it. People read encrypted git and picture a product with a server in the middle. There is a server, and it is the least interesting part. A vault is a set of encrypted files laid out by a convention: blobs, trees, commits and one mutable pointer per branch, every immutable object named by the SHA-256 of its ciphertext and marked -imm- in its name. Nothing in it has to be discovered: the vault key gives the read key, the read key gives the name of the ref, and the ref leads to the commit, the trees and the file, four plain GETs from any host that answers one. Writing is the same objects plus one compare-and-swap, which is all the API is for. Two independent implementations, the CLI and the browser app, speak it and check each other. So deploying sgit is choosing where the objects live, from a folder to a laptop to a static host to the hosted service, and how fast it is depends on how close they are. That design was not a plan to be minimal: it is what is left when the server cannot read a byte.
version: v0.12.79
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, standards, git, vaults, encryption, architecture, caching, static-hosting, open-source, deployment, article
status: published
---

!shot sd-onehash.webp | images/ | Everything in a vault is one hash away: the vault key gives the read key, the read key gives the ref's name by an HMAC, and the ref, the commit, the trees on the path and the blob are plain GETs; reads come from any host that answers a GET, writes need a compare-and-swap, and caching is by name, not by header. | architecture

## In short {#in-short}

- **Git is a standard.** That is why it won, not any one server.
- **sgit is one too.** Encrypted objects laid out by a convention.
- **Everything is one hash away.** The key gives every name; a file is four GETs.
- **The name says what can be cached.** `-imm-` is for ever; `-muw-` is the ref.
- **Any storage implements the read half.** A bucket, a CDN, GitHub Pages, a folder.
- **The server protects writes.** A compare-and-swap, and not much else.
- **The constraint designed it.** A server that cannot read leaves only small designs.

## Git is a standard {#git}

Git is not GitHub. It is a format: blobs, trees, commits and refs, named by their hashes, laid out in a way any tool can read. GitHub, GitLab, a bare repository on a server and a folder on a laptop all implement it, and that is why git survived every centralised system that promised to be faster: your history is not in anyone's product.

sgit was built the same way on purpose. Git solved the hard problems of history, branching and merging twenty years ago, and the workflows built on them are why it won, so sgit [copies git's object model](/articles/from-send-to-sgit.html#git) and changes one thing: where the trust sits. Everything is encrypted on the client, and the convention is designed so that nothing about reading a vault needs anyone's help. People read "encrypted git" and picture a product with a server in the middle. There is a server, and it is the least interesting part.

## What a vault is {#vault}

A vault is a set of files laid out by a convention. Four kinds of object, all ciphertext: blobs, the file contents; trees, a folder's encrypted names pointing at blob and tree ids; commits, a tree id, parents, a message and a signature; and one mutable pointer per branch, the ref. Every object except the ref and the branch index is named by the SHA-256 of its own ciphertext, so a name can never point at different bytes, anyone can check an object against its name, and anyone who has fetched one can keep it for ever.

The name says which is which. An immutable object's id is `obj-cas-imm-` and a hash; the mutable pointers are `ref-pid-muw-` and a hash. So anything between the storage and the reader, a browser, a proxy, a CDN, a CI cache, a page on a website, can decide to keep an object for ever by looking at its name, without reading a byte of it and without being told by a header. That is how the vault app in the browser got fast: it caches every `-imm-` object the first time it sees one and refetches only the ref. sgit.ai's own documentation pages are a vault read that way: [a cold load fetches 18 objects](https://sgit.ai/case-studies/live-vault-docs.html), the next load one 69-byte ref, and a load inside the two-minute freshness window nothing at all.

It is a trade made on purpose. sgit keeps no deltas between versions of a file; a changed file is a new object. Git stores deltas and has to be told what changed; sgit stores whole objects that anyone can cache without asking.

## Everything from one hash {#one-hash}

What makes it a standard rather than a service is that nothing in a vault has to be discovered. It is all derived from the key:

1. **The vault key** gives the vault id and, one way, the read key. The read key cannot be turned back into the write key, so it can be published.
2. **The read key gives the ref's name.** In the CLI's code it is the first twelve hex characters of an HMAC of the read key over `sg-vault-v1:file-id:ref:` and the vault id. The server never told you where the head is; you computed it.
3. **The ref holds the head commit id.** The commit holds the tree id; trees hold the ids of blobs and subtrees, with the names encrypted inside them. Ref, commit, the trees on the path, the blob: a file is four kinds of request from its read key, and every one is a plain GET of a fixed path.
4. **Writing is the same objects, PUT in batches,** and one compare-and-swap on the ref and the branch index.

Two independent implementations speak this format: the CLI, and the browser vault app, which the CLI team says sgit.ai's pages reduce to a reader of about ninety lines. A change made in the browser is one the CLI verifies, and the other way round. That is what a standard is: a format with more than one implementation that agree.

## Any storage implements the read half {#storage}

!shot sd-storage.webp | images/ | Deploying sgit is choosing where the objects live: a folder; a laptop running the hosted image; your own server; a static host such as GitHub Pages; or the hosted service, a Lambda in front of S3 behind CloudFront; from closer and faster to further and shared. | comparison

Because reading is plain GETs of fixed paths, any storage that answers a GET implements the read half of the convention: an S3 bucket, a CDN, GitHub Pages, a folder, Python's one-line file server. `sgit clone --transport static` reads from any of them, and `sgit publish` lays a vault out for one. This site [measured the difference](/articles/the-homepage-is-a-vault.html): 317 milliseconds a request through the vault API, against 44 for a small file from GitHub Pages.

The write half needs the one thing plain storage does not give you, a compare-and-swap on the ref, and that is what the API is for. Strip the convention down and the API has two jobs: protect writes, with an access token and the compare-and-swap, and shorten reads a little, with batches of fifty objects and a listing that makes a cold full clone fast. Everything else is storage.

So deploying sgit is choosing where the objects live, and every option is shipped: a folder, with `--transport local`; a laptop, with `sgit serve` running the hosted service's own image in Docker, Podman or a plain Python process; your own server, one container with a disk or a bucket; a static host, read-only; or the hosted service, a Lambda in front of S3 behind CloudFront. And how fast sgit is depends on how close they are. On [the vault behind this newsroom](/articles/one-vault-ten-agents.html), a one-folder clone is 13 seconds hosted and 0.8 seconds from a local server; on ruv.sgit.ai's hive runs, on a local server, every operation takes between 0.4 and 1.5 seconds, most of it starting Python and deriving the key. "How fast is sgit" is the wrong question. The right one is where the storage is, and how close.

## A cache you can compute {#cache}

Four GETs is cheap, but a page that serves one record a thousand times a minute does not want to walk trees. So the convention has a cache layer, shipped: `sgit cache add <path>` declares a path, and every push keeps an encrypted cache object for it at a location derived from the read key and the path. A reader with only the vault id and the read key computes where to look, makes one batch request for the ref and the candidates, checks the commit inside against the ref, and has the file with no walk. A miss or a stale entry falls back to the ordinary walk, so correctness never depends on the cache; losing one is a performance problem, never a correctness one.

This is Scion's "derived data", built by the writer instead of a server, and named by the key instead of indexed by it.

## Why the work stays on the client {#client}

[Scion](/articles/scion-and-sgit.html) moves history, blame and merges to the server. sgit keeps them on the client, and would even if the server could read the data, for the reason git did: a merge is a workflow step that needs the context of the change, the history and the policy that says who may merge what. In ruv.sgit, every worker in a hive writes to its own branch and the host merges them under the run's written mandate; in the vault behind this newsroom, ten agents meet on a named branch and resolve on the clone that has the conflict in front of it. Scion's own post concedes the point from the other side: it could not keep a merge queue at its rate, so "concurrent changes can conflict, but Claude can typically fix these conflicts". The merge went back to the agent there too.

And sgit keeps the property that made git git: a full clone is one command and a complete, verifiable copy of everything, and anyone with the key can rebuild it from any host. What changed is that the full clone became optional. A folder scope, a history depth, a sparse clone and the cache layer mean a client takes the part it needs, and a repository can hold large files without every client paying for them, which every git team has had to police by hand. The whole-history clone is the backup and the audit, and it is still there.

## The constraint that designed it {#constraint}

None of this was a plan to be minimal. The server cannot read a byte, so "just do it on the server" was never available: no server-side index, no server-side render, no merge the client did not make, no derived data the client could not compute from the key. Every feature had to be expressible as objects a writer produces and a reader derives. That is why the designs are small enough to be a standard, and why they fit in an article. It is the argument of [The value of constraints](/articles/the-value-of-constraints.html), applied to the format itself.

## What this does not claim {#limits}

- **Not a formal standard.** No standards body; a documented format with two implementations.
- **Not proven at Scion's scale.** The largest vault in daily use is about 35,000 objects and ten agents.
- **No blame or bisect yet.** And a partial clone of a long history walks the commits one at a time until a commit-chain object ships; a depth avoids it today.
- **The CDN in front of the hosted API does not cache object reads yet.** Browsers, clients and static hosts do.

If you want to implement the format somewhere new, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, after the sgit CLI team's review of the Scion article; written by this site's agent in the voice of this site, from the CLI team's draft; the editorial responsibility is mine. The derivation and the cache layer were checked by this site's agent in the [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) code (`Vault__Crypto`, `CLI__Cache`) and changelog; the loading numbers are from sgit.ai's [live-vault case study](https://sgit.ai/case-studies/live-vault-docs.html); the hive timings from ruv.sgit.ai's published ledger of 16 October; the Scion quote from [Anthropic's post](https://www.anthropic.com/engineering/redesigning-source-control).
