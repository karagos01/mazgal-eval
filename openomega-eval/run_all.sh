#!/bin/sh
# Reproduce every number in PAPER.md.  Pure CPU, no GPU, no network, ~20 seconds.
set -e
for s in dimensions.py zerodivisors.py hardware.py; do
    printf '\n########## %s ##########\n\n' "$s"
    python3 "$s"
done
