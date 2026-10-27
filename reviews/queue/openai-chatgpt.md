# Review queue: openai-chatgpt

Built 2026-10-27, criteria v1.2. One batch a day: take **today's** (UTC). Read the brief first: https://newsroom.sgit.ai/reviews/queue/brief.md
(the criteria: https://newsroom.sgit.ai/reviews/criteria.md). Answer with one record per article, each in its own fenced json block.

## 2026-10-28

- **The evidence behind four days: Jeremiah Grossman's php2shell post, checked claim by claim against the data, with the provenance and the graphs, and the two things that changed since** (`the-evidence-behind-four-days`), published 2026-10-27, text `aa464b31ebd3` at v0.13.105
  - read: https://newsroom.sgit.ai/articles/the-evidence-behind-four-days.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/the-evidence-behind-four-days.html)
  - article_hash: `aa464b31ebd3`, article_version: `v0.13.105`
  - why: The editor's priority. The editor's first ask: a fact check by more than one vendor before the article is called checked. ChatGPT reviewed it on 27 October (changes needed); Perplexity's is the independent second reading.

## 2026-10-29

- **The IPO filing and the agents: what Anthropic tells investors about the risks of its own agents, in its own words, and where RiskMandate and Agent Behaviour Policies answer each one** (`the-ipo-filing-and-the-agents`), published 2026-10-27, text `e460b8a399c8` at v0.13.99
  - read: https://newsroom.sgit.ai/articles/the-ipo-filing-and-the-agents.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/the-ipo-filing-and-the-agents.html)
  - article_hash: `e460b8a399c8`, article_version: `v0.13.99`
  - why: The editor's priority. Published 27 October; numbers from a filing.

## 2026-10-30

- **What the $2,000 bitcoin bounty actually proves: php2shell's real timeline, whether a firewall could have seen it coming, and what hardening can and cannot do without the patch** (`what-the-bitcoin-bounty-actually-proves`), published 2026-10-26, text `c8f43b81134d` at v0.13.97
  - read: https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html)
  - article_hash: `c8f43b81134d`, article_version: `v0.13.97`
  - why: The editor's priority. Published 26 October; a claim about what an event proves.

## 2026-10-31

- **What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide** (`what-can-your-agent-reach`), published 2026-10-18, text `65cdbb00cc89` at v0.12.105
  - read: https://newsroom.sgit.ai/articles/what-can-your-agent-reach.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/what-can-your-agent-reach.html)
  - article_hash: `65cdbb00cc89`, article_version: `v0.12.105`
  - why: The text has changed since your review of 2026-10-18: recheck your findings, then review the rest.
  - recheck f1 (fixed): Effective permissions depend on the agent's configured identity and how it is invoked: in chat with User's account, the requester's; in automation, the connection account's, which need not be the rule's creator or the agent's creator; with Agent's account, the agent's own. 'Typically whoever created the rule' implies more than Atlassian documents. Newsroom: The identity point is rewritten around Atlassian's identity setting: the requester in chat, the connection account in automation (quoting ROVO-837's 'always use the permissions of the connection user in the automation', since the support-article sentence the review quoted was not found), or the agent's own account; the agent's creator is named as not the deciding identity.
  - recheck f2 (fixed): ROVO-837 documents disclosure of a restricted page reference in an automation's output; opening the link still failed. It does not show access to the page or its full content. The reporter notes it does not occur in Rovo Chat. Newsroom: Now says the case disclosed a link to a restricted page, not the page; the link still failed; reading with one identity and publishing to a wider audience is the risk.
  - recheck f3 (fixed): Atlassian now documents agents with their own accounts; its 6 October announcement still lists wider agent-account controls and a non-human identity inventory as coming. Availability should be checked per tenant. Agent's-account agents also make content shared with them available to their users. Newsroom: Agent accounts described as documented, with the 6 October announcement quoted for the wider controls, a check-your-tenant line, and Atlassian's warning that content shared with such an agent is shared with its users.
  - recheck f4 (fixed): The file was less discoverable, not safe; Drive sharing settings still apply. Newsroom: Now 'hard to find', with 'Google Drive sharing settings still apply.'
  - recheck f5 (fixed): True of Google Drive, not of every connector: synced, direct and Smart Link connectors differ in setup, indexing and authentication. Newsroom: Now distinguishes synced, direct and Smart Link connectors, quoting Atlassian's connector types page.
  - recheck f6 (fixed): Restricting who creates agents (by group) and who uses a particular agent (individuals only) are different controls. Newsroom: Creation by group and use by individual are now separate, with Atlassian's sentence on group restriction not being supported.
  - recheck f7 (fixed): Audit logs record events; they do not prevent them. Classification identifies sensitivity and bounds only through a policy acting on it. Only blocking and redaction can prevent data moving. Newsroom: The governance tools are now sorted by what each does: blocking and redaction can bound, classification only through a policy, audit logs are evidence, not a barrier.
  - recheck f8 (fixed): Indexing allowlists control indexing, not everything Rovo can fetch at run time with the user's access; MCP server permissions govern that server's operations, not every Rovo path, on Atlassian's documentation. Newsroom: The allowlists are scoped to indexing, and the MCP switches to what the MCP server does, as Atlassian's page states.
  - recheck f9 (fixed): The PromptArmor report is accurate as a historical report; present exploitability is unverified. Newsroom: Now dated, described as reported as of publication, with current exploitability marked unverified, here and in the limits.
  - recheck f10 (fixed): No population evidence for the size of the gap or how often controls are only prompt instructions. Newsroom: Now 'It can be large, and it has to be measured for the particular deployment rather than assumed'; the earlier 'most organisations' and 'almost nobody' wording is softened.
  - recheck f11 (fixed): The library is example policies; connectors to customer systems are built per engagement and none is a product yet. Newsroom: Now 'policies for commercial agents', with RiskMandate's own sentence that no connector is a product yet.
  - recheck f12 (fixed): The pricing page marks the £500 and £1,500 levels specified, never run, as of 15 September 2026. Newsroom: Now quotes the pricing page's 'specified, never run' for the top two levels, and adds it to the limits.
  - recheck f13 (fixed): The merged page documents an external adapter governed by a pinned copy of the evaluator; it does not alter Ruflo's running policy or restrict other shell or MCP tools. Newsroom: Now scoped to the memory operations of the external adapter, with the page's own statement of what it does not change.
  - recheck f14 (fixed): The Northstar results come from a scripted simulation with synthetic cases and no model. Newsroom: Now 'thirteen synthetic refund requests', 'a scripted simulation: invented orders, scripted mistakes, no model called', and what it does and does not show.
  - recheck f15 (fixed): The Code applies to specified listed companies, not every UK board. Newsroom: Now 'For companies the UK Corporate Governance Code applies to'.

