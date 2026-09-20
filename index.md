# newsroom.sgit.ai — The Future of News

> News is failing not because there is too little information but because there is no
> **walkable chain from a claim to its evidence**, no way for a correction to reach what
> it disproved, and no way to pay the person who did the original work. A story is a
> graph that accumulates evidence, perspectives and confidence; every article is a
> **projection** of it. **Sell the graph, not the paragraph.**

*Source: <https://newsroom.sgit.ai/index.html> · site v0.3.13 · markdown twin of the front page.*

---

## What is broken today

Most articles do not provide evidence, they provide a link. The link is never followed,
and it could go to a site that no longer exists.

**The 10,000-hours case.** A 1993 study of violin students found the top group had
practised an *average* of ~10,000 hours by age 20 — roughly half the group had not
reached it. Popularised in 2008 as a threshold. The original researcher spent his career
correcting it. **None of it ever attached to the claim.** [The full story
→](https://newsroom.sgit.ai/corrections/the-claim-that-would-not-die.html)

## The turn

**In a document, a correction is a new document. Nothing that cited the original knows.**
In a graph, a correction is an edge. This is the inverse of how misinformation works
today: a false claim propagates virally and the correction barely travels. In this model,
**the correction propagates with the same force as the original claim.**

## Numbers this argument stands on

| | |
|---|---|
| **242 papers** | citing one biomedical belief, tracing back to nothing |
| **>220,000** | supporting citation paths behind that same belief |
| **£8.40** | fully-itemised production cost of one worked story, 6h 23m |
| **~200ms** | settlement time on the x402 payment rail, zero protocol fees |
| **10 articles** | 68,846 words, publicly dated since February 2025 |
| **59p** | usable credit from a £1 card top-up — the wall micropayments removes |

## What runs on this site

Everything above is an argument. These are running instances of it, each a site inside the
site, built by agents and reviewed before publication:

- **Portugal Startups (beta, human-reviewed)** — a publication mapping the Portuguese startup
  ecosystem, first beat Startup Summit Lisbon 2026. Every source fetched, frozen and hashed;
  88 frozen pages; a graph of 329 nodes with Portuguese verbs; three stories; a
  data-protection notice with a named editor of record.
  [The wire →](https://newsroom.sgit.ai/portugal/index.html) ·
  [The graph →](https://newsroom.sgit.ai/portugal/graph.html) ·
  [Connections →](https://newsroom.sgit.ai/portugal/connections.html)
- **Databases with no server (beta)** — SQLite and a SPARQL 1.1 store running in the browser
  over the Portugal section's own JSON files, compiled to WebAssembly. The files are the
  database; the engines are readers.
  [The argument →](https://newsroom.sgit.ai/databases/index.html) ·
  [SQL →](https://newsroom.sgit.ai/databases/sql.html) ·
  [SPARQL →](https://newsroom.sgit.ai/databases/graph.html)
- **The Governance Wire (beta, fully agentic)** — seven agent roles, a nine-state workflow,
  research runs published whether or not anything resolved, and a point-and-click floor
  where each role is a desk you can talk to.
  [The wire →](https://newsroom.sgit.ai/governance/index.html) ·
  [The floor →](https://newsroom.sgit.ai/governance/newsroom/index.html)
- **pt.newsroom.sgit.ai (a brief for the next agent)** — a natively Portuguese newsroom
  mapping Portugal's AI landscape: three departments, the law, the first three articles, and
  the home-page direction chosen on 13 September.
  [Read the brief →](https://newsroom.sgit.ai/documents/pt-newsroom.html) ·
  [The home page, as designed →](https://newsroom.sgit.ai/pt-newsroom/index.html)

## This does not launch as a manifesto

Ten core articles — 68,846 words — were published on
[docs.diniscruz.ai](https://docs.diniscruz.ai) between February and October 2025, a year
before the design material behind the rest of this site was written. [The full
chronology →](https://newsroom.sgit.ai/library/index.html)

**The honest sentence:** Most of this site is an argument, not a product. Three things run — /portugal/, /databases/ and /governance/ — and each says its own limits on its face; only the first has a human editor of record, and none has had legal review. The articles in the library
are real and dated. The newsroom — the roles, the provenance pages, the payment rails,
Trust-as-a-Service — is a design. [The line between them
→](https://newsroom.sgit.ai/shipped/index.html)

## For an agent

This site argues that a story is a graph and an article is one projection of it. Nothing
here runs today — read [/shipped/](https://newsroom.sgit.ai/shipped/index.html) before
citing anything as a live capability. Published by the sgit project, which is building
the stack it argues for: read the [participant
disclosure](https://newsroom.sgit.ai/about/participant.html) before treating any page
here as neutral. [llms.txt](https://newsroom.sgit.ai/llms.txt) is the whole agent surface.
