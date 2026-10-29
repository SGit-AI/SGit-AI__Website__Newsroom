# Quillon Heat & Plumbing (fictional demonstration)

This folder is a small website for **Quillon Heat & Plumbing**, a made-up heating and plumbing firm in the made-up town of Harrowby. It was built by **Kitewing Websites**, which is also made up, as a demonstration for the newsroom.sgit.ai article [Websites you own](https://newsroom.sgit.ai/articles/websites-you-own.html).

Nothing here is real: the business, the villages, the guides and the phone number (01632 960 418 is in a range reserved for drama and does not connect). There are no customer reviews or testimonials on purpose, because any review of an invented business would be invented too.

## What is in the folder

- `index.html`: the whole site in one file (styles, icons drawn in inline SVG, and the script). It also holds a copy of the content so it opens on its own.
- `content.json`: the words. Services, opening hours, areas covered, emergency steps, the 19 household guides and the questions.
- `app.json`: tells the vault to open `index.html` as an app.
- `README.md`: this note.

The household guides are general guidance, sample text for a demonstration, not professional advice. Anything involving gas points the reader to a Gas Safe registered engineer.

## How the owner would change it

The owner does not need to edit code. They open their Claude account, which is connected to the site's repository, and ask in plain words, for example:

- "Add Thornby to the villages we cover, weekdays only."
- "Change Saturday hours to 9am to 12pm."
- "Write a new guide on what to do when the hot water runs out, in the same style as the others."

Claude edits `content.json` (and the copy inside `index.html`), and the repository keeps every earlier version, so any change can be undone.
