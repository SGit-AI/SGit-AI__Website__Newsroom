# Every mistake added a rule: complexity, agents, and the way back to shipping, sgit.ai

> A friend who uses agents better than most, one writing, others verifying, ChatGPT reviewing, every claim resting on an output read in full, sent me two messages about a verification that keeps breaking. The code is holding up. The process around it is not: long sessions compact and skip steps, outputs of failing commands are lost, prompts have grown to 100 KB, scripts are edited in place, the harness suggests what the rules forbid, and every mistake added a rule that caused new mistakes. This is complexity, and it is what hits the founders who are doing the right thing, clever, careful, now working as engineers without the scar tissue of engineering. This article maps their process as a Wardley map, where complexity is a position, custom-built process sitting where commodities already exist, and maps it again with each piece made small, shipped and moved right. Then it sets out the principles I work by: map it, commoditise small chunks and let them compound, ship, keep sessions small and the context yours, memory as versioned files, slow down when complexity hits, security by asset and attack vector, rules for incidents and machines for enforcement, run it in five environments, reverse-engineer the path to the destination, and learn the engineering that already exists. It ends with direct answers to their questions on compaction, audit cards and what deserves a STOP.

*Source: <https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Every mistake added a rule: complexity, agents, and the way back to shipping

# Every mistake added a rule: complexity, agents, and the way back to shipping

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-08 · [article v1.1.0, 2 versions](versions/every-mistake-added-a-rule.md) · [sgit.ai v0.7.1](https://sgit.ai/admin/versions.md) · agentscomplexitywardley-mapsengineering-practicecontext-windowcompactionmemoryshippingfoundersnfrstestingcoworkchatgptarticle

***Abstract:** A friend who uses agents better than most, one writing, others verifying, ChatGPT reviewing, every claim resting on an output read in full, sent me two messages about a verification that keeps breaking. The code is holding up. The process around it is not: long sessions compact and skip steps, outputs of failing commands are lost, prompts have grown to 100 KB, scripts are edited in place, the harness suggests what the rules forbid, and every mistake added a rule that caused new mistakes. This is complexity, and it is what hits the founders who are doing the right thing, clever, careful, now working as engineers without the scar tissue of engineering. This article maps their process as a Wardley map, where complexity is a position, custom-built process sitting where commodities already exist, and maps it again with each piece made small, shipped and moved right. Then it sets out the principles I work by: map it, commoditise small chunks and let them compound, ship, keep sessions small and the context yours, memory as versioned files, slow down when complexity hits, security by asset and attack vector, rules for incidents and machines for enforcement, run it in five environments, reverse-engineer the path to the destination, and learn the engineering that already exists. It ends with direct answers to their questions on compaction, audit cards and what deserves a STOP.*

**Five readerstwo minutes · the arc · 9 slides · a map · 137 catalogued items, 6 flagged**

This article read again, after it was written, by five of the desk's readers: the Explainer, the Historian, the Storyteller, the Cartographer and the Librarian. None adds a claim the article does not make. Read from article v1.0.0 on 10 October 2026; the views are not part of the article's text and do not change its version. [How the five readers work](one-article-five-readers.md).

**In two minutes (Explainer): When an AI assistant keeps making mistakes, more rules make it worse**

**The point.** A friend checked a software tool using several agents (AI programs that do tasks by themselves), one writing and others checking. The tool held up: 812 attacks produced no failures. The process around it kept breaking: "Every mistake added a rule, and every new rule caused new mistakes." The answer is to stop adding rules and build small, tested pieces that make each mistake impossible, using plain files and version history.

**An example.** When a command failed, the software running the agents did not save its output and cut out the middle, so a whole test run was lost. The fix is not a rule saying "save the output". It is one small script that every command goes through, which writes the output to a file before anything reads it.

**Why it matters to you.** Asked whether all this rigour was overdoing it, the author says: for the process, yes; for the intent, no. If you are not getting faster, complexity is winning, and the answer is to slow down and break the work into small pieces.

**If you remember one thing.** When a rule fails, replace it with something that makes the mistake impossible, then delete the rule.

**Words used.**

- **Compaction:** a long AI conversation replaced by a short summary, losing detail.
- **Wardley map:** a chart of a system's parts, showing which are custom-made and which are standard products.

**In the arc (Historian): What it added, and where it sits**

**Introduced.**

- Complexity as a position on a Wardley map: custom-built process sitting where commodities already exist (`complexity`).
- The rule loop: each mistake adds a rule, the prompt grows, the session compacts sooner, and compaction decides which rules survive (`rule-growth`, `compaction`, `forgetting`).
- The harness as a party that can work against the rules (`harness`).
- The audit card: a script over the transcript, run after the step, read by something that was not part of the work (`record-reading`).

**The nugget.** "When a rule fails, the question is not how to word it more strongly but which of the stronger barriers can replace it." It turns the previous article's count into a method, and it is the question articles 4 and 5 answer for one rule each.

**Reused.** `agent-behaviour-policy`, the barrier kinds and `accepted-risk` from the-behaviour-policy-is-the-business-logic, though this article does not link it. From before the set: the policy text graded weak in the-agent-team-as-it-runs; footprint and blast radius from footprint-and-blast-radius (the basis of the audit card); memory as files from memory-is-not-a-spectator-sport; risk acceptance from every-risk-is-already-accepted; the bridge vault's gate of 44 checks and green-does-not-mean-live as examples of `gate`. The Cartographer counts `second-reader`, `gate`, `agent-team`, `blast-radius` and `memory-as-files` as new; within the set they are, but four of them have earlier homes on the site.

**Changed.** It moves the argument from a business's policy to an engineer's process, and narrows what a rule is for: "Rules only for incidents, and each rule replaced by structure as soon as one can be built." Article 1 counted rules; this one says to delete them.

**Left open.**

- The friend "asked two questions", but only the second is stated; the answers section answers four (Librarian flag).
- Map one's six blob components are not the six listed patterns (Librarian flag).
- "Closing a session that compacts is a good rule, because it is a boundary, not a request." Under the ABP test a close the agent performs on itself is not enforced above its grant; the article does not say what enforces it.

**Contribution.** 11 new / 19 total. A high share for the second article, because it brings in the session's own failure modes (compaction, harness, rule growth) that the business-layer article never touched.

**In pictures (Storyteller): 9 slides**

1 / 92 / 93 / 94 / 95 / 96 / 97 / 98 / 99 / 9

Swipe or scroll sideways. [Download the deck as a PDF](views/every-mistake-added-a-rule/every-mistake-added-a-rule.pdf) (one page per slide, ready for a LinkedIn document post).

**On the map (Cartographer): The argument as a map: why a rule for every mistake makes the process worse, and what replaces the rule.**

The argument as a map: why a rule for every mistake makes the process worse, and what replaces the rule.

**The catalogue (Librarian): 137 items, each anchored to a sentence of the article**

Everything the article contains, by kind. Every item was extracted with the exact sentence it came from, and a script checked each one against the article.

**Claims: 39**

- Adding a rule grows the prompt, brings compaction sooner, and compaction decides which rules survive; shipping a component makes the mistake impossible so the rule can go (lead)
- The code is fine; the process is the problem (In short)
- In a Wardley map, complexity shows up as custom-built components where the world already has products and commodities; each fixing rule adds another (In short)
- Shipping is how complexity stays under control: small shipped components compound, large unshipped ones accumulate (In short)
- The urge to push through is the most expensive one; if you are not getting faster, complexity is winning (In short)
- The friend is doing what the author recommends: not trusting one model's account of its own work, and building the checks in (Two messages from somebody doing the right thing)
- The friend's changes are right; the article adds why, so the next problem gets the same answer without a new rule (Two messages from somebody doing the right thing)
- A healthy map has a thin custom layer where the value is, resting on products or commodities (Complexity is a position on a map)
- Wardley maps keep the author's world sane: they predict roughly what will happen and explain why something happened (Complexity is a position on a map)
- Failures are usually a mismatch on the evolution axis: commodity assumed when still custom, or custom rebuilt when already a commodity (Complexity is a position on a map)
- The problem is the blob between the agents and the commodities: recovery, output capture, proof of bytes, kilobytes of rules, long sessions, an all-firing STOP, each built by hand every session (Complexity is a position on a map)
- The way out is not a better rule: make each piece of the blob a small component with one job, test it once, ship it, let it move right (Move the pieces right)
- Rules from incidents, enforced by machines, stay few; rules from worry, enforced by attention, multiply (Move the pieces right)
- Custom components the world treats as commodity, and assumed-commodity components still custom, are where the next failure comes from (The principles I work by)
- Know your users and focus on user needs start with the person preparing the install, not with the process (The principles I work by)
- Each self-contained component keeps its blast radius under control because it was shipped as a unit of its own (The principles I work by)
- The friend is doing too much at once, so nothing gets to become boring (The principles I work by)
- Shipping is probably the single most important thing; without it you over-engineer, which LLMs make very easy (The principles I work by)
- If you are not releasing something, you are probably not solving problems at the right altitude (The principles I work by)
- Making it public removes complexity: you cannot hide an over-engineered thing in public (The principles I work by)
- With large contexts you lose control; when Claude or ChatGPT compacts you do not control what it keeps (The principles I work by)
- If a session needs 100 KB of rules to be productive, the rules are doing the job structure should do (The principles I work by)
- Every document an agent writes is a compression of what was learned, in a form the next agent can read; it is a graph (The principles I work by)
- If compaction is hurting you, you are giving the model far too much context (The principles I work by)
- Compromising now to go faster usually slows you down (The principles I work by)
- Secure and safe are not the same; sometimes ship something not fully hardened if its attack surface is controlled (The principles I work by)
- Most companies ship software far less secure than users assume; the difference is whether they know their compromises (The principles I work by)
- On an isolated machine with no network and nothing of value, many attacks are not available and requirements drop (The principles I work by)
- A rule is a weak barrier; a record detects; a boundary prevents (The principles I work by)
- Running in many environments shows where the bottlenecks are, most useful when complexity starts to hit (The principles I work by)
- If you have a choice and do not use what you built, it is not good enough yet; the author would build a solution not using the vaults (The principles I work by)
- Closing a session that compacts is a good rule, because it is a boundary, not a request (Answers to the questions)
- The agent does not police itself on every command; the record is read afterwards by something not part of the work (Answers to the questions)
- If everything is a STOP, a STOP stops meaning anything (Answers to the questions)
- For the process, yes; for the intent, no; rigour should match the assets and blast radius (Answers to the questions)
- The process has become a second product nobody asked for, costing more than the verification it serves (Answers to the questions)
- The lesson applies to companies too, including the author's own (The same lesson, one level up)
- If it cannot work in the simple use cases, it will struggle in the complex ones (The same lesson, one level up)
- Funding can give a false sense of having a product, or of it being ready to scale (The same lesson, one level up)

**Evidence: 8**

- Pattern 1, compaction: long sessions compact and the agent then skips mandatory steps or writes its report from the summary; this caused most failures (Two messages from somebody doing the right thing)
- Pattern 2, lost outputs: on non-zero exit the harness does not save the output and truncates the middle (Two messages from somebody doing the right thing)
- Pattern 3, 100 KB prompts: asked for an exact copy of its prompt for recovery, the agent reproduced it from memory, incomplete or wrong (Two messages from somebody doing the right thing)
- Pattern 4, scripts edited in place: afterwards there is no way to prove which bytes ran (Two messages from somebody doing the right thing)
- Pattern 5, the harness against the rules: the harness suggests cat, sed and heredocs, which their rules forbid (Two messages from somebody doing the right thing)
- Pattern 6, too many rules, quoted from the friend: every mistake added a rule, and every new rule caused new mistakes (Two messages from somebody doing the right thing)
- nfrs.sgit.ai, reading down its failure column: what a machine enforces, holds; what attention enforces, drifts (Move the pieces right)
- In the agent team's own grading, the policy text is graded weak (The principles I work by)

**Data points: 8**

- 812 concurrency attacks, 0 failures (Two messages from somebody doing the right thing)
- Prompts of 100 KB (Two messages from somebody doing the right thing)
- 9 small sessions planned in place of 2 large ones (Two messages from somebody doing the right thing)
- coding.sgit.ai: 31 documented rules, and 4 structural guards as the working automated enforcement, each encoding an incident (Move the pieces right)
- 40 doctrines listed on wardley-maps.sgit.ai (The principles I work by)
- Bridge simulation: a 126-file vault with an app, an API description, economics and 4 themes (The principles I work by)
- Agent team: one step per agent of up to 12 minutes (The principles I work by)
- Bridge vault's gate runs 44 checks, many existing because something broke once (The principles I work by)

**Facts: 5**

- The verification rules: no network, everything sandboxed, every claim resting on an output read in full, any deviation is a STOP (Two messages from somebody doing the right thing)
- The results on the tool are good; the tests reproduce (Two messages from somebody doing the right thing)
- Files, hashes and version control have solved most of those problems for decades (Complexity is a position on a map)
- As nfrs.sgit.ai puts it, every guard encodes a rule that was violated at least once (Move the pieces right)
- Drafted by agent@riskmandate.ai (Claude Opus 5.5) in the sgit.ai site session on 8 October 2026; Dinis Cruz holds editorial responsibility (colophon (after Where to start))

**Hypotheses: 2**

- The author sees very few hallucinations and thinks it is because briefs and sessions are tight, many and isolated (The principles I work by)
- A mapped path from agent behaviour policies to a licence to operate to insurance, which the author thinks is strong (The same lesson, one level up)

**Open questions: 5**

- The friend's question: does this level of rigour make sense, or am I overdoing it? (Two messages from somebody doing the right thing)
- Do you let sessions compact, or design every step to finish before? (Answers to the questions)
- How does the post-session audit card work? (Answers to the questions)
- When an agent makes a mistake of form, do you log it and continue? (Answers to the questions)
- Is this level of rigour overdoing it? (Answers to the questions)

**Definitions: 8**

- Wardley map: places each component by visibility to the user (top to bottom) and evolution (left to right: genesis, custom-built, product, commodity) (Complexity is a position on a map)
- Complexity (on a map): not the number of components but custom-built components sitting where commodities already exist, each maintained by attention (Complexity is a position on a map)
- FIRE doctrine: fast, inexpensive, restrained, elegant (The principles I work by)
- To ship: to make something usable by somebody else, an agent included (The principles I work by)
- Context window: what the model receives when it makes a call (The principles I work by)
- Iterative Flow Development: the estate's methodology, naming developer attention as the scarce resource (The principles I work by)
- Audit card: a script over the transcript, run after the step, counting tools, tokens, files and network calls and flagging anything outside policy (Answers to the questions)
- In the agent team, a stop is a hold file only a person can release (Answers to the questions)

**Methods: 21**

- Replace steps skipped after compaction with steps short enough to finish before compaction, reading and writing state in files (Move the pieces right)
- Replace hand output capture with a run wrapper that writes stdout, stderr, exit code and timing to a file before anything reads it (Move the pieces right)
- Replace 100 KB recited prompts (model used as storage) with a short policy and a hashed reference folder on disk, read never recited (Move the pieces right)
- Replace provenance by trust with scripts committed and hashed before each run; the run record names the commit (Move the pieces right)
- Where rules fight the environment, change the environment or accept harmless defaults; a rule that fights the tool loses (Move the pieces right)
- Where policy is used as the control, keep rules only for incidents and replace each by structure as soon as one can be built (Move the pieces right)
- Principle 1: map your project and the complexity itself; get an LLM to teach mapping and draw a first version you argue with (The principles I work by)
- Principle 2: commoditise small chunks continuously so they compound; a healthy workflow gets faster the more of it there is (The principles I work by)
- End long threads by asking the agent for a document of what was learned and decided, and start a new session from it (The principles I work by)
- Test: a new session in Claude or ChatGPT should be productive from the first prompt, with focused, compressed reference material read by you (The principles I work by)
- Principle 6: when complexity hits, slow down, go back to a first draft, break into small components and define them (The principles I work by)
- Ask: what are the assets, the threat, the attack vector, and what customers buy; write a one-page threat model, publish it, ask the community (The principles I work by)
- When a rule fails, ask which stronger barrier can replace it, not how to word it more strongly (The principles I work by)
- Principle 9: run it in five environments, locally, air-gapped, Azure, GCP and AWS; each breaks a different assumption (The principles I work by)
- Principle 10: reverse-engineer the five, seven or ten paths that evolve into a large design (The principles I work by)
- Principle 11: learn the engineering that already exists, CI, Kanban, patterns, history of what worked (The principles I work by)
- Do not ask an agent to recite its prompt: point it at the file and record the file's hash in the run (Answers to the questions)
- Log mistakes of form and carry on; stop for harm, or for a boundary that broke (Answers to the questions)
- Where to start: draw the map, make the most expensive piece a small tool, cut the prompt to a page, outputs to file via wrapper, commit before run, split STOPs, publish a threat model, run elsewhere, delete rules (Where to start)
- Delete a rule every time a component makes it unnecessary (Where to start)
- Split the STOPs: harm stops, form is logged (Where to start)

**Decisions: 7**

- The friend is not named and their project not described, because the patterns are the point; Cowork and ChatGPT are named because they are the products in use (lead)
- The friend has decided: nine small sessions instead of two large, a hashed reference folder instead of a huge prompt, outputs to file read in full, scripts versioned and hashed before each run, and a compacting session closes immediately (Two messages from somebody doing the right thing)
- A lot of what the author publishes is half-baked by design; every release teaches something, and then he stops (The principles I work by)
- The author prefers version control (git or a vault) for memory, because it gives history and proves which prompt version a session read (The principles I work by)
- Testing rule of no mocks and no patches, affordable because cheap typed objects make the real thing easy; type system and testing philosophy are one decision (The principles I work by)
- The author designs steps to finish before compaction and keeps step state on disk (Answers to the questions)
- Way to market: break what they have into much simpler components to earn customers, because customers struggle with simpler things (The same lesson, one level up)

**Limitations: 3**

- Every map on the site is a claim, not a finding, with its source below the figure so it can be argued with (Complexity is a position on a map)
- The messages are paraphrased and their author is not named; only one line is quoted from them (colophon (after Where to start))
- Every placement in the two maps is a claim (colophon (after Where to start))

**Examples: 9**

- The session that drafted this article had its own context compacted earlier the same day and continued from a summary (lead)
- The friend's case: an independent verification of a tool before it is installed on a machine (Two messages from somebody doing the right thing)
- A whole race run was lost because a failing command's output was not saved (Two messages from somebody doing the right thing)
- Once, the recited prompt tripped the platform's safety filter (Two messages from somebody doing the right thing)
- The bridge simulation, published yesterday, was quick to build because almost nothing in it was new (The principles I work by)
- The newsroom experiments were stopped once they had answered their question, before the story vault work (The principles I work by)
- Green does not mean live: the story of one of the gate checks (The principles I work by)
- The forest picture: stages change the ground for the next; early species are gone when the big trees stand (The principles I work by)
- An accidental calendar call, which failed and sent nothing, was logged by the agent against its own policy rather than held (Answers to the questions)

**Sources: 8**

- Two messages from an unnamed friend about a verification run with agents in Cowork, with ChatGPT as reviewer (lead)
- A voice memo recorded by the author after reading the messages; the article is drafted from messages and memo (lead)
- nfrs.sgit.ai, the estate's account of non-functional requirements, testing, CI, documentation and resilience (The principles I work by)
- coding.sgit.ai, how the code is actually written, counted rather than claimed (The principles I work by)
- wardley-maps.sgit.ai, which lists forty doctrines (The principles I work by)
- Who reads the code, a brief on what quality engineering each stage of evolution needs (The principles I work by)
- Related site articles: risk acceptance and footprint and blast radius (The principles I work by)
- Memory is not a spectator sport (site article) (The principles I work by)

**Artefacts: 6**

- Figure cx-loops.webp: two ways to answer an agent mistake, add a rule or ship a component (lead)
- Map one (cx-map-now.webp): the verification as it runs, six failing things in a blob on the left, files, hashes and git unused at the far right (Complexity is a position on a map)
- Mermaid wardley-beta source for map one (Complexity is a position on a map)
- Map two (cx-map-next.webp): the same verification with each piece made small and moving right; tests and report judgment stay custom (Move the pieces right)
- Mermaid wardley-beta source for map two (Move the pieces right)
- Figure cx-compound.webp: how the components compounded on this site, from sgit and vaults up to story vaults and the bridge simulation (The principles I work by)

**Names: 8**

- Cowork, the product in which the friend's agents run (lead)
- ChatGPT, used as reviewer in the friend's verification (Two messages from somebody doing the right thing)
- Mermaid's wardley-beta diagram, used to render the two maps (colophon (after Where to start))
- Simon Wardley, originator of the doctrine names and Wardley Mapping (CC BY-SA 4.0) (colophon (after Where to start))
- Email-FS, through which agents talk to each other (The principles I work by)
- Issues-FS, where work is tracked (The principles I work by)
- Agent Behaviour Policies, one of the compounded layers on the site (The principles I work by)
- Dinis Cruz, author of the argument and person with editorial responsibility (colophon (after Where to start))

**Flagged for the author: 6**

- Count mismatch: the friend 'asked two questions' (anchor: "And they asked two questions, the second of which is the one I want to answer properly"), but 'Answers to the questions' answers four (compaction, audit card, mistakes of form, rigour). The first of the two is never stated.
- Quote count: the colophon says 'the one line quoted from them is theirs' (anchor: "the one line quoted from them is theirs"), yet the friend's question "does this level of rigour make sense, or am I overdoing it?" is also presented as their words (unquoted, introduced with a colon).
- Six versus six: map one's caption says 'The six things that keep failing sit in a blob on the left', but the six blob components (100 KB rules, recovery after compaction, long sessions, output capture, proof of bytes, STOP on every deviation) are not the six listed patterns: the map adds 'STOP on every deviation' and 'Long sessions' and omits 'The harness against the rules'. Likewise map two adds an audit card and harm-only stops that the replacement table does not list.
- Map two source: "Scripts committed and hashed before they run" has no incoming edge (only an edge to "Files, hashes, git"), so it is not connected to the agents or report, unlike the other moved components and unlike its map one counterpart "Proof of which bytes ran".
- Relative date: "The bridge simulation I published yesterday is a good test of this." depends on the publication date (2026-10-08); a reader of the catalogue cannot resolve 'yesterday' without it.
- Unsupported in-article: '40 doctrines' ("lists forty doctrines"), '31 documented rules ... four structural guards' and '44 of them' are cited from other sites/articles with no figure or quotation shown here; checkable only at the linked sources.

**The five readers have also read:**

- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md#views)
- [Hope or enforcement](hope-or-enforcement.md#views)
- [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md#views)
- [Re-anchoring](re-anchoring-agent-behaviour-policies.md#views)

Every view, the role files and the tools are in the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md).

Two ways to answer a mistake an agent makes. Add a rule, and the prompt grows, the session compacts sooner, and compaction decides which rules survive. Ship a component, and the mistake stops being possible, so the rule can go.

**Where this comes from.** A friend sent me two messages about a verification they are running with agents in Cowork, with ChatGPT as a reviewer. Both messages were written with their agents, which says a lot about how they work: the structure, the numbering and the attention to detail are what you get from somebody who has made agents check each other. I recorded a voice memo after reading them, and this article is drafted from the messages and the memo. My friend is not named and their project is not described; the patterns are the point, and they apply to many people I talk to. Cowork and ChatGPT are named because they are the products in use. The session that drafted this article had its own context compacted earlier the same day and carried on from a summary, which is one reason the advice below is written the way it is.

## In short

- **The code is fine. The process is the problem.** The tool under verification reproduces its tests, and 812 concurrency attacks produced no failures. What keeps breaking is the machinery around it: compaction, lost outputs, 100 KB prompts, scripts edited in place, rules that fight the harness, and rules that breed rules.
- **Complexity is a position on a map.** In a Wardley map, complexity shows up as a blob of custom-built components sitting where the world already has products and commodities. Every rule added to fix one of them is another custom component in the same place.
- **Move the pieces right, one at a time.** Each failure belongs to a component that can be made small, tested once and shipped: a short policy read from disk, steps that finish before compaction, a wrapper that writes every output, scripts committed before they run, an audit card read from the transcript, and a stop rule reserved for harm.
- **Shipping is how complexity stays under control.** A shipped component is a unit of its own: testable, battle-hardened, usable by somebody else, an agent included. Small shipped components compound. Large unshipped ones accumulate.
- **You have time.** The urge to push through is the most expensive one. If you are not getting faster, complexity is winning, and the answer is to slow down, map it, and break it into pieces.

## Two messages from somebody doing the right thing

My friend is running an independent verification of a tool before it is installed on a machine. The setup is impressive. One agent writes, other agents verify, ChatGPT reviews. The rules are strict: no network, everything sandboxed, every claim resting on an output read in full, and any deviation is a STOP. They are, in other words, doing what I keep telling people to do with agents: not trusting one model's account of its own work, and building the checks in.

The results on the tool are good. The tests reproduce. 812 concurrency attacks produced no failures. What keeps failing is the process, and they listed the patterns with a precision I wish more incident reports had:

1. **Compaction.** Long sessions compact, and afterwards the agent skips mandatory steps or writes its report from the compaction summary. This caused most of the failures.
2. **Lost outputs.** When a command exits non-zero, the harness does not save its output to a file and truncates the middle. A whole race run was lost that way.
3. **100 KB prompts.** Asked for an exact copy of its prompt, for recovery after compaction, the agent reproduced it from memory, incomplete or wrong. Once that tripped the platform's safety filter.
4. **Scripts edited in place.** Afterwards there is no way to prove which bytes actually ran.
5. **The harness against the rules.** The harness suggests `cat`, `sed` and heredocs, which their rules forbid.
6. **Too many rules.** In their words: "Every mistake added a rule, and every new rule caused new mistakes."

They have already decided what to change: nine small sessions instead of two large ones, a reference folder with hashes instead of a huge prompt, every output written to a file and read in full, scripts versioned and hashed before each run, and a session that compacts closes immediately. And they asked two questions, the second of which is the one I want to answer properly: does this level of rigour make sense, or am I overdoing it?

Their changes are right. What I want to add is why they are right, because the why is what lets the next problem get the same answer without a seventh pattern and a new rule. The why is complexity, and the tool I use to see it is a Wardley map.

## Complexity is a position on a map

A [Wardley map](https://wardley-maps.sgit.ai/) places each component of a system by how visible it is to the user, top to bottom, and by how evolved it is, left to right: genesis, custom-built, product, commodity. A healthy map has a thin custom layer where the value is, resting on parts that are products or commodities. I would go on record saying Wardley maps are what keep my world sane. They let me predict roughly what will happen, and they explain, after the fact, why something happened. When I look back at a failure, it is usually a mismatch on the evolution axis: something treated as a commodity that was still custom, or something rebuilt by hand that the world had already turned into a commodity.

Here is my friend's verification, mapped. Like every map on this site it is a claim, not a finding, and its source is below the figure so it can be argued with.

Map one: the verification as it runs. The person preparing the install needs confidence the tool is safe, which comes from a report, which rests on the tool's tests, holding, and on a team of agents. The six things that keep failing sit in a blob on the left, each rebuilt by hand inside a prompt every session. Files, hashes and git sit at the far right, unused.

The tool and its tests are where they should be: custom, because that is the work. The problem is the blob between the agents and the commodities. Recovery after compaction, capture of every output, proof of which bytes ran, a rule set measured in kilobytes, long sessions, and a STOP rule that fires on everything: each is being built by hand, in a prompt, by an agent, every session, from a memory that compaction rewrites. And at the bottom right, unconnected, are files, hashes and version control, which have solved most of those problems for decades.

That is what complexity looks like on a map. It is not the number of components; it is custom-built components sitting where commodities already exist, so that every one of them has to be maintained by attention. Every rule added to fix one of them is one more custom component in the same place, which is exactly the loop my friend described.

**Map one, the Mermaid wardley-beta source**

[rendered image](images/cx-map-now.webp)

```
wardley-beta
  title The verification as it runs: the process is a custom-built blob
  anchor "The person preparing the install" [0.97, 0.55]
  component "Confidence the tool is safe to install" [0.88, 0.42]
  component "The verification report" [0.80, 0.34]
  component "The tool's tests and race runs" [0.72, 0.46]
  component "Writer, verifier and reviewer agents" [0.66, 0.30]
  component "100 KB of rules in the prompt" [0.58, 0.14]
  component "Recovery after compaction" [0.52, 0.08]
  component "Long sessions" [0.46, 0.24]
  component "Capture of every output" [0.42, 0.16]
  component "Proof of which bytes ran" [0.36, 0.11]
  component "STOP on every deviation" [0.30, 0.20]
  component "Cowork and ChatGPT" [0.26, 0.76]
  component "Sandbox, no network" [0.14, 0.60]
  component "Files, hashes, git" [0.08, 0.88]
  "The person preparing the install" --> "Confidence the tool is safe to install"
  "Confidence the tool is safe to install" --> "The verification report"
  "The verification report" --> "The tool's tests and race runs"
  "The verification report" --> "Writer, verifier and reviewer agents"
  "Writer, verifier and reviewer agents" --> "100 KB of rules in the prompt"
  "Writer, verifier and reviewer agents" --> "Long sessions"
  "100 KB of rules in the prompt" --> "Recovery after compaction"
  "Long sessions" --> "Recovery after compaction"
  "Writer, verifier and reviewer agents" --> "Capture of every output"
  "Writer, verifier and reviewer agents" --> "Proof of which bytes ran"
  "Writer, verifier and reviewer agents" --> "STOP on every deviation"
  "Long sessions" --> "Cowork and ChatGPT"
  "The tool's tests and race runs" --> "Sandbox, no network"
```

## Move the pieces right

The way out is not a better rule. It is to take each piece of the blob, make it a small component with one job, test it once, ship it, and let it move right, so that it stops needing attention. Each of the six patterns maps to one such component.

| What failed | What it is on the map | The component that replaces the rule |
|---|---|---|
| Steps skipped after compaction | State held in the context, which compaction rewrites | Steps short enough to finish before compaction, reading their state from files and writing it back |
| Outputs lost on non-zero exit | Output capture done by hand | A run wrapper: every command goes through one small script that writes stdout, stderr, exit code and timing to a file before anything reads it |
| 100 KB prompts recited from memory | The model used as storage | A short policy and a reference folder on disk, with hashes; the session reads them and never recites them |
| Scripts edited in place | Provenance by trust | Scripts committed and hashed before each run; the run record names the commit |
| The harness suggests what the rules forbid | Rules fighting the environment | Change the environment, or accept its defaults where they are harmless; a rule that fights the tool loses |
| Every mistake adds a rule | Policy used as the control | Rules only for incidents, and each rule replaced by structure as soon as one can be built |

Map two: the same verification with each piece of process made small and drawn moving right. The tool's tests and the judgment in the report stay custom, because that is the work. Everything else becomes boring on purpose, leaning on files, hashes and git.

The table is not new advice. It is what [nfrs.sgit.ai](https://nfrs.sgit.ai/) found when it measured this estate against its own list of non-functional requirements and read down the failure column: "what a machine enforces, holds; what attention enforces, drifts." [coding.sgit.ai](https://coding.sgit.ai/) found the same from the other side: 31 documented rules, and the working automated enforcement is four structural guards, each of which encodes an incident rather than a rule. The rule that keeps that set healthy, as nfrs.sgit.ai puts it, is that every guard encodes a rule that was violated at least once. Rules that come from incidents, enforced by machines, stay few. Rules that come from worry, enforced by attention, multiply.

**Map two, the Mermaid wardley-beta source**

[rendered image](images/cx-map-next.webp)

```
wardley-beta
  title The same verification, with the process moved right
  anchor "The person preparing the install" [0.97, 0.55]
  component "Confidence the tool is safe to install" [0.88, 0.42]
  component "The verification report" [0.80, 0.40]
  component "The tool's tests and race runs" [0.72, 0.46]
  component "Writer, verifier and reviewer agents" [0.66, 0.36]
  component "Short policy read from disk, hashed" [0.58, 0.14]
  component "Steps that finish before compaction" [0.52, 0.10]
  component "A run wrapper that writes every output" [0.44, 0.16]
  component "Scripts committed and hashed before they run" [0.37, 0.12]
  component "Audit card from the transcript" [0.31, 0.22]
  component "Harm stops, form is logged" [0.26, 0.26]
  component "Cowork and ChatGPT" [0.26, 0.76]
  component "Sandbox, no network" [0.14, 0.60]
  component "Files, hashes, git" [0.06, 0.88]
  evolve "Short policy read from disk, hashed" 0.62
  evolve "Steps that finish before compaction" 0.58
  evolve "A run wrapper that writes every output" 0.70
  evolve "Scripts committed and hashed before they run" 0.82
  evolve "Audit card from the transcript" 0.60
  evolve "Harm stops, form is logged" 0.56
  "The person preparing the install" --> "Confidence the tool is safe to install"
  "Confidence the tool is safe to install" --> "The verification report"
  "The verification report" --> "The tool's tests and race runs"
  "The verification report" --> "Writer, verifier and reviewer agents"
  "The verification report" --> "Audit card from the transcript"
  "Writer, verifier and reviewer agents" --> "Short policy read from disk, hashed"
  "Writer, verifier and reviewer agents" --> "Steps that finish before compaction"
  "Writer, verifier and reviewer agents" --> "A run wrapper that writes every output"
  "Writer, verifier and reviewer agents" --> "Harm stops, form is logged"
  "A run wrapper that writes every output" --> "Files, hashes, git"
  "Scripts committed and hashed before they run" --> "Files, hashes, git"
  "Steps that finish before compaction" --> "Cowork and ChatGPT"
  "The tool's tests and race runs" --> "Sandbox, no network"
```

## The principles I work by

My friend is very clever, and very good at getting agents to keep an eye on other agents. What they do not have yet is the experience that tells an engineer when something is over-engineered, when it is good enough, and when to stop. So here are the principles I operate by. They are written for people, and they are also written to be handed to the agents that watch other agents, because most of them can be checked.

### 1. Map it, and look for the custom-built blob

Draw the map of your own project, and draw one of the complexity itself. Get an LLM to teach you the mapping if you have not done it before, and to draw a first version you then argue with. You are looking for components in custom-built that the world treats as a commodity, and for components you are treating as a commodity that are still custom. Both are where the next failure will come from. Then read the doctrine and the gameplay: [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/) lists forty doctrines, from *focus on user needs* and *use appropriate methods* to *think FIRE* (fast, inexpensive, restrained, elegant), *manage inertia* and *there is no core, everything is transient*. Several of them are exactly the problem here. *Know your users* and *focus on user needs* start with the person preparing the install, not with the process.

### 2. Commoditise small chunks all the time, and let them compound

A healthy workflow gets faster the more of it there is. The only way I have found to make that true in practice is to commoditise small chunks continuously, so they compound. If you look back at the work on this site you can trace it: small components that became bigger, that became the base for the next ones, each operating on top of the one below. Each is self-contained, and each keeps its blast radius under control, because it was shipped as a unit of its own: testable, battle-hardened, usable.

How the components compounded on this site, read from the bottom: sgit and encrypted vaults, vault apps and the publishing method, files as the database through Email-FS and Issues-FS, fractal semantic graphs, Agent Behaviour Policies, the agent team, and on top the story vaults and the bridge simulation. Each layer shipped before the next leaned on it.

The bridge simulation I published yesterday is a good test of this. It is a 126-file vault with an app, an API description, economics and four themes, and it was quick to build because almost nothing in it was new: the vault, the read key, the publishing method, the graph shapes, the review and the gate all existed already. The problem my friend has is the opposite. They are doing too much at once, so nothing gets to become boring.

### 3. Ship, and stop

Shipping is probably the single most important thing, end to end. To ship is to take something and make it usable by somebody else, and that somebody can be an agent: an agent that then gives feedback to another agent counts. If you do not ship, you over-engineer, and with LLMs it is very easy to over-engineer, because they can. Experience is largely knowing when to stop: what is good enough, what is over-engineered, and what is fine as it is. If you are not releasing something, you are probably not solving problems at the right altitude.

That is why a lot of what I publish is half-baked, by design. Every release teaches me something, usually what is missing, and then I stop. Stopping matters, because it means not continuing for the sake of continuing. I did a lot of newsroom experiments before the story vault work, and I stopped them when they had answered their question; the recent work here would not have been as good if I had pushed those through. Many sgit projects started as a problem I had, were solved to the point where the problem went away, and were left there. That is how it compounds: sometimes on tangents, but always with something shipped.

Making it public helps more than it seems to, because it removes a lot of complexity. You cannot hide an over-engineered thing in public, and you stop solving problems that do not need solving yet.

### 4. Keep sessions small and the context yours

The context window is what the model receives when it makes a call. The problem with large contexts is that you lose control of them, and when Claude or ChatGPT compacts, you do not control how it compresses or what it keeps. I see very few hallucinations these days, and I think it is because my briefs are tight, my sessions are tight, and I have many of them, each isolated, each with one focus. The agent team on this site works that way: [one step per agent of up to twelve minutes](the-agent-team-as-it-runs.md), each reading its state from files, doing one kind of work, writing its state back and stopping.

When I started, I had very long threads with an agent, and I would end each one by asking it to write a document with everything we had learned, decided and figured out, so that I could start a new session from that document. That is compression too, but compression you can read and correct. Start new sessions often; a new session is how you reset what is going on.

A good test: you should be able to open a new session, in Claude or in ChatGPT, and have it productive from the first prompt. The first prompt means the prompt plus the reference material, the project, the history and the guidance, and none of that needs to be large. It needs to be focused, architectural, compressed so that it makes sense, and read by you, because a document nobody reads drifts. If a session needs 100 KB of rules to be productive, the rules are doing the job that structure should do.

### 5. Memory is files, versioned

The reason for the file-system approach on this site, a brief, a brief of the brief, comments on the brief, a review, an index, is that every document an agent writes is a compression of what was learned, in a form the next agent can read. It is a graph, and [memory is not a spectator sport](memory-is-not-a-spectator-sport.md): it is the context you choose to give the next session. Agents talk to each other through Email-FS, work is tracked in [Issues-FS](https://issues-fs.sgit.ai/), and all of it is files, much of it in git and much of it in [vaults](what-sgit-is.md). Folders work; you can do this with folders. I prefer version control, git or a vault, because then the memory has a history, and you can prove which version of the prompt a session read, which is half of my friend's problem.

### 6. When complexity hits, slow down

If you are being hit by complexity, you have a problem, and the answer is to slow down: back to a first draft, break it into small components, take a step back and define them. If compaction is hurting you, you are giving the model far too much context, and you need to bring it down. And remember that you have time. For me the worst reason not to do something properly is "I just have to get this over the line". Compromising now to go faster usually slows you down. The check is simple: if you are not getting faster, you are paying for complexity, and most software teams before us have hit the same wall of diminishing returns. We have a better way now, and it is the one above: small pieces, productised, commoditised, then used to build the whole. That is why I use the file system as my database, keep things isolated, and build one thing on top of another.

### 7. Secure against the threat, not against everything

You want things secure; more than that, you want them safe, and those are not the same. Sometimes it is right to ship something that is not fully hardened, as long as its attack surface is controlled: you monitor it, or nothing valuable is reachable from it. In my experience most companies ship software that is far less secure than its users assume; the difference is whether they know which compromises they made. The questions are: what are the assets, what is the threat, what is the attack vector, and what are the customers actually buying? If something runs on an isolated machine with no network and nothing of value on it, many attacks are simply not available, and the requirements drop accordingly. Write the threat model down, one page, publish it, and ask the community whether you are making the right compromises. That will tell you more about whether you are overdoing it than another rule will. The site's articles on [risk acceptance](every-risk-is-already-accepted.md) and [footprint and blast radius](footprint-and-blast-radius.md) go further into how to record the compromises you choose.

### 8. Rules for incidents, machines for enforcement

This is the principle the six patterns come down to, and it is the one I would hand straight to the agents that watch other agents. A rule is a weak barrier: it relies on the agent remembering and judging, and in [the agent team's own grading](the-agent-team-as-it-runs.md) the policy text is graded weak. A record, the transcript, the history, the hashes, detects. A boundary, an account the agent does not have or a network it cannot reach, prevents. When a rule fails, the question is not how to word it more strongly but which of the stronger barriers can replace it. On this site, the vaults and the site itself are published through gates of checks that fail the build; the [bridge vault's gate](the-bridge-followed-to-the-end.md) runs 44 of them, and many exist because something broke once. [Green does not mean live](green-does-not-mean-live.md) is the story of one of them.

### 9. Run it in five environments

Running in isolation is good. Running in five different environments is better: locally, air-gapped, and on Azure, GCP and AWS. A solution that runs in all of them has had a great many problems solved out of it, because each environment breaks a different assumption. It is the most useful thing to do when complexity starts to hit, because it shows you where the bottlenecks are. Then go back to the question of what you actually want to ship, and get that over the line.

### 10. Reverse-engineer the path to the destination

It is very easy now to design very large, comprehensive solutions. They are fine as a destination, but you need to reverse-engineer the five, seven or ten paths that evolve into them. A forest is a useful picture: it grows through stages, each changing the ground for the next, and by the time the big trees stand, many of the earlier species are gone, because they do not fit the ecosystem they helped create. Components are like that. Open source helps here, because it puts little sense of ownership on the technology, and you are glad to get rid of it. The vaults are open source, so I will gladly build a solution that does not use them. That is brutal, but if you have a choice and you do not use what you built, it is not good enough yet. Keep iterating, releasing and shipping, and keep reducing complexity, which is the name of the game.

### 11. Learn the engineering that already exists

If you have caught the engineering bug, and with agents many founders have, you are working as an engineer now, so geek out on the practice. Continuous integration, Kanban boards, engineering patterns, the history of what worked: much of what my friend is rediscovering under pressure has a name and a literature. On this site, [nfrs.sgit.ai](https://nfrs.sgit.ai/) is the estate's own account of testing, CI, documentation, resilience and the methodology we call Iterative Flow Development, which names developer attention as the scarce resource the whole process exists to protect; and [coding.sgit.ai](https://coding.sgit.ai/) is how the code is actually written, counted rather than claimed. Its testing rule, no mocks and no patches, is affordable only because cheap typed objects make the real thing as easy to build as a stand-in: the type system and the testing philosophy are one decision. That is the kind of lesson that is cheaper to read than to rediscover. [Who reads the code](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/humans/dinis_cruz/briefs/03/21/v0.16.26__article__who-should-read-the-code.md), and what quality engineering each stage of evolution needs, is the same map applied to code.

## Answers to the questions

**Do you let sessions compact, or design every step to finish before?** I design steps to finish before compaction, and I keep the state of the step on disk so that compaction, if it happens, loses nothing that matters. Closing a session that compacts is a good rule, because it is a boundary, not a request. And do not ask an agent to recite its prompt: point it at the file, and record the file's hash in the run.

**How does the post-session audit card work?** It is a script over the transcript, run after the step. It counts tools, tokens, files and network calls, and flags anything outside the agent's policy; the card is attached to the step's record. The point is that the agent does not police itself on every command, which costs attention and context, and that the record is read afterwards by something that was not part of the work. [Footprint and blast radius](footprint-and-blast-radius.md) is the idea behind it, and [the agent team](the-agent-team-as-it-runs.md) describes what the first card flagged.

**When an agent makes a mistake of form, do you log it and continue?** Yes. Log mistakes of form and carry on; stop for harm, or for a boundary that broke. If everything is a STOP, a STOP stops meaning anything, and the process spends its attention on itself. In the agent team, a stop is a hold file that only a person can release. An accidental calendar call, which failed and sent nothing, was logged by the agent against its own policy rather than treated as a hold.

**Is this level of rigour overdoing it?** For the process, yes. For the intent, no. The rigour should match the assets and the blast radius. The code is where it was needed, and it is holding. The process around it has become a second product nobody asked for, and it is costing more than the verification it serves. Make the process small and boring, and spend the rigour on the tool.

## The same lesson, one level up

This applies to companies as much as to sessions, and I say it about my own. We have mapped what I think is a strong path, from agent behaviour policies to a licence to operate to insurance. But the customers we talk to are struggling with something much simpler, and our way to market is to break what we have into much simpler components, so that we earn the customers and the projects that need the bigger capabilities. It is brutal, because if it cannot work in the simple use cases, it will struggle in the complex ones. Funding does not always help here; it can give you a false sense of having a product, or of a product being ready to scale when it is not.

## Where to start

- **Draw the map.** Your project, then the process around it. Mark the blob.
- **Pick the most expensive piece of the blob** and make it a small tool with one job. Test it. Ship it, even if the only user is your own agents.
- **Cut the prompt to a page.** Move the rest into files the session reads, with hashes.
- **Make outputs a file by construction**, through a wrapper every command goes through.
- **Commit before you run.** The run record names the commit.
- **Split the STOPs**: harm stops, form is logged.
- **Write the threat model on one page, publish it, and ask** whether the compromises are right.
- **Run it somewhere else**, then somewhere else again.
- **Delete a rule** every time a component makes it unnecessary.

And then ship the next small thing. It probably sounds daunting at first. It is less daunting than the complexity you already have.

*Drafted from two messages and a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 8 October 2026. The messages are paraphrased and their author is not named; the one line quoted from them is theirs. Quotations from nfrs.sgit.ai and coding.sgit.ai are from those sites as published. The doctrine names are Simon Wardley's, as listed on wardley-maps.sgit.ai; Wardley Mapping is provided courtesy of Simon Wardley, CC BY-SA 4.0. The two maps were rendered with Mermaid's wardley-beta diagram from the sources shown, and every placement in them is a claim.*

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#every-mistake-added-a-rule)

### Builds on

- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.
- [Green does not mean live](green-does-not-mean-live.md) Two releases passed every check and never reached the site because the checks stopped at the git remote; a release now ends by asking the live site its version.

### Continued by

- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault](from-a-spreadsheet-to-a-folder-per-person.md) A walkthrough from a spreadsheet CRM to one Drive folder per person, worked by Claude under a six-line policy, with five exercises, before any vault is needed.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 43 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=43)

## From the desk

- [Range is the feature, so the stop has to be designed](desk/range-is-the-feature-so-the-stop-is-designed.md) thread, 2026-10-08
- [How agents decide, and when they stop](collections/how-agents-decide.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [every-mistake-added-a-rule.jpg](banners/every-mistake-added-a-rule.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html)*
