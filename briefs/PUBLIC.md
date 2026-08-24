# What was changed before publication

The brief pack in this directory is published **verbatim except for the redactions
recorded below**. This file exists because a silent redaction is the worse of the two
options: a reader who cannot see that something was removed cannot judge what was
removed, and on a site whose whole argument is that provenance should be walkable, an
undisclosed edit to its own source documents would be the argument refuting itself.

This is the same transparency convention the sibling `*.sgit.ai` sites use when
republishing a source pack.

---

## The redactions

**Nine redactions, in three files.** Every one replaces an identifier with a visible
`[redacted]` marker — the surrounding sentence, table row and manifest column are
otherwise untouched, so what the pack *says* about each item is fully readable.

| File | What was redacted | Why |
|---|---|---|
| `03__corpus-index__send-repo.md` | A named venture-capital firm (in a filename); an investor-facing internal hostname (in a filename); a B2B price range | Tier 3 rows. The pack lists these documents in order to say **do not publish them**; the identifiers inside those rows are the very thing being withheld |
| `06__boundaries-and-house-style.md` | The same named venture-capital firm; an AWS account number; the same investor-facing hostname; the same B2B price range | This is the pack's own redaction watch-list. It names each item in the course of forbidding its publication — which means publishing the watch-list verbatim would publish exactly what it forbids |
| `08__source-manifest.csv` | The same firm and hostname (in two filenames and two "why it matters" cells); the same price range | Tier 3 manifest rows, same reason |

## What is *not* redacted, deliberately

- **The reasoning is intact.** Every entry still says what kind of thing was withheld
  and why — a named VC and a real planned meeting, a live product's B2B pricing and
  legal-entity to-do list, an internal investor review, infrastructure account detail.
  A reader can see the shape of what is missing and disagree with the decision.
- **The tiering is intact.** All 48 manifest rows are still present, still tiered, still
  counted. Nothing was removed from the pack; identifiers inside four rows were masked.
- **No substantive argument was touched.** The redactions are identifiers only: a
  company name, a hostname, an account number, a price range. No sentence of analysis,
  no quotation, and no source path outside those four rows was altered.

## Why this was needed

The pack's watch-list (`06` §2) is a list of things not to publish. Publishing the pack
verbatim published that list, and the list names its own subjects — so the act of
documenting the exclusion performed the disclosure. The pre-release gate now checks the
published pack alongside every other file rather than exempting it, so this specific
failure cannot recur silently: an unredacted identifier in `briefs/` fails the build.

The unredacted pack remains the source of truth privately. What is published here is the
redacted copy, and this file is the difference.

---

This document is released under the Creative Commons Attribution 4.0 International
licence (CC BY 4.0).
