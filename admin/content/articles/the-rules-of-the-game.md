---
title: The rules of the game: a policy for which files an agent may change, and the least GitHub can enforce today without a new tool
date: 2026-10-22
author: Dinis Cruz
author_url: about/index.html
summary: The agents that build this site can change the pipeline that checks them. In the last eleven days, 62 of 227 commits touched the workflow, the validator, the tests or the build scripts, from six agents, and 17 changed the workflow itself, one of them a speed-up this session made. That is useful work, and it is also the hole: an agent that can change the check can pass any release. So we wrote the rules of the game down as a policy, in five zones: content an agent changes freely; the gates, which need a second key; identity, which only the owner changes; vendored code, refreshed only from its source; and the rules themselves, which no agent touches. Then we mapped what GitHub can enforce on a public repository today, with no new tool. The answer is less than I expected, but enough. A hook in the agent's harness and a guard job in CI mean an agent has to make two deliberate changes to get round them, which is no longer a mistake. One setting by the owner, a token that cannot change workflow files, turns the guard into a boundary. GitHub's path rules for pushes exist, but only for private repositories; and there is a known gap we describe. The next article puts the last step in a repository the agent cannot touch.
version: v0.13.39
license: https://creativecommons.org/licenses/by/4.0/
tags: abp, ci, github, agents, security, policy, article
status: published
---

!shot rg-zones.webp | images/ | The rules of the game in five zones: content, the gates, identity, vendored code and the rules themselves. | concept

## In short {#in-short}

- **Agents change the pipeline.** 62 of 227 commits in eleven days; 17 to the workflow.
- **So we wrote the rules down.** Five zones, from free to never.
- **A gate needs a second key, not a ban.** The changes are often good ones.
- **Two deliberate changes to get round it.** A hook, then the CI guard.
- **One owner setting makes it a boundary.** A token that cannot change workflows.
- **GitHub's path rules are for private repositories.** Not for this one.
- **There is a known gap.** Closed properly by the sidecar.

## The hole {#hole}

This site is built and released by agents. Every push to `dev` is a release: the workflow validates the site, runs the reader's tests in a browser, tags the release and deploys it. In [where a check runs](/articles/where-a-check-runs.html) I argued that moving checks out of the agent's environment and into that pipeline turns them from settings into gates. But a gate is only as strong as the agent's inability to open it.

And today the agents can open it. Between 11 and 22 October, 62 of the 227 commits to this repository touched a file that checks the work: the workflow, the validator, the test files, the build scripts. They came from six agents and from commits with no agent label. 17 of them changed the workflow itself, including one from this session, v0.13.7, which cached the browser the tests use and made every release faster. So the credential this session pushes with can change the pipeline that gates it.

None of those changes was malicious; most were improvements. That matters for the design. A rule that says "never change the pipeline" would have blocked good work 62 times. The rule we want is that the agent can propose a change to what checks it, and someone else has to agree.

!shot rg-commits.webp | images/ | Commits that touched the checks, by agent, from 11 to 22 October 2026: 62 of 227 in all. | comparison

## The policy {#policy}

So the first step is the one I asked for in the memo: write the rules of the game down, so that whatever enforces them, now or later, has something to enforce. The policy is [published with this article](/articles/data/the-rules-of-the-game__policy.json). Its principle is one sentence: an agent may change content freely; it may change what checks its work only with a second key; it may never change its own rules.

It has five zones:

- **Content, free.** The articles, the newsletter, the release notes, the notes, and every page the builders generate. The version file only to the next version, which CI already checks.
- **The gates, a second key.** The workflow, the validator, the test runner and the test files, the wording and summaries checks, the publish and sync scripts, `.gitignore`, and the code that runs in the reader's browser, which is not content even though it ships with it.
- **Identity, the owner only.** Who the agents are, the published vault keys, the domain the site is served on, and the agents' own settings.
- **Vendored, from upstream only.** Code copied from another project and pinned by hash.
- **The rules, never by an agent.** The policy itself, and whatever enforces it.

The copy published here is for reading. The copy that counts has to live somewhere the agent cannot write, or the last zone means nothing; that is the subject of [the sidecar repository](/articles/the-sidecar-repository.html).

## What GitHub offers today {#github}

!shot rg-github.webp | images/ | What GitHub offers a public repository today without a new tool, and what needs a paid plan or an organisation. | comparison

Then the research: what can GitHub itself enforce, on this repository, today? This site's repository is public, owned by an organisation, and its release branch had no protection when we checked on 22 October. From GitHub's documentation:

- **Path rules for pushes exist, but not here.** A push ruleset can "prevent commits that include changes in specified file paths from being pushed", and GitHub's own example is the workflow files. But push rulesets are available "in internal and private repositories" on the Team plan and above. For a public repository, the one rule that does exactly what we want is not on offer.
- **Required workflows are for pull requests.** A ruleset can require a workflow from another repository to pass, but it is set at the organisation level, and the documentation says it "will block direct pushes" and belongs on branches "where all changes to the branch are performed by pull requests". Our releases are direct pushes.
- **Code owners need pull requests too.** A `CODEOWNERS` file with a required review means "any pull request that modifies content with a code owner must be approved by that code owner", and the file can own itself. But it applies to pull requests; a branch rule requiring them applies to the whole branch, content and all.
- **Branch rules that are not about paths are available.** Rulesets and protected branches work on public repositories on the free plan: block force pushes, block deletion, restrict who can create branches.
- **Deployments can require a person.** Environments with required reviewers work on public repositories on every current plan, and "users who initiate a deployment cannot approve the deployment job".
- **A token can lack the right to change workflows.** A classic token needs the `workflow` scope, and a GitHub App the Workflows permission, to change files in `.github/workflows`. A token without it cannot push a change there.

