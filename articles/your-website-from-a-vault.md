# Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again, sgit.ai

> There are a lot of people I want to show a Sovereign Agentic Website to, and the best way is to show them their own: five versions of it, made by agents. The problem is that a demo cannot be public. Our repositories and sites are public by default, and "public but not linked" has never felt right. The answer has been in front of us: encrypted vaults. The demo cell takes a name, researches only public information, builds five designs, has them reviewed, and seals all five into one sgit vault. The person gets a QR code, a link with the key after the #, or a zip, and drops it on one page, which decrypts the vault in their browser and shows their site in a sandboxed frame, with a banner and the five designs one tap apart. Nothing is published, the key never reaches a server, and if they say yes, the factory makes their repository from the same vault, so the demo becomes the first chapter of their site's history. This piece maps the workflow and the pipeline, and what is still to build.

*Source: <https://newsroom.sgit.ai/articles/your-website-from-a-vault.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again

# Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/your-website-from-a-vault.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · sovereign-websitesgitvaultsdemosqr-codesgo-to-marketarticle

***Abstract:** There are a lot of people I want to show a Sovereign Agentic Website to, and the best way is to show them their own: five versions of it, made by agents. The problem is that a demo cannot be public. Our repositories and sites are public by default, and "public but not linked" has never felt right. The answer has been in front of us: encrypted vaults. The demo cell takes a name, researches only public information, builds five designs, has them reviewed, and seals all five into one sgit vault. The person gets a QR code, a link with the key after the #, or a zip, and drops it on one page, which decrypts the vault in their browser and shows their site in a sandboxed frame, with a banner and the five designs one tap apart. Nothing is published, the key never reaches a server, and if they say yes, the factory makes their repository from the same vault, so the demo becomes the first chapter of their site's history. This piece maps the workflow and the pipeline, and what is still to build.*

The demo pipeline: a name in, five designs sealed in one vault, opened by QR code, link or zip.

## In short

- **The best demo is someone's own website,** five versions of it.
- **A demo cannot be public,** and "public but not linked" never felt right.
- **So it goes in an encrypted vault:** five designs, one key.
- **One drop page, three ways in:** a QR code, a link with the key after the #, or a zip.
- **The browser decrypts it;** nothing is published and the key never reaches a server.
- **If they say yes,** their sovereign website is made from the same vault.

## The problem with demos

I want to reach a lot of people with this: owners of small businesses, people I meet at events, investors, partners. The most convincing thing I can show any of them is not our site, or a slide. It is their own website, in five versions, made by agents from what is already public about them.

But that demo cannot be public. Everything we put in our repositories is public by default, and I want to keep it that way: I do not want to start dealing with private repositories. Until now the workaround has been a site that is public but not linked, which works, and has never felt right. A person who has not yet agreed to anything should not find a version of themselves on the open web.

## The answer: a vault

sgit's vaults solve exactly this. Everything in a vault is encrypted before it leaves the machine that wrote it, and a web page can open one in the browser: compute where the head is from the key, fetch a handful of objects, decrypt them, and either read files or run an app in a sandboxed frame ([how a vault works](how-a-vault-works.md)). A website is just files. So a website can live in a vault, and a page can show it to whoever holds the key, and to nobody else.

It also feels natural in a way the public-but-unlinked site never did. The vault is not a hiding place; it is where the work lives, versioned and signed, and the demo is just the first thing in it. And there is a continuation: the same vault can become the person's real site.

## The drop page

The drop page: three ways in, and the site rendered in the browser with five designs a tap apart.

One page, with three ways in:

- **Scan a QR code,** on a card, a letter or a slide ([a secret is a QR code](a-secret-is-a-qr-code.md)).
- **Open a link,** with the key after the `#`. That part of a link is never sent to the server, so the server that serves the page never sees the key.
- **Drop a zip,** the whole site in one file, opened in the browser with no server at all. For someone who wants to evaluate it offline, or deploy it themselves, it is the simplest form there is.

The page decrypts the vault and renders the site in a sandboxed frame, with a banner on top: a demo made for you, by agents; five designs; nothing here is public; make it yours. The five designs are one tap apart. The banner can be hidden, so the site can be seen as it would really be.

It needs a name, and I would keep it under sgit, at an address we already have, something like from.sgit.ai: one generic page, the same for everyone, and the same page could sit on sovereignwebsite.ai.

## The demo pipeline

This is a job for an agentic cell, and it maps cleanly:

1. **A name.** I give the demo cell a person or a company, and why: someone I am about to meet, an investor, a shop I walked past.
2. **Research,** from public information only: what they do, in their own words, how they look today.
3. **Five designs,** by the cell's designers, as for every site we make ([the website cell](the-website-cell.md)).
4. **Review:** nothing private, every claim checked against its source, and every page marked as a demo.
5. **Seal:** all five into one vault, and from its key a QR code, a link and a zip.
6. **Send:** the agent drafts the email, and I send it, as I do every email the agents draft for me.
7. **Open:** they drop it on the page and see their site.

All I am doing is selling. The cell does the rest, and a Claude session can run it for many names at once.

## From demo to their site

If they say yes, nothing is thrown away. The factory makes their repository from the same vault: the design they chose becomes their [sovereign website](sovereign-agentic-website.md), live at its own address, with [the team inside it](a-website-with-a-team-inside.md). The vault they opened is the first chapter of the site's history.

The keys follow the same path. Today the vault key is the whole secret. The better version gives the person a key pair of their own, so that what we send them is sealed to their key, and once the site is theirs, only they can change it ([a key for every person](a-key-for-every-person.md)). Vaults do not fully support that yet; it is on the list.

## What is still to build

- **The drop page,** taking a QR code, a link or a zip, and rendering a vault's site with the banner and the five designs.
- **A demo cell** that runs the pipeline from a name to a sealed vault and a drafted email.
- **The step from vault to repository** in the factory.
- **Private keys for vaults,** so a demo can be sealed to its recipient.

## What this does not claim

- **None of this is built yet;** the vault and its browser reading are, the drop page and the demo cell are not.
- **A demo uses public information only,** is marked as a demo, and is shown only to the person it is about.
- **The address is a proposal;** nothing has been registered for it.

## Where this comes from

My own thinking, in writer-10's session on 19 November 2026, building on [how a vault works](how-a-vault-works.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [a key for every person](a-key-for-every-person.md), [the website cell](the-website-cell.md), [Sovereign Agentic Website](sovereign-agentic-website.md) and [a website with a team inside](a-website-with-a-team-inside.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#your-website-from-a-vault)

### Builds on

- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [Sovereign Agentic Website: the name for what we have been building, a website built by agents and owned by the person it is for, an open pattern anyone can use without paying us as WordPress was, a hosted version on sovereignwebsite.site, and why sovereign and agentic are the two words that make it different from the web of 2000](sovereign-agentic-website.md) Sovereign Agentic Website: built by agents, owned by you; an open pattern anyone can use, and a hosted version on sovereignwebsite.site.
- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 497 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=497)

**Posting this article on LinkedIn?** The cover is [your-website-from-a-vault.jpg](banners/your-website-from-a-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/your-website-from-a-vault.html)*
