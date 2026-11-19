# Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository, sgit.ai

> Since the sites for Yiheng Wang and Silvio Switha went up, people have been asking for one of their own. Each site is cheap in tokens. What costs is the workflow around it: collecting the person's details and photos, the first round of designs, and the hand-over. So the product is the workflow, and this is the plan, written up by the conductor agent of PrompTugal from my brief and now in my words. A person arrives at a start page, their browser makes a key pair, and they ask for a cell with a signed request and no secrets. I approve it. A welcome pack arrives sealed to their key: a template vault, their own lane to the factory, and a key scoped to creating one vault. They fill their vault over days with photos, words, links, style and a signed consent, then seal its read key to the factory. The factory turns it into a request, I merge it, and the site factory makes the repository, the address, the site and a first round of five designs, written back into their vault. They choose, I approve a GitHub invitation, and they carry on in their own Claude, with a CLAUDE.md written for them. Everything is automated, signed and encrypted, except three gates that are mine: approve the request, merge it, approve the invitation.

*Source: <https://newsroom.sgit.ai/articles/your-own-agentic-cell.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository

# Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/your-own-agentic-cell.md) · [newsroom v0.14.137](https://newsroom.sgit.ai/admin/versions.html) · agenticcellssite-factoryonboardingpkivaultsproductarticle

***Abstract:** Since the sites for Yiheng Wang and Silvio Switha went up, people have been asking for one of their own. Each site is cheap in tokens. What costs is the workflow around it: collecting the person's details and photos, the first round of designs, and the hand-over. So the product is the workflow, and this is the plan, written up by the conductor agent of PrompTugal from my brief and now in my words. A person arrives at a start page, their browser makes a key pair, and they ask for a cell with a signed request and no secrets. I approve it. A welcome pack arrives sealed to their key: a template vault, their own lane to the factory, and a key scoped to creating one vault. They fill their vault over days with photos, words, links, style and a signed consent, then seal its read key to the factory. The factory turns it into a request, I merge it, and the site factory makes the repository, the address, the site and a first round of five designs, written back into their vault. They choose, I approve a GitHub invitation, and they carry on in their own Claude, with a CLAUDE.md written for them. Everything is automated, signed and encrypted, except three gates that are mine: approve the request, merge it, approve the invitation.*

Your own agentic cell: a key, a request, a vault, the factory, five designs, a hand-over; three human gates.

## In short

- **People ask for a site like Yiheng's and Silvio's;** the sites are cheap, the workflow is not.
- **So the product is the workflow:** a secure, guided intake, the factory, and a hand-over.
- **It starts with a key pair in the browser** and a signed request with no secrets.
- **The person fills their own vault,** over days, and seals it to the factory.
- **The factory makes the site and five designs,** written back into their vault.
- **They continue in their own Claude,** on their own repository.
- **Three human gates:** approve, merge, invite.

## Why now

When the sites for [Yiheng Wang](a-website-that-is-her.md) and [Silvio Switha](a-portfolio-with-a-film-first.md) went up, the first reaction from several people was: can I have one? Each site is cheap to make in tokens. What costs is everything around it: collecting a person's details and photos, running the first round of designs, and handing it over so they can keep it alive. Today that means a Claude session per person waiting for "drop the photos here", and me in the middle of every step.

So the thing to build is not the site; it is the workflow. I briefed it, by mistake, in PrompTugal's conductor session instead of here, and its conductor wrote a thorough plan. This is that plan, in my words, because it is the right one.

## Ask, with a key

It starts at a start page, "create your own agentic cell", with what it is, three live examples, what you will be asked for and what happens to your data. On arrival, the browser makes a key pair with pki.sgit.ai's own module, one key to receive and one to sign, with the private halves kept in the browser and never exported, and shows it as a code and a QR code: this is you ([a secret is a QR code](a-secret-is-a-qr-code.md)). A draft of the basics, name, what you do, links, what you want the site to say, stays in the browser.

Then one button: ask for a cell. It writes to the factory's intake lane: the public key, a short signed note, the headline fields and a way to reach you. An append lane accepts writes and returns nothing, so the page can carry its token openly: the worst anyone can do is send a request ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)).

## Gate one: I approve

The intake agent drains the lane, checks each signature against the key inside it, and lists the requests for me, in a private vault, with Approve and Not now. One tap per request. This is the cost control and the abuse control: nothing that costs tokens or storage happens before it.

## A welcome pack, sealed to your key

Once approved, the person receives one message, sealed to their public key and signed by the factory's, with an expiry: as a pki.sgit.ai link by email, or on a lane their page watches. Inside: the template vault to start from, which holds no secrets; their own lane to the factory; a key scoped to creating one vault; and the factory's public key, also published at a stable address so they can check it. No key ever travels in clear.

## Your vault, filled by you

The template vault carries a small app that guides them: about you, photos (originals kept, web sizes made in the browser), your own words, links, style (three sites you like and why, colours, what to avoid), and consent, what may be public and that agents will read the vault, signed with their key. They can fill it over days, share it with someone who helps them, and it stays theirs, encrypted ([how a vault works](how-a-vault-works.md)).

