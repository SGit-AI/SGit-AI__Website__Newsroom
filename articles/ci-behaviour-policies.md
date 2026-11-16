# CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents, sgit.ai

> The AgentiCCells site factory turns a committed request into a live website in under three minutes, and it holds no long-lived key. But to do what is a simple thing, create one repository and make one DNS change, we ended up giving the pipeline far more power than it needs. Its GitHub App token covers the whole organisation, with write access to administration, contents and workflows on every repository, including the power to delete them; nothing limits how many repositories it can create. Its AWS role is well scoped by type and zone, but it may create, change or delete any CNAME under agenticcells.site and point it anywhere. Why should a pipeline that makes one site per request be able to make five hundred repositories, or thousands of DNS entries? In the past we got away with this because pipeline code did not change: you could lock it and use other security primitives around it. Here it does change. Requests arrive as pull requests, agents write them, and the workflow runs as it is in the merged commit, so a pull request that also edits the workflow would inherit the whole grant. This is the same problem Agent Behaviour Policies address for agents, and the same grammar fits: each capability with a reach, an undo class, a limit, and a boundary that enforces it from outside the grant. Here is that mapping, half seriously named CI behaviour policies.

*Source: <https://newsroom.sgit.ai/articles/ci-behaviour-policies.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents

# CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/ci-behaviour-policies.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · abpcigithub-actionssecurityleast-privilegeagenticcellsriskmandatearticle

***Abstract:** The AgentiCCells site factory turns a committed request into a live website in under three minutes, and it holds no long-lived key. But to do what is a simple thing, create one repository and make one DNS change, we ended up giving the pipeline far more power than it needs. Its GitHub App token covers the whole organisation, with write access to administration, contents and workflows on every repository, including the power to delete them; nothing limits how many repositories it can create. Its AWS role is well scoped by type and zone, but it may create, change or delete any CNAME under agenticcells.site and point it anywhere. Why should a pipeline that makes one site per request be able to make five hundred repositories, or thousands of DNS entries? In the past we got away with this because pipeline code did not change: you could lock it and use other security primitives around it. Here it does change. Requests arrive as pull requests, agents write them, and the workflow runs as it is in the merged commit, so a pull request that also edits the workflow would inherit the whole grant. This is the same problem Agent Behaviour Policies address for agents, and the same grammar fits: each capability with a reach, an undo class, a limit, and a boundary that enforces it from outside the grant. Here is that mapping, half seriously named CI behaviour policies.*

What the site factory's pipeline was granted, and what one request actually needs: three rows far too wide.

## In short

- **The job is small:** create one repository and one DNS record per merged request.
- **The grant is large:** write on administration, contents and workflows for every repository in the organisation, and any CNAME under the zone.
- **No limits on scale:** nothing stops five hundred repositories or thousands of DNS records.
- **The old excuse no longer holds:** pipeline code used to be fixed; here requests arrive as pull requests, and a pull request can change the workflow.
- **The fix is a behaviour policy for the pipeline:** reach, undo, limit, and a boundary outside the grant.

## A simple job, a large grant

The site factory makes a website from a commit ([the site factory works](the-site-factory-works.md)). For each merged request it creates a repository, seeds it, sets up Pages, writes a CNAME in Route 53 and lets Claude Code write a first version. The credentials are good in one sense: there is no long-lived key anywhere. GitHub's token comes from a GitHub App, AWS is reached through OpenID Connect, and Claude through workload identity federation, all bound to one environment of one repository.

But look at what those credentials can do. The GitHub App was installed on all repositories, with write access to administration, contents, pages, actions and workflows. Its token covers the whole installation, because a repository that does not exist yet cannot be named in advance. That means the pipeline can change the settings of every repository in the organisation, rewrite their workflows, and delete them. The factory agent wrote the risk down plainly when it offered me the choice: if the key leaks, "administration of every repository in the organisation, including deletion". I chose it anyway, to get going, and noted that we would move it to a separate organisation later.

## Why five hundred repositories?

Nothing in the grant limits scale. A pipeline that makes one site per request can create as many repositories as it likes. The AWS role is much better scoped: one hosted zone, CNAME records only, names under `*.agenticcells.site` only, and the check workflow proved that AWS refuses a TXT record and the apex. But within that, it may create, change or delete any CNAME and point it at any target. Route 53's policy conditions can limit record names, types and actions; they cannot limit the value. So the same role that adds `qa-2.agenticcells.site` could repoint my brother's subdomain to somewhere else entirely, or create thousands of names.

