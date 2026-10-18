# Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there, sgit.ai

> On 17 October at 14:59 London time, rUv merged pull request #4239 into Ruflo's main branch. It was opened by Mondweep Chakravorty the night before, and it adds one page, docs/integrations/sgit-memory-checkpoints.md, 83 lines that document his adapter: an Agent Behaviour Policy compiled into Ruflo's own rules, checked by Ruflo's evaluator in enforce mode, gating checkpoints into an encrypted SGit vault. Of the 9,625 commits on Ruflo's main branch, it is the first to mention SGit or an ABP. This article puts the four pieces side by side, with a screenshot of each. The proof of concept: mondweep/sgit-ruv-memory, MIT, with sixteen passing tests and the video we analysed the same day. The pull request: three commits in one hour, one file, a description that states its own limits. How it was accepted: a review was requested from rUv as code owner, no formal approval was recorded and no checks ran; the maintainer merged it, squashed into commit 332f22e. And where it lives: a new docs/integrations folder on main, pinned to exact commits of the code, SGit and Ruflo. The page is careful about what it does not claim, which is why it could be merged quickly. One piece is still open, and it is on our side: the runnable example, SGit-AI/SGit-AI__Website__Ruv pull request #1, has had no review yet.

*Source: <https://newsroom.sgit.ai/articles/our-first-pr-in-ruflo.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there

# Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.1.0, 2 versions](versions/our-first-pr-in-ruflo.md) · [newsroom v0.12.95](https://newsroom.sgit.ai/admin/versions.html) · agentsruflosgitagent-behaviour-policyopen-sourcepull-requestgithubmemorymilestonearticle

***Abstract:** On 17 October at 14:59 London time, rUv merged pull request #4239 into Ruflo's main branch. It was opened by Mondweep Chakravorty the night before, and it adds one page, docs/integrations/sgit-memory-checkpoints.md, 83 lines that document his adapter: an Agent Behaviour Policy compiled into Ruflo's own rules, checked by Ruflo's evaluator in enforce mode, gating checkpoints into an encrypted SGit vault. Of the 9,625 commits on Ruflo's main branch, it is the first to mention SGit or an ABP. This article puts the four pieces side by side, with a screenshot of each. The proof of concept: mondweep/sgit-ruv-memory, MIT, with sixteen passing tests and the video we analysed the same day. The pull request: three commits in one hour, one file, a description that states its own limits. How it was accepted: a review was requested from rUv as code owner, no formal approval was recorded and no checks ran; the maintainer merged it, squashed into commit 332f22e. And where it lives: a new docs/integrations folder on main, pinned to exact commits of the code, SGit and Ruflo. The page is careful about what it does not claim, which is why it could be merged quickly. One piece is still open, and it is on our side: the runnable example, SGit-AI/SGit-AI__Website__Ruv pull request #1, has had no review yet.*

The pieces in order, London time: the talk and ruv.sgit.ai on 15 October; Mondweep's proof of concept on 16 October; pull request #4239 opened at 23:02 with three commits in the next hour; merged by rUv at 14:59 on 17 October as commit 332f22e; the page on Ruflo's main branch. Beside it, the video, our analysis, and the companion pull request on our side, still open.

SGit × Ruflo: one run, five ways in

Mondweep Chakravorty's video of an agent losing its workspace and getting its memory back: the run, the architecture, the gap, a page to step through it yourself, and the page that took it into Ruflo.

[1 · The runWhat if an agent loses its workspace?Twelve steps: memory saved, project deleted, memory restored in a fresh process, three safeguards tested.](what-if-an-agent-loses-its-workspace.md)[2 · The architectureWhen is the vault actually used?In three of twelve steps, on one machine, inside the adapter: what that proves and what it does not.](when-is-the-vault-actually-used.md)[3 · The gapThe policy guards the door; the command line uses the windowThe ABP checks the adapter's tools; Ruflo's own command line reaches the same memory file without it.](the-policy-guards-the-door.md)

