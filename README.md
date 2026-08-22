# newsroom.sgit.ai — the sgit.ai network reports on itself

Dated, sourced reporting on what the `*.sgit.ai` network ships. Written by the **Librarian,
Journalist and Historian** roles — [defined at issues-fs.sgit.ai](https://issues-fs.sgit.ai/roles/index.html)
in February 2026 for a different corpus, applied here for the first time to the estate's own
engineering activity. Every checkable fact is sourced to the named site's own repository,
checked directly, on a stated date — never copied from another `*.sgit.ai` page's claim about
it.

Live site: https://newsroom.sgit.ai (GitHub Pages, deployed from `dev`).

## Structure

- `index.html` — front page: the thesis, the live-network table, the three roles
- `index.md` — the markdown twin of the front page
- `stories/` — every dated story, newest first; `network-launch.html` is the first: the network,
  live, checked against six sibling repositories on 22 August 2026, with one stale hostname
  found and corrected along the way
- `roles/` — Librarian, Journalist, Historian, as applied to this site's own remit
- `network/` — the sibling boundary table, and three open questions
- `admin/` — engineering: comms (open requests, in public), versions, build tooling
  - `admin/build/chrome.py` — the single definition of nav and footer, applied across every page
  - `admin/build/validate.js` — the pre-release gate
- `about/participant.html` — the participant disclosure: this site is published by the same
  project as everything it reports on, and states plainly where that means it is not an
  independent newsroom
- `assets/site.css` + `assets/nav.js` — the shared `sgit.ai` design language, carried over
  unchanged from `issues-fs.sgit.ai`

## Release process

1. Bump `admin/build/version.txt` (vX.Y.Z, exactly once per release) and add a row to
   `admin/versions.html`; update `admin/comms.html`.
2. `python3 admin/build/chrome.py` — propagates the version badge and any nav/footer change to
   every page, and stamps the version into `llms.txt` and `index.md`.
3. `node admin/build/validate.js`
4. `git commit -am "site vX.Y.Z: ..." && git push origin dev`

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate → auto-tag (`vX.Y.Z`,
verified against `version.txt` and the commit subject, next-minor enforced) → deploy to GitHub
Pages. Pull requests run validation only. Same pipeline as
[SGit-AI__Website](https://github.com/SGit-AI/SGit-AI__Website),
[SGit-AI__Website__PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI),
[SGit-AI__Website__Graphs](https://github.com/SGit-AI/SGit-AI__Website__Graphs) and
[SGit-AI__Website__Issues-FS](https://github.com/SGit-AI/SGit-AI__Website__Issues-FS).

### What the gate checks

Structure and version agreement, that every internal link resolves, that every page declares a
canonical on the host in `CNAME`, that every section hub is named in `llms.txt` and that the
sitemap and the tree agree both ways, that `<div>`s balance, that no vault-key-shaped string is
in the tree, and — inherited from issues-fs.sgit.ai — that every page carries a "for an agent"
block.

## v0.1.0 — what shipped, and what did not

This is the first release. **Unlike every sibling `*.sgit.ai` site, it was not built from a
commissioned brief pack** — no such document set exists for this site yet (open request N1 on
`admin/comms.html`). Rather than invent scope, v0.1.0 ships the pipeline — carried in unchanged
from issues-fs.sgit.ai, the same order that site's own v0.1.0 shipped in — plus the smallest
real content that could be built on checked facts alone: one story reporting the state of the
network on 22 August 2026, the three roles that do the checking, and the boundary with every
sibling site. Full detail on `admin/versions.html`.

## Licence

Two licences — see [`LICENSES.md`](LICENSES.md). Code Apache 2.0; site content CC BY 4.0.
Facts this site reports about a sibling site are cited to that site's own repository, not
reproduced wholesale.
