# What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead, sgit.ai

> Between 3 and 27 October, sgit shipped ten releases, and each one fixed a bottleneck that a real workload had found. A one-file commit on a 76,000-file vault went from 29 minutes to 4.6 seconds; a pull of a 300-file pass on 228,000 files from 566 to 31.7 seconds; a one-folder clone of a pack vault from 36 to 2.8 seconds. The ideas came from earlier work of mine: MGraph-DB's cross-references, Memory-FS's reads by offset, caching on content addresses, and the rule that the writer pays. It is time to stop describing sgit as "like Git". This is the map of what sgit does that Git does not, what Git also has, where Git is clearly ahead, and what is designed but not yet shipped.

*Source: <https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead

# What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-27 · [article v1.0.0](versions/what-sgit-does-that-git-does-not.md) · [newsroom v0.13.112](https://newsroom.sgit.ai/admin/versions.html) · sgitperformancegitgithub-pagesvaultsencryptionengineeringarticle

***Abstract:** Between 3 and 27 October, sgit shipped ten releases, and each one fixed a bottleneck that a real workload had found. A one-file commit on a 76,000-file vault went from 29 minutes to 4.6 seconds; a pull of a 300-file pass on 228,000 files from 566 to 31.7 seconds; a one-folder clone of a pack vault from 36 to 2.8 seconds. The ideas came from earlier work of mine: MGraph-DB's cross-references, Memory-FS's reads by offset, caching on content addresses, and the rule that the writer pays. It is time to stop describing sgit as "like Git". This is the map of what sgit does that Git does not, what Git also has, where Git is clearly ahead, and what is designed but not yet shipped.*

sgit's measured speed-ups in October 2026, before and after, on a log scale.

## In short

- **Ten sgit releases between 3 and 27 October,** each one a bottleneck found by a real workload and fixed.
- **Minutes to seconds, per command:** a one-file commit on 76,000 files, 29 minutes to 4.6 seconds; a pull on 228,000 files, 566 to 31.7 seconds.
- **The ideas are not new to me:** MGraph-DB, Memory-FS, caching on content addresses, and the writer pays.
- **Stop comparing sgit with Git as a copy.** Compare what it does that Git does not.
- **Git has no equivalent** for encrypted names and messages, read keys, blind writes, or byte-range folder reads from plain storage.
- **Git has it too:** partial clones, shallow clones, no-checkout clones and kept packs. My memo over-claimed these.
- **Git is far ahead** on merges, identity, its ecosystem and maturity.
- **Next, not now:** reading one file with no clone, and websites whose files come from vaults.

## Every bottleneck becomes a release

