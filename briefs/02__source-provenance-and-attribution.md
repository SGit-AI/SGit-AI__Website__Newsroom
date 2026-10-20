# 02 — Source Provenance and Attribution

**This is the load-bearing file in the pack.**

`newsroom.sgit.ai` will republish — in original or curated form — material first published on `docs.diniscruz.ai` between February 2025 and October 2025. **The historical link to the source must survive that move.**

There is a second reason beyond good practice. This is a site whose central argument is that *most articles do not provide evidence, they provide a link, the link is never followed, and it could go to a site that no longer exists.* A future-of-news site that loses its own provenance chain has refuted itself on page one. **The provenance discipline is the demonstration.**

---

## 1. The provenance contract

Every page on `newsroom.sgit.ai` that derives from previously published material MUST carry these fields. Machine-readable values for all of them are in `sources__docs-diniscruz-ai.json`.

```yaml
# ---- provenance block: required on every derived page ----
source_title:        "The Future of News Monetization: Embracing Micro and Nano Payments"
source_url:          https://docs.diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html
source_site:         docs.diniscruz.ai
first_published:     2025-04-02          # the ORIGINAL date, never the republication date
authors:             ["Dinis Cruz", "ChatGPT Deep Research"]
source_repo:         https://github.com/DinisCruz/docs.diniscruz.ai
source_repo_path:    docs/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.md
source_pdf:          https://files.diniscruz.ai/github/pdf/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.pdf
source_linkedin:     https://www.linkedin.com/posts/diniscruz_the-future-of-news-monetization-activity-7313197799121039360-8PKH
source_licence:      CC0-1.0             # docs.diniscruz.ai is CC0; this site is CC BY 4.0 — see §5
republished:         2026-08-21          # when it landed here
curation:            verbatim            # verbatim | edited | excerpted | synthesised
curation_note:       "Republished unchanged; headings normalised to house style."
```

### Field rules

| Field | Rule |
|---|---|
| `first_published` | **The original date, always.** This is the single most important field. A reader must be able to see that the micropayments argument is from April 2025, not from this site's launch week. |
| `republished` | When it appeared here. Never conflate with `first_published`. |
| `curation` | One of four values. Be honest — `synthesised` is not a lesser status, it is a different claim about the text. |
| `authors` | Copy verbatim from source. **72 of the source articles credit `["Dinis Cruz", "ChatGPT Deep Research"]`** — the co-authorship is explicit and must be preserved, not quietly dropped. See §5. |
| `source_pdf` | Every core article has one and all resolve. Keep it — the PDF is a fixed artefact where the HTML may drift. |
| `source_linkedin` | Present for most. It is the record of first *public* circulation, distinct from first publication. |

---

## 2. The visible rendering

The block above is metadata. The reader needs a visible version. Proposed, at the **top** of every derived page — not buried in a footer, because the date is part of the argument:

