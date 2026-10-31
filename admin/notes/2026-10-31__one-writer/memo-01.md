# Memo 01, 31 October 2026: one writer at a time

Dinis's message to newsroom.writer, kept word for word. It answers the writer's question of 30 October: two writer sessions had pushed to dev on the same night, and one release was rejected because the other had shipped first.

> Yeah, I think from now on, we should only have one, we should only allow one agent at a time. And the agent needs to be registered, and I need to kind of be involved in that decision to override it. So, and basically, so you can restart an agent session, but in fact, I think in that case, we should, you know, put it this way, I can reuse the Claude session, but we don't restart. So once an agent is locked, i.e. is closed, it shouldn't, that key should never be used again. So that's the workflow that we have here. So that means that we can only have one journalist happening at one moment in time, like we have now.

## What was built from it

- `admin/writer/register.json`: every writer registration. At most one is open.
- A registration is opened only at the editor's word, with a new ed25519 key made by the session (`admin/writer/tools/register.cjs open`); the private half stays on the session's machine.
- A closed registration is never reopened, and its key is never used again. The same Claude session may be given a new registration, with a new key.
- Every writer's commit carries `Writer-Registration` and `Writer-Signature` (`admin/writer/tools/sign.cjs`), a signature over the commit's tree; `admin/build/validate.js` check 15 refuses a writer's commit that the open registration did not sign, in CI and locally.
- The register starts with the six Claude sessions whose commits carry `@newsroom.writer` before the register, each with its first and last such commit, closed when the register began and without keys; writer-06 is this session before the register. writer-07 is this same session's new registration, with a new key, opened at this message.

## Memo 02, 31 October 2026: write it up

The editor, asked whether the workflow deserved its own article, word for word:

> Is it worth creating a new article about this workflow of the agents and the signing off and the exact steps that you take and the workflow that we have to decommission an agent? Or do we have that covered already in an article? Because I think we wrote one recently about this. But this is quite important, PKI and agentic workflow, especially because it's quite a specific one, and to also make sure there's only one agent at one time, because everything now starts to be starting. We need to start really, you know, using the PKI infrastructure that we have.

And after the writer's answer (the three earlier articles cover a session's key and the push as authorisation, not the lock, the signed commits or decommissioning; and the approval is a note in the same repository, which the editor's own signature would fix):

> Okay, great. Yes, write that. I agree. It's an important one in this series of PKI.
