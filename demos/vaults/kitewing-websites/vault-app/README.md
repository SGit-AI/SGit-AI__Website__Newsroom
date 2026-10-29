# Kitewing Websites (a fictional demonstration)

Kitewing Websites is a made-up web studio. This folder is its home page, built as a vault app for
[newsroom.sgit.ai](https://newsroom.sgit.ai/articles/websites-you-own.html) to show a business model for small
websites: one-off work, no monthly fee, and a site the owner keeps in their own accounts and changes by talking to Claude.
The studio, its prices, its clients and the town of Harrowby are all invented.

## What is in this folder

- `index.html`: the whole page. All styles and scripts are inline, pictures are inline SVG, and there are no
  external requests. It renders from `content.json`, and carries a copy of it inside so it also works when opened as a file.
- `content.json`: every word on the page (hero, how it works, prices, what you own, why no monthly fee, lift and shift,
  examples, questions, the footer notes).
- `app.json`: tells the vault to open `index.html` as an app.
- `examples/`: three fictional client sites built the same way: `tidewrack-pottery/`, `fennick-lane-garden/` and
  `quillon-heating/`.

## How the owner would change it

Ask Claude, in plain words, from the Claude account connected to the repository. For example: "change the price of the
larger site to £1,200", "add a question about email addresses to the FAQ", or "make the red a little darker". Claude edits
`content.json` (for words) or `index.html` (for layout and colours), and refreshes the copy of the content inside
`index.html`. GitHub keeps every version, so any change can be undone.
