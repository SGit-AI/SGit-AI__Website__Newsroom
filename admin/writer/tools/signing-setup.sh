#!/usr/bin/env bash
# signing-setup.sh: sign the writer's commits in this checkout as git SSH signatures, with the writer's registered key
# (Dinis, 19 November 2026; admin/notes/2026-11-19__signed-commits/notes.md).
#   bash admin/writer/tools/signing-setup.sh [--publish]
# Uses the open registration in admin/writer/register.json and its private half ~/.newsroom-writer/<id>.pem (made by
# register.cjs open; never committed, never printed). Sets THIS checkout's git only (never global: the environment's own
# signer stays for its other repositories): gpg.format ssh, gpg.ssh.program admin/writer/tools/sshsig.mjs,
# user.signingkey the .pem, commit.gpgsign true. --publish writes the key's OpenSSH line and the time into the open
# registration as "git_signing"; from then on validate.js check 15 requires every commit of that registration to carry
# a git SSH signature by that key and a Claude-Session: trailer naming the registration's session. Commit that change
# yourself, signed (the setup is done first, so it is).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
# With twins (two open registrations), the one whose private key is on this machine, as sign.cjs does.
ID=$(node -e 'const fs=require("fs"),os=require("os"),r=require("./admin/writer/register.json").registrations.filter(x=>!x.closed&&fs.existsSync(os.homedir()+"/.newsroom-writer/"+x.id+".pem"));if(r.length!==1){console.error("signing-setup: "+r.length+" open registrations with a key on this machine; exactly one signs");process.exit(1)}console.log(r[0].id)')
KEY="$HOME/.newsroom-writer/$ID.pem"
[ -f "$KEY" ] || { echo "signing-setup: no private key for $ID on this machine ($KEY); this session is not $ID"; exit 1; }
git config --local gpg.format ssh
git config --local gpg.ssh.program "$PWD/admin/writer/tools/sshsig.mjs"
git config --local user.signingkey "$KEY"
git config --local commit.gpgsign true
LINE=$(node -e '
  const c=require("crypto"),fs=require("fs"),k=c.createPublicKey(c.createPrivateKey(fs.readFileSync(process.argv[1])));
  const raw=Buffer.from(k.export({format:"jwk"}).x,"base64url"),s=b=>{const l=Buffer.alloc(4);l.writeUInt32BE(b.length);return Buffer.concat([l,b])};
  console.log("ssh-ed25519 "+Buffer.concat([s(Buffer.from("ssh-ed25519")),s(raw)]).toString("base64"))' "$KEY")
echo "signing-setup: this checkout signs as $ID with $LINE"
if [ "${1:-}" = "--publish" ]; then
  node -e '
    const fs=require("fs"),[id,line]=process.argv.slice(1),f="admin/writer/register.json",j=JSON.parse(fs.readFileSync(f,"utf8"));
    const r=j.registrations.find(x=>x.id===id&&!x.closed);
    r.git_signing={ssh:line,since:new Date().toISOString().replace(/\.\d+Z$/,"Z"),approved:"admin/notes/2026-11-19__signed-commits/notes.md"};
    fs.writeFileSync(f,JSON.stringify(j,null,1)+"\n");console.log("signing-setup: "+f+": "+id+" now carries git_signing")' "$ID" "$LINE"
fi
