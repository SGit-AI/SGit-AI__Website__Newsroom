# The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says, sgit.ai

> The third piece on Mondweep Chakravorty's SGit × Ruflo proof of concept is about a path, not a failure. His adapter compiles the four Agent Behaviour Policy rows into Ruflo rules and checks every one of its tools with a pinned copy of Ruflo's own policy evaluator, in enforce mode. In the video those checks cover steps 4, 5, 6, 8 and 11, and every one behaved as the policy said. But in steps 3, 9 and 10, Ruflo's own command line writes and reads the same SQLite memory file directly, and that path does not pass the gate. His README states the limit in one line: "Only adapter tools pass through this gate. Other shell/network tools are unaffected." It is the same lesson this site keeps learning about its own agent: a policy holds only on the paths that pass through its enforcer. The fix is on his list of follow-ups, native plugin registration, so the same compiled rules run where Ruflo runs. His code also answers the other questions the video left open: why every error reads the same, whether decisions are recorded, where the vault goes next, why the file name changes, and why approval means stop.

*Source: <https://newsroom.sgit.ai/articles/the-policy-guards-the-door.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says

# The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.1.0, 2 versions](versions/the-policy-guards-the-door.md) · [newsroom v0.12.90](https://newsroom.sgit.ai/admin/versions.html) · agentsruflosgitagent-behaviour-policysecuritymcpenforcementmemoryvideoarticle

***Abstract:** The third piece on Mondweep Chakravorty's SGit × Ruflo proof of concept is about a path, not a failure. His adapter compiles the four Agent Behaviour Policy rows into Ruflo rules and checks every one of its tools with a pinned copy of Ruflo's own policy evaluator, in enforce mode. In the video those checks cover steps 4, 5, 6, 8 and 11, and every one behaved as the policy said. But in steps 3, 9 and 10, Ruflo's own command line writes and reads the same SQLite memory file directly, and that path does not pass the gate. His README states the limit in one line: "Only adapter tools pass through this gate. Other shell/network tools are unaffected." It is the same lesson this site keeps learning about its own agent: a policy holds only on the paths that pass through its enforcer. The fix is on his list of follow-ups, native plugin registration, so the same compiled rules run where Ruflo runs. His code also answers the other questions the video left open: why every error reads the same, whether decisions are recorded, where the vault goes next, why the file name changes, and why approval means stop.*

Two ways into the same memory: the adapter's tools pass the policy gate, a pinned copy of Ruflo's evaluator running the compiled ABP rules, on their way to SGit and the vault, in steps 4, 5, 6, 8 and 11; Ruflo's own command line reads and writes the memory file directly, in steps 3, 9 and 10, with no ABP check. The author states this limit in his README.

SGit × Ruflo: one run, four ways in

Mondweep Chakravorty's video of an agent losing its workspace and getting its memory back: the run, the architecture, the gap, and a page to step through it yourself.

[1 · The runWhat if an agent loses its workspace?Twelve steps: memory saved, project deleted, memory restored in a fresh process, three safeguards tested.](what-if-an-agent-loses-its-workspace.md)[2 · The architectureWhen is the vault actually used?In three of twelve steps, on one machine, inside the adapter: what that proves and what it does not.](when-is-the-vault-actually-used.md)[you are here3 · The gapThe policy guards the door; the command line uses the windowThe ABP checks the adapter's tools; Ruflo's own command line reaches the same memory file without it.](the-policy-guards-the-door.md)

