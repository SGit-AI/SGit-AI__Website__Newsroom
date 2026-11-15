---
title: From a commit to a live website: a site factory where a request file in a commit makes a CI pipeline create the GitHub repository, the DNS record and the sgit vault, seed a page, check HTTPS, run a first pass with Claude Code, and record it all, so an agent can create sites by committing
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: Every new site we create needs the same three things: a GitHub repository, a DNS record, and an sgit vault. Today I make them by hand, with a lot of clicks. Scripts or a command-line tool would be faster, but they would still need a person with the keys. My hypothesis is that the right answer is a CI pipeline, a site factory: a control repository where each new site is a request, a folder with a small site file and a brief, added in a commit. On the pull request, the pipeline checks the request and posts a plan; on merge, it creates the repository from a template, turns on Pages, creates the DNS record, creates the vault and publishes its read key, commits a test page, waits for HTTPS, optionally runs a first pass with Claude Code to build the site from the brief, writes the result back into the request's folder and lists the site on the hub. The credentials can be good ones: a GitHub App for GitHub and OpenID Connect federation for AWS, so no long-lived keys sit in the pipeline. Because every site and its content are public, the factory and its record can be public too, with only the credentials kept private. And because it all starts with a commit, the agent I run in a loop only needs access to the control repository to create a site.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: ci, automation, github-actions, aws, dns, sgit, agenticcells, architecture, article
status: published
---

!shot csf-factory.webp | images/ | The site factory: a request in a commit, a plan on the pull request, and on merge a repo, a record, a vault and a site. | architecture

## In short {#in-short}

- **Every site needs three things:** a GitHub repository, a DNS record and an sgit vault.
- **By hand is slow, scripts still need a person;** a CI pipeline does it from a commit.
- **A request is a folder:** a site file and a brief, committed to a control repository; the pipeline writes the result back.
- **Plan on the pull request, apply on merge,** then seed a page, check HTTPS, and optionally build a first version with Claude Code.
- **Good credentials:** a GitHub App and OpenID Connect for AWS, with no long-lived keys in the pipeline.
- **Public by default:** the control repository and its record are public; only the credentials are not.
- **An agent can drive it** by committing a request: the factory is how our agents will create sites.

## The question {#question}

I want to create a lot of sites ([a hub for agentic sites](/articles/a-hub-for-agentic-sites.html)). The next one is for the Web Summit team: the people who took part, the videos, including the one Silvio Switha made, and more. Every one of them needs the same three things before an agentic team can start: a GitHub repository with Pages turned on, a DNS record on agenticcells.site or the customer's domain, and an sgit vault. How do we go from a commit to a live website with its link?

## Three options {#options}

!shot csf-options.webp | images/ | Three ways to create a site: by hand, with scripts or a command-line tool, or with a CI pipeline. | comparison

**By hand** is what I do today: a lot of clicks across GitHub, AWS and sgit. It is slow, easy to get wrong, and only I can do it.

**Scripts, or a command-line tool,** would make it faster and repeatable. But someone still has to run them, on a machine that holds the keys, and the only record is a shell history.

**A CI pipeline** turns it around: a commit is the request, and the pipeline does the rest. In the worst case we give the pipeline the secrets it needs; in the best case, which exists, we give it short-lived, scoped credentials instead.

## A request is a folder {#request}

The factory is a control repository. Each new site is a folder, `requests/<date>__<label>/`, with two files: `site.json`, saying the site's name, its label, its domain, its owner, its template and whether to list it on the hub; and `brief.md`, saying what the site is for. A person or an agent adds the folder in a commit.

The pipeline writes back a third file, `status.json`, with everything it created: the repository, the live address, the vault and its read key, the times of each step. So every site has its own folder of history, and you can see, for any site, who asked for it, when, and exactly what was done. A change to a site's settings is the same: a commit that edits its request.

## Plan, then apply {#pipeline}

On the **pull request**, the pipeline checks the request against its rules (is the label free and well formed, is the template known, is the requester allowed) and posts a plan as a comment: the repository, the record and the vault it would create. Nothing changes yet.

