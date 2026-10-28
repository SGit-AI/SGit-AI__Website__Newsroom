import sharp from 'sharp'; import fs from 'fs';
const OUT=(process.env.OUT_DIR || './out/');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const INK='#1A1917',TEAL='#0F766E',ORANGE='#C2410C',BLUE='#1F4FD1',PURPLE='#7C3AED',GREY='#8A8780',RED='#B91C1C',BODY='#3C3A36',LINE='#D5D0C2';
const wrap=(s,max)=>{const w=s.split(' ');const L=[];let c='';for(const x of w){if((c+' '+x).trim().length>max){L.push(c.trim());c=x;}else c+=' '+x;}if(c.trim())L.push(c.trim());return L;};
const text=(x,y,lines,size,fill,extra='')=>lines.map((l,i)=>`<text x="${x}" y="${y+i*(size+5)}" font-size="${size}" fill="${fill}" ${extra}>${esc(l)}</text>`).join('');
const head=(W,H,t,sub)=>`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" font-family="ui-sans-serif,system-ui,sans-serif"><rect width="${W}" height="${H}" fill="#F7F6F2"/><text x="40" y="44" font-family="Georgia,serif" font-size="28" fill="${INK}">${esc(t)}</text>`+text(40,74,wrap(sub,165),14,BODY);
const foot=(W,H,t)=>`<text x="${W-40}" y="${H-14}" font-size="11" fill="${GREY}" text-anchor="end">${esc(t)}</text></svg>`;
const save=async(s,n)=>{const png=await sharp(Buffer.from(s),{density:144}).resize({width:1400}).png().toBuffer(); fs.writeFileSync('png/'+n+'.png',png); await sharp(png).webp({quality:88}).toFile(OUT+n+'.webp');};
const box=(x,y,w,h,t,b,c,fill='#fff',dash='')=>{const tl=wrap(t,Math.floor((w-32)/9.2));return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12" fill="${fill}" stroke="${c}" stroke-width="2" ${dash}/>`+text(x+16,y+30,tl,16,c,'font-weight="700"')+text(x+16,y+30+tl.length*21+6,wrap(b,Math.floor((w-32)/7.2)),13.5,BODY);};
const arr=(x1,y1,x2,y2,c,label='',dash='')=>{const a=Math.atan2(y2-y1,x2-x1),hx=x2-12*Math.cos(a),hy=y2-12*Math.sin(a);return `<line x1="${x1}" y1="${y1}" x2="${hx}" y2="${hy}" stroke="${c}" stroke-width="2.4" ${dash}/><path d="M${hx-6*Math.sin(a)},${hy+6*Math.cos(a)} L${x2},${y2} L${hx+6*Math.sin(a)},${hy-6*Math.cos(a)} Z" fill="${c}"/>`+(label?text((x1+x2)/2-60,(y1+y2)/2-10,[label],12.5,c,'font-weight="700"'):'');};
const MUTE = '#6B6860', GRID = '#E4E0D6';
// vertical bars, one series; rounded data end, 2px gap, direct labels on a few
function vbars(x, y, w, h, data, col, lab = (v) => String(v), every = 1, labelAll = true) {
  const mx = Math.max(...data.map(d => d[1])), bw = w / data.length; let s = '';
  [0.5, 1].forEach(f => { const yy = y + h - h * f; s += `<line x1="${x}" y1="${yy}" x2="${x + w}" y2="${yy}" stroke="${GRID}"/><text x="${x - 8}" y="${yy + 4}" font-size="12" fill="${MUTE}" text-anchor="end">${Math.round(mx * f)}</text>`; });
  s += `<line x1="${x}" y1="${y + h}" x2="${x + w}" y2="${y + h}" stroke="${MUTE}"/>`;
  data.forEach((d, i) => { const bh = Math.max(1, h * d[1] / mx), bx = x + i * bw + 1, bwid = bw - 2;
    s += `<path d="M${bx},${y + h} V${y + h - bh + 4} Q${bx},${y + h - bh} ${bx + 4},${y + h - bh} H${bx + bwid - 4} Q${bx + bwid},${y + h - bh} ${bx + bwid},${y + h - bh + 4} V${y + h} Z" fill="${col}"/>`;
    if (labelAll && d[1]) s += `<text x="${bx + bwid / 2}" y="${y + h - bh - 6}" font-size="12" fill="${INK}" text-anchor="middle">${d[1]}</text>`;
    if (i % every === 0) s += `<text x="${bx + bwid / 2}" y="${y + h + 18}" font-size="12" fill="${MUTE}" text-anchor="middle">${esc(lab(d[0]))}</text>`; });
  return s;
}
function hbars(x, y, w, rowh, data, col) {
  const mx = Math.max(...data.map(d => d[1])); let s = '';
  data.forEach((d, i) => { const yy = y + i * rowh, bw = Math.max(2, w * d[1] / mx);
    s += `<text x="${x - 12}" y="${yy + rowh / 2 + 5}" font-size="14" fill="${INK}" text-anchor="end">${esc(d[0])}</text>`;
    s += `<path d="M${x},${yy + 4} H${x + bw - 4} Q${x + bw},${yy + 4} ${x + bw},${yy + 8} V${yy + rowh - 10} Q${x + bw},${yy + rowh - 6} ${x + bw - 4},${yy + rowh - 6} H${x} Z" fill="${col}"/>`;
    s += `<text x="${x + bw + 8}" y="${yy + rowh / 2 + 5}" font-size="13" fill="${INK}">${d[1]}</text>`; });
  return s;
}
const GREEN='#15803D',AMBER='#B7791F';
const lbl=(x,y,t,c=MUTE,sz=13,extra='')=>`<text x="${x}" y="${y}" font-size="${sz}" fill="${c}" ${extra}>${esc(t)}</text>`;
let s;
