---
title: sgit in GitHub Actions, side by side: a showcase repository and site that runs four ways of moving a vault between jobs on every run, measured, with a budget for its LLM steps
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: sgit in a CI pipeline described how an encrypted vault can carry data in and out of GitHub Actions, and between its jobs. The next step is to show it running, and to keep showing it. So this is a brief for a dedicated repository and website, just for that: its own issues, its own CI pipeline, and on every run four ways of moving a vault between jobs, side by side, in parallel. A vault server with the keys in the repository's secrets; the encrypted vault itself as an artefact, a zip that one job uploads and the next downloads; the vault published as files and cloned read-only from any web host; and append lanes for jobs that only need to hand results in. Each lane reports its time, its bytes, the keys each job held and a screenshot, and repeats on vaults of growing size with full, thin and path clones. I measured the core of it locally for this article. A clone of one folder barely grows with the vault: 0.59 seconds at 100 files, 0.77 at 2,000. A full clone grows with it, from 0.95 to 5.55 seconds. The repository should also have a budget, because some steps will call models, from more than one provider, and every token they spend should be counted against it.
version: v0.12.50
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, github-actions, ci, vaults, artefacts, append-lanes, performance, llm, token-budget, brief, article
status: published
---

!shot as-lanes.webp | images/ | Four ways to move a vault between jobs, run side by side: a vault server with keys in secrets, the vault as an artefact, the vault published as files, and append lanes for shards. On every run of the showcase repository, each lane reports its time, its bytes, the keys each job held, a screenshot of the result, and the tokens spent by any LLM step against the run's budget. | architecture

## In short {#in-short}

- **A showcase of its own.** A dedicated repository and website for sgit in GitHub Actions, with its own issues and its own CI pipeline.
- **Four lanes, side by side.** A server; the vault as an artefact; the vault as published files; append lanes for shards.
- **In parallel, on every run.** Time, bytes, keys and a screenshot per lane, as the vaults get bigger.
- **Measured locally first.** A one-folder clone: 0.59 s at 100 files, 0.77 s at 2,000. A full clone: 0.95 s to 5.55 s.
- **Artefacts and lanes fit together.** Artefacts are immutable and one per job; a lane collects from many jobs.
- **A budget for the models.** Every LLM step counted against the run's budget, across providers.

## Why a site of its own {#why}

[sgit in a CI pipeline](/articles/sgit-in-a-ci-pipeline.html) tested the pieces locally: data in and out, scoped clones between jobs, keys as the boundaries, append lanes for test shards, a key pair per job. Its workflow file was a sketch; it said so. The next step is to run it on GitHub Actions for real, and to keep running it, where anyone can see.

That needs its own repository and its own website, not a corner of another project. The repository holds the workflows and the issues; its CI pipeline exists to show itself working; and the site publishes what each run found. It is also a good place to show sgit in more than one shape at once, because the same job can be done several ways, and the differences are the point.

## Four lanes {#lanes}

On every run, the same small build output travels from a build job to a test job and a release job, four ways, in parallel:

1. **A vault server.** The keys are in the repository's secrets, each job clones only the folders it needs with `--path`, and pushes back. This is the setup the CI article tested.
2. **The vault as an artefact.** No server: the encrypted vault is zipped and uploaded with GitHub's artefact action, and the next job downloads it and opens it with the key. GitHub's own documentation says artefacts "persist data after a job has completed, and share that data with another job in the same workflow". Two properties of the current version shape this lane: "Artifacts created by upload-artifact@v4 are immutable", and they "are retained for 90 days by default". Because the zip holds only ciphertext, it can be published as a file and downloaded anywhere without the key leaving the secrets.
3. **Published as files.** The vault's encrypted objects put on any web host, and cloned read-only with sgit's `static` transport, which reaches "any GET host, read-only". No server and no write path.
4. **Append lanes for shards.** Each shard posts its encrypted result with its own token, and the summary job drains the inbox. This fills a gap in artefacts: the current version of the upload action does not support several jobs uploading to the same artefact. A lane takes them all.

## What each run reports {#report}

Each lane reports the same things: the wall time per job and for the run; the bytes each job downloaded and the bytes on its disk; which keys each job held, and therefore what it could have read; and a screenshot of the result. The screenshot comes from a vault app, a page that draws the vault's contents; it is taken in the job and stored back in the vault, so the run's evidence travels with its data.

