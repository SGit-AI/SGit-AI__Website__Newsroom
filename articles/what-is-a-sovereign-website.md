# What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer, sgit.ai

> I searched for "sovereign website" and found almost nothing. That is an opportunity: we get to define the category, the way serverless was defined, with principles anyone can test a site against. A sovereign website is a website you own and can move. Moving is the hard part, and the lesson I do not think has been learned is that one proprietary component in the middle, however small, is enough to stop you: nobody can move the site for you without rebuilding that part, so you cannot even pay your way out. Lock-in comes from the domain, the technology and the platform alike. So a sovereign website is built only on commodity technology, its content and schema in open formats, its domain in its owner's name. This piece proposes seven principles, a maturity model from level 0, rented, to level 5, sovereign and proven, and a proof every Sovereign Agentic Website should carry: the same commit deployed by one pipeline to GitHub Pages, Cloudflare, Netlify, Azure, AWS, a European host and your own computer. Agentic is how we build them; sovereign is what they are. The principles belong at sovereignwebsite.org.

*Source: <https://newsroom.sgit.ai/articles/what-is-a-sovereign-website.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer

# What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/what-is-a-sovereign-website.md) · [newsroom v0.14.174](https://newsroom.sgit.ai/admin/versions.html) · sovereign-websitesovereigntyopen-sourceeuropehostingprinciplesarticle

***Abstract:** I searched for "sovereign website" and found almost nothing. That is an opportunity: we get to define the category, the way serverless was defined, with principles anyone can test a site against. A sovereign website is a website you own and can move. Moving is the hard part, and the lesson I do not think has been learned is that one proprietary component in the middle, however small, is enough to stop you: nobody can move the site for you without rebuilding that part, so you cannot even pay your way out. Lock-in comes from the domain, the technology and the platform alike. So a sovereign website is built only on commodity technology, its content and schema in open formats, its domain in its owner's name. This piece proposes seven principles, a maturity model from level 0, rented, to level 5, sovereign and proven, and a proof every Sovereign Agentic Website should carry: the same commit deployed by one pipeline to GitHub Pages, Cloudflare, Netlify, Azure, AWS, a European host and your own computer. Agentic is how we build them; sovereign is what they are. The principles belong at sovereignwebsite.org.*

A sovereignty maturity model for websites, from level 0, rented, to level 5, sovereign and proven.

## In short

- **Almost nobody searches for "sovereign website",** so we get to define it.
- **A sovereign website is one you own and can move.**
- **One proprietary part in the middle is enough to lock you in,** however small.
- **Seven principles** to test a site against, and a **maturity model** from rented to proven.
- **The proof:** the same site deployed to every host we can find, in Europe and on your own computer.
- **The principles at sovereignwebsite.org;** the commercial side at sovereignwebsite.ai.

## Defining the category

When I searched for "sovereign website" there was very little: a few uses of the words, no category, no principles. That is an opportunity. Serverless was a category before it was a product; someone had to say what it meant and what it did not, and then everyone could build against that. We can do the same for websites you own.

[Sovereign Agentic Website](sovereign-agentic-website.md) is our name for how we make them. But the two words do different jobs. Agentic is how the site is built and changed: by a team of agents, and then by your own AI. Sovereign is what the site is, whoever built it. A sovereign website could be made by hand. That independence matters: the definition should hold for anyone, not only for us.

## The lesson about lock-in

A sovereign website is a website you own and can move. Owning is the easy part. Moving is where it fails, and here is the lesson I do not think has been learned, or really drawn for people to see.

Once there is a piece of proprietary technology in the middle, it does not matter how small it is: you cannot move the site. There is friction, and worse, nobody else can move it for you. You cannot even pay someone to move it, because they would have to rebuild that component first, and sometimes it is not small at all. A paid plugin, a platform's form handler, a hosting company's special function, an agency's private framework: any one of them is enough.