This is how I like to work. Push a tool until something breaks, measure exactly where it broke, fix that, release, and push again. In October the push came from the [PHP October 2026 newsroom](https://team.php.oct.2026.newsroom.sgit.ai/), whose agents took sgit vaults from thousands of files to tens of thousands, then to gigabytes of captures. Every time they hit a wall, they wrote a field report, the sgit CLI team reproduced it on a synthetic vault of the same shape, and a release followed.

Ten sgit releases, 3 to 27 October 2026, with the number that made the case for each one.

The [sgit-ai package on PyPI](https://pypi.org/project/sgit-ai/) shows ten releases in that window, from 0.17.0 on 3 October to 0.26.0 at 01:26 UTC on 27 October. The early ones were about the network: keep-alive connections, fetching each shared sub-tree once, a full clone in one parallel sweep. The middle ones were about trust in history: a format gate, signed commits checked on every client, rewinds refused, signed tags, undo and amend. The last three are where the numbers changed by orders of magnitude.

- **0.24.0, [pack mode](https://cli.sgit.ai/docs/update-to-0-24-0.html), 22 October.** A vault whose objects travel as one zip per push, compressed before they are encrypted. The newsroom's source watch, 29,861 files and 1.6 GB, had outgrown the server's object listing, which timed out after 90.8 seconds. As a [pack vault](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/), the listing took 0.73 seconds and a fresh clone went from 827 to 95 seconds.
- **0.25.0, [the cost follows the change](https://cli.sgit.ai/docs/update-to-0-25-0.html), 26 October.** A flat-map cache, a scan cache built on Git's own index rule, and a commit that rebuilds only the folders on the changed file's path. On a 76,000-file vault, a one-file commit went from 1,739 seconds to 4.6.
- **0.26.0, [index packs](https://cli.sgit.ai/docs/update-to-0-26-0.html), 27 October.** Every data pack now carries an index pack beside it, and the client can keep packs whole and fetch one folder by byte ranges. A pull of a 300-file pass on 228,000 files went from 566 to 31.7 seconds, and with the indexes to 16.9.

The last of those took [eighteen hours](https://cli.sgit.ai/articles/pack-indexes-shipped.html), from the newsroom's first morning on 0.25.0 to the merge of 0.26.0, through five reviews and three rounds of fixes.

From the newsroom's first morning on 0.25.0 to 0.26.0 in eighteen hours. Figure from cli.sgit.ai.

And it has not stopped. A fix on a branch, planned for 0.26.1, takes `pack index verify` from 1,002 seconds to 3.5 on 24,000 files, after the newsroom's researcher measured the released version at about 57 seconds a pack.

## Minutes to seconds, with the caveats

The chart at the top has the headline ratios. They are real, and I am pleased with them, but they need reading carefully.

- **They are per command, not per working day.** The newsroom's full pass went from 57 minutes to 35, not to seconds, because, in the researcher's own words, "They are 33 of the 35 minutes": the capture work, not sgit.
- **Where each was measured matters.** The 228,000-file and 76,000-file numbers are the CLI team's synthetic vaults on an in-memory host, with the network left out. The newsroom's numbers are real vaults in cloud sessions, with the network in.
- **There was a regression.** The first `status` after upgrading to 0.25.0 took 18 minutes 23 seconds on the curator's 4.2 GB clone, because the new cache had to read every file once on a slow session disk. 0.26.0 fixed it by seeding the cache on every write.
- **Some things got slower, on purpose.** On 76,000 files, the first push and each compaction take 35 to 50 seconds longer in 0.26.0, because the writer now builds the snapshot index. That is the price, paid once.

## Where the speed came from

None of these ideas appeared from nowhere. Most of what made 0.25.0 and 0.26.0 fast is work I had done before, in other projects, applied to a vault.

Where the speed came from: earlier work, the principle it taught, and the sgit release that used it.

- **[MGraph-DB](https://pypi.org/project/mgraph-db/).** My typed graph library keeps, for every edge, its two ends, and for every node, its edges both ways. That is the principle the CLI team wrote down as "cross-reference everything", and it is why an index pack has members that map each blob to its paths and each file to its commits.
- **[Memory-FS](https://pypi.org/project/memory-fs/).** Its storage providers already cover memory, disk, SQLite and zip. The CLI team's measurement showed the one change it needed: keep the zip's directory between reads, and "that turns 1.3 s per read into 5 µs". `clone --pack-store` now reads every object from its pack by offset, verified on every read.
- **Caching on content addresses.** A tree id is the hash of the tree, so, as the 0.25.0 notes put it, "the cache needs no invalidation". The flat-map cache and the scan cache rest on that, and so does the older `sgit cache` command from August.
- **[Type_Safe, in OSBot-Utils](https://pypi.org/project/osbot-utils/).** This one is a lesson against myself. The 0.24.0 slowness was mostly Type_Safe parsing on the read path, about 3 ms a tree. The fix was to keep the types where they belong: "Type and validate at the writer; read plain JSON at the reader."
- **The writer pays.** On 26 October I set out the indexing principles I have used before, including a graph built on a JSON store; the CLI team [wrote them down](https://cli.sgit.ai/articles/indexes-the-writer-pays-for.html) and built them that evening. In LETS terms (load, extract, transform, save), the expensive step is done once, by the writer, and saved next to the data. In the words of the release image: "The writer pays once, at push time; every reader after it skips the walk."

This is also the [explorer and villager](https://newsroom.sgit.ai/articles/explorer-coding.html) cycle I keep writing about. A brief from 12 March, in the sgit CLI repository, put it as "The Explorer builds. The Villager improves." In October the cycle ran in days: build, review in the open, fix, release.

## Stop comparing sgit with Git

sgit's own documentation still opens with "sgit is git for encrypted vaults", and the [guide for Git users](https://cli.sgit.ai/docs/sgit-for-git-users.html) says "If you know git, you know most of sgit." That framing helped when sgit was young: same verbs, same mental model. It now undersells it, because the interesting parts are the ones Git does not have. So I asked my research team for a row-by-row comparison against Git's and GitHub's own documentation, with an honest verdict on each row. Here is the result.

What sgit does that Git does not, what Git also has, where Git is ahead, and what is next.

## What Git has no equivalent for

- **The host reads nothing.** Contents, file names, commit messages and branch names are encrypted on the client. The closest Git add-on, git-crypt, says in its [README](https://github.com/AGWA/git-crypt/blob/master/README.md) that it "does not encrypt file names, commit messages, symlink targets, gitlinks, or other metadata". The honest edge: sgit's host still sees sizes, timing and object counts, and in pack mode which commit each push carried.
- **A read key is a capability, not a permission.** A read key is [derived from the vault key by a one-way function](https://cli.sgit.ai/docs/credentials.html), so it can never become write access, and it works from any static host with no account. GitHub's read role is enforced by a server you have to trust, and it can be revoked; sgit's cannot be revoked after the fact. And it is per vault, not per folder: "A partial clone is not an access boundary", says sgit's [limitations page](https://cli.sgit.ai/docs/limitations.html), so the answer today is a vault per folder.
- **Write without read.** An [append lane](https://cli.sgit.ai/docs/append-lane-messaging.html) lets a sender put something into a vault and learn nothing, not even whether anyone else writes there: the answer to a write is `{"ok": true}`. No Git or GitHub role can write without reading. This is a server feature, with no sgit command of its own yet.
- **Fetch one folder by byte ranges from plain storage.** On a pack vault, `clone --path` reads the zip's directory and then just the byte ranges of that folder's objects, each one verified by its hash: 2.8 seconds and 12.5 MB, against 36 seconds and the whole 88 MB pack. Git's HTTP code uses ranged requests only to resume an interrupted download; its partial clones need a smart server that can read the content.
- **Indexes shipped by the writer, signed and encrypted.** Git's commit-graph and pack indexes are fast, mature and built locally, as trusted plaintext caches. sgit's index packs travel with the data and are checked against the commit and its signature before use; a bad one is skipped. As the threat model puts it, "An index is a plan, never a proof."
- **Encrypt a file to a person, inside the store.** `sgit pki encrypt --recipient` seals a file to someone's public key. Git signs commits; it has no "encrypt this to that person" inside the repository.

## What Git has too, and my memo over-claimed

My memo for this article listed "packs, the path, the ability to have selective repos" as things sgit has and Git does not. The research says otherwise, and I would rather correct it here than have someone else do it.

- **Packs.** Git has stored and transferred packs from its early days, and they are delta-compressed, which sgit's are not. Keeping received packs whole, as `--pack-store` does, is Git's default above `fetch.unpackLimit`. What is different is that sgit's packs are ciphertext on plain object storage, with no Git server.
- **The path.** `clone --path` is close to Git's partial clone plus sparse-checkout, which is mature and used at very large scale. sgit's differences: it works against ciphertext on S3, it refuses a commit outside the scope by name, and two scoped clones in different folders never conflict.
- **Selective working copies.** `git clone --no-checkout` has existed for years. sgit's addition is the agent loop: `pull --no-checkout`, then `checkout --since-pull`, so an agent writes the few hundred files that changed instead of 79,000.
- **Shallow clones, private branches and signed commits** all have Git equivalents.
Where sgit does less work than Git, and where Git is faster. Figure from cli.sgit.ai.

## Where Git is clearly ahead

- **Merges.** Git's default merge detects renames and merges line by line. sgit's merges are whole-file, with conflict files.
- **Staging and partial commits.** sgit refuses them by design; its limitations page says, plainly, "If your workflow depends on committing three of seven changed files, sgit will fight you".
- **Identity.** GitHub knows who pushed, protects branches per person, and signing keys can expire and be revoked. sgit's signatures say which clone wrote a commit, not who is allowed to write.
- **Storage and ids.** Git has delta packs and garbage collection; sgit has no pruning yet. Git's ids are 160-bit by default; sgit's format 1 is 48-bit, and format 2, 128-bit, is opt-in per vault.
- **The ecosystem and maturity.** Forges, review, CI, search, blame, bisect, every IDE, and twenty years of stability. Most of it needs a host that can read the content, which is exactly what sgit refuses to have.

## Next, not now: one file with no clone, and websites from vaults

Two things in my memo are designed, not shipped, and I want to be clear about which is which.

- **Hitting a file directly.** On a normal vault this already works: [a file is four plain GETs of fixed paths](https://cli.sgit.ai/articles/sgit-is-a-standard-one-hash-away.html), from any static host, GitHub Pages included. What is not shipped is reading one file from a pack vault by byte range with no clone at all. The 0.26.0 notes say so: Phase 4 "is not in this release", though the offsets it needs are already written into every pack.
- **Websites on GitHub Pages, with their files in vaults.** The PHP newsroom opened PROJECT-003 today, at the design stage: three normal vaults for the sites' assets, data and archive, with GitHub Pages carrying only the pages. GitHub's own [repository limits page](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits) advises: "Store programmatically generated files outside of Git, such as in object storage." And [Git LFS cannot be used with GitHub Pages](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage). The newsroom's sites are nowhere near GitHub's [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) of a 1 GB site and a 10-minute deploy. The problem is history growth: every site's deploy runs every 15 minutes and uploads the whole site, and the references site changed 177,426 lines of generated HTML in one day. It also needs normal vaults, because the browser library cannot read pack vaults yet.

## The workflows where this matters

Put together, these are the jobs that are hard in Git and natural in sgit today:

1. **Many agents on one very large vault, one folder each.** Each agent clones its folder; its commits outside the folder are refused by name; agents in different folders never conflict; the host learns nothing about the contents. In Git you can get close with partial clones and sparse-checkout, but you need a server that reads everything.
2. **Give a reader read-only access to encrypted material, with no account.** Publish a read key; the reader fetches from a static host. This site publishes read keys for its vaults on purpose.
3. **Let an agent deposit into someone's inbox without being able to read it.** An append lane, with the payload sealed to the recipient's public key.
4. **Trust an index without trusting the host.** Every index is verified against a signed commit before it is used.

## What this does not claim

- **The timings are the CLI team's and the newsroom's own measurements,** not re-run for this article; the setting of each is stated above.
- **The verdicts are against sgit-ai 0.26.0 and Git's and GitHub's documentation,** read on 27 October 2026.
- **sgit's own documentation is partly out of date.** Its limitations page still says commit signing is "planned work", though commits have been signed since 0.19.0, and its 0.26.0 notes still sit under an "Unreleased" heading in the changelog.
- **"Git has no equivalent" means the mainstream toolchain.** Add-ons such as git-crypt and git-remote-gcrypt cover parts of it, with the trade-offs their own READMEs state.

## Where this comes from

sgit's release notes for [0.24.0](https://cli.sgit.ai/docs/update-to-0-24-0.html), [0.25.0](https://cli.sgit.ai/docs/update-to-0-25-0.html) and [0.26.0](https://cli.sgit.ai/docs/update-to-0-26-0.html); cli.sgit.ai's articles [pack indexes, shipped](https://cli.sgit.ai/articles/pack-indexes-shipped.html), [indexes the writer pays for](https://cli.sgit.ai/articles/indexes-the-writer-pays-for.html), [indexes in the pack](https://cli.sgit.ai/articles/indexes-in-the-pack.html), [is there any overhead?](https://cli.sgit.ai/articles/is-there-any-overhead.html), [pack mode in four rounds](https://cli.sgit.ai/articles/pack-mode-four-rounds.html) and [keys the way Git does it](https://cli.sgit.ai/articles/keys-the-way-git-does-it.html); its docs on [partial clones](https://cli.sgit.ai/docs/partial-clones.html), [history integrity](https://cli.sgit.ai/docs/history-integrity.html) and [limitations](https://cli.sgit.ai/docs/limitations.html); the sgit CLI repository's changelog, response notes and threat model, read on 27 October 2026; [PyPI release times](https://pypi.org/project/sgit-ai/#history); the PHP October 2026 newsroom's briefs on [pack mode](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__moving-a-vault-to-pack-mode/), [0.25.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-26__brief__for-the-sgit-cli-team-0-25-0-in-the-newsroom/) and [0.26.0](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__sgit-0-26-0/); Git's documentation on [git-clone](https://git-scm.com/docs/git-clone), [pack format](https://git-scm.com/docs/gitformat-pack) and [commit-graph](https://git-scm.com/docs/commit-graph); GitHub's documentation linked above. Two figures are cli.sgit.ai's own, credited in their captions. Related: [you can feel good engineering](https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html). Written up by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#what-sgit-does-that-git-does-not)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 308 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=308)

**Posting this article on LinkedIn?** The cover is [what-sgit-does-that-git-does-not.jpg](banners/what-sgit-does-that-git-does-not.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.html)*
