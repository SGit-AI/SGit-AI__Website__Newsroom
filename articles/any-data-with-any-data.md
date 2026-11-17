# Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells, sgit.ai

> Today I showed someone PrompTugal.news, our encrypted vaults and how our agents talk to each other, and the thing they picked up on was not any of it. It was a problem: the disconnect, in Portugal, between areas, between entities and between data sources. Each holds part of a picture and none can see the whole. I think we can now fix that, and I am comfortable saying it plainly: we can connect any data with any data. The method is not magic and that is the point. Access the source; parse it; transform it; put it in a vault; move the vault to the other side; share the key with that side's public key; on the other side, open it, parse it and map it to their data; and produce the output. Every step signed and recorded, the parsers written once as code, and a person approving every key that crosses from one owner to another. We do more complex things than this every day: the Storm Charles site put 34 public datasets behind one weather page in a night. So here is the method, what it means for the owners, the human gates, four example connections, and why it belongs on the shelf of an agentic cell: do you want to connect two datasets, five, fifty, a hundred?

*Source: <https://newsroom.sgit.ai/articles/any-data-with-any-data.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells

# Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/any-data-with-any-data.md) · [newsroom v0.14.142](https://newsroom.sgit.ai/admin/versions.html) · dataintegrationvaultspkiagenticcellsportugalpublic-sectorarticle

***Abstract:** Today I showed someone PrompTugal.news, our encrypted vaults and how our agents talk to each other, and the thing they picked up on was not any of it. It was a problem: the disconnect, in Portugal, between areas, between entities and between data sources. Each holds part of a picture and none can see the whole. I think we can now fix that, and I am comfortable saying it plainly: we can connect any data with any data. The method is not magic and that is the point. Access the source; parse it; transform it; put it in a vault; move the vault to the other side; share the key with that side's public key; on the other side, open it, parse it and map it to their data; and produce the output. Every step signed and recorded, the parsers written once as code, and a person approving every key that crosses from one owner to another. We do more complex things than this every day: the Storm Charles site put 34 public datasets behind one weather page in a night. So here is the method, what it means for the owners, the human gates, four example connections, and why it belongs on the shelf of an agentic cell: do you want to connect two datasets, five, fifty, a hundred?*

Any data with any data, in nine steps: access, parse, transform, vault, move, key, open, map, output.

## In short

- **The problem I keep hearing:** areas, entities and data sources that do not talk to each other.
- **What I can now say plainly:** we can connect any data with any data.
- **Nine steps,** from access to an output, each signed and recorded.
- **Each owner keeps control:** data moves in vaults, keys move sealed, a person approves each one.
- **Code does the running; agents do the building,** so it is cheap to keep.
- **It should be a product:** connect two datasets, five, fifty, a hundred.

## The disconnect

Today I showed someone what we have been building: PrompTugal.news, sgit's encrypted storage, the way our agents talk to each other through lanes in a vault. What they picked up on was a problem I hear often. In Portugal, as in most places, the disconnect is the issue: between regions, between entities, between the data each one holds. A municipality, a regional authority, a university, a water company and a tourism body each see part of a picture. Nobody sees the whole, and joining it up is usually a project that takes years, a shared platform nobody owns, and an argument about who keeps the data.

## Any data, with any data

I am now comfortable saying it: we can connect any data with any data. Not because of one clever system, but because of a method our agents use every day, which reduces the problem to steps that are each small and boring:

1. **Access:** read the source where it lives, an API, a file, a page, a database export, a spreadsheet, with the owner's permission.
2. **Parse:** a parser for that source, written once, as code.
3. **Transform:** shape it into a schema both sides can read, with where each value came from and when it was read.
4. **Vault:** save it into an encrypted, versioned vault ([how a vault works](how-a-vault-works.md)).
5. **Move:** send the vault to the other side; the server in between never sees inside it.
6. **Key:** share the vault's read key with the other side's public key, sealed so only they can open it ([a secret is a QR code](a-secret-is-a-qr-code.md)).
7. **Open:** the other side opens it with their own key.
8. **Map:** parse it there and map it to their own data, a join, a graph, a table.
9. **Output:** produce what was asked for, a dashboard, a report, an alert, a page, saved back as new files with its provenance.

That is our LETS cycle, Load, Extract, Transform, Save, run across an organisational boundary instead of inside one ([Relate, debriefed](relate-debriefed.md)).

## Why I believe it

Because we do more complicated things than this every day. When Storm Charles reached Lisbon, our agents built a site overnight with 34 public datasets in a catalogue with their hashes, warnings and observations joined station by station, every line labelled fact, evidence or hypothesis ([Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md)). PrompTugal.news runs an agent for every town in the Algarve, each joining public sources for its place ([PrompTugal.news by place](promptugal-news-by-place.md)). Our agents pass work to each other through vaults and lanes all day. Two organisations swapping a dataset is a smaller version of what already runs.

## Each owner keeps control

Each owner keeps its data: vaults move, keys move sealed, a person approves every key that crosses.

