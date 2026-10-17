# The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP checks the adapter's tools, while Ruflo's own command line reaches the same memory file without it, and five other questions for the author, sgit.ai

> The third piece on Mondweep Chakravorty's SGit × Ruflo proof of concept is about a path, not a failure. The Agent Behaviour Policy in the run is enforced by the adapter, on its three tools: checkpoint, close run and restore. Those are steps 4, 5, 6, 8 and 11, and every one of them behaved as the policy said. But in steps 3, 9 and 10, Ruflo's own command line writes and reads the same SQLite memory file directly, and that path does not pass the policy gate. On screen this is simply how the test was built. By inference, an agent with shell access could change its memory without an ABP check. It is the same lesson this site keeps learning about its own agent: a policy holds only on the paths that pass through its enforcer. The addendum suggests compiling the rows into Ruflo's own policy engine in enforce mode, so the command line is covered too. Alongside it are five smaller questions from the analysis: whether each decision is recorded, the same error text for different causes, where the vault goes after this machine, a file name that changes between steps, and an approval path that was not tested with an approver. They are questions, not findings, and Mondweep has agreed to their publication.

*Source: <https://newsroom.sgit.ai/articles/the-policy-guards-the-door.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP checks the adapter's tools, while Ruflo's own command line reaches the same memory file without it, and five other questions for the author

