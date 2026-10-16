---
id: 068
title: The desks run unattended: one wording for the four, Sonnet as the model, and what the permission check refused, recorded
kind: story
priority: high
created: 2026-10-16T12:00:00Z
source: the owner, 16 October 2026: "the industry wire now runs nicely, but the other two don't... it says it's data exfiltration... it's not data exfiltration, it's memory... try to do this with Sonnet"
release: v0.12.74
estimated_effort: small
---
# The desks run unattended: one wording for the four, Sonnet as the model, and what the permission check refused, recorded
## Scenario
```gherkin
Given the desks' scheduled runs, of which the AWS and Portugal ones were refused at the install or the clone on 16 October
When their prompts are brought into line with the Industry Wire's (the clone key without its prefix, as the owner wrote it), say in plain terms what the run is and who authorised it (the owner's own vault on the owner's own server, the wire's memory, public news in it), and install and clone in separate commands
Then the runs reach their vaults, and every run's report says which command, if any, was refused and whether a retry went through
And every desk runs on Sonnet, with its verifier on a different model (Haiku)
```

## Outcome
The four desks' prompts updated on 16 October 2026 (Industry, AWS, Portugal, OWASP), all on Sonnet; the AWS and Portugal runs fired again the same day to test. Tested the same day: the AWS re-run published its edition (53 new stories, the Friday digest) on Sonnet for $2.58 with nothing refused, against $10.06 for the Industry run on Opus that morning; the Portugal re-run, under the same wording, had its clone refused three more times ("Code from External"). So the wording helps and does not settle it. The durable fix is the owner's: pre-installing the sgit client in the desks' environment and allowing `sgit clone` and `sgit push` to the owner's server in the tasks' settings, so no run depends on a retry.
