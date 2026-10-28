#!/usr/bin/env bash
# Leak scan for the staged diff of the repository you run it in. Run after `git add -A`, before committing.
# Reads private inputs from files that never live in a repository:
#   ~/.claude/abp/deny-names.txt   one case-insensitive pattern per line (see private/deny-list.md)
#   ~/.claude/abp/secrets.txt      one secret per line (tokens, passphrases), at least 8 characters
#   admin/local/demo-keys/         the local key tier, if this machine has it (*-vault-key, *-derive.log)
#   $WRITER_KEYS                   a glob of sgit init outputs (*.init.txt) whose vault keys must never appear
# Exit 0 and PASS, or exit 1 and the reason. Never prints a secret.
cd "$(git rev-parse --show-toplevel)" || exit 2
K=admin/local/demo-keys; fail=0
D=$(mktemp); git diff --cached -U0 -- . ':(exclude)admin/writer/tools/leakscan.sh' | grep '^+' | grep -v '^+++' > "$D"
p=$(git diff --cached --name-only | grep -E "demo-keys|admin/local|node_modules|\.sg_vault"); [ -n "$p" ] && { echo "FAIL paths: $p"; fail=1; }
n=$(grep -cE '\b[a-z0-9]{24}:[a-z0-9]{4,24}\b|sgit_private_[a-z]+_[A-Za-z0-9]|sgit_vk1_[A-Za-z0-9]|PRIVATE KEY|GOCSPX-|AKIA[0-9A-Z]{16}' "$D"); [ "$n" != 0 ] && { echo "FAIL secret regex: $n lines"; fail=1; }
keys=0
if [ -d $K ]; then
  for f in $K/*-vault-key; do [ -f "$f" ] || continue; while IFS= read -r line || [ -n "$line" ]; do [ -z "$line" ] && continue; keys=$((keys+1)); body=$(echo "$line" | sed -E 's/^sgit_private_vault_//; s/:[a-z0-9]+$//'); [ ${#body} -ge 12 ] && grep -qF -- "$body" "$D" && { echo "FAIL vault key body: $f"; fail=1; }; done < "$f"; done
  for f in $K/*-derive.log; do [ -f "$f" ] || continue; while read -r k v || [ -n "$k" ]; do case "$k" in write_key:|passphrase:) [ ${#v} -ge 12 ] && grep -qF -- "$v" "$D" && { echo "FAIL $k $f"; fail=1; };; esac; done < "$f"; done
fi
if [ -n "$WRITER_KEYS" ]; then for f in $WRITER_KEYS; do [ -f "$f" ] || continue; for k in $(grep -oE '[Vv]ault key:?[[:space:]]*[^[:space:]]+:[^[:space:]]+' "$f" | sed -E 's/^[Vv]ault key:?[[:space:]]*//'); do keys=$((keys+1)); for part in "$k" "${k%%:*}"; do [ ${#part} -ge 12 ] && grep -qF -- "$part" "$D" && { echo "FAIL vault key from $f"; fail=1; }; done; done; done; fi
[ -f ~/.claude/abp/secrets.txt ] && while IFS= read -r sec || [ -n "$sec" ]; do [ ${#sec} -ge 8 ] && grep -qF -- "$sec" "$D" && { echo "FAIL a secret from secrets.txt"; fail=1; }; done < ~/.claude/abp/secrets.txt
[ -n "$SG_SEND_ACCESS_TOKEN" ] && grep -qF "$SG_SEND_ACCESS_TOKEN" "$D" && { echo "FAIL access token"; fail=1; }
if [ -f ~/.claude/abp/deny-names.txt ]; then
  pat=$(grep -v '^\s*$' ~/.claude/abp/deny-names.txt | paste -sd'|' -)
  # A name fails only where the staged file holds more of it than the published (HEAD) file did:
  # regenerated indexes re-emit lines that were already public (13 Oct: a summit speaker who shares
  # a first name with someone on the list, confirmed a different person by the owner).
  if [ -n "$pat" ] && grep -qiE "\b($pat)\b" "$D"; then
    while IFS= read -r f; do
      new=$(git show ":$f" 2>/dev/null | grep -aoiE "\b($pat)\b" | wc -l)
      old=$(git show "HEAD:$f" 2>/dev/null | grep -aoiE "\b($pat)\b" | wc -l)
      [ "$new" -gt "$old" ] && { echo "FAIL names: $f adds $((new-old)) ($(git show ":$f" | grep -aoiE "\b($pat)\b" | sort -u | tr '\n' ' '))"; fail=1; }
    done < <(git diff --cached --name-only --diff-filter=AM)
    [ $fail = 0 ] && echo "note: names on the list appear in re-emitted lines only, no file gains one"
  fi
else echo "WARN no ~/.claude/abp/deny-names.txt: names not checked"; fi
grep -n 'claude-[a-z]*-[0-9]' "$D" | grep -v 'agent@riskmandate.ai' | grep -q . && { echo "FAIL model id outside the byline"; fail=1; }
em=$(git diff --cached -U0 -- admin/content | grep '^+' | grep -c $'\xe2\x80\x94'); [ "$em" != 0 ] && { echo "FAIL em-dash in admin/content: $em"; fail=1; }
[ -f admin/build/wording.py ] && { python3 admin/build/wording.py --staged || { echo "FAIL wording: superlative self-claim or overstatement added (fix it, or list a reviewed phrase in admin/build/wording-allow.txt)"; fail=1; }; }
echo "leak scan: $(wc -l < "$D") added lines; vault key lines checked: $keys$([ -d $K ] || echo ' (no local key tier on this machine)'); $([ $fail = 0 ] && echo PASS || echo FAIL)"
rm -f "$D"; exit $fail
