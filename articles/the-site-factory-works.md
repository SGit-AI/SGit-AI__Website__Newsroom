# The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy, sgit.ai

> Last night I made three websites on agenticcells.site by hand, and then one was made automatically, and that was freaking awesome. A request, a site file and a brief, committed to the AgentiCCells site factory and merged, made a CI pipeline create the GitHub repository, seed it from a template, set up Pages, write the DNS record in Route 53, wait for public DNS, set the custom domain, deploy, get the certificate and turn on HTTPS, and then run Claude Code to write the first version of the site. The RiskMandate at Web Summit site went from merge to live over https in 87 seconds, and had its first version 72 seconds later. That is a textbook Wardley map moment: a website has a ridiculous number of moving parts, each of them already a product or a utility, and what was still custom was putting them together. Now it is a commit. Getting there was not for the faint of heart: a GitHub App, an AWS role through OpenID Connect, Claude through workload identity federation, environments, trust policies, and a list of things that broke on the way. Claude did the heavy lifting, but it still felt like surgery, and it shows how immature this technology still is. And the pipeline ended up with far more power than its job needs, which is the subject of a companion article.

*Source: <https://newsroom.sgit.ai/articles/the-site-factory-works.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy

# The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/the-site-factory-works.md) · [newsroom v0.14.116](https://newsroom.sgit.ai/admin/versions.html) · agenticcellssite-factorycigithubawswardley-mapswebsitesarticle

***Abstract:** Last night I made three websites on agenticcells.site by hand, and then one was made automatically, and that was freaking awesome. A request, a site file and a brief, committed to the AgentiCCells site factory and merged, made a CI pipeline create the GitHub repository, seed it from a template, set up Pages, write the DNS record in Route 53, wait for public DNS, set the custom domain, deploy, get the certificate and turn on HTTPS, and then run Claude Code to write the first version of the site. The RiskMandate at Web Summit site went from merge to live over https in 87 seconds, and had its first version 72 seconds later. That is a textbook Wardley map moment: a website has a ridiculous number of moving parts, each of them already a product or a utility, and what was still custom was putting them together. Now it is a commit. Getting there was not for the faint of heart: a GitHub App, an AWS role through OpenID Connect, Claude through workload identity federation, environments, trust policies, and a list of things that broke on the way. Claude did the heavy lifting, but it still felt like surgery, and it shows how immature this technology still is. And the pipeline ended up with far more power than its job needs, which is the subject of a companion article.*

Six sites on agenticcells.site on 16 November 2026: three made by the factory, two by hand, and the home page.

## In short

- **Three sites by hand, then one by a commit.** The factory made the RiskMandate at Web Summit site live over https 87 seconds after the merge.
- **Every moving part, automated:** repository, template, Pages, DNS, custom domain, certificate, HTTPS, and a first version by Claude Code.
- **A Wardley map moment:** every part was already a commodity; putting them together was the custom bit, and now it is a commit.
- **It was hard to set up:** a GitHub App, AWS through OpenID Connect, Claude through identity federation, and six things that broke.
- **No long-lived keys anywhere,** but a pipeline with far more power than it needs: that is the next article.

## Three by hand, then one by a commit

[AgentiCCells](starting-agenticcells.md) sells agentic teams, and its first offering is a website, as a cell ([atomic cells, end to end](atomic-cells-end-to-end.md)). For that to work without me in the loop, making a site has to be a step anyone, or any agent, can run. On 15 November I wrote down the idea: a request is a folder, a site file and a brief, committed to a control repository, and the pipeline writes the result back; plan on the pull request, apply on merge ([from a commit to a live website](from-a-commit-to-a-live-website.md)).

That evening the factory agent started building it, in stages, in the open: the request format and a validator, a plan job with no secrets, a dry run, a template repository. Then, just after midnight, I made three sites by hand: I created each repository with an initial commit between 00:45 and 00:47, and the sites agent pushed the site, its scripts, its CI and an encrypted vault. One of them is for my brother Gabriel ([a website for my brother](a-website-for-my-brother.md)); another is an example site for an orange grower in the hills above Silves. By 01:30 all three were live on their own subdomains of agenticcells.site. They were the worked example the factory had to automate.

Then came the credentials, which I will come back to, and the first real runs. QA-1, merged at 02:35, created and deployed a site, but GitHub checked the custom domain seconds before the DNS record was visible, so no certificate was issued. The fix was to wait for public DNS before setting the domain. QA-2, merged at 03:07:59, went from merge to live with a first version by Claude Code in under three minutes.

