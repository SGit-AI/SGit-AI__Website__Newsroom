---
title: Who owns the record: an answer to Nitin Pandya's question about AI kill switches in Indian banks, why a kill switch cannot stop a valid workflow acting on a tampered record, and why the answer is a signed mandate for every change that can move money, checked outside the workflow
date: 2026-11-25
author: Dinis Cruz
author_url: about/index.html
summary: Nitin Pandya asks a sharp question. Indian banks spent 2026 building kill switches for AI, the RBI's draft model risk guidance asks for them, and the attacks CERT-In and I4C warned about this month never touched a model. Fraudsters put a mule account where a borrower's account should be, on loans already approved, and the lender's own disbursal workflow paid out, from allow-listed addresses, with every step looking legitimate: more than Rs 65 crore from 12 NBFCs in one police case. He is right that the control has to sit outside the model and the workflow, and right that the accountability question is uncomfortable: the CISO, the model owner or the head of operations? My answer is that the record has no owner today because nothing records who was allowed to change it. Make every change to a record that can release money carry a signed mandate, who asked, under which grant, for what scope and until when, and have something the workflow does not control check it before the money moves. Then the question has an answer: whoever signed the mandate, and whoever owns the policy that accepted it. We run our own agents this way, and we learnt it the hard way three days ago.
version: v0.14.214
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, abp, mandates, banking, cert-in, rbi, accountability, reply, article
status: published
---

!shot kil-post.webp | images/ | Nitin Pandya's post on LinkedIn: kill switches for AI, and attackers who never touched the model. | screenshot

## In short {#in-short}

- **The attacks never touched a model:** a tampered record, then a valid workflow did the rest.
- **A kill switch stops a model, not a legitimate instruction** acting on a record nobody checked.
- **Sign the change, not just the payment:** every change to a record that can move money carries a signed mandate.
- **Check it outside the workflow,** with a verifier the workflow cannot skip or edit.
- **Then accountability has an answer:** the key that signed the mandate, and the owner of the policy that accepted it.

## The question {#question}

