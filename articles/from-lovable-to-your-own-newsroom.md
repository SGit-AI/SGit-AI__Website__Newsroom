# From Lovable to your own newsroom: a brief for José Bota and his agent, to put every app on GitHub Pages under his own domain, and publish each one as an article, sgit.ai

> José Bota, one of our collaborators, has built a couple of very good examples in Lovable that measure the reach of an AI agent: what is your agent doing, and how could you know? They work well. What they do not have yet is a home. This article is a brief, written for José and for the agent he works with, so he can point his Claude or ChatGPT at it and carry on. Step one: when Lovable has finished the MVP, move it into a GitHub repository and publish it with GitHub Pages, so everything he makes is visible. Step two: a domain with his name on it, bought in AWS Route 53, because it is his brand: a main site, and one subdomain per app under a demos subdomain. Step three: newsroom on that domain, the same workflow as this newsroom, so that every app gets an article and every idea gets written down. The measure of success is simple: José sends me two or three links, apps live on his domain and the articles about them on his newsroom, and we write about them here and amplify them from RiskMandate. The work I want to do with José is a family of small tools that show the reach of an agent and how dangerous it could be, which is also a business for him: help a company understand what its agents can reach, then help protect it. The demos are public; a client who wants their own version gets a private repository with their customisations, through exactly the same workflow. A starter pack for his agent comes with the article: the brief, a Pages workflow, the DNS records, an app list and house rules for the newsroom.

*Source: <https://newsroom.sgit.ai/articles/from-lovable-to-your-own-newsroom.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / From Lovable to your own newsroom: a brief for José Bota and his agent, to put every app on GitHub Pages under his own domain, and publish each one as an article

