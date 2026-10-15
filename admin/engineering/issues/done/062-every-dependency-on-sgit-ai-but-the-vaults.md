---
id: 062
title: Every dependency on sgit.ai but the vaults: the footer first, and the report that counts the rest
kind: task
priority: high
created: 2026-10-14T18:40:00Z
source: the owner, in chat, 14 October 2026: "we need to remove every single dependency from skit.ai... the only thing... is the vaults... when we have an article that has a vault, we can link to the vault... Everything else has to be self-contained into the newsroom"
release: v0.12.52
estimated_effort: medium
---
# Every dependency on sgit.ai but the vaults

## What is asked
The newsroom stands on its own. The one link it keeps outside itself is to a vault, from the page that has one. Everything else (the footer's network line, the "part of the sgit.ai network" blurb, the front page imported from sgit.ai's build, and in the end the generator itself) goes.

## Outcome in this release
The root front page is this site's own (card 058). The footer's network line (sgit.ai, pt.newsroom, graphs, pki, nhi, docs.diniscruz.ai) and the "part of the sgit.ai network" sentence are gone from every page; the network keeps its own page. `admin/build/deps.py` writes `admin/notes/sgit-ai-dependencies.md`: by kind, generator (492 imported files), network (links, with the 16 files this site writes itself listed first), words (the name in prose: the disclosure, the kit, the method) and vault (allowed), so each release can show the count going down.

## What is left
The imported pages (articles, account, personas, newsletter, collections) link to sgit.ai's about page and docs from their bylines and kits; those are fixed in the generator when it moves here (the port to api.newsroom.sgit.ai is the next large card). The participant disclosure keeps naming the sgit project: it is a fact about the publisher, not a dependency.
