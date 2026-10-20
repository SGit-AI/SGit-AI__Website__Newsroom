# Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault, sgit.ai

> A tour of the vault behind the no-server startup. The no-server studio turns a document into an infographic in the browser. It is one HTML file of seven native web components, with no framework, no build step and no server, built from separate component files that a small script inlines, because a vault app must be one page. Most of it is simulated, on purpose. A deterministic extractor stands in for the model, so every feature works offline and every result replays; inside the vault, the studio asks the vault host for a model, and on a public read the host answers that there is no key, so the studio says so and stays in simulation. Served as its own page, it can use OpenRouter's OAuth or a pasted key, held in memory; that path is written and checked, not yet run against a live key. The flow walks the blueprint's eight steps with invented money. The business plan, for somebody to build, has three businesses, prices as hypotheses and a calculator. Nine of the blueprint's twelve steps are done, two are partial and one is simulated. Three synthetic users walked it before it was published, and the vault caught one real bug on the way: its sandbox has no session storage.

*Source: <https://newsroom.sgit.ai/articles/inside-the-no-server-studio.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault

# Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.0.0](versions/inside-the-no-server-studio.md) · [newsroom v0.12.146](https://newsroom.sgit.ai/admin/versions.html) · startupsarchitectureclient-sideno-servervaultsbusiness-modelsarticle

***Abstract:** A tour of the vault behind the no-server startup. The no-server studio turns a document into an infographic in the browser. It is one HTML file of seven native web components, with no framework, no build step and no server, built from separate component files that a small script inlines, because a vault app must be one page. Most of it is simulated, on purpose. A deterministic extractor stands in for the model, so every feature works offline and every result replays; inside the vault, the studio asks the vault host for a model, and on a public read the host answers that there is no key, so the studio says so and stays in simulation. Served as its own page, it can use OpenRouter's OAuth or a pasted key, held in memory; that path is written and checked, not yet run against a live key. The flow walks the blueprint's eight steps with invented money. The business plan, for somebody to build, has three businesses, prices as hypotheses and a calculator. Nine of the blueprint's twelve steps are done, two are partial and one is simulated. Three synthetic users walked it before it was published, and the vault caught one real bug on the way: its sandbox has no session storage.*

The no-server studio, opened from its vault in the official vault UI, read-only, with the published key. The host reports no AI key for a public read, and the studio says so and stays in simulation.

The no-server startup

A blueprint for products with no server and no database of their own, a tour of an MVP built to it, and the MVP itself, in a vault, with its business plan.

[1 · The blueprintThe no-server startupTen principles, the provider gaps, how to build and charge, and a checklist for agents.](the-no-server-startup.md)[you are here2 · The tourInside the no-server studioAn infographic studio built to the blueprint: what is real, what is simulated, and the plan.](inside-the-no-server-studio.md)

3 · The vaultThe no-server studioMake an infographic from your own text, walk the flow, and run the business plan's numbers.[Use it](https://newsroom.sgit.ai/demos/vaults/no-server-studio/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_f12934c9b37c9c8911aafa6897c6a89b8375ef6fb84232fcf929c40b1c7cdc98%3Aiozssz56)

## In short

- **An infographic studio, built to the blueprint.** One HTML file, seven web components, no server.
- **Mostly simulated, on purpose.** A deterministic extractor stands in for the model.
- **The model's key is never the studio's.** The vault host holds it, caps it and asks first.
- **The flow, with invented money.** Passkey, provider, credit, cap, generation, the share.
- **A business plan, for somebody to build.** Three businesses, prices as hypotheses, a calculator.
- **Nine of twelve steps done.** Two partial, one simulated, each with its evidence.
- **Three synthetic users walked it first.** And the vault caught one real bug.

## The studio

Pick one of four sample documents, or paste your own, choose a layout and a theme, and the browser draws the infographic. There are four layouts, a poster, big numbers, cards and steps, and three themes. The samples are an invented bakery's quarter, the no-server startup in brief, how a passkey opens your data, and the Pellbridge day. What you make, you can keep in the session's gallery.

The Pellbridge day as big numbers, in the night theme.

The gallery draws every sample in every layout, live, from the same engine, so it is also a test that the engine handles every combination.

The gallery: four sample documents, four layouts, three themes, all drawn in the browser.

## How the content is made

The engine, `studio.js`, has four functions. `extract` is the simulation: it reads a document's title and subtitle, finds the numbers with what they count, "6,400 loaves" from "The new sourdough line sold 6,400 loaves", keeps the other sentences as points, and turns a sentence that starts "First" into steps. `prompt` and `parse` are the model's path: the same document, sent with an instruction to reply with the same shape as JSON, and only the facts it contains. `render` draws the result as SVG, whichever of the two wrote it.

So the model only ever writes the words. The drawing is code, in the browser, and the same for both, which is what makes the simulation a fair stand-in and the output the same shape every time.

## Where the model's key comes from

There are three ways, and the studio shows which one is in use.

