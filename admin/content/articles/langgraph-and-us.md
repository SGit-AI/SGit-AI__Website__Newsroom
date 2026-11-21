---
title: LangGraph and us: how the way we build agent pipelines maps to LangChain, LangGraph, LangSmith and the agent testing toolkits, what is the same, what we do differently, code for each function and every step saved to a vault, what we can learn from them, and where they could run inside our own pipelines
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: A lot of what we do maps to LangGraph and LangChain, and I wanted to see how much. LangGraph's state is our vault; its nodes are our agents and our plain code; its checkpoints and time travel are sgit's history; its interrupts are our protected environments and reviewers' verdicts; its middleware is our behaviour policies; LangSmith's traces and evaluations are our signed commits, call ledgers and evals. The ideas are the same. The default is different. We write specific code for specific functions, load, extract, transform and save, and use a model only where judgement is needed; we store everything at every stage, raw and curated, in vaults others can read; and we score in code wherever we can. That gives us more determinism, more control and less black magic, and it is what let the PHP desk, PrompTugal and the Swarm scale. But they have learnt things we should take: one readable definition of the graph, interrupts as a first-class part of the runtime, versioned datasets pinned in CI, and a common trace format. And where a tool is good, we should use it inside our pipeline: Inspect and promptfoo for evals and red teaming, OpenTelemetry for traces, and LangGraph itself where a customer already runs it, with its checkpoints saved to a vault.
version: v0.14.192
license: https://creativecommons.org/licenses/by/4.0/
tags: langgraph, langchain, evals, agents, determinism, vaults, article
status: published
---

!shot lg-map.webp | images/ | LangGraph's concepts and ours: the same ideas, with a different default. | concept

## In short {#in-short}

- **What we do maps to LangGraph closely:** state, nodes, edges, checkpoints, interrupts, traces, evals.
- **The default is different:** code for each function, a model only where judgement is needed.
- **We save every step to a vault,** raw and curated, signed, readable by others.
- **We can learn from them:** a readable graph, first-class interrupts, pinned datasets, a common trace format.
- **We should use the good tools inside our pipelines,** not replace the pipeline with them.

## The landscape today {#landscape}

