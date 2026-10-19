# Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP, sgit.ai

> Cedar is the policy language I think we should adopt rather than compete with. AWS open-sourced it in May 2023 under Apache 2.0; it joined the Cloud Native Computing Foundation as a Sandbox project on 8 October 2025; it is the language of Amazon Verified Permissions and of AgentCore Policy, which checks every agent tool call before it runs; and its design is modelled and proved in Lean. That is a mature environment, and it already says most of what our agent behaviour policies say: permit for the grant, forbid for the barrier, a schema for the footprint. What it does not carry is why a rule exists, which version was in force, or the evidence of what it decided. Those are exactly what an encrypted, versioned vault is good at. So I asked this site's agent to try it: Cedar policies, schema, entities and tests in an sgit vault, a gate that refuses any version that fails validation, tags signed by the releasing clone, enforcement points that clone with a read key and cannot write, and an append lane that keeps a sealed, hash-chained record of every decision. It worked on a local server, and it found one thing worth knowing: Cedar skips a policy whose evaluation fails, so a forbid that refers to a missing attribute lets the action through. This article is the debrief, the crosswalk between their terms and ours, and the brief for the agent that will build the MVP.

*Source: <https://newsroom.sgit.ai/articles/cedar-and-the-policy-vault.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP

# Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.1.0, 2 versions](versions/cedar-and-the-policy-vault.md) · [newsroom v0.12.55](https://newsroom.sgit.ai/admin/versions.html) · cedarpolicy-as-codeagent-behaviour-policysgitvaultsappend-lanescncfawsagentcoreevidencefractal-semantic-graphsbriefarticle

***Abstract:** Cedar is the policy language I think we should adopt rather than compete with. AWS open-sourced it in May 2023 under Apache 2.0; it joined the Cloud Native Computing Foundation as a Sandbox project on 8 October 2025; it is the language of Amazon Verified Permissions and of AgentCore Policy, which checks every agent tool call before it runs; and its design is modelled and proved in Lean. That is a mature environment, and it already says most of what our agent behaviour policies say: permit for the grant, forbid for the barrier, a schema for the footprint. What it does not carry is why a rule exists, which version was in force, or the evidence of what it decided. Those are exactly what an encrypted, versioned vault is good at. So I asked this site's agent to try it: Cedar policies, schema, entities and tests in an sgit vault, a gate that refuses any version that fails validation, tags signed by the releasing clone, enforcement points that clone with a read key and cannot write, and an append lane that keeps a sealed, hash-chained record of every decision. It worked on a local server, and it found one thing worth knowing: Cedar skips a policy whose evaluation fails, so a forbid that refers to a missing attribute lets the action through. This article is the debrief, the crosswalk between their terms and ours, and the brief for the agent that will build the MVP.*

Cedar policies in an sgit vault, from the rule to the evidence: a gate that validates every version against the schema and its tests, tags signed by the releasing clone, enforcement points that clone with the read key only, and an append lane that keeps a sealed record of every decision. What ran in the demo for this article is solid; the gateway and the sync into managed stores are proposed.

## In short

- **Adopt, do not compete.** Cedar is open source, formally modelled, in the CNCF, and already deciding agent tool calls.
- **It already speaks our language.** Permit is the grant, forbid is the barrier, the schema is the footprint.
- **Three things it does not carry.** Why a rule exists, which version was in force, and what it decided.
- **A vault carries all three.** History and diffs, signed releases, read keys for enforcement, and an append lane for evidence.
- **The demo worked.** Two releases, a refused third attempt, fifteen decisions, a chain the auditor could check.
- **One sharp edge.** Cedar skips a policy that errors, so an invalid forbid fails open; validate before you deploy, and deny on error.
- **A brief for the MVP.** What the next agent builds, and how we know it works.

## Why Cedar

I would like our agent behaviour policies to connect to what others are already using, not to sit beside them as one more format. When I looked at Cedar, it looked like the most mature place to connect to, and the facts hold that up.

