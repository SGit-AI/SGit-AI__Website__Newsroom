---
title: What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead
date: 2026-10-27
author: Dinis Cruz
author_url: about/index.html
summary: Between 3 and 27 October, sgit shipped ten releases, and each one fixed a bottleneck that a real workload had found. A one-file commit on a 76,000-file vault went from 29 minutes to 4.6 seconds; a pull of a 300-file pass on 228,000 files from 566 to 31.7 seconds; a one-folder clone of a pack vault from 36 to 2.8 seconds. The ideas came from earlier work of mine: MGraph-DB's cross-references, Memory-FS's reads by offset, caching on content addresses, and the rule that the writer pays. It is time to stop describing sgit as "like Git". This is the map of what sgit does that Git does not, what Git also has, where Git is ahead today and how little of that is out of reach, and what is designed but not yet shipped. On 28 October sgit-ai 0.27.0 closed six of the eighteen rows where Git was ahead, line-level merges, partial commits, signing with your own key, rename detection, blame and grep, each checked against Git's own output. The sgit CLI team reviewed this article against their code, and it is corrected and extended from their review.
version: v0.13.112
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, performance, git, github-pages, vaults, encryption, engineering, article
status: published
---

!shot sf-speedups.webp | images/ | sgit's measured speed-ups in October 2026, before and after, on a log scale. | chart

## In short {#in-short}

- **Ten sgit releases between 3 and 27 October,** each one a bottleneck found by a real workload and fixed.
- **Minutes to seconds, per command:** a one-file commit on 76,000 files, 29 minutes to 4.6 seconds; a pull on 228,000 files, 566 to 31.7 seconds.
- **The ideas are not new to me:** MGraph-DB, Memory-FS, caching on content addresses, and the writer pays.
- **Stop comparing sgit with Git as a copy.** Compare what it does that Git does not.
- **Git has no equivalent** for a host that reads nothing, read keys, custody without access, policy the vault enforces on every clone, blind writes, or byte-range folder reads from plain storage.
- **Git has it too:** partial, shallow and no-checkout clones, kept packs, and committing named files. My memo over-claimed some of these.
- **sgit-ai 0.27.0 closed six of Git's leads on 28 October:** line-level merges, partial commits, signing with your own key, rename detection, blame and grep, each checked against Git.
- **Git is still ahead** on cherry-pick, rebase, bisect, hooks and worktrees, designed and next; on deltas and garbage collection; and on hosted review and CI. Almost all of it is client-side, so it can be built.
- **A few things are out of reach by design:** anything the host would have to read, and taking back what a reader already has.
- **Next, not now:** one file from a pack vault with no clone, and websites whose files come from vaults.
- **Reviewed by the sgit CLI team** against their code, and corrected.

## Every bottleneck becomes a release {#releases}

