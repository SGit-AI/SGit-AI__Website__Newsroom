# GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed, sgit.ai

> On 28 June 2024, at OWASP Global AppSec EU in Lisbon, I gave Deterministic GenAI Outputs with Provenance, 132 slides and a live demo of The Cyber Boardroom, the project I had been building for two months: an assistant that explains cyber security to board members, in their language and at their level. The talk opened with a quiz, what is the sixth most powerful programming language in the world, and the answer was Portuguese, because prompts are written in natural languages and 236 million people speak it first. Its core was a set of principles: GenAI matters because it can understand content, not because it creates it; hallucinations are a feature for creativity and a bug for facts; use read-only models, bring your own content, assume every prompt is exposed, and use graphs instead of RAG. And it ended with a challenge to Portugal: the future depends on getting this right, otherwise Portugal becomes just another consumer of global technology. Two years later most of it holds, and some of it is the foundation of what I do now: provenance, graphs and determinism are the core of this newsroom; the board assistant became agents with a mandate; and Portugal has released Amália, an open model for European Portuguese, which is what I asked for. What changed is the word: in 2024 I talked about models and prompts; in 2026 it is agents, and the problem is controlling what they do.

*Source: <https://newsroom.sgit.ai/articles/portugal-2024-genai-in-portuguese.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed

# GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.1.0, 2 versions](versions/portugal-2024-genai-in-portuguese.md) · [newsroom v0.12.78](https://newsroom.sgit.ai/admin/versions.html) · portugalowaspgenaicyber-boardroomtalksprovenancegraphsagentslanguagehistoryarticle

***Abstract:** On 28 June 2024, at OWASP Global AppSec EU in Lisbon, I gave Deterministic GenAI Outputs with Provenance, 132 slides and a live demo of The Cyber Boardroom, the project I had been building for two months: an assistant that explains cyber security to board members, in their language and at their level. The talk opened with a quiz, what is the sixth most powerful programming language in the world, and the answer was Portuguese, because prompts are written in natural languages and 236 million people speak it first. Its core was a set of principles: GenAI matters because it can understand content, not because it creates it; hallucinations are a feature for creativity and a bug for facts; use read-only models, bring your own content, assume every prompt is exposed, and use graphs instead of RAG. And it ended with a challenge to Portugal: the future depends on getting this right, otherwise Portugal becomes just another consumer of global technology. Two years later most of it holds, and some of it is the foundation of what I do now: provenance, graphs and determinism are the core of this newsroom; the board assistant became agents with a mandate; and Portugal has released Amália, an open model for European Portuguese, which is what I asked for. What changed is the word: in 2024 I talked about models and prompts; in 2026 it is agents, and the problem is controlling what they do.*

Twelve slides from Deterministic GenAI Outputs with Provenance, OWASP Global AppSec EU, Lisbon, June 2024.

## In short

- **June 2024, Lisbon.** OWASP Global AppSec EU; 132 slides; a live demo.
- **Portuguese is a programming language.** The sixth most powerful, by speakers.
- **GenAI understands.** That matters more than that it creates.
- **Principles.** Read-only models, your own content, prompts exposed, graphs not RAG.
- **The Cyber Boardroom.** Explaining security to a board, in its own language.
- **A challenge to Portugal.** Lead, or be another consumer of technology.
- **Two years later.** Provenance and graphs hold; models became agents.

## The talk

