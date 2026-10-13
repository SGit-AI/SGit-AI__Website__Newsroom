---
id: 037
title: The top bar on one row: eight groups, one cluster of tools, measured breakpoints
kind: bug
priority: high
created: 2026-10-13T13:30:00Z
source: the owner, in chat, with a screenshot of an article at 2000px wide: nine groups, five tools and the version on the bar, GitHub alone on a second line; "can you also clean up the top menu"
release: v0.12.12
estimated_effort: small
---
# The top bar on one row: eight groups, one cluster of tools, measured breakpoints

## What happens
By v0.12.11 the bar carried nine groups (Newsroom, Industry Wire, Account, How it runs, Design, Replicate, World News Day, Archive, About), Search, the balance, Vault, GitHub and the version, and on the legacy pages a "part of sgit.ai" pill. At 2000px it still wrapped: GitHub sat alone on a second row. Two stylesheets owned the bar's layout and disagreed: sgit.ai's (assets/newsroom.css, which this site cannot edit) collapsed it to the phone menu at 820px and the legacy one (assets/site.css) at 1200px, and neither knew about the tools this site had added. Adding the theme pill (card 036) would have made it worse.

## Scenario
```gherkin
Given a viewport of 1200px or wider, in either look
Then the bar is one row: the brand and the version, the groups, and one cluster of tools on the right
Given a viewport narrower than 1200px
Then the groups collapse behind Menu and the tools stay on the bar
Given a phone
Then the bar is two rows on purpose: the brand and Menu, then the tools
And nothing at any width is wider than the viewport
```

## Mock-up
`newsroom.sgit.ai  v0.12.12 | Newsroom · Industry Wire · Account · How it runs · Design · Replicate · Archive · About | [Search] [£5.00] [Vault] [● Newsprint] [★]`

## Outcome
Shipped in v0.12.12. `assets/site-nav.css`, loaded by chrome.py on every page in both looks, owns the bar's layout: the tools are one flex item (`.nav-tools`) so they move together and never split; the collapse is at 1199px for both looks, found by a sweep of widths (`node admin/build/shots_themes.mjs --sweep`: eight groups plus the tools fit at 1200 and not at 1181); GitHub is its star below 1400px; a phone is two rows by design, the brand and Menu above the tools. Eight groups, not nine: World News Day moved under Archive, where the footer already had it, and the "part of sgit.ai" pill went, because the footer's network line says it on every page. `admin/build/test_themes.mjs` section 4 sweeps the widths and fails on a second row at 1200 or above, or on overflow at any width.

## Screenshots
![The bar at 2000px, one row](../shots/037-bar-2000.png)
![The bar at 1440px](../shots/037-bar-1440.png)
![The bar at 1280px, GitHub as its star](../shots/037-bar-1280.png)
![At 1200px, the last width on one row](../shots/037-bar-1200.png)
![At 1199px, collapsed behind Menu](../shots/037-bar-1199.png)
![On a phone, two rows by design](../shots/037-bar-390.png)
