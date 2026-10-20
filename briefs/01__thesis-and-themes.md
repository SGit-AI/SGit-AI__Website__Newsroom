# 01 — Thesis, Themes and Quotes

Founder briefs abbreviated as `briefs/` (= `team/humans/dinis_cruz/briefs/` in `SGraph-AI__App__Send`). All paths verified at v0.33.62. **PL** = the project lead's own voice, transcribed.

---

## 1. The eight themes

### T1 · The story is a graph; the article is a projection *(very developed)*
Traditional news is article-centric; this is story-centric. A story node accumulates evidence, perspectives, timeline, entity cross-references and a confidence model. The article, the infographic, the short version, the audio version, the per-sector version are all **projections** of it.
**Sources:** `briefs/05/12/v0.27.38__strategy-brief__ai-powered-news-organisation-principles.md` (principles 2–3) · `briefs/05/12/v0.27.38__strategy-brief__portuguese-newsroom-workflow.md` (per-story vault tree, seven audience projections) · `briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-evidence-packs-as-a-service-agentic-api-sg-vaults-skills-model-on-demand-micropayments.md`
Specified down to directory layouts and acceptance criteria. Never built.

### T2 · Provenance is the product; the editorial process is public *(very developed)*
The differentiator is not the byline but the walkable chain. Every claim links to evidence. The review process is a **decision graph with named ownership at each step**, not a yes/no. The newsroom's 15 departments each have a public page. Every story carries a provenance page showing tips, assignments, bounce-backs, fact-checks, diffs, cost and corrections.
**Sources:** `briefs/05/12/v0.27.38__dev-brief__newsroom-layout-visible-editorial-process.md` · `briefs/06/13/vault-platform-and-commercialisation/v0.33.26__arch-brief__sg-send-agentic-content-website-provenance-decision-graph-research-publish.md` · `briefs/05/17/v0.27.55__dev-brief__articles-as-vaults-publishing-workflow.md` · `briefs/02/23/part-2/v0.6.14__vision__content-trust-infrastructure-pki-signed-facts.md`

### T3 · Corrections must propagate; staleness is first-class *(the most distinctive argument)*
A correction in a document set reaches nothing; a correction in a graph reaches everything downstream. Superseded claims are marked from a date and never deleted, so *"what did we believe in March"* stays answerable. Citation edges are **typed by faithfulness** — supports / partially supports / extends beyond / contradicts. Freshness is recorded and priced.
**Sources:** `briefs/08/09/graphing-text/v0.33.57__arch-brief__sg-send-fact-does-not-exist-in-a-vacuum-agenda-is-context-corrections-must-propagate.md` · `briefs/07/31/projects-budgets-and-evidence/v0.33.54__strategy-brief__sg-send-paying-the-fact-creator-contextual-validation-not-truth-micropayments-for-correct-use.md` · `briefs/07/31/canonical-act-build/v0.33.54__research-brief__sg-send-no-canonical-ai-act-consolidated-version-absent-article-10-probe-three-states-of-staleness.md` · `briefs/02/23/part-3/v0.6.14__architecture__fractal-document-signing-pki-paragraphs.md`

### T4 · Pay the fact creator, not the last-mile publisher *(argued; mechanism open)*
Today the last-mile publisher captures the revenue and the original researcher gets little. Provenance makes upstream flow trackable, so an author micropayment becomes a **consumption billing event** fired when a cited source is read or queried. The 31 July refinement: what is billable is not *is this true* but ***is this use of it sound***, cached per claim-and-context pair.
**Sources:** `briefs/02/23/part-2/…content-trust-infrastructure-pki-signed-facts.md` (the 60/25/10/5 split) · `briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-news-backed-evidence-vaults-grounding-risk-graphs-trust-as-a-service-author-micropayments.md` · `briefs/07/31/projects-budgets-and-evidence/…paying-the-fact-creator…md` · `briefs/08/09/graphing-text/v0.33.57__arch-brief__sg-send-enrichment-and-shared-anchors-research-paid-once-wikidata-is-the-concept-layer.md`
**Every open question about metering, settlement and licensing is still open.**

