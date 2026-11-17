---
title: Governance from zero: Nina J. noticed that identity and behaviour policies come with our smallest £500 offer, not as a premium upgrade, because "we're only testing it" has never reassured a security review; my answer is that even the £0 offer has all of it, and here is why open source is what makes that possible, why security sold as an upgrade is a choice, and why a pilot with its governance built in is a pilot that can convert
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Nina J., who tells deep tech founders why their pilots did not convert, left a comment on my post about our stack of companies that I want to answer properly. She noticed that at our £500 entry point governance is not a premium upgrade: identity and behaviour policies are part of the smallest deployment, not something a customer discovers after the pilot. A small experiment does not mean a small risk, she wrote; someone still needs to know what the agent can reach, what it is allowed to do and who can stop it. And "we're only testing it" has never been a reassuring answer to a security review. She is right, and my reply was that it goes further: even the £0 offer has all of it. That is the power of open source. When the code, the policies and the schemas are all public, there is no commercial reason and no strategic pressure to hold any of it back for a higher tier. We sell time, setup, judgement and a signature; we do not sell the governance. Here is why that matters: what the industry does instead, with single sign-on and audit logs priced as luxuries; what our £0 really contains; what each paid step adds; and why I think a pilot that already passes its security review is the pilot that converts.
version: v0.14.143
license: https://creativecommons.org/licenses/by/4.0/
tags: governance, open-source, security, agents, pricing, pilots, riskmandate, agenticcells, reply, article
status: published
---

!shot gov-comment.webp | images/ | Nina J.'s comment on my post: governance is not a premium upgrade, and "we're only testing it" does not reassure. | screenshot | medium

## In short {#in-short}

- **Nina J. spotted it:** at our £500 entry point, governance is included, not an upgrade.
- **A small experiment is not a small risk:** someone must know what the agent can reach, and who can stop it.
- **My answer: even £0 has all of it,** because everything is open source.
- **There is no commercial reason to hold governance back** when nothing is proprietary.
- **The industry often does the opposite:** security sold as the enterprise tier.
- **We sell time, setup, judgement and a signature,** not the controls.
- **A pilot with its governance built in** is a pilot that can pass its security review, and convert.

## The comment {#comment}

My post on LinkedIn was about how SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells work as one stack of separate companies, with one ladder of offers, from £500 ([the intersection](/articles/the-intersection.html)). Nina J., who describes her work as telling deep tech founders why their pilots did not convert, wrote:

> "There's something particularly interesting about the £500 entry point, Dinis....governance isn't being treated as a premium upgrade. From the enterprise side, that's significant. A small experiment doesn't automatically mean a small risk. Someone still needs to understand what the agent can access, what it's authorized to do, and who can stop it when something goes sideways. I like that identity and behavior policies are part of the smallest deployment rather than something a customer discovers they need after the pilot. Because "we're only testing it" has never been a particularly reassuring answer to a security review."

And I answered: correct, and that is the power of having everything open source; there is no commercial reason or strategic pressure to limit what is delivered. In fact, even the £0 offer has all of that.

## A small experiment is not a small risk {#risk}

Her three questions are exactly the ones our Agent Behaviour Policies were written to answer: what can the agent reach, what was it asked to do, and who can stop it ([what can your agent reach?](/articles/what-can-your-agent-reach.html)). None of them gets smaller because the deployment is small. An agent in a pilot with access to a real inbox, a real repository or a real customer list has the same reach as one in production. Only the number of people who know about it is smaller.

That is why, in our cells, the first agent arrives with its key and its policy, and the stop is designed in from the first day, the way we stopped more than 60 agents at once at Web Summit ([stopping a hundred agents](/articles/stopping-a-hundred-agents.html)).

## Why open source makes it free {#open}

