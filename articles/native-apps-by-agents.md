# Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief, sgit.ai

> Around Web Summit, our agents built native apps, which I had not expected them to do so fast. On 7 November a small iPhone app, 1,164 lines of Swift, was imported from a vault into its own repository; by 11 November that workspace held four apps sharing thirteen Swift packages and 48,230 lines of code: the public PrompTugal reader, the team's own app, a RiskMandate app, and a guide to the Lisbon Tech Fringe. Every push to the development branch uploaded a build to TestFlight. Apple rejected one upload for a missing purpose string, and a good build followed an hour and twenty-five minutes later. On 8 November at 20:33 an Android app for the RiskMandate stand was started from nothing, and four hours and eleven minutes later a signed build was installed on my tablet; by the end it had 33,042 lines of Kotlin, an on-device Gemma chat and a stand mode. On 11 November the fringe guide went from brief to a valid TestFlight build in about ten and a half hours. This is the fourth article in the Ten days series.

*Source: <https://newsroom.sgit.ai/articles/native-apps-by-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief

# Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/native-apps-by-agents.md) · [newsroom v0.14.103](https://newsroom.sgit.ai/admin/versions.html) · iosandroidappsagentstestflightweb-summitpromptugalseriesarticle

***Abstract:** Around Web Summit, our agents built native apps, which I had not expected them to do so fast. On 7 November a small iPhone app, 1,164 lines of Swift, was imported from a vault into its own repository; by 11 November that workspace held four apps sharing thirteen Swift packages and 48,230 lines of code: the public PrompTugal reader, the team's own app, a RiskMandate app, and a guide to the Lisbon Tech Fringe. Every push to the development branch uploaded a build to TestFlight. Apple rejected one upload for a missing purpose string, and a good build followed an hour and twenty-five minutes later. On 8 November at 20:33 an Android app for the RiskMandate stand was started from nothing, and four hours and eleven minutes later a signed build was installed on my tablet; by the end it had 33,042 lines of Kotlin, an on-device Gemma chat and a stand mode. On 11 November the fringe guide went from brief to a valid TestFlight build in about ten and a half hours. This is the fourth article in the Ten days series.*

The PrompTugal iOS site, its three apps, features and build log, and VoiceDebrief, on 15 November 2026.

## In short

- **Four iOS apps from one workspace,** from 1,164 lines of Swift on 7 November to 48,230 by 11 November.
- **TestFlight on every push** to the development branch, and a first build approved for testers in about a day.
- **An Android tablet app from nothing:** a signed build on my tablet four hours and eleven minutes after the first commit.
- **A fringe guide in a day:** from brief to a valid TestFlight build in about ten and a half hours.
- **Agents in many sessions,** on separate branches, with conductors merging green branches.
- **Part of a series:** this is article four of [Ten days at Web Summit](ten-days-at-web-summit.md).

## From one small app to four

At 01:41 UTC on 7 November, a small iPhone app, version 0.3.1 and 1,164 lines of Swift, was imported from an sgit vault into a new repository. It was the start of PrompTugal's iOS workspace. In the first two days the agents made 517 and then 623 commits, and by 11 November the workspace built four apps from shared code:

- **PrompTugal,** the public reader app: the news, the agenda in Lisbon time, your own day, reminders, offline reading, and a private vault opened with Face ID.
- **Team,** the team's own app: dashboards of people, agents and decisions, briefings, and messages through encrypted vaults.
- **RiskMandate,** the company's app.
- **Lisbon Fringe,** the guide to the summit's fringe events.

By then the workspace had 13 shared Swift packages and 48,230 lines of Swift, all written by agents, and about 1,470 commits across its branches.

Four iOS apps from one workspace and an Android tablet app, and how much code the agents wrote.

## TestFlight on every push

The release pipeline came first. By 22:47 on 7 November, every push to the development branch built the apps and uploaded them to TestFlight, Apple's channel for test builds. The first build was approved by Beta App Review in about 24 hours. Apple also rejected an upload on 8 November, for a missing purpose string explaining why the app uses speech recognition; a good build followed an hour and twenty-five minutes later. At 23:20 that night the public app was submitted to the App Store.

The builds needed Macs, and that turned out to be the real constraint: the agents spent far longer waiting for a Mac than building on one. That is the next article in this series.

## Many sessions, separate branches

The work was spread across sessions, each on its own branch. The build log for one night describes seven sessions, five building the app, one releasing it and one editing the site, with a conductor merging the branches that passed into the development branch about once an hour. There were dozens of role branches, and commits named the agents that made them: conductors, a release agent, and agents from Indi Gupte's and Silvio Switha's teams as well as mine. Indi's agents later submitted more builds for testers on their own.

The iOS build log: seven sessions through the night, a conductor merging green branches about once an hour.

## An Android app for the stand

