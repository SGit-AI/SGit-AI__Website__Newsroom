// The writer register (admin/writer/register.json; the rule is in admin/build/writer_register.js).
//   node admin/writer/tools/register.cjs open  --id writer-NN --session <claude session url> --approved <path to the editor's words>
//   node admin/writer/tools/register.cjs close --id writer-NN [--reason "..."]
// open makes a new ed25519 key; the private half goes to ~/.newsroom-writer/<id>.pem and never into the
// repository. close marks the registration closed and deletes the private half: the key is never used again.
// Only open a registration at the editor's word, and only when no other is open.
'use strict';
const fs = require('fs'), path = require('path'), os = require('os'), crypto = require('crypto');
const { fingerprint, REL } = require('../../build/writer_register');
const ROOT = path.resolve(__dirname, '..', '..', '..');
const FILE = path.join(ROOT, REL), KEYS = path.join(os.homedir(), '.newsroom-writer');
const args = process.argv.slice(2), cmd = args[0];
const opt = k => { const i = args.indexOf('--' + k); return i > 0 ? args[i + 1] : undefined; };
const reg = JSON.parse(fs.readFileSync(FILE, 'utf8'));
const now = new Date().toISOString().replace(/\.\d+Z$/, 'Z');
const id = opt('id');
if (!id) { console.error('--id is required'); process.exit(2); }

if (cmd === 'open') {
  const open = reg.registrations.filter(r => !r.closed);
  if (open.length) { console.error(`refused: ${open.map(r => r.id).join(', ')} is open; the editor closes it first`); process.exit(1); }
  if (reg.registrations.some(r => r.id === id)) { console.error(`refused: ${id} exists; a registration is never reopened, take a new id`); process.exit(1); }
  const approved = opt('approved');
  if (!approved || !fs.existsSync(path.join(ROOT, approved))) { console.error('refused: --approved must point at the editor\'s words in the repository'); process.exit(1); }
  const { publicKey, privateKey } = crypto.generateKeyPairSync('ed25519');
  const pub = publicKey.export({ format: 'der', type: 'spki' }).toString('base64');
  fs.mkdirSync(KEYS, { recursive: true, mode: 0o700 });
  fs.writeFileSync(path.join(KEYS, id + '.pem'), privateKey.export({ format: 'pem', type: 'pkcs8' }), { mode: 0o600 });
  reg.registrations.push({ id, session: opt('session') || null, opened: now, closed: null,
    key: { alg: 'ed25519', public: pub, fingerprint: fingerprint(pub) }, approved });
  console.log(`opened ${id}, key ${fingerprint(pub)}; private half in ${path.join(KEYS, id + '.pem')}`);
} else if (cmd === 'close') {
  const r = reg.registrations.find(x => x.id === id);
  if (!r || r.closed) { console.error(`refused: ${id} is not open`); process.exit(1); }
  r.closed = now; if (opt('reason')) r.closed_because = opt('reason');
  fs.rmSync(path.join(KEYS, id + '.pem'), { force: true });
  console.log(`closed ${id}; its key is never used again`);
} else { console.error('usage: register.cjs open|close --id ...'); process.exit(2); }
fs.writeFileSync(FILE, JSON.stringify(reg, null, 1) + '\n');