LangGraph describes itself as a "low-level orchestration framework for building stateful agents" ([its repository](https://github.com/langchain-ai/langgraph)); it reached 1.0 in October 2025 and is at 1.2.24 today, under the MIT licence. LangChain, also MIT and now at 1.5, builds agents on top of it with `create_agent`, whose middleware hooks are, in its own words, the defining feature ([LangChain v1](https://docs.langchain.com/oss/python/releases/langchain-v1)). LangSmith adds tracing, datasets and evaluations, from a free developer plan to 39 dollars a seat a month ([pricing](https://www.langchain.com/pricing)), and hosts graphs as LangSmith Deployment. Around them: the OpenAI Agents SDK, CrewAI, Google's ADK, Pydantic AI, the Claude Agent SDK, and Microsoft's Agent Framework, which reached 1.0 in April and replaces AutoGen and Semantic Kernel ([Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx)).

## How we map {#mapping}

- **State is a vault.** A `StateGraph` passes a shared state between nodes. Our state is files in a vault: versioned, encrypted, committed at every step ([one vault, ten agents](/articles/one-vault-ten-agents.html)).
- **Nodes are agents and code.** Some of our nodes are agents with behaviour policies. Many are plain code: load, extract, transform, save.
- **Edges are a conductor, lanes and a board.** Often a fixed chain, the researcher to the curator to the journalist; sometimes a conductor handing out work through append lanes ([who hands out the work](/articles/who-hands-out-the-work.html)).
- **Checkpoints and time travel are sgit's history.** LangGraph saves a snapshot per thread to a database ([persistence](https://docs.langchain.com/oss/python/langgraph/persistence)). We commit every intermediate result, signed by the agent that made it.
- **Interrupts are our gates.** A protected environment waits for a person's approval; a reviewer gives every draft one verdict, Ready, Fix first or Hold ([PrompTugal.news](/articles/promptugal-news-the-newsroom-we-ran.html)).
- **Middleware is our behaviour policies,** and the harness that enforces them around an agent ([feature behaviour policies](/articles/feature-behaviour-policies.html)).
- **LangSmith's traces are our signed commits and ledgers.** The Swarm records every model call, storing the text only as its length and hash ([the swarm](/articles/the-swarm-one-real-run-at-a-time.html)).
- **Datasets and evaluators are our evals,** scored in code and rescored from stored outputs when a check is wrong ([one night on Mistral](/articles/one-night-on-mistral.html)).

## Where we differ {#different}

The ideas are the same. What differs is the default, and that is where most of our determinism comes from.

- **Specific code for specific functions.** A model is not asked to do what code can do. It reads, judges and writes; code fetches, parses, counts, compares and checks. In the X-ray, a model lists a page's claims, but code gives each claim its verdict.
- **Everything stored, at every stage.** The PHP desk ran as a chain: a researcher captured pages, raw, into one vault; a curator promoted what held into a second; a journalist updated the site from that ([almost working](/articles/almost-working.html)). Every input, every transformation and every output is still there to read, replay or audit. Capture first, then think ([capture first](/articles/capture-first.html)).
- **State others can read.** A LangGraph checkpoint lives in the application's database. A vault moves: it can be handed to another team, another pipeline or an auditor, with a key ([any data with any data](/articles/any-data-with-any-data.html)).
- **Identity on every step.** Every agent commits with its own key, so the record says who did what, not only what happened.

That is what let these pipelines scale from one article to the PHP story, to PrompTugal's 73 articles in ten days, to the Swarm. Less black magic: when something is wrong, the step, its input and its author are all on file.

None of this is impossible in LangGraph, which is low-level and can be as deterministic as you make it. The difference is the habit, not the library.

## What we can learn from them {#learn}

- **One readable definition of the graph.** Our flows are spread across schedules, lanes and policies. A single file that declares the nodes and edges, as a `StateGraph` does, would make each pipeline easier to see and review.
- **Interrupts as part of the runtime.** LangGraph makes pausing for a person a feature of the graph, resumable from the checkpoint. Ours are spread across GitHub environments and reviewer agents.
- **Versioned datasets, pinned in CI.** LangSmith's guidance is to pin the dataset version an evaluation runs on ([evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)). Our evals are small and recorded, but not yet a pinned suite every release runs.
- **A common trace format.** OpenTelemetry's GenAI conventions define spans for agents, model calls and tools ([agent spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/)), still marked as in development. If our ledgers spoke that format, any tracing tool could read them.
- **Simulated users.** τ²-bench tests agents in conversations where a simulated user acts too ([tau2-bench](https://github.com/sierra-research/tau2-bench)). That is how we should test the site's message channel and the career interview.

## Should we use them? {#use}

Yes, inside our pipeline, where each is good, and with its results saved to a vault like everything else:

- **Inspect for evals.** The UK AI Security Institute's toolkit, MIT, with datasets, solvers, scorers, sandboxes and a log viewer, and it can run external agents such as Claude Code ([Inspect](https://inspect.aisi.org.uk/)). Our Mistral evals would port to it naturally.
- **promptfoo for red teaming,** MIT and built for CI ([promptfoo](https://github.com/promptfoo/promptfoo)): the injection lab's scam note, and attacks on behaviour policies, run on every release. OpenAI announced in March that it is acquiring promptfoo and that it stays open source ([announcement](https://openai.com/index/openai-to-acquire-promptfoo/)).
- **Langfuse for traces,** MIT at its core and self-hostable ([Langfuse](https://langfuse.com/blog/joining-clickhouse)), fed from our ledgers once they speak OpenTelemetry.
- **LangGraph where a customer already runs it.** A cell installed in a customer's environment should work with the framework they have. The natural bridge is a checkpointer that saves LangGraph's state to an sgit vault, so their graph gets our history, signing and portability. That is a proposal; nobody has built it yet.
- **An open comparison.** The same brief through our pipeline and through a LangGraph version, side by side, with time, cost and the record each leaves, as the Mistral site did with five models.

What I would not do is put a framework at the centre and our pipeline around it. The centre is the data and its history; frameworks are tools that read and write it.

## The criticism, fairly {#criticism}

LangChain was criticised early for abstractions on abstractions that made simple things complex and debugging hard ([Max Woolf, 2023](https://minimaxir.com/2023/07/langchain-problem/); [Octomind, 2024](https://octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents)), and Anthropic's own guidance is to start with direct calls to the model ([building effective agents](https://www.anthropic.com/engineering/building-effective-agents)). Most of that criticism predates version 1, which promised no breaking changes until 2.0 and made the agent loop explicit with middleware ([releases](https://docs.langchain.com/oss/python/releases-v1)). LangChain's own answer is that LangGraph has no hidden prompts ([how to think about agent frameworks](https://blog.langchain.com/how-to-think-about-agent-frameworks)). Both are fair. It is also why we use them as tools, not foundations.

## What this does not claim {#limits}

- **We have not run LangGraph, Inspect or promptfoo in our pipelines yet;** the proposals above are to be tested.
- **Versions and prices are as read on 21 November 2026.**
- **The mapping is ours;** LangGraph's own features go beyond what is listed here.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026; the projects' own documentation, repositories and package records, read that day and linked above; and our earlier articles on how our pipelines work. Related: [almost working](/articles/almost-working.html), [capture first](/articles/capture-first.html), [one vault, ten agents](/articles/one-vault-ten-agents.html), [the swarm, one real run at a time](/articles/the-swarm-one-real-run-at-a-time.html), [one night on Mistral](/articles/one-night-on-mistral.html), [feature behaviour policies](/articles/feature-behaviour-policies.html).