This is the part that usually stops these projects, and the part the method changes:

- **Nobody moves to a shared platform.** Each side keeps its own systems; we build around them ([integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md)).
- **The data travels encrypted;** the host never holds a key.
- **Each side chooses what crosses:** a slice, a summary, an aggregate, never the whole if the whole is not needed.
- **Keys are per version:** stop sharing the next version, and the connection stops.
- **Everything is signed:** which data, which version, who approved, who opened it, when.

## Agents, with a person in charge

Agents write the parsers, the transforms and the maps, and they keep them working when a source changes. But three things stay with a person, every time: approving access to a source, approving a key that crosses from one owner to another, and approving an output that goes public. Each agent works under a written behaviour policy that says what it may read and what it may never send ([where assist becomes execute](where-assist-becomes-execute.md)).

And the running is cheap. Once a parser and a map exist, they are code: a scheduled job, no model in the loop, almost no tokens. The tokens go into building the connection and fixing it when something changes, not into every run.

## Four connections worth making

Proposals, to show the shape:

- **Weather, civil protection and schools:** official warnings joined to the schools and roads of each parish, so a closure decision has the evidence beside it.
- **Water and tourism:** water use joined to occupancy, week by week, in a region where drought is a real risk.
- **Heritage and planning:** a university's survey of archaeological sites joined to a municipality's planning applications, with sensitive locations kept on the university's side ([HeritageTech, together](heritage-tech-together.md)).
- **Local news and public records:** a town's news joined to the council's published decisions and budgets, so a story can show the record it rests on.

## A product: connect two, five, fifty, a hundred

Connecting datasets as an agentic cell: two, five, fifty, a hundred, each with its own human gates.

This is something an agentic cell should sell ([the cell is the unit](the-cell-is-the-unit.md)). Do you want to connect two datasets? Five? Fifty? A hundred? The work grows, but the method does not change:

- **Two datasets:** one connection, one output, in a session.
- **Five:** a small cell that builds and keeps the connections, with a board where the owners approve keys.
- **Fifty:** a team, with a conductor, several owners, a catalogue of every dataset with its provenance.
- **A hundred:** a network of cells, one per owner or area, connected by vaults and keys.

It sits on the same ladder as everything else we sell ([the intersection](the-intersection.md)), and on the same open stack, so an owner can take it in-house at any point.

## What this does not claim

- **Access is the owner's decision;** the method does not get past a closed door, and it should not.
- **The examples are proposals,** not projects we run.
- **Some data needs more than encryption:** personal data still needs a legal basis, and aggregates can still identify people; the method helps record those decisions, it does not make them.

## Where this comes from

My own conversation on 17 November 2026, with someone I showed our work to, who is not named. Earlier on this site: [how a vault works](how-a-vault-works.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [Relate, debriefed](relate-debriefed.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [PrompTugal.news by place](promptugal-news-by-place.md), [integrate with whatever is on the other side](integrate-with-whatever-is-on-the-other-side.md), [where assist becomes execute](where-assist-becomes-execute.md), [HeritageTech, together](heritage-tech-together.md), [the cell is the unit](the-cell-is-the-unit.md), [the intersection](the-intersection.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#any-data-with-any-data)

### Builds on

- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle](relate-debriefed.md) A debrief of Neo4j's Relate, and how it compares with keeping graphs as JSON in encrypted, versioned sgit vaults, and why they fit together.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI](promptugal-news-by-place.md) PrompTugal.news goes local: Portugal, the Algarve and every Algarve town, each on its own subdomain, each a lens on one graph, every story tied to AI.
- [Integrate with whatever is on the other side: why we never start by asking a customer to move, how we build around the systems they already run, from Odoo 12 to Salesforce, and how, over time, either their system gets better and we retire our code, or ours becomes the better place](integrate-with-whatever-is-on-the-other-side.md) We never start by asking a customer to move. We integrate with what they run, build around it, and either retire our code or become the better place.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [HeritageTech, together: how our open-source stack could plug into UAlgTec Heritage, the University of the Algarve's new European centre of excellence for heritage science and technology, mapped from the dig to the museum, with encrypted evidence vaults per site, signed finds, graphs of every excavation, agents with written policies, and what I would write in its "start a conversation" form](heritage-tech-together.md) How our open-source trust stack could plug into UAlgTec Heritage, the Algarve's new European centre for heritage science and technology.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.

### Continued by

- [Partners sell, we build: the AgentiCCells partner programme in full, three kinds of partner, a freelancer, a small consultancy and a larger firm, what each one sells, the agent team behind even the smallest website cell, the rules of engagement, who owns what, who invoices, who gets paid and when, what stays with the partner, and why a partner who takes the open code and does it alone is still a win](partners-sell-we-build.md) The AgentiCCells partner programme: three kinds of partner, the agent team they resell, and the rules of engagement, 50/50.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 459 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=459)

**Posting this article on LinkedIn?** The cover is [any-data-with-any-data.jpg](banners/any-data-with-any-data.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/any-data-with-any-data.html)*
