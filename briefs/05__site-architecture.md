# 05 — Site Architecture

Page-by-page IA for `newsroom.sgit.ai`, each page mapped to its source.

**Status key:** ✅ publishable near-as-is · ✏️ needs framing or de-scoping · ✍️ **write fresh** · 🔗 links out · 📎 **carries a provenance block** (see `02`)

`briefs/` = `team/humans/dinis_cruz/briefs/`.

---

## Shape

```
newsroom.sgit.ai                     "The Future of News"
├── /                                the walkable chain, in one screen
├── /thesis/                         the argument, five pages
├── /corrections/                    why corrections must propagate   ← lead with this
├── /provenance/                     the editorial process as publication
├── /economics/                      paying the fact creator
├── /rights/                         CC-Signed and the legal stick
├── /newsroom/                       operations: roles, clock, departments
├── /library/                        the published record, 2025→   📎
├── /shipped/                        what runs vs what is argued
├── /network/                        boundaries with the four siblings
├── /documents/                      raw markdown, source of truth
├── /about/participant.html
├── /admin/{comms,versions,index}
└── /llms.txt  +  /llms-full.txt
```

---

## `/` — the front page

| Element | Content | Source | Status |
|---|---|---|---|
| The claim | *"Most articles do not provide evidence, they provide a link, the link is never followed, and it could go to a site that no longer exists."* | `briefs/06/13/…provenance-decision-graph-research-publish.md` | ✅ |
| The story | **The 10,000-hours case.** No technical background required; lands the whole thesis in 200 words | `briefs/07/31/…paying-the-fact-creator…md` | ✏️ |
| The turn | *"In a document, a correction is a new document. Nothing that cited the original knows."* | `briefs/08/09/…fact-does-not-exist-in-a-vacuum…md` | ✅ |
| The proof strip | 242 papers · 220,000 citation paths · £8.40 per story · 200ms settlement · 10 articles since Feb 2025 | `01` §3 | ✅ |
| Honesty line | *"Nothing here is running yet. The articles are real and dated; the newsroom is a design."* | — | ✍️ |

---

## `/corrections/` — build this first

The most distinctive argument in the corpus and the one nobody else is making. Everything else on the site is downstream of it.

| Page | Content | Source | Status |
|---|---|---|---|
| `/corrections/the-claim-that-would-not-die/` | The 10,000-hours case in full: average not threshold, half the group short of it, ~3,000 vs >20,000 hours, and *"none of it attached to the claim"* | `briefs/07/31/…paying-the-fact-creator…md` | ✅ |
| `/corrections/242-papers/` | The citation network: 675 citations, >220,000 supporting paths, back to nothing. Citation bias · amplification · invention · diversion | same + `briefs/08/09/…evidence-packs-attach-never-mutate…md` | ✅ |
| `/corrections/how-a-graph-answers-it/` | Supersede-never-delete; citation edges typed by faithfulness; *"how much of what I believe rests on claims that have since been corrected?"* | `briefs/08/09/…fact-does-not-exist-in-a-vacuum…md` | ✅ |
| `/corrections/agenda-is-context/` | Agenda as disclosure, not dismissal — **including the self-critique**: *"the same tool that helps a reader discount a vendor's study helps them discount a regulator's finding"* and *"the graph has an agenda too"* | same | ✅ **publish the self-critique** |
| `/corrections/staleness-in-the-wild/` | The AI Act: consolidated text dated 12 July 2024 incorporating nothing; three states of staleness; one source carrying a draft that *"never was the law"* | `briefs/07/31/canonical-act-build/…no-canonical-ai-act…md` | ✅ |

---

## `/provenance/` — the editorial process as publication

