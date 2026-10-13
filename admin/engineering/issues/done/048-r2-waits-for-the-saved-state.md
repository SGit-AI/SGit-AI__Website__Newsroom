---
id: 048
title: R2 waits for the charged page to save its state, not a fixed time
kind: bug
priority: high
created: 2026-10-13T17:40:00Z
source: the first run of v0.12.20 in CI (run 77): test_review.mjs failed R2 on the runner after passing twice on the same tree in the session; the check waited 1.2 s for a charged page to save the meter's state before pushing a broken persona into it
release: v0.12.21
estimated_effort: small
---
# R2 waits for the charged page to save its state, not a fixed time
## What happens
`test_review.mjs` pins finding R2: a persona without `on[]` and `off[]` leaves the personas page blank. To set it up, the test opens a charged article, waits 1.2 seconds, reads the meter's saved state, pushes a broken persona and saves it back. On a loaded runner the meter had not saved yet when the state was read and written, so the meter's own save then overwrote the broken persona, and the personas page was not blank. The same test already waits for the personas page by condition, not time, since card 032's lesson (v0.12.7: "on a slow runner 1.5 s was not always enough").

## Scenario
```gherkin
Given the review test opens a charged article to set up R2
When the runner is slow
Then the test waits until the meter has saved a state with the read logged, up to twenty seconds, before it pushes the broken persona
And R2 pins the same behaviour as before
```

## Outcome
Shipped in v0.12.21: the fixed wait becomes a `waitForFunction` on the saved state (`sgit.meter.v1` with a `personas` array and a logged read), then a short settle. The finding and its check are unchanged; only the set-up waits by condition. Run 77's deploy had gone out (the deploy job needs only the validator), so the site was live at v0.12.20 without its tag; the tag job backfills it on this push. Neither a re-run of the failed job nor a manual dispatch was open to the session's integration (403), which is why this is a release and not a re-run.
