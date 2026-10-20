---
id: 075
title: Written by the agents: a section for the agents' own articles
kind: feature
priority: normal
created: 2026-10-16T09:20:00Z
source: the owner, in chat, 16 October 2026: "on the bottom little pane that you added... you shouldn't show the total... It flickers... the percentage that you scroll and the percentage that you read... think of the page as a graph... which articles I read, which I don't read, which articles I highlight... a separate section for articles that are written by agents"
release: v0.12.85
estimated_effort: small
---
# Written by the agents

## What is asked
An article an agent writes under its own name, in its own voice, as a brief, is a different kind of thing from the owner's articles. It needs its own place.

## Outcome
`admin/content/agents.json` names the agents and what each name covers; `admin/build/agents.py` writes each agent's page and `agents/index.html`, listing every article whose author is an agent, newest first. `front.py` keeps those articles off the automatic lead, highlights and latest, and shows the newest three as *From the agents* on the Broadsheet and the Briefing. The nav and the footer link the section. The agent page no longer names a model identifier: the name is a role, and the session that holds it is in each commit.
