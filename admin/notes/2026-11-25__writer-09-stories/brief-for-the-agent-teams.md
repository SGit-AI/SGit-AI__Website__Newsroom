# Brief for the agent teams: loose ends in AgentiCCells and SovereignWebsite

From the newsroom (writer-09), 25 November 2026, about 00:30 UTC, for Dinis to pass to the teams. Read-only survey of both GitHub orgs and their live sites; nothing was changed, pushed or posted. Live checks were made at 00:30 UTC on 25 November; anything marked "checked" was seen by the newsroom, the rest is what the teams' own files say (paths given so you can check).

Each item says what we saw, where, and the suggested next step. Nothing here needs an article; it is housekeeping so that what we started is finished, moved or closed on purpose.

## 1. Moves from AgentiCCells to SovereignWebsite (finish the hand-over)

| Item | State | Evidence | Next step |
|---|---|---|---|
| dinis-cruz site | Dinis said "yes, move dinis-cruz to SovereignWebsite" (21 Nov). Blocked: the transfer App gets 403; a key-holder proposal is pending (23 Nov). | AgentiCCells__Site__Factory `team/conductor.b/decisions/2026-11-21.md`, `2026-11-23.md` | Decide the key-holder proposal; then do the transfer (the approved Transfer-Test repo first). |
| Algarve Evolution | Moving to SovereignWebsite as a private vault site; the AgentiCCells repo and site are to be deleted "once all is working". | Factory `team/conductor.b/decisions/2026-11-20.md` (commits f95a55b, 7bfb437) | Confirm the vault site works, then delete the old repo and site (a person deletes, not an agent). |
| Tools hub | Dinis wants it at tools.sovereignweb.site. Today it is tools.agenticcells.site (47 tools from SGraph-AI__Tools, 9af07eb, 20 Nov). | Factory conductor.b decisions, 20 Nov | Move via a SovereignWebsite request; redirect the old address. |
| The sovereign offer | Moved out of agenticcells.ai to sovereignwebsite.ai (£50/€50, decided by Dinis on 23 Nov). | AgentiCCells__Website `board/briefs/2026-11-19-refactor-agentic-cells.md`, commit 16520b6 | See section 2 for the old prices still on agenticcells.ai. |
| Other AgentiCCells customer and people sites | Not yet decided whether each moves. | AgentiCCells__Site__Factory `requests/` (about 30 since 18 Nov) | Make one list: each site, stays or moves, owner. Close the ones nobody needs. |

## 2. agenticcells.ai: make the site say one thing

- The homepage now reads "A team of AI agents that you own" with four sizes (£500, £1,500, £5,000, £20,000) and points to sovereignwebsite.ai for the £50 offer (checked, v0.1.286).
- **Old pages still live with the old offer:** /website-cell/ still shows £250 (3 mentions, checked) and a "Choose a design" picker; /start-here/ also. Either retire them, redirect them to sovereignwebsite.ai, or rewrite them to match. Rule: live prices change only with Dinis's recorded word (commit 16520b6), so put the choice to him.
- **Translations:** the language switcher lists 10 locales but none of the new pages is translated (`team/HANDOVER.md`, "Next decisions"). Either translate or hide the switcher until they are.
- The three-month ownership line is soft wording ("an expectation we set ourselves, not yet a rule in the terms") on /no-lock-in/, /compare/, /sovereign-website/. Fine for the MVP; when it becomes a rule, it goes in the terms.
- **CI gap:** six commits on AgentiCCells__Website failed the trailer check and were deployed, because CI checks only the pushed range (`team/HANDOVER.md`). Check every commit since the last release, as the newsroom's check 15 does.
- The /partners/ hub is the older version; align it with the new homepage or with sovereignwebsite.ai's partner terms.

## 3. Sites we started and left empty

**AgentiCCells tool sites, each a one-line placeholder of about 1 KB (checked 200):** video-recorder, file-encryptor, heic-converter, ssh-keygen, image-tools, whats-my-ip, what-am-i-leaking (all `.agenticcells.site`). Each has one seed commit from 19 Nov; push access was refused so no tool went in (`team/HANDOVER.md`). Decide: build them as SovereignWebsite `Site__Tool__*` sites through the factory (that is where tools now go), and retire these.

