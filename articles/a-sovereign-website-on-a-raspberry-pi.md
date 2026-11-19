# A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes, sgit.ai

> We are going to run a sovereign website, and everything that makes it, on one Raspberry Pi. The box is a Raspberry Pi 5 with 16GB of memory and a 256GB card, the hardware of the Pi Pro tier in our Kickstarter plan. The experiment has six parts. Serve the site from home, from a git checkout, on the local network first. Take updates only when every commit's signature checks out. Run open-weight models locally, behind an endpoint the build page can call. Point the build page at that model, and build a website on the Pi itself, with the agents working under a policy guard and no internet unless it is allowed. Back up the site and the runs to an encrypted vault. And, if the owner wants, reach it from the internet without a proprietary tunnel. We will measure the model's speed, the time a site takes, its quality against cloud models, and the power it uses, and publish the sites and the recipe so anyone can repeat it. Nothing in the brief, the model, the drafts or the designs leaves the house. This is the prototype for the Raspberry Pi sovereign website, which launches officially once the Kickstarter finishes.

*Source: <https://newsroom.sgit.ai/articles/a-sovereign-website-on-a-raspberry-pi.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes

# A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/a-sovereign-website-on-a-raspberry-pi.md) · [newsroom v0.14.177](https://newsroom.sgit.ai/admin/versions.html) · sovereign-websiteraspberry-pilocal-aiexperimentbehaviour-policieskickstarterarticle

***Abstract:** We are going to run a sovereign website, and everything that makes it, on one Raspberry Pi. The box is a Raspberry Pi 5 with 16GB of memory and a 256GB card, the hardware of the Pi Pro tier in our Kickstarter plan. The experiment has six parts. Serve the site from home, from a git checkout, on the local network first. Take updates only when every commit's signature checks out. Run open-weight models locally, behind an endpoint the build page can call. Point the build page at that model, and build a website on the Pi itself, with the agents working under a policy guard and no internet unless it is allowed. Back up the site and the runs to an encrypted vault. And, if the owner wants, reach it from the internet without a proprietary tunnel. We will measure the model's speed, the time a site takes, its quality against cloud models, and the power it uses, and publish the sites and the recipe so anyone can repeat it. Nothing in the brief, the model, the drafts or the designs leaves the house. This is the prototype for the Raspberry Pi sovereign website, which launches officially once the Kickstarter finishes.*

Everything sovereign on one box: what runs on the Pi, what it talks to, and what never leaves the house.

## In short

- **The experiment:** a sovereign website, and everything that makes it, on one Raspberry Pi at home.
- **The box:** a Raspberry Pi 5 with 16GB and 256GB, the Pi Pro hardware.
- **Six parts:** serve, check signatures, run a local model, build a site on the device, back up, and reach it from outside.
- **We measure** speed, time per site, quality against cloud models, and power.
- **Nothing leaves the house** unless the owner publishes it.
- **The product launches** once the Kickstarter finishes.

## Why a Pi

A sovereign website is one its owner owns and can move ([what is a sovereign website](what-is-a-sovereign-website.md)). The strongest form of that is a site that lives on a computer the owner holds, made by a model the owner runs, under rules the owner can read. Not only where the site is served from, but where it is made. A Raspberry Pi is the simplest computer that might do all of it: small, cheap, open, and quiet enough for a shelf.

So we are going to try. The box is a Raspberry Pi 5 with 16GB of memory and a 256GB card, in a starter kit with an active cooler and its own power supply: the hardware of the £900 Pi Pro tier in [the Kickstarter plan](launching-the-sovereign-website-appliance.md).

## The six parts

1. **Serve the site from home.** A plain web server, such as Caddy or nginx, serves the site from a git checkout of its repository, on the local network first. The site stays on GitHub Pages too: the Pi is a second host, not the only one.
2. **Take only signed updates.** A small timer pulls the repository's dev branch and serves a new version only if every new commit's signature checks out against the keys the repository already trusts, the same rule this newsroom's own releases now follow. An update nobody signed never reaches the shelf.
3. **Run a local model.** Open-weight models, run with a tool such as llama.cpp or Ollama, behind a local endpoint that speaks the same API the cloud providers do, so the agents do not need to know the difference. We will try a few models of different sizes, to find the largest that is still usable.
4. **Build a website on the Pi.** Point the build page from [watch your website being built](watch-your-website-being-built.md) at that local endpoint. From a browser on the same network, the owner describes a site, watches the conductor hand out the work, the designers and writer draft, the policy guard check every call, and the designs arrive, all computed on the Pi. The model has no internet unless a rule allows it.
5. **Back up to a vault.** The site, the briefs and the recorded runs go into an encrypted sgit vault, so the box can fail and nothing is lost ([how a vault works](how-a-vault-works.md)).
6. **Reach it from outside, if wanted.** A dynamic DNS name and the home router keep everything under the owner's control, where the internet provider allows it; otherwise a tunnel to a small server the owner controls. No proprietary tunnel in the middle, because that would be the part a sovereign website avoids.

