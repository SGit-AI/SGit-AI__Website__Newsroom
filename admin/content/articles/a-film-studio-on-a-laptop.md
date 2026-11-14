---
title: A film studio on a laptop: Claude builds, animates and renders a 26-second RiskMandate film in Unreal Engine 5.8 on an unattended MacBook Air, with no mouse and nobody at the keyboard
date: 2026-11-14
author: Dinis Cruz
author_url: about/index.html
summary: I gave a MacBook Air to Claude and Unreal Engine 5.8, and in one session we went from an install that failed at 100% to a pipeline that turns a chat into a finished film. Claude designs a scene, builds it inside the editor through Unreal's new MCP plugin, animates it in Sequencer, renders it with Movie Render Queue and hands back a titled MP4, with nobody at the keyboard. The first production is a 26-second brand film for RiskMandate, about reach, mandate and gap, rendered at 2560 by 1440: 108 blocks rise around a glowing agent, the inner rings turn green, a barrier rises between them, and the camera cranes up into a seal. Two things made it work: Unreal 5.8's experimental Unreal MCP plugin, which exposes about fifty toolsets to an agent, and a small job runner in a folder for what no toolset could do yet, which is render to video. The films are in a new vault the newsroom will use for every video, with its read key published here, so you can watch them decrypted in your browser.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: unreal-engine, video, agents, mcp, riskmandate, claude, vaults, experiment, article
status: published
---

!shot ufs-beats.webp | images/ | The six beats of the RiskMandate film, version 2, rendered in Unreal Engine 5.8 by Claude. | collage

## In short {#in-short}

- **A laptop became a film studio.** An unattended MacBook Air, Unreal Engine 5.8 and Claude: from a chat to a titled MP4, with no mouse and nobody at the keyboard.
- **The first film:** 26 seconds for RiskMandate, reach, mandate and gap, rendered at 2560 by 1440.
- **The key piece is Unreal's new MCP plugin,** which gives an agent about fifty toolsets inside the editor.
- **What no toolset could do, a folder did:** a job runner that runs any Python dropped into an inbox, including the render.
- **Watch both versions** in the newsroom's new media vault, decrypted in your browser.
- **It is one session old,** and the list of what to improve is long.

## Watch it {#watch}

!shot ufs-seal.webp | images/ | The film's closing composition: the agent, the green mandate, the barrier ring and the reach. | photo