So, on a public repository where agents push straight to the release branch, GitHub has one boundary that is about paths, and it covers only the workflow files. Everything else is either about the whole branch or needs a private repository. That is the starting point.

## The least we can do {#minimal}

!shot rg-layers.webp | images/ | The controls in order, and what it takes to get round each, from the policy to the sidecar repository. | concept

Here is the smallest set that works, in the order of the barriers in an [Agent Behaviour Policy](/articles/behaviour-policies-from-the-checks.html):

1. **The policy.** An expectation. It catches nothing on its own; it is what the rest enforce.
2. **A hook in the agent's harness.** A setting. Claude Code can deny edits to paths with permission rules, such as `Edit(/.github/workflows/**)`, and a `PreToolUse` hook "can block" a tool call before it runs. This catches mistakes at the moment they are made. Its documented limit: the rules do not apply to "a Python or Node script" that writes the file. So it is a guard against accidents, not against intent.
3. **A guard job in CI.** A setting. In the validation job, before anything else: compare the files changed since the last release with the policy's paths, and if any gate, identity or rules path changed, fail, unless the commit arrived as a pull request approved by an account the agent does not act as. Validation failing stops the tag and the deploy, as it does today.
4. **A token that cannot change workflows.** A boundary, and the owner's step.
5. **The sidecar repository.** A boundary even under full compromise, in the next article.

With only the first three, getting a change to the validator into a release takes two deliberate acts: getting round the hook, by writing the file some other way or by changing the agent's settings, which are themselves in the identity zone; and editing the guard out of the workflow. An agent does not do both by accident. If it does both, it is, as I put it in the memo, borderline malicious, and both acts are in the history for anyone to see.

Step 4 changes the picture more than its size suggests. If the agent's token cannot change workflow files, it cannot edit the guard either, and the guard lives in the workflow. So the guard becomes a boundary, not just for the workflow but for every path the policy lists: one owner setting turns the whole gates zone into a second-key zone. The guard's path list has to be written in the workflow file itself, not read from a script the agent could change. And whether the integration this session pushes through can be given a token without that permission is something I have not been able to check; v0.13.7 shows it can change workflows today.

## Where it can still break {#gaps}

Assuming the agent tries, here is what the first four steps leave open:

- **An old workflow can come back.** GitHub's documentation for the classic scope says a workflow file "can be committed without this scope" if an identical file exists on another branch. So an agent that can create a branch at an old commit, from before the guard, may be able to bring the old workflow back. Blocking branch creation for the agent with a ruleset closes the obvious route; the sidecar closes it properly, because it compares the workflow with an approved copy.
- **Rewriting history.** A force push to `dev` could replace the history the guard compares against. Blocking force pushes on `dev` and `main` is available today on the free plan.
- **Manual runs on other branches.** The workflow can be run by hand on a branch. The deployment environment already restricts which branches can deploy, and that restriction is a setting only the owner can change.
- **Approving itself.** If the agent acts as the owner's account, the owner's approval is not a second key. The approver has to be an account, and a person, the agent does not act as.
- **Content is still free.** An agent can still publish a bad article, or leak something into one. The validator's tripwires and the leak scan catch some of that; the private lists belong in the sidecar, where the agent cannot read them.

## Second key, not never {#second-key}

The point of the design is not to stop agents improving the pipeline. They have improved it, many times, and some of those changes, like the browser cache, made every later release faster. The point is that a change to what checks an agent's work is a different kind of change from an article, and it should be seen and agreed by someone other than the agent. That is the same rule, at a smaller scale, as in [the delegation record](/articles/the-delegation-record.html): a change to authority needs approval; a change in behaviour needs evaluation.

And even if all we have done today is write the policy, that is worth something: it is the specification that somebody else, a hook, a CI job, an owner, a second repository, can now enforce.

## What this does not claim {#limits}

- **Nothing here is enforced yet.** The policy is proposed; no hook, guard or token change is in place.
- **The GitHub findings are from documentation.** Read on 22 October 2026, not tested on this repository.
- **The token step is untested.** I do not know yet whether this session's integration can be given a token without the workflow permission.
- **The old-workflow gap is documented for the classic scope.** Whether an App token behaves the same is not stated.
- **The commit counts are by path.** A commit touching a gate file is counted, whatever it changed.

## Where this comes from {#sources}

My voice memo of 22 October 2026; this repository's history from 11 to 22 October, counted by path and by the agent label in each commit's subject; the workflow file as it is at v0.13.38; and GitHub's documentation, read that day, on rulesets and the rules they offer, push rulesets, protected branches, code owners, deployment environments, OAuth scopes and GitHub App permissions, and Claude Code's documentation on permission rules and hooks. The research was done by a background agent and checked against the documentation's source. Related: [where a check runs](/articles/where-a-check-runs.html), [behaviour policies from the checks](/articles/behaviour-policies-from-the-checks.html), [the checks, measured](/articles/the-checks-measured.html), [the sidecar repository](/articles/the-sidecar-repository.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
