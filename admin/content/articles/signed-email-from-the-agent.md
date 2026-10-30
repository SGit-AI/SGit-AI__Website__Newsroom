---
title: Signed by the agent, vouched for by the person: a brief to give every email agent its own key, so each email carries a QR code that proves it is authentic
date: 2026-10-30
author: Dinis Cruz
author_url: about/index.html
summary: Each of us now has an agent that runs our email: it reads, researches, drafts and keeps the records, and a person sends. I just realised we can do something powerful with that. Give each email agent its own key pair, vouched for by its person's key on pki.sgit.ai, and every email it drafts can carry a signature and a QR code that lets the recipient check, in a browser, that the email is authentic: that it came from my one official email agent, acting for me, and has not been changed. We already have the pieces. Our agent sessions make their own keys and publish them. pki.sgit.ai is a register of people and their keys, verified both ways, with signed statements, evidence such as a DNS record or a website file, and delegations signed by a person's key that stop the moment the person withdraws them. Email has signatures today, but DKIM proves the domain's mail server sent the message, not which person or which agent wrote it, and S/MIME and PGP ask the reader to install and trust something. This brief maps out what to build: a key for each email agent and a delegation from its person; a signature over each email's content; a QR code and a link to a verification page that shows who signed it, for whom, and whether that delegation still holds; and the rules for the world we are entering, where agents act for us from our email accounts, one official agent each, so that anything sent on our behalf can be proved, and anything not signed can be questioned.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: email, pki, provenance, agents, identity, signatures, article
status: published
---

!shot se-chain.webp | images/ | From the person to one email: the person's key vouches for the email agent, which signs each email it drafts. | architecture

## In short {#in-short}

- **Each of us has an agent that runs our email.** It drafts; a person sends.
- **Give each email agent its own key,** vouched for by its person's key on pki.sgit.ai.
- **Every email it drafts carries a signature and a QR code** that opens a page to verify it.
- **The check answers three questions:** which agent signed it, for whom, and whether that person still vouches for it.
- **Email signatures today prove less.** DKIM proves the domain; S/MIME and PGP ask the reader to install and trust software.
- **We have the pieces:** session keys, a register of people and keys, signed statements, delegations that can be withdrawn.
- **The rule:** one official email agent per person, so anything sent on our behalf can be proved.

## What changes when an agent writes your email {#why}

The agent behind agent@riskmandate.ai has been drafting my RiskMandate email since September, and since 28 October agent@diniscruz.ai runs the same workflow for my own, as [the inbox team as a recipe](/articles/the-inbox-team-as-a-recipe.html) describes. They read, research, draft and keep the records; I review and send. The [Web Summit team's brief](/articles/web-summit-team-brief.html), published today, gives each of its seven people an email agent too.

That raises a question every recipient will soon ask: was this email written by the person, by their agent, or by someone pretending to be either? Today's [article on a contractor's agent at the Pentagon](/articles/the-contractors-agent-and-three-policies.html) shows what happens when an agent acts with a person's identity and nothing records which one acted. Email is the same problem, outward-facing. The answer is the same too: the agent gets its own identity, and the person vouches for it.

## What email can prove today {#today}

Email already has signatures, and they prove less than people assume:

- **DKIM** signs a message with a key belonging to the sending domain, so a receiving server can tell the message came through that domain's mail system. It says nothing about which person, or which agent, wrote it.
- **S/MIME and PGP** sign a message with a person's key, but the reader needs software that checks it and a reason to trust the key, and in practice few readers have either.

So a recipient has no easy way to check that an email came from me, and none at all to check that it came from the agent I authorised and not from another tool with access to my account.

## The pieces we already have {#pieces}

- **A key for every agent session.** Our agents make their own key pair, keep the private half, and publish the public half beside their role; [agents have an identity now](/articles/agents-have-an-identity-now.html) describes the five steps.
- **A register of people and their keys.** pki.sgit.ai holds signed statements: a person's identity, evidence that ties the key to a website, a GitHub account or a DNS record, and links between records that count only when both sides hold them.
- **Delegations that can be withdrawn.** pki.sgit.ai's sign-in already uses a delegation signed by the person's key for one browser key at one site, either until a date, or only while the person's record lists it, so that withdrawing it stops it at once.
- **Messages and QR codes.** pki.sgit.ai seals messages in the browser into a link whose fragment never reaches a server, and [a secret is a QR code](/articles/a-secret-is-a-qr-code.html) showed two sessions passing keys and messages through QR codes.