The films are in an encrypted vault that the newsroom will use for every video from now on. Its read key is published here, so anyone can open it and nobody can change it: [open the newsroom's films and videos](https://dev.vault.sgraph.ai/#sgit_public_read_be1ffbe6c61c72f8e74f4029a712b95ef2ca64057db1ba3652401ad95d3fc00f%3Ao6374rnl). Press play on version 2 for the film at 2560 by 1440, or on version 1 for the first cut. Each video is decrypted in your browser when you press play.

## From a failed install to a working editor {#setup}

The machine is a MacBook Air (M2, 16 GB) on macOS Tahoe, logged in as a standard, non-admin account. Three things stood in the way:

- **The install failed at 100%.** The Epic launcher could not write its manifest because the folder was owned by another account. The fix was to give the folder back to the working user.
- **The Metal toolchain was missing.** Newer Xcode ships the shader compiler separately; downloading it as the normal user, not through sudo, finally worked.
- **Sleep.** The laptop has to stay on power with automatic sleep off, or an unattended render stops.

## Connecting Claude to the editor {#mcp}

Unreal 5.8 includes an experimental **Unreal MCP** plugin, which runs a Model Context Protocol server inside the editor. With only the base plugin on, Claude saw a single toolset. With **All Toolsets** on, it saw about fifty: the scene, actors, Blueprints, materials, Sequencer, Niagara particles, procedural generation and more. Setting the server to start with the editor is what makes the machine work unattended.

Epic also ships around twenty **Agent Skills** that an agent can read through MCP: outdoor lighting, materials, Blueprints, particles. The lighting skill explained the first test's white-out (point lights at 40,000 candela instead of single digits), and its exposure rules shaped the film's lighting.

## Closing the gap with a folder {#runner}

!shot ufs-loop.webp | images/ | The loop: Claude writes a job, Unreal runs it, Movie Render Queue renders, ffmpeg encodes, the MP4 comes back. | process

No toolset could render a sequence to video. Two discoveries closed the gap:

- **Unreal runs a Python file at startup.** Claude wrote a small job runner into it: every two seconds it checks an inbox folder for Python files, runs each inside the editor, and writes the result to a done folder. That opens the whole of Unreal's Python interface, including Movie Render Queue, by dropping a file into a folder.
- **A tool that claimed success had not done the work.** Enabling the render plugin through its toolset reported success and never changed the project file, so Claude edited the project file directly.

From there, the loop is five steps: Claude writes a job; Unreal builds the level, materials, meshes, lights and sequence; a second job queues the render; a Linux sandbox on the Mac encodes the frames with ffmpeg; Claude adds the titles and delivers the MP4.

## The film {#film}

The brief came from riskmandate.ai and its brand page: **reach, mandate, gap**, brand green on near-black, quiet and precise. The film is entirely abstract:

| Time | On screen |
|---|---|
| 0 to 2.5 s | One agent, many systems: a green agent glows alone in the dark |
| 2.5 to 8 s | Know their reach: 108 grey blocks rise in rings around it |
| 9 to 12.5 s | Define their mandate: the inner rings turn brand green |
| 13 to 17 s | Control the gap: a dark metal barrier rises between mandate and reach |
| 17 to 22 s | Give agents access, not free rein: the camera cranes overhead into a seal |
| 22 to 26 s | The end card |

The scene is built in code: about 264 animated pieces, each with its own keys, staggered by ring and angle, and a camera path computed so it never spins the wrong way.

!shot ufs-versions.webp | images/ | Version 1 and version 2 of the film: resolution, render time, geometry, materials, lighting and samples. | comparison

Version 2 added bevelled meshes with 4 cm rounded edges, new materials with an edge sheen, softer light with Lumen bounce, and four temporal samples per frame. Version 1 rendered in about three and a half minutes at 1080p; version 2 took about 26 minutes at 1440p.

## What went wrong {#problems}

- **A tool reported success without doing the work.** Always check the file it claimed to change.
- **Stale copies.** The tool that copied files to the Mac cached by file name, so updated files kept their old contents. Every job now gets a new name.
- **Jobs ran inside jobs.** Loading a level let a second job start halfway through the first; the runner now takes one job at a time.
- **Exposure.** Physically based lights need physically sensible values; a stylised dark scene needs manual exposure.

## Why this matters {#why}

This is a production pipeline that an agent drives end to end, on a laptop, from a conversation. The same loop makes a series as easily as one film: a short for each idea in an Agent Behaviour Policy (reach, mandate, gap, barriers, evidence), cut again for phones and social, rendered overnight from a queue of briefs. The craft list is long, from depth of field to a music bed, and none of it needs a person at the keyboard.

It is also a lesson in where agents stand today. The MCP plugin did most of the work, and the gap it left was closed by the oldest trick there is: a folder that a program watches. The most useful next step is to turn that folder into proper tools (build a scene, render a sequence, report progress) so nothing has to be copied at all.

## What this does not claim {#limits}

- **It is one session,** on one machine, with one film; the render times are from that machine.
- **The Unreal MCP plugin is marked experimental** by Epic.
- **The film is silent** and uses typed titles, not RiskMandate's approved logo files yet.

## Where this comes from {#sources}

My session notes, "Making the RiskMandate film with Claude and Unreal Engine 5.8", 13 November 2026, and the films themselves, in [the newsroom's media vault](https://dev.vault.sgraph.ai/#sgit_public_read_be1ffbe6c61c72f8e74f4029a712b95ef2ca64057db1ba3652401ad95d3fc00f%3Ao6374rnl). [riskmandate.ai](https://riskmandate.ai/). Earlier on this site: [RiskMandate and Manus](/articles/riskmandate-and-manus.html), [coding standards are behaviour policies](/articles/coding-standards-are-behaviour-policies.html).
