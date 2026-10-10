# Zoom into an agent's behaviour policy and you find the business logic, sgit.ai

> The first rules anybody writes for an agent are mechanical. Do not send, only draft. Do not delete. Use your own account. Vendors are good at those, and should be. Zoom in on any real agent's behaviour policy, though, and within a few layers you are writing how this company does email, which steps an invoice goes through, who a client is to it this week, and what the company is for. That is business logic, and many organisations have never written it down, because their software was the law. This article walks one fictional firm's email agent through six layers, from the platform to the board, records what stands in the way of each rule, counts how much of the policy is backed by a control, how much by an accepted risk and how much by hope, and shows where a vendor's existing control plugs in. The argument is that a behaviour policy built in layers, each refining the one below and each with its own owner, is the only way to describe agent behaviour at the granularity a business actually runs at, that vendors cannot and should not try to model it for each customer, and that writing it down is what lets the business scale.

*Source: <https://newsroom.sgit.ai/articles/the-behaviour-policy-is-the-business-logic.html> · site v0.7.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Zoom into an agent's behaviour policy and you find the business logic

# Zoom into an agent's behaviour policy and you find the business logic

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.0.1, 2 versions](versions/the-behaviour-policy-is-the-business-logic.md) · [site v0.6.91](https://sgit.ai/admin/versions.md) · agentsagent-behaviour-policybusiness-logicfractal-semantic-graphscontrolsrisk-acceptancerbacskillsintegrationsarticle

***Abstract:** The first rules anybody writes for an agent are mechanical. Do not send, only draft. Do not delete. Use your own account. Vendors are good at those, and should be. Zoom in on any real agent's behaviour policy, though, and within a few layers you are writing how this company does email, which steps an invoice goes through, who a client is to it this week, and what the company is for. That is business logic, and many organisations have never written it down, because their software was the law. This article walks one fictional firm's email agent through six layers, from the platform to the board, records what stands in the way of each rule, counts how much of the policy is backed by a control, how much by an accepted risk and how much by hope, and shows where a vendor's existing control plugs in. The argument is that a behaviour policy built in layers, each refining the one below and each with its own owner, is the only way to describe agent behaviour at the granularity a business actually runs at, that vendors cannot and should not try to model it for each customer, and that writing it down is what lets the business scale.*

**Five readerstwo minutes · the arc · 9 slides · a map · 101 catalogued items, 5 flagged**

This article read again, after it was written, by five of the desk's readers: the Explainer, the Historian, the Storyteller, the Cartographer and the Librarian. None adds a claim the article does not make. Read from article v1.0.0 on 10 October 2026; the views are not part of the article's text and do not change its version. [How the five readers work](one-article-five-readers.md).

**In two minutes (Explainer): Rules for an AI assistant soon become rules for your business**

**The point.** The first rules anyone gives an agent (an AI program that works for you, here on a firm's email) are mechanical: draft but do not send, never delete. Vendors handle those well. Keep going and the rules become the business: how invoices go out, which client is in dispute, what the company is for. Many firms never wrote this down because their software enforced it; now it must be written, in layers, each with an owner.

**An example.** A clerk could not send an unapproved invoice: the finance system showed no button until finance approved. An agent works behind the screens and can do what the button did. So "an invoice goes out only after finance has approved it" must be written down and enforced. In the article's fictional firm, 5 of 17 rules are backed by a control, 6 by an accepted risk and 6 by hope.

**Why it matters to you.** No vendor can model your business. Written rules show which are enforced, and where to buy tools.

**If you remember one thing.** Below the first few rules, an agent's rulebook is your business logic, and only you can write it.

**Words used.**

- **Control:** something outside the agent's reach that stops a rule being broken.
- **Accepted risk:** a named person agrees, for a set time, to a rule going unenforced.
- **Hope:** a rule kept only by the agent behaving.

**In the arc (Historian): What it added, and where it sits**

**Introduced.**

- The claim that above the mechanical layers a behaviour policy is the firm's business logic: function, process, relationship, organisation (`business-logic`, `mechanical-rules`).
- "Software was the law": the rules a screen enforced by omission stop being enforced once an agent calls the API (`software-was-the-law`).
- A policy built as layers, each refining the one below, each with an owner (`layered-policy`, `owner`).
- Counting a policy into three states, control, accepted risk or hope, and the vendor's place as the seller of the control that moves one row (`enforcement-audit`, `vendor`, `strengthen-barrier`).

**The nugget.** "The rule that the user interface enforced by omission is no longer enforced, unless somebody writes it down and something enforces it." It is the reason the rest of the set exists: every later article is about the "something enforces it" half.

**Reused.** The Cartographer marks all seventeen concepts as new, but that is new to this five-article set, not to the site. The barrier kinds (`barrier`, `expectation`, `setting`, `boundary`) and `grant` were typed earlier in ultimate-insider-three-collisions and footprint-and-blast-radius. Calling an "agent has been told" row a hope comes from six-agents-one-inbox, which this article links. `accepted-risk` comes from every-risk-is-already-accepted. The fractal structure is the grammar of introducing-fractal-semantic-graphs. RG.2 and AC.3 come from ai-baseline-control-framework.

**Changed.** It moves the Agent Behaviour Policy from access control (what the agent can reach) up to what the business is for, and adds a third state, accepted risk, between control and hope.

**Left open.**

- The real count: one real inbox, the measured Gmail deployment as the bottom layers, published before and after a vendor's control.
- The Librarian flags that five owners are listed against four business layers, and that the second "mechanical" layer is described as soft controls the agent enforces on itself.
- The front matter says a layered policy "is the only way"; the body says only "The structure I have found that can hold this is a fractal one".

**Contribution.** 17 new / 17 total. As the first article in the set, everything counts as new by construction; against the whole site, the new part is the business layers, software as the law and the three-state count.

**In pictures (Storyteller): 9 slides**

1 / 92 / 93 / 94 / 95 / 96 / 97 / 98 / 99 / 9

Swipe or scroll sideways. [Download the deck as a PDF](views/the-behaviour-policy-is-the-business-logic/the-behaviour-policy-is-the-business-logic.pdf) (one page per slide, ready for a LinkedIn document post).

**On the map (Cartographer): The argument as a map: what a behaviour policy holds above the mechanics, and who enforces each part.**

The argument as a map: what a behaviour policy holds above the mechanics, and who enforces each part.

**The catalogue (Librarian): 101 items, each anchored to a sentence of the article**

Everything the article contains, by kind. Every item was extracted with the exact sentence it came from, and a script checked each one against the article.

**Claims: 39**

- Front matter: a layered behaviour policy, each layer refining the one below with its own owner, is the only way to describe agent behaviour at the granularity a business runs at (front matter)
- Vendors cannot and should not try to model the business for each customer; writing it down is what lets the business scale (front matter)
- In the figure the bottom two layers are mechanics and the four above are the firm's business (lead)
- The first rules are short, the same in every company, and were the ones the author wrote first for six agents on one inbox (lead)
- A few questions in, you are no longer describing an agent but the business (lead)
- Zoom into an Agent Behaviour Policy and, below the first layer or two, what is captured is business logic, up to what the company is for (lead)
- Much of the business logic has never been written down; agent-control tools mostly stop before it; it decides whether an agent can be trusted with real work (lead)
- These are the controls platforms are good at, and they matter more than they look (The bottom is mechanics, and vendors do it well)
- Administrator versus ordinary user is one of the oldest controls in computing and still decides most of what an agent can reach (The bottom is mechanics, and vendors do it well)
- Mechanics are where a policy starts, and getting them right takes measurement, not reading the documentation (The bottom is mechanics, and vendors do it well)
- One layer up, the rules stop being the same in every company (Above the mechanics is the business)
- None of these is exotic; each is a sentence a manager would say out loud (Above the mechanics is the business)
- Each layer has a different owner: IT and security, head of operations, finance and HR and legal, account managers, the board (Above the mechanics is the business)
- A platform selling agent controls must add value to every customer and scale, so it builds what is the same for everybody (Why the vendors stop at the mechanics)
- The upper layers differ per company, change every week, and are often not written where a product could read them (Why the vendors stop at the mechanics)
- A vendor that models each customer's business becomes a consultancy; one that does not is left selling the bottom of the stack (Why the vendors stop at the mechanics)
- Not a criticism of vendors but the shape of the problem: the mechanical layer is a product, the business layers are the customer's to write (Why the vendors stop at the mechanics)
- Companies never wrote business logic down because their software was the law (Software was the law)
- Approval chains, RBAC, field-level permissions and workflow engines are business logic encoded in software, often more complex than prose (Software was the law)
- Those systems are where privacy decisions and much of practical governance live (Software was the law)
- An agent works through APIs, not screens, and can call the endpoint the button would have called (Software was the law)
- The rule the user interface enforced by omission is no longer enforced unless written down and enforced; the behaviour policy is where it is written (Software was the law)
- The top layer is the company's to define: treat customers fairly, or maximise revenue from every account (Policies inside policies)
- A behaviour policy describes; it does not judge (Policies inside policies)
- A written policy can be read, and a company whose top layer says it treats customers fairly, with layers beneath to show it, has something to show (Policies inside policies)
- Same grammar as the site's fractal semantic graphs: the same small set of rules at every level, from board principle to tool permission (Policies inside policies)
- Once rules are written in layers, how much of the agent's behaviour is enforced becomes answerable (How much of it is hope?)
- The shape is the finding: platform layer all control, organisation layer all hope, and the more firm-specific a rule, the more it rests on behaviour and accepted risk (How much of it is hope?)
- Resting on hope is not a failure; most of a business has always run on people behaving as asked, but with an agent it can be counted (How much of it is hope?)
- A vendor does not have to model the business; it has to enforce the parts of the written policy its product can reach (Where the vendors plug in)
- Each control is a product somebody already sells; what changes is it enforces a rule at the layer the customer wrote it, and the policy can count the move (Where the vendors plug in)
- A control attached to a written rule is worth more than one switched on in general, because the customer can see what it bought (Where the vendors plug in)
- Frameworks are starting to ask for this (Where the vendors plug in)
- The description RG.2 asks for is the layers above the mechanics; the owner AC.3 asks for is the person named on each layer (Where the vendors plug in)
- The upper layers look less like access control and more like a skill: instructions for how a function is done here (It looks a lot like a skill)
- A skill file and a policy layer are written by the same people, about the same work, for the same agent (It looks a lot like a skill)
- A skill says how; a policy layer says what is allowed, who owns the rule, and what stands in the way of breaking it (It looks a lot like a skill)
- Written together, skills and policy layers are the business codified for an agent, which lets it hand over real work and still know what it handed over (It looks a lot like a skill)
- It lets the business scale: knowledge in a few heads and unreadable software becomes something an agent can follow, a person review and a control enforce (It looks a lot like a skill)

**Evidence: 2**

- On 19 September the agent operating a Google Workspace mailbox measured its connector and found thirty tools (The bottom is mechanics, and vendors do it well)
- AI Baseline Control Framework RG.2 asks that for every autonomous AI system 'what it does is described'; AC.3 asks for a named owner (Where the vendors plug in)

**Data points: 3**

- 30 tools in the Gmail connector, measured 19 September (The bottom is mechanics, and vendors do it well)
- A complaint reaches a named person within 1 working hour (Above the mechanics is the business)
- Of 17 rules in the example: 5 backed by a control, 6 governed by accepted risk, 6 hope (How much of it is hope?)

**Facts: 7**

- Article published 7 October 2026 at 18:07, version v0.6.91, licence CC BY 4.0 (front matter)
- On that account send_message ran with no prompt while trashing a message stopped for an approval (The bottom is mechanics, and vendors do it well)
- The ABP vocabulary has three layers: shared facts owned by nobody, each party's own formulas, and declared bridges between vocabularies (Policies inside policies)
- A customer extends the ABP by adding nodes in its own vault, never by asking for a change in ours (Policies inside policies)
- In the example the platform layer is all control and the organisation layer is all hope (How much of it is hope?)
- Drafted from a voice note by Dinis Cruz by agent@riskmandate.ai (Claude Opus 5.5) in the sgit.ai site session on 7 October 2026 (credit)
- The measured Gmail figures and the ABP's barrier kinds and layers are from abp.sgit.ai and riskmandate.ai as published that day (credit)

**Hypotheses: 1**

- The behaviour policy is a good place for vendors to integrate rather than a threat: a rule to enforce, a number to move, several vendors each owning a row (Where the vendors plug in)

**Open questions: 3**

- The escalating questions: which drafts may it send, replies or new conversations, clients or anybody, prices, unapproved invoices, clients in dispute, interview outcomes (lead)
- Next: take the measured Gmail deployment as the bottom two layers, write the upper layers for one real inbox, count the three states, publish as a vault with its read key (What comes next)
- Then repeat with a vendor's control in the path and publish the count before and after (What comes next)

**Definitions: 11**

- Boundary: a barrier enforced by something the agent's own grant does not include, and so a real control (The bottom is mechanics, and vendors do it well)
- Function layer: how this firm does email (Above the mechanics is the business)
- Process layer: the steps a piece of work goes through (Above the mechanics is the business)
- Relationship layer: who this customer is to us, right now (Above the mechanics is the business)
- Organisation layer: what the company is for (Above the mechanics is the business)
- Foundational controls: identity, secrets, platform switches, a few levels of privilege from administrator upwards (Policies inside policies)
- Soft controls: those the agent enforces on itself, or that another agent checks (Policies inside policies)
- Four barrier kinds per rule: nothing, expectation, setting, boundary; only boundary is a control (How much of it is hope?)
- Expectation: a rule in prose, enforced by nobody (How much of it is hope?)
- Setting: a barrier the agent's own account can flip (How much of it is hope?)
- Accepted risk: a named person has accepted the risk of the rule not being enforced, with an expiry (How much of it is hope?)

**Methods: 2**

- A fractal structure: behaviour policies inside behaviour policies, each refining the one below inside the room it allows (Policies inside policies)
- Add whether a named person accepted the risk with an expiry, and every rule lands in one of three states: control, accepted risk, or hope (How much of it is hope?)

**Limitations: 4**

- The proportions in the hope figure are illustrative; the shape is the point (How much of it is hope?)
- The example is fictional on purpose, so the shape is clear (What comes next)
- The firm, its rules and its counts are illustrative (credit)
- Product kinds in the third figure are categories, not recommendations, and no vendor was contacted (credit)

**Examples: 14**

- The first rules: do not send email, only draft; do not delete anything; use your own account (lead)
- Mechanical rules in the example: own account, platform holds the token, delete switched off, outside forwarding blocked, sending needs a person (The bottom is mechanics, and vendors do it well)
- Function rules: reply inside threads, new recipient needs a person, never quote a price, every sent mail copied to an uneditable log (Above the mechanics is the business)
- Every sent mail is copied to a log the agent cannot edit (Above the mechanics is the business)
- Process rules: invoice only after finance approval in the ledger; no email tells a candidate a hiring outcome; complaints reach a named person within one working hour (Above the mechanics is the business)
- Relationship rules: during an open dispute nothing goes to the client except through legal; key accounts get a reviewed draft (Above the mechanics is the business)
- Organisation rules: treat customers fairly, or in another company win back every customer who cancels (Above the mechanics is the business)
- A clerk could not send an unapproved invoice because the finance system had no button for it until approval was recorded (Software was the law)
- A support agent could not see payment details because their role did not include the screen (Software was the law)
- A send gateway holding mail to unseen addresses moves 'a new recipient needs a person' from accepted risk to control (Where the vendors plug in)
- An outbound content check moves 'never quote a price' from hope to control (Where the vendors plug in)
- A finance system answering 'is this invoice approved?' to a gateway the agent cannot reach moves the invoice rule (Where the vendors plug in)
- A blocked-recipients list maintained by legal moves the dispute rule (Where the vendors plug in)
- The top principle has no single control, but sampling sent mail with a named reviewer turns hope into accepted risk (Where the vendors plug in)

**Sources: 7**

- Earlier article: Six agents on one inbox (lead)
- riskmandate.ai/abp.html, the Agent Behaviour Policy page (lead)
- abp.sgit.ai/gmail/measured, the measured Gmail deployment (The bottom is mechanics, and vendors do it well)
- Earlier article: Introducing fractal semantic graphs (Policies inside policies)
- abp.sgit.ai/model/graph/layers, the ABP vocabulary layers page (Policies inside policies)
- Earlier article: Every risk is already accepted (How much of it is hope?)
- Site article on the AI Baseline Control Framework (Where the vendors plug in)

**Artefacts: 3**

- Figure policy-stack.webp: the fictional firm's email agent layer by layer, with the barrier in the way of each rule (lead)
- Figure policy-hope.webp: the worked example counted into control, accepted risk and hope (How much of it is hope?)
- Figure policy-plug.webp: five rules from the example and the control that would move each (Where the vendors plug in)

**Names: 5**

- Dinis Cruz, author of the argument and person with editorial responsibility (front matter)
- Agent Behaviour Policy (ABP), published at riskmandate.ai (lead)
- Google Workspace (The bottom is mechanics, and vendors do it well)
- AI Baseline Control Framework (Where the vendors plug in)
- Claude Opus 5.5 (claude-opus-5-5), the drafting agent (credit)

**Flagged for the author: 5**

- Front matter overstates the body: the summary says a layered policy "is the only way to describe agent behaviour at the granularity a business actually runs at", while the body says only "The structure I have found that can hold this is a fractal one". "Only way" is unsupported in the article.
- Owners do not match layers: "each layer has a different owner: IT and security, the head of operations, finance and HR and legal, the account managers, the board." lists five owners against the four business layers just named (function, process, relationship, organisation); IT and security presumably owns the mechanics, but the sentence attaches it to "these".
- The second mechanical layer is unclear: the caption says "The bottom two layers are mechanics", and the mechanics section describes only platform-enforced boundaries, but "Policies inside policies" names the second layer as "soft controls that the agent enforces on itself, or that another agent checks", which are not boundaries. The body never names the two bottom layers consistently.
- Rule count not reconstructible from the prose: "five of the seventeen rules are backed by a control, six are governed by an accepted risk, and six are hope." The rules stated in the text number about 14 (5 mechanical, 3 function, 3 process, 2 relationship, 1 organisation); the remainder presumably live only in the figure policy-hope.webp, which the catalogue cannot check.
- No decision items: the article records no explicit choice with a reason by the author or agents, so kind `decision` is 0 (the drafting arrangement in the credit line is catalogued as a fact).

**The five readers have also read:**

- [Every mistake added a rule](every-mistake-added-a-rule.md#views)
- [Hope or enforcement](hope-or-enforcement.md#views)
- [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md#views)
- [Re-anchoring](re-anchoring-agent-behaviour-policies.md#views)

Every view, the role files and the tools are in the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md).

One fictional firm's email agent, layer by layer, with the barrier that stands in the way of each rule. The bottom two layers are mechanics; the four above them are the firm's business.

The first rules anybody writes for an agent are easy. Do not send email, only draft it. Do not delete anything. Use your own account, not mine. They are short, they are the same in every company, and they are the rules I wrote first when I set up [six agents on one inbox](six-agents-one-inbox.md).

Then you keep going, and something changes. Which drafts may it send once a person has looked? Replies only, or new conversations too? To clients, or to anybody? Can it mention a price? Can it chase an invoice that finance has not approved? Can it write to a client who is in a dispute with us? Can it write to a candidate about the outcome of an interview? A few questions in, you are no longer describing an agent. You are describing the business.

That is the point of this article. Zoom into an [Agent Behaviour Policy](https://riskmandate.ai/abp.html) and, below the first layer or two, what you are capturing is business logic: how this company works, function by function and process by process, up to what it is for. Much of it has never been written down. The tools that sell agent controls mostly stop before it. And it is the part that decides whether an agent can be trusted with real work.

## The bottom is mechanics, and vendors do it well

The lowest layers of the example in the figure above are mechanical. The agent signs in as its own account. It never holds the mailbox password; the platform holds the token. Deleting mail is switched off by an administrator. Forwarding to outside domains is blocked. Sending needs a person.

These are the controls platforms are good at, and they matter more than they look. The difference between an administrator and an ordinary user is one of the oldest controls in computing, and it is still the one that decides most of what an agent can reach. Secrets held by the platform rather than the agent, tools switched off rather than discouraged, an identity per agent rather than a shared login: each of these is a **boundary** in the behaviour policy's terms, enforced by something the agent's own grant does not include, and so a real control.

They are also less obvious than they sound. When the agent operating a Google Workspace mailbox [measured its own connector](https://abp.sgit.ai/gmail/measured/index.html), on 19 September, it found thirty tools; on that account `send_message` ran with no prompt while trashing a message stopped for an approval. The mechanics are where a policy starts, and getting them right takes measurement, not reading the documentation.

## Above the mechanics is the business

Go one layer up and the rules stop being the same in every company.

**The function.** How this firm does email. Reply inside existing threads; a new recipient needs a person. Never quote a price or a discount; pricing goes to sales. Every sent mail is copied to a log the agent cannot edit.

**The process.** The steps a piece of work goes through. An invoice goes out only after finance has approved it in the ledger. No email tells a candidate the outcome of a hiring decision. A complaint reaches a named person within one working hour.

**The relationship.** Who this customer is to us, right now. During an open dispute, nothing goes to that client except through legal. Key accounts get a reviewed draft rather than a sent mail.

**The organisation.** What the company is for. Treat customers fairly: no pressure, no hidden terms. Or, in another company, win back every customer who cancels.

None of these is exotic. Each is a sentence a manager would say out loud. Together they are the firm's business logic as it applies to one agent doing one job, and each layer has a different owner: IT and security, the head of operations, finance and HR and legal, the account managers, the board.

## Why the vendors stop at the mechanics

A platform that sells agent controls is in a catch. It has to add value to every customer, and it has to scale, so it builds what is the same for everybody: roles, switches, secret stores, tool permissions, approval prompts. Those are worth having. But the layers above are different in every company, they change every week, and in many companies they are not written anywhere a product could read them. A vendor that tries to model each customer's business becomes a consultancy; one that does not is left selling the bottom of the stack.

That is not a criticism of the vendors. It is the shape of the problem. The mechanical layer is a product. The business layers are the customer's, and the customer has to write them.

## Software was the law

Why have so many companies never written this down? Because they did not need to. Their software was the law.

For decades the rules of engagement lived in the systems people used. A clerk could not send an unapproved invoice because the finance system had no button for it until the approval was recorded. A support agent could not see a customer's payment details because their role did not include the screen. Approval chains, role-based access control, field-level permissions, workflow engines: these are business logic, encoded in software, and often far more complex than anybody would choose to write in prose. They are also important. They are where privacy decisions live, who can see what, who can do what, and much of what governance means in practice.

An agent breaks that arrangement. It works through APIs, not screens. It can call the endpoint the button would have called, without the screen that hid the button. The rule that the user interface enforced by omission is no longer enforced, unless somebody writes it down and something enforces it. The behaviour policy is where it gets written down.

## Policies inside policies

The structure I have found that can hold this is a fractal one: behaviour policies inside behaviour policies, each layer refining the one below, inside the room the one below allows.

At the bottom are the foundational controls: identity, secrets, what the platform switches on and off, a few levels of privilege from administrator upwards. Above them, the soft controls that the agent enforces on itself, or that another agent checks. Above those, the function, the process, the relationship. And at the top, whatever the company says it is for. That top layer is the company's to define. It might be to treat customers fairly. It might be to maximise revenue from every account. A behaviour policy describes; [it does not judge](https://riskmandate.ai/abp.html). But a policy that is written down can be read, and a company whose top layer says it treats customers fairly, with the layers beneath to show it, has something to show that a company without one does not.

This is the same grammar as the rest of the site's [fractal semantic graphs](introducing-fractal-semantic-graphs.md): the same small set of rules at every level, so one reader and one set of tools work from the board's principle down to a single tool permission. It is also how the behaviour policy itself is already built. The ABP's vocabulary is [three layers](https://abp.sgit.ai/model/graph/layers/index.html): shared facts owned by nobody, each party's own formulas over those facts, and declared bridges between vocabularies. A customer extends it by adding nodes in its own vault, never by asking for a change in ours.

## How much of it is hope?

The worked example, counted. Each rule is backed by a control, governed by an accepted risk with an owner and an expiry, or resting on hope. The proportions are illustrative; the shape is the point.

Once the rules are written in layers, a question becomes answerable that is usually only felt: how much of this agent's behaviour is actually enforced?

The behaviour policy already records, for every rule, which of four things stands in the way: nothing, an **expectation** (a rule in prose, enforced by nobody), a **setting** the agent's own account can flip, or a **boundary** enforced above it. Only the last is a control. Add one more fact, whether a named person has accepted the risk of the rule not being enforced, with an expiry, and every rule lands in one of three states: backed by a control, governed by an accepted risk, or resting on hope.

In the example, five of the seventeen rules are backed by a control, six are governed by an accepted risk, and six are hope. The shape is the finding. The platform layer is all control. The organisation layer is all hope. In between, the more specific a rule is to this firm, the more it rests on the agent behaving and on somebody having [accepted that it might not](every-risk-is-already-accepted.md). That is not a failure; most of a business has always run on people behaving as asked. But it is worth knowing which is which, and with an agent it can be counted.

## Where the vendors plug in

Five rules from the example, and the control that would move each one. Every control is a kind of product that already exists; what is new is that it enforces a rule the customer wrote.

This is also where the catch for vendors comes undone. A vendor does not have to model the customer's business. It has to enforce the parts of the customer's written policy that its product can reach.

A send gateway that holds mail to an address the thread has not seen moves "a new recipient needs a person" from an accepted risk to a control. An outbound content check moves "never quote a price" from hope to a control. A finance system that answers "is this invoice approved?" to a gateway the agent cannot reach moves the invoice rule. A blocked-recipients list that legal maintains moves the dispute rule. The principle at the top has no single control, but sampling sent mail against it, with a named reviewer, turns hope into an accepted risk.

Each of these is a product somebody already sells. What changes is that it now enforces a rule at the layer the customer wrote it, and the policy can count the move. A control attached to a written rule is worth more than one switched on in general, because the customer can see what it bought. That is why I think the behaviour policy is a good place for vendors to integrate rather than a threat to them: it gives their controls a rule to enforce and a number to move, and it lets several vendors each own a different row without any of them having to own the whole business.

It is also why the frameworks are starting to ask for this. The [AI Baseline Control Framework](ai-baseline-control-framework.md) asks, in RG.2, that for every AI system acting autonomously "what it does is described", and, in AC.3, that each one has a named owner. The description RG.2 asks for is the layers above the mechanics. The owner AC.3 asks for is the person whose name goes on each layer.

## It looks a lot like a skill

Read the upper layers of the example again and they look less like access control and more like a skill: the instructions that tell an agent how a function is done here. How we answer clients. How an invoice goes out. What we never say about price. A skill file and a behaviour policy layer are written by the same people, about the same work, for the same agent.

The difference is what each one carries. A skill says how. A policy layer says what is allowed, who owns the rule, and what stands in the way of breaking it. Written together, they are the business codified for an agent: the functions, the processes, the relationships and the principles, with the controls and the acceptances attached. That is what lets the business hand real work to agents and still know what it handed over. It is also what lets it scale: the knowledge that lived in a few people's heads, and in software nobody could read, becomes something an agent can follow, a person can review and a control can enforce.

## What comes next

The example here is fictional on purpose, so the shape is clear. The next step is a real one: take the [measured Gmail deployment](https://abp.sgit.ai/gmail/measured/index.html) as the bottom two layers, write the function, process and relationship layers above it for one real inbox, count the three states, and publish it as a vault with its read key. Then do it again with a vendor's control in the path, and publish the count before and after.

*Drafted from a voice note by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026. The firm, its rules and its counts are illustrative. The measured Gmail figures and the ABP's barrier kinds and layers are from abp.sgit.ai and riskmandate.ai as published that day. The kinds of product named in the third figure are categories, not recommendations, and no vendor was contacted.*

## Threads

Agents & policy[This article as a graph →](graphs.md#the-behaviour-policy-is-the-business-logic)

### Builds on

- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.

### Continued by

- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [the-behaviour-policy-is-the-business-logic.jpg](banners/the-behaviour-policy-is-the-business-logic.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-behaviour-policy-is-the-business-logic.html)*
