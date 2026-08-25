# 09 — The Risk & Governance Newsroom

**Kind:** Commissioning brief — a publication to build, not a description of what this site already is
**Pack:** `newsroom.sgit.ai` brief pack **v1.1 addendum** · 25 August 2026
**Type:** Strategy + dev brief
**To:** Strategy, @Content, @Dev, Librarian, Ontologist
**Target:** a daily risk-and-governance publication, assembled from the `*.sgit.ai` network, whose commercial destination is **RiskMandate.ai**

**Sources.** `newsroom.sgit.ai` v0.2.4 · `graphs.sgit.ai` v0.4.27 · `risks.sgit.ai` v0.1.0 · `pki.sgit.ai` v0.1.26 · `sgit.ai` (vault layer) · `riskmandate.ai` · `the-cyber-boardroom/SGraph-AI__App__Send` @ v0.33.62, principally the 23 June persona brief, the 26 June vision capstone and the 30 June library brief.

> ⚠️ **Every figure below attributed to a sibling site is as that site's own agent surface stated it on 25 August 2026.** Per this site's own standing rule, a fact about a sibling must be re-checked against that site's repository before it is repeated. Re-verify at build time; do not inherit these numbers from this document.

---

## 0. The one-paragraph brief

Build a daily publication that covers **risk, governance and accountability in autonomous systems** — the regulation, the enforcement, the guidance, the named people who sign. It is a news operation, not a content-marketing channel: it runs on this site's editorial model (story-as-graph, article-as-projection, corrections propagate, provenance is the product), it is produced by an agentic newsroom with humans as the bar, and every claim it publishes is anchored, signed, dated and expiring. Its structural advantage over any other publication on this beat is that **the graph it would need already exists** — 1,523 nodes of parsed regulation, three worked risk graphs and a 42-concept published ontology, built by sibling sites before the publication has written a word. Its commercial function is not to advertise RiskMandate.ai but to be the thing RiskMandate.ai cannot compute without: **a supply of grounded, signed, public Facts about the regulatory world**, to which a customer attaches their own private systems. The publication sells the graph; the product sells the join.

**The inversion is held.** This site's `06__boundaries-and-house-style.md` §1 states that risk management is *one customer* of the future-of-news stack, not its parent. This brief is the reciprocal statement the network page promises — *this is what the same machinery looks like pointed at corporate risk* — and it is written that way round. A news operation whose first customer is a risk product. Not a risk product with a blog.

---

## 1. Why this beat: the graph is already built

The [Portugal instance](../mvps/portugal.html) established the scoping criterion for a publication MVP, and it is the right one:

> The Portuguese GenAI scene is **small enough to map comprehensively and large enough to be interesting.**

Portugal's acceptance criteria required an entity graph of **≥200 entities** seeded before the publication could report competently on its beat. That graph was never built and the publication never launched. **That is the precedent this brief has to beat, and the reason to think it can is that the equivalent graph for this beat is already public.**

| Asset | State | Owner |
|---|---|---|
| **EU AI Act regulation graph** — 1,523 nodes · 1,944 edges, parsed from official Formex XML, SHA-256 verification at every provenance point, RDF/Turtle export, 11 fractal views | Published, live | graphs.sgit.ai |
| **Two-factor authentication risk graph** — 51 nodes · 53 edges, 24 node classes, 34 edge types, MITRE T1110.004 | Published, live | graphs / risks |
| **Agentic browser isolation risk graph** — 59 nodes · 75 edges, five altitudes, **three risks created by the mitigation itself** | Published, live | graphs / risks |
| **Article 26(5) case study** — 8 facts, 5 risks, 9 questions of which **5 unanswered**; finds 30 days retention against a six-month minimum | Published, live | risks.sgit.ai |
| **The risk ontology** — 42 concepts, stable anchors, machine-readable at `/data/concepts.json` | Published, v0.1.0 | risks.sgit.ai |
| **Published vaults** — 4 vaults, 468 files, 111 commits, read keys public | Published | risks / sgit.ai |

**Portugal needed 200 entities before day one and never got them. This publication starts at 1,523 with a published ontology and four readable vaults.** The beat also passes the closability test on its own terms: the corpus of binding text on autonomous-systems governance is finite, the regulators are countable, and the enforcement record is short enough to map exhaustively and long enough to be worth mapping.

