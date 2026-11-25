---
title: Almost a hundred repositories in under six days: how a pipeline built as infrastructure as code made creating a website a commit, and what happened to our GitHub organisation once a website cost one request file and Dinis's yes
date: 2026-11-25
author: Dinis Cruz
author_url: about/index.html
summary: On 19 November at 15:27 UTC I created one repository, SovereignWebsite__IaC. Fourteen minutes later its pipeline had created three more by itself, and by 11:00 UTC on 25 November it had made 97, in a GitHub organisation that now shows 99. Each one is a website with its own address, its own history and its own release tags, created because someone committed a small request file and I said yes. The innovation is simple, in quotes: a GitHub App and an AWS role that a pipeline can use, every action they take listed in an agent behaviour policy and checked before it runs, and nothing else allowed. That turned the repetitive part of my week, making a repository and wiring it to DNS, into a commit that takes seconds. What followed was an explosion of sites: agents, tools, platforms, startups, people and organisations, 31 of them on one day, and it has not slowed down. This is how the pipeline works, what it may never do, how fast it is, what broke when it went too fast, and why I think this is the most important thing we built this month.
version: v0.14.214
license: https://creativecommons.org/licenses/by/4.0/
tags: site-factory, infrastructure-as-code, ci, abp, sovereign-website, github, article
status: published
---

!shot nrd-repos.webp | images/ | The SovereignWebsite organisation on GitHub on 25 November: 99 repositories, 97 of them made by its pipeline. | screenshot

## In short {#in-short}

- **One repository made by hand,** SovereignWebsite__IaC, on 19 November at 15:27 UTC.
- **97 repositories made by its pipeline** in the five and a half days after, each a website.
- **A website is a request file** with my yes; the pipeline makes the repository, Pages, the address and the first release.
- **Every action is listed and checked** against an agent behaviour policy; anything not listed is refused.
- **The fastest took 23 seconds** from request to repository; the bottleneck was GitHub's rate limit, not people.

## The unlock {#unlock}

Making a website used to start with me. On 17 November I wrote it down in a request to the AgentiCCells site factory: "I need to create a new repo and link it to DNS, which I do all the time and is quite time consuming and repetitive … can you do this?", and then, "it will really make a massive difference". The AgentiCCells factory had already shown the idea worked: on 16 November three site repositories were made by hand and then one by a commit, merged to live in under three minutes ([the site factory works](/articles/the-site-factory-works.html)).

On 19 November we started again, properly, as infrastructure as code. At about 15:10 UTC I told the conductor: "let's take the opportunity to add as much automation (via CI pipelines) as possible, and then use our ABP to control it", and "let's try to do this completely from the CI pipeline and if we need to add more privs to the GH App and the AWS Role, we'll add them". At 15:27 I created SovereignWebsite__IaC. At 15:36 a commit named "The three apex sites" asked for sovereignwebsite.ai, .org and .site. At 15:40:52 the first repository appeared whose first commit was not mine but the factory's App's, and the run's record says it all: "created SovereignWebsite__Website, __Org and __Site … 19 actions, all allowed by the policy".

## How a request becomes a website {#how}

!shot nrd-pipeline.webp | images/ | One request, one website: a request file with my yes, a checked plan, then Org apply and DNS apply. | figure

A site starts as a folder in the factory's repository, `requests/<date>__<label>/site.json`, with a label, a group, a title, a description, a kind and who can see it. Its name follows a rule: the repository is `Site__<Group>__<Name>` and the address is `<label>.<group>.sovereignweb.site`. The README is plain about who decides: "A request is committed to dev only with Dinis's yes for that site." My yes is quoted in the commit message, and the policy file lists `requests/**` among the paths that need my merge.

When the request lands on dev, two workflows run.

- **Org apply** mints a short-lived token from the factory's GitHub App, plans the change, checks every planned action against the policy, and then applies it: it creates the repository, makes `dev` the default branch, turns on Pages, seeds the site from a template in one commit, sets the custom domain, gives the agents' team push, adds two rulesets (main is locked; dev cannot be deleted or force-pushed) and turns on HTTPS once GitHub has the certificate. It never touches secrets.
- **DNS apply** assumes an AWS role over OIDC, so there is no stored AWS key, and writes one record in Route 53. The role can only upsert A, AAAA, CNAME and TXT records, in four zones.

Each new site arrives with its own pipeline: a signer check, a version from its tags, link, em dash and leak checks, HTML and accessibility checks, a deploy and a release tag. There are templates for a public site, a private vault site behind a gate, an agent's site and a redirect.

## What it may never do {#never}

The power is in what the pipeline is allowed to do, and that is written down. The policy, `policy/abp.json`, starts from "Anything not listed is refused." For Org apply it lists what is refused always: deleting, transferring, archiving or making private a repository, changing members or the App, granting admin or maintain, and deleting or weakening a ruleset. Each agent has the paths it may change and three things it may never do: push to main, print or commit a key or token, or name a private prospect. Changes to the policy, the workflows, the build, the organisation, the seeds and the requests need my merge.

