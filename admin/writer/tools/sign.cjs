// Signs what is staged, for a writer's commit (check 15 of admin/build/validate.js).
//   git add -A && node admin/writer/tools/sign.cjs
// prints two lines to put in the commit message, after the body and before Co-Authored-By:
//   Writer-Registration: writer-NN
//   Writer-Signature: <ed25519 over "newsroom.writer|writer-NN|<tree of the staged index>">
// Stage nothing after signing: the signature covers the tree exactly as staged.
'use strict';
const fs = require('fs'), path = require('path'), os = require('os'), crypto = require('crypto');
const { execFileSync } = require('child_process');
const { statement, REL } = require('../../build/writer_register');
const ROOT = path.resolve(__dirname, '..', '..', '..');
const reg = JSON.parse(fs.readFileSync(path.join(ROOT, REL), 'utf8'));
const open = reg.registrations.filter(r => !r.closed);
if (open.length !== 1) { console.error(`refused: ${open.length} open registrations; exactly one writer signs`); process.exit(1); }
const id = open[0].id, pem = path.join(os.homedir(), '.newsroom-writer', id + '.pem');
if (!fs.existsSync(pem)) { console.error(`refused: no private key for ${id} on this machine; this session is not ${id}`); process.exit(1); }
const tree = execFileSync('git', ['write-tree'], { cwd: ROOT, encoding: 'utf8' }).trim();
const sig = crypto.sign(null, Buffer.from(statement(id, tree)), crypto.createPrivateKey(fs.readFileSync(pem)));
console.log(`Writer-Registration: ${id}\nWriter-Signature: ${sig.toString('base64')}`);
