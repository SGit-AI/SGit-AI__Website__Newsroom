# Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs, sgit.ai

> Someone working on assurance for agents described to me how ruv.sgit and their work fit together, and asked me to check it. They were almost right, and the part to make precise is the word "enforces". An Agent Behaviour Policy does not enforce anything by itself. It says what each role is granted and for, writes each rule down, and says how each rule is kept, at one of three levels: in the prompt, which is a hope; by hooks in the agent's harness, which are deterministic but sit on the agent's own machine; or by a third-party system that does the blocking, which is the level we recommend. In ruv.sgit that third party is Ruflo's own policy engine in enforce mode, which writes a decision receipt for every action, and an sgit vault keeps the memory encrypted and versioned. What none of that gives you is something a third party can check without taking the operator's word for it. That is the attestation layer: it signs what was assured, so a customer, an auditor or an insurer can verify it. Different layers of the same stack. This article shows the stack, the three levels, the business case with and without attestation, and one action going through all of it.

*Source: <https://newsroom.sgit.ai/articles/governs-enforces-attests.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs

# Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-19 · [article v1.2.0, 3 versions](versions/governs-enforces-attests.md) · [newsroom v0.12.135](https://newsroom.sgit.ai/admin/versions.html) · abpagentsenforcementassurancerufloarticle

***Abstract:** Someone working on assurance for agents described to me how ruv.sgit and their work fit together, and asked me to check it. They were almost right, and the part to make precise is the word "enforces". An Agent Behaviour Policy does not enforce anything by itself. It says what each role is granted and for, writes each rule down, and says how each rule is kept, at one of three levels: in the prompt, which is a hope; by hooks in the agent's harness, which are deterministic but sit on the agent's own machine; or by a third-party system that does the blocking, which is the level we recommend. In ruv.sgit that third party is Ruflo's own policy engine in enforce mode, which writes a decision receipt for every action, and an sgit vault keeps the memory encrypted and versioned. What none of that gives you is something a third party can check without taking the operator's word for it. That is the attestation layer: it signs what was assured, so a customer, an auditor or an insurer can verify it. Different layers of the same stack. This article shows the stack, the three levels, the business case with and without attestation, and one action going through all of it.*

Four layers of the same stack: the mandate, enforcement, the record and attestation.

## In short

- **A good summary, nearly right.** The word to make precise is "enforces".
- **An ABP governs.** It states the mandate per role, and how each rule is kept.
- **Rules are kept at three levels.** The prompt, hooks, and a third-party system that blocks.
- **The third level is the one we recommend.** In ruv.sgit it is Ruflo's policy engine.
- **The receipt comes from the enforcer.** The vault keeps it, with the memory.
- **None of that is verifiable from outside.** Today, a third party takes the operator's word.
- **An attestation layer signs what was assured.** So a customer, auditor or insurer can check it.
- **Different layers of one stack.** And a natural early integration.

## A summary, nearly right

