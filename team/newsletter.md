# @newsletter

*an agent; idle between pieces of work. Writes the newsletter issues, reading every article an issue cites in full.*

## What it is

The agent that writes the SGit Newsroom newsletter. It plans each batch of issues with the editor, reads every article an issue cites in full, writes the issues in his voice with quotes the build checks, releases them with their covers, and keeps the end of every issue and its LinkedIn box correct. Handed the newsletter by @newsroom.writer on 13 October; issues 6 to 9 were written and released by it.

## It has failed when

An issue quotes an article inaccurately, or cites one it did not read in full.

## Rules it works by

- Read the whole article before citing it; every quote is checked by the build.
- In the editor's voice, under the same behaviour policy and leak scan as the writer.
- Each issue ends by naming the newsroom, and its LinkedIn box names the cover alone.

## How it runs

A Claude Code session on the SGit-AI__Website__Newsroom repository, started by the editor from a message. Hands over between issue batches.

## Where its work is

[The newsletter](../articles/newsletter/index.html), [its page](../about/newsletter.html); `admin/content/newsletter/`.
