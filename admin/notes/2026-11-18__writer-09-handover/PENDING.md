# Pending articles from writer-09 (not published)

writer-09's registration closed before these four could be released. They are installed (md, images, summaries, graphs, front/sections.json rows, notes) but NOT stamped, built, signed or pushed to dev.

| Slug | Title | State |
|---|---|---|
| fliplet-and-the-website-cell | Rent or own | validated in a 3-article build |
| no-lock-in | No lock-in | validated in a 3-article build |
| sovereignty-you-can-move | Sovereignty you can move | validated in a 3-article build |
| the-sovereign-website | The sovereign website (agenticcells.ai pivot brief, with the £50/€50 European launch) | not yet built |

For writer-10, under your own registration and key:
1. `git fetch origin && git merge origin/handoff/writer-09-pending` into your up-to-date dev. Only source files are on this branch (no generated HTML), so conflicts should be limited to `admin/content/front/sections.json`; keep both sides' rows.
2. Edit as you see fit (versions in front matter say v0.14.159; the build restamps).
3. Follow DEBRIEF.md section 2 from step 6: wording check, `release_stamp.py --pending`, `release.sh`, then the gate. Captions are already ≤120 characters.
4. Send the AgentiCCells conductor the sovereignty and pivot briefs once Dinis restarts that team (ownership and no-lock-in briefs were already sent).
