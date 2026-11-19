---
title: The launch plan in eleven turns: how one afternoon took the plan for launching Sovereign Website from a £50 site on Kickstarter, through Indiegogo, PPL, Patreon, countries as stretch goals and the UK as home ground, to a configured Android tablet, a supporter tier and a Raspberry Pi, with every variation we tried and why each was kept or set aside
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: This is the record of an afternoon of thinking out loud, written down so that none of it is lost. It started with a question, why not launch Sovereign Website on Kickstarter, now that for the first time I have something I can simply give someone, and ended somewhere quite different: a Kickstarter campaign for a sovereign website on a configured Android tablet, with a £50 supporter tier for the site alone and a Raspberry Pi as a box at home. In between there were eleven turns: Kickstarter's rules on services and AI; Indiegogo, PPL and Product Hunt; Patreon and its one-off sales; countries as stretch goals and the angle of bringing sovereign websites to the world; the UK as home ground, with Portugal next; stretch goals as places rather than languages, since every language is there from day one; a hardware appliance, which brings Kickstarter back; iPad or Android, and why TestFlight is not a shop; cost plus 50%, then a simpler promise of what we spend on the tablet; no T-shirt; and the Pi. The plan itself is in the next piece.
version: v0.14.175
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, crowdfunding, kickstarter, go-to-market, android, strategy, article
status: published
---

!shot lpe-turns.webp | images/ | One afternoon, eleven turns: what was set aside, what was kept, and where the launch plan landed. | concept

## In short {#in-short}

- **It started as:** a £50 site on Kickstarter, and £50,000 to hire a team.
- **It ended as:** a sovereign website on a configured Android tablet, on Kickstarter, with a £50 supporter tier and a Raspberry Pi.
- **Eleven turns in between,** each from a question, kept here with why.
- **What held throughout:** one campaign, value first, the UK first, open source.
- **The plan itself** is in [launching the sovereign website appliance](/articles/launching-the-sovereign-website-appliance.html).

## Where the afternoon started {#start}

By the afternoon of 19 November the morning's pieces were out: the name and the domains ([Sovereign Agentic Website](/articles/sovereign-agentic-website.html)), the brief for its site ([designing sovereignwebsite.ai](/articles/designing-sovereignwebsite-ai.html)), a site with [a team inside](/articles/a-website-with-a-team-inside.html), demos [from a vault](/articles/your-website-from-a-vault.html), [the investment case](/articles/sovereign-websites-the-investment-case.html), and [what a sovereign website is](/articles/what-is-a-sovereign-website.html), its principles now at sovereignwebsite.org. The next question was the launch.

## 1. Why not Kickstarter? {#kickstarter}

For the first time, I have a platform I can just give somebody: a website. So why not a Kickstarter, with the £50 site as a reward, a goal of about £50,000 to hire a team and launch in several countries, a mix of offerings, and all the visibility a launch brings? I can fulfil it even if the number is low.

