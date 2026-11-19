# Your own registrar: which domain registrar to recommend to a small business in Europe taking its website's domain into its own name, sixteen compared on price and renewal, .eu, .pt and .ai, privacy, and APIs safe enough to hand to an agent, why AWS now sells .ai but is still a heavy choice, and the three we would put forward, sgit.ai

> Some of the people whose websites AgentiCCells builds want their domain in their own name, at a registrar of their own. I wanted to recommend one, and my instinct was AWS, but a whole AWS account just to hold a domain is a heavy thing to ask of a small business. So we compared sixteen registrars from their own pages on 19 November 2026. AWS does now sell .ai, at $137 a year with no privacy protection, but not .pt, and its DNS is billed separately. Cloudflare sells at cost but offers neither .eu nor .pt and makes you use its DNS. The biggest catch across Europe's registrars is renewal: Gandi's .com goes from €11.65 to €31.98 a year. Agent tooling has moved fast: Porkbun, Dynadot, OVHcloud, Hostinger, Namecheap and Cloudflare have official MCP servers, and the controls differ, from keys limited by domain and a spend cap to an agent that cannot pay at all. For a European small business we would put forward OVHcloud, Hostinger and INWX, each with its catch.

*Source: <https://newsroom.sgit.ai/articles/your-own-registrar.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Your own registrar: which domain registrar to recommend to a small business in Europe taking its website's domain into its own name, sixteen compared on price and renewal, .eu, .pt and .ai, privacy, and APIs safe enough to hand to an agent, why AWS now sells .ai but is still a heavy choice, and the three we would put forward

# Your own registrar: which domain registrar to recommend to a small business in Europe taking its website's domain into its own name, sixteen compared on price and renewal, .eu, .pt and .ai, privacy, and APIs safe enough to hand to an agent, why AWS now sells .ai but is still a heavy choice, and the three we would put forward

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/your-own-registrar.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · domainsregistrarseuropesovereigntyagenticcellsagentsarticle

***Abstract:** Some of the people whose websites AgentiCCells builds want their domain in their own name, at a registrar of their own. I wanted to recommend one, and my instinct was AWS, but a whole AWS account just to hold a domain is a heavy thing to ask of a small business. So we compared sixteen registrars from their own pages on 19 November 2026. AWS does now sell .ai, at $137 a year with no privacy protection, but not .pt, and its DNS is billed separately. Cloudflare sells at cost but offers neither .eu nor .pt and makes you use its DNS. The biggest catch across Europe's registrars is renewal: Gandi's .com goes from €11.65 to €31.98 a year. Agent tooling has moved fast: Porkbun, Dynadot, OVHcloud, Hostinger, Namecheap and Cloudflare have official MCP servers, and the controls differ, from keys limited by domain and a spend cap to an agent that cannot pay at all. For a European small business we would put forward OVHcloud, Hostinger and INWX, each with its catch.*

Seven registrars compared: where they are, .com, .eu, .pt and .ai prices, and what an agent can use.

## In short

- **The ask:** a registrar a small business in Europe can hold its own domain at, without a cloud account.
- **AWS does sell .ai now,** at $137 a year with no privacy, but no .pt, and DNS costs extra.
- **Renewal is the catch:** first-year prices often double or triple.
- **Agents are now expected:** six registrars have official MCP servers, with very different controls.
- **Our three:** OVHcloud, Hostinger and INWX, each with its catch.

## Why this matters

A website you own includes its name. AgentiCCells builds sites the owner can take anywhere ([sovereignty you can move](sovereignty-you-can-move.md), [no lock-in](no-lock-in.md)), and some owners now want the domain at a registrar of their own, not ours. The registrar is where the name is really held, so it matters which one they pick: who it answers to, what the second year costs, and what can be done with the account if a key is ever handed to an agent.

My first thought was AWS. It is solid, and we use Route 53 for our own zones. But asking a florist or a language school to open a full AWS account to hold one domain is a lot: billing, IAM, and a console built for engineers. So we looked at the market, from each registrar's own pages, on 19 November 2026.

## What we compared

Sixteen registrars: Gandi, OVHcloud, INWX, Hostinger, IONOS, Hetzner and Infomaniak in Europe; Porkbun, Namecheap, Cloudflare, AWS Route 53, Squarespace, Dynadot, Hover, name.com and GoDaddy beyond it. For each: where it is based; the price of a .com, .eu, .pt, .co.uk and .ai, first year and renewal; whether WHOIS privacy is free; DNS and DNSSEC; whether there is an API and what it takes to use; and anything an agent could be given.

Three facts frame every choice. A .ai name needs a two-year minimum everywhere. A .eu name needs an owner in the EU or EEA. And a few registrars could not be read at all on the day (Namecheap, GoDaddy and Hover refused our requests; Cloudflare's and Infomaniak's price pages did not load), so their prices here are not confirmed.

## What we found

- **AWS Route 53** now offers .ai, two to ten years, at $137 a year and $274 to transfer, with privacy "not supported" for it. It has no .pt, and on .eu neither privacy nor domain locking is supported. Its prices are steady ($16 a .com, $8 a .eu), but every hosted zone costs $0.50 a month.
- **Cloudflare** sells at cost and includes privacy and DNSSEC, but .eu and .pt are not on its list of extensions, and a domain registered there must use Cloudflare's own nameservers. Its registrar API has been in beta since April.
- **Renewal jumps** are the commonest catch among Europe's registrars. At Gandi a .com is €11.65 the first year and €31.98 after, and a .eu goes from €3.99 to €30.00. OVHcloud's .ai goes from €70.99 to €119.99, Hostinger's from $50 to $109.99, and IONOS's welcome offers of £1 become renewals of £10 to £15.
- **Privacy is not always free.** INWX and Infomaniak charge for it (Infomaniak from CHF 2.40 a year); Gandi, Hostinger and Porkbun include it.
- **Agent tooling has arrived,** and the controls are where the registrars differ most. Porkbun's keys can be limited by domain, by IP address and by permission, including "manage but no purchases", with an account-wide spend limit that starts at $100 a month and an MCP endpoint that cannot buy. OVHcloud's MCP server signs in through the owner's browser and can prepare an order but "the order form must be paid" by a person. Dynadot's API buys only from a prepaid balance. Gandi issues tokens scoped to permissions and resources, and they expire.

