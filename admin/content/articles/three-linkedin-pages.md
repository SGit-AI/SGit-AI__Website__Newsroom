---
title: Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: I now have three active companies, sgit.ai, the SGit Newsroom and RiskMandate, and none of them has a LinkedIn page. So I asked this site's agent to gather what LinkedIn needs, what we already have, and to draft the pages, the first posts and a new profile and bio for me. I am publishing the result rather than keeping it private, because that is what this site is for: documenting the story of what is actually going on, including the parts that are usually done quietly. The newsroom is the story, and the people who subscribe to it are following exactly this. What follows is the decisions to make first, with what LinkedIn says about each (the newsroom gets a company page rather than a showcase page, because people need to be able to say they work there); the drafted fields for each page, with their character counts against LinkedIn's limits; ten first posts for each, every one an article or page already published; and my own headline, about and bios. The addresses for all three looked free on 18 October. The RiskMandate page will be agreed with my co-founder before it goes up.
version: v0.12.107
license: https://creativecommons.org/licenses/by/4.0/
tags: linkedin, companies, sgit, riskmandate, newsroom, article
status: published
---

!shot li-pages.webp | images/ | Three LinkedIn pages and a profile. sgit.ai, Git for encrypted vaults; the SGit Newsroom, a publication written in the open by an editor and a desk of agents; and RiskMandate, Agent Behaviour Policies for AI agents; each with its tagline, its industry and ten first posts drawn from material already published; and the founder's profile tying them together. The Cyber Boardroom, the legal entity behind sgit.ai and RiskMandate, sits underneath. | concept

## In short {#in-short}

- **Three active companies, no LinkedIn pages.** sgit.ai, the SGit Newsroom and RiskMandate.
- **Done in the open.** This site documents the story, including the parts usually done quietly.
- **The addresses look free.** All three returned 404 on 18 October.
- **The newsroom gets a company page.** A showcase page cannot be anyone's employer.
- **Every field drafted, with its count.** Taglines under 120 characters, abouts under 2,000.
- **Thirty first posts, all already written.** Ten per page, each an article or page on the sites.
- **A new profile and bio.** Built from the three companies and the record.
- **RiskMandate's page is shared.** It is agreed with my co-founder before it goes up.

## Why in the open {#why}

The point of this site is to capture the story of what is actually happening: the products, the decisions, the mistakes, and the work that is usually invisible. Setting up a company's presence is part of that story. The people who subscribe to the newsroom are following exactly this, and the drafts below are the kind of thing a founder usually works on in private and then publishes as if it had always been there. Here it is before it is done.

## Decide first {#decide}

**The addresses.** Requested without logging in on 18 October 2026, `linkedin.com/company/sgit-ai`, `/riskmandate` and `/sgit-newsroom` all returned 404, as did the obvious variants. That means the address is free, not that no page exists anywhere; web searches found none. `/the-cyber-boardroom` exists.

**Company page or showcase page for the newsroom.** LinkedIn's [showcase pages](https://www.linkedin.com/help/linkedin/answer/a570165) are for a brand or initiative of a parent page. They do not share followers with the parent, appear in search only for people who already follow them, cannot have jobs, and nobody can list one as their employer. The newsroom is now a business of its own, with its own model, so it gets a company page.

**How the pages relate.** sgit.ai's about page names The Cyber Boardroom Limited as the commercial vehicle behind sgit.ai and RiskMandate, and RiskMandate's says a company of its own is being set up. The three new pages list each other as affiliated, and The Cyber Boardroom's page stays as the entity.

