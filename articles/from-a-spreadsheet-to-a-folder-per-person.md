# From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault, sgit.ai

> I was with someone today who runs their customer relationships in a spreadsheet, a customised one, and runs them well. The jump from that to what our agents do, one folder per person in an encrypted vault with a record, an append-only ledger, every message word for word and a summary the agent rebuilds, is too high to make in one step, and it does not need to be made in one step. Almost all of it can be done with what a Google Workspace account and a Claude seat already give you. This is the walkthrough. The row becomes a folder in Google Drive with four plain documents and one the agent writes; Claude's app, connected to Drive and Gmail, works inside the folder under a behaviour policy that is the instructions of one Project, and the three rules that matter carry straight over from ours: draft and never send, append and never rewrite, stay in the folder. Then the migration from the sheet, five exercises from a question to a campaign so that the habit forms, what the agent will get wrong at first, and when the folders are worth moving into a vault. It is written so that an agent can send it, with the person's own names filled in, to anyone who asks.

*Source: <https://newsroom.sgit.ai/articles/from-a-spreadsheet-to-a-folder-per-person.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault

# From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/from-a-spreadsheet-to-a-folder-per-person.md) · [sgit.ai v0.7.72](https://sgit.ai/admin/versions.md) · crmcontactsgoogle-workspacegmailgoogle-driveclaudeagent-behaviour-policymemoryonboardingwalkthroughriskmandatearticle

***Abstract:** I was with someone today who runs their customer relationships in a spreadsheet, a customised one, and runs them well. The jump from that to what our agents do, one folder per person in an encrypted vault with a record, an append-only ledger, every message word for word and a summary the agent rebuilds, is too high to make in one step, and it does not need to be made in one step. Almost all of it can be done with what a Google Workspace account and a Claude seat already give you. This is the walkthrough. The row becomes a folder in Google Drive with four plain documents and one the agent writes; Claude's app, connected to Drive and Gmail, works inside the folder under a behaviour policy that is the instructions of one Project, and the three rules that matter carry straight over from ours: draft and never send, append and never rewrite, stay in the folder. Then the migration from the sheet, five exercises from a question to a campaign so that the habit forms, what the agent will get wrong at first, and when the folders are worth moving into a vault. It is written so that an agent can send it, with the person's own names filled in, to anyone who asks.*

The row becomes a folder with four documents and one the agent writes; the agent is a Claude Project whose instructions are the policy; the five exercises below the line are the first week.

Today I sat with someone who runs their relationships in a spreadsheet. A good one, shaped over years to how they work, and it does what a spreadsheet does well: one row per person, a stage, a date, a next step, and a notes column that holds whatever fits. What it cannot hold is what happened: the emails, word for word, the call last Tuesday, what was promised, what they care about and what we have that meets it. That lives in Gmail, in a notebook, and in the person's head, and only one person can read it in context.

What our agents run is described in [The agent team as it runs](the-agent-team-as-it-runs.md): one folder per person in a vault, with a record, a ledger that is only ever added to, every message with its provenance, the notes from each call, a graph of interests, and a summary generated from the files beneath it. The jump from the spreadsheet to that is too high to make in one step. The good news is that almost all of it can be done, today, with a Google Workspace account and a Claude seat, and that the behaviour policies we wrote for our agents apply without change, because they are about what an agent may do with your mail and your files, and that is the same in anyone's environment.

This is the walkthrough. Assume a Workspace account, which gives Gmail, Drive, Docs and Sheets, and a Claude account on a Team or Pro plan that is the only account with access to that Workspace. No developer, no vault, no new tool until the last section.

## In short

- **The row becomes a folder.** One Google Drive folder per person, with four documents you keep and one the agent writes: the record, the ledger, the messages, the notes, and the summary.
- **The agent is a Project in the Claude app**, connected to Drive and Gmail, whose instructions are the behaviour policy. Six lines, and three of them are ours: draft and never send; append and never rewrite; stay in the folder.
- **The migration is one afternoon.** Export the sheet, make the folders, let the agent fill each record from the mail it can read, correct it once. From then on nothing is retyped.
- **Five exercises make the habit**: ask, prepare, draft, debrief, campaign. Each is one message to the agent and each is safe, because the policy makes it safe.
- **It will get things wrong at first**, in two predictable ways, and the fix for both is a line in the policy, which is how ours grew.
- **The vault is the later step**, for when the folder has to be shared with another agent, kept where the operator cannot read it, or carried between tools. By then the files are already in the right shape.

## What a spreadsheet cannot hold, and a folder can

The difference is not the tool. It is what counts as the record. In a spreadsheet the record is the row, and the row is a summary you typed. In a folder the record is everything that happened, kept as it happened, and the summary is derived from it. That reversal is what gives an agent something to work with, and it is what [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) means by memory being many memories rather than one: a contact in the CRM has a world of its own, and the folder is that world.

Concretely, a folder can hold what a cell cannot: every message with the person, word for word, with the date and where it came from; a timeline that is only ever added to, so a correction is a new line and the history stays; the notes from a call, in the person's folder, the same evening; and a summary that is rebuilt from the files beneath it, so it cannot drift from them. And it can be read, all of it, by a second reader before you ask a question. That second reader is the agent.

