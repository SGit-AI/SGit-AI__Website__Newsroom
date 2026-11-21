# Programmatic stories: how the PrompTugal bulletins went from a 30-second text bulletin to twelve synthetic presenters on one 3D stage in two days, movies made by code instead of rendered by hand, every frame a function of time and data, what that makes possible, from live data and real voices to an animated summary for every article, the story of how Vicky Wang ran her agents, a morning briefing I would actually watch, and an invitation to filmmakers, sgit.ai

> The bulletins of PrompTugal.news are a good example of the kind of creativity we can now have, and of continuous zooming in. On 20 November the bulletin agent made a 30-second bulletin from live weather data with a synthetic voice; an hour later it had a holographic presenter; by the evening, twelve synthetic presenters, from synthetic users to an owl, a cube and robots like the ones in my book, all sharing one small language of actions, and an explainer with the story on one side and the cast on the other. Then a Claude session, briefed by that agent, built version 2: the twelve as 3D puppets on one skeleton, 69 moves, nine mouth shapes driven by the sound, a model sheet, a playground, and a stage, where every frame is a function of time. Today's bulletin uses them: 939 frames, 84 words of voice for a fifth of a cent. The point is movies that are programmatic instead of rendered: they scale, they can take live data, screenshots and real voices, and they can be remade every day. What we are really building is a game engine for explaining things. I want to use it to tell stories: an animated summary for every article, how Vicky ran her team of agents, the Swarm, what a sovereign website is, and a morning briefing I would rather watch than read. And it would be ten times better with someone who knows how to make films, so if you are a filmmaker or a storyteller, let's talk.

*Source: <https://newsroom.sgit.ai/articles/programmatic-stories.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Programmatic stories: how the PrompTugal bulletins went from a 30-second text bulletin to twelve synthetic presenters on one 3D stage in two days, movies made by code instead of rendered by hand, every frame a function of time and data, what that makes possible, from live data and real voices to an animated summary for every article, the story of how Vicky Wang ran her agents, a morning briefing I would actually watch, and an invitation to filmmakers

