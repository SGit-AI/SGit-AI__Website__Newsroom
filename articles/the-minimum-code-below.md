# The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool, sgit.ai

> A conversation at Chainguard's event today sharpened something I have thought for a while. Chainguard does security from the bottom up, and does it very well: it rebuilds the operating system and the libraries from source, keeps the images minimal and manages the whole process. But even the most locked-down image still holds a great deal of code the application never runs, the assurance still depends on testing, and the loop that caused the problem in the first place is still there: when something breaks, you give it more. As soon as the work reaches the application, it stops. My proposal is to come from the other end. Start from the user story and, at every layer down, ask one question: what is the minimum code below this that the layer above needs? Keep that, remove everything else, and draw the immutable line as high as the evidence allows. It did not scale before; with models and fractal semantic graphs, it can. I measured it for this article on a real tool, sgit and its dependencies, running a CI-style use case under coverage and then running it again from a tree holding only the files that ran. Of 1,500 files, 428 were kept, and the use case passed; commands outside it failed because their code was not there. It also showed the limits: one compiled binary held three quarters of the bytes and no coverage tool can see inside it, and coverage missed a compiled module the tests then caught. Tools that minimise containers at run time already exist, so the new part is the direction: from what the application is for, through a graph, down to a build that can be certified. Chainguard is unusually well placed to offer it, and someone will build it.

*Source: <https://newsroom.sgit.ai/articles/the-minimum-code-below.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool

# The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.1.0, 2 versions](versions/the-minimum-code-below.md) · [newsroom v0.12.38](https://newsroom.sgit.ai/admin/versions.html) · containerssupply-chainattack-surfaceminimisationchainguardfractal-semantic-graphscode-coveragehigh-assurancepythonarticle

***Abstract:** A conversation at Chainguard's event today sharpened something I have thought for a while. Chainguard does security from the bottom up, and does it very well: it rebuilds the operating system and the libraries from source, keeps the images minimal and manages the whole process. But even the most locked-down image still holds a great deal of code the application never runs, the assurance still depends on testing, and the loop that caused the problem in the first place is still there: when something breaks, you give it more. As soon as the work reaches the application, it stops. My proposal is to come from the other end. Start from the user story and, at every layer down, ask one question: what is the minimum code below this that the layer above needs? Keep that, remove everything else, and draw the immutable line as high as the evidence allows. It did not scale before; with models and fractal semantic graphs, it can. I measured it for this article on a real tool, sgit and its dependencies, running a CI-style use case under coverage and then running it again from a tree holding only the files that ran. Of 1,500 files, 428 were kept, and the use case passed; commands outside it failed because their code was not there. It also showed the limits: one compiled binary held three quarters of the bytes and no coverage tool can see inside it, and coverage missed a compiled module the tests then caught. Tools that minimise containers at run time already exist, so the new part is the direction: from what the application is for, through a graph, down to a build that can be certified. Chainguard is unusually well placed to offer it, and someone will build it.*

Top down, one question at every layer: what is the minimum code below this that the layer above needs? From a user story, through the workflow, modules and functions, to the dependencies, the language runtime and the operating system. Projected from the top, derived from the code; derived and not projected is code nobody asked for.

Less code: a series in four parts

Code is a liability: remove what each use case does not call, apply it to the browser, and build on small blocks you did not have to write.

[you are here1 · MeasuredThe minimum code belowOne real use case of sgit, under coverage: 428 of 1,500 files ran, and a tree of only those passed.](the-minimum-code-below.md)[2 · Less codeThe code you do not shipThe worst bugs sit in features nobody needed; models make removing them safe, and someone can be paid to keep it small.](the-code-you-do-not-ship.md)[3 · The browserA minimal viable browserA small kernel and components loaded when needed: a browser for one app, one agent, or a reader, sold as speed.](a-minimal-viable-browser.md)[4 · Small blocksCloudflare as Lego blocksStorage, compute, models, email and identity as blocks, and an sgit vault server in 83 lines.](cloudflare-as-lego-blocks.md)

## In short

- **Chainguard secures from the bottom up.** Rebuilt from source, minimal images, a managed process, and it stops where the application starts.
- **Three gaps remain.** Code the application never runs, assurance that depends on testing, and the loop of granting more when something breaks.
- **Come from the top.** At every layer, ask for the minimum code below that the layer above needs, and remove the rest.
- **Measured on one tool.** sgit and its dependencies, one use case: 1,500 files down to 428, the use case passing, other commands failing because their code was gone.
- **And its limits.** One compiled binary was three quarters of the bytes; coverage missed a compiled module; only 38% of the statements in the kept files ran.
- **Others minimise at run time already.** SlimToolkit and RapidFort watch what a container touches. The new part is starting from the use case, through a graph.
- **The prize is assurance.** If the code with a vulnerability is not there, there is nothing to patch, and a build traced to its use case can be certified.

## Bottom up, and where it stops

