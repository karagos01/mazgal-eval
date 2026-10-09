#!/bin/sh
# Download all 16 Zenodo records by this author and convert them to text.
#
# This is the one script here that needs the network.  Nothing is cached in the
# repository: the deposits are the author's work, CC BY 4.0, and are left where
# he published them.  Rerunning this reproduces the inputs to keywords.py
# against whatever is on Zenodo at the time.
#
# Requirements: curl, pdftotext (poppler-utils), python3.
#
#   ./fetch.sh [output-directory]      default: ./corpus
set -e

OUT="${1:-corpus}"
mkdir -p "$OUT"
echo "corpus directory: $OUT"

# record id : short name                 (oldest first; openQL and MPPT have
#                                          two versions each)
RECORDS="
22876757:acoustic-projector
22877345:x-ternary
22877912:mppt-v1.0
22914238:mppt-v1.1
22923154:cobar
22934058:momentum-drive
22959886:cqft
22962188:pctp
22962557:sotp
23112560:openql-v1.0
23156927:cymatic
23174932:phytomining
23186884:na-ion-hfrs
23209266:hemocyanin
23241148:openql-v1.1
23241777:intensional-physics
"

for rec in $RECORDS; do
    id=${rec%%:*}; name=${rec##*:}
    if [ -f "$OUT/$name.txt" ]; then
        echo "  have    $name"
        continue
    fi
    echo "  fetch   $name  (zenodo $id)"
    url=$(curl -sS "https://zenodo.org/api/records/$id" \
          | python3 -c 'import json,sys; print(json.load(sys.stdin)["files"][0]["links"]["self"])')
    curl -sS -L "$url" -o "$OUT/$name.pdf"
    pdftotext -layout "$OUT/$name.pdf" "$OUT/$name.txt"
done

echo
echo "done.  now run:  python3 keywords.py $OUT"
