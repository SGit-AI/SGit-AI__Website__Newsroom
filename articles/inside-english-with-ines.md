# English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy, sgit.ai

> The brief for an independent English teacher's site, in a teacher and agents she can trust, comes with a worked example you can open: English with Inês, a vault app for a fictional teacher and three fictional students. A student opens it with a link and practises between lessons: four lessons, each with an experiment that explains by moving (a window of time that slides past now, the four ideas the particle up adds, a minimal-pairs listening game, an email to put in order), exercises, cards that come back after one, three, seven and fourteen days, and a tutor that answers only about the lesson on the screen, through the vault's own AI key, which the page never sees. Their progress is saved in their browser, and their path is drawn from a map of thirteen concepts. Then the teacher's side: the pipeline from enquiry to renewal, the students, the weekly brief with three decisions, what is paid for and how, and the seven agents, each with its Agent Behaviour Policy and the barrier that holds each line. It is one HTML file and one JSON file, built and tested in this session.

*Source: <https://newsroom.sgit.ai/articles/inside-english-with-ines.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy

# English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-03 · [article v1.0.0](versions/inside-english-with-ines.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · vaultseducationteachersagentsbehaviour-policiesknowledge-graphsvault-apparticle

***Abstract:** The brief for an independent English teacher's site, in a teacher and agents she can trust, comes with a worked example you can open: English with Inês, a vault app for a fictional teacher and three fictional students. A student opens it with a link and practises between lessons: four lessons, each with an experiment that explains by moving (a window of time that slides past now, the four ideas the particle up adds, a minimal-pairs listening game, an email to put in order), exercises, cards that come back after one, three, seven and fourteen days, and a tutor that answers only about the lesson on the screen, through the vault's own AI key, which the page never sees. Their progress is saved in their browser, and their path is drawn from a map of thirteen concepts. Then the teacher's side: the pipeline from enquiry to renewal, the students, the weekly brief with three decisions, what is paid for and how, and the seven agents, each with its Agent Behaviour Policy and the barrier that holds each line. It is one HTML file and one JSON file, built and tested in this session.*

English with Inês: the home page of the worked example, with the loop around every lesson.

## In short

