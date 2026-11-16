---
title: The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with one gateway agent that alone touches Gmail, a digital twin of the mailbox in a vault that people and agents work on together, signed proposals, approvals and even reads on append lanes, and behaviour policies at five altitudes
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: The time has come to build our own email connector. We have tried using Gmail through the usual connectors, and it is just too messy, and from a security point of view it is a mess: no enforcement, no way to apply policies, every agent given access to everything, as we did for a demo, and either I click allow all the time or I authorise everything, with no context in the decision. So here is the architecture of an email agentic cell. The user connects Gmail through Google's own OAuth, choosing how much to give, and features and agents switch on per tier. One gateway agent alone holds the token: it syncs the mailbox into a digital twin in a vault, and it sends only actions that were approved and pass the policy. Everyone else, people in the browser, in the iPhone CRM app or in Claude, and agents for triage, drafting and the CRM, work on the twin, and propose actions on an append lane. That gives a clean separation, an air gap between reading an email and sending one, and it lets many people collaborate on one inbox while only one gateway receives and sends. Every proposal, approval, send and even read is signed with a key and ordered on an append lane, a cryptographic sequence of events without a commit per click. And behaviour policies apply at five altitudes, from the OAuth grant to what a single email may say: recipients, languages, templates, rates. It starts in the CRM app, as an AgentiCCells cell, under RiskMandate's Google project.
version: v0.14.122
license: https://creativecommons.org/licenses/by/4.0/
tags: email, gmail, agents, vaults, pki, abp, agenticcells, crm, architecture, article
status: published
---

!shot gml-arch.webp | images/ | The email agentic cell: one gateway touches Gmail; people and agents work on a twin in a vault. | architecture

## In short {#in-short}

- **Connecting Gmail to agents the usual way is a mess:** no enforcement, no policies, everything allowed, or a click on every action.
- **One gateway agent alone touches Gmail:** it syncs in, and sends only approved, policy-checked actions.
- **A digital twin of the mailbox in a vault:** people and agents read it and propose actions on lanes.
- **Many people, one inbox:** collaborate on the twin; only the gateway receives and sends.
- **Everything signed, even reads,** on append lanes: a sequence of events, not a commit per click.
- **Behaviour policies at five altitudes,** from the OAuth grant to what one email may say.
- **It starts in the CRM app,** as an AgentiCCells cell, under RiskMandate's Google project.
- **A brief for the team that builds it:** fifteen features, from an inbound firewall to a calendar twin.

## Why not the usual connector {#why}

We have tried using Gmail through the connectors that come with AI assistants, and the reality is that it is too messy and not good enough. From a security point of view it is a mess. There is no enforcement. There is no way to apply policies. To make a demo work, we ended up giving every agent permission to connect to everything. And to keep it usable, I either click allow on every action, or I authorise all of it, neither of which makes sense. Worst of all, there is no context in the decision: what is right for one email is wrong for the next, and the prompt cannot tell them apart ([the grant, not the prompt](/articles/the-grant-not-the-prompt.html)).

That is a good example of something that does not work. So we will build our own, because we can, and because only then can we enforce Agent Behaviour Policies, and put them all the way up, on the behaviour of the email itself.

## One gateway, a twin, many hands {#architecture}

The design rests on one idea: only one agent ever touches Gmail.

- **The gateway agent** holds the Google token and nothing else does. It syncs the mailbox in, and it sends out only actions that were approved and pass the email policy.
- **The digital twin** is the mailbox as files in a vault: one file per message, threads, labels as data, and the attachments, all encrypted, with a read key given only to those allowed to read ([how a vault works](/articles/how-a-vault-works.html)).
- **The lanes** carry everything that changes: an actions lane for proposals (reply, label, archive, forward), an approvals lane for signatures, a reads lane for receipts, and an outbox with what was sent and its result ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).
- **Many hands** work on the twin: people in the browser, in the iPhone CRM app or in Claude, and agents for triage, drafting and the CRM.

