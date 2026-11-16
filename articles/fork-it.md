# Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team, sgit.ai

> Forking is one of the ideas that made GitHub so powerful, and I think it is the way people should adopt what we make. If I create a template site, a cell, and someone wants it, they should be able to fork it, point Claude at their copy, and have their own version, live, within minutes. That already works on GitHub today; our job is to make it as smooth as possible, for a stranger who has never met our tools. So every template on the AgentiCCells hub should offer five ways to make it yours: fork it on GitHub and let Pages host it; deploy it in one click to Netlify, Vercel or Cloudflare Pages; run it inside an assistant, locally with Claude Code or hosted as a page by the assistant itself; take it as a vault, with no account at all; or ask us, and the site factory makes it, on the paid ladder. And not only single repositories but paths: start with this repository, then fork that one, then add this cell. For that, our repositories must be fork-ready, not factory-ready: a README with the one prompt that makes it yours, a CLAUDE.md for any agent, one settings file, sample content clearly marked, its behaviour policy included, and upstream updates proposed to every fork. Then the business is simple: make dozens, hundreds of small templates, put them on the hub, and let forks and requests tell us which ones to invest in. Probably in a GitHub organisation of their own. Here is the pattern, and the brief for the team.

*Source: <https://newsroom.sgit.ai/articles/fork-it.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team

# Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/fork-it.md) · [newsroom v0.14.125](https://newsroom.sgit.ai/admin/versions.html) · agenticcellsforkingtemplatesgithubhubgo-to-marketopen-sourcearticle

***Abstract:** Forking is one of the ideas that made GitHub so powerful, and I think it is the way people should adopt what we make. If I create a template site, a cell, and someone wants it, they should be able to fork it, point Claude at their copy, and have their own version, live, within minutes. That already works on GitHub today; our job is to make it as smooth as possible, for a stranger who has never met our tools. So every template on the AgentiCCells hub should offer five ways to make it yours: fork it on GitHub and let Pages host it; deploy it in one click to Netlify, Vercel or Cloudflare Pages; run it inside an assistant, locally with Claude Code or hosted as a page by the assistant itself; take it as a vault, with no account at all; or ask us, and the site factory makes it, on the paid ladder. And not only single repositories but paths: start with this repository, then fork that one, then add this cell. For that, our repositories must be fork-ready, not factory-ready: a README with the one prompt that makes it yours, a CLAUDE.md for any agent, one settings file, sample content clearly marked, its behaviour policy included, and upstream updates proposed to every fork. Then the business is simple: make dozens, hundreds of small templates, put them on the hub, and let forks and requests tell us which ones to invest in. Probably in a GitHub organisation of their own. Here is the pattern, and the brief for the team.*

Five ways to make a cell yours: fork on GitHub, one-click deploy, run it in your assistant, a vault, ask us.

## In short

- **Forking is how people should adopt our cells,** as GitHub made it the way people adopt code.
- **Fork, point Claude at it, and it is yours:** that already works on GitHub today.
- **Five ways to make a cell yours,** four of them free: GitHub, one-click deploy, your assistant, a vault; or ask us.
- **Paths, not only repositories:** start here, then fork that, then add this cell.
- **Fork-ready, not factory-ready:** what our repositories need for a stranger with Claude.
- **Let usage decide:** many templates on the hub, and invest in what people fork.
- **A brief for the team** at the end.

## Why forking

Forking is one of the things that made GitHub ridiculously powerful. You see something you like, you press a button, and you have your own copy that you can change, while the link back to where it came from stays. Open source grew on it.

It is also, I think, the most natural way for someone to use what we make. We are about to have the AgentiCCells hub properly online, listing agentic sites ([a hub for agentic sites](a-hub-for-agentic-sites.md)). If I make a template site, a cell, and someone wants it, the simplest thing is for them to fork it. And that already works: fork the repository that holds a site on GitHub, point Claude at your copy, and you have your own version, with your name and your content, served by GitHub Pages. Our job now is to make that as smooth and as effective as possible.

## Five ways to make a cell yours

Every template on the hub should offer the same five choices:

1. **Fork it on GitHub.** Press Fork, point Claude at your copy with the one prompt in its README, and GitHub Pages hosts it. Free, and it keeps the link to the original.
2. **Deploy it in one click.** Not everyone wants a GitHub account. Netlify, Vercel and Cloudflare Pages can take a repository and deploy it with almost no settings, so a template should carry the buttons and files they need.
3. **Run it in your assistant.** A site like ours needs no server, so Claude Code can run it on your own machine; and assistants can now host small pages themselves, so the copy can live where you already work, with no repository at all.
4. **Take it as a vault.** Download the cell as an encrypted vault, or a zip, with its brief and its policy, and open it wherever you like ([how a vault works](how-a-vault-works.md)).
5. **Ask us.** Commit a request, or press the button, and the site factory makes it for you, live in minutes, on the paid ladder ([the site factory works](the-site-factory-works.md)).

The first four are free, on purpose. What we want is for people to try it, and to find their own uses for it.

## Paths, not only repositories

A single repository is a start. A path is better: start with this repository, a one-page site; then fork that one, which adds a feedback lane; then add this cell, which puts an agentic team behind it. Each step is a repository Claude can be pointed at, small enough to understand, and each one teaches the next. Connected to an agentic workflow, the path is something an agent can walk you through, one fork at a time ([reading your way into an agentic team](reading-your-way-into-an-agentic-team.md)).