I have a lot of time for what Chainguard does. In [Attacks rewritten as mandates](attacks-rewritten-as-mandates.md) its public ledger of supply-chain attacks was the example, and the controls it sells, packages rebuilt from source, no install-time scripts, actions pinned to a commit, would by my reading have held in most of them. Its images come in minimal variants without shells or package managers. That is security built from the bottom up: take the operating system, take the libraries, rebuild them, keep them current, and give the customer something they can trust more than the public registry.

But bottom up has three gaps, and the conversation today made them clearer.

First, even the most locked-down image holds code the application never runs. My estimate is that in most images it is the large majority; the one case measured below found about 70% of the files in the dependency tree never ran. Every one of those files is attack surface and a source of vulnerability reports.

Second, the assurance still depends on testing. A hardened base says the parts are trustworthy; whether the application still works on them, and does only what it should, is the customer's problem.

Third, the loop that caused the problem in the first place is still there. When something breaks, the reflex is to give it more: another package, another permission, a shell back in the image. Chainguard's own tool for tailoring images, Custom Assembly, is built in that direction. Its documentation says it "only allows you to add packages into a given container image" and that "you cannot remove the packages included in the source application image by default."

And the application itself, where the code is hardest to change, is where the bottom-up model stops. When I asked about virtual patching and similar fixes at the application layer, I did not hear that it is something they do, and I could not find it on their public pages.

## Top down: the minimum code below

My proposal is to come from the other end, and ask one question at every layer: what is the minimum code below this that the layer above needs?

Start from the user story. What is the code needed to run this use case? Then the workflow: which commands does it call? Then the modules those commands load, the functions in them that actually run, the files in each dependency those functions touch, the parts of the language runtime the code imports, and the binaries and libraries in the operating system the runtime calls. At each layer, keep what the layer above needs and remove everything else. The higher you can draw the line below which nothing changes, the immutable line, the more of the system is fixed, exact and small.

This is the same shape as the review model in [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md): a graph projected from the top, from objectives and stories down to the commands they will touch, joined to a graph derived from the code. In that article's words, a node the code has and no story asked for is "derived, not projected". In a code review that is a question for the author. In an image, it is code to remove.

What it kills is living off the land. An attacker who gets into a process uses what is already there: a shell, an interpreter's standard library, a network tool, a module that can write files. If the only code on the box is the code the use case runs, there is very little to live off. It is what a good linker does when it pulls in only the functions a program references, applied to the whole stack, from the story to the operating system.

## Measured on one real tool

One use case, measured. sgit 0.21.0 and its dependencies, run under coverage for a CI-style use case, then run again from a tree holding only the files that ran: 1,500 files down to 428, Python source from 4.72 MB to 1.98 MB, compiled code unchanged at 14.78 MB. Inside the kept files 38% of the statements ran; commands outside the use case failed; coverage missed a compiled module the tests caught.

Years ago I did a version of this by hand. I had a Python application with close to full code coverage, ran the coverage across the dependencies as well as my own code, took every file the coverage had touched, built a new package from only those, and deployed it. It worked. I used it to shrink Python deployments for Lambda functions, and the cut, as I remember it, was close to 90% of the dependency code.

So I did it again for this article, on a real tool. The tool was sgit 0.21.0, installed in a fresh virtual environment with its four dependencies: cryptography, osbot-utils, cffi and pycparser. The use case was the one from [sgit in a CI pipeline](sgit-in-a-ci-pipeline.md), run against a local vault server: create a vault, commit a build manifest, push it, clone only the build folder in a fresh home, make a key pair, encrypt a file and decrypt it. I ran it under coverage, measuring every file in the dependency tree, not only sgit's own. Then I copied only the files that had run, plus the compiled modules and data files beside them, into a new tree, and ran the same use case again from that tree with the original packages out of reach.

- **It worked.** The use case passed from the minimal tree: the manifest came back from the scoped clone and the decrypted file read "secret".
- **The tree was much smaller.** 1,500 files became 428. Of 1,416 Python files, 418 had run, and the Python source went from 4.72 MB to 1.98 MB. Two of the four dependencies, cffi and pycparser, ran no Python code at all.
- **What was not needed was not there.** Commands outside the use case failed: `sgit history log` and `sgit vault backup` both stopped with `ModuleNotFoundError`, because the code they needed had been removed.

## What the measurement also showed

Three results matter as much as the cut.

**The compiled code did not move.** 14.78 MB of the dependencies is compiled, three quarters of the whole, and almost all of it is one file: the 14.4 MB Rust binary inside cryptography. Coverage sees Python; it cannot see which functions inside a compiled library ran, so file-level minimisation keeps all of it. Going further means building that binary with only what is used, which is a build-time decision, made by whoever builds from source.

**Coverage was not enough.** cffi ran no Python code, so a pure coverage cut would drop it. When I removed its compiled backend, the use case failed with `No module named '_cffi_backend'`: something in the stack loads it without running any of cffi's Python. The tests caught what the coverage missed, which is the point of the method. The evidence for what is needed is the test suite passing, not the coverage report.