None of that is needed. The job needs one new repository, one new name, and one target that never changes: `agenticcells.github.io`.

## Why we used to get away with it

CI pipelines have always held powerful credentials, and mostly we got away with it. The reason is that pipeline code did not change: a deploy job was written once, reviewed, and locked, and the security came from other primitives around it, branch protection, a small set of people with merge rights, and code owners.

Here the code does change, by design. Requests arrive as pull requests. Agents write them, and the plan is for agents to drive the factory by committing requests. And the apply workflow runs on a push to dev that touches `requests/`, as the workflow is in that push. So a pull request that adds a request folder and also edits `.github/workflows/apply.yml` would run its own version of the workflow, with the App token and the DNS role.

The path: a merged change to the workflow inherits the whole grant; what stands in the way today.

What stands in the way today, in the terms of an Agent Behaviour Policy ([what actually stands in the way](https://abp.sgit.ai/model/barriers/index.html)): the expectation that only requests change in that repository, which nobody enforces; a required reviewer on the apply environment, which is a setting an organisation admin can flip; and two real boundaries, the IAM conditions and the patch check that keeps Claude Code's first pass inside `src/`. Only boundaries bound anything.

## A behaviour policy for a pipeline

A behaviour policy for the pipeline: each capability with its reach, undo class, limit and what enforces it.

An [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) records what an agent can reach, what it was authorised to do, the gap between them, and what actually stands in the way. A pipeline is an agent that runs code instead of a model, and the same grammar fits it, as I argued for agents in [where assist becomes execute](where-assist-becomes-execute.md):

- **Create a repository:** the name in the request only, one per request, a few a day; undo with effort. Enforced by a small broker that mints a create-only token, not by the pipeline's own grant.
- **Change settings:** the new repository only. Enforced by narrowing the token to that repository right after creation.
- **Delete a repository:** never. Not in any token the pipeline holds.
- **Write workflows:** the new repository's seed only, from the template, in a separate step with its own token.
- **Write a DNS record:** one new name, pointing only to `agenticcells.github.io`, no overwrite, a few a day. Enforced by a small DNS broker that checks the target, since IAM cannot.
- **Change the factory's own workflows:** a person approves, enforced by branch protection and code owners on `.github/`, never by the reviewer setting alone.

Each limit is enforced by something the pipeline's grant does not include. That is the test that matters: "a control bounds a grant only if it is enforced by something the grant does not include."

## Why this matters beyond one factory

This is a small example of a large shift. Pipelines used to be fixed code with powerful credentials. Now they are being driven by agents, through requests and pull requests, at a pace no person reviews line by line. The credentials did not get smaller, and the code stopped being fixed. That is the gap RiskMandate exists to map and close ([approve at altitude](approve-at-altitude.md)), and a pipeline needs it as much as any agent does.

## What this does not claim

- **Nothing was exploited.** This is a reading of the grants and the workflow, 16 November 2026.
- **I have not checked** whether a required reviewer is set on the apply environment, or whether dev and `.github/` are protected.
- **The proposed limits and brokers do not exist yet;** FAC-007, the pipeline's behaviour policy, is on the factory's board as proposed.
- **The capability names in the figure** follow the grammar of abp.sgit.ai, applied to a pipeline; they are not part of the published list.

## Where this comes from

AgentiCCells__Site__Factory, read on 16 November 2026: `docs/github-app.md`, `docs/aws-oidc.md`, `docs/SETUP.md`, `.github/workflows/apply.yml`, `build/first-pass.mjs`, `board/FAC-007.md` and the merge commits. [abp.sgit.ai](https://abp.sgit.ai/): [the capability grammar](https://abp.sgit.ai/model/capabilities/index.html), [the undo class](https://abp.sgit.ai/model/undo/index.html) and [the barrier](https://abp.sgit.ai/model/barriers/index.html). Earlier on this site: [the site factory works](the-site-factory-works.md), [where assist becomes execute](where-assist-becomes-execute.md), [what can your agent reach?](what-can-your-agent-reach.md), [approve at altitude](approve-at-altitude.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#ci-behaviour-policies)

### Builds on

- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.

### Continued by

- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 425 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=425)

**Posting this article on LinkedIn?** The cover is [ci-behaviour-policies.jpg](banners/ci-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/ci-behaviour-policies.html)*
