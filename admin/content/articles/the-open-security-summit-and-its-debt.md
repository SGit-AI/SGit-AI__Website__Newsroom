---
title: The Open Security Summit and its debt: how a summit that treated every participant as a presenter stalled on its own website, what the code shows, and why agents make it worth restarting
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: The Open Security Summit is something I started a long time ago, out of the OWASP Summits of 2008, 2011 and 2017. What made the in-person summits work was that every participant was treated as a presenter: working sessions, collaboration, outcomes. In 2018 the website was part of that: 180 different people committed to it that year, editing their own pages and sessions, 434 commits on the first day alone. Then the summit went online, became monthly mini-summits, and kept going until the end of 2024. But each year's site was a copy of the last, with more exceptions added and no time to refactor. The template code grew from about 5,200 lines to 9,600 and then froze in 2022, while the content kept coming; the number of people committing fell from 180 to 14. The technical debt ground it to a halt, and the follow-up, the personal path for each participant that the in-person summits had, never scaled. It holds a lot of very good material on security, 194 recorded sessions among it. I kept it alive at a cost to me. Now, with agents to map it, follow up and personalise, it is time to restart it: in person in London, online, and as a home for open source projects. It needs someone to fund it.
version: v0.13.22
license: https://creativecommons.org/licenses/by/4.0/
tags: open-security-summit, technical-debt, community, events, agents, article
status: published
---

!shot os-commits.webp | images/ | Left: commits a quarter across the four summit websites. Right: people committing each year, 2018 to 2025. | comparison

## In short {#in-short}

- **Every participant was a presenter.** That was the model, from the OWASP Summits to the Open Security Summit.
- **The website was part of it.** In 2018, 180 people committed to it, 434 commits on the first day.
- **Then the debt grew.** Each year's site was a copy of the last, with more exceptions and no refactoring.
- **The code froze in 2022.** About 9,600 lines of templates, while the content kept coming.
- **The people went.** From 180 committing in 2018 to 14 in 2024.
- **The follow-up never scaled.** And that was what made the in-person summits work.
- **It is time to restart it.** With agents, in London, online, and as a home for projects. It needs funding.

## Where it came from {#history}

