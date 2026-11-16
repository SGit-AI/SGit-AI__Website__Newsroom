---
title: The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: Last night I made three websites on agenticcells.site by hand, and then one was made automatically, and that was freaking awesome. A request, a site file and a brief, committed to the AgentiCCells site factory and merged, made a CI pipeline create the GitHub repository, seed it from a template, set up Pages, write the DNS record in Route 53, wait for public DNS, set the custom domain, deploy, get the certificate and turn on HTTPS, and then run Claude Code to write the first version of the site. The RiskMandate at Web Summit site went from merge to live over https in 87 seconds, and had its first version 72 seconds later. That is a textbook Wardley map moment: a website has a ridiculous number of moving parts, each of them already a product or a utility, and what was still custom was putting them together. Now it is a commit. Getting there was not for the faint of heart: a GitHub App, an AWS role through OpenID Connect, Claude through workload identity federation, environments, trust policies, and a list of things that broke on the way. Claude did the heavy lifting, but it still felt like surgery, and it shows how immature this technology still is. And the pipeline ended up with far more power than its job needs, which is the subject of a companion article.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, site-factory, ci, github, aws, wardley-maps, websites, article
status: published
---

!shot acf-sites.webp | images/ | Six sites on agenticcells.site on 16 November 2026: three made by the factory, two by hand, and the home page. | collage

## In short {#in-short}

- **Three sites by hand, then one by a commit.** The factory made the RiskMandate at Web Summit site live over https 87 seconds after the merge.
- **Every moving part, automated:** repository, template, Pages, DNS, custom domain, certificate, HTTPS, and a first version by Claude Code.
- **A Wardley map moment:** every part was already a commodity; putting them together was the custom bit, and now it is a commit.
- **It was hard to set up:** a GitHub App, AWS through OpenID Connect, Claude through identity federation, and six things that broke.
- **No long-lived keys anywhere,** but a pipeline with far more power than it needs: that is the next article.

## Three by hand, then one by a commit {#story}

[AgentiCCells](/articles/starting-agenticcells.html) sells agentic teams, and its first offering is a website, as a cell ([atomic cells, end to end](/articles/atomic-cells-end-to-end.html)). For that to work without me in the loop, making a site has to be a step anyone, or any agent, can run. On 15 November I wrote down the idea: a request is a folder, a site file and a brief, committed to a control repository, and the pipeline writes the result back; plan on the pull request, apply on merge ([from a commit to a live website](/articles/from-a-commit-to-a-live-website.html)).

That evening the factory agent started building it, in stages, in the open: the request format and a validator, a plan job with no secrets, a dry run, a template repository. Then, just after midnight, I made three sites by hand: I created each repository with an initial commit between 00:45 and 00:47, and the sites agent pushed the site, its scripts, its CI and an encrypted vault. One of them is for my brother Gabriel ([a website for my brother](/articles/a-website-for-my-brother.html)); another is an example site for an orange grower in the hills above Silves. By 01:30 all three were live on their own subdomains of agenticcells.site. They were the worked example the factory had to automate.

Then came the credentials, which I will come back to, and the first real runs. QA-1, merged at 02:35, created and deployed a site, but GitHub checked the custom domain seconds before the DNS record was visible, so no certificate was issued. The fix was to wait for public DNS before setting the domain. QA-2, merged at 03:07:59, went from merge to live with a first version by Claude Code in under three minutes.

## Two minutes and thirty-nine seconds {#flow}

!shot acf-flow.webp | images/ | The RiskMandate at Web Summit request: live over https 87 seconds after the merge, first version at 159 seconds. | timeline

At 03:44:06 I merged the request for the RiskMandate at Web Summit site. The pipeline validated it, created the repository, seeded it from the template, set the default branch and Pages, wrote the CNAME in Route 53 and waited until public DNS could see it, set the custom domain, started the deploy, and at 03:45:33 the certificate was issued and Enforce HTTPS was on: 87 seconds. Then Claude Code, running in its own job with file tools only, wrote the first version, and at 03:46:45 it was pushed to the site's dev branch. Every step wrote its result back into the request's `status.json`.

