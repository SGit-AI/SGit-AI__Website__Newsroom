---
title: When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: The first piece walked through Mondweep Chakravorty's video step by step. This one asks a sharper question: in a run that is about an encrypted vault, when is the vault actually used? The answer, drawn stage by stage from the frames, is in three steps of twelve. It is written in step 5, when a consistent copy of Ruflo's memory database is saved as encrypted SGit objects with fingerprints of the data, the ABP and the compiled policy. It is read in step 8, when a brand-new process restores it with the same fingerprint. It is read and rejected in step 11, when one object has been altered. In step 6 it is what the policy protects, and in step 7 it survives the deletion because it lives outside the project. It sits on the same machine, with its keys in a separate folder; no vault server, push or clone appears. It is implemented in the adapter, which calls the SGit library at a pinned commit, and Ruflo knows nothing about it. Not used: Ruflo's hive-mind, its own policy engine, and vector search. That is not a weakness; it is what a recovery copy should look like, and it shows the pattern works with any tool's memory file. What it does not yet show is the vault leaving the machine.
version: v0.12.89
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, ruflo, sgit, vaults, architecture, agent-behaviour-policy, mcp, memory, video, article
status: published
---

!shot rf-matrix.webp | images/ | Who does what, step by step: the vault is written or read in steps 5, 8 and 11, protected in step 6 and survives step 7; Ruflo's own command line touches memory in steps 3, 9 and 10, where the ABP is not on the path. From the architecture addendum to the analysis of Mondweep Chakravorty's video. | comparison

!trail sgit-ruflo

## In short {#in-short}

- **Three steps of twelve.** The vault is written in 5, read in 8, read and rejected in 11.
- **Protected and survives.** In 6 it is what the policy guards; in 7 it outlives the deletion.
- **One machine.** Encrypted SGit objects in a folder, keys in another; no server, push or clone is shown.
- **In the adapter, not in Ruflo.** The adapter calls the SGit library at a pinned commit.
- **Not used.** Ruflo's hive-mind, its own policy engine and vector search.
- **That is the right shape.** A recovery copy should be touched when you save and when you restore.
- **What is missing.** The vault leaving the machine, so a lost machine is also recoverable.

## Six short answers {#answers}

The [walkthrough](/articles/what-if-an-agent-loses-its-workspace.html) tells the run in order. Here are the same twelve steps read for one thing: the vault.

- **When is it used?** Written in step 5, read in step 8, read and rejected in step 11. Protected in step 6, survives step 7. Untouched otherwise.
- **What is it used for?** A recovery copy of Ruflo's memory database, sealed with fingerprints of the data, the ABP and the compiled policy.
- **Where is it stored?** A checkpoint folder on the same machine, as encrypted SGit objects, with the keys in a separate private folder.
- **Where is it implemented?** Inside the adapter, a local MCP server at version 0.2, which calls the SGit library at a pinned commit. Ruflo knows nothing about the vault.
- **Where does the ABP come in?** Only on the adapter's tools, in steps 4, 5, 6, 8 and 11. Ruflo's own command line, in steps 3, 9 and 10, does not pass through it; [the third piece](/articles/the-policy-guards-the-door.html) is about that.
- **Which parts of Ruflo ran?** Its memory store and retrieve commands, its SQLite memory file, its bundled embedding model, which stored no vectors, and its worker daemon, which was not running. Not its hive-mind, not its policy engine, not vector search.

Throughout, I keep two things apart, as the analysis does: what is shown on screen, and what is inferred from it. In the diagrams, solid arrows are on screen and dashed ones are inferred.

## The component map {#map}

!shot rf-map.webp | images/ | The component map: the test script calls Ruflo's command line in steps 3, 9 and 10 and the ABP adapter's tools in steps 4, 5, 6, 8 and 11; the adapter's policy gate leads to the SGit library, which writes the vault and its keys on the machine's disk. Ruflo's hive-mind, its policy engine and a remote vault server were not used. Blue is Ruflo, amber the ABP adapter, green SGit and the vault, grey plain files. | architecture

Two lines run from the test script. One goes to Ruflo's command line, which writes and reads its memory file directly. The other goes to the adapter's three tools, `checkpoint`, `close_run` and `restore`, each guarded by a policy gate that fails closed, and through it to the SGit library, which writes the vault and keeps the keys apart. Everything happens on one machine's disk.

## Step 5: the vault is written {#step-5}

!shot rf-stage-05.webp | images/ | Step 5: the checkpoint tool passes the policy gate; a SQLite backup takes a consistent copy of memory.db; fingerprints of the database, the ABP and the policy are taken; the SGit library encrypts on the machine and writes ciphertext only to the checkpoint store, with keys kept apart. | architecture

This is where the vault is created. The checkpoint request for the `project` namespace is allowed. The adapter takes a consistent copy of Ruflo's memory file with a SQLite backup, fingerprints it, and SGit stores it encrypted, with the id `2fa35d1b71ce4361b458c8a64f6ec668`.

