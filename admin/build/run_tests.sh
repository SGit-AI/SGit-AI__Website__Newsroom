#!/usr/bin/env bash
# Runs the reader's browser and library tests (admin/build/test_*.mjs) in parallel, and fails if any fails.
#
#   bash admin/build/run_tests.sh [jobs] [log dir]      jobs defaults to 4, the logs to a temporary directory
#
# The tests are independent: each starts its own server on a port the system picks (listen(0)), and each launches
# its own browser, so they can run side by side. Run one at a time they took about six minutes; six at a time,
# under two (v0.13.7). A test that prints SKIP is a failure here, because it means Playwright or Chromium is missing.
#
# Two tests measure timing in the page and are run alone, after the rest: test_themes reads a page's contrast right
# after switching theme, and under load it read a page mid-switch; test_reading measures reading time.
#
# LEAVE_OUT names tests this run leaves out, by file name, separated by spaces (v0.13.48). CI uses it for test_wire,
# which reads the real vault server and runs in a job of its own that reports without stopping a release.
set -uo pipefail
cd "$(dirname "$0")/../.."
JOBS="${1:-4}"
LOGS="${2:-$(mktemp -d)}"
mkdir -p "$LOGS"
export LOGS
SERIAL="test_themes.mjs test_reading.mjs"
one='
  t="{}"; b=$(basename "$t"); s=$(date +%s)
  if timeout 900 node "$t" > "$LOGS/$b.log" 2>&1 && ! grep -q "^SKIP" "$LOGS/$b.log"; then
    echo "ok   $b ($(( $(date +%s) - s ))s)"
  else
    echo "FAIL $b ($(( $(date +%s) - s ))s), log: $LOGS/$b.log"; exit 1
  fi'
export one
rc=0
ls admin/build/test_*.mjs | grep -v -F -e test_themes.mjs -e test_reading.mjs $(for b in ${LEAVE_OUT:-}; do printf -- "-e %s " "$b"; done) | xargs -P "$JOBS" -I{} bash -c "$one" || rc=1
for b in $SERIAL; do case " ${LEAVE_OUT:-} " in *" $b "*) continue;; esac; t="admin/build/$b"; [ -f "$t" ] && { bash -c "${one//\{\}/$t}" || rc=1; }; done
if [ $rc -ne 0 ]; then
  for f in "$LOGS"/*.log; do grep -q "^SKIP\|FAIL\|Error" "$f" 2>/dev/null && { echo "== $(basename "$f")"; tail -20 "$f"; }; done
  echo "tests: at least one failed"; exit 1
fi
echo "tests: all passed"
