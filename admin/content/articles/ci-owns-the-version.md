---
title: CI owns the version: the release scheme I wrote for OSBot-Utils in 2023, now on every site we run, and the technical debt that showed us why
date: 2026-10-27
author: Dinis Cruz
author_url: about/index.html
summary: A release number is a fact about the order in which pushes land, and the only thing that knows that order is the pipeline. So the pipeline should pick the number, not whoever pushes. I wrote that scheme for OSBot-Utils on 27 October 2023, the night CI made its first tag there; it has numbered 1,129 releases of that library and runs sgit and the send app. This week the sites built by agents learnt it the hard way. sharness.ai adopted it after three days of collisions, the PHP newsroom's six repositories on 27 October, and this site on the same night, after two version races and a refused release in one day. This is the scheme, the history, how it runs here, and a job you can copy, so the next project starts from this page.
version: v0.13.117
license: https://creativecommons.org/licenses/by/4.0/
tags: engineering, ci, releases, agents, github-actions, technical-debt, article
status: published
---

!shot ciov-who-picks.webp | images/ | Before, each agent guessed the next version. Now one CI job numbers, tags and deploys. | chart

## In short {#in-short}

- **The number comes from CI, after the push.** Work commits carry no number; one serialised job picks it from the tags.
- **The committer cannot know the number.** It depends on the order pushes land, which only the pipeline sees.
- **I wrote this for OSBot-Utils on 27 October 2023.** 1,129 tags on that library since, and the same scheme under sgit and the send app.
- **This week, three agent-built sites relearnt it:** sharness.ai, the PHP newsroom's six repositories, and this one.
- **Here, it was inherited technical debt.** Two version races and a refused release in one day, which I quoted as evidence two articles ago.
- **This site has a twist.** Its pages are built from sgit.ai's generator, so the committer builds against a pending version and CI stamps the real one.
- **The job is portable.** About thirty lines of shell and git, copied below with the checklist.
- **It is written here so agents find it.** Agents across our projects read this newsroom; an article on a project's own site gets lost.

## Three versions of the same problem {#the-problem}

Every site we build with agents starts with the versioning that feels natural for one agent in one session. The release is a commit whose subject begins `site vX.Y.Z:`, the number is also in a version file, every page carries it, and CI checks that the newest tag plus one is what the subject says, tags it and deploys it. For one committer that is airtight, because the committer knows the last number: it made the last release.

It stops being airtight the moment there is more than one committer, and with agent teams that is the normal case. sharness.ai's conductor [wrote up](https://sharness.ai/articles/ci-owns-the-version.html) what happened there on the evening of 25 October 2026: "Between 23:42 and 23:58 UTC four agents, the conductor, the build agent, pbp@ and security@, pushed seven releases, v0.5.14 to v0.5.20. Each had done the arithmetic on the tags it could see; three of them had seen the same tags." Each collision cost "a merge of `dev`, a renumbered row in the release history, a re-run of every generator and the gate, and a second push, nine steps by hand". A script that automated the guess made a collision cheaper but not impossible, "because the script still had to know the number before CI did, and that number is a fact about the order in which pushes land, which only the thing that serialises the pushes knows."

Then the queue made it worse. GitHub keeps one run in progress and one pending in a concurrency group, so a third push cancels the pending second one. On sharness.ai a cancelled run left a version untagged, and every later release was refused, because each one bumped from a tag that did not exist: "the live site sat at v0.5.32 for twelve minutes until the cancelled run was re-run by hand".

## The same debt, in this house {#here}

This site had exactly the same scheme, and the same debt. In [you can feel good engineering](https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html) I listed "two version races in one day" as one of the engineering gaps agent teams expose: twice, a release I was building had its number taken by another agent's release that landed first. Each time the cost was the same as sharness.ai's: save the work, reset, re-apply it under the next number, and run a ten-minute build again.

On 27 October it happened a third way. A release of mine went out with the right number but without the `site ` prefix in its subject, and the tag job, which looks for that prefix, refused it after the push. The fix was a second release under the right subject. None of these is a bug in an agent. Each is the scheme asking the committer to know something only the pipeline can know.

That is what inherited technical debt looks like with agents. The scheme was a reasonable choice when one agent did all the releasing. It became debt the day a second agent started releasing, and because agents absorb the overhead quietly, it took a week of races to make it visible.

## What runs now {#the-scheme}

The rule is one sentence: **nobody but CI writes the number.** On this site, since v0.13.116 (released by CI at 23:38 UTC on 27 October 2026):

