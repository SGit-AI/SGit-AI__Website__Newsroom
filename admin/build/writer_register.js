// The writer register: one journalist agent at a time (the editor's rule, 31 October 2026,
// admin/notes/2026-10-31__one-writer/memo-01.md), or two as twins on different accounts since the editor's word of
// 22 November 2026 (admin/notes/2026-11-22__newsroom.d-twin/memo-01.md). Used by validate.js as check 15.
//
// admin/writer/register.json lists every writer registration. A registration is opened only at the
// editor's word, with a new ed25519 key made by the session; the private half never leaves the
// session's machine. A registration that is closed stays closed, and its key is never used again;
// the same Claude session may be given a new registration, with a new key, never the old one back.
//
// Checked here:
//   - ids and key fingerprints are unique, so a closed key cannot come back under a new id;
//   - at most max_open registrations are open (1, or 2 or 3 with the editor's approval on file), each on its own account
//     when there is more than one, and each has a key and the editor's approval on file;
//   - every fingerprint matches its public key;
//   - when the commit being built is a writer's ("@newsroom.writer:"), it names the open
//     registration and carries its signature over the commit's tree;
//   - when the signing registration carries "git_signing" (signed commits for every agent, the
//     editor's word of 19 November 2026, admin/notes/2026-11-19__signed-commits/notes.md), the
//     commit is also a git SSH signature by that same key (namespace "git"), and its Claude-Session:
//     trailer names the registration's session; CI's own version commits ("site v...") are not
//     writer commits and are exempt;
//   - with full history (locally; CI checks out one commit), no registration that was ever
//     closed is open now, and every writer commit since its registration's git_signing began
//     passes the same signature check.
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execFileSync } = require('child_process');

const REL = 'admin/writer/register.json';

function fingerprint(pub) {
  return 'sha256:' + crypto.createHash('sha256').update(Buffer.from(pub, 'base64')).digest('hex').slice(0, 32);
}
function statement(id, tree) { return `newsroom.writer|${id}|${tree}`; }

function git(root, args) {
  try { return execFileSync('git', args, { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }); }
  catch { return null; }
}

// A commit's git SSH signature (OpenSSH SSHSIG, ed25519), verified against a registration's key without ssh-keygen.
function u32(n) { const b = Buffer.alloc(4); b.writeUInt32BE(n); return b; }
function sstr(x) { const b = Buffer.isBuffer(x) ? x : Buffer.from(x); return Buffer.concat([u32(b.length), b]); }
function rd(b, o) { const n = b.readUInt32BE(o); return [b.subarray(o + 4, o + 4 + n), o + 4 + n]; }
function sshLine(spkiB64) {
  const raw = Buffer.from(crypto.createPublicKey({ key: Buffer.from(spkiB64, 'base64'), format: 'der', type: 'spki' }).export({ format: 'jwk' }).x, 'base64url');
  return 'ssh-ed25519 ' + Buffer.concat([sstr('ssh-ed25519'), sstr(raw)]).toString('base64');
}
function gitSigError(root, sha, r) {
  const obj = git(root, ['cat-file', 'commit', sha]);
  if (!obj) return 'cannot read the commit';
  const lines = obj.split('\n'), keep = [], sig = [];
  let i = 0, inSig = false;
  for (; i < lines.length && lines[i] !== ''; i++) {
    if (lines[i].startsWith('gpgsig ')) { inSig = true; sig.push(lines[i].slice(7)); }
    else if (inSig && lines[i].startsWith(' ')) sig.push(lines[i].slice(1));
    else { inSig = false; keep.push(lines[i]); }
  }
  if (!sig.length) return 'no git signature (unsigned; admin/writer/tools/signing-setup.sh)';
  const payload = Buffer.from(keep.concat(lines.slice(i)).join('\n'));
  try {
    const b = Buffer.from(sig.join('\n').replace(/-----(BEGIN|END) SSH SIGNATURE-----/g, '').replace(/\s+/g, ''), 'base64');
    if (b.subarray(0, 6).toString() !== 'SSHSIG') return 'the signature is not an SSH signature';
    let o = 10, pk, ns, rs, ha, sg;
    [pk, o] = rd(b, o); [ns, o] = rd(b, o); [rs, o] = rd(b, o); [ha, o] = rd(b, o); [sg, o] = rd(b, o);
    if ('ssh-ed25519 ' + pk.toString('base64') !== sshLine(r.key.public)) return `signed by another key, not ${r.id}'s`;
    if (ns.toString() !== 'git') return 'the signature is not in the git namespace';
    const alg = ha.toString(); if (!/^sha(256|512)$/.test(alg)) return `unexpected hash ${alg}`;
    const [st, so] = rd(sg, 0); if (st.toString() !== 'ssh-ed25519') return 'not an ed25519 signature';
    const msg = Buffer.concat([Buffer.from('SSHSIG'), sstr('git'), sstr(rs), sstr(alg), sstr(crypto.createHash(alg).update(payload).digest())]);
    const pub = crypto.createPublicKey({ key: Buffer.from(r.key.public, 'base64'), format: 'der', type: 'spki' });
    if (!crypto.verify(null, msg, pub, rd(sg, so)[0])) return `${r.id}'s git signature does not verify`;
  } catch (e) { return `the signature cannot be read (${e.message})`; }
  const sess = (obj.match(/^Claude-Session:\s*\S*?(session_[A-Za-z0-9]+)/m) || [])[1];
  const want = ((r.session || '').match(/session_[A-Za-z0-9]+/) || [])[0];
  if (!sess || sess !== want) return `Claude-Session ${sess || '(none)'} is not ${r.id}'s session ${want || '(none)'}`;
  return null;
}