### T5 · Trust as a purchasable product *(commercially developed, operationally thin)*
The register splits into risk-acceptor and **fact-certifier** — a distinct, payable, warranted role. Credibility is a track record over time that **decouples the weight of a statement from the rank of the speaker**. Weight comes from independence of sources, not count. Named **Trust-as-a-Service** (43 occurrences across 21 files).
**Sources:** `briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-evidence-economy-force-of-proof-fact-certification-two-prices-evidence-based-revenue-models.md` · `briefs/07/04/credibility-and-feedback/v0.33.42__arch-brief__sg-send-credibility-calibration-time-learning-track-record-feedback-loop-decouple-from-power.md` · `briefs/08/09/graphing-text/v0.33.57__arch-brief__sg-send-evidence-packs-attach-never-mutate-weight-by-independence-not-count.md`

### T6 · Content rights and the legal stick *(one strong doc, untouched since February)*
Technology without enforcement is optional. **CC-Signed** licence variants (BY-S, BY-SA-S, BY-NC-S, BY-ND-S) make signature preservation a licence *condition*, so stripping attribution becomes a provable breach — with an explicit target list: content aggregators, news outlets, AI training pipelines, LLM applications.
**Source:** `briefs/02/23/part-4/v0.6.14__architecture__signed-creative-commons-legal-enforcement.md` — the strongest content-rights document in the corpus, and the closest thing to an AI-content-compensation position.

### T7 · Agentic newsroom operations: more humans, not fewer *(developed, unbuilt)*
Agents absorb production grunt-work so **more** humans become affordable in more roles — verifiers, translators, curators, personalisers, reader-contributors — funded per contribution rather than employed. Eleven agent roles mapped to newsroom functions; an hour-by-hour daily clock; a three-phase soft launch with go/no-go gates.
**Sources:** the three `briefs/05/12/v0.27.38__*` briefs · `team/roles/journalist/REFERENCE__from-issues-fs.md` (the craft doctrine — inverted pyramid, five Ws, **second stories**, editorial independence) · `team/roles/journalist/ROLE.md`

### T8 · Meaning, concepts and multilingual publishing *(newest, actively moving)*
Lifting text into concepts is **decompilation, not compilation** — ambiguous, needing an oracle, and the author is the only oracle. *"Disagreement is the product."* Concepts anchor to language-independent identifiers (Wikidata; EuroVoc for EU instruments) so cross-language inconsistency does not creep in.
**Sources:** `briefs/08/09/graphing-text/v0.33.57__strategy-brief__sg-send-refactoring-meaning-decompilation-not-compilation-author-is-the-arbiter.md` · `…enrichment-and-shared-anchors…` · `…index-is-not-a-source…` · `briefs/07/31/canonical-act-build/v0.33.54__arch-brief__sg-send-paragraph-as-bow-tie-concept-extraction-eu-authority-tables-declining-cost-curve-shades-of-compliance.md`

---

## 2. The quote bank

### On the product
> **PL** — "how do you create this website that fundamentally sells trust, that sells access to good and reliable data, that can be used effectively and consumed effectively."
> `briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-news-backed-evidence-vaults-grounding-risk-graphs-trust-as-a-service-author-micropayments.md`

> **PL** — "if I was a journalist with a news website looking for ways to monetize the research and the information, I would create a service where you sell facts, you sell trust, and you sell evidence packs."
> `briefs/07/05/evidence-economy/…evidence-packs-as-a-service…md`

> **PL** — "not just the news story, but the evidence, the trails, the assurance, you have done the legwork to connect the dots, and then you have the graph of your article."
> *Same file, with its own gloss:* **"Selling the graph, not the paragraph, is the core of the model."**

> **PL** — "they are not using the LLMs to produce the materials, they are using LLMs to parse information, create tools and visualisations, and maintain semantic knowledge graphs that **they still own**."
> *Same file.* **This is the sentence that separates this position from every "AI in the newsroom" pitch.**

### On what is broken
> **PL** — "most articles do not provide evidence, they provide a link, the link is never followed, and it could go to a site that no longer exists. We do not get a reference of what references what."
> `briefs/06/13/vault-platform-and-commercialisation/v0.33.26__arch-brief__…provenance-decision-graph-research-publish.md`

> **PL** — "a decision should never be a yes or no. A decision should always be a graph that collects a bunch of evidence… The question becomes who takes ownership."
> *Same file.*

> **PL** — "there is no point having humans in the loop who just approve without context, that is not human in the loop."
> *Same file.*

### On corrections — the site's sharpest material
> **PL** — "the fact doesn't exist in a vacuum."
> `briefs/08/09/graphing-text/v0.33.57__arch-brief__…fact-does-not-exist-in-a-vacuum…md`

