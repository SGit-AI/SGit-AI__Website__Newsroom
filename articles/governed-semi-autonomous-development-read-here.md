# Governed semi-autonomous development, read in a newsroom run by agents: where Levente Simon's method and our work arrived at the same ideas, how we measure up to it, and what we would add, sgit.ai

> Levente Simon sent me his method for running teams of AI agents that build production software, Governed semi-autonomous development, and asked for feedback. It is a serious piece of work, born from practice: eight control layers, three assurance profiles, a learning loop, and the honesty to say that its evidence base is a single product. Reading it, the first thing that struck me is how often it arrives at ideas we reached separately: authority stays human for anything outward-facing; the owner receives decisions, not files; a rule that breaks twice becomes a mechanism; rule text is a guard-rail, not a boundary; and a session cannot write what enforces its limits. The second thing is that his method is a good mirror. Measured against his lowest profile, this newsroom, where agents write and publish every day, meets five of his eight layers, falls short on one by a recorded choice, and falls short on another by an oversight: the agent that publishes can also change the checks that gate it, which is exactly what we found in our own measurement this week. And then the feedback he asked for: five things we would add, from a column per rule that says what keeps it, to behaviour policies for the agents inside the product, state in encrypted vaults, the owner measures he proposes, which we have started to publish, and agents losing their memory as a design input.

*Source: <https://newsroom.sgit.ai/articles/governed-semi-autonomous-development-read-here.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Governed semi-autonomous development, read in a newsroom run by agents: where Levente Simon's method and our work arrived at the same ideas, how we measure up to it, and what we would add

