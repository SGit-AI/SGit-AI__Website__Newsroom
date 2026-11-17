# Working with WizPress: how the AI operating system for newsrooms, built in Faro, and our open-source trust stack fit together, WizPress doing the production, from the inbox to the draft to the CMS, and our layer making every article carry its own proof, with an evidence vault per story, a behaviour policy per agent, a journalist's signature and signed responses, and a thirty-day pilot with one regional newsroom, sgit.ai

> I am with WizPress today, and I think we fit together unusually well. WizPress, built in Faro and led by Nuno Costa, a former journalist and newsroom manager, describes itself as the AI operating system for newsrooms: it monitors inboxes, the web and trends, captures and transcribes interviews, turns press releases and documents into drafts with a fact-checking agent and house style, and publishes to WordPress or any CMS, with the journalist deciding. It already works with local, national and specialist media in Europe and the Middle East. What we have been building is the layer underneath: how a reader can see who wrote an article, who checked it and who stands behind it. At PrompTugal.news we now describe every piece with five axes, origin, research, claims, review and external responses, and a ladder from "published by an agent" to "on the record". WizPress's four stages map onto those axes almost one to one. So here is how we could work together: a behaviour policy for every agent that reads a newsroom's inbox; an encrypted evidence vault per story for recordings, transcripts and documents; a provenance record exported with every draft; the journalist's signature on the version readers see, with any later change a signed difference; signed responses from the people a story is about; and a network of local newsrooms whose stories climb, with their proof, to the region and the country. And a first step: one regional newsroom, thirty days, in the open.

*Source: <https://newsroom.sgit.ai/articles/working-with-wizpress.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Working with WizPress: how the AI operating system for newsrooms, built in Faro, and our open-source trust stack fit together, WizPress doing the production, from the inbox to the draft to the CMS, and our layer making every article carry its own proof, with an evidence vault per story, a behaviour policy per agent, a journalist's signature and signed responses, and a thirty-day pilot with one regional newsroom

