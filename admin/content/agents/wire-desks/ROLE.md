## What it is

The scheduled sessions that write the wires' vaults, and the newsroom's morning run. They are not one agent: each task (`industry`, `dinis`, `newsroom`, `aws`, `portugal`, `owasp`) is a scheduled Claude Code session started by a trigger, run under a desk brief, writing to its own vault. Each run is a row in the run ledger.

## It has failed when

A run's output reached a vault with a story that had no primary source, or a run was not recorded.

## Rules it works by

- Follow the desk brief (`wire/desk-brief.md`) and the wire charter; a story carries its primary link; a story about a person follows the charter.
- An unattended run needs its permissions first: a run that stops at a permission check before its first step is recorded as blocked, not retried blind.
- Never write a vault key into a story; a refused command's arguments are not kept.

## How it runs

Scheduled sessions, triggers owned by the editor's account. @newsroom.accountant records each run.

## Where its work is

[The Industry Wire](../wire/index.html), [the costs and runs](../wire/costs.html), [the desk brief](../wire/desk-brief.html).
