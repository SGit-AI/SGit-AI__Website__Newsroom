# A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle, sgit.ai

> Since Chrome 148, on 5 May 2026, any web page can talk to a language model that runs on the reader's own machine: Gemini Nano, through the Prompt API, with text, image and audio input, JSON-schema output, and no network once the model is downloaded. For the pattern I described in No server, by design, that is the missing piece, because the hardest thing to move to the client was always the intelligence itself. I tried it this week, and the experience was rough: a download with no sense of time, a progress bar that vanished on refresh, and a model that turned up by the morning. That is partly the platform and partly the pages, and the documentation explains most of it. I also looked for good examples in the wild and found very few, which is less strange than it looks: the API shipped five months ago, over formal objections from Mozilla, Apple's WebKit team and the W3C TAG, to desktops with a 22 GB free-disk floor, in five languages, with tool calling still experimental. This article is a briefing on what actually works today, an honest account of the rough edges, the case for and against building on it, and a map of where we can put it to real use: answers grounded in the graph instead of the prose, personas inferred without leaving the browser, voice memos transcribed on the device, alt text for every figure, and a download experience that tells people what is happening.

*Source: <https://newsroom.sgit.ai/articles/a-model-in-the-tab.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle

# A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/a-model-in-the-tab.md) · [sgit.ai v0.7.46](https://sgit.ai/admin/versions.md) · client-sidegemini-nanoprompt-apichromebuilt-in-aion-deviceprivacysovereigntyinteroperabilitywebmcpnewsroompersonasarticle

***Abstract:** Since Chrome 148, on 5 May 2026, any web page can talk to a language model that runs on the reader's own machine: Gemini Nano, through the Prompt API, with text, image and audio input, JSON-schema output, and no network once the model is downloaded. For the pattern I described in No server, by design, that is the missing piece, because the hardest thing to move to the client was always the intelligence itself. I tried it this week, and the experience was rough: a download with no sense of time, a progress bar that vanished on refresh, and a model that turned up by the morning. That is partly the platform and partly the pages, and the documentation explains most of it. I also looked for good examples in the wild and found very few, which is less strange than it looks: the API shipped five months ago, over formal objections from Mozilla, Apple's WebKit team and the W3C TAG, to desktops with a 22 GB free-disk floor, in five languages, with tool calling still experimental. This article is a briefing on what actually works today, an honest account of the rough edges, the case for and against building on it, and a map of where we can put it to real use: answers grounded in the graph instead of the prose, personas inferred without leaving the browser, voice memos transcribed on the device, alt text for every figure, and a download experience that tells people what is happening.*

The client-side puzzle. Files, state, storage, payments and, next, identity were already off the server. Intelligence was the piece that kept a back end in the picture. Since May 2026, on capable desktops, Chrome supplies it.

In [No server, by design](no-server-by-design.md), I listed what still seems to need a server, and one row was models. The answer I gave was "in the client, with the reader's own key, or a small local model". That row just got a lot more interesting.

Since Chrome 148, released on 5 May 2026, any web page can talk to a language model that runs on the reader's own machine. Not a model the page downloads itself, but one the browser ships and manages: Gemini Nano, through a JavaScript interface called the Prompt API. Once the model is on the device, the network is not needed at all. No key, no bill per token, and nothing sent to anyone.

For the client-side pattern, this is the most important piece so far, and the hardest one. Files, state, storage and payments were always going to move to the browser; they are things browsers were built for, and as of today the newsroom's payments are live, on a Stripe link and nothing of ours. Intelligence was the piece that kept a back end in the picture. A page could download a model of its own and run it in the browser, and libraries have done that for a while, but every site paid the download separately and few readers would wait for it, so in practice a model behind a page meant renting one somewhere and calling it. Now, on capable desktops, the browser supplies one, once, for every site. It is in the tab.

So I tried it. And this article is what I found: what actually works, why the experience was as rough as it was, why there are so few good examples, the honest case against building on it, and a map of where I think we can put it to real use.

## In short

