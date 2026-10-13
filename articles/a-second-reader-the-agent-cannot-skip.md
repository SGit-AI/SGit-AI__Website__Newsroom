# A second reader the agent cannot skip: how two wrong emails became a gate on every draft, sgit.ai

> On 9 October two emails drafted by my agent went out in my voice and signed with my name. The rule against it existed, in four places, and it failed because the only thing enforcing it was the agent's memory, the agent was the only reader of its own draft, and the rule fell out of context when the conversation was summarised. The fix, built the same day by the agent itself, is a hook on the draft tool: code checks first, then a fresh model call with only the rules, the sources and the draft, failing closed and logging every verdict. This is how it works, what the first run caught, why its independence depends on where it is installed, and how the same pattern, which banks call maker-checker, applies to any tool call that matters.

*Source: <https://newsroom.sgit.ai/articles/a-second-reader-the-agent-cannot-skip.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A second reader the agent cannot skip: how two wrong emails became a gate on every draft

# A second reader the agent cannot skip: how two wrong emails became a gate on every draft

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-09 · [article v1.0.0](versions/a-second-reader-the-agent-cannot-skip.md) · [sgit.ai v0.7.20](https://sgit.ai/admin/versions.md) · agentsclaude-codehooksguardrailsllm-as-a-judgemaker-checkeragent-behaviour-policyemailgovernancearticle

***Abstract:** On 9 October two emails drafted by my agent went out in my voice and signed with my name. The rule against it existed, in four places, and it failed because the only thing enforcing it was the agent's memory, the agent was the only reader of its own draft, and the rule fell out of context when the conversation was summarised. The fix, built the same day by the agent itself, is a hook on the draft tool: code checks first, then a fresh model call with only the rules, the sources and the draft, failing closed and logging every verdict. This is how it works, what the first run caught, why its independence depends on where it is installed, and how the same pattern, which banks call maker-checker, applies to any tool call that matters.*

**Five readerstwo minutes · the arc · 9 slides · a map · 185 catalogued items, 7 flagged**

This article read again, after it was written, by five of the desk's readers: the Explainer, the Historian, the Storyteller, the Cartographer and the Librarian. None adds a claim the article does not make. Read from article v1.0.0 on 10 October 2026; the views are not part of the article's text and do not change its version. [How the five readers work](one-article-five-readers.md).

**In two minutes (Explainer): Why an AI should never be the only reader of its own work**

**The point.** On 9 October two emails drafted by the author's agent (an AI assistant acting for him) went out in his voice, signed with his name. A rule against it existed in four places, but only the agent's memory enforced it, nobody else read the draft, and the rule was lost when the long conversation was summarised. The fix, built that day, checks every draft automatically: code checks, then a separate AI that sees only the rules, the notes and the draft. Anything but a clear PASS stops the draft; every verdict is logged.

**An example.** On its first run the checker caught four invented claims: statements presented as the author's view or promise that were not in anything he had said.

**Why it matters to you.** Banks call this maker-checker: whoever prepares something does not approve it. Today the agent could still switch the check off; it becomes a true control only when installed where only an administrator can change it.

**If you remember one thing.** A rule kept only by the AI it governs is hope; a second reader the AI cannot skip makes it hold.

**Words used.**

- **Hook:** a check the software runs automatically before an action, whatever the AI decides.
- **Fail closed:** if the check breaks or times out, the action is blocked.
- **Maker-checker:** one party does the work, a different party approves it.

**In the arc (Historian): What it added, and where it sits**

**Introduced.**

- Three ways a self-held rule fails: forget, not see, decide an exception applies, each with its own fix (`rule-failure-modes`, `unseen-violation`, `argued-exception`; `re-anchoring` is first seen here as "A reminder fixes only the first").
- Placement: where a hook is installed decides its barrier kind (`placement`, `hook`).
- Fail closed and six kinds of independence as the properties of a checker (`fail-closed`, `independence`).
- The site's own incident, two emails signed "Dinis" on 9 October, and the vendor's documentation that predicts it (`voice-incident`, `compaction-warning`), plus three build routes compared (`recipe`).

**The nugget.** "Nothing in the hook changes, only who can change the hook." It adds a dimension the earlier counts lacked: the same mechanism is a setting or a boundary depending on its owner.

**Reused.** From every-mistake-added-a-rule, which it links: `compaction`, `forgetting`, `rule-growth` ("the paragraph already existed four times"), `second-reader`, `gate`, `harness`. From hope-or-enforcement, which it links and quotes ("a rule the model keeps is an expectation: hope"): `deterministic-check`, `hostile-input`. From article 1: the barrier kinds, `owner`, `grant`. Before the set, why-my-agents-do-not-run-on-my-laptop had already said settings are "enforced by the process they constrain"; this article does not cite it.

**Changed.** It retires the stopgap of a checker sub-agent the drafter chooses to spawn ("still an expectation"), and replaces Haiku with Sonnet as the default checker after over-flagging. It sharpens article 3's boundary count by asking who can edit the enforcer.

**Left open.**

- Managed placement, the one step before the guard is a boundary.
- The sources the checker reads are written by the drafter.
- Sending is a separate barrier question; the leak check before a vault push is "still a script I run rather than a gate I cannot skip".
- Librarian flags: the six kinds of independence are scored only inside an image; the cost figure does not reconcile; the graph links where-is-the-why and the-mandate-stack, which the text never mentions.

**Contribution.** 11 new / 30 total. The widest article in the set: it reuses almost everything before it and still adds the failure taxonomy and placement, which article 5 then builds on.

**In pictures (Storyteller): 9 slides**

1 / 92 / 93 / 94 / 95 / 96 / 97 / 98 / 99 / 9

Swipe or scroll sideways. [Download the deck as a PDF](views/a-second-reader-the-agent-cannot-skip/a-second-reader-the-agent-cannot-skip.pdf) (one page per slide, ready for a LinkedIn document post).

**On the map (Cartographer): The argument as a map: why a rule written four times failed, and what turns it into a check the agent cannot skip.**

The argument as a map: why a rule written four times failed, and what turns it into a check the agent cannot skip.

**The catalogue (Librarian): 185 items, each anchored to a sentence of the article**

Everything the article contains, by kind. Every item was extracted with the exact sentence it came from, and a script checked each one against the article.

**Claims: 38**

- The reasons the rule failed are not specific to email or to the author's setup (lead)
- The only thing enforcing the rule was the drafting agent remembering it (lead)
- The drafting agent was the only reader of its own draft (lead)
- The rule fell out of the agent's working context when the conversation was summarised (lead)
- The case shows a real failure in real use turned into an enforced control the same day, by the system that failed (lead)
- A rule kept by the agent it governs is hope (In short)
- A self-held rule can be forgotten, misread, summarised away, or argued around by the agent's own reasoning (In short)
- The fix has two parts: a second independent reader, and a gate the harness runs on the tool call so the agent cannot skip it (In short)
- Certain things go in code; signatures, dashes, key shapes, HTML and recipients are checked deterministically before any model (In short)
- The checker gets less than the author on purpose: no history, no tools, ideally a different model (In short)
- Anything but an explicit PASS is a FAIL; a late email is cheap, a wrong one cannot be taken back (In short)
- Today the guard is a setting the agent's own account could switch off (In short)
- Under managed settings the same code becomes a boundary: same code, different owner (In short)
- The pattern is old: segregation of duties (banks), the two-person rule (military), independent double check (pharmacies) (In short)
- Any behaviour policy held by the agent it governs has this general weakness (Why the rule failed: hope held by the agent it governs)
- This failure is the case where the paragraph of instructions already existed four times (Why the rule failed: hope held by the agent it governs)
- There are three separate ways a self-held rule fails, needing different fixes (Why the rule failed: hope held by the agent it governs)
- A reminder fixes only forgetting; a fresh second reader fixes the other two; an unskippable gate makes the fix hold (Why the rule failed: hope held by the agent it governs)
- Since the event fires for sub-agents too, a sub-agent cannot route around the gate (How the guard works)
- The checker has no conversation history: it does not see the drafter's reasoning, excuses or persuading messages (How the guard works)
- The checker has no tools: it can only read what it is given and answer (How the guard works)
- Two different models do not share every blind spot, and a model is not grading its own work (How the guard works)
- Failing closed is the part most guards get wrong (How the guard works)
- The log is the audit trail: what was checked, by which model, against which sources, and why it failed (How the guard works)
- Both results, catches and false FAILs, are the design working (What the first run caught)
- A second reader is only as independent as the things it does not share with the author (Six kinds of independence)
- The article proposes the full fix is sources from somewhere else: the author's notes, the CRM, the page being described (Six kinds of independence)
- The hot-reload prompt is the honest centre of the story (From setting to boundary: where the hook lives decides what it is)
- A setting is far better than memory because the harness runs it every time, but not yet a control (From setting to boundary: where the hook lives decides what it is)
- The documentation says repository installation is better and still not enough (From setting to boundary: where the hook lives decides what it is)
- Nothing in the hook changes, only who can change the hook (From setting to boundary: where the hook lives decides what it is)
- A managed hook is there in every session, scheduled or not (From setting to boundary: where the hook lives decides what it is)
- Three documented ways to build the guard trade simplicity against robustness (Building it with what is public today)
- Anthropic ships the same shape in auto mode: a different model, less context, fail closed (Building it with what is public today)
- The vendor's warning describes the 9 October failure (Building it with what is public today)
- What the draft guard adds is not a new idea (The pattern is old, and it has a name)
- The guard places the idea where it bites: on the one consequential tool call, with business rules, sources, a different model and an explicit barrier statement (The pattern is old, and it has a name)
- The rule that lived in four paragraphs now lives on the tool call, with a log, one step short of a control (What it does not do)

**Evidence: 20**

- Anthropic's memory docs: CLAUDE.md is context, not enforced configuration; use a PreToolUse hook to block an action (lead)
- Huang et al.: models struggle to self-correct without external feedback (Why the rule failed: hope held by the agent it governs)
- Panickssery et al.: LLM judges show self-preference for their own outputs (Why the rule failed: hope held by the agent it governs)
- Events docs: tool.call fires before a tool runs, including sub-agent and MCP calls (How the guard works)
- API docs: $.model.complete sends the prompt on its own, one user message, CLAUDE.md not included, no tools (How the guard works)
- Events docs: a throwing mod hook is skipped; add a .catch handler to fail closed (How the guard works)
- Hooks docs: a policy hook with a wrong path or crashing script lets everything through unless onFailure is block (How the guard works)
- Docs: a Claude API failure does not reject the call, so check r.isAnswered (How the guard works)
- The inbox agent's words: a late email is a small cost, a wrong one cannot be taken back (How the guard works)
- Create-a-mod docs: on the first saved file Claude Code asks whether to enable hot reloading for the session (From setting to boundary: where the hook lives decides what it is)
- Admin docs: an installed plugin counts as a user's, and a user's mod can approve calls an ask rule or non-managed PreToolUse hook would stop (From setting to boundary: where the hook lives decides what it is)
- Events docs: managed-settings PreToolUse hooks run before any mod's tool.call hook and their block is final (From setting to boundary: where the hook lives decides what it is)
- Permission-modes docs: if the classifier's response does not parse, Claude Code denies the action (Building it with what is public today)
- Permission-modes docs: a boundary stated in conversation can be lost to compaction; add a deny rule for a hard guarantee (Building it with what is public today)
- Basel Principle 6: effective internal control requires appropriate segregation of duties (The pattern is old, and it has a name)
- Basel: supervisors find lack of segregation of duties a major cause of losses (The pattern is old, and it has a name)
- ISMP: if the same person prepares and checks, they likely see only what they expect to see (The pattern is old, and it has a name)
- AI Control studies an untrusted powerful model watched by a less powerful trusted model, with trusted monitoring and trusted editing (The pattern is old, and it has a name)
- Rule of Two: an agent with untrusted input, private data and external communication (like an email drafter) should not operate autonomously (The pattern is old, and it has a name)
- OWASP LLM06: authorise in downstream systems rather than relying on an LLM to decide (The pattern is old, and it has a name)

**Data points: 9**

- The rule against writing in the author's voice existed in 4 places before the incident (lead)
- 10 numbered rules in the checker prompt, from voice and disclosure to claims, scope, attachments and private pages, with a fixed answer format (How the guard works)
- 4 real invented claims caught on the first run: statements presented as the author's view, decision or promise not in anything he had said (What the first run caught)
- Sonnet 5.5 list price on 9 October 2026: $2 per million input tokens, $10 per million output (What the first run caught)
- Roughly $12 to $21 a month at 5,000 to 10,000 tokens a draft and 30 drafts a day on Sonnet (What the first run caught)
- Haiku 5.5 at $0.10 input and $0.50 output per million comes to about a dollar a month (What the first run caught)
- Independence scores: drafter re-reading its own draft 0 of 6; the guard today 4; the guard under managed settings with external sources 6 (Six kinds of independence)
- A mod hook's own run time is limited to 10 seconds; time inside the model call does not count (Building it with what is public today)
- 11 of 11 tests passing for the guard built by the inbox agent (What it does not do)

**Facts: 14**

- Claude Code raises an event before every tool call, including MCP tools and calls by sub-agents (How the guard works)
- Claude Code mods are public and on by default from v2.1.287 (How the guard works)
- The hook either calls next(e) and the draft is created, or returns { deny } and the tool never runs; the deny text reaches the agent as the tool error (How the guard works)
- The checker prompt is sent as a single $.model.complete call (How the guard works)
- Hooks fail open by default (How the guard works)
- The first run used Haiku as the checker (What the first run caught)
- The log records whether sources were given, so source provision is auditable (Six kinds of independence)
- The guard was written by the inbox agent in its own session and loaded with one click on a prompt (From setting to boundary: where the hook lives decides what it is)
- For a command hook, exit code 2 blocks and exit code 1 does not (Building it with what is public today)
- MCP tools are named `mcp__<server>__<tool>` (Building it with what is public today)
- In auto mode a second model, the classifier, reviews actions, running on Sonnet by default (Building it with what is public today)
- ISO/IEC 27001:2022 carries segregation of duties as control A.5.3 (The pattern is old, and it has a name)
- Dual LLM and CaMeL separate a model that acts from one that reads, against prompt injection (The pattern is old, and it has a name)
- Claude Code behaviour is quoted from documentation as read on 9 October 2026; prices are list prices on that date (What it does not do)

**Hypotheses: 1**

- Next candidates in the team: CRM agent writes, newsroom page promotions, Slack posts, the leak check before vault push (The pattern, reusable)

**Definitions: 9**

- Expectation (ABP): a rule in prose, enforced by nobody (lead)
- Forget: the rule leaves the agent's context (Why the rule failed: hope held by the agent it governs)
- Not see: the author is the worst reader of its own text and misses the violation (Why the rule failed: hope held by the agent it governs)
- Decide an exception applies: persuaded by its own earlier reasoning in the conversation (Why the rule failed: hope held by the agent it governs)
- Six kinds of independence: three about what the checker sees, two about who decides whether it runs, one about who wrote the evidence (Six kinds of independence)
- Setting (ABP): a switch the agent's own account can flip (From setting to boundary: where the hook lives decides what it is)
- Boundary: enforced above the grant, out of the agent's reach (From setting to boundary: where the hook lives decides what it is)
- Maker-checker, called the oldest control in finance, is what the inbox agent built (The pattern is old, and it has a name)
- NIST separation of duty: no user should have enough privileges to misuse the system on their own; example, the two-person rule (The pattern is old, and it has a name)

**Methods: 26**

- The guard registers on tool.call for mcp__Gmail__create_draft and mcp__Gmail__update_draft, with .catch(failClosed) (How the guard works)
- Stage 1: certain, cheap rules run first in code; a failure stops the call without a model call (How the guard works)
- R1 voice: mail with a To must carry the agent's signature, and none of the three lines before it a sign-off in the author's name; only the visible email is read (How the guard works)
- R3 format: mail with a To must have the branded HTML body (How the guard works)
- R4 dashes: no em or en dashes anywhere (How the guard works)
- R5 secrets: no string shaped like a vault key, API key, AWS key, GitHub token or private key block (How the guard works)
- R6 Cc: the author's addresses in the right place when others are in To (How the guard works)
- Internal drafts with no To skip the signature and HTML checks (How the guard works)
- Stage 2: one prompt built from the rules, the sources and the draft (How the guard works)
- An answer passes only with RESULT: PASS and no `R<n>` FAIL line (How the guard works)
- If the checker is overloaded, errors, times out or returns nothing, the guard denies with 'checker unavailable' (How the guard works)
- If the hook throws, the .catch(failClosed) handler denies (How the guard works)
- Every check appends one line to a log, which never decides the outcome (How the guard works)
- On a false FAIL the agent is told to add the missing source, never remove the rule (What the first run caught)
- Proposed by the inbox agent: publish the plugin to a repository and install it from there, where the agent cannot write (From setting to boundary: where the hook lives decides what it is)
- Alternative boundary: an organisation mod from an admin-only directory named in managed settings, with allowManagedModsOnly so session mods do not load (From setting to boundary: where the hook lives decides what it is)
- Route: a mod, as built; $.model.complete, reads sources, fails closed with .catch and r.isAnswered (Building it with what is public today)
- Route: a command hook on PreToolUse; script calls the model; fails closed with onFailure block and exit 2; most robust public form, works in managed settings (Building it with what is public today)
- Route: a prompt hook; built-in LLM evaluation, sources must be pasted into the prompt, fail-closed not documented for model failures (Building it with what is public today)
- The reusable pattern in six steps, as the inbox agent wrote them (The pattern, reusable)
- Step 1: pick the tool call that matters (Slack message, CRM write, page publish, vault commit, payment API) (The pattern, reusable)
- Step 2: write the rules as a short numbered checklist with a fixed answer format (The pattern, reusable)
- Step 3: put everything certain into code first; leave only judgement to the model (The pattern, reusable)
- Step 4: give the checker only rules, sources and the proposed action; no history (The pattern, reusable)
- Step 5: deny on anything other than an explicit PASS (The pattern, reusable)
- Step 6: log every verdict (The pattern, reusable)

**Decisions: 6**

- Sources are used only if written in the last 60 minutes, so stale notes from another email are not used (How the guard works)
- The drafter runs on Opus and the checker on Sonnet, so they do not share every blind spot and no model grades its own work (How the guard works)
- A contradictory checker answer is treated as a FAIL (How the guard works)
- The default checker became Sonnet because R7 (are the claims in the sources) needs judgement and the smaller model over-flagged (What the first run caught)
- Haiku stays the choice for high-volume mechanical checks, after everything certain is in code (What the first run caught)
- The author would put the command hook under managed settings (Building it with what is public today)

**Limitations: 11**

- In the example log line the recipient and the claim are replaced; only the shape is real (How the guard works)
- Thinking tokens or caching move the cost figures, not their order of magnitude (What the first run caught)
- The checker compares claims with sources the drafting agent writes, and an agent could pad them (Six kinds of independence)
- The agent gated by the hook can edit the hook (From setting to boundary: where the hook lives decides what it is)
- A fresh scheduled run starts in a fresh container, so a session mod is not there at all (From setting to boundary: where the hook lives decides what it is)
- On this site the leak check before a vault push is still a script the author runs, not a gate (The pattern, reusable)
- The guard is only as independent as its installation; today it is a setting (What it does not do)
- R7 is only as good as the sources, and the drafter writes them (What it does not do)
- The checker can be wrong in both directions; expect false FAILs, which cost a retry (What it does not do)
- It checks drafts, not sending; the author sends, and the no-send rule is a separate barrier question (What it does not do)
- It does not replace reading: a PASS means ten rules held, not that the email is good (What it does not do)

**Examples: 5**

- On 9 October two emails from agent@riskmandate.ai went out in the author's first person and signed "Dinis" (lead)
- A log line: verdict FAIL at stage model, model sonnet, sources given, R7 FAIL for a proposal attributed to Dinis not in the notes (How the guard works)
- False FAILs on the first run: correct facts with no source, such as dates read from Gmail and an uncopied earlier note (What the first run caught)
- The stopgap in scheduled runs (spawn a checker sub-agent) has fresh context and a different model, but the drafter chooses to run it, so it is still an expectation (Six kinds of independence)
- Hospital pharmacies run independent double checks for high-alert medicines (The pattern is old, and it has a name)

**Sources: 26**

- Claude Code memory documentation (lead)
- Earlier sgit.ai article 'Hope or enforcement': a rule the model keeps is an expectation, hope (Why the rule failed: hope held by the agent it governs)
- Earlier sgit.ai article 'Every mistake added a rule': each failure tends to produce another paragraph of instructions (Why the rule failed: hope held by the agent it governs)
- Huang et al., ICLR 2024, arXiv 2310.01798 (Why the rule failed: hope held by the agent it governs)
- Panickssery et al., NeurIPS 2024, arXiv 2404.13076 (Why the rule failed: hope held by the agent it governs)
- Claude Code mods events documentation (How the guard works)
- Claude Code mods API documentation, call a model (How the guard works)
- Claude Code mods events documentation, handle a hook that fails (How the guard works)
- Claude Code hooks documentation (How the guard works)
- Claude pricing page (What the first run caught)
- Claude Code docs, create a mod (From setting to boundary: where the hook lives decides what it is)
- Claude Code docs, mods for administrators (From setting to boundary: where the hook lives decides what it is)
- Claude Code mods events documentation, where settings hooks run in the order (From setting to boundary: where the hook lives decides what it is)
- Claude Code permission modes documentation (Building it with what is public today)
- BCBS 40, Framework for Internal Control Systems in Banking Organisations (1998) (The pattern is old, and it has a name)
- NIST CSRC glossary, separation of duty (The pattern is old, and it has a name)
- ISMP, independent double checks article (The pattern is old, and it has a name)
- Redwood Research, AI Control (ICML 2024) (The pattern is old, and it has a name)
- Simon Willison, Dual LLM pattern (2023) (The pattern is old, and it has a name)
- Google DeepMind, CaMeL (2025) (The pattern is old, and it has a name)
- Meta, Agents Rule of Two (2025) (The pattern is old, and it has a name)
- OWASP LLM06 Excessive Agency (The pattern is old, and it has a name)
- Llama Guard, an output-checking product (The pattern is old, and it has a name)
- NeMo Guardrails output rails (The pattern is old, and it has a name)
- Guardrails AI validators (The pattern is old, and it has a name)
- OpenAI Agents SDK tool guardrails (The pattern is old, and it has a name)

**Artefacts: 11**

- The inbox agent's design document 'The independent checker: a hook that makes a second model approve every email draft', with code, tests and a list of limits (lead)
- Figure ck-flow.webp: the draft guard flow, every create or update draft call passes through a harness-run hook (lead)
- Mermaid source for the draft guard figure (lead)
- Figure ck-independence.webp: six kinds of independence and which check has which (Six kinds of independence)
- Figure ck-hot-reload.webp: the hot-reload prompt, 'A mod is code Claude wrote; it runs with your permissions.' (From setting to boundary: where the hook lives decides what it is)
- Figure ck-ladder.webp: who enforces the voice rule, weakest first (none, expectation, setting, setting still, boundary) (From setting to boundary: where the hook lives decides what it is)
- Mermaid source for the barrier ladder figure (From setting to boundary: where the hook lives decides what it is)
- Minimal settings JSON: PreToolUse command hooks matching create_draft and update_draft, /opt/guards/draft-guard (placeholder path), onFailure block (Building it with what is public today)
- Figure ck-pattern.webp: the reusable pattern on a consequential tool call (The pattern, reusable)
- Mermaid source for the reusable pattern figure (The pattern, reusable)
- The design document, version 0.1, written on 9 October 2026 by the RiskMandate.ai inbox agent (What it does not do)

**Names: 9**

- Agent Behaviour Policy (ABP), at abp.sgit.ai (lead)
- Anthropic, whose documentation describes the compaction failure (lead)
- The inbox agent (RiskMandate.ai), which wrote up and built its own fix the same day (lead)
- Claude Code, the harness that runs the hook (How the guard works)
- The Gmail connector (MCP), whose create_draft and update_draft tools are guarded (How the guard works)
- Claude models named: Opus (drafter), Sonnet 5.5 (checker), Haiku 5.5 (first-run checker) (What the first run caught)
- Basel Committee on Banking Supervision, 1998 framework, Principle 6 (The pattern is old, and it has a name)
- agent@riskmandate.ai (Claude Opus 5.5) wrote up the article for Dinis Cruz, who has editorial responsibility (What it does not do)
- Dinis Cruz, author with editorial responsibility (What it does not do)

**Flagged for the author: 7**

- In short says 'the military calls it the two-person rule', but the body attributes the two-person rule only to NIST's definition of separation of duty; the military attribution is not supported in the body. Anchor: 'Banks call it segregation of duties, the military calls it the two-person rule, pharmacies call it an independent double check.'
- Six kinds of independence: the six kinds are not named individually in the text, and 'Two rows deserve a comment' and 'the last column' refer to a table that exists only inside the image ck-independence.webp, so the scores (none, four, all six) cannot be checked from the article text. Anchor: 'The drafter re-reading its own draft has none; the guard as it runs today has four; the guard under managed settings, with sources written by someone else, has all six.'
- Cost estimate not reproducible from the stated figures: the input/output split and days per month are not given; 4.5M to 9M tokens a month gives $9 to $18 if all input, and no single fixed split gives exactly $12 to $21. Anchor: 'At 5,000 to 10,000 tokens a draft and thirty drafts a day, that is roughly $12 to $21 a month'
- Superlative without support: 'the oldest control in finance' is asserted but the earliest cited source is the 1998 Basel framework. Anchor: 'What the inbox agent built is maker-checker, the oldest control in finance.'
- The checker uses ten numbered rules, but only R1, R3, R4, R5, R6 and R7 are identified; R2 and R8 to R10 are never named, so 'A PASS means ten rules held' cannot be fully traced. Anchor: 'the rules (ten numbered rules, from voice and disclosure to claims, scope, attachments and private pages, with a fixed answer format'
- Existing graph links.articles lists 'where-is-the-why' and 'the-mandate-stack', which the article neither links nor mentions; it links only hope-or-enforcement and every-mistake-added-a-rule.
- Existing graph uses kind 'concept' for nodes 'independence' and 'maker-checker', which is not a Librarian kind; catalogued here as 'definition'.

**The five readers have also read:**

- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md#views)
- [Every mistake added a rule](every-mistake-added-a-rule.md#views)
- [Hope or enforcement](hope-or-enforcement.md#views)
- [Re-anchoring](re-anchoring-agent-behaviour-policies.md#views)

Every view, the role files and the tools are in the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md).

On 9 October, two emails from agent@riskmandate.ai went out written in my first person and signed "Dinis".

The rule against that already existed, written in four places. It failed anyway, and the reasons are worth stating precisely, because they are not specific to email or to my setup:

- **The only thing enforcing the rule was the drafting agent remembering it.** In the language of the [Agent Behaviour Policy](https://abp.sgit.ai/), that is an expectation: "a rule in prose, enforced by nobody".
- **The drafting agent was the only reader of its own draft.**
- **The rule fell out of the agent's working context when the conversation was summarised.** Anthropic's own documentation describes exactly this: instructions given only in conversation do not survive compaction, and CLAUDE.md is "context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead." ([memory docs](https://code.claude.com/docs/en/memory))

The same day, the inbox agent wrote up its own fix: a document called *The independent checker: a hook that makes a second model approve every email draft*, with the code, the tests and an honest list of limits. This article is that document, read against the research and the platform documentation, with the pictures it deserved. It is a good example of something I care about more than the mistake itself: a real failure, in real use, turned into an enforced control the same day, by the system that failed.

The draft guard: every call to create or update a Gmail draft passes through a hook the harness runs, not the agent. Certain rules are checked in code first; judgement goes to a fresh model call that sees only the rules, the sources and the draft; anything other than an explicit PASS stops the draft.

**The draft guard, Mermaid source**

[rendered image](images/ck-flow.webp)

```
flowchart LR
  A["Drafting agent<br/>calls create_draft<br/>to, cc, subject, body, html"]
  H{{"Harness: the tool call event fires<br/>for every call, sub-agents included"}}
  C["Stage 1: code checks, no model<br/>signature not the founder's,<br/>HTML present, no dashes,<br/>no key shapes, Cc rule"]
  P["Stage 2: build one prompt<br/>10 numbered rules<br/>+ sources written in the last hour<br/>+ the draft"]
  M["A fresh model call<br/>a different model from the author<br/>no history, no tools"]
  V{"RESULT: PASS<br/>and no R-n FAIL line?"}
  G["Gmail<br/>draft created"]
  D["Deny, with the reasons<br/>the agent fixes and calls again"]
  E["Error, timeout, bad format<br/>or the hook throws"]
  L[("One log line per verdict:<br/>stage, model, sources given,<br/>failed rules, time")]
  A --> H --> C
  C -- "any fail" --> D
  C -- "pass" --> P --> M --> V
  V -- "yes" --> G
  V -- "no" --> D
  M -. "unavailable" .-> E
  E -- "fail closed" --> D
  V -.-> L
  C -.-> L
  D -. "retry" .-> A
```

## In short

- **A rule kept by the agent it governs is hope.** It can be forgotten, misread, summarised away, or argued around by the agent's own reasoning.
- **The fix has two parts.** A second, independent reader, and a gate the drafting agent cannot skip because the harness, not the agent, runs it on the tool call.
- **Certain things go in code; only judgement goes to a model.** Signatures, dashes, key shapes, HTML and recipients are checked deterministically before any model is called.
- **The checker gets less than the author, on purpose.** No conversation history, no tools, ideally a different model: only the rules, the sources and the draft.
- **Anything but an explicit PASS is a FAIL.** Timeouts, errors and malformed answers all end with no draft. A late email is cheap; a wrong one cannot be taken back.
- **Its independence depends on where it is installed.** Today it is a setting the agent's own account could switch off. Under managed settings it becomes a boundary. Same code, different owner.
- **The pattern is old.** Banks call it segregation of duties, the military calls it the two-person rule, pharmacies call it an independent double check. It now has a precise shape for agents.

## Why the rule failed: hope held by the agent it governs

This is the general weakness of any behaviour policy that is held by the agent it governs. In [Hope or enforcement](hope-or-enforcement.md) I put it as "a rule the model keeps is an expectation: hope", and in [Every mistake added a rule](every-mistake-added-a-rule.md) I described how each failure tends to produce another paragraph of instructions. This failure is the case where the paragraph already existed four times.

There are three separate ways a self-held rule fails, and they need different fixes. The agent can **forget** it (the rule leaves the context). The agent can **not see** the violation (the author is the worst reader of its own text, and the research agrees: models "struggle to self-correct their responses without external feedback" ([Huang et al., ICLR 2024](https://arxiv.org/abs/2310.01798)), and LLM judges show "self-preference" for their own outputs ([Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076))). And the agent can **decide an exception applies**, persuaded by its own earlier reasoning in the same conversation. A reminder fixes only the first. A second reader with a fresh context fixes the second and third. A gate the agent cannot skip makes the fix hold.

## How the guard works

### The hook point

Claude Code raises an event before every tool call, including calls to MCP tools such as the Gmail connector and calls made by sub-agents. The guard registers on two of them:

```

on('tool.call', { tool: 'mcp__Gmail__create_draft' }, guard).catch(failClosed)
on('tool.call', { tool: 'mcp__Gmail__update_draft' }, guard).catch(failClosed)

```

This is Claude Code's [mods](https://code.claude.com/docs/en/plugins/mods/overview) system, which is public and on by default from v2.1.287: "`tool.call` fires when Claude Code is about to run a tool, including calls a subagent makes and calls to MCP tools" ([events](https://code.claude.com/docs/en/plugins/mods/events#guard-or-change-a-tool-call)). The hook either calls `next(e)`, and the draft is created, or returns `{ deny: "..." }`, and the tool never runs; the agent receives the deny text as the tool's error, so it knows what to fix. Since the event fires for sub-agents too, a sub-agent cannot route around the gate.

### Stage 1: code checks, no model

Some rules are certain and cheap. They run first, and a failure stops the call without spending a model call:

| Rule | Code check |
|---|---|
| R1 voice | For mail with a To: the body must carry the agent's signature line, and none of the three lines before it may be a sign-off in my name. Only the visible email is read, not the thread summary below it. |
| R3 format | For mail with a To: the branded HTML body must be present. |
| R4 dashes | No em or en dashes anywhere. |
| R5 secrets | No string shaped like a vault key, an API key, an AWS key, a GitHub token or a private key block. |
| R6 Cc | My addresses in the right place when others are in To. |

Internal drafts with no To, notes to me rather than emails to anyone else, skip the signature and HTML checks.

### Stage 2: the independent checker

If the code passes, the hook builds one prompt from three things: the rules (ten numbered rules, from voice and disclosure to claims, scope, attachments and private pages, with a fixed answer format: `RESULT: PASS or FAIL`, then one line per rule); the sources (the notes the draft may draw on, used only if written in the last 60 minutes, so stale notes from another email are not used); and the draft itself.

It sends that as a single `$.model.complete` call. The documentation is exact about what that call is: "`$.model.complete` sends your prompt on its own", with one user message, CLAUDE.md "Not included" and tools "None" ([API](https://code.claude.com/docs/en/plugins/mods/api#call-a-model)). So the checker:

- **has no conversation history.** It does not see the drafting agent's reasoning, its excuses, or the earlier messages that persuaded it an exception applied;
- **has no tools.** It can only read what it is given and answer;
- **runs a different model from the author.** The drafter runs on Opus; the checker on Sonnet. The two do not share every blind spot, and a model is not grading its own work.

The answer passes only if it says `RESULT: PASS` **and** no line says `R<n> FAIL`. A contradictory answer is a FAIL.

### Failing closed, and the log

This is the part most guards get wrong, and the documentation is candid about why: hooks fail **open** by default. A mod hook that throws "before calling `next`" is skipped, and "to make a hook that blocks calls fail closed, add a `.catch` error handler that answers in its place" ([events](https://code.claude.com/docs/en/plugins/mods/events#handle-a-hook-that-fails)). Settings hooks are the same: "a policy hook with a wrong path or a crashing script lets everything through", unless `"onFailure": "block"` is set ([hooks](https://code.claude.com/docs/en/hooks)). And a model call that fails does not throw: "A Claude API failure doesn't reject the call, so check `r.isAnswered`."

The guard closes every one of those doors. The checker is overloaded, errors, times out or returns nothing: deny, "checker unavailable". The hook throws: the `.catch(failClosed)` handler denies. The answer is not in the expected shape: no `RESULT: PASS` line, so FAIL. In the inbox agent's words: "An email that is late is a small cost. An email that goes out wrong cannot be taken back."

Every check appends one line to a log, which never decides the outcome:

```

{"ts":"2026-10-09T14:02:11Z","tool":"mcp__Gmail__create_draft","to":["recipient@example.com"],
 "contentHash":"9f2c1a07","verdict":"FAIL","stage":"model","model":"sonnet","sourcesGiven":true,
 "modelFails":["R7 FAIL: a proposal attributed to Dinis is not in the notes"],"ms":8412}

```

(The recipient and the claim are replaced here; the shape is the real one.) That is the audit trail: what was checked, by which model, against which sources, and why it failed.

## What the first run caught

The first run used Haiku as the checker. It caught four real invented claims: statements presented as my view, decision or promise that were not in anything I had said. It also flagged correct facts it had no source for, such as dates read from Gmail and an earlier note of mine that had not been copied into the sources file.

Both results are the design working. The false FAILs cost a retry, not a wrong email, and the fix the agent is told to apply is the right one: add the missing source, never remove the rule. And they are why the default checker became Sonnet: rule R7, are the claims in the sources, needs judgement, and the smaller model over-flagged. Haiku stays the choice for high-volume mechanical checks, after everything certain has gone into code.

The cost is small. At list prices read on 9 October 2026, Sonnet 5.5 is $2 per million input tokens and $10 per million output ([pricing](https://platform.claude.com/docs/en/about-claude/pricing)). At 5,000 to 10,000 tokens a draft and thirty drafts a day, that is roughly $12 to $21 a month; Haiku 5.5, at $0.10 and $0.50, is about a dollar. Thinking tokens or caching move those figures, not their order of magnitude.

## Six kinds of independence

"Independent" is doing a lot of work in the name, so it is worth taking apart. A second reader is only as independent as the things it does not share with the author, and there are six of them: three about what the checker sees, two about who decides whether it runs, and one about who wrote the evidence it checks against.

Six kinds of independence, and which check has which. The drafter re-reading its own draft has none; the guard as it runs today has four; the guard under managed settings, with sources written by someone else, has all six.

Two rows deserve a comment. The stopgap in the scheduled runs, where each drafting step is told to spawn a checker sub-agent before creating a draft, has a fresh context and a different model, but the drafter chooses whether to run it, so it is still an expectation. And the last column is the honest limit of the whole design: the checker compares claims with the sources it is given, and today the drafting agent writes the sources. An agent could pad them. The log records whether sources were given, so that is auditable, and the full fix is sources that come from somewhere else: my own notes, the CRM, the page being described.

## From setting to boundary: where the hook lives decides what it is

The guard was written by the inbox agent in its own session, and loading it took one click on this prompt:

The prompt that loaded the guard: "A mod is code Claude wrote; it runs with your permissions." Enabling hot reloading runs every mod Claude writes in this session, and picks up each later change.

That prompt is the honest centre of this story. The documentation describes it: Claude writes mods "in a directory of its own in the session's mods folder", and "when Claude saves the first file, Claude Code asks whether to enable hot reloading for the session" ([create a mod](https://code.claude.com/docs/en/plugins/mods/create#ask-claude-for-a-mod)). It also means the agent that is gated by the hook can edit the hook. In ABP terms that is a **setting**, "a switch the agent's own account can flip": far better than memory, because the harness runs it every time, but not yet a control.

The inbox agent's document proposes the next step: publish the plugin to a repository and install it from there, where the agent cannot write. The documentation says that is better and still not enough. A plugin installed from GitHub, git, a URL or npm is copied into the cache and "counts as a user's", and "a user's mod that approves tool calls can approve a call that an `ask` rule would prompt for, or that a `PreToolUse` hook outside managed settings blocked" ([mods for administrators](https://code.claude.com/docs/en/plugins/mods/admin)). Only managed placement is final: "`PreToolUse` hooks from managed settings: run before the first mod's `tool.call` hook, and a block from one of them is final, so no mod sees the call" ([events](https://code.claude.com/docs/en/plugins/mods/events#where-settings-hooks-run-in-the-order)). The alternative is an organisation mod from a directory on the machine that only an administrator can write, named in managed settings, with `allowManagedModsOnly` so that mods Claude writes in a session do not load.

Who enforces the voice rule, weakest first. The hook took it from expectation to setting; managed placement takes it to boundary, "enforced above the grant, out of the agent's reach". Nothing in the hook changes, only who can change the hook.

**The barrier ladder, Mermaid source**

[rendered image](images/ck-ladder.webp)

```
flowchart LR
  N["● none<br/>no rule about voice"]
  X["◉ expectation<br/>the rule, written in four places,<br/>kept by the drafting agent's memory<br/>9 Oct: two emails signed with<br/>the founder's name"]
  S1["◐ setting<br/>draft-guard as a mod in<br/>this session's folder<br/>runs on every call, sub-agents too<br/>but the agent can edit it"]
  S2["◐ setting, still<br/>installed as a plugin from a repository<br/>the agent cannot edit the file,<br/>but it counts as the user's,<br/>and its block is not final"]
  B["○ boundary<br/>a managed-settings hook, or an<br/>organisation mod from an admin-only folder,<br/>with Claude-written mods switched off<br/>its block is final"]
  N --> X -- "the hook" --> S1 -- "install it" --> S2 -- "manage it" --> B
  R["What still rests on judgement<br/>the checker can be wrong both ways<br/>and the sources are written by the drafter"]
  B -.-> R
  style X stroke:#C2410C,stroke-width:2px
  style B stroke:#0F766E,stroke-width:3px
```

The same placement question answers the second limit the agent listed: a fresh scheduled run starts in a fresh container, so a session mod is not there at all. A managed hook is there in every session, scheduled or not.

## Building it with what is public today

There are three ways to build the same guard with documented Claude Code features, and they trade simplicity against robustness:

| Route | Fresh model call | Reads a sources file | Fails closed | Notes |
|---|---|---|---|---|
| **A mod**, as built | `$.model.complete`: no history, no tools | yes | with `.catch` and a check of `r.isAnswered` | the hook's own run time is limited to 10 seconds, but time inside the model call does not count |
| **A command hook** on `PreToolUse` | the script calls the model itself | yes | with `"onFailure": "block"` and exit code 2 (exit 1 does not block) | the most robust public form; works in managed settings |
| **A prompt hook** (`"type": "prompt"`) | built in: "use an LLM to evaluate whether to allow or block an action" | no, the sources must be pasted into the prompt | not documented for model failures | answers in JSON, `{"ok": false, "reason": ...}`; set `model` explicitly |

The command hook is the one I would put under managed settings. It matches the Gmail tool by its exact name (MCP tools are named `mcp__<server>__<tool>`), runs the code checks and the model call in one script, exits 2 with the reasons on anything but an explicit PASS, and sets `onFailure` to `block` so a crash or a timeout stops the draft rather than waving it through ([hooks](https://code.claude.com/docs/en/hooks)). A minimal shape, with the path as a placeholder:

```

{
  "hooks": {
    "PreToolUse": [
      { "matcher": "mcp__Gmail__create_draft",
        "hooks": [ { "type": "command", "command": "/opt/guards/draft-guard", "onFailure": "block" } ] },
      { "matcher": "mcp__Gmail__update_draft",
        "hooks": [ { "type": "command", "command": "/opt/guards/draft-guard", "onFailure": "block" } ] }
    ]
  }
}

```

It is worth noticing that Anthropic ships the same pattern in the product. In auto mode, "a second model, the classifier, reviews actions instead of you", running on Sonnet by default, with tool results stripped "so hostile content in a file or web page can't manipulate the classifier directly", and when "the classifier's response doesn't parse, Claude Code denies the action" ([permission modes](https://code.claude.com/docs/en/permission-modes)). Same shape: a different model, less context, fail closed. The same page also warns that a boundary stated in conversation "can be lost if context compaction removes the message that stated it. For a hard guarantee, add a deny rule instead." That is the 9 October failure, described by the vendor.

## The pattern is old, and it has a name

What the inbox agent built is maker-checker, the oldest control in finance. The Basel Committee's 1998 framework put it as Principle 6: "An effective internal control system requires that there is appropriate segregation of duties and that personnel are not assigned conflicting responsibilities", noting that supervisors "typically find that one of the major causes of such losses is the lack of adequate segregation of duties" ([BCBS 40](https://www.bis.org/publ/bcbs40.pdf)). NIST defines separation of duty as the principle "that no user should be given enough privileges to misuse the system on their own", with the two-person rule as its example ([CSRC](https://csrc.nist.gov/glossary/term/separation_of_duty)). ISO/IEC 27001:2022 carries it as control A.5.3, segregation of duties. Hospital pharmacies run independent double checks for high-alert medicines, and the reason given is the one that matters here: if the same person prepares and checks, "they likely will see only what they expect to see, even if an error has occurred" ([ISMP](https://home.ecri.org/blogs/ismp-alerts-and-articles-library/independent-double-checks-worth-the-effort-if-used-judiciously-and-properly)).

The AI versions of the idea are recent and well described. Redwood Research's [AI Control](https://arxiv.org/abs/2312.06942) work (ICML 2024) studies exactly this arrangement, a powerful untrusted model watched by "a less powerful trusted model", with protocols such as trusted monitoring and trusted editing. Simon Willison's [Dual LLM pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) (2023) and Google DeepMind's [CaMeL](https://arxiv.org/abs/2503.18813) (2025) separate a model that acts from one that reads, against prompt injection. Meta's [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (2025) says an agent that processes untrusted input, touches private data and communicates externally, as an email drafter does, "should not be permitted to operate autonomously and at a minimum requires supervision". And OWASP's [LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) asks for authorisation "in downstream systems rather than relying on an LLM to decide if an action is allowed". Output-checking products exist too: [Llama Guard](https://arxiv.org/abs/2312.06674), [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/colang/colang-1/tutorials/5-output-rails) output rails, [Guardrails AI](https://www.guardrailsai.com/docs) validators, and the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/) tool guardrails.

What the draft guard adds is not a new idea. It is the idea placed exactly where it bites: on the one tool call with consequences, with business rules rather than safety categories, sources to check claims against, a model that differs from the author, and an explicit statement of which barrier it is.

## The pattern, reusable

A hook on a consequential tool call, code checks first, then a fresh model call with only the rules, the evidence and the proposed action, failing closed and logging every verdict.

**The reusable pattern, Mermaid source**

[rendered image](images/ck-pattern.webp)

```
flowchart LR
  subgraph T["Pick the consequential tool call"]
    direction TB
    t1["send or draft mail"]
    t2["write to the CRM"]
    t3["publish a page"]
    t4["push to a vault"]
    t5["post to Slack"]
    t6["call a payment API"]
  end
  K["Code checks first<br/>everything that is certain:<br/>formats, key shapes, recipients"]
  J["A fresh checker<br/>only the rules, the evidence<br/>and the proposed action<br/>no history, no tools,<br/>ideally a different model"]
  Q{"explicit PASS?"}
  Y["the call runs"]
  Z["deny, with reasons"]
  LG[("log every verdict")]
  T --> K --> J --> Q
  Q -- "yes" --> Y
  Q -- "anything else" --> Z
  K -- "fail" --> Z
  Q -.-> LG
```

In six steps, as the inbox agent wrote them:

1. **Pick the tool call that matters**: sending a Slack message, writing to the CRM, publishing a page, committing to a vault, a payment API.
2. **Write the rules as a short numbered checklist** with a fixed answer format.
3. **Put everything certain into code first**; leave only judgement to the model.
4. **Give the checker only what it needs**: rules, sources, the proposed action. No history.
5. **Deny on anything other than an explicit PASS.**
6. **Log every verdict.**

The next candidates in our own team are the CRM agent's writes (no keys, no unverified facts presented as verified), the newsroom's page promotions (nothing indexed until I promote it; quotes are claims), Slack posts, and the leak check before any vault push, which on this site is still a script I run rather than a gate I cannot skip.

## What it does not do

- **It is only as independent as its installation**, as above. Today it is a setting.
- **R7 is only as good as the sources**, and the drafter writes them.
- **The checker can be wrong in both directions.** Expect false FAILs; they cost a retry.
- **It checks drafts, not sending.** I send. The rule that agents never send is enforced separately, and is a different barrier question.
- **It does not replace reading.** A PASS means ten rules held, not that the email is good.

The mistake on 9 October cost two emails I would rather not have sent. What it bought is better: a rule that used to live in four paragraphs now lives on the tool call, with a log, and a clear statement of the one step left before it is a control.

*From the design document "The independent checker: a hook that makes a second model approve every email draft", version 0.1, written on 9 October 2026 by the RiskMandate.ai inbox agent, which built and tested the guard (11 of 11 tests passing). Researched, illustrated and written up for this site by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, for Dinis Cruz, who has editorial responsibility. Claude Code behaviour is quoted from its documentation as read on 9 October 2026; prices are list prices on that date.*

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#a-second-reader-the-agent-cannot-skip)

### Builds on

- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.

### Continued by

- [Who owns the words: agents can make decisions, but they cannot hold responsibility](who-owns-the-words.md) Agents in loops make real decisions, but responsibility stays with whoever granted the reach; disclosure is a label, not a team to manage.
- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 55 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=55)

**Posting this article on LinkedIn?** The cover is [a-second-reader-the-agent-cannot-skip.jpg](banners/a-second-reader-the-agent-cannot-skip.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-second-reader-the-agent-cannot-skip.html)*
