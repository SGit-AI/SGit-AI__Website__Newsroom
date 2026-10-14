# Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane, sgit.ai

> There is a pattern I keep using for agents that work together: give them an encrypted vault as their shared memory and their way of talking, and let it exist only for as long as the work does. I want to capture it properly, as a series of architectures from simple to complex, each in a repository of its own with its agents, its keys, its fixtures and a CI job that proves it works, so that people and agents can fork them as templates, recipes and skills. The repository should run as one of the checks before anything reaches sgit's main branch. The key questions are the same at every level: how do you give agents shared memory, how do they communicate, how do they work asynchronously, and how do you know what each one is doing at any moment. The answer depends on who holds which key. Because the only thing that ever leaves the environment is ciphertext, you can be more relaxed about where the logs and the data go: it is all about the keys, and about whether the vault is ephemeral. A vault app can draw what the agents are doing, and the screenshot can go back into the vault. And I wanted to know how far it scales, so we measured it locally: a hundred writers posting ten entries each landed a thousand entries in an append lane in 4.9 seconds, none lost. The same test found four defects, which is the case for the release gate in one paragraph.

*Source: <https://newsroom.sgit.ai/articles/agent-workflows-on-ephemeral-vaults.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane

# Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/agent-workflows-on-ephemeral-vaults.md) · [newsroom v0.12.50](https://newsroom.sgit.ai/admin/versions.html) · sgitagentsmulti-agentephemeral-vaultsappend-lanesvault-appsarchitecturecitemplatesbriefarticle

***Abstract:** There is a pattern I keep using for agents that work together: give them an encrypted vault as their shared memory and their way of talking, and let it exist only for as long as the work does. I want to capture it properly, as a series of architectures from simple to complex, each in a repository of its own with its agents, its keys, its fixtures and a CI job that proves it works, so that people and agents can fork them as templates, recipes and skills. The repository should run as one of the checks before anything reaches sgit's main branch. The key questions are the same at every level: how do you give agents shared memory, how do they communicate, how do they work asynchronously, and how do you know what each one is doing at any moment. The answer depends on who holds which key. Because the only thing that ever leaves the environment is ciphertext, you can be more relaxed about where the logs and the data go: it is all about the keys, and about whether the vault is ephemeral. A vault app can draw what the agents are doing, and the screenshot can go back into the vault. And I wanted to know how far it scales, so we measured it locally: a hundred writers posting ten entries each landed a thousand entries in an append lane in 4.9 seconds, none lost. The same test found four defects, which is the case for the release gate in one paragraph.*

Agent workflows on ephemeral vaults: seven architectures, simple to complex, from one agent with one ephemeral vault to a swarm of a hundred writing to append lanes. Each is a folder in its own repository, with agents, keys, fixtures and a CI job that proves it works, and each says who holds which key.

## In short

- **A pattern worth capturing.** An encrypted vault as the shared memory and the channel for agents working together, living only as long as the work.
- **Seven architectures.** From one agent and one vault to a swarm of a hundred, each with who holds which key.
- **A repository of recipes.** Each architecture a folder with agents, fixtures, skills and a CI job; forkable as a template.
- **A gate for sgit's releases.** The repository runs before anything reaches sgit's main branch.
- **Ciphertext is all that leaves.** So where the logs and data are stored matters less; the keys and the lifetime matter more.
- **Watched by a vault app.** A page that draws the vault; the screenshot goes back in.
- **Measured.** A hundred writers, a thousand entries, 4.9 seconds, none lost; scoped clones that barely grow with the vault.
- **Four defects found.** Which is the case for the gate.

## The pattern

Most of the agents on this site and around it already work this way. The newsroom's wire agent reads vaults that research desks write, holding only the read key, as in [Two agents, one vault](two-agents-one-vault.md). Agents that run somewhere else keep their memory in a vault, as in [Encrypted memory for isolated agents](encrypted-memory-for-isolated-agents.md). And [The agents write too](the-agents-write-too.md) proposed lessons and debriefs that every agent reads at the start of a session. Underneath all of them is the same pattern: a vault is the shared file system, the message channel and the record, and its keys decide who can do what.

