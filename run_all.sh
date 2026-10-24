#!/bin/sh
# Run every evaluation in sequence, in the order of the deposits they cover.
# About 25 minutes in total, almost all of it octonion-mppt-eval.
#
# One subdirectory is not pure CPU: xternary-eval needs a CUDA GPU for
# everything but bits.py.  A failure there does not stop the sweep; the summary
# at the end says what failed.
#
#   ./run_all.sh              everything
#   ./run_all.sh fast         skip octonion-mppt-eval (the 20-minute search)
#   ./run_all.sh openql-eval openomega-eval     only these

set -u

ALL='octonion-mppt-eval xternary-eval causal-trilogy-eval openql-eval
     cymatic-eval naion-hfrs-eval phytomining-eval hemocyanin-eval
     intensional-physics-eval openomega-eval hospv-eval reference-audit'

case "${1:-}" in
    '')     targets=$ALL ;;
    fast)   targets=$(echo "$ALL" | tr ' ' '\n' | grep -v '^octonion-mppt-eval$') ;;
    *)      targets="$*" ;;
esac

root=$(cd "$(dirname "$0")" && pwd)
failed=''
ok=''

for d in $targets; do
    [ -x "$root/$d/run_all.sh" ] || { echo "no such evaluation: $d" >&2; failed="$failed $d"; continue; }
    printf '\n################################################################\n'
    printf '##  %s\n' "$d"
    printf '################################################################\n\n'
    if (cd "$root/$d" && ./run_all.sh); then ok="$ok $d"; else failed="$failed $d"; fi
done

printf '\n################################################################\n'
printf '##  summary\n'
printf '################################################################\n'
for d in $ok;     do printf '  ok      %s\n' "$d"; done
for d in $failed; do printf '  FAILED  %s\n' "$d"; done
[ -z "$failed" ] || exit 1
