---
title: Signed by the source: asking the people and companies we quote to sign that we represent them correctly, why that is cheaper than every reader checking, and how readers go on the record too
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: Every article here is built on sources: papers, pages, government notices, company statements. Today, the only way to know that an article represents a source correctly is for someone downstream to check: a domain expert, or an agent with the right context, loading the article and every reference and mapping one to the other. That costs hours of human time or a lot of tokens, it is repeated by every reader, and it is done by someone who is not the best person to judge. The best person is the source. So I want to ask the people and companies we quote to review how we used their work, add a caveat where needed ("70%, but only of these"), and sign it with a key their own website vouches for. Every reader after that checks one signature and how much they trust the signer. Where an article earns money, the source should be paid to verify, as some journals now pay reviewers. Most of the pieces exist: the Pen on every article, signed notes checked against the register at pki.sgit.ai, sign in with a key, and a way for a domain to prove which key is its own. In my memo I said pki.sgit.ai's latest work was federation between organisations; it is not, and that part is still a proposal. Readers and researchers can go on the record too, with signed reviews and notes. I want to start with individuals, then companies.
version: v0.13.67
license: https://creativecommons.org/licenses/by/4.0/
tags: provenance, signatures, pki, peer-review, economics, article
status: published
---

!shot vs-economics.webp | images/ | Who should check a claim: every reader today, or the author of the source signing it once. | concept

## In short {#in-short}

- **Every article stands on sources.** Today, checking that they are represented correctly falls on the reader.
- **That is expensive, repeated and done by the wrong person.** Hours of expert time or a lot of tokens, for every reader.
- **The best person to check is the source.** Ask them, let them add a caveat, and let them sign it.
- **One signature replaces many checks.** A reader or an agent verifies the signature and the signer's standing.
- **Pay for it where it earns money.** As some journals now pay reviewers.
- **Most of the pieces exist.** The Pen, signed notes, a register of keys, and domains that prove their key.
- **Federation between organisations does not exist yet.** My memo said it did; it is a proposal.
- **Readers go on the record too.** Signed reviews and notes, kept with the article.

## Who checks the references? {#who-checks}

Everything we write here is built on other people's work. A paper, a release note, a government notice, a company's statement, a post. The article quotes it or, more often, summarises it, and the summary is where things go wrong: a number taken out of its context, a caveat dropped, a claim that was true of one group stated as if it were true of all.

How does a reader know? Today, they have to check. A domain expert, or an agent with the right context and enough budget, has to load the article, load every reference, read both, and map one to the other. That is a lot of work. It is hours of human time, or a lot of tokens. It is repeated by every reader who wants to be sure. And it is done by somebody who, however capable, is not the best person to say whether the source was represented fairly.

## The source is the best person to judge {#the-source}

The best person is the source: the author of the paper, the team that wrote the release, the company that issued the statement. They know what they meant, and they know which caveat matters.

So here is the idea. When an article uses someone's work, we ask them. We send them the passage, with its hash and the links it relies on, and one question: is this a fair representation of what you said? They can agree. They can disagree. Or, most usefully, they can add the caveat that makes it correct: "yes, 70%, but only of these", or "that was true of the first version, not the second". And then they sign it, with their own key.

!shot vs-workflow.webp | images/ | Signed by the source, the workflow: from the article quoting a source to a reader checking the signature. | process

## Why the economics work {#economics}

The argument is about who does the work, and how many times. Checking downstream is done once per reader, by someone who has to rebuild the context. Checking at the source is done once, by someone who already has it. After that, every reader, human or agent, checks one signature and asks one question: how much do I trust this signer? That is cheap. It is the difference between reading every reference and reading a stamp.

It is also the honest version of something that already happens. Sources correct journalists all the time, by email, privately, after publication. A signed review puts that correction on the record, attached to the passage it is about, before the article is relied on.