## Two minutes and thirty-nine seconds

The RiskMandate at Web Summit request: live over https 87 seconds after the merge, first version at 159 seconds.

At 03:44:06 I merged the request for the RiskMandate at Web Summit site. The pipeline validated it, created the repository, seeded it from the template, set the default branch and Pages, wrote the CNAME in Route 53 and waited until public DNS could see it, set the custom domain, started the deploy, and at 03:45:33 the certificate was issued and Enforce HTTPS was on: 87 seconds. Then Claude Code, running in its own job with file tools only, wrote the first version, and at 03:46:45 it was pushed to the site's dev branch. Every step wrote its result back into the request's `status.json`.

That site has since grown into the page for our film at Web Summit ([know the reach](know-the-reach.md)), by the same agents that keep the other sites. The factory's job was to make a place for it to exist, in less time than it takes to make a coffee.

## A Wardley map moment

A Wardley map of a small website: every part is a product or a utility; the assembly was custom, and now it is a commit.

A website has a ridiculous number of moving parts: a repository, CI, hosting, a DNS record, a certificate, a domain check, a first version, and a team that keeps it. None of them is new. GitHub, Pages, Route 53, certificates and even the model are products or utilities. What was still custom was putting them together, every time, by hand, with a person who knew where each setting lives.

That is exactly the movement Simon Wardley's maps describe: an activity moves from custom built to product to commodity, and when it does, everything above it can be built faster. Making a site is now a commit. Which means the interesting work moves up: the brief, the content, and the agentic team that keeps the site alive.

## What it took to make it easy

Everything I did by hand before a commit could make a site: GitHub, the App, AWS, Anthropic, and what broke.

Here is the uncomfortable part. Making this easy was hard. The factory agent wrote a step-by-step guide and three check workflows that told me what was missing after each step, and Claude did the heavy lifting throughout. But every click in that guide was mine, and there were a lot of them.

- **GitHub:** two environments, one limited to dev with me as a reviewer, one holding no secrets; a GitHub App with six permissions, a private key pasted as a secret and then deleted, installed on the whole organisation.
- **AWS:** the domain moved to Route 53, an OpenID Connect identity provider, a role whose trust policy names one environment of one repository, and a permission policy for one zone, CNAME records only, subdomains only.
- **Anthropic:** workload identity federation, so the pipeline exchanges GitHub's token for a short-lived one and holds no API key: a rule, a service account, three IDs.

And six things broke on the way: a `.gitignore` that dropped the build scripts, an OpenID Connect subject format carrying numeric IDs, GitHub's domain check racing the DNS record, a piped check that printed OK after a failure, a retry that lost a status file, and Pages refusing to deploy from dev until an environment rule changed.

The result is good security: there is no long-lived key anywhere, and every credential is short-lived and bound to one environment of one repository. But it felt like surgery. It should have been far easier to give a pipeline exactly the power to create one repository and one DNS record, and nothing else. That it was not, even with an agent doing most of the work, shows how immature this part of the technology still is.

## What this unlocks

This was one of the last manual, painful pieces of the puzzle. Repositories, DNS and AWS configuration can now be made programmatically, from a commit that a person or an agent writes. From here it is variations of the same thing: a site per customer, a site per project, a site per town for [PrompTugal.news](every-story-has-an-address.md), each one a request folder. That is what makes the £500 cell something we can sell and deliver at scale.

## What this does not claim

- **Four sites have been made by the factory so far,** two of them tests (QA-1 and QA-2); QA-1's domain had to be re-checked by hand.
- **The times are from the pipeline's own status files,** written back by the workflow.
- **The factory makes public sites only,** on agenticcells.site; the vault step is not automated yet.
- **The pipeline holds more permission than it needs;** that is the companion article, [CI behaviour policies](ci-behaviour-policies.md).

## Where this comes from

The AgentiCCells repositories, read on 16 November 2026: AgentiCCells__Site__Factory (README, REALITY.md, `docs/SETUP.md`, `docs/github-app.md`, `docs/aws-oidc.md`, `requests/*/status.json`, commits), AgentiCCells__Site__Template, the site repositories, and `map/site-creation.md` in AgentiCCells__Website. The live sites, screenshotted on 16 November 2026. Earlier on this site: [from a commit to a live website](from-a-commit-to-a-live-website.md), [starting AgentiCCells](starting-agenticcells.md), [atomic cells, end to end](atomic-cells-end-to-end.md), [a website for my brother](a-website-for-my-brother.md), [know the reach](know-the-reach.md).

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#the-site-factory-works)

