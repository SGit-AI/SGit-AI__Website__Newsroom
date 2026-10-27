# CI owns the version

From v0.13.116 (27 October 2026), at the editor's request: the number of a release on this site is chosen by the pipeline, never by whoever pushes. Every agent that releases here (newsroom.writer, newsroom.dev, the accountant, the desks) follows this note from its next push.

## Why

Until v0.13.115 the committer picked the number: it bumped `admin/build/version.txt`, added a row to `admin/versions.html` and a note under `admin/engineering/releases/`, built, and pushed a commit whose subject began `site vX.Y.Z:`. CI only checked the guess and tagged it. With more than one agent releasing, the guess collides: on 27 October v0.13.103 and v0.13.111 were each taken by another agent's release while a build was running, and each collision cost a save, a reset, a re-apply and a second ten-minute build. A release whose subject lacked the `site ` prefix was refused by the tag job after it had been pushed. The pipeline is the one place that sees pushes in order, so it picks the number.

The scheme is the one Dinis Cruz wrote for OSBot-Utils on 27 October 2023, which sharness.ai adopted on 26 October 2026 ([CI owns the version](https://sharness.ai/articles/ci-owns-the-version.html)) and the PHP newsroom's repositories on 27 October. This site's version differs in one way: its pages are built from sgit.ai's generator, which the CI runner does not have, so the committer still builds, against a placeholder.

## The committer

1. Fetch and fast-forward `dev`.
2. `python3 admin/build/release_stamp.py --pending "one line on what this release does" --by @newsroom.<you>`. This sets `version.txt` to the pending version (the constant `PENDING` in `admin/build/release_stamp.py`, shaped like a version so every generator and check works unchanged, and sorting after every real release). It writes the release note and the versions row under the pending version, or adds your line to them if another agent's pending release is already on `dev`.
3. A new article's front matter says `version:` followed by the pending version. Copy it from `version.txt`; never guess a number.
4. Build and test as before (README, Release process), then commit with a subject that carries **no number**: `@newsroom.writer: what sgit does that Git does not`. Push to `dev`.
5. Watch the run. CI's release commit, "site vX.Y.Z: <your subject>" by GitHub Actions, is the release; the live site shows it within a few minutes.

If your push is refused because `dev` moved, fetch, merge `dev`, rebuild and push again. Generated files conflict, version numbers no longer do. Where the pending note or row conflicts, keep both lines.

A push that ran no build (a test fix, a note) needs none of this. CI writes its note and row from the commit message.

## What CI does (`.github/workflows/deploy-pages.yml`, job `release`)

- **The guard.** A commit on `dev` not made by GitHub Actions may set `version.txt` only to the pending version. Anything else fails the run, and nothing is released or deployed.
- **The number.** From the newest tag `vA.B.C`, a push to `dev` releases `vA.B.(C+1)` and a push to `main` releases `vA.(B+1).0`. One release runs at a time (the concurrency group). A push that landed while the run waited is taken in, and rides this release.
- **The stamp.** `release_stamp.py vX.Y.Z` turns every pending version in the served tree into the number, in contents and paths. It writes `version.txt`, and the note and row for a push that ran no build. Then it re-stamps the chrome, the engineering pages, the sitemap and `llms-full.txt`. `validate.js` gates the result, and refuses any served file still carrying the pending version.
- **The release.** One commit by GitHub Actions, `site vX.Y.Z: <the pushed subject>`, tagged, pushed (the branch, then the tag, three attempts if `dev` moves), and deployed from that commit in the same run. The push uses `GITHUB_TOKEN`, so it starts no second run.
- **Majors.** `dev` goes to `main` by pull request. The merge's push releases `vA.(B+1).0` on `main`, publishes a GitHub Release from its note, and fast-forwards `dev`, so `dev`'s next release is `vA.(B+1).1`.

## What it does not fix yet

Every page still carries the site's version in its nav and footer, so every release rewrites about 1,800 files. That is now CI's doing rather than the committer's, but it is the same churn. The next step is to take the number out of the pages (a `version.json` the chrome reads), as the PHP newsroom proposed for its own split.