- **Inside the vault.** The studio asks the vault host for a model through `sg.llm`. The host holds the key, caps the spend per session, asks the user before the first call, and never shows the key to the page. That is the capped key the providers are missing, at the vault layer. On a public read there is no key, and the host answers `ENOKEY`, which the studio shows rather than hides.
- **Served as its own page.** OpenRouter's OAuth flow, with the user signing in at OpenRouter and the studio receiving a key on their account; or a key pasted by the user, for OpenRouter or OpenAI, held in the page's memory only. This path is written and checked in code. It has not yet been run against a live key.
- **Neither.** Simulation, which is where everything in the published vault runs.

## The flow, with invented money

The flow tab walks the blueprint's eight steps. Press each one: a simulated passkey produces a storage key; a simulated OAuth round trip returns a key on the user's account; £10 of credit is bought at the provider, not the studio; a cap of £2 is set; a generation spends a penny of it; the result is kept with the user. The eighth step is the gap: the studio would earn £2 of that £10 if a provider paid apps a fifth, and none does today.

The flow after every step has been tried: the credit at the provider, what was spent, and what the studio would earn at a fifth.

## The business plan

The plan is for somebody to build. It has three businesses: the studio for one segment, a studio that builds no-server products for others, and the credit layer the providers are missing. It has who it is for, five packages from free to "build me one", go-to-market starting where documents already exist, the first ninety days, the risks as acceptances with a door and an interval each, and the open questions.

The calculator turns a handful of hypotheses into a month. At its starting values, 2,000 visitors, 4% converting to £4 a month, three small teams, a quarter of an install and half a build a month, it comes to about £4,250, and £4,364 if a provider paid a fifth of the credit users buy. The model's cost is not on the page: the users pay it, at the provider. Every number is a hypothesis to change.

## The checklist

The blueprint's twelve steps, marked for this MVP, each with its evidence. Nine are done, from no backend and native components to simulation mode, synthetic users and pricing. Two are partial: the repository has no dev and main branches yet, only the vault's history; and the user's own key is written but not yet run live. One is simulated: the passkey, because the vault viewer runs the app in a sandboxed frame.

The checklist for this studio: nine done, two partial, one simulated.

## Synthetic users, and the bug they did not find

Before publishing, three personas walked the studio in a headless browser: Maya, who owns a bakery and uses a phone; Tom, a consultant who pastes his own text; and Ana, deciding whether to build it, who walks the flow, the plan and the checklist. Each has checks: Maya sees her sales as a big number and finds it in the gallery; Tom gets steps from his own words and is told no model was called; Ana sees the credit bought at the provider, not the studio. All passed, with no script errors and no sideways scroll. Their results are in the vault, in `tests/synthetic-users.json`.

The first run caught a rounding slip, a simulated price of less than a penny that a £10 wallet did not show. The bug they could not find was the vault's own: the sandboxed frame the vault viewer runs apps in has no session storage, so the OAuth return code threw an error there. The live check in the vault UI found it, and the code now guards it. Synthetic users test the product; a live check tests the place it runs.

## How it is built

The components are separate files in `components/`: `ns-key`, `ns-studio`, `ns-gallery`, `ns-flow`, `ns-plan`, `ns-calc` and `ns-checklist`, with a shared `ns-base` for the event bus and the session state. A vault app must be one page with everything inlined, so `tools/bundle.py` inlines them, the engine and the data into `index.html`. `tools/assemble.py` writes the gallery's SVGs, the business plan as markdown and the checklist, and `tools/synthetic_users.mjs` runs the personas. The same `index.html` opens from the vault, from a file on a laptop, or from any static host. [The vault's page](https://newsroom.sgit.ai/demos/vaults/no-server-studio/index.html) has the read key and the studio to use in place.

## What this does not claim

- **It is mostly simulated.** The documents, money, prices and plan numbers are invented or hypotheses.
- **The live-key path is not proven.** Written and checked in code; not yet run against a real key.
- **The passkey is simulated.** The vault's sandboxed frame cannot use WebAuthn.
- **The extractor is not a model.** It picks words from the document; it does not write them.
- **No provider pays apps today.** The fifth is a hypothesis.

## Where this comes from

[The no-server startup](the-no-server-startup.md), for the blueprint, the gaps and the checklist. The vault host's model interface is from the vault platform's own authoring guide, read 20 October 2026. Every number in this article is from [the no-server studio vault](https://newsroom.sgit.ai/demos/vaults/no-server-studio/index.html), built for it. Related: [inside the Pellbridge agents](inside-the-pellbridge-agents.md), [free models with your own key](free-models-your-own-key.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Startups & strategyVaults & method[This article as a graph →](graphs.md#inside-the-no-server-studio)

### Builds on

- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.

### Continued by

- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: three levels for secrets, and a hook tested against nine leaks.
- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 221 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=221)

**Posting this article on LinkedIn?** The cover is [inside-the-no-server-studio.jpg](banners/inside-the-no-server-studio.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/inside-the-no-server-studio.html)*