That gives a much cleaner separation, and an air gap between reading an email and sending one that the policy can see. It also changes how an inbox works: many people can collaborate on the same inbox, and only one gateway has the power to receive and to send.

## Four flows {#flows}

!shot gml-flows.webp | images/ | Four flows: connect, receive, work together and send, each step signed, each send through the gateway. | process

- **Connect.** The user consents on Google's own screen, choosing a tier: metadata, read, compose, send. The app gets only those scopes, and features and agents switch on per tier. Revoking is one click, at Google or in the app.
- **Receive.** Gmail nudges the gateway when something changes, through a watch and a Pub/Sub topic; the gateway reads the changes from the history and writes them into the twin. Google warns that nudges can be delayed or lost, so the gateway also re-checks on a timer ([Gmail push notifications](https://developers.google.com/gmail/api/guides/push)).
- **Work together.** People and agents read the twin; triage links messages to people and introductions in the CRM; drafts are written in our voice and language; nothing changes in Gmail.
- **Send.** A proposal reaches the approvals lane; a person signs it, or a signed policy allows it; the gateway checks the email policy and sends; the result is written back to the twin and to the CRM ([a CRM for us and for our agents](/articles/a-crm-for-us-and-our-agents.html)).

## Signed, even when you read {#signed}

All of this runs on keys. Every proposal, approval and send is signed by whoever made it, person or agent, and so is every email that leaves, the way our email agents already sign what they draft ([a signed email from the agent](/articles/signed-email-from-the-agent.html)). We can go further and sign reads: who read what, and who saw what, as receipts on the reads lane. That leaves a digital trail of attention, not only of action.

This is where we need to use append lanes strategically. We do not want a commit for every click; an append lane gives us a cryptographic sequence of events instead, each entry signed and connected to the one before, so that when lanes are merged we can still work out exactly what happened, in what order, and who did it ([messaging-fs](/articles/messaging-fs.html)).

## Behaviour policies at five altitudes {#altitudes}

!shot gml-altitudes.webp | images/ | Behaviour policies at five altitudes, from the OAuth grant to what a single email may say. | concept

The policy model is the same one we use everywhere ([where assist becomes execute](/articles/where-assist-becomes-execute.html)), enforced at five levels:

1. **The OAuth grant:** which Gmail scopes the user gave. Enforced by Google.
2. **Who holds the token:** one gateway agent. Enforced by where the key lives.
3. **What each agent may do:** read the twin, propose, approve or send, per agent and per key. Enforced on the lanes.
4. **What an email may be:** recipients and domains, languages, templates, attachments, how many a day, first contact or reply. Checked by the gateway before every send.
5. **Who approves:** a person signs consequential sends; routine ones go by a signed policy. Recorded on the approvals lane.

The fourth altitude is the new one. Today's connectors cannot say "this agent may send a reply in Portuguese to an existing correspondent, using this template, but never a first contact". Ours can, and that is what makes the few emails I want to send automatically safe to automate.

## The features to build {#features}

!shot gml-features.webp | images/ | The email cell's features: from a shared inbox with roles to an inbound firewall, signed mail and a calendar twin. | concept

This article is the brief for the team that builds it, so here is the whole of it, not the first slice:

- **A shared inbox, with roles.** Many people and agents on one inbox: readers, drafters, approvers, and one sender. A team's inbox stops being one person's burden.
- **An inbound firewall.** Agents never read raw email. They read a cleaned copy in which links, hidden text and likely prompt injections are flagged, so a hostile email cannot instruct an agent ([the grant, not the prompt](/articles/the-grant-not-the-prompt.html)).
- **Signed outbound mail.** Every email carries the signature of its agent and its person, with a QR code and a page where the recipient can check who sent it and on whose behalf ([a signed email from the agent](/articles/signed-email-from-the-agent.html)).
- **Vault links, not attachments.** A file goes out as a link to an encrypted vault with its own key: revocable, versioned, and with signed reads, so you know it was opened.
- **Approve anywhere.** On the iPhone with Face ID, by voice from VoiceDebrief, or in the browser; each approval a signature on the lane.
- **A policy simulator.** Run a new policy against last month's mail before it goes live, and see what it would have blocked, held or allowed.
- **Synthetic recipients.** Drafts go first to synthetic people who read, answer and push back, so the team sees the reply before a real person does.
- **Templates and voice.** A template for each kind of contact, in each language, with images and infographics inline, written in the voice of the person who signs.
- **Follow-ups that run themselves.** "No reply in five days" becomes a drafted nudge, waiting for approval, linked to the person and the introduction in the CRM.
- **Time travel.** The twin is versioned: see the inbox as it was on any day, and replay who read, proposed, approved and sent what.
- **Data-loss checks.** No secret, key or private note leaves in an email; the gateway refuses and says why.
- **A calendar twin.** The same pattern for Google Calendar: invites drafted by agents, accepted by a person, every change signed.
- **A kill switch.** One tap stops the gateway, and nothing sends until a person starts it again ([who owns the stop button](/articles/who-owns-the-stop-button.html)).
- **More than Gmail.** Outlook, IMAP and a company's own mail server, behind the same gateway and the same policies.
- **Inbox analytics.** Who waits on whom, how long replies take, which introductions went nowhere.

## Where it lives {#where}

This is a good example of an [AgentiCCells](/articles/the-intersection.html) cell: an email agentic cell that a team can switch on, starting with ours. It needs an OAuth app registered with Google, and the natural place is RiskMandate's Google project, or the one we already have for The Cyber Boardroom. It will run in three places: in the browser, in the iPhone CRM app, which needs an email component anyway, and alongside Claude. It may become an app of its own later; it starts inside the CRM.

## What Google requires {#google}

Google's own rules shape the plan. Sending (`gmail.send`) is a sensitive scope, which needs verification but not a security assessment. Reading (`gmail.readonly`) is a restricted scope, and an app that stores restricted data on servers needs an annual security assessment under the App Defense Alliance's framework ([Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes)). Before verification, an app is limited to 100 test users. So we start in testing, with our own inboxes, and decide on verification when the cell is ready for customers. Whether a twin encrypted on the user's side counts as storing restricted data on servers is a question to settle with Google's process, not to assume.

## A build order for the team {#plan}

1. **Our own inboxes first:** register the OAuth app in testing, build the gateway and the twin, and sync one mailbox.
2. **The lanes and the signatures:** actions, approvals, reads and the outbox, each entry signed.
3. **The email policy:** recipients, languages, templates and rates, checked before every send; first contacts always approved by a person.
4. **The CRM app's email component,** on the twin, on the iPhone and in the browser.
5. **The first automated sends:** the few routine emails I want to automate, under a signed policy.
6. **Then the cell:** offered to teams, with verification when it leaves testing.

## What this does not claim {#limits}

- **This is a brief and an architecture** for the team that builds it; none of it is built yet.
- **Google's verification and assessment requirements** are from Google's documentation and integrators' guides, read on 16 November 2026; the details, and how they apply to an encrypted twin, need confirming.
- **Signed reads record that a key opened a message,** not that a person understood it.

## Where this comes from {#sources}

My own thinking, 16 November 2026, after trying to use Gmail through assistants' connectors. Google: [Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes), [push notifications](https://developers.google.com/gmail/api/guides/push) and [restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification); integrators' guides from [Nylas](https://developer.nylas.com/docs/dev-guide/provider-guides/google/google-verification-security-assessment-guide) and [Unipile](https://www.unipile.com/gmail-api-push-notifications/). Earlier on this site: [a signed email from the agent](/articles/signed-email-from-the-agent.html), [messaging-fs](/articles/messaging-fs.html), [the inbox team as a recipe](/articles/the-inbox-team-as-a-recipe.html), [the grant, not the prompt](/articles/the-grant-not-the-prompt.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [how a vault works](/articles/how-a-vault-works.html), [a CRM for us and for our agents](/articles/a-crm-for-us-and-our-agents.html), [the intersection](/articles/the-intersection.html), [who owns the stop button](/articles/who-owns-the-stop-button.html).