On **merge**, it applies:

1. **GitHub:** create the repository from a template, turn on Pages, set the custom domain.
2. **AWS Route 53:** create the record, `label.agenticcells.site` pointing at GitHub Pages, and nothing else.
3. **sgit:** create the vault, push the site's files, publish its public read key, and seal the vault key to the owner's public key, so the secret never sits anywhere in plain text.
4. **Seed and verify:** commit a test page, wait for GitHub's certificate, turn on HTTPS-only, and check the address answers.
5. **First pass, optionally:** run Claude Code in the pipeline with the brief, to build a first version of the site and open a pull request.
6. **Record:** write `status.json` back to the request, and list the site on the hub.

By the time it finishes, the site is live, in a vault and on the hub, and everything is ready for an agentic team to do its work. Removing a site is a second pipeline: delete the request, and it removes the record the same day and archives the repository, so no address is ever left pointing at nothing ([atomic cells, end to end](/articles/atomic-cells-end-to-end.html)).

## Credentials worth trusting {#credentials}

The pipeline holds real power, so its credentials matter:

- **GitHub:** a GitHub App installed on our organisation, allowed to create repositories and manage Pages; the pipeline mints a short-lived token for each run, instead of a personal access token that never expires.
- **AWS:** OpenID Connect federation from GitHub Actions to an IAM role whose trust is limited to the control repository's main branch, and whose permission is to change records in our customer-site hosted zones, nothing more. No AWS keys are stored at all.
- **sgit:** the vault server's access token as a repository secret, until a better mechanism exists.
- **Claude:** a key, kept as a secret, for the optional first pass.

## A policy for the pipeline {#policy}

The pipeline is an agent in all but name, so it gets an Agent Behaviour Policy like any other ([what can your agent reach?](/articles/what-can-your-agent-reach.html)). It may create repositories in one organisation, records in two zones, labels that match a pattern, and a limited number a day. It can create; only the teardown pipeline can remove. Requests must come from signed commits by people or agents on an allowed list, and the plan on the pull request is the moment a person, or a rule, says yes.

## Public by default {#public}

Every site we build is public, and so is everything in it, so the factory can be public too: the control repository, every request folder, the pipeline's code, and the record of what it did. That turns the audit trail into a public one: anyone can see which sites exist, who asked for each, and exactly what the pipeline created, and anyone can copy the factory for themselves.

What stays private is only the credentials, and a public repository needs care with them. Anyone can open a pull request on a public repository, so the plan step runs with no secrets and no cloud access at all; it only reads the request and writes a comment. The credentials are reachable only by the apply step, which runs on a merge to the main branch, by people or agents on the allowed list. GitHub already keeps secrets away from pull requests opened from forks, and the pipeline must never work around that by running untrusted code with secrets. The AWS role trusts only the main branch, and the vault key is sealed, never stored.

## Why this suits agents {#agents}

The best part is who can use it. The agent I run in a loop does not need GitHub, AWS or sgit credentials of its own; it needs to be able to open a pull request on the control repository. It writes a request, the plan comes back, and on merge the site exists. The same is true for the AgentiCCells team, and eventually for customers' own agents. The factory turns creating infrastructure into writing a file, which is exactly the kind of work agents do well, with the dangerous parts kept where they belong: in a pipeline with a policy ([six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html)).

## What this does not claim {#limits}

- **This is a hypothesis and an architecture,** not yet built; the AgentiCCells team is the natural place to build it.
- **The vault step depends on sgit's token model today;** sealing the vault key to the owner keeps the secret out of the repository.
- **Running Claude Code in CI needs a key** and costs tokens; it is optional, and the agentic loop can do the first pass instead.

## Where this comes from {#sources}

My own thinking, 15 November 2026. Earlier on this site: [a hub for agentic sites](/articles/a-hub-for-agentic-sites.html), [atomic cells, end to end](/articles/atomic-cells-end-to-end.html), [starting AgentiCCells](/articles/starting-agenticcells.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html).