4 · Step through itSGit × Ruflo, step by stepEvery step with its frame, command, output and diagram, linked to its moment in the video.[Watch the video ↗](https://youtu.be/rkh6BJiaIrQ)[Step through it](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html)[Read the code ↗](https://github.com/mondweep/sgit-ruv-memory)

## In short

- **The rules run in Ruflo's own evaluator.** Compiled from the ABP, checked in enforce mode, inside the adapter.
- **Every guarded step behaved.** Steps 4, 5, 6, 8 and 11 did exactly what the policy said.
- **Two paths reach the memory.** The adapter's tools, through the gate; Ruflo's command line, around it.
- **The author says so himself.** "Only adapter tools pass through this gate."
- **A policy holds on the paths through its enforcer.** It is the lesson this site keeps learning about its own agent.
- **The fix is on his list.** Native plugin registration, so the rules run where Ruflo runs.
- **The other questions have answers.** In the code: the errors, the records, the vault's next home, the file name, approval.

## Two paths to the same memory

The run has two ways into Ruflo's memory file, and the [matrix in the architecture piece](when-is-the-vault-actually-used.md) shows them side by side.

The first is the adapter. Mondweep's code, [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), compiles the four ABP rows into Ruflo rules when the server starts, and before each of its tools runs, `checkpoint`, `inspect`, `restore` and `close_run`, it asks a pinned copy of Ruflo's own policy evaluator for a decision in enforce mode. Anything not allowed is refused, and an unsupported or ambiguous policy rejects the whole document. That is the path for steps 4, 5, 6, 8 and 11, and every one of them did what the policy said: the out-of-scope checkpoint refused, the in-scope one allowed, the deletion stopped, the restore allowed, and the tampered restore allowed by the policy and then refused by the adapter's integrity check.

The second is Ruflo's own command line. In step 3 it writes the two facts straight into the SQLite memory file. In steps 9 and 10 it reads the restored file. None of those calls passes the gate. The analysis put it as "The ABP guards the adapter, but Ruflo's command-line tool writes and reads the same SQLite file without passing through it", and Mondweep's README says the same in his own words: "This is an external adapter using a pinned copy of Ruflo's evaluator, not Ruflo's running policy state. Only adapter tools pass through this gate. Other shell/network tools are unaffected."

## What the screen shows, and what it does not

Step 3: the test script calls the ruflo command line's memory store, which loads its embedding model, stores no vectors, and writes two rows of plain text into the source workspace's memory.db; the ABP adapter and the vault are not on this path.

**Shown on screen:** in step 3, `ruflo memory store` with `--no-embedding --path memory.db`, "[OK] Data stored", and "Vector: No". At this point the memory file is ordinary, unencrypted SQLite.

Step 9: the ruflo command line's memory retrieve reads memory.sqlite in the fresh-runner workspace and returns both facts exactly; the vault and the ABP adapter are not on this path.

**Shown on screen:** in step 9, `ruflo memory retrieve` reading `memory.sqlite`, both values printed, and a pass. Ruflo reads a plain copy that came out of the vault; neither the vault nor the ABP is on this path.

**Not tested:** what an agent with shell access would do with the same command line, or with any SQLite client. The code confirms the path exists; nobody tried to misuse it, and it was not the run's question.

To be fair to the run: using the command line in steps 3 and 9 is what makes it convincing. Step 9 is strong precisely because Ruflo itself, not the adapter, reads the facts back. The gap is not a mistake in the test. It is a property of where this ABP is enforced, and the author documents it.

## Why this matters beyond this run

A policy holds on the paths that pass through its enforcer, and nowhere else. I keep relearning that about this site's own agent. When I measured it in [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md), ten of its eleven rules were kept by the agent choosing to follow them, and the one hard limit was a platform setting the policy did not even list.

At [The AI Conference](the-ai-conference-read-for-governance.md), speaker after speaker said policy must live outside the model. This run does that, and better than most: the ABP is compiled, strictly, into the rule format of the tool it governs, evaluated by that tool's own evaluator, and it fails closed. What it adds is the next lesson. Outside the model is necessary; around every path to the data is the harder part.

## How it could close

The rules are already in Ruflo's format and already checked by Ruflo's evaluator. What is missing is running them where Ruflo itself runs, so the command line's memory calls are checked too. Mondweep's README lists it among the follow-ups: "native plugin registration", alongside remote sync, key rotation and multi-tenant isolation.

Two other ways come to mind, and I offer them as ideas, not findings. Keep the working memory file somewhere only the adapter can reach, so the command line has to go through it. Or make the adapter the only thing that can decrypt memory at all, so a plain file never sits in a workspace an agent can write to. His README is candid that "Plaintext exists during staging and intentionally in restored workspaces", which is the trade that makes step 9 possible. Each option has costs, and he will know better than I do which fits Ruflo.

## The other questions, and the answers in the code

The video left five smaller questions open. The repository answers each of them.

1. **Why does every error read the same?** On purpose. The server replaces the detail with "operation failed; check configuration, policy and integrity", with a comment: "Do not leak dependency errors containing private paths or credentials." Inside, the gate's own message names the reason: "Policy blocked operation", followed by the evaluator's reason.
2. **Is each decision recorded?** Not yet. The evaluator returns a decision for every call; nothing writes it to a log. An operator log naming the row that fired would turn each decision into evidence.
3. **Where does the vault go next?** Nowhere yet: "no remote push is performed", and remote sync is a follow-up. Each checkpoint is its own SGit vault on the same machine. [The architecture piece](when-is-the-vault-actually-used.md#where) says what a second machine would add.
4. **Why `memory.db`, then `memory.sqlite`?** The adapter stages and restores every checkpoint as `memory.sqlite`, whatever the source file was called.
5. **Why does approval mean stop?** Because there is nothing yet to give approval with. The README: "There is no human approval fulfilment mechanism yet." The policy file records it in the row's own barrier: "Human approval is required; MVP blocks this operation". The run proves the row blocks; proving it releases with a named approver is the next test.

And one note on the video, not the run: the terminal is labelled a real-time capture, and between step 2 at run clock 00:11 and the first fact in step 3 at 00:39, 28 seconds of run pass in a few seconds of video. One wait was trimmed, most likely Ruflo loading its model. That is fine for a demo, and worth a caption.

## Where to go next

Back to [the walkthrough](what-if-an-agent-loses-its-workspace.md) for the run in order, or to [the architecture](when-is-the-vault-actually-used.md) for when the vault is used. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html): steps 3, 9 and 10 each link back here, and every step shows what the code confirms.

## What this does not claim

- **Not a vulnerability report.** No one tried to bypass the policy; the author documents the path himself.
- **Not that the run failed.** Every step the policy guarded behaved as written.
- **The fixes are ideas.** Native plugin registration is his follow-up; the other two are mine, untested.
- **The code was read, not run, here.** Its tests and evidence are the author's.

If you are Mondweep, or anyone who has run this, and want to add to any of these, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation; this analysis is published with his agreement. The code: [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, read at its commit of 16 October 2026: the README, `sgit_ruv_memory/core.py`, `server.py`, `abp.py`, `policy/bridge.mjs` and `examples/memory.abp.json`. The analysis and its architecture addendum: Claude (Anthropic), 17 October 2026, made for me from on-screen content; written up and checked against the video's timeline and the code by this site's agent; the editorial responsibility is mine. Ruflo: [ruvnet/ruflo](https://github.com/ruvnet/ruflo), MIT. Related: [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md), [The AI Conference 2026, read for agent governance](the-ai-conference-read-for-governance.md), [a policy beside the prompt](a-policy-beside-the-prompt.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-policy-guards-the-door)

### Builds on

- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [Your agent's logs are a self-report: an answer to a GRC adviser's post on The AI Conference, with this site's own agent as the worked example, including the two commits its own counter got wrong](your-agents-logs-are-a-self-report.md) An answer to a GRC adviser's post: why an agent's logs are a self-report, and this site's agent measured, including two commits its own counter got wrong.
- [The AI Conference 2026, read for agent governance: six claims traced, five disagreements, and what the speaker notes say that the slides do not](the-ai-conference-read-for-governance.md) Six claims from a post about The AI Conference traced to the slides, five open disagreements, and the best fact-check, in a speaker's notes.
- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.

### Continued by

- [When is the vault actually used? In Mondweep Chakravorty's SGit × Ruflo run, the encrypted vault is written or read in three steps of twelve, on one machine, inside the adapter, and why that is the honest shape of a recovery copy](when-is-the-vault-actually-used.md) In the SGit × Ruflo run the vault is written or read in three steps of twelve, on one machine, inside the adapter: the right shape for a recovery copy.
- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 163 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=163)

**Posting this article on LinkedIn?** The cover is [the-policy-guards-the-door.jpg](banners/the-policy-guards-the-door.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-policy-guards-the-door.html)*
