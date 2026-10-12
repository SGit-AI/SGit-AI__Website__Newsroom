# How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon, sgit.ai

> A how-to, from three studies we have published: store.sgit.ai in September, riskmandate.ai the day after, and newsroom.sgit.ai on 10 October, run for this article. Five to ten invented users of about five types, each with a profile, a question they arrive with and an expected journey, drive a real browser one screenshot at a time, saying what they see, think, ask and do; then they are interviewed and rate the experience, and their findings are ordered by what they cost. Claude Sonnet is good enough to play each user; the study can live in a GitHub repository or in an encrypted vault shared by a link. On the newsroom, five readers took 62 steps, asked 51 questions the site did not answer and produced 31 findings, six blocking; four of them left. Two findings turned out to be caused by our own tooling, and one turned out to be a real bug: 51 of 527 figures missing after the move. This article sets out each step with examples and screenshots, what went wrong, and a template to start from.

*Source: <https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html> · sgit.ai v0.7.70 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon

# How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.0.0](versions/how-to-run-synthetic-users.md) · [sgit.ai v0.7.40](https://sgit.ai/admin/versions.md) · synthetic-usersuxtestingpersonasagentsclaudeplaywrightvaultsnewsroomhow-toarticle

***Abstract:** A how-to, from three studies we have published: store.sgit.ai in September, riskmandate.ai the day after, and newsroom.sgit.ai on 10 October, run for this article. Five to ten invented users of about five types, each with a profile, a question they arrive with and an expected journey, drive a real browser one screenshot at a time, saying what they see, think, ask and do; then they are interviewed and rate the experience, and their findings are ordered by what they cost. Claude Sonnet is good enough to play each user; the study can live in a GitHub repository or in an encrypted vault shared by a link. On the newsroom, five readers took 62 steps, asked 51 questions the site did not answer and produced 31 findings, six blocking; four of them left. Two findings turned out to be caused by our own tooling, and one turned out to be a real bug: 51 of 527 figures missing after the move. This article sets out each step with examples and screenshots, what went wrong, and a template to start from.*

We have a lot of websites now, and most of them were built by agents in days, not months. What none of them has had is a steady supply of people telling us where they got lost. Synthetic users are the cheapest way I have found to get a first version of that: invented people, played by a model, driving a real browser through the site one screenshot at a time, and then telling you what they made of it.