The research said: careful. Kickstarter is for new creative work, and its rules, as quoted from a copy of its rules page, exclude projects "centered around establishing and providing services"; it allows generative AI if disclosed, but not projects "where AI output makes up most of the work" ([Kickstarter on AI](https://help.kickstarter.com/hc/en-us/articles/16848396410267)). It supports UK creators, but Portugal is not one of its 25 creator countries ([who can use Kickstarter](https://help.kickstarter.com/en-us/articles/16236650-who-can-use-kickstarter)), and Portuguese is not one of its page languages. A website built by agents and sold as a service hits both rules.

## 2. Indiegogo, PPL and Product Hunt {#indiegogo}

So the first plan was Indiegogo. Since October 2025 it is all-or-nothing too, at 5% plus 3% and 0.20 per transaction ([Indiegogo fees](https://help.indiegogo.com/article/596-fees)), it pays out in the UK and Portugal, and it can import backers from another campaign. PPL, Portugal's own platform, would be a Portuguese second wave, and Product Hunt the launch-day noise.

The question of running on two or three platforms at once settled itself: Kickstarter recommends "just one campaign, on one site" ([multiple platforms](https://help.kickstarter.com/en-us/articles/16236800-can-i-launch-my-project-on-multiple-platforms)), and splitting the total makes each part look smaller, which is the opposite of a launch. One campaign, then late pledges and pre-orders elsewhere.

And because it is all-or-nothing, the goal should be one we are confident of reaching early, with stretch goals beyond it.

## 3. Patreon {#patreon}

What about Patreon, where people support someone directly, including the people we work with? It can take one-off payments, through its shop of digital products and posts ([selling posts and collections](https://support.patreon.com/hc/en-us/articles/28352305460749-Selling-posts-and-collections-FAQ)), but it is built for ongoing support. So it became the second act: a supporters' page after the campaign, and a way for the people whose sites we build to be supported on their own pages, which a sovereign website can link to.

## 4. Countries as stretch goals {#countries}

The campaign needed an angle, and going to different countries gave it one: bring sovereign websites to the world, one country at a time. Backers unlock the next country and vote on which; a map lights up as they do.

## 5. The UK is home ground {#uk}

I first put Portugal as the first stretch goal, as home ground. But my home ground is the UK. So the UK goes in the base goal, where the campaign runs, in pounds and in English, and Portugal is the first stretch goal: deep roots, material already there, and likely to unlock early.

## 6. Places, not languages {#places}

But we will launch in several languages straight away; it makes no sense not to. So a stretch goal cannot be a language. It is a place: going there properly, with local partners, demo sites, perhaps for local charities, domain advice for its names, an event or a person. Stretch goals do not have to be announced at the start; most campaigns reveal them as they go. And with all-or-nothing, the money arrives once, at the end, only if the goal is met; nothing is paid out as each stretch goal is passed.

## 7. A hardware appliance {#appliance}

Then the idea that changed the plan, one I had already had at Web Summit: sell a tablet fully configured with all of it. The website, the editing, the monitoring, Claude or ChatGPT installed, the whole flow on one device. A sovereign website on a tablet: it can run the site locally, change it by talking, and back it up to a vault.

It also brings Kickstarter back. A physical product with a real prototype is what Kickstarter is for, and the site and its agents become the software that ships on it. The plain website stays on sale on its own, on sovereignwebsite.ai.

## 8. iPad or Android {#android}

An iPad was the first thought. But Android is open source, gives full control of the device, and the team already had a signed Android tablet build running four hours after its first commit at Web Summit ([native apps by agents](/articles/native-apps-by-agents.html)). TestFlight is for beta testing, not for selling to customers, so iOS really means the App Store and its review, and the App Store is itself a part you do not control. Android first, then: sgit and everything else can run on it with no limits, iOS becomes a stretch goal, and backers can tell us if they want an iPad. And it may not need to be an app at all: a site that installs like an app and runs on the device is enough.

Along the way a website turned out to be an application: a sovereign website is a sovereign application you own, which is why the app should be one way in, never the only one.

## 9. Cost plus 50%, then a simpler promise {#price}

To be transparent, I first proposed showing the tablet's cost plus 50% for the work, plus shipping. It sounded fair, but it is complicated to explain and moves with exchange rates. The simpler promise is what we spend: of a £500 pledge, about £250 goes on the tablet; of a £1,000 pledge, about £500, on the best one available at the time. That also opens the door to buying a European tablet.

## 10. A £50 supporter, and no T-shirt {#supporter}

Is a T-shirt worth it? No: it adds complexity. But a £50 supporter tier is: the sovereign website without a tablet, a real thing rather than a donation, and the cheaper way in that most backers choose. Above the tablets, the work we can do with them: their own app from their site, or their own product configured to run on the device.

## 11. A Raspberry Pi too {#pi}

And finally: why not a Raspberry Pi? It is a website. The same pipeline that deploys to GitHub Pages can deploy to a small computer at home, and a sovereign website served from a box its owner holds is sovereignty you can put on a shelf.

## What held throughout {#held}

- **One campaign,** one link, one total that keeps climbing.
- **Value first:** every backer can see their own site, in a vault, before it ships.
- **The UK first,** then country by country.
- **Open source** all the way down, launching on our own, and partnering with device makers later, once the flow is working and we look the part.

## What this does not claim {#limits}

- **This is a record of thinking,** not a decision; the plan is in the next piece.
- **Platform rules and fees are as their own pages showed on 19 November 2026,** except Kickstarter's rules page, read through a copy, and Indiegogo's creator rules, which did not load.
- **Nothing has been submitted** to any platform.

## Where this comes from {#sources}

A conversation in writer-10's session on the afternoon of 19 November 2026, and the platform research done for it: [Kickstarter on AI](https://help.kickstarter.com/hc/en-us/articles/16848396410267), [who can use Kickstarter](https://help.kickstarter.com/en-us/articles/16236650-who-can-use-kickstarter), [Kickstarter on multiple platforms](https://help.kickstarter.com/en-us/articles/16236800-can-i-launch-my-project-on-multiple-platforms), [Indiegogo fees](https://help.indiegogo.com/article/596-fees), [Indiegogo's platform upgrade](https://help.indiegogo.com/article/645-what-changed-with-the-platform-upgrade), [PPL's FAQ](https://ppl.pt/en/faq), [Patreon on selling posts](https://support.patreon.com/hc/en-us/articles/28352305460749-Selling-posts-and-collections-FAQ). Related: [native apps by agents](/articles/native-apps-by-agents.html), and the day's pieces linked above.
