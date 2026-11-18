---
title: A factory that films its work: a review of ESF, Mitko Vasilev's open-source Engineering Software Factory, one task into one microVM, one agent, deterministic gates and a verified patch with its evidence, the demo videos and review queue his post shows, which are not yet in the public repository, and what our own factories should take from it, starting with a recording made by the same run that proves the change
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: Mitko Vasilev posted that his software factory has started making video demos: it takes bugs and features from the backlog, runs them through a Temporal workflow, a coding agent in a disposable sandbox and deterministic verification gates, and he came back from a meeting to a reviewed change, the agent's full trajectory, all the traces and a 14-second clip of the feature working, recorded by the same run that proves it. I like that last idea a lot, so I read his repository, github.com/mitkox/esf. ESF, the Engineering Software Factory, is serious work: MIT-licensed, mostly Go, at version 1.0.0-rc.1, with a clear rule, "one task in, one isolated Cube microVM, one agent, one verified patch out". Each run gets its own microVM, credentials are injected at the network edge and never placed in the sandbox, the gates read exit codes so "the model never declares success", a behaviour monitor can quarantine a run, and every run leaves an evidence folder and OpenTelemetry traces. What the public repository does not have yet is the part of the post that caught my eye: no video recording, no backlog connector, no pull requests and no review queue with approve, reject and defer; the screenshot shows a separate application. That is not a criticism: the core is the hard part, and it is open. Here is what it does, how it compares with our own factories, and what we should take from it: the recording from the run that proves the change, a gate that stops a change rewriting its own gates, and a sandbox per run.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: software-factory, agents, sandboxes, verification, video, open-source, reply, article
status: published
---

!shot esf-post.webp | images/ | Mitko Vasilev's post: a software factory that hands back a reviewed change, traces and a 14-second demo clip. | screenshot | medium

## In short {#in-short}

- **Mitko Vasilev's factory makes video demos** of each change, from the run that proves it.
- **The public core, ESF, is serious:** one task, one microVM, one agent, one verified patch.
- **The gates read exit codes;** "the model never declares success".
- **Credentials stay outside the sandbox;** a monitor can quarantine a run.
- **The video, backlog, pull requests and review queue** are not in the public repository yet.
- **What we should take:** a recording from the proving run, gates that cannot be rewritten, a sandbox per run.

## The post {#post}

Mitko Vasilev, a CTO, wrote that his software factory "just started making video demos". It works on the bugs and features "directly from the backlog", and he "came back to a reviewed PR, full agent trajectory, all traces and a 14-second clip of the thing working". The loop: "Backlog in -> Temporal workflow -> coding agent in a disposable sandbox -> deterministic verification gates -> DoR/DoD + evidence + demo video out". And the line I liked most: "The factory records it from the same run that proves the change." He ends with "Make sure you own your AI."

## What ESF is {#esf}