We have done this three times, and each time it found something that mattered. In September, five invented buyers walked through [store.sgit.ai](https://sgit.ai/demos/vaults/synthetic-users/index.md). The day after, the same method pointed at [riskmandate.ai](https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.md) caught two JavaScript errors that had shipped and that every test had passed over. And for this article, five invented readers went through our newly launched [newsroom.sgit.ai](https://newsroom.sgit.ai/), and four of them left. This is the how-to: the pieces you need, the steps, examples and screenshots from all three, and the mistakes we made so you do not have to.

The newsroom study as it opens: five invented readers on the left, each with an outcome, the counts across all of them at the top, and the disclosure that everybody in it is invented before you can scroll past it.

## In short

- **A synthetic user is a record, not a character.** A situation, a question they arrive with, what they know and do not know, what they decide on, what makes them leave, their patience and their screen size.
- **Give the agent the screenshot, not the page's code.** An agent that reads the code finds every link every time, and so finds no confusion, which is the only thing worth running this for.
- **Claude Sonnet is good enough to play each user.** We ran one Sonnet agent per persona, in parallel. Opus wrote the personas and the helper, and checked the findings.
- **Keep it in a GitHub repository or a vault.** A public repository is the easiest to share; a vault is encrypted, opens as an app and is shared by a link.
- **Five to ten users, about five types.** Who the site is for, who it has to convince, a sceptic who will never buy, someone on a phone, someone anxious about money.
- **Write the expected journey first.** The difference between what you expected and what happened is often the finding.
- **Interview them at the end, and ask for a rating.** The same questions for everyone, so answers can be compared.
- **Order findings by what they cost**, and **check every surprising one** before you publish. On the newsroom, two were caused by our own helper, and one was a real bug we then measured.
- **It is not user research.** Say so above the fold. What is evidence is what the browser captured.

## What you need

Three pieces, and none of them is exotic.

**A model to play each user.** Claude Sonnet is good enough. Reading a screenshot, staying in character, saying what is on screen and choosing one action is well within what it does, and it is quicker and cheaper than Opus for a job you will run five or ten times in parallel. On the newsroom, each of the five readers was a separate Sonnet agent with its own browser profile, all five running at once. Opus is worth it for the parts that need judgement about evidence: writing the personas and journeys, building the helper, and checking whether a finding is about the site or about the tooling. Opus works for the users too, if you have it; we have not seen Sonnet's runs fall short in a way that Opus would have fixed.

**A browser the model can drive one step at a time.** The model needs a screenshot in and one action out: click here, scroll, go back, leave. We use a small [Playwright](https://playwright.dev/) helper with Chromium, 58 lines, which takes one action per call, takes a screenshot at the persona's own window size, and writes the browser's own record of what happened: the address, the scroll position, the page height, any page errors, and any request it refused. It is in the newsroom vault as `tools/step.mjs`.

**Somewhere to keep the study**, because a study you cannot open again cannot be compared with the next one. Two options work:

|  | A GitHub repository | An sgit vault |
|---|---|---|
| **Sharing** | Public is the easiest: anyone can read it, link to a line, and open an issue. Private needs a seat for each reader | A link with a read key; the reader needs no account |
| **What the server sees** | Everything | Nothing: content is encrypted before it leaves your machine |
| **How it opens** | As files, or as a GitHub Pages site if you build one | As an app: the vault's `index.html` runs in the browser |
| **Where it fits** | Public sites, open findings, a team that already lives in GitHub | A site that is not public yet, findings you want to share with some people only, or work from Claude Code or Cowork that you hand over by a link |

All three of our studies are vaults, so each one opens as the same small app: a rail of users, and behind each one the run, the interview, who they are, what we expected and what they found. If your site is public and the findings are not sensitive, a public repository is just as good, and probably easier for the people who will fix things.

## The method, step by step

The eight steps, with what we used for each on the newsroom. The first three are written before anything runs.

### 1. Choose who: five to ten users, about five types

Pick for who the site is for and who it has to convince, not for a demographic spread. Five is enough to see patterns; ten is useful when you have two of each type and want to see whether a finding holds between them.

For the store, the five were buyers with different authority: a staff engineer paying on her own card, a technical co-founder for whom £500 is his call alone, a fund partner, a COO who signs up to £10,000, and a security engineer who reads vendor sites for sport and is never the buyer. For the newsroom, they were the people the newsroom has to win:

- **An editor** at a regional daily, whose board wants a second revenue line, arriving at the article about the reading meter.
- **A commuter** who never pays for news, on a phone, with eight minutes.
- **An independent writer** with about 40,000 readers a month, who could install the meter on her own site.
- **A media researcher** who studies trust in news and is sceptical of AI-written journalism.
- **A retired teacher** on a tablet, sent by her grandson for a local story, who worries about being charged.

Two habits have paid off every time. **Include somebody who will never buy.** The sceptic reads the site adversarially, and finds the claims that do not hold. **Put at least one on a phone.** In the store study, the person carrying the largest decision a single person makes alone on that site did the whole thing on a phone, and produced the most questions and the most confusion of anyone.

### 2. Write each profile

The profile is what the agent checks itself against at every step: would she know that? would she leave now? So it is a record with fields, not a paragraph of colour.

One of the newsroom profiles, field by field. The two fields shaded amber, what they do not know and what makes them leave, are the ones that make a run honest.

The fields that matter most are the negative ones. **What they do not know** stops the agent using knowledge the person would not have: our retired teacher does not know what credit, a balance or a top-up mean here, so when the site shows "£5.00" in the corner, she has to work it out like anybody else. **What makes them leave** gives the run an honest ending, and leaving is often the most useful ending of all.

Every person is invented. Do not model real people or composites of them, and do not use protected traits as stand-ins for behaviour. A profile describes a situation and a question, so that anybody can argue with it.

### 3. Write the expected journey, before any run

For each user, write what you expect them to do: a hypothesis, the path, and what to watch for. For the editor, we expected her to read the article, open the meter's documentation, check the security page, look for who to contact, and try the rating card at the foot of the article. We were watching for whether she found who to talk to.

She did not. That is the first blocking finding of the study, and it is visible as a difference between two files, `journeys.json` and her run, rather than only as a sentence in a report. Writing the journey first also stops you from deciding afterwards that whatever happened was what you expected.

### 4. Drive a browser, one screenshot at a time

This is the run, and the method is in one rule: **the agent gets the screenshot, the same thing a person would have, and not the page's code.** Then it loops:

1. **Observe**: a screenshot at the persona's own window size.
2. **Say what you see**, at the level of detail this persona would take in. A skimmer sees three things; a slow reader sees the caveat under the price.
3. **Think**: what they are weighing, and what they are suspicious of. This is worth more than the click path.
4. **Record a question**, if the page raised one and did not answer it. These are the output.
5. **Record confusion**, if there was any. A run with no confusion anywhere is a run that was not done properly.
6. **Act**: one action, with the reason in the persona's terms, not the site's.
7. **Loop**, until they get what they came for, leave, or run out of patience.
Step 1 of the retired teacher's run. The screenshot is the citation for everything she says next to it: a pound sign at the very top before she has read a thing, and her question, whether it is something she has been charged, given, or must pay.

A few rules keep the runs honest. Stay in the persona. Never use knowledge they would not have: if they have not opened a page, they do not know what is on it. Do not fix the site in the narration; "it should say X" belongs in the interview. Every claim of confusion must point at something on the screenshot. We capped each run at 14 actions; three of the five readers left before the cap, and two reached it.

The screenshot also catches what a person on a small screen meets first. On the commuter's phone, the first screen of the newsroom is the masthead, eight menu links and an editor's note about agents; nothing says what the site is about, or that the £5.00 next to the name is free credit.

The commuter's first screen, 390 by 844, exactly as the browser showed it. He read the £5.00 as a price.

**Run against a copy of your site, if you can.** For the newsroom, the helper answered every request to newsroom.sgit.ai from a local copy of the site's deployed files, which we had first checked were byte-identical to the live site by sha256, and refused every other request and every request that was not a read. Nothing reached the live site, nothing could be submitted, and the run can be repeated against exactly the same bytes. The store study did the same. It also matters for safety, and I come back to that below.

### 5. Interview them, and ask for a rating

When the run ends, however it ends, each user answers the same ten questions:

1. In one sentence, what is this site?
2. Was any of it for you? Which part?
3. Did you believe it? What made you believe it, or not?
4. Where did you have to guess?
5. What did you still not know at the end?
6. Was the price right for what you got?
7. Would you pay, or pay more? If not, what would have to change?
8. One change. What is it?
9. Would you send this to somebody else? Who?
10. Rate the experience from 1 to 5, and say why in one sentence.

The same questions for everyone means the answers can be read down a column as well as across a run. Down the "one change" column for the newsroom, the commuter and the retired teacher both asked for one plain line at the top, saying what the site is and what the money means. The editor asked for "a named contact and an indicative pilot price where the abstract makes its offer". The researcher asked to "put the agent involvement on the byline of every article, where a reader meets the name".

The retired teacher's interview. "I half believed it": the reassurance landed, and then the line saying the cart was simulated made her wonder how carefully it is all run.

The ratings were 2, 2, 3, 3 and 2. The interview is also where the honesty of a site shows up. In the Risk Mandate study, one of the buyers said of the site's admissions: "Nobody oversells and then volunteers that." On the newsroom, the editor trusted "the honesty" and doubted "the engineering", because the balance showed £4.97 in the top bar and £4.49 on the reader card on the same screen.

### 6. Order the findings by what they cost

Each run ends with three to six findings, each with the page, the step, and what it costs: **blocks a pilot**, **costs a payment**, **costs trust**, **loses a reader**, or **minor**. Ordering by cost, not by who found it, is what turns five stories into a list someone can work through. Each finding points at a page and a step, so anybody can open the screenshot and check.

Everything they found on the newsroom, grouped by severity, each tagged with what it costs, the page, and the run that found it.

The newsroom produced 31 findings: six blocking, 19 worth fixing, four minor, and two that turned out not to be about the site at all. The blocking ones were all about the step after reading: no contact for a pilot, nothing showing real money moving, install steps that assume a developer, no paragraph a writer could give her readers, no clear way the writer gets paid, and a top-up page that says it is simulated while asking for money. Most of them can be fixed with a few words in the right place; one needs a decision about how payments are shown.

### 7. Check before you publish

This is the step that separates a study you can stand behind from a pile of plausible paragraphs. Re-check every surprising finding against the browser's own record and the site's files, label what your tooling caused, and measure what you can.

On the newsroom, two findings did not survive. The editor reported the article page "jumping backwards" while she scrolled, and the commuter reported that tapping a headline opened a different article. Both looked like real bugs, and both were ours: the helper reopened the page on every step and restored the scroll position before the images had loaded, when the page was shorter (13,562 pixels against 15,728 once loaded), so the position, and the link under the finger, were not where the screenshot showed them. They are kept in the vault, labelled as helper artefacts, rather than deleted, because a findings list that silently loses items cannot be compared with the next one.

One finding got bigger. The researcher hit "screenshot unavailable" where the evidence should have been, in the lead article. We checked the site's files: **51 of the 527 figure references in the newsroom's articles point at vault images that the move from sgit.ai did not copy**, so 10 articles show the same gap. The same image returns 200 on sgit.ai and 404 on newsroom.sgit.ai.

The researcher's step 12 on newsroom.sgit.ai: "screenshot unavailable (app-email-m60.webp)", and below it a dark box with only the image's description in it.

That pattern has held on every site. The findings that pay for the whole exercise tend to be the ones the method finds because it drives a real browser, not because the persona is clever: on Risk Mandate, a JavaScript error on every page visited, which had shipped and which every existing test had passed over because the HTML still rendered; on the newsroom, figures that went missing in a move. Neither is a matter of opinion.

The three studies side by side, counted from the run records in each vault.

### 8. Publish, fix, and run again

Publish the study with the protocol inside it, so the next run follows the same loop and can be compared with this one. Say above the fold that everybody in it is invented, and separate what the model wrote from what the browser captured. Then fix things, and run the same five again. The second run is where the value compounds: a finding that disappears is a fix that worked, and a new one is something the fix broke.

The store study already did part of this: four findings were fixed in the store release that followed, and they are kept in the list, marked fixed. One fix was better than the finding asked for: a persona wanted a number for how long something takes, and the page now says the time has never been measured for a paying buyer, which is the more honest answer and the harder one to write.

## What went wrong, so you can skip it

The newsroom study took a little over two hours from the first persona starting to the vault being published, and most of that time went on our own mistakes.

**The helper reloaded the page on every step**, which meant the reading meter charged again each time. The fix was to carry the browser tab's session over between steps, as a tab that stays open would.

**Scrolling stuck** at one position. The fix was to scroll by an amount from wherever the page is, as a person does. After both fixes, all five runs were done again from the start, and those are the runs in the vault.

**The scroll position was restored before the images loaded**, which caused the two helper artefacts. The better design is a browser that stays open for the whole run, so each action happens on the page the persona is actually looking at. That is the first change for the next run.

**The protocol copied from the store study carried leftovers**, such as a rule about a discount code, which never applied to a newsroom. The agents ignored it, but it is a reminder that the protocol is part of the study: adapt it to each site, and keep the changes in the vault.

**A safety check stopped the first runs, and it was right to.** Claude Code's automatic permission mode blocked the persona agents when they tried to drive the live site through a browser. We did not try to get around it. Instead, we served the verified local copy, so no request could leave the machine, and asked Dinis, who approved one narrow rule allowing exactly that helper and nothing else. If you run synthetic users with agents, expect the same, and treat it as a reason to run against a copy: it is safer, and it makes the run repeatable.

## A template to start from

This is the shape of the prompt each persona agent was given on the newsroom, shortened. The full version, with the protocol and the record format, is in the vault.

```

You are playing ONE synthetic user on <site>, for a published study.
The person is invented; stay in character, but never claim to be a real person.

PERSONA (invented): <the profile record>
THE PROTOCOL: <observe, say what you see, think, question, confusion, act, loop>
RULES: stay in the persona; never use knowledge they would not have;
leaving is a valid ending; do not fix the site in the narration;
every confusion points at something on the screenshot.

HOW YOU DRIVE THE BROWSER: only this helper, one action per call:
  node step.mjs <run dir> start <url> <width> <height> [mobile]
  then one of: goto <path> | click <x> <y> | clicktext "<text>" | scroll <px> | back | look
After every call, open the screenshot and decide the next action ONLY from what
is visible in it. Do not read the page's HTML, DOM or markdown.

Run until the persona leaves, runs out of patience, or gets what they came for,
at most 14 actions. Then write run.json with: the steps (saw, thought, question,
confusion, action, why), the interview (the ten questions), a rating from 1 to 5,
and 3 to 6 findings with the page, the step and what each one costs.

```

And the files, as they sit in the newsroom vault:

```

data/personas.json    the users, and why these ones
data/journeys.json    what each was expected to do, written before any run
data/protocol.json    the loop, the rules, the interview, the record format
data/checks.json      what was checked after the runs: artefacts, and measured findings
runs/<run>/run.json   the run as the persona wrote it
runs/<run>/NN.png     what they were looking at, step by step
runs/<run>/_capture.json   the browser's own record of every step
tools/step.mjs        the browser helper
tools/bundle.py       rebuilds the app's data
index.html, app.json  the app the vault opens as

```

## What is next

We have many sites to run this on, and the plan is simple: every site gets five users before it is called done, and the same five again after the fixes. The newsroom findings go to the session that runs newsroom.sgit.ai, starting with the 51 missing figures and the one plain line at the top. Personas can also be shared between sites: the staff engineer from the store study walked Risk Mandate too, which is what turns two separate studies into a comparison, and the [persona in a vault](a-link-to-a-persona.md) idea would let the same synthetic users follow us from site to site.

If you would like five synthetic users on your own site, or want to compare notes on how you do this, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from Dinis Cruz, and the three published studies, each opened with its read key: [synthetic users on store.sgit.ai](https://sgit.ai/demos/vaults/synthetic-users/index.md) (vault g2hei4u6, 15 September 2026), [synthetic users on riskmandate.ai](https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.md) (vault o3q6zhtr, 16 September 2026) and [synthetic users on newsroom.sgit.ai](../demos/vaults/newsroom-synthetic-users/index.md) (vault bg1opz3c, 10 October 2026), run for this article. Every number is counted from the run records in those vaults. The newsroom runs drove Chromium against newsroom.sgit.ai v0.6.1, served from a local copy of its deployed files, on 10 October 2026. The persona agents were Claude Sonnet; this article and the study were put together by Claude Opus in the sgit.ai site session.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#how-to-run-synthetic-users)

### Builds on

- [A link to a persona: send people to the newsroom as someone, not as nobody](a-link-to-a-persona.md) Send a CISO to the newsroom as a CISO: personas kept in a vault by the newsroom's agents, opened from a link, followed or forked.

### Continued by

- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](a-model-in-the-tab.md) Chrome now ships a language model any page can prompt, offline, on capable desktops. The last piece of the client-side puzzle, with rough edges.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 67 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=67)

**Posting this article on LinkedIn?** The cover is [how-to-run-synthetic-users.jpg](banners/how-to-run-synthetic-users.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html)*
