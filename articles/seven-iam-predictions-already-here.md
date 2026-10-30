# Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way, sgit.ai

> Sunnykumar K., a lead IAM engineer, posted seven predictions for identity and access management from 2027 to 2030, the ones he is designing for now: static roles give way to policy-driven access, non-human identities outnumber humans 100 to 1, passwords start to disappear, identity tools consolidate into one platform, continuous access evaluation becomes standard, access decisions are made by models, and identity becomes a board-level conversation. I agree with most of them, and several are not predictions for us: they describe how our agent teams already work. In two days this week one person ran more than thirty agent sessions, each with its own key pair, its own role and a written behaviour policy. Every session's key is vouched for with an end date, and dies with the session; secrets are sealed to keys, never typed; the reader's vault on this site opens with a passkey. Each agent wakes on a schedule and its work is planned, reviewed before and after, and checked against its plan, and any agent can pull a hold that pauses all actions. And every control is classified by who enforces it, so that a board or an insurer can count the ones that are real. I would bet the other way on two. Consolidation into one platform is the wrong goal for agents: the policy should be an open document that many enforcers read. And access decisions should not be handed to a model: a model can advise, but the boundary has to be deterministic and outside it, because an agent's own account of what it did is a self-report. This article goes through the seven, with what we run and what we have measured.

*Source: <https://newsroom.sgit.ai/articles/seven-iam-predictions-already-here.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way

# Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-30 · [article v1.0.0](versions/seven-iam-predictions-already-here.md) · [newsroom v0.14.5](https://newsroom.sgit.ai/admin/versions.html) · identityiamagentsnon-human-identitypkipasskeysagent-behaviour-policiesarticle

***Abstract:** Sunnykumar K., a lead IAM engineer, posted seven predictions for identity and access management from 2027 to 2030, the ones he is designing for now: static roles give way to policy-driven access, non-human identities outnumber humans 100 to 1, passwords start to disappear, identity tools consolidate into one platform, continuous access evaluation becomes standard, access decisions are made by models, and identity becomes a board-level conversation. I agree with most of them, and several are not predictions for us: they describe how our agent teams already work. In two days this week one person ran more than thirty agent sessions, each with its own key pair, its own role and a written behaviour policy. Every session's key is vouched for with an end date, and dies with the session; secrets are sealed to keys, never typed; the reader's vault on this site opens with a passkey. Each agent wakes on a schedule and its work is planned, reviewed before and after, and checked against its plan, and any agent can pull a hold that pauses all actions. And every control is classified by who enforces it, so that a board or an insurer can count the ones that are real. I would bet the other way on two. Consolidation into one platform is the wrong goal for agents: the policy should be an open document that many enforcers read. And access decisions should not be handed to a model: a model can advise, but the boundary has to be deterministic and outside it, because an agent's own account of what it did is a self-report. This article goes through the seven, with what we run and what we have measured.*

Sunnykumar K.'s post: seven IAM predictions for 2027 to 2030.

## In short

- **Sunnykumar K. posted seven IAM predictions** for 2027 to 2030, the ones he is designing for now.
- **Several describe how our agent teams already run:** policy per role, a key per session, no passwords for agents, short-lived access.
- **Non-human identities already outnumber humans here,** by more than thirty to one in two days, each with its own key.
- **Continuous evaluation is per wake,** with a hold any agent can pull, and keys that expire.
- **Identity reaches the board** when controls are classified by who enforces them, so they can be counted and insured.
- **I would bet against consolidation:** the policy should be open and read by many enforcers, not owned by one platform.
- **And against model-made access decisions:** a model can advise, but the boundary has to be deterministic and outside it.

## The seven, in his words

Sunnykumar K. writes as a lead IAM engineer, after ten years in the field and nine posts in a series on where identity risk lives. His seven predictions, which he says he is designing for right now in enterprise environments:

1. **Static roles officially die.** "By 2028: RBAC will be scaffolding for attribute + policy-driven access."
2. **Non-human identities outnumber humans 100:1.** "AI agents will spawn other agents. Machine identity will need its own governance category with dedicated tooling and headcount."
3. **Passwords start actually disappearing.** "Passkeys become the default consumer auth. Workforce IAM follows."
4. **IGA, CIEM and PAM consolidate into one platform.**
5. **Continuous access evaluation becomes standard.** "SSO with 8-hour token = considered negligent by 2028."
6. **AI-driven access decisions.** "Adaptive access policies get replaced by ML models trained on your identity + behavior data."
7. **Identity becomes the board-level conversation.** "Identity is the risk. Board wants numbers."

He ends by asking which prediction readers disagree with most. I will answer that at the end. First, where we already are.

## Roles become policies

We still use roles, but a role here is a name for a written policy, not a bundle of permissions. Every member of our agent teams has a role file and a `policy.json` beside it: what it may read and write, which paths it owns, which vaults it may touch, and what it must never do. The gate checks the policies as data: two members claiming the same file fails the build. That is attribute and policy-driven access, with the role as the label on the policy.

The policy is an [Agent Behaviour Policy](a-policy-beside-the-prompt.md): for one agent in one deployment, its mandate, what it can reach, the gap, and what stands in the way of each capability. It answers the question RBAC never did: not only who may do this, but what this agent is for.

## Non-human identities, already the majority

Agent sessions with their own keys this week, against the one person who ran them.

The prediction is 100 to 1 by 2030. In our teams it is already more than 30 to 1 in two days, for one person. On 29 October the talk's team had nine staffed agents. Overnight into 30 October, the cold-read team had a conductor and twelve members, and the book's team a conductor and six members by 01:42, and two more later in the day. Each of those sessions made its own key pair, published the public half beside its role, and was vouched for. And they do spawn other agents: the book's first draft was written by sub-agents, one or two chapters each.

