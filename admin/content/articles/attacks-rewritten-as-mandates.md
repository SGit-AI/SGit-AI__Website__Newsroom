---
title: Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent
date: 2026-10-13
author: Dinis Cruz
author_url: about/index.html
summary: Chainguard keeps a public ledger of software supply-chain attacks, 28 incidents from May 2024 to October 2026, 23 of them this year. I read it the way I read an agent's permissions, and every row turns out to be the same shape. A credential, a tag or a build step could do far more than it was ever meant to do, and the attacker used the difference. A maintainer token that could publish any version of any package, used by someone whose job was to release one SDK from a reviewed build. That is reach beyond mandate, the gap an Agent Behaviour Policy is written to make visible. Sorted by what would have stopped each attack, by our reading, a control on the consumer's side, a hardened registry, a cooldown, no install scripts, appears in 26 of the 28; a control on the publisher's side, a written answer to what a credential was for, appears in 16. The first kind is a product you can buy. The second is a document almost nobody has written. And it matters more every month, because the next maintainer holding a publish token is an agent: Chainguard's own engineers describe a fleet that opened 4,746 pull requests in eight weeks against their code, fenced by rules that are an excellent mandate, kept in prompts, bot configuration and a blog post. One pipeline needs three records: trusted inputs, a written mandate, and provable outputs with a memory that outlives the session. As an open source project we would like to be on the first list, and this article is about the other two.
version: v0.12.33
license: https://creativecommons.org/licenses/by/4.0/
tags: supply-chain, agents, agent-behaviour-policy, reach, mandate, open-source, registries, skills, sgit, riskmandate, chainguard, article
status: published
---

!shot am-ledger.webp | images/ | Chainguard's 28 public supply-chain incidents, May 2024 to October 2026, one dot each, with every vector counted. | timeline

## In short {#in-short}

- **A public ledger, 28 attacks.** Chainguard's incident list runs from a hallucinated package name in May 2024 to a compromised SDK last week. 23 of the 28 are from 2026.
- **Every row is reach beyond mandate.** A token, a tag or a CI step could do more than its job, and the attacker used exactly the difference.
- **Two kinds of barrier.** By our reading, a consumer-side control would likely have held in 26 incidents; a publisher-side mandate in 16; both in 14.
- **The consumer side is a product.** Rebuilt from source, a cooldown, no install scripts, an allowlisted registry. You can buy it without trusting anyone upstream.
- **The publisher side is a document.** Trusted publishing, scoped tokens, two people to release: each one is a written answer to "what was this credential for?", and only the publisher can write it.
- **The next maintainer is an agent.** Agents open pull requests, add dependencies and hold tokens. One attack in the ledger already worked through a model's suggestion.
- **Three records, one pipeline.** Trusted inputs, a written mandate, and outputs and memory you can prove. The first has products; the other two are what this site and RiskMandate work on.
- **An open source question.** sgit is Apache-2.0, pure Python, two dependencies. How does a small, active project get into a hardened registry, and on what terms?

## A ledger of attacks {#ledger}