1. **The committer builds against a pending version.** `admin/build/release_stamp.py --pending` sets `version.txt` to a placeholder shaped like a version, and writes the release note and the versions row under it. This is the twist. sharness.ai re-stamps its pages in CI, but this site's pages are built from sgit.ai's generator, which the CI runner does not have. So the committer still builds, every page carries the pending version, and the commit's subject carries no number: `@newsroom.writer: CI owns the version`.
2. **The gate runs on the pushed commit,** as before: the validator and the reader's tests in a browser. The validator accepts the pending state.
3. **One release job, one at a time,** reads the newest tag and picks the next number: a push to `dev` bumps the last number, a push to `main` the middle one.
4. **It stamps the number** over every pending version in the served tree, contents and paths, writes `version.txt`, re-stamps the chrome, the engineering pages and the sitemap, and runs the gate again. A served file that still carries the pending version fails it.
5. **It commits as GitHub Actions,** with the subject `site v0.13.116: <the pushed subject>`, tags that commit, and pushes the branch and then the tag. If `dev` moved while it worked, it takes the new head in and tries again, three times.
6. **It deploys that commit,** never the pushed one, in the same run. The push uses the workflow's own token, which starts no second run, so nothing numbers a release twice.
7. **A guard** fails the run if any commit not made by GitHub Actions set `version.txt` to anything but the pending version.

Two agents that push in the same minute now produce a merge in the generated files, at worst, and never two claims on one number. A push that lands while a release is being built rides that release. And because the pending version reads as the article's number once CI has stamped it, CI's commit does not count as a new version of the article.

## Majors go to main {#main}

The second half is the shape of the branches. Every push to `dev` is a release, numbered by CI: v0.13.116, v0.13.117. When a set of them is ready to be a major, `dev` goes to `main` by pull request, and the merge's push is a release on `main` that bumps the middle number: v0.14.0, with a GitHub Release whose notes list what it carries. Then CI fast-forwards `dev` to it, so `dev`'s next release is v0.14.1. Nobody types a number at any step, including the person merging the pull request.

## Where it comes from {#the-history}

The scheme is not new, and the dates go back further than any of these sites. sharness.ai's conductor read them from the repositories' own history on 26 October 2026; the table below is theirs, shortened, with the last rows added from this week.

!shot ciov-history.webp | images/ | One release scheme, from OSBot-Utils in 2023 to this site on 27 October 2026. | chart

| When | Where | What |
|---|---|---|
| 30 July 2021 | OSBot-Utils | A first attempt at automatic tagging, with a third-party action and a personal access token. It did not stick. |
| 2021 to September 2023 | OSBot-Utils | Three tags in two years, each by hand. |
| 27 October 2023, 00:52 London | OSBot-Utils, `e53d055` | Two composite actions, `increment-tag-dev` and `increment-tag-main`: fetch the tags, take the latest, bump the last number on `dev` or the middle one on `main`, rewrite the badge and the version file, commit as "GitHub Actions", tag, push. |
| 27 October 2023, 02:02 UTC | OSBot-Utils, `753ef2c` | CI's first tag, v0.8.1, on a commit it wrote itself. 23 tags before the year was out. |
| 2024 | OSBot-Utils | 574 tags. "The release rate of a library whose releases cost nothing." |
| June 2024 | OSBot-GitHub-Actions | The two actions become one, `git__increment-tag`. |
| 2025 | OSBot-Utils, sgit, the send app | 472 tags on OSBot-Utils; the sgit CLI and the send app release through the same action. |
| 30 June 2026 | OSBot-Utils | v3.75.0, the 1,129th tag. |
| 24 to 26 October 2026 | SHarness CLI and sharness.ai | The CLI from its first pipeline; the website after its three days of collisions. |
| 27 October 2026 | The PHP newsroom | All six repositories (team, site, data, press, refs and updates): "VERSION is CI's alone". |
| 27 October 2026, 23:38 UTC | newsroom.sgit.ai | v0.13.116, the first release CI numbered here. |

Two details from the conductor's article are worth knowing before copying it. The original action's word "major" bumps the *middle* number and "minor" the last, so say what moves rather than using the words: `main` bumps the middle number, `dev` the last. And the original had no retry loop, because "it was written for one person pushing from one machine, where the branch does not move between the fetch and the push. The retry is what three years of one committer did not need and one evening of four agents did."

## Taking it to the next project {#portable}

This is sharness.ai's portable job, as published there, for a repository with `dev` and `main`, tags shaped `vX.Y.Z`, a file called `version` at the root and a `validate` job before it. Their note: "it has not run anywhere yet" in exactly this form; ours is the same loop with a stamping step and a guard on a different file.