**Files are a coarse unit.** `sgit publish`, which was not in the use case, still worked, because the module it lives in was loaded by commands that were. Inside the 418 files that ran, only 38% of the statements executed. Function-level removal would cut much more than file-level, and that is where a semantic graph of the code, function by function, earns its place.

## It did not scale before, and now it can

None of this is new as an idea. Doing it for one application, by hand, with coverage and a script, works and is too much effort to do for every service and every release. What changed is that the expensive part, understanding what each layer is for and what it calls, is now the part models are good at, and the result can be held as a [fractal semantic graph](introducing-fractal-semantic-graphs.md): the story, its workflows, the modules, the functions, the dependencies and the files of the operating system, each in its own vocabulary, with named edges between them. Then "what is the minimum below this?" is a walk, and "why is this file here?" has an answer, the path up to the story that needs it.

And it is deterministic where it matters. The graph says what should be kept; the build keeps exactly that; the tests prove the use case still works. Change the use case, and the build is regenerated.

## Who does what today

Three ways to get to less code. Bottom up and hardened, as Chainguard does; runtime minimisation, as SlimToolkit and RapidFort do; and top down by use case, proposed here, which starts from what the application is for and ties every remaining line to a reason.

I said it never scaled before, and that needs a correction: minimising containers is a real field already. [SlimToolkit](https://github.com/slimtoolkit/slim), formerly DockerSlim and now a CNCF Sandbox project, runs a container, watches what it touches and builds a smaller image, by up to 30 times in its own words. [RapidFort](https://www.rapidfort.com/) profiles applications at run time and removes the components that never run, and reports large reductions in attack surface and in vulnerabilities; those are its own figures.

Both work from what a container did. What I am proposing starts from what the application is for: the use case defines what must run, the graph traces every layer, the unit of removal goes down to the function and the build, and the tests are the evidence. Runtime observation is one input to that, not the whole of it.

## The business model: certify what is left

Here is the question that turns this into a business. A package has a vulnerability. If the vulnerable code is never called by the use case, why care? And more to the point, why is that code there at all? In a build that keeps only the code a use case needs, a vulnerability in removed code is not a patch to apply; it is a line in the record saying the code is absent.

That is something that can be certified. A build traced from the story to the operating system, with the graph saying why every remaining line is there and the tests proving the use case, is a high-assurance artefact: a third party can check that the code with each known vulnerability is not present, and say so. That is the next product for a company like Chainguard, which already builds every layer from source and is trusted to say what is in it. It is also the product that, built by someone else on top of a platform like theirs, could eventually deploy without needing the base images at all, which is why I think they should build it, or partner with whoever does.

## What this does not claim

- **One tool, one use case.** sgit and four dependencies, measured once; other applications will differ, and the bottom two layers, the Python runtime and the operating system, were not measured here.
- **The 70% to 90% figures are estimates and memory.** My Lambda result is from memory; the 70% is this measurement's share of files that never ran.
- **Chainguard's plans are not public to me.** That they do not do this is from their public pages and one conversation; they may be working on it.
- **Runtime minimisation tools exist.** SlimToolkit's and RapidFort's figures are their own; I have not tested them here.
- **A use case is only as complete as its tests.** Anything the tests do not exercise is removed, so the test suite becomes the definition of the application.

If you are running hardened images and wondering how much of what is in them your application needs, or you want to build the top-down version, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, after a conversation at Chainguard's event, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The measurement was run for this article: sgit 0.21.0 in a fresh virtual environment, a use case against a local vault server run under coverage 7 across the whole dependency tree, a tree built from the files that ran, and the same use case run from it. Chainguard, [Custom Assembly overview](https://edu.chainguard.dev/chainguard/containers/custom-assembly/overview/); [SlimToolkit](https://github.com/slimtoolkit/slim); [RapidFort](https://www.rapidfort.com/). All read on 14 October 2026.

## Threads

Site & engineeringGraphs & knowledge[This article as a graph →](graphs.md#the-minimum-code-below)

### Builds on

- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](attacks-rewritten-as-mandates.md) 28 supply-chain attacks read as reach beyond mandate: what a hardened registry stops, what only a written mandate can, and why agents change it.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.

### Continued by

- [The jobs that never scaled: on-demand expertise, the work before and after the meeting, and why a historian, a librarian or a consultant can now work for every project that needs one](jobs-that-never-scaled.md) What never scaled is on-demand expertise: the before and after the meeting. Agents can now carry them, for any expert, anywhere.
- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.
- [The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production](the-eyeballs-get-cheap.md) Cheap, deep AI security review gives open source the eyeballs it never had; with sovereignty and paid maintenance, all point at the least code in production.
- [Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in](chainguard-mapped.md) Chainguard mapped from OS to agents, its public feeds counted, and the context layer above the package where an open policy and a vault fit.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 112 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=112)

**Posting this article on LinkedIn?** The cover is [the-minimum-code-below.jpg](banners/the-minimum-code-below.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-minimum-code-below.html)*
