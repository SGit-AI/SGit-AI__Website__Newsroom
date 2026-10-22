# Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom, sgit.ai

> Tests are deterministic: they run, or they do not, and they pass, or they fail. That makes them good enforcers of an Agent Behaviour Policy, and it raises a question we had not asked: where should each test run? A test the agent runs in its own environment is, at best, a setting the agent could skip. The same test run in a CI pipeline that stops the deploy is out of the agent's session; and with the platform protecting the pipeline, it is out of the agent's reach altogether. Moving checks outward should reduce the agent's grant. So we measured it on this newsroom, where a release takes about 7 minutes of building and testing on the agent's machine and about 5 more in CI. Of the 57 checks we mapped this week, 19 stop a deploy in CI today; 26 run only on the agent's side. Moving everything that can run on the repository into CI, as a gate, would make it 49, leave 7 with the agent because they govern the agent itself, and, by our estimate from the measured parts, cut each release by about a third. The cost of moving is small and visible: most checks already pass on all of today's content; a few need a clean-up first. One rule matters more than the numbers: moving a check out of the agent's environment improves security only if the new place is a gate. And whether a policy can be enforced is always specific to its context, so this is one example, with the cases that do not work yet said plainly.

*Source: <https://newsroom.sgit.ai/articles/where-a-check-runs.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom

# Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-22 · [article v1.0.0](versions/where-a-check-runs.md) · [newsroom v0.13.38](https://newsroom.sgit.ai/admin/versions.html) · abptestingciagentssecurityarticle

***Abstract:** Tests are deterministic: they run, or they do not, and they pass, or they fail. That makes them good enforcers of an Agent Behaviour Policy, and it raises a question we had not asked: where should each test run? A test the agent runs in its own environment is, at best, a setting the agent could skip. The same test run in a CI pipeline that stops the deploy is out of the agent's session; and with the platform protecting the pipeline, it is out of the agent's reach altogether. Moving checks outward should reduce the agent's grant. So we measured it on this newsroom, where a release takes about 7 minutes of building and testing on the agent's machine and about 5 more in CI. Of the 57 checks we mapped this week, 19 stop a deploy in CI today; 26 run only on the agent's side. Moving everything that can run on the repository into CI, as a gate, would make it 49, leave 7 with the agent because they govern the agent itself, and, by our estimate from the measured parts, cut each release by about a third. The cost of moving is small and visible: most checks already pass on all of today's content; a few need a clean-up first. One rule matters more than the numbers: moving a check out of the agent's environment improves security only if the new place is a gate. And whether a policy can be enforced is always specific to its context, so this is one example, with the cases that do not work yet said plainly.*

Where a check can run, and what that makes it: in the agent's environment, a prompt rule, a hook, a test the agent runs or signs, which the agent can skip or change; in CI as a gate, a required job or one that holds private lists as secrets, a setting while the agent can edit the workflow; and on the platform, branch protection and a person's review, a boundary set by the owner.

## In short

- **Tests are enforcers of behaviour policies.** Deterministic: they run or they do not.
- **Where a test runs decides what it is.** In the agent's environment it is a setting at best.
- **Today, 19 of our 57 checks stop a deploy in CI.** 26 run only on the agent's side.
- **Moved, it would be 49.** Seven stay with the agent, because they govern it.
- **About a third faster, by our estimate.** From the measured parts.
- **Moving out helps only if the new place is a gate.** Otherwise it is a loss.
- **Enforceable is always context-specific.** One example, with what does not work yet.

## The idea

This newsroom has gathered a lot of checks: no broken links, the version on every page, the voice, the sources, the tests of the reader's tools. That is great. But two questions follow. Are the checks running at the right altitude? And is this the best place to run each of them?

A test is a behaviour policy in disguise. In [behaviour policies from the checks](behaviour-policies-from-the-checks.md) we took all 57 of this site's checks apart and found the eight behaviours they protect: every test is checking for a behaviour. And tests have a property prompts do not: they are deterministic. They run or they do not, and they pass or they fail. So they are natural enforcers of an Agent Behaviour Policy.

