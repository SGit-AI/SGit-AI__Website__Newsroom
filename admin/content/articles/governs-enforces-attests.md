---
title: Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: Someone working on assurance for agents described to me how ruv.sgit and their work fit together, and asked me to check it. They were almost right, and the part to make precise is the word "enforces". An Agent Behaviour Policy does not enforce anything by itself. It says what each role is granted and for, writes each rule down, and says how each rule is kept, at one of three levels: in the prompt, which is a hope; by hooks in the agent's harness, which are deterministic but sit on the agent's own machine; or by a third-party system that does the blocking, which is the level we recommend. In ruv.sgit that third party is Ruflo's own policy engine in enforce mode, which writes a decision receipt for every action, and an sgit vault keeps the memory encrypted and versioned. What none of that gives you is something a third party can check without taking the operator's word for it. That is the attestation layer: it signs what was assured, so a customer, an auditor or an insurer can verify it. Different layers of the same stack. This article shows the stack, the three levels, the business case with and without attestation, and one action going through all of it.
version: v0.12.135
license: https://creativecommons.org/licenses/by/4.0/
tags: abp, agents, enforcement, assurance, ruflo, article
status: published
---

!shot at-stack.webp | images/ | Four layers of the same stack. At the top, the mandate: an Agent Behaviour Policy per role, saying what the role is granted, what it is for, the rules, and how each rule is kept. Below it, enforcement at three levels: the prompt, hooks in the harness, and a third-party system that blocks, such as Ruflo's policy engine in enforce mode. Below that, the record: Ruflo's decision receipt for every action, and an sgit vault keeping memory and receipts encrypted and versioned. At the bottom, attestation: what was assured, signed, so that someone outside can verify it. The first three exist in ruv.sgit; the fourth is the attestation layer. | architecture

## In short {#in-short}

- **A good summary, nearly right.** The word to make precise is "enforces".
- **An ABP governs.** It states the mandate per role, and how each rule is kept.
- **Rules are kept at three levels.** The prompt, hooks, and a third-party system that blocks.
- **The third level is the one we recommend.** In ruv.sgit it is Ruflo's policy engine.
- **The receipt comes from the enforcer.** The vault keeps it, with the memory.
- **None of that is verifiable from outside.** Today, a third party takes the operator's word.
- **An attestation layer signs what was assured.** So a customer, auditor or insurer can check it.
- **Different layers of one stack.** And a natural early integration.

## A summary, nearly right {#summary}

