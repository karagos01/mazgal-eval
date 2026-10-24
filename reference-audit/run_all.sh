#!/bin/sh
# Reproduce every number in PAPER.md.  No network, no GPU, about 1 second.
#
# keywords.py prints recorded values unless a corpus directory is given.  To
# recompute the citation-marker counts from the deposits themselves:
#
#     ./fetch.sh corpus && python3 keywords.py corpus
set -e
for s in carrier.py audit.py hidden.py keywords.py; do
    printf '\n########## %s ##########\n\n' "$s"
    python3 "$s"
done
