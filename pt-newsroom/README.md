# pt.newsroom.sgit.ai — the home page, as designed

The site does not exist yet. This section holds its front page as designed on 13 September 2026,
rendered as pages on this site so it can be seen at full size rather than as a picture.

| Page | What |
|---|---|
| `index.html` | The chosen design (a classic broadsheet, natively Portuguese) at 1440px and 390px |
| `directions.html` | All four directions drawn that day, with the motivation and trade-off of each; three were not chosen |
| `design/*.dc` | The artboard sources, verbatim (plain HTML; `.dc` so the site validator does not treat them as pages) |
| `design/canvas.json` | The canvas layout and the notes written beside each artboard |

## Build

```
python3 pt-newsroom/build/build.py     # renders both pages from design/
python3 admin/build/chrome.py
node admin/build/validate.js
```

The builder scopes each artboard's stylesheet under a per-artboard class so it cannot restyle the
site chrome or another artboard, swaps the Google Fonts links for the vendored faces in
`assets/fonts.css`, and edits nothing else. A change to a design is a change to its `.dc` file.

## Typefaces

Seven faces, all SIL Open Font License 1.1, latin subsets as woff2 under `assets/fonts/`, attributed
in `LICENSES.md`: Newsreader and IBM Plex Mono (the chosen design), Archivo and JetBrains Mono (B),
Space Grotesk (C, with Newsreader), Bodoni Moda and Karla (D). Loaded only by this section.

## What the copy is

The Portugal section's real data of 13 September 2026 — the three stories, the 60→64 speaker diff,
the seven press pages, the programme. It is not maintained: take the structure, not the numbers.
The design system for the chosen direction is section 16 of the commissioning brief,
`briefs/11__pt-newsroom-commissioning-brief.md`.