And lock-in has more than one place to hide: where the domain is registered, the technology underneath, and the platform it runs on. A site that is portable in its code but registered in someone else's name is not sovereign. Nor is one in your name that only runs on one company's servers.

## Seven principles

A website is sovereign when:

1. **You own it.** The site, its content and its history are in a repository in your name, and the domain is registered to you, at a registrar you chose ([your own registrar](your-own-registrar.md)).
2. **You can move it.** It runs on any commodity host that can serve files, without changes.
3. **Nothing in the middle is proprietary.** Every part it needs to build and run is open and commodity; if one part is not, the site is not sovereign, however small that part is.
4. **Its content and schema are open.** Words, data and their structure are in open formats you can read without the tool that made them.
5. **Anyone can change it.** You, any developer, or your own AI, without asking the company that built it ([no lock-in](no-lock-in.md)).
6. **What works on it is bounded.** Agents and tools that change it work inside a behaviour policy that says what they may touch ([feature behaviour policies](feature-behaviour-policies.md)).
7. **It is proven, not claimed.** It is deployed, regularly, on more than one host, so that moving is a thing that already happened, not a promise.

## The maturity model

Sovereignty is not yes or no; it is how far you can move, on your terms. The model has six levels:

- **Level 0, rented.** A hosted builder decides everything, and little leaves but some content. Most website platforms sit here by their own terms of service.
- **Level 1, exportable.** You can export your words and images; the design and the functions stay behind.
- **Level 2, self-hosted, with a part you do not control.** The software is open, but one paid plugin, theme or agency component holds the site where it is.
- **Level 3, open, on one host.** Open code in your repository, but tied to one host's special features.
- **Level 4, portable.** Plain files and open tools; any static host can serve it; your domain at your registrar. The website cell is here today.
- **Level 5, sovereign and proven.** Portable, and proven by being deployed on many hosts, one of them in Europe and one your own machine.

The same model works inside a company. A corporate site built on one cloud provider's proprietary services sits at level 3 at best, however well it is engineered; it cannot move without rebuilding. That is exactly the question many European organisations are now asking of their cloud providers, and it is the same question, smaller, for every website.

## One site, every host

One site, every host: GitHub Pages today, and the hosts the same commit should be proven on.

Principle seven needs a demonstration, and we can build it. Our sites deploy today to GitHub Pages. The next step is a pipeline that takes the same commit of one of our demo sites and deploys it everywhere it can: Cloudflare Pages, Netlify, Azure Static Web Apps, AWS S3 and CloudFront, Codeberg Pages in Germany, a European cloud's storage bucket, and a plain folder on your own computer served by any web server. I will open the accounts; the automation is the factory's.

There is an interesting extra case: whether such a site can be built and served inside Claude's own sandbox. I do not know yet if its limits allow it; it may need special instructions. If it works, it is a striking proof: a website that runs wherever its owner's AI runs. Either way, each host gets a short set of instructions, so that anyone can repeat it.

## Not plain, and not small

A sovereign website must not look like a sovereign website demo. Too many open alternatives look vanilla, the way default slide themes do. Every site we make keeps the standard of the website cell: five designs to choose from, very visual, made from the owner's own photos and words ([the website cell](the-website-cell.md)). And the pattern goes further than brochure sites. Shops, catalogues and booking pages can be built without a heavy backend, from static files and open services, and still pass all seven principles. We should show that, with real examples.

## What comes next

- **sovereignwebsite.org** for the principles and the open pattern, as wordpress.org is to WordPress; **sovereignwebsite.ai** for the hosted service.
- **The principles and the maturity model as a page anyone can test a site against,** and a self-assessment.
- **The every-host pipeline** on one demo site, then on all of ours.
- **Moving our existing sites** to the new brand, with their owners' agreement.

## What this does not claim

- **The principles and the model are a proposal,** written to be argued with and improved.
- **The every-host pipeline does not exist yet;** only GitHub Pages is in use today.
- **Platform placements on the model are by their published terms,** as in [no lock-in](no-lock-in.md); a given site may do better or worse.

