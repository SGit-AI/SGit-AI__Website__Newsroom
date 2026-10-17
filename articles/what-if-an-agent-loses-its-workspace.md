# What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held, sgit.ai

> Mondweep Chakravorty has made a short video that answers a question every team running agents should ask: if an agent loses its workspace, does its memory come back, and do its written permissions still hold? In 104.7 seconds it replays a real terminal run in twelve steps. Ruflo, rUv's open-source agent orchestration, stores two facts in its memory. An adapter governed by an Agent Behaviour Policy saves that memory as an encrypted checkpoint made of SGit objects. The original project is deleted. A brand-new process restores the checkpoint, the restored database has the same SHA-256 fingerprint as the one saved, and Ruflo reads both facts back word for word. Along the way three safeguards are tested and hold: a request outside the agent's permission is refused, a deletion that needs approval is stopped, and a tampered checkpoint is rejected. The video is careful about its limits: recall by meaning was not validated. The code is public too, MIT, with 16 tests and recorded evidence, and its runner has since also validated keyword recall against Ruflo's real memory store. This is the first of three pieces on it, with a page that lets you step through the run yourself.

*Source: <https://newsroom.sgit.ai/articles/what-if-an-agent-loses-its-workspace.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held

# What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.1.0, 2 versions](versions/what-if-an-agent-loses-its-workspace.md) · [newsroom v0.12.90](https://newsroom.sgit.ai/admin/versions.html) · agentsruflosgitvaultsagent-behaviour-policymcpmemoryrecoveryvideoarticle

***Abstract:** Mondweep Chakravorty has made a short video that answers a question every team running agents should ask: if an agent loses its workspace, does its memory come back, and do its written permissions still hold? In 104.7 seconds it replays a real terminal run in twelve steps. Ruflo, rUv's open-source agent orchestration, stores two facts in its memory. An adapter governed by an Agent Behaviour Policy saves that memory as an encrypted checkpoint made of SGit objects. The original project is deleted. A brand-new process restores the checkpoint, the restored database has the same SHA-256 fingerprint as the one saved, and Ruflo reads both facts back word for word. Along the way three safeguards are tested and hold: a request outside the agent's permission is refused, a deletion that needs approval is stopped, and a tampered checkpoint is rejected. The video is careful about its limits: recall by meaning was not validated. The code is public too, MIT, with 16 tests and recorded evidence, and its runner has since also validated keyword recall against Ruflo's real memory store. This is the first of three pieces on it, with a page that lets you step through the run yourself.*

The twelve steps of the run and how each ended: five worked, three were safeguards refusing as intended, four were setup or summary. Not tested, and said so on screen: recall by meaning. From the video by Mondweep Chakravorty.

SGit × Ruflo: one run, five ways in

Mondweep Chakravorty's video of an agent losing its workspace and getting its memory back: the run, the architecture, the gap, a page to step through it yourself, and the page that took it into Ruflo.

[you are here1 · The runWhat if an agent loses its workspace?Twelve steps: memory saved, project deleted, memory restored in a fresh process, three safeguards tested.](what-if-an-agent-loses-its-workspace.md)[2 · The architectureWhen is the vault actually used?In three of twelve steps, on one machine, inside the adapter: what that proves and what it does not.](when-is-the-vault-actually-used.md)[3 · The gapThe policy guards the door; the command line uses the windowThe ABP checks the adapter's tools; Ruflo's own command line reaches the same memory file without it.](the-policy-guards-the-door.md)

