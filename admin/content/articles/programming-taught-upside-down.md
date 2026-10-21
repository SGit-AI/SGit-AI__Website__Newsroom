---
title: Programming, taught upside down: what Lockhart said about maths applies to code, the tools that got the loop right, and why explorer coding finally starts at the right end
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: In the book I quote Paul Lockhart's A Mathematician's Lament: if you set out to design a system that destroys a child's curiosity about maths, you could not do better than the one we have. I think we do the same thing with programming. It is usually taught upside down: concepts first, functions and structures that make no sense yet, exercises that build nothing anyone uses. Of course people hate it. What hooks a programmer is something else: the ability to control something, to go from a thought to something that works, in a short loop. I learned that way, on a ZX Spectrum, then an Amiga and an x86, meeting each concept when a problem needed it. The tools that taught people well all had that loop: BASIC at the prompt, Visual Basic, the spreadsheet, Scratch, and the Code Clubs in the UK. And when people were taught programming with nothing useful to build, they went back to Excel, and programmed there. Now explorer coding, by voice, starts at the right end: what you want, and seeing it work. Coding is communication with a computer, and I expect people will end up reading more code, not less, and understanding variables and classes because they already need them.
version: v0.13.19
license: https://creativecommons.org/licenses/by/4.0/
tags: gen-z-book, learning, programming, education, explorer-coding, article
status: published
---

!shot pu-upside.webp | images/ | Programming, taught upside down. Usually: syntax and types, variables and functions, classes and structure, exercises with no purpose, and often nothing useful at the end. How it is learned: something you want to control, make it work and see it work, the concept you need when you need it, and structure because you need it. | concept

## In short {#in-short}

- **We teach maths as if to make people hate it.** Lockhart said so in 2002; I say it in the book.
- **We teach programming the same way.** Concepts first, purpose later, often nothing useful at all.
- **What hooks a programmer is control.** Going from a thought to something that works, in a short loop.
- **The tools that taught well had that loop.** BASIC, Visual Basic, the spreadsheet, Scratch, Code Club.
- **Taught badly, people went back to Excel.** And programmed there anyway.
- **Explorer coding starts at the right end.** What you want, by voice, and seeing it work.
- **Coding is communication.** People will read more code, not less.

## Lockhart, on maths {#lockhart}

One of the books I love is *A Mathematician's Lament*, by Paul Lockhart, an essay from 2002 and a book in 2009. I quote it in the book, in the chapter [Connect the dots backwards](https://gen-z-developers.sgit.ai/v2/book/connect-the-dots-backwards.html). It opens with a musician who "wakes from a terrible nightmare", in which music is taught the way maths is. And it says, of maths: "if I had to design a mechanism for the express purpose of destroying a child's natural curiosity and love of pattern-making, I couldn't possibly do as good a job as is currently being done". For Lockhart, "mathematics is an art", and we teach it as if it were not.

(The memo behind this article gave his name wrongly, as it did once before; it is Paul Lockhart.)

## We do the same with programming {#programming}

I would say we do exactly the same thing with coding. Not every time, but usually, programming is taught upside down. You are introduced to functions, types and structures, capabilities that make no sense yet, before you have anything you want them for. Even at university, when my kids were doing more advanced work and using statistics software like SPSS, they were being introduced to concepts that, from a programming point of view, are important, but were not relevant at that moment. Of course people hate it. It does not make sense, because nothing has made it make sense yet.

If we wanted to create a system to make children, and adults, dislike programming and not understand it, we could hardly come up with a better model than the way we usually teach it. That is Lockhart's point, moved from maths to code.

## What hooks a programmer {#hook}

The thing about programming is the ability to control something: to make something work. The hook you get as a developer is the moment you realise that, and it is very exciting, because you can go from a thought to its execution.

I was lucky. By the time I was taught any of those concepts, I already knew how to program, on a ZX Spectrum, then on an Amiga, then on an x86. So for me the concepts were interesting, and I met each one because I needed it to solve a particular problem. I learned them by doing, which is the best way, with the feedback loop always there: the REPL, read, evaluate, print, loop. Type something, see what it does, change it. That loop is what makes it addictive, in a good way: you are solving puzzles all the time, little problems, and it is very rewarding, especially when you build tools you use yourself.

## The tools that got the loop right {#loop}

!shot pu-loop.webp | images/ | The tools that got the loop right: BASIC on the ZX Spectrum, Visual Basic, the spreadsheet, Scratch, Code Club, and now explorer coding. Each made the distance from an idea to seeing it work very short. | timeline

The places where I have seen programming taught really well all had that short loop:

- **Visual programming for children.** [Scratch](https://scratch.mit.edu/), developed at the MIT Media Lab, is a "block-based visual programming language": you snap blocks together and watch something move. Version 1.0 came out in 2007.
- **Code Club, in the UK.** Volunteer-run, after-school coding clubs, planned from April 2012, which joined the Raspberry Pi Foundation in November 2015. I think they did an amazing job, and that is how it should be.
- **Visual Basic.** Introduced in 1991, and powerful for the same reason. In Wikipedia's words, "Forms are created using drag-and-drop techniques": you drew the interface, wired it up and ran it. One of the most powerful ways to create user interfaces in a visual and interactive way.
- **The spreadsheet.** Change a cell and see the result. It is programming, even if nobody calls it that.

## The irony: back to Excel {#excel}

!shot pu-excel.webp | images/ | The irony: taught programming with nothing useful to build, people go back to the spreadsheet, and program there anyway. Microsoft calls Excel the world's most widely used programming language. | concept

The other problem with teaching programming upside down is that people learn it and then do nothing useful with it, so they do not use it day to day. And guess what? They go back to Excel, where they program anyway. That is the irony. Microsoft's own researchers call Excel "the world's most widely used programming language", and in January 2021, with the LAMBDA function, "Excel has become Turing-complete."

The book makes the same point from the other side, in [Everyone who can brief an agent is a developer](https://gen-z-developers.sgit.ai/v2/book/everyone-is-a-developer.html): the persistence of the spreadsheet is evidence that software failed the people using it, because it is the one tool where they control the shape of the thing. And [the citizen developer](/articles/the-citizen-developer.html) is the spreadsheet grown up. People can program. They program wherever the loop is short and the result is theirs.

## Explorer coding starts at the right end {#explorer}

That is why [explorer coding](/articles/explorer-coding.html), what most people call vibe coding, is so powerful. It starts at the right end: what you want, and seeing it work. People are now coding with their voice, as in [omnichannel programming](/articles/omnichannel-programming.html), and the distance from a thought to a running thing is now very short.

And here is what I find interesting. I know entrepreneurs who have been explorer coding for a while, and I think they are now ready to understand the concepts the classroom tried to teach first. In fact they are already being exposed to them: a variable, a procedure, a method, a class, a structure. They meet them in the code the agent writes, the way I met them on the Spectrum: because a problem needed them.

## Coding is communication {#communication}

!shot pu-communication.webp | images/ | Coding is communication: voice and briefs, visual blocks, code and its primitives, and the machine underneath. The way in changes; the primitives stay. | concept

This is the trick we sometimes miss. Coding is communication: speaking to a computer, through an abstraction layer. Each programming language has its own sweet spot.

So I think it is going to be ironic. People will end up reading a lot more code, not less, and reading more of those primitives, because code is still a very efficient way of communicating what a system does. It may become more visual. But the core primitives will still be there, and more people will understand them, because they arrived at them from something they wanted to do.

## What I hope changes {#hope}

The visual, conversational way in is still crude, but it is getting better, because the connection between what you do and what happens is now much more real. I hope it means a lot more people come into development and discovery, because it is amazing: solving puzzles, little problems, all the time, and building tools you use yourself. That is the experience the classroom so often took away, and the one the book wants every reader to have.

## What this does not claim {#limits}

- **Not every programming course is like this.** Many teachers do it well; the pattern is common, not universal.
- **The experiences are mine.** Mine and my children's, not a study.
- **Explorer coding is not a curriculum.** It is a way in; the concepts still have to be learned.
- **Lockhart wrote about maths.** Applying his argument to programming is mine.

## Where this comes from {#sources}

A voice memo of 21 October 2026, related to the book's chapters [Connect the dots backwards](https://gen-z-developers.sgit.ai/v2/book/connect-the-dots-backwards.html), [Everyone who can brief an agent is a developer](https://gen-z-developers.sgit.ai/v2/book/everyone-is-a-developer.html) and [Explorer coding, not vibe coding, and the handover](https://gen-z-developers.sgit.ai/v2/book/explorer-coding-and-the-handover.html). Paul Lockhart, [A Mathematician's Lament](https://dept.math.lsa.umich.edu/~jchw/LockhartLament.pdf), 2002. Microsoft Research, [LAMBDA: The ultimate Excel worksheet function](https://www.microsoft.com/en-us/research/blog/lambda-the-ultimatae-excel-worksheet-function/), 25 January 2021. Code Club, [joining the Raspberry Pi Foundation](https://codeclub.org/2015/11/03/code-club-and-the-raspberry-pi-foundation-join-forces), 3 November 2015. Wikipedia on [Scratch](https://en.wikipedia.org/wiki/Scratch_(programming_language)) and [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic_(classic)). Related: [explorer coding](/articles/explorer-coding.html), [the citizen developer](/articles/the-citizen-developer.html), [you are a developer](/articles/you-are-a-developer.html), [omnichannel programming](/articles/omnichannel-programming.html), [the jobs that never scaled](/articles/jobs-that-never-scaled.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
