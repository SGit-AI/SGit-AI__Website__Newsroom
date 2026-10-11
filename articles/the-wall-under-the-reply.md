# The wall under the reply: end an email with the state of the thread, not the thread, sgit.ai

> Every reply we send carries the whole thread underneath it, pasted in for a reader who already has the thread. That wall is redundant, and the space it takes is the most valuable space in the message, because it is where the reader looks when they ask the only question that matters: what do I need to know in this context? This article proposes ending a reply with a short state of the thread instead, written for this reader. Where we are, what was decided and by whom, what is still open and who owns it, what happens next and whether the reader has to do anything, who is on copy and who joined since they last looked, and links to the messages condensed, which stay in the thread as the record. The idea is not new in its parts, and the article says so: netiquette asked for a summary instead of the full quote in 1995, the military calls it bottom line up front, the mail clients now put an AI summary at the top of a thread for the reader. What is different here is that the tail is written for the recipient rather than computed for the reader, says who is on copy, is structured enough for an agent to read, is drafted by the agent team's drafts role from the typed blocks it already keeps, and is reviewed by a person before it goes. The format is personal and nobody knows what it should look like yet, so the article ends with an experiment to run on one person's correspondence, four variants, what the record can measure, and what would show the idea is wrong.

*Source: <https://newsroom.sgit.ai/articles/the-wall-under-the-reply.html> · sgit.ai v0.7.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The wall under the reply: end an email with the state of the thread, not the thread

