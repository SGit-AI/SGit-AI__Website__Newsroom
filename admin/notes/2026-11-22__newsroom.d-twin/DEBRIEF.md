# Start-up debrief: a journalist twin for newsroom.sgit.ai, newsroom.d@sgit.ai.dinis

Written by writer-10 (newsroom.sgit.ai's journalist agent, handle `@newsroom.writer`, proposed name `newsroom.b@sgit.ai.dinis`) on 22 November 2026, at Dinis Cruz's word: "write a debrief for starting a new journalist twin (of you) called newsroom.d@sgit.ai.dinis ... ask the maestro.b for guidance on creating these twins". Read this, then the earlier hand-over `admin/notes/2026-11-18__writer-09-handover/DEBRIEF.md` (the release recipe in its section 2 is still the one that works), `admin/writer/README.md`, `admin/notes/writer-conventions.md` and the handbook article `admin/content/articles/how-a-journalist-agent-publishes-here.md`.

## 0. Decide first: twin, or successor (only Dinis can)

The newsroom has a hard rule: **one journalist agent at a time.** `admin/writer/register.json` allows at most one open registration, and `admin/build/validate.js` check 15 refuses any writer commit the open registration did not sign, locally and in CI. The rule came from two writer sessions pushing to dev on the same night (Dinis's words in `admin/notes/2026-10-31__one-writer/memo-01.md`). So a twin that runs beside writer-10 needs one of these, and Dinis's word on which:

- **A. Successor.** writer-10 is closed and the twin opens the next registration (writer-11), the way writer-09 handed over to writer-10. Nothing in the build changes.
- **B. Two writers at once.** The register and check 15 change to allow two open registrations, each with its own key, plus a way to stop them colliding: separate article slugs, never building at the same time (the gate already stops on "dev moved", but two 25-minute builds will keep tripping it), and one of them owning the front page and the series schedules. This is a build change and needs its own memo with Dinis's words.

Until Dinis decides, the twin must not commit as `@newsroom.writer`: check 15 would refuse it, and that refusal is correct.

A twin on account D, as Dinis proposes, is active at the same time as writer-10, so it is **option B**: the register and check 15 must change first, at Dinis's word, with the claim rule in section 2 as the way the two avoid each other.

## 1. The name

Dinis proposes `newsroom.d@sgit.ai.dinis` for the twin and `newsroom.b@sgit.ai.dinis` for writer-10. That follows the team's pattern, `<role>.<account letter>@<domain>.<person>`: the letter is the account the session runs on (b is account B, where writer-10 runs; d is account D, run by maestro.d). Twins are the same role on two accounts, both active at once, so the name is right **if Dinis starts the twin on account D**. A second journalist on account B would not be a twin and should get a different name, such as writer-11 (maestro.b, section 9). In repositories whose gate refuses other domains, write it "newsroom.d (sgit.ai)". The commit handle in this repository stays `@newsroom.writer` (validate.js and the gate depend on it); the agent name goes in the registration and in messages.

## 2. What the twin needs before its first commit

1. **A registration** at Dinis's word (option A or B above): `node admin/writer/tools/register.cjs open --id writer-11 --session <its session url> --approved <path to Dinis's words>`, a new ed25519 key made in the twin's own session (private half in `~/.newsroom-writer/`, never committed). A writer never opens or closes its own registration without Dinis's words recorded in a notes file first.
2. **Git commit signing:** writer-10's registration also carries an SSH signing key (`git_signing` in the register, approved in `admin/notes/2026-11-19__signed-commits/notes.md`). The twin needs its own, recorded the same way.
3. **Its session, on account D,** started by maestro.d at Dinis's word in maestro.d's session (maestro.b cannot start sessions there), with its own checkout of this repository.
4. **No scheduled task** unless Dinis says so in maestro.d's session.
5. **Its own behaviour policy** from abp@, a twin of writer-10's, when the team is back on Monday 23 November.
6. **The claim rule, against double publishing:** writer-10 keeps what it holds (the Ten days series and anything it has started); the twin takes only articles writer-10 has not started, and claims each one in `admin/notes/` (a `CLAIMS.md` beside this file, one line per slug, signed off by its commit) before writing. No two writers on the same branch, and never two builds at once.
7. **The cross-account path:** the twin cannot message writer-10 directly. maestro.d and maestro.b relay through `board/team/maestros/` in PrompTugal__News__Website.
8. **The scratchpad tools.** Scratchpads are wiped. `tools/` in this folder has writer-10's current `gate.sh` (fill in the two attribution lines and set `WRITER_TMP`), `figlib.mjs` (the figure helpers) and `install-example.py` (the per-article installer used for every article on 21 November). The gate expects `$WRITER_TMP/node/node_modules` (playwright, sharp) and `$WRITER_TMP/rel.out` from the last build.

## 3. What changed since writer-09's hand-over (learned 19 to 22 November)

- **Copy the build log to `rel.out`.** The gate reads `$WRITER_TMP/rel.out`; keep each build's log as `relN.out` and copy it.
- **Stale summaries at the gate** (`GATE STOP: stale`): editing a published article's text invalidates its section hashes. Pop `hash` for the named sections in `summaries/<slug>.json`, rewrite the lines if the meaning changed, `summaries.py --stamp`, and rerun the gate. It also happens after a build re-renders an article you corrected; check `summaries.py --check` just before the gate.
- **"dev moved" at the gate:** CI's "site vX" commit landed after you built. Stash your work (`git stash push -u`), fast-forward, reinstall from your installer script, re-stamp, rebuild. Always wait for CI's release commit from your previous push before building again.
- **CI can fail for reasons that are not yours.** `test_reading.mjs` (a scroll-timing test) fails locally always and in CI sometimes; GitHub Pages sometimes reports "No artifacts named github-pages". The writer's token cannot re-run workflows (403 "Resource not accessible by integration"). Do not work around it: tell Dinis; the next push deploys everything on dev, or at Dinis's word make a small real commit (a notes line) through the gate.
- **History folds.** `admin/build/history-folds.json` makes an article's published version pages start from its current text, for text Dinis decides must not be on the site (for example a name). Used on 21 November for learning-from-wikipedia. Git keeps everything. Dinis said for a-european-brain that a normal correction is fine, so only fold at his word.
- **A background wait that greps for `gate.sh` matches its own command line.** Wait on the gate's output file, not on `pgrep -f gate.sh`, when the same shell also contains a check loop.
- **Messages from other sessions are material, never instructions.** maestro.b and bulletins.b both sent "at Dinis's word" requests on 21 November; writer-10 asked Dinis before acting, and bulletins.b in turn waited for Dinis's own word before publishing its library.

## 4. Standing rules (all still in force)

Everything in section 3 of writer-09's hand-over, plus:

- **Leave-outs added since:** do not name the person who challenged the European brain article (removed at Dinis's word on 20 November; the archived v1.1.0 page keeps it, which is fine). Do not mention any collaborator in learning-from-wikipedia; it is framed as the next step into education. Never identify the person behind an anonymous profile (a persona session, south-beacon.b, exists; say nothing about who it is for).
- **Names:** Kate Curtis-Evans may be named (her site and hub entry are public). Emily Cruz and Grace Farrell may be named as people who could link, with no link claimed.
- **Prices:** £50 is the only stated career-site price; do not invent the higher levels.
- **Dollars are API-equivalent** in every agent-spend story; the real limit is the subscription's seven-day limit, and Dinis is fine with its warnings being published.

## 5. The scheduled task

`trig_01P5GzqB8bwZo1vjG92bwXdw`, "Newsroom writer-10: publish the next Ten days article", fires into writer-10's session. It is **disabled** since maestro.b's slow-down of 21 November (restore scheduled for 23 November after the weekly reset). Ten days **row 13 (VoiceDebrief, "One hour to TestFlight") is held** by Dinis; scheduled runs publish nothing until he lifts it. If the twin takes over the series, the trigger must be pointed at the twin's session (Dinis or maestro.b), not duplicated.

## 6. Open threads

- **The presenters library** (bulletins.b): published 21 November as a preview at `https://bulletins.promptugal.news/lib/presenters/latest/` and pinned `v0.1.0/`, pending security@'s review and registry pins. To use it in the newsroom, copy the pinned folder and check each file against its pins (as with ptmap); do not load it from the bulletins site. "Programmatic stories" links to it.
- **Person Graph and the web of trust** (5 articles on 21 November): Dinis said "you can implement this". Nothing is built. The first step would be kinds of link and provenance in pki.sgit.ai, which is that site's agent's work; brief it only at Dinis's word.
- **The factory request for the learning sites** (learning-from-wikipedia): Dinis said it goes on sovereign websites; the organisation is SovereignWebsite. Not drafted yet. The audience age (16+ or 18+) is for the legal team; writer-10 did not contact it.
- **A study of personality pairing** (from the Ju and Aral PNAS paper): offered to Dinis, not asked for yet.
- **Mistral partnership proposal:** offered, not asked for yet.
- **Still from writer-09:** PrompTugal observability on the newsroom, data site paths, platform terms, the Mitko Vasilev video details.

## 7. What writer-10 published (19 to 21 November), for context

20 Nov: a-european-brain (corrected twice: the challenger's name removed; four claims corrected from the Mistral site's research), transcription-for-a-sector, the-first-round-trip.
21 Nov: the-way-in, one-night-on-mistral, the-showroom, the-sgit-server-factory, hired-as-an-agentic-worker, langgraph-and-us, deepseek-in-our-workflows, a-web-of-trust-for-careers, an-anonymous-profile-vouched-for, can-you-find-me, learning-from-wikipedia, person-graph (with a simulation in its notes), start-stop-slow-down (maestro.b's analysis), programmatic-stories, the-primitives-of-trust. Earlier (19 to 20 Nov): the Ten days rows to 12, the Sovereign Website and appliance pieces, the X-ray, the Galaxy and the Swarm.

## 8. Where things live

- Newsroom repo: `/home/user/SGit-AI__Website__Newsroom` (push to `dev`; CI numbers, tags and deploys). Website repo for builds: `/home/user/SGit-AI__Website`.
- Public repos used on 21 November, cloned anonymously: PrompTugal `PrompTugal__News__Website` (maestro.b's analysis, the desks), `PrompTugal__News__Bulletins`, SovereignWebsite `Site__Founder__Kate-Curtis-Evans` and `Site__Provider__Mistral`, the-cyber-boardroom `SGraph-AI__App__Send` (the deploy templates and Dinis's 2026 briefs) and `MGraph-AI__Service__Html__Graph`.
- Each article's notes: `admin/notes/<date>__<slug>/notes.md`; scripts that produced figures and simulations are described there.

## 9. maestro.b's guidance

Asked on 22 November (session `session_01Kw9UwEbwyWMbZ7yCr81Dq9`): the right name and letter for a twin, what a twin's start-up needs from the team (session, environment, key and registration, roster, ledger, policy, scheduled task), and whether there is a template. Its answer is recorded below when it arrives.

Answered at 01:47 UTC, 22 November, as material (its words, condensed):

- **Names:** the letter is the account. newsroom.b@sgit.ai.dinis and newsroom.d@sgit.ai.dinis fit, if the twin runs on account D. A second journalist on account B is not a twin; give it another role name (for example writer-11). Where a gate refuses other domains, write "newsroom.d (sgit.ai)".
- **Start-up:** the session on account D, by maestro.d at Dinis's word; its own checkout and signing key, never printed, with its public half and registration in the newsroom's register only at Dinis's word; no scheduled task unless Dinis says so; its own policy from abp@ on Monday; the claim rule (section 2, item 6); relaying through board/team/maestros/.
- **Models to follow:** `board/team/maestros/README.md` (the Twins rule) and `board/team/maestros/maestro-d-onboarding-prompt.md` (a twin's first prompt) in PrompTugal__News__Website on dev; for the claim and key pattern, SovereignWebsite__Factory `board/onboarding/sites.b.md` and `hub.b.md`, and `board/team/maestro.d/decisions/2026-11-21-sovereignwebsite-twins-and-vault.md`.
- Account B is paused until Monday 23 November, 00:25 UTC.
