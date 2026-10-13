# Five themes, and the bar on one row

*A design note, 13 October 2026, for v0.12.12 (cards 036, 037, 038). What was decided and why, in the order the decisions were made. The guidance that came out of it is `assets/themes/README.md`.*

## The ask

A reader of the wire replied to the owner's link with two words, "Dark mode!", and the owner asked for the five colour schemes VoiceDebrief ships, done here; then, with a screenshot of the bar wrapping at 2000px, to clean up the top menu; then to use the occasion to improve the documentation and the design guidance.

## Constraint one: the imported stylesheet cannot be edited

The newsroom's look is `assets/newsroom.css`, sgit.ai's stylesheet, imported on every sync, and `validate.js` check 11 fails the build if an imported file changes. It defines fifteen colour tokens in `:root` and then writes forty-odd literal colours in its rules: `#101114` on every heading, `#34363c` on every paragraph, `#fff` on every accent fill. Redefining the tokens alone would have produced a dark page with black headings.

The answer is a layer that loads after it and shadows exactly those rules: same selector, same specificity, later in the cascade, with a token whose Newsprint value is the literal. The list was generated, not guessed: a twenty-line script parses the stylesheet and prints every rule with a literal and its declarations, and the map in `themes.css` section B is that list, in file order, so a re-import is a diff and not a hunt. The stylesheets this site owns were rewritten to tokens instead, because they can be.

## Constraint two: the first paint

A theme that arrives after the first paint is a flash of Newsprint on every page, which is worse than one look. chrome.py only writes the nav and footer blocks, not `<head>`, and the nav block is the top of `<body>`. So the stylesheet and a classic, blocking script are the first three lines of the nav block: by the time the parser reaches the first heading, `data-theme` is on `<html>` and the theme's rules are loaded. VoiceDebrief puts its script in the head for the same reason and says so.

## Which five

Not VoiceDebrief's five copied: the newsroom's own tokens, extended. Newsprint is the look since v0.6.0 and stays the default, pixel for pixel, so nobody who does not open the picker sees a change. Night is the ask: dark, with the teal lifted two steps so it holds 4.5:1 on the dark page. Paper, Blueprint and Ember are the three moods VoiceDebrief found worth having, warm, cool and warm-dark, drawn with this site's structure. Every theme states its contrast and the test measures it rather than trusts it: ink, text, headings and links on the page, and the ink on the accent, all at 4.5:1.

One naming decision is worth recording. The heading token is `--head`, not `--ink`, because the deck viewer in the imported stylesheet already reads `var(--ink)` as the colour of a dark bar, and a heading token that is near-white in Night would have turned that bar white under its white text. VoiceDebrief's tokens file describes exactly this conflation in its own bridge layer. A token is named for what it is for.

## What stays literal

The terminal palette and the dark panels on it: a transcript is dark the way a terminal is, in every theme. The vault button's three status dots and the wire's amber "new" flag: signals, not surfaces, and each carries its own dark ink, which was the one place the rewrite had to be undone by hand (a light `--fg` on an amber fill). The print page: white, always, with the Newsprint tokens restated under `@media print`.

## The bar

The screenshot showed the problem: nine groups, five tools, the version and (on legacy pages) a "part of sgit.ai" pill, and the two stylesheets collapsing the bar at different widths, 820 and 1200, with neither knowing about the tools this site had added. The fix is one stylesheet for the bar's layout in both looks, loaded with the themes, and three cuts: World News Day under Archive (the people its outreach writes to land on its pages by the links in that outreach, which a top-level group never carried), the parent pill gone (the footer's network line says it), and the tools as one flex item so they move as one and never split. The breakpoints are measured by a sweep of widths and asserted by the test: one row at 1280 and up, Menu below, and on a phone two rows by design: the brand and Menu, then the tools. The first measurement said 1200, on this machine's fonts, and CI's Ubuntu fonts broke the row at exactly that width; a limit measured on one machine is not a limit, so it moved to 1280 with the difference as slack (v0.12.13).

## The gate

A theme with a hole inherits Newsprint's value for it silently. So the test reads `themes.css`, takes the union of tokens, and fails on any theme missing any; and it reads every stylesheet this site owns and fails on a literal colour outside the allowed signals. This is VoiceDebrief's `check_themes.py` rule, carried over because it is the one that keeps the other decisions true after the people who made them have moved on.

## What was not done

The imported stylesheet still carries its literals; only the map shadows them, and the map has to be checked against each re-import. The meter is at v1.4.1 for its five literals; the component base and the vault library are vendored and untouched. No theme is offered per persona, though `--pc` exists and a persona's colour could become a sixth entry. The choice is not carried by the vault between devices, on the view that a theme belongs to a screen, which a reader may disagree with.
