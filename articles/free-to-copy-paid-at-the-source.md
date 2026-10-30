# Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed, sgit.ai

> I think we have hit on a commercial model almost by accident. This newsroom, and the book's website, already charge per use: every reader starts with £5 of credit, and each page draws a few pence from it. Now apply that to our behaviour policies and hooks. They are open, CC BY 4.0 and Apache 2.0, and anyone may copy them. But a hook is code: Claude Code's own documentation says a plugin "can execute arbitrary code on your machine with your user privileges". Taking one from a website you do not know is like downloading software from unknown sources, and a company will not do it. So the official website, with its brand, its authority, its usability and its trust, is where people will come, even for something free to copy, and it can charge per use there: a customer with £50 of credit might pay £1 for the page with a hook on it. To earn that, it cannot be us saying "trust us". The policies we publish, the hooks above all, should be reviewed and audited by others, with the scanners and services that now exist for skills and plugins, and signed with our keys. The price is something to discover.

*Source: <https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed

# Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.1.0, 2 versions](versions/free-to-copy-paid-at-the-source.md) · [newsroom v0.12.158](https://newsroom.sgit.ai/admin/versions.html) · business-modelsopen-sourceagent-behaviour-policyhookstrustarticle

***Abstract:** I think we have hit on a commercial model almost by accident. This newsroom, and the book's website, already charge per use: every reader starts with £5 of credit, and each page draws a few pence from it. Now apply that to our behaviour policies and hooks. They are open, CC BY 4.0 and Apache 2.0, and anyone may copy them. But a hook is code: Claude Code's own documentation says a plugin "can execute arbitrary code on your machine with your user privileges". Taking one from a website you do not know is like downloading software from unknown sources, and a company will not do it. So the official website, with its brand, its authority, its usability and its trust, is where people will come, even for something free to copy, and it can charge per use there: a customer with £50 of credit might pay £1 for the page with a hook on it. To earn that, it cannot be us saying "trust us". The policies we publish, the hooks above all, should be reviewed and audited by others, with the scanners and services that now exist for skills and plugins, and signed with our keys. The price is something to discover.*

Free to copy, paid at the source: the policy and its hook are open; the official site adds provenance and a signature.

## In short

- **We already charge per use.** Every page on this newsroom draws a few pence from prepaid credit.
- **Our policies and hooks are open.** Anyone may copy them, fork them, run them.
- **But a hook is code.** It runs on your machine, with your permissions.
- **So the source matters.** A company will not run code from a website it does not know.
- **The official site can charge per use, even for open content.** £1 a page from £50 of credit, say.
- **To earn it, others must review it.** Scanners, audits, and a signature from our keys.
- **The price is to discover.** High or low, it is what customers are happy to pay.

## We already charge per use

This is already running. On this newsroom every reader starts with £5 of credit, and each page they read draws from it: 10p for a new article read to the end, 5p for an older one, less for other pages, and in proportion to how far you read. You can set the price of a page from free to double, or refuse it, and the balance can go below zero; when you want to, you top up with a £5 payment link, which has been live since 11 October. The book's website runs the same meter. I wrote about why in [paying after the value](paying-after-the-value.md): you pay for what you have already read, not for what you hope to read.

What I had not seen until now is how far that goes. It is a way to earn from the traffic to a website, whatever the website holds, and it works even when what it holds is free to copy.

## Open, and still worth coming to

Everything we publish about Agent Behaviour Policies is open: the vocabulary and the policies under CC BY 4.0, the code under Apache 2.0. Anyone can take a policy or a hook and use it. [The fork next door](the-fork-next-door.md) argued that this is what protects our customers: if we stop delivering, someone else can carry on.

But think about what a policy is for. Some of our policies are code. The hook in [a leak without breaking the policy](a-leak-without-breaking-the-policy.md) runs on every tool call an agent makes. Claude Code's own documentation is plain about what that means: "A Claude Code plugin you install can execute arbitrary code on your machine with your user privileges", and hooks "are shell commands that run with your full user permissions". It also says "A marketplace's name tells you who publishes the catalog, not what each plugin in it does."

So a copy of our hook on a website you do not know is like downloading software from an unknown source. It might be the same text. It might not. From a company's point of view, that is not a risk worth taking for something that sits in the path of every action its agents take. They will come to the official site: the one with the brand, the authority, the current version, and the trust.

## Charging where the trust is

That is where the model is. Even when someone uses the content under its open licence, even when all they are doing is using the website to find the policy or the hook they need, the use can be metered, and charged per use. The price can be quite different from a news article. A customer who starts with £50 of credit might pay £1 for the page with a reviewed hook on it, and draw the credit down as they use the site. Or it might be much less. That is the question to discover with [our first customers](our-first-customers.md): what they are willing to pay, and what they are happy with.

It does not conflict with [hooks are kernel code](hooks-are-kernel-code.md), which said nobody should pay to run a hook. Running it stays free, and so does copying it. What is metered is the visit to the source: the page where you get the current, reviewed, signed version, with its record.

