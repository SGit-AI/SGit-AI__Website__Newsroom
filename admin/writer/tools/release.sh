#!/usr/bin/env bash
# Build, validate and test a release locally, before committing. Run from anywhere; takes 25 to 40 minutes.
# Needs: WRITER_SITE (a read-only clone of SGit-AI/SGit-AI__Website), WRITER_NODE (a node_modules with sharp,
# playwright and jsqr), WRITER_TMP (scratch space, a few GB). Prints "fails=0" when everything passed.
set -e
: "${WRITER_SITE:?set WRITER_SITE to a read-only clone of SGit-AI/SGit-AI__Website}"
: "${WRITER_NODE:?set WRITER_NODE to a node_modules folder with sharp, playwright and jsqr}"
: "${WRITER_TMP:?set WRITER_TMP to a scratch folder}"
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
export TMPDIR="$WRITER_TMP" PLAYWRIGHT_BROWSERS_PATH="${PLAYWRIGHT_BROWSERS_PATH:-/opt/pw-browsers}"
rm -rf "$WRITER_TMP"/newsroom-publish-*
python3 admin/build/publish.py --from "$WRITER_SITE" --node-modules "$WRITER_NODE"
for n in find front desks sections publishers briefs deps ids hubs agents personas lists passkey_lab wire api_map archive engineering mesa_ranch_vault northstar_twin thistlewood_twin pellbridge_agents no_server_studio research_vault sgit_ruflo_video drafts page_fixes reviews series summaries gen_sitemap search_index chrome gen_sitemap gen_llms_full; do
  if [ -f admin/build/$n.py ]; then python3 admin/build/$n.py; else python3 admin/build/build_$n.py; fi
done
node admin/build/validate.js
trap 'rm -f node_modules' EXIT INT TERM HUP
ln -sfn "$WRITER_NODE" node_modules
fails=0
bash admin/build/run_tests.sh 6 "$WRITER_TMP/testlogs" > "$WRITER_TMP/tests.out" 2>&1 || { grep '^FAIL' "$WRITER_TMP/tests.out"; fails=1; }
tail -1 "$WRITER_TMP/tests.out"
echo fails=$fails