Then it repeats on vaults of growing size, with a full clone, a thin clone of the latest state, and a clone of one folder. The outputs differ on purpose: a job that cloned one folder should hold one folder.

## Measured locally {#measured}

!shot as-clones.webp | images/ | Clone time as a vault grows, measured locally: median of three runs, sgit 0.21.0 against a local vault server over HTTP, on four cores. A clone of one folder, 5% of the files, barely grows with the vault; a full clone grows with it. Git, reading local disk without encryption, is shown for scale, not as a like-for-like race. | comparison

I measured the core of it for this article on one machine, sgit 0.21.0 against a local vault server over HTTP, with files of random bytes spread over 20 folders, three runs each.

- **A clone of one folder barely grows.** 0.59 seconds for a 100-file vault, 0.64 at 500, 0.77 at 2,000. It downloads only that folder: 4.1 MB on disk out of 82.7 MB for the full clone of the largest.
- **A full clone grows with the vault.** 0.95, 1.98 and 5.55 seconds for the same three vaults.
- **Large files are different.** For 40 files of 3 MB each, a full sgit clone took 4.4 seconds; a full git clone of the same files from local disk took 16.1, most likely because git tries to compress data that cannot be compressed. Git's own partial clone with a sparse checkout was the fastest of all, at 0.4 seconds, reading local disk with no encryption; it is shown for scale, not as a race.

And three things went wrong, which is exactly what this repository is for. A push of a file over 4 MB failed against a server using local disk storage, because sgit sends large files through cloud storage uploads. A thin "headless" clone could not then fetch a single file in this version. And ten full clones at once took 21.1 seconds on a single server process, while ten one-folder clones took 1.9. A showcase that runs on every release finds those before a user does.

## A budget for the models {#budget}

Some steps in the showcase will call models: summarising a run, reading a screenshot, writing the release note. So the repository should have a budget, and every token spent should be counted against it, per run and per provider. It should also run the same step on more than one provider, side by side, for the same reason it runs four lanes.

There are two places a model call can happen. In the job, with a provider key in the repository's secrets, as [The key is the billing system](/articles/the-key-is-the-billing-system.html) described for a product that runs on the user's own key. Or in the browser, inside a vault app: the vault app runtime lists `sg.llm.{available,models,chat,cancel,usage}`, and its documentation says "the vault's key stays in the HOST; your frame never sees it". The `usage` call is where a budget can be read. Which of the two works best in a CI run is one of the things the showcase should find out.

## The brief {#brief}

*For the session that builds the showcase. Written by @newsroom.writer for Dinis Cruz, 14 October 2026, on top of v0.12.49.*

1. **A repository and a site.** Its own issues, its own CI pipeline, and a website that publishes every run's results. Where it lives is the owner's call.
2. **The four lanes.** Server, artefact, published files, append lanes, as four parallel paths through the same build, test and release jobs.
3. **The report per lane.** Time, bytes, keys held and a screenshot, as one file per run, stored in a vault and drawn by a vault app.
4. **Growing vaults.** The same run on vaults from 100 to several thousand files, with full, thin and one-folder clones; the local numbers above are the baseline.
5. **The failures as issues.** Large files without cloud storage, a headless clone fetching a file, concurrent full clones: each an issue with a reproduction, checked on every release.
6. **The budget.** A token budget per run, counted per provider, with at least two providers for the same step.
7. **Publish it.** A page per run and a running chart, so anyone can see sgit working in GitHub Actions, and where it does not yet.

What to be careful about. Keys only in secrets, never in a workflow file, a log or an artefact's name. Every artefact and published file is ciphertext. Read keys may be published on purpose; write keys never. And the budget is a hard limit, not a report after the fact.

## What this does not claim {#limits}

- **The numbers are local.** One four-core machine, a local server over HTTP, three runs each; GitHub's runners and a real network will differ.
- **Git is not a like-for-like baseline.** It read local disk with no encryption and no HTTP.
- **Lanes 2 and 3 are untested.** The artefact and static lanes are built from the documentation; lanes 1 and 4 were tested locally for the CI article.
- **Nothing in the brief is built.**

If you are moving sensitive data through GitHub Actions and want to try one of the lanes, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The measurements were run for this article by a research agent on one machine, with sgit 0.21.0, version 0.34.0 of the vault server and git 2.43.0. GitHub, [workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) and the [upload-artifact action](https://github.com/actions/upload-artifact); the vault app runtime from sgit.ai's [skills](https://sgit.ai/skills/index.html). All read on 14 October 2026.
