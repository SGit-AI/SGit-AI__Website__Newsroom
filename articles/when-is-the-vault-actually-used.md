# When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy, sgit.ai

> The first piece walked through Mondweep Chakravorty's video step by step. This one asks a sharper question: in a run that is about an encrypted vault, when is the vault actually used? The answer, drawn stage by stage from the frames, is in three steps of twelve. It is written in step 5, when a consistent copy of Ruflo's memory database is saved as encrypted SGit objects with fingerprints of the data, the ABP and the compiled policy. It is read in step 8, when a brand-new process restores it with the same fingerprint. It is read and rejected in step 11, when one object has been altered. In step 6 it is what the policy protects, and in step 7 it survives the deletion because it lives outside the project. It sits on the same machine, with its keys in a separate folder; no vault server, push or clone appears. It is implemented in the adapter, which calls the SGit library at a pinned commit and creates a separate vault for each checkpoint, and Ruflo knows nothing about it. The policy is compiled into Ruflo's own rule format and checked by a pinned copy of Ruflo's evaluator, inside the adapter. Not used: Ruflo's hive-mind, Ruflo's running policy state, and vector search. All of this is confirmed by the author's published code. That is not a weakness; it is what a recovery copy should look like, and it shows the pattern works with any tool's memory file. What it does not yet show is the vault leaving the machine.

*Source: <https://newsroom.sgit.ai/articles/when-is-the-vault-actually-used.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy

# When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.1.0, 2 versions](versions/when-is-the-vault-actually-used.md) · [newsroom v0.12.90](https://newsroom.sgit.ai/admin/versions.html) · agentsruflosgitvaultsarchitectureagent-behaviour-policymcpmemoryvideoarticle

***Abstract:** The first piece walked through Mondweep Chakravorty's video step by step. This one asks a sharper question: in a run that is about an encrypted vault, when is the vault actually used? The answer, drawn stage by stage from the frames, is in three steps of twelve. It is written in step 5, when a consistent copy of Ruflo's memory database is saved as encrypted SGit objects with fingerprints of the data, the ABP and the compiled policy. It is read in step 8, when a brand-new process restores it with the same fingerprint. It is read and rejected in step 11, when one object has been altered. In step 6 it is what the policy protects, and in step 7 it survives the deletion because it lives outside the project. It sits on the same machine, with its keys in a separate folder; no vault server, push or clone appears. It is implemented in the adapter, which calls the SGit library at a pinned commit and creates a separate vault for each checkpoint, and Ruflo knows nothing about it. The policy is compiled into Ruflo's own rule format and checked by a pinned copy of Ruflo's evaluator, inside the adapter. Not used: Ruflo's hive-mind, Ruflo's running policy state, and vector search. All of this is confirmed by the author's published code. That is not a weakness; it is what a recovery copy should look like, and it shows the pattern works with any tool's memory file. What it does not yet show is the vault leaving the machine.*

Who does what, step by step: the vault is written or read in steps 5, 8 and 11, protected in step 6 and survives step 7; Ruflo's own command line touches memory in steps 3, 9 and 10, where the ABP is not on the path. From the architecture addendum to the analysis of Mondweep Chakravorty's video.

SGit × Ruflo: one run, five ways in

Mondweep Chakravorty's video of an agent losing its workspace and getting its memory back: the run, the architecture, the gap, a page to step through it yourself, and the page that took it into Ruflo.

[1 · The runWhat if an agent loses its workspace?Twelve steps: memory saved, project deleted, memory restored in a fresh process, three safeguards tested.](what-if-an-agent-loses-its-workspace.md)[you are here2 · The architectureWhen is the vault actually used?In three of twelve steps, on one machine, inside the adapter: what that proves and what it does not.](when-is-the-vault-actually-used.md)[3 · The gapThe policy guards the door; the command line uses the windowThe ABP checks the adapter's tools; Ruflo's own command line reaches the same memory file without it.](the-policy-guards-the-door.md)