That last point is the one I care about most. A registrar's API is a resource with a large reach: it can buy, transfer and repoint names. The registrars that let the owner narrow a key to one domain, take away purchasing, and cap spending are writing the resource's behaviour policy for us ([policies in practice](policies-in-practice.md)).

## Our three for a European small business

- **OVHcloud (France).** An EU company with low, steady prices on European names (a .eu €7.49 then €8.59, a .co.uk €7.49 then €7.98, a .pt €16.99 then €13.39, all excluding VAT), DNSSEC included, and an official MCP server that cannot pay. *Catch:* the .com renews at €14.29 after €8.49, and the .ai at €119.99 after €70.99; we could not confirm whether privacy is free.
- **Hostinger (Lithuania).** EU-based, every one of the five extensions, free privacy, a public API and an official MCP server with an OAuth option for agents. *Catch:* promotional first years; the $0.01 .com needs a three-year term and renews at $19.99, and the .ai more than doubles.
- **INWX (Germany).** A registrar built around its API: every function of its site through it, a free test environment, and official Terraform and Ansible tools, with all five extensions (.ai at €100 for two years). *Catch:* privacy is a paid extra, and its renewal prices would not load for us.

Outside the EU, Porkbun has the flattest prices and the safest controls for an agent, but no .pt and US jurisdiction. Gandi is European and well tooled, and held back only by its renewals.

## What this does not claim

- **Prices are as each registrar's own pages showed on 19 November 2026,** in the currency and tax basis shown; they change, and some were promotions.
- **Pages we could not read are marked unconfirmed,** in the figure and the notes; we bought nothing and opened no accounts.
- **This is not paid placement;** none of these registrars knows about this piece.

## Where this comes from

Each registrar's own pages, read on 19 November 2026, among them: AWS's [.ai](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ai.html), [.eu](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/eu.html) and [Route 53 pricing](https://aws.amazon.com/route53/pricing/) pages; Cloudflare's [TLD policies](https://www.cloudflare.com/tld-policies/), [registrar FAQ](https://developers.cloudflare.com/registrar/faq/) and [registrar API](https://developers.cloudflare.com/api/resources/registrar/); Gandi's [.com page](https://www.gandi.net/en/domain/tld/com) and [authentication docs](https://api.gandi.net/docs/authentication/); OVHcloud's [.eu page](https://www.ovhcloud.com/en-ie/domains/tld/eu/) and [domain MCP guide](https://docs.ovhcloud.com/en/guides/web-cloud/domains/mcp-domain-getting-started); INWX's [API page](https://www.inwx.com/en/offer/api) and [privacy note](https://kb.inwx.com/en-us/29-domain-contacts/50-how-can-i-activate-or-deactivate-whois-privacy); Hostinger's [TLD prices](https://www.hostinger.com/tld) and [API and MCP page](https://www.hostinger.com/support/11079316-hostinger-api-mcp-server/); Porkbun's [prices](https://porkbun.com/products/domains) and [API documentation](https://porkbun.com/api/json/v3/documentation); Dynadot's [prices](https://www.dynadot.com/domain/prices); Infomaniak's [domain privacy](https://www.infomaniak.com/en/domains/domain-privacy). The full comparison, with every source, is in the article's notes. Related: [sovereignty you can move](sovereignty-you-can-move.md), [the sovereign website](the-sovereign-website.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#your-own-registrar)

### Builds on

- [Sovereignty you can move: why where your data is hosted is not sovereignty, why being able to move the site, the data and the schema is, why that makes the website cell a direct competitor to Wix, Squarespace and Fliplet with a proper sovereign offer, European-aligned, multilingual and privacy-first, and the business that other companies can build on it](sovereignty-you-can-move.md) Sovereignty is being able to move your site, data and schema, not where it is hosted; the website cell as a sovereign competitor.
- [No lock-in: why the one thing that most separates the website cell from Wix, Squarespace, Fliplet and the rest is that the customer can leave, what the platforms' own terms and export pages say, how large the market of people paying monthly for sites they cannot take with them is, and what a site that promises to move into its owner's hands should say on its front page](no-lock-in.md) The website cell's biggest difference is that the customer can leave; the platforms' own terms show why that matters.
- [Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open](policies-in-practice.md) Four uses of feature behaviour policies: a real key's gap, signed CI changes, requests carrying policies, and release notes as fixes.
- [The sovereign website: a pivot brief for agenticcells.ai, what the site says today and what it should say next, sovereignty as the headline, a website you own, control, change and can run anywhere, the deliverables explained, the infographics to draw, five homepage designs to choose from, and the partner programme and examples that already prove it](the-sovereign-website.md) A pivot brief for agenticcells.ai: lead with sovereignty, show the deliverables, draw the infographics, and make five homepage designs.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 493 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=493)

**Posting this article on LinkedIn?** The cover is [your-own-registrar.jpg](banners/your-own-registrar.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/your-own-registrar.html)*
