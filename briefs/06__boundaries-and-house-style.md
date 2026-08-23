# 06 — Boundaries, Redaction and House Style

---

## 1. Boundaries against the five siblings

The largest risk to this site is not scarcity — it is **duplication**. Map by subject, because `__Send` @ v0.33.62 predates most of the subdomain build-out (the only `*.sgit.ai` hostnames appearing in the whole repo are `hub.sgit.ai`, `pki.sgit.ai` once, and `star.sgit.ai`).

| Sibling | What newsroom would duplicate | Where the boundary sits |
|---|---|---|
| **sgit.ai** | The entire delivery substrate: articles-as-vaults, mini-site deployment, static vault projections, vault CI. ~6 briefs | **Cite, don't re-explain.** Zero words on S3/CloudFront/loaders. And inherit its known problem: client-side-assembled vault pages are invisible to crawlers — existential for a news site |
| **pki.sgit.ai** | PKI-signed claims, key registries, chain of trust, the identity spectrum | Newsroom owns the **application** of PKI to *claims and citations* — the source-attribution chain, and **CC-Signed**, a rights argument PKI would not naturally carry |
| **nhi.sgit.ai** | Agent trust scores, web of trust, NHI 2.0 identity graphs | Newsroom borrows *who is the actor* but owns **whose agenda, whose funding, who is citing** — the five attribution roles. An editorial model, not an identity model |
| **graphs.sgit.ai** | The grounding ladder, node-type formulas, graphs-of-graphs, Wikidata anchoring, decompilation, assertion-vs-pointer | Newsroom owns the **news ontology** — stories, claims, sources, authors — plus the two things graphs would state generically and news must state urgently: **correction propagation** and **citation edges typed by faithfulness** |
| **sg-sentinel.sgit.ai** | Source reputability scoring | Sentinel scores infrastructure; newsroom scores **sources and authors**. One cross-link on the shared principle: reputation is context, not verdict |

### The Risk Mandate inversion — the most important boundary

`briefs/07/05/evidence-economy/` (all three), `briefs/07/04` credibility-calibration, `briefs/06/30` riskmandate-library and `briefs/07/31` paying-the-fact-creator were **written for Risk Mandate**, framing news as the evidence supply for risk graphs.

**Invert it.** Risk Mandate is *one customer* of the future-of-news stack, not its parent. The material is genuinely dual-use — but published under Risk Mandate it reads as a compliance feature; published here it reads as a thesis about journalism. Strip the risk-register framing from every republished evidence-economy brief and let the news argument stand on its own. Add a `/network/riskmandate/` page that says, honestly, "this is what the same machinery looks like pointed at corporate risk."

---

## 2. Redaction watch-list

Run these before any bulk publication.

| Item | Reach | Action |
|---|---|---|
| **MyFeeds.ai** | **212 mentions across 52 files.** The `05/17` briefs carry the strategic repositioning, the **full B2B price list (£2k–£50k+)**, the legal-entity and contracting to-do list, the dual-track editorial-independence discussion, and the `investor.myfeeds.ai` review | **Highest priority.** Ideas yes; pricing, clients and entity detail no |
| **33N Ventures** | Named Porto-based VC with a planned meeting and a private collaboration vault | **Do not publish** |
| **The Cyber Boardroom / CBR** | Named in the Portuguese newsroom brief and the town-planner reviews | De-name in `/newsroom/` pages |
| **Dan Raywood** | Named journalist, subject of a personalised briefing (2025-06-06) | **Already published** on docs.diniscruz.ai — but confirm consent before featuring it on a new site |
| **Named provider / clinical topic** | `06/11/doctor-patient-workflow` and `06/13` reference a provider's clinical-guidance site as first customer; `06/13` flags health-content safety risk | **Do not name** |
| **Placeholders "Dr. X, Prof. Y", "User A/B"** | `05/12` newsroom-layout, `02/17` stakeholder-communication | Already anonymised — the pattern signals real names sat behind them. Leave anonymised |
| **Palantir Foundry OSMM assessment** | `briefs/07/24/sovereignty-and-osmm/…palantir-foundry-scrydon-level-1…` | Named public assessment of a third party — legal sign-off if republished |
| **Family reference** | `briefs/02/23/part-3` email-and-messaging brief uses "my daughter" | Strip |
| **Exposed-vault-key runbook** | `08/14` topic-sections brief links sgit.ai's runbook including the case study of when it happened to that site | Linking re-surfaces the incident. Deliberate choice, not an accident |
| **AWS account `745506449035`** | 49 occurrences / 17 files (infra docs) | Scrub on any bulk docs-tree publication |

**Safe with citations:** Malcolm Gladwell and Anders Ericsson (public figures in published, cited work — note Ericsson is deceased and the brief characterises his career; keep the sources attached) · Replit's production-database deletion · Microsoft/EchoLeak (CVE-2025-32711) · Gartner, Forrester, Bloomberg, Cloudflare, AWS, Stripe, Coinbase as benchmarks.

---

## 3. House style, inherited

Full treatment in the graphs pack `06__house-style-and-conventions.md`. The essentials:

**Structure:** `/llms.txt` at root · `/documents/` with raw markdown as source of truth and rendered reader pages · `/about/participant.html` · `/admin/comms.html` with numbered asks (N1, N2…) and tasks (T1, T2…) in explicit states · `/admin/versions.html` · a build order published unresolved with open questions and honest tensions.

**Voice:** short declarative sentences making checkable claims · publish the argument before the implementation and say which is which · name what you got wrong · open questions stay open and numbered · no marketing adjectives.

**`llms.txt` is the whole surface.** Measured on sgit.ai: the index fetch worked and was *"better than almost anything comparable"*, then link-following failed because agent fetch tools refuse URLs a search has not returned. Each entry must carry the page's **single most important fact**, not just its topic. Publish `/llms-full.txt` as a single-file concatenation.

**Decide rendering before content.** A client-side-decrypted vault site is invisible to crawlers. For a *news* site this is existential — not a nice-to-have.

**Every section serves three readers:** documentation · live demonstration · **agent guidance** (the one most sites omit). For this site the agent block matters commercially, not just editorially: the evidence-packs thesis is that an agent buys facts by API. The site should be the first worked example of its own product.

**Vault rules:** publish read keys, never write keys · escrow the write key before publishing · audit before publish and adopt the `PUBLIC.md` transparency convention · no metered capability behind a published read key.

**Licence:** CC BY 4.0, per the 21 August 2026 decision. Source material from `docs.diniscruz.ai` is CC0 — state the source licence per page; see `02` §5.1.

---

## 4. Two demonstrations to build in from day one

The site's credibility rests on practising what it argues. Two are cheap and available immediately:

1. **A corrections log that propagates.** When a page is revised, do not overwrite — attach, date, and link to what it supersedes, then show what else cited the superseded claim. That is theme 3 running on the site itself.
2. **A provenance block on every derived page.** Original date, original link, original co-authors, honest curation label — `02` §1. A future-of-news site that loses its own chain has refuted itself on page one.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
