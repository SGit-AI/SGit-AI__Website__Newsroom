# Fennick Lane Community Garden (fictional demonstration)

This folder is a small website for **Fennick Lane Community Garden**, a made-up community group in the made-up town
of Harrowby. It is a demonstration built for newsroom.sgit.ai, to go with the article
https://newsroom.sgit.ai/articles/websites-you-own.html . The garden, its members, events, rota and guides are all
invented. In the story, the site was built by Kitewing Websites, which is also a made-up studio.

## What is in the folder

- `index.html`: the whole site in one file. All styles, scripts and illustrations (inline SVG) are inside it. It
  makes no external requests, and it carries an inlined copy of the content so it still works when opened as a file.
- `content.json`: every word on the page: what we grow, plots and the waiting list, the season's events (15), the
  volunteer rota, news, and the growing guides library (14 guides, opened in a reader view).
- `app.json`: tells the vault host to open `index.html` as an app.
- `README.md`: this file.

## How the owners would change it

The garden committee would not edit code. They would open their own Claude account, which is connected to the
GitHub repository that holds this site, and ask in plain words, for example:

- "Add an event: bat walk on Friday 20 August, 8pm, meet at the lane gate."
- "Move Ruth to watering for the week of 5 July."
- "Write a new guide on growing garlic, in the same style as the others."
- "Add a news item saying the new shed roof is finished."

Claude updates `content.json` (and the inlined copy in `index.html`), and GitHub keeps every version, so any change
can be undone.