This is how I like to work. Push a tool until something breaks, measure exactly where it broke, fix that, release, and push again. In October the push came from the [PHP October 2026 newsroom](https://team.php.oct.2026.newsroom.sgit.ai/), whose agents took sgit vaults from thousands of files to tens of thousands, then to gigabytes of captures. Every time they hit a wall, they wrote a field report, the sgit CLI team reproduced it on a synthetic vault of the same shape, and a release followed.

!shot sf-releases.webp | images/ | Ten sgit releases, 3 to 27 October 2026, with the number that made the case for each one. | chart

The [sgit-ai package on PyPI](https://pypi.org/project/sgit-ai/) shows ten releases in that window, from 0.17.0 on 3 October to 0.26.0 at 01:26 UTC on 27 October. The early ones were about the network: keep-alive connections, fetching each shared sub-tree once, a full clone in one parallel sweep. The middle ones were about trust in history: a format gate, signature verification that every sgit client enforces in a vault that requires it, rewinds refused, signed tags, undo and amend. The last three are where the numbers changed by orders of magnitude.

- **0.24.0, [pack mode](https://cli.sgit.ai/docs/update-to-0-24-0.html), 22 October.** A vault whose objects travel as one zip per push, compressed before they are encrypted. The newsroom's source watch, 29,861 files and 1.6 GB, had outgrown the server's object listing, which timed out after 90.8 seconds. As a [pack vault](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/), the listing took 0.73 seconds and a fresh clone went from 827 to 95 seconds.
- **0.25.0, [the cost follows the change](https://cli.sgit.ai/docs/update-to-0-25-0.html), 26 October.** A flat-map cache, a scan cache built on Git's own index rule, and a commit that rebuilds only the folders on the changed file's path. On a 76,000-file vault, a one-file commit went from 1,739 seconds to 4.6, as cli.sgit.ai's build agent measured it for the [release notes](https://cli.sgit.ai/docs/update-to-0-25-0.html); on the newsroom's own 79,465-file vault, the CLI team's record has it going from 4 minutes to 9 seconds.
- **0.26.0, [index packs](https://cli.sgit.ai/docs/update-to-0-26-0.html), 27 October.** Every data pack now carries an index pack beside it, and the client can keep packs whole and fetch one folder by byte ranges. A pull of a 300-file pass on 228,000 files went from 566 to 31.7 seconds (measured under a profiler, which inflates both; the ratio stands), and with the indexes to 16.9 in a plain run.

The last of those took [eighteen hours](https://cli.sgit.ai/articles/pack-indexes-shipped.html), from the newsroom's first morning on 0.25.0 to the merge of 0.26.0, through five reviews and three rounds of fixes.

!shot sf-cli-pack-indexes-shipped.webp | images/ | From the newsroom's first morning on 0.25.0 to 0.26.0 in eighteen hours. Figure from cli.sgit.ai. | screenshot

And it has not stopped. A fix now on `dev` as the pre-release 0.26.1.dev0, and in the next release, takes `pack index verify` from 1,002 seconds to 3.5 on 24,000 files, after the newsroom's researcher measured the released version at about 57 seconds a pack.

## Minutes to seconds, with the caveats {#numbers}

The chart at the top has the headline ratios. They are real, and I am pleased with them, but they need reading carefully.

- **They are per command, not per working day.** The newsroom's full pass went from 57 minutes to 35, not to seconds, because, in the researcher's own words, "They are 33 of the 35 minutes": the capture work, not sgit.
- **Where each was measured matters.** The 228,000-file and 76,000-file numbers are the CLI team's synthetic vaults on an in-memory host, with the network left out. The newsroom's numbers are real vaults in cloud sessions, with the network in.
- **There was a regression.** The first `status` after the upgrade to 0.25.0 took 18 minutes 23 seconds on the curator's 4.2 GB pack clone, because the new scan cache was built by reading every file of a freshly written clone, almost all of it waiting on a slow session disk. 0.26.0 fixed it by seeding the cache on every write.
- **Some things got slower, on purpose.** On 76,000 files, the first push and each compaction take 35 to 50 seconds longer in 0.26.0, because the writer now builds the snapshot index. That is the price, paid once.

## Where the speed came from {#lineage}

None of these ideas appeared from nowhere. Most of what made 0.25.0 and 0.26.0 fast is work I had done before, in other projects, applied to a vault.

!shot sf-lineage.webp | images/ | Where the speed came from: earlier work, the principle it taught, and the sgit release that used it. | chart

- **[MGraph-DB](https://pypi.org/project/mgraph-db/).** My typed graph library keeps, for every edge, its two ends, and for every node, its edges both ways. That is the principle the CLI team wrote down as "cross-reference everything", and it is why an index pack has members that map each blob to its paths and each file to its commits.
- **[Memory-FS](https://pypi.org/project/memory-fs/).** Its storage providers already cover memory, disk, SQLite and zip. The CLI team's measurement showed the one change it needed: keep the zip's directory between reads, and "that turns 1.3 s per read into 5 µs". `clone --pack-store` now reads every object from its pack by offset, verified on every read.
- **Caching on content addresses.** A tree id is the hash of the tree, so, as the 0.25.0 notes put it, "the cache needs no invalidation". The flat-map cache and the scan cache rest on that, and so does the older `sgit cache` command from August.
- **[Type_Safe, in OSBot-Utils](https://pypi.org/project/osbot-utils/).** This one is a lesson against myself. The 0.24.0 slowness was mostly Type_Safe parsing on the read path, about 3 ms a tree. The fix was to keep the types where they belong: "Type and validate at the writer; read plain JSON at the reader."
- **The writer pays.** On 26 October I set out the indexing principles I have used before, including a graph built on a JSON store; the CLI team [wrote them down](https://cli.sgit.ai/articles/indexes-the-writer-pays-for.html) and built them that evening. In LETS terms (load, extract, transform, save), the expensive step is done once, by the writer, and saved next to the data. In the words of the release image: "The writer pays once, at push time; every reader after it skips the walk."

This is also the [explorer and villager](https://newsroom.sgit.ai/articles/explorer-coding.html) cycle I keep writing about. A brief from 12 March, in the sgit CLI repository, put it as "The Explorer builds. The Villager improves." In October the cycle ran in days: build, review in the open, fix, release.

## Stop comparing sgit with Git {#framing}

sgit's own documentation still opens with "sgit is git for encrypted vaults", and the [guide for Git users](https://cli.sgit.ai/docs/sgit-for-git-users.html) says "If you know git, you know most of sgit." That framing helped when sgit was young: same verbs, same mental model. It now undersells it, because the interesting parts are the ones Git does not have. So I asked my research team for a row-by-row comparison against Git's and GitHub's own documentation, with an honest verdict on each row. Here is the result.

!shot sf-map.webp | images/ | What sgit does that Git does not, what Git also has, what can be built, and what never can. | chart

## What Git has no equivalent for {#only-sgit}

Grouped by what they give you. The sgit CLI team's review added four of these, which I had missed.

**Privacy and access**

- **The host reads nothing.** Contents, file names, commit messages and branch names are encrypted on the client. The closest Git add-on, git-crypt, says in its [README](https://github.com/AGWA/git-crypt/blob/master/README.md) that it "does not encrypt file names, commit messages, symlink targets, gitlinks, or other metadata". The honest edge, in full: the host still sees sizes, timing and object counts; which trees are equal; in pack mode, which commit each push carried and which files share a folder; with compression on, how compressible each file is; and, for a scoped clone, which byte ranges it reads.
- **A read key is a capability.** It is [derived from the vault key](https://cli.sgit.ai/docs/credentials.html) one way, so it never becomes write access, and it works from any static host with no account. Writing, though, is a permission the host checks, not cryptography. A read-key holder who can also write to the store can make history that verifies, which is the threat model's top accepted risk. It is per vault, not per folder: "A partial clone is not an access boundary", says sgit's [limitations page](https://cli.sgit.ai/docs/limitations.html), so the answer today is a vault per folder.
- **Rotation, and moving house.** `sgit vault rekey` and `sgit vault move` give a vault a new key, and optionally a new server, going forward. Nobody can revoke a clone someone already has, in sgit or on GitHub.
- **Custody without access.** `sgit vault mirror` copies and verifies a published vault without its key. A backup service or a second host can hold the vault, check it, and learn nothing.

**Trust carried by the vault**

- **Policy the vault enforces on every clone.** The format gate (the minimum client, the features in use) and `signatures-required` live in the vault's encrypted branch index, and every sgit client enforces them at clone and pull, before it writes anything. In Git, signature checks are each user's local settings; a repository cannot require them of whoever clones it.
- **Rewinds refused on every clone.** A remote head that does not descend from the last one accepted is refused by name, unless you pass `--accept-rewind`. Git's default fetch takes a forced update with one line of output.
- **A secret guard.** A commit refuses vault keys, zips carrying keys, and links in the tree pointing at secrets.
- **Indexes shipped by the writer, signed and encrypted.** Git's commit-graph and pack indexes are fast, mature and built locally, as trusted plaintext caches. sgit's index packs travel with the data, anchored to their commit and checked under the vault's signature policy before use (an unsigned index is accepted unless the vault requires signatures), and a bad one is skipped. As the threat model puts it, "An index is a plan, never a proof."

**Reading and writing on plain storage**

- **Fetch one folder by byte ranges from plain storage.** On a pack vault, `clone --path` reads the zip's directory and then just the byte ranges of that folder's objects, each one verified by its hash: 2.8 seconds and 12.5 MB, against 36 seconds and the whole 88 MB pack. Git's HTTP code uses ranged requests only to resume an interrupted download; its partial clones need a smart server that can read the content.
- **A read path that skips the walk.** `sgit cache add <path>` puts a hot file at a location only key holders can compute, read in one request, for an edge function or a page.
- **Any static host, or none.** `sgit serve` runs the vault's browser and API locally in a container; `sgit publish` and `serve --static` lay a vault out for any host that answers a GET. A reader with the read key needs no account and no server code.
- **Write without read.** An [append lane](https://cli.sgit.ai/docs/append-lane-messaging.html) lets a sender put something into a vault and learn nothing, not even whether anyone else writes there: the answer to a write is `{"ok": true}`. No Git or GitHub role can write without reading. It is a server feature; the sgit command for it is still to come.
- **Writes shaped for agents.** `sgit write <path> --also <path> --push --json` commits named files straight to the head, atomically, and publishes them in one call, without scanning the working copy; `checkout --since-pull` writes only what changed.
- **Seal a file to a person.** `sgit pki encrypt --recipient` writes a file sealed to someone's public key, which you then commit. Git signs; it has no "encrypt this to that person".

## What Git has too, and my memo over-claimed {#git-has-it}

My memo for this article listed "packs, the path, the ability to have selective repos" as things sgit has and Git does not. The research says otherwise, and I would rather correct it here than have someone else do it.

- **Packs.** Git has stored and transferred packs from its early days, and they are delta-compressed, which sgit's are not. Keeping received packs whole, as `--pack-store` does, is Git's default above `fetch.unpackLimit`. What is different is that sgit's packs are ciphertext on plain object storage, with no Git server.
- **The path.** `clone --path` is close to Git's partial clone plus sparse-checkout, which is mature and used at very large scale. sgit's differences: it works against ciphertext on S3, it refuses a commit outside the scope by name, and two scoped clones in different folders never conflict.
- **Selective working copies.** `git clone --no-checkout` has existed for years. sgit's addition is the agent loop: `pull --no-checkout`, then `checkout --since-pull`, so an agent writes the few hundred files that changed instead of 79,000.
- **Committing named files, and now hunks.** `sgit write` commits the files you name, atomically, and leaves other edits alone: Git's `git commit <paths>`, in the form an agent needs. Since 0.27.0, `sgit commit` takes paths too, `commit -p` commits parts of a file, and `--list-hunks` and `--hunk` let an agent pick hunks by number. There is no persistent staging area, by design.
- **History tools.** `history log` with `--grep`, `--since`, `--until`, `--author`, `--file`, `--patch` and `--stat`; `history diff`, `show`, `reflog`, `undo`, `revert` and `reset`; `commit --amend`, stash and signed tags; and since 0.27.0, `history blame`, `sgit grep` over the working copy or any revision, `log -S` and `-G`, and rename detection with `log --follow`.
- **Shallow clones, private branches and signed commits** all have Git equivalents, and sgit has them: `clone --depth`, `fetch --unshallow`, combinable with `--path`, and a key per clone; since 0.27.0, also a signature with your own SSH or OpenPGP key, verified against your allowed signers, beside the clone's own.

!shot sf-cli-where-git-is-faster.webp | images/ | Where sgit does less work than Git, and where Git is faster. Figure from cli.sgit.ai. | screenshot

## Where Git is ahead, and how fast the gap is closing {#git-ahead}

These were real gaps when I wrote the first version of this map, and most of them were minor or mid-level for the way we use sgit. Almost everything Git is ahead on runs on the client in Git too, on plaintext the client already has, so sgit can build it the same way. The CLI team wrote a Git-parity roadmap on 28 October, with Git the client as the bar and every new feature off by default, and released the first part of it the same day.

!shot sf-parity.webp | images/ | Six of Git's eighteen leads closed in sgit-ai 0.27.0, each checked against Git, and the twelve still open. | comparison

**Closed in sgit-ai 0.27.0, 28 October**, each checked by the CLI's build agent against Git's own output:

- **Line-level merges.** `pull --merge lines` and `branch merge --merge lines`, with Git's conflict markers; opt-in, with the whole-file `.conflict` still the default. 4,500 random merges were byte-identical to `git merge-file`.
- **Partial commits.** `commit` with paths, `commit -p`, and `--list-hunks` and `--hunk` for agents.
- **Signing with your own key.** `commit -S`, signed tags, merges and reverts, with SSH or OpenPGP keys, verified against the allowed signers in your Git configuration. It is a second signature beside the clone's own.
- **Rename detection,** a port of Git's: 90 of 90 pairs equal `git diff -M --name-status`.
- **Blame:** 25 of 25 files equal `git blame --porcelain`.
- **Grep and the pickaxe.** `sgit grep` over the working copy or any revision, decrypted in memory, and `log -S` and `-G`: 120 of 120 grep runs equal `git grep`.

**Still ahead, by how firm the plan is:**

- **Designed and next in the CLI team's queue,** about 21 days of work in all: cherry-pick, built on the line merge; local hooks that never sync; rebase, never rewriting pushed history; bisect; and worktrees.
- **Waiting on another team or the server:** reading one file from a pack vault with no clone, and a command for append lanes.
- **Sketched, built when a workload asks:** garbage collection, delta compression, and `archive`, `shortlog`, `describe` and aliases.
- **No working plan yet:** per-folder read access, which needs per-folder keys, and submodules.
- **Who may write.** GitHub knows who pushed, protects branches per person, and expires and revokes its signing keys. A signature with your own key now says which person signed, when you verify it against your allowed signers; accounts, protected branches and an owner-signed list of who may write are moved to a future server the roadmap calls SGitHub, with review and CI.
- **Maturity.** Twenty years of it. Only time fixes that one.

## What a host that reads nothing can never do {#limits-of-the-model}

A few things are out of reach by design, not by effort, and each has a client-side substitute:

- **Anything the host would have to read:** server-side search, diffs, a merge button, scanning. Do it in the client, the browser, or a runner that holds the key.
- **Taking back what a reader already has.** No system can; GitHub cannot either. sgit rotates forward.
- **Per-folder permissions inside one key.** The host cannot tell folders apart. Per-folder access needs per-folder keys, which are designed.
- **Hiding every piece of metadata.** Padding and decoy reads reduce the leak; they never remove it.
- **Optimising the store on the host,** and a host that enforces fast-forward only. The client does both jobs instead: client-side deltas and pruning, and the rewind guard that ships today.

## Next, not now: one file with no clone, and websites from vaults {#next}

Two things in my memo are designed, not shipped, and I want to be clear about which is which.

- **Hitting a file directly.** On a normal vault this already works, from any static host, GitHub Pages included: [four plain GETs](https://cli.sgit.ai/articles/sgit-is-a-standard-one-hash-away.html) for a file at the root, one more for each folder above it, and one batch request for a path declared with `sgit cache add`. `history log --vault-key` already runs with no clone; a `cat` that does is a small addition. What is not shipped is reading one file from a pack vault by byte range with no clone at all. The 0.26.0 notes say so: Phase 4 "is not in this release", though the offsets it needs are already written into every pack.
- **Websites on GitHub Pages, with their files in vaults.** The PHP newsroom opened PROJECT-003 today, at the design stage: three normal vaults for the sites' assets, data and archive, with GitHub Pages carrying only the pages. GitHub's own [repository limits page](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits) advises: "Store programmatically generated files outside of Git, such as in object storage." And [Git LFS cannot be used with GitHub Pages](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage). The newsroom's sites are nowhere near GitHub's [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) of a 1 GB site and a 10-minute deploy. The problem is history growth: every site's deploy runs every 15 minutes and uploads the whole site, and the references site changed 177,426 lines of generated HTML in one day. It also needs normal vaults, because the browser library cannot read pack vaults yet.

## The workflows where this matters {#workflows}

Put together, these are the jobs that are hard in Git and natural in sgit today:

1. **Many agents on one very large vault, one folder each.** Each agent clones its folder; its commits outside the folder are refused by name; agents in different folders never conflict; the host learns nothing about the contents. In Git you can get close with partial clones and sparse-checkout, but you need a server that reads everything.
2. **Give a reader read-only access to encrypted material, with no account.** Publish a read key; the reader fetches from a static host. This site publishes read keys for its vaults on purpose.
3. **Let an agent deposit into someone's inbox without being able to read it.** An append lane, with the payload sealed to the recipient's public key.
4. **Trust an index without trusting the host.** Every index is anchored to its commit and checked under the vault's signature policy before it is used.
5. **Hand a vault to a backup host that cannot read it.** `vault mirror` copies and verifies it, keyless.
6. **Make a vault's rules travel with it.** Require signatures, or a minimum client, and every clone enforces it.

## What this does not claim {#limits}

- **The timings are the CLI team's and the newsroom's own measurements,** not re-run for this article; the setting of each is stated above.
- **The verdicts are against sgit-ai 0.26.0, and the section on where Git is ahead against 0.27.0,** with Git's and GitHub's documentation, read on 27 and 28 October 2026.
- **The checks against Git are the CLI team's.** The 4,500 merges, 90 rename pairs, 25 blamed files and 120 grep runs were run by cli.sgit.ai's build agent, not re-run for this article.
- **"Git has no equivalent" means the mainstream toolchain.** Add-ons such as git-crypt and git-remote-gcrypt cover parts of it, with the trade-offs their own READMEs state.

## Reviewed, and corrected {#review}

The sgit CLI team reviewed this article on 28 October against their code at `640069a`: the source, every command group's help, the changelog, the threat model and their response notes. Their verdict: accurate on the whole, too strong in sgit's favour in two places, and underselling it in several. What changed:

- **The 29 minutes.** They could not find it in their records. It is in cli.sgit.ai's 0.25.0 release notes, measured by that site's build agent on its own 76,000-file vault, so it stays, attributed, with their own figures beside it.
- **Two claims were too strong:** that a signature says which clone wrote a commit (it proves a key holder), and that every index is checked against a signed commit (it is checked under the vault's signature policy, which may not require one). Both now say so.
- **Several were too weak.** sgit commits named files (`sgit write`), reads one file with no clone on a normal vault, rotates keys, mirrors vaults it cannot read, carries its policy to every clone, refuses rewinds, and guards against committing secrets. All of that is above now.
- **Smaller fixes:** commits were signed long before 0.19.0, which added verification; the 18-minute `status` was the cache's first build on a fresh clone; the `pack index verify` fix is on `dev` as 0.26.1.dev0; the 566-second pull was measured under a profiler; a file deep in folders takes more than four requests; and the list of what the host sees is longer.

The review is [on the record](https://newsroom.sgit.ai/reviews/), with an answer to each finding.

## Where this comes from {#sources}

The sgit CLI site's [comparison of sgit and Git](https://cli.sgit.ai/docs/sgit-and-git.html), checked against 0.27.0, its [sign-off of 0.27.0](https://cli.sgit.ai/builds/0-27-0.html) and the CLI team's [Git-parity roadmap](https://cli.sgit.ai/research/git-parity-roadmap.html), read on 28 October 2026; sgit's release notes for [0.24.0](https://cli.sgit.ai/docs/update-to-0-24-0.html), [0.25.0](https://cli.sgit.ai/docs/update-to-0-25-0.html) and [0.26.0](https://cli.sgit.ai/docs/update-to-0-26-0.html); cli.sgit.ai's articles [pack indexes, shipped](https://cli.sgit.ai/articles/pack-indexes-shipped.html), [indexes the writer pays for](https://cli.sgit.ai/articles/indexes-the-writer-pays-for.html), [indexes in the pack](https://cli.sgit.ai/articles/indexes-in-the-pack.html), [is there any overhead?](https://cli.sgit.ai/articles/is-there-any-overhead.html), [pack mode in four rounds](https://cli.sgit.ai/articles/pack-mode-four-rounds.html) and [keys the way Git does it](https://cli.sgit.ai/articles/keys-the-way-git-does-it.html); its docs on [partial clones](https://cli.sgit.ai/docs/partial-clones.html), [history integrity](https://cli.sgit.ai/docs/history-integrity.html) and [limitations](https://cli.sgit.ai/docs/limitations.html); the sgit CLI repository's changelog, response notes and threat model, read on 27 October 2026; [PyPI release times](https://pypi.org/project/sgit-ai/#history); the PHP October 2026 newsroom's briefs on [pack mode](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/), [0.25.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-26__brief__for-the-sgit-cli-team-0-25-0-in-the-newsroom/) and [0.26.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__sgit-0-26-0/); Git's documentation on [git-clone](https://git-scm.com/docs/git-clone), [pack format](https://git-scm.com/docs/gitformat-pack) and [commit-graph](https://git-scm.com/docs/commit-graph); GitHub's documentation linked above. Two figures are cli.sgit.ai's own, credited in their captions. Related: [you can feel good engineering](https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html). The sgit CLI team's review of this article, 28 October 2026, on the record. Written up by this site's agent, newsroom.writer; the editorial responsibility is mine.
