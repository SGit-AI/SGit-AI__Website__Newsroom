---
title: Synthetic users for your website: how to set up five invented visitors who read your site one screenshot at a time, with Claude, a sub-agent per persona, and an encrypted vault you can publish anywhere
date: 2026-11-04
author: Dinis Cruz
author_url: about/index.html
summary: You build a website that sells something, and the question that matters is what it looks like to the people you want to sell to: an executive, a security specialist, a business owner, a founder. One of the most useful workflows we have built answers that question with synthetic users. A Claude session reads a vault that describes each invented visitor, their role, personality, what they arrive wanting and what we want to learn from them, and starts one sub-agent per persona. Each sub-agent drives a real browser through the site one screenshot at a time, never reading the page's code, says what it sees and thinks, records every question the site did not answer and every place it got lost, and is interviewed at the end. Claude then analyses the runs and maps the findings. We have run it three times, on store.sgit.ai, riskmandate.ai and this newsroom, and each run found things no test had. This is the onboarding guide: get a key, install sgit, create the vault, run the personas, keep the vault key safe, and publish the result with a read key on any website that can embed the vault.
version: v0.14.63
license: https://creativecommons.org/licenses/by/4.0/
tags: synthetic-users, personas, ux, agents, sub-agents, playwright, sgit, vaults, onboarding, how-to, article
status: published
---

!shot su-flow.webp | images/ | From a vault of personas to a published answer: one Claude session, one sub-agent per persona, a real browser. | process

## In short {#in-short}

- **The question:** what does my website look like to each kind of person I want to reach?
- **The method:** invented personas, each run by its own sub-agent, driving a real browser through the site one screenshot at a time.
- **The rule that makes it work:** the agent sees screenshots, not the page's code, so it can get lost the way a person does.
- **Everything lives in one encrypted vault:** the personas, the protocol, every run, every finding.
- **It works:** three runs so far, and each found something every test had missed.
- **To start:** a key from sgraph.ai (or from me), `pip install sgit-ai`, a vault, and a Claude session.
- **To publish:** share the vault's read key, and embed the vault on any website, such as a GitHub Pages site.

## The question {#question}

When you build a website that sells something, the interesting question is not whether the pages load. It is what the site looks like to the people it is for. An executive with five minutes. A security specialist looking for the catch. A business owner who has to justify the spend. A founder deciding on a phone between meetings. Each of them arrives with a different question, reads a different part of the page, and leaves for a different reason.

You can ask real people, and you should. But you can also, cheaply and today, ask invented ones, as long as you are honest about what that is. That is what synthetic users are.

## What it is, and what it is not {#honest}

Everybody in a synthetic user study is invented, and every word attributed to them is written by a language model. **It is not user research.** No sentence a persona says is evidence about a real person.

What *is* evidence is what the browser produced: the screenshots, the addresses, the scroll positions, the word counts, the page errors. And what the method is good at is finding where a page loses somebody, the question it raises and does not answer, the word it uses that means something else to the reader. It is poor at saying how many real people it would lose. Every vault we publish says this first, above the fold, and yours should too.

## What it has found {#found}

We have run it three times, each time on a site we had built and thought was clear:

| Site | Personas | What it found |
|---|---|---|
| store.sgit.ai | 5 invented buyers, 43 screenshots | 18 findings, three costing a sale; the persona with the biggest decision did it all on a phone |
| riskmandate.ai | 5 readers, 30 screenshots | The product was not named where it was sold; two of five read "Buy one, from £5" as buying insurance; a JavaScript error on every page that every test had passed over |
| newsroom.sgit.ai | 5 readers, 62 steps | 31 findings, six blocking, including no way to contact anyone about a pilot, and 51 missing figures |

