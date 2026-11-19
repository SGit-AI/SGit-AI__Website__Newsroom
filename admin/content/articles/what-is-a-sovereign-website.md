---
title: What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: I searched for "sovereign website" and found almost nothing. That is an opportunity: we get to define the category, the way serverless was defined, with principles anyone can test a site against. A sovereign website is a website you own and can move. Moving is the hard part, and the lesson I do not think has been learned is that one proprietary component in the middle, however small, is enough to stop you: nobody can move the site for you without rebuilding that part, so you cannot even pay your way out. Lock-in comes from the domain, the technology and the platform alike. So a sovereign website is built only on commodity technology, its content and schema in open formats, its domain in its owner's name. This piece proposes seven principles, a maturity model from level 0, rented, to level 5, sovereign and proven, and a proof every Sovereign Agentic Website should carry: the same commit deployed by one pipeline to GitHub Pages, Cloudflare, Netlify, Azure, AWS, a European host and your own computer. Agentic is how we build them; sovereign is what they are. The principles belong at sovereignwebsite.org.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, sovereignty, open-source, europe, hosting, principles, article
status: published
---

!shot smm-levels.webp | images/ | A sovereignty maturity model for websites, from level 0, rented, to level 5, sovereign and proven. | concept

## In short {#in-short}

- **Almost nobody searches for "sovereign website",** so we get to define it.
- **A sovereign website is one you own and can move.**
- **One proprietary part in the middle is enough to lock you in,** however small.
- **Seven principles** to test a site against, and a **maturity model** from rented to proven.
- **The proof:** the same site deployed to every host we can find, in Europe and on your own computer.
- **The principles at sovereignwebsite.org;** the commercial side at sovereignwebsite.ai.

## Defining the category {#category}

When I searched for "sovereign website" there was very little: a few uses of the words, no category, no principles. That is an opportunity. Serverless was a category before it was a product; someone had to say what it meant and what it did not, and then everyone could build against that. We can do the same for websites you own.

[Sovereign Agentic Website](/articles/sovereign-agentic-website.html) is our name for how we make them. But the two words do different jobs. Agentic is how the site is built and changed: by a team of agents, and then by your own AI. Sovereign is what the site is, whoever built it. A sovereign website could be made by hand. That independence matters: the definition should hold for anyone, not only for us.

## The lesson about lock-in {#lockin}

A sovereign website is a website you own and can move. Owning is the easy part. Moving is where it fails, and here is the lesson I do not think has been learned, or really drawn for people to see.

Once there is a piece of proprietary technology in the middle, it does not matter how small it is: you cannot move the site. There is friction, and worse, nobody else can move it for you. You cannot even pay someone to move it, because they would have to rebuild that component first, and sometimes it is not small at all. A paid plugin, a platform's form handler, a hosting company's special function, an agency's private framework: any one of them is enough.

And lock-in has more than one place to hide: where the domain is registered, the technology underneath, and the platform it runs on. A site that is portable in its code but registered in someone else's name is not sovereign. Nor is one in your name that only runs on one company's servers.

## Seven principles {#principles}

A website is sovereign when:

1. **You own it.** The site, its content and its history are in a repository in your name, and the domain is registered to you, at a registrar you chose ([your own registrar](/articles/your-own-registrar.html)).
2. **You can move it.** It runs on any commodity host that can serve files, without changes.
3. **Nothing in the middle is proprietary.** Every part it needs to build and run is open and commodity; if one part is not, the site is not sovereign, however small that part is.
4. **Its content and schema are open.** Words, data and their structure are in open formats you can read without the tool that made them.
5. **Anyone can change it.** You, any developer, or your own AI, without asking the company that built it ([no lock-in](/articles/no-lock-in.html)).
6. **What works on it is bounded.** Agents and tools that change it work inside a behaviour policy that says what they may touch ([feature behaviour policies](/articles/feature-behaviour-policies.html)).
7. **It is proven, not claimed.** It is deployed, regularly, on more than one host, so that moving is a thing that already happened, not a promise.

## The maturity model {#maturity}

Sovereignty is not yes or no; it is how far you can move, on your terms. The model has six levels:

- **Level 0, rented.** A hosted builder decides everything, and little leaves but some content. Most website platforms sit here by their own terms of service.
- **Level 1, exportable.** You can export your words and images; the design and the functions stay behind.
- **Level 2, self-hosted, with a part you do not control.** The software is open, but one paid plugin, theme or agency component holds the site where it is.
- **Level 3, open, on one host.** Open code in your repository, but tied to one host's special features.
- **Level 4, portable.** Plain files and open tools; any static host can serve it; your domain at your registrar. The website cell is here today.
- **Level 5, sovereign and proven.** Portable, and proven by being deployed on many hosts, one of them in Europe and one your own machine.

The same model works inside a company. A corporate site built on one cloud provider's proprietary services sits at level 3 at best, however well it is engineered; it cannot move without rebuilding. That is exactly the question many European organisations are now asking of their cloud providers, and it is the same question, smaller, for every website.

## One site, every host {#hosts}

!shot smm-hosts.webp | images/ | One site, every host: GitHub Pages today, and the hosts the same commit should be proven on. | concept

Principle seven needs a demonstration, and we can build it. Our sites deploy today to GitHub Pages. The next step is a pipeline that takes the same commit of one of our demo sites and deploys it everywhere it can: Cloudflare Pages, Netlify, Azure Static Web Apps, AWS S3 and CloudFront, Codeberg Pages in Germany, a European cloud's storage bucket, and a plain folder on your own computer served by any web server. I will open the accounts; the automation is the factory's.

There is an interesting extra case: whether such a site can be built and served inside Claude's own sandbox. I do not know yet if its limits allow it; it may need special instructions. If it works, it is a striking proof: a website that runs wherever its owner's AI runs. Either way, each host gets a short set of instructions, so that anyone can repeat it.

## Not plain, and not small {#design}

A sovereign website must not look like a sovereign website demo. Too many open alternatives look vanilla, the way default slide themes do. Every site we make keeps the standard of the website cell: five designs to choose from, very visual, made from the owner's own photos and words ([the website cell](/articles/the-website-cell.html)). And the pattern goes further than brochure sites. Shops, catalogues and booking pages can be built without a heavy backend, from static files and open services, and still pass all seven principles. We should show that, with real examples.

## What comes next {#next}

- **sovereignwebsite.org** for the principles and the open pattern, as wordpress.org is to WordPress; **sovereignwebsite.ai** for the hosted service.
- **The principles and the maturity model as a page anyone can test a site against,** and a self-assessment.
- **The every-host pipeline** on one demo site, then on all of ours.
- **Moving our existing sites** to the new brand, with their owners' agreement.

## What this does not claim {#limits}

- **The principles and the model are a proposal,** written to be argued with and improved.
- **The every-host pipeline does not exist yet;** only GitHub Pages is in use today.
- **Platform placements on the model are by their published terms,** as in [no lock-in](/articles/no-lock-in.html); a given site may do better or worse.

## Where this comes from {#sources}

My own thinking, in writer-10's session on 19 November 2026, after a search for "sovereign website" that found little. sovereignwebsite.org was registered the same day, to hold the principles. It builds on [Sovereign Agentic Website](/articles/sovereign-agentic-website.html), [sovereignty you can move](/articles/sovereignty-you-can-move.html), [no lock-in](/articles/no-lock-in.html), [the website cell](/articles/the-website-cell.html), [your own registrar](/articles/your-own-registrar.html) and [feature behaviour policies](/articles/feature-behaviour-policies.html).