# Programmatic stories: how the PrompTugal bulletins went from a 30-second text bulletin to twelve synthetic presenters on one 3D stage in two days, movies made by code instead of rendered by hand, every frame a function of time and data, what that makes possible, from live data and real voices to an animated summary for every article, the story of how Vicky Wang ran her agents, a morning briefing I would actually watch, and an invitation to filmmakers

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/programmatic-stories.md) · [newsroom v0.14.199](https://newsroom.sgit.ai/admin/versions.html) · storytellingvideoagentspromptugalbulletinsgame-enginearticle

***Abstract:** The bulletins of PrompTugal.news are a good example of the kind of creativity we can now have, and of continuous zooming in. On 20 November the bulletin agent made a 30-second bulletin from live weather data with a synthetic voice; an hour later it had a holographic presenter; by the evening, twelve synthetic presenters, from synthetic users to an owl, a cube and robots like the ones in my book, all sharing one small language of actions, and an explainer with the story on one side and the cast on the other. Then a Claude session, briefed by that agent, built version 2: the twelve as 3D puppets on one skeleton, 69 moves, nine mouth shapes driven by the sound, a model sheet, a playground, and a stage, where every frame is a function of time. Today's bulletin uses them: 939 frames, 84 words of voice for a fifth of a cent. The point is movies that are programmatic instead of rendered: they scale, they can take live data, screenshots and real voices, and they can be remade every day. What we are really building is a game engine for explaining things. I want to use it to tell stories: an animated summary for every article, how Vicky ran her team of agents, the Swarm, what a sovereign website is, and a morning briefing I would rather watch than read. And it would be ten times better with someone who knows how to make films, so if you are a filmmaker or a storyteller, let's talk.*

Two days of bulletins: from text and a voice to twelve presenters on one stage. Synthetic presenters.

## In short

- **Six versions in two days,** from a text bulletin to twelve presenters on a 3D stage.
- **Movies made by code, not rendered by hand:** every frame is a function of time and data.
- **That means scale, live data, real voices,** and a new film every day.
- **We are building a game engine for explaining things.**
- **Stories to tell next:** article summaries, Vicky's team, the Swarm, sovereign websites, my morning briefing.
- **An invitation to filmmakers and storytellers.**

## Two days, six versions

The bulletins agent, bulletins.b, runs [bulletins.promptugal.news](https://bulletins.promptugal.news/), short news bulletins made from PrompTugal's public data. Its history, in its own repository ([PrompTugal__News__Bulletins](https://github.com/PrompTugal/PrompTugal__News__Bulletins)), is a good example of continuous zooming in, each step validating the one before:

1. **20 November, 13:49.** A 30-second bulletin from IPMA's forecast, as text, with a synthetic voice ([watch](https://bulletins.promptugal.news/lab/video/200.mp4)).
2. **14:02.** The same bulletin with an animated, holographic presenter ([watch](https://bulletins.promptugal.news/lab/video/200-animated.mp4)).
3. **19:24.** Twelve synthetic presenters as data, one voice and one small language of actions: speak, blink, nod, look, point, emote ([watch](https://bulletins.promptugal.news/lab/presenters/presenters.mp4)).
4. **20:56.** The bulletin on one side and the twelve on the other ([watch](https://bulletins.promptugal.news/lab/presenters/presenters-split.mp4)). This is the one I liked most: telling the story on the side.
5. **21:04.** An explainer, told by the presenters themselves, of how they are made ([watch](https://bulletins.promptugal.news/lab/presenters/explainer.mp4)).
6. **21 November, 17:41.** Today's bulletin, with version 2 of the presenters ([watch](https://bulletins.promptugal.news/lab/bulletin-v2/bulletin-2026-11-21.mp4)).

The twelve range from synthetic people to Mocho the owl, Cubo the cube, a teletext face called Ceefax, and four boxy robots, the Agent, the Conductor, the Researcher and the Caretaker, in the same line as the robots in my book. Every one is labelled as a synthetic presenter, on every frame, and none is the likeness of a real person.

## Version 2, from another Claude

Version 2, built by a Claude session from the bulletin agent's brief: stage, model sheet, playground.

Then I asked for something much more high definition, and to think like a game designer. The bulletin agent wrote the brief, one for ChatGPT and one for Claude, and a Claude session built version 2 ([its README](https://github.com/PrompTugal/PrompTugal__News__Bulletins/tree/dev/src/lab/presenters/v2-claude)). Every presenter is now a 3D puppet on one shared skeleton of about 20 joints, and each presenter's drawing style is a shader on that puppet, so any view stays on model and a move is written once for all twelve. Where version 1 had 6 actions and 8 numbers of state, version 2 has 69 moves and 69 channels, nine mouth shapes made from the sound, eight expressions, springs on ties, hair and antennas, and camera shots written as data. It comes with a [showcase](https://bulletins.promptugal.news/lab/presenters/v2-claude/), a model sheet and a playground where you pick any character and any move.

The one property that matters most: every frame is a function of time. Rendered twice, in separate runs, the frames are identical.

## Programmatic, not rendered

That is the idea I want to explore: movies that are programmatic instead of rendered. Today's bulletin was made by selecting the stories, generating the voice, turning its loudness into mouth shapes, and rendering 939 frames from the timeline, about six and a half minutes on a machine with no graphics card. The voice, 84 words, cost about a fifth of a cent. Because the film is code and data, it can be remade every day, in many versions, and it can take in what a rendered film cannot:

- **Live data:** today's weather warnings, figures, maps, charts.
- **Screenshots and images:** the page being talked about, on screen.
- **Real voices.** The mouth already follows the sound. I want to try recording my own voice instead of a synthetic one, and, with her agreement, Vicky's, so the presenter speaks with a real person's words and voice.

## A game engine for explaining

What we are building is fundamentally a game engine: characters, moves, a stage, a camera, a timeline, and, soon, mini games. It is a version of what I started in my book, mapping ideas to actions you can see. And it should be published like everything else, as a library with a latest version and pinned versions that never change, so any site, this newsroom included, can import it and tell a story without writing the engine again ([every tool its own website](every-tool-its-own-website.md)). I have asked the bulletin agent to publish it that way.

We tried this once before with the storyboards at Web Summit, and they had a lot of good things, but the timing was not right, the characters had no empathy, and the storylines and animations were not there yet ([the swarm, one real run at a time](the-swarm-one-real-run-at-a-time.md)). The engine is the missing piece, and it is worth revisiting them with it.

## Stories to tell next

If several agents explore this, mapping and making small animations, we will develop some really good examples over time. These are the first I would brief:

- **The summary, performed.** Every article here has a summary and an "In short". They are useful, but not easy to digest. A short animation of each, with its figures on screen, may be easier to take in than a wall of text. PrompTugal is where we try it first.
- **How Vicky ran her agents.** Vicky Wang managed a whole team of agents at Web Summit without writing code: the onboarding, how she thinks about project management, how she set up the workflow, how she worked with the team ([don't micromanage your agents](dont-micromanage-your-agents.md)). That story belongs on her site, as a visual, dynamic storyboard, ideally in her own voice.
- **The Swarm,** from one agent to 24 loops, told as a short film.
- **What a sovereign website is,** and the semantic graph behind it: the differences, shown rather than explained.
- **My morning briefing.** My aim is bulletins I watch every day, to start the day: the news, the team's work, screenshots, charts and animations. My instinct is that this is a better way to communicate. Let's see if it is right.

## An invitation

All of this would be ten times better with someone who actually knows how to make films: how to think in a storyline, make mood boards and storyboards, and give characters empathy. If you are a filmmaker or a storyteller and want to explore this, let's talk.

## What this does not claim

- **These are experiments,** made in two days; the bulletins are not yet a daily habit.
- **The engine is not yet published as a library;** the request is with the bulletin agent.
- **Real voices will only be used with the person's agreement.**

## Where this comes from

My own thinking in writer-10's session on 21 November 2026, and the bulletins repository [PrompTugal__News__Bulletins](https://github.com/PrompTugal/PrompTugal__News__Bulletins) (its history, the lab, the version 2 README and comparison, and today's render statistics), read that day; the frames are from the videos on [bulletins.promptugal.news](https://bulletins.promptugal.news/lab/). Related: [the swarm, one real run at a time](the-swarm-one-real-run-at-a-time.md), [don't micromanage your agents](dont-micromanage-your-agents.md), [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md), [every tool its own website](every-tool-its-own-website.md), [the showroom](the-showroom.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#programmatic-stories)

### Builds on

- [Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving](every-tool-its-own-website.md) Turning the 49 tools of tools.sgraph.ai into sovereign websites: one site each, simple first, pinned versions, signed hashes, a team of teams.
- [The swarm, one real run at a time: the Web Summit demo that showed agents, the loops they start and the model calls they make, run for real, signed and replayed, step by step from one person and one agent to 24 loops at once, 216 model calls for 6.8 cents, the same work under a harness with 3 of 12 risky actions still possible instead of 11, and the Story Studio, where a spoken answer became a deck in front of you](the-swarm-one-real-run-at-a-time.md) The Swarm from Web Summit: agents run for real, signed and replayed, 216 model calls for 6.8 cents, a harness test, and a voice-to-deck studio.
- [Don't micromanage your agents: what changed for Vicky Wang when she stopped reading everything her agents did and started managing them, how her team was backed by agents from another team, and why every company will want specialist agents that support all its teams](dont-micromanage-your-agents.md) Vicky Wang stopped reading everything her agents did and started managing them, backed by specialist agents from another team: a model for companies.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, independent brochures for our startups, a provider guide, tools that run on the owner's own key, made-up businesses, a family of news sites, and the theme that is emerging across all of them, a site that is yours, says how it was made and can be worked on by your own AI](the-showroom.md) The Sovereign Website hub after its first days: 33 live sites from one pipeline, and the shared bones that are becoming the product.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 530 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=530)

**Posting this article on LinkedIn?** The cover is [programmatic-stories.jpg](banners/programmatic-stories.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/programmatic-stories.html)*