## Where this comes from

My own thinking, in writer-10's session on 19 November 2026, after a search for "sovereign website" that found little. sovereignwebsite.org was registered the same day, to hold the principles. It builds on [Sovereign Agentic Website](sovereign-agentic-website.md), [sovereignty you can move](sovereignty-you-can-move.md), [no lock-in](no-lock-in.md), [the website cell](the-website-cell.md), [your own registrar](your-own-registrar.md) and [feature behaviour policies](feature-behaviour-policies.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#what-is-a-sovereign-website)

### Builds on

- [Sovereign Agentic Website: the name for what we have been building, a website built by agents and owned by the person it is for, an open pattern anyone can use without paying us as WordPress was, a hosted version on sovereignwebsite.site, and why sovereign and agentic are the two words that make it different from the web of 2000](sovereign-agentic-website.md) Sovereign Agentic Website: built by agents, owned by you; an open pattern anyone can use, and a hosted version on sovereignwebsite.site.
- [Your own registrar: which domain registrar to recommend to a small business in Europe taking its website's domain into its own name, sixteen compared on price and renewal, .eu, .pt and .ai, privacy, and APIs safe enough to hand to an agent, why AWS now sells .ai but is still a heavy choice, and the three we would put forward](your-own-registrar.md) Which registrar a small business in Europe should hold its own domain at: sixteen compared, and OVHcloud, Hostinger and INWX.
- [No lock-in: why the one thing that most separates the website cell from Wix, Squarespace, Fliplet and the rest is that the customer can leave, what the platforms' own terms and export pages say, how large the market of people paying monthly for sites they cannot take with them is, and what a site that promises to move into its owner's hands should say on its front page](no-lock-in.md) The website cell's biggest difference is that the customer can leave; the platforms' own terms show why that matters.
- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [Sovereignty you can move: why where your data is hosted is not sovereignty, why being able to move the site, the data and the schema is, why that makes the website cell a direct competitor to Wix, Squarespace and Fliplet with a proper sovereign offer, European-aligned, multilingual and privacy-first, and the business that other companies can build on it](sovereignty-you-can-move.md) Sovereignty is being able to move your site, data and schema, not where it is hosted; the website cell as a sovereign competitor.

### Continued by

- [Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving](every-tool-its-own-website.md) Turning the 49 tools of tools.sgraph.ai into sovereign websites: one site each, simple first, pinned versions, signed hashes, a team of teams.
- [A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes](a-sovereign-website-on-a-raspberry-pi.md) The experiment: a sovereign website, its local model, its build and its signed updates, all on one Raspberry Pi 5 at home.
- [Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from](watch-your-website-being-built.md) A page that builds a first version of a sovereign website in your browser, showing every agent, behaviour policy and penny, then hands back a zip.
- [The launch plan in eleven turns: how one afternoon took the plan for launching Sovereign Website from a £50 site on Kickstarter, through Indiegogo, PPL, Patreon, countries as stretch goals and the UK as home ground, to a configured Android tablet, a supporter tier and a Raspberry Pi, with every variation we tried and why each was kept or set aside](the-launch-plan-in-eleven-turns.md) How one afternoon took the launch plan from a £50 site on Kickstarter to a configured Android tablet, a supporter tier and a Raspberry Pi.
- [Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a Raspberry Pi, five tiers from a £50 supporter to £1,000, the two Pro tiers running local AI models that can build a website on the device itself, the hardware we would buy in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone](launching-the-sovereign-website-appliance.md) The Kickstarter plan: a sovereign website on a Raspberry Pi or a tablet, five tiers from £50 to £1,000, local AI on the Pro tiers.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 500 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=500)

**Posting this article on LinkedIn?** The cover is [what-is-a-sovereign-website.jpg](banners/what-is-a-sovereign-website.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-is-a-sovereign-website.html)*