[ESF](https://github.com/mitkox/esf), the Engineering Software Factory, is an independent fork of Owain Lewis's Machinist, MIT-licensed, written mostly in Go with a React console and some Python tools, and at version 1.0.0-rc.1, released on 5 November after 91 commits in seven weeks. It describes itself honestly as "a production-oriented candidate, not a production qualification". Its design rule is one line: "One task in. One isolated Cube microVM. One agent. One verified patch out."

- **The flow:** a task, a Temporal workflow, a Tencent CubeSandbox microVM, a coding agent, verification, and a patch with its evidence.
- **The agents:** OpenCode by default, with Claude Code and Codex as options, their permission-bypass flags confined to the microVM; local model endpoints are supported, which is the "own your AI" part.
- **The gates:** build and test steps, mandatory by default, judged by exit codes: the agent can report success and the factory can still say "verification failed". A gate-integrity check stops "a tree that rewrites the gates judging it".
- **The evidence:** every run leaves a folder with the task, the baseline, the before and after, the patch, a manifest with digests, the audit log of actions and the agent's redacted prompt and output; and OpenTelemetry traces.
- **The security:** the caller can never name an executable, a host path, an environment variable or a credential; provider credentials are injected at the network boundary and "not placed inside the sandbox"; open egress has to be acknowledged; a threat monitor can quarantine a run; and `factory halt` stops runs by agent, scope or repository. Releases carry GitHub attestations and a software bill of materials.
- **The review:** a person approves or rejects each run's change from the command line, and a rejection note goes back as the rework instruction. "ESF produces changes for review; it does not decide what ships."

## What is not in the repository yet {#gap}

The parts of the post that caught my attention are not in the public code. I found no video or screen recording, no connector that takes work from a backlog, no pull requests, the code says plainly that "nothing in this package pushes, creates a branch on a remote, or opens a pull request", and no review queue with approve, reject and defer or a "what should the lead learn from this?" question; the console in the repository is read-only. The screenshot in the post shows a separate desktop application with that review queue and the video beside each item. The repository's last release is from 5 November; the post is from today. So the video layer is newer, or private, or in another repository.

I say this not as a criticism. The microVM per run, the gates and the evidence are the hard part, and they are open. The repository is also candid about what is not finished: a 24-hour soak test, Kubernetes qualification, and acceptance with real models, since the release candidate was validated with a deterministic test agent rather than a live model.

## How it compares with our factories {#compare}

!shot esf-compare.webp | images/ | ESF and our factories side by side: isolation, gates, evidence, review, policy, video. | comparison

We run two kinds of factory: the AgentiCCells site factory, where a commit becomes a repository, an address and a site ([the site factory works](/articles/the-site-factory-works.html)); and the agent teams that build our sites and apps, whose every release goes through CI checks, a leak scan and a signed commit, as this newsroom does.

- **Isolation:** ESF puts every run in its own microVM. Ours run in cloud sessions, bounded by behaviour policies and, at the strongest, SHarness ([introducing SHarness](/articles/introducing-sharness.html)). A microVM per run is stronger, and simpler to reason about.
- **Gates:** both judge by checks, not by the agent's word. ESF's check that a change cannot rewrite its own gates is one we should copy.
- **Evidence:** both keep a record per run. Ours is spread across commits, run reports and debriefs; ESF's is one folder per run, which is easier to hand to a reviewer.
- **Policy:** ESF declares agents, models, egress and scopes in configuration, operator-wide. We write a behaviour policy per agent ([what can your agent reach?](/articles/what-can-your-agent-reach.html)). The two would fit: an Agent Behaviour Policy could be compiled into ESF's egress and scope settings, and since both are open, either side could build that in.
- **Video:** neither has it in public yet. That is the idea to take.

## The recording that proves the change {#video}

!shot esf-loop.webp | images/ | The loop to copy: the change, the gates, a recording made by the same run, and the reviewer sees all three. | process

Our own sites already take screenshots in their checks: this newsroom checks every article at a phone's width, and our site builds run browser tests. The step from there to Mitko's idea is small: let the run that proves a change also record it, a short clip of the page or the feature working, made by the same browser that ran the test, and put it beside the change for the reviewer. A reviewer then sees three things together: the diff, the gates that passed, and the thing working. And because it comes from the proving run, it is evidence, not a demo made afterwards for show.

I would like this for every website cell: when the owner's Claude changes their site, the change comes back with a 15-second clip of the new page, and the owner approves what they can see ([start with an interview](/articles/start-with-an-interview.html)).

## What I would take {#take}

- **A recording from the proving run,** for every change our agents make to a site.
- **A gate-integrity check:** no change may rewrite the checks that judge it.
- **One evidence folder per run,** easy to hand over.
- **A sandbox per run** where the work allows it.
- **A conversation with Mitko** about compiling behaviour policies into ESF's configuration, both being open source.

## What this does not claim {#limits}

- **I read the repository; I did not run it.**
- **The video and review queue are described from the post and its screenshot,** not from code.
- **ESF's own status is a release candidate,** as it says.

## Where this comes from {#sources}

Mitko Vasilev's post on LinkedIn, 18 November 2026, shown above; the ESF repository, [github.com/mitkox/esf](https://github.com/mitkox/esf), read on 18 November 2026 at v1.0.0-rc.1: README.md, ARCHITECTURE.md, docs/FACTORY.md, the architecture decision records, docs/console.md, docs/review-v1.0.0-rc.1.md, docs/release-v1.0.0-rc.1.md and internal/repository/provider.go. Earlier on this site: [the site factory works](/articles/the-site-factory-works.html), [introducing SHarness](/articles/introducing-sharness.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html), [start with an interview](/articles/start-with-an-interview.html).
