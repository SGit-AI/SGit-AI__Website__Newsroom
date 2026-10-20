---
id: 038
title: Colour is a token: the design guidance, and the gate that keeps it
kind: task
priority: normal
created: 2026-10-13T14:00:00Z
source: the owner, in chat: "take the opportunity to improve areas like documentation, design guidances"; and the agent's own reading of the stylesheets while building card 036
release: v0.12.12
estimated_effort: small
---
# Colour is a token: the design guidance, and the gate that keeps it

## What is asked
Five themes only work if every colour on the site comes from one place. Before this card the stylesheets this site owns wrote their colours as literals with a fallback in a few places and as bare hexes in most: `#0f6b4f` in the vault pane, `#1c1d21` as a badge fill in search and the wire, `#101114` in the reading meter. Each would have stayed its light-theme colour in Night. The rule was nowhere written down, and nothing checked it.

## Scenario
```gherkin
Given a stylesheet this site owns
When it names a colour
Then it names a token, var(--head) and not #101114
And the token is defined in assets/themes/themes.css in all five themes
When a stylesheet breaks the rule, or a theme leaves a token out
Then node admin/build/test_themes.mjs fails, and so does CI
Given someone new, a person or an agent, is asked to style a page
Then assets/themes/README.md tells them the tokens, what each is for, what stays literal and why, and how to add a theme
```

## Mock-up
A table of tokens with their meaning; a short list of what stays literal; the three steps to add a theme.

## Outcome
Shipped in v0.12.12. The stylesheets this site owns (site.css, the vault pane, search and ask, the wire, the reading lists, the passkey lab, the engineering pages) read tokens, with their Newsprint value as the fallback where the file already used fallbacks. The reading meter is v1.4.1, the same component with its last five literals made tokens; a component path is immutable, so the change is a new path and `sync_newsroom.py` points every page at it. The guidance is `assets/themes/README.md`; the gate is sections 1 and 2 of `admin/build/test_themes.mjs`. Three things stay literal on purpose and the README says why: the terminal palette, the status dots and the amber flag, and the print page. The README of the repository and `admin/index.html` name the new files.