Chainguard, the company that rebuilds open source images and packages from source, keeps a public ledger on its [AI threat protection page](https://www.chainguard.dev/solutions/ai-threat-protection), and its framing is blunt: "Executing a sophisticated supply chain attack used to require time, resources, and a skilled team. AI has removed all three constraints." The list has 28 incidents, from 28 May 2024 to 8 October 2026. I will be at their Assemble conference in London tomorrow, 14 October, where one of the lightning talks is called "Attacks rewritten", and this article is my version of that exercise, written so that it stands on its own.

The ledger reads like the last two years of the news. The tj-actions/changed-files action, where "attackers retroactively modified all version tags to reference a malicious commit", and over 23,000 repositories were affected. The chalk and debug packages, where "a single maintainer was phished via a fake npm 2FA reset email" and malicious versions of 18 packages went out, with 2.6 billion combined weekly downloads behind them. Shai-Hulud, where phished maintainer credentials published worm-style packages that republish themselves; one of its later waves put 639 malicious versions across 323 packages in about 22 minutes. Trivy, where compromised credentials were used "to force-push 75 of 76 version tags in trivy-action", and then LiteLLM, where credentials "stolen via the Trivy breach" published two backdoored versions of a package with 280 million monthly downloads. A security scanner's breach became an AI gateway's breach, five days later.

Counting the vectors myself, an incident can have two: an install-time hook ran the payload in 17, a maintainer account or token was taken over in 16, a typosquat or lookalike name in 5, a CI workflow exploited to publish in 3, version tags repointed in 3, and a fork farm or dependency confusion in 2.

## Every attack is reach beyond mandate {#reach}

I spend most of my time on a different question: what an AI agent can actually do, against what it was asked to do. An Agent Behaviour Policy has four columns for it: the reach, measured from what the agent is connected to; the mandate, what it was asked to do; the gap between them; and the barrier on each row of the gap, typed by whether anything real stands in the way. [Footprint and blast radius](/articles/footprint-and-blast-radius.html) put the reason for measuring reach in one sentence: "An attacker who takes an agent over, through a prompt injection, a poisoned document, a compromised skill, inherits the agent's reach and ignores its mandate entirely."

Read the ledger with those four columns and it fills itself. Take the newest row, tensorlake, a TypeScript SDK with about 400,000 monthly downloads, where a malicious release went out through a maintainer's compromised identity:

- **Reach:** the maintainer's token could publish any version of any package the maintainer owned.
- **Mandate:** publish releases of one SDK, from a reviewed build.
- **Gap:** everything else that token could do, which is what the attacker did.
- **Barrier:** publishing bound to the CI identity, so a stolen personal token publishes nothing; and a cooldown before new versions are consumed.

By my reading, the other rows have the same shape. A version tag that could be moved, when its mandate was to name one commit. A CI workflow that would run text from a pull request comment, when its mandate was to release on a tag, which is how elementary-data, with 1.1 million monthly downloads, shipped a release that stole credentials: the attack came in "via a malicious PR comment". A scanner's CI that held credentials for someone else's package index. As far as the public accounts show, nobody had written down that these credentials were for one thing, so nothing could notice when they were used for another.

## Two kinds of barrier {#barriers}

!shot am-barriers.webp | images/ | For each of the 28 incidents, the control that would most likely have stopped it, by our reading. | comparison

For each incident I wrote down what would most likely have stopped it, and sorted the answers into two kinds.

**The consumer side** is what you let in: packages rebuilt from source, a cooldown before a new version is used, no install-time scripts, an allowlisted registry with no public fallback, new packages detonated in a sandbox first, actions pinned to a commit rather than a tag. By our reading, one of these would likely have held in 26 of the 28. Its great strength is that it needs nobody's cooperation: it works on the assumption that any publisher can be compromised. This is what Chainguard sells, and its page lists the controls in its own words: building "from verified source", "malware and greyware scanning", not building libraries "that use install-time scripts", actions built "using immutable SHA commits".

**The publisher side** is what a credential was for: trusted publishing bound to a CI identity, a publish scope per package, two people to release, publishing separated from contributing, short-lived tokens, and pull request text treated as data. One of these appears in 16. Only the publisher can do it, and every item is a mandate: a written answer to what this token, this workflow, this account was allowed to do. In two of the incidents, a compromised account publishing under a scope it legitimately held, it is the only kind that helps.

The consumer side scales, and I would buy it. But it is a defence against everyone else's missing mandate, and it grows by detecting harder, faster. The publisher side makes the bad publish impossible rather than detected. It is the same move [Hope or enforcement](/articles/hope-or-enforcement.html) made with one customer service agent built three ways: the share of its rules kept only by good behaviour fell from 97% to 23% when the rules moved into the platform.

## The next maintainer is an agent {#agents}

The first incident in the ledger is the one I keep coming back to. In May 2024, "a security researcher discovered that ChatGPT repeatedly hallucinated a package called huggingface-cli", registered the name as a proof of concept, and it was downloaded more than 30,000 times in three months. Nobody's account was taken over. The reach was whatever a model suggested, and the mandate, for the developer or agent adding the dependency, was never written. The barrier is a mandate for the agent: it may only add dependencies from an approved source.

Agents now hold the credentials in the rest of the ledger. They open pull requests, add dependencies, run CI and, with a token in the environment, could publish. Chainguard's own engineering shows what that looks like done carefully. In [How AI keeps our code on standard](https://www.chainguard.dev/unchained/this-shit-is-hard-how-ai-keeps-our-code-on-standard), Maxime Gréau describes a fleet of agents keeping their repositories on standard: "Over the last 8 weeks, across our repositories, skillup opened 4,746 standards-fix pull requests." A confidence bot, rolled out partway through, graded 3,044 of them; of 1,117, "it judged 840 (75.2%) as low-risk and merged them with no human in the loop." The fences are the interesting part. The fixer may fix only what is broken. Changes touching sensitive surfaces, production infrastructure or authentication, are capped and go to a person. In the confidence score, "the model is the heaviest single input, but it's still under half the total." And the grade is bound to a commit, because "a label alone can let a grade computed for an old, good commit vouch for a new, broken one."

Read as a policy, that post already has three of the four columns. The reach is configured: their Workspaces sessions, a sandboxed place to run coding agents, reach the model, the session's own repository, their registry, and the user's identity "while you're attached and for up to an hour after you detach"; "no long-lived credential enters a session"; anything else asks. The barriers are in code: checks bound to a commit, caps, gates. And the gap was found the way most gaps are, by accident: the label that outlived its commit is a row of reach nobody had listed until it was nearly used. The mandate is there too, in good sentences, but it lives in prompts, bot configuration and a blog post. That is not a criticism; it is a careful account of giving agents real power over a codebase, and as far as I can see it is the state of most of the industry. It is also the argument of [A policy beside the prompt](/articles/a-policy-beside-the-prompt.html): write the mandate down as a document the agent takes as an input, versioned beside the reach and barriers it constrains, and owned by someone who can be asked.

## One pipeline, three records {#records}

!shot am-records.webp | images/ | One pipeline, three records: what an agent consumes, what it was allowed to do, and what it produced and remembers. | architecture

So I think the supply chain for an agent needs three records, and only the first has a market yet.

**Trusted inputs.** What the agent loads should be what its source says it is: images and packages rebuilt from source and attested, and now the instructions too. Chainguard's hardened [agent skills](https://edu.chainguard.dev/chainguard/agent-skills/public-registry.md) come from a public registry where each skill ships a HARDENING.md that records "the exact commit Chainguard hardened from" and whether the skill's own instructions were changed.

**A written mandate.** A hardened skill is a trustworthy input. It says nothing about what the agent that loads it may do with the mailbox, the repository or the publish token it is connected to. That is the Agent Behaviour Policy, and the business argument for it is in [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html): when something goes wrong, a written mandate is what separates "the agent did what it was allowed" from "the product ignored what it was told". [RiskMandate](https://riskmandate.ai) is the work of writing these down, per agent and per deployment, for the people who will be asked about them.

**Provable outputs and memory.** What the agent produces, and what it learns, should outlive the session and be checkable later. Chainguard's post says a reverted auto-merge "is concrete proof that a change it called safe wasn't", and the bot keeps those reverts to grade similar changes more carefully: memory, held in one bot's store. Their Workspaces park a session when you leave and "a parked session expires 5 days after it parks." [sgit](/articles/what-sgit-is.html) is what we use for this: an encrypted, versioned vault per unit of work, with a branch per agent, a reviewed merge, content-addressed history, and a server that holds only ciphertext. This newsroom runs on it, and [two agents share one vault](/articles/two-agents-one-vault.html) with only the read key on the public side.

## An open source question {#oss}

There is a practical side to this for us, and a wider question behind it. sgit is open source: Apache-2.0, pure Python, two runtime dependencies, published on PyPI and as a container image, with skills that agents load to work with vaults. It is exactly the kind of input the first record is about, and I would like it to be a trusted one.

Today our container image is built on `python:3.12-slim`. Moving it onto a minimal, rebuilt base is a one-line change in its Dockerfile, and for a tool that handles vault keys it is the obvious next step. Beyond that, a hardened registry has three doors, and the terms behind each are worth knowing for any small project. Chainguard's [pricing page](https://www.chainguard.dev/pricing) offers "five images to test and deploy in production for free" per organisation, and a set of about 50 developer images on their latest tag only, outside the CVE remediation agreement; [Libraries](https://edu.chainguard.dev/chainguard/libraries/python/overview.md) are "rebuilt from source and require that source be available", added when customers request them, and priced per language by the number of developers; the public skills registry is free to pull from, "no entitlement and no legal terms required", and namespaced by upstream repository, but the documentation does not say how a project becomes an upstream. Their [EmeritOSS](https://www.chainguard.dev/unchained/introducing-chainguard-emeritoss) programme looks after mature projects whose maintainers have stepped back. I could not find a published path for the other end: small, active projects, the long tail where many of the ledger's victims started.

That is the question I will be asking, and not only of one company. The hardened supply chain is paid for by the consumers of open source, which is right, because they carry the risk. The producers are the inputs. If the next maintainer is an agent, and the next dependency is suggested by a model, then the small projects are where both the risk and the fix begin, and the terms on which they can join the trusted list are part of the security model.

## What this does not claim {#limits}

- **The incidents are Chainguard's; the columns are ours.** Names, dates, ecosystems and counts are from their ledger as published on 13 October 2026. The vectors, the reach and mandate readings and the barrier for each row are my reading, and they would draw some rows differently.
- **"Would likely have held" is a judgement.** I sorted each incident by the control most likely to have stopped it; no control was tested against these attacks here.
- **The four-column reading is a lens, not an audit.** It has not been applied to any company's agents with their access; the Chainguard examples are from what they have published.
- **The registry terms are as their pages state.** I have not asked Chainguard about open source terms yet; the gap I describe is in what is published, not in what they may do.
- **The image change is planned, not made.** sgit's image is still built on `python:3.12-slim` as this goes out.

If you maintain an open source project and have been through a hardened registry's door, or you have written a mandate for an agent that holds a publish token, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

Two voice memos and a message of mine on 13 October 2026, the night before Chainguard Assemble London, written by this site's agent in the voice of this site from Chainguard's public pages and from research done in an encrypted vault for the day; the argument and the editorial responsibility are mine. Chainguard: [AI threat protection](https://www.chainguard.dev/solutions/ai-threat-protection), the incident ledger and the list of controls; Maxime Gréau, [This Sh*t is Hard: How AI keeps our code on standard](https://www.chainguard.dev/unchained/this-shit-is-hard-how-ai-keeps-our-code-on-standard), 24 June 2026; [Workspaces overview](https://edu.chainguard.dev/chainguard/workspaces/overview.md) (beta); [the public skills registry](https://edu.chainguard.dev/chainguard/agent-skills/public-registry.md); [Libraries for Python](https://edu.chainguard.dev/chainguard/libraries/python/overview.md); [pricing](https://www.chainguard.dev/pricing); [Introducing EmeritOSS](https://www.chainguard.dev/unchained/introducing-chainguard-emeritoss); the [Assemble London agenda](https://www.chainguard.dev/assemble-london-2026/agenda). All fetched on 13 October 2026. sgit's Dockerfile is in its public repository.