# From Lovable to your own newsroom: a brief for José Bota and his agent, to put every app on GitHub Pages under his own domain, and publish each one as an article

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/from-lovable-to-your-own-newsroom.md) · [newsroom v0.14.25](https://newsroom.sgit.ai/admin/versions.html) · lovablegithub-pagesnewsroomdomainsagentsagent-reachbriefarticle

***Abstract:** José Bota, one of our collaborators, has built a couple of very good examples in Lovable that measure the reach of an AI agent: what is your agent doing, and how could you know? They work well. What they do not have yet is a home. This article is a brief, written for José and for the agent he works with, so he can point his Claude or ChatGPT at it and carry on. Step one: when Lovable has finished the MVP, move it into a GitHub repository and publish it with GitHub Pages, so everything he makes is visible. Step two: a domain with his name on it, bought in AWS Route 53, because it is his brand: a main site, and one subdomain per app under a demos subdomain. Step three: newsroom on that domain, the same workflow as this newsroom, so that every app gets an article and every idea gets written down. The measure of success is simple: José sends me two or three links, apps live on his domain and the articles about them on his newsroom, and we write about them here and amplify them from RiskMandate. The work I want to do with José is a family of small tools that show the reach of an agent and how dangerous it could be, which is also a business for him: help a company understand what its agents can reach, then help protect it. The demos are public; a client who wants their own version gets a private repository with their customisations, through exactly the same workflow. A starter pack for his agent comes with the article: the brief, a Pages workflow, the DNS records, an app list and house rules for the newsroom.*

From a Lovable MVP to your own newsroom: the loop José Bota's agent follows, step by step.

## In short

- **José Bota has built tools in Lovable that measure an agent's reach.** They need a home.
- **Step one: GitHub and Pages,** so every app he makes is visible.
- **Step two: a domain with his name,** bought in Route 53, with one subdomain per app.
- **Step three: a newsroom on that domain,** the same workflow as this one, an article per app.
- **Success is two or three links** from José, which we then write about and amplify.
- **The business:** help a company see what its agents can reach, and protect it.
- **Public demos, private versions:** a client gets a private repository through the same workflow.

## The tools José has built

José Bota is one of our collaborators; he is the person I am working with on voice debriefs. He has taken the question at the heart of [what can your agent reach](what-can-your-agent-reach.md), what is your agent doing, and how could you know, and built a couple of very good examples of it in Lovable. They work well.

What they do not have yet is a home. A Lovable app lives in Lovable, and a link to it says nothing about who made it or what else they have made. So this article is a brief, written for José and for the agent he works with: he can point his Claude or ChatGPT at this page, and continue from here.

## Step one: from Lovable to GitHub Pages

When Lovable has finished the MVP, the next move is to put it in a GitHub repository and publish it with GitHub Pages, so that everything José makes is visible and has a history:

1. **Connect GitHub in Lovable,** so the project syncs to a repository under José's account.
2. **Check the stack first.** Older Lovable projects are Vite apps, which build to static files that GitHub Pages can serve. Newer ones use TanStack Start with server rendering, which needs either a static build or a host that runs Node. The agent should say which it is before going on.
3. **Add a workflow** that builds the app and publishes it to Pages on every push; the starter pack has one.
4. **Push, open the link, send it.** Every step ends with something José can open.

## Step two: a domain with his name

Every app needs an address, and the address should be José's, because the brand is him. So the recommendation is a domain with his name on it, bought in AWS:

- **Buy it in Route 53.** Route 53 registers .com, .io, .site, .ai and .dev among many others. It does not register .pt; a .pt name can be bought from a .pt registrar and still use Route 53 for its DNS.
- **A main site** on the domain itself, with the list of everything he has made.
- **One subdomain per app,** under a demos subdomain, such as `agent-reach.demos.` followed by his domain. Each is a CNAME record pointing at GitHub Pages, and the same name set as the repository's custom domain.
- **Verify the domain in GitHub** for his account, so nobody else can point a repository at it.

## Step three: newsroom on his domain

Once the apps have a home, they need a voice. That means `newsroom.` on his domain, with the same workflow as this newsroom, described step by step in [your own newsroom](your-own-newsroom.md): one public repository, Pages published after a validation step, a house-rules file for the agent, and articles written from voice memos and checked before they go out. The reader pages and [the reader API](https://api.newsroom.sgit.ai/) of this newsroom are open to copy, and the [PHP story site](php-october-at-8pm.md) was a variation of the same thing.

The first articles are easy: one per app, saying what it does, who it is for, what it does not do yet, and the link.

## What done looks like

The measure of success is when I receive two or three links from José: apps live on his domain, and the articles about them on his newsroom. Then we can write about his work here, and amplify it from RiskMandate. When José communicates with me, he sends me articles he wrote.

## The work, and the business

The area I want to work on with José is a family of small tools that anyone can use to see the reach of their agents, and how dangerous that reach could be: which systems an agent can touch, what data it can read, what it can do without asking. That is the gap [Agent Behaviour Policies](three-policies-for-an-agent.md) describe, made visible.

It is also a business for him. He can go to a company, or a person, and say: let's understand the reach of your agent, and then let's protect it.

And the commercial model uses exactly the same workflow. The demos are public. When a client says, I love that, but I want to run it on my side, with my changes, José sells them a private repository with their customisations: the same build, the same publishing, their data never in the public demo. It is finite work, handed over, as in [villager services](villager-services-for-explorer-coders.md).

## The starter pack

To help José, and the agent he works with, the brief comes with a starter pack, in this site's repository:

- **`BRIEF.md`:** the three steps, written for the agent, ending in the links José sends.
- **`deploy-pages.yml`:** a GitHub Actions workflow that builds a Vite app and publishes it with Pages.
- **`dns.md`:** the Route 53 records for a main site, a newsroom and an app, with an example domain.
- **`apps.example.json`:** the list of apps the main site shows, with their status and article.
- **`newsroom-CLAUDE.md`:** house rules for his newsroom, to change to his voice.

## What this does not claim

- **It is a brief.** None of the steps has been done yet; José's apps and their names in the pack are examples.
- **Prices and registries change.** Route 53's list of domain endings was read on 31 October 2026.
- **Private repositories cost.** Publishing Pages from a private repository needs a paid GitHub plan, or the client hosts it.
- **My interest:** José is a collaborator, and the tools would support RiskMandate's work.

## Where this comes from

- My voice memo of 31 October 2026, word for word in `admin/notes/2026-10-31__jose-bota/memo-01.md` in this site's repository, with the starter pack in the same folder.
- Amazon Route 53, [domains you can register](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html), read on 31 October 2026.
- Related: [your own newsroom](your-own-newsroom.md), [what can your agent reach](what-can-your-agent-reach.md), [villager services for explorer coders](villager-services-for-explorer-coders.md), [Lovable with SHarness](lovable-with-sharness.md).

## Threads

Site & engineeringAgents & policy[This article as a graph →](graphs.md#from-lovable-to-your-own-newsroom)

### Builds on

- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [PHP October 2026, at 8pm: where the php2shell story stands, and a guided tour of the site that tracks it, built in one day by a team of agents from an evidence vault anyone can read](php-october-at-8pm.md) Where the php2shell story stands at 8pm on 22 October, and a guided tour of the site built in one day to track it.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent](villager-services-for-explorer-coders.md) Villager services for explorer coders: founders with ten years of checklists build the apps; we sell everything behind them in finite packs.
- [Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today](lovable-with-sharness.md) Lovable with SHarness, and the trojanised Claude Code extension: where a policy boundary has to sit, and what SHarness can stop today.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 347 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=347)

**Posting this article on LinkedIn?** The cover is [from-lovable-to-your-own-newsroom.jpg](banners/from-lovable-to-your-own-newsroom.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/from-lovable-to-your-own-newsroom.html)*
