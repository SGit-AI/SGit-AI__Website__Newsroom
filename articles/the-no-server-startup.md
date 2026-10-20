# The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them, sgit.ai

> This is a blueprint, for founders and for the agents that work with them, of a kind of product that a lot of what I have written here adds up to. Phase one has no server and no database of its own. The product is a folder of HTML, CSS and JavaScript, built from native web components with the few libraries it needs vendored inside it, so it runs offline and anywhere a web page can be served, from a laptop to GitHub Pages to a customer's isolated network. The user brings the expensive parts: their own AI key, capped and paid by them, called straight from the browser; their own storage, in the browser, in an encrypted vault or in their own cloud drive; and their own passkey, which can give the browser a secret that only their device can produce. You are not in the line of any request, so the product scales with its users, not with your servers. The pieces mostly exist today, OpenRouter's OAuth among them, which bills each user's requests to their own credit. The gaps are on the providers' side: a user's own key with a cap, and paying the app that brought them the customer, which none of the providers I checked offers. Then how to build it, with agent sessions, a dev and a main site and an explorer as the first hire; how to charge for it; and a checklist an agent can work through.

*Source: <https://newsroom.sgit.ai/articles/the-no-server-startup.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them

# The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.0.0](versions/the-no-server-startup.md) · [newsroom v0.12.144](https://newsroom.sgit.ai/admin/versions.html) · startupsarchitectureclient-sideno-serveragentsbusiness-modelsblueprintarticle

***Abstract:** This is a blueprint, for founders and for the agents that work with them, of a kind of product that a lot of what I have written here adds up to. Phase one has no server and no database of its own. The product is a folder of HTML, CSS and JavaScript, built from native web components with the few libraries it needs vendored inside it, so it runs offline and anywhere a web page can be served, from a laptop to GitHub Pages to a customer's isolated network. The user brings the expensive parts: their own AI key, capped and paid by them, called straight from the browser; their own storage, in the browser, in an encrypted vault or in their own cloud drive; and their own passkey, which can give the browser a secret that only their device can produce. You are not in the line of any request, so the product scales with its users, not with your servers. The pieces mostly exist today, OpenRouter's OAuth among them, which bills each user's requests to their own credit. The gaps are on the providers' side: a user's own key with a cap, and paying the app that brought them the customer, which none of the providers I checked offers. Then how to build it, with agent sessions, a dev and a main site and an explorer as the first hire; how to charge for it; and a checklist an agent can work through.*

The usual SaaS and the no-server product. On the left, the company sits in the line of every request, with its servers, its database, its AI key and its bill. On the right, the product is a folder of files, and the user brings the AI key, the storage and the passkey.

## In short

- **No server and no database of yours.** Phase one is a folder of HTML, CSS and JavaScript.
- **Native web components, few libraries, all vendored.** It runs offline, and anywhere a page can be served.
- **The user brings the expensive parts.** Their AI key, their storage, their passkey.
- **You are not in the line.** No request passes through you, so it scales with users.
- **The pieces mostly exist.** The gaps are capped per-user keys and paying the app that brings the customer.
- **Build it with agents.** A dev and a main site, synthetic users, an explorer as the first hire.
- **Charge for the build, the users and the keys.** Even when they bring their own.
- **A checklist for agents.** Each step can be marked done.

## What this is

A lot of what I have written here over the last weeks is one idea in pieces: [the passkey that opens the vault](the-passkey-opens-the-vault.md), [free models with your own key](free-models-your-own-key.md), [the code you do not ship](the-code-you-do-not-ship.md), [Cloudflare as Lego blocks](cloudflare-as-lego-blocks.md), [explorer coding](explorer-coding.md), [your own newsroom](your-own-newsroom.md), [paying after the value](paying-after-the-value.md). This puts the pieces in one place, as principles, a worked example and next steps.

It is written for two readers. For a founder, it is the shape of a product that costs almost nothing to run and that nobody needs permission to deploy. For the agents a founder works with, it is a set of requirements and a checklist: what to build, what not to build, and what to mark done.

It needs a name. I would call it a **no-server product**, and a company built that way a **no-server startup**. Serverless is taken, and it means something else: there are servers, you just do not manage them. Here, in phase one, there are none of yours at all.

## The principles

