#!/usr/bin/env bash
# vault-publish.sh <folder> <card-name> "<label>": make <folder> an sgit vault, commit, push, write the public card
# admin/content/vaults/<card-name>.json (vault id and public read key only), and verify with a read-only clone.
# The vault key goes to <folder>/../<card-name>.init.txt and is never printed. Keep that file out of every repository.
set -e
F=$(cd "$1" && pwd); N=$2; L=$3; REPO=$(git rev-parse --show-toplevel)
: "${SG_SEND_ACCESS_TOKEN:?the write token for the vault server}"
INIT="$(dirname "$F")/$N.init.txt"
( cd "$F" && sgit init --existing > "$INIT" 2>&1 && sgit commit "$L" > /dev/null 2>&1 || true
  sgit push --token "$SG_SEND_ACCESS_TOKEN" 2>&1 | sed "s/$SG_SEND_ACCESS_TOKEN/***/g" | tail -1 )
python3 - "$INIT" "$REPO/admin/content/vaults/$N.json" "$L" <<'PY'
import json, re, subprocess, sys
key = re.search(r'[Vv]ault key:?\s*(\S+:\S+)', open(sys.argv[1]).read()).group(1)
o = subprocess.run(['sgit', 'vault', 'derive-keys', key], capture_output=True, text=True).stdout
vid = re.search(r'vault_id\W+(\w+)', o).group(1); rk = re.search(r'read_key\W+([0-9a-f]{64})', o).group(1)
json.dump({"vault_id": vid, "read_key": "sgit_public_read_" + rk, "remote": "https://dev.send.sgraph.ai", "label": sys.argv[3]}, open(sys.argv[2], 'w'), indent=1)
print('vault id', vid)
PY
RK=$(python3 -c "import json,sys;d=json.load(open(sys.argv[1]));print(d['read_key']+':'+d['vault_id'])" "$REPO/admin/content/vaults/$N.json")
T=$(mktemp -d); ( cd "$T" && sgit clone "$RK" check > /dev/null 2>&1 ); diff -rq --exclude=.sg_vault "$F" "$T/check" && echo "verified: a read-only clone matches the folder"; rm -rf "$T"