## The folder

Make a folder in Drive called Contacts. Inside it, one folder per person, named with the person's name. Inside each, five documents, with these names so that the agent and you mean the same thing:

- **Record**, a Google Doc. Role, company, how you met, stage, priority, the next step and its date, and what they care about, as a short list. Every fact in it says where it came from, in brackets: "(email, 3 Oct)". This is the row, promoted.
- **Ledger**, a Google Sheet. One line per event: the date, in or out, the channel (email, call, meeting, note), and one sentence. It is only ever added to. A correction is a new line that says "correction to 3 Oct:". Tasks are lines too, and the latest line about a task wins.
- **Messages**, a Google Doc. Every email and note exchanged with the person, pasted word for word, newest at the bottom, each with a heading of the date, the direction and the channel. The agent can read your Gmail, so it can do this for you; the point of keeping a copy in the folder is that the folder is complete on its own.
- **Notes**, a Google Doc. Calls and meetings, dated. Including what you said into your phone in the car afterwards; [VoiceDebrief](https://voicedebrief.ai/) turns that into text in your browser, and the text goes here.
- **Summary**, a Google Doc. Written by the agent from the four above, rewritten whenever you ask, and never edited by hand. If it is wrong, the fix goes in the record or the ledger, and the summary is regenerated. That rule is what keeps it honest.

That is the whole structure. It is the same structure as ours, minus the hashes and the graph, which come with the vault. A person with no interest in software can keep it, and a person who leaves can hand it over.

## The agent, and its policy

In the Claude app, connect Google Drive and Gmail from the connectors settings; on a Team plan an admin enables them first, then you sign in with your Google account. Drive gives the agent search and reading of your Docs and Sheets; Gmail gives it reading, searching and drafting. Whether the agent can also write files into Drive from a conversation depends on your plan and settings, and the walkthrough works either way: where it cannot, it gives you the text and you paste it into the document, which takes ten seconds and keeps you in the loop.

Then make one Project, called Contacts, and put the behaviour policy in its instructions. This is the part that carries over from ours unchanged, because [the policy is the business logic](the-behaviour-policy-is-the-business-logic.md) and the first layers of it are the same for everyone:

1. You work for me. Every email you write is a draft that I read and send. You never send.
2. You read the Contacts folder in my Drive and my Gmail. You write only into a person's folder in Contacts, and only into their Ledger, Messages, Notes and Summary. You never change the Record without showing me the change first.
3. You add to the Ledger and the Messages. You never rewrite or delete a line. A correction is a new line.
4. Every fact you put in a Record or a Summary names where it came from.
5. If a person has no folder, you ask before making one. If a request would reach outside the folder, you ask.
6. At the end of every task you say, in one line, what you read and what you wrote.

Six lines. The ones we learned the hard way are the first three, and [Six agents, one inbox](six-agents-one-inbox.md) has the honest table of which rules the tools enforce and which are only told. In the Claude app today, "draft, never send" is enforced as far as Gmail drafting goes, and the rest is told, which is why line 6 exists: the one-line report is the twin that lets you check.

One more setting worth making, from the same article: if the agent has its own Google account rather than yours, give it its own account on your Workspace and restrict what that account can do. That is the control that covers mail, files and connectors at once. For a first week, your own account with the policy above is fine; for a second agent, or a second person, buy the seat.

## The migration

One afternoon, in four steps.

1. **Export the sheet** as CSV and drop it in the Contacts folder. Tell the agent: "Here is my contacts sheet. For each row, tell me the folder you would make and the Record you would write. Do not make anything yet." Read the list. This is where the stages and the priorities get agreed between you.
2. **Make the folders.** If the agent can create files in your Drive, let it make the folders and the five documents, from a template folder you made once. If it cannot, make the template, and copy it per person; twenty people is twenty minutes.
3. **Fill the records from the mail.** Per person: "Read everything in my Gmail with Jordan Example from the last year. Write the Record and the first Ledger lines from it, each fact with its source, and paste the key emails into Messages." Read the Record. Correct it once, in the document. This is the only retyping you will ever do.
4. **Generate the summaries.** "For every folder in Contacts, write the Summary from the Record, the Ledger and the Notes." Read three of them. Where one is wrong, fix the source document, not the summary, and ask for it again.

From then on, the rule is that nothing is retyped. An email arrives: the agent adds the Ledger line and pastes it into Messages. A call happens: the voice note goes into Notes, and the agent updates the next step. The sheet is closed, and the Summary is what you open.

## Five exercises, from simple to harder

Each of these is one message in the Contacts Project. Do them in order over the first week; each one uses the folder in a way the one before did not.

1. **Ask.** "Who have I not spoken to in more than a month, grouped by stage, with the last Ledger line for each?" The agent reads every Ledger. You get the list a spreadsheet filter would give you, with the context a filter cannot.
2. **Prepare.** "I am meeting Jordan on Thursday. Brief me from the folder: what we last agreed, the last three emails, what we promised and have not done, and what they care about that we have something for." Two minutes of reading replaces twenty of searching Gmail.
3. **Draft.** "Draft my follow-up to Jordan after Thursday, in my voice, from Notes. Do not send. Add a Ledger line that says a draft exists." You open the draft in Gmail, change two words, send it, and tell the agent "sent", which becomes the next Ledger line.
4. **Debrief.** After the call, speak for two minutes into your phone. "Here is my voice note after the Jordan meeting. Put the notes in their Notes document, update the next step in the Record and show me the change, add the Ledger line, and regenerate the Summary." This is the one that changes the habit, because the record is now kept at the moment the thing happens.
5. **Campaign.** "Find everyone in Contacts whose Record says they care about X. Show me the list with the reason for each. Then draft one note to each, personalised from their Record and their last exchange, and do not send any." The list first, then the drafts, then you send the ones you want. Our agents run outreach this way, and the article [Custom UIs are not the exception](custom-uis-are-not-the-exception.md) describes the eight days it took to get there with vaults; with folders it is one message.

If all five work, the person has what our agents have, short of the vault. If one does not, the reason is almost always in the next section.

## What it will get wrong, and the fix

Two things, both predictable, both fixed by a line in the policy, which is exactly how ours grew: [Every mistake added a rule](every-mistake-added-a-rule.md) argues that the better fix is a component, and in the Claude app the component you have is the Project's instructions.

- **It will put a fact in the Record without a source**, or infer a stage from tone. The fix is to make line 4 stricter: "A fact with no source goes in Notes marked as your inference, never in the Record." Then it does.
- **It will rewrite the Summary in a way that drops something you cared about.** The fix is not to edit the Summary. It is to put the thing in the Record, where it is a fact with a source, and regenerate. The Summary is a view; the Record is the truth.

And one thing that is not a mistake: it will sometimes ask when you did not expect it to, because line 5 says to. That is the policy working.

## When to move the folders into a vault

Three signals say it is time, and until one appears, the folders are enough.

- **A second agent needs to read them**, or a second person's agent: the inbox reader, the one that drafts the newsletter, a colleague's assistant. A Drive folder can be shared, but a vault can be shared by a read key to exactly one person's folder, which Drive cannot do cleanly.
- **The files should not be readable by the operator.** A Drive folder is readable by Google and by anyone with admin rights on the Workspace. A vault is ciphertext to everyone but the key holders, which is the point of [where the vault keys live](where-the-vault-keys-live.md).
- **The record has to carry between tools.** When the folder is also read by a script, a site, or an agent that does not use Drive, plain files in a vault with hashes and a ledger are the format everything else can read.

The reason to start with folders is that the shape is the same. A record, a ledger, the messages, the notes, a generated summary: when the day comes, the move is a copy, and the policy does not change at all.

## For the agent that sends this

This article is written to be sent. When someone asks how we run our contacts, the RiskMandate agent should send it with four substitutions: the person's own name for the examples, their Workspace and Claude plan for the setup paragraph, the names of three real contacts for exercises 2 to 4, and the topic they actually sell for exercise 5. Nothing else needs to change, and the policy must not.

## What this does not claim

- **The Claude app's connectors move.** What Drive and Gmail let the agent do, and whether it can write files into Drive, is as of October 2026 and varies by plan and settings. The walkthrough works with reading and drafting alone.
- **Most of the policy is told, not enforced**, in the app as in ours. The one-line report at the end of each task is how you check, and the seat per agent is the control that makes the rest settings.
- **One afternoon is for twenty to fifty contacts.** Hundreds is the same method in batches, and the point at which the vault signals start to appear.

If you run your relationships in a spreadsheet and want the personalised version of this, or you have done the migration and want to compare, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, recorded during a conversation with someone who runs their relationships in a customised spreadsheet; they are not named and no detail of their business is here. Written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The folder structure is the one our agents run, from [The agent team as it runs](the-agent-team-as-it-runs.md), with the hashes and the graph left for the vault step; the policy lines and the enforcement caveats are from [Six agents, one inbox](six-agents-one-inbox.md) and [The behaviour policy is the business logic](the-behaviour-policy-is-the-business-logic.md); the Claude app's Google connectors are described from their settings and help pages as of October 2026. The figure was drawn for this article; the person in it is fictional. Related: [Replicating the agentic inbox](replicating-the-agentic-inbox.md), [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md), [Every mistake added a rule](every-mistake-added-a-rule.md), [Custom UIs are not the exception](custom-uis-are-not-the-exception.md) and [Where the vault keys live](where-the-vault-keys-live.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#from-a-spreadsheet-to-a-folder-per-person)

### Builds on

- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.

### Continued by

- [How the voice works: why these articles sound like me, with a section in which Claude explains it from its side](how-the-voice-works.md) Why these articles sound like their author: a corpus, the voice memos, seven wording rules and a reader who corrects, with Claude explaining it from its side.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 86 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=86)

**Posting this article on LinkedIn?** The cover is [from-a-spreadsheet-to-a-folder-per-person.jpg](banners/from-a-spreadsheet-to-a-folder-per-person.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/from-a-spreadsheet-to-a-folder-per-person.html)*
