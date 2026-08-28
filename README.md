# newsroom.sgit.ai — The Future of News

News is failing not because there is too little information but because there is no
walkable chain from a claim to its evidence, no way for a correction to reach what it
disproved, and no way to pay the person who did the original work. A story is a graph
that accumulates evidence, perspectives and confidence; every article, translation and
infographic is a **projection** of it. **Sell the graph, not the paragraph.**

Live site: https://newsroom.sgit.ai (GitHub Pages, deployed from `dev`).

## Structure

- `index.html` — front page: the claim, the 10,000-hours story, the proof strip
- `thesis/` — the thesis: sell the graph, evidence not truth, the author is the oracle
- `corrections/` — **corrections must propagate**, the site's most distinctive argument:
  the 10,000-hours case, the 242-paper citation network, how a graph answers it, the
  self-critique on agenda ("the graph has an agenda too"), and a live staleness example
- `provenance/` — provenance is the product: fifteen departments, the £8.40 worked
  story, the decision graph, articles as vaults
- `library/` — the published record, chronological, 2025 → present: ten core articles
  and three adjacent pieces, 68,846 words, every entry carrying a provenance block
- `economics/` — paying the fact creator: the 60/25/10/5 split, Trust-as-a-Service, the
  x402 payment rail, and the 2025 micropayments argument republished and paired with it
- `rights/` — content rights: CC-Signed, a licence family with an enforceable stick
- `newsroom/` — operations: roles, the daily clock, departments, the craft doctrine
- `mvps/` — the publication instances: the newsroom specified as a series of small,
  separately launchable publications rather than one platform. The programme index, the
  flagship bilingual country publication and its eleven-role agentic newsroom, and the
  seven Creative Commons seed companies. Designed April–May 2026; none of it was built
- `governance/` — **The Governance Wire (beta)** — the first running MVP of the
  risk-and-governance publication, self-contained so it can move to its own domain. JSON is
  the source of truth for structure (`data/*.json`), markdown for prose (`content/*.md`), and
  the HTML is a projection built by `governance/build/build.py` and checked by
  `governance/build/gates.py`. Fully agentic: seven roles under `governance/team/`, one page
  each; no human review before publication, no legal sign-off, nothing anchored — every page
  says so. `governance/newsroom/` is the room itself: a clickable floor whose dialogue is
  assembled from live data, and a state map whose `frozen` door is shut, which is why nothing
  in the graph is anchored. `governance/research/` publishes the Researcher's runs, including
  the URLs our own egress could not reach
- `briefs/10__the-newsroom-floor.md` — a **debrief**, published for the other `*.sgit.ai`
  sites: how the agentic team was rendered as a point-and-click room, the rule that keeps
  it from being a mock-up, the defects it shipped into, and a porting recipe. Rendered at
  `documents/newsroom-floor.html`
- `shipped/` — what runs vs what is argued. Non-negotiable
- `network/` — sibling boundaries, the Risk Mandate inversion, open questions
- `documents/` — the brief pack this site was built from, published verbatim in `briefs/`,
  plus one **v1.1 addendum** that looks forward instead of back:
  `09__risk-and-governance-newsroom.md`, a commissioning brief for a risk-and-governance
  publication assembled from this network, with `riskmandate.ai` as its named customer
- `about/participant.html` — participant disclosure; two years of disclosed model
  co-authorship, stated as an asset rather than an awkwardness
- `admin/` — engineering: comms (open requests, in public), versions, build tooling
  - `admin/build/chrome.py` — the single definition of nav and footer, applied across every page
  - `admin/build/validate.js` — the pre-release gate, including the provenance-contract
    and redaction-watch-list checks specific to this site
- `assets/site.css` + `assets/nav.js` — the shared `sgit.ai` design language

## The provenance contract

Every page that republishes or derives from previously published material carries a
visible block: the **original** publication date (never the republication date), a link
to the original, the original authors including any AI co-authorship, and an honest
curation label (verbatim / edited / excerpted / synthesised). Full contract in
[`briefs/02__source-provenance-and-attribution.md`](briefs/02__source-provenance-and-attribution.md) —
the load-bearing file in this site's own brief pack. This site's central argument is
that most articles do not provide evidence and the link is never followed; losing its
own provenance chain would refute the site on page one.

## Release process

1. Bump `admin/build/version.txt` (vX.Y.Z, exactly once per release) and add a row to
   `admin/versions.html`; update `admin/comms.html`.
2. `python3 admin/build/chrome.py` — propagates the version badge and any nav/footer
   change to every page, and stamps the version into `llms.txt` and `index.md`.
3. `python3 governance/build/build.py` — regenerates `/governance/` from its JSON and
   markdown (run before chrome.py if governance data or prose changed)
4. `python3 governance/build/gates.py` — the section's own thirteen checks
5. `node admin/build/validate.js`
6. `git commit -am "site vX.Y.Z: ..." && git push origin dev`

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate → auto-tag
(`vX.Y.Z`, verified against `version.txt` and the commit subject, next-minor enforced) →
deploy to GitHub Pages. Pull requests run validation only. Same pipeline as
[SGit-AI__Website](https://github.com/SGit-AI/SGit-AI__Website),
[SGit-AI__Website__PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI),
[SGit-AI__Website__Graphs](https://github.com/SGit-AI/SGit-AI__Website__Graphs) and
[SGit-AI__Website__Issues-FS](https://github.com/SGit-AI/SGit-AI__Website__Issues-FS).

### What the gate checks

The shared core (version agreement, links, canonical, agent surface, key-leak, block
balance, agent block) plus two checks specific to this site: **the provenance
contract** — every `class="provenance"` block must state a first-published date and a
working source link — and **the redaction watch-list** — a fixed set of Tier 3 strings
from the brief pack's own source manifest may never appear in the published tree.

## v0.2.0 — what shipped, and what is honestly still open

v0.1.0 shipped before a brief pack existed for this site and built on a wrong premise
(the site reporting on the `*.sgit.ai` network's own activity). v0.2.0 replaces that
content in full against the real, commissioned brief — *newsroom.sgit.ai, The Future of
News* — and follows its build order for the first five steps. Three sections
(`rights/`, `newsroom/`, `thesis/`) ship as single comprehensive hub pages rather than
the full multi-page trees the brief specifies, tracked as open task T1 on
`admin/comms.html`. Full detail on `admin/versions.html`.

## Licence

Two licences — see [`LICENSES.md`](LICENSES.md). Code Apache 2.0; this site's own
content CC BY 4.0. Republished library material is CC0 1.0 Universal at source
(`docs.diniscruz.ai`) — stated per page, never silently relicensed.
