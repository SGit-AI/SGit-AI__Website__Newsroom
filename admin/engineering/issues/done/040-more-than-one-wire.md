---
id: 040
title: More than one wire: the OWASP Wire and the AWS Wire beside the Industry Wire, each from its own vault
kind: story
priority: high
created: 2026-10-13T14:10:00Z
source: the owner, in chat, 13 October 2026, relaying the research agent's brief: two wires alongside /wire/, same contract as admin/build/wire-vault.json, /wire/owasp/ reading vault eitf274v and /wire/aws/ reading vault v202bla5, each bundle adding wire (title, beats) and optionally map (OWASP projects graph) and stack (AWS stack and deadlines); the lens dinis the named reader as before
release: v0.12.14
estimated_effort: medium
---
# More than one wire: the OWASP Wire and the AWS Wire beside the Industry Wire, each from its own vault
## What is asked
Two more vaults, built on the Industry Wire's pipeline, are to be read on this site at `/wire/owasp/` and `/wire/aws/`, under the same contract. Each bundle adds `wire` (the wire's title, cadence and beats), and one adds `map` (the OWASP projects graph: entities with aliases, facts, leaders and standards) and the other `stack` (the AWS services a reader runs, with aliases, what to watch and dated deadlines). The named reader is the same person, by the same agreement, extended.

## Scenario
```gherkin
Given a config admin/build/wire-vault.<slug>.json records a vault, its public read key and the named reader's agreement
When I open /wire/<slug>/
Then the edition is read from that vault with the same code and drawn the same way: the bar, the lens, the releases, the corrections, a decision per story
And the strip at the top names every wire and marks this one
And the lenses are the vault's own personas, all but the personal one, plus the named reader

Given the vault carries a map
Then a section under the bar lists its entities, each with its facts, leaders and standards, and the stories whose entities name it

Given the vault carries a stack
Then the edition's header lists its deadlines, soonest first, with the days left
And a section under the bar lists each service with the items the join says touched it

Given I read two wires in one browser
Then what one wire saw is not new on the other, each remembers its own lens, and a story id shared by two vaults is kept apart
```

## Mock-up
```
The wires: The Industry Wire · [The OWASP Wire] · The AWS Wire
EDITION OF 2026-10-13 · first edition: two weeks of OWASP, with September context
Editor's note …
▸ Projects graph: 20 entities, 12 named by a story in this edition
   ▸ OWASP Top 10 · project · flagship · 3 stories
       Level flagship · Latest release Top 10:2025 · Repository github.com/OWASP/Top10
       Leaders: … · Standards: CWE
       • The new owasp.org … · 2026-10-09
```

## Outcome
Shipped in v0.12.14 (built as v0.12.11 on the session branch, merged onto v0.12.13). `admin/build/wire.py` loads every `wire-vault*.json`, the Industry Wire first, and writes each wire's three pages and snapshot (`--from <slug>=<clone>`); the pages at `wire/<slug>/` load `../wire.js` and `../wire.css`, and the config block carries the slug and the path to the site root. `wire/wire.js`: the lenses from the vault's personas when the bundle has `wire`, the Industry Wire's six otherwise; `mapSection` and `stackSection`; the deadlines in the header; every link to the site through the config's `up`. `assets/vault-pane/wire-state.js`: a scope per wire for seen, visit and lens; a scoped seen id is stored as `slug:id`, and the device file carries it so. The nav, the footer, the search index (every snapshot), the API map, the hub, llms.txt and the README name the wires. `test_wire.mjs` runs for every wire recorded, with the map, the stack and the per-wire state checked. The note: `admin/notes/2026-10-13__more-than-one-wire.md`.
