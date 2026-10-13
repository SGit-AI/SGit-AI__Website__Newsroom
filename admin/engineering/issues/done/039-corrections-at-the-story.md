---
id: 039
title: Corrections propagate on the wire: each corrected story carries its changes, the edition its corrections note
kind: story
priority: high
created: 2026-10-13T11:20:00Z
source: the wire's vault update of 13 October 2026 (release 2026-10-13.1): 13 stories of 11 October corrected after their primary sources were fetched, each with a dated entry in the story's changes[]; and this site's own argument that corrections must propagate
release: v0.12.14
estimated_effort: small
---
# Corrections propagate on the wire: each corrected story carries its changes, the edition its corrections note
## What is asked
The desk's second edition corrected thirteen stories of the first (the US executive order does not create the Super Intelligence Force; the NCSC page is Asos's primary; people with name and address protection were not in the Danish CPR breach; Mistral says only that open weights are "coming soon"). The vault records each correction in the story's `changes[]` with its date, and the brief carries a `corrections` note. The page showed none of it: a corrected story read like any other, and the only trace was the Updated flag, which lasts as long as the release that named it is the one shown. This site's argument is that a correction has to reach the reader where they read the claim, not in a note elsewhere.

## Scenario
```gherkin
Given a story in the vault carries changes with a date and what changed
When I open the wire
Then the story shows each change under its text, dated, as the vault records it
And it is flagged Updated when a release shown in the bar or the edition's updated_in_edition names it
And a story from an earlier edition says which edition it is from

Given the brief carries a corrections note
Then the edition's header carries it, after the editor's note

Given a story has no changes and the brief no corrections note
Then nothing is drawn for them and nothing breaks
```

## Mock-up
```
Trump creates 'Super Intelligence Force' led by DNI Jay Clayton…            [Updated]
2026-10-04 · Donald J. Trump (Truth Social) · first-party · confidence medium · from the edition of 2026-10-11
…
Why it matters: …
| 2026-10-13  Correction: the 29 September executive order (EO 14434) renames AI as
|             'Super Intelligence' but does not create the Force; the Force rests on
|             the Truth Social post and press reports.
```

## Outcome
Shipped in v0.12.14 (built as v0.12.10 on the session branch, merged onto v0.12.13): `wire/wire.js` draws `changes[]` under the story (`ul.changes`, each `li` with the date and the words), the brief's `corrections` in the edition's header (`.corrections`), the Updated flag from a release or from `updated_in_edition`, and the story's `edition` in its meta line when it is not the current one; `wire.css` gives corrections their own colour, the blue of Updated. The contract on `wire/how.html` names the three fields as optional. `wire/snapshot.json` now carries each story's edition and changes and the desk's latest release note, so an agent without a browser sees the corrections too. Checked by `test_wire.mjs` against the live vault: thirteen corrected stories on 13 October.