Nitin Pandya [posted](https://www.linkedin.com/posts/nitinpandya_dataleadership-nrichsouls-datastrategy-share-7530848714999984128-7obv) this week: "Indian banks spent 2026 building kill switches for AI. But the attackers found a way around them. They never touched the model." His description of the method is "Change a business record. Alter an approval relationship. Then let the bank's own payment workflow do the rest", with "No suspicious payment instruction. No obvious policy violation." He ends with the question I want to answer: when an AI agent releases money through a valid workflow using a record that was quietly tampered with, "who answers to the regulator? The CISO, the model owner, or the head of operations?"

!shot kil-infographic.webp | images/ | The post's own summary: the attack path, the impact, the real gap and the accountability question. | screenshot

## What the advisories describe {#advisories}

I read the public reporting on the advisories behind the post. CERT-In's critical advisory of 9 October (CIAD-2026-0046) is about unauthorised transfers through payment and disbursal APIs; a later one names an AI-assisted actor, CRAFTY FALCON (CIAD-2026-0058, early November); and I4C's coordination unit asked banks, NBFCs and fintechs to act on them, adding that the use of agentic AI frameworks "makes the attack possible at machine speed" ([The Federal](https://thefederal.com/category/business/ai-cyberattacks-target-banks-nbfcs-i4c-warning-262227)). Cyble's reading of the advisory describes a path from exposed staging servers and shared credentials into production, API calls through allow-listed addresses, and "A Rs 1 transfer confirms the route" before the large transfers to mule accounts ([Cyble](https://cyble.com/blog/crafty-falcon-ai-assisted-financial-threat-actor/)).

One case shows it plainly, the one MediaNama reported from a Delhi police investigation: hackers "had found loans that were approved but not yet disbursed", and the disbursal command "carries a mule account in place of the borrower's account". Over three months, at 12 NBFCs in Delhi NCR, that took more than Rs 65 crore ([MediaNama](https://www.medianama.com/2026/11/223-ai-hackers-approved-loans-nbfc/)). That is exactly Nitin's point. The loan was approved. The workflow was valid. One field in one record was wrong, and nothing between that record and the money asked who had changed it, or on whose authority.

## Why the kill switch misses it {#gap}

The RBI's draft guidance on model risk, published for comment in June, asks regulated entities for override, suspension and deactivation arrangements for AI models, including kill switches, and for humans in or on the loop. That is sensible, and Nitin says so. But a kill switch is a control on a model's behaviour. In these attacks, the model, if there was one, did exactly what it should: it executed a valid instruction against the data it was given. The failure is earlier and quieter. The record changed, and nobody had to prove they were allowed to change it.

I wrote about this shape when reading another ledger of attacks: every incident is something that could do far more than it was meant to, and the attacker used the difference ([attacks rewritten as mandates](/articles/attacks-rewritten-as-mandates.html)). A disbursal field that anything with a valid token can rewrite is a mandate nobody wrote down.

## Sign the change, check it outside {#control}

!shot kil-control.webp | images/ | Sign the record and check it outside the workflow: a change with no valid mandate does not release money. | figure

Nitin's control is the right one: "Any change to a record that can trigger a payment should undergo independent verification before that record is allowed to release money." I would make it concrete in three parts.

- **The change carries a mandate.** Changing a beneficiary, an account or an approval is itself an action with an author, a grant, a scope and an expiry. Write that down as a record and sign it with the key of whoever, person or agent, was allowed to make that change ([approved business mandates](/articles/approved-business-mandates.html)).
- **Something outside the workflow checks it.** Before release, a verifier the workflow does not control checks the signature, that the key was allowed to make this kind of change, and that the scope covers this loan and this amount. A token from an allow-listed IP proves nothing about authority; a signature on a scoped mandate does. Cyble's summary of the advisory points the same way: "Stop trusting the client and the source IP", with signed requests.
- **No mandate, no money.** A change without a valid mandate does not release funds, and the refusal is itself a record. A Rs 1 test transfer to a new beneficiary would need a mandate too, so the route never gets confirmed.

This is the same answer to Nitin's other worry, agents that step outside their own permissions: an agent's permissions should be a written policy that lists what it may do, with anything not listed refused, checked by something that is not the agent ([a policy beside the prompt](/articles/a-policy-beside-the-prompt.html)). If an agent is still acting within its intended mandate, and you can show it, you know ([drift is the mandate moving](/articles/drift-is-the-mandate-moving.html)).

## We learnt this three days ago {#ours}

We run a large team of AI agents that create websites and push code, and on 22 November one of them pushed two commits signed with a key it had never registered, and a release went live. Every step was valid: the agent had push access, the pipeline ran, the site deployed. The incident note says it in two sentences: "Nothing refused it. Only Dinis noticed." The fix was the control above, applied to our world: a signer check in every site's pipeline, outside the agent and outside the build, that refuses a commit whose key is not in the published list ([almost a hundred repositories](/articles/almost-a-hundred-repositories.html)).

My own decisions work the same way now. When I say yes to something, a decisions agent records my words with the time and the exact scope and signs the record, and "An agent acts only on a signed record that it has checked." Keys are trusted through a chain that starts at my key on pki.sgit.ai ([who runs the agents](/articles/who-runs-the-agents.html)). It is a small version of what a bank needs, and it works at the speed agents work.

## Who answers to the regulator {#accountability}

Nitin's list is the CISO, the model owner or the head of operations. Today the honest answer is that nobody owns the integrity of the record, because nothing records who was allowed to change it, so the three owners can each point at the other two. With signed mandates, the question answers itself:

- **The person or agent whose key signed the change** answers for the change, and the person who granted that key its authority answers for the grant.
- **The owner of the policy that accepted the mandate** answers for what the policy allowed. That is a named role, and I would give it to the business owner of the payment process, with the CISO owning the verifier and its keys.
- **If nobody signed it,** the record was never valid, and whoever released money on an unsigned change owns the failure. That is a much easier conversation with a regulator than "every step appeared legitimate".

This is what we mean by RiskMandate: turning approved business mandates into controls that are checked, so that authority is something you can show, not something you infer after the money has gone ([a trusted framework for agentic finance](/articles/a-trusted-framework-for-agentic-finance.html)).

## What this does not claim {#limits}

- **I have not read the advisories themselves;** the facts here are from Cyble, MediaNama and The Federal's reporting, which differ on some dates.
- **I could not find the advisory's own wording** on attackers altering approval relationships, or on agents under evaluation exceeding their permissions; those are from Nitin's post.
- **Signing changes does not stop stolen keys:** it moves the attack to the keys, which is why grants should be narrow, short-lived and checked.
- **Our incident is about code and websites, not money;** it is the same shape at a smaller scale.

## Where this comes from {#sources}

[Nitin Pandya's post](https://www.linkedin.com/posts/nitinpandya_dataleadership-nrichsouls-datastrategy-share-7530848714999984128-7obv) on LinkedIn, read on 25 November 2026 from screenshots shared with me. Reporting on the CERT-In and I4C advisories by [Cyble](https://cyble.com/blog/crafty-falcon-ai-assisted-financial-threat-actor/) (11 November), [MediaNama](https://www.medianama.com/2026/11/223-ai-hackers-approved-loans-nbfc/) (18 November) and [The Federal](https://thefederal.com/category/business/ai-cyberattacks-target-banks-nbfcs-i4c-warning-262227) (8 November); the RBI's [press release](https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=63006) on the draft model risk management guidance (June 2026). Our incident note `board/incidents/2026-11-22__pushed-before-key-published.md` in [SovereignWebsite__IaC](https://github.com/SovereignWebsite/SovereignWebsite__IaC) and the [decisions](https://decisions.agents.sovereignweb.site/) site. Related: [attacks rewritten as mandates](/articles/attacks-rewritten-as-mandates.html), [approved business mandates](/articles/approved-business-mandates.html), [drift is the mandate moving](/articles/drift-is-the-mandate-moving.html), [a policy beside the prompt](/articles/a-policy-beside-the-prompt.html), [a trusted framework for agentic finance](/articles/a-trusted-framework-for-agentic-finance.html).
