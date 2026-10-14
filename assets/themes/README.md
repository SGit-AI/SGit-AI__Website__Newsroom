# The themes, and the rule for colour on this site

*Design guidance for anyone, person or agent, who writes a stylesheet for newsroom.sgit.ai. Since v0.12.12 (cards 036, 037, 038).*

## What a reader sees

A **theme** pill in the top bar, beside Search and Vault, showing a swatch and the name of the theme the page is in. It opens a list of five, each with its swatch, its name and three words on what it is:

| key | name | what it is | for |
|---|---|---|---|
| `newsprint` | Newsprint | warm off-white, teal | the default; the look the site has had since v0.6.0 |
| `night` | Night | dark, teal | the dark mode that was asked for |
| `paper` | Paper | warm cream, terracotta | long reads with the lights down |
| `blueprint` | Blueprint | white, electric blue | the cool, high-contrast one |
| `ember` | Ember | dark, amber | a warm dark, where Night is a cool one |

The choice is kept in this browser (localStorage, key `newsroom.theme`) and nowhere else: it is a property of the screen in front of the reader, so the vault does not carry it between devices. With nothing chosen, a system set to dark gets Night and anything else gets Newsprint; the first choice ends that. Print is always Newsprint on white.

## How it works

Three files, all loaded on every page by `admin/build/chrome.py` as the first things in the nav block, which is the top of `<body>`:

1. `assets/themes/themes.css` defines every colour token in every theme (`:root[data-theme="night"] { ... }`), restates the rules of sgit.ai's stylesheet that carry literal colours (see below), and styles the picker.
2. `assets/themes/themes.js` is a classic, blocking script. It reads the stored key, checks it against the list of five, sets `data-theme` on `<html>`, and later draws the picker into `<div class="theme-pick">`. It runs before the first paint, so a page opens in the reader's theme rather than in Newsprint with a flip. `window.__newsroomTheme` is the API (`get`, `set`, `themes`), and `newsroom:theme-changed` is the event.
3. `assets/site-nav.css` is the bar's layout in both looks (card 037), not a theme file, but it travels with them.

## The rule

**A stylesheet on this site names a colour through a token, and a token is defined in `themes.css`, in all five themes.** Not `#101114` but `var(--head)`; not `#fff` on an accent fill but `var(--on-accent)`. The test, `admin/build/test_themes.mjs`, fails the build on a literal colour in a stylesheet this site owns and on a token any theme leaves out, because a theme with a hole inherits Newsprint's value for it silently, which is how a dark theme ships with one light panel that nobody can explain.

The tokens, with what each is for:

| token | meaning |
|---|---|
| `--bg` `--panel` `--panel2` | the page, a card on it, a second surface (table heads, bands) |
| `--line` `--line2` | hairlines, and the borders of controls |
| `--fg` `--dim` `--dim2` | the default ink, secondary text, tertiary text |
| `--head` `--text` `--code-ink` | headings, paragraphs in a document, inline code |
| `--accent` `--accent-dk` `--on-accent` | the accent as a fill or a mark, the accent as a link, the ink on an accent fill |
| `--tint` `--tint-line` `--tint-solid` | the accent as a pale background, as a pale border, and as an opaque pale fill (a badge) |
| `--mute-bg` `--input-bg` `--mark` | a neutral chip, an input, a highlight |
| `--warm` `--yellow` `--red` | the three signal colours as text |
| `--warn-bg` `--warn-line` `--warn-ink` | a warning box |
| `--danger-bg` `--danger-ink` `--info-bg` `--info-ink` | a red tag, a blue tag |
| `--nav-bg` `--shadow` `--shadow-pop` | the bar's translucent background, the resting shadow, the shadow of a menu |
| `--swatch` | the theme's own colour, for a picker to show |
| `--term-*` | the terminal palette, dark in every theme on purpose |

What stays literal, and why: the terminal palette and the dark panels built on it (a transcript is dark the way a terminal is); the vault button's three status dots and the wire's amber "new" flag, which are signals, not surfaces, and carry their own dark ink; the print page, which is white.

`--head` is deliberately not called `--ink`. sgit.ai's deck viewer reads `var(--ink)` as the colour of a dark bar; a heading token that is near-white in Night would have turned that bar white under its white text. A token's name must say what the colour is *for*, not what it looks like in one theme.

## The imported stylesheet

`assets/newsroom.css` is sgit.ai's and this site must not edit it (`validate.js` check 11). It writes forty-odd literal colours: `#101114` on every heading, `#34363c` on every paragraph, `#fff` on every accent fill. `themes.css` section B restates each of those rules, same selector, same specificity, later in the cascade, with the token whose Newsprint value is that literal. So Newsprint renders as it did, and the other four themes reach every heading. When sgit.ai's stylesheet changes, the list to check is `python3 -I <the literals script>` over it: every rule with a literal is a rule the map must shadow. A stylesheet this site owns that reuses one of those class names (`.btn`, `.chip`) must outrank the map by specificity (`body .btn`), or the map's ink wins over its own; the wire's button went white on white that way on the first screenshot.

The reading meter is a shadow-DOM component and reads the page's tokens through the shadow boundary, which custom properties cross. Its own five literals were made tokens in v1.4.1 of the component; a component path is immutable, so the change is a new path (`sync_newsroom.py` item 11).

## Adding a theme

1. Add a `:root[data-theme="<key>"]` block to `themes.css` with every token. Check the contrast the test checks: ink, body text, headings and links at 4.5:1 on the page, and the ink on the accent at 4.5:1 on the accent.
2. Add the key, label and note to `THEMES` in `themes.js`, and a `.sw-<key>` swatch rule to the picker section.
3. Run `node admin/build/test_themes.mjs` and `node admin/build/shots_themes.mjs`, and look at the pictures.