There is a second reason for the timing, and it is the better story. This site already publishes [a worked example of the beat's central failure](../corrections/staleness-in-the-wild.html): Regulation (EU) 2026/1744 was adopted 8 July 2026 and entered into force 27 July 2026, and **its official consolidated text is dated 12 July 2024 and incorporates nothing since.** A reader following the official source is reading a document that predates entry into force by over a year. The publication's founding beat is a domain where the primary sources are demonstrably, checkably stale — which is the condition under which a graph-backed publication is not a nicety but the only thing that works.

---

## 2. What each property supplies

The publication is an assembly, not an invention. Each row is a capability that already has an owner, a published specification and a boundary.

| Property | What it supplies to this publication |
|---|---|
| **newsroom.sgit.ai** | The editorial model. The story is a graph; the article is a projection. Corrections must propagate. Provenance is the product — 15 public departments, 8 scoped for a first MVP. The per-story cost ledger (£8.40, 6h 23m). The 60/25/10/5 upstream split. The provenance contract of `02__source-provenance-and-attribution.md` and its enforcing gate. |
| **graphs.sgit.ai** | The fractal semantic graph machinery. **One grammar, one validator, one provenance rule at every altitude** — zoom into any node and the same rules apply. Node-type formulas, so classification is a queryable, arguable formula rather than a classifier's opinion. The grounding ladder. Supersede-never-delete. The Universe layer's **byte-offset anchoring against frozen source bytes**. The EU AI Act graph itself. |
| **risks.sgit.ai** | The risk ontology and the editorial spine. **No deny button.** The interval ladder (1h / 4h / 1–2d / 1–2w / 1m / 6m). Acceptance as underwriting by a named person. Accepted ≠ acceptable. **Absence as fact** — missing evidence is countable and assignable. Blast radius and recoverability. |
| **pki.sgit.ai** | Signed claims. **Identity and mandate as two separate signed statements.** The four registry rules. Revocation as a signed append rather than a deletion. Shipped keys in sgit v0.16.0+ (RSA-OAEP 4096, ECDSA P-256). |
| **sgit vault** | The substrate. Zero-knowledge, client-side encryption, keys held by the endpoints. A vault per story. Commit DAG with SHA-256 object IDs. **Typed `.link.json` cross-vault edges** — the mechanism §5.3 depends on entirely. Read keys published, write keys never. |
| **MyFeeds** | The projection layer, already proven as a running pipeline. One story, many audience projections; per-reader briefings; the B2B research briefing as a delivered evidence pack. |
| **RiskMandate.ai** | The customer, the commercial destination, and the persona cast the projections are cut against. |

---

## 3. The architectural claim: who owns which rung

This is the load-bearing section. Everything commercial in this brief follows from it.

`risks.sgit.ai` publishes the grounding ladder as concept C6:

> **Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk.** Downward paths ground; upward paths classify.

and defines node types as path formulas rather than descriptions (C7), the canonical example being:

> `Vulnerability := a Fact that also has an upward gives_rise_to path to a Risk`

Read that formula commercially and the division of labour falls out of it:

| Rung | Owner | Why |
|---|---|---|
| **Reality · Twin · Measure** | **The customer.** Their systems, their agents, their configuration, their people. | Private by necessity. Zero-knowledge vault; the customer holds the keys. Nobody else can supply it and nobody else should hold it. |
| **Evidence · Fact** | **The publication.** What the regulation says, what changed, what a regulator did, what is unanswered. | Public by nature. This is journalism. It is the same work for every reader, so it should be done once, in the open, and paid for upstream. |
| **Vulnerability · Risk** | **RiskMandate.ai**, computed at the join. | By the published formula a Vulnerability *is* a Fact with an upward path to a Risk — and that path only comes into existence when a public Fact meets a private Twin. It cannot be computed from either side alone. |

**That is why the publication is commercially load-bearing rather than promotional.** The product cannot compute a Vulnerability without a supply of grounded public Facts. Today that supply is a human reading a PDF. The publication is the proposal to make it a signed, dated, machine-readable graph.

It is also the reciprocal of a boundary the sibling already publishes: `risks.sgit.ai` explicitly does not own `newsroom.sgit.ai`, and names its relationship to it in two words — **evidence supply**. This brief is that phrase taken seriously enough to staff.

---

## 4. The story is a risk graph

The Portugal instance gave every story its own vault holding sources, evidence, drafts, graph and projections. Two folders in that layout — `evidence/disputed.json` and `evidence/contradictions.md` — existed so that disagreement between sources was *stored rather than resolved away*.

This publication keeps that layout and makes one change with large consequences: **the story's graph is built to the published risk ontology, at the same altitudes, with the same node-type formulas.**

```
story-{date}-{slug}/
├── brief.md                    what this story is, why it matters
├── sources/
│   ├── frozen/                 source bytes, hashed, never edited
│   └── coverage/               how others reported it
├── anchors/
│   └── anchors.json            every quoted provision → byte offset in sources/frozen/
├── graph/
│   ├── facts.json              Fact and Evidence nodes — the publication's own rungs
│   ├── absence.json            enumerated unanswered questions, each assignable
│   ├── formulas.json           the node-type formulas this story classifies under
│   └── supersedes.json         what this story's facts replace, and what cited them
├── assessment/
│   ├── claim.md                the assessment, if the story makes one
│   ├── mandate.jws             the signed mandate the by-line asserts under
│   └── interval.json           accepted-until, and by whom, by name
├── projections/                per-persona renderings (see §8)
└── _page.json
```

A news story about a regulatory change and a risk-register entry are, under this layout, **the same object type at different altitudes**. That is the fractal claim from `graphs.sgit.ai` — *one grammar, one validator, one provenance rule at every altitude* — applied to the boundary between a publication and its readers' registers. It is what makes §5.3 possible at all.

One discipline is inherited without modification, from the RiskMandate vision capstone, and it is the thing that keeps this from becoming threat-modelling with a masthead:

> Everything must be real.

Phase one admits **facts only**. No speculative risk, no scored scenario, no "could conceivably". A publication that inherits the register's anti-speculation rule is a publication that cannot inflate its own beat — see §10, where this is the mitigation that has to do the real work.

---

## 5. Four formats nobody else publishes

The case for the publication is not that it covers this beat better. It is that four editorial products fall out of the stack that a conventional outlet structurally cannot produce.

### 5.1 The absence report

`risks.sgit.ai` concept C17 makes missing evidence a first-class node: **absence is a fact — countable, assignable, and productive.** The Article 26(5) case study is the worked example, and its finding is the format's whole argument: nine questions asked, five unanswered, and **the unanswered five are the exercise's actual output.**

No newsroom publishes this. An article that ends "the regulator did not respond to questions" is a failure state; an **absence report** is a deliverable — an enumerated, dated, individually-assignable list of what a regulation does not determine, published as nodes rather than as a closing paragraph.

It is also the cheapest format to produce, the hardest to fabricate, and the one that converts best: an unanswered question is an unpriceable risk, and an unpriceable risk is a standing reason to hold a tool that tracks it.

### 5.2 The staleness wire

`graphs.sgit.ai` anchors nodes to verbatim quotes at byte offsets in frozen source documents, and **fails the build if the quotes no longer match the frozen source bytes.** Point that mechanism at live regulatory sources and it stops being a build gate and becomes a wire service.

The publication anchors every provision it quotes to a byte offset in a hashed copy. When the upstream source changes, the anchor breaks. **The broken anchor is the story** — and it fires without a human noticing, without a press release, and without the publisher of the changed text choosing to announce it.

This site already publishes [the three states of staleness](../corrections/staleness-in-the-wild.html): *current and correct*, *stale but was once true*, and **never was the law** — a pre-adoption negotiating draft presented without the caveat that it never had legal force, which the site notes is "worse than stale because it never was the law", and which at least one public source in circulation currently is. Those three states become a machine-assignable label carried by every source the publication cites, and the Article 10 probe becomes a repeatable test rather than a one-off observation.

### 5.3 The correction that reaches the register

This is the feature no GRC platform has, and it is a direct consequence of this site's founding argument rather than an add-on to it.

The vault layer supports **typed `.link.json` cross-vault edges**. A customer's private register can therefore hold a typed edge into a public Fact node in the publication's vault. When the publication supersedes that Fact — never deleting, always superseding, per the graph rule — every register holding an edge into it **knows**.

> In a document, a correction is a new document. Nothing that cited the original knows.

That sentence is why this site exists. Pointed at corporate risk it reads: *a regulatory change stops being an email somebody has to notice and becomes an invalidated edge that announces itself.* The [242-paper citation network](../corrections/242-papers.html) is the measured version of the failure this avoids — one belief, 675 citations, more than 220,000 supporting citation paths, tracing back to nothing, with no mechanism by which the correction could ever have reached them.

### 5.4 The assessment that expires

The interval ladder is a publishing mechanic as much as a governance one. Every assessment the publication makes carries an **interval and a named underwriter**: accepted for an hour, four hours, two days, two weeks, a month, six months — chosen by volatility and consequence, not by convenience. At expiry the assessment returns for re-underwriting or is marked lapsed in place.

**A publication whose articles expire on a schedule, and say so on their face.** Set that against the story this site opens with: a 1993 finding, popularised as something it never said, which the original researcher spent his career correcting, and *none of it ever attached to the claim*. The interval ladder is the mechanism that makes that specific failure structurally impossible — not because someone remembers to revisit, but because the claim stops being current on a date it named in advance.

---

## 6. The by-line is a signed mandate

The [Portugal instance](../mvps/portugal.html#open) left six questions open. Question 5 is the one this site has said it should be least comfortable about:

> **Editorial accountability** — who is the editor of record, and who carries legal responsibility for published content. *No candidate is named.*

This stack answers the editorial half of it, and the answer is not a masthead.

`pki.sgit.ai` separates two signed statements that are usually conflated: **identity** ("this key belongs to this agent") and **mandate** ("this agent may perform X actions until date Y, on whose authority"). Combine that with underwriting-by-interval and a by-line becomes a compound, checkable object:

| Component | Statement | Signed by |
|---|---|---|
| **Identity** | This key belongs to this analyst or this agent | The holder |
| **Mandate** | This holder may assert claims of this class, until this date, on this authority | The publication |
| **Underwriting** | This assessment is accepted by this named person until this date | The underwriter |

**The editor of record is whoever's signature is on the current interval.** Not a title held permanently, but a dated act that expires and must be repeated. Revocation is a signed append rather than a deletion, so the record of who stood behind a claim survives their ceasing to stand behind it — which is exactly what a reader auditing an old story needs and never gets.

**What this does not answer, stated plainly.** `pki.sgit.ai` is explicit that a signed mandate constrains *authorisation, not execution*, and that a registry cannot verify a key remains in its holder's sole possession — that needs attestation, which "neither keys nor vaults supply". The shipped PKI in sgit v0.16.0+ documents itself as having **no revocation and no directory**; the registry is a static-file MVP. And none of this touches the legal half of Portugal's question 5: **who is answerable in a jurisdiction for a defamatory or negligent publication.** A signature is evidence of who asserted something. It is not a legal person, and it is not a defence. That half stays open — see §14, Q1.

---

## 7. The newsroom

Eleven roles, adapted from the Portugal design. Three are new and specific to this beat.

| Role | Function | New? |
|---|---|---|
| **Conductor** | Sets the day's priorities, allocates stories | |
| **Researcher** | Continuous monitoring of named regulators, registers, enforcement feeds | |
| **Anchor keeper** | Maintains frozen sources and byte-offset anchors; owns the staleness wire (§5.2) | **New** |
| **Verifier** | Cross-references, flags uncertainty, builds the Evidence set alongside the draft | |
| **Ontologist** | Owns the story's own ontology and its bridges to the shared one | |
| **Formula keeper** | Owns the node-type formulas the publication classifies under; publishes every change to them as a change, because a reclassification is a correction | **New** |
| **Writer** | Drafts against the evidence set, citing into it | |
| **Editor** | Style, clarity, length, missing context | |
| **Underwriter** | The named human who accepts each assessment for an interval (§6) | **New** |
| **Visual** | Infographics generated from the story's own graph | |
| **Projectionist** | Generates the per-persona renderings (§8) | |
| **Community** | Monitors response, routes reader challenges to facts as first-class inputs | |

The 30 June library brief named almost this cast for the RiskMandate library, and its reasoning transfers intact — *"the librarian, a good historian, a good journalist, good content writers, and maybe a whole set of agents focusing on information design, structure, and presentation, including how to represent the semantic graphs, and the ontologists"* — because **"each of these articles is its own world, its own ontology and taxonomy, with a lot of reuse, and it is a good example of graphs of graphs of graphs."** That is the fractal claim arriving from the commercial side independently, and it is the reason the Ontologist is a standing role rather than a shared service.

The daily clock is inherited from Portugal unchanged, including the one structural detail worth preserving: **writer and verifier work in parallel, not in sequence**, so a story that skipped verification is visibly missing its evidence rather than merely unchecked. One addition — a **decay pass** runs before the morning conference: every assessment whose interval expires today surfaces for re-underwriting or lapse, and lapses are published as such.

Humans are the bar; agents are the volume.

---

## 8. The commercial path

The persona brief settles the audience, and its central observation is that the cast is **fractal**:

> Everyone who uses AI also has to sell it. *"You use AI for something, and you have to sell it, usually upward or outward… so you start to have this very rich graph."*

The same roles recur at every company in the chain — the one using AI, the one building it, the one selling it, the one buying it. For a publication that is not a marketing insight, it is a **projection specification**: one story, cut for the CEO, the CSO, the CIO, the CFO, legal counsel, the GRC team, the buying business function, the internal dev team, the third-party vendor, and the chief revenue officer. Legal counsel is flagged in the source as *"often the real decision-maker"* and is the projection to get right first.

That is the MyFeeds layer doing exactly the work it was built for, on a beat where the same fact genuinely means different things to different readers.

**The funnel, stated as a mechanism rather than a hope:**

| Layer | What it is | Price |
|---|---|---|
| **The public graph** | Every Fact, every absence, every staleness alert, every superseded claim. CC BY, indexed, citable, agent-readable. | Free |
| **The projection** | The same story cut for one persona; the per-reader briefing. | Free → subscription |
| **The join** | The customer's private vault holds typed edges into the publication's public Fact nodes. Corrections propagate inward. | **The product** |
| **Certification** | A warranted, signed assertion that a named fact was correct at a named date, with a named underwriter. [Trust-as-a-Service](../economics/trust-as-a-service.html). | Per assertion |

**The conversion event is not a demo request. It is a `.link.json` edge.** The moment a reader's register cites the publication's graph, the publication is infrastructure rather than content, and the relationship is measurable in edges rather than in attributed pipeline.

Upstream payment follows this site's published 60/25/10/5 split, and the fact-creator argument applies to the publication's own contributors before it applies to anyone else's — a publication arguing that the fact creator should be paid, which does not pay its own, has refuted itself the same way losing its provenance chain would.

---

## 9. Boundaries — what this publication must not re-explain

The largest risk to this brief is the same one `06__boundaries-and-house-style.md` names for this site: **duplication, not scarcity.**

| Sibling | Owns | This publication may |
|---|---|---|
| **risks.sgit.ai** | The risk ontology, the acceptance mechanic, the interval ladder, the 42 concepts | **Use and cite.** Never restate the ontology in its own words — a second definition is a fork |
| **graphs.sgit.ai** | The grammar, the validator, node-type formulas, the grounding ladder, anchoring | **Use and cite.** Zero words explaining how the graph works |
| **pki.sgit.ai** | Keys, registry rules, identity-vs-mandate, revocation | **Use and cite.** Never describe a signing scheme of its own |
| **sgit.ai** | Vaults, substrate, publishing, CI, `.link.json` | **Use and cite.** Zero words on storage, hosting or loaders |
| **sg-sentinel.sgit.ai** | In-line enforcement | Out of scope. This publication measures and reports; it does not enforce |
| **RiskMandate.ai** | The commercial product | **Cite, never speak for.** The publication reports on the beat; the product is a customer of its output. A publication that announces its customer's roadmap is that customer's newsletter |

**The publication owns exactly one thing:** the editorial operation that turns public regulatory reality into a signed, dated, superseding evidence supply. That is a real job, nobody else in the network has it, and it is enough.

---

## 10. Editorial independence: the tension that breaks this if it is not designed for

State it without softening. **A publication whose commercial purpose is to sell a risk product has a structural incentive to report risk as more severe, more urgent and more numerous than it is.** Every reader will see that immediately, most will discount the publication for it, and they will be right to unless the incentive is answered structurally rather than promised away. The source corpus knows this — the 17 May MyFeeds repositioning brief contains a dual-track editorial-independence discussion, which is Tier 3 and not reproduced here, but the concern is live in the material and predates this brief.

Promises are worthless here. These are the four answers that are structural:

1. **Severity is computed, not asserted.** `graphs.sgit.ai` makes confidence a function of connectivity — it "runs from no edges to rich multi-hop connectivity", and the remedy for low confidence is **enrichment, never enforcement**. A publication whose severity comes from edge count cannot inflate a story by writing more forcefully; it can only inflate it by fabricating edges, which are signed, dated and auditable by the reader.
2. **Facts only, phase one.** Inherited unmodified from the register (§4). No speculative risk enters the graph. This is the rule that stops a commercially-motivated newsroom from manufacturing its own demand, and it is already published as the product's own discipline, so relaxing it for the publication would be visible.
3. **The absence report is the counterweight.** §5.1's output is *questions*, not severity. A newsroom whose flagship format's deliverable is an enumerated list of things nobody knows is structurally biased toward admitting uncertainty rather than resolving it upward.
4. **The agenda is published.** This site already publishes [the graph has an agenda too](../corrections/agenda-is-context.html) as a self-critique of its own central mechanism. The publication inherits that page and extends it with its commercial relationship stated on its face, alongside the [participant disclosure](../about/participant.html) convention every site in the network already carries.

**And one hard editorial rule, proposed here and load-bearing.** The RiskMandate vision names *"worked, evidence-backed assessments of real platforms"* as **"the proof that travels"**. That is commercially correct and editorially the single most dangerous thing in this brief: it is a plan to publish adverse assessments of named third parties, produced by an organisation that profits when those assessments land. The rule:

> **No severity assessment of a named third party's product is published without that party's right of reply recorded in the same vault, at the same altitude, and reachable from the same node.**

Not a quote in the last paragraph. A node in the graph, with the same anchoring and the same signature requirements as the assessment it answers. If the party declines, the declining is recorded as an absence fact per §5.1 — which is both fairer and more informative than "did not respond to a request for comment".

---

## 11. Honest limits — what does not exist

This site's [shipped page](../shipped/index.html) is the authority, and this brief adds to what it lists rather than qualifying it.

| Limit | Stated by |
|---|---|
| **The risk engine does not exist.** *"All items below are PROPOSED. None have been code-verified. The implementing engine does NOT exist"* — zero repository matches for `risk_`, `RiskAcceptance` or `risk_register`. Everything in §3, §4 and §5.4 is argued. | risks.sgit.ai |
| **PKI ships keys, not a trust system.** No revocation, no directory in sgit v0.16.0+. The registry is a static-file MVP. Append-lane token derivation is published with *"do not code against this"*. §6 is a design. | pki.sgit.ai |
| **There is no graph database.** No SPARQL, no Cypher, no RDF in code — *"a hand-written content-addressed object graph in the browser"*, 71 nodes / 141 edges in the shipped vault. "Query the graph" means something much narrower than a reader will assume. | graphs.sgit.ai |
| **Nothing in this newsroom runs.** No department, no role, no cost ledger, no payment rail integration. | newsroom.sgit.ai |
| **Client-assembled vault pages are invisible to crawlers.** Inherited, unresolved, and **existential for a news publication** rather than inconvenient. Rendering must be decided before content, not after. | this site, T4 |
| **The precedent is a publication that did not launch.** Portugal had a named beat, a dated deadline, a phased ramp and ten acceptance criteria, and shipped nothing. This brief has more assets and the same failure mode. | ../mvps/portugal.html |

One further tension, which is not a limit so much as a recursion worth naming: **this publication would report on the governance of agentic systems while being one.** Its own agents would hold mandates, act on them, and publish. That is either the strongest possible demonstration or the most obvious conflict, depending entirely on whether the publication holds itself to the standard it reports against — which means its own mandates, intervals and underwriters must be public from day one, not added when someone asks.

---

## 12. Build order

Six steps. Steps 1–3 are the minimum viable publication and can be done against assets that already exist.

| # | Step | Depends on |
|---|---|---|
| **1** | **The anchor set.** Freeze and hash the primary sources for the opening beat; build the byte-offset anchor table. Publish the three-state staleness label for every source. | Nothing — the sources are public |
| **2** | **One story, end to end.** A single story through the full vault layout of §4, including its facts, its absence set, its signed by-line and its interval. **Proves the architecture or kills it.** | Step 1 |
| **3** | **The staleness wire.** Automate the anchor check; publish the first break as a story. | Steps 1–2 |
| **4** | **The absence beat.** Reproduce the Article 26(5) method as a repeatable weekly format. | Step 2 |
| **5** | **Projections.** Two personas first — legal counsel and GRC. Not ten. | Step 2 |
| **6** | **The join.** One customer register holding a typed edge into a public Fact node, and one correction propagating into it. **This is the commercial proof and everything before it is preparation.** | Steps 2–4, and a risk engine that does not yet exist |

Steps 1–4 are honestly available today. **Step 6 is not**, and the brief should not imply otherwise: it depends on the register engine that `risks.sgit.ai` states does not exist.

---

## 13. Acceptance criteria

| # | Criterion | Verification |
|---|---|---|
| 1 | Every quoted provision resolves to a byte offset in a hashed frozen source | Anchor check runs in CI and fails the build on drift |
| 2 | Every cited source carries one of the three staleness labels | No source published unlabelled |
| 3 | One story exists end-to-end in the §4 vault layout | Open the vault; walk from headline to frozen bytes |
| 4 | Every assessment carries an interval and a named underwriter | No assessment publishes without both |
| 5 | An expired assessment visibly lapses rather than silently persisting | Set a 1h interval; observe the lapse |
| 6 | One absence report published with each unanswered question individually assignable | Questions are nodes, not prose |
| 7 | One correction supersedes a published Fact **without deleting it**, and what cited it is enumerable | Follow the supersedes edge in both directions |
| 8 | Two persona projections generated from one story, both faithful to the same evidence set | Diff the claims, not the prose |
| 9 | The publication's own mandates, intervals and underwriters are public | A reader can audit the newsroom by the standard it reports against |
| 10 | Right of reply recorded as a node for every named-third-party assessment | No assessment ships without a reply node or a recorded declining |
| 11 | Pages are crawler-visible | Fetch as a bot; compare against rendered |
| 12 | No sibling's material is restated in this publication's own words | Boundary review against §9 before release |

---

## 14. Open questions

Published unresolved, per house convention.

| # | Question | Note |
|---|---|---|
| **Q1** | **Who is legally answerable for what this publication asserts?** | Portugal's question 5, still open. §6 answers the editorial half and explicitly not the legal half. **This is a precondition for launch, not a detail to settle afterwards** |
| **Q2** | What is the formula language? | `risks.sgit.ai` Q1, published as *undefined*. The Formula Keeper role has no notation to work in until it is answered |
| **Q3** | Which beat exactly? EU AI Act only, or agentic governance broadly? | Closability is the criterion. Broader is more interesting and may not close |
| **Q4** | Who underwrites an assessment the publication's own agents produced? | A named human per §6 — but at what volume does that stop being possible, and what happens then? |
| **Q5** | Does the publication assess RiskMandate.ai's own product? | If no, the independence claim in §10 is hollow. If yes, by whom |
| **Q6** | Server-rendered or client-assembled? | This site's T4, inherited, and existential here |
| **Q7** | What is the interval default for a regulatory fact? | The ladder is published; the mapping from volatility to interval is not |
| **Q8** | Does a reader's challenge to a fact enter the graph as a node? | `risks.sgit.ai` C2 allows *challenge the facts* as a first-class move. Extending that to readers is either the best feature here or an abuse surface |

---

## 15. Relationship to prior work

| Date | Document | Relationship |
|---|---|---|
| 23 Jun 2026 | Audience, personas and the name: Risk Mandate.ai | The persona cast §8 projects against; the fractal-market argument |
| 26 Jun 2026 | Risk Mandate.ai: vision and positioning | The no-deny mechanic, facts-only discipline, and *"the proof that travels"* that §10 constrains |
| 30 Jun 2026 | The Risk Mandate Library | The direct precursor. The agent cast and *"each article is its own world, its own ontology and taxonomy"* |
| 12 May 2026 | Portuguese newsroom workflow | The roles and the daily clock §7 adapts; open question 5, which §6 half-answers |
| 12 May 2026 | Portugal bilingual GenAI publication | The MVP scoping criterion §1 applies |
| 17 May 2026 | Articles as vaults | The per-story vault §4 extends |
| 21 Aug 2026 | `02__source-provenance-and-attribution.md` | The provenance contract, unchanged and non-negotiable |
| 21 Aug 2026 | `06__boundaries-and-house-style.md` | §1's Risk Mandate inversion, which §0 and §9 hold to |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