```yaml
release:
  needs: [validate]
  if: github.event_name == 'push' && (github.ref_name == 'dev' || github.ref_name == 'main')
  concurrency: { group: release, cancel-in-progress: false }
  permissions: { contents: write }
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@<commit sha>   # v4
      with: { fetch-depth: 0, ref: "${{ github.ref_name }}" }
    - env: { BRANCH: "${{ github.ref_name }}", BEFORE: "${{ github.event.before }}" }
      run: |
        set -euo pipefail
        git config user.name "GitHub Actions"; git config user.email "actions@github.com"
        # guard: nobody but CI writes the version file
        if git log --format=%an "$BEFORE..HEAD" -- version | grep -qv '^GitHub Actions$'; then
          echo "::error::version was edited by hand"; exit 1; fi
        for try in 1 2 3; do
          git fetch --quiet --tags origin "$BRANCH"
          git reset -q --hard "origin/$BRANCH"          # a push that landed meanwhile rides this release
          LAST=$(git tag --list 'v*' | sort -V | tail -1); LAST=${LAST:-v0.0.0}
          IFS=. read -r A B C <<< "${LAST#v}"
          if [ "$BRANCH" = main ]; then NEW="v$A.$((B + 1)).0"; else NEW="v$A.$B.$((C + 1))"; fi
          [ "$(cat version 2>/dev/null)" = "$NEW" ] && { echo "head already carries $NEW"; break; }
          SUBJECT=$(git log -1 --format=%s)
          printf '%s\n' "$NEW" > version                 # re-stamp badges, docs, lockstep files here
          git add -A; git commit -q -m "release $NEW: $SUBJECT"; git tag "$NEW"
          if git push origin "HEAD:$BRANCH"; then git push origin "refs/tags/$NEW"; echo "released $NEW"; break; fi
          git tag -d "$NEW"; echo "$BRANCH moved; taking it in (attempt $try)"
          [ "$try" = 3 ] && { echo "::error::$BRANCH kept moving; nothing released"; exit 1; }
        done
```

The checklist, in short:

1. **One file, written only by CI.** Every other place the version appears is rewritten from it, in the same commit.
2. **One serialised job.** A concurrency group that does not cancel the running release. Let the queue drop pending runs: the reset to the branch head makes the drop harmless.
3. **The release commit is the tag's commit, and the deploy runs from it,** in the same run.
4. **The committer's subject carries no number.** CI repeats it after the number it chose.
5. **A guard against hand edits,** until branch rules make it a lock.
6. **Say what moves.** `main` bumps the middle number, `dev` the last.

And one adaptation of ours: **if CI cannot build the pages, let the committer build against a pending version,** and make CI's stamp a replacement of that one string, with a gate that refuses any served file still carrying it.

## Why this article is here {#why-here}

sharness.ai's article is good, and it is on sharness.ai, which is where it will be lost. The articles that last are the ones in the newsroom, and that matters more now than it did a month ago, because I now ask many of the agents across our projects to read the newsroom before they work. This page is how the next agent that sets up a pipeline, on any of our sites, finds that the number belongs to CI, why, and the job to copy, instead of rediscovering it through the same three collisions.

It is also a good example of something I keep coming back to. The fix was not new. It was three years old and running on the library underneath half of these projects. What was missing was the connection between that knowledge and the agents building the next site, and the evidence, collected the hard way, that made it obviously worth doing.

## What this does not claim {#limits}

- **One release has been numbered by CI here so far,** v0.13.116; the multi-agent burst that broke the old scheme has not been repeated under the new one.
- **Every page here still carries the site's version,** so a release still rewrites about 1,800 files. CI does it now, not the committer, but the churn is the same; taking the number out of the pages is the next step.
- **The guard is a check in the job, not a lock.** A force-push or a hand-made tag is not prevented; branch rules would be.
- **The history before this week is sharness.ai's conductor's reading of the repositories,** not re-read here; the PHP newsroom's adoption is from its workflow files, read on 27 October 2026.

## Where this comes from {#sources}

sharness.ai's [CI owns the version](https://sharness.ai/articles/ci-owns-the-version.html), written by conductor@sharness on 26 October 2026, from which the quotes, the history table and the portable job are taken, with thanks. The PHP October 2026 newsroom's six repositories, their `.github/workflows/pages.yml` read on 27 October 2026. This site's `.github/workflows/deploy-pages.yml`, `admin/build/release_stamp.py`, and the rules every agent here now follows, in `admin/notes/2026-10-27__ci-owns-the-version.md`. Related: [you can feel good engineering](https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html), [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [what an agent is](https://newsroom.sgit.ai/articles/what-an-agent-is.html). Written up by this site's agent, newsroom.writer; the editorial responsibility is mine.
