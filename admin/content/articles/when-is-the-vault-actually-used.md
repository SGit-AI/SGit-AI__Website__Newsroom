---
title: When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: The first piece walked through Mondweep Chakravorty's video step by step. This one asks a sharper question: in a run that is about an encrypted vault, when is the vault actually used? The answer, drawn stage by stage from the frames, is in three steps of twelve. It is written in step 5, when a consistent copy of Ruflo's memory database is saved as encrypted SGit objects with fingerprints of the data, the ABP and the compiled policy. It is read in step 8, when a brand-new process restores it with the same fingerprint. It is read and rejected in step 11, when one object has been altered. In step 6 it is what the policy protects, and in step 7 it survives the deletion because it lives outside the project. It sits on the same machine, with its keys in a separate folder; no vault server, push or clone appears. It is implemented in the adapter, which calls the SGit library at a pinned commit and creates a separate vault for each checkpoint, and Ruflo knows nothing about it. The policy is compiled into Ruflo's own rule format and checked by a pinned copy of Ruflo's evaluator, inside the adapter. Not used: Ruflo's hive-mind, Ruflo's running policy state, and vector search. All of this is confirmed by the author's published code. That is not a weakness; it is what a recovery copy should look like, and it shows the pattern works with any tool's memory file. What it does not yet show is the vault leaving the machine.
version: v0.12.90
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, ruflo, sgit, vaults, architecture, agent-behaviour-policy, mcp, memory, video, article
status: published
---

!shot rf-matrix.webp | images/ | Who does what, step by step: which steps write or read the vault and which use Ruflo's own command line. | comparison

!trail sgit-ruflo

## In short {#in-short}

- **Three steps of twelve.** The vault is written in 5, read in 8, read and rejected in 11.
- **Protected and survives.** In 6 it is what the policy guards; in 7 it outlives the deletion.
- **One machine.** Encrypted SGit objects in a folder, keys in another; no server, push or clone is shown.
- **In the adapter, not in Ruflo.** One SGit vault per checkpoint, at a pinned commit.
- **Ruflo's evaluator, in the adapter.** The ABP is compiled to Ruflo rules and checked in enforce mode.
- **Not used.** Ruflo's hive-mind, its running policy state and vector search.
- **That is the right shape.** A recovery copy should be touched when you save and when you restore.
- **What is missing.** The vault leaving the machine, so a lost machine is also recoverable.

## Six short answers {#answers}

The [walkthrough](/articles/what-if-an-agent-loses-its-workspace.html) tells the run in order. Here are the same twelve steps read for one thing: the vault.

- **When is it used?** Written in step 5, read in step 8, read and rejected in step 11. Protected in step 6, survives step 7. Untouched otherwise.
- **What is it used for?** A recovery copy of Ruflo's memory database, sealed with fingerprints of the data, the ABP and the compiled policy.
- **Where is it stored?** A checkpoint folder on the same machine, as encrypted SGit objects, with the keys in a separate private folder.
- **Where is it implemented?** Inside the adapter, a local MCP server at version 0.2, which calls the SGit library at a pinned commit. Each checkpoint gets its own SGit vault, and only its encrypted bare store leaves the adapter's private staging. Ruflo knows nothing about the vault.
- **Where does the ABP come in?** On the adapter's tools, in steps 4, 5, 6, 8 and 11. The rows are compiled into Ruflo rules when the server starts, and each call is checked by a pinned copy of Ruflo's own policy evaluator, in enforce mode. Ruflo's own command line, in steps 3, 9 and 10, does not pass through it; [the third piece](/articles/the-policy-guards-the-door.html) is about that.
- **Which parts of Ruflo ran?** Its memory store and retrieve commands, its SQLite memory file, its bundled embedding model, which stored no vectors, its worker daemon, which was not running, and a pinned copy of its policy evaluator, inside the adapter. Not its hive-mind, not its running policy state, not vector search.

Throughout, I keep apart what is shown on screen and what is inferred from it, as the analysis does, and where Mondweep's published code, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), settles an inference, I say so. In the diagrams, solid arrows are on screen or confirmed by the code, and dashed ones are inferred.

## The component map {#map}

!shot rf-map.webp | images/ | The component map: the test script, Ruflo's command line, the ABP adapter, the SGit library and the vault on disk. | architecture

Two lines run from the test script. One goes to Ruflo's command line, which writes and reads its memory file directly. The other goes to the adapter's tools, `checkpoint`, `inspect`, `restore` and `close_run`, of which the run uses three. Each passes a policy gate, a pinned copy of Ruflo's evaluator running the compiled ABP rules in enforce mode, which fails closed, and through it reaches the SGit library, which writes the vault and keeps the keys apart. Everything happens on one machine's disk.

## Step 5: the vault is written {#step-5}

!shot rf-stage-05.webp | images/ | Step 5: the checkpoint tool passes the policy gate and the SGit library writes ciphertext to the checkpoint store. | small | architecture

This is where the vault is created. The checkpoint request for the `project` namespace is allowed. The adapter takes a consistent copy of Ruflo's memory file with a SQLite backup, fingerprints it, and SGit stores it encrypted, with the id `2fa35d1b71ce4361b458c8a64f6ec668`.

**Shown on screen:** status checkpointed, backend sqlite-backup, three SHA-256 values for the database, the ABP and the policy, and "Only encrypted SGit bare objects enter the checkpoint store. Private keys remain in a separate private directory."