1. **No server and no database of yours.** There is a CRM and an email list somewhere, but the product itself has no backend. Everything it does, it does in the user's browser.
2. **HTML, CSS and JavaScript, as native web components.** No JavaScript framework for components, no build step. The browser is the runtime. The conventions are written down at [coding.sgit.ai](https://coding.sgit.ai/javascript/index.html): a component is three files, behaviour, markup and styles, with one URL per version.
3. **Do not reinvent the wheel; vendor it.** If you need Mermaid for diagrams, or a library for charts, use it, at a pinned version, copied into the product's `vendor/` folder. Nothing is fetched from a CDN at run time.
4. **It runs offline, and anywhere.** From a file on a laptop, a simple local server, a container, a Lambda or Cloud Function that returns files, Cloudflare, any cloud, or a customer's isolated network. If something can serve a web page, it can run the product.
5. **The user brings the compute.** The expensive part, the AI model, is paid for by the user, through a key that is theirs, ideally capped, and called from their browser.
6. **The user's data stays with the user.** In the browser's storage, in an [encrypted vault](https://sgit.ai/), or in their own cloud drive. You never hold it, so you never have to protect it.
7. **The passkey is the identity.** A passkey can give the browser a secret that only the user's device can produce, and from it the keys to their data, with nothing to remember and nothing to sign up for.
8. **You are not in the line.** No request passes through you. The product scales with its users, not with your servers, and an outage of yours does not stop anyone.
9. **Everything is in version control, and agents maintain it.** A dev site and a main site, every change a commit, every release a note.
10. **Charge for value, not for servers.** For building it, for its users, and for the keys, even when the user brings their own.
One folder, served from anywhere: a laptop with no network, a simple server, a container, GitHub Pages, Cloudflare or any cloud, a function that returns files, or a customer's isolated network.

## A worked example: an infographic studio

Take a product that turns a document into infographics. Today it would be built as a SaaS: an account, a server that calls an image model with the company's key, a database of every user's images, and a margin on top of the model's price. As a no-server product, it looks like this.

The user opens the studio, which is a folder of static files, served from anywhere. They sign in with a passkey, and the browser gets a secret only their device can produce, from which it derives the keys to their storage. They connect an AI provider. With [OpenRouter's OAuth flow](https://openrouter.ai/docs/use-cases/oauth-pkce), "Each user signs in to OpenRouter and authorizes your app, and your app receives an API key tied to their account. Their requests are billed to their own OpenRouter credits." If they have no credit, they buy it there, from the provider, and come back. The studio calls the image model from the browser, with their key, and keeps the results in the browser, in an encrypted vault, or in the user's own Google Drive, in the [application data folder](https://developers.google.com/workspace/drive/api/guides/appdata), which "is only accessible by your app and its contents are hidden from the user and from other Google Drive apps."

Nothing in that loop passes through the company that built the studio. It did the work once, in the product, and a sale can happen without anyone at the company doing anything.

The infographic studio as eight steps, none through the company that built it. Six work today; a cap on the user's own key works with a catch; and getting paid for bringing the provider a customer is missing.

Every AI feature should also work without a key, in a simulation mode that returns example results. It is how a prospect tries the product before paying anyone, how the synthetic users test it, and how a demo survives a bad network.

## The gaps today

The pieces mostly exist. The gaps are on the providers' side, as their documentation reads on 20 October 2026.

- **A cap on the user's own key.** OpenRouter can create keys with a credit limit through its [provisioning API](https://openrouter.ai/docs/features/provisioning-api-keys), but those keys belong to your account, so you pay, and you are back in the business of reselling. Its OAuth page documents no spending limit for a key a user grants an app. OpenAI has project hard spend limits, and a key the user creates in their own project could carry one, but that is a setting the user has to make.
- **Keys in the browser.** OpenAI's API reference says "Don't share it with others or expose it in any client-side code such as browsers or apps", and Google's Gemini guidance says "Never expose keys client-side in production". Both are about a developer's key shipped to every user, and both are right about that. A user's own key, held in their own browser, is a different case, and OpenRouter is the provider built for it.
- **The user's own plan.** OpenAI's [Sign in with ChatGPT](https://developers.openai.com/siwc/quickstart) lets "Eligible ChatGPT Plus and Pro users" use their plan for AI requests in participating apps. It is "currently available to selected commercial partners through a limited trial", and for a website the app's backend exchanges the code, so it does not fit phase one yet. It is the right direction.
- **Paying the app that brought the customer.** OpenRouter's [app attribution](https://openrouter.ai/docs/app-attribution) gives an app rankings and analytics. I could not find a revenue share from OpenRouter, or from OpenAI, Google or Anthropic. This is the biggest gap and the biggest opportunity: a provider that gives the app a share of the credit its users buy, say a fifth, would turn every no-server product into a sales channel for that provider, with no work on either side.
- **Hosting when you sell.** GitHub Pages is the right place to start, but its own rules say it is not for a site "primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS)". Build and demo there; when the product sells, move the same folder to a host that allows it, such as Cloudflare or any cloud's static hosting.

## The stack

- **The product:** HTML, CSS and JavaScript; native web components; vendored libraries; no build step.
- **Hosting:** GitHub Pages to build and demo; Cloudflare or any static host to sell; or the folder, shipped to the customer.
- **Identity:** a passkey, with the WebAuthn PRF extension giving the browser a per-user secret, as in [the passkey opens the vault](the-passkey-opens-the-vault.md).
- **Storage:** the browser's own storage for what is small and can be lost; an encrypted sgit vault for what must last and move between devices, as [the vault crosses Chrome profiles](the-vault-crosses-chrome-profiles.md) showed; or the user's own Google Drive, in an app folder only this product can see.
- **AI:** the user's own key, capped, called from the browser.
- **Payments:** ideally the provider's; otherwise a payment link, with the credit kept in the browser or the vault, as this newsroom does with [pay after you read](paying-after-the-value.md).

## How to build it

Start on GitHub Pages, with a repository, two branches, and a site per branch, and move hosts when it starts to sell. Dev is where things change, and main is what customers use. An agent session, such as Claude Code wired to the repository, maintains it, and every change is a commit with a release note. This newsroom is built exactly that way, and [your own newsroom](your-own-newsroom.md) describes how.

Add synthetic users early: personas that use every page on every release, and tell you when something stops working for them. Add more agents as the product grows, each with a role and a written behaviour policy.

The team grows in Simon Wardley's order, in the names this site uses: explorers, villagers, town planners. The founder's first hire is an explorer, one person who works with the agents in [explorer coding](explorer-coding.md) mode, from a chat or the command line, and changes the dev site fast. Villagers come next, to turn what works into a product: tests, versions, releases that do not break. Town planners come last, when it has to be a utility.

How a founder builds it: agent sessions and synthetic users around one repository, a dev site and a main site, and the team hired in order, explorers, then villagers, then town planners.

## How to charge for it

The costs are almost nothing, so the price is about value, not about covering servers.

- **For building it.** A new site for a customer, their segment, their workflow, their brand, is a project with a price.
- **For its users.** Per user, per month or per use.
- **For the keys.** Even when users bring their own key, they pay you for the product that uses it: a share of what they buy, when providers allow it, or a fee for the credit you manage for them.
- **For running it where they are.** The same folder, installed inside a customer's own network, is a licence.

This newsroom uses the same model on itself: you start with credit, you pay for what you read, and the price falls as you read more. The product is the same set of files for everyone; what changes is who brings what.

## For agents: the next steps

Each step is a checkbox an agent can mark, with the evidence that it is done.

- [ ] **NS-01 Repository.** One repository, a `dev` and a `main` branch, a site per branch, a version file and a release note per release.
- [ ] **NS-02 No backend.** No server code, no database, no secret in the repository. A scan in the release script proves it.
- [ ] **NS-03 Components.** Every UI element is a native web component, three files, versioned path. No framework.
- [ ] **NS-04 Vendored.** Every library is in `vendor/`, pinned, with its licence. The site loads nothing from another origin except the AI provider and the storage the user chose.
- [ ] **NS-05 Offline.** The product opens from a file and from a local server with the network off, and says clearly what needs the network.
- [ ] **NS-06 Anywhere.** The same folder is served from GitHub Pages and from one other host, with no change.
- [ ] **NS-07 Passkey.** Sign-in with a passkey; the PRF secret derives the user's storage keys; nothing to remember.
- [ ] **NS-08 Storage.** Local storage first; then an encrypted vault; then, optionally, the user's own drive.
- [ ] **NS-09 The user's key.** Connect the user's AI provider, store the key only where the user's data is stored, show the cap and the spend.
- [ ] **NS-10 Simulation mode.** Every AI feature works without a key, with simulated results, for demos and tests.
- [ ] **NS-11 Synthetic users.** Personas that walk through every page on every release, in the release script.
- [ ] **NS-12 Pricing.** A price page, and a payment path that never requires a server of yours.

## What this does not claim

- **Phase one only.** Some products will need a server later; the point is not to start with one.
- **The name is a proposal.** No-server, as distinct from serverless.
- **Provider terms change.** What each provider allows is as of 20 October 2026.
- **Not every product fits.** Anything that must hold shared state between users needs more than this.
- **This is a blueprint, not a product.** A working MVP is the next step.

## Where this comes from

A voice memo of 20 October 2026, with the provider facts checked against their documentation that day. The conventions for components are from [coding.sgit.ai](https://coding.sgit.ai/javascript/index.html). The pieces are from earlier articles here: [the passkey opens the vault](the-passkey-opens-the-vault.md), [free models with your own key](free-models-your-own-key.md), [the code you do not ship](the-code-you-do-not-ship.md), [Cloudflare as Lego blocks](cloudflare-as-lego-blocks.md), [explorer coding](explorer-coding.md), [your own newsroom](your-own-newsroom.md), [paying after the value](paying-after-the-value.md) and [the vault crosses Chrome profiles](the-vault-crosses-chrome-profiles.md). Simon Wardley, [on pioneers, settlers and town planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html), 2015. Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#the-no-server-startup)

### Builds on

- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.
- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it](the-vault-crosses-chrome-profiles.md) The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 220 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=220)

**Posting this article on LinkedIn?** The cover is [the-no-server-startup.jpg](banners/the-no-server-startup.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-no-server-startup.html)*