**What LinkedIn asks.** An account more than a day old with more than one connection, possibly a verified work email ([who can create a page](https://www.linkedin.com/help/linkedin/answer/a726850)); a logo of at least 268 by 268 pixels, 400 by 400 recommended ([images](https://www.linkedin.com/help/linkedin/answer/a563309)). A page newsletter needs more than 150 followers ([newsletters](https://www.linkedin.com/help/linkedin/answer/a591266)). The limits used below, a tagline of 120 characters and an about of 2,000, are from LinkedIn Learning, not a help page; the headline's 220 and the profile about's 2,600 are from third-party guides and LinkedIn's Talent blog.

## sgit.ai {#sgit}

Industry: Software Development. Size: 1 to 10. Type: privately held.

- **Tagline** (117 of 120 characters): Git for encrypted vaults, for people and AI agents. Files are encrypted on your machine; servers see only ciphertext.
- **Website**: https://sgit.ai
**About** (1171 of 2000 characters):

> sgit is Git for encrypted vaults. You clone, commit, branch and merge as you do with Git, but every file is encrypted on your machine (AES-256-GCM) before it leaves, and the server stores only ciphertext under opaque ids. A read key lets someone read a vault without being able to change it; a write key is separate.
>
> We built it for people and AI agents that need to share files they cannot afford to leak: an agent's memory and checkpoints, a team's research, a CI pipeline's secrets, a published vault anyone can verify. Append lanes let an agent or a browser send into a vault without being able to read it back.
>
> Three parts, all open source under Apache 2.0: the sgit command line (pip install sgit-ai), SG/Vault in the browser, and SG/Send, the zero-knowledge storage behind them. The code is free; the running, maintained service is what we sell, through sgraph.ai.
>
> sgit is in beta and has no compliance certification yet. Everything we claim about it is written down, versioned and testable: the docs, the security model and more than fifty published vaults with their read keys.
>
> The SGit Newsroom (newsroom.sgit.ai) is written and published on the same stack.

- **Specialties**: encrypted storage, client-side encryption, version control, AI agents, agent memory, zero-knowledge storage, open source, Git, vaults, secure file sharing, CI/CD secrets, provenance
- **Locations**: London, United Kingdom (confirm)
- **Custom button**: Visit website → https://sgit.ai/docs/quickstart.html

The first ten posts, from what is already published:

1. [Why sgit](https://sgit.ai/why/index.html): Open with the problem: agents need to share files that must not leak.
2. [What sgit is](/articles/what-sgit-is.html): The one-paragraph explanation, for people who skipped the first post.
3. [Quickstart](https://sgit.ai/docs/quickstart.html): pip install sgit-ai, then a vault in three commands.
4. [The security model](https://sgit.ai/security/index.html): What the server can and cannot see, and what beta means.
5. [Published vaults](https://sgit.ai/demos/vaults/index.html): More than fifty vaults with their read keys: verify, don't trust.
6. [sgit in a CI pipeline](/articles/sgit-in-a-ci-pipeline.html): A concrete job: secrets and artefacts in a pipeline.
7. [One vault, ten agents](/articles/one-vault-ten-agents.html): What happened when ten agents shared one vault.
8. [From Send to sgit](/articles/from-send-to-sgit.html): The origin: a server that holds nothing.
9. [sgit is a standard](/articles/sgit-is-a-standard.html): Why it is a format, not just a tool.
10. [A vault on Cloudflare](/articles/cloudflare-as-lego-blocks.html): A read-write vault server in 83 lines.

## The SGit Newsroom {#newsroom}

Industry: Online Media. Size: 1 to 10. Type: privately held. The six newsletter issues so far are already on LinkedIn, in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/); once the page has more than 150 followers it can carry its own.

- **Tagline** (118 of 120 characters): A publication about AI agents, security and the future of news, written in the open by an editor and a desk of agents.
- **Website**: https://newsroom.sgit.ai
**About** (1063 of 2000 characters):

> The SGit Newsroom is a publication about AI agents, security and the next generation of publishing, written in the open by Dinis Cruz with a desk of agents.
>
> Articles start as his voice memos and are researched, written, checked and published by named agents under published rules. Every claim links to its source, every version of every article is kept, and each article has a graph of its argument that people and agents can query. Content is CC BY 4.0 and the code is Apache 2.0.
>
> It is also a working model of how news could be paid for. Readers pay for the share of a page they actually read, after they have read it, and their rating sets the price. The balance lives in the reader's own browser and vault, not on our servers.
>
> More than 180 articles since 17 August 2026, four wires in beta (industry, OWASP, AWS and Portugal), and a newsletter. Every article can be reviewed on the record by other models, the editor and the desk, against published criteria.
>
> Published by the sgit project, which builds the stack it writes about; we say so on every page.

- **Specialties**: AI agents, agent security, application security, future of news, journalism, publishing, provenance, AI governance, open source, encrypted vaults, micropayments, newsletters
- **Locations**: London, United Kingdom (confirm)
- **Custom button**: Visit website → https://newsroom.sgit.ai

The first ten posts, from what is already published:

1. [About](/about/): Who writes it and how: an editor and a desk of agents, in the open.
2. [Pay after you read](/articles/pay-after-you-read.html): The payment model in one post: pay for what you read, after.
3. [No server by design](/articles/no-server-by-design.html): The whole newsroom runs in the reader's browser.
4. [Reviews on the record](/articles/reviews-on-the-record.html): Other models, the editor and the desk review every article.
5. [The agent is the reader](/articles/the-agent-is-the-reader.html): Why publishers should serve agents a graph, and get paid for it.
6. [A story vault, not a paywall](/articles/future-of-news-story-vault-not-paywall.html): The argument for selling the graph behind the article.
7. [For publishers](/publishers/): What is live today that another newsroom could copy.
8. [The OWASP Wire](/wire/owasp/): A weekly wire written by agents, labelled as such.
9. [Research delivered as a vault](/articles/research-delivered-as-a-vault.html): A pitch to research firms, and the model behind it.
10. [On the record](/articles/on-the-record.html): Signed expert opinions, paid when readers value them.

## RiskMandate {#riskmandate}

Industry: Computer and Network Security. Size: 1 to 10. Type: privately held. RiskMandate is co-founded, and its page is agreed with my co-founder before it goes up. The drafts use only what riskmandate.ai says publicly, and follow [what can your agent reach?](/articles/what-can-your-agent-reach.html) on one point where the site reads differently: RiskMandate stays out of the request path, and enforcement happens elsewhere.

- **Tagline** (114 of 120 characters): Give agents access. Not free rein. Agent Behaviour Policies: what an agent can reach, what it may do, and the gap.
- **Website**: https://riskmandate.ai
**About** (1038 of 2000 characters):

> Give agents access. Not free rein.
>
> RiskMandate writes Agent Behaviour Policies. An ABP is a record for one agent in one deployment, in four parts: its reach, what it can actually access, measured; its mandate, what the business authorised; the gap between the two; and the barriers that stand in the way of each capability. It carries no score. It is the document a CEO, a CISO or an insurer can read to decide whether an agent is allowed to do what it is about to do.
>
> We stay out of the request path on purpose. Enforcement happens in the tools and platforms the agent already runs on; the ABP says what should be enforced, and records what is.
>
> One-time pricing, per agent per deployment: the pack (£10), a working vault (£50), corrected for your situation (£500, free to early users in exchange for feedback), and two sessions with a professional who signs it (£1,500). Sixteen ABP templates are free, and the vocabulary is open at abp.sgit.ai under CC BY 4.0.
>
> RiskMandate is not an insurer. Its aim is to make agentic AI insurable.

- **Specialties**: AI agents, agent security, AI governance, risk management, cyber insurance, policy as code, Agent Behaviour Policy, CISO, compliance, insurability
- **Locations**: London, United Kingdom (confirm)
- **Custom button**: Learn more → https://riskmandate.ai/agent-behaviour-policy.html

The first ten posts, from what is already published:

1. [Give agents access. Not free rein.](https://riskmandate.ai/): The tagline post: what RiskMandate is for.
2. [What can your agent reach?](/articles/what-can-your-agent-reach.html): The explainer for the person who has to decide.
3. [The Agent Behaviour Policy](https://riskmandate.ai/agent-behaviour-policy.html): Reach, mandate, gap, barriers, in one picture.
4. [Pricing](https://riskmandate.ai/pricing.html): One-time, per agent: from £10 to £1,500.
5. [The open vocabulary](https://abp.sgit.ai/what-is-an-abp/index.html): The ABP library is free under CC BY 4.0.
6. [Ten questions](/articles/riskmandate-ten-questions.html): The questions customers ask, answered.
7. [Every risk is already accepted](/articles/every-risk-is-already-accepted.html): The idea behind the product: someone already accepted it.
8. [A policy beside the prompt](/articles/a-policy-beside-the-prompt.html): What aviation and payments teach about agents.
9. [A licence to operate](https://riskmandate.ai/licence-to-operate.html): The next document after the ABP.
10. [Our first PR in Ruflo](/articles/our-first-pr-in-ruflo.html): The ABP inside an open-source agent framework.

## My profile {#profile}

- **Headline** (152 of 220 characters): Founder of sgit.ai and the SGit Newsroom · Co-founder of RiskMandate · Encrypted vaults and behaviour policies for AI agents · Former OWASP Board member
**About** (1139 of 2600 characters):

> I build the tools I think AI agents need before we can trust them with real work, and I write about it in the open.
>
> sgit.ai is Git for encrypted vaults: files encrypted on your machine, shared with people and agents through read and write keys, on a server that only sees ciphertext. RiskMandate, which I co-founded, writes Agent Behaviour Policies: for each agent, what it can reach, what it was allowed to do, and the gap. The SGit Newsroom is where I think out loud: articles written from my voice memos by a desk of agents, every source linked, every version kept, and readers paying for what they actually read.
>
> Before this, I spent around thirty years in security in the UK, as a practitioner, a CISO and a founder. I was on the OWASP Board, created the OWASP O2 Platform, and organised the OWASP Summits in Lisbon in 2011 and Woburn in 2017. I have written ten books on Leanpub, on security, DevSecOps and developers.
>
> What connects it all: agents should get access, not free rein; what they do should be on the record; and the people who create the value, the experts, the researchers and the readers, should be the ones it pays.

**Short bio (50 words)**:

> Dinis Cruz is the founder of sgit.ai, Git for encrypted vaults, and of the SGit Newsroom, and co-founder of RiskMandate, which writes behaviour policies for AI agents. He has spent around thirty years in security in the UK as a practitioner, CISO and founder, and is a former OWASP Board member.

**Long bio (about 130 words)**:

> Dinis Cruz builds tools that let people and AI agents work with sensitive material safely, and writes about it in the open. He founded sgit.ai, Git for encrypted vaults, where files are encrypted on the user's machine and the server sees only ciphertext, and the SGit Newsroom, a publication written from his voice memos by a desk of agents, with every source linked and every version kept. He co-founded RiskMandate, which writes Agent Behaviour Policies: what an agent can reach, what it was allowed to do, and the gap. He has spent around thirty years in security in the UK, as a practitioner, CISO and founder. A former OWASP Board member, he created the OWASP O2 Platform, organised the OWASP Summits in 2011 and 2017, and has written ten books on Leanpub.


The experience entries: founder of sgit.ai, founder and editor of the SGit Newsroom, co-founder of RiskMandate, and founder of The Cyber Boardroom, each linked to its page once the pages exist, so the logos show.

## What this does not claim {#limits}

- **None of the pages exists yet.** These are drafts.
- **A free address is not proof that no page exists** under another address.
- **Some limits are not from LinkedIn's help pages.** The tagline, about and headline limits are from LinkedIn Learning, LinkedIn's blogs and guides; check them in the editor.
- **The founding years and locations are not on the sites.** The drafts say London, from my GitHub profile.
- **RiskMandate's text is not final** until it is agreed with my co-founder.

If you have set up pages for a family of small companies and have advice, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. LinkedIn's help pages, read that day by a research agent: [creating a page](https://www.linkedin.com/help/linkedin/answer/a543852), [who can create one](https://www.linkedin.com/help/linkedin/answer/a726850), [showcase pages](https://www.linkedin.com/help/linkedin/answer/a570165), [images](https://www.linkedin.com/help/linkedin/answer/a563309), [newsletters](https://www.linkedin.com/help/linkedin/answer/a591266), and the [industry codes](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/industry-codes-v2). The companies, from their own sites: [sgit.ai](https://sgit.ai/about/index.html), [riskmandate.ai](https://riskmandate.ai/about.html), [abp.sgit.ai](https://abp.sgit.ai/), and this site's [about page](/about/index.html), [articles/ids.json](/articles/ids.json) and [shipped](https://newsroom.sgit.ai/shipped/index.html). Related: [what can your agent reach?](/articles/what-can-your-agent-reach.html), [your own newsroom](/articles/your-own-newsroom.html). Written up and checked by this site's agent; the editorial responsibility is mine.