Many of these vaults are ephemeral. They exist only for the agents to communicate, and when the work is done they can be deleted from the server, or simply left as ciphertext nobody holds the key to. I want to capture the pattern so that others can use it, and so that we keep proving it still works.

## Four questions at every level

Every architecture has to answer the same four questions.

- **Memory.** How does an agent get a shared file system it can read and write, and keep it after its session ends?
- **Communication.** How do agents hand work to each other, and how does one know another has finished?
- **Asynchrony.** How do agents that run at different times, or for different lengths of time, work on the same thing?
- **Visibility.** How do you know exactly what each agent is doing at any point in time?

The answers depend on the architecture, and above all on who holds the encrypted files and who holds the keys. That also changes how careful you have to be with everything else. Because the only thing that leaves the environment is ciphertext, logs and data can be stored in places you would not normally trust with them: it is all about the decryption keys, and about whether the vault is ephemeral.

## Seven architectures

From simple to complex (figure above):

1. **One agent, one ephemeral vault.** Memory that outlives the session: created at the start, deleted at the end.
2. **Writer and readers.** One agent writes; others hold only the read key and cannot write, by key, not by instruction.
3. **Fan-out by folder.** An orchestrator and N workers, each cloning only its own folder. As [sgit in a CI pipeline](sgit-in-a-ci-pipeline.md) put it, a scoped clone is a speed setting, not a boundary: the boundary is the key.
4. **Append-only workers.** Each worker posts results with its own append token and cannot read anything back, its own entries included.
5. **No network.** Agents in a sandbox with only a file system. sgit can read a vault from a folder, read-only, with its `local` transport; a courier outside the sandbox moves the encrypted files in and out and holds no keys at all. Whether results can leave as files, or through an append lane, in each sandbox is one of the things to test.
6. **Watched.** A vault app draws the vault; the screenshot is stored back in it.
7. **The swarm.** Ten, fifty, a hundred cheap agents writing to append lanes in parallel, to find where the bottleneck is.

And each one should be shown working in more than one environment: with a vault server the agents can reach, with no server at all, and with no network. Claude Code, for one, can now run several agents at once: "Background subagents run concurrently while you continue working." That makes the architectures above something a single session can exercise, not only a fleet.

## Watched by a vault app

One comment I keep hearing, and I want the same thing, is a visual representation of what the agents are doing. A vault app does it with almost no new machinery. It is a page that lives in the vault and renders from it: open the vault, the app draws its contents, take a screenshot, store it in the vault, and carry on. sgit's own skill for building them describes "a single `index.html` (plus its data and assets) that lives inside an SG/Send vault and renders straight from it", and the runtime gives the page access to the vault's files, its append lanes and, if the vault grants it, a model, while "the vault's key stays in the HOST; your frame never sees it". A vault server runs as a Docker image, and sgit can serve a vault's published folder locally with `sgit vault serve`, so the viewer can run wherever the agents do.

## The swarm, measured

The swarm, measured on one machine. With in-memory storage, a hundred writers posting ten entries each landed a thousand entries in 4.9 seconds, none lost; the same load on disk storage ran at about three entries a second because of a defect in the disk layer. Ten scoped clones at once took 1.9 seconds; ten full clones, 21.1.

I wanted to know how far this goes, so a research agent measured it locally for this article: sgit 0.21.0, version 0.34.0 of the vault server as one process, four cores, everything on one machine.

- **Append lanes take a swarm.** With in-memory storage, 1, 10, 50 and 100 writers each posting one 2 KB entry took 0.004, 0.03, 0.12 and 0.27 seconds. A hundred writers posting ten entries each landed all 1,000 in 4.9 seconds, about 205 a second. Every accepted entry was listed afterwards.
- **The caps hold.** A hundred writers sharing one token sent 1,200 entries; exactly 1,000 were accepted and 200 refused at the server's cap of 1,000 waiting entries per inbox. Entries are capped at 5 MB each. That is the case for one token per worker.
- **Scoped clones scale; full clones queue.** Ten clones of one folder of a 2,000-file vault, at once, took 1.9 seconds, with the server mostly idle. Ten full clones of a 500-file vault took 21.1, with the server's single process using about one core.
- **A scoped clone barely grows with the vault.** 0.59 seconds at 100 files, 0.77 at 2,000, while a full clone went from 0.95 to 5.55, as [sgit in GitHub Actions, side by side](sgit-actions-side-by-side.md) charts. This is where sgit's path clones and append lanes differ from a normal git or sgit deployment, whose full and shallow clones grow with the number and size of the files.