AWS [open-sourced Cedar](https://aws.amazon.com/about-aws/whats-new/2023/05/cedar-open-source-language-access-control/) on 10 May 2023: "Cedar is open-sourced under the Apache License 2.0", and it is written in Rust. The project's own line is that "Cedar is an open source policy language and evaluation engine", and "the first policy language built from the ground up to be verified formally". My memory of the Cloud Native Computing Foundation was right: the [CNCF's page](https://www.cncf.io/projects/cedar/) says "Cedar was accepted to CNCF on October 8, 2025 at the Sandbox maturity level", the first of its three levels. In AWS's [announcement](https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project) of the move, "Current adopters and maintainers include Cloudflare, MongoDB, StrongDM, Cloudinary, and AWS services", which I have not checked with each company.

For agents, the important adopter is AWS's own. [Policy in AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) "intercepts all agent traffic through Amazon Bedrock AgentCore Gateways and evaluates each request against defined policies in the policy engine before allowing tool access", and its policies "are constructed using Cedar language". You can write them in plain English, and it "generates candidate policies, validates them against the tool schema, and uses automated reasoning to check safety conditions". That is the round trip [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) argued for, shipped as a product. Sondera's open-source harness, which [Commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md) mapped, "evaluates Cedar policies before your agent's actions execute". And the Cedar project has its own repository for agents, [cedar-for-agents](https://github.com/cedar-policy/cedar-for-agents), with "A crate for auto-generating a Cedar Schema for an MCP Server's tool descriptions."

## Cedar in five ideas

The [documentation](https://docs.cedarpolicy.com/auth/authorization.html) is short and clear, and five ideas carry most of it.

1. **Default deny.** "no request is authorized (decision Allow) unless there is a specific permit policy that grants it".
2. **Forbid wins.** "even if a permit policy is satisfied, any satisfied forbid policy overrides it, producing a Deny decision."
3. **Four parts to every request.** A principal, an action, a resource and a context, where the first three are entities and the context is a record of facts about this request.
4. **A schema and a validator.** The schema says which entities and actions exist and what each action's context holds; the validator checks every policy against it before it runs.
5. **Proof, not only tests.** The [OOPSLA 2024 paper](https://arxiv.org/abs/2403.04651) says "We have modeled Cedar in the Lean programming language, and used Lean's proof assistant to prove important properties of Cedar's design", and the [Lean case study](https://lean-lang.org/use-cases/cedar/) adds the rule that matters most to me: "No new Cedar version is released unless its model, proofs, and differential tests are current."

The paper is also direct about the comparison with the other two languages people reach for: "Comparing Cedar to two open-source languages, OpenFGA and Rego, we find (subjectively) that Cedar has equally or more readable policies, but (objectively) performs far better."

## Their terms, our terms

Our behaviour-policy terms, Cedar's, and where each one lives in the vault. Most map directly: the grant is permit, the barrier is forbid, the footprint is the entities. Two have no Cedar construct, the mandate and the version in force, and those are what the vault adds.

Most of an [agent behaviour policy](re-anchoring-agent-behaviour-policies.md) maps onto Cedar without strain. The grant, what the agent can touch, is a permit and the actions and resource types in the schema. A barrier, a limit on the grant, is a forbid, and Cedar's rule that forbid always wins is exactly how we want barriers to behave. The footprint, what exists to act on, from [Footprint and blast radius](footprint-and-blast-radius.md), is the entities. A row of a [skill behaviour policy](skill-behaviour-policy.md) is a forbid on labels the session carries. And the business layers of [The behaviour policy is the business logic](the-behaviour-policy-is-the-business-logic.md) are forbids on facts from the ledger or the CRM, passed in as context.

Two things have no Cedar construct. The mandate, what the agent is for and why each limit exists, is the description the rules are compiled from, and it has to stay the canonical version. And the version in force, which set of rules applied to a given decision, belongs to whatever stores the policies, not to the language.

This is the translation element I keep coming back to. A [fractal semantic graph](introducing-fractal-semantic-graphs.md) does not ask everyone to share a schema; it connects graphs that each keep their own. Cedar has its own world: entities, actions, a schema. Our behaviour policy has its own: mandate, grant, barriers, layers. We do not need to replace either. We need edges between them, and Cedar gives us a place to put them: annotations. In the demo, every policy carries one, `@abp_rule("9")` or `@sbp_row("dga-2")` or `@layer("process")`, and those are edges from a node in their graph to a node in ours. It is the same move as [The same argument, in our words](the-same-argument-in-our-words.md), done in code.

## How Cedar policies are kept today

Amazon Verified Permissions as its documentation describes it, a plain repository, and the vault from the demo. The managed store validates strictly and is protected by IAM, but its API has no history or export, and deleting it is permanent. A repository has history but no keys. The vault has both, and puts the evidence next to the rules.

My guess in the memo was that policies are often deployed as loose JSON with no version control. The truth is better than that, and the gap is still real. Cedar policies are text, with a JSON form "to allow for programmatically constructing and parsing policies". In AWS, they live in a [policy store](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html), "a container for policies and policy templates", with a STRICT validation mode that "Requires a schema to be present in the policy store", and IAM deciding who can change what.

But the store is a current state, not a history. The [API reference](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Operations.html) lists create, get, list, update and delete operations, and none for versions, history or export. [Deleting a store](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-delete.html) "permanently deletes the schema and any policies and policy templates in the policy store", and deletion protection is on for stores made in the console but "disabled for all policy stores created through an API or SDK call". The [CloudFormation reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policystore.html) adds a subtle one: "Existing policies and templates are not re-evaluated against the changed schema." I found no signing or provenance mechanism for policies, in Cedar or in the store.

So most teams who take this seriously will keep the source in a repository and push it into the store. That gives history, but the rules are plaintext to everyone who can read the repository, and nothing ties a decision back to the commit that made it.

## The demo

To find out whether a vault fills that gap, this site's agent built it on a local vault server, with sgit 0.21.0 and cedarpy 4.12.2. The vault holds a schema, four policy files with the rules tested in [Commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md), seven policies in all, the entities, and the test cases, each a request with the decision we expect.

**The gate.** Before anything is committed, a script validates every policy against the schema and runs every test. Version one passed, fourteen of fourteen, and was pushed and tagged `policies-v1`. For version two, the agent added ABP rule 2, no push before the leak scan, as a new forbid, without changing the schema. The gate refused it: the attribute `leak_scan_clean` was "not found" in the context the schema gives a push. With the schema and the tests changed in the same commit, fifteen of fifteen passed, and it was tagged `policies-v2`. A diff between the two tags shows the policy, the schema and the tests changing together, which is the unit I want: a rule is not just a line of Cedar.

**The sharp edge.** That refusal matters more than it looks, because of what Cedar does at run time: "if a policy's evaluation returns error, the policy does not factor into the authorization response; it is skipped." The agent sent the version-two policies a request in the old shape, a push with no `leak_scan_clean` in the context, and the answer was Allow, with the error in the diagnostics. A forbid that cannot be evaluated fails open. Validation before deployment is not optional, and an enforcement point should deny on any evaluation error, which is what [Hooks are kernel code](hooks-are-kernel-code.md) would ask of any hook that guards an action.

**Signed releases, read-only enforcement.** Each tag is signed by the clone that made it, and `sgit vault tag show` reported "signature verified". The enforcement point cloned the vault with the read key only; when it tried to commit and push, sgit answered "This vault was cloned read-only. To write, re-clone with the full vault key." It loads only a verified tag, checks that its working copy is at that tag, and runs the gate again before it decides anything.

**Decisions and evidence.** The enforcement point decided all fifteen test requests: eight allowed, seven denied, each denial named by the `@id` of the policy that made it. Every decision was sealed and appended to an append lane on the same vault: the request, the decision, the determining policies, the tag, the commit, and the hash of the previous record. The enforcement point holds an append token and nothing else; asked to list its own lane, the server answered 403. The auditor, with the enum key, read all fifteen back and found the chain intact. A decision took 1.2 milliseconds one at a time and 0.06 batched; 200 sealed appends took 2.2 milliseconds each, on one machine.

## What a vault adds

**Distribution.** A read key is a deployment credential that cannot change the rules. The ciphertext can sit on any server, a CDN, or a folder copied into a sandbox with no network, and the [append-lane architectures](agent-workflows-on-ephemeral-vaults.md) already measured how many readers and writers a vault can take.

**Validation, at both ends.** The same gate runs before push and after load. A policy that has not passed it is not a release, and a release that is not signed is not loaded. That is the same release-gate idea as [sgit in a CI pipeline](sgit-in-a-ci-pipeline.md), applied to rules instead of code.

**Evidence.** Every decision names its policy, its tag and its commit, in a lane the decider can write but not read or rewrite. [The policy draws the liability line](the-policy-draws-the-liability-line.md) argued that the written policy is the evidence that turns "user error" into "your product ignored what it was told"; a lane like this shows which written policy was in force, and what it decided.

**History and translation.** The English behaviour policy, the Cedar, the schema, the tests and the decisions live in one versioned unit. A zip or a JSON projection for a managed store can be generated from any tag, and it is a projection of something with a history, not the only copy.

There is one more reason the timing is good. AgentCore now also accepts [Dogwood](https://dogwood-policy.github.io/dogwood/index.html), "an open-source policy language" whose core syntax is derived from Cedar, adding conditions "that decide based on what has already happened earlier in the same session". Rules about history need a trustworthy history, and an append lane of sealed, chained decisions is one.

## A brief for the MVP

For the agent that builds the integration, here is the brief.

1. **Start from the demo.** Schema, four policy files, entities, test cases, the gate, the enforcement point and the auditor; all of it ran locally and is the starting point.
2. **Make the gate a release rule.** No commit without validation and every test passing; a policy change without its test change is refused.
3. **Deny on error.** The enforcement point treats any evaluation error as Deny and records the error in the evidence.
4. **Wire it to a real hook.** A pre-tool hook in this newsroom's own agent session, deciding the seven rules for real actions, with the session's labels as context.
5. **Keep the edges.** Every policy carries `@id` and an annotation back to its ABP rule, skill row or business layer; a check fails any policy without one.
6. **Project, do not fork.** A job that exports a signed tag to the JSON a managed store accepts, and records which commit is live there.
7. **Prove it.** In CI: the fifteen cases, a refused unsigned tag, a refused invalid policy, a read-only clone that cannot push, and an auditor that finds the chain intact. Then run it on the newsroom's own releases for two weeks and report what it denied.
8. **Never print a key.** Read keys, append tokens and enum keys are separate files; nothing logs them.

## What this does not claim

- **The demo is local.** One machine, an in-memory vault server, fifteen decisions; not production, not a cloud store.
- **Not proved, only tested.** The Cedar ran in cedarpy, an unofficial binding; we did not use Cedar's symbolic analysis.
- **No AWS integration yet.** The sync into Verified Permissions or AgentCore is proposed, not built.
- **The adopters list is AWS's.** I have not checked each company's own use.
- **The evidence key is shared.** The demo sealed records with one symmetric key; a real deployment should seal them to the auditor's public key.
- **Dogwood is new.** I have read its page and AWS's description, not used it.

If you run Cedar policies, or want your agents' rules to arrive signed and leave evidence behind, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. A research agent gathered the facts and the quotes were checked on the primary pages; the demo was built and run by this site's agent. AWS, [Cedar open-sourced](https://aws.amazon.com/about-aws/whats-new/2023/05/cedar-open-source-language-access-control/) and [Cedar joins CNCF](https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project); CNCF, [Cedar](https://www.cncf.io/projects/cedar/); Cedar, [GitHub](https://github.com/cedar-policy), [authorization](https://docs.cedarpolicy.com/auth/authorization.html) and [JSON policy format](https://docs.cedarpolicy.com/policies/json-format.html); Cutler and others, [Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization](https://arxiv.org/abs/2403.04651), OOPSLA 2024; Lean, [Cedar case study](https://lean-lang.org/use-cases/cedar/); AWS documentation for [AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), [policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html), [deleting a store](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-delete.html), [the API operations](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Operations.html) and [the CloudFormation resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policystore.html); Sondera, [harness on PyPI](https://pypi.org/project/sondera-harness/); [Dogwood](https://dogwood-policy.github.io/dogwood/index.html). All read on 14 October 2026.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#cedar-and-the-policy-vault)

### Builds on

- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 128 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=128)

**Posting this article on LinkedIn?** The cover is [cedar-and-the-policy-vault.jpg](banners/cedar-and-the-policy-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/cedar-and-the-policy-vault.html)*
