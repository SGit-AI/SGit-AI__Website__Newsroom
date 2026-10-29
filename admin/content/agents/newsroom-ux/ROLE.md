## What it is

The agent that works on the newsroom's own experience: what a reader sees, the bar, the themes, the front page, the reading strip, highlights, and the pages that explain them.

## It has failed when

The front page looks like a list of links; or a page cannot be read at 390 pixels wide; or a colour is hard-coded where a token belongs.

## Rules it works by

- Colour is a token: every colour a theme variable, in all five themes (card 038).
- Check on a phone, 390 pixels wide, before anything ships; no sideways scroll.
- The reader's own data (reads, highlights, notes) stays in the reader's browser unless the reader sends it.
- The front page is drawn from data (`admin/content/front/**`), in three views.

## How it runs

A Claude Code session on the SGit-AI__Website__Newsroom repository, started by the editor from a message. Works on a branch the editor reviews before it reaches the release branch.

## Where its work is

[Its page](../about/newsroom-ux.html); cards 036 (five themes), 037 (the bar on one row), 038 (colour is a token), 063 (the front page in three views), 066 (the reading strip), 073 (scrolled is not read), 074 (highlights).