But a test run by the agent, in the agent's own environment, is only as strong as the agent's willingness to run it. In the ABP's words it is a setting at best: the agent could skip it, or change it. Run the same test somewhere the agent does not control, and it becomes something else. That is the point of the exercise: the grant shrinks when a check moves out of the agent's reach. The behaviour policy also gives us the confidence not to run something in one layer, because we know it runs in the next.

## Today, measured

One release, today and moved: on the agent's machine 435 seconds, the generator 223, builders 33, validation 7 and the 18 test files 172; in CI 324 seconds; and, estimated, about 266 seconds on the agent's machine and 217 in CI with the browser tests moved to CI in parallel jobs.

We rebuilt the current release on 22 October and timed every step:

- **On the agent's machine, 435 seconds.** Borrowing sgit.ai's generator, 223; this site's builders, 33; validation, 7; the 18 browser and Node test files, 172.
- **In CI, a median of 324 seconds since 21 October.** The validator and the test job, then the tag and the deploy.
- **The session's own checks are cheap.** Summaries, 0.5 seconds; wording, 1.3; the voice, 0.2; the graph checks, under 1; page width, about 1 per page.

The ten to fifteen minutes it feels like is that, plus my own checks, plus the rebuilds when one of them fails: in [the checks, measured](the-checks-measured.md), 123 builds in a week had a median of 13 minutes from start to result, and 29 ended in a failure to fix.

## Where each check could run

Where the 57 checks run, today and moved: today 19 block the deploy in CI, 12 report in CI and 26 run only on the agent's side; moved, 49 block the deploy, 1 reports and 7 stay with the agent.

We gave each of the 57 checks in the policy map a proposed place:

- **Into CI, as a gate.** The voice rules, the summaries check, the graph checks, the reach checks we now borrow from sgit.ai's validator, the phone-width check as a test, and the reader's tests, once the two that read live services are pinned to fixed data. The private lists, the names that must never appear, can run in CI too, held as secrets the agent cannot read.
- **Reporting, not gating.** The wire test that reads its real vaults on purpose: it should tell us when live data changes, not stop a release.
- **With the agent.** Seven checks: the hooks that read the policy back after every compaction and report on it, the rule to commit before stopping, the repository scope, contacting nobody, research before writing, and an image-name clash only the build sees. They govern the agent, so they belong where the agent runs.

That moves the gating checks from 19 to 49, and the checks that only the agent runs from 26 to 7.

## The rule that matters

Moving a check out of the agent's environment improves security only if the new place is a gate. This site has the counter-example. Its browser tests run in CI, and a failure there skips the tag but does not stop the deploy: in [the checks, measured](the-checks-measured.md) that happened 43 times. If we stopped running those tests locally and left CI as it is, broken reader code could ship. So the move and the gate go together: the tests leave the agent's machine only when CI requires them for the deploy.

And CI itself is only a setting while the agent can edit the workflow and the validator in the same push it is gating. The step that turns it into a boundary is on the platform: branch protection with the checks required, and a person's review for any change to the validator, the workflow or the policy map. That step is the owner's to take, not the agent's, which is exactly right: an agent should not set its own boundaries.

## What it takes to move them

What it takes to move them: the voice and the summaries already pass on all of today's content; wording has 13 hits, mostly one phrase; graphs have two stale quotes; a rebuild differs from the commit in ten files; and two browser tests reach live services.

A check can only stop a deploy if today's content passes it. We ran each one against everything:

- **Ready now.** No em-dash and no banned word in any of the 158 articles written here; no stale summary in 2,836 sections.
- **A small clean-up.** The wording check finds 13 hits, mostly one deliberate phrase in three articles, which needs a reviewed allow-list entry; the graph check finds two quotes in one older article that no longer match its text.
- **Real work.** A rebuild of the same commit changes ten files: the date in the sitemap, a timestamp in the wire's costs, a version page that says "this release" before the commit and links the commit after it, and summaries stamped after the build. A job that rebuilds and compares would fail until the build is deterministic. And two browser tests reach live services, the wire's vaults and the vault viewer's server, so they need pinned data before they can gate.

## The estimate

