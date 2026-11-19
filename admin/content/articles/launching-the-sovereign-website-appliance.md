---
title: Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a set of Raspberry Pis, three tiers from a £50 supporter to £1,000, what we promise to spend on hardware and examples of what that buys in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: This is the plan we arrived at, after an afternoon of turns recorded in the previous piece. We launch Sovereign Website on Kickstarter as an appliance: a sovereign website on a device its owner holds, an Android tablet configured with the site, its editing, its monitoring and an AI app, or a set of Raspberry Pis that serve it from home. Three tiers. £50, the supporter: the website, set up and handed over, no hardware. £500: we spend about £250 on hardware, the backer's choice, a tablet such as a Lenovo Idea Tab at £209.99 today, or two Raspberry Pi 5 kits with 2GB each. £1,000: we spend about £500, a tablet that can run AI models such as a Samsung Galaxy Tab S10 FE at £509, the German-made Volla tablet with the de-Googled /e/OS, or Pi kits, five with 1GB or three with 2GB. Add-ons for their own app or their own product. The UK is the base goal; Portugal is the first stretch goal; backers vote on the countries after it, and on iOS. All-or-nothing: if we do not reach the goal, nobody pays and we build nothing. And we launch on our own, with Android and open source, and talk to device makers once it works.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, crowdfunding, kickstarter, android, raspberry-pi, go-to-market, article
status: published
---

!shot lsa-tiers.webp | images/ | The tiers: what you pledge, and what we spend on hardware, your choice of tablet or Raspberry Pis. | concept

## In short {#in-short}

- **On Kickstarter, as an appliance:** a sovereign website on a device you hold.
- **Android first,** or a set of Raspberry Pis; open source all the way down.
- **Three tiers:** £50 supporter; £500 with about £250 of hardware; £1,000 with about £500.
- **The backer chooses the hardware;** we buy the best available at the time.
- **The UK is the base goal,** Portugal the first stretch goal, then countries and iOS by vote.
- **We launch alone,** and partner once the flow works.

## The product {#product}

A sovereign website is a website its owner owns and can move ([what is a sovereign website](/articles/what-is-a-sovereign-website.html)), built by agents and handed over with [a team inside it](/articles/a-website-with-a-team-inside.html). The appliance puts all of it on a device the owner holds:

- **An Android tablet,** configured with the site, a way to change it by talking, monitoring of the live site, the AI app of their choice (they sign in with their own Claude or ChatGPT account), and a backup to an encrypted vault. The site can also run on the tablet itself, as an installable web app, so it does not depend on any app store.
- **Or Raspberry Pis,** small computers that serve the site from home, deployed from the same repository by the same pipeline that deploys it to GitHub Pages.

On Kickstarter this is a physical product with a working prototype, which is what Kickstarter is for. The site on its own, without a device, stays on sale directly on sovereignwebsite.ai.

## Android, and why not an iPad first {#android}

Android is open source and gives us full control of the device: sgit, the site and the agents' tools can all run on it. The team already had a signed Android tablet build running four hours after its first commit at Web Summit ([native apps by agents](/articles/native-apps-by-agents.html)), and I have the Android tablet I bought for Web Summit to make the prototype and film it. An iPad would mean the App Store and its review, a part we do not control, so iOS is a stretch goal, and backers can tell us if they want one.

## The tiers {#tiers}

- **£50, Supporter.** Your sovereign website, set up and handed over, with no hardware. A real thing, not a donation, and the cheapest way in.
- **£500, Appliance.** Your website, and we spend about £250 on hardware, your choice: a tablet, or two Raspberry Pi kits with 2GB each.
- **£1,000, Appliance Pro.** Your website, and we spend about £500 on hardware, your choice: a tablet that can run AI models on the device, a European tablet, or Raspberry Pi kits, five with 1GB or three with 2GB.
- **Add-ons, at any tier:** your own app made from your site, about £500; your own product configured to run on the device, about £1,500.

The promise is about what we spend, not a model number. Choices are collected after the campaign, in the pledge survey, and we buy the best hardware available for that amount at the time. What is left of each pledge pays for the configuration, the site, the team inside it, support, shipping and the platform's fees.

No T-shirt. It only adds complexity.

## What £250 and £500 buy today {#hardware}

Examples from UK retailers' own pages on 19 November 2026, which will change before we ship:

