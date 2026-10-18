/* The map of the graph of meaning, drawn in the page from data/map.json. No library: SVG by createElementNS, text
   nodes only, every colour a theme token (graphs.css). Two layouts (spectral, force), two colourings (the cut, the
   clusters), labels for the top thirty or all, hover for a name, click for its page. Below, the same nodes turned in
   three dimensions on a canvas, from the Laplacian's second to fourth eigenvectors. */
(function () {
  'use strict';
  var SVG = 'http://www.w3.org/2000/svg';
  var svg = document.getElementById('gm-live');
  var pick = document.getElementById('gm-pick');
  var canvas = document.getElementById('gm-3d');
  if (!svg) return;
  var W = 900, H = 620, PAD = 40;
  var state = { layout: 'cut', colour: 'side2', labels: 30 };
  var data = null;
  var CLUSTER_COLOURS = ['--accent', '--warm', '--info-ink', '--yellow', '--red', '--accent-dk', '--dim', '--head'];

  function el(tag, attrs, parent) {
    var e = document.createElementNS(SVG, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function token(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || '#0f766e';
  }
  function nodeFile(id) { var i = id.indexOf(':'); return 'nodes/' + id.slice(0, i) + '--' + id.slice(i + 1) + '.html'; }

  function coords(n) {
    if (state.layout === 'spectral') return [n.x3, n.y3];
    if (state.layout === 'cut') return [n.xr, n.y];
    return [n.x, n.y];
  }
  function scaled(nodes) {
    var xs = nodes.map(function (n) { return coords(n)[0]; }), ys = nodes.map(function (n) { return coords(n)[1]; });
    var lo = [Math.min.apply(null, xs), Math.min.apply(null, ys)], hi = [Math.max.apply(null, xs), Math.max.apply(null, ys)];
    return nodes.map(function (n) {
      var c = coords(n);
      return [PAD + (c[0] - lo[0]) / ((hi[0] - lo[0]) || 1) * (W - 2 * PAD), PAD + (c[1] - lo[1]) / ((hi[1] - lo[1]) || 1) * (H - 2 * PAD)];
    });
  }
  function colourOf(n) {
    if (state.colour === 'side' || state.colour === 'side2') {
      var sd = state.colour === 'side' ? n.side : n.side2;
      return token(sd === 1 ? '--warm' : sd === 0 ? '--accent' : '--line2');
    }
    if (n.cluster < 0) return token('--line2');
    return token(CLUSTER_COLOURS[n.cluster % CLUSTER_COLOURS.length]);
  }

  function draw() {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var nodes = data.nodes, P = scaled(nodes);
    var maxW = 1;
    data.edges.forEach(function (e) { if (e[3] > maxW) maxW = e[3]; });
    var thr = 0;
    var ws = data.edges.map(function (e) { return e[3]; }).sort(function (a, b) { return a - b; });
    if (ws.length) thr = ws[Math.floor(ws.length * 0.8)];
    var g = el('g', {}, svg);
    data.edges.forEach(function (e) {
      if (e[3] < thr) return;
      var a = nodes[e[0]], b = nodes[e[1]];
      var cross = state.colour === 'side' ? a.side !== b.side : state.colour === 'side2' ? a.side2 !== b.side2 : a.cluster !== b.cluster;
      el('line', { 'class': 'edge' + (cross ? ' strong' : ''), x1: P[e[0]][0].toFixed(1), y1: P[e[0]][1].toFixed(1), x2: P[e[1]][0].toFixed(1), y2: P[e[1]][1].toFixed(1), 'stroke-width': (0.5 + 2.5 * e[3] / maxW).toFixed(2) }, g);
    });
    var order = nodes.map(function (n, i) { return i; }).sort(function (a, b) { return nodes[b].articles - nodes[a].articles; });
    var gn = el('g', {}, svg);
    order.slice().reverse().forEach(function (i) {
      var n = nodes[i];
      var c = el('circle', { 'class': 'node', cx: P[i][0].toFixed(1), cy: P[i][1].toFixed(1), r: (2.5 + 2.2 * Math.sqrt(n.articles)).toFixed(1) }, gn);
      c.style.fill = colourOf(n);
      c.addEventListener('mouseenter', function () { show(n); });
      c.addEventListener('focus', function () { show(n); });
      c.addEventListener('click', function () { window.location.href = nodeFile(n.id); });
      c.setAttribute('tabindex', '0');
    });
    var gl = el('g', {}, svg);
    var lim = state.labels === 'all' ? order.length : state.labels;
    order.slice(0, lim).forEach(function (i, rank) {
      var n = nodes[i];
      var t = el('text', { 'class': 'lbl' + (rank < 10 ? ' big' : ''), x: (P[i][0] + 4 + 2.2 * Math.sqrt(n.articles)).toFixed(1), y: (P[i][1] + 4).toFixed(1) }, gl);
      t.appendChild(document.createTextNode(n.label.length > 30 ? n.label.slice(0, 29) + '…' : n.label));
    });
    var cap = el('text', { 'class': 'cap', x: PAD, y: H - 12 }, svg);
    cap.appendChild(document.createTextNode(state.colour === 'side' ? 'colour: the two sides of the cut, the frame included. size: articles. thicker lines: more shared articles; teal lines cross the cut.'
      : state.colour === 'side2' ? 'colour: the two sides of the cut made without the frame; grey: the frame. size: articles. thicker lines: more shared articles; teal lines cross the cut.'
      : 'colour: cluster (' + data.clusters.length + '); grey: unplaced. size: articles. thicker lines: more shared articles; teal lines cross clusters.'));
  }

  function show(n) {
    while (pick.firstChild) pick.removeChild(pick.firstChild);
    var b = document.createElement('b'); b.appendChild(document.createTextNode(n.label));
    pick.appendChild(b);
    var cl = data.clusters[n.cluster];
    pick.appendChild(document.createTextNode(' · ' + (n.kind === 'entity' ? ('a name' + (n.type ? ', ' + n.type : '')) : 'an idea') + ' · ' + n.articles + ' articles, ' + n.claims + ' claims · ' + (n.side2 < 0 ? 'the frame' : 'side ' + n.side2) + ' · ' + (n.cluster < 0 ? 'unplaced' : 'cluster ' + n.cluster + (cl ? ' (' + cl.label + ')' : '')) + ' · first in '));
    var a = document.createElement('a'); a.href = '../articles/' + n.first + '.html';
    a.appendChild(document.createTextNode((data.articles[n.first] || {}).title || n.first));
    pick.appendChild(a);
    pick.appendChild(document.createTextNode(' · '));
    var a2 = document.createElement('a'); a2.href = nodeFile(n.id); a2.appendChild(document.createTextNode('what the newsroom states about it'));
    pick.appendChild(a2);
  }

  document.querySelectorAll('.gm-controls button[data-layout],.gm-controls button[data-colour],.gm-controls button[data-labels]').forEach(function (b) {
    b.addEventListener('click', function () {
      var key = b.dataset.layout ? 'layout' : b.dataset.colour ? 'colour' : 'labels';
      var val = b.dataset.layout || b.dataset.colour || b.dataset.labels;
      state[key] = key === 'labels' && val !== 'all' ? parseInt(val, 10) : val;
      document.querySelectorAll('.gm-controls button[data-' + key + ']').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      draw();
      if (key === 'colour') draw3d.colourChanged = true;
    });
  });

  /* ---- the 3D turn */
  var spin = true, ang = 0.6, tilt = 0.35, dragging = false, last = null, raf = null;
  function draw3d() {
    if (!canvas || !data) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = token('--panel'); ctx.fillRect(0, 0, w, h);
    var nodes = data.nodes;
    var ca = Math.cos(ang), sa = Math.sin(ang), ct = Math.cos(tilt), st = Math.sin(tilt);
    var pts = nodes.map(function (n) {
      var x = n.xf, y = n.yf, z = n.zf;
      var x1 = x * ca - z * sa, z1 = x * sa + z * ca;          // turn about y
      var y2 = y * ct - z1 * st, z2 = y * st + z1 * ct;        // tilt about x
      var depth = 1 / (1 + 0.18 * (z2 + 3));
      return { x: w / 2 + x1 * (w / 4.2) * depth, y: h / 2 + y2 * (h / 4.2) * depth, z: z2, d: depth, n: n };
    });
    var maxW = 1; data.edges.forEach(function (e) { if (e[2] > maxW) maxW = e[2]; });
    ctx.lineWidth = 0.6;
    data.edges.forEach(function (e) {
      if (e[2] < 3) return;
      var a = pts[e[0]], b = pts[e[1]];
      var cross = state.colour === 'side' ? a.n.side !== b.n.side : state.colour === 'side2' ? a.n.side2 !== b.n.side2 : a.n.cluster !== b.n.cluster;
      ctx.strokeStyle = token(cross ? '--accent' : '--line2');
      ctx.globalAlpha = 0.25 + 0.5 * (e[2] / maxW);
      ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
    });
    ctx.globalAlpha = 1;
    pts.slice().sort(function (p, q) { return p.z - q.z; }).forEach(function (p) {
      var r = (2 + 2 * Math.sqrt(p.n.articles)) * p.d;
      ctx.fillStyle = colourOf(p.n);
      ctx.globalAlpha = 0.55 + 0.45 * p.d;
      ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, Math.PI * 2); ctx.fill();
    });
    ctx.globalAlpha = 1;
    ctx.fillStyle = token('--head'); ctx.font = '12px Georgia, serif';
    pts.slice().sort(function (p, q) { return q.n.articles - p.n.articles; }).slice(0, 12).forEach(function (p) {
      ctx.fillText(p.n.label.length > 26 ? p.n.label.slice(0, 25) + '…' : p.n.label, p.x + 6, p.y + 4);
    });
    ctx.fillStyle = token('--dim'); ctx.font = '12px Georgia, serif';
    ctx.fillText('a force layout in three dimensions. colour: ' + (state.colour === 'cluster' ? 'clusters' : 'the cut') + '. drag to turn.', 12, h - 10);
  }
  function tick() {
    if (spin && !dragging) ang += 0.004;
    draw3d();
    raf = window.requestAnimationFrame(tick);
  }
  if (canvas) {
    var spinBtn = document.getElementById('gm-spin');
    if (spinBtn) spinBtn.addEventListener('click', function () { spin = !spin; spinBtn.setAttribute('aria-pressed', spin ? 'true' : 'false'); spinBtn.textContent = spin ? 'Turning' : 'Still'; });
    canvas.addEventListener('pointerdown', function (e) { dragging = true; last = [e.clientX, e.clientY]; canvas.setPointerCapture(e.pointerId); });
    canvas.addEventListener('pointermove', function (e) { if (!dragging) return; ang += (e.clientX - last[0]) * 0.008; tilt += (e.clientY - last[1]) * 0.006; last = [e.clientX, e.clientY]; });
    canvas.addEventListener('pointerup', function () { dragging = false; });
    canvas.addEventListener('pointercancel', function () { dragging = false; });
  }

  fetch('data/map.json').then(function (r) { return r.json(); }).then(function (d) {
    data = d;
    draw();
    if (canvas) tick();
  }).catch(function (e) {
    while (pick.firstChild) pick.removeChild(pick.firstChild);
    pick.appendChild(document.createTextNode('The map could not load data/map.json: ' + e));
  });
})();
