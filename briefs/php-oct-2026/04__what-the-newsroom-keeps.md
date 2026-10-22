# 04: What the newsroom keeps, and how the two sites link

## The split

| | php.oct.2026.newsroom.sgit.ai | newsroom.sgit.ai |
|---|---|---|
| What | The facts: claims with a status, sources, timeline, numbers, agencies, inventory, briefings by role | Context and opinion: what the story means, how it was covered, what it says about disclosure, AI-found flaws and newsrooms |
| Voice | No first person; fact-driven | Dinis's voice, through the agents, or an agent under its own name |
| Evidence | Reads the vault; publishes hashes, never captures | Links to your pages for every fact |
| Releases | Your gate, your `release.sh` | Its own gate and release process |

## Links from the newsroom to you

- **The front page:** a "Developing story" strip in all three views, with your title, a dek, your
  version, your source count and your `data_as_of`. From `status.json` once it exists; until then from
  `data/vault.json` and `data/versions.json`.
- **Articles:** the first is `capture-first`, included here. Later articles link to your pages for each
  fact, by URL. Please keep your URLs stable, and if a page must move, leave a pointer.
- **`/php-flaws/`:** until retired, it shows a "This story has its own site" panel at the top, with the five
  checks and their state.

## Links from you to the newsroom (requests)

- Your README already links to `newsroom.sgit.ai/php-flaws/`. Once that is a pointer, please link to the
  article `https://newsroom.sgit.ai/articles/capture-first.html` instead, as the account of how the
  coverage started, and keep a link to the newsroom's front page in your footer.
- Breadcrumbs already go up to "October 2026" and the newsroom. Keep them.

## Corrections

If the article gets a fact about your site wrong, open an issue on
`SGit-AI/SGit-AI__Website__Newsroom` or tell Dinis. The fix is a new version of the article, with its
diff page.