When they are ready, "send to the factory" seals the vault's read key, not its write key, to the factory's public key.

## Gate two: I merge

The intake agent opens the vault, checks it is complete, photos present and consent signed, and writes the factory request as a pull request: what the site needs, copy, photos and style notes, while their private notes stay in the vault. I merge it, and the factory's apply workflow does what it already does: the repository, the address at `<name>.agenticcells.site`, and the site ([the site factory works](the-site-factory-works.md)).

## Five designs, back in their vault

One factory session runs the first round of five designs from the vault's photos and words, the way Yiheng's and Silvio's five designs were made, instead of a waiting session per person. The designs go back into their vault, each with a screenshot, a preview link and a note, and their app shows them side by side. They pick one and comment in the vault; the factory applies it.

## Gate three: the hand-over

The factory proposes inviting their GitHub account to the site's repository as a collaborator; I approve; they accept. The repository carries a CLAUDE.md written for its owner: what the site is, how to change words and photos, the checks, how to release, what not to touch. From then on they work in their own Claude session, the way Yiheng's own agent took over her site within an hour of it being handed to her.

The invitation itself is made by a small workflow in the factory, triggered by a merged invite file, with the admin token as a CI secret, so no agent session ever holds it.

## Security, and what it costs

- **Keys travel only sealed to a public key;** templates hold no secrets; every request and every send is signed.
- **The factory reads only what a person seals to it,** and only the read key.
- **Consent is a signed file** in the person's vault; what is public is their choice.
- **A security specialist agent reviews** the start page and the lane protocol before the first outside person.
- **Free for the first ten cells,** to learn the workflow and count the tokens per cell, before any price.

## What this does not claim

- **This is a plan,** for me to decide and for the factory's agents to build; none of it exists end to end yet.
- **The scoped key is a pilot** until per-person keys exist.
- **The GitHub hand-over needs checking** with the first person before it is promised.

## Where this comes from

The plan "Your own agentic cell, end to end", written by conductor@PrompTugal.dinis from my brief of 17 November 2026, in the PrompTugal.news repository (`board/spec-agentic-cells-onboarding.md`). Earlier on this site: [a website that is her](a-website-that-is-her.md), [a portfolio with a film first](a-portfolio-with-a-film-first.md), [the site factory works](the-site-factory-works.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [how a vault works](how-a-vault-works.md), [patient vaults, answered](patient-vaults-answered.md).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#your-own-agentic-cell)

### Builds on

- [A website that is her: how Yiheng Wang's site was made in three passes in one evening, by the site factory, five design agents and then her own agent, with five designs, a kitchen brigade of 26 agents, a printable brief and a page for your AI, and why every claim on it is something she can talk about because she did it](a-website-that-is-her.md) Yiheng Wang's website, made in one evening by the site factory, five design agents and her own agent: five designs, every claim sourced, all of it her.
- [A portfolio with a film first: Silvio Switha's site, made in under an hour by the site factory and five design agents, with his music video in the first screen, his agents as a solar system and a mixing desk, a producer's studio, a proposal for clients and a gig poster, and every claim something he built](a-portfolio-with-a-film-first.md) Silvio Switha's portfolio site, made in under an hour by the factory and five design agents: his film first, his agents as a solar system and a mixing desk.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links](patient-vaults-answered.md) Seven questions a healthcare team asked before putting real patient data into sgit vaults, answered, and why QR codes should carry keys and links.

### Continued by

- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.
- [Start with an interview: how someone goes from "I want to try it" to editing their own site with Claude, by being interviewed by Claude first, about what they want, the sections, their materials and the sites they like, then sending their material in whichever way suits them, getting five designs inspired by what they like, or a better version of the site they already have, and reaching the one milestone that matters](start-with-an-interview.md) Onboarding by interview: Claude asks what you want and which sites you like, material comes any way, and you end up editing with Claude.
- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these](our-companies-and-uth.md) Each of our companies, technologies and websites mapped to what UAlgTec Heritage needs to build a European HeritageTech sector.
- [Keys after payment: how to hand vault keys and access keys to customers once they have paid, what Stripe does and does not do after the money is taken, what FastSpring, Paddle, Lemon Squeezy, Polar, Gumroad and Square offer instead, and a design where the key is sealed to the buyer's own public key, keys are stock, and a payment provider can sell them without ever holding one](keys-after-payment.md) How to hand vault and access keys to customers after payment: what Stripe and others do, and a design that seals each key to the buyer's own key.
- [Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links](patient-vaults-answered.md) Seven questions a healthcare team asked before putting real patient data into sgit vaults, answered, and why QR codes should carry keys and links.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 451 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=451)

**Posting this article on LinkedIn?** The cover is [your-own-agentic-cell.jpg](banners/your-own-agentic-cell.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/your-own-agentic-cell.html)*
