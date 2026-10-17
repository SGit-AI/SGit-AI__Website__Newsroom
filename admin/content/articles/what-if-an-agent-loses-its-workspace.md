---
title: What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: Mondweep Chakravorty has made a short video that answers a question every team running agents should ask: if an agent loses its workspace, does its memory come back, and do its written permissions still hold? In 104.7 seconds it replays a real terminal run in twelve steps. Ruflo, rUv's open-source agent orchestration, stores two facts in its memory. An adapter governed by an Agent Behaviour Policy saves that memory as an encrypted checkpoint made of SGit objects. The original project is deleted. A brand-new process restores the checkpoint, the restored database has the same SHA-256 fingerprint as the one saved, and Ruflo reads both facts back word for word. Along the way three safeguards are tested and hold: a request outside the agent's permission is refused, a deletion that needs approval is stopped, and a tampered checkpoint is rejected. The video is careful about its limits: recall by meaning was not tested. This is the first of three pieces on it, with a page that lets you step through the run yourself.
version: v0.12.89
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, ruflo, sgit, vaults, agent-behaviour-policy, mcp, memory, recovery, video, article
status: published
---

!shot rf-board.webp | images/ | The twelve steps of the run and how each ended: five worked, three were safeguards refusing as intended, four were setup or summary. Not tested, and said so on screen: recall by meaning. From the video by Mondweep Chakravorty. | comparison

!trail sgit-ruflo

## In short {#in-short}

- **The question.** If an agent loses its workspace, does its memory come back, and do its permissions still hold?
- **The answer, on screen.** Both facts came back exactly, in a fresh process, after the original was deleted.
- **The fingerprint matched.** The restored database has the same SHA-256 as the one saved.
- **Three safeguards held.** Out of scope refused, deletion without approval stopped, tampered copy rejected.
- **It says what it did not test.** Recall by meaning was switched off and is marked not validated.
- **It is a real run.** A replay of a terminal capture, with the Ruflo version and the SGit commit pinned.
- **Step through it yourself.** Every step has a page with its frame, command, output and diagram.

## The question {#question}

Agents keep memory: facts they were told, decisions they made, what they found. That memory usually lives in a file in the agent's workspace. So what happens when the workspace goes, a container recycled, a disk wiped, a project deleted by mistake? Does the memory come back, and does it come back with the rules the agent was working under?

