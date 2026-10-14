---
id: 036
title: Dark mode, and four more: five themes, chosen once and kept in this browser
kind: story
priority: high
created: 2026-10-13T13:02:00Z
source: a reader of the wire, on WhatsApp, 13 October 2026, 13:02, replying to the owner's link to /wire/: "Dark mode! 😁"; the owner's ask, "add 5 themes like what we did with VoiceDebrief.ai"
release: v0.12.12
estimated_effort: medium
---
# Dark mode, and four more: five themes, chosen once and kept in this browser

## What is asked
The site has had one look since v0.6.0, warm off-white and teal. The first reaction to the wire from outside was two words: dark mode. VoiceDebrief shipped five colour schemes behind one control in its bar (Signal, Night, Paper, Blueprint, Ember), and the owner asked for the same here.

## Scenario
```gherkin
Given I open any page of the newsroom
Then the bar has a theme pill beside Search and Vault, showing a swatch and the name of the theme I am in
When I open it
Then it lists five themes, each with its swatch, its name and three words on what it is
When I choose Night
Then the page repaints dark before my eyes, and every page I open next is dark too
And the choice is kept in this browser and nowhere else
Given I have chosen nothing and my system is set to dark
Then the newsroom opens in Night
Given something writes a value that is not a theme into the stored key
Then the page is Newsprint, not broken
When I print
Then the page is Newsprint on white, whatever theme I read in
```

## Mock-up
The pill: `● Night ▾`. The list, right-aligned under it: Newsprint (warm off-white, teal), Night (dark, teal), Paper (warm cream, terracotta), Blueprint (white, electric blue), Ember (dark, amber); the current one in the accent and bold.

## Outcome
Shipped in v0.12.12. `assets/themes/themes.css` defines the five (every token in every theme), `assets/themes/themes.js` sets `data-theme` on `<html>` before the first paint and draws the picker, and `admin/build/chrome.py` loads both first in the nav block on all 601 pages. sgit.ai's stylesheet, which this site must not edit, writes forty-odd literal colours; section B of the themes file restates each of those rules with a token, so Newsprint is pixel for pixel what it was and the other four reach every heading. The stylesheets this site owns were rewritten to tokens (card 038). The reading meter went to v1.4.1 for its last five literals. `admin/build/test_themes.mjs` checks the picker, the memory, the contrast in every theme (ink, text, headings, links at 4.5:1 on the page; the ink on the accent at 4.5:1), and that every theme defines every token. `admin/build/shots_themes.mjs` took the pictures. The article: [Dark mode, and four more](../../articles/dark-mode-and-four-more.html).

## Screenshots
![The picker open, on the wire in Night](../shots/036-picker.png)
![The wire in Night](../shots/036-night-wire.png)
![The wire in Paper](../shots/036-paper-wire.png)
![The wire in Blueprint](../shots/036-blueprint-wire.png)
![The wire in Ember](../shots/036-ember-wire.png)
![The five together](../shots/036-collage.png)