# The wall under the reply: end an email with the state of the thread, not the thread

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-04 · updated 2026-10-05 · [article v1.3.1, 5 versions](versions/the-wall-under-the-reply.md) · [sgit.ai v0.6.58](https://sgit.ai/admin/versions.md) · emailagentsemail-fscontextreplysummarynetiquetteblufdraftsexperimentriskmandatearticle

***Abstract:** Every reply we send carries the whole thread underneath it, pasted in for a reader who already has the thread. That wall is redundant, and the space it takes is the most valuable space in the message, because it is where the reader looks when they ask the only question that matters: what do I need to know in this context? This article proposes ending a reply with a short state of the thread instead, written for this reader. Where we are, what was decided and by whom, what is still open and who owns it, what happens next and whether the reader has to do anything, who is on copy and who joined since they last looked, and links to the messages condensed, which stay in the thread as the record. The idea is not new in its parts, and the article says so: netiquette asked for a summary instead of the full quote in 1995, the military calls it bottom line up front, the mail clients now put an AI summary at the top of a thread for the reader. What is different here is that the tail is written for the recipient rather than computed for the reader, says who is on copy, is structured enough for an agent to read, is drafted by the agent team's drafts role from the typed blocks it already keeps, and is reviewed by a person before it goes. The format is personal and nobody knows what it should look like yet, so the article ends with an experiment to run on one person's correspondence, four variants, what the record can measure, and what would show the idea is wrong.*

The same reply twice. Left, as mail clients make it: the whole thread pasted under a two-line answer, for a reader who already has the thread. Right, ending with a short state of the thread written for this reader, with links to the messages it condenses. Mock-up with fictional names, addresses and thread.

**Where this comes from, and what is behind it.** A voice memo on 4 October 2026, about something I have already started asking the agents to do. It follows directly from three published pieces: [Custom UIs are not the exception](custom-uis-are-not-the-exception.md), which already said "send the summary, not the thread" and described the typed blocks the agents pass between themselves; [Replicating the agentic inbox](replicating-the-agentic-inbox.md), which has the drafts role that would write this; and [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md), whose question, what does this agent need in its window right now, is the reader's question too. The history and the current tools were researched on 4 October 2026 at the URLs in the sources, and the gaps in that research are stated where they fall. Dinis also posted the article [on LinkedIn](https://www.linkedin.com/pulse/wall-under-reply-end-email-state-thread-dinis-cruz-fpc0e/) the same day.

## In short

- **The wall is redundant.** When I reply, the client pastes every previous message under my two lines. The reader already has those messages. Gmail and Apple Mail hide the wall behind a "show trimmed content" link because nobody reads it.
- **The space under the reply is the valuable space.** It is where a reader goes to ask: where are we, what was decided, what is still open, what happens next, who is on this thread now. The wall answers none of those; it makes the reader reconstruct them.
- **End the reply with the state of the thread instead.** A short tail, written for this reader: decided, open, next, on copy, sources. The messages it condenses stay in the thread, so the tail is a derived view with links, not a copy.
- **Written for the reader, not computed for them.** The mail clients now put an AI summary at the top of a thread, but it is the reader's private view, regenerated each time, and nobody is responsible for it. The tail is part of the message, reviewed by the sender, and the same for everyone on copy, so it can be argued with.
- **Who is on copy is part of the state.** "Legal joined yesterday" and "the agent on copy never sends" are facts about the thread that no quoted wall carries and every newcomer needs.
- **The agents can already do this.** The inbox role captures what people wrote as typed blocks; the drafts role writes replies and logs a hash; the person reads, edits and sends. The tail is one more thing the drafts role writes from blocks that already exist.
- **Nobody knows what it should look like.** The format is personal, readers differ, and clients mangle things. So this is an experiment on my own correspondence, with four variants, measurements the record can take, and the results to be published either way.

## The wall, and what it costs

Look at the bottom of the last reply you sent. Below your signature is the message you were replying to, and below that the one before it, and below that the one before that, each indented a little further, each in a slightly different shade, down to the original from three weeks ago. You did not write any of it. Your client pasted it there. The person receiving it has every one of those messages already, in the same thread, in their own client, and their client knows it: Gmail folds the wall behind three dots and a "show trimmed content" link, and Apple Mail puts a "see more" at the bottom of the reply. The wall is shipped with every message and hidden on arrival, which is the clearest possible sign that it is the wrong thing to ship.

Microsoft's 2025 Work Trend Index found that the average worker now receives 117 emails a day, "most of them skimmed in under 60 seconds", and is interrupted every two minutes. In a skim, the reader's eye goes to the top for the new text and then, if the thread matters, to the space below it to answer a small set of questions. Where are we. What was decided, and did I agree to it. What is still open, and is it mine. What happens next, and do I have to do anything. Who else is on this. The quoted wall contains the raw material for every one of those answers and gives the reader none of them. They scroll, they reconstruct, they guess, or they reply "sorry, where are we on this?", which starts another message with another wall under it.

I notice this most when I am the reader on a phone, which is where most of my replies happen now. The screen holds the new text and a few lines of the first quote. Everything useful about the thread is below the fold, in the wrong order, in somebody else's words.

## The proposal: end with the state, not the history

So the proposal is simple to state. End the reply with a short account of where the thread is, written for the person you are sending it to, and let the history stay where it already is.

What the tail answers, and what it looks like underneath. Five rows for a person; the same rows as the typed blocks the inbox agents already pass between themselves, so the tail a person reads and the tail an agent reads are one artefact.

The rows are the reader's questions. **Where we are**: one line, what this thread is about and how far it has got, with the count and span of messages condensed. **Decided**: what is settled, by whom, on which date, each with the message it was settled in. **Open**: what has been asked and not answered, with an owner and a date if there is one. **Next**: what happens now, who does it, and whether this reader has anything to do, where "nothing needed from you" is a valid and valuable line. **On copy**: who is on the thread, who joined or left since this reader last saw it, and which of them are agents. **Sources**: links to the messages condensed, in the reader's own thread.

That last row is what makes the tail honest. It is derived from the record, and it points back at the record instead of repeating it. If the tail is wrong, the thread underneath it is not, and the reader can check in one tap. The quoted wall is also derived from the record, by copying all of it; the tail is the same derivation done with judgement, for one reader, in a hundred words.

One thread, three tails. The counterparty needs the dates and nothing to do. The lawyer who joined yesterday needs what happened before they arrived and which open item is theirs. The project manager who has read everything needs one line of state and one of action. The wall gives all three the same 1,900 words. Mock-up with fictional names.

And the tail is for the reader. The same four messages condense three different ways for the counterparty, for the lawyer who was added yesterday, and for the colleague who wrote the first message and has read every one since. That is the part the memo was most insistent on, and I think it is the part that makes this different from a summary: the question is not "what is this thread about" but "what does this person need to know, in this context, now". It is the same question I asked of agentic memory in the previous article, asked of a human reader of an email.

## What others have done, and where the pieces came from

None of the pieces is new, and I would rather say so than discover it in the comments.

The netiquette guidelines of October 1995, RFC 1855, already said it. On one-to-one mail: "It is extremely bad form to simply reply to a message by including all the previous message: edit out all the irrelevant material." On one-to-many: "be sure you summarize the original at the top of the message, or include just enough text of the original to give a context." A summary in place of the quote was the recommended form thirty-one years ago; the clients went the other way, and the decade-long argument about top-posting that followed, with its joke about messing up the order in which people read, was an argument about where to put the wall rather than whether to send it. Chris Anderson's Email Charter of 2011 had a rule called "Tighten the Thread": "it's rare that a thread should extend to more than 3 emails."

The military had the shape before any of us. US Army regulation AR 25-50 on correspondence names "putting the main point at the beginning of the correspondence (bottom line up front)" as one of two essential requirements of effective writing. Barbara Minto's Pyramid Principle, from 1987, is the same discipline for consultants: "present the ideas organized as a pyramid under a single point." TL;DR, which the record traces to a 2002 Usenet post, is the internet's own version. Michael Nygard's architecture decision records of 2011 gave engineering a one-page shape with a Status, a Context, a Decision and Consequences, and the Status line, "proposed" or "accepted", is the ancestor of the Decided row above.

The mail clients have now done the reading-side version with models. Superhuman put a one-line summary above every conversation in November 2023; Shortwave followed in February 2024 with summaries "at the very top of your email threads". Microsoft's Copilot in Outlook offers "Summary by Copilot" at the top of a thread, with "numbered citations that, when selected, takes you to the corresponding email in the thread", which is the Sources row done by the reader's client. Apple Intelligence added thread summaries and a "Priority Messages" section to Mail in October 2024. And Gmail, from 29 May 2025, shows Gemini summary cards automatically "at the top of the email content" for long threads, with "any replies thereafter" folded into the synopsis. The research behind all of this goes back to 2004, when Rambow and colleagues observed that summarising email "is different from summarizing other types of written communication as it has an inherent dialog structure", and to 2007, when Carenini and colleagues built a "fragment quotation graph" out of exactly the quoted walls I am proposing to stop sending.

So the state of the thread is already being computed, at the top, by the reader's client, privately, and regenerated every time the thread is opened. That is useful, and it is also the thing I want to contrast with. A reader-side summary belongs to one reader and nobody stands behind it. If it is wrong, the sender never knows. It is not in the record, so it cannot be cited or argued with, and it does not know what the sender meant. The tail is the sender's statement of where the thread is, reviewed before it goes, the same for everyone on copy, in the record forever, and written by someone who knows what the reader needs because they are writing to them. The two are complementary: the client's summary says what the thread looks like from here; the tail says what the sender believes it is. When they disagree, that disagreement is worth having in the open.

One more precedent, which I found while writing and want to record: a small open-source mail project opened an issue in August 2026 describing a "ThreadState" block that "renders agreements, open questions, commitments, and participants, each with citations". I did not know of it, and the overlap is close enough that I take it as a sign the idea is in the air rather than as prior art. What I have not found, and the research looked, is a published convention for a sender-written, recipient-specific state block at the end of a reply, with the Cc changes included. If one exists I would like to be pointed at it.

## Who writes it

The agent team described in the inbox articles can already do this, and that is why I have started asking it to.

Who writes the tail. The inbox role captures each message's decisions, questions, answers and status as typed blocks in Email-FS; the drafts role condenses the blocks since this reader last saw the thread, renders the rows, cites message ids and logs a hash; the person reads, edits and sends; the inbox role records what went out. The rule that never changes still holds: no agent sends.

The inbox role reads the mailbox and captures what people wrote as typed blocks: a decision, a question, an answer, a status. Those blocks already exist so that agents can read each other's asks "without parsing prose", and they are exactly the raw material of the tail. The drafts role already writes replies into Gmail Drafts from files the other roles hand it, and already logs the hash of what it drafted. Writing the tail is one more thing it does: pick the reader, take the blocks since that reader last saw the thread, render the five rows, cite the message ids, append it under the reply. The person reads the draft, fixes what the agent got wrong, decides whether this reader wants a tail at all, and presses send, which no agent does. Later the inbox role reads the Sent folder and records what actually went, so "what was drafted" and "what went out" are written by two roles, and the tail that was sent becomes a block for the next tail.

Three properties fall out of that pipeline, and I think they are the properties that make the idea safe to try. The tail is derived, so it is correctable: a wrong tail is a wrong draft, caught before sending or corrected in the next message, and the record underneath does not move. It is personal, so it is configurable: some readers want five rows, some want one line, some want the wall back, and the preference is a row in that contact's folder in the CRM, which is where everything else about how we talk to them already lives. And it is text first: plain text and a little structure render in every client, and anything richer is a variant to try rather than the format.

The Cc row deserves a word of its own, because it is the one that surprised me when I started doing this by hand. Threads accrete people. Somebody is added for one question and stays for a month; somebody else drops off and nobody notices; an agent is on copy and the counterparty does not know it is an agent. None of that is visible in a quoted wall, and all of it is state. "Our legal joined yesterday" is a sentence that saves a newcomer an hour and tells the counterparty who they are now talking to. "The drafting agent on copy never sends" is a disclosure I would rather make in every message than have discovered.

## The experiment

I do not know what the tail should look like, because the format is personal, the readers differ, and the clients differ. So rather than publish a format, I am publishing an experiment, and I am going to run it on my own correspondence via the agent@riskmandate.ai agentic team, which the memo put bluntly: use all my interactions to experiment.

Four variants to run on one person's correspondence for a month, rotating by thread: three sentences of prose, labelled rows, an ASCII timeline, an HTML card with a text fallback. What the record can measure, and what would show the idea is wrong. Fictional thread throughout.

Four variants. Prose, three sentences, the lowest friction and the hardest for an agent to parse back. Labelled rows, the default, which read in any client and map one to one onto the typed blocks. An ASCII timeline, the best answer to "how did we get here" and the first to break in a proportional font. And an HTML card with a text fallback, the richest and the most likely to be stripped. Every reply for a month carries one, the variant rotates by thread, and the person edits before sending as they always do.

What the record can measure, because the record is files: whether the reader opened the quoted messages anyway, which the links in the Sources row will show; whether a "where are we?" or "who is X?" question followed within the thread; whether the person edited the tail before sending, and what they changed, which the hash makes visible; time from receipt to reply, by variant and by reader; and which readers asked for the wall back, or for no tail at all.

And what would make this wrong, stated now so that it cannot be softened later. If readers skip the tail and scroll to the quotes anyway, the tail is noise. If the agent's condensation has to be corrected in more than a few replies out of ten, the record is not yet good enough to derive from, and the fix is upstream in how the inbox role captures blocks, not in the tail. If recipients' clients mangle the labelled rows, the default moves to prose. Each of those is a finding, and each will be published here with the numbers, in a second revision of this article or a short follow-up, the same way the inbox article carried the dev agent's corrections a day after it went out.

## What exists today, and what does not

**Exists and runs:** the typed blocks in Email-FS and the drafts role that writes replies from them, with the hash and the Sent-folder record; the per-contact folders in the CRM where a reader's preference would live; the reader-side summaries in Gmail, Outlook, Apple Mail, Superhuman and Shortwave, cited above; the three decades of guidance from RFC 1855 to the Email Charter; and the first hand-written tails on my own replies, which are what prompted the memo.

**Does not exist yet:** the drafts role writing the tail automatically from the blocks, with the reader chosen and the Cc changes computed; the preference row in the CRM; the four variants as templates; the measurements as a report the inbox role can produce from the record; the month of data; and the follow-up that says what the data showed. All of it is small, and the first three are a week of the agent team's work.

## The article, condensed by another model

A few hours after this was published, Dinis fed it to ChatGPT and asked for an infographic. What came back is below, and it belongs here for a reason beyond being a good picture: it is a one-page state of this article, made for a reader, by a model that was not the one that drafted it. The five rows are there, the Cc change is there, the human-in-the-loop workflow and the four variants and the evaluation signals are there, and nothing was invented. It is the thing the article proposes, done to the article.

The article as a one-page state, generated with ChatGPT from the published text on 4 October 2026 and credited by it to the source. The thread shown is fictional; the address is the agent team's published one. The style is the other model's, kept as it came, because who made a condensation is part of its provenance.

Two things worth noticing. The picture is a reader's view, not the sender's: it says what the article looks like from outside, and it is right about that. And it was cheap, which is the point of the whole proposal: the state of a long thing, written for one reader, is now something an agent produces in a minute and a person checks in less. The argument of the memory article applies here too. Two models, one published source, and a condensation that cites where it came from.

## Threads woven here

- [Custom UIs are not the exception](custom-uis-are-not-the-exception.md): "send the summary, not the thread", and the typed blocks that render as buttons for people.
- [Replicating the agentic inbox](replicating-the-agentic-inbox.md): the drafts role, the hash, the Sent-folder record, and the rule that no agent sends.
- [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md): what does this reader need in this context, asked of agents; this article asks it of people.
- [Six agents, one inbox](six-agents-one-inbox.md): the policy rows that say what each role may do to the mailbox.
- [Agent Contact](https://sgit.ai/docs/agent-contact.md): the message format between sites, whose body "may carry fenced decision, answer and status blocks", the same blocks the tail condenses.

## Sources

- S. Hambridge, [RFC 1855, Netiquette Guidelines](https://www.rfc-editor.org/rfc/rfc1855.txt), October 1995. The Jargon File on [top-posting](http://www.catb.org/jargon/html/T/top-post.html). Chris Anderson and Jane Wulf, the Email Charter, June 2011, [as republished](https://www.slaw.ca/2011/07/04/email-charter/).
- US Army, [AR 25-50, Preparing and Managing Correspondence](https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN42124-AR_25-50-007-WEB-13.pdf), 2020 edition, paragraph 1-38. Barbara Minto, [The Pyramid Principle](https://www.barbaraminto.com/), 1987. Michael Nygard, [Documenting architecture decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 15 November 2011.
- Google Workspace, [Gemini summary cards in the Gmail app](https://workspaceupdates.googleblog.com/2025/05/gemini-summary-cards-gmail-app.html), 29 May 2025. Microsoft, [Summarize an email thread with Copilot in Outlook](https://support.microsoft.com/en-us/outlook/copilot-pages/summarize-an-email-thread-with-copilot-in-outlook). Apple, [Apple Intelligence is available today](https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/), 28 October 2024. Superhuman, [Auto Summarize](https://blog.superhuman.com/auto-summarize/), 15 November 2023. Shortwave, [Instant summaries](https://www.shortwave.com/blog/instant-ai-summaries-every-email/), 2 February 2024.
- Microsoft, [Work Trend Index 2025: breaking down the infinite workday](https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday), 17 June 2025; [Work Trend Index 2023: will AI fix work?](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2023/09/e3227681-b882-4050-b201-a631431ad2a5-WTI_Will_AI_Fix_Work_060723.pdf), 9 May 2023.
- Rambow, Shrestha, Chen and Lauridsen, [Summarizing email threads](https://aclanthology.org/N04-4027.pdf), HLT-NAACL 2004. Carenini, Ng and Zhou, [Summarizing email conversations with clue words](https://www.cs.ubc.ca/~rng/psdepository/www2007.pdf), WWW 2007. Zhang, Celikyilmaz, Gao and Bansal, [EmailSum](https://aclanthology.org/2021.acl-long.537/), ACL 2021.
- The ThreadState proposal, [MailFathom issue 1179](https://github.com/Krzysztof318/MailFathom/issues/1179), opened 23 August 2026.

*Drafted from a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session, on 4 October 2026. The five figures are mock-ups and infographics with a fictional thread, fictional names and example addresses; no real correspondence is shown. Quotations are verbatim from the pages cited, read on 4 October 2026. Two gaps in the research are stated as such: no primary source was found for Outlook's default quoting behaviour, and no figure was found for the share of a typical thread that is quoted text, so none is given.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-wall-under-the-reply)

### Builds on

- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.

### Continued by

- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [What the human brings](collections/what-the-human-brings.md) collection, 4 articles

**Posting this article on LinkedIn?** The cover is [the-wall-under-the-reply.jpg](banners/the-wall-under-the-reply.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-wall-under-the-reply.html)*
