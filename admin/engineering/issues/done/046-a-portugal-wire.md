---
id: 046
title: A Portugal wire: the same beats, Portuguese sources and stories, under the same contract
kind: story
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: one more news feed, for Portugal, same topics, AI governance and so on; a source of material for the Portuguese publication
release: v0.12.32
estimated_effort: medium
---
# A Portugal wire: the same beats, Portuguese sources and stories, under the same contract
## Scenario
```gherkin
Given a vault for the Portugal wire exists under the contract, with wire.id "portugal"
When its read key reaches the owner
Then admin/build/wire-vault.portugal.json records it and the named reader's agreement
And /wire/portugal/ reads it with no other change
```

## Outcome
Done the same day. The desk built the vault (`p6twygul`, two commits: the first edition and the verifier's fixes to four stories, in `wire-factcheck/v1`) and the owner relayed its read key in chat on 13 October: 36 stories from 29 September to 13 October across the five beats, each with its headline and summary in English and Portuguese and its quote in the language of its source; 45 Portuguese sources; an ecosystem map of 40 organisations. Shipped in v0.12.32 as `admin/build/wire-vault.portugal.json`, one config file as the card said, plus what the bilingual bundle asked of the page (card 052): the language switch. The desk also scheduled its own daily run at 05:58 London, with pitches for pt.newsroom on Mondays.
