---
id: 092
title: The reviewers' vaults: a public vault per external reviewer, gated by a security agent, worked by a review desk
kind: story
priority: high
created: 2026-10-27T18:00:00Z
source: Dinis, 27 October 2026: "Actually, ChatGPT can use vaults, because I've used it before. What about we create a collaborative vault for ChatGPT? ... it's a public vault, so we have to make sure that everything goes there is public. We can even track issues FS, we can track tasks ... which agent should we set up to process this? And which agent should we then basically give the vault key, and which one should create a PKI so that you can communicate with this? ... we probably also need to wire up the security agent on schedule, so that the security agent reviews everything that goes on there before it gets processed." Then: "One per external reviewer and yes it keeps files between runs."
release: v0.13.111
estimated_effort: large
---
# The reviewers' vaults: a public vault per external reviewer, gated by a security agent, worked by a review desk

## What is asked
1. A collaborative vault for ChatGPT, one per external reviewer, public, so everything in it must be public.
2. Reviews, issues and tasks tracked in it.
3. Which agent processes it, which holds the vault key, which makes the pki keys to communicate with it.
4. The security agent, on a schedule, reviewing everything in it before it is processed.

## Scenario
```gherkin
Given a reviewer's public vault, with the desk's signed brief and queue
When the reviewer writes a review and signs it with its pinned key
And the security agent's signed verdict clears the file's SHA-256
Then the review desk takes it into the repository, saying who signed it and who cleared it

Given a file that talks to the agents, a desk file changed by someone else, or a review changed after it was cleared
Then the verdict flags it and the desk does not take it

Given a verdict changed after it was signed
Then the desk refuses it and takes nothing
```

## Outcome
Shipped in v0.13.111. `admin/build/review_vault.py` (`create`, `publish`, `gate`, `take`, `scan`) and `admin/build/review_keys.mjs` (the desk's and the security agent's keys, with pki.sgit.ai's code, their register submissions, and sealing to the editor). ChatGPT's vault is uni3mldz, its public read key in `admin/content/reviews/vaults.json` (published as `reviews/vaults.json`, and on `reviews/queue/`); the desk's key sha256:2fed42a3c24d6d20 and the security agent's sha256:e43d606266630bec in `admin/content/reviews/keys/` (published at `reviews/keys/`); the private halves and the vault key sealed to Dinis's pki.sgit.ai key. The brief gains the vault route. Test: `admin/build/test_review_vault.mjs` (27 checks, the real sgit CLI against the mock, the reviewer played with `sgit pki`). Design and the two scheduled runs' prompts: `admin/notes/2026-10-27__the-reviewers-vaults.md`. Left: the three secrets into the environment, the submissions filed and linked with `operates`, ChatGPT's key made and pinned, the `review-gate` branch allowed, then the two scheduled runs.
