# newsroom.sgit.ai — the sgit.ai network reports on itself

> Six sites now carry the `*.sgit.ai` name. Nobody was writing down what each one actually
> ships, at what version, checked against its own repository rather than copied from a
> sibling's footer. That is this site's job — written by the **Librarian, Journalist and
> Historian**, three roles [defined at issues-fs.sgit.ai](https://issues-fs.sgit.ai/roles/index.html)
> in February 2026 for a different purpose, applied here for the first time to the estate's
> own engineering activity as the corpus.

*Source: <https://newsroom.sgit.ai/index.html> · site v0.1.0 · markdown twin of the front page.*

---

## Live in the network today

Checked directly on 22 August 2026 — each site's own `CNAME` and `admin/build/version.txt`
(or, for sgit.ai, `build_pages.py`'s `SITE_VERSION`), not a claim repeated from another site's
page.

| Site | Version | What it is |
|---|---|---|
| [sgit.ai](https://sgit.ai) | **v0.2.39** | The parent: the vault layer and the shipped CLI |
| [graphs.sgit.ai](https://graphs.sgit.ai) | **v0.3.18** | The graph philosophy at length, and as a book |
| [issues-fs.sgit.ai](https://issues-fs.sgit.ai) | **v0.1.1** | Git-native issue tracker; origin of this site's roles |
| [pki.sgit.ai](https://pki.sgit.ai) | **v0.1.24** | Public-key identity and trust |
| [nhi.sgit.ai](https://nhi.sgit.ai) | **v0.1.19** | Non-human identity |
| [sg-sentinel.sgit.ai](https://sg-sentinel.sgit.ai) | **v0.1.1** | Newest sibling before this one |
| **newsroom.sgit.ai** | **v0.1.0** | This site. First release |

One correction shipped with this: a sibling's own network page names a site `sentinel.sgit.ai`;
its repository's actual `CNAME` reads `sg-sentinel.sgit.ai`. [Full story, with the method
used](https://newsroom.sgit.ai/stories/network-launch.html).

## Three roles, one corpus

- **Librarian** — finds the primary source for a claim and cites it, rather than repeating a
  sibling site's claim about itself.
- **Journalist** — writes the dated story: what shipped, what changed, what it means.
- **Historian** — keeps the record after the story ages, for later readers and agents.

[The full page](https://newsroom.sgit.ai/roles/index.html).

## The boundary, stated plainly

[issues-fs.sgit.ai](https://issues-fs.sgit.ai) owns the role definitions and is where
Librarian, Journalist and Historian were written. This site owns applying them to the
network's own activity — dated stories, checked facts, a running record. [The full boundary
map, with every sibling](https://newsroom.sgit.ai/network/index.html).

## For an agent

Every version number above was read directly from the named site's own repository on 22
August 2026 — treat it as a snapshot, not a live value. This site is published by the sgit
project and reports on the sgit project: read the [participant
disclosure](https://newsroom.sgit.ai/about/participant.html) before treating any page here as
neutral. [llms.txt](https://newsroom.sgit.ai/llms.txt) is the whole agent surface.
