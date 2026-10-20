/* newsroom.sgit.ai: a pause button for animated figures (v0.12.151). Loaded by the nav on every page
 * (admin/build/chrome.py).
 *
 * A figure is animated when its image is named <name>-anim.webp, whether assets/shots.js fills the figure at run
 * time or the page writes the <img> itself.
 *
 * Pause draws the frame showing at that moment onto a canvas over the image, which works on the web and inside a
 * vault alike, where the image is a blob: URL. Play takes the canvas away and starts the animation again.
 *
 * The choice is kept in this browser (sgit.anim.paused), so a reader who paused one animation finds the next one
 * paused too. With no choice yet, prefers-reduced-motion decides. A figure that starts paused shows the still
 * beside it, <name>-anim-still.webp, on the web; inside a vault it shows its first frame. */
(function () {
  'use strict';
  if (window.__sgitAnimStarted) return;
  window.__sgitAnimStarted = true;

  var KEY = 'sgit.anim.paused', ANIM = /-anim\.webp$/;

  function wantsPaused() {
    try { var v = localStorage.getItem(KEY); if (v === '1' || v === '0') return v === '1'; } catch (e) { /* storage blocked */ }
    return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  }
  function remember(paused) { try { localStorage.setItem(KEY, paused ? '1' : '0'); } catch (e) { /* storage blocked */ } }

  function setup(img) {
    var fig = img.closest && img.closest('figure');
    if (!fig || fig.dataset.anim || !ANIM.test(fig.getAttribute('data-shot') || (img.getAttribute('src') || '').split('?')[0])) return;
    fig.dataset.anim = '1';
    var top = img.parentNode && img.parentNode.classList && img.parentNode.classList.contains('shot-link') ? img.parentNode : img;
    var wrap = document.createElement('div');
    wrap.className = 'anim-wrap';
    top.parentNode.insertBefore(wrap, top);
    wrap.appendChild(top);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'anim-btn';
    wrap.appendChild(btn);

    var animSrc = img.src, canvas = null, paused = false;
    var stillSrc = /^blob:/.test(animSrc) ? null : animSrc.replace(/-anim\.webp(\?.*)?$/, '-anim-still.webp');

    function label() {
      btn.textContent = paused ? '▶ Play' : '❚❚ Pause';
      btn.setAttribute('aria-pressed', paused ? 'true' : 'false');
      btn.title = paused ? 'Play the animation' : 'Pause the animation';
      fig.classList.toggle('anim--paused', paused);
    }
    function freeze() {
      if (!img.naturalWidth) return;
      canvas = document.createElement('canvas');
      canvas.className = 'anim-frame';
      canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
      try { canvas.getContext('2d').drawImage(img, 0, 0); } catch (e) { canvas = null; return; }
      canvas.setAttribute('role', 'img');
      canvas.setAttribute('aria-label', img.alt || 'Paused animation');
      wrap.insertBefore(canvas, btn);
    }
    function pause(viaStill) {
      paused = true; label();
      if (viaStill && stillSrc) {
        img.addEventListener('error', function back() { img.removeEventListener('error', back); img.src = animSrc; img.addEventListener('load', freeze, { once: true }); });
        img.src = stillSrc;
      } else freeze();
    }
    function play() {
      paused = false; label();
      if (canvas) { canvas.remove(); canvas = null; }
      img.src = animSrc;
    }
    btn.addEventListener('click', function () {
      if (paused) play(); else pause(false);
      remember(paused);
    });
    if (wantsPaused()) pause(true); else label();
  }

  // shots.js adds the images lazily; a load event does not bubble, so listen in the capture phase.
  document.addEventListener('load', function (e) { if (e.target && e.target.tagName === 'IMG') setup(e.target); }, true);
  [].forEach.call(document.querySelectorAll('figure img'), function (img) { if (img.complete && img.naturalWidth) setup(img); });
})();
