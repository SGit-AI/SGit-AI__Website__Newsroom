---
title: The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: When agents write native apps, the scarce thing is not the agents. It is the machines they build on. Over two days around Web Summit, our iOS builds used 6,980 minutes of Mac time and spent 22,427 minutes waiting for a Mac, on a pool of five hosted macOS runners that was full for 1,177 of the 1,524 minutes any Mac job ran. Each push to dev that changed app code took a median of ten separate macOS jobs, each starting cold, and 821 jobs on side branches were cancelled before they ever got a Mac. I could see that the allocation of the Mac was the bottleneck; an agent measured it, across 579 workflow runs, and changed the pipeline so that a push takes one Mac job: build everything, test on the iPhone and iPad simulators, and publish to TestFlight from dev only when every test passed. Six days later, with many agent sessions pushing through the night, the runners flooded again, and the fix was a rule rather than code: workers push to branches with no CI, and the conductor runs one integrated build an hour. Night builds went from about 35 minutes to about 7, and a push now reaches TestFlight in 19 to 44 minutes when a Mac is free.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: ios, ci, github-actions, macos, testflight, agents, web-summit, series, article
status: published
---

!shot mac-queue.webp | images/ | Two days of iOS builds: 6,980 Mac-minutes run, 22,427 queued, on a pool of five Macs that was nearly always full. | chart

## In short {#in-short}

- **The agents were not the bottleneck; the Macs were.** Our iOS jobs waited about three times longer than they ran.
- **Ten Macs per push:** every build, test and upload step took its own Mac, each starting cold, all queuing for five slots.
- **An agent measured it** across 579 workflow runs, then rebuilt the pipeline: one Mac job per push, publish from dev only when green.
- **Then the runners flooded again,** with many sessions pushing at night; the fix was a rule: one integrated build an hour.
- **Now:** night builds in about 7 minutes, and push to TestFlight in 19 to 44 minutes when a Mac is free.

## Part five of ten days {#series}

This is part five of [ten days at Web Summit](/articles/ten-days-at-web-summit.html), the series about what six of us (Dinis Cruz, Angelo Leggio, Vicky Wang, Silvio Switha, José Bota and Indi Gupte) built with around 250 agents between 3 and 13 November. Part four, [native apps by agents](/articles/native-apps-by-agents.html), told how a small iPhone app became four apps sharing thirteen Swift packages in five days, with every push to dev going to TestFlight. This is the part of that story that was not about code at all.

## What I could see {#diagnosis}

On 10 November, at about 02:40 in the morning, I asked for the pipeline to change. My words, as the brief records them: "the CI pipeline that we have is good, but it's very inefficient, because it has lots of steps, and the steps all need a separate Mac ... the allocation of the Mac is where the bottlenecks are. So we need to reduce the number of steps, and we need to publish directly from dev."

I could see it from the outside: agents finishing work in minutes and then waiting most of an hour to see it on a phone. I could not say how much, or why. That is what I asked an agent to find out.

## What the agent measured {#measured}

The iOS devops agent wrote a small script, `measure.py`, and ran it over every workflow run and job of the previous two days: 579 runs, from 8 November at midnight to 10 November at 04:00. It counted a job as run only if it got a runner, because jobs cancelled while waiting also carry start and end times.

The numbers were stark. Our pool was five hosted macOS jobs at once, and for 1,177 of the 1,524 minutes when any Mac job ran, exactly five were running: the pool was full. The 1,244 jobs that got a Mac ran for 6,980 minutes and waited 22,427. A typical job ran for about five minutes after waiting 12.2 (the slowest tenth waited 45 minutes or more, the worst two hours).

Each push to dev that changed app code took a median of ten macOS jobs, and up to thirty. For every affected app: a Debug simulator build, a Release device build, iPhone tests and iPad tests, four Macs; one more Mac for each affected Swift package, up to twelve; and two more to archive and upload. From push to the last TestFlight upload took a median of 47.5 minutes.

## Six reasons for the wait {#reasons}

The agent's brief lists them, and each is worth knowing for anyone running agents against shared machines:

1. **Every step was its own Mac,** queuing on its own for the same five slots. The builds ran for under three minutes after waiting more than seven.
2. **Every job started cold:** a full checkout, Xcode selected, a simulator booted, everything compiled from nothing. The iPhone and iPad test jobs each built the same app again.
3. **Three stages in sequence,** release, package, TestFlight, each queuing again.
4. **The upload did not wait for the tests:** a red run could still upload.
5. **A Mac sat idle while Apple processed the build,** polling for up to twenty minutes.
6. **Side branches crowded out dev.** Manual runs on agents' branches used half of all Mac minutes, and 821 of their jobs were cancelled before they got a Mac at all.

## One Mac per push {#one-mac}

The change put all the Mac work of a run into one job. It builds every affected app and package first, with no simulator running, in one shared build folder; then boots the iPhone simulator and runs every test there; then the iPad simulator; and only on a green dev push does it sign, archive and upload to TestFlight. The wait for Apple's processing moved to a Linux runner, so no Mac sits idle for it.

The first runs taught two things worth passing on. Booting the simulators while compiling roughly tripled build time on the three-core runner, so the order matters: build first, then test. And building for a specific simulator device failed while the simulators were booting, so the job builds for the generic simulator destination instead. With one shared build folder, each package went from six to eight minutes as its own job to one or two.

!shot mac-change.webp | images/ | What changed: ten macOS jobs per push became one, and night builds went from about 35 minutes to about 7. | comparison

The result: one macOS job per push instead of ten; about 40 Mac-minutes for the heaviest possible push, which builds and uploads every app, against a median of 56.8 before; and an upload that now waits for every test. The trade-off was explicit in the brief: pushes now take turns on their one Mac, so when they land faster than about every forty minutes, the next one waits, and a newer push replaces the waiting one and covers both.

## Then it flooded again {#flood}

That trade-off came due on the night of 15 November. Several agent sessions were building the local news features for the iPhone app, and they were all pushing. At 00:35 the shared macOS runners were flooded again: about thirty iOS runs in an hour, each more than 25 minutes, most cancelled by the next push. I wrote to the conductor what I needed: "builds must go fast, I need to test quickly."

This time the fix was not in the pipeline; it was in how the team worked. Workers push only to their own work branches, which run no CI, and tell the conductor when they are ready. The conductor merges the ready work and runs one build an hour for everyone; green goes to dev. A devops agent then cut the night builds to what had changed: only the affected apps, a Debug build, no Release build. Night builds went from about 35 minutes to about 7. Dev pushes now test on the iPhone simulator only and upload the news app first, the one on my iPad.

## Where it stands {#now}

!shot mac-status.webp | images/ | The live CI status page on ios.app.promptugal.news: push to processed in TestFlight, per app and per run. | screenshot

The iOS site now has a [CI status page](https://ios.app.promptugal.news/admin/status.html), and the app a matching screen, that show how long a push takes to reach production. When I read it this morning, the latest push took 20 minutes 42 seconds to be processed in TestFlight, with a median of 24 minutes 36 seconds over nine pushes. Overnight, seven builds of the news app went from dev to TestFlight between 01:54 and 05:54. The open question, waiting on me, is whether to pay for larger macOS runners or a Mac of our own.

## What it taught us {#lessons}

- **Agents scale; shared machines do not.** Every new session is another set of jobs for the same five Macs.
- **Measure before you fix.** I could see the wait; the agent could count it, and the counts showed where half the Mac time went.
- **Fewer, longer jobs beat many short ones** when the scarce thing is a slot, not compute.
- **Some fixes are rules, not code.** One integrated build an hour, run by the conductor, did more on the night than any pipeline change.
- **Show the number.** A status page that says how long push to production takes keeps everyone, agents included, honest about it.

## What this does not claim {#limits}

- **The two-day figures are the agent's measurements,** from GitHub's run and job data, 8 to 10 November; I did not re-run them.
- **The "after" figures are from two runs** that built every app; most pushes touch fewer and are faster.
- **The night figures are from the conductor's notes** for 16 November, approximate as written there.
- **Mac minutes are on GitHub's hosted runners** under our plan; I do not price them here.

## Where this comes from {#sources}

The repository PrompTugal__App__iOS, read on 16 November 2026: the brief `briefs/2026-11-10__ci-on-one-mac/` (README and `measure.py`), the brief `briefs/2026-11-15__going-local/` (`tonight.md`, the CI rule and where it stands), its commits and workflows. The live [CI status page](https://ios.app.promptugal.news/admin/status.html), read 16 November 2026. Earlier in the series: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [the team's operating system](/articles/the-teams-operating-system.html), [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [native apps by agents](/articles/native-apps-by-agents.html).