> **First published 2 April 2025** on [docs.diniscruz.ai](https://docs.diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html) by Dinis Cruz and ChatGPT Deep Research · [original PDF](https://files.diniscruz.ai/github/pdf/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.pdf) · [LinkedIn](https://www.linkedin.com/posts/diniscruz_the-future-of-news-monetization-activity-7313197799121039360-8PKH)
> *Republished here 21 August 2026, unchanged.*

And where the text has been changed, say so in the same breath:

> *Republished here 21 August 2026, **edited**: the 2025 payment-rail section has been superseded by x402 and the Cloudflare Monetization Gateway; see [/economics/rails/](#). The original text is unchanged at the source link above.*

**That second pattern is the one that matters.** It is the site practising correction-propagation on itself: the original stays where it is, the newer knowledge attaches rather than overwrites. That is theme 3 made visible, and it costs nothing.

---

## 3. Do not break the old links

`docs.diniscruz.ai` uses `use_directory_urls: false`, so every article is a `.html` file at a dated path:

```
https://docs.diniscruz.ai/{YYYY}/{MM}/{DD}/{slug}.html
```

Those URLs are live, indexed, and referenced from LinkedIn posts going back to early 2025.

**Rules:**

1. **Never redirect `docs.diniscruz.ai` to `newsroom.sgit.ai`.** The old URLs are the provenance anchor. If they move, every LinkedIn post from 2025 loses its target and the site's own chain breaks.
2. **Link forward, not backward.** Add a line to the *source* article pointing at the newsroom page — "a developed version of this argument is at newsroom.sgit.ai/…". That preserves both directions without moving anything.
3. **Keep the PDFs reachable.** They are served from S3 at `files.diniscruz.ai/github/pdf/{date}/{name}.pdf`. See the durability warning in §4.
4. **Use `rel="canonical"` pointing at the source** for verbatim republications, so search engines attribute the original correctly and the newsroom page does not compete with it.

---

## 4. ⚠️ A durability problem to fix first

The CI in `files.diniscruz.ai` syncs `./files/` to S3 (`749670524505--files-diniscruz-ai`, target prefix `github/`). But:

- **The bucket holds 94 PDFs. The git repo holds 11.** `files.diniscruz.ai` last committed 2025-04-02; `docs.diniscruz.ai` kept publishing to 2025-10-03.
- All 94 serve correctly today — this is not a broken-link problem.
- It is a **provenance problem**: 83 published PDFs exist only in an S3 bucket, with no git history, no version, no reproducibility, and no second copy.

If `newsroom.sgit.ai` is going to cite those PDFs as durable source artefacts, **back-fill them into the repo first.** Otherwise the site's evidence chain terminates in a single mutable bucket — precisely the failure mode the site exists to argue against.

Same category, worth checking while you are in there: **11 articles on `docs.diniscruz.ai` render a literal `{{title}}`** as their heading, including *Semantic OWASP* and *The Future of News: Building Trust Through Fact Provenance* — one of the ten core news articles. Fix before linking to it as canonical.

---

## 5. Two attribution decisions to make deliberately

### 5.1 Licence mismatch

| Site | Licence | Means |
|---|---|---|
| `docs.diniscruz.ai` | **CC0 1.0 Universal** | Public-domain dedication. No attribution required. |
| `*.sgit.ai` family | **CC BY 4.0** (decision of 21 Aug 2026) | Attribution required. |

These are different grants over closely related material. CC0 is the more permissive, so republishing CC0 material under CC BY 4.0 is legally fine — **but the newsroom page cannot make the original more restrictive than it is.** State the source licence in the provenance block (`source_licence: CC0-1.0`) and let the newsroom's own additions carry CC BY 4.0.

Cleanest resolution, and the one this site should argue for: **align `docs.diniscruz.ai` to CC BY 4.0 going forward**, leaving already-published articles as CC0. A site about attribution that dedicates its own work to the public domain with no attribution requirement is making an argument it may not intend.

### 5.2 Model co-authorship is explicit here

Across `docs.diniscruz.ai`: **72 files credit `["Dinis Cruz", "ChatGPT Deep Research"]`**, 10 credit Dinis Cruz alone, **7 credit ChatGPT Deep Research alone**, and several add Claude 3.5 / 3.7 / Opus 4 / Opus 4.1.

The `*.sgit.ai` default is "unless explicit on the doc, authored by Dinis Cruz." **Here it is explicit, and it is shared.** Two consequences:

1. **Preserve the credit verbatim.** Dropping a co-author on republication is exactly the attribution failure the site is about.
2. **It is an asset, not an awkwardness.** A site arguing for provenance and disclosed agenda, which discloses its own model co-authorship in structured front-matter going back to February 2025, has a two-year track record of the practice it recommends. Put that on `/about/participant/` rather than hiding it.

---

## 6. Extending the contract to `__Send` material

The same discipline applies to briefs lifted out of the `__Send` repo, with different field values:

```yaml
source_repo:      https://github.com/the-cyber-boardroom/SGraph-AI__App__Send
source_repo_path: team/humans/dinis_cruz/briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-evidence-packs-as-a-service-agentic-api-sg-vaults-skills-model-on-demand-micropayments.md
source_version:   v0.33.44
first_written:    2026-07-05
source_licence:   CC BY 4.0
curation:         edited
curation_note:    "Risk Mandate framing removed; see 06__boundaries §2."
```

Note `source_version` rather than `source_url` — these were never published, so the version tag *is* the address. Use `first_written` rather than `first_published` so the two cases stay distinguishable in the data.

---

## 7. Checklist before publishing any derived page

- [ ] `first_published` is the **original** date, not today
- [ ] `source_url` resolves (all 13 verified 21 Aug 2026)
- [ ] Co-authors copied verbatim, models included
- [ ] `curation` value is honest
- [ ] Where edited, the change is named and the original is linked
- [ ] `rel="canonical"` set for verbatim republications
- [ ] Source PDF exists in **git**, not only S3 (see §4)
- [ ] Source licence stated where it differs from CC BY 4.0
- [ ] The source article has a forward-link to this page

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
