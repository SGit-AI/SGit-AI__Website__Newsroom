/* shots.js — fill walkthrough figures with their screenshots at runtime.

   The site's authoring contract forbids declarative <img src> in the page source (a
   page must survive being served from inside a vault, where the host answers reads
   over the bridge rather than serving declarative fetches). So the markup carries
   placeholders:

     <figure class="shot" data-shot="lightbox.webp" data-cap="…"></figure>

   and this fills them in. Two paths, and the difference between them matters more
   than it looks:

     1. INSIDE A VAULT — sg.vfs.read gives us bytes, which become a blob: URL. This
        is unavoidably asynchronous: we have to have the bytes before there is
        anything for an <img> to point at.
     2. THE ORDINARY WEB — we set img.src to the path and stop. No fetch, no blob.
        The browser owns the load, which means it is an ordinary pending document
        resource, which means the PRINT pipeline knows to wait for it. Going through
        fetch() here would be pure loss: same bytes, but invisible to the printer.

   Loading is lazy (IntersectionObserver): a walkthrough page carries most of a
   megabyte of WebP below the fold, and a reader who never scrolls should never pay
   for it. Print is the one exception, and it is handled ON PRINT rather than by
   pre-loading for everybody — see printPrep. */
(function () {
  'use strict';
  // Run once per page. Loading it twice (an inline loader plus the build's injected one, on 32
  // vault pages until v0.6.13) created a second IntersectionObserver and a second set of print
  // and keyboard listeners. The per-figure dataset.loaded guard hid it; this stops it.
  if (window.__sgitShotsStarted) return;
  window.__sgitShotsStarted = true;

  function vaultHost() {
    var sg = window.sg || (window.parent && window.parent.sg);
    return (sg && sg.vfs && sg.vfs.read) ? sg : null;
  }

  // Images live in the vault's own folder:
  //   demos/vaults/<slug>/index.html  ->  demos/vaults/<slug>/images/<name>
  // A page-relative path means a vault folder is self-contained: move it and its
  // pictures move with it. Deeper pages under the same vault (views/, videos/) point
  // back up with data-dir, so one vault keeps ONE image folder however many pages
  // describe it.
  function pathOf(fig) {
    return (fig.getAttribute('data-dir') || 'images/') + fig.getAttribute('data-shot');
  }

  function failed(fig, name) {
    fig.classList.add('shot--failed');
    var p = document.createElement('p');
    p.className = 'small dim';
    p.textContent = 'screenshot unavailable (' + name + ')';
    fig.insertBefore(p, fig.firstChild);
  }

  // eager=true is the print path: no awaiting anywhere on the web branch, and
  // loading="eager" so the browser does not defer the DECODE of an image that is far
  // below the viewport. That deferral is what used to export blank gaps — the <img>
  // existed and had fetched, but sat at naturalWidth 0 because it had never been
  // scrolled into view.
  function fill(fig, eager) {
    var name = fig.getAttribute('data-shot');
    if (!name) return;
    if (fig.dataset.loaded) {
      if (eager) [].forEach.call(fig.querySelectorAll('img'), function (i) { i.loading = 'eager'; });
      return;
    }
    fig.dataset.loaded = '1';
    var path = pathOf(fig);
    var img  = document.createElement('img');
    img.alt = fig.getAttribute('data-alt') || '';
    img.loading = eager ? 'eager' : 'lazy';
    if (eager) {
      // Print is a deadline, not a scroll. Ask for the bytes ahead of anything else on
      // the page, and for a synchronous decode so the image is presentable the moment
      // it lands rather than a frame later — the paginator does not wait for a frame.
      img.decoding = 'sync';
      try { img.fetchPriority = 'high'; } catch (e) { /* not in every engine */ }
    }
    img.addEventListener('load', function () { fig.classList.add('shot--in'); });
    img.addEventListener('error', function () { failed(fig, name); });

    // A figure with data-href is a picture of something that can be opened: the image
    // becomes a link to it (v0.6.14, every vault page's first screenshot opens its vault).
    var node = img;
    var href = fig.getAttribute('data-href');
    if (href) {
      node = document.createElement('a');
      node.className = 'shot-link';
      node.href = href; node.target = fig.getAttribute('data-href-target') || '_blank'; node.rel = 'noopener';
      node.setAttribute('aria-label', fig.getAttribute('data-href-label') || 'Open the real thing in a new tab');
      node.appendChild(img);
    }
    var sg = vaultHost();
    if (!sg) {                       // the ordinary web: hand the URL straight over
      img.src = path;
      fig.insertBefore(node, fig.firstChild);
      return;
    }
    sg.vfs.read(path).then(function (data) {
      var ext = (path.split('.').pop() || '').toLowerCase();
      img.src = URL.createObjectURL(new Blob([data], { type: ext === 'jpg' || ext === 'jpeg' ? 'image/jpeg' : ext === 'png' ? 'image/png' : 'image/webp' }));
      fig.insertBefore(node, fig.firstChild);
    }, function () { failed(fig, name); });
  }

  // Trail cards (v0.6.102): the same two paths as fill(), for a card thumbnail drawn as a background.
  function trails() {
    var sg = vaultHost();
    [].forEach.call(document.querySelectorAll('[data-trail-img]'), function (el) {
      var path = el.getAttribute('data-trail-img');
      if (!sg) { el.style.backgroundImage = 'url("' + path.replace(/"/g, '%22') + '")'; return; }
      sg.vfs.read(path).then(function (data) {
        var ext = (path.split('.').pop() || '').toLowerCase();
        el.style.backgroundImage = 'url("' + URL.createObjectURL(new Blob([data], { type: ext === 'jpg' || ext === 'jpeg' ? 'image/jpeg' : ext === 'png' ? 'image/png' : 'image/webp' })) + '")';
      }, function () { /* a missing thumbnail leaves the card readable */ });
    });
  }

  function all() {
    return [].slice.call(document.querySelectorAll('figure.shot[data-shot]'));
  }

  function start() {
    trails();
    var figs = all();
    if (!figs.length) return;
    // forEach passes (value, index) — never hand it fill directly, or the index
    // arrives as the `eager` flag and every figure but the first loads eagerly.
    if (!('IntersectionObserver' in window)) {
      figs.forEach(function (f) { fill(f, true); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { io.unobserve(e.target); fill(e.target, false); }
      });
    }, { rootMargin: '400px' });
    figs.forEach(function (f) { io.observe(f); });

    // Print needs every figure; ordinary reading does not. So the bypass fires only
    // when a print is actually starting — nobody pays for it by scrolling past.
    // It works because the web branch of fill() is synchronous: by the time this
    // handler returns, the <img> elements are in the document with loads pending,
    // and Chrome's print pipeline waits for pending image loads before it paginates.
    var printPrep = function () {
      io.disconnect();
      all().forEach(function (f) { fill(f, true); });
    };
    window.addEventListener('beforeprint', printPrep);
    if (window.matchMedia) {                       // Safari fires no beforeprint
      var mq = window.matchMedia('print');
      if (mq.addEventListener) mq.addEventListener('change', function (e) { if (e.matches) printPrep(); });
    }
    // Cmd/Ctrl-P lands a few hundred milliseconds BEFORE beforeprint — the dialog has
    // to open first. Same user action, same "only on print" rule, but the images get a
    // head start on the download instead of racing the paginator from a standing stop.
    // (Measured: with zero grace after beforeprint, 1 of 9 images made the PDF; with
    // any real grace, 9 of 9. This is what buys the grace on a cold page.)
    window.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && !e.altKey && (e.key === 'p' || e.key === 'P')) printPrep();
    }, true);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
}());