- **[Open the vault](https://dev.vault.sgraph.ai/#sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc%3A3d0fw3dl):** a teacher's site as a vault app, for a fictional teacher and three fictional students.
- **Four lessons, four experiments** that explain by moving.
- **Exercises and spaced cards,** saved per browser and fed into the student's path.
- **A tutor bound to one lesson,** through the vault's AI key, or a simulation without one.
- **A concept map** of thirteen ideas, and each student's path drawn from it.
- **The back office:** pipeline, students, the weekly brief, billing, and seven agents with their policies.
- **One HTML file and one JSON file;** edit the JSON to make it yours.

## What it is

This is the worked example for [a teacher and agents she can trust](a-teacher-and-agents-she-can-trust.md). Inês is fictional, and so are Rui, Sofia and Tomás, her students. The lessons are real English teaching, the flows and policies are the brief's design, and the app works: open the vault and it starts.

It follows the vault app rules: all its styles and code inline, its content in `content.json` read through the vault host, and a copy inlined so it also works as a plain file. It asks the vault host for one permission, to chat with the vault's AI model, for the tutor.

## The lessons

A lesson: the explanation for a Portuguese speaker, and the experiment, a window of time that slides past now.

Each lesson is written for a Portuguese speaker, because that is who Inês teaches: the present perfect starts from the fact that the pretérito perfeito covers both English tenses, and the pronunciation lesson from the fact that Portuguese has one i sound and English has two. And each has an experiment that explains by moving, the thing I wanted from my own slides:

- **Present perfect or past simple:** drag a window of time; while it closes before now it is the past simple, and the moment it reaches now it becomes the present perfect, with an example for each.
- **Phrasal verbs with up:** pick one of the four ideas up adds, completion, increase, appearing or approaching, and watch a bar fill, columns grow, a circle appear or a ball approach.
- **Ship or sheep:** press play, the browser says one word of a pair, and you pick which you heard, with a running score.
- **A work email:** five lines in the wrong order; tap to move them until the email has its shape, greeting, context, request, details, next step.
The phrasal verbs experiment: each of the four ideas up adds, drawn as a movement.

## Practice that is saved

Under each experiment are the exercises, marked as you answer, and the score goes into the student's path. Then the cards: each comes back after one, three, seven and then fourteen days if you knew it, and the next day if you did not. That is retrieval practice, spaced out, which is what the research supports, rather than a "learning style".

The progress is kept in the browser, through the vault host's own storage for the app, or local storage when the file is opened on its own. Switch between Rui, Sofia and Tomás and each has their own. Nothing is written into the vault, so nothing about a student leaves their device; a real deployment would keep progress in the student's own vault, which is the next step.

## A tutor that knows its place

At the foot of every lesson there is a tutor. Inside a vault with an AI key, it answers through the vault host, which holds the key, caps the spend and asks before the first call; the page never sees the key. The tutor is sent only the current lesson's text and the student's level, and told to answer in at most eighty words, with one example, and not to give the exercise answers before the student has tried.

That last instruction is an Expectation, and the agents page says so: a model can drift. What is a Boundary is what it is sent: one lesson, nothing else, and no tool at all. Without an AI key, the tutor says it is in simulation and answers by quoting the lesson's own words.

## The concept map and the path

The concept map for Rui: thirteen ideas, what each needs first, his mastery in colour, and what is next ringed.

The thirteen concepts the lessons teach are a small knowledge graph: each with its level and what it needs first. The student's mastery colours it, and the plan rings what is next: concepts whose foundations are in place and which are not yet mastered. My path shows the same thing as a list, with the lesson for each, the student's goal, level, package and next lesson. Click a concept and its lesson opens. Inês sees the same list before each lesson, and decides.

## The teacher's side

The back office: the pipeline from enquiry to renewal, and the students.

- **The pipeline:** enquiry, trial booked, trial done, package bought, active, renewal due, paused, with who is where and why.
- **The students:** level, goal, package, next lesson.
- **This week's brief:** three things that need her, each with a recommendation: a renewal to send, a follow-up to finish, a five-minute start for Sofia's next lesson.
- **Paid for:** the lesson packages by link, the price class of each lesson page on the reading meter, and what else she could sell.
- **The agents:** seven, each with its mandate, its grant, its delta and its barriers, marked Boundary, Setting or Expectation.
- **Setup:** the nine steps behind the scenes, and who does each.

In the example these are on one site so you can see them together. In a real deployment the back office lives in a private, encrypted vault, and the public site never holds a student's name.

## Make it yours

Everything the app shows is in `content.json`: the teacher, the lessons and their experiments, the concepts, the students, the pipeline, the agents and the setup. Clone it with `sgit clone sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc:3d0fw3dl english-with-ines`, change the JSON, and it is another teacher's site. The experiments are small functions in the HTML; a new one is a new function and a name in the lesson.

## What this does not claim

- **Inês, her students and the pipeline are fictional.**
- **Progress is per browser,** not synced between devices or shared with the teacher.
- **The tutor needs an AI key in the vault;** without one it runs as a simulation, and it says so.
- **The listening game uses the browser's own voice,** which varies by device and may be unavailable.
- **It was tested in Chromium,** at desktop and phone widths, outside the vault host; the live tutor was not tested here.

## Where this comes from

[The vault](https://dev.vault.sgraph.ai/#sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc%3A3d0fw3dl) (`sgit clone sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc:3d0fw3dl english-with-ines`), built in this session on 3 November 2026. The brief: [a teacher and agents she can trust](a-teacher-and-agents-she-can-trust.md).

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#inside-english-with-ines)

### Builds on

- [A teacher and agents she can trust: a brief for an independent online English teacher's site, the workflows around every lesson, an Agent Behaviour Policy for every agent, the plumbing behind it, and content made for each student](a-teacher-and-agents-she-can-trust.md) A brief for an independent online English teacher: a loop around every lesson where agents draft and she decides, and a behaviour policy for every agent.

### Continued by

- [A teacher and agents she can trust: a brief for an independent online English teacher's site, the workflows around every lesson, an Agent Behaviour Policy for every agent, the plumbing behind it, and content made for each student](a-teacher-and-agents-she-can-trust.md) A brief for an independent online English teacher: a loop around every lesson where agents draft and she decides, and a behaviour policy for every agent.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 372 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=372)

**Posting this article on LinkedIn?** The cover is [inside-english-with-ines.jpg](banners/inside-english-with-ines.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/inside-english-with-ines.html)*
