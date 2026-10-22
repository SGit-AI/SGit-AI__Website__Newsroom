# The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised, sgit.ai

> In the rules of the game we wrote down which files an agent may change and found that, on a public repository, GitHub can enforce only part of it. This is the other part. A sidecar repository, which no agent can write to, holds the Agent Behaviour Policies, the policy for this repository, the approved hashes of every file that checks the agent's work, the public keys, and the private lists. At the end of each release it reads the release commit; checks the changed paths against the policy; compares the workflow and the tests with their approved copies; verifies GitHub's signed attestation that the approved tests passed on that exact commit, instead of running them again; runs its own checks, which the agent can neither see nor change; and only then deploys the site, which moves to the sidecar. We designed it assuming the worst: an agent that removes its hooks, rewrites the workflow, fakes statuses and adds workflows of its own. Each of those either does nothing or stops the deploy until the owner looks. It uses only what we already have: GitHub Actions, GitHub's attestations and its command-line tool, and our own signing. It is a design, not yet built, and it has residual risks we say plainly.

*Source: <https://newsroom.sgit.ai/articles/the-sidecar-repository.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised

# The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-22 · [article v1.0.0](versions/the-sidecar-repository.md) · [newsroom v0.13.39](https://newsroom.sgit.ai/admin/versions.html) · abpcigithubagentssecuritypkiarticle

***Abstract:** In the rules of the game we wrote down which files an agent may change and found that, on a public repository, GitHub can enforce only part of it. This is the other part. A sidecar repository, which no agent can write to, holds the Agent Behaviour Policies, the policy for this repository, the approved hashes of every file that checks the agent's work, the public keys, and the private lists. At the end of each release it reads the release commit; checks the changed paths against the policy; compares the workflow and the tests with their approved copies; verifies GitHub's signed attestation that the approved tests passed on that exact commit, instead of running them again; runs its own checks, which the agent can neither see nor change; and only then deploys the site, which moves to the sidecar. We designed it assuming the worst: an agent that removes its hooks, rewrites the workflow, fakes statuses and adds workflows of its own. Each of those either does nothing or stops the deploy until the owner looks. It uses only what we already have: GitHub Actions, GitHub's attestations and its command-line tool, and our own signing. It is a design, not yet built, and it has residual risks we say plainly.*

The sidecar, end to end: the agent pushes a release to the site's repository; its CI runs the tests and signs the result; the sidecar reads the commit, checks the paths against the policy, compares the workflow and tests with approved hashes, verifies the signed result, runs its own private checks, asks the owner when something in the gates changed, and deploys the site.

## In short

- **A second repository the agent cannot write to.** It holds the policy and the keys.
- **It is the only thing that deploys.** The site moves there.
- **It treats the site's repository as data.** It never runs that code with secrets.
- **It trusts a signed check, not a status.** Only from the approved workflow.
- **Changed gates wait for the owner.** Everything else goes straight out.
- **Designed for full compromise.** Each attack does nothing, or stops the deploy.
- **No new tools.** Actions, attestations, and our own signing.

## Why a second repository

In [the rules of the game](the-rules-of-the-game.md) we set out five zones and found the limit of what GitHub enforces on this public repository: a hook and a guard job make getting round the rules a deliberate act, and a token without the right to change workflows turns the guard into a boundary. But the last zone, the rules themselves, cannot live in the same repository as the agent. Anything an agent can write, a compromised agent can rewrite. And there is a known gap: an older workflow, without the guard, may be able to come back.

So the memo's second idea: a sidecar. A separate repository, with its own CI, which the agents have no access to. It holds what the agents must not change, and it decides what goes live. The site's own pipeline still runs, still gives the agent fast feedback, and still does the expensive work. The sidecar checks that work, and adds the checks the agent should never see.

## What it holds

- **The Agent Behaviour Policies and the repository's policy.** The copy of [the policy](data/the-rules-of-the-game__policy.json) that counts.
- **The lock.** The approved hash of every file in the gates zone: the workflow, the validator, the test files, the build scripts and the reader's code. It changes only when the owner approves a change.
- **Its own checks.** Its own copy of the validator's rules and the voice, summaries and graph checks, pinned in the sidecar.
- **The private lists, as secrets.** The names that must never appear, the local key fragments the leak scan looks for. The agent cannot read them, so it cannot write around them.
- **The public keys.** Of each agent, from their key pairs, and of the owner.
- **The site.** The domain and the Pages deployment move here, so nothing else can publish.
- **The record.** A signed line for every release it deployed, or refused.

