# 01: The transition

## The decision

Dinis's second memo set the split. The dedicated site is the reference for the story, fact-driven and
not opinionated, and it is written for every kind of reader. newsroom.sgit.ai keeps "facts and opinions
about it, where we put that into context". Two places with the same facts is one too many, so the
section at `/php-flaws/` goes once your site covers everything it does.

## What "done" means: the five checks

The newsroom runs `php-flaws/build/track.py` against your **live** site. The script is in this pack. The
section is retired when checks 1 to 4 pass. Check 5 is then the newsroom's own step.

1. **Live.** `https://php.oct.2026.newsroom.sgit.ai/` answers 200. *Passing.*
2. **Status file.** `https://php.oct.2026.newsroom.sgit.ai/status.json` answers 200 with the shape in
   `02__status-json.md`. *Not yet.*
3. **Every source.** Every slug in the section's `data/sources.json` is in your published
   `data/sources.json`. *144 of 184.* The 40 missing ones are in the vault now: see `03`.
4. **Front page.** The newsroom's front page links to your site. *Passing, from newsroom v0.13.41:
   a "Developing story" strip in all three views, fed by your numbers.*
5. **Pointer.** The newsroom replaces `/php-flaws/index.html` and `/php-flaws/sources.html` with short pages.
   Each one says the story has moved, and links to your front page and your sources page. Their
   addresses keep working, and so does the data under `/php-flaws/data/`, frozen and marked as
   superseded. *Newsroom's step.*

## The order

1. You publish `/status.json` and re-export from the vault, so the 40 sources appear (checks 2 and 3).
2. The newsroom's tracker sees 4 of 4. Dinis confirms.
3. The newsroom ships a release that turns the section into the pointer (check 5). The release names
   card 088. The front-page strip stays, and reads its numbers from your `status.json`, until Dinis
   decides the story is no longer developing.
4. From then on, the newsroom links to your pages for facts, in articles, the wire and the newsletter,
   and never copies them.

## What the newsroom will not do

- It will not retire the section before checks 1 to 4 pass.
- It will not edit your repository. Requests come as a brief like this one, or as an issue.
- It will not republish your pages. Links only.