The Open Security Summit grew out of the OWASP Summits I helped organise: the Algarve in 2008, Lisbon in 2011, and Woburn in 2017, which I wrote up in [a history of the in-person summits](https://diniscruz.ai/2025/06/07/history-and-analysis-of-owasp-in-person-summits.html). After 2017 it carried on as the Open Security Summit: in person at Woburn Forest, 4 to 8 June 2018, and again in England, 3 to 7 June 2019; fully online, 15 to 19 June 2020; and then as monthly online mini-summits, from October 2020 to September 2024. Since 9 April 2019 it has been a UK community interest company, Open Security Summit CIC, and this week we proposed it as the home of [Agent Behaviour Policies](/articles/agent-behaviour-policies-move-to-the-open-security-summit.html).

What made the in-person summits powerful was simple to say and hard to do: every participant was treated as a presenter. It was never a conference of talks. It was working sessions, collaboration, people preparing before and producing outcomes after. That is even more needed today.

## The website was part of the summit {#website}

The website was not a brochure. It was a Hugo site in a public repository, and participants edited it: their own pages, their sessions, the outcomes. In 2018, 180 different people committed to it. On 4 June 2018, the first day of the summit, the site took 434 commits; on 2 and 3 June 2019, nearly 600. I was the one doing a lot of the programming, and in a couple of those summits we really nailed the structure: participants, sessions, tracks, schedules and outcomes, all as files, all linked.

## What the code shows {#code}

!shot os-frozen.webp | images/ | Left: lines of Hugo template code, 2018 to now. Right: content files in the current site, 2020 to 2024. | comparison

I went back to the repositories. The OpenSecuritySummit organisation on GitHub has 24 of them; four are the summit websites, `oss2018`, `oss2019`, `oss2020` and `oss-website`, with 19,045 commits between them. Read as a record, they show the debt growing:

- **Each year was a copy of the last.** 171 of the 2019 site's 186 template files had the same paths as 2018's, and 272 of the current site's 315 came from 2020.
- **The templates kept growing.** About 5,200 lines in 2018, 5,700 in 2019, 8,500 in 2020 and 9,600 in the current site; the `if` and `with` conditions in them went from 255 to 408, and the partials from 110 files to 218.
- **Then the code stopped changing.** From 2022 the template code barely moved, about 9,600 lines from mid-2022 to today, while the content files went from 140 to 998. Nobody had the time to change the structure, so everything new went into a structure that could not change.
- **Exceptions accumulated.** 39 template files have a year written into them, and 37 of the 218 partials are never called by name, among them pages for 2017, 2018 and 2019 that stayed in.
- **Leftovers were copied forward.** The 2019 venue page still says `year: 2018`; the 2022 sessions page still carries a note to add content "from the next 2021 main Summit event"; the current repository's README still welcomes you to the Open Security Summit 2021.
- **The platform kept moving underneath.** The build went from Hugo 0.55 on AWS CodeBuild in 2019 to GitHub Actions, and the Hugo version was pinned and re-pinned: 0.75 in 2020, four different versions in January 2023, 0.139 in December 2024. The theme is a third-party Hugo theme, kept as a submodule.

None of that is unusual. It is what happens to any site that is built in bursts, around an event, by someone who is also organising the event. It was a salad of code, and whenever we had a new summit and wanted to change something, there was never the time to refactor first. So the debt just kept growing, until it stalled.

## The people went {#people}

The clearest number is the one on the right of the first chart. 180 people committed to the summit's website in 2018, 121 in 2019, 50 in 2020, 24 in 2021, and 14 in 2024. Commits stayed high through 2022 and 2023, but they came from fewer and fewer people. The site stopped being something participants could change, and became something a few of us maintained.

And the live site shows where it stopped. Its home page still says "Open Security Summits in 2024", with "Next Summit: 9th - 13th Dec 2024". The last session page is from 2025, the last real work from December 2024.

## The follow-up never scaled {#follow-up}

!shot os-sessions.webp | images/ | Sessions on the current site by year, and how many link a recording, from 2020 to 2024. | comparison

The sad part is what is in there. The summit holds a lot of very good material on security: working sessions on application security, threat modelling, DevSecOps, governance, and, when this whole AI wave started, some very good sessions on it. The current site alone has 409 session pages from 2020 to 2024, and 194 recordings. Some of my own history, and a lot of knowledge I shared in those sessions, is in those videos, and it got lost.

What never scaled was the follow-up. In person, the summit worked because of what happened before and after the sessions: preparation, outcomes, people connected to the next thing. Online, we could run the sessions, but we could not afford to create a personal path for each participant, to follow up, to connect what was said to who should hear it. That is the same pattern as [the jobs that never scaled](/articles/jobs-that-never-scaled.html): the value is in the before and the after, and they cost too much. I kept funding it, at some cost to me, and it still did not fulfil its potential.

## Why now {#now}

!shot os-loop.webp | images/ | How the debt grew, as a loop of copying, exceptions and slower changes, and the restart that follows. | concept

The difference now is the workflow I have. I am not going to start by rebuilding the website. I am going to put an agent on the case: to understand everything that is there, map the data, connect the dots, analyse the videos and what was said in them, and create much better personal pages for everybody. Then follow up with people, which is the part we could never afford.

From there, the plans:

- **In person, in London.** Real events again, working sessions, prepared and followed up.
- **Online sessions.** Shorter and more condensed, with more people bringing their work, and some of what I have been working on.
- **Hosted open source projects.** An independent home for projects that want one, as we described for [Agent Behaviour Policies](/articles/agent-behaviour-policies-move-to-the-open-security-summit.html), the first of them.

And I still think we should go back and capture what was said at the in-person summits too. If we organised one now, with the capability we have to capture the information and follow up, I think it would be remarkable. We just need somebody to fund it.

## The lesson {#lesson}

The Open Security Summit is my clearest example of what technical debt does when there is no development team to pay it down. Nothing broke all at once. Each summit added a little, each exception made sense at the time, and the cost arrived as friction: changes that took longer, people who stopped contributing, follow-up that never happened. The potential was there the whole time. The debt, and the cost of the follow-up, stopped it being reached.

## What this does not claim {#limits}

- **The counts are from the public repositories.** Read on 21 October 2026, all branches.
- **People committing are counted by email address.** One person with two addresses counts twice.
- **Partials "never called by name" may be called another way.** The count is a sign, not proof.
- **Hosting projects is a proposal.** As described in the Agent Behaviour Policies article.
- **The plans are plans.** The London events and online sessions are being organised; they need funding.

## Where this comes from {#sources}

A voice memo of 21 October 2026. The git history and files of [oss2018](https://github.com/OpenSecuritySummit/oss2018), [oss2019](https://github.com/OpenSecuritySummit/oss2019), [oss2020](https://github.com/OpenSecuritySummit/oss2020) and [oss-website](https://github.com/OpenSecuritySummit/oss-website), and the [OpenSecuritySummit organisation](https://github.com/OpenSecuritySummit) on GitHub; the live site, [open-security-summit.org](https://open-security-summit.org/), read the same day. [History and analysis of the OWASP in-person summits](https://diniscruz.ai/2025/06/07/history-and-analysis-of-owasp-in-person-summits.html), on diniscruz.ai. Related: [Agent Behaviour Policies move to the Open Security Summit](/articles/agent-behaviour-policies-move-to-the-open-security-summit.html), [the jobs that never scaled](/articles/jobs-that-never-scaled.html), [the code you do not ship](/articles/the-code-you-do-not-ship.html), [explorer coding](/articles/explorer-coding.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