## Fork-ready, not factory-ready

What makes a repository fork-ready: built for a stranger with Claude, not only for our own factory.

Forking is only as smooth as the repository allows, and ours are built for our own factory. The AgentiCCells site template has placeholders only the factory replaces, a CLAUDE.md written for our team, a commit check that wants an AgentiCCells agent name, and a domain and hub entry pointing at ours. A stranger who forks it would fall at the first push.

A fork-ready repository is built for a stranger with Claude:

- **"Point Claude here":** the README opens with the one prompt that makes the copy yours.
- **A CLAUDE.md for any agent,** with our own rules as an option, not a requirement.
- **One settings file:** name, domain, colours, contact; everything else follows from it.
- **Sample content clearly marked,** and replaced on the first run.
- **Its behaviour policy included,** so the fork starts governed, not wide open ([CI behaviour policies](ci-behaviour-policies.md)).
- **Upstream updates:** when the original improves, an agent proposes the change to every fork that wants it, and the fork's owner decides.

## Let usage decide

The fork loop: make many templates, list them on the hub, watch what is forked, invest where it pulls, keep forks alive.

The business follows from that. We make dozens, then hundreds, of these small templates and cells, from our own work and from what people ask for ([the cell is the unit](the-cell-is-the-unit.md)). We put them on the hub, each with its page, a Fork button and a path. We watch what people fork, star and ask about. And we invest where it pulls: a better template, paid help on the ladder, the next cell in that line. Forks that stay linked get the improvements, so the popular templates keep getting better for everyone.

It is the open source model again: the free fork drives usage and finds the use cases, and the paid help is there for those who want it done for them ([integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md)).

## The brief for the team

1. **A GitHub organisation for templates,** separate from the team's own repositories, so forks and stars measure the templates alone.
2. **Make the site template fork-ready,** with the six points above, and keep a factory mode for our own use.
3. **The first twenty templates,** from what we already have: the newsroom-style site, the hub, a person's site, a producer's site, a town page, a review page, a vault-backed page, and the cells in [the cell is the unit](the-cell-is-the-unit.md).
4. **Five buttons on every hub entry:** fork, deploy, run in your assistant, download as a vault, ask us.
5. **Three paths,** each three or four repositories long, from a one-page site to a site with an agentic team.
6. **Test with strangers:** synthetic users first, then real people, forking each template with only the README, and fix where they stop ([synthetic users for your website](synthetic-users-for-your-website.md)).
7. **Count it:** forks, deploys, downloads and requests per template, on the hub, so we know what to make next.

## What this does not claim

- **This is a plan;** the hub lists sites today, without Fork buttons or paths.
- **The one-click deploys and assistant hosting** need checking template by template; each service has its own limits.
- **The template organisation does not exist yet.**

## Where this comes from

My own thinking, 16 November 2026. The AgentiCCells hub at [hub.agenticcells.site](https://hub.agenticcells.site/) and the repositories AgentiCCells__Site__Hub and AgentiCCells__Site__Template, read the same day. Earlier on this site: [a hub for agentic sites](a-hub-for-agentic-sites.md), [the site factory works](the-site-factory-works.md), [the cell is the unit](the-cell-is-the-unit.md), [reading your way into an agentic team](reading-your-way-into-an-agentic-team.md), [CI behaviour policies](ci-behaviour-policies.md), [how a vault works](how-a-vault-works.md), [integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md), [synthetic users for your website](synthetic-users-for-your-website.md).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#fork-it)

### Builds on

- [A hub for agentic sites: every site AgentiCCells builds in a repository and an sgit vault, served at its own address, and listed on hub.agenticcells.site, where it can be found, promoted and copied as a template; with an orange grower as the first example](a-hub-for-agentic-sites.md) hub.agenticcells.site: every agentic site in a repository and an sgit vault, served at its own address, found, promoted and copied as a template.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [Reading your way into an agentic team: eight public sites a new team should read before it builds anything, how an agent should read them, and ten questions to answer first, because our websites are its memory](reading-your-way-into-an-agentic-team.md) Eight public sites a new agentic team should read before it builds anything, how an agent should read them, and ten questions to answer first.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place](integrate-with-whatever-is-on-the-other-side.md) We never start by asking a customer to move. We integrate with what they run, build around it, and either retire our code or become the better place.
- [Synthetic users for your website: how to set up five invented visitors who read your site one screenshot at a time, with Claude, a sub-agent per persona, and an encrypted vault you can publish anywhere](synthetic-users-for-your-website.md) Onboarding for synthetic users: invented personas, a sub-agent each, a real browser one screenshot at a time, all in a vault you publish.

### Continued by

- [Show me the evidence: websites for people looking for a job, built by an agentic cell, with seven pages that prove instead of list, a page made for each employer, a pack for recruiters, eight personas to fork, a ladder from a free recipe to a recruiter's cell, and the brief for the team that builds it](show-me-the-evidence.md) Websites for people looking for a job that show evidence instead of lists: seven pages, a page per employer, a recruiter pack, eight personas to fork.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 437 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=437)

**Posting this article on LinkedIn?** The cover is [fork-it.jpg](banners/fork-it.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/fork-it.html)*
