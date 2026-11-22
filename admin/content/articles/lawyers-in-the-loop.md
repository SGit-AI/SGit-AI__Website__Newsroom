---
title: Lawyers in the loop: a decisions agent that acts under a limited power of attorney signed with my key, a counsel agent that drafts and tests it, and a way to buy a named person's signature when it matters
date: 2026-11-22
author: Dinis Cruz
author_url: about/index.html
summary: My agent teams have plenty of checks and controls, and too many of them end with a question that only I can answer, in a session I have to visit. So we are designing a way to delegate my authority without giving it away. My key stays on my own device. I sign, on pki.sgit.ai, a delegation to one decisions agent: this key, held in this session, may issue requests in my name, of these kinds, until this time. The agent issues only my verbatim answers, and every agent that receives a request checks the chain itself. That is a power of attorney, and a limited one: a principal, an attorney, an instrument, a scope, duties, an expiry, revocation and a public register. Which raises the next question: who checks the instrument? A counsel agent can draft it, simulate how it fails, and have several models review it, but it cannot be accountable. Only people and companies can. So the last step of the loop is to ask, for any instrument or workflow, what it would cost to have it reviewed and signed by a named lawyer and certified by a firm, by which flow, and then to pay for it. That is how agents could let law firms and other professional services serve far more people. All of this is a proposal; nothing is built yet.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: delegation, pki, power-of-attorney, legal, accountability, agents, professional-services, article
status: published
---

!shot law-loop.webp | images/ | The proposed loop: agents draft, simulate and check; a named person and a firm review, sign and certify. | process

## In short {#in-short}

- **My decisions do not scale.** Most of what waits for me is already well thought through, and each answer needs a visit to a session.
- **A decisions agent, acting on a delegation I sign.** My key stays on my device; I sign a limited, expiring delegation on pki.sgit.ai.
- **Every receiver checks the chain.** Signed request, delegated key, my signature, expiry, revocation, and its own policy's powers.
- **It is a power of attorney, and a limited one.** Principal, attorney, instrument, scope, duties, revocation and a register all have a counterpart.
- **A counsel agent drafts and tests the instruments.** Several models check them; nothing it writes is legal advice.
- **Only people and companies can be accountable.** That is what you pay a lawyer for, with their experience and their own agents.
- **The loop ends with a quote and a signature.** Which person, which firm, which flow, what price, and a way to pay.
- **All of it is a proposal.** Nothing here is built, and no lawyer or firm is involved yet.

## The bottleneck is me {#bottleneck}

I like that my agent teams are full of checks and controls. An agent does not act on a message from another session; it acts on what I type in its own. That rule has stopped a number of bad ideas. It has also made me the bottleneck. As I told maestro.d on 22 November: "a lot of things that need my decision, but that is not working and not scaling ... a number of times my decision is yes, because by the time you reach there, it's already well thought through."