That site has since grown into the page for our film at Web Summit ([know the reach](/articles/know-the-reach.html)), by the same agents that keep the other sites. The factory's job was to make a place for it to exist, in less time than it takes to make a coffee.

## A Wardley map moment {#wardley}

!shot acf-wardley.webp | images/ | A Wardley map of a small website: every part is a product or a utility; the assembly was custom, and now it is a commit. | concept

A website has a ridiculous number of moving parts: a repository, CI, hosting, a DNS record, a certificate, a domain check, a first version, and a team that keeps it. None of them is new. GitHub, Pages, Route 53, certificates and even the model are products or utilities. What was still custom was putting them together, every time, by hand, with a person who knew where each setting lives.

That is exactly the movement Simon Wardley's maps describe: an activity moves from custom built to product to commodity, and when it does, everything above it can be built faster. Making a site is now a commit. Which means the interesting work moves up: the brief, the content, and the agentic team that keeps the site alive.

## What it took to make it easy {#setup}

!shot acf-setup.webp | images/ | Everything I did by hand before a commit could make a site: GitHub, the App, AWS, Anthropic, and what broke. | infographic

Here is the uncomfortable part. Making this easy was hard. The factory agent wrote a step-by-step guide and three check workflows that told me what was missing after each step, and Claude did the heavy lifting throughout. But every click in that guide was mine, and there were a lot of them.

- **GitHub:** two environments, one limited to dev with me as a reviewer, one holding no secrets; a GitHub App with six permissions, a private key pasted as a secret and then deleted, installed on the whole organisation.
- **AWS:** the domain moved to Route 53, an OpenID Connect identity provider, a role whose trust policy names one environment of one repository, and a permission policy for one zone, CNAME records only, subdomains only.
- **Anthropic:** workload identity federation, so the pipeline exchanges GitHub's token for a short-lived one and holds no API key: a rule, a service account, three IDs.

And six things broke on the way: a `.gitignore` that dropped the build scripts, an OpenID Connect subject format carrying numeric IDs, GitHub's domain check racing the DNS record, a piped check that printed OK after a failure, a retry that lost a status file, and Pages refusing to deploy from dev until an environment rule changed.

The result is good security: there is no long-lived key anywhere, and every credential is short-lived and bound to one environment of one repository. But it felt like surgery. It should have been far easier to give a pipeline exactly the power to create one repository and one DNS record, and nothing else. That it was not, even with an agent doing most of the work, shows how immature this part of the technology still is.

## What this unlocks {#unlocks}

This was one of the last manual, painful pieces of the puzzle. Repositories, DNS and AWS configuration can now be made programmatically, from a commit that a person or an agent writes. From here it is variations of the same thing: a site per customer, a site per project, a site per town for [PrompTugal.news](/articles/every-story-has-an-address.html), each one a request folder. That is what makes the £500 cell something we can sell and deliver at scale.

## What this does not claim {#limits}

- **Four sites have been made by the factory so far,** two of them tests (QA-1 and QA-2); QA-1's domain had to be re-checked by hand.
- **The times are from the pipeline's own status files,** written back by the workflow.
- **The factory makes public sites only,** on agenticcells.site; the vault step is not automated yet.
- **The pipeline holds more permission than it needs;** that is the companion article, [CI behaviour policies](/articles/ci-behaviour-policies.html).

## Where this comes from {#sources}

The AgentiCCells repositories, read on 16 November 2026: AgentiCCells__Site__Factory (README, REALITY.md, `docs/SETUP.md`, `docs/github-app.md`, `docs/aws-oidc.md`, `requests/*/status.json`, commits), AgentiCCells__Site__Template, the site repositories, and `map/site-creation.md` in AgentiCCells__Website. The live sites, screenshotted on 16 November 2026. Earlier on this site: [from a commit to a live website](/articles/from-a-commit-to-a-live-website.html), [starting AgentiCCells](/articles/starting-agenticcells.html), [atomic cells, end to end](/articles/atomic-cells-end-to-end.html), [a website for my brother](/articles/a-website-for-my-brother.html), [know the reach](/articles/know-the-reach.html).