The same kind of rule shows up in places I did not plan. The newsroom's own policy refuses merge commits into its release branch, so when one writer agent's registration closed with articles still unpublished, the next writer could not simply merge that branch: it had to copy the files and commit them again under its own key, so every published line points to the agent that is answerable for it. A policy that says no to a convenient shortcut is the policy working.

That is why I can say yes to a site in a sentence. I am not approving a person's access to my organisation; I am approving one request that a pipeline will carry out within a list of actions I have already read.

## How fast {#speed}

The fastest request so far went from commit to repository in 23 seconds: a London site on 24 November, committed at 19:56:39 and created at 19:57:02. A guide to domain registrars took 26 seconds, with its seed commit and its v0.1.0 tag 38 seconds after the request. Most single requests take between 25 seconds and two minutes. A batch takes longer because the pipeline creates one repository at a time: one commit on 22 November asked for 14 sites and got them in four to eight minutes.

## The explosion {#explosion}

!shot nrd-explosion.webp | images/ | 97 repositories in under six days: 31 on 20 November, 25 on 22 November, 19 on 24 November. | chart

Once a website cost a request file, we made a lot of them. Five on the first afternoon, 31 the next day, 25 on 22 November, 19 on 24 November, and 8 more by 03:01 UTC on 25 November, among them Apple, NVIDIA and Puter as platforms, a Google Calendar tool and a site for my book: 97 in all, and GitHub shows 99 in the organisation at 11:00 UTC, counting the factory itself and one site moved in from AgentiCCells. The first customer-style request came on 20 November at 09:14, a Google Maps tool and a pipeline demo, with my "Yes to pipeline-demo.sovereignwebsite.site" in the commit. The factory's own repository has 602 commits.

The mix tells the story of the week: 32 agents' sites (more on those in [who runs the agents](/articles/who-runs-the-agents.html)), 12 tools, 12 platforms, 5 startup brochures, 5 redirects, 3 organisations, and sites for people, companies, investors, a designer, authors, a founder and, since this morning, a padel player. Many are on the hub ([the showroom](/articles/the-showroom.html)); the hub's list, the requests folder and the organisation do not yet agree on a single count, which is a job in itself.

## What broke when it went too fast {#broke}

Two things, both written up by the agents themselves.

- **The rate limit.** Org apply used to read every repository on every push and every hour, about six API calls each plus one per seed file. With 70 repositories that ran out the App's hourly limit at 01:15 UTC on 24 November, and the workflow was disabled at 02:03. My ask was "keep it focused on the actions that I'm working on and reviewing": a push now acts only on the repositories it names, and the full sweep runs every sixth hour. Three requests waited ten to twelve hours that day.
- **A key nobody had registered.** On 22 November a site's agent that could not reach the factory pushed two commits signed by a key it had not published, and a release went live. The incident note says it plainly: "Nothing refused it. Only Dinis noticed." The fix was a signer check in every site's pipeline, which I said yes to the same afternoon. It is on the agents' sites; the customer sites get it with the next full sweep.

## Why it matters {#why}

This is the Wardley map moment again, at a larger scale. A repository with a domain, Pages, rules and a release process used to be a small project; it is now a commodity that costs seconds. On 22 November, giving the factory one more permission, I said it in one line: "For tasks like this I should not be the bottleneck." That is the whole point. Every agent can have a site, every tool can be its own website ([every tool its own website](/articles/every-tool-its-own-website.html)), every person we meet can see their site the same day ([the first round trip](/articles/the-first-round-trip.html)), and each one is a public repository with a full history that the owner can take anywhere.

And the same pattern now points at other things that are repetitive and governed: servers for sgit vaults ([the SGit server factory](/articles/the-sgit-server-factory.html)) are next. The pipeline does the work; the policy says what work is allowed; I say yes.

## What this does not claim {#limits}

- **Repository creation times come from each repository's first commit,** not from GitHub's API, which this survey could not use.
- **Request-to-repository is not request-to-live:** Pages and the certificate add time we did not measure here; a few sites still had no certificate on 25 November.
- **Counts differ by source and keep moving:** at 11:00 UTC on 25 November, 97 made by the pipeline, 99 in the organisation and 90 request folders (some requests make several sites); the hub lists fewer.

## Where this comes from {#sources}

The public repositories of the [SovereignWebsite](https://github.com/SovereignWebsite) organisation, read on 24 and 25 November 2026: [SovereignWebsite__IaC](https://github.com/SovereignWebsite/SovereignWebsite__IaC) (its README, `requests/README.md`, `.github/workflows/`, `build/org-apply.mjs`, `policy/abp.json`, REALITY.md, `board/incidents/2026-11-22__pushed-before-key-published.md`, commits 397f661, d6d7ccb, febc366 and ba0d197) and the first commit of each site repository. The AgentiCCells site factory's REALITY.md, `docs/github-app.md` and `requests/2026-11-17__data-promptugal-news/brief.md`. Related: [the site factory works](/articles/the-site-factory-works.html), [the showroom](/articles/the-showroom.html), [who runs the agents](/articles/who-runs-the-agents.html), [a repository per agent](/articles/a-repository-per-agent.html), [the SGit server factory](/articles/the-sgit-server-factory.html).