At 20:33 on 8 November, the Android app for the RiskMandate stand did not exist. At 00:44 on 9 November, four hours and eleven minutes later, a signed build was installed on my tablet, and the next one arrived as a one-tap update through Firebase. The next day was its busiest: 935 commits.

It was built for a tablet on the stand, in Kotlin, and it grew to 33,042 lines. It has a stand mode that pins the screen and resets when idle; a step-through demo of Agent Behaviour Policies in every layer; and a chat with Gemma, a small open model, running on the tablet itself, at about five tokens a second in the one run that was measured. It went to the team's tablets through Firebase App Distribution, not through Google Play, which I decided to leave for later.

## A guide to the fringe in a day

On 11 November, the day after Storm Charles made Web Summit call off its second day, the brief for a Lisbon Fringe app arrived at 10:45. Seven minutes later there was code; in the evening, Indi's design replaced the first version; and at 21:11 the Fringe app was valid in internal TestFlight, about ten and a half hours after the brief. It carried 173 events and a filter for the events the storm had moved, from the same data as [the fringe guide's website](https://lisbontechfringe.com/).

## What it taught us

- **Native apps are within reach of agents:** four iOS apps and an Android app in five days, from a small start and from nothing.
- **Ship the pipeline first:** TestFlight on every push meant every change could be tried on a phone the same day.
- **Shared code pays:** four apps from one workspace and thirteen packages.
- **The bottleneck moves to the machines and the stores:** Macs to build on, and review queues to wait in.

## What this does not claim

- **Figures are from the repositories on 15 November 2026;** line counts are raw lines of Swift and Kotlin files.
- **Commit counts are approximate** across branches; most early commits carry no agent name, so per-agent counts are partial.
- **The Gemma speed is from one measured run.**

## Where this comes from

The repositories PrompTugal__App__iOS, PrompTugal__App__Android and PrompTugal__App__Mobile, read 15 November 2026: their commits, briefs, status files and workflows. Pages: [ios.app.promptugal.news](https://ios.app.promptugal.news/), its [three apps](https://ios.app.promptugal.news/apps.html) and [build log](https://ios.app.promptugal.news/admin/build-log/index.html), and [VoiceDebrief](https://ios.app.voicedebrief.ai/). Earlier on this site: [ten days at Web Summit](ten-days-at-web-summit.md), [the team's operating system](the-teams-operating-system.md), [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#native-apps-by-agents)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.

### Continued by

- [The launch plan in eleven turns: how one afternoon took the plan for launching Sovereign Website from a £50 site on Kickstarter, through Indiegogo, PPL, Patreon, countries as stretch goals and the UK as home ground, to a configured Android tablet, a supporter tier and a Raspberry Pi, with every variation we tried and why each was kept or set aside](the-launch-plan-in-eleven-turns.md) How one afternoon took the launch plan from a £50 site on Kickstarter to a configured Android tablet, a supporter tier and a Raspberry Pi.
- [Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a set of Raspberry Pis, three tiers from a £50 supporter to £1,000, what we promise to spend on hardware and examples of what that buys in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone](launching-the-sovereign-website-appliance.md) The Kickstarter plan: a sovereign website on a configured Android tablet or Raspberry Pis, from a £50 supporter to £1,000.
- [Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these](our-companies-and-uth.md) Each of our companies, technologies and websites mapped to what UAlgTec Heritage needs to build a European HeritageTech sector.
- [Shipping an iOS app with agents: how our agents build, test and send native apps to TestFlight from a Linux container, with CI on a Mac as the compiler, signing done once through the App Store Connect API, every green push in testers' hands, and what the three doors to users took for us, internal testers in about an hour, external testers in half a day to a day, and the App Store still waiting after eight days](shipping-an-ios-app-with-agents.md) How our agents ship iOS apps from Linux containers via CI on a Mac, and what TestFlight and App Store review actually took.
- [Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code](build-on-voicedebrief.md) VoiceDebrief's techniques for any voice app: record without loss, transcribe offline, debrief with Apple Intelligence, voice control, CI.
- [VoiceDebrief, relaunched: what the iPhone and iPad app already does, from recording without loss to an on-device transcript, a debrief and an encrypted vault, why the agent workflows move to the CRM app, and the list that takes it to the App Store properly, under its own name and its own accounts](voicedebrief-relaunch.md) VoiceDebrief is ready for market: record, transcribe and debrief on the device, save to a vault. A simpler relaunch, under its own name and accounts.
- [A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it](a-crm-for-us-and-our-agents.md) Our next stage is a CRM of our own, on vaults with an iOS app, for us and our agents. Twenty leads the field; agents propose, people send.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 417 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=417)

**Posting this article on LinkedIn?** The cover is [native-apps-by-agents.jpg](banners/native-apps-by-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/native-apps-by-agents.html)*