function check(root, errors) {
  const file = path.join(root, REL);
  if (!fs.existsSync(file)) { errors.push(`${REL}: missing; the writer register is required`); return; }
  let reg;
  try { reg = JSON.parse(fs.readFileSync(file, 'utf8')); }
  catch (e) { errors.push(`${REL}: not JSON (${e.message})`); return; }
  const list = reg.registrations || [];
  const ids = new Set(), fps = new Set();
  for (const r of list) {
    if (ids.has(r.id)) errors.push(`${REL}: registration ${r.id} appears twice`);
    ids.add(r.id);
    if (r.key) {
      if (fingerprint(r.key.public) !== r.key.fingerprint) errors.push(`${REL}: ${r.id}'s fingerprint does not match its public key`);
      if (fps.has(r.key.fingerprint)) errors.push(`${REL}: ${r.id} reuses a key; a key is never used again`);
      fps.add(r.key.fingerprint);
    }
  }
  const open = list.filter(r => !r.closed);
  // How many may be open: one, unless the editor raised it (two since 22 November 2026, twins on different accounts;
  // three since the same evening, one per account, admin/notes/2026-11-22__newsroom.c-twin/memo-01.md).
  let max = 1;
  if (reg.max_open !== undefined) {
    if (!Number.isInteger(reg.max_open) || reg.max_open < 1 || reg.max_open > 3) errors.push(`${REL}: max_open must be 1, 2 or 3`);
    else if (reg.max_open > 1 && (!reg.max_open_approved || !fs.existsSync(path.join(root, reg.max_open_approved)))) errors.push(`${REL}: max_open ${reg.max_open} does not point at the editor's approval in the repository`);
    else max = reg.max_open;
  }
  if (open.length > max) errors.push(`${REL}: ${open.length} registrations are open (${open.map(r => r.id).join(', ')}); at most ${max}, and only the editor decides otherwise`);
  if (open.length > 1) {
    const accts = open.map(r => r.account);
    if (accts.some(a => !a)) errors.push(`${REL}: with more than one writer open, every open registration names its account (${open.filter(r => !r.account).map(r => r.id).join(', ')} does not)`);
    else if (new Set(accts).size !== accts.length) errors.push(`${REL}: two open writers on the same account (${accts.join(', ')}); twins run on different accounts`);
  }
  for (const r of open) {
    if (!r.key) errors.push(`${REL}: open registration ${r.id} has no key`);
    if (!r.approved || !fs.existsSync(path.join(root, r.approved))) errors.push(`${REL}: open registration ${r.id} does not point at the editor's approval in the repository`);
  }

  // The commit being built: a writer's commit must be signed by the open registration.
  const msg = git(root, ['log', '-1', '--format=%B']);
  const tree = (git(root, ['rev-parse', 'HEAD^{tree}']) || '').trim();
  if (msg && tree && /^@newsroom\.writer:/.test(msg)) {
    const id = (msg.match(/^Writer-Registration:\s*(\S+)/m) || [])[1];
    const sig = (msg.match(/^Writer-Signature:\s*(\S+)/m) || [])[1];
    const r = list.find(x => x.id === id);
    if (!id || !sig) errors.push(`HEAD: a writer's commit without Writer-Registration and Writer-Signature (admin/writer/tools/sign.cjs)`);
    else if (!r) errors.push(`HEAD: signed by ${id}, which is not in ${REL}`);
    else if (r.closed) errors.push(`HEAD: signed by ${id}, which is closed; its key is never used again`);
    else if (!r.key) errors.push(`HEAD: signed by ${id}, which has no key`);
    else {
      const pub = crypto.createPublicKey({ key: Buffer.from(r.key.public, 'base64'), format: 'der', type: 'spki' });
      if (!crypto.verify(null, Buffer.from(statement(id, tree)), pub, Buffer.from(sig, 'base64')))
        errors.push(`HEAD: ${id}'s signature does not verify over tree ${tree.slice(0, 12)}`);
      if (r.git_signing) { const e = gitSigError(root, 'HEAD', r); if (e) errors.push(`HEAD: ${e}`); }
    }
  }

  // Closed stays closed, where the history is here to check it.
  if ((git(root, ['rev-parse', '--is-shallow-repository']) || '').trim() === 'false') {
    const shas = (git(root, ['log', '--format=%H', '--', REL]) || '').split('\n').filter(Boolean);
    const everClosed = new Set();
    for (const sha of shas) {
      const old = git(root, ['show', `${sha}:${REL}`]);
      if (!old) continue;
      try { for (const r of JSON.parse(old).registrations || []) if (r.closed) everClosed.add(r.id); } catch {}
    }
    for (const r of open) if (everClosed.has(r.id)) errors.push(`${REL}: ${r.id} was closed and is open again; a closed registration is never reopened`);
    for (const e of checkSignatures(root).fails) errors.push(e);
  }
}

