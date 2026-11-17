# Shipping an iOS app with agents: how our agents build, test and send native apps to TestFlight from a Linux container, with CI on a Mac as the compiler, signing done once through the App Store Connect API, every green push in testers' hands, and what the three doors to users took for us, internal testers in about an hour, external testers in half a day to a day, and the App Store still waiting after eight days, sgit.ai

> Building native iOS apps solved a lot of problems for us, and shipping them turned out to be the part worth explaining. Our agents work in Linux containers that cannot compile Swift, so CI on a Mac is the compiler: every push runs one Mac job that builds and tests, and copies the errors into the job summary where an agent can read them. Signing is done once, through an App Store Connect API key: archive unsigned, sign ad hoc with the entitlements, export with cloud-managed signing and upload. Every green push to the development branch goes to TestFlight, and a script sends it to external testers with its release notes as What to Test. Then there are three doors to users, and our experience of each, in November 2026. Internal testers, people you add to your App Store Connect team, have a build within about an hour, often less. External testers, by email or a public link, go through Beta App Review: about half a day to a day, and our first approval took about 24 hours. And the App Store itself: PrompTugal's public app has been waiting for review since 8 November, eight days and counting, possibly because that build is now out of date. For most validation, the first two doors are more than enough. Here is the pipeline, the doors, and a prompt to set it up with your own Claude.

*Source: <https://newsroom.sgit.ai/articles/shipping-an-ios-app-with-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Shipping an iOS app with agents: how our agents build, test and send native apps to TestFlight from a Linux container, with CI on a Mac as the compiler, signing done once through the App Store Connect API, every green push in testers' hands, and what the three doors to users took for us, internal testers in about an hour, external testers in half a day to a day, and the App Store still waiting after eight days

# Shipping an iOS app with agents: how our agents build, test and send native apps to TestFlight from a Linux container, with CI on a Mac as the compiler, signing done once through the App Store Connect API, every green push in testers' hands, and what the three doors to users took for us, internal testers in about an hour, external testers in half a day to a day, and the App Store still waiting after eight days

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/shipping-an-ios-app-with-agents.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · iostestflightapp-storecigithub-actionsagentsvoicedebriefarticle

***Abstract:** Building native iOS apps solved a lot of problems for us, and shipping them turned out to be the part worth explaining. Our agents work in Linux containers that cannot compile Swift, so CI on a Mac is the compiler: every push runs one Mac job that builds and tests, and copies the errors into the job summary where an agent can read them. Signing is done once, through an App Store Connect API key: archive unsigned, sign ad hoc with the entitlements, export with cloud-managed signing and upload. Every green push to the development branch goes to TestFlight, and a script sends it to external testers with its release notes as What to Test. Then there are three doors to users, and our experience of each, in November 2026. Internal testers, people you add to your App Store Connect team, have a build within about an hour, often less. External testers, by email or a public link, go through Beta App Review: about half a day to a day, and our first approval took about 24 hours. And the App Store itself: PrompTugal's public app has been waiting for review since 8 November, eight days and counting, possibly because that build is now out of date. For most validation, the first two doors are more than enough. Here is the pipeline, the doors, and a prompt to set it up with your own Claude.*

From a push to a phone: one Mac job, signing through the API key, TestFlight, external testers, the App Store.

## In short

- **Native iOS apps solved a lot of problems for us;** shipping them is the part worth explaining.
- **CI is the compiler:** agents in Linux containers push, a Mac builds and tests, errors come back as text.
- **Signing once, through the API key:** archive unsigned, sign with the entitlements, export and upload.
- **Every green push goes to TestFlight,** and on to external testers with its release notes.
- **Internal testers: about an hour.** External testers: about half a day to a day. The App Store: still waiting after eight days.
- **For most validation, TestFlight is enough,** including a public link.

## Why native

For a lot of what we build, a website is enough. For VoiceDebrief it was not: recording that never loses a note, transcription and debriefs on the device with Apple's models, keys in the Secure Enclave, the share sheet. Those need a native app, and once we could build one with agents, a lot of problems simply went away ([build on VoiceDebrief](build-on-voicedebrief.md)). The surprise was how much of the work was not the code but the road to people's phones. At Web Summit, four iOS apps and an Android app came out of five days ([native apps by agents](native-apps-by-agents.md)). This is how they ship.

## CI is the compiler

Our agents run in Linux containers, which cannot build Swift. So the repository's rule is that CI is the compiler. An agent pushes; GitHub Actions runs one Mac job that tests the vault engine, builds for the simulator, builds Release for a device, and runs the unit tests on an iPhone and an iPad simulator. Each step goes through a small script that copies compiler errors and failed tests into the job summary, so an agent reads its own failures through the Actions API and fixes them, without ever seeing Xcode (`ios.yml`, `.github/scripts/run-and-summarize.sh` in [VoiceDebrief__App__iOS](https://github.com/VoiceDebrief/VoiceDebrief__App__iOS)).

One Mac job per push matters. We learned the hard way that ten separate Mac jobs per push, on a pool of five Macs, meant builds waited three times longer than they ran; one job per push, and one integrated build an hour at night, fixed it ([the Mac bottleneck](the-mac-bottleneck.md)).

Because nobody can run the app from a container, CI also photographs every screen, from invented sample data with the network off, on an iPhone and an iPad, light and dark, and synthetic users review the pictures. That is how an agent sees what it built.

## Signing, once

Signing is where most people lose a day, and where we lost a few. What works, in `scripts/release/testflight.sh`:

1. **Install the App Store Connect API key** from CI secrets (`ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_KEY_P8_BASE64`) and the team id; the key needs the Admin role.
2. **Archive unsigned,** for a generic iOS device. Letting the archive sign automatically creates a development certificate on every run and uses up the account's limit.
3. **Sign the app ad hoc** with its entitlements file, so the export knows what the app declares.
4. **Check the archive is the app you mean,** by its bundle id.
5. **Export with destination "upload":** Xcode signs with a cloud-managed distribution certificate and profile, and uploads.

CI owns the version and the build number, so two agents never race for them. A missing purpose string (why the app uses speech recognition) got one upload rejected; a good build followed 85 minutes later.

## Every green push, to testers

Every green push to the development branch uploads to TestFlight. Then a second workflow puts it in front of external testers: it waits for App Store Connect to finish processing, writes What to Test from that version's release notes, adds the build to the external group and submits it for Beta App Review; a newer build replaces one still waiting, and `[internal]` in a commit message holds one back (`testflight-external.yml`, `testflight_external.py`). A third workflow pulls the crash reports testers share into a job summary, so an agent can read them without App Store Connect (`testflight-crashes.yml`). The App Store submission itself stays a manual, deliberate step: metadata, screenshots, pricing and the privacy questions ([PrompTugal__App__iOS](https://github.com/PrompTugal/PrompTugal__App__iOS), `ios-submit.yml`).

## Three doors, and how long each took

Three doors to users: internal testers in about an hour, external in half a day to a day, the App Store still waiting.

This is our experience, in November 2026, and it is the part I most want people to know before they plan a launch.

- **Internal testers: about an hour, often less.** No review. The catch: they have to be added to your App Store Connect team, as users of your developer account. For a small team, this works really well.
- **External testers: about half a day to a day.** Invite people by email, or share a public link that anyone can use. The first build of an app goes through Beta App Review; PrompTugal's first was approved in about 24 hours, and later builds have been quicker. With a public link, this is more than enough for validation, and I think it suits most people's use cases.
- **The App Store: still waiting.** PrompTugal's public app, version 0.4.24 (build 205), was submitted just before midnight on 8 November and has been "Waiting for Review" since: eight days and counting as I write. It could be a queue; it could be the app, and to be fair that build is now well out of date, with fixes on the development branch waiting for it. Either way, do not plan a launch that depends on a date for App Store review.

So for an early product: ship to TestFlight from day one, use internal testers for the team and a public external link for everyone else, and treat the App Store as a separate milestone.

## How fast it can be

With this pipeline in place, VoiceDebrief went from an empty repository to an accepted TestFlight upload in about an hour, reusing the vault engine and the release scripts from PrompTugal. A fringe guide went from brief to a valid TestFlight build in about ten and a half hours. The speed comes from the pipeline being copied, not rebuilt.

## The prompt for your Claude

```

Set up CI so that agents without a Mac can build, test and ship my
iOS app [name, bundle id] to TestFlight.
Use the open-source VoiceDebrief iOS repository as the reference:
https://github.com/VoiceDebrief/VoiceDebrief__App__iOS (Apache 2.0).
Read website/develop/index.md first, then .github/workflows/ios.yml,
.github/scripts/run-and-summarize.sh, scripts/release/testflight.sh,
.github/workflows/testflight-external.yml and
.github/scripts/testflight_external.py.

1. One Mac job per push: build, unit tests on an iPhone and an iPad
   simulator, errors copied into the job summary.
2. Signing through an App Store Connect API key (tell me exactly which
   secrets and roles I must create, and where).
3. Upload to TestFlight on every green push to dev; CI owns the
   build number.
4. Optional: send each build to an external group for Beta App Review,
   with release notes as What to Test.
5. Optional: a screenshot of every screen from sample data.
List what I must do by hand in App Store Connect, and credit the source.

```

## What this does not claim

- **The timings are our experience,** not Apple's commitments, and they vary.
- **The App Store wait is one submission;** I do not know why it is still waiting.
- **The App Store submission is manual by design;** only TestFlight is automatic.
- **Agents still cannot test speech, Apple Intelligence or passkeys** in CI; those need a person with a device.

## Where this comes from

The repositories [VoiceDebrief__App__iOS](https://github.com/VoiceDebrief/VoiceDebrief__App__iOS) (`website/develop/index.md`, `scripts/release/testflight.sh`, its workflows and `.github/scripts/testflight_external.py`) and [PrompTugal__App__iOS](https://github.com/PrompTugal/PrompTugal__App__iOS) (its briefs and `ios-submit.yml`), read on 17 November 2026. My own experience of TestFlight and App Store review, November 2026. Earlier on this site: [native apps by agents](native-apps-by-agents.md), [the Mac bottleneck](the-mac-bottleneck.md), [VoiceDebrief, relaunched](voicedebrief-relaunch.md), [build on VoiceDebrief](build-on-voicedebrief.md).

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#shipping-an-ios-app-with-agents)

### Builds on

- [Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code](build-on-voicedebrief.md) VoiceDebrief's techniques for any voice app: record without loss, transcribe offline, debrief with Apple Intelligence, voice control, CI.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [VoiceDebrief, relaunched: what the iPhone and iPad app already does, from recording without loss to an on-device transcript, a debrief and an encrypted vault, why the agent workflows move to the CRM app, and the list that takes it to the App Store properly, under its own name and its own accounts](voicedebrief-relaunch.md) VoiceDebrief is ready for market: record, transcribe and debrief on the device, save to a vault. A simpler relaunch, under its own name and accounts.

### Continued by

- [Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code](build-on-voicedebrief.md) VoiceDebrief's techniques for any voice app: record without loss, transcribe offline, debrief with Apple Intelligence, voice control, CI.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 444 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=444)

**Posting this article on LinkedIn?** The cover is [shipping-an-ios-app-with-agents.jpg](banners/shipping-an-ios-app-with-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/shipping-an-ios-app-with-agents.html)*
