#!/bin/sh
# Everything in this repository, in order.  No GPU, no network, about ten seconds.
# External data: data/ASTMG173.csv is shipped and checked against the sha256 in
# constants.py; data/hospv.txt is produced by ./fetch_data.sh and only census.py
# needs it.
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}

echo "### provenance of the constants"
$PY constants.py
echo
echo "### the reference spectrum, and the loss census of section 1"
$PY spectrum.py
echo
echo "### section 6.2: the photocurrent integral"
$PY photocurrent.py
echo
echo "### the 45.9% limit, against the model it is cited from"
$PY detailed_balance.py
echo
echo "### sections 3 and 4: CISS and the Pauli spin blockade"
$PY spin.py
echo
echo "### sections 2.2 and 5, and table 1: the materials"
$PY materials.py
echo
echo "### the vocabulary of the series, in this deposit"
$PY census.py
echo
echo "### the preprint against itself: the same quantity twice"
$PY consistency.py