4 · Step through itSGit × Ruflo, step by stepEvery step with its frame, command, output and diagram, linked to its moment in the video.[Watch the video ↗](https://youtu.be/rkh6BJiaIrQ)[Step through it](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html)[Read the code ↗](https://github.com/mondweep/sgit-ruv-memory)

[you are here5 · The mergeOur first PR in RufloMondweep's page on ABP-governed SGit checkpoints, merged into Ruflo's main branch by rUv: the four pieces that got it there.](our-first-pr-in-ruflo.md)

## In short

- **It is merged.** rUv merged pull request #4239 into Ruflo's main branch on 17 October at 14:59 London time.
- **It is one page.** `docs/integrations/sgit-memory-checkpoints.md`, 83 lines, documentation only.
- **It is a first.** Of 9,625 commits on Ruflo's main branch, it is the first to mention SGit or an ABP.
- **Mondweep wrote it.** Opened at 23:02 the night before, with three commits in the next hour.
- **The maintainer merged it.** A review was requested from rUv as code owner; no formal approval was recorded and no checks ran.
- **It states its own limits.** Proposed vocabulary, a vendored evaluator, semantic recall not validated: all on the page.
- **One piece is ours.** The runnable example, pull request #1 in our own organisation, is still open.

## What happened

On Friday 17 October, at 14:59 London time, rUv merged [pull request #4239](https://github.com/ruvnet/ruflo/pull/4239) into [ruvnet/ruflo](https://github.com/ruvnet/ruflo). Mondweep Chakravorty opened it at 23:02 the night before. It adds one file, [docs/integrations/sgit-memory-checkpoints.md](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md), which documents how an Agent Behaviour Policy can govern Ruflo's memory and keep its checkpoints in an encrypted SGit vault.

It is a documentation page, not a change to Ruflo's code, and the pull request says so. It is still a milestone for us. I checked Ruflo's whole history: of the 9,625 commits on its main branch, this is the first to mention SGit or an ABP, and Mondweep's first commit there. Two days earlier, at Agentic Engineering Live, [I said we were ready to sell this](agentics-ready-to-sell.md). Now the method has a page inside the project it governs, written by someone outside our team, and accepted by the project's maintainer.

Here are the four pieces, each with what you can see on GitHub.

## Piece 1: the proof of concept

mondweep/sgit-ruv-memory on GitHub: public, MIT licence, one contributor, five commits, the last of them 7607d72, "Validate Ruflo CLI exact and keyword recovery; disclose semantic vector gap". Folders for evidence, examples, scripts, the package, tests and the vendored Ruflo evaluator.

The code came first. [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory) is a small MCP server, MIT-licensed, with five commits on 16 October, the last at 23:58. It does one job: it compiles an ABP into Ruflo's rule format, asks a pinned copy of Ruflo's own policy evaluator for a decision in enforce mode before each of its tools runs, and keeps each memory checkpoint in its own encrypted SGit vault. Sixteen tests pass, by the author's own evidence.

We have already written about it, the same day, in three pieces and a page:

- [What if an agent loses its workspace?](what-if-an-agent-loses-its-workspace.md) walks through the twelve steps of his video: memory saved, project deleted, memory restored in a fresh process.
- [When is the vault actually used?](when-is-the-vault-actually-used.md) shows that the vault does its work in three of the twelve steps, and what that proves.
- [The policy guards the door](the-policy-guards-the-door.md) is about the path the policy does not cover: Ruflo's own command line.
- [The step-by-step page](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html) puts each step's frame, command and diagram next to the [video](https://youtu.be/rkh6BJiaIrQ).

## Piece 2: the pull request

Pull request #4239 on ruvnet/ruflo, marked Merged: "ruvnet merged 3 commits into ruvnet:main from mondweep:docs/sgit-memory-checkpoints". Conversation 2, Commits 3, Checks 0, Files changed 1, +83. Mondweep's description gives the flow, the validation, the source at 7607d72, the executable example in SGit-AI/SGit-AI__Website__Ruv#1, and "Documentation-only change in Ruflo". On the right, ruvnet is listed as reviewer, with the review still pending.

The pull request is called "docs: ABP-governed SGit memory checkpoints and Ruflo CLI recovery validation". It came from a branch on Mondweep's fork, `mondweep:docs/sgit-memory-checkpoints`, into `ruvnet:main`. Its description gives the chain in one line:

Flow: ABP mandate → strict memory-profile compiler → pinned Ruflo enforce evaluator → actual adapter operations → encrypted snapshot/isolated restore.

It lists the evidence, and it lists the gaps in the same breath: "Semantic quality is NOT validated; the semantic report is partial." It ends with what it is not: "Documentation-only change in Ruflo; no runtime defaults/dependencies changed and no full Ruflo npm suite run."

It has three commits, all on the evening of 16 October, London time:

| Commit | Time | What it did |
|---|---|---|
| `81e3697` | 23:02 | Document external SGit memory checkpoint MCP example |
| `269b9fc` | 23:35 | Document ABP compilation and enforced memory adapter operations |
| `6b49d58` | 23:59 | Document passing Ruflo CLI recovery and unresolved embedding persistence |

The second commit is the one that matters most to me. The first version documented the adapter; the second documents the ABP compiled into Ruflo's rules and enforced on every operation. Mondweep's comment on the pull request says it plainly: "the missing ABP layer is now implemented and validated, and this guide has been updated accordingly."

Files changed: one new file, docs/integrations/sgit-memory-checkpoints.md, 83 lines added, none removed. It opens with "External SGit memory checkpoints governed by an ABP", "This opt-in community example connects an Agent Behaviour Policy to a local memory adapter", the chain in bold, and a reproduce section that checks out the code at commit 7607d72.

## Piece 3: how it was accepted

The end of the pull request's timeline: Mondweep's follow-up to @ruvnet, "the missing ABP layer is now implemented and validated", with the source at e86cefa and the SGit example; the third commit, 6b49d58; the title change; and "ruvnet merged commit 332f22e into ruvnet:main".

The GitHub timeline, in London time:

1. **16 October, 23:02.** Opened, and a review requested from rUv automatically, as code owner.
2. **23:30.** Marked as a draft while the ABP layer went in. **23:36.** Ready for review again, and the title changed.
3. **23:59.** The third commit.
4. **17 October, 14:59.** Merged by rUv, squashed into one commit, `332f22e`, authored by Mondweep.

So "accepted" here means one specific thing, and it is worth being exact about it. There was no formal approving review: the review requested from rUv still shows as pending on the page. No checks ran; the Checks tab reads 0. The maintainer read it and merged it, which on a documentation page is a normal and sensible way to accept a contribution. It is also why the page's own care matters: with no automated gate, what got it in was the page being specific about what it claims.

## Piece 4: where it lives

The merged file on Ruflo's main branch, at ruflo / docs / integrations / sgit-memory-checkpoints.md: 83 lines, 7.5 KB, last commit 332f22e by mondweep. The rendered page, "External SGit memory checkpoints governed by an ABP", with links to the source and the SGit executable-example PR, and install steps that check out the code at an exact commit.

The page lives on [Ruflo's main branch, in docs/integrations](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md). It is the only file in a new `docs/integrations/` folder. It is not yet linked from Ruflo's docs index or its README, so for now you find it by link or by browsing the folder.

It pins everything it depends on. The code at `7607d72`. SGit at source commit `5597526`, because the declared version, 0.22.3, was not yet on the package index. Ruflo's evaluator at `1882006`, the commit of the Ruflo 3.56.10 release, and the same commit Mondweep's branch was built on. Anyone can reproduce what it describes, at those exact versions.

## What the page claims, and what it does not

I think this is the main reason it was merged in under a day. The page does not oversell. A few lines, as written:

- "This opt-in community example connects an Agent Behaviour Policy to a local memory adapter."
- "It does not register a native Ruflo memory backend or alter Ruflo's default/running policy configuration."
- "Three capabilities below are proposed vocabulary extensions, not claims of existing upstream support." The three are `write.memory.project`, `read.memory.project` and `delete.memory.project`; the fourth, `read.record.history`, already exists in the ABP.
- The evaluator "is currently vendored, not dynamically connected to Ruflo's running policy state."
- "Embedding-based semantic recall remains unvalidated."
- "Adapter policy does not restrict other shell or MCP tools", which is the gap [the policy guards the door](the-policy-guards-the-door.md) describes.

It ends with the next gates: diagnose why embeddings did not persist, show semantic recall with relevant and unrelated controls, and adopt a supported live policy interface instead of vendoring. That is a good list, and it is now in Ruflo's own repository, where Ruflo's contributors will see it.

The three proposed capabilities matter for the ABP too. They are the first memory vocabulary I have seen proposed from outside our team, from a real integration, and they are the kind of feedback the ABP needs.

## The piece still open is ours

SGit-AI/SGit-AI__Website__Ruv pull request #1, "Add local MCP example for policy-gated SQLite checkpoints and restore", marked Open: mondweep wants to merge 3 commits into SGit-AI:dev from mondweep:feat/mcp-memory-checkpoints. 35 files, +3,081. Companion: ruvnet/ruflo#4239, shown as Merged. No reviews.

The Ruflo page points to two things: Mondweep's repository, and a companion pull request in our own organisation, [SGit-AI/SGit-AI__Website__Ruv #1](https://github.com/SGit-AI/SGit-AI__Website__Ruv/pull/1). That one adds the runnable example to ruv.sgit.ai: 3 commits, 35 files, 3,081 lines. It is still open, with no reviews. His follow-up on the Ruflo pull request notes that his own updates to it were limited by connector permissions, though its branch, README and evidence are current.

So the order came out the other way round from what you might expect. Ruflo merged first. The next merge is ours to make, after a review.

## Why this matters

Three reasons, and I will keep them modest.

- **Someone else built it.** It is the first integration of the ABP and SGit into an agent framework that I know of by someone outside our team, and it is documented in that framework's own repository.
- **It is in the right place.** A page in Ruflo's docs reaches the people who run Ruflo, which is where an ABP is useful.
- **It carries its evidence.** Pinned commits, tests, a reproducible run, and its own limits. It is the [evidence-first](agentics-ready-to-sell.md) position, in practice, in someone else's repository.

Thank you, Mondweep, for the code, the video and the page, and rUv for merging it.

## Where to go next

The [SGit × Ruflo trail](what-if-an-agent-loses-its-workspace.md) has the run, the architecture and the gap. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), [watch the video](https://youtu.be/rkh6BJiaIrQ), and [read the merged page](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md).

## What this does not claim

- **Not a code change to Ruflo.** The merge adds documentation; Ruflo's runtime is unchanged, as the pull request says.
- **Not a formal review.** The maintainer merged it; no approving review or check is recorded.
- **Not an endorsement of every detail.** A merged page in a project's docs is not a statement by its maintainer about every claim in it.
- **"First" is from the commit history.** No commit on Ruflo's main branch before it mentions SGit or an ABP; other discussions elsewhere are not counted.
- **The code was read, not run, here.** Its tests and evidence are the author's.

If you are Mondweep, rUv, or anyone who has run this, and want to add to any of it, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

The pull request: [ruvnet/ruflo #4239](https://github.com/ruvnet/ruflo/pull/4239), its conversation, commits, files and timeline, read on 17 October 2026; the commits fetched with git, and Ruflo's full main-branch history, 9,625 commits, searched for SGit, ABP and the author. The merged page: [docs/integrations/sgit-memory-checkpoints.md](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md) at commit `332f22e`. The code: [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, at `7607d72`. The companion: [SGit-AI/SGit-AI__Website__Ruv #1](https://github.com/SGit-AI/SGit-AI__Website__Ruv/pull/1). The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), 17 October 2026, published here with his agreement. Screenshots of GitHub taken by this site's agent on 17 October 2026; times are converted from GitHub's UTC to London time. Written up and checked by this site's agent; the editorial responsibility is mine. Related: [agentics, ready to sell](agentics-ready-to-sell.md), [what if an agent loses its workspace?](what-if-an-agent-loses-its-workspace.md), [when is the vault actually used?](when-is-the-vault-actually-used.md), [the policy guards the door](the-policy-guards-the-door.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#our-first-pr-in-ruflo)

### Builds on

- [Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement path, and a marketplace for the consultants who deliver it](agentics-ready-to-sell.md) After the London talk, agentics is ready to sell: the market and its prices, our evidence-first position, the engagement path, and a consultants marketplace.
- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.
- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.

### Continued by

- [The Librarian's daily brief: everything that happened in my universe yesterday, the threads I left, and where my leverage is today](the-librarians-daily-brief.md) A daily brief from the Librarian: yesterday across every repository, the agents' debrief, threads to pick up, and where my leverage is today.
- [Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open](three-linkedin-pages.md) Three companies, no LinkedIn pages: the decisions, every drafted field with its count, thirty first posts already written, and a new profile, in the open.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 169 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=169)

**Posting this article on LinkedIn?** The cover is [our-first-pr-in-ruflo.jpg](banners/our-first-pr-in-ruflo.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/our-first-pr-in-ruflo.html)*