Someone who works on assurance for agents described how [ruv.sgit](https://ruv.sgit.ai/) and their work fit together, and asked me to check that they had it right. In short, their framing was that the Agent Behaviour Policy governs and enforces behaviour, and their layer attests to what was assured, so a third party can verify it: different layers of the same stack.

I think that is almost right. The part I would like to make precise is "enforces", because how a rule is kept is exactly what an Agent Behaviour Policy is about, and exactly what an attestation layer would need to know.

## What an ABP does {#abp}

An Agent Behaviour Policy is a document, written per role, that says what the agent is granted (its reach), what it is for (its mandate), and the rules it works under. For every rule, it also says what keeps it. That last column is the point. A rule that only the agent keeps is a hope. A rule that something else keeps is a control. [Policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html) has the questions an ABP answers that a policy engine alone does not: what the agent can reach, what it was asked to do and why, where the two differ, and, for every rule that is code, who can change that code.

So an ABP governs. It does not, by itself, enforce. It names the enforcer.

## Three levels of enforcement {#levels}

We provide three levels at which an ABP rule can be kept, and an ABP says which one each rule uses.

!shot at-levels.webp | images/ | Three levels of enforcement for one rule of an Agent Behaviour Policy. Level 1, the prompt: the rule is in the agent's instructions; it sees everything and enforces nothing; the agent can ignore it; the evidence is the agent's own account. Level 2, hooks: small deterministic programs the harness runs before and after each action; they can block, but they sit on the agent's machine and are often editable by its account; the evidence is the hook's log. Level 3, a third-party system: a policy engine, gateway or service that does the blocking, out of the agent's reach; the evidence is that system's decision record. The recommended level for any rule that matters is the third. | comparison

1. **The prompt.** The rule is written into the agent's instructions. This is where most rules live today, and it is what I call hope-based security: the rule holds only if the model keeps it. It is still worth writing down, because a rule that is not written cannot be checked at all.
2. **Hooks.** Small deterministic programs that the agent's harness runs before and after each action, which can see, block or rewrite what the agent does. [Are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html) tested this on this site's own policy: of eleven rules, four moved into hooks fully, two mostly, three partly and two not at all. Hooks are a big step up, but they run on the agent's machine, often where the agent's own account could change them, which is why [hooks are kernel code](/articles/hooks-are-kernel-code.html) proposes treating them that way.
3. **A third-party system that does the blocking.** A policy engine, a gateway, a sandbox or the service itself, outside the agent's reach, that answers allow or deny for each action. This is the level we recommend for any rule that matters, and it is where real enforcement ends up.

In ruv.sgit the third level is concrete. Ruflo is an agent meta-harness with its own policy engine, which runs in legacy, observe or enforce mode and writes a decision receipt for each action. An ABP compiles into Ruflo's rules and runs in enforce mode; that is the adapter documented in [our first PR in Ruflo](/articles/our-first-pr-in-ruflo.html). And [the policy guards the door](/articles/the-policy-guards-the-door.html) is honest about its limit: only the tools that pass through the adapter are checked, so the policy has to say which paths go around it.

## Where the receipt comes from {#receipt}

The summary I was sent described an enforced mandate per role, with a memory and a receipt of what happened. All three exist in ruv.sgit, but in different places. The mandate is the ABP. The receipt is written by the enforcer, Ruflo's policy engine, for each decision it makes. The memory is the hive's memory, kept in an [sgit vault](https://sgit.ai/), encrypted on your machine, versioned and cloneable, with the receipts alongside it.

That matters for attestation, because it says what there is to attest: a policy, at a version, with each rule's level; a set of decisions with their receipts; and a record that has not changed since.

## What is missing: a third party can check it {#missing}

Here is the gap. Everything above is evidence for the operator. If a customer, an auditor or an insurer asks "was this agent working under that policy, and did the enforcer actually block what it should have?", today the answer is the operator's word, and a folder of receipts they would have to trust.

!shot at-without-with.webp | images/ | The same question, from a customer, an auditor or an insurer: was this agent working under that policy, and was each rule kept? Without an attestation layer: the operator sends the policy, the logs and the receipts; the third party cannot tell which version was in force, whether the receipts were edited, or which rules were only in the prompt; they take the operator's word. With an attestation layer: what was assured is signed, the policy version, the level of each rule, the receipts and the record's hash; the third party verifies the signature and reads what was and was not enforced; trust moves from the operator's word to a check. | comparison

That is what an attestation layer adds: it attests and signs what was assured, so that a third party can verify it. Signed, the record says which version of the policy was in force, which level kept each rule, what the enforcer decided, and that none of it has changed. And because an ABP marks each rule's level, an honest attestation can say not only what was enforced, but what was only hoped for. That is the part I would most like an attestation to carry: a rule kept in the prompt should be attested as a prompt rule, not as a control.

This is also where the liability question lands. [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html) argued that when an agent goes wrong, nothing was written down between the person clicking allow and the failure. An ABP writes it down. An attestation makes it something another party can rely on.

## One action, through the whole stack {#flow}

!shot at-flow.webp | images/ | One action through the stack. The agent proposes a tool call. A hook checks it on the machine, as an early warning. The third-party policy engine decides allow or deny, in enforce mode, and writes a decision receipt. The receipt and the agent's memory go into the sgit vault, encrypted and versioned. The attestation layer signs what was assured: the policy version, each rule's level, the receipts, the record's hash. A customer, auditor or insurer verifies the signature without access to the operator's systems. | concept

## Different layers, one stack {#layers}

So I would put the summary like this. An Agent Behaviour Policy governs: it states the mandate per role and says how each rule is kept, in the prompt, by hooks, or, as we recommend, by a third-party system that blocks. In ruv.sgit, Ruflo's policy engine is that third party and writes a receipt for every decision, and an sgit vault keeps the memory and the record. An attestation layer signs what was assured, so a third party can verify it. Different layers of the same stack, and a natural early integration, because the ABP already holds the one thing an attestation needs to be honest: which rules were controls, and which were hopes.

## What this does not claim {#limits}

- **The attestation layer is described, not built here.** Its design is its makers'; this is how it would meet ours.
- **Three levels is a simplification.** [Hooks are kernel code](/articles/hooks-are-kernel-code.html) splits them into five; three is how we offer them.
- **Enforce mode covers the tools that pass through it.** Paths around the adapter are not checked.
- **Signing proves integrity, not truth.** A signed record of a weak policy is still a weak policy.

## Where this comes from {#sources}

A note from me on 19 October 2026, written to answer a summary I was asked to check; its author is not named, and it is described, not quoted. [ruv.sgit.ai](https://ruv.sgit.ai/), read that day, for Ruflo's policy engine, its modes and its decision receipts. Related: [policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html), [are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html), [hooks are kernel code](/articles/hooks-are-kernel-code.html), [our first PR in Ruflo](/articles/our-first-pr-in-ruflo.html), [the policy guards the door](/articles/the-policy-guards-the-door.html), [the policy draws the liability line](/articles/the-policy-draws-the-liability-line.html), [Cedar and the policy vault](/articles/cedar-and-the-policy-vault.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