On Friday 28 June 2024, in the last session before the closing of [OWASP Global AppSec EU](https://diniscruz.ai/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.html) at the Lisbon Congress Centre, I gave *Deterministic GenAI Outputs with Provenance*. The page on my site has the [slides](https://files.diniscruz.ai/s3/pdf/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.pdf), the [video](https://www.youtube.com/watch?v=IEN9Ittv4V0) and a full transcript. I said at the start: "my focus (and this presentation) is on GenAI". The title was the whole argument: deterministic, GenAI, output, with provenance, "Traceability, Source Tracking & Documentation, Lineage, Origin Verification".

## Portuguese is a programming language

It began with a quiz for the room: what is the sixth most powerful programming language in the world? "Since data is now code, and GenAI prompts are written in natural languages", the answer was Portuguese: "Portuguese, as English and every other language in the world (dead or alive) can be used to give instructions to LLMs", to "define actions, workflows and create applications". With 236 million first-language speakers, that is a lot of programmers. And I asked for models in our language: "we need Portuguese from Portugal, Portuguese from Angola, Portuguese from Mozambique, Portuguese from Cape Verde".

**Two years later.** It happened, at least for Portugal: [Amália](https://thenextweb.com/news/portugal-open-source-ai-model-amalia), an open model for European Portuguese, built on the European EuroLLM and released as open source in 2026, with a [technical report](https://arxiv.org/abs/2603.26511) and a benchmark for pt-PT. The other varieties are still waiting. And the idea that language is the programming language is now ordinary: it is what [explorer coding](explorer-coding.md) is.

## Understanding, not creating

The slides I would keep in any version: GenAI is the next technological revolution "Not because it can CREATE content, But because it can UNDERSTAND content"; hallucinations "Are a FEATURE when creating content and when we want creativity, But are a BUG and PROBLEM when we want facts, evident and trust". Is it secure? No. Is it safe? Maybe, depending on implementation. From an attacker's point of view, GenAI is "Your most vulnerable API", "Your most dangerous Insider Threat" and "A crazy 'Black Box'".

Then the principles: "Read-only models", "It's about the Prompts", "Bring your content", "Assume all content and prompts are exposed", "Double down on AppSec and Cyber". And one slide I am proud of now: *Use Graphs instead of RAG*. In the talk I said: "I think the stuff with graphs is a lot more interesting. I think you take the content, you summarize, you build graphs of it, then you navigate the graph."

**Two years later.** This is the part that held best, because it became the work. Provenance is the rule of this newsroom: every claim checked against a source and linked. Graphs became [fractal semantic graphs](introducing-fractal-semantic-graphs.md), and every article here has one. Determinism became the principle that the further a thing moves towards commodity, the fewer agents in line. What changed is the threat: in 2024 the insider was a model answering questions; in 2026 it is an agent with tools, and the answer is [a behaviour policy](the-mandate-stack.md) and authority outside the model.

## The Cyber Boardroom

The middle of the talk was a live demo of The Cyber Boardroom, which I had spent the previous two months building, open source, with every release on PyPI, Docker Hub and AWS. The problem it solved was not specific to security: "how do you communicate with stakeholders using their language, culture, knowledge, state, interests, and level of ownership?" I showed it answering a board member's question in several languages, three board-member personas asking the same question, a fourth model reviewing the other three, and Athena, the cyber security advisor, with the prompt that created her on the screen. And: "Security incidents are a good thing", if you use small ones as training.

**Two years later.** The idea, personalised briefings for people who own the risk, is still at the centre of what I do. The shape changed: one assistant answering questions became teams of agents doing work, each with a role, a mandate and a record, which is what [the agentics talk](agentics-ready-to-sell.md) showed last week.

## The challenge to Portugal

The talk ended where my Portugal talks always end. To the Portuguese in the room: "the future of Portugal kind of depends on you. I think it can really make a massive difference, but we need to get it right. Otherwise, Portugal just becomes another consumer of global technology, which is not where it should be, because now we actually have the ability to make a difference."

**What holds.** All of it. It is the same challenge as [2010](portugal-2010-a-challenge.md) and [2016](portugal-2016-hacking-portugal.md), with a better lever: in 2010 the lever was security, in 2016 code, and in 2024 language. Amália suggests Portugal heard some of it. The essays I wrote the next year took it to [the scale of Europe](portugal-and-europe-2025.md).

## What this does not claim

- **Not the first time I mentioned The Cyber Boardroom.** It was its first live demo in Portugal that I can document.
- **Not that the talk led to Amália.** Many people asked for a Portuguese model.
- **The commentary is mine, now.** The slides and transcript are from 2024.

If you were in the room in Lisbon, or want to talk about agents for boards, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the commentary and the editorial responsibility are mine. [The talk's page](https://diniscruz.ai/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.html) on diniscruz.ai, with the [slides](https://files.diniscruz.ai/s3/pdf/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.pdf), the [video](https://www.youtube.com/watch?v=IEN9Ittv4V0) and the transcript, from which every quote is taken. For today: Amália, via [The Next Web](https://thenextweb.com/news/portugal-open-source-ai-model-amalia) and its [technical report](https://arxiv.org/abs/2603.26511). Read on 16 October 2026.

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#portugal-2024-genai-in-portuguese)

### Builds on

- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement path, and a marketplace for the consultants who deliver it](agentics-ready-to-sell.md) After the London talk, agentics is ready to sell: the market and its prices, our evidence-first position, the engagement path, and a consultants marketplace.
- [A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands](portugal-2010-a-challenge.md) My 2010 IBWAS keynote in Lisbon, slide by slide: twelve actions for Portugal, more of which came true than I expected, mostly from Brussels.
- [Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs](portugal-2016-hacking-portugal.md) Hacking Portugal, my 2016 BSidesLisbon keynote and the book at 95%: a Hacking Service, OpenSource.pt, a Ministry of Code, and what holds ten years on.
- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.

### Continued by

- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.
- [Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs](portugal-2016-hacking-portugal.md) Hacking Portugal, my 2016 BSidesLisbon keynote and the book at 95%: a Hacking Service, OpenSource.pt, a Ministry of Code, and what holds ten years on.
- [A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands](portugal-2010-a-challenge.md) My 2010 IBWAS keynote in Lisbon, slide by slide: twelve actions for Portugal, more of which came true than I expected, mostly from Brussels.
- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 151 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=151)

**Posting this article on LinkedIn?** The cover is [portugal-2024-genai-in-portuguese.jpg](banners/portugal-2024-genai-in-portuguese.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/portugal-2024-genai-in-portuguese.html)*