People already pay for this in software. Red Hat says "A Red Hat subscription allows customers to download Red Hat tested and certified enterprise software", and its products "are backed by a dedicated Product Security team". Docker runs a Verified Publisher programme, "a paid subscription program that provides high-quality images from commercial publishers verified by Docker". The reason is the same one: Sonatype reports that "Throughout 2025, Sonatype identified more than 454,600 new malicious packages".

## Not "trust us"

The official site only deserves that trust if it is not just us saying "trust us". So the policies we publish, and the hooks above all, should be reviewed and audited by others, and the record published next to them.

There is now a whole set of services for this, built for agent skills and plugins, and we should use them, paid or free:

- **Cisco's Skill Scanner**, open source, a "Security Scanner for Agent Skills", which says of itself that it "provides best-effort detection, not comprehensive or complete coverage".
- **Snyk's Agent Scan**, formerly Invariant's mcp-scan, which scans "agent components on your machine for prompt injections and vulnerabilities".
- **NVIDIA's SkillSpector**, a "Security scanner for AI agent skills", which we used in [a skill behaviour policy](skill-behaviour-policy.md); and NVIDIA's NeMo Guardrails and garak, its guardrails toolkit and its "LLM vulnerability scanner".
- **Socket**, whose audits now appear on the skills.sh registry, and **Anthropic's community plugin marketplace**, where every plugin has "passed automated security scanning".

No scanner is enough on its own. When we ran NVIDIA's scanner over a skill that reads your chat history, searches HackerNews and sends a report to Slack, it said "SAFE", and the skill had the whole lethal trifecta, honestly described. A scanner and a policy answer different questions. So the record should hold both: what the scanners found, and what a person who reviewed it, by name, signed off.

## Signed, so the source can be checked

The last piece is the one that turns the brand into something a machine can verify. Every policy and hook we publish should be signed with our keys, as [PKI everywhere](pki-everywhere.md) argued for everything we send, and the keys should be in a register anyone can check. The software world has the tools: Sigstore, where signing events are "recorded in a tamper-resistant public log", and SLSA, where a package at level 1 "has provenance showing how it was built". Then a copy found anywhere can be checked against the source, and the source is where the review, the signature and the current version live.

## What this does not claim

- **The prices are not set.** £1 a page is an example; the right price is to discover.
- **No policy is audited yet.** The reviews and signatures are what we will do next.
- **Scanners miss things.** Cisco's says so itself; ours rated a risky skill safe.
- **Copying stays free.** The licences do not change.
- **The second meter is the book's site.** Both are ours, and small.

## Where this comes from

A voice memo of 20 October 2026. Claude Code's [plugin security page](https://code.claude.com/docs/en/plugins/security). [Cisco's Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), [Snyk's Agent Scan](https://github.com/snyk/agent-scan), [NVIDIA's SkillSpector](https://github.com/NVIDIA/SkillSpector), [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) and [garak](https://github.com/NVIDIA/garak), and [Anthropic's community plugins](https://github.com/anthropics/claude-plugins-community). [Red Hat's subscription FAQ](https://www.redhat.com/en/about/subscription-model-faq), [Docker's Verified Publisher programme](https://docs.docker.com/docker-hub/repos/manage/trusted-content/dvp-program/), and Sonatype's [2026 report on open source malware](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware). [Sigstore](https://docs.sigstore.dev/about/overview/) and [SLSA](https://slsa.dev/spec/v1.0/levels). Related: [paying after the value](paying-after-the-value.md), [the fork next door](the-fork-next-door.md), [hooks are kernel code](hooks-are-kernel-code.md), [a skill behaviour policy](skill-behaviour-policy.md), [PKI everywhere](pki-everywhere.md), [our first customers](our-first-customers.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#free-to-copy-paid-at-the-source)

### Builds on

- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [The fork next door: why open source protects founders, customers and investors from each other, why forks only take hold when someone stops executing, and why a maturing company should give its explorers a way out](the-fork-next-door.md) Founders, customers and investors are each protected from the others because anyone can fork; forks take hold only after a breakdown.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [Our first customers: an early access programme for Agent Behaviour Policies, with credit to spend, a start-here site, daily follow-up, and a list for the next batch](our-first-customers.md) Agent Behaviour Policies move to execution: a first batch of customers with credit, a start-here site, daily follow-up, and a list for the next batch.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.

### Continued by

- [Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue](selling-less-code.md) The economics of customised open source: the customer pays for the features they use, the maker certifies it, and the pipeline is tied to revenue.
- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [Agent Behaviour Policies move to the Open Security Summit: the first hosted project of a community interest company, with RiskMandate as a founding contributor](agent-behaviour-policies-move-to-the-open-security-summit.md) The Agent Behaviour Policy moves to the Open Security Summit CIC as its first hosted project, with a charter and an independent steering majority to come.
- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 228 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=228)

**Posting this article on LinkedIn?** The cover is [free-to-copy-paid-at-the-source.jpg](banners/free-to-copy-paid-at-the-source.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html)*