| Page | Content | Source | Status |
|---|---|---|---|
| `/provenance/show-your-work/` | *"A newsroom that shows its work earns trust that a black-box newsroom cannot."* 15 departments, each with a public page | `briefs/05/12/…newsroom-layout-visible-editorial-process.md` | ✅ |
| `/provenance/a-worked-story/` | The **£8.40 / 6h 23m** page, fully itemised, 12 sources, 3 reader contributions | same | ✅ **the single most persuasive page available** |
| `/provenance/the-decision-graph/` | *"A decision should never be a yes or no."* Named ownership per step; the 100%-LLM → 100%-human spectrum; *"no point having humans in the loop who just approve without context"* | `briefs/06/13/…provenance-decision-graph-research-publish.md` | ✅ |
| `/provenance/articles-as-vaults/` | Each article a vault: text + evidence + graph + sources + translations + **every prompt and decision** | `briefs/05/17/v0.27.55__dev-brief__articles-as-vaults-publishing-workflow.md` | ✏️ light MyFeeds de-naming |
| `/provenance/the-citation-chain/` | PKI-signed claims researcher → journalist → outlet → social; evidence-weight scoring worked HIGH vs LOW | `briefs/02/23/part-2/…content-trust-infrastructure-pki-signed-facts.md` | ✅ |

---

## `/thesis/`

| Page | Content | Source | Status |
|---|---|---|---|
| `/thesis/story-not-article/` | The story is a graph; article, infographic, translation, per-sector briefing are projections | `briefs/05/12/…ai-powered-news-organisation-principles.md` | ✅ |
| `/thesis/sell-the-graph/` | *"Sell the graph, not the paragraph."* And *"semantic knowledge graphs that they still own."* | `briefs/07/05/…evidence-packs-as-a-service…md` | ✅ |
| `/thesis/evidence-not-truth/` | *"The system doesn't decide what's TRUE — it measures what's EVIDENCED."* | `briefs/02/23/part-2/…content-trust-infrastructure…md` | ✅ |
| `/thesis/the-author-is-the-oracle/` | Decompilation not compilation; *"disagreement is the product"*; a disputed reading tells the author something new | `briefs/08/09/…decompilation-not-compilation…md` | ✏️ |
| `/thesis/independence-not-count/` | *"More evidence does not mean more confidence unless the evidence is independent."* | `briefs/08/09/…evidence-packs-attach-never-mutate…md` | ✅ |

---

## `/economics/`