[Mondweep Chakravorty](https://www.linkedin.com/in/mondweepchakravorty/), a member of the #Ruflo-Federation and co-founder of the [Agentics Foundation's London chapter](https://london.agentics.org/), made a video that answers it with a real run: [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026. It is 104.7 seconds long. Each slide has the story on the left, for someone with no code knowledge, and the terminal on the right, labelled as an actual capture of the run.

The analysis behind this piece was made from what is on screen, frame by frame, in a separate session with Claude. The audio was not transcribed. Every number below comes from the video's timeline or a frame. If you would rather click than read, [step through it here](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html).

## The run, in twelve steps {#steps}

### 1 · A real, pinned runtime {#step-1}

At [0:09](https://youtu.be/rkh6BJiaIrQ?t=9), `ruflo --version` returns v3.56.10, and the run prints the SGit source commit it uses, `559752641bc5…6ad0d4ad`, and the adapter: an ABP-governed local MCP server, version 0.2. Pinning the versions is what makes a run like this reproducible. [Step 1, in detail](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-1).

### 2 · Define the mandate {#step-2}

At [0:14](https://youtu.be/rkh6BJiaIrQ?t=14), four Agent Behaviour Policy rows, all scoped to the project: write memory, yes; read memory, yes; read history, yes; delete memory, approval. And one line that matters more than it looks: "No raw rule overrides. Unsupported or ambiguous policies fail closed." That is an [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) in miniature: what the agent may do, and where a person has to step in. [Step 2](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-2).

### 3 · Store two facts through Ruflo {#step-3}

At [0:21](https://youtu.be/rkh6BJiaIrQ?t=21), Ruflo's own command line stores two synthetic facts, with embeddings switched off: "Kestrel vehicles may charge only between 01:00 and 04:00 UTC", and "Kestrel checkpoints are retained for seven days". The terminal reports "[OK] Data stored successfully". [Step 3](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-3).

### 4 · Try something outside its permission {#step-4}

At [0:32](https://youtu.be/rkh6BJiaIrQ?t=32), the run asks the adapter to checkpoint a namespace called `forbidden`. It is refused with a `PermissionError`, and `checkpoint_files` is 0: nothing was written. [Step 4](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-4).

### 5 · Save an encrypted recovery point {#step-5}

!shot rf-term-05.webp | images/ | Step 5 on the terminal: the checkpoint is saved with its id, a consistent SQLite backup, and three SHA-256 fingerprints, of the database, the ABP and the compiled policy. "Only encrypted SGit bare objects enter the checkpoint store." Frame from the video by Mondweep Chakravorty. | comparison

At [0:38](https://youtu.be/rkh6BJiaIrQ?t=38), the checkpoint for the `project` namespace is allowed. The adapter takes a consistent copy of the memory database, a SQLite backup rather than a raw file copy, and records three fingerprints: of the database, of the ABP and of the compiled policy. The screen says: "Only encrypted SGit bare objects enter the checkpoint store. Private keys remain in a separate private directory." Binding the data to the rules in force is the detail I like most. [Step 5](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-5).

### 6 · Approval means stop {#step-6}

At [0:45](https://youtu.be/rkh6BJiaIrQ?t=45), the run tries to close the run, which would delete memory. That row says approval, and none is supplied, so it stops with a `PermissionError` and `checkpoint_retained: true`. [Step 6](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-6).

### 7 · Remove the original workspace {#step-7}

At [0:51](https://youtu.be/rkh6BJiaIrQ?t=51), the disposable test project is deleted: `source_project_exists: false`, `original_database_exists: false`. The loss is real, not simulated. [Step 7](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-7).

### 8 · Restore in a fresh process {#step-8}

!shot rf-term-08.webp | images/ | Step 8 on the terminal: a new MCP server restores the checkpoint into a workspace called fresh-runner; the database fingerprint is the same as in step 5, and matches_checkpoint is true. Frame from the video by Mondweep Chakravorty. | comparison

At [0:58](https://youtu.be/rkh6BJiaIrQ?t=58), a brand-new MCP server process restores the checkpoint into a workspace called `fresh-runner`. The database's SHA-256 begins `10ab6c56` and ends `d66a0b`, the same as in step 5, and `matches_checkpoint` is true. [Step 8](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-8).

### 9 · Ask Ruflo what it remembers {#step-9}

!shot rf-term-09.webp | images/ | Step 9 on the terminal: Ruflo's own retrieve command returns both facts word for word, and the run reports a pass. Frame from the video by Mondweep Chakravorty. | comparison

At [1:04](https://youtu.be/rkh6BJiaIrQ?t=64), Ruflo itself, not the adapter, reads the restored memory. Both facts come back word for word: "PASS: both values match the CLI-written facts exactly." That the original tool does the reading is what makes this proof stronger than a demo that checks its own output. [Step 9](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-9).

### 10 · A missing fact stays missing {#step-10}

At [1:14](https://youtu.be/rkh6BJiaIrQ?t=74), a key that was never stored is looked up: "Key not found: never-stored", exit 1. The restore did not invent anything, and the check can fail. [Step 10](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-10).

### 11 · Change the saved copy, try again {#step-11}

!shot rf-term-11.webp | images/ | Step 11 on the terminal: one checkpoint object is altered, the restore fails with a ValueError, and tampered_workspace_created is false. Frame from the video by Mondweep Chakravorty. | comparison

At [1:20](https://youtu.be/rkh6BJiaIrQ?t=80), one encrypted checkpoint object is altered and a restore is tried into a workspace called `tampered`. It fails with a `ValueError`, and `tampered_workspace_created` is false. Integrity fails closed. [Step 11](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-11).

### 12 · What this run proves {#step-12}

At [1:26](https://youtu.be/rkh6BJiaIrQ?t=86), the acceptance summary: exact recall PASS 2/2; ABP denial PASS; deletion that needs approval BLOCKED, checkpoint retained; fresh-process restore PASS; tampered restore BLOCKED; and semantic recall NOT VALIDATED, because embeddings were off. [Step 12](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html#step-12).

## What it proves, and what it says it does not {#proves}

!shot rf-outcome.webp | images/ | The video's closing slide: the facts came back and the safeguards held; still to validate, recall by meaning, real-world value, and installation and ongoing reliability. Frame from the video by Mondweep Chakravorty. | comparison

The video's own closing slide puts it well: both facts recovered exactly; unauthorised access blocked; unapproved deletion blocked; altered checkpoint rejected. And still to validate: recall by meaning, real-world value, and installation and ongoing reliability.

What makes it more than a demo is the shape of the loop. Most "memory that persists" demos skip the deletion or reuse the same process. This one stores, saves, deletes for real, restores in a new process, and reads back with the original tool. It also tests the refusals, not only the happy path, and includes a negative control. And it is honest about scope, in the run itself, not in a footnote.

## Why it matters to me {#why}

This is the first time someone outside our own sessions has taken the two ideas we keep arguing for, an encrypted vault as an agent's memory and a [behaviour policy beside the prompt](/articles/a-policy-beside-the-prompt.html), and run them together inside someone else's agent stack, on camera. It is exactly the combination [Agentics, ready to sell](/articles/agentics-ready-to-sell.html) describes as the product: a hive, a memory and a mandate. Mondweep is one of the two people that piece names to deliver it.

## Where to go next {#next}

The run raises two questions this piece does not answer. **When is the vault actually used?** In twelve steps it is written or read in three, on one machine, inside the adapter: [the architecture piece](/articles/when-is-the-vault-actually-used.html) explains why that is the honest answer. **Is every path to the memory guarded?** Ruflo's own command line reaches the memory file without the policy: [the third piece](/articles/the-policy-guards-the-door.html) asks what that means. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), with every frame, command and diagram.

## What this does not claim {#limits}

- **From the screen only.** The audio was not transcribed; what Mondweep says may add context.
- **A proof of concept, not a product.** The video says so; reliability and real-world value are still to validate.
- **Recall by meaning was not tested.** Exact recall was.
- **The facts are synthetic.** Kestrel is a test name, not a real fleet.
- **The analysis is an AI's, reviewed here.** It was made by Claude for me and checked against the frames by this site's agent.

## Where this comes from {#sources}

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation and published here with his agreement; the frames are his and are not covered by this site's licence. The analysis: Claude (Anthropic), 17 October 2026, made for me from on-screen content only, delivered as an sgit vault with the video's timeline, frames and an architecture addendum, and written up and checked against the timeline by this site's agent; the editorial responsibility is mine. Ruflo is [rUv's open-source agent orchestration](https://github.com/ruvnet/ruflo), under the MIT licence. Context: [Agent Behaviour Policies](https://abp.sgit.ai/what-is-an-abp/index.html), [Agentics, ready to sell](/articles/agentics-ready-to-sell.html).