- **About £250, a tablet:** the Lenovo Idea Tab, 11 inches, 8GB and 128GB, with a pen, £209.99 at John Lewis; or the Samsung Galaxy Tab A11+, 11 inches, from £199 to £259 by option, also at John Lewis.
- **About £500, a tablet for AI on the device:** the Samsung Galaxy Tab S10 FE, 12GB and 256GB, with Galaxy AI, £509 at John Lewis. Two others to compare at the time, whose current prices we could not confirm: Lenovo's Yoga Tab, with a Snapdragon 8 Gen 3 and 12GB, and the OnePlus Pad 3, with a Snapdragon 8 Elite and 12GB, launched at £529.
- **A European tablet:** the Volla Tablet, made by Volla in Germany, sold by Murena with /e/OS, a version of Android without Google: 12.6 inches, 12GB and 512GB, €569.99 in Murena's current offer, normally €649.99. Its chip is old and slow for AI on the device, but for sovereignty it is a strong choice: a European device and an open operating system.
- **Raspberry Pis:** a complete Raspberry Pi 5 starter kit, with the board, power supply, case with fan and a 64GB card, is £99.70 with 1GB of memory and £130.90 with 2GB at The Pi Hut. A static website needs very little memory, so about £250 buys two 2GB kits (£261.80), and about £500 buys five 1GB kits (£498.50) or three 2GB kits (£392.70); the backer chooses.

Memory prices have risen sharply this year, and Raspberry Pi prices with them, which is one more reason the promise is a spend, not a part list.

## A website served from home {#pi}

A sovereign website served from a box its owner holds is sovereignty you can put on a shelf. There are two ways to reach it from the internet. A dynamic DNS name and port forwarding on the home router keep everything in the owner's control, but fail when the internet provider shares one address between customers, and reveal the home's address. A tunnel service works everywhere, but the common ones are proprietary, which is exactly the kind of part in the middle a sovereign website avoids, so a self-hosted tunnel to a small server the owner controls is the better version.

So the honest design is that the Pis are hosts, not the only host: the site stays on GitHub Pages or any static host, and the Pis serve it from home and keep a full copy. With two or five of them, the site runs on more than one machine its owner holds, which is the seventh principle: proven, not claimed.

## The goal and the stretch goals {#goals}

- **The base goal is the UK,** in pounds and in English, with every page in our other languages from day one. It should be a goal we are confident of reaching early; the stretch goals carry it further.
- **Portugal is the first stretch goal:** going there properly, with local partners, demo sites, domain advice for .pt names, and a launch there.
- **Then countries by vote,** each one a place we go to, shown on a map that lights up as backers unlock it.
- **iOS** is a stretch goal too.

Stretch goals are revealed as the campaign goes. It is all-or-nothing: backers are charged only if the goal is met when the campaign ends, and the money arrives once, after it closes. If we do not reach it, nobody pays and we produce nothing.

## Value first {#value}

Every backer can see their own website before anything ships: five designs, made by agents and sealed in a vault they open with a QR code, a link or a zip ([your website, from a vault](/articles/your-website-from-a-vault.html)). The campaign video shows a real tablet, the one from Web Summit, running a real site.

## Launch alone, partner later {#partners}

We do not need a device maker or an operating system to launch with us. We launch with Android out of the box, open source, and our own flow working end to end. Then we talk to the companies that make tablets, small computers and open operating systems, Europe's first, as a project that is already funded and already shipping, which is a much better conversation. That is the open source strategy: anyone can build on it, and we are the ones who showed it working.

## After the campaign {#after}

Late pledges on Kickstarter, then pre-orders on sovereignwebsite.ai, and the plain site on sale there throughout. Patreon later, for the people who want to support the work as it goes, and for the creators whose sites we build to be supported on their own pages ([the launch plan in eleven turns](/articles/the-launch-plan-in-eleven-turns.html)).

## What this does not claim {#limits}

- **Nothing has been submitted to Kickstarter;** its review may ask for changes, and its rules on AI and on services apply.
- **Hardware prices are examples** from UK retailers on 19 November 2026; two tablet prices could not be confirmed.
- **The appliance's software,** the editing, monitoring and vault backup on the device, is a plan; the Android build and the sites exist.
- **The goal amount is not yet set.**

## Where this comes from {#sources}

A conversation in writer-10's session on 19 November 2026, recorded in [the launch plan in eleven turns](/articles/the-launch-plan-in-eleven-turns.html), and hardware prices read that day from [John Lewis's Lenovo Idea Tab](https://www.johnlewis.com/-/p114200305), [Samsung Galaxy Tab A11+](https://www.johnlewis.com/samsung-galaxy-tab-a11-tablet-android-wi-fi-11-inch/grey/p114370544) and [Galaxy Tab S10 FE](https://www.johnlewis.com/samsung-galaxy-tab-s10-fe-tablet-with-bluetooth-s-pen-android-12gb-ram-wi-fi-10-9-inch-256gb/grey/p113528276) pages, [OnePlus's Pad 3 page](https://www.oneplus.com/uk/oneplus-pad-3), [Murena's Volla Tablet](https://murena.com/shop/smartphones/brand-new/murena-volla-tablet/), [The Pi Hut's Raspberry Pi 5 starter kit](https://thepihut.com/products/raspberry-pi-5-starter-kit) and [Raspberry Pi 5](https://thepihut.com/products/raspberry-pi-5). Related: [what is a sovereign website](/articles/what-is-a-sovereign-website.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html), [your website, from a vault](/articles/your-website-from-a-vault.html), [native apps by agents](/articles/native-apps-by-agents.html), [sovereign websites, the investment case](/articles/sovereign-websites-the-investment-case.html).