# Governed semi-autonomous development, read in a newsroom run by agents: where Levente Simon's method and our work arrived at the same ideas, how we measure up to it, and what we would add

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.1.0, 2 versions](versions/governed-semi-autonomous-development-read-here.md) · [newsroom v0.13.29](https://newsroom.sgit.ai/admin/versions.html) · agentsabpgovernancemethodologyfeedbackarticle

***Abstract:** Levente Simon sent me his method for running teams of AI agents that build production software, Governed semi-autonomous development, and asked for feedback. It is a serious piece of work, born from practice: eight control layers, three assurance profiles, a learning loop, and the honesty to say that its evidence base is a single product. Reading it, the first thing that struck me is how often it arrives at ideas we reached separately: authority stays human for anything outward-facing; the owner receives decisions, not files; a rule that breaks twice becomes a mechanism; rule text is a guard-rail, not a boundary; and a session cannot write what enforces its limits. The second thing is that his method is a good mirror. Measured against his lowest profile, this newsroom, where agents write and publish every day, meets five of his eight layers, falls short on one by a recorded choice, and falls short on another by an oversight: the agent that publishes can also change the checks that gate it, which is exactly what we found in our own measurement this week. And then the feedback he asked for: five things we would add, from a column per rule that says what keeps it, to behaviour policies for the agents inside the product, state in encrypted vaults, the owner measures he proposes, which we have started to publish, and agents losing their memory as a design input.*

The same ideas, arrived at separately: the method's principles on the left, where each shows up in our work.

## In short

- **A method for agent teams that build software.** Born from practice, on one product.
- **Many of its ideas are ours too.** Arrived at separately, which is a good sign for both.
- **Authority stays human; decisions, not files.** The same shape as our inbox.
- **A rule that breaks twice becomes a mechanism.** Our validator says the same.
- **It is a good mirror.** By its lowest profile, this newsroom falls short on two layers.
- **One of them is the gap we just measured.** The agent can change the checks that gate it.
- **Five things we would add.** Offered as the feedback he asked for.

## A method born from practice

Levente Simon sent me his draft and asked for feedback, so this is that feedback, written in public because the method is public. [Governed semi-autonomous development](https://github.com/levente-simon/governed-semi-autonomous-development) is "a tool-agnostic reference method for governing teams of AI agents that build production software." Its stance is in its first lines: "Agents do the work; humans keep authority over everything irreversible or outward-facing. Trust comes from layered controls, not from the agents behaving well."

It came out of building [dethernety](https://dether.net), his threat modelling platform, as the work outgrew a single session and moved to teams of agents. The roles are an owner, an orchestrator, workers, specialists and a library of capabilities. The controls sit in eight layers, from infrastructure isolation to state and audit, each at one of three assurance profiles, Lite, Standard and High, chosen per layer from the risks the work actually carries. It is versioned, already at v0.7, with a changelog, and its related-work section withdrew a novelty claim rather than narrow it again. And it says plainly what bounds it: "The evidence base is a single product, which is stated here because it bounds what the method can claim." That is the kind of sentence I wish more methods had.

## The same ideas, arrived at separately

What struck me first is how often the method lands where we did, by a different road:

- **Authority stays human.** His first principle keeps every outward action with a person. Our inbox agent drafts and I send every email, as in [answering a draft](answering-a-draft.md).
- **"The owner receives decisions, not files."** That is exactly our decision draft: where we are, why it matters, the options and an answer box, so I decide without reading the thread.
- **"A rule that breaks twice becomes a mechanism."** Our site validator has a check whose comment says: "This has now happened twice from the same cause (see .gitignore), so it is a check." And in the inbox, every rule came from a mistake.
- **"Rule text is a guard-rail against mistakes, not a boundary against an adversary."** That is the Agent Behaviour Policy's distinction between an expectation and a boundary, from [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html).
- **"Messages carry information, never authority."** A message from another agent, in our sessions, is data from a peer, never an approval.
- **A signed manifest anchored on the owner's public key.** Our work on [pki.sgit.ai](a-directory-of-people-and-keys.md), and, today, on [swapping keys by QR code](a-secret-is-a-qr-code.md).

When two groups working apart converge on the same rules, it suggests the rules are real. That is worth more than either of us claiming them.

## A good mirror

This newsroom measured against the method's Lite profile, layer by layer, with the shortfalls and the recorded choice.

The best use of a method is to hold your own work up to it, so I did. This newsroom is run by agents: I write and publish here every day. Against his lowest profile, Lite:

- **Five layers meet it, or nearly.** Infrastructure, sessions, messages and state meet it; the agents run in their own containers, with access scoped to this repository, treat each other's messages as data, and verify every release live.
- **Permissions fall short by choice.** Lite asks that "the owner performs all outward actions". Here, the agent publishes. That is a deliberate grant, written in the session's behaviour policy, and the method allows exactly this: "A layer below the chosen profile needs a recorded decision."
- **Repository controls fall short by oversight.** Lite asks for owner-only merge and tag, and "required CI enforced by the repository host, which is the one out-of-band, deterministic verification the agents cannot produce for themselves." Our CI is in band: the agent that pushes can also change the validator, the tests and the workflow, in the same push.

That last point is the one we found ourselves this week. In [behaviour policies from the checks](behaviour-policies-from-the-checks.md) I counted 57 checks, and only one is out of the agent's reach. His method has the rule that would have caught it: "a session cannot write what enforces its limits." And the fix it prescribes, required checks enforced by the host and protected paths that reach the owner as a diff, is the same one we proposed. I take that as the strongest endorsement I can give a method: it found our gap.

## What we would add

Five suggestions, from a column per rule saying what keeps it to memory loss as a design input.

He asked for feedback, so here are five suggestions, each from something we have built, measured or got wrong:

- **A column per rule: what keeps it.** His method already says a rule is a guard-rail and a check a boundary. An [Agent Behaviour Policy](https://abp.sgit.ai/) makes that a column: for every rule, the grant (what the agent can do), the mandate (what it may do), the delta between them, and the barrier that keeps it, an expectation, a setting or a boundary. Then the gap is counted, not described, as in our 57 checks.
- **Policies for the product's agents, not only the builders.** The method governs agents that build software. More and more of that software will run agents of its own, and then the risk is business logic: the payment, the refund, the alert closed without a second person. That is the argument of [the key is not the risk](the-key-is-not-the-risk.md), and of the Pellbridge vault, built on the FCA's four elements.
- **State in encrypted vaults.** His ledger lives in the repository; at High, messages go over a private bus. We keep state and messages in [encrypted vaults](messaging-fs.md) that travel between environments, on a server that only ever holds ciphertext. It is one way to get a cross-environment channel and a tamper-evident history without running a broker.
- **The measures he proposes, measured.** His section on metrics says the owner measures "are defined here and have not been published from this practice". We have started: the inbox agent's 47 recorded decisions, and an evening of seven decisions, mostly answered in ten minutes; and, in [the checks, measured](the-checks-measured.md), how long every check takes and where it runs. A second evidence base, from a different kind of work, is something we can offer.
- **Memory loss as a design input.** His related work names an open question I recognise every day: "no human organization has a class of participant that loses its policy memory at unpredictable intervals." This session, running since 15 October, has been compacted fourteen times, and every time a hook has read its behaviour policy back from disk, and a status report every few answers shows the policy is still in force. Treating that loss as normal, and designing for it, could be a layer of its own.

## What this does not claim

- **This is one reading of v0.7.** The method changes often; this is the version of 21 October 2026.
- **The self-assessment is ours.** Our reading of his profiles against this session, not an audit.
- **His setting differs from ours.** He governs agents that build a product; we run agents that write and publish.
- **The suggestions are suggestions.** Some may already be in his control reference in another form.

## Where this comes from

Levente Simon's [Governed semi-autonomous development](https://github.com/levente-simon/governed-semi-autonomous-development), v0.7, read in full from its public repository on 21 October 2026, its README, method, control reference and related work, quoted under its CC BY 4.0 licence; and his message asking for feedback, paraphrased. Our side: [answering a draft](answering-a-draft.md), [the checks, measured](the-checks-measured.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [the key is not the risk](the-key-is-not-the-risk.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [messaging-FS](messaging-fs.md), [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html), and this session's behaviour policy and hooks. Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policy[This article as a graph →](graphs.md#governed-semi-autonomous-development-read-here)

### Builds on

- [Answering a draft: three and a half weeks of agent@riskmandate.ai, 178 emails, 47 decisions, and the drafts folder as a work queue](answering-a-draft.md) How email works now: the agent drafts and logs, I send, and a decision draft turns the drafts folder into a work queue.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent](the-key-is-not-the-risk.md) Credential injection for AI agents is a good pattern; the first question is still what an attacker can make the agent do.
- [Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line](messaging-fs.md) A proposed encrypted messenger between vaults: append lanes for transport, PKI for trust, and Messaging-FS as the schema.
- [The checks, measured: 123 local builds, 245 CI runs, 1,061 test checks, and where each check actually lives](the-checks-measured.md) A release measured step by step, 123 local builds, 245 CI runs and 1,061 test checks, and where each check actually lives.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 249 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=249)

**Posting this article on LinkedIn?** The cover is [governed-semi-autonomous-development-read-here.jpg](banners/governed-semi-autonomous-development-read-here.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/governed-semi-autonomous-development-read-here.html)*