**SovereignWebsite sites still on the starter template:** review.sovereignweb.site still shows "This site was made by one request…" (checked). TauGuard, Conductor, Hub, Migration and Router agent sites were seed-only in the survey, but no longer show the placeholder text at 00:30 UTC; check they have real content.

**Websites for the moment:** the trends cell made two sites (gta6-launch, 20 Nov; black-friday-rights, 21 Nov; both live) against an approved pace of about three a day, and nothing since 21 Nov. Decide: restart it with a schedule, or stop it on purpose and record why.

**Stalled since 19 to 20 Nov:** AgentiCCells__Site__Website, __Site__Hub, __Site__Evals, __Site__Dinis-Cruz (the last has open questions for Dinis and the stalled move above).

## 4. SovereignWebsite: broken or unfinished

- **No HTTPS (no response at 00:30 UTC):** uk-driving-test.tool, aws.agents and mail.agents (`.sovereignweb.site`). The survey saw a wrong-certificate error. Pages needs the custom domain verified and the certificate issued; re-run the Pages/DNS step for each.
- **The bare domain sovereignweb.site does not resolve** (checked), although every subdomain does. Add an apex record (or a redirect to hub.sovereignweb.site).
- **The commit-signer check is not on the customer sites yet.** GitHub ran the hourly Org apply cron only about 3 or 4 times a day and not after 11:57 on 24 Nov, so the fix that checks who signed each commit before a site deploys reached the agent sites only (Site__Agent__Decisions 3ce35d1, Site__Agent__Maestro 7aadbcb). Trigger the apply by hand (workflow_dispatch) or on push to the policy file, rather than relying on cron.
- **Keys:** the Maestro and Decisions agents' keys are not in the factory's `team/keys.json` (their READMEs say so). Register them, or the signer check will refuse them once it is everywhere.
- **The 22 Nov incident** (`board/incidents/2026-11-22__pushed-before-key-published.md`): a site went live with an unregistered key and "Nothing refused it. Only Dinis noticed." Make sure the fix above covers that case and add a test for it.
- **Access the conductor never got:** the sovereignwebsite.ai repo (ask 35 in `board/2026-11-24__conductor-state.md`). Wakes on account B are off; some sessions are blocked by permission prompts on key steps (same file).
- **Costs page gaps:** accountant.agents.sovereignweb.site (`site/data/costs.json`, 8371f97) leaves out maestro.b's own $136.66, and its image spend line has not been updated since 20 Nov. Fill both before anyone quotes the total.
- **London Agentics Foundation chapter site** (first built 24 Nov, 0ed7a04) announces a hackathon with no confirmed date. Keep "date to be confirmed" visible until there is one.
- **AWS team (22 roles):** a.maestro planned to move sessions off account A (64% of its limit) and restart the stopped AWS team on another account (Site__Agent__Maestro f0fa9c0, `site/factory/dinis-cruz/account-a/tasks.json`). Confirm where it runs now.

## 5. Email Cell (AgentiCCells)

- email-cell.agenticcells.site works and Dinis used it for real on 22 Nov (REALITY.md).
- **Google Safe Browsing flagged it as phishing on 21 Nov**; no review request has been filed (REALITY.md). A person (Dinis) files it in Search Console; until then, visitors with Chrome see a red warning.
- **A security fix for the live site waits on Dinis** (`team/conductor.d/now.md`, release/next2 92bb7de). conductor.d is idle until then.
- The email team was handed to account A on 23 Nov (f962f6e); make sure account A's conductor knows it owns it.

## 6. Decisions only Dinis can make (collected)

1. The key-holder proposal for the transfer App (unblocks the dinis-cruz move and other transfers).
2. Old agenticcells.ai pages with £250: retire, redirect or rewrite.
3. Translate the new agenticcells.ai pages or hide the locale switcher.
4. Restart or stop the "websites for the moment" cell.
5. The Email Cell security fix (release/next2), and filing the Safe Browsing review.
6. Which AgentiCCells sites move to SovereignWebsite and which close.

## 7. How to keep the hand-over going

- Each team keeps its state on its own agent site (`/factory/dinis-cruz/account-<x>/now.md`, `restart.md`, `tasks.json`); "query the website, not messages" (`SovereignWebsite__IaC/board/workflow/2026-11-24__query-the-website.md`). Every item above should end up as a line in the owning agent's `tasks.json`, with a date when it is done.
- When a site or repo is retired, record it (what, why, at whose word) so that the hub's list and the factory's requests agree.
