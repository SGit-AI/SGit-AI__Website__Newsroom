---
id: 032
title: CI: the R2 check read the meter after a fixed wait, and failed on a slow runner
kind: bug
priority: high
created: 2026-10-13T10:30:00Z
source: CI of v0.12.6, 13 October 2026: reader-tests failed on R2 in test_review.mjs; v0.12.6 deployed and was not tagged
release: v0.12.7
estimated_effort: small
---
# CI: the R2 check read the meter after a fixed wait, and failed on a slow runner
## What happens
The review test pins finding R2 (a persona without on[] and off[] leaves the personas page blank) by opening the page, waiting 1.5 seconds and reading the meter. Since v0.12.6 every page with the meter loads two more small modules for the vault pane; on the CI runner the meter was not ready at 1.5 seconds, the check read a state that was not the finding, and the job failed. Locally it passed.

## Scenario
```gherkin
Given the personas page is opened with a persona that has no lists
When the check runs
Then it waits until the meter says it is ready or failed, up to 20 seconds
And then reads the page as before
```

## Outcome
Shipped in v0.12.7: the check waits for the meter's data-state instead of a fixed time. The finding itself is unchanged and still pinned.
