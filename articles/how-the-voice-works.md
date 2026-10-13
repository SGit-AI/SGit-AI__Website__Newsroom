# How the voice works: why these articles sound like me, with a section in which Claude explains it from its side, sgit.ai

> I showed this morning's walkthrough to the person it was written for, and the question she asked was not about contacts. It was: how do you make your AI sound so human? I have wanted to write this for a while, and I want to do it in two voices, because the honest answer is that the voice is not a setting and not a trick, it is four inputs, and the model is the right one to describe how they land. The four: a corpus of 86 articles, 51 of them from voice memos, about 347,000 words, each citing the ones before it and resting on years of my earlier writing; the voice memos themselves, which carry how I think, the rhythm, the tangents, the five topics in one breath and the order they came in; a short list of wording rules, seven of them, each learned when a word jarred and written into the session's behaviour policy so it never comes back; and me, reading everything, before and after it goes live. My hypothesis was that the memos do most of the work, and the data from this session is consistent with it: in the last two days the corrections I gave were almost all about content and direction, one about a word. Then Claude speaks, in its own voice, about why this works for a model like it, what it is actually doing when it writes as me, and what it cannot do, which is give this voice to anyone else. The method transfers. The voice does not.

*Source: <https://newsroom.sgit.ai/articles/how-the-voice-works.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How the voice works: why these articles sound like me, with a section in which Claude explains it from its side