**Confirmed in the code:** the order is a policy check, a consistent SQLite backup, an integrity check, a new SGit vault for this checkpoint and a commit, and then only the encrypted bare store is copied out of private staging. No remote push is performed. The encrypted manifest records the source ABP's hash, the compiled rules' hash, the profile, the owner, the principal, the database digest and the time. The README is precise about what those are: "These hashes bind evidence to a mandate; they are not digital signatures or immutable audit receipts."

What goes into the vault is one consistent copy of the memory database, sealed with fingerprints of the data and of the rules in force. That last part is the one I would point every architect at: the checkpoint records which policy was in force when it was taken, so a restore can be tied to the rules that governed the data.

## Step 8: the vault is read {#step-8}

!shot rf-stage-08.webp | images/ | Step 8: a new MCP server process restores the checkpoint, and memory.sqlite is written into the fresh-runner workspace. | narrow | architecture

A brand-new adapter process restores the checkpoint into a new workspace, `fresh-runner`. The restored database is byte for byte the one saved in step 5.

**Shown on screen:** status restored, new_workspace fresh-runner, a database SHA-256 identical to step 5, and matches_checkpoint true.

**Confirmed in the code:** the restore checks the stored ciphertext's digest, decrypts with the key record kept in the private folder, checks the manifest and the database digest, checks that the SQLite file is sound, and only then promotes it into a new workspace, as `memory.sqlite`. It never overwrites an existing workspace.

## Step 11: the vault is read, and refuses {#step-11}

!shot rf-stage-11.webp | images/ | Step 11: one object in the vault is altered, the adapter finds a digest mismatch and no workspace is created. | narrow | architecture

One encrypted object in the vault is altered, and a restore is tried. The ABP allows the restore; the adapter's check of the stored ciphertext is what refuses it.

**Shown on screen:** an error, ValueError, and tampered_workspace_created false.

**Confirmed in the code:** before anything is decrypted, the adapter compares the digest of the stored ciphertext with the one it recorded when it saved the checkpoint, and refuses with "Checkpoint ciphertext integrity mismatch". SGit is never asked to decrypt the altered copy.

## Steps 6 and 7: protected, then left standing {#step-6}

In step 6, closing the run would delete memory. That ABP row needs approval, none is given, and the run stops with the checkpoint retained. Here the vault is what the policy is protecting; it is not touched. In step 7 the original project is deleted, with Ruflo's memory file, and the vault and its keys survive because they live in folders outside the project. Step 8 confirms they were still there.

## Where the vault lives {#where}

!shot rf-where.webp | images/ | Where the video's vault lives: on one machine, with the adapter, the SGit library, the checkpoint store and the keys. | architecture

Encryption happens on the machine, and the ciphertext stays there. The README says so plainly: no remote push is performed, and remote sync is on its list of follow-ups. So it survives the project being deleted, which is what the video tests. It would not survive the machine being lost, which the video does not claim.

That is the step I most want to see next, and it is the one SGit was built for. The same objects can be pushed to a vault server that only ever holds ciphertext, and cloned on another machine with the key. A second run that restores on a different machine, and shows the server holding nothing readable, would close the loop. This site already runs on that pattern: [one vault, ten agents](/articles/one-vault-ten-agents.html) measures what cloning a shared vault from the hosted service costs.

## Is three steps of twelve a weakness? {#three}

No. A recovery copy should be touched when you save and when you restore, and otherwise left alone. If the vault were written in every step, it would be Ruflo's working memory, not its backup, and the test would be about something else.

The more interesting finding is where the vault is implemented. Ruflo knows nothing about it. The adapter wraps Ruflo's memory file from outside, through MCP, and the SGit library does the encryption, one vault per checkpoint, so checkpoints share no history. That means the same adapter pattern could wrap any agent tool that keeps its memory in a file, without changing the tool. It also means the vault is only as complete as the adapter's reach, which is the subject of the next piece.

## Where to go next {#next}

[The policy guards the door; the command line uses the window](/articles/the-policy-guards-the-door.html) looks at the paths the adapter does not see: steps 3, 9 and 10, where Ruflo's own command line writes and reads the same memory file without passing the ABP. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), where every step opens its own diagram, and back to [the walkthrough](/articles/what-if-an-agent-loses-its-workspace.html).

## What this does not claim {#limits}

- **From the screen and the code.** Where a diagram goes beyond both, the arrow is dashed and the text says inferred.
- **Not a review of SGit's cryptography.** The tampered object is caught by the adapter's digest check, before decryption.
- **Not a criticism of the run.** One machine is what a proof of concept on a laptop looks like.
- **Ruflo's unused parts are not judged.** They were outside this test's scope.

## Where this comes from {#sources}

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation and published here with his agreement. The code: Mondweep Chakravorty, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, read at its commit of 16 October 2026, including `core.py`, `abp.py`, `policy/bridge.mjs` and the README. The architecture: an addendum to the analysis made for me by Claude (Anthropic) on 17 October 2026 from on-screen content, with one diagram per stage, rendered here from its sources and corrected where the code shows otherwise; written up and checked against the video's timeline and the code by this site's agent; the editorial responsibility is mine. Ruflo: [ruvnet/ruflo](https://github.com/ruvnet/ruflo), MIT. Related: [One vault, ten agents](/articles/one-vault-ten-agents.html), [SGit is a standard](/articles/sgit-is-a-standard.html).
