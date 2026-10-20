# newsroom.sgit.ai — Brief Pack

**Pack version:** v1.0 · 21 August 2026
**Target site:** `newsroom.sgit.ai` — *The Future of News*
**Sources:** `the-cyber-boardroom/SGraph-AI__App__Send` @ **v0.33.62** (read-only) · `DinisCruz/docs.diniscruz.ai` @ **v0.3.123** · `DinisCruz/files.diniscruz.ai`
**Siblings:** sgit.ai · nhi.sgit.ai (v0.1.19) · pki.sgit.ai (v0.1.4) · graphs.sgit.ai (in build) · sg-sentinel.sgit.ai (v0.1.1)

---

## 0. Why `newsroom` and not `news`

The corpus names this domain to itself as **"the future-of-news stack"** — 21 occurrences across 13 files, always hyphenated, coined in the 5 July evidence-economy brief and propagated into the reality tree. Unhyphenated "future of news" returns zero.

But the *material* is overwhelmingly about how news gets **made, proven and paid for**, not about news itself: `newsroom` appears 173 times across 42 files. `newsroom.sgit.ai` also sidesteps the convention that a `news.` subdomain means company announcements — a slot `sgit.ai/updates/` already fills.

And, as the brief for this pack put it, it holds for **future directions as we start to execute some of these ideas**. A site called `news` is a research site. A site called `newsroom` can become a running newsroom without a rename.

**Site title:** *The Future of News.* Domain terse, title carrying the thesis — the same split as pki.sgit.ai ("Public Key Infrastructure for Agents").

---

## 1. The one-paragraph thesis

News is failing not because there is too little information but because there is no walkable chain from a claim to its evidence, no way for a correction to reach what it disproved, and no way to pay the person who did the original work. Each of those is a graph problem. A story is not an article — it is a graph that accumulates evidence, perspectives, entities and confidence, of which every article, infographic, translation and per-sector briefing is a **projection**. Make the editorial process public, make the citation chain typed and signed, and the two things that follow are that **corrections propagate** and **facts become billable upstream**. That is the future-of-news stack: sell the graph, not the paragraph.

---

## 2. What exists — three corpora, ~110,000 words

| Source | Material | State |
|---|---|---|
| **`__Send` repo** | ~35,000 words of core news material across 18 Tier-A documents, plus trust/rights/monetisation infrastructure | Unpublished. Almost all CC BY 4.0 |
| **`docs.diniscruz.ai`** | **68,846 words** across **10 core published articles**, Feb 2025 – Oct 2025 | **Already public.** Full metadata captured — see §4 |
| **External CBR repo** | ~15,000 words, three documents that look like the origin of the thread | **Not retrieved.** See gap N1 |

The `docs.diniscruz.ai` material predates the `__Send` material by roughly a year and is in the founder's public voice. **It is the site's prior art and must be linked, not silently absorbed** — see `02__source-provenance-and-attribution.md`, which is the load-bearing file in this pack.

---

## 3. The eight themes

Full treatment with sources in `01__thesis-and-themes.md`.

1. **The story is a graph; the article is a projection.** *(Very developed.)* One story node → seven audience projections. "Sell the graph, not the paragraph."
2. **Provenance is the product; the editorial process is public.** *(Very developed.)* 15 newsroom departments each with a public page; a per-story provenance page with a real cost breakdown. *"A newsroom that shows its work earns trust that a black-box newsroom cannot."*
3. **Corrections must propagate; staleness is first-class.** *(The most distinctive argument in the corpus.)* *"In a document, a correction is a new document. Nothing that cited the original knows."*
4. **The economics: pay the fact creator, not the last-mile publisher.** *(Argued, mechanism open.)* A worked 60/25/10/5% upstream split from Feb 2026.
5. **Trust as a purchasable product.** *(Commercially developed, operationally thin.)* The **fact-certifier** as a distinct, payable, warranted role. Named **Trust-as-a-Service** (43 occurrences).
6. **Content rights and the legal stick.** *(One strong doc, untouched since Feb.)* CC-Signed licence variants — break the signature chain, break the licence.
7. **Agentic newsroom operations: more humans, not fewer.** *(Developed, unbuilt.)* Explicitly *"not an effort to replace journalists with agents. The opposite."*
8. **Meaning, concepts and multilingual publishing.** *(Newest, actively moving.)* The author is the oracle; *"disagreement is the product."*

---

## 4. The four numbers that carry the site

Real, sourced, and unusually good for a public argument. Full set in `01__thesis-and-themes.md` §4.