4 · Step through itSGit × Ruflo, step by stepEvery step with its frame, command, output and diagram, linked to its moment in the video.[Watch the video ↗](https://youtu.be/rkh6BJiaIrQ)[Step through it](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html)[Read the code ↗](https://github.com/mondweep/sgit-ruv-memory)

[5 · The mergeOur first PR in RufloMondweep's page on ABP-governed SGit checkpoints, merged into Ruflo's main branch by rUv: the four pieces that got it there.](our-first-pr-in-ruflo.md)

## In short

- **Three steps of twelve.** The vault is written in 5, read in 8, read and rejected in 11.
- **Protected and survives.** In 6 it is what the policy guards; in 7 it outlives the deletion.
- **One machine.** Encrypted SGit objects in a folder, keys in another; no server, push or clone is shown.
- **In the adapter, not in Ruflo.** One SGit vault per checkpoint, at a pinned commit.
- **Ruflo's evaluator, in the adapter.** The ABP is compiled to Ruflo rules and checked in enforce mode.
- **Not used.** Ruflo's hive-mind, its running policy state and vector search.
- **That is the right shape.** A recovery copy should be touched when you save and when you restore.
- **What is missing.** The vault leaving the machine, so a lost machine is also recoverable.

## Six short answers

The [walkthrough](what-if-an-agent-loses-its-workspace.md) tells the run in order. Here are the same twelve steps read for one thing: the vault.

- **When is it used?** Written in step 5, read in step 8, read and rejected in step 11. Protected in step 6, survives step 7. Untouched otherwise.
- **What is it used for?** A recovery copy of Ruflo's memory database, sealed with fingerprints of the data, the ABP and the compiled policy.
- **Where is it stored?** A checkpoint folder on the same machine, as encrypted SGit objects, with the keys in a separate private folder.
- **Where is it implemented?** Inside the adapter, a local MCP server at version 0.2, which calls the SGit library at a pinned commit. Each checkpoint gets its own SGit vault, and only its encrypted bare store leaves the adapter's private staging. Ruflo knows nothing about the vault.
- **Where does the ABP come in?** On the adapter's tools, in steps 4, 5, 6, 8 and 11. The rows are compiled into Ruflo rules when the server starts, and each call is checked by a pinned copy of Ruflo's own policy evaluator, in enforce mode. Ruflo's own command line, in steps 3, 9 and 10, does not pass through it; [the third piece](the-policy-guards-the-door.md) is about that.
- **Which parts of Ruflo ran?** Its memory store and retrieve commands, its SQLite memory file, its bundled embedding model, which stored no vectors, its worker daemon, which was not running, and a pinned copy of its policy evaluator, inside the adapter. Not its hive-mind, not its running policy state, not vector search.

Throughout, I keep apart what is shown on screen and what is inferred from it, as the analysis does, and where Mondweep's published code, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), settles an inference, I say so. In the diagrams, solid arrows are on screen or confirmed by the code, and dashed ones are inferred.

## The component map

The component map: the test script calls Ruflo's command line in steps 3, 9 and 10 and the ABP adapter's tools in steps 4, 5, 6, 8 and 11; the ABP rows are compiled to Ruflo rules and checked by a pinned copy of Ruflo's evaluator in enforce mode, which leads to the SGit library, which writes the vault and its keys on the machine's disk. Ruflo's hive-mind, its running policy state and a remote vault server were not used. Blue is Ruflo, amber the ABP adapter, green SGit and the vault, grey plain files.

Two lines run from the test script. One goes to Ruflo's command line, which writes and reads its memory file directly. The other goes to the adapter's tools, `checkpoint`, `inspect`, `restore` and `close_run`, of which the run uses three. Each passes a policy gate, a pinned copy of Ruflo's evaluator running the compiled ABP rules in enforce mode, which fails closed, and through it reaches the SGit library, which writes the vault and keeps the keys apart. Everything happens on one machine's disk.

## Step 5: the vault is written

Step 5: the checkpoint tool passes the policy gate; a SQLite backup takes a consistent copy of memory.db; fingerprints of the database, the ABP and the policy are taken; the SGit library encrypts on the machine and writes ciphertext only to the checkpoint store, with keys kept apart.

This is where the vault is created. The checkpoint request for the `project` namespace is allowed. The adapter takes a consistent copy of Ruflo's memory file with a SQLite backup, fingerprints it, and SGit stores it encrypted, with the id `2fa35d1b71ce4361b458c8a64f6ec668`.

**Shown on screen:** status checkpointed, backend sqlite-backup, three SHA-256 values for the database, the ABP and the policy, and "Only encrypted SGit bare objects enter the checkpoint store. Private keys remain in a separate private directory."

**Confirmed in the code:** the order is a policy check, a consistent SQLite backup, an integrity check, a new SGit vault for this checkpoint and a commit, and then only the encrypted bare store is copied out of private staging. No remote push is performed. The encrypted manifest records the source ABP's hash, the compiled rules' hash, the profile, the owner, the principal, the database digest and the time. The README is precise about what those are: "These hashes bind evidence to a mandate; they are not digital signatures or immutable audit receipts."

What goes into the vault is one consistent copy of the memory database, sealed with fingerprints of the data and of the rules in force. That last part is the one I would point every architect at: the checkpoint records which policy was in force when it was taken, so a restore can be tied to the rules that governed the data.

## Step 8: the vault is read

Step 8: a new MCP server process restores the checkpoint; the policy gate allows it; the SGit library reads ciphertext from the vault and keys from the private folder, decrypts and verifies, and writes memory.sqlite into the fresh-runner workspace, with the same SHA-256 as in step 5.

A brand-new adapter process restores the checkpoint into a new workspace, `fresh-runner`. The restored database is byte for byte the one saved in step 5.

**Shown on screen:** status restored, new_workspace fresh-runner, a database SHA-256 identical to step 5, and matches_checkpoint true.

**Confirmed in the code:** the restore checks the stored ciphertext's digest, decrypts with the key record kept in the private folder, checks the manifest and the database digest, checks that the SQLite file is sound, and only then promotes it into a new workspace, as `memory.sqlite`. It never overwrites an existing workspace.

## Step 11: the vault is read, and refuses

Step 11: one object in the vault is altered; the restore tool passes the policy gate; the adapter compares the digest of the stored ciphertext with the one recorded in step 5, finds a mismatch, and a ValueError means the tampered workspace is never created; SGit is never asked to decrypt.

One encrypted object in the vault is altered, and a restore is tried. The ABP allows the restore; the adapter's check of the stored ciphertext is what refuses it.

**Shown on screen:** an error, ValueError, and tampered_workspace_created false.

**Confirmed in the code:** before anything is decrypted, the adapter compares the digest of the stored ciphertext with the one it recorded when it saved the checkpoint, and refuses with "Checkpoint ciphertext integrity mismatch". SGit is never asked to decrypt the altered copy.

## Steps 6 and 7: protected, then left standing

In step 6, closing the run would delete memory. That ABP row needs approval, none is given, and the run stops with the checkpoint retained. Here the vault is what the policy is protecting; it is not touched. In step 7 the original project is deleted, with Ruflo's memory file, and the vault and its keys survive because they live in folders outside the project. Step 8 confirms they were still there.

## Where the vault lives

Where the video's vault lives: on one machine, the adapter and SGit library, the checkpoint store, the private key folder and the workspaces; a vault server was not used.

Encryption happens on the machine, and the ciphertext stays there. The README says so plainly: no remote push is performed, and remote sync is on its list of follow-ups. So it survives the project being deleted, which is what the video tests. It would not survive the machine being lost, which the video does not claim.

That is the step I most want to see next, and it is the one SGit was built for. The same objects can be pushed to a vault server that only ever holds ciphertext, and cloned on another machine with the key. A second run that restores on a different machine, and shows the server holding nothing readable, would close the loop. This site already runs on that pattern: [one vault, ten agents](one-vault-ten-agents.md) measures what cloning a shared vault from the hosted service costs.

## Is three steps of twelve a weakness?

No. A recovery copy should be touched when you save and when you restore, and otherwise left alone. If the vault were written in every step, it would be Ruflo's working memory, not its backup, and the test would be about something else.

The more interesting finding is where the vault is implemented. Ruflo knows nothing about it. The adapter wraps Ruflo's memory file from outside, through MCP, and the SGit library does the encryption, one vault per checkpoint, so checkpoints share no history. That means the same adapter pattern could wrap any agent tool that keeps its memory in a file, without changing the tool. It also means the vault is only as complete as the adapter's reach, which is the subject of the next piece.

## Where to go next

[The policy guards the door; the command line uses the window](the-policy-guards-the-door.md) looks at the paths the adapter does not see: steps 3, 9 and 10, where Ruflo's own command line writes and reads the same memory file without passing the ABP. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html), where every step opens its own diagram, and back to [the walkthrough](what-if-an-agent-loses-its-workspace.md).

## What this does not claim

- **From the screen and the code.** Where a diagram goes beyond both, the arrow is dashed and the text says inferred.
- **Not a review of SGit's cryptography.** The tampered object is caught by the adapter's digest check, before decryption.
- **Not a criticism of the run.** One machine is what a proof of concept on a laptop looks like.
- **Ruflo's unused parts are not judged.** They were outside this test's scope.

## Where this comes from

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation and published here with his agreement. The code: Mondweep Chakravorty, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, read at its commit of 16 October 2026, including `core.py`, `abp.py`, `policy/bridge.mjs` and the README. The architecture: an addendum to the analysis made for me by Claude (Anthropic) on 17 October 2026 from on-screen content, with one diagram per stage, rendered here from its sources and corrected where the code shows otherwise; written up and checked against the video's timeline and the code by this site's agent; the editorial responsibility is mine. Ruflo: [ruvnet/ruflo](https://github.com/ruvnet/ruflo), MIT. Related: [One vault, ten agents](one-vault-ten-agents.md), [SGit is a standard](sgit-is-a-standard.md).

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#when-is-the-vault-actually-used)

### Builds on

- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.
- [One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom](one-vault-ten-agents.md) The vault behind this newsroom, 35,000 objects and ten agents, measured eight ways: one folder in 13 seconds, history as the edge, storage as the bottleneck.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.

### Continued by

- [Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there](our-first-pr-in-ruflo.md) rUv merged Mondweep's pull request #4239: one docs page, the first commit on Ruflo's main branch to mention SGit or an ABP. The four pieces, shown.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 165 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=165)

**Posting this article on LinkedIn?** The cover is [when-is-the-vault-actually-used.jpg](banners/when-is-the-vault-actually-used.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/when-is-the-vault-actually-used.html)*
