# Know the Reach (RiskMandate song and music video, part one)

Requested by Dinis, 14 November 2026: an article about the first part of the music video for RiskMandate's song on Spotify, with the production audit he pasted.

- Sources: "RiskMandate production audit, 14 November 2026" (pasted in chat); Spotify oEmbed and page for track 1J6zgXwUBtbuUkqUMi6wI6 (title Know the Reach, "RiskMandate · Know the Reach · Song · 2026"), read 15 Nov.
- Used the audit's safe public wording: 43 images, 16 clips, 21 exports, almost 25 minutes of versioned material and not unique footage, about 2,300 words of direction. The 464 gallery entries are not described as new images.
- The audit's "Silviu" is taken as Silvio Switha (the team's video lead; Drive videos are "By Silvio Switha"); "Dennis" in it is Dinis.
- The video is on YouTube (https://youtu.be/BjN-K-C2fsw, sent by Dinis 15 Nov); linked, not copied: downloading it was not allowed from this session. Moving it into the media vault later needs the MP4 itself (video-cut.sh, videos/know-the-reach-part1/web, then a !video line).
- Figures: ktr-funnel, ktr-decisions.

## Second article and the YouTube player (15 Nov)

- Dinis asked (15 Nov, after the first article) for a second article on the human and artistic side, and for the video to play from YouTube on a click: no download, nothing loaded from Google until the reader presses play, a YouTube label on it.
- admin/build/youtube_embed.py (sync_newsroom item 15), assets/youtube/youtube.{js,css}: `!youtube <id> <poster> | caption`. Poster is our own image (ktr-poster.webp, drawn here, to be replaced by the song's artwork). On click, a youtube-nocookie.com iframe with referrerpolicy strict-origin (origin only; YouTube's embeds refuse to play with no referrer).
- Article: every-hour-is-twenty-years, from Dinis's account; figures eht-producer, eht-loop. Claims marked as his view: Silvio's band, "perhaps a fifth", the band recording as a challenge. The second Spotify song is not yet named.