On our open source site I put it this way: everything the company does, the code, the logic, the functionality and the schemas, is open source, and "there should be nothing proprietary", because a bait model, with the best features locked away, is something "the community always sees through" ([open core, or packaging?](https://open-source.sgit.ai/views/open-core.html)). The code is Apache 2.0; the policies and documents are CC BY 4.0 ([the licences in force](https://open-source.sgit.ai/practice/index.html)).

Once that is true, there is nothing to gate. The behaviour policy standard is public ([abp.sgit.ai](https://abp.sgit.ai/)). SGit's vaults are public code. pki.sgit.ai makes a key for every person and agent in the browser, for free ([a key for every person](/articles/a-key-for-every-person.html)). SHarness, which puts a kernel-enforced boundary round every process an agent starts, is public ([introducing SHarness](/articles/introducing-sharness.html)). A tier that withheld any of it would be withholding something anyone can download.

And there is a test for whether we keep to it, which I proposed on the same site: does the customer build contain anything the public repository does not? If no, it is packaging. If yes, it is open core, and we should say so plainly.

## Security as an upgrade is a choice {#upgrade}

Much of software does the opposite. The SSO Wall of Shame lists vendors that charge more, sometimes several times more, for single sign-on, the feature that lets a company control who can log in ([sso.tax](https://sso.tax/)). Audit logs, role-based access and data retention are often on the same top tier. It is a reasonable business, and it means the cheapest version of a product is the least safe one, which is exactly the version a pilot runs on.

With agents that choice gets worse, because the risk of a small agent is not small. If a policy, a key and a stop cost extra, the pilot runs without them, and the security review finds out afterwards.

## What £0 contains, and what each step adds {#ladder}

!shot gov-ladder.webp | images/ | The same governance at every step, from £0 to £20,000; what changes is who does the work, and who signs. | comparison

- **£0:** everything, yourself. The open policies and hooks, SGit's vaults, a key from pki.sgit.ai, SHarness, and hundreds of articles explaining how we use them. The governance is complete; the work is yours.
- **£500:** one workflow, set up with you in a session, with its agent, its key and its policy from the start.
- **£1,500:** a few sessions and a handover, and on RiskMandate, a policy reviewed for your situation with a professional's signature.
- **£5,000:** a team, with a conductor, keys, a board and a stop.
- **£20,000:** a network of teams, bespoke.

At every step the controls are the same. What a customer pays for is time, setup, judgement, and a person who signs their name to it. As the open source site says, we are selling trust ([open-source.sgit.ai](https://open-source.sgit.ai/)).

## A pilot that can convert {#convert}

Nina's work is pilots that did not convert, so this is the part I would most like her view on. I suspect many die at the same moment: the pilot worked, the business wants it, and then the security review asks what the agent can reach, who authorised it and who can stop it, and nobody has the answer written down. The project goes back to the start, or into a queue.

A pilot that already has those answers, a written policy, a key per agent, a record of what each one did, and a tested stop, walks into that review with its evidence. The pilot is then production minus scale, not a demo that needs rebuilding.

## What this does not claim {#limits}

- **Free code is not free work:** at £0, running and maintaining it is yours.
- **The prices are first proposals** on most of our sites; only AgentiCCells and RiskMandate show them today.
- **Why pilots fail is Nina's field, not mine;** the last section is my guess, and I would like to be corrected.

## Where this comes from {#sources}

Nina J.'s comment and my reply on my LinkedIn post of [the intersection](/articles/the-intersection.html), 17 November 2026, shown above. [open-source.sgit.ai](https://open-source.sgit.ai/), its pages [open core, or packaging?](https://open-source.sgit.ai/views/open-core.html) and [three licences, three layers](https://open-source.sgit.ai/practice/index.html); [the SSO Wall of Shame](https://sso.tax/); [abp.sgit.ai](https://abp.sgit.ai/); all read on 17 November 2026. Earlier on this site: [what can your agent reach?](/articles/what-can-your-agent-reach.html), [stopping a hundred agents](/articles/stopping-a-hundred-agents.html), [a key for every person](/articles/a-key-for-every-person.html), [introducing SHarness](/articles/introducing-sharness.html), [the intersection](/articles/the-intersection.html).
