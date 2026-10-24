#!/bin/sh
# Re-derive every piece of external data this evaluation uses, so that the
# copies in data/ can be checked rather than trusted.  Needs network access;
# run_all.sh does not.
set -e
cd "$(dirname "$0")"
mkdir -p data

echo "== ASTM G173-03 reference spectrum"
# NREL distributes the spectrum as an .xls workbook.  The pvlib project ships
# the same table as a CSV under a BSD licence, which is what data/ASTMG173.csv
# is a copy of; this re-extracts it from the published wheel and compares.
tmp=$(mktemp -d)
url=$(python3 -c "import json,urllib.request;d=json.load(urllib.request.urlopen('https://pypi.org/pypi/pvlib/json'));print([f['url'] for f in d['urls'] if f['filename'].endswith('.whl')][0])")
echo "   $url"
python3 -c "import sys,urllib.request;urllib.request.urlretrieve(sys.argv[1], sys.argv[2])" "$url" "$tmp/pvlib.whl"
python3 -c "
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
open(sys.argv[2], 'wb').write(z.read('pvlib/data/ASTMG173.csv'))
" "$tmp/pvlib.whl" "$tmp/ASTMG173.csv"
if cmp -s "$tmp/ASTMG173.csv" data/ASTMG173.csv; then
    echo "   data/ASTMG173.csv is byte-identical to the published table"
else
    echo "   DIFFERS from data/ASTMG173.csv:"
    cp "$tmp/ASTMG173.csv" data/ASTMG173.csv.new
    echo "   written to data/ASTMG173.csv.new"
fi
sha256sum data/ASTMG173.csv
rm -rf "$tmp"

echo
echo "== NIST Atomic Spectra Database, halogen ground-term splittings"
echo "   (the four values in constants.py HALOGEN_SOC)"
for sp in "F+I" "Cl+I" "Br+I" "I+I"; do
    printf '   %-6s ' "$sp"
    curl -s "https://physics.nist.gov/cgi-bin/ASD/energy1.pl?de=0&spectrum=${sp}&units=0&format=3&output=0&page_size=15&multiplet_ordered=0&conf_out=on&term_out=on&level_out=on&j_out=on&temp=&submit=Retrieve+Data" \
        | sed -n '3p' | tr -d '"'
done

echo
echo "== the preprint itself, for census.py"
curl -s "https://zenodo.org/api/records/23364732" -o data/record.json
python3 -c "
import json, sys, urllib.request
record = json.load(open('data/record.json'))
link = record['files'][0]['links']['self']
print('  ', link)
urllib.request.urlretrieve(link, 'data/hospv.pdf')
"
pdftotext -layout data/hospv.pdf data/hospv.txt
echo "   data/hospv.txt: $(wc -l < data/hospv.txt) lines"