| Page | Content | Source | Status |
|---|---|---|---|
| `/economics/paying-the-fact-creator/` | The 60/25/10/5 split; *"the rewards… need to trickle down to the people who actually did the original analysis"* | `briefs/02/23/part-2/…` + `briefs/07/31/…paying-the-fact-creator…md` | ✅ |
| `/economics/contextual-validation/` | Not *is this true* but ***is this use of it sound***, cached per claim-and-context pair. *"Arguably the larger market."* | `briefs/07/31/…paying-the-fact-creator…md` | ✅ |
| `/economics/trust-as-a-service/` | The **fact-certifier** as a payable, warranted role; two prices; *"trade on facts and evidence rather than attention"* | `briefs/07/05/…force-of-proof…md` | ✅ |
| `/economics/credibility-over-time/` | Track record decouples weight from rank — *"the quiet person who is usually right is heard"* | `briefs/07/04/…credibility-calibration…md` | ✅ |
| `/economics/rails/` | x402, 200ms, zero protocol fees, Cloudflare's gateway — **and the £1→59p wall** | `briefs/08/06/payments-platform/…x402…md` | ✅ |
| `/economics/micro-and-nano-payments/` | The 2025 argument, republished | 📎 [docs.diniscruz.ai 2025-04-02](https://docs.diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html) | 📎 ✅ |

**Pair the last two deliberately.** The 2025 argument plus the 2026 rail is the site demonstrating its own thesis: the argument held, the mechanism arrived, and the original is unedited at its original URL.

---

## `/rights/`

| Page | Content | Source | Status |
|---|---|---|---|
| `/rights/cc-signed/` | The signed licence family; break the chain, break the licence; the named target list | `briefs/02/23/part-4/…signed-creative-commons-legal-enforcement.md` | ✅ |
| `/rights/the-danger-is-in-the-amendments/` | Per-paragraph signing; *"that's where problems hide — because attention has dropped"* | `briefs/02/23/part-3/…fractal-document-signing-pki-paragraphs.md` | ✅ |
| `/rights/scraping-and-compensation/` | Cloudflare's crawler charges | 📎 [2025-07-04](https://docs.diniscruz.ai/2025/07/04/from-free-scraping-to-fair-compensation-cloudflares-genai-crawler-charges-and-the-future-of-news-monetization.html) | 📎 ✅ |
| `/rights/personal-content-rights/` | Deepfakes and AI cloning — the only treatment of **individual** rights | 📎 [2025-06-15](https://docs.diniscruz.ai/2025/06/15/personal-content-rights-protecting-individuals-in-the-age-of-deepfakes-and-ai-cloning.html) | 📎 ✅ |

---

## `/newsroom/` — the "future directions" half of the name

| Page | Content | Source | Status |
|---|---|---|---|
| `/newsroom/principles/` | Eight design principles; **"not an effort to replace journalists with agents. The opposite."** | `briefs/05/12/…ai-powered-news-organisation-principles.md` | ✅ |
| `/newsroom/the-roles/` | 11 agent roles mapped to newsroom functions; *"humans are the bar; agents are the volume"* | `briefs/05/12/…portuguese-newsroom-workflow.md` | ✏️ de-scope Portugal/CBR |
| `/newsroom/the-daily-clock/` | 06:00 scans → 12:00 publish + fan-out → 14:00+ community; three-phase launch with go/no-go gates | same | ✏️ |
| `/newsroom/departments/` | 15 departments as vault folders, each with a public page and a corrections desk | `briefs/05/12/…newsroom-layout…md` | ✅ |
| `/newsroom/the-craft/` | Inverted pyramid, five Ws, source attribution, editorial independence, **second stories** (Three Mile Island, Equifax) | `team/roles/journalist/REFERENCE__from-issues-fs.md` | ✏️ licence check — Issues-FS origin |

---

## `/library/` — the published record 📎

**Build this early.** It is the evidence that this is a two-year thread, not a launch.

Ten core articles, 68,846 words, Feb 2025 – Oct 2025. Full table with verified URLs, dates, authors, PDFs and LinkedIn posts in `04__prior-art__docs-diniscruz-ai.md`; machine-readable in `sources__docs-diniscruz-ai.json`.

**Every page here carries the provenance block from `02` §1 and the visible rendering from `02` §2.** Sort by `first_published` ascending — the chronology *is* the argument. Show the date prominently; a reader who sees "2 April 2025" on the micropayments piece understands the thread differently from one who does not.

---

## `/shipped/` — non-negotiable

The entire evidence-economy cluster is marked **PROPOSED — does not exist yet** in `team/roles/librarian/reality/` (P-428/429/430, P-817/818/819).

- **Runs:** the vault substrate (cite sgit.ai, do not re-explain) · the ten published articles · MyFeeds as a live pipeline (ideas only — no pricing, no clients)
- **Designed only:** every newsroom brief, every evidence-pack brief, Trust-as-a-Service, author micropayments, CC-Signed
- ⚠️ **Never publish as a claim:** the SecureDrop-style source-protection vertical (`library/docs/_to_process/secure-send-strategic-opportunities.md` §16.3). Design-labelled or omitted — a source who believes an unbuilt protection is real is a safety problem.

---

## `/network/`

| Bridge | The connection |
|---|---|
| **graphs.sgit.ai** | The news ontology is an instance of the grounding ladder. News owns **correction propagation** and **citation edges typed by faithfulness** |
| **pki.sgit.ai** | Signed claims and the citation chain. News owns CC-Signed — a rights argument PKI would not carry |
| **nhi.sgit.ai** | *Who is the actor* vs **whose agenda, whose funding, who is citing** — the five attribution roles |
| **sg-sentinel.sgit.ai** | Sentinel scores infrastructure; news scores **sources and authors**. Shared principle: reputation is context, not verdict |
| **sgit.ai** | How it is published. Cite; spend zero words on S3/CloudFront |
| **docs.diniscruz.ai** | 📎 The prior art. **Link forward from the source, never redirect it** — see `02` §3 |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
