// The writer register: one journalist agent at a time (the editor's rule, 31 October 2026,
// admin/notes/2026-10-31__one-writer/memo-01.md). Used by validate.js as check 15.
//
// admin/writer/register.json lists every writer registration. A registration is opened only at the
// editor's word, with a new ed25519 key made by the session; the private half never leaves the
// session's machine. A registration that is closed stays closed, and its key is never used again;
// the same Claude session may be given a new registration, with a new key, never the old one back.
//
// Checked here:
//   - ids and key fingerprints are unique, so a closed key cannot come back under a new id;
//   - at most one registration is open, and it has a key and the editor's approval on file;
//   - every fingerprint matches its public key;
//   - when the commit being built is a writer's ("@newsroom.writer:"), it names the open
//     registration and carries its signature over the commit's tree;
//   - with full history (locally; CI checks out one commit), no registration that was ever
//     closed is open now.
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
  if (open.length > 1) errors.push(`${REL}: ${open.length} registrations are open (${open.map(r => r.id).join(', ')}); only one writer at a time, and only the editor decides otherwise by closing one`);
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
  }
}

module.exports = { check, fingerprint, statement, REL };