// Every commit since git_signing began (security@'s five controls, via conductor.b@, 19 November 2026):
//   - every non-merge writer commit ("@newsroom.writer:") in the history since the earliest git_signing.since is
//     checked, side branches included; a writer commit that is a merge fails (a writer never merges);
//   - each commit is checked against its PARENT's register, never its own, so a commit cannot add the key it is signed
//     with; the commit that first publishes a registration's git_signing is the one commit of it not yet checked;
//   - the Claude-Session: must be the registration's full session;
//   - no exemption by name or subject: a commit that is not a writer's is not checked as one. Unsigned commits by
//     anyone else (CI's version commits, @newsroom.accountant) are listed as warnings, not passed silently; making
//     them fail needs CI and every other agent to sign, which is the editor's to decide (register.json "enforce").
// One failure fails validate.js, and the deploy workflow's signatures job refuses the release.
function checkSignatures(root, rev = 'HEAD') {
  const fails = [], warns = [];
  let reg; try { reg = JSON.parse(fs.readFileSync(path.join(root, REL), 'utf8')); } catch { return { fails, warns }; }
  const starts = (reg.registrations || []).filter(r => r.git_signing).map(r => r.git_signing.since).sort();
  if (!starts.length) return { fails, warns };
  const log = git(root, ['log', rev, `--since=${starts[0]}`, '--format=%H%x1f%P%x1f%B%x1e']) || '';
  const regAt = new Map();
  for (const rec of log.split('\x1e').map(x => x.trim()).filter(Boolean)) {
    const [sha, parents, body] = rec.split('\x1f'), id = sha.slice(0, 10), writer = /^@newsroom\.writer:/.test(body);
    if (parents.split(' ').length > 1) { (writer ? fails : warns).push(`${id}: a merge commit${writer ? ' by the writer; a writer never merges' : ''}`); continue; }
    if (!writer) { if (!/^gpgsig /m.test(git(root, ['cat-file', 'commit', sha]) || '')) warns.push(`${id}: unsigned, not a writer commit (${body.split('\n')[0].slice(0, 50)})`); continue; }
    const rid = (body.match(/^Writer-Registration:\s*(\S+)/m) || [])[1];
    if (!rid) { fails.push(`${id}: a writer commit with no Writer-Registration`); continue; }
    if (!regAt.has(parents)) { let j = null; try { j = JSON.parse(git(root, ['show', `${parents}:${REL}`]) || 'null'); } catch {} regAt.set(parents, j); }
    const pr = regAt.get(parents), r = pr && (pr.registrations || []).find(x => x.id === rid);
    if (!pr) { fails.push(`${id}: its parent has no readable ${REL}`); continue; }
    if (!r) { fails.push(`${id}: ${rid} is not in its parent's register`); continue; }
    if (r.closed) { fails.push(`${id}: ${rid} was already closed in its parent's register`); continue; }
    if (!r.git_signing) continue;   // the commit that publishes git_signing for this registration
    const e = gitSigError(root, sha, r); if (e) fails.push(`${id}: ${e}`);
  }
  return { fails, warns };
}

module.exports = { check, checkSignatures, fingerprint, statement, gitSigError, sshLine, REL };