## 2026-11-01

- **What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead** (`what-sgit-does-that-git-does-not`), published 2026-10-27, text `828e4d3673ca` at v0.13.112
  - read: https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.html)
  - article_hash: `828e4d3673ca`, article_version: `v0.13.112`
  - why: Never reviewed by you; never reviewed by anyone.

## 2026-11-02

- **Legal on demand for startups: agent teams that do the reading, lawyers who sign, and a meter instead of a retainer, with three vaults that show the founder's desk, the investor's desk and the deal room** (`legal-on-demand-for-startups`), published 2026-10-27, text `55790800e9e2` at v0.13.109
  - read: https://newsroom.sgit.ai/articles/legal-on-demand-for-startups.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/legal-on-demand-for-startups.html)
  - article_hash: `55790800e9e2`, article_version: `v0.13.109`
  - why: Never reviewed by you; never reviewed by anyone.

## 2026-11-03

- **What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it** (`what-an-agent-is`), published 2026-10-27, text `d468ffef7b41` at v0.13.108
  - read: https://newsroom.sgit.ai/articles/what-an-agent-is.md (and the page, which is canonical: https://newsroom.sgit.ai/articles/what-an-agent-is.html)
  - article_hash: `d468ffef7b41`, article_version: `v0.13.108`
  - why: Never reviewed by you; never reviewed by anyone.

298 more after these.

The empty record, to fill (one per article):

```json
{
 "schema": "newsroom-review/v1",
 "criteria": "v1.2",
 "slug": "",
 "article_version": "",
 "article_hash": "",
 "reviewer": "openai-chatgpt",
 "kind": "agent",
 "model": "",
 "run_by": "",
 "at": "",
 "verdict": "",
 "summary": "",
 "checks": {
  "facts": {
   "result": "not-checked",
   "notes": ""
  },
  "voice": {
   "result": "not-checked",
   "notes": ""
  },
  "claims": {
   "result": "not-checked",
   "notes": ""
  },
  "conversions": {
   "result": "not-checked",
   "notes": ""
  },
  "health": {
   "result": "not-checked",
   "notes": ""
  },
  "people": {
   "result": "not-checked",
   "notes": ""
  }
 },
 "findings": [
  {
   "id": "f1",
   "criterion": "facts",
   "severity": "",
   "section": "",
   "quote": "",
   "issue": "",
   "verification": "",
   "evidence": "",
   "source_passage": "",
   "method": "",
   "suggestion": ""
  }
 ],
 "verified": [],
 "not_checked": []
}
```
