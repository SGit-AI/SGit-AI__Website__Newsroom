# The Librarian's daily brief: a build brief

*18 October 2026, written by newsroom.writer for the agent that builds it. Status: a brief; nothing in it is built. The article is [the Librarian's daily brief](https://newsroom.sgit.ai/articles/the-librarians-daily-brief.html). Facts checked on 18 October 2026.*

## The ask

Every morning, a brief for Dinis of everything that happened in his universe the day before, and a debrief of what the agents did: across every repository and organisation, the pull requests (his and other people's), the releases, the scheduled runs and what they cost, the cloud sessions and what each did, the reviews, the briefs that moved. Then what is coming soon, major events in his field, and the threads he started and left that are worth returning to now. So that he can work on many things at once without losing any of them, and choose each day where his highest leverage is. Mainly for him; others may read it.

## The role

The Librarian is a role this site already names but has never run: findability waits on it for unmapped tags, the briefs map has entries for it to keep one vocabulary, and the newsroom's policies borrow its principle from the SG/Send team, *flag, do not fix*. This gives it a daily job.

- **Reads:** everything below. **Writes:** only its own folder, `admin/content/librarian/<YYYY-MM-DD>.md` and `.json`, and a line in the run log. **Never:** edits anything else, sends anything, contacts anyone, merges or closes anything. It flags; others fix.
- Add `newsroom/roles/librarian.md` and its row in the roles table. The checker the policy page describes, `admin/build/policy_check.py --role <role>`, is in the sgit.ai repository, not this one: port it here first, so the Librarian's write limit is enforced, not only written.

## The sources, and how to read each

| Source | Read with | Note |
|---|---|---|
| Repositories and organisations: DinisCruz, SGit-AI, the-cyber-boardroom, Risk-Mandate, owasp-sbot, OpenSecuritySummit | GitHub search (`org:X updated:>=<yesterday>`, `is:pr`, `is:issue`) and the repositories' commits | The events API covers only 30 days and up to 300 events, can lag up to 6 hours, and no longer lists the commits in a push; use search and the commits endpoints for an exact yesterday. A personal token gives 5,000 requests an hour. |
| Outside contributions | `is:pr involves:DinisCruz` and the watched repositories (ruvnet/ruflo and others in a watch list) | Mondweep's Ruflo PR is the pattern to catch. |
| Releases of this site | `admin/engineering/releases/v*.md` by date | Already one file per release. |
| Scheduled runs and costs | `admin/build/wire-runs.json` (the accountant's ledger) | Includes runs blocked by refused fetches or clones: report those first. |
| Cloud sessions | the remote-session tools (`list_sessions`, `get_session`, `list_events` with `kinds: ["result"]`) | The same calls `runs_ledger.py` uses. |
| The briefs map | `admin/content/briefs.json` | Status changes since yesterday; open briefs untouched for longest. |
| Reviews | `reviews/status.json` | New reviews, open findings, articles changed since their last review. |
| The editor's channel | the editor vault's `down/` reports, when built | |
| Coming up | a curated `admin/content/librarian/calendar.json` (talks, deadlines, releases) | Not his calendar; only what he puts there. |
| Major events | the wires' latest editions | Already written daily by their desks. |

## The brief, and the debrief

One page a day, short enough to read on a phone:

1. **Needs you.** Pull requests waiting for a review, runs that failed or were refused, review findings marked high, questions agents left for Dinis.
2. **Yesterday.** Per repository with activity: what changed, in a line each; releases; outside contributions, named.
3. **The agents' debrief.** Each run and session: what it set out to do, what it did, what it cost, what it left open.
4. **Threads to pick up.** Open briefs, articles and repositories untouched for longest that connect to yesterday's work, with the reason each is worth returning to now.
5. **Coming up.** From the calendar file and the wires.
6. **Where the leverage is.** At most three suggestions, each with its reason. Dinis decides.

Published three ways: the JSON for agents, the markdown in the repository, and a page; and, when the browser for one exists, in its inbox.

## The loop

After the pattern rUv's Ruflo calls retrieve, judge, distill and consolidate: each brief records what Dinis acted on the next day (which links he opened, which threads he picked up, what he marked as noise), and the next brief weights its sections by that. Kept as a small file of weights in the Librarian's folder, readable and editable, never a hidden model.

## The runner

A scheduled task each morning, the way the wires already run, or a GitHub Actions schedule (free on public repositories; note a public repository's schedule is switched off after 60 days with no activity). The ledger shows scheduled runs being blocked by refused fetches and clones: the run must say when a source could not be read, rather than produce a quiet, partial brief.

## Order

1. The role file and policy row; yesterday from this repository alone (releases, ledger, briefs, reviews).
2. GitHub across the organisations, with a token; outside contributions.
3. Cloud sessions and their debriefs.
4. Threads to pick up, and where the leverage is.
5. The loop.

## Tests

- Given a fixture day (a release, a failed run, a new PR, a moved brief), the brief contains each in the right section and nothing else.
- A source that cannot be read appears as such at the top.
- The Librarian's writes stay in its folder (the ported `policy_check.py --role librarian`).

## Questions for Dinis

- Which organisations and outside repositories to watch?
- What time in the morning, and where do you want to read it first?
- Should it go to anyone else?