- **It is real, and it is stable.** The Prompt API shipped to all web pages in Chrome 148 on 5 May 2026, after being available to Chrome extensions since Chrome 138. The Summarizer, Translator and Language Detector APIs have been stable since 138. Writer, Rewriter and Proofreader are still developer trials.
- **It does more than chat.** It accepts text, images and audio (a video counts as its current frame); it returns text, optionally constrained by a JSON schema; it keeps sessions, clones them, and reports how much of its context window is used. Five languages so far: English, Japanese, Spanish, German and French.
- **Tool calling is not there yet.** Native tool use in the Prompt API is experimental and behind a flag. What works today is structured output: ask for JSON that names a tool and its arguments, and your code runs it. WebMCP, which lets a site describe its own tools to the reader's agent, is a separate API, in origin trial.
- **The rough download was mostly the pages, not the model.** The download carries on in the background when the tab is refreshed or closed, and resumes after a restart. What the refresh lost was the progress bar, because a page only sees progress for downloads it asks about. Chrome's own guidance says what a good page should show; the demo pages I used did not.
- **There are few good examples for real reasons.** Five months on the open web; desktop only; 22 GB of free disk, a GPU with more than 4 GB of video memory or 16 GB of RAM; a download of roughly 4 GB; five languages; and formal opposition from Mozilla, WebKit, the W3C TAG and Microsoft, which makes careful teams wait.
- **The objections are serious, and they line up with things I care about.** One vendor's model, and one vendor's usage policy, behind a web API. Prompts tuned to Gemini Nano may not travel. The way to build on it without being captured by it is to keep the meaning in the data, not in the prompt.
- **The fit with what we have built is unusually good.** A graph answer from the five readers is about 2,600 tokens; a small model's context window is small. Answers grounded in anchored graph slices, personas inferred locally, voice memos transcribed on the device before they go into a vault lane, alt text for the 527 figures, and a download panel that tells people the truth.

## What Chrome actually ships

Chrome now has a family of built-in AI APIs. Some run on small task-specific models; the rest run on Gemini Nano, a model in the 2 to 4 billion parameter range that Chrome downloads once per device, not once per site.

What Chrome ships today: the built-in AI APIs and their status, what the Prompt API accepts and returns, the hardware it needs, and how the browser manages the model's life. Status from Chrome's own documentation, as of October 2026.

| API | What it does | Status on the web |
|---|---|---|
| **Prompt API** | Free-form prompts to Gemini Nano, with text, image and audio input | Stable since Chrome 148 (extensions since 138) |
| **Summarizer** | Condenses long text into key points, a headline, a teaser | Stable since 138 |
| **Translator** | Translates on the device | Stable since 138 |
| **Language Detector** | Detects the language of a text | Stable since 138 |
| **Writer and Rewriter** | Drafts and revises text to a brief | Developer trial |
| **Proofreader** | Interactive corrections | Developer trial |

The Prompt API is the one that matters for what follows. In practice:

