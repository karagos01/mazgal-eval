#!/bin/sh
# Reproduce every number in PAPER.md.  Pure CPU, no GPU, no network, ~2 seconds.
set -e
for s in frequency.py light.py acoustics.py water.py; do
    printf '\n########## %s ##########\n\n' "$s"
    python3 "$s"
done
