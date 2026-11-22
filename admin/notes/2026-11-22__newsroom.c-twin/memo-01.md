# Memo 01, 22 November 2026: newsroom.c, the writer on account C (writer-12)

maestro.c started this session (newsroom.c@sgit.ai.dinis) on account C at Dinis's word in its own session, about 19:00 UTC on 22 November 2026: "can you create the newsroom.c@sgit.dinis, which is my newsroom that's going to write articles." His rule from about 02:00 UTC the same day is one writer (journalist) per account. With writer-10 (account b) and writer-11 (account d) open, the register's `max_open: 2` left no room for a third, so newsroom.c asked Dinis to confirm two things: that it registers as writer-12 on account c, with the limit raised to three writers, one per account; and that it publishes its first article, "Out of the box", whose draft it showed him.

Dinis's answer, word for word, in newsroom.c's session, 22 November 2026, about 21:00 UTC:

> Yes can you register as a writer and push that article

## What it changes

- `admin/writer/register.json`: `max_open` is 3, approved by this memo. Every open registration still names its account, and no two open writers share one (the twins rule of `admin/notes/2026-11-22__newsroom.d-twin/memo-01.md`, unchanged).
- `admin/build/writer_register.js` (validate.js check 15) accepts a `max_open` of 1 to 3; above 1 it still needs the editor's approval on file.
- writer-12 opens in a commit that is not a writer commit, git-signed by writer-12's key, as writer-11 did (memo 02 of the twin's folder): check 15 checks a writer commit against its parent's register, so a writer commit cannot add the key it is signed with. The next commit, a writer commit, publishes writer-12's `git_signing` line and claims `out-of-the-box` in `admin/notes/2026-11-22__newsroom.d-twin/CLAIMS.md`.
- Every other rule stands: a registration opens only at the editor's word, with a new key made in the writer's own session (private half in `~/.newsroom-writer/`, never committed, never printed); a closed registration is never reopened; the writers claim each article before writing and never build at the same time.
- The private lists are not in this container on 22 November; until they are, newsroom.c says so with every release.
