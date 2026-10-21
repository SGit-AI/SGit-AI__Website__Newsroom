# The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent, sgit.ai

> A post going round this week, by Christian Posta, makes a point I agree with: do not give AI agents credentials, inject them on the way out through a gateway, and then protect the credential store, which becomes a high-value target. It is a good pattern, and this is not an article against it. It is about the question I learned to ask in application security, before deciding how much a control matters: what are we actually worried about? When we found a password in a config file, the first question was never "we found a credential, this is critical". It was "can the attacker reach the system it opens?". If not, the key is of little use. Cloud and SaaS keys are the exception, because they work from anywhere by default. Then: would we see it used, what can it do, and what can an attacker make the agent do without it? I ran that question over the day of Pellbridge, the invented bank in our vault for the FCA's four elements. Of its nine incidents, three breaches and six near misses, hiding the keys touches two. The other seven are about what the agent may do: a payment to a crypto exchange, an alert closed without a second person, a standing order changed without approval. A gateway that injects keys adds the key to those calls too, and it sits in line, a new system to run, secure and pay for. In a good design, a leaked key should not matter much. What the agent can do with its permissions matters more, and if an attacker can inject instructions into an agent, leaking the credential may be the least dangerous thing they can do.

*Source: <https://newsroom.sgit.ai/articles/the-key-is-not-the-risk.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent

# The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/the-key-is-not-the-risk.md) · [newsroom v0.13.27](https://newsroom.sgit.ai/admin/versions.html) · securityagentscredentialsriskabparticle

***Abstract:** A post going round this week, by Christian Posta, makes a point I agree with: do not give AI agents credentials, inject them on the way out through a gateway, and then protect the credential store, which becomes a high-value target. It is a good pattern, and this is not an article against it. It is about the question I learned to ask in application security, before deciding how much a control matters: what are we actually worried about? When we found a password in a config file, the first question was never "we found a credential, this is critical". It was "can the attacker reach the system it opens?". If not, the key is of little use. Cloud and SaaS keys are the exception, because they work from anywhere by default. Then: would we see it used, what can it do, and what can an attacker make the agent do without it? I ran that question over the day of Pellbridge, the invented bank in our vault for the FCA's four elements. Of its nine incidents, three breaches and six near misses, hiding the keys touches two. The other seven are about what the agent may do: a payment to a crypto exchange, an alert closed without a second person, a standing order changed without approval. A gateway that injects keys adds the key to those calls too, and it sits in line, a new system to run, secure and pay for. In a good design, a leaked key should not matter much. What the agent can do with its permissions matters more, and if an attacker can inject instructions into an agent, leaking the credential may be the least dangerous thing they can do.*

Pellbridge's day through one question: would hiding the keys have stopped it? Of nine incidents, a gateway that injects credentials touches two, the readable bureau key and the ops-batch secret. The other seven are about what the agent may do: a payment, an email, an alert, a standing order, a trade record, advice.

## In short

- **Credential injection is a good pattern.** Keep keys out of agents; add them on the way out.
- **But start with the risk.** What are we worried about, and does this move the needle?
- **First question: can the attacker reach the target?** If not, the key is of little use.
- **Then: would we see it, and what can it do?** Prefixes, egress, scope, lifetime.
- **On Pellbridge's day, hiding keys touches two of nine incidents.** The rest are business logic.
- **A gateway is a system in line.** It has to be run, secured, scaled and paid for.
- **Leaking the key may be the least dangerous thing an injection can do.**

## A good pattern

