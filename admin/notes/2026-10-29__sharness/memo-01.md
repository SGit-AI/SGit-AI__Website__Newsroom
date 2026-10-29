# Memo 01: introducing sharness.ai (29 October 2026)

Dinis Cruz, in session, word for word:

> Okay, so now here's another major milestone for us. Since, you know, we always talk about this idea that we need to have a secure harness outside the risk mandate environment, outside the hook. After not finding one, I actually took the time and I did a really good productive session with a couple of Claude agents, and we built one, and it's now being released, and this is very exciting. So can you write a very detailed article explaining and introducing sharness.ai, which is, you know, the latest stuff we publish, and we really want feedback, and it's, I think, a super powerful capability. So can you take a very good read and then write a nice article introducing it, and basically starting with the key, almost start strategic, start business, start explaining what he's doing, put in context on our agent behavior policy, read what we talk on the website about the process behavior policies, which is fundamentally what this is, right? And the multiple ways it works, the architecture, there should be some good materials, and then you can go more technical as the article goes.
>
> https://sharness.ai/
> https://github.com/SHarness-AI/SHarness-AI__CLI

## What was read

- sharness.ai, site v0.6.33, read on 29 October 2026 from `/llms.txt` and `/llms-full.txt` (every page's markdown in one file): the brief, Why, Architecture, Components, the PBP on one page, the levels, the decision at the door, the components hub and each door, the landscape and the enforceability matrix, Security, What exists today, the members, the agents and their keys, and Dinis's article of 24 October, "A secure harness for agents".
- The CLI repository, `dev` at 7ea23c6 (29 Oct 2026, 03:16 UTC): README, pyproject (v0.2.0, Apache-2.0, standard library only), `sharness_ai/` (6,041 lines of Python), `tests/` (2,457 lines).
- PyPI: sharness-ai 0.1.0 (24 Oct 2026, 16:27 UTC) and 0.2.0 (29 Oct 2026, 03:11 UTC).
- The E09 page, https://sharness.ai/code/browser/demo/index.html, opened in headless Chromium in this site's container on 29 October 2026: the guest booted and `hello` printed "6/6 held · measured 29 Oct 2026, Landlock ABI 7" at 111 seconds. Running the CLI directly in this container was not permitted by the session's permission policy, so nothing here was run on the container's own kernel.
