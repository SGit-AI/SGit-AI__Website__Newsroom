# Out of the box: the five stages it takes today to put a website and a local model on a Raspberry Pi from a Mac, and how the Factory can do every one of them once, so that the sovereign website appliance just works when it is plugged in and scales to many units the same way, sgit.ai

> I wrote a setup guide this week for putting a website and a local model on a Raspberry Pi, prepared from a MacBook. It has five stages: write Raspberry Pi OS Lite to the card with Raspberry Pi Imager, boot the Pi, connect from the Mac's Terminal over SSH, update it, and add the website and the models. It works, and every step is in the official getting-started guide. It is also the reason the appliance has to exist. Along the way the person setting it up chooses the right drive, accepts a host key, finds an address in a router, picks a runtime that depends on their website, and picks a model that fits the Pi's memory, and each of those is a place where someone who only wants their website gives up. So the idea is to turn the guide round. Everything the guide asks the owner to do, the Factory does once, as a build: one image with the operating system, the updates, the runtime and a model chosen for the memory, tested on a real Pi. What is different for each owner, their website, their keys, their network, is written per unit, and nothing secret is baked into the image. The owner plugs in the power and the network, opens a page on their phone, and sees their site, served from a box on their shelf, with the agents taking signed updates from then on. That is what makes it scale: a thousand units made from one tested image are a thousand of the same thing, and fixing the image fixes them all. For the Kickstarter it changes what we promise: not a guide, a box that works when it is plugged in, with the guide kept open for anyone who would rather do it by hand. None of the appliance is built yet; this is the plan, and the next step is one card, imaged once by the Factory, and timed from the power cable to the website.

*Source: <https://newsroom.sgit.ai/articles/out-of-the-box.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Out of the box: the five stages it takes today to put a website and a local model on a Raspberry Pi from a Mac, and how the Factory can do every one of them once, so that the sovereign website appliance just works when it is plugged in and scales to many units the same way