# Working with WizPress: how the AI operating system for newsrooms, built in Faro, and our open-source trust stack fit together, WizPress doing the production, from the inbox to the draft to the CMS, and our layer making every article carry its own proof, with an evidence vault per story, a behaviour policy per agent, a journalist's signature and signed responses, and a thirty-day pilot with one regional newsroom

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/working-with-wizpress.md) · [newsroom v0.14.140](https://newsroom.sgit.ai/admin/versions.html) · wizpressnewsroomsjournalismprovenancepkivaultspartnershipsportugalarticle

***Abstract:** I am with WizPress today, and I think we fit together unusually well. WizPress, built in Faro and led by Nuno Costa, a former journalist and newsroom manager, describes itself as the AI operating system for newsrooms: it monitors inboxes, the web and trends, captures and transcribes interviews, turns press releases and documents into drafts with a fact-checking agent and house style, and publishes to WordPress or any CMS, with the journalist deciding. It already works with local, national and specialist media in Europe and the Middle East. What we have been building is the layer underneath: how a reader can see who wrote an article, who checked it and who stands behind it. At PrompTugal.news we now describe every piece with five axes, origin, research, claims, review and external responses, and a ladder from "published by an agent" to "on the record". WizPress's four stages map onto those axes almost one to one. So here is how we could work together: a behaviour policy for every agent that reads a newsroom's inbox; an encrypted evidence vault per story for recordings, transcripts and documents; a provenance record exported with every draft; the journalist's signature on the version readers see, with any later change a signed difference; signed responses from the people a story is about; and a network of local newsrooms whose stories climb, with their proof, to the region and the country. And a first step: one regional newsroom, thirty days, in the open.*

WizPress does the production; we add the trust underneath: a policy, a vault, the claims, a signature.

## In short

- **WizPress is the AI operating system for newsrooms:** monitor, capture, draft, publish, with the journalist deciding.
- **We build the trust layer underneath:** who wrote it, who checked it, who signs it.
- **The two fit almost one to one:** WizPress's stages are our five provenance axes.
- **Six ways to work together,** from evidence vaults to signed responses to a local news network.
- **A first step:** one regional newsroom, thirty days, in the open.
- **Our side is open source,** free to adopt; WizPress keeps its product and its customers.

## WizPress

[WizPress](https://wizpress.io/) was created in 2025 and is led by Nuno Costa, a former journalist and newsroom manager, with a team of about ten, supported by the Dengun product studio, at the Tech Campus in Faro. It calls itself the AI operating system for newsrooms, and the description is accurate:

- **Monitor:** it connects to a newsroom's email, so press releases arrive in WizPress and are scored against a keyword profile, and it watches web pages and trends.
- **Capture:** recordings on the phone with automatic transcription, audio and video uploads, documents and images.
- **Draft:** AI drafts from press releases, emails and documents, with the source beside the draft, a fact-checking agent, house-style rules and an assistant for rewrites and angles.
- **Publish:** one click to WordPress, or any CMS through its API.

Its customers are local, national and specialist media, in Portugal and beyond, and its own line is the right one: "The decision is always the journalist's." The goal "is not to replace journalism, but to free up time for it."

## What we build

We have spent the last months on the other half of the problem: when an AI can write five versions of the same article in a minute, how does a reader know what they are reading? At PrompTugal.news, the newsroom we ran at Web Summit, we now answer with a profile, not a label ([who wrote this, who checked it, who signs it](https://promptugal.news/articles/who-wrote-this-who-checked-it-who-signs-it.html)): five axes, each recorded with who and when. Origin: did a person write it, dictate it, or brief an agent? Research: whose, and how? Claims: how many facts, each with its evidence. Review: which agents and models checked it, which person edited it, with the diff. External: signed responses from the people it is about. And a ladder, from published by an agent, to sourced, to verified by several models, to signed by a person, to on the record.

Underneath that sit the pieces of our stack: sgit's encrypted, versioned vaults ([how a vault works](how-a-vault-works.md)); a key for every person, and QR codes to pass keys and links safely ([a secret is a QR code](a-secret-is-a-qr-code.md)); and behaviour policies that say what each agent may reach ([where assist becomes execute](where-assist-becomes-execute.md)). All of it open source.

## How we fit together

WizPress's four stages map onto those five axes almost one to one. That is the opportunity: WizPress already keeps the journalist in charge; our layer lets the reader see it.

1. **A behaviour policy for the inbox.** WizPress reads newsrooms' email, which is the most sensitive thing an agent can touch. A written, measured policy, what it may read, what it may never do, such as send, makes that easy for a publisher to approve ([the email agentic cell](the-email-agentic-cell.md)).
2. **An evidence vault per story.** Recordings, transcripts, press releases and documents behind an article, kept in an encrypted vault the newsroom owns, opened by an editor or a lawyer with a key, never by the host. Sources stay protected, and the evidence for every claim stays one link away ([every story has an address](every-story-has-an-address.md)).
3. **A provenance record with every draft.** WizPress already knows the origin, the source beside the draft and what its fact-checking agent found. Exported as a small record, that is most of the five axes, ready to show beside the article.
4. **The journalist's signature.** The journalist signs the version readers see with their own key; any change after that, a headline included, is a signed difference in public ([signed by the source](signed-by-the-source.md)).
5. **Signed responses.** The people and companies a story is about are asked to respond, and their answers, signed, sit on the article. On the record, not in the comments.
6. **A network of local newsrooms.** WizPress's customers are exactly the local and regional media that PrompTugal.news is designed around: news filed where it happens, climbing to the region and the country with its proof, and local outlets certifying big outlets' stories about their patch ([local trust, certified upwards](local-trust-certified-upwards.md)).

## A first pilot

A first pilot: one regional newsroom, thirty days, keys, vaults, provenance, signatures, responses.

The way to find out is small and in the open. One WizPress customer, one section, thirty days. In the first week, keys for its journalists and an evidence vault per story. In the second, WizPress exports a provenance record with each draft. In the third, journalists sign what they publish, and a provenance page sits beside each article. In the fourth, the people the stories are about are asked for signed responses. And we measure: time per article, corrections, and what readers make of it.

The newsroom keeps using WizPress exactly as it does today.

## What each side brings

- **WizPress:** a working product, paying newsrooms, the journalism and newsroom experience of its founder, and the trust of local media in Portugal and beyond.
- **Us:** an open-source trust stack, vaults, keys, signatures and behaviour policies, already running in our own newsrooms, and PrompTugal.news as a live test bed.
- **Both:** a story that matters now, that AI in newsrooms can make journalism more trustworthy, not less, if the proof travels with every article.

## What this does not claim

- **This is a proposal,** written on the day we met; nothing is agreed.
- **WizPress's figures and claims are its own,** from its website.
- **The provenance model is new,** and is itself still climbing its own ladder at PrompTugal.news.

## Where this comes from

[wizpress.io](https://wizpress.io/), read on 17 November 2026: its product, pricing, team and customers as it describes them. PrompTugal.news, [who wrote this, who checked it, who signs it](https://promptugal.news/articles/who-wrote-this-who-checked-it-who-signs-it.html), 17 November 2026. Earlier on this site: [how a vault works](how-a-vault-works.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [where assist becomes execute](where-assist-becomes-execute.md), [the email agentic cell](the-email-agentic-cell.md), [every story has an address](every-story-has-an-address.md), [signed by the source](signed-by-the-source.md), [local trust, certified upwards](local-trust-certified-upwards.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#working-with-wizpress)

### Builds on

- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with one gateway agent that alone touches Gmail, a digital twin of the mailbox in a vault that people and agents work on together, signed proposals, approvals and even reads on append lanes, and behaviour policies at five altitudes](the-email-agentic-cell.md) Our own email connector: one gateway agent touches Gmail, everyone else works on a signed twin of the mailbox in a vault, with policies at five altitudes.
- [Every story has an address: a design proposal for PrompTugal.news as a ground-up newsroom, where news is filed where it happens and climbs to the region and the country with its proof, mocked up from the live data of 19 local editions](every-story-has-an-address.md) A design proposal for PrompTugal.news as a ground-up newsroom: every story filed at an address, climbing with its proof. Mockups from live data.
- [Signed by the source: asking the people and companies we quote to sign that we represent them correctly, why that is cheaper than every reader checking, and how readers go on the record too](signed-by-the-source.md) Ask the people and companies we quote to sign that we represent them fairly: one signature instead of every reader checking.
- [Local trust, certified upwards: why local and niche publishers should take everything that has become commodity, certify the big outlets' stories about their patch and be paid for it, and why stories, like software, need someone to maintain them](local-trust-certified-upwards.md) Local and niche publishers own the trust: take in commodity, certify the big outlets' local stories for pay, and keep stories maintained.

### Continued by

- [Paid by the read: a proposal to news editors who want more revenue from the journalism they already make, without another subscription, the evidence on micropayments and why it mostly failed, the meter that charges by how much of a page was read and runs in the reader's browser, free for any publisher, a revenue share when PrompTugal.news carries a newsroom's stories with their source, and the associations we should be talking to in the UK and Portugal](paid-by-the-read.md) A proposal to news editors: earn from the read, not the subscription, with free client-side code, a revenue share and the associations.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 455 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=455)

**Posting this article on LinkedIn?** The cover is [working-with-wizpress.jpg](banners/working-with-wizpress.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/working-with-wizpress.html)*