From the measured parts, rearranged: the agent's machine runs the generator, the builders, the validator and the cheap policy checks, about 266 seconds instead of 435; CI runs the browser tests in parallel jobs, with the longest at about 110 seconds including set-up, so a run of about 217 seconds instead of 324. In all, about 480 seconds a release instead of about 760: roughly a third less, before counting the rebuilds a failed local check causes. The cheap, deterministic checks run in both places: on the agent's side as early feedback, in CI as the gate. The expensive ones run once, in CI.

On security, the same move takes the checks that stop a deploy from 19 to 49, and the checks kept only by the agent from 22 expectations to three. With branch protection and reviews set by the owner, all 49 become boundaries.

## Signing the test run

Some checks cannot leave the agent's environment, or should not run twice. For those there is a middle step, now that our agents are close to having key pairs of their own: the agent signs its test run. A small attestation, the commit, the hashes of the test files, and the results, signed with the agent's key, which CI verifies before the deploy.

It is worth being precise about what that buys. It does not prove the agent ran the tests honestly; the run is still in the agent's environment. It does prove which agent claims to have run what, on which commit, and it makes skipping a test visible rather than silent. Combined with CI re-running a sample of the signed tests, a forged attestation becomes a detectable event. That is defence in depth, not a boundary, and the policy should label it so.

## Enforceable is always specific

This will not work for everything. It works where the agent's work runs through a code base and a pipeline, as it does here. For an agent answering customers in a chat, there is no pipeline between its action and the world, and the checks have to sit in the systems it calls. Whether a policy can be enforced, and where, is always specific to its context. What we need is many examples like this one: for this scenario, this check, here, with this effect on time and security; and, just as useful, the cases where we cannot do it yet, said plainly.

## The proposed steps

For the owner to decide, in order:

1. **Port the cheap checks into this site's validator and a CI job:** the voice, the summaries, the graph checks. They pass today, apart from the small clean-up.
2. **Clean up:** the reviewed allow-list entry for the wording check, and the two graph quotes.
3. **Pin the live tests' data, split the browser tests into parallel jobs, and require them for the deploy.**
4. **Then stop running the browser tests locally for a content release.** Never before step 3.
5. **Make the build deterministic, and add a rebuild-and-compare job.**
6. **Branch protection and reviews on the checks.** The owner's step.
7. **Signed test runs, when the agents have their keys.**

## What this does not claim

- **The CI and total times after the move are estimates.** From measured parts, not a measured run.
- **One release timed.** On one machine, on 22 October 2026.
- **The placement is a proposal.** Nothing has been moved yet.
- **CI is still a setting until the platform protects it.** The boundary needs the owner's step.
- **A signed run is not a boundary.** It makes skipping visible, not impossible.

## Where this comes from

My voice memo of 22 October 2026; a timed rebuild of v0.13.37 that day; the timings of the session's own checks; a run of the wording, summaries and graph checks and of a voice scan over all of this site's content; GitHub Actions job medians since v0.13.7; and the policy map published with [behaviour policies from the checks](behaviour-policies-from-the-checks.md). Related: [the checks, measured](the-checks-measured.md), [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html), [the delegation record](the-delegation-record.md), [a secret is a QR code](a-secret-is-a-qr-code.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#where-a-check-runs)

### Builds on

- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [The checks, measured: 123 local builds, 245 CI runs, 1,061 test checks, and where each check actually lives](the-checks-measured.md) A release measured step by step, 123 local builds, 245 CI runs and 1,061 test checks, and where each check actually lives.
- [The delegation record: RiskMandate's go-to-market plan, one workflow taken from an existing business rule to evidence that still holds after a change, starting with our own inbox](the-delegation-record.md) RiskMandate's go-to-market plan: one workflow from an existing business rule to evidence that still holds after a change, starting with our own inbox.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.

### Continued by

- [The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised](the-sidecar-repository.md) A second repository the agent cannot write to, which checks every release, trusts signed checks instead of re-running them, and is the only thing that deploys.
- [The rules of the game: a policy for which files an agent may change, and the least GitHub can enforce today without a new tool](the-rules-of-the-game.md) A policy for which files an agent may change, and the least GitHub can enforce on a public repository today without a new tool.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 256 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=256)

**Posting this article on LinkedIn?** The cover is [where-a-check-runs.jpg](banners/where-a-check-runs.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-a-check-runs.html)*
