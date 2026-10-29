# Briefing pack: php.oct.2026.newsroom.sgit.ai takes over the PHP story

**For:** the team and agents running `php.oct.2026.newsroom.sgit.ai` (repository
`SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP`).
**From:** the newsroom.sgit.ai desk, on behalf of Dinis Cruz (editor), 22 October 2026.
**Goal:** the PHP story moves completely to your site. Then the section at
`https://newsroom.sgit.ai/php-flaws/` is **retired**, and its address points to you.

There are no keys, tokens or vault credentials in this pack. If you need write access to the evidence
vault and do not have it, ask Dinis.

## Read in this order

1. `01__the-transition.md`: what "the move is done" means. These are the five checks the newsroom runs
   against your live site, and the order the retirement happens in.
2. `02__status-json.md`: the one file we are asking you to publish, `/status.json`, and its exact shape.
   The newsroom's front page and its tracker read it.
3. `03__the-evidence-vault.md`: the state of the shared vault, the 40 sources your export does not have yet,
   and two rules the morning taught us.
4. `04__what-the-newsroom-keeps.md`: the editorial split. You keep the facts; the newsroom keeps context and
   opinion. It also covers how the two sites link to each other.
5. `05__checklist.md`: the whole thing as a list you can tick.

## Also in this pack

- `data/`: the section's data as it is today. `sources.json` holds 184 sources with capture hashes,
  `claims.json`, `timeline.json` and `story.json`, and `transition.json` holds the tracker's latest
  result against your site.
- `data/missing-from-site.json`: the slugs the tracker could not find in your `data/sources.json`.
- `capture-first.md`: the newsroom's article on how the coverage started, in its source form. It links
  to your site as the place to read the story.
- `track.py`: the tracker itself, so you can run the same checks before we do.

## Where things stand (22 October 2026, 12:30 UTC)

| Check | State |
|---|---|
| Site live at its domain | yes, HTTP 200, v0.2.2 |
| `/status.json` published | no (404) |
| Every source in the section is on the site | 144 of 184; 40 missing |
| Newsroom front page links to the site | yes, from v0.13.41 |
| Section replaced by a pointer | not yet: the last step, done by the newsroom |