## What we will measure

- **The model's speed,** in words a second, for each model we try.
- **The time a site takes,** from the brief to five designs, on the Pi.
- **Its quality against cloud models:** the same brief run in the cloud and on the Pi, side by side, as in the evals of the build page.
- **The power it uses,** for a build and at rest, with a plug-in meter.
- **What breaks:** memory, heat, the card's speed, and anything else we hit.

And then we publish all of it: the sites built on the Pi, the timings, and the recipe as instructions in an open repository, so that anyone with the same box can repeat it.

## What could go wrong

The likely problems are known. A local model on a Pi will be slow, so a build may take a long time; for this, that is acceptable, and the measurement is the point. The largest useful model may be smaller than we hope, and its designs weaker than a cloud model's; then the honest result is a split, the Pi serving and editing locally and building with a cloud model when the owner chooses. A microSD card is slow to load models from; a small drive on the Pi's PCIe slot would fix that later. We will report whichever happens.

## From experiment to product

This is the prototype for the Raspberry Pi sovereign website, one of the appliances in the Kickstarter plan: the £400 Pi, where we build the site and the Pi runs it, and the £900 Pi Pro, where it can build sites itself. Those products launch officially once the Kickstarter finishes. What this experiment gives the campaign is the proof: a real box on a real shelf, a site built on it, and the numbers.

## What this does not claim

- **Nothing has been run yet;** this is the plan, and the results will be published as they come.
- **The tools named are candidates,** to be tested, not choices made.
- **No claim is made about model speed or quality on a Pi** until we have measured it.

## Where this comes from

My own thinking, in writer-10's session on 19 November 2026, building on [launching the sovereign website appliance](launching-the-sovereign-website-appliance.md), [watch your website being built](watch-your-website-being-built.md), [what is a sovereign website](what-is-a-sovereign-website.md) and [how a vault works](how-a-vault-works.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#a-sovereign-website-on-a-raspberry-pi)

### Builds on

- [What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer](what-is-a-sovereign-website.md) What a sovereign website is: owned and movable, commodity only, seven principles, a maturity model from rented to proven, and every host.
- [Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a Raspberry Pi, five tiers from a £50 supporter to £1,000, the two Pro tiers running local AI models that can build a website on the device itself, the hardware we would buy in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone](launching-the-sovereign-website-appliance.md) The Kickstarter plan: a sovereign website on a Raspberry Pi or a tablet, five tiers from £50 to £1,000, local AI on the Pro tiers.
- [Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from](watch-your-website-being-built.md) A page that builds a first version of a sovereign website in your browser, showing every agent, behaviour policy and penny, then hands back a zip.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.

### Continued by

- [Websites for the moment: an experiment in letting an agent team keep building topical sites, around what people are looking for now, GTA VI on its launch day, Christmas posting dates, an advent of tools, the Kickstarter itself, each built in a day within a budget, every fact sourced, live for its moment and then archived, and a first calendar to start from](websites-for-the-moment.md) An agent team building topical websites around what people are looking for now, each built in a day within a budget and sourced.
- [Where to sell the book and the appliances: a map of the places a UK author and maker can sell physical products, printed copies of One Human, Nine Agents, Nineteen Hours from early December and the sovereign website appliances from 1 January after a December Kickstarter, with Amazon, IngramSpark, eBay, OnBuy and our own shop, what each charges, the rules that matter, and the law that comes with selling hardware](where-to-sell-the-book-and-the-appliances.md) Where to sell the printed book and the sovereign website appliances in the UK, when, what each platform charges, and the law that comes with hardware.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 504 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=504)

**Posting this article on LinkedIn?** The cover is [a-sovereign-website-on-a-raspberry-pi.jpg](banners/a-sovereign-website-on-a-raspberry-pi.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-sovereign-website-on-a-raspberry-pi.html)*