> **PL** — "this is not necessarily conspiracy theories, it's just that every person has an agenda, every entity has core objectives, whether it's to sell more or provide certain things, the bias is always there."
> *Same file.*

> **PL** — "even quotes sometimes don't have the correct meaning, and the original author didn't actually mean what is now being quoted as reference."
> *Same file.*

> *Brief voice, same file* — "In a document, a correction is a new document. Nothing that cited the original knows. In a graph, a correction is an edge… **how much of what I believe rests on claims that have since been corrected?** No document set can answer that. A graph answers it as a traversal."

> *Brief voice, same file* — "**The hazard is what a reader, or a downstream system, does with it.** … The same tool that helps a reader discount a vendor's study of its own product helps them discount a regulator's finding about their own industry." And: "**the graph has an agenda too.**"
> **Publish this one.** A site that names the way its own tool can be abused is making the argument the rest of the site depends on.

> *Brief voice* — "This is the INVERSE of how misinformation works today. Currently, a false claim propagates virally and the correction barely travels. **In this model, the correction propagates with the same force as the original claim.**"
> `briefs/02/23/part-2/v0.6.14__vision__content-trust-infrastructure-pki-signed-facts.md`

> *Brief voice, same file* — "The system doesn't decide what's TRUE — it measures what's **EVIDENCED**. The reader sees the evidence chain and decides."

### On the economics
> **PL** — "the angle is not just, is this statement correct in itself; the question is, **is this correct in this context, for this use, for this conclusion**."
> `briefs/07/31/projects-budgets-and-evidence/v0.33.54__strategy-brief__…paying-the-fact-creator…md`

> **PL** — "in companies that's okay, because that's already covered by the cost of the company operating, but in the real world at the moment we don't have that."
> *Same file, with its gloss:* **"The public evidence base is a commons with no maintenance budget, and it decays accordingly."**

> *Brief voice, same file, on Ericsson* — "**And none of it attached to the claim.** … The person best placed in the world to say *that is not what my study showed* had no channel, no standing at the point of use, and no economic reason to keep doing it beyond his own conviction."

> **PL** — "we also need to have a commercialisation model for journalists, and entities who do research, they should also have a way to confirm that research is correct and has been used in that particular way." — *with the brief's assessment:* "**That is arguably the larger market.**"

> **PL** — "the rewards of the person that is benefiting from that extra analysis need to trickle down to the people who actually did the original analysis."

### On the newsroom
> *Brief voice* — "Traditional newsrooms have an editorial process that readers never see… **A newsroom that shows its work earns trust that a black-box newsroom cannot.**"
> `briefs/05/12/v0.27.38__dev-brief__newsroom-layout-visible-editorial-process.md`

> *Brief voice* — "Critical to state upfront: this is **not** an effort to replace journalists with agents. The opposite. Agents make it possible to involve **more** humans, in more roles, at more scale than was previously affordable."
> `briefs/05/12/v0.27.38__strategy-brief__ai-powered-news-organisation-principles.md`

> *Brief voice* — "**Humans are the bar; agents are the volume.**"
> `briefs/05/12/v0.27.38__strategy-brief__portuguese-newsroom-workflow.md`

### On authorship and meaning
> **PL** — "the point here is not to have absolute truth; it is to have a bias from the point of view of the creator of the document, because what we want is to make sure that the creator of the document confirms what he means by the document."
> `briefs/08/09/graphing-text/v0.33.57__strategy-brief__…decompilation-not-compilation-author-is-the-arbiter.md`

> *Brief voice, same file* — "**A structured reading that the author disputes has told them something they did not know about their own text.**"

### On rights and credibility
> *Brief voice* — "The danger is in the amendments. The small changes. The 'we updated our terms' email. The clause that shifted between v3 and v4. That's where problems hide — **because attention has dropped**."
> `briefs/02/23/part-3/v0.6.14__architecture__fractal-document-signing-pki-paragraphs.md`

> *Brief voice* — "**Licences are not optional.** … What if we add a SIGNED requirement to the licence? … Break the signature chain → break the licence → legal liability. **This is the legal stick that forces players to maintain provenance.**"
> `briefs/02/23/part-4/v0.6.14__architecture__signed-creative-commons-legal-enforcement.md`