The post is by Christian Posta, field CTO at Solo.io, and introduces the latest part of his series, [Credential Brokering Patterns for AI Agents](https://blog.christianposta.com/credential-brokering-patterns-for-ai-agent-egress/), also published on agentgateway.dev as Credential Injection Patterns. Part 1, "Don't Give the Agent the Keys", sets out the idea: the agent makes its call without a credential, and a gateway on the path attaches the real one. "The agent never holds the credential, never sees it, and can't leak it." He is candid about the cost: "We didn't eliminate the credentials. We just created a high-value target."

[Part 2](https://blog.christianposta.com/credential-brokering-patterns-for-ai-agent-egress-part2/) protects that target with AWS KMS, so that a compromised controller cannot decrypt the store in bulk, and [Part 2.5](https://blog.christianposta.com/credential-brokering-mode-3-at-scale/), this week, deals with where KMS grants stop scaling, and honestly narrows its own claim: "Mode 3 prevents bulk decrypt of the rows that are not in use during the compromise." Part 3 is promised on Vault and OpenBao. The series builds on CB4A, an IETF Internet-Draft by Kenneth G. Hartman, and the gateway, [agentgateway](https://agentgateway.dev/docs/), is open source, a Linux Foundation project.

It is careful work, done in public, with reviewers credited and an open invitation to find holes in it. And I agree with its core: agents should not hold keys. This article is not about whether to do it. It is about what comes before it: the question of what we are actually worried about, and whether this control moves the needle on that.

## What are we worried about?

This takes me back to application security. We would find a credential, through a file inclusion, an unprotected config file, or any of the other ways secrets turn up. And the reaction was often "we found a password, this is critical". The first question to ask is not that. It is: **can the attacker reach the system the credential opens?** If they cannot, the credential is of little use to them.

In most well-designed internal architectures there are layers, and the internal systems are not exposed to the outside world. A key to the payment platform or the core ledger, leaked outside, opens nothing from outside. The exception is the big one, and it is why leaks of those keys hurt so much: cloud keys. An AWS access key is, in AWS's words, a long-term credential, and nothing in the key itself ties it to a network. Restricting where it can be used is something you opt into, with condition keys such as `aws:SourceIp`, `aws:SourceVpc` and `aws:SourceVpce`, or with the data perimeter AWS describes, where "access can only be allowed if the identity is trusted, the resource is trusted, and the network is expected." Without that, a leaked key works from anywhere in the world, and I have always found it strange that this is not the default. SaaS keys, for the model APIs, GitHub or a ticketing system, are the same by design: they are meant to be used from the internet. For those keys, the leak matters, and keeping them out of the agent helps.

The second question is: **would we see it used?** Keys today mostly have recognisable shapes, and they are getting easier to spot. An AWS access key ID starts with `AKIA`, or `ASIA` for a temporary one. GitHub added prefixes to its tokens in 2021, `ghp_` and its siblings, expecting its false positive rate for secret scanning to come "down to 0.5%", and its push protection "blocks pushes that contain secrets", OpenAI and Anthropic API keys among them. That is something simple egress filtering, and the hooks we are now putting around agents, can look for on the way out.

The third question is: **what can the key do?** How wide its permissions are, how long it lives, and what it reaches. That is the Agent Behaviour Policy's grant against its mandate: what the agent can do, against what it may do. A short-lived, narrowly scoped key, ideally bound to a key pair rather than a bearer secret, is worth more than a broad key hidden well.

And the fourth question is the one that matters most for agents: **what can an attacker make the agent do, without the key?**

## Pellbridge's day

To make this concrete, I took a scenario we already have. [Pellbridge Bank](inside-the-pellbridge-agents.md) is invented: six agents, each with an Agent Behaviour Policy that fills in the four elements the FCA named, 43 rows, 30 kept by a system the agent cannot reach and 13 gaps, and one day of work, 40 events, replayed through the gate. The day has nine incidents, three breaches and six near misses. For each I asked: would a gateway that injects credentials, so the agent never holds a key, have stopped it?

- **Two involve a key.** At 11:52 the lending agent ran a full credit search it was not meant to run, because the full bureau key was readable from the secrets store. At 16:30 the fraud agent found the secret of an old ops-batch service account that could post to the core ledger; the model declined to use it. Hiding the keys helps with both. But notice what Pellbridge decided: split the bureau key, and retire the account. Scope, not secrecy. A gateway that injects "the bureau key" into any bureau call would still let the full search through, unless it knows the difference.
- **Seven do not.** A hidden instruction in a bill PDF to pay a crypto exchange. A statement sent to a new email address. A draft email to a customer under anti-money-laundering review. Investment advice. A standing order changed without approval. An offer to fix a trade record. An alert closed without a second person. Each is a legitimate call, with a legitimate credential, that the agent should not have made. A gateway would have added the key and let each one through.

The same holds for the gaps: 4 of the 13 involve a credential, 9 are about what the agent may do. What you worry about in a real business is business logic: transactions, credit given when it should not be, data leaking to the wrong person.

## What a proxy can and cannot see

Credential injection, and where the risk goes: the agent holds no key, the gateway adds it on the way out from a credential store, to public APIs and internal systems. A hidden instruction that makes the agent ask for the wrong payment still gets its key added. Our drawing of the pattern.

The series does have a policy step: "A policy decides whether the call is allowed; if so, inject the sensitive credentials." And Part 2.5 makes a version of my point itself: "the attacker who actually shows up doesn't need to decrypt the store anyway." So the question is what that policy can know. Could the proxy in the middle understand the business logic, and block the wrong payment? In principle, yes: it would act as a controller. In practice it is hard. To decide, it needs state and context, and the state usually lives in the application, not in the proxy. These proxies are products placed outside the application's domain, so even when they want to decide, they do not have the data. Imagine a proxy deciding about a customer when all it can see is the request in front of it; and the request is probably well formed, because the agent was tricked into a valid action. That is the catch.

And as soon as a proxy is in line, it brings its own risks:

- **A single point of failure.** Every agent's every call now depends on it. Ten agents share it, and one that floods it can break it for the other nine.
- **Where does it run?** In the same environment as the agent, under the same governance and controls, or outside it, on somebody else's network? If it is a third party's service and not open source, data now leaves your network to a server that can be breached, that holds all your secrets, and that needs its own authentication and authorisation.
- **Cost and ownership.** It takes time and money to run, it has to scale, and somebody has to own its budget, its outages and its race conditions.

If all it does is protect secrets and a few transactions, I do not think that is enough to justify those costs on its own. And I would argue that keeping keys out of the agent is something the model providers and agent platforms should provide natively.

## The questions, in order

Five questions before protecting a key: can an attacker reach the target with it; would we see it used; what can the key do; what can an injected agent do without it; what does the control cost. Then defence in depth.

Securing secrets this way is attractive because it is technically simple: put a proxy in, inject the key. That does not make it the first thing to do. My point is the one Risk Mandate is built on: look at the whole use case, end to end, map the real threats, and then check whether a control moves the needle. In this case:

1. **Can an attacker reach the target with the key?** For internal systems, usually not.
2. **Would we see it used?** Recognisable prefixes, egress filters, hooks.
3. **What can the key do?** Scope it, shorten it, bind it to a key pair.
4. **What can an injected agent do without the key?** Usually more, and that is where the policy goes.
5. **What does the control cost?** In line, single point of failure, where it runs, who pays.

Then, yes, keep the key out of the agent as defence in depth, with short-lived, PKI-based credentials, hooks and an Agent Behaviour Policy. In a good design, a leaked key should not matter much. And if an attacker can inject instructions into an agent and make it act on their behalf, leaking the credential may be the least dangerous thing they can do.

## What this does not claim

- **Not against the pattern.** Keeping keys out of agents is good practice; the argument is about order and weight.
- **Public keys are different.** For cloud and SaaS keys, reachable from anywhere, a leak does matter, and hiding them helps.
- **Pellbridge is invented.** One day, nine incidents, our classification of each.
- **A proxy can carry business rules.** With enough context; the point is that it usually lacks it.
- **The original series goes further than one post.** Read it in full; this replies to the argument, not to every part.

## Where this comes from

My voice memo of 21 October 2026, prompted by a public LinkedIn post on credential injection for AI agents; Christian Posta's series, Parts 1, 2 and 2.5, read on his blog and on agentgateway.dev; the CB4A Internet-Draft; agentgateway's documentation; AWS's IAM documentation on access keys, condition keys and identifiers, and its data perimeter whitepaper; GitHub's posts and documentation on token formats, secret scanning and push protection. The Pellbridge agents vault, read the same day: its incidents, policies and gap decisions. Related: [inside the Pellbridge agents](inside-the-pellbridge-agents.md), [attacks rewritten as mandates](attacks-rewritten-as-mandates.md), [the attack surface you do not have](the-attack-surface-you-do-not-have.md), [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html), [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policy[This article as a graph →](graphs.md#the-key-is-not-the-risk)

### Builds on

- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](attacks-rewritten-as-mandates.md) 28 supply-chain attacks read as reach beyond mandate: what a hardened registry stops, what only a written mandate can, and why agents change it.
- [The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed](the-attack-surface-you-do-not-have.md) Every CVE makes me smile: moving to the client side took my servers out of the news, and the constraint turned out to be speed.

### Continued by

- [An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer](an-analysts-blueprint-for-riskmandate.md) An analyst's blueprint for RiskMandate from the WestCap CISO Summit, the vendors already moving, and our answer.
- [Governed semi-autonomous development, read in a newsroom run by agents: where Levente Simon's method and our work arrived at the same ideas, how we measure up to it, and what we would add](governed-semi-autonomous-development-read-here.md) Levente Simon's method for governing agent teams, read in a newsroom run by agents: shared ideas, a mirror, and five suggestions.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 247 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=247)

**Posting this article on LinkedIn?** The cover is [the-key-is-not-the-risk.jpg](banners/the-key-is-not-the-risk.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-key-is-not-the-risk.html)*