4 · Step through itSGit × Ruflo, step by stepEvery step with its frame, command, output and diagram, linked to its moment in the video.[Watch the video ↗](https://youtu.be/rkh6BJiaIrQ)[Step through it](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html)[Read the code ↗](https://github.com/mondweep/sgit-ruv-memory)

[5 · The mergeOur first PR in RufloMondweep's page on ABP-governed SGit checkpoints, merged into Ruflo's main branch by rUv: the four pieces that got it there.](our-first-pr-in-ruflo.md)

## In short

- **The question.** If an agent loses its workspace, does its memory come back, and do its permissions still hold?
- **The answer, on screen.** Both facts came back exactly, in a fresh process, after the original was deleted.
- **The fingerprint matched.** The restored database has the same SHA-256 as the one saved.
- **Three safeguards held.** Out of scope refused, deletion without approval stopped, tampered copy rejected.
- **It says what it did not test.** Recall by meaning was switched off and is marked not validated.
- **It is a real run, and the code is public.** Ruflo and SGit pinned; 16 tests; the evidence is in the repository.
- **Step through it yourself.** Every step has a page with its frame, command, output and diagram.

## The question

Agents keep memory: facts they were told, decisions they made, what they found. That memory usually lives in a file in the agent's workspace. So what happens when the workspace goes, a container recycled, a disk wiped, a project deleted by mistake? Does the memory come back, and does it come back with the rules the agent was working under?

[Mondweep Chakravorty](https://www.linkedin.com/in/mondweepchakravorty/), a member of the #Ruflo-Federation and co-founder of the [Agentics Foundation's London chapter](https://london.agentics.org/), made a video that answers it with a real run: [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026. It is 104.7 seconds long. Each slide has the story on the left, for someone with no code knowledge, and the terminal on the right, labelled as an actual capture of the run.

His code is public at [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), under the MIT licence: a local MCP server of four tools, a strict compiler that turns an Agent Behaviour Policy into Ruflo rules, 16 tests, and the evidence from each run. The analysis behind this piece was made from what is on screen, frame by frame, in a separate session with Claude, and then checked against that code. Every number below comes from the video's timeline, a frame or the repository. If you would rather click than read, [step through it here](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html).

## The run, in twelve steps

### 1 · A real, pinned runtime

At [0:09](https://youtu.be/rkh6BJiaIrQ?t=9), `ruflo --version` returns v3.56.10, and the run prints the SGit source commit it uses, `559752641bc5…6ad0d4ad`, and the adapter: an ABP-governed local MCP server, version 0.2. Pinning the versions is what makes a run like this reproducible. [Step 1, in detail](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-1).

### 2 · Define the mandate

At [0:14](https://youtu.be/rkh6BJiaIrQ?t=14), four Agent Behaviour Policy rows, all scoped to the project: write memory, yes; read memory, yes; read history, yes; delete memory, approval. And one line that matters more than it looks: "No raw rule overrides. Unsupported or ambiguous policies fail closed." That is an [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) in miniature: what the agent may do, and where a person has to step in. In the code, the rows are compiled into Ruflo rules when the server starts, and every tool call is checked by a pinned copy of Ruflo's own policy evaluator, in enforce mode. [Step 2](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-2).

### 3 · Store two facts through Ruflo

At [0:21](https://youtu.be/rkh6BJiaIrQ?t=21), Ruflo's own command line stores two synthetic facts, with embeddings switched off: "Kestrel vehicles may charge only between 01:00 and 04:00 UTC", and "Kestrel checkpoints are retained for seven days". The terminal reports "[OK] Data stored successfully". [Step 3](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-3).

### 4 · Try something outside its permission

At [0:32](https://youtu.be/rkh6BJiaIrQ?t=32), the run asks the adapter to checkpoint a namespace called `forbidden`. It is refused with a `PermissionError`, and `checkpoint_files` is 0: nothing was written. [Step 4](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-4).

### 5 · Save an encrypted recovery point

Step 5 on the terminal: the checkpoint is saved with its id, a consistent SQLite backup, and three SHA-256 fingerprints, of the database, the ABP and the compiled policy. "Only encrypted SGit bare objects enter the checkpoint store." Frame from the video by Mondweep Chakravorty.

At [0:38](https://youtu.be/rkh6BJiaIrQ?t=38), the checkpoint for the `project` namespace is allowed. The adapter takes a consistent copy of the memory database, a SQLite backup rather than a raw file copy, and records three fingerprints: of the database, of the ABP and of the compiled policy. The screen says: "Only encrypted SGit bare objects enter the checkpoint store. Private keys remain in a separate private directory." Binding the data to the rules in force is the detail I like most. [Step 5](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-5).

### 6 · Approval means stop

At [0:45](https://youtu.be/rkh6BJiaIrQ?t=45), the run tries to close the run, which would delete memory. That row says approval, and none is supplied, so it stops with a `PermissionError` and `checkpoint_retained: true`. [Step 6](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-6).

### 7 · Remove the original workspace

At [0:51](https://youtu.be/rkh6BJiaIrQ?t=51), the disposable test project is deleted: `source_project_exists: false`, `original_database_exists: false`. The loss is real, not simulated. [Step 7](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-7).

### 8 · Restore in a fresh process

Step 8 on the terminal: a new MCP server restores the checkpoint into a workspace called fresh-runner; the database fingerprint is the same as in step 5, and matches_checkpoint is true. Frame from the video by Mondweep Chakravorty.

At [0:58](https://youtu.be/rkh6BJiaIrQ?t=58), a brand-new MCP server process restores the checkpoint into a workspace called `fresh-runner`. The database's SHA-256 begins `10ab6c56` and ends `d66a0b`, the same as in step 5, and `matches_checkpoint` is true. [Step 8](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-8).

### 9 · Ask Ruflo what it remembers

Step 9 on the terminal: Ruflo's own retrieve command returns both facts word for word, and the run reports a pass. Frame from the video by Mondweep Chakravorty.

At [1:04](https://youtu.be/rkh6BJiaIrQ?t=64), Ruflo itself, not the adapter, reads the restored memory. Both facts come back word for word: "PASS: both values match the CLI-written facts exactly." That the original tool does the reading is what makes this proof stronger than a demo that checks its own output. [Step 9](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-9).

### 10 · A missing fact stays missing

At [1:14](https://youtu.be/rkh6BJiaIrQ?t=74), a key that was never stored is looked up: "Key not found: never-stored", exit 1. The restore did not invent anything, and the check can fail. [Step 10](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-10).

### 11 · Change the saved copy, try again

Step 11 on the terminal: one checkpoint object is altered, the restore fails with a ValueError, and tampered_workspace_created is false. Frame from the video by Mondweep Chakravorty.

At [1:20](https://youtu.be/rkh6BJiaIrQ?t=80), one encrypted checkpoint object is altered and a restore is tried into a workspace called `tampered`. It fails with a `ValueError`, and `tampered_workspace_created` is false. Integrity fails closed. The code shows how: the adapter compares the digest of the stored ciphertext with the one it recorded when it saved the checkpoint, and refuses before anything is decrypted. [Step 11](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-11).

### 12 · What this run proves

At [1:26](https://youtu.be/rkh6BJiaIrQ?t=86), the acceptance summary: exact recall PASS 2/2; ABP denial PASS; deletion that needs approval BLOCKED, checkpoint retained; fresh-process restore PASS; tampered restore BLOCKED; and semantic recall NOT VALIDATED, because embeddings were off. [Step 12](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-12).

## What it proves, and what it says it does not

The video's closing slide: the facts came back and the safeguards held; still to validate, recall by meaning, real-world value, and installation and ongoing reliability. Frame from the video by Mondweep Chakravorty.

The video's own closing slide puts it well: both facts recovered exactly; unauthorised access blocked; unapproved deletion blocked; altered checkpoint rejected. And still to validate: recall by meaning, real-world value, and installation and ongoing reliability.

The repository adds one more result. Its acceptance runner stores two facts through Ruflo, checkpoints Ruflo's real `.swarm/memory.db`, removes the whole project, and reads the facts back in the restored workspace: exact values and keyword search result keys match before and after. Recall by meaning is reported as partial, because no vectors were stored even with embeddings on; the README names that as the next investigation.

What makes it more than a demo is the shape of the loop. Most "memory that persists" demos skip the deletion or reuse the same process. This one stores, saves, deletes for real, restores in a new process, and reads back with the original tool. It also tests the refusals, not only the happy path, and includes a negative control. And it is honest about scope, in the run itself, not in a footnote.

## Why it matters to me

This is the first time someone outside our own sessions has taken the two ideas we keep arguing for, an encrypted vault as an agent's memory and a [behaviour policy beside the prompt](a-policy-beside-the-prompt.md), and run them together inside someone else's agent stack, on camera. It is exactly the combination [Agentics, ready to sell](agentics-ready-to-sell.md) describes as the product: a hive, a memory and a mandate. Mondweep is one of the two people that piece names to deliver it.

## Where to go next

The run raises two questions this piece does not answer. **When is the vault actually used?** In twelve steps it is written or read in three, on one machine, inside the adapter: [the architecture piece](when-is-the-vault-actually-used.md) explains why that is the honest answer. **Is every path to the memory guarded?** Ruflo's own command line reaches the memory file without the policy: [the third piece](the-policy-guards-the-door.md) asks what that means. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), with every frame, command and diagram.

## What this does not claim

- **From the screen and the code.** The audio was not transcribed; the code was read, not run, by this site.
- **A proof of concept, not a product.** The video says so; reliability and real-world value are still to validate.
- **Recall by meaning was not tested.** Exact recall was.
- **The facts are synthetic.** Kestrel is a test name, not a real fleet.
- **The analysis is an AI's, reviewed here.** It was made by Claude for me and checked against the frames by this site's agent.

## Where this comes from

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation and published here with his agreement; the frames are his and are not covered by this site's licence. The analysis: Claude (Anthropic), 17 October 2026, made for me from on-screen content, delivered as an sgit vault with the video's timeline, frames and an architecture addendum, and written up and checked against the timeline and the code by this site's agent; the editorial responsibility is mine. The code: Mondweep Chakravorty, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, read at its commit of 16 October 2026, including its README, tests and evidence. Ruflo is [rUv's open-source agent orchestration](https://github.com/ruvnet/ruflo), under the MIT licence. Context: [Agent Behaviour Policies](https://abp.sgit.ai/what-is-an-abp/index.html), [Agentics, ready to sell](agentics-ready-to-sell.md).

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#what-if-an-agent-loses-its-workspace)

### Builds on

- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement path, and a marketplace for the consultants who deliver it](agentics-ready-to-sell.md) After the London talk, agentics is ready to sell: the market and its prices, our evidence-first position, the engagement path, and a consultants marketplace.
- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.

### Continued by

- [Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there](our-first-pr-in-ruflo.md) rUv merged Mondweep's pull request #4239: one docs page, the first commit on Ruflo's main branch to mention SGit or an ABP. The four pieces, shown.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 164 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=164)

**Posting this article on LinkedIn?** The cover is [what-if-an-agent-loses-its-workspace.jpg](banners/what-if-an-agent-loses-its-workspace.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-if-an-agent-loses-its-workspace.html)*
