---
id: 052
title: A wire in two languages: the EN/PT switch, kept per wire
kind: story
priority: high
created: 2026-10-13T23:05:00Z
source: the Portugal Wire's vault (wire.languages ["en","pt"], headline_pt, summary_pt, quote_lang), relayed by the owner on 13 October 2026
release: v0.12.32
estimated_effort: small
---
# A wire in two languages: the EN/PT switch, kept per wire
## Scenario
```gherkin
Given a vault whose wire.languages lists two or more languages
When I open the wire
Then a switch under the lens offers them, the first chosen
When I pick the second
Then every story's headline, summary and why-it-matters are drawn in it where the vault carries them, the first language otherwise
And a quote stays in the language of its source and says which
And the choice is remembered for this wire in this browser, and for no other wire
```

## Outcome
Shipped in v0.12.32: `wire/wire.js` (the switch, `tx()` picking `<field>_<lang>`), the contract on each how page names `languages`, `headline_<lang>`, `summary_<lang>`, `why_it_matters_<lang>` and `quote_lang` as optional; the snapshot carries `headline_pt` and the search indexes it. Checked in `test_wire.mjs` on the Portugal Wire.