# The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP checks the adapter's tools, while Ruflo's own command line reaches the same memory file without it, and five other questions for the author

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.0.0](versions/the-policy-guards-the-door.md) · [newsroom v0.12.89](https://newsroom.sgit.ai/admin/versions.html) · agentsruflosgitagent-behaviour-policysecuritymcpenforcementmemoryvideoarticle

***Abstract:** The third piece on Mondweep Chakravorty's SGit × Ruflo proof of concept is about a path, not a failure. The Agent Behaviour Policy in the run is enforced by the adapter, on its three tools: checkpoint, close run and restore. Those are steps 4, 5, 6, 8 and 11, and every one of them behaved as the policy said. But in steps 3, 9 and 10, Ruflo's own command line writes and reads the same SQLite memory file directly, and that path does not pass the policy gate. On screen this is simply how the test was built. By inference, an agent with shell access could change its memory without an ABP check. It is the same lesson this site keeps learning about its own agent: a policy holds only on the paths that pass through its enforcer. The addendum suggests compiling the rows into Ruflo's own policy engine in enforce mode, so the command line is covered too. Alongside it are five smaller questions from the analysis: whether each decision is recorded, the same error text for different causes, where the vault goes after this machine, a file name that changes between steps, and an approval path that was not tested with an approver. They are questions, not findings, and Mondweep has agreed to their publication.*

Two ways into the same memory: the adapter's tools pass the ABP's policy gate on their way to SGit and the vault, in steps 4, 5, 6, 8 and 11; Ruflo's own command line reads and writes the memory file directly, in steps 3, 9 and 10, with no ABP check. Solid arrows are shown on screen; that an agent could use the second path is an inference.

SGit × Ruflo: one run, four ways in

Mondweep Chakravorty's video of an agent losing its workspace and getting its memory back: the run, the architecture, the gap, and a page to step through it yourself.

[1 · The runWhat if an agent loses its workspace?Twelve steps: memory saved, project deleted, memory restored in a fresh process, three safeguards tested.](what-if-an-agent-loses-its-workspace.md)[2 · The architectureWhen is the vault actually used?In three of twelve steps, on one machine, inside the adapter: what that proves and what it does not.](when-is-the-vault-actually-used.md)[you are here3 · The gapThe policy guards the door; the command line uses the windowThe ABP checks the adapter's tools; Ruflo's own command line reaches the same memory file without it.](the-policy-guards-the-door.md)

4 · Step through itSGit × Ruflo, step by stepEvery step with its frame, command, output and diagram, linked to its moment in the video.[Watch the video ↗](https://youtu.be/rkh6BJiaIrQ)[Step through it](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html)

## In short

- **Every guarded step behaved.** Steps 4, 5, 6, 8 and 11 did exactly what the policy said.
- **Two paths reach the memory.** The adapter's tools, through the ABP; Ruflo's command line, around it.
- **On screen, that is the test's design.** By inference, an agent with a shell could take the second path.
- **A policy holds on the paths through its enforcer.** It is the lesson this site keeps learning about its own agent.
- **One fix is suggested.** Compile the rows into Ruflo's own policy engine, in enforce mode.
- **Five smaller questions.** Records, error text, the vault's next home, a file name, the approval path.
- **Questions, not findings.** Mondweep agreed to publish them, and his answers are welcome here.

## Two paths to the same memory

The run has two ways into Ruflo's memory file, and the [matrix in the architecture piece](when-is-the-vault-actually-used.md) shows them side by side.

The first is the adapter. Its three tools, `checkpoint`, `close_run` and `restore`, each pass a policy gate built from the four ABP rows, and the gate fails closed. That is the path for steps 4, 5, 6, 8 and 11, and every one of them did what the policy said: the out-of-scope checkpoint refused, the in-scope one allowed, the deletion stopped for want of approval, the restore allowed, and the tampered restore allowed by the policy and then rejected by the vault.

The second is Ruflo's own command line. In step 3 it writes the two facts straight into the SQLite memory file. In steps 9 and 10 it reads the restored file. None of those calls passes the gate. In the addendum's words: "The ABP guards the adapter, but Ruflo's command-line tool writes and reads the same SQLite file without passing through it."

## What the screen shows, and what it does not

Step 3: the test script calls the ruflo command line's memory store, which loads its embedding model, stores no vectors, and writes two rows of plain text into the source workspace's memory.db; the ABP adapter and the vault are not on this path.

**Shown on screen:** in step 3, `ruflo memory store` with `--no-embedding --path memory.db`, "[OK] Data stored", and "Vector: No". At this point the memory file is ordinary, unencrypted SQLite.

Step 9: the ruflo command line's memory retrieve reads memory.sqlite in the fresh-runner workspace and returns both facts exactly; the vault and the ABP adapter are not on this path.

**Shown on screen:** in step 9, `ruflo memory retrieve` reading `memory.sqlite`, both values printed, and a pass. Ruflo reads a plain copy that came out of the vault; neither the vault nor the ABP is on this path.

**Inferred, not shown:** that an agent with shell access could use the same command line, or any SQLite client, to change its memory without an ABP check. The test does not try it, and it was not the test's question. It is the question I would ask next.

To be fair to the run: using the command line in steps 3 and 9 is what makes it convincing. Step 9 is strong precisely because Ruflo itself, not the adapter, reads the facts back. The gap is not a mistake in the test. It is a property of where this ABP is enforced.

## Why this matters beyond this run

A policy holds on the paths that pass through its enforcer, and nowhere else. I keep relearning that about this site's own agent. When I measured it in [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md), ten of its eleven rules were kept by the agent choosing to follow them, and the one hard limit was a platform setting the policy did not even list.

At [The AI Conference](the-ai-conference-read-for-governance.md), speaker after speaker said policy must live outside the model. This run does that: the gate is code, it fails closed, and it held. What it adds is the next lesson. Outside the model is necessary; around every path to the data is the harder part.

## How it could close

The addendum suggests one way: compile the ABP rows into Ruflo's own policy engine, in enforce mode, so the command line's memory calls are checked too. The engine exists in Ruflo; it was not used in this run.

Two other ways come to mind, and I offer them as ideas, not findings. Keep the working memory file somewhere only the adapter can reach, so the command line has to go through it. Or make the adapter the only thing that can decrypt memory at all, so a plain file never sits in a workspace an agent can write to. Each has costs, and Mondweep will know better than I do which fits Ruflo.

## Five more questions for the author

The analysis raised these alongside the gap. They are questions, not findings.

1. **Is each decision recorded?** The ABP is enforced by a custom local adapter. Does it keep a record of each allow and deny, and which row fired?
2. **Same message, different causes.** The scope denial and the approval stop both read "PermissionError: operation failed; check configuration, policy and integrity", and the tamper reads the same text as a ValueError. Uniform messages avoid leaking detail; an operator log naming the row would help.
3. **Where does the vault go next?** The checkpoint store is SGit objects on the same machine. A push to a vault server, a clone on another machine, and a check that the server holds only ciphertext would close the loop, as [the architecture piece](when-is-the-vault-actually-used.md#where) argues.
4. **`memory.db` and `memory.sqlite`.** Step 3 stores with `--path memory.db`; step 9 reads `--path memory.sqlite`. Probably the restore writes under a new name; one line would explain it.
5. **The approval path, with an approver.** Deletion is blocked without approval. Showing it succeed with a named approver would prove the row is approval, not simply no.

And one note on the video, not the run: the terminal is labelled a real-time capture, and between step 2 at run clock 00:11 and the first fact in step 3 at 00:39, 28 seconds of run pass in a few seconds of video. One wait was trimmed, most likely Ruflo loading its model. That is fine for a demo, and worth a caption.

## Where to go next

Back to [the walkthrough](what-if-an-agent-loses-its-workspace.md) for the run in order, or to [the architecture](when-is-the-vault-actually-used.md) for when the vault is used. Or [step through the run](https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html): steps 3, 9 and 10 each link back here.

## What this does not claim

- **Not a vulnerability report.** No one tried to bypass the policy; the second path is inferred from the design.
- **Not that the run failed.** Every step the policy guarded behaved as written.
- **The fixes are ideas.** The addendum's suggestion and mine are untested here.
- **From the screen only.** The audio was not transcribed; the author may already address some of these.

If you are Mondweep, or anyone who has run this, and have an answer to any of these, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai) and it will be added here.

## Where this comes from

The video: Mondweep Chakravorty, [SGit × Ruflo | Working Proof of Concept](https://youtu.be/rkh6BJiaIrQ), published on YouTube on 17 October 2026, made as a member of the #Ruflo-Federation; this analysis and its questions are published with his agreement. The analysis and its architecture addendum: Claude (Anthropic), 17 October 2026, made for me from on-screen content only; written up and checked against the video's timeline by this site's agent; the editorial responsibility is mine. Ruflo: [ruvnet/ruflo](https://github.com/ruvnet/ruflo), MIT. Related: [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md), [The AI Conference 2026, read for agent governance](the-ai-conference-read-for-governance.md), [a policy beside the prompt](a-policy-beside-the-prompt.md).

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
