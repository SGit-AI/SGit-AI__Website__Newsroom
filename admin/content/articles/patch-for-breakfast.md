---
title: Patch for breakfast: nobody refuses to patch because they want to, a patch is surgery without tests and a pipeline, and why the PHP crisis is the moment to invest in being able to change
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: php2shell has done something rare: it has the board's attention, and executives are asking good questions. There is some hype, but the impact is real. Nobody takes a website down lightly, and organisations took real sites down this week because they could not answer one question: are we safe? And you cannot be safe if you cannot deploy a patch. In my experience nobody fails to patch because they do not want to. The teams with the best pipelines patch for breakfast and run out of things to patch, because a patch is a change to a system, and they have the tests and the automation that make a change routine. Without them, patching is surgery: manual testing, people who could deploy long gone, side effects nobody knows. So it gets postponed, and a system that has not been updated in years is a signal of technical debt and of risk that we can measure. The PHP fix itself touched 389 files. The answer is not to patch, bring the site back and move on, because the next flaw will find it in the same state. It is to invest in the pipeline, the tests and paid maintenance, and the money being spent bringing sites back this week says the economics already add up.
version: v0.13.67
license: https://creativecommons.org/licenses/by/4.0/
tags: patching, ci-cd, maintenance, php2shell, non-functional-requirements, article
status: published
---

!shot bx-surgery.webp | images/ | A patch is a change to a system: surgery without tests and a pipeline, routine with them. | concept

## In short {#in-short}

- **Never waste a good crisis.** php2shell has the board asking real questions.
- **Sites went dark because nobody could say "we are safe".** You cannot be safe if you cannot deploy a patch.
- **Nobody refuses to patch because they want to.** The best pipelines patch for breakfast.
- **Without tests and automation, a patch is surgery.** So it is postponed, and the debt grows.
- **We can measure it.** When was each system last updated, and how long would a change take?
- **Do not do it as a one-off.** Invest in the pipeline, the tests and paid maintenance.

## Never waste a good crisis {#the-crisis}