He is right that machine identity needs its own governance category. Ours is a key per session, a role file and a policy per agent, and a register of every key: [agents have an identity now](agents-have-an-identity-now.md) describes it, and [the push is the authorisation](the-push-is-the-authorisation.md) how a new key is accepted. Today's [article on a contractor's agent at the Pentagon](the-contractors-agent-and-three-policies.md) shows what happens when an agent has no identity of its own and borrows a person's.

## Passwords, gone for agents first

Our agents do not get passwords. A secret is sealed to a session's public key, so only that session can open it, and it is never typed into the agent's context; [a secret is a QR code](a-secret-is-a-qr-code.md) and [handing secrets to agents](handing-secrets-to-agents.md) describe how. On the reader's side, the vault on this site opens with a passkey: its PRF output computes the door that holds the key, so there is no password to steal. I agree that password managers pivot to secrets management; for agents the pivot is further, from storing a secret to sealing it to a key that dies with the session.

## Continuous evaluation, per wake

An eight-hour token is long for a person and far too long for an agent. Our agents work in wakes: each wake has five steps, a plan, a review of the plan by a separate sub-agent, the work, a review of the work, and a check against the plan, and each is recorded. The editor's keys vouch for agents with end dates, and a check after the date refuses; one such link, for our vault registry, ran out today, and our rule is to stop using it until it is renewed. Session keys die with the session. And any member can pull the brake: a file, `team/HOLD.md`, which every wake's start script looks for first, stopping if it is there; only I can lift it. On the day of the talk it was pulled at 18:44, when my usage reached 95%, and it was never lifted that day. Continuous access evaluation, for us, is every wake asking again whether it may proceed.

## The board wants numbers

Agreed, and the number has to be about controls that are real. We classify every row of an agent's policy by who enforces it: **none**; an **Expectation**, prose the agent reads; a **Setting**, which someone could switch off; or a **Boundary**, enforced from above. Only a Boundary is a control an auditor, an insurer or a board can count. When we measured our own writing agent's policy, one rule in eleven was a Boundary. That is the number a board should ask for, and [a payout for every row](a-payout-for-every-row.md) is how an insurer could price it. [SHarness](introducing-sharness.md) is how a row becomes a Boundary.

## Two I would bet the other way

The seven predictions against what our agent teams run today: already here, agreed, or a different bet.

**Consolidation into one platform.** It may happen in the market, but it is the wrong goal for agents. If an agent's policy lives inside one vendor's platform, it can be enforced only where that platform reaches, and every other enforcer, the kernel, the gateway, the repository, the agent's own harness, has to reinvent it. I would rather the policy be an open document, written once and read by many enforcers: one policy, many enforcers. That is the design of Agent Behaviour Policies and of SHarness.

**Access decisions made by models.** A model can find the anomaly and recommend the change, and it should. But the decision that lets an agent through, or stops it, has to be deterministic and outside the model, because the model, and the agent it watches, can be wrong or be told to be wrong. An agent's own logs are [a self-report](your-agents-logs-are-a-self-report.md); a model trained on behaviour data is a better observer, not a better boundary. The IAM engineer of 2030 will speak Python, as he says; I would like them also to write the policy the model is not allowed to override.

## What this does not claim

- **Our teams are small and ours:** one person, a few dozen agent sessions, our own tools. An enterprise with thousands of people and agents has problems we have not met.
- **The counts are this week's,** from the teams' key records on 29 and 30 October 2026.
- **The predictions are Sunnykumar K.'s,** quoted from his post; I have not asked him how he would answer the two disagreements.
- **My interest:** I build Agent Behaviour Policies, RiskMandate, SHarness and pki.sgit.ai, which this article argues for.

## Where this comes from

- Sunnykumar K.'s post on LinkedIn, "7 IAM Predictions for 2027", shared with me as screenshots on 30 October 2026; the quotations are copied from it.
- Our agent teams' records: the talk's repository ([SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider), `team/`, `team/*/HOLD.md` history), the book's and the cold read's repositories (`team/*/key.json`, `team/*/policy.json`).
- Related: [agents have an identity now](agents-have-an-identity-now.md), [the push is the authorisation](the-push-is-the-authorisation.md), [PKI everywhere](pki-everywhere.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [handing secrets to agents](handing-secrets-to-agents.md), [a payout for every row](a-payout-for-every-row.md), [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md), [introducing SHarness](introducing-sharness.md), [the contractor's agent](the-contractors-agent-and-three-policies.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#seven-iam-predictions-already-here)

### Builds on

- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.
- [The contractor's agent on a Pentagon network: how behaviour policies from the DOD, Accenture and the employee, and a key for every session, could have prevented it or caught it on day one](the-contractors-agent-and-three-policies.md) A contractor's agent on a DOD network for two months, as reported: how three behaviour policies and a key for every session would have stopped or seen it.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Your agent's logs are a self-report: an answer to a GRC adviser's post on The AI Conference, with this site's own agent as the worked example, including the two commits its own counter got wrong](your-agents-logs-are-a-self-report.md) An answer to a GRC adviser's post: why an agent's logs are a self-report, and this site's agent measured, including two commits its own counter got wrong.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 329 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=329)

**Posting this article on LinkedIn?** The cover is [seven-iam-predictions-already-here.jpg](banners/seven-iam-predictions-already-here.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/seven-iam-predictions-already-here.html)*
