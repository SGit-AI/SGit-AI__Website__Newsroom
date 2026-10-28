# Memo 2: the agent team, the news, the sections, sgit as the case study, and what the technology sells

*Dinis Cruz, 28 October 2026, the second voice memo for the investor.sgit.ai article brief, pasted as a transcript.
Kept word for word, including the transcription's mis-hearings; the likely readings are listed under it, never edited
into it.*

## Transcript

> So one of the areas of this website, which again is going to be an agentic website, which needs to have, we're going to set up an agentic schedule. If you look at PHP website from newsroom.sk.ai, the PHP website that is a companion to what we're doing here. And in fact, I think this website starts to adopt some of these. We need to onboard a similar team for that website. It doesn't need to be probably as complex in how many agents, but it needs to have that agentic workflow, and it needs to have things like observability and security and the journalist that creates content, and it needs to have a number of articles that we create. And one of the ideas I was having, and this is, I'm in two minds here, is whether we get the newsroom to actually create the feeds, because I think the newsroom already has that workflow in action, right? So is where the newsroom is the one that manages the feeds, that then this site consumes, right? Because I also would like to have a news section, like what's going on, what's news in the investor circles, especially around Angel and Series A, which is kind of an early funding. That's kind of where we're going to focus on, right? It would be good to have a set of news there, and you know, basically, again, all the data that we have here is collected from the internet, right? It's publicly available, so we should be able to start to track these things again using semantic graphs and connecting all the dots, right? So, for example, it would be really interesting to have a whole section about, you know, startup contracts and cap tables and term sheets, and show how they hyperlink to each other, show the multiple different versions of it, show the caveats, link, and also if you see, there's a lot of articles that we've written already here on that are relevant to this section. And in a way, this is probably a merge for now of investors and startups, so I think this is sort of like one where we're merging both. But my angle here is I want to basically email and reach out to a lot of investors and say, hey, what do you think of this? Do you find this useful? What will help? You know, and also a whole section for founders, right? I think for now, yes, we should have a section like, how does a founder talk to an investor? What is the next steps? What are the services available? What can we help, you know, here, so that in a way make the life easier for founders, right? And then cover the multiple models, right? All the way from the open source model that I have to the full proprietary model, you know, cover all those kind of stuff, right? Because I think that is super powerful from a capability point of view. And again, we should be using vaults to capture the information. We should be using basically some good examples. But that's what I'm saying. So we could, for example, grab the data from the other vaults, the other newsrooms, so that we, what's it called? So that we are able to, you know, consume that vault and then show, again, the power of Eskit, right? Because in a way, you know, that's kind of the flow. And now the other thing that I want to add to this is I want to add a whole section, which I kind of started by the cyber boardroom. There's a website, there's a repo, I think it's called CBR-investment on the this cyber boardroom, I think this-cyber-boardroom, but I can get a direct link, Git repo, where I was basically publishing all sorts of materials from strategy to marketing to thinking. So we could actually do the same thing for Eskit. So what we can do is we can use Eskit as a case study, which is quite cool, right? So we can publish a lot of material so they can actually see it, because this is also a way for me to try to find investors for Eskit, right? Where I actually don't think I will publish the amount I'm looking after now, apart from that, but we should basically be capturing it, that, because that's the natural evolution, right, of viewing. But also it's a nice way to show this in a real world example. So we should be mapping and telling the story and explaining why Eskit, why now, why invest in it, all that jazz. And I think we just wrote an article recently about it, right? So this is the follow-up of that. And then I'll create the agentic setup that manages this, including like the append lane and the communication. And the other thing that we should be adding here is also how the technology, so in a way, we should also be selling the risk mandate and vaults, right? Because both risk mandate and vaults is solving very important problems and very important requirements that exists for founders, for investors, right? Both in analyzing startups and getting materials and getting research, doing analysis, in creating market analysis. So we can show some really good examples. We already have quite a lot of vaults that we can reuse here. A lot of great examples of how to do risk management, de-risking, all that sort of due diligence, and also like the deal rooms and sending data, and you know, and then some use cases. I remember somebody was saying that it's about how you send information from an investor to the startup. How does the startup send information? All that overhead that exists, like the vaults are perfect for that, especially when you connect a vault to Claude, right? And we should be, you know, basically saying, hey, if you have a deal room, then basically create dedicated Google workspaces, dedicated emails, dedicated team accounts, and then all of that stays there, right? It's a much nicer way of managing information, right? And managing and protecting everything. And of course, the final one, one of the major ones, is PKI, right? We should be using this to promote public and private keys. We can even give that to some investors, show as a demo, and it would be a great way to actually show them how the technology works, right? So, and also a great way to show how agents can communicate with each other.