**Shown on screen:** status checkpointed, backend sqlite-backup, three SHA-256 values for the database, the ABP and the policy, and "Only encrypted SGit bare objects enter the checkpoint store. Private keys remain in a separate private directory."

**Inferred:** the exact order of backup, hashing and encryption, and that the store has sgit's usual bare layout. No push to a server appears.

What goes into the vault is one consistent copy of the memory database, sealed with fingerprints of the data and of the rules in force. That last part is the one I would point every architect at: the checkpoint records which policy was in force when it was taken, so a restore can be tied to the rules that governed the data.

## Step 8: the vault is read {#step-8}

!shot rf-stage-08.webp | images/ | Step 8: a new MCP server process restores the checkpoint; the policy gate allows it; the SGit library reads ciphertext from the vault and keys from the private folder, decrypts and verifies, and writes memory.sqlite into the fresh-runner workspace, with the same SHA-256 as in step 5. | architecture

A brand-new adapter process restores the checkpoint into a new workspace, `fresh-runner`. The restored database is byte for byte the one saved in step 5.

**Shown on screen:** status restored, new_workspace fresh-runner, a database SHA-256 identical to step 5, and matches_checkpoint true.

**Inferred:** that the keys come from the private folder, and that SGit decrypts and then verifies.

## Step 11: the vault is read, and refuses {#step-11}

!shot rf-stage-11.webp | images/ | Step 11: one object in the vault is altered; the restore tool passes the policy gate; the SGit library reads the altered ciphertext, the integrity check fails, and a ValueError means the tampered workspace is never created. | architecture

One encrypted object in the vault is altered, and a restore is tried. The ABP allows the restore; the vault's own integrity check is what refuses it.

**Shown on screen:** an error, ValueError, and tampered_workspace_created false.

**Inferred:** that SGit's check, authenticated encryption or object hashes, caught it, rather than the adapter comparing fingerprints. Both would produce this output.

## Steps 6 and 7: protected, then left standing {#step-6}

In step 6, closing the run would delete memory. That ABP row needs approval, none is given, and the run stops with the checkpoint retained. Here the vault is what the policy is protecting; it is not touched. In step 7 the original project is deleted, with Ruflo's memory file, and the vault and its keys survive because they live in folders outside the project. Step 8 confirms they were still there.

## Where the vault lives {#where}

!shot rf-where.webp | images/ | Where the video's vault lives: on one machine, the adapter and SGit library, the checkpoint store, the private key folder and the workspaces; a vault server was not used. | architecture

Encryption happens on the machine, and the ciphertext stays there. So it survives the project being deleted, which is what the video tests. It would not survive the machine being lost, which the video does not claim.

That is the step I most want to see next, and it is the one SGit was built for. The same objects can be pushed to a vault server that only ever holds ciphertext, and cloned on another machine with the key. A second run that restores on a different machine, and shows the server holding nothing readable, would close the loop. This site already runs on that pattern: [one vault, ten agents](/articles/one-vault-ten-agents.html) measures what cloning a shared vault from the hosted service costs.

## Is three steps of twelve a weakness? {#three}

No. A recovery copy should be touched when you save and when you restore, and otherwise left alone. If the vault were written in every step, it would be Ruflo's working memory, not its backup, and the test would be about something else.

The more interesting finding is where the vault is implemented. Ruflo knows nothing about it. The adapter wraps Ruflo's memory file from outside, through MCP, and the SGit library does the encryption. That means the same adapter pattern could wrap any agent tool that keeps its memory in a file, without changing the tool. It also means the vault is only as complete as the adapter's reach, which is the subject of the next piece.

## Where to go next {#next}

[The policy guards the door; the command line uses the window](/articles/the-policy-guards-the-door.html) looks at the paths the adapter does not see: steps 3, 9 and 10, where Ruflo's own command line writes and reads the same memory file without passing the ABP. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), where every step opens its own diagram, and back to [the walkthrough](/articles/what-if-an-agent-loses-its-workspace.html).

## What this does not claim {#limits}

- **From the screen only.** Where a diagram goes beyond the frames, the arrow is dashed and the text says inferred.
- **Not a review of SGit's cryptography.** The video shows a tampered object rejected; it does not show how.
- **Not a criticism of the run.** One machine is what a proof of concept on a laptop looks like.
- **Ruflo's unused parts are not judged.** They were outside this test's scope.

## Where this comes from {#sources}

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation and published here with his agreement. The architecture: an addendum to the analysis made for me by Claude (Anthropic) on 17 October 2026 from on-screen content only, with one diagram per stage, rendered here from its sources; written up and checked against the video's timeline by this site's agent; the editorial responsibility is mine. Ruflo: [ruvnet/ruflo](https://github.com/ruvnet/ruflo), MIT. Related: [One vault, ten agents](/articles/one-vault-ten-agents.html), [SGit is a standard](/articles/sgit-is-a-standard.html).