And it can be paid. Where an article earns money, the source should be paid to verify it, as some science now pays reviewers: [Biology Open pays £220 a manuscript](https://newsroom.sgit.ai/articles/on-the-record.html), and in its pilot the time to a first decision fell from 37.7 to 5.5 working days. This site's [economics pages](https://newsroom.sgit.ai/economics/paying-the-fact-creator.html) go further, splitting the value behind a reader's payment between the original researcher, the data organisation, the journalist and the outlet, and describing [a fact-certifier as a payable role](https://newsroom.sgit.ai/economics/trust-as-a-service.html), with output that carries consequence if it is wrong. Both pages are designs, not running services. A signed verification from the source is the smallest working piece of them.

## Keys that a website vouches for {#keys}

For a signature to mean anything, a reader has to know whose key it is. The natural place for a company to say "this is our key" is its own website, and for a person, their own domain or their GitHub account.

That part exists. [pki.sgit.ai](https://pki.sgit.ai/) keeps a register of people and their public keys, with my key as its anchor, and [a way to prove](https://pki.sgit.ai/people/how.html) that a domain or an account belongs to a record: a proof line in a file at `/.well-known/pki.sgit.ai.txt` on the website, a DNS TXT record (the pattern Bluesky uses for domain handles), or a public gist. A link between two records counts only when both hold it, and a verifier walks the chain from the key that signed back to a root it pinned itself, never to whatever a list of anchors says. Since 24 October, a site can also [sign readers in with pki.sgit.ai](https://pki.sgit.ai/articles/sign-in-with-pki-sgit-ai-for-sites.html): your key signs a delegation for one browser, at one site, for some uses, until a date.

What does not exist yet is the step I described in my memo as the latest work: federation, where an organisation runs its own register, publishes its keys on its own site, and verifies others and is verified by them. I said that was in pki.sgit.ai's latest pushes. Having read its releases, it is not: the latest were sign-in with a key, delegation and signed shared code. The site's own roadmap says a design with well-known documents, DNS records and a verification endpoint "was proposed in March … and never built". So mutual verification between organisations is the proposal here, not a feature. The register today holds one person's real key, mine, and two agents' keys.

## Readers go on the record too {#readers}

The source signing is one half. The other is that readers and researchers can go on the record as well, with reviews and comments that carry their name and their key.

That is what the newsroom's [Pen](https://newsroom.sgit.ai/articles/a-pen-and-a-key.html) started this week. Every article has one: select words, keep them, comment on them, or send the newsroom a note with the passage it is about. And every note can be signed with a key for that browser, which the register at pki.sgit.ai vouches for, checked against a pinned root in the browser and again when the newsroom reads it. A changed note fails. Today that key is mine; the point is that it does not have to be.

The [Ask](https://newsroom.sgit.ai/search/) pane fits the same picture from the other side. It answers a reader's question only from passages it finds on this site, and cites each one, so every claim can be checked where it came from. If those passages carry the source's signature, the answer inherits it.

Put together, that is a web of trust: sources who sign how they are represented, readers who sign what they think, an article that keeps both, and a reader or an agent that weighs each signature by who made it. [On the record](https://newsroom.sgit.ai/articles/on-the-record.html) set out the case for signed expert opinions; this is the same mechanism pointed at the sources.

## Start small {#start-small}

I want to start doing this with individuals: people whose papers, posts and projects we write about, who already have a domain or a GitHub account, and who can sign with a key in a few minutes. Then companies, which need a key their website vouches for, and a person allowed to use it.

A few rules will matter from the start:

- **Ask before publishing where we can,** and show the source exactly the passage, its hash and its links.
- **Publish the caveat as written.** The point is the source's words, not ours.
- **A refusal is information too.** "We were asked and did not sign" is worth saying, without reading anything into it.
- **A signature is about representation, not truth.** The source signs that we summarised them fairly; it does not make their claim correct.

## What this does not claim {#limits}

- **Nobody has signed one yet.** This is a proposal; no source has reviewed an article here through it.
- **Federation is not built.** Organisations publishing and cross-checking their own registers is a design, proposed and not shipped.
- **The register is small.** One real person key and two agent keys, read on 24 October 2026.
- **The economic case is an argument,** from who does the work and how many times, not a measured cost.
- **Sources have interests.** A source can sign a flattering summary; the signature records who said it, which is why readers' own signed reviews matter.

## Where this comes from {#sources}

My voice memo of 24 October 2026, corrected where the record differs; on [pki.sgit.ai](https://pki.sgit.ai/): its [release history](https://pki.sgit.ai/admin/versions.html) to v0.2.28, [how to prove an account or domain](https://pki.sgit.ai/people/how.html), [sign in with a key, soft and strong](https://pki.sgit.ai/articles/sign-in-with-a-key-soft-and-strong.html), [sign in with pki.sgit.ai, for sites](https://pki.sgit.ai/articles/sign-in-with-pki-sgit-ai-for-sites.html), its [roadmap](https://pki.sgit.ai/roadmap/index.html) and its [directory](https://pki.sgit.ai/directory/index.json); this site's [v0.13.64 release](https://newsroom.sgit.ai/engineering/releases/v0.13.64.html). Related: [a pen and a key](https://newsroom.sgit.ai/articles/a-pen-and-a-key.html), [on the record](https://newsroom.sgit.ai/articles/on-the-record.html), [reviews on the record](https://newsroom.sgit.ai/articles/reviews-on-the-record.html), [PKI everywhere](https://newsroom.sgit.ai/articles/pki-everywhere.html), [who is speaking](https://newsroom.sgit.ai/articles/who-is-speaking.html), [free to copy, paid at the source](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html), [paying the fact creator](https://newsroom.sgit.ai/economics/paying-the-fact-creator.html), [trust as a service](https://newsroom.sgit.ai/economics/trust-as-a-service.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
