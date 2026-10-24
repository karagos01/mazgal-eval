# Data

* `ASTMG173.csv` — the ASTM G173-03 reference solar spectra (extraterrestrial,
  global tilt, direct normal), 280–4000 nm, derived from SMARTS 2.9.2 and
  tabulated by NREL. This copy is the one distributed with the
  [pvlib](https://pvlib-python.readthedocs.io/) project under a BSD 3-clause
  licence. `constants.py` records its sha256 and `spectrum.py` refuses to run if
  it does not match; `fetch_data.sh` re-extracts it from the published pvlib
  wheel and compares byte for byte.

* `hospv.txt` — the text of the preprint under evaluation, extracted with
  `pdftotext -layout`. Not kept in the repository: run `./fetch_data.sh` to
  download the PDF from Zenodo and produce it. Only `census.py` reads it, and it
  says so if the file is missing. The census of one run is in `results.log`.