## What it does

At the end of each release, in order:

1. **Read the release commit.** The site's repository is public, so the sidecar can read `dev` and check out the commit with no credential at all. It deploys only commits that follow on from the last one it deployed.
2. **Check the paths.** Compare the files changed since the last deployed release with the policy's zones. Content goes on. Identity and rules paths stop the run.
3. **Check the lock.** Hash every gate file in the commit and compare with the lock. If they all match, the pipeline that tested this commit is the approved one.
4. **Verify the signed result.** The site's CI attests a small results file: the commit, the hashes of the test files, and each test's outcome. The sidecar verifies the attestation with GitHub's own tool, requiring that it was signed by the site's repository, by the deploy workflow, for this exact commit.
5. **Run its own checks.** The cheap ones, on the files as committed: the voice, the summaries, the version, the private lists. Seconds, as we measured in [where a check runs](where-a-check-runs.md).
6. **Ask the owner when the gates changed.** If any hash differs from the lock, the deploy job waits on an environment with the owner as required reviewer, showing the diff. On approval, the lock is updated with the new hashes.
7. **Deploy, and sign the outcome.** Publish the site, and add a signed line to the record: the commit, the policy version, the checks run, the checks trusted, and the result.

Nothing in it needs a new tool. GitHub Actions runs it. Artifact attestations are built into Actions; for a public repository they are recorded in a public transparency log, and GitHub's hosted runners already have the command-line tool that verifies them. Our own key pairs, the kind described in [a secret is a QR code](a-secret-is-a-qr-code.md), sign the record.

## Trust the signed check, not the status

When the sidecar trusts a check and when it runs it again: if the workflow and every test file match the lock and the attestation is valid for the commit, the result is trusted and nothing is re-run; if anything in the gates differs, the owner decides, and the tests run again in the sidecar, without secrets.

The efficiency in the memo comes from here. The reader's tests are the slowest part of a release: 227 seconds in the last run, against 19 for validation and 44 for the deploy. The sidecar should not run them again if it can know they ran honestly.

What makes that possible is what an attestation records. It is signed with a short-lived certificate tied to the identity of the workflow run, and it records the repository, the commit and the workflow that produced it. So the sidecar can ask a precise question: did the deploy workflow, on this commit, produce this result? And the lock answers the rest: was that workflow, and were those tests, the approved ones? If both answers are yes, the result is as good as one the sidecar produced itself, and it does not re-run anything.

A commit status, or a green tick on a check, is not the same. Anything with the right token can post a status. An agent that can write to the repository may well be able to post one. The sidecar ignores them.

The agents' own signatures fit here too, with a clear label. When the agents have their key pairs, they can sign their local test runs, and the sidecar can verify them against their public keys. That proves which agent claims to have run what. Under full compromise, the agent's key is compromised with it, so the sidecar treats an agent's signature as attribution, never as a reason to skip a check.

## Assume total compromise

What a fully compromised agent can try, and what the sidecar does: remove its hooks, nothing relies on them; rewrite the workflow or the tests, the lock differs and the owner decides; fake a status, ignored; forge a signed result, it fails verification; add a workflow to steal secrets, the site's repository holds none; bring back an old workflow, the lock differs; rewrite history, the sidecar deploys only from the last release; ring the doorbell, it reads the state itself; leak in content, the private lists catch it.

The memo asked for the analysis to assume the agent is fully compromised: it can do anything its credentials allow. So, attack by attack:

- **It removes its hooks.** Nothing in the sidecar relies on them. They were there to catch mistakes early.
- **It rewrites the workflow, the validator or a test.** The lock differs. The deploy waits for the owner, who sees exactly which gate changed.
- **It brings back an old workflow without the guard.** The lock differs, so the same thing happens. This closes the gap left in the first article.
- **It fakes a status or a check.** The sidecar reads neither.
- **It forges a signed result.** It cannot get a certificate for the deploy workflow without running the deploy workflow; and if it changes the deploy workflow to sign a false result, the lock differs.
- **It adds a workflow to steal secrets.** The site's repository holds no secrets today: its workflow uses none. The Pages deployment, the private lists and the owner's approval all live in the sidecar. The design depends on keeping it that way.
- **It rewrites the history.** The sidecar deploys only a commit that follows on from the last one it deployed. Anything else waits for the owner.
- **It plants code that runs during the tests.** When the sidecar has to run the tests itself, it runs them in a job with no secrets and no write permission, and keeps only the result.
- **It rings the doorbell, or never rings it.** If the site's CI triggers the sidecar, the token for that lives in the site's repository, where the agent can find it. So it is only a doorbell: the sidecar ignores what the message says and reads the commit itself, and it also runs on a schedule, so silence does not stop a release check.
- **It leaks a key, or a name, in an article.** Content is free in the policy, but the sidecar's leak scan uses the private lists the agent has never seen.

## What remains

Total compromise of the agent is covered; other things are not:

- **The owner's approval is the last line.** A compromised agent can ask for it with a plausible reason. The approval page shows the diff, and that is what has to be read.
- **The sidecar's own owner and GitHub itself.** If either is compromised, so is the sidecar. That is outside this design.
- **Content within the rules.** An agent can still publish a bad but valid article. The sidecar checks rules, not judgement; the editor's review does that.
- **The reader's code in the free zone, until the lock covers it.** The policy now lists it as a gate; the lock has to hash it from the first day.
- **It is a design.** None of it is built. The first version will find gaps this one missed.

## The cost

Two repositories instead of one, and a few changes to the site's pipeline: attest the test results; remove the deploy job and the domain, which move to the sidecar; keep validation and the tests for fast feedback. A release that changes only content would cost the sidecar its own checks, a few seconds, plus verification and the deploy, instead of running the tests a second time. A release that changes a gate costs the owner a look at the diff. Over the last eleven days that would have been a look at 62 of 227 commits, which is too many; the answer is to batch machinery changes, not to drop the rule.

## The steps

For the owner to decide, in order:

1. **Create the sidecar repository**, with no agent given access to it.
2. **Put the policy, the lock and the private lists there.**
3. **Add the attestation to the site's test job.**
4. **Build the sidecar workflow**, with the owner as required reviewer on its deployment.
5. **Run it alongside the current deploy for a week**, comparing what each would have published.
6. **Move the domain**, and remove the deploy from the site's repository.

## What this does not claim

- **Nothing here is built.** It is a design, and a proposal to the owner.
- **The timings are from one run.** The jobs of v0.13.38, on 22 October 2026.
- **The GitHub features are from documentation.** Attestations, environments and their availability, read on 22 October 2026, not yet tested here.
- **The agents' key pairs are not yet in use.** Their signatures are planned, and are attribution only.
- **The secrets claim is about today's workflow.** It uses none; a later change could add one.

## Where this comes from

My voice memo of 22 October 2026; this repository's workflow at v0.13.38 and the job timings of its last run; GitHub's documentation, read that day, on artifact attestations, the verify command, OpenID Connect claims, deployment environments, the events that trigger workflows, and rulesets; and the research and policy in [the rules of the game](the-rules-of-the-game.md). Related: [where a check runs](where-a-check-runs.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [the delegation record](the-delegation-record.md), [a secret is a QR code](a-secret-is-a-qr-code.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#the-sidecar-repository)

### Builds on

- [The rules of the game: a policy for which files an agent may change, and the least GitHub can enforce today without a new tool](the-rules-of-the-game.md) A policy for which files an agent may change, and the least GitHub can enforce on a public repository today without a new tool.
- [Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom](where-a-check-runs.md) Tests as enforcers of behaviour policies, and what moving them out of the agent's environment would gain, measured on this newsroom.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [The delegation record: RiskMandate's go-to-market plan, one workflow taken from an existing business rule to evidence that still holds after a change, starting with our own inbox](the-delegation-record.md) RiskMandate's go-to-market plan: one workflow from an existing business rule to evidence that still holds after a change, starting with our own inbox.

### Continued by

- [The rules of the game: a policy for which files an agent may change, and the least GitHub can enforce today without a new tool](the-rules-of-the-game.md) A policy for which files an agent may change, and the least GitHub can enforce on a public repository today without a new tool.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 258 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=258)

**Posting this article on LinkedIn?** The cover is [the-sidecar-repository.jpg](banners/the-sidecar-repository.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-sidecar-repository.html)*