# Out of the box: the five stages it takes today to put a website and a local model on a Raspberry Pi from a Mac, and how the Factory can do every one of them once, so that the sovereign website appliance just works when it is plugged in and scales to many units the same way

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-22 · [article v1.0.0](versions/out-of-the-box.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · sovereign-websiteraspberry-piappliancelocal-aikickstarterfactorysetupgo-to-marketarticle

***Abstract:** I wrote a setup guide this week for putting a website and a local model on a Raspberry Pi, prepared from a MacBook. It has five stages: write Raspberry Pi OS Lite to the card with Raspberry Pi Imager, boot the Pi, connect from the Mac's Terminal over SSH, update it, and add the website and the models. It works, and every step is in the official getting-started guide. It is also the reason the appliance has to exist. Along the way the person setting it up chooses the right drive, accepts a host key, finds an address in a router, picks a runtime that depends on their website, and picks a model that fits the Pi's memory, and each of those is a place where someone who only wants their website gives up. So the idea is to turn the guide round. Everything the guide asks the owner to do, the Factory does once, as a build: one image with the operating system, the updates, the runtime and a model chosen for the memory, tested on a real Pi. What is different for each owner, their website, their keys, their network, is written per unit, and nothing secret is baked into the image. The owner plugs in the power and the network, opens a page on their phone, and sees their site, served from a box on their shelf, with the agents taking signed updates from then on. That is what makes it scale: a thousand units made from one tested image are a thousand of the same thing, and fixing the image fixes them all. For the Kickstarter it changes what we promise: not a guide, a box that works when it is plugged in, with the guide kept open for anyone who would rather do it by hand. None of the appliance is built yet; this is the plan, and the next step is one card, imaged once by the Factory, and timed from the power cable to the website.*

The guide's five stages, done by the owner, beside the same work done once by the Factory: two cables and a page.

## In short

- **Today it takes five stages and a Mac.** Image the card, boot, connect over SSH, update, then add the website and the models: the guide I wrote this week, checked against the official getting-started page.
- **Every stage works, and every stage has a choice in it.** The right drive, a host key, an address in a router, a runtime that depends on the site, a model that fits the memory.
- **Each choice is a place where an owner gives up.** The people a sovereign website is for want their website, not a Linux machine to look after.
- **So the guide is turned round.** What it asks the owner to do, the Factory does once, as a build, and tests on a real Pi.
- **One image, and a small part per unit.** The operating system, the runtime and the model are the same on every card; the owner's site and keys are written for each one, and nothing secret is in the image.
- **The Wi-Fi can be set the way a printer does it.** The Pi opens its own setup network on first boot, the owner gives it the home Wi-Fi from a phone, and the password never passes through us.
- **The owner plugs in two cables and opens a page.** The site is served from their shelf, and the agents take signed updates from then on.
- **It scales because every unit is the same.** Test the image once and every card made from it has been tested; fix it once and they are all fixed.
- **For the Kickstarter, we promise a box that works, not a guide.** The guide stays open for anyone who would rather do it by hand.
- **Nothing of the appliance is built yet.** The next step is one card, imaged by the Factory, timed from the power cable to the website.

## The guide, as it stands

The appliance plan has a Raspberry Pi in it ([launching the sovereign website appliance](launching-the-sovereign-website-appliance.md)), and an experiment to run the whole thing on one ([a sovereign website on a Raspberry Pi](a-sovereign-website-on-a-raspberry-pi.md)). Before either can happen, someone has to set the Pi up. So this week I wrote the setup down, the way I would do it from my MacBook, as a guide anyone could follow. It has five stages.

1. **Prepare the card on the Mac.** Install Raspberry Pi Imager, choose the Pi model, choose Raspberry Pi OS Lite 64-bit, which is the command line without a desktop, and choose the 256GB card as the destination, checking it is the right drive, because writing erases it. In the customisation screens, set a hostname, a username and password, the Wi-Fi network and its country, and turn on SSH. Write, let it verify, eject.
2. **Boot the Pi.** Move the card into the Pi, connect Ethernet if you use it, then power, and give the first start a few minutes. No monitor or keyboard is needed; the Mac and the Pi only need to be on the same network.
3. **Connect from the Mac.** In Terminal, `ssh` to the username at the hostname followed by `.local`. Check that it is your Pi before accepting the host key, type the password with nothing showing, and if the name does not resolve, find the Pi's address in the router's list of devices.
4. **Update it.** `sudo apt update`, `sudo apt full-upgrade`, `sudo reboot`, and connect again.
5. **Add the website and the models.** Install the runtime the site needs, such as Python or Node.js, copy or clone the site and its dependencies, set it up as a service so it starts on boot, then install a model runtime for 64-bit ARM Linux and a model that suits the Pi's memory.

And one rule throughout: shut it down with `sudo shutdown -h now` before taking the card out or pulling the power.

Every one of those steps is in the official [getting-started documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html), which I checked them against today: the Pi 5 wants the 27W USB-C supply, Imager asks for the hostname, the user, the Wi-Fi and SSH before it writes, OS Lite is the command-line version for a Pi without a screen, and other devices on the network can reach the Pi at its hostname with `.local`. The guide works.

## Where it stops being simple

Read the guide again as someone who has never opened Terminal, and count the decisions. Which of the drives in Imager's list is the card. What a host key is, and how to tell that it is your Pi. Why nothing appears when you type a password. Where the router keeps its list of devices, and why guest Wi-Fi hides the Pi. Then, in stage five, the two sentences that carry the most weight: the exact commands depend on your website, and storage does not decide which models run well, the memory, the processor, the model's size and the cooling do.

The guide is honest about all of that, and it should be. But each of those decisions is a place where the person it is for stops. A sovereign website is for someone who wants to own their website and be able to move it ([what is a sovereign website](what-is-a-sovereign-website.md)): a founder, a writer, a small business, a family. They want the website. They did not ask for a Linux machine to look after, and the guide, at its best, hands them one.

So the question is not how to make the guide easier to follow. It is who should follow it.

## The steps are the Factory's job

The idea is to turn the guide round. Everything it asks the owner to do on their Mac, we do once, in the Factory, as a build, and the result is an image that every card is written from.

- **Stage one becomes the image.** Raspberry Pi OS Lite 64-bit, for the Pi model in the tier, prepared once, not chosen by each owner from a list.
- **Stage four is done before it ships.** The packages are updated in the build, so the first boot is not a long upgrade, and from then on updates come the way the experiment already plans: a timer that takes a new version only when every commit's signature checks out ([a sovereign website on a Raspberry Pi](a-sovereign-website-on-a-raspberry-pi.md), part 2).
- **Stage five is decided for the owner.** The runtime the site needs is known, because the Factory built the site; the web server and the site's service are set up to start on boot; the model is the one we measured on that Pi's memory, on the Pro tier, behind the local endpoint the build page can call ([watch your website being built](watch-your-website-being-built.md)).
- **The image is tested on a real Pi** before any card is written from it: boot it, serve the site, run the model, check the update path, shut it down cleanly.

This is the same move as [the SGit server factory](the-sgit-server-factory.md) and the rest of how we build: the work an expert does by hand becomes a recipe the agents run, recorded and repeatable, and the expert's time goes into the recipe instead of into each copy.

## One image, and what is different per unit

Not everything can be in one image, and the line between the two parts is the design.

What is the same on every unit goes in the image: the operating system, the updates, the runtime, the web server, the model and the update timer. What is different for each owner is written for that unit: the hostname, their website, the keys that let them and the agents in, and their Wi-Fi if they do not use a cable. These are the same values Imager asks for in its customisation screens, so the per-unit part is small, and the Factory can write it for each card instead of the owner typing it.

Two rules for that part. Nothing secret goes in the image, because one image is copied many times and a secret in it would be on every card. And each unit makes its own identity on first boot, its own host key among them, so no two boxes share one. The owner's site comes from their own repository, or from their vault ([your website, from a vault](your-website-from-a-vault.md)), the same site they saw before anything shipped.

The Wi-Fi does not even have to be typed in by us. A printer solves the same problem: on first start it makes its own small Wi-Fi network, you join it from your phone, tell it the name and password of your home network, and it joins that one instead. The Pi can do the same. Since Bookworm, Raspberry Pi OS manages its network with NetworkManager, as the official [configuration page](https://www.raspberrypi.com/documentation/computers/configuration.html) says, and NetworkManager has a hotspot mode of its own (`nmcli device wifi hotspot`), so a unit that finds no known network on first boot can open its own setup network, the owner joins it from their phone, picks their home Wi-Fi on a page, and the Pi moves across to it. The password then never passes through us at all, and the card in the box is the same for everyone. That setup page and the move from one network to the other are ours to build and test; a network cable remains the simplest way, and needs none of it.

## What the owner does

If the Factory does all of that, the owner's part is short. Take the box out, connect the power and, ideally, a network cable, or join the box's own setup network from a phone to give it the home Wi-Fi; wait the few minutes a first boot takes; open a page on a phone or a laptop on the same network, and see their website, served from the box on their shelf. On the Pro tier, the same page can build or change the site with the model on the device, with nothing leaving the house.

No Terminal, no host key, no router list. The Mac in the guide is gone from the owner's side; it is on ours, in the Factory, where it belongs. And the safe shutdown, the one rule that cannot be skipped on a Pi with a card, becomes a button on that page rather than a command to remember.

## Why it scales

A guide does not scale. Each person who follows it makes their own Pi, slightly differently, and when something goes wrong, the first question is what they did.

An image does. A thousand units written from one tested image are a thousand of the same thing. Testing the image tests them all; a fault found on one is a fault in the image, fixed once and sent to every unit as a signed update. Support becomes a question about one image and a small per-unit part, not about a thousand different machines. And the agents do the rest, the same way on every unit: the updates, the monitoring of the live site, the backup to the vault.

That is the sense in which this "just works out of the box": not that the steps disappeared, but that they are done once, by us, and proven, instead of every time, by someone who did not want to do them.

## What it means for the Kickstarter

The [launch plan](the-launch-plan-in-eleven-turns.md) put the Raspberry Pi in the campaign as a box at home, and [the appliance plan](launching-the-sovereign-website-appliance.md) has two Pi tiers, the standard Pi where we build the site and the Pi runs it, and the Pi Pro that can build sites itself with a local model. This article is how those tiers can be made.

It changes three things about the campaign. The promise is a box that works when it is plugged in, which is something a backer who has never used Terminal can believe. The video can show exactly that: a box out of its packaging, two cables, a page, a website. And the risks section can be honest and short: the image is one thing we test, and the per-unit part is small.

The guide does not go away. It stays published, open, for anyone who would rather do it themselves on their own Pi, and it is also the specification for the image: every step in it is a step the Factory has to do. That is the open source strategy of the plan: anyone can build on it, and we are the ones who show it working.

## Where things stand

The guide exists and works, and its steps match the official documentation. The appliance is not built: there is no image, no per-unit step, no first-boot page and no measured model yet.

So the next step is small and concrete: one card, written by the Factory from a first image, put into the experiment's Pi 5, and timed from the power cable to the website. Then the experiment's measurements on top of it, the model's speed, the time a site takes and the power it uses. Then the same card again, written from the same image, to show that the second unit is the same as the first. That is the proof a campaign needs.

## What this does not claim

- **The appliance is a plan.** No image, per-unit step or first-boot page has been built or tested.
- **The guide's steps are checked against the official page,** not against every Pi model or network; the official documentation is the reference.
- **The image's contents are proposals.** Which web server, which model runtime and which model are to be chosen when they are tested, as in the experiment.
- **No model has been measured on the Pi yet,** so nothing here claims how fast or how good a local model is on it.
- **The tiers are the published plan of 19 November 2026,** and nothing has been submitted to Kickstarter; no goal, date or backer is claimed here.
- **The setup network is a design, not a test.** The hotspot is NetworkManager's own feature; the official Raspberry Pi pages do not cover it, and the first-boot page and the switch to the home Wi-Fi have not been built or tried on the Pi.
- **Reaching the site from the internet is not covered.** The guide and this plan serve the site on the local network; public access needs its own hosting and network setup, as the appliance plan describes.
- **Selling a bundle brings its own obligations,** set out in [where to sell the book and the appliances](where-to-sell-the-book-and-the-appliances.md), and not repeated here.

If you have set up a Raspberry Pi for someone who is not technical, or would like a sovereign website on a box on your shelf, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A setup guide I wrote on 22 November 2026, for preparing a Raspberry Pi with a MacBook and a 256GB card, and my words that day to this newsroom's agents: that we should set it up so that it just works out of the box and it scales, building on the conversation about appliances and the Kickstarter. Written up by newsroom.c, this newsroom's writer on account C, in my voice. The argument and the editorial responsibility are mine. The steps were checked on 22 November 2026 against the Raspberry Pi [getting-started documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html) (the 27W USB-C supply for the Pi 5; Imager's hostname, user, Wi-Fi and SSH settings; OS Lite for a Pi without a screen; the hostname with `.local`). NetworkManager as the default since Bookworm is from the Raspberry Pi [configuration page](https://www.raspberrypi.com/documentation/computers/configuration.html), read the same day; it does not describe a hotspot. The tiers are from [launching the sovereign website appliance](launching-the-sovereign-website-appliance.md), and the signed updates, local model and vault backup from [a sovereign website on a Raspberry Pi](a-sovereign-website-on-a-raspberry-pi.md). Related: [the launch plan in eleven turns](the-launch-plan-in-eleven-turns.md), [where to sell the book and the appliances](where-to-sell-the-book-and-the-appliances.md), [what is a sovereign website](what-is-a-sovereign-website.md), [the SGit server factory](the-sgit-server-factory.md), [watch your website being built](watch-your-website-being-built.md) and [your website, from a vault](your-website-from-a-vault.md).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#out-of-the-box)

### Builds on

- [Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a Raspberry Pi, five tiers from a £50 supporter to £1,000, the two Pro tiers running local AI models that can build a website on the device itself, the hardware we would buy in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone](launching-the-sovereign-website-appliance.md) The Kickstarter plan: a sovereign website on a Raspberry Pi or a tablet, five tiers from £50 to £1,000, local AI on the Pro tiers.
- [A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes](a-sovereign-website-on-a-raspberry-pi.md) The experiment: a sovereign website, its local model, its build and its signed updates, all on one Raspberry Pi 5 at home.
- [What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer](what-is-a-sovereign-website.md) What a sovereign website is: owned and movable, commodity only, seven principles, a maturity model from rented to proven, and every host.
- [Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from](watch-your-website-being-built.md) A page that builds a first version of a sovereign website in your browser, showing every agent, behaviour policy and penny, then hands back a zip.
- [The SGit Server Factory, a brief: an agent and a pipeline that deploy SG/Send and sgit servers the way the site factory makes websites, a request file in and a live, tested server out, in any AWS region and any account, as an ephemeral Lambda, a Lambda on S3, an EC2 appliance or Fargate, with one bootstrap stack to onboard a new account and no keys anywhere](the-sgit-server-factory.md) A brief for the SGit Server Factory: a request file in, a tested SG/Send and sgit server out, in any AWS account and region, with no keys.
- [Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again](your-website-from-a-vault.md) Show someone five versions of their own website without publishing anything: sealed in a vault, opened with a QR code, a link or a zip.
- [The launch plan in eleven turns: how one afternoon took the plan for launching Sovereign Website from a £50 site on Kickstarter, through Indiegogo, PPL, Patreon, countries as stretch goals and the UK as home ground, to a configured Android tablet, a supporter tier and a Raspberry Pi, with every variation we tried and why each was kept or set aside](the-launch-plan-in-eleven-turns.md) How one afternoon took the launch plan from a £50 site on Kickstarter to a configured Android tablet, a supporter tier and a Raspberry Pi.
- [Where to sell the book and the appliances: a map of the places a UK author and maker can sell physical products, printed copies of One Human, Nine Agents, Nineteen Hours from early December and the sovereign website appliances from 1 January after a December Kickstarter, with Amazon, IngramSpark, eBay, OnBuy and our own shop, what each charges, the rules that matter, and the law that comes with selling hardware](where-to-sell-the-book-and-the-appliances.md) Where to sell the printed book and the sovereign website appliances in the UK, when, what each platform charges, and the law that comes with hardware.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 536 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=536)

**Posting this article on LinkedIn?** The cover is [out-of-the-box.jpg](banners/out-of-the-box.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/out-of-the-box.html)*