Someone who works on assurance for agents described how [ruv.sgit](https://ruv.sgit.ai/) and their work fit together, and asked me to check that they had it right. In short, their framing was that the Agent Behaviour Policy governs and enforces behaviour, and their layer attests to what was assured, so a third party can verify it: different layers of the same stack.

I think that is almost right. The part I would like to make precise is "enforces", because how a rule is kept is exactly what an Agent Behaviour Policy is about, and exactly what an attestation layer would need to know.

## What an ABP does

An Agent Behaviour Policy is a document, written per role, that says what the agent is granted (its reach), what it is for (its mandate), and the rules it works under. For every rule, it also says what keeps it. That last column is the point. A rule that only the agent keeps is a hope. A rule that something else keeps is a control. [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) has the questions an ABP answers that a policy engine alone does not: what the agent can reach, what it was asked to do and why, where the two differ, and, for every rule that is code, who can change that code.

So an ABP governs. It does not, by itself, enforce. It names the enforcer.

## Three levels of enforcement

We provide three levels at which an ABP rule can be kept, and an ABP says which one each rule uses.

Three levels of enforcement for one rule of an Agent Behaviour Policy: the prompt, hooks and a third-party system.

1. **The prompt.** The rule is written into the agent's instructions. This is where most rules live today, and it is what I call hope-based security: the rule holds only if the model keeps it. It is still worth writing down, because a rule that is not written cannot be checked at all.
2. **Hooks.** Small deterministic programs that the agent's harness runs before and after each action, which can see, block or rewrite what the agent does. [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md) tested this on this site's own policy: of eleven rules, four moved into hooks fully, two mostly, three partly and two not at all. Hooks are a big step up, but they run on the agent's machine, often where the agent's own account could change them, which is why [hooks are kernel code](hooks-are-kernel-code.md) proposes treating them that way.
3. **A third-party system that does the blocking.** A policy engine, a gateway, a sandbox or the service itself, outside the agent's reach, that answers allow or deny for each action. This is the level we recommend for any rule that matters, and it is where real enforcement ends up.

In ruv.sgit the third level is concrete. Ruflo is an agent meta-harness with its own policy engine, which runs in legacy, observe or enforce mode and writes a decision receipt for each action. An ABP compiles into Ruflo's rules and runs in enforce mode; that is the adapter documented in [our first PR in Ruflo](our-first-pr-in-ruflo.md). And [the policy guards the door](the-policy-guards-the-door.md) is honest about its limit: only the tools that pass through the adapter are checked, so the policy has to say which paths go around it.

## Where the receipt comes from

The summary I was sent described an enforced mandate per role, with a memory and a receipt of what happened. All three exist in ruv.sgit, but in different places. The mandate is the ABP. The receipt is written by the enforcer, Ruflo's policy engine, for each decision it makes. The memory is the hive's memory, kept in an [sgit vault](https://sgit.ai/), encrypted on your machine, versioned and cloneable, with the receipts alongside it.

That matters for attestation, because it says what there is to attest: a policy, at a version, with each rule's level; a set of decisions with their receipts; and a record that has not changed since.

## What is missing: a third party can check it

Here is the gap. Everything above is evidence for the operator. If a customer, an auditor or an insurer asks "was this agent working under that policy, and did the enforcer actually block what it should have?", today the answer is the operator's word, and a folder of receipts they would have to trust.

The same question from a customer, an auditor or an insurer, answered without and with an attestation layer.

That is what an attestation layer adds: it attests and signs what was assured, so that a third party can verify it. Signed, the record says which version of the policy was in force, which level kept each rule, what the enforcer decided, and that none of it has changed. And because an ABP marks each rule's level, an honest attestation can say not only what was enforced, but what was only hoped for. That is the part I would most like an attestation to carry: a rule kept in the prompt should be attested as a prompt rule, not as a control.

This is also where the liability question lands. [The policy draws the liability line](the-policy-draws-the-liability-line.md) argued that when an agent goes wrong, nothing was written down between the person clicking allow and the failure. An ABP writes it down. An attestation makes it something another party can rely on.

## One action, through the whole stack

One action through the stack, from the agent's tool call to the signed attestation a customer can verify.

## Different layers, one stack

So I would put the summary like this. An Agent Behaviour Policy governs: it states the mandate per role and says how each rule is kept, in the prompt, by hooks, or, as we recommend, by a third-party system that blocks. In ruv.sgit, Ruflo's policy engine is that third party and writes a receipt for every decision, and an sgit vault keeps the memory and the record. An attestation layer signs what was assured, so a third party can verify it. Different layers of the same stack, and a natural early integration, because the ABP already holds the one thing an attestation needs to be honest: which rules were controls, and which were hopes.

## What this does not claim

- **The attestation layer is described, not built here.** Its design is its makers'; this is how it would meet ours.
- **Three levels is a simplification.** [Hooks are kernel code](hooks-are-kernel-code.md) splits them into five; three is how we offer them.
- **Enforce mode covers the tools that pass through it.** Paths around the adapter are not checked.
- **Signing proves integrity, not truth.** A signed record of a weak policy is still a weak policy.

## Where this comes from

A note from me on 19 October 2026, written to answer a summary I was asked to check; its author is not named, and it is described, not quoted. [ruv.sgit.ai](https://ruv.sgit.ai/), read that day, for Ruflo's policy engine, its modes and its decision receipts. Related: [policy as code needs a policy first](policy-as-code-needs-a-policy-first.md), [are hooks the sweet spot?](are-hooks-the-sweet-spot.md), [hooks are kernel code](hooks-are-kernel-code.md), [our first PR in Ruflo](our-first-pr-in-ruflo.md), [the policy guards the door](the-policy-guards-the-door.md), [the policy draws the liability line](the-policy-draws-the-liability-line.md), [Cedar and the policy vault](cedar-and-the-policy-vault.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policy[This article as a graph →](graphs.md#governs-enforces-attests)

### Builds on

- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there](our-first-pr-in-ruflo.md) rUv merged Mondweep's pull request #4239: one docs page, the first commit on Ruflo's main branch to mention SGit or an ABP. The four pieces, shown.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP](cedar-and-the-policy-vault.md) Cedar is mature and adopted; it lacks the why, the version in force and the evidence. A vault carries all three, and the demo shows it working.

### Continued by

- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in](a-trusted-framework-for-agentic-finance.md) The FCA plans a framework for agentic finance. Our open behaviour policies cover its four elements; a vault shows six bank agents at play.
- [Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open](ten-questions-one-graph.md) Phil Venables' ten questions for a CISO's tool are graph questions. Risk acceptance is half the answer; a twin in a vault answers all ten.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 214 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=214)

**Posting this article on LinkedIn?** The cover is [governs-enforces-attests.jpg](banners/governs-enforces-attests.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/governs-enforces-attests.html)*