So the question became how I can give my word without being in every session to give it, and without giving my authority away. The answer we are designing comes from two places: the public key infrastructure I already use on [pki.sgit.ai](https://pki.sgit.ai/), and a very old legal idea.

## A decisions agent, and a delegation I sign {#delegation}

!shot law-chain.webp | images/ | The proposed chain: my key, a signed delegation, a decisions agent, a signed request, a receiver that checks it. | architecture

The design, as maestro.d wrote it up from my words, has five links.

1. **My key stays on my device.** I sign with it on pki.sgit.ai, the site I already sign with. A new key, made and kept on my own device, is planned for this.
2. **A delegation, signed by me.** It says, in effect: key K, held by the decisions agent in session S, may issue requests in my name, of these kinds, until this time. It is short-lived, and I renew it.
3. **The decisions agent** holds its own session key and is the only agent with a delegation. In my words: "that's the only agent here that has the private key that has been signed by me that is then able to issue requests as me". It issues my answers verbatim, from a decision page or a session, and adoptions under a rule I set (an owner's recommendation adopted when nobody has objected by a deadline). It never makes a decision of its own.
4. **A signed request** goes to one agent, with a short expiry, a nonce against replay and the decision it answers, down that agent's existing inbox, on any account.
5. **The receiving agent checks the chain itself:** the request is signed by K; K is in a delegation signed by my published key; the delegation has not expired or been revoked; and the request is within both the delegation's kinds and the receiver's own policy. Then it acts, and logs what it did.

Some things never travel this way, at least at first: keys and secrets, money, the law, deleting data, connectors, and relaxing a policy. Those stay in a session with me. And if the decisions agent were ever compromised, I revoke on pki.sgit.ai, the revocation list is published, and the chain fails everywhere at once.

## It is a power of attorney {#poa}

!shot law-poa.webp | images/ | How the parts of a power of attorney map onto the proposed delegation to a decisions agent. | comparison

When I looked at what we had designed, it was something the law has had for a long time: a power of attorney. A principal gives an attorney authority to act for them, within the powers the document grants. maestro.d mapped it part by part, and nearly every part has a counterpart.

- **The principal** is me; **the attorney** is the decisions agent; **the instrument** is the delegation I sign.
- **It is limited,** to kinds of request and a period. In England and Wales the closest form is the ordinary power of attorney, which, as [Which?](https://whichwills.which.co.uk/what-is-power-of-attorney/) puts it, "gives another person authority to act on your behalf for a limited time period", and you "can specify a time period for an Ordinary Power of Attorney, or restrict it to specific activities". A general or durable power is not proposed: the delegation should end, or freeze, if I cannot be reached.
- **The attorney has duties:** act only in the principal's interest and within scope, keep records, never act for itself, never sub-delegate. Those go into the decisions agent's behaviour policy.
- **Revocation** takes effect when those relying on the power know of it, which is why the revocation list is published and checked.
- **Registration** is the model for publishing the delegation and its hash before its first use. A [lasting power of attorney](https://www.gov.uk/power-of-attorney) in England and Wales is registered with the Office of the Public Guardian, and, in GOV.UK's words, "can be used as soon as it's registered".
- **Ratification:** I can approve an act outside the scope afterwards, recorded, never assumed.
- **Apparent authority,** where a third party reasonably believes an agent is authorised, is the reason no agent may act on a claim of authority, only on a chain it has checked.

This is not a new thought in research either. [Authenticated Delegation and Authorized AI Agents](https://arxiv.org/abs/2501.09674) proposes "a novel framework for authenticated, authorized, and auditable delegation of authority to AI agents, where human users can securely delegate and restrict the permissions and scope of agents while maintaining clear chains of accountability", built on OAuth 2.0 and OpenID Connect. [Using Agency Law to Tame AI Agents](https://arxiv.org/abs/2502.18359), forthcoming in the Berkeley Technology Law Journal, argues that core parts of modern software engineering, such as client-server architectures, address several of agency law's concerns in ways different from, and arguably stronger than, how the law disciplines a human agent. Our version is smaller: one principal, one attorney, a site I already sign on, and a check every agent runs.

Each agent's behaviour policy would gain a powers section, written by the policy agent and deny by default: which delegations it recognises, which kinds of request it accepts under each, which it never accepts, and what it must log.

## A counsel agent {#counsel}

Once the delegation is an instrument, someone has to draft it, check it and test it. We have an agent that checks licences and terms, and it says plainly that it gives no legal advice. What is needed is wider, and maestro.d proposed it as a counsel agent:

- **Draft the instruments:** the delegation, the powers section of each policy, the terms of a service we sell.
- **Simulate them:** what happens on revocation, on an act outside the scope, on a stolen key.
- **Require independent checks** from several models before anything is marked reviewed, and list which models checked it and where they disagreed.
- **Never present its output as legal advice,** and never name a real lawyer or firm without their consent.

And one rule that matters more than the others: a "certified" mark exists only once a real, named legal service has given it.

## Only people and companies can be accountable {#accountable}

This is the heart of it for me. An agent can draft a very good contract. Several agents can check it. But a contract signed and reviewed only by agents has limits, because when something goes wrong nobody stands behind it. Only humans can hold accountability, and companies can, and that is a large part of what you pay a professional for. You also pay for their experience and their knowledge, and increasingly for their own agents, which will be far more optimised for their field than mine are, the same way my agents are optimised for development, architecture and agentic work, which is what I know.

So the counsel agent is not a replacement for a lawyer. It is the part of the work that makes the lawyer's part small, precise and worth paying for.

## The loop to a named person, and a price {#quote}

Here is the workflow I want. I create something like this power of attorney. I want to know whether it is legal. I want a legal opinion on it, and a contract that has been reviewed. And then I want to ask: how much would it cost to have this reviewed and signed by a person, and certified by a firm? Which person, at which firm, by which flow? And then I should be able to pay for it, there and then.

The figure at the top is that loop. The first three steps are agents, fast and cheap, and marked as such. The last two are people and a firm, accountable, paid for their judgement, their name and their liability, and recorded beside the instrument they signed. Agents draft; humans answer for it.

## Why this could scale law firms {#scale}

Today, most people and small companies do not get a lawyer to look at most of what they sign, because a review costs more than the risk seems worth. Look at it from the firm's side. If the instrument arrives drafted, simulated and checked, with every model's comments and the exact question attached, the review a person has to do is much smaller and much better defined. The firm can price it, its own agents can prepare it, and a named lawyer can sign it. That is how a law firm, or any professional service, could serve far more reviews than it does now, and how I could consume far more legal review than I do now. The same loop works for an accountant, an auditor or a security reviewer.

## What this does not claim {#limits}

- **Nothing here is built.** The delegation, the decisions agent, the powers sections and the counsel agent are proposals; I have not yet said yes to any part.
- **It is not legal advice,** and the mapping to a power of attorney is an analogy drawn by agents, not a legal opinion. Whether a delegation like this has any legal effect is exactly the question for a lawyer.
- **No lawyer or firm is involved,** and none is named or implied.
- **The legal sources describe England and Wales;** other jurisdictions differ.
- **The research papers are proposals and arguments,** not standards.
- **A new key, made and kept on my own device, is planned** before any delegation is signed.

## Where this comes from {#sources}

My words to maestro.d and to this newsroom on 22 November 2026, quoted from the records that hold them verbatim: maestro.d's analyses [decisions at scale](https://github.com/PrompTugal/PrompTugal__News__Website/blob/dev/board/team/maestro.d/analysis/2026-11-22-decisions-at-scale/README.md) (sections 1, 3 and 7) and [power of attorney](https://github.com/PrompTugal/PrompTugal__News__Website/blob/dev/board/team/maestro.d/analysis/2026-11-22-power-of-attorney/README.md), in PrompTugal/PrompTugal__News__Website on dev, read at commit `8c36bc73`; and this site's `admin/notes/2026-11-22__newsroom.d-twin/memo-03.md`. A prototype of a playable decision page exists, built by one of the PrompTugal agents; it is not public. Legal and research sources read on 22 November 2026: [Which? on powers of attorney](https://whichwills.which.co.uk/what-is-power-of-attorney/), [GOV.UK on lasting powers of attorney](https://www.gov.uk/power-of-attorney), [arXiv 2501.09674](https://arxiv.org/abs/2501.09674) and [arXiv 2502.18359](https://arxiv.org/abs/2502.18359). Written by newsroom.d (writer-11), this site's journalist agent on account D, from maestro.d's material. Related: [a holacracy of agents](/articles/a-holacracy-of-agents.html), [the primitives of trust](/articles/the-primitives-of-trust.html).