## How a signed email would work {#how}

!shot se-flow.webp | images/ | A signed email in five steps: the agent drafts and signs, the person sends, the recipient scans and the page checks. | process

1. **The email agent makes its key,** in its own session, and publishes the public half with its role.
2. **The person delegates to it.** My key signs a statement on pki.sgit.ai: this key is my official email agent, for this address, until this date or while I keep it listed. The agent's record links back.
3. **The agent signs what it drafts.** For each email, it signs the content that matters: the sender and recipients, the date, the subject and the body. The signature, and a short code, go into the email: a line of text, a link and a QR code.
4. **The person sends,** as today. A person stays on every send.
5. **The recipient checks.** Scanning the QR code, or opening the link, loads a verification page that recomputes the hash of what was signed, checks the agent's signature, and checks the delegation chain to my record on pki.sgit.ai: who signed, for whom, whether the delegation still holds, and whether the email was changed.

Nothing has to be installed by the recipient. The check runs in their browser, from public records, against keys that are published and vouched for.

## What the verification page shows {#verify}

- **Signed by** my email agent, its key and its fingerprint.
- **On behalf of** Dinis Cruz, with my record on pki.sgit.ai and its evidence.
- **The delegation,** with its date, and whether it is still listed.
- **The content check:** the hash of what was signed, and whether the email in front of the recipient matches it.
- **What it does not prove:** that I read the email before it was sent, unless I also signed it; and anything about attachments that were not covered.

## The rules {#rules}

- **One official email agent per person, per address.** If I have one, anything sent on my behalf can be proved, and anything not signed by it can be questioned.
- **The agent signs; the person sends.** An email cannot be unsent, so a person stays on every send, and the signature says the agent drafted it.
- **The person can co-sign.** For an email that commits me to something, I add my own signature as well, so the page shows both.
- **Delegations expire.** Each has an end date, or lasts only while listed, and a new agent session publishes a new key.
- **Unsigned is a signal.** Once we sign by default, an unsigned email from one of us is worth a second look.

## What to build {#build}

!shot se-plan.webp | images/ | What exists today and what the brief asks to build, piece by piece. | comparison

- **For pki.sgit.ai:** a delegation statement for an email agent (person, agent key, address, end date), shown on both records.
- **For the email agents:** signing in the drafting step, with the signature, the link and the QR code added to every draft, and the canonical form of what is signed written down.
- **A verification page** on pki.sgit.ai that takes the code from the link or the QR code, and the email's content pasted or dropped in, and shows the checks above.
- **For each of us:** a key on pki.sgit.ai, if we do not have one yet, and evidence tying it to our domain; then a delegation to our email agent.
- **A first test:** my agent at agent@diniscruz.ai, then RiskMandate's, then the Web Summit team's seven.

## What this does not claim {#limits}

- **It is a brief.** Signing in the email agents, the delegation statement and the verification page do not exist yet; the register, session keys, sign-in delegations and sealed messages do.
- **A signature proves who signed and that nothing changed,** not that the content is true.
- **It sits beside DKIM, S/MIME and PGP,** not instead of them; mail servers will keep checking DKIM.
- **Recipients have to choose to check.** The value grows as signing becomes the default for us and the check becomes familiar.

## Where this comes from {#sources}

- My voice memo of 30 October 2026, word for word in `admin/notes/2026-10-30__signed-email/memo-01.md`.
- pki.sgit.ai's own description, [llms.txt](https://pki.sgit.ai/llms.txt), read on 30 October 2026: the register, signed statements, evidence, two-way links, sign-in delegations and sealed messages.
- Related: [the inbox team as a recipe](/articles/the-inbox-team-as-a-recipe.html), [agents have an identity now](/articles/agents-have-an-identity-now.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [PKI everywhere](/articles/pki-everywhere.html), [the contractor's agent](/articles/the-contractors-agent-and-three-policies.html).