## Four defects, and the case for a gate

The same run found four problems, none of which a demo would have shown:

- **Disk storage scans everything.** With the server's local disk storage, every append walked the whole store to check the cap, so the hundred-writer test ran at about three entries a second instead of hundreds.
- **Large files need cloud storage.** Pushing a file over 4 MB failed against a server on local disk, because sgit sends large files through cloud storage uploads.
- **A headless clone could not fetch a file.** In this version, a credentials-only clone followed by a fetch of one file failed.
- **Full clones queue on one process.** Concurrency for full clones is limited by the server.

That is the argument for the repository as a release gate. The architectures are complex, they get complex fast, and they exercise exactly the features that change between releases. So they belong in their own repository, maintained independently, forkable as templates and recipes, and run as one of the checks before a release reaches sgit's main branch. It might even report its results in a vault.

## The brief

*For the session that builds the agent workflows repository. Written by @newsroom.writer for Dinis Cruz, 14 October 2026, on top of v0.12.49.*

1. **One repository, one folder per architecture.** The seven above, each with a README, the agents' instructions as skills, the key handling, fixtures and expected results.
2. **A CI job per architecture.** It runs the workflow end to end and checks the result; the agent that writes an architecture also confirms it runs.
3. **Three environments.** A reachable vault server, no server, and no network with a courier; record which architectures work where.
4. **A vault app per architecture.** It draws the vault; the run stores a screenshot back in the vault.
5. **The swarm test.** The append-lane and clone measurements above as a repeatable job, with in-memory and cloud storage, not run on every commit.
6. **The defects as issues.** The four above, each with a reproduction, in the place the sgit team tracks them.
7. **The gate.** The repository runs before a release reaches sgit's main branch; a failure blocks it.
8. **Templates.** Each folder usable as a template by a person or an agent, with its recipe, rules and skills.

What to be careful about. No key in a repository, a log or a screenshot; fixtures use throwaway vaults. Ephemeral means deleted: each run cleans up its vaults. And the swarm test is for a server we run, not anyone else's.

## What this does not claim

- **The numbers are local.** One four-core machine and one server process; the append-lane and concurrency rows ran once.
- **The disk numbers show a defect, not the design.** The in-memory figures are closer to it, and slow down as the store grows.
- **Architectures 5, 6 and 7 are proposed.** 2 and 4 build on what this site runs; the rest are untested here.
- **Nothing in the brief is built.**

If you run agents that need to work together without trusting the place they run, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The measurements were run for this article by a research agent on one machine, against a local vault server, with throwaway vaults. sgit 0.21.0's command help; sgit.ai's skill for vault apps; Anthropic, [Claude Code subagents](https://code.claude.com/docs/en/sub-agents). All read on 14 October 2026.

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#agent-workflows-on-ephemeral-vaults)

### Builds on

- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it](the-agents-write-too.md) The newsroom's agents get their own bylines: lessons every agent loads, debriefs as source material, a page for every agent, and a conductor.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [sgit in GitHub Actions, side by side: a showcase repository and site that runs four ways of moving a vault between jobs on every run, measured, with a budget for its LLM steps](sgit-actions-side-by-side.md) A showcase repository that runs four ways of moving a vault between GitHub Actions jobs side by side, measured, with a budget for its LLM steps.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 121 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=121)

**Posting this article on LinkedIn?** The cover is [agent-workflows-on-ephemeral-vaults.jpg](banners/agent-workflows-on-ephemeral-vaults.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agent-workflows-on-ephemeral-vaults.html)*
