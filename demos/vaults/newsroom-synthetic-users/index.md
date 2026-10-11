# Synthetic users, newsroom.sgit.ai, five invented readers, sgit.ai

> Five invented readers drove a browser through newsroom.sgit.ai one screenshot at a time, were interviewed and rated it: 62 steps, 51 questions, 31 findings, six blocking, two labelled as helper artefacts, and a measured bug of 51 missing figures. Published with its read key.

*Source: <https://newsroom.sgit.ai/demos/vaults/newsroom-synthetic-users/index.html> · sgit.ai v0.7.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](https://sgit.ai/demos/vaults/index.md) / Synthetic users · newsroom.sgit.ai

# Synthetic users, third run: five people who do not exist, reading newsroom.sgit.ai

Five invented readers each drove a browser through [newsroom.sgit.ai](https://newsroom.sgit.ai/) one screenshot at a time, on 10 October 2026, said what they saw, thought, asked and did at every step, and were interviewed and asked for a rating at the end. **62 steps, 51 questions the site did not answer, 56 places somebody got lost, and 31 findings, six of them blocking.** Four of the five left; the researcher kept reading. It is the same method as [the store study](https://sgit.ai/demos/vaults/synthetic-users/index.md) and [the Risk Mandate study](https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.md), and it was published with the how-to article [How to run synthetic users on your own site](../../../articles/how-to-run-synthetic-users.md).

Five readers, five outcomes, and the disclosure above the fold.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_12a24c3e7c90295577788971088c70e42b747fe274d2b543cee8b263909f7f36:bg1opz3c`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_12a24c3e7c90295577788971088c70e42b747fe274d2b543cee8b263909f7f36%3Abg1opz3c) · From the CLI: `sgit clone sgit_public_read_12a24c3e7c90295577788971088c70e42b747fe274d2b543cee8b263909f7f36:bg1opz3c`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0.

**Everybody in it is invented, and the vault says so first.** The personas, their names and every word attributed to them were written by a language model (Claude Sonnet, one agent per persona) reading screenshots. **It is not user research**, and no sentence in it is evidence about a real person. What *is* evidence is what the browser produced: the screenshots, the addresses, the scroll positions, the step order and the page-error counts, captured by driving Chromium against newsroom.sgit.ai v0.6.1, served from a local copy of the deployed files verified byte-identical to the live site by sha256. Every other request was refused, so nothing reached the live site and nothing could be submitted.

## See it live, here

The vault opens as an app: a rail of five readers, and behind each the run, the interview, who they are, what we expected and what they found. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_12a24c3e7c90295577788971088c70e42b747fe274d2b543cee8b263909f7f36%3Abg1opz3c).

## The five readers

| Persona (invented) | Arrives with | Outcome | Steps | Questions | Confusions | Viewport | Rating |
|---|---|---|---|---|---|---|---|
| **Hannah Okafor**: head of digital at a regional daily | Could my paper use this, and what would it take? | left | 14 | 11 | 12 | 1440×900 | 2/5 |
| **Leo Marchetti**: junior analyst, reads news on the train | Is this worth my eight minutes, and is it going to ask me for money? | left | 13 | 9 | 12 | **390×844** | 2/5 |
| **Ruth Adeyemi**: independent writer, about 40,000 readers a month | Could I put this on my site this weekend, and would my readers pay? | left | 10 | 10 | 10 | 1366×768 | 3/5 |
| **Dr Samir Haddad**: media researcher, studies trust in news | Who writes this, how do I know what is true, and what are they not telling me? | **kept reading** | 14 | 12 | 12 | 1680×1050 | 3/5 |
| **Margaret Lindqvist**: retired teacher, reads local news daily | Will this cost me money, and can I trust what it says? | left | 11 | 9 | 10 | **820×1180** | 2/5 |

Zero page errors on all five runs. The ratings average 2.4 out of 5. Every number above is counted from the run records in the vault.

The first money she sees is a £5.00 chip with no label. Her first question is whether it is something she owes.

## What it found

Findings are ordered by what they cost, each with the page and the step, so anyone can go and check. The six blocking ones:

1. **No way to contact anyone about a pilot.** The article invites sites with traffic to test the meter; the Replicate page ends with no named person, email or form. (Editor)
2. **Nothing shows real money moving.** No count of payments, readers or revenue, so a buyer cannot tell a demo from a running business. (Editor)
3. **The install steps assume a developer.** Five file paths, ES modules and relative paths, with no download and no word about hosted platforms. (Writer)
4. **No paragraph a writer could give her readers** about what the meter does and why it will not block them. (Writer)
5. **How the writer gets paid is not clear**, when balances live in the reader's browser and can go below zero. (Writer)
6. **The top-up page says it is simulated while asking for money.** She could not tell whether real money would move. (Local reader)

Among the 19 worth fixing: the first screen on a phone does not say what the site is or that the £5 is free credit; "credit can go below zero" reads as a debt; the balance drops by a penny on opening a page with no notice there; "How the meter works" leads to developer documentation; the byline names one human while the AI authorship is in the footer; three version numbers appear for one site; and the Replicate page has no balance chip.

Grouped by severity, tagged by cost, attributed to the run that found it.

## The bug it found, measured

The researcher hit "screenshot unavailable (app-email-m60.webp)" in the lead article, where the evidence should have been. That was checked against the site's files after the run, and it is not alone: **51 of the 527 figure references in the newsroom's articles point at vault images under `/demos/vaults/*/images/` that the move from sgit.ai did not copy**, so 10 articles show the same gap. The same image returns 200 on sgit.ai and 404 on newsroom.sgit.ai (checked 10 October 2026).

The researcher's step 12, exactly as the browser showed it.

## Checked after the run, and what was not the site

Two findings were caused by the helper that drove the browser, not by the site, and they are kept and labelled rather than deleted: the editor's page "jumping backwards" while scrolling, and the commuter's taps opening the wrong article. The helper reopens the page on every step and restores the scroll position before the images have loaded, when the page is shorter (13,562 pixels against 15,728 once loaded), so the position and the link under the finger were not where the screenshot showed them. A person scrolling an open page would not see this, although layout shift while images load is worth checking on a phone.

The same ten questions for every reader, so the answers read down a column as well as across a run.

## How it is built

`data/personas.json` holds the five readers and why they were chosen; `data/journeys.json` the path each was expected to take, written before any run; `data/protocol.json` the observe, think, act loop, the driver and the interview; `data/checks.json` what was checked after the runs. Each run is `runs/<date>-<persona>-01/`: `run.json` as the persona wrote it, one PNG per step, and `_capture.json`, the browser's own record of every action, address, scroll position, page height, page error and refused request. `tools/step.mjs` is the 58-line Playwright helper (one action per call, one screenshot after it) and `tools/bundle.py` rebuilds the app's data. The app is the one from the store study, adapted.

The protocol is in the vault, so the next run can be compared with this one.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, the SG/Send access token, and the vault's own key, passphrase and write key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, produced nothing.

**What changed after the first push.** Version 0.1.1 adapted the protocol file to the newsroom: the store study's discount-code rule, given to the agents as written, is kept as a labelled note because it never applied; the record fields and the driver are described as built; and two answers that guessed a pronoun for the site's author were reworded.

**What it does not claim.** It is not user research. Five invented readers are a structured reading of the site from five points of view, good for finding where a page loses someone and poor at saying how many real people it would lose.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py bg1opz3c <read key hex>`, read-only, no token, no clone.

- **Files:** 83 · **plaintext size:** 11991 KB
- **Commits:** 3 · **last updated:** 2026-10-10 · **HEAD:** `obj-cas-imm-31bd2d3ef28c`
- **Top level:** `FINDINGS.md`, `README.md`, `app.json`, `data/`, `index.html`, `runs/`, `tools/`
- **File types:** .png ×62, .json ×16, .md ×2, .html ×1, .py ×1, .mjs ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**The site it reads.** [newsroom.sgit.ai](https://newsroom.sgit.ai/), the newsroom moved from sgit.ai in October, with the reading meter described in [Pay after you read](../../../articles/pay-after-you-read.md).

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](https://sgit.ai/demos/vaults/index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/demos/vaults/newsroom-synthetic-users/index.html)*
