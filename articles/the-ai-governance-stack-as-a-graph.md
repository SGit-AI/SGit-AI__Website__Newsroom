# The AI governance stack, as a graph: an answer to Hari Kota, built, sgit.ai

> Hari Kota posted The Full AI Governance Stack, ten layers from principles to people, and asked how I would structure the graph across the layers. This is the answer, built as a vault you can open. Hari's table is kept exactly as posted, every cell a node. The table already contains ten edges between layers before anything is added. Each layer is its own world with its own vocabulary, and the edges between those worlds come from the provisions themselves, so a gap is a missing edge and a missing edge is a query. Hari's three gaps and the "do this today" test run as queries on a fictional shop, and the line "most teams cover only 4 or 5" gets three honest readings.

*Source: <https://newsroom.sgit.ai/articles/the-ai-governance-stack-as-a-graph.html> · sgit.ai v0.7.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The AI governance stack, as a graph: an answer to Hari Kota, built

# The AI governance stack, as a graph: an answer to Hari Kota, built

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-09 · [article v1.1.0, 2 versions](versions/the-ai-governance-stack-as-a-graph.md) · [sgit.ai v0.7.18](https://sgit.ai/admin/versions.md) · ai-governancefractal-semantic-graphsgraphseu-ai-actiso-42001nist-ai-rmfriskinventorycompetencevaultsarticle

***Abstract:** Hari Kota posted The Full AI Governance Stack, ten layers from principles to people, and asked how I would structure the graph across the layers. This is the answer, built as a vault you can open. Hari's table is kept exactly as posted, every cell a node. The table already contains ten edges between layers before anything is added. Each layer is its own world with its own vocabulary, and the edges between those worlds come from the provisions themselves, so a gap is a missing edge and a missing edge is a query. Hari's three gaps and the "do this today" test run as queries on a fictional shop, and the line "most teams cover only 4 or 5" gets three honest readings.*

Hari Kota posted [The Full AI Governance Stack](https://lnkd.in/p/erGx6fqM) on LinkedIn: ten layers, what each does, and forty-six global examples ([quoted in full below](#hari)), under the line "10 layers. 1 global view. Most teams cover only 4 or 5." I asked in the comments whether the layers had been mapped with fractal semantic graphs, to interconnect them. Hari answered:

"I haven't mapped it that way. How would you structure the graph across the layers? What would be your take? Curious to know."

This is my take, and rather than describe it I built it. The [AI Governance Graph vault](https://sgit.ai/demos/vaults/ai-governance-graph/index.md) opens as an app with its read key published, and everything below is a view of it.

Hari's stack, exactly as posted: every layer and every example, labels unchanged. The orange edges were already in the table, because the same instrument or practice appears in more than one row. Nothing has been added yet except the lines.

**Hari's table as a graph, Mermaid source**

[rendered image](images/gg-hari-graph.webp)

```
flowchart LR
  subgraph L1["1 Principles & Policy"]
    direction TB
    e11["OECD AI Principles"]
    e12["UNESCO Recommendation"]
    e13["G7 Hiroshima Code of Conduct"]
    e14["Council of Europe AI Convention"]
  end
  subgraph L2["2 Binding Law"]
    direction TB
    e21["EU AI Act"]
    e22["China Generative AI rules"]
    e23["South Korea AI Basic Act"]
    e24["Colorado SB 26-189"]
    e25["India DPDP"]
    e26["SDAIA (Saudi)"]
  end
  subgraph L3["3 Soft Law & National Guidance"]
    direction TB
    e31["Singapore Model AI Governance Framework"]
    e32["Japan AI Guidance for Business"]
    e33["UK principles-based approach"]
    e34["UAE sectoral guidance"]
    e35["Brazil PL 2338/2023 (pending)"]
  end
  subgraph L4["4 Standards & Frameworks"]
    direction TB
    e41["ISO/IEC 42001"]
    e42["NIST AI RMF"]
    e43["ISO 31000"]
    e44["IEEE 7000 series"]
  end
  subgraph L5["5 Inventory & Intake"]
    direction TB
    e51["AI use-case register"]
    e52["owner assignment"]
    e53["Credo AI"]
    e54["Holistic AI"]
    e55["IBM watsonx.governance"]
    e56["OneTrust"]
  end
  subgraph L6["6 Risk Classification & Impact Assessment"]
    direction TB
    e61["EU AI Act risk tiers"]
    e62["AI impact assessment"]
    e63["DPIA"]
    e64["NIST MAP"]
  end
  subgraph L7["7 Technical Guardrails"]
    direction TB
    e71["Guardrails AI"]
    e72["NeMo Guardrails"]
    e73["Azure AI Content Safety"]
    e74["access controls"]
  end
  subgraph L8["8 Testing & Evaluation"]
    direction TB
    e81["AI Verify (Singapore)"]
    e82["Fairlearn"]
    e83["AIF360"]
    e84["promptfoo"]
    e85["garak"]
  end
  subgraph L9["9 Accountability & Reporting"]
    direction TB
    e91["AI committee"]
    e92["RACI"]
    e93["model cards"]
    e94["board risk reporting"]
  end
  subgraph L10["10 People & Competence"]
    direction TB
    e101["AI literacy duty (EU AI Act)"]
    e102["ISO 42001 competence requirement"]
    e103["AIGP (IAPP)"]
    e104["role-based training"]
  end
  e21 -. "same instrument" .- e61
  e21 -. "same instrument" .- e101
  e41 -. "same instrument" .- e102
  e42 -. "same framework" .- e64
  e31 -. "same regulator's toolkit" .- e81
  e52 -. "names the owner in" .- e92
  e92 -. "who is trained by" .- e104
  e63 -. "named in Art 26(9) and 27(4)" .- e21
  L1 ~~~ L2 ~~~ L3 ~~~ L4 ~~~ L5
  L6 ~~~ L7 ~~~ L8 ~~~ L9 ~~~ L10
  classDef hidden stroke-dasharray:4 3
  linkStyle 0,1,2,3,4,5,6,7 stroke:#C2410C,stroke-width:2px,color:#C2410C
```

## In short

- **Keep the stack as the view; make the graph the model.** Hari's ten layers are a great way to read governance, and the vault keeps them exactly as posted. Every cell is a node.
- **The table already contains a graph.** Before anything is added, ten edges cross the layers: the EU AI Act sits in rows 2, 6 and 10; ISO/IEC 42001 in rows 4 and 10; the NIST AI RMF in rows 4 and 6; Singapore in rows 3 and 8; the owner of row 5 is the RACI of row 9 and the training of row 10.
- **Each layer is its own world.** Law is articles and paragraphs; standards are clauses and controls; inventory is systems and owners; testing is tests and results. No layer has to adopt another's schema. They share only a grammar, so an edge can be drawn from any of them to any other.
- **The edges between worlds come from the provisions themselves.** Article 26(2) of the EU AI Act joins binding law to people; GOVERN 1.6 of the NIST AI RMF joins a framework to the inventory. 119 such edges, each citing the fact it rests on.
- **A gap is a missing edge, and a missing edge is a query.** Hari's "do this today" test, and the three gaps Hari names in layers 3, 5 and 10, run as queries anyone can read, on a fictional shop.
- **The stack is a snapshot; the graph keeps time.** Several of Hari's examples moved in 2026. The labels stay as posted and the changes sit underneath as dated edges.

## Hari's stack, exactly as posted

This is the mental model the graph has to respect, so it comes first, word for word, from the infographic and the post:

| # | Layer | What it does | Global examples |
|---|---|---|---|
| 1 | Principles & Policy | Sets the values and the internal AI policy | OECD AI Principles, UNESCO Recommendation, G7 Hiroshima Code of Conduct, Council of Europe AI Convention |
| 2 | Binding Law | Maps hard legal obligations by jurisdiction | EU AI Act, China Generative AI rules, South Korea AI Basic Act, Colorado SB 26-189, India DPDP, SDAIA (Saudi) |
| 3 | Soft Law & National Guidance | Covers regimes with guidance but no AI statute | Singapore Model AI Governance Framework, Japan AI Guidance for Business, UK principles-based approach, UAE sectoral guidance, Brazil PL 2338/2023 (pending) |
| 4 | Standards & Frameworks | Provides the management-system backbone | ISO/IEC 42001, NIST AI RMF, ISO 31000, IEEE 7000 series |
| 5 | Inventory & Intake | Tracks every AI use case and its owner | AI use-case register, owner assignment, Credo AI, Holistic AI, IBM watsonx.governance, OneTrust |
| 6 | Risk Classification & Impact Assessment | Tiers risk before deployment | EU AI Act risk tiers, AI impact assessment, DPIA, NIST MAP |
| 7 | Technical Guardrails | Enforces controls inside the system | Guardrails AI, NeMo Guardrails, Azure AI Content Safety, access controls |
| 8 | Testing & Evaluation | Tests for bias, robustness and safety | AI Verify (Singapore), Fairlearn, AIF360, promptfoo, garak |
| 9 | Accountability & Reporting | Gives the board ownership and evidence | AI committee, RACI, model cards, board risk reporting |
| 10 | People & Competence | Ensures owners are trained and accountable | AI literacy duty (EU AI Act), ISO 42001 competence requirement, AIGP (IAPP), role-based training |

The post adds the claims the graph will test: "The gaps show up in layers 3, 5 and 10. Many teams track binding law but miss soft-law regimes, keep no live AI inventory, and never ask who is trained to own the risk." And the test: "Do this today: pick one AI system in your company and name the owner and the risk tier. If you can't, you've found your gap."

In the vault this table is the first thing you see, transcribed into one input file that the release gate checks byte for byte against every node that carries Hari's words: ten layers, ten purposes, forty-six examples, the title, the subtitle, the footer and the post's claims, eighty-five nodes in all. Our additions are hidden until you ask for them.

Hari's stack, as posted, in the vault: every cell is a node you can click for its edges and its zoom. Rows 3, 5 and 10 are marked because the post marks them.

## The table already contains a graph

Read a table and every example lives in exactly one row, so the EU AI Act looks like a layer 2 thing. Read it as a graph and the table turns out to say more than its rows do. Where two rows name the same instrument, role or jurisdiction, they share a node one level down, and that shared node is an edge across layers that Hari's table already contained:

- **EU AI Act** (row 2) shares an instrument with **EU AI Act risk tiers** (row 6) and with **AI literacy duty (EU AI Act)** (row 10); the risk tiers and the literacy duty share it with each other.
- **EU AI Act** (row 2) cites the **DPIA** of row 6: deployers use the provider's information "to comply with their obligation to carry out a data protection impact assessment under Article 35 of Regulation (EU) 2016/679" (Article 26(9)), and the fundamental rights impact assessment now cross-references it (Article 27(4), as amended in 2026).
- **ISO/IEC 42001** (row 4) shares an instrument with **ISO 42001 competence requirement** (row 10).
- **NIST AI RMF** (row 4) shares an instrument with **NIST MAP** (row 6).
- **Singapore Model AI Governance Framework** (row 3) shares a jurisdiction with **AI Verify (Singapore)** (row 8): a soft-law regime that ships its own testing toolkit.
- **owner assignment** (row 5) names the same role as **RACI** (row 9) and **role-based training** (row 10), and those two name it to each other.

Ten edges, and none of them is ours. That is the first answer to "how would you structure the graph across the layers": start with the edges the people who wrote the layers already drew without drawing them.

The same table as a graph: forty-six example nodes in Hari's ten rows, and the ten curves the table already contained. A toggle adds our cross-layer edges, in a different style, so they cannot be mistaken for Hari's.

## Each layer is its own world

The second answer is the fractal part, and it is the part that makes the rest workable. Each layer gets its own ontology, in its own owners' vocabulary. Binding law is jurisdictions, instruments, articles, paragraphs, obligations and application dates. Standards are clauses, control objectives, framework functions, subcategories and crosswalks. Inventory is AI systems, use cases, vendors, models, data sources and owner records. Testing is tests, metrics, results and tools. Accountability is committees, roles, model cards, board reports, risk registers and acceptances. People are roles, training, certifications and competence evidence.

None of those worlds is asked to fit the others. A lawyer's graph of the EU AI Act should look like the Act, and in the [Regulation Graph](https://sgit.ai/demos/vaults/regulation-graph/index.md) vault it does: parsed from the official XML, article by article. A risk team's register should look like a register. What the worlds share is only the grammar from [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md), five rules:

1. Every edge is a verb, stated in both directions, with an inverse a person would say: a provision `requires` a record, the record `is_required_by` the provision.
2. `relates_to` is banned, along with every verb that means nothing. The gate refuses them.
3. Properties carry data, never meaning.
4. Supersede, never delete.
5. Never render the whole graph: render the answer to a question.

The vault has ninety-one verbs, each with its inverse, in one file. Every view opens with the question it answers.

Each layer's world: its own node types and verbs, with the five grammar rules that every world shares.

## The edges between worlds come from the provisions

The third answer is where our additions start, and the rule for them is that each one must rest on a provision someone can read. Some of the strongest:

- **Binding law to people.** Article 26(2) of the EU AI Act: "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support." One sentence, and it joins layer 2 to layer 10, for a system in layer 5 whose tier came from layer 6.
- **Binding law to people, again, reworded.** Article 4 on AI literacy, as replaced in July 2026 by [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng): providers and deployers "shall take measures to support the development of AI literacy of their staff". The 2024 wording stays in the graph, struck through.
- **Binding law to risk classification.** Article 6 with Annex III. Point 4(a) covers "AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates".
- **Framework to inventory.** NIST AI RMF GOVERN 1.6: "Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities." This is the clearest anchor I found for Hari's layer 5.
- **Standard to people.** ISO/IEC 42001 clause 7.2, Competence, which NIST's own [crosswalk](https://airc.nist.gov/airmf-resources/crosswalks/) maps to GOVERN 2.2, training.
- **Standard to standard.** NIST publishes thirteen official crosswalks, including the AI RMF to ISO/IEC 42001 and to AI Verify: edges between layer 4 and layers 4 and 8 that somebody already wrote down.

Counted, the knowledge graph has 329 edges, 140 of them between layers: the ten from Hari's table, eleven from what Hari's labels name, and 119 of ours, every one citing the fact it rests on and marked as an addition. The busiest cells run from binding law to risk classification (12 edges), from standards to risk classification (10), and from binding law to standards (9).

Between the layers: every edge counted by the layer it starts in and the layer it ends in. Click a cell for its edges, each with its provision, quote and source.

Read per instrument, the same count says something the table cannot. In Hari's table the EU AI Act is one example in row 2. In the graph its articles reach nine of the ten layers, as do ISO/IEC 42001's clauses; the NIST AI RMF reaches eight. That is the argument for a graph in a single row of a table.

One row of the table, many layers of the graph. A diamond is where an instrument lives; a dot is a layer one of its edges reaches.

## Zoom from one cell down

Put the three together and the walk looks like this. Three of Hari's cells name the same instrument. Open it and its provisions appear. Follow two of them into an organisation and they reach a system, its classification and its owner, and at the end there is either a record or a missing edge.

Zoom from one cell of Hari's table to one missing edge. Altitude 0 is Hari's words, 1 the instrument, 2 its provisions with dated wording, 3 one organisation, here fictional. The orange edge is the gap.

**The zoom, Mermaid source**

[rendered image](images/gg-zoom.webp)

```
flowchart LR
  subgraph A0["Altitude 0: Hari's table, as posted"]
    direction TB
    H2["row 2 · EU AI Act"]
    H6["row 6 · EU AI Act risk tiers"]
    H10["row 10 · AI literacy duty (EU AI Act)"]
  end
  subgraph A1["Altitude 1: the instrument"]
    R["Regulation (EU) 2024/1689<br/>amended by 2026/1744"]
  end
  subgraph A2["Altitude 2: provisions"]
    direction TB
    P4["Art 4 · AI literacy<br/>as reworded in 2026"]
    P26["Art 26(2) · oversight by persons with<br/>competence, training and authority"]
    PA["Annex III 4(a) · recruitment<br/>or selection"]
  end
  subgraph A3["Altitude 3: Hollow Oak Home, fictional"]
    direction TB
    SYS["CV screening assistant · layer 5"]
    CL["classification · layer 6<br/>assigns: high-risk"]
    HR["HR Lead · owner and overseer · layer 10"]
    TR["training or competence record"]
  end
  RG["Regulation Graph vault<br/>the Act parsed from official XML"]
  H2 -- "refers_to" --> R
  H6 -- "refers_to" --> R
  H10 -- "refers_to" --> P4
  R -- "has_part" --> P26
  R -- "has_part" --> PA
  R -- "is_detailed_in" --> RG
  SYS -- "is_classified_in" --> CL
  CL -- "is_made_on_the_basis_of" --> PA
  SYS -- "is_owned_by, is_overseen_by" --> HR
  P26 -- "applies_to" --> SYS
  P4 -- "applies_to" --> SYS
  HR -. "has_completed: missing" .-> TR
  style TR stroke:#C2410C,stroke-width:2px,stroke-dasharray:5 4,color:#C2410C
  linkStyle 11 stroke:#C2410C,stroke-width:2px,color:#C2410C
```

Every deeper node keeps a breadcrumb back to the cell of Hari's table it came from, so whoever is reading always knows which part of the original model they are standing under. And the instrument node does not have to hold the whole Act: it `is_detailed_in` the Regulation Graph vault, which does. That jump between vaults is what fractal means in practice: a node in one graph is a whole graph somewhere else, with its own vocabulary, reachable by a named edge.

## The stack is a snapshot; the graph keeps time

The research behind the vault checked every one of Hari's forty-six examples on 9 October 2026, and several had moved during 2026. The EU AI Act was amended by Regulation (EU) 2026/1744, in force from 27 July: the Annex III high-risk obligations now apply from 2 December 2027 and Annex I from 2 August 2028, and Article 4 was reworded. Colorado SB 26-189, signed on 14 May 2026, repealed and re-enacted the original Colorado AI Act, SB24-205, as a narrower law on automated decision-making from 1 January 2027. Japan passed an AI Promotion Act in 2025 and is on version 1.2 of its AI Guidelines for Business. promptfoo became part of OpenAI in March 2026 and remains open source.

None of that makes the table wrong: it names SB 26-189, which is exactly the current law. It shows what a table cannot do. A table is correct on the day it is drawn. A graph keeps the label as posted, puts the instrument underneath, and records each change as a dated edge (`was_amended_by`, `repeals_and_replaces`, `supersedes`) with the old value kept and struck through. Ask "what changed under row 2 this year?" and it is a query. The neutral notes, one per example where we used something more specific than the label, are in the vault's `docs/sources-notes.md`.

## Do this today, as a traversal

Hari's test is the best line in the post, because it is a query in disguise: for a system, follow `is_owned_by` to a person, follow `is_classified_in` to a classification, which `assigns` a tier and `is_made_on_the_basis_of` a provision. If either path ends early, that is the gap.

To run it on something I invented an organisation, deliberately: Hollow Oak Home, the online homeware shop from the [Hope or enforcement](https://sgit.ai/demos/vaults/hope-or-enforcement/index.md) vault, with eight AI systems, three jurisdictions (the UK, the EU and Singapore) and roles rather than names. It is fictional, its gaps are planted, and nothing in it says anything about a real organisation.

Five of the eight systems pass: an owner and a tier with its basis. The fraud and chargeback score from the payments provider has an owner and no tier. The demand forecasting model has a tier and no owner. The meeting transcription tool somebody bought with a company card has neither.

The more interesting result is a system that passes. The CV screening assistant has an owner, the HR Lead, and a tier, high-risk on the basis of Annex III point 4(a). Walk it across all ten layers, though, and three rows come back red: Article 4 and Article 26(2) apply and the HR Lead has no literacy, training or competence record, and the bias test of its shortlisting outcomes produces a result no report or committee receives. Hari's test is the right first question. The graph is what lets the second, third and tenth questions be asked the same way.

Do this today for the CV screening assistant: the owner and the tier pass, and the walk across ten layers finds three missing edges, in layers 2, 9 and 10.

## Hari's three gaps, as queries

Each of the gaps Hari names becomes a query with a plain question, a traversal written out step by step, and a result:

- **Layer 3, soft law that no role tracks.** Start at each jurisdiction that a guidance document `is_issued_in`; keep the ones where a system `is_deployed_in`; report those with no `is_tracked_by` edge to a role. For Hollow Oak Home: Singapore, where the demand forecast and the transcription tool are used, with three Model AI Governance Frameworks in the graph and no role tracking them.
- **Layer 5, no live inventory.** Start at each system that `was_found_in` a piece of evidence (expenses, sign-ins, code); report those the register does not record. Result: the meeting transcription tool, found in the September expenses review.
- **Layer 10, owners without training.** Start at each system whose classification assigns the high-risk tier; follow `is_owned_by` and `is_overseen_by` to roles; report roles with no training or competence record. Result: the HR Lead, with Article 4 and Article 26(2) as the provisions that require it.

Four more follow the same pattern: obligations with nothing meeting them, guardrails with no test, test results that reach no report, and the instruments that reach many layers.

The gaps as queries: Hari's three first, each with the claim it tests, the traversal and the result.

## What "4 or 5" means in a graph

"Most teams cover only 4 or 5" is a good provocation, and in a graph it splits into three questions with three different answers. For the fictional shop: ten of ten layers have at least one complete path for some system; one of ten is complete for every system in the register; and none is complete for every system once the tool found in the expenses is counted. Per system, the layers answered are 10, 7, 10, 4, 6, 9, 0 and 9 of ten.

So "covering a layer" is not one thing. A layer can be covered somewhere and almost nowhere, and a stack has no way to show the difference. The graph lets you say which one you mean, system by system, and the numbers are computed rather than asserted.

## Bring your own

The last view is the one I would start with if I were Hari's reader. Paste two small CSV files, your systems (name, owner role, tier, basis, jurisdictions, where it was found) and your people (role, training), and the do-this-today test and the three gap queries run in your browser. Nothing is sent anywhere and the vault is never written. The templates hold Hollow Oak Home's data as the example.

Bring your own: two CSV inputs and the same queries, computed locally.

## How the vault is built, and what it does not claim

One model script writes every data file: 335 nodes, 702 edges, one ontology per layer, and exports as CSV, JSON-LD and Turtle. Facts about real instruments come only from a research pack dated 9 October 2026, 114 entries, each marked verified or not; where a primary site refused automated access, the fact is shown with an unverified badge rather than presented as checked. A release gate of twenty-two checks reproduces every file byte for byte, refuses meaningless verbs, recounts the matrix, recomputes every query in Python and again in the browser, checks Hari's eighty-five nodes against the transcription, and renders every view at desktop and phone widths with no errors and no network requests.

It is a method and a worked example. Hollow Oak Home is fictional. Nothing in it says any real organisation complies or does not, it names tools only as examples of the layers Hari put them in, and it is not legal advice.

## Prior art

The idea of mapping AI law to standards as a graph is not new, and the vault leans on work that came first. Julio Hernandez, Delaram Golpayegani and Dave Lewis proposed [an open knowledge graph for mapping the EU AI Act to international standards](https://arxiv.org/abs/2408.11925) in 2024. The [AI Risk Ontology (AIRO)](https://w3id.org/AIRO) and the W3C Data Privacy Vocabularies community's [AI extension](https://www.w3.org/community/reports/dpvcg/CG-FINAL-ai-20240801/) give vocabularies for AI systems, risks and the Act. NIST's [crosswalks](https://airc.nist.gov/airmf-resources/crosswalks/) are, in effect, published edges between frameworks. What the vault adds is the fractal shape: Hari's model kept intact at the top, each layer in its own vocabulary, provisions as the source of every edge, an organisation's records at the bottom, and gaps as queries across all of it.

## Open it

- The vault, with its read key: [AI Governance Graph](https://sgit.ai/demos/vaults/ai-governance-graph/index.md). From the command line: `sgit clone sgit_public_read_0a899b9e46ba92b1c2625ef911cbff307814fd3e1abf8a5fa1cf8a31045a01b9:1wp3xpf4`
- The method: [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md), and the same method applied to code in [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md).
- The EU AI Act itself, as a graph: [Regulation Graph](https://sgit.ai/demos/vaults/regulation-graph/index.md); an open control framework, as a graph: [AI BCF as a graph](https://sgit.ai/demos/vaults/aibcf-graph/index.md).

Hari, thank you for the question. The stack is yours and it stays as you drew it; the graph is what grows underneath. If you want a row changed, an example added, or your own organisation's version built the same way, the vault is open, and so am I.

*Written from the comment thread under Hari Kota's LinkedIn post [The Full AI Governance Stack](https://lnkd.in/p/erGx6fqM) (October 2026), whose table is quoted exactly. Researched, built and written by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, for Dinis Cruz, who has editorial responsibility. Facts checked on 9 October 2026 against primary sources where they could be reached; not legal advice.*

## Threads

Graphs & knowledgeAgents & policy[This article as a graph →](graphs.md#the-ai-governance-stack-as-a-graph)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [the-ai-governance-stack-as-a-graph.jpg](banners/the-ai-governance-stack-as-a-graph.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-ai-governance-stack-as-a-graph.html)*