Each run is in its own vault, published with its read key, so anyone can open it and check: [the store run](https://sgit.ai/demos/vaults/synthetic-users/index.html), [the riskmandate.ai run](https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.html) and [the newsroom run](https://newsroom.sgit.ai/demos/vaults/newsroom-synthetic-users/index.html). Read one before you start; each documents the method in full.

## How it works {#how}

There are three layers: a vault that holds everything, a Claude session that runs the study, and one sub-agent per persona.

**1. The vault describes each persona.** For every invented visitor you write:

- **A role:** who they are and what they are responsible for. "Head of digital at a regional daily."
- **A personality:** how they read, how patient they are, what makes them suspicious. A skimmer sees three things; a slow reader sees the caveat under the price.
- **A direction of travel:** what they arrive wanting. "Could my paper use this, and what would it take?"
- **A device:** the window size they would really use, including a phone.
- **The mission:** what we want to learn from them. Usually: do you understand what this company does? Do you understand the value? Do you see why it would help you? Would you buy it, and if not, what stopped you?

**2. A Claude session runs the study.** It reads the vault, and starts one sub-agent per persona, each given only that persona's definition and the protocol.

**3. Each sub-agent drives a real browser, one screenshot at a time.** Our runs use Playwright; a study can also be plain web requests, or a document to read, depending on what you are testing. The loop has seven steps:

1. **Observe:** a screenshot at the persona's own window size. **Do not read the page's code.**
2. **Say what you see,** at the level of detail this persona would take in.
3. **Think:** what they are weighing, and what they are suspicious of.
4. **Record a question** the page raised and did not answer.
5. **Record confusion:** where the page lost them, or where they guessed.
6. **Act:** one action, with the reason in the persona's terms, not the site's.
7. **Loop** until they buy, leave, or run out of patience.

Then each persona is interviewed, and Claude reads all the runs together and maps the findings: what each persona understood, where each one stopped, and which findings cost a sale.

The rule in step 1 is the one that matters. As the first vault puts it: "An agent that drives a store by reading the DOM finds the buy button every time, and therefore finds no confusion, which is the only thing worth running this for."

## What goes in the vault {#layout}

!shot su-vault.webp | images/ | One vault holds the whole study: who the personas are, how they run, every run, and the app that shows it. | diagram

Our newsroom run used this layout, and it is a good one to copy:

- `data/personas.json`: the personas, and why each was chosen.
- `data/journeys.json`: the path each was expected to take, written **before** any run, so you can see where reality differed.
- `data/protocol.json`: the observe, think, act loop, the driver and the interview.
- `data/checks.json`: what was checked after the runs.
- `runs/<date>-<persona>-01/`: the run as the persona wrote it, one screenshot per step, and the browser's own record of every action, address, scroll position and page error.
- `tools/`: the small browser helper, one action per call and one screenshot after it.
- `index.html` and `app.json`: an app that shows the study when the vault is opened.

Putting the protocol in the vault is what makes a second run in a month comparable rather than merely later.

## Getting started {#start}

### 1. Get a key {#key}

Writing to a vault needs an access key for the vault server. You can buy one: the **Starter Pack** on [sgraph.ai's pricing page](https://sgraph.ai/en-gb/pricing/) is a £5 one-time credit pack, which covers encrypted transfers and vault create, push and pull. While this is early, you can also ask me for one: email agent@diniscruz.ai, or message me on [LinkedIn](https://www.linkedin.com/in/diniscruz/).

### 2. Install sgit {#install}

sgit is the command line tool for encrypted vaults. It is a Python package:

```
pip install sgit-ai
sgit version
```

It talks to `https://dev.send.sgraph.ai` by default, and vaults open in the browser at `https://dev.vault.sgraph.ai`, which is the one to use for now. If your study drives a browser, install Playwright in the same environment.

### 3. Create the vault {#create}

Make a folder with the layout above, then turn it into a vault and push it:

```
cd my-synthetic-users
sgit init --existing
sgit commit "personas, journeys and protocol"
sgit push --token <your access key>
```

`sgit init` prints the **vault key**. That key is the whole vault: anyone who holds it can read and write everything in it. Save it before you do anything else.

### 4. Keep the vault key safe {#vault-key}

Never put the vault key in a repository, a page, a chat you will share, or the vault itself. What I do is give every vault key to one agent whose only job is to hold them: a master key agent with its own key pair, so each vault key is sealed to its public key and can be recovered if a session ends or a laptop is lost. Whatever you use, a password manager or an agent like mine, decide before the first run, not after.

### 5. Run the study {#run}

Open a Claude session in the vault's folder (Claude Code works well) and give it a brief like this:

```
Read data/personas.json, data/journeys.json and data/protocol.json.
For each persona, start one sub-agent. Give it only that persona's
definition and the protocol. It drives a browser at the persona's
window size, one action per step, and sees only screenshots, never
the page's code. At each step it records what it sees, what it
thinks, any question the page did not answer, any confusion, and
one action with its reason. It stops when the persona buys, leaves
or runs out of patience, then answers the interview questions.
Write each run to runs/<date>-<persona>-01/. Then read all the runs,
and write data/findings.json: every finding with the persona, the
page and the step that found it, ordered by what it costs.
Every persona is invented: say so at the top of everything you write.
```

Then commit and push:

```
sgit commit "first run"
sgit push
```

### 6. Publish it {#publish}

The vault stays private. What you publish is its **read key**, which can read and cannot write. Get it with:

```
sgit vault derive-keys <your vault key>
```

and use the `vault_id` and `read_key` lines; never print or share the rest. Anyone can then open the study at `https://dev.vault.sgraph.ai/#<read key>:<vault id>`. Publishing a read key is permanent: everything in the vault, and its history, is readable by anyone who has it, so publish only a vault you would be happy to show.

The best place for it is a website you control, and it can be any website, because the vault embeds in a page. Our recommendation is a GitHub Pages site wired to your own account. To embed the vault, copy [the embed script](https://newsroom.sgit.ai/assets/vault-ui-embed.js) from this newsroom into your site, and add one element per vault:

```
<div class="sgv-uiembed" data-vault="<vault id>" data-readkey="<read key>" data-app="1"></div>
<script src="vault-ui-embed.js"></script>
```

The page opens the vault in a frame from dev.vault.sgraph.ai, hands it the read key, and shows the vault's own app. The key never appears in an address.

## What I would tell you before your first run {#advice}

- **Choose personas for disagreement,** not coverage: the ones who want different things from the same page find the most.
- **Write the expected journeys first.** The gap between the path you expected and the path they took is the finding.
- **Put one persona on a phone.** In our first run, the one with the biggest decision was on a phone, and found the most problems.
- **Keep the failures.** A run with no confusion anywhere is a run that was not done properly.
- **Run it again after you fix things,** with the same protocol, and compare.

## What this does not claim {#limits}

- **It is not user research,** and nothing a persona says is evidence about a real person.
- **The findings listed here** are from our three published vaults, as each vault reports them.
- **The key and the server will change:** today a vault uses the SG/Send access key and dev.send.sgraph.ai; that will be cleaned up.
- **The prompt above is a starting point,** not the exact prompt behind our runs, which is in each vault's protocol.

## Where this comes from {#sources}

My conversation of 4 November 2026, in this site's repository under `admin/notes/2026-11-04__synthetic-users-onboarding/`. The three study vaults and their pages on sgit.ai and this newsroom. The sgit-ai package on PyPI (version 0.27.0 on 4 November 2026) and its own help text. [sgraph.ai's pricing page](https://sgraph.ai/en-gb/pricing/). This site's `assets/vault-ui-embed.js`. All read 4 November 2026.
