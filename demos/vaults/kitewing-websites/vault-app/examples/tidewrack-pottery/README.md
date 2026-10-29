# Tidewrack Studio Pottery (fictional demonstration)

This folder is a small website for **Tidewrack Studio Pottery**, a made-up ceramicist in the made-up town of
Harrowby. It is one of three example client sites for Kitewing Websites, a made-up studio, built as a
demonstration for the newsroom.sgit.ai article
[Websites you own, and can talk to](https://newsroom.sgit.ai/articles/websites-you-own.html).
The maker, the pieces, the classes and the prices are all invented.

## What is in the folder

- `index.html`: the whole site in one self-contained file (inline CSS, inline JavaScript, inline SVG drawings,
  no external requests). It reads `content.json` and, if that cannot be loaded (for example when the file is
  opened straight from disk), falls back to a copy of the same data inlined in the page.
- `content.json`: all the words and data: the maker's story, the 28 catalogue pieces (name, type, glaze, size,
  price or "on enquiry", status), the eight glazes and their colours, classes, open studio days and the care guide.
- `app.json`: tells the vault viewer to open `index.html` as an app.
- `README.md`: this file.

The catalogue has no checkout, by design: it is a static site. "Ask about this piece" shows a note asking the
visitor to enquire in the studio, quoting the reference number. There is no email address or form.

## How the owner would change it

The owner does not need to edit code. They ask Claude, which is connected to the site's repository, for example:

- "Add a new mug called Rock samphire mug, Sea glass glaze, 300 ml, £34."
- "Mark TW-07 as sold" or "Remove the moon jar until the next firing."
- "Add an open studio day on Saturday 24 April 2027."
- "Add a ninth glaze called Lugworm grey, a pale warm grey."

Claude edits `content.json` (and `index.html` if the layout needs to change), and GitHub keeps every version,
so any change can be undone.
