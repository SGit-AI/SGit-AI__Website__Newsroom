---
title: Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Today I showed someone PrompTugal.news, our encrypted vaults and how our agents talk to each other, and the thing they picked up on was not any of it. It was a problem: the disconnect, in Portugal, between areas, between entities and between data sources. Each holds part of a picture and none can see the whole. I think we can now fix that, and I am comfortable saying it plainly: we can connect any data with any data. The method is not magic and that is the point. Access the source; parse it; transform it; put it in a vault; move the vault to the other side; share the key with that side's public key; on the other side, open it, parse it and map it to their data; and produce the output. Every step signed and recorded, the parsers written once as code, and a person approving every key that crosses from one owner to another. We do more complex things than this every day: the Storm Charles site put 34 public datasets behind one weather page in a night. So here is the method, what it means for the owners, the human gates, four example connections, and why it belongs on the shelf of an agentic cell: do you want to connect two datasets, five, fifty, a hundred?
version: v0.14.142
license: https://creativecommons.org/licenses/by/4.0/
tags: data, integration, vaults, pki, agenticcells, portugal, public-sector, article
status: published
---

!shot cad-steps.webp | images/ | Any data with any data, in nine steps: access, parse, transform, vault, move, key, open, map, output. | process

## In short {#in-short}

- **The problem I keep hearing:** areas, entities and data sources that do not talk to each other.
- **What I can now say plainly:** we can connect any data with any data.
- **Nine steps,** from access to an output, each signed and recorded.
- **Each owner keeps control:** data moves in vaults, keys move sealed, a person approves each one.
- **Code does the running; agents do the building,** so it is cheap to keep.
- **It should be a product:** connect two datasets, five, fifty, a hundred.

## The disconnect {#disconnect}

Today I showed someone what we have been building: PrompTugal.news, sgit's encrypted storage, the way our agents talk to each other through lanes in a vault. What they picked up on was a problem I hear often. In Portugal, as in most places, the disconnect is the issue: between regions, between entities, between the data each one holds. A municipality, a regional authority, a university, a water company and a tourism body each see part of a picture. Nobody sees the whole, and joining it up is usually a project that takes years, a shared platform nobody owns, and an argument about who keeps the data.

## Any data, with any data {#claim}

I am now comfortable saying it: we can connect any data with any data. Not because of one clever system, but because of a method our agents use every day, which reduces the problem to steps that are each small and boring:

1. **Access:** read the source where it lives, an API, a file, a page, a database export, a spreadsheet, with the owner's permission.
2. **Parse:** a parser for that source, written once, as code.
3. **Transform:** shape it into a schema both sides can read, with where each value came from and when it was read.
4. **Vault:** save it into an encrypted, versioned vault ([how a vault works](/articles/how-a-vault-works.html)).
5. **Move:** send the vault to the other side; the server in between never sees inside it.
6. **Key:** share the vault's read key with the other side's public key, sealed so only they can open it ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).
7. **Open:** the other side opens it with their own key.
8. **Map:** parse it there and map it to their own data, a join, a graph, a table.
9. **Output:** produce what was asked for, a dashboard, a report, an alert, a page, saved back as new files with its provenance.

That is our LETS cycle, Load, Extract, Transform, Save, run across an organisational boundary instead of inside one ([Relate, debriefed](/articles/relate-debriefed.html)).

## Why I believe it {#why}

Because we do more complicated things than this every day. When Storm Charles reached Lisbon, our agents built a site overnight with 34 public datasets in a catalogue with their hashes, warnings and observations joined station by station, every line labelled fact, evidence or hypothesis ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html)). PrompTugal.news runs an agent for every town in the Algarve, each joining public sources for its place ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)). Our agents pass work to each other through vaults and lanes all day. Two organisations swapping a dataset is a smaller version of what already runs.

## Each owner keeps control {#control}

!shot cad-owners.webp | images/ | Each owner keeps its data: vaults move, keys move sealed, a person approves every key that crosses. | concept

This is the part that usually stops these projects, and the part the method changes:

- **Nobody moves to a shared platform.** Each side keeps its own systems; we build around them ([integrate with whatever is on the other side](/articles/integrate-with-whatever-is-on-the-other-side.html)).
- **The data travels encrypted;** the host never holds a key.
- **Each side chooses what crosses:** a slice, a summary, an aggregate, never the whole if the whole is not needed.
- **Keys are per version:** stop sharing the next version, and the connection stops.
- **Everything is signed:** which data, which version, who approved, who opened it, when.

## Agents, with a person in charge {#gates}

Agents write the parsers, the transforms and the maps, and they keep them working when a source changes. But three things stay with a person, every time: approving access to a source, approving a key that crosses from one owner to another, and approving an output that goes public. Each agent works under a written behaviour policy that says what it may read and what it may never send ([where assist becomes execute](/articles/where-assist-becomes-execute.html)).

And the running is cheap. Once a parser and a map exist, they are code: a scheduled job, no model in the loop, almost no tokens. The tokens go into building the connection and fixing it when something changes, not into every run.

## Four connections worth making {#examples}

Proposals, to show the shape:

- **Weather, civil protection and schools:** official warnings joined to the schools and roads of each parish, so a closure decision has the evidence beside it.
- **Water and tourism:** water use joined to occupancy, week by week, in a region where drought is a real risk.
- **Heritage and planning:** a university's survey of archaeological sites joined to a municipality's planning applications, with sensitive locations kept on the university's side ([HeritageTech, together](/articles/heritage-tech-together.html)).
- **Local news and public records:** a town's news joined to the council's published decisions and budgets, so a story can show the record it rests on.

## A product: connect two, five, fifty, a hundred {#product}

!shot cad-ladder.webp | images/ | Connecting datasets as an agentic cell: two, five, fifty, a hundred, each with its own human gates. | comparison

This is something an agentic cell should sell ([the cell is the unit](/articles/the-cell-is-the-unit.html)). Do you want to connect two datasets? Five? Fifty? A hundred? The work grows, but the method does not change:

- **Two datasets:** one connection, one output, in a session.
- **Five:** a small cell that builds and keeps the connections, with a board where the owners approve keys.
- **Fifty:** a team, with a conductor, several owners, a catalogue of every dataset with its provenance.
- **A hundred:** a network of cells, one per owner or area, connected by vaults and keys.

It sits on the same ladder as everything else we sell ([the intersection](/articles/the-intersection.html)), and on the same open stack, so an owner can take it in-house at any point.

## What this does not claim {#limits}

- **Access is the owner's decision;** the method does not get past a closed door, and it should not.
- **The examples are proposals,** not projects we run.
- **Some data needs more than encryption:** personal data still needs a legal basis, and aggregates can still identify people; the method helps record those decisions, it does not make them.

## Where this comes from {#sources}

My own conversation on 17 November 2026, with someone I showed our work to, who is not named. Earlier on this site: [how a vault works](/articles/how-a-vault-works.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [Relate, debriefed](/articles/relate-debriefed.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [integrate with whatever is on the other side](/articles/integrate-with-whatever-is-on-the-other-side.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [HeritageTech, together](/articles/heritage-tech-together.html), [the cell is the unit](/articles/the-cell-is-the-unit.html), [the intersection](/articles/the-intersection.html).