php2shell has one advantage over most vulnerabilities: it has board attention. Executives are asking good questions. There is definitely some hype, but the questions are real, and so is the impact. Nobody takes a website down lightly. These were real websites with real users: [the PHP story's source watch](https://php.oct.2026.newsroom.sgit.ai/compromise/) tracks 295 sites that somebody named as taken offline.

Why did they take them down? Because they could not answer a good question: are we safe? And if you cannot deploy a patch, you cannot be safe. So the real question is the next one: why can't they patch?

## Nobody refuses to patch {#nobody-refuses}

What I have learned over many years is that nobody fails to patch because they do not want to. In fact the best teams patch for breakfast. They run out of things to patch. Not because they are the best engineers, but because they have the best pipelines: they have the tests, they know the side effects, and they have automation that turns a change into a routine.

That is the point people miss: a patch is a change to a system. If you have good tests and a healthy pipeline, a change is small and safe. If you do not, patching is like surgery. You go to the operating table. The testing has to be done by hand. The people who could deploy are not there any more. The people who are there may be very capable, but they do not understand the system, they do not know the side effects, and they do not have good documentation. No wonder organisations do not want to patch.

The PHP fix shows why this is not about the size of the patch. As [the PHP story's journalist](https://php.oct.2026.newsroom.sgit.ai/articles/why-not-patch-every-version/index.html) found, it touched 389 files, 113 of them outside the tests, changing how the whole engine handles memory errors, and it adds new limits with defaults. Most of the fixes that reached servers did so through someone else's pipeline: a distribution's update, a hosting panel, an extended-support vendor. And for many platforms the fix was "fixed, if you rebuild": nothing already running changes until its owner rebuilds and redeploys it. If your organisation cannot rebuild and redeploy, the fix existing does not help you. As I said in my brief to that team, "if you have a website that's been going for years, updating it is very risky".

## A system you cannot update is a signal {#a-signal}

If you do not patch regularly, that is a massive signal. It is a signal of technical debt, and a signal of risk. When something like php2shell happens, you have to patch anyway, under pressure, on the operating table.

And we can measure it, even now, in the middle of the incident. When was this system last updated? How long would a change take, from commit to production? Can we still build it? Who knows its side effects? Two of those are close to what [DORA's research](https://dora.dev/guides/dora-metrics/) measures: deployment frequency, and change lead time, "the amount of time it takes for a change to go from committed to version control to deployed in production". DORA has also found, repeatedly, that speed and stability are not trade-offs: "top performers do well across all five metrics". These are not new ideas. What is new is the moment: this week, every organisation that switched a site off has a list of the systems it could not answer for.

I would go further. Show me a system that has not been updated and cannot be touched, and I will show you a system that is probably not serving its users as well as it could, and is not as effective as it could be. There is a direct connection. The ability to patch and the ability to improve are the same ability.

## The root causes {#root-causes}

A lot of security tools and security actions do not touch the root causes. A scanner can tell you that you are vulnerable; it cannot give you a team that can change the system. What you need is a team, funding, automation, and investment in the non-functional requirements and the whole life cycle of an application: the version control, the tests, the pipeline, the documentation, the ability to rebuild from scratch. I have argued for years that this is [a business in its own right](https://open-source.sgit.ai/views/villagers.html), and that whole companies should be built around providing it.

It is also more urgent than it was. We are not yet seeing large amounts of AI-driven exploitation, but the tools are arriving: the [AI insurance paper I reviewed this week](https://newsroom.sgit.ai/articles/underwriting-the-agent-economy-reviewed.html) points to a frontier model that can find and exploit previously unknown vulnerabilities on its own. The time between a flaw being found and being used will keep shrinking, and so will the time an organisation can afford to spend on the operating table.

## Do not do it as a one-off {#not-one-off}

So here is the opportunity. Do not answer this crisis by patching PHP, bringing the site back, saying "all good" and moving on. That is the whack-a-mole we have been playing for decades, and the next flaw, next week or next month, will find the same system in the same state.

!shot bx-three-ways.webp | images/ | Three ways to answer the crisis: the one-off, the measured and the investment. | concept

Instead, invest. Fix the second and third stories, not only the first: the pipeline, the tests, the people who can change the system. And pay for it properly. Somebody should be supporting that work and providing it as a cost-effective service, and the money is there: look at what organisations are spending this week to bring their sites back online, and imagine paying a fraction of that, every month, to keep them maintainable. I would argue the economics add up.

That is also what the signed, supported version in [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html) is for. When you pay the people who maintain the code to sign off the version you run, and to help you set it up and keep it current, what you are buying is exactly this: the ability to change safely, whenever you need to.

Think of a shop or a factory where key pieces of the infrastructure are things nobody knows how they work, nobody knows how to change, and nobody can update, but they are mission critical. We have got away with that in technology for a long time. It is time to move on, and this is a great moment to move the dial.

## What this does not claim {#limits}

- **No cost estimate exists for the shutdowns.** "The money is there" is an argument from what organisations are visibly spending, not a measured figure.
- **Some teams cannot patch for other reasons.** Vendor contracts, certified configurations and regulated changes are real constraints.
- **A pipeline does not remove judgement.** It makes a change cheap to test; someone still decides.
- **AI-driven exploitation is a trend, not yet a measurement** of this incident.

## Where this comes from {#sources}

My voice memo of 24 October 2026; the PHP story site's [why can't every version of PHP just be patched?](https://php.oct.2026.newsroom.sgit.ai/articles/why-not-patch-every-version/index.html) and [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/); DORA's [guide to its metrics](https://dora.dev/guides/dora-metrics/); the [AI insurance stack paper](https://arxiv.org/abs/2607.11999v2). Related: [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html), [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html), [who will fix your mess?](https://newsroom.sgit.ai/articles/who-will-fix-your-mess.html), [underwriting the agent economy, reviewed](https://newsroom.sgit.ai/articles/underwriting-the-agent-economy-reviewed.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