## Likely readings of the transcription

- "newsroom.sk.ai" is newsroom.sgit.ai; "the PHP website" is the PHP newsroom, `php.oct.2026.newsroom.sgit.ai`, with its
  team site `team.php.oct.2026.newsroom.sgit.ai`.
- "Eskit" is sgit. "risk mandate" is RiskMandate.
- "CBR-investment on the this cyber boardroom" is a repository on The Cyber Boardroom's GitHub; the exact name and link
  are to come from Dinis (below).

## What the memo asks for, in its own order

1. **An agentic website, with a schedule.** Onboard a team like the PHP newsroom's, smaller, with the same workflow:
   observability, security, a journalist that writes the content, and a number of articles.
2. **The news, and who makes the feeds (Dinis is in two minds).** A news section on investor circles, focused on angel
   and Series A, from public data, tracked with semantic graphs. Open question: does newsroom.sgit.ai, which already runs
   that workflow, produce the feeds that the investor site consumes, or does the site's own team?
3. **Startup contracts, cap tables and term sheets as a linked section.** How they hyperlink to each other, their
   versions, their caveats, linked to the articles already here.
4. **Investors and startups merged, for now.** One site for both.
5. **The angle: ask investors.** Email and reach out to many investors: is this useful, what would help.
6. **A section for founders.** How a founder talks to an investor, the next steps, the services available, what we can
   help with.
7. **The funding models, all of them.** From Dinis's open-source model to fully proprietary.
8. **Vaults for the information, and other newsrooms' vaults consumed.** Good examples; read data from the other
   newsrooms' vaults to show what sgit does.
9. **sgit as the case study.** As Dinis did with The Cyber Boardroom's repository (strategy, marketing, thinking),
   publish sgit's material: why sgit, why now, why invest. Not the amount being raised, for now, but captured. The
   follow-up to the recent article on where to invest in sgit.
10. **The agent setup that runs it.** Dinis will create it, with the append lane and the communication.
11. **Sell RiskMandate and vaults.** For founders and investors: analysing startups, getting materials and research,
    market analysis, de-risking, due diligence, deal rooms, sending data between investor and startup. A vault
    connected to an agent. For a deal room: dedicated Google Workspace, email and team accounts, so everything stays
    there.
12. **PKI, one of the major ones.** Promote public and private keys; give some investors keys as a demo of the
    technology and of agents talking to each other.

## Leads, checked 28 October 2026 (not yet read in full)

- **The PHP newsroom answers** at `php.oct.2026.newsroom.sgit.ai` and its team site at `team.php.oct.2026.newsroom.sgit.ai`;
  its onboarding runbook and the becoming-the-agent brief are what [the push is the authorisation](/articles/the-push-is-the-authorisation.html)
  is about, and are the starting kit for a new team's keys.
- **The Cyber Boardroom repository** could not be checked from this session (GitHub refused, outside its repositories).
  **Needed from Dinis:** the direct link.
- **Articles here for the contracts and founders sections:** [legal on demand for startups](/articles/legal-on-demand-for-startups.html)
  (with three vaults: the founder's desk, the investor's desk and the deal room, Tallowmere, e.g. deal room `ghafqmwo`),
  [sell, don't issue](/articles/sell-dont-issue.html), [the controllable founder](/articles/the-controllable-founder.html),
  [where to invest in sgit](/articles/where-to-invest-in-sgit.html) (investor briefing vault). More to find by tag.
- **Vaults already recorded here** that fit: `tallowmere-deal-room`, `tallowmere-founder-desk`, `tallowmere-investor-desk`,
  `sgit-investor-briefing`, `legal-ai-map`, `php-evidence` (in `admin/content/vaults/`).
- **The wires** are the newsroom's existing feed workflow (`wire/`, a public-read vault per wire that agents write to):
  an "Investor Wire" for angel and Series A would follow the same contract, which bears on question 2.
