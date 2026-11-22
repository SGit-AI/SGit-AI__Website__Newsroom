# Memo 02, 22 November 2026: how writer-11 opens, and its first two articles

newsroom.d (writer-11, account d) asked Dinis how to open its registration. Check 15 checks each writer commit against its parent's register (since 19 November), so a writer commit cannot add the key it is signed with, and the debrief's "first commit signs both" is refused ("writer-11 is not in its parent's register"). writer-10 opened on 18 November, before that rule. newsroom.d proposed two commits: the first adds the registration and is not a writer commit; the second, a writer commit, publishes its git signing line and a fix to `signing-setup.sh` (it refused with two writers open; it now picks the open registration whose key is on this machine, as `sign.cjs` does). It also asked for the private lists (the leak scan's names check) to be added to its container, and proposed its first two articles from `admin/notes/articles-to-write.md`.

Dinis's answer, word for word (dictated), 22 November 2026, about 03:25 UTC:

> Yes, correct. Arc with 2 commits. Agree. Okay. Yeah, add them to the container, those leaks. Yeah, okay, can you start writing those 2 articles? That's cool.

## What it changes

- writer-11 opens in this commit, which is not a writer commit; it is git-signed by writer-11's key. The next commit, a writer commit, publishes `git_signing`; from then on check 15 checks every writer-11 commit in full.
- The two articles are claimed in `CLAIMS.md`: "Maintaining the core platforms as a cost item in every project" and "Versioned API sites".
- The private lists are still not in this container on 22 November at 03:28 UTC; until they are, newsroom.d says so with every release.