- **Input:** text, plus images (an image file, a canvas, a video's current frame, and so on) and audio (a recording, a buffer). Audio input needs a GPU.
- **Output:** text only, streamed or whole, and it can be constrained by a JSON schema, so the model returns, for example, a boolean, a label from a list, or an object with fields you defined.
- **Sessions:** a system prompt that is never dropped, initial prompts to restore a conversation, appending context before asking, cloning a session to fork it, and a running count of context used against the window. When the window fills, the oldest turns are dropped, and the page is told.
- **Languages:** English, Japanese, Spanish, German and French, declared when the session is created.
- **Sampling:** on the web, temperature and similar knobs are not exposed by default; an origin trial offers named modes from most predictable to most creative.

What it needs is the part that decides who can use it. Windows 10 or 11, macOS 13 or later, Linux, or ChromeOS on Chromebook Plus devices; no Android or iOS yet. At least 22 GB free on the disk with the Chrome profile. Either a GPU with strictly more than 4 GB of video memory, or 16 GB of RAM and four CPU cores. An unmetered connection for the first download. Chrome measures the GPU with a test shader and picks the model variant to match: a larger one, a smaller one, or CPU inference.

## Why the download felt so bad

My experience, in order. I opened one of Chrome's demo pages, typed a message, and the download started. There was a small banner that told me something was happening, but not how much, how fast, or how long. I tried another playground, with the same result. I refreshed the page and the banner was gone, so I assumed the download was gone too. I left the laptop open overnight, and by the morning the model was there. The only sign of life in between was network traffic in the system monitor, on a fast connection that should have done better.

What I saw, against what was actually happening, and what a page should show. The download never stopped; the page that asked about it did. Chrome's guidance covers most of this, and the demos did not follow it.

Most of that is explained in Chrome's own documentation, and it is worth knowing before building anything:

- **The download did not stop.** It continues in the background if the tab that started it is refreshed or closed, resumes where it left off if the connection drops, and resumes on the next start if the browser is closed (within 30 days).
- **The progress bar is the page's job.** A page sees download progress only through the monitor it passes when it creates a session. After a refresh, the new page has to ask again, and if it does, it is told how much is still missing. The demo pages did not ask again; that is why the banner vanished.
- **It is roughly 4 GB, downloaded once per device.** Every site shares the same model. Updates are full downloads, done in the background and swapped in without downtime.
- **There is a pause after the download.** Once the bytes are in, the model is unpacked and loaded into memory, which the documentation recommends showing as an indeterminate state.
- **It can disappear.** If free disk space falls below about 10 GB, Chrome deletes the model, even mid-session, and does not fetch it again until a page asks.
- **There is a page for this.** `chrome://on-device-internals` shows the model, its version and an event log.

So the rough experience was real, and it is fixable at the page level. Chrome's guidance even describes a hybrid pattern, used by the shopping site Miravia: answer with a server-side model while the local one downloads, then switch. What I have not found, anywhere I looked, is a small, honest component that shows bytes, rate and time remaining, survives a refresh, says it is safe to close the tab, and, because the API reports only that a device is unavailable and not why, lists the likely reasons in plain words. That is the first thing worth shipping.

## Why there are so few examples

I looked for good examples of the Prompt API in action, and found surprisingly few. Chrome's own case studies are real but narrow: CyberAgent's blogging tools, review summaries on redBus and Miravia, article summaries at Terra and BrightSites, and translation at Policybazaar and JioHotstar. Most of those use the task APIs, summarising and translating, rather than the Prompt API itself. Chrome uses Gemini Nano for its own scam detection. Beyond that, there are demos, extensions, and wrappers that expose the browser's model to other programs. That surprised me, until I listed the reasons:

- **It is new.** Five months on the open web is not long for a platform feature.
- **The audience is gated.** Desktop only, with a 22 GB free-disk floor and real hardware requirements. A team cannot assume its readers have it, so every feature needs a fallback, and the fallback often becomes the feature.
- **The first run is a 4 GB download.** No product manager wants that to be a user's first impression.
- **It is small.** A model in the 2 to 4 billion parameter range is good at classifying, extracting, summarising and rephrasing, and not at long reasoning. Teams that try it as a chatbot are disappointed; teams that try it as a function are not.
- **Five languages.** A lot of the web is in the others.
- **Tool calling is not ready.** Native tool use is behind a flag and unreliable; the documented path is structured output.
- **The standards fight.** That is the next section, and it is the reason I would take most seriously if I were deciding whether to build on it.

## The case against, taken seriously

Chrome shipped the Prompt API over formal opposition. Mozilla's position is that the API has "severe negative consequences to the interoperability, updatability, and neutrality of the web platform." Apple's WebKit team filed an opposing position on interoperability, portability and privacy. The W3C Technical Architecture Group recorded several concerns, and Microsoft, which builds its own version of the API on its own models in Edge, objected too. The objections come down to three things.

- **Prompts do not travel.** A prompt tuned for Gemini Nano may behave differently on another browser's model, and the proposal itself says it does not guarantee quality, stability or interoperability between browsers. That pushes the web towards writing for one model, the way it once wrote for one browser.
- **A vendor policy sits in front of a web API.** Using it means accepting Google's Generative AI Prohibited Uses Policy, which is new for a web platform feature.
- **The browser decides.** Which model, which version, when it updates, when it is deleted. A page cannot pin a version, and cannot even read it from JavaScript.

I agree with most of this, and it lines up with what I keep writing about: sovereignty, determinism and explainability. A model I cannot pin, version or inspect, behind a policy I did not write, is not sovereign infrastructure. But I do not think the answer is to wait. Edge already offers the same API shape on its own models (Phi-4-mini, and a smaller one called Aion in developer preview), so the interface is not Chrome's alone, even if the standards process is unfinished. And there is a design discipline that limits the damage:

- **Keep the meaning in the data, not in the prompt.** If the page hands the model a slice of an anchored graph and asks a narrow question with a JSON schema, the work the model does is small and checkable, and the answer can be verified against the anchors. Swap the model and the graph still works.
- **Use the model as a function, not as an oracle.** Classify, extract, label, rephrase. Never let it be the only source of a fact.
- **Always have a path without it.** The graph itself, or the reader's own key to a larger model, or nothing at all. The page should be complete without the model, and better with it.

## Why this fits what we have built

This is the part I find most exciting. A small model with a small context window is a bad match for raw prose and a very good match for the graphs this site is building.

In [The agent is the reader](the-agent-is-the-reader.md), the five readers' graph answered a question about any of 45 concepts in a median of 2,579 tokens, with every statement anchored to its sentence, against 25,698 tokens to read the five articles. A context window measured in thousands of tokens, not hundreds of thousands, cannot hold the five articles. It can hold the graph's answer, with room left for the question. The same work that makes the graph worth paying for, for an agent with a big model, makes it usable for a small model in the reader's tab. And the anchors mean every answer can show its sources, which is the honest way to use a model this size.

The model also fills the gaps the client-side pattern still had. The newsroom builds [personas](pay-to-keep-your-persona.md) from what the reader reads, using rules; a local model can infer them from the text itself, without anything leaving the browser. My whole publishing workflow starts with voice memos; the Prompt API accepts audio, so a memo could be transcribed and structured on the device before it is encrypted into a vault lane. And the [synthetic readers](how-to-run-synthetic-users.md) found 51 missing figures out of 527; a local model can describe what each figure shows, and say when a figure says something different from its caption.

## Where we can use it

Where a model in the tab fits, by how much it would be worth to readers and how ready the platform is for it today. The top right is where to start; the left column waits on tool calling, more languages or mobile.

| Opportunity | What the model does | Built on | Ready today? |
|---|---|---|---|
| **Ask this article** | Answers a reader's question from the graph slice, citing anchors | Prompt API, JSON schema, the five readers' graph | Yes |
| **Personas inferred locally** | Labels what a reader reads into persona traits, in the browser | Prompt API, JSON schema, SG Meter's history | Yes |
| **A download panel that tells the truth** | Not the model: a component that shows bytes, rate and time, survives a refresh, and explains "unavailable" | `availability()`, the download monitor | Yes |
| **Voice memo to vault** | Transcribes and structures a memo on the device, then encrypts it to a lane | Prompt API audio input (GPU), append lanes | Yes, on GPU machines |
| **Alt text and figure checks** | Describes each figure; flags a figure that contradicts its caption | Prompt API image input | Yes |
| **Read it in Portuguese** | Translates an article for pt.newsroom readers on the device | Translator API | Yes |
| **A behaviour-policy helper for RiskMandate** | Classifies each rule a user writes as boundary, setting, expectation or none, privately | Prompt API, JSON schema | Yes, as a draft for a person to check |
| **A local second reader** | Checks a draft against rules and sources before it is sent | Prompt API, JSON schema | Partly: too small to be the only check |
| **Tools for the reader's agent** | The newsroom describes its own actions to the reader's agent | WebMCP | Origin trial |
| **Native tool calling** | The model decides which of our functions to call | Prompt API tools | Not yet: behind a flag |

The first four are the ones I want to build, in roughly that order. They share one property: the model never decides anything important on its own. It answers from anchors, labels into a fixed set, or transcribes, and the page or the person checks the result.

## What we are building next

A vault is being built alongside this article to explore all of this properly: a test page per capability, measured on real machines, with the numbers published. The first round:

1. **The model status panel.** An open component, in the spirit of SG Meter: it checks support and eligibility, shows download progress with bytes, rate and time remaining, survives a refresh, and, when a device cannot run the model, explains the likely reasons in plain words.
2. **Ask this article, grounded in the graph.** A question box on articles that have the five readers' graph, answering only from anchored items, with a JSON schema that forces it to cite them, and a fallback that shows the graph slice when the model is missing.
3. **Personas, inferred on the device.** The same traits SG Meter uses, inferred from the text a reader keeps, never sent anywhere.
4. **Voice memo to vault.** Record, transcribe and structure on the device, then encrypt and drop it into an append lane.
5. **Measurements.** Download time, time to first token, tokens per second, context window, and accuracy against the anchors, on the machines we have. These are the numbers missing from almost every piece about Gemini Nano, including this one.

The client-side pattern had one piece left that seemed to need someone else's server. On capable desktops, it no longer does. The model is small, the platform is contested, and the first-run experience is poor. All three are true, and none of them is a reason to wait. If you are building with the Prompt API, or have found good examples I missed, let's talk: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded after trying Gemini Nano in Chrome for the first time, with my first impressions of the download and the demos. I asked an agent in a separate Claude session to research the current state of the Prompt API and the built-in AI APIs, check my impressions against Chrome's own documentation, and draft this article with its figures; where my impressions and the documentation disagreed (the download stopping on refresh, native tool support), the article follows the documentation and says so. This site's agent then gave it a last pass: plainer wording, and a correction to the claim that renting was the only way to put a model behind a page. The argument is mine, and so is the editorial responsibility.

The status of each API, the hardware requirements, the Prompt API's inputs, outputs and sessions, and the model's download, update and deletion behaviour are from Chrome for Developers: [Built-in AI APIs](https://developer.chrome.com/docs/ai/built-in-apis), [The Prompt API](https://developer.chrome.com/docs/ai/prompt-api), [Understand built-in model management](https://developer.chrome.com/docs/ai/understand-built-in-model-management) and [Inform users of model download](https://developer.chrome.com/docs/ai/inform-users-of-model-download), with [WebMCP and agents](https://developer.chrome.com/docs/ai/agents) and the [demos](https://chrome.dev/web-ai-demos/). The ship date and the objections are from coverage in [Tech Times](https://www.techtimes.com/articles/316729/20260516/google-ships-chrome-prompt-api-over-objections-mozilla-apple-w3c-microsoft.htm) and [Gigazine](https://www.gigazine.net/gsc_news/en/20260501-google-chrome-prompt-api/), which cite Mozilla's standards position (issue 1213) and WebKit's (issue 495); the model size of about 4.27 GB is from the same coverage. The state of native tool calling, tested on Chrome 151 in August 2026, is from the [flutter_gemma_builtin_ai](https://pub.dev/packages/flutter_gemma_builtin_ai/versions/0.2.0) documentation. Edge's Prompt API and its models are from [Microsoft's announcement](https://blogs.windows.com/msedgedev/2025/05/19/introducing-the-prompt-and-writing-assistance-apis/) and [coverage of Build 2026](https://www.thurrott.com/?p=336953). The graph numbers are from [The agent is the reader](the-agent-is-the-reader.md); the figure count is from [How to run synthetic users](how-to-run-synthetic-users.md). No measurements of speed or quality are claimed here; those are what the vault is for.

## Threads

Site & engineeringGraphs & knowledge[This article as a graph →](graphs.md#a-model-in-the-tab)

### Builds on

- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.

### Continued by

- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 73 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=73)

**Posting this article on LinkedIn?** The cover is [a-model-in-the-tab.jpg](banners/a-model-in-the-tab.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-model-in-the-tab.html)*