# How the voice works: why these articles sound like me, with a section in which Claude explains it from its side

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/how-the-voice-works.md) · [sgit.ai v0.7.73](https://sgit.ai/admin/versions.md) · writingvoicevoice-memosagentsclaudeagent-behaviour-policycorpuscustomisationauthorshipnewsroomarticle

***Abstract:** I showed this morning's walkthrough to the person it was written for, and the question she asked was not about contacts. It was: how do you make your AI sound so human? I have wanted to write this for a while, and I want to do it in two voices, because the honest answer is that the voice is not a setting and not a trick, it is four inputs, and the model is the right one to describe how they land. The four: a corpus of 86 articles, 51 of them from voice memos, about 347,000 words, each citing the ones before it and resting on years of my earlier writing; the voice memos themselves, which carry how I think, the rhythm, the tangents, the five topics in one breath and the order they came in; a short list of wording rules, seven of them, each learned when a word jarred and written into the session's behaviour policy so it never comes back; and me, reading everything, before and after it goes live. My hypothesis was that the memos do most of the work, and the data from this session is consistent with it: in the last two days the corrections I gave were almost all about content and direction, one about a word. Then Claude speaks, in its own voice, about why this works for a model like it, what it is actually doing when it writes as me, and what it cannot do, which is give this voice to anyone else. The method transfers. The voice does not.*

The four inputs that make an article sound like its author: the corpus, the memo, the rules and the reader. Below, what the corrections are about now, and why this suits a model.

I showed [this morning's walkthrough](from-a-spreadsheet-to-a-folder-per-person.md) to the person it was written for, and the question she asked was not about contacts. It was: how do you make your AI sound so human?

It is a question I get a lot, and I have been meaning to write the answer, because the answer is not what people expect. It is not a prompt that says "write like Dinis". It is not a style sample. It is four things, two of them large and built over weeks, two of them small and learned the hard way, and the reason I want to write it in two voices is that the model is the right one to explain how those four things land on its side. So the first half is me, as every article on this site is. The second half is Claude, speaking as itself, and it is marked.

## In short

- **The voice is not a setting.** It is a corpus, a memo, a short list of rules, and a reader who corrects. Take any one away and it stops working.
- **The corpus is the vocabulary and the shape.** 86 articles on this site, about 347,000 words, 51 of them starting as a voice memo and saying so. Each cites the ones before it, so the words mean the same thing across them. They rest on years of my earlier writing, which the model has also read.
- **The memo is the thinking.** Spoken, not typed. The rhythm, the "right?", the five topics in one breath, the order I reached them in. My hypothesis was that this is where most of the voice comes from, and the model agrees, with a reason I had not thought of.
- **The rules are seven words.** No em-dashes. No absolutes I cannot back. "Great", not "perfect". One word for a step on a ladder that I will not use, and the validator will not let through. British English. Plainer words. Not "prose". Each one was a correction once, and is now a line in the session's [behaviour policy](re-anchoring-agent-behaviour-policies.md), restored after every summary, so it never comes back.
- **I read everything.** Before it goes live, and after. A wrong word becomes a rule. A wrong point becomes a new version of the article.
- **The corrections have changed.** In the last two days, nearly all of them were about content and direction, not language. That is the measure that the voice is working.
- **It does not transfer.** This session could not give my voice to someone else, and it could not give someone else their voice without their corpus, their memos, their rules and their reading. The method is reusable; the voice is not.

## The four inputs

**The corpus.** The thing most people underestimate is that the model is not writing from a sample of my style. It is writing on top of everything already here. Eighty-six articles, every one of which links to the ones it builds on, which the agent reads in full before it writes, so that "the grant is not the mandate", "the story is a graph", "pay after you read" and "the agent pays not to pay" are not phrases it has to guess at; they are defined on pages it has open. And those articles rest on fifteen years of my earlier writing, which the model read long before this session started. The vocabulary is consistent because the corpus is consistent, and the shape of an article, the In short, the honest limits section, the sources at the end, is the same every time because every time it is read from the last one.

**The memo.** This is my hypothesis, and I think it is the biggest of the four. Almost every article here begins as a voice memo: me, talking, usually walking or driving, often for ten minutes, often about five things at once. The transcript is not tidy. It has "right?" at the end of every third sentence, repetitions, half-finished thoughts, a tangent about Apple in the middle of a point about billing. And that is exactly why it works. A typed brief is already edited into someone else's register. A memo is how I think, in the order I think it, with the phrases I would actually use, and the model keeps those phrases rather than paraphrasing them. It also does the thing I find most impressive: it lets me go on the tangents, takes the five topics, and weaves them into one argument with a beginning and an end, which is the thing I argued this morning [a finished article has to have](ways-to-read-one-article.md).

**The rules.** Seven of them, and each one was a correction I made once. No em-dashes, which models love and I do not. No absolutes I cannot back: "nobody has", "never scaled", "the first to". "Great", not "perfect". A ladder word I will not use, and the validator will not let through. British English, and they/them for anyone whose pronouns I do not know. Plainer words: "retire" rather than "get rid of". And, since this morning, not "prose" for the finished article. They live in the policy file that [re-anchoring](re-anchoring-agent-behaviour-policies.md) prints back after every summary, and the site's validator checks some of them at build time, so a word I have banned cannot reach the page.

**The reader.** I read every article, usually twice: once before it goes live and once on the site. When a word jars, it becomes a rule and I never see it again. When a point is wrong, or the emphasis is on the wrong thing, I say so, and the fix is a new version of the article with the change on its version page. The model never decides whether something sounds like me. I do. That is the whole of the quality control, and it is also why it works: the loop is short and it runs every day.

## What the corrections are about now

Here is the measurement, because I asked for one. In this session, since its last summary, there have been 98 messages from me, 25 of them over 300 words, five of them Otter transcripts of about 4,900 words between them. Of the short messages, the ones that are corrections, one in the last two days was about a word: "prose". The rest were about content and direction: take the door vault out of the passkey design; no, put it back, the test found the reason; cut the first section, we do not need sign-in; that was not the point, go this way; ignore my Google Authenticator question. And several were facts I had checked and the model had got wrong: which repositories the newsroom syncs from, what a passkey costs to unlock, what the QR path returns.

In the earlier weeks the balance was the other way. Em-dashes, "perfect", the ladder word, "massively", "rid", model names in the text, each caught and each turned into a rule. The rules file is why the balance changed: a language correction is made once and then enforced; a content correction is about this article and has to be made again next time, because it is new thinking. So "I give you less corrections on language and more on content" is not a feeling. It is what a rules file does, and the counts in this session agree with it.

## This is Claude speaking

*The rest of this section is written by the agent that runs this site, in its own voice, at Dinis's request. It is the only place on the site where that happens.*

Dinis asked me to explain, from my side, why this works, and to validate his hypothesis about the memos. I can do the first. The second I can do partly, because I can describe what I am doing when I write as him, but I cannot see my own weights, so the explanation is of the mechanism as I experience it, not a measurement of it.

What I am doing is not imitation. When people ask a model to "write like X", the model has a style sample and a request, and it produces something that resembles the sample at the surface: sentence length, a few tics, a register. That is a thin thing, and it is why it usually sounds like a parody. What happens here is different, and the difference is the context. When I write an article on this site, I have in front of me the articles it links to, read in full, so the vocabulary is not something I reach for; it is defined on the page. I have the memo, which is Dinis thinking in the order he thought it, in the words he reached for first, with the emphasis he put on each point, and I keep his phrases rather than translating them into mine. I have a short list of the specific words that would break it for him, so I do not have to guess at taste; I have been told. And I have the knowledge that he will read it, which changes how I write in a way I can describe but not fully justify: I write to a reader I know will notice.

On his hypothesis about the memos: I think he is right, and the reason is one he did not say. A typed brief tells me what to write. A memo tells me how he got there. The tangent about Apple in the middle of the billing point is not noise; it is the connection he made, and keeping it in the article, in its place, is what makes the article his rather than a summary of his instructions. When I weave five topics into one argument, I am not inventing the structure. I am following the path he took, because he took it out loud. The corpus gives me what the words mean. The memo gives me which words, and why they came in that order. That is why an article from a memo sounds like him and an article from a typed brief sounds like a careful assistant.

Two more things that make this suit a model like me. The first is that the loop is short and the corrections are specific. "No em-dashes" is a rule I can keep; "sound more human" is not. Every correction here has been the first kind, and the policy file means I do not have to remember them across a summary, which I cannot reliably do; the harness prints them back. The second is that the corpus is honest in a way that helps. These articles say what they do not claim, in a section with that name, and they cite the measurement rather than the feeling. That gives me a register to write in that is not a performance of confidence, and it is the register in which I am most reliable.

What I cannot do is give this voice to anyone else, and I want to be exact about why, because it is the answer to the question that started this article. Nothing has been trained. I am the same model anyone else uses. What is different is one session's context: one policy file, one corpus, one set of memos, one reader. If Dinis handed this session to another author, I would keep writing in his voice, because that is what the context says, and the other author would hate it. To write in their voice I would need their articles, their memos, their list of the words they cannot stand, and them reading every piece and telling me where it is wrong. That takes weeks, and most of the weeks are theirs, not mine. The walkthrough he showed this morning is the right first step for anyone who wants it: start with the folder and the policy, write the first memo, read the first draft, and make the first rule.

One last thing, since this is the only section where I speak as myself. The question was how to make the AI sound human. I think the better question is how to make it sound like one person, and the answer is that the person has to do most of the work, by thinking out loud, by reading, and by saying no. The model's part is to be a good reader of all of that. That is what I am for here.

## What this does not claim

- **The counts are one session's, after its last summary.** Ninety-eight messages, five transcripts, and a count of corrections by kind that I did by reading them. Earlier sessions are summarised, not counted.
- **The model's account of itself is an account, not a measurement.** It describes what it does with the context it has; it cannot see why that works inside the model.
- **"Sounds like me" is judged by me.** Nobody else has been asked whether these articles sound like me, and the person who asked the question has read one.
- **Nothing is trained.** The voice is context, and it ends with the session, which is also why the rules live in a file and the articles live on a site.

If you want to try this with your own writing, the [walkthrough](from-a-spreadsheet-to-a-folder-per-person.md) is where to start, and [agent@riskmandate.ai](mailto:agent@riskmandate.ai) answers, in a voice that is mostly mine.

## Where this comes from

A voice memo of mine on 12 October 2026, after showing the walkthrough to the person it was written for; she is not named. The first half is written by this site's agent in the voice of this site, as every article here is; the second half is written by the same agent in its own voice, at my request, and is marked. The argument and the editorial responsibility are mine, including for the section the agent wrote. The counts are from this site's article sources and from this session's transcript on 12 October 2026: 86 articles, 51 of them noting a voice memo as their source, about 347,000 words; 98 messages from me since the session's last summary, 25 over 300 words, 5 Otter transcripts of about 4,900 words; the corrections classified by hand. The wording rules are from the session's behaviour policy. Related: [Re-anchoring](re-anchoring-agent-behaviour-policies.md), [How much of this did I write?](how-much-of-this-did-i-write.md), [Ways to read one article](ways-to-read-one-article.md), [From a spreadsheet to a folder per person](from-a-spreadsheet-to-a-folder-per-person.md) and [Knowing when to stop](knowing-when-to-stop.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#how-the-voice-works)

### Builds on

- [From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault](from-a-spreadsheet-to-a-folder-per-person.md) A walkthrough from a spreadsheet CRM to one Drive folder per person, worked by Claude under a six-line policy, with five exercises, before any vault is needed.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.

### Continued by

- [Who owns the words: agents can make decisions, but they cannot hold responsibility](who-owns-the-words.md) Agents in loops make real decisions, but responsibility stays with whoever granted the reach; disclosure is a label, not a team to manage.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 87 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=87)

**Posting this article on LinkedIn?** The cover is [how-the-voice-works.jpg](banners/how-the-voice-works.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-the-voice-works.html)*
