# Bringing my past work back: a build brief for the back-catalogue worker

*18 October 2026, written by newsroom.writer for the agent that builds it. Status: a brief; nothing in it is built. The article is [bringing my past work back](https://newsroom.sgit.ai/articles/bringing-my-past-work-back.html). The inventory below was taken on 18 October 2026 without logging in anywhere.*

## The ask

A worker that runs every day, takes Dinis's past work one item at a time, and writes two or three articles a day that bring it back as linkable, connected content on this site: what the work was, what it said, what has changed since, and how it connects to what this newsroom argues now. So that work which is not linkable today becomes linkable, the thinking has a continuous line, and the site has regular content, for the newsletter and for days Dinis is offline.

## The sources, in the order to work through them

| # | Source | Size | Read with | Licence |
|---|---|---|---|---|
| 1 | Essays at diniscruz.ai (canonical; docs.diniscruz.ai serves the same) | 103 essays, Feb 2024 to Oct 2025; 27 already cited here | `llms.txt`, the `.md` twin of each page, or the repository `DinisCruz/DinisCruz-AI__Website` | CC BY 4.0 |
| 2 | The NotebookLM repository `DinisCruz/NotebookLM__Infographics-and-slides` | 2,038 files; about 248 dated items, Jan to Mar 2026; decks, infographics, video overviews, links to the LinkedIn posts | a blobless clone, markdown and link files only | CC BY 4.0 |
| 3 | Talks: SlideShare `DinisCruz`, paired with the Leanpub books by topic | 65 public decks, 2010 to 2020; 10 books, free to read online, manuscripts in `DinisCruz/Book_*` | the page's embedded JSON; the book repositories | uploader terms; check each book repository |
| 4 | The tools at tools.sgraph.ai | 29 tools in production, 45 on dev | `/_common/js/sg-tool-registry.js`, then each tool's `manifest.json` | the repository's |
| 5 | The blog, diniscruz.blogspot.com (blog.diniscruz.com) | 1,289 posts, 2008 to 2018; labels O2 Platform, TeamMentor, OWASP, Philosophy, SecDevOps | the Blogger JSON feed, 150 at a time | none stated |
| 6 | YouTube: `@diniscruz-ai` and `@DinisCruz` | 152 recent videos; 69 from 2012 to 2013 | the channel feeds (latest 15 only) and oEmbed | YouTube's |
| 7 | graphs.sgit.ai | three books; already well covered here | `llms.txt` | CC BY 4.0 |
| 8 | Needs Dinis's export | LinkedIn posts and articles, X/Twitter, the NotebookLM notebooks themselves | his data exports, dropped into a vault | his |

Already done here, not to repeat: the Portugal series (the 2010 and 2016 talks, the 2024 OWASP Lisbon talk, the five Europe essays), the graphs books, books from articles, and the 27 essays cited somewhere.

## What leaves the queue

- **Material that is not his:** the NotebookLM repository's collaborator, third-party and strategic-partnership folders; a deck by another speaker on SlideShare; the repositories `Book__Empowering_You_To_Defend_Against_Cancer` and `Cruz-and-Cruz__Music`.
- **Personal or job material:** CV decks and job applications.
- **Employer and customer work** is read for what it says about the ideas, not republished; customers are not named unless the original was public and naming them is the point.
- **People:** the site's rules apply. A person named in an old piece is named only if they were named in public and it matters; never anyone on the private list.

## Each article

- Written in Dinis's voice, through the agent, as every article here; labelled in its front matter `from_archive: <source>` and with the tag `back-catalogue`.
- **What it was**: the original, with its date and link; a figure from the original where its licence allows, or a new one.
- **What it said**: the ideas, quoted exactly where a quote matters.
- **Then and now**: what has changed since, checked, with sources; where the original was wrong or is outdated, say so plainly.
- **How it connects**: links to the newsroom articles and graphs it anticipates or contradicts. This is the point of the exercise.
- The graph and the section summaries, as for every article.

## The register

`admin/content/back-catalogue.json`: one entry per source item (source, id, URL, date, status: queued, written, skipped with reason, needs export), and the article it became. The worker takes the next queued items, two or three a day, oldest unprocessed first within the order above, and never writes the same item twice. Skips carry their reason. Same pattern as the reviews and the briefs: one record per unit of work.

## The runner

A scheduled task each morning, like the wires: build the queue from the sources if it is stale, write the day's articles, run the site's checks (wording, widths, summaries, the leak scan), and release. If a source cannot be read, the run says so and moves to the next one, rather than producing a thin article.

## Order

1. The register, filled from sources 1 and 2.
2. Three articles from the essays, reviewed by Dinis, to set the shape.
3. The daily run.
4. Sources 3 to 6.
5. The exports, when Dinis provides them.

## Questions for Dinis

- Two or three a day, or one a day plus the wires?
- Which ten essays first?
- Can the exports (LinkedIn, X, NotebookLM) go into a vault this worker can read?
