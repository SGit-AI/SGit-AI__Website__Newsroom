# Videos from a vault, inside an article

Dinis, 14 November 2026: "see also the home page of PrompTugal.news, a good example of using a video directly embedded from a vault"; then "comment on that, see if it's better or worse and more performant from a user point of view to split that in 4 megabytes chunks ... make sure the video starts playing as soon as possible"; then "yes, go ahead with the !video embed and the cut script".

## The measurement (14 November 2026, Chromium, cold start)

| Route | First frame, fast link | First frame, 20 Mbit/s |
|---|---|---|
| 2-second fMP4 pieces, Media Source Extensions, PrompTugal's reader | 4.2 to 5.7 s after page load | 4.0 to 4.6 s after page load |
| One 24 MB file through the full vault app (temporary S3 link) | about 3 s after play | about 11.5 s after play, plus about 10 s for the app |
| One 24 MB file through the simple reader | fails: the read API answers 502 for it | |

Why: each vault file is one AES-GCM block, decryptable only once all of it has arrived, so a single file cannot start early even from S3. Pieces can. Of the 4 s, 2.5 to 3 s is the reader walking the vault's tree; a flat index would cut it. A longer-term fix in the vault format: encrypt large files in sealed chunks so a browser can range-read and decrypt as bytes arrive.

On the article page after the change: 1.3 s from click to playing (posters and manifests loaded with the page).

## The pieces

- `admin/writer/tools/video-cut.sh <video> <folder>`: re-encodes (keyframe every 2 s, x264 CRF 20), cuts, writes manifest.json and poster.jpg.
- `admin/build/vault_video.py`: turns `!video <vault card> <folder> | <caption>` into the player in built pages and a link in the markdown twins; first in release.sh's list.
- `assets/vault-video/vault-video.js` and `.css`: the player, adapted from PrompTugal.news (Apache-2.0).
- `assets/vendor/sgit-ai/2026-11-05/vault-embed.js`: sgit.ai's reader, pinned, unmodified.
