#!/usr/bin/env bash
S="${WRITER_TMP:?set WRITER_TMP to your scratchpad}"; cd /home/user/SGit-AI__Website__Newsroom || exit 1
die(){ echo "GATE STOP: $1"; exit 1; }
grep -q '^validate: OK' $S/rel.out || die validate
[ "$(grep -c '^FAIL test_' $S/rel.out)" = "$(grep -c '^FAIL test_reading.mjs' $S/rel.out)" ] || die tests
python3 admin/build/summaries.py --stamp | tail -1
python3 admin/build/summaries.py --check | grep -q '(0 stale)' || die stale; echo "0 stale"
python3 admin/build/summaries.py >/dev/null; for x in gen_sitemap search_index chrome gen_llms_full; do f=$(ls admin/build/$x.* | head -1); case $f in *.py) python3 $f >/dev/null;; *) NODE_PATH=$S/node/node_modules node $f >/dev/null;; esac; done
v=$(NODE_PATH=$S/node/node_modules node admin/build/validate.js | tail -1); echo "$v" | cut -c1-40; echo "$v" | grep -q "^validate: OK" || die validate2
w=$(NODE_PATH=$S/node/node_modules node admin/writer/tools/width.cjs $PWD/articles/$1.html); echo "width $w"; [ "$w" = 390 ] || die width
ln -sfn $S/node/node_modules node_modules; m=$(node admin/build/test_meter.mjs 2>&1 | tail -1); rm -f node_modules; echo "$m"; [ "$m" = "ALL METER CHECKS PASS" ] || die meter
git add -A
l=$(WRITER_KEYS="$S/media/newsroom-media.init.txt $S/demo/agentic-patterns.init.txt $S/console/agentic-console.init.txt" bash admin/writer/tools/leakscan.sh 2>&1); echo "$l" | grep -v '^WORDING' | tail -3; echo "$l" | tail -1 | grep -q "PASS$" || { echo "$l" | grep WORDING; die leakscan; }
python3 admin/build/wording.py --staged || die wording
git fetch -q origin dev; [ -z "$(git log --oneline HEAD..origin/dev)" ] || die "dev moved"
node admin/writer/tools/sign.cjs > $S/sig.txt || die sign
git commit -q -F - <<E || die commit
$2

$(cat $S/sig.txt)

Co-Authored-By: <the attribution line your session gives you>
Claude-Session: <your session URL>
E
for i in 1 2 3 4; do git push -q origin HEAD:dev && break; sleep $((2**i)); done; git status -sb | head -1; git status --short | wc -l