### Builds on

- [Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day](starting-agenticcells.md) AgentiCCells: a new company that sets up small agentic teams in the customer's environment, with a control centre, all open, no state on our side.
- [Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder](atomic-cells-end-to-end.md) AgentiCCells' first offering: a £500 website as an atomic cell, steered by the customer from their browser with a key, handed over to their GitHub.
- [From a commit to a live website: a site factory where a request file in a commit makes a CI pipeline create the GitHub repository, the DNS record and the sgit vault, seed a page, check HTTPS, run a first pass with Claude Code, and record it all, so an agent can create sites by committing](from-a-commit-to-a-live-website.md) A site factory: a request in a commit makes a CI pipeline create the repository, DNS record and vault, seed a page, check HTTPS and record it all.
- [A website for my brother: a brief for Gabriel DaCruz's Claude, to rebuild gabrieldacruz.com on GitHub Pages and Google Workspace, interview him every day, and tell the story of a musician who will not tell it himself](a-website-for-my-brother.md) A brief for Gabriel DaCruz's Claude: his site on GitHub Pages, Google Workspace, daily interviews and a newsroom.
- [Know the Reach: RiskMandate has a song on Spotify, and its music video is being made with AI, shot by shot, from about 2,300 words of human direction; this is how the first part was made](know-the-reach.md) RiskMandate's song Know the Reach is on Spotify; the first 53 seconds of its video were made with AI from about 2,300 words of direction.
- [Every story has an address: a design proposal for PrompTugal.news as a ground-up newsroom, where news is filed where it happens and climbs to the region and the country with its proof, mocked up from the live data of 19 local editions](every-story-has-an-address.md) A design proposal for PrompTugal.news as a ground-up newsroom: every story filed at an address, climbing with its proof. Mockups from live data.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.

### Continued by

- [Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories](five-primitives-one-store.md) A reply to Andy Goundry: Anthropic's five always-on primitives can share one versioned, signed store, and every AgentiCCells cell ships with all five.
- [A portfolio with a film first: Silvio Switha's site, made in under an hour by the site factory and five design agents, with his music video in the first screen, his agents as a solar system and a mixing desk, a producer's studio, a proposal for clients and a gig poster, and every claim something he built](a-portfolio-with-a-film-first.md) Silvio Switha's portfolio site, made in under an hour by the factory and five design agents: his film first, his agents as a solar system and a mixing desk.
- [A website that is her: how Yiheng Wang's site was made in three passes in one evening, by the site factory, five design agents and then her own agent, with five designs, a kitchen brigade of 26 agents, a printable brief and a page for your AI, and why every claim on it is something she can talk about because she did it](a-website-that-is-her.md) Yiheng Wang's website, made in one evening by the site factory, five design agents and her own agent: five designs, every claim sourced, all of it her.
- [Show me the evidence: websites for people looking for a job, built by an agentic cell, with seven pages that prove instead of list, a page made for each employer, a pack for recruiters, eight personas to fork, a ladder from a free recipe to a recruiter's cell, and the brief for the team that builds it](show-me-the-evidence.md) Websites for people looking for a job that show evidence instead of lists: seven pages, a page per employer, a recruiter pack, eight personas to fork.
- [Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team](fork-it.md) Forking as the way people adopt our cells: fork a template, point Claude at it, and it is yours. Five ways, fork-ready repositories, and a hub.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place](integrate-with-whatever-is-on-the-other-side.md) We never start by asking a customer to move. We integrate with what they run, build around it, and either retire our code or become the better place.
- [Odoo's agents can now write to the system of record: how our stack fits around Odoo, from version 12 to 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, an ephemeral proof of concept that went from nothing to customised in under a minute on four versions, and why we use whatever version is on the other side](odoo-and-our-stack.md) Odoo's agents can write to the system of record. Our stack fits every Odoo from 12 to 20: a proof of concept ran on four versions in under a minute each.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 426 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=426)

**Posting this article on LinkedIn?** The cover is [the-site-factory-works.jpg](banners/the-site-factory-works.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-site-factory-works.html)*