- **The 10,000-hours case** — 1993 Berlin violin study; the figure was an *average*, not a threshold, and roughly half the top group had not reached it. The researcher spent his career correcting it. **None of it ever attached to the claim.**
- **The citation network** — one biomedical belief supported by **242 papers, 675 citations, >220,000 supporting citation paths**, tracing back to nothing. Three named distortion mechanisms: citation bias, amplification, invention.
- **A worked per-story provenance page** — "EU AI Act Implementation in Portugal", 12 May 2026: **£8.40 production cost**, 6h 23m, broken down research £3.20 / reporting £2.80 / fact-checking £0.90 / translation £1.10 / graphics £0.40. 12 sources, 2 expert validations, 3 reader contributions.
- **The payment rail is now real** — x402 at the Linux Foundation since April 2026, **~200ms settlement**, ~169m transactions in year one, zero protocol fees; GA in CloudFront/WAF June 2026; Cloudflare Monetization Gateway announced 1 July 2026. And the wall it removes: **a £1 card top-up returns 59p of usable credit.**

---

## 5. Build order

| Step | Section | Why here | Status |
|---|---|---|---|
| **1** | `/` + `/thesis/` — the walkable chain | The one argument everything else serves | ✍️ fresh, from quotes in `01` |
| **2** | `/corrections/` — why corrections must propagate | The most distinctive argument, and the 10,000-hours story carries it with no technical background needed | ✅ near-as-is |
| **3** | `/provenance/` — the editorial process as publication | "Provenance is the product." Ships with the worked £8.40 page | ✅ near-as-is |
| **4** | `/library/` — the 10 published articles, with full source metadata | **Do this early.** It is the site's evidence that this is a two-year thread, not a launch | ✅ data ready in `sources__docs-diniscruz-ai.json` |
| **5** | `/economics/` — paying the fact creator | Where the argument becomes a business | ✅ near-as-is |
| **6** | `/newsroom/` — operations, 11 agent roles, the daily clock | The "future directions" half of the name | ✏️ de-scope from Portugal specifics |
| **7** | `/rights/` — CC-Signed and the legal stick | Untouched since Feb; strong and unusual | ✅ |
| **8** | `/shipped/` — what runs vs what is argued | Non-negotiable. See §6 | ✍️ fresh |
| **9** | `/network/` — boundaries against the four siblings | Prevents the duplication mapped in `06` | ✏️ |
| **10** | `/infographics/` | Inherits the graphs-pack pipeline work | ✏️ |

---

## 6. The honesty constraint

Per `team/roles/librarian/reality/`, **the entire evidence-economy cluster is marked "PROPOSED — does not exist yet"** (P-428/429/430, P-817/818/819). Nothing in the newsroom stack ships.

What *does* exist and can be pointed at: the vault substrate (articles-as-vaults, mini-site deployment, vault CI) — which belongs to sgit.ai and should be cited, not re-explained; MyFeeds as a live personalised-news pipeline, which cannot be published in detail; and the ten published articles, which are real and dated.

**The honest sentence:** *"Nothing on this site is running yet. The articles are real and dated; the newsroom is a design. Here is the line between them."*

⚠️ **One safety-specific caution.** `library/docs/_to_process/secure-send-strategic-opportunities.md` §16.3 describes a SecureDrop-style source-protection vertical — no IP logging, Tor, anonymous upload, auto-delete. **Publishing that as a claim before it exists would put a real source at risk.** Publish it as a *design*, explicitly labelled, or not at all.

---

## 7. What is in this pack

| File | Contents |
|---|---|
| `00__BRIEF.md` | This document |
| `01__thesis-and-themes.md` | Eight themes, 32 sourced quotes, the numbers |
| `02__source-provenance-and-attribution.md` | **The provenance contract** — how every republished page keeps its link to the original |
| `03__corpus-index__send-repo.md` | The `__Send` documents, tiered, with paths |
| `04__prior-art__docs-diniscruz-ai.md` | The 10 published articles with verified URLs, dates, authors, PDFs, LinkedIn posts |
| `05__site-architecture.md` | Page-by-page IA with sources |
| `06__boundaries-and-house-style.md` | Sibling boundaries, redaction watch-list, conventions |
| `07__gaps-and-open-questions.md` | What must be written fresh; what must be retrieved |
| `08__source-manifest.csv` | Machine-readable, both corpora, with provenance columns |
| `sources__docs-diniscruz-ai.json` | Machine-readable provenance record — 13 articles |

Every `__Send` path was verified at v0.33.62. Every `docs.diniscruz.ai` URL was resolved live.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
