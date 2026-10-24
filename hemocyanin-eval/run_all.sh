#!/bin/sh
# Reproduce every number in PAPER.md.  Pure CPU, no GPU, no network, ~1 second.
set -e
for s in oxygen.py genetics.py; do
    printf '\n########## %s ##########\n\n' "$s"
    python3 "$s"
done