> *Brief voice* — credibility "**decouples the weight a statement carries from the volume, power, or rank of the person making it, so the quiet person who is usually right is heard and the loudest or most senior voice does not automatically win.**"
> `briefs/07/04/credibility-and-feedback/v0.33.42__arch-brief__…credibility-calibration…md`

> *Brief voice* — "**more evidence does not mean more confidence unless the evidence is independent** … any percentage put in front of a reader carries an implied promise of calibration that somebody has to keep."
> `briefs/08/09/graphing-text/v0.33.57__arch-brief__…evidence-packs-attach-never-mutate…md`

> *Brief voice* — "Privacy policies are promises. **Transparency panels are proof.**"
> `team/roles/journalist/site/_pages/transparency.md`

---

## 3. The numbers

### The 10,000-hours case — the site's best non-technical story
`briefs/07/31/projects-budgets-and-evidence/v0.33.54__strategy-brief__…paying-the-fact-creator…md`
- 1993 study of violin students at a Berlin academy; popularised 2008.
- The figure was an **average, not a threshold**: the top group averaged ~10,000 hours by age 20; **roughly half had not reached it**.
- The original researcher called the number *"catchy rather than meaningful… it could as easily have been eleven thousand."*
- The mechanism was **deliberate practice**, not accumulated time. The students were not yet experts.
- Individual variation: one chess player reached master level in **~3,000 hours**, another needed **>20,000**.
- Correction attempts: books, articles, interviews, an open letter. **None attached to the claim.**
- Named: Malcolm Gladwell (populariser), Anders Ericsson (researcher, deceased — keep the cited sources attached).

### The citation network — the same failure, measured
- One biomedical belief: **242 papers, 675 citations, >220,000 supporting citation paths** — tracing back to nothing.
- Three named distortion mechanisms: **citation bias**, **amplification**, **invention** (a hypothesis converted into a fact by citation alone). A fourth from commentary: **citation diversion**.
- Distortions extended into grant applications. Sources cited in-document, including `pubmed.ncbi.nlm.nih.gov/19622839/`.

### A worked per-story provenance page
`briefs/05/12/v0.27.38__dev-brief__newsroom-layout-visible-editorial-process.md`
- Story: *"EU AI Act Implementation in Portugal: Where We Are"*, 12 May 2026, EN + PT.
- **Production cost £8.40** · **production time 6h 23m** · 0 human hours.
- Breakdown: research £3.20 · reporting £2.80 · fact-checking £0.90 · translation £1.10 · graphics £0.40.
- 12 sources consulted · 2 expert validations · **3 reader contributions incorporated** · 4 draft versions with a change log.

### The value split
`briefs/02/23/part-2/…content-trust-infrastructure-pki-signed-facts.md` — reader pays Outlet X; actual value **60% original researcher · 25% data organisation · 10% journalist synthesis · 5% outlet distribution**.

### The payment rail
`briefs/08/06/payments-platform/v0.33.56__research-brief__sg-send-micropayments-stablecoins-x402-hyperscalers-shipped-it-sovereignty-is-awkward.md`
- **x402**: Linux Foundation since April 2026, **>20 founding members**, **~200ms settlement**, "a fraction of a cent", **~169 million transactions** in year one, **zero protocol fees**. GA in CloudFront/WAF June 2026.
- **Cloudflare Monetization Gateway** announced 1 July 2026, waitlist-only.
- AWS Bedrock AgentCore Payments (7 May 2026, with Coinbase and Stripe): ticket sizes **$0.001 – $1,000**.
- The wall it removes: **a £1 card top-up returns 59p of usable credit.** *"The fixed fee is not an inconvenience in that market, it is a wall."*

### Newsroom operational targets
`briefs/05/12/v0.27.38__strategy-brief__portuguese-newsroom-workflow.md` — ≥7 agent roles · **Portuguese entity graph seeded with ≥200 entities** · ≥3 audience projections per story · Phase 1: 1 story/day for 7 days → Phase 3: 5+/day. Daily clock 06:00 scans → 12:00 publish + personalisation fan-out → 14:00+ community.

### The staleness diagnostic — a ready-made news story about news
`briefs/07/31/canonical-act-build/…no-canonical-ai-act…md` — Regulation (EU) 2026/1744 adopted 8 July 2026, in force 27 July. The official consolidated text is dated **12 July 2024 and incorporates nothing**. Public sources fall into three states of staleness; at least one carries a pre-adoption negotiating draft — *"worse than stale because it never was the law."*

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
