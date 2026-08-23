# Licences

This repository carries two licences, and a third that applies to a specific subset of
content it republishes.

> **Code** in this repository is licensed under the Apache License 2.0 (see `LICENSE`).
>
> **This site's own documentation and written content** — every `.html` page,
> `index.md`, `llms.txt`, and the brief pack in `briefs/` — is licensed under the
> Creative Commons Attribution 4.0 International licence (CC BY 4.0), unless a specific
> page states otherwise.

## What that means here

| Path | Licence |
|---|---|
| `admin/build/*.py`, `admin/build/*.js`, `assets/*.js`, `assets/*.css`, `.github/workflows/*` | Apache License 2.0 |
| `briefs/*.md`, `briefs/*.csv`, `briefs/*.json`, `index.md`, `llms.txt`, every `*.html` page | CC BY 4.0 |

## One limit specific to this site: the republished library

`library/index.html`, `economics/micro-and-nano-payments.html`, and the two
provenance-blocked sections on `rights/index.html` synthesise material first published
on [`docs.diniscruz.ai`](https://docs.diniscruz.ai), which is released under **CC0 1.0
Universal** — a public-domain dedication, not CC BY. These are different grants:

- **CC0** is more permissive than CC BY, so republishing CC0 material under this
  repository's CC BY 4.0 terms is legally sound.
- This repository's pages **cannot make the original more restrictive than it already
  is.** Every page deriving from `docs.diniscruz.ai` material states the source licence
  explicitly in its provenance block, per `briefs/02__source-provenance-and-attribution.md`.
- **This site does not claim verbatim reproduction of that material.** Every republished
  section is labelled with an honest curation status — see the provenance block on the
  page itself. Where a page is a synthesis, only this site's own summarising text is CC
  BY 4.0 content of this repository; the original remains CC0 at its source.

## Not included in this repository

Per `briefs/08__source-manifest.csv`, a small set of Tier 3 source material — a named
venture-capital firm, live product pricing, an internal investor review, and an
unbuilt source-protection design that would endanger a real source if published as a
working claim — is deliberately excluded from this repository and is not licensed for
publication here under any of the above.

## The decision behind it

Per a decision of 21 August 2026, applied across the `*.sgit.ai` estate: unless a
document explicitly says otherwise, content on a `*.sgit.ai` website is released under
CC BY 4.0. This site's own participant disclosure additionally argues that
`docs.diniscruz.ai` should align to CC BY 4.0 for future publication, leaving
already-published articles as CC0 — see `about/participant.html`.
