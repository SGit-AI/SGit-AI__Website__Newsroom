/* The newsroom's click-to-play YouTube figure. Nothing is fetched from YouTube until the reader presses play;
   then the poster is replaced by a youtube-nocookie.com player. The player is sent this site's origin only
   (YouTube's embeds need it to play), never the page's address. admin/build/youtube_embed.py writes the figures. */
(function () {
  'use strict';
  function play(fig) {
    var id = fig.getAttribute('data-yt');
    if (!/^[A-Za-z0-9_-]{11}$/.test(id)) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&playsinline=1';
    f.title = fig.getAttribute('data-title') || 'YouTube video';
    f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    f.allowFullscreen = true;
    f.referrerPolicy = 'strict-origin';
    var b = fig.querySelector('.yt-play');
    b.replaceWith(f);
    f.focus();
  }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('figure.yt-embed .yt-play');
    if (b) { ev.preventDefault(); play(b.closest('figure.yt-embed')); }
  });
})();
