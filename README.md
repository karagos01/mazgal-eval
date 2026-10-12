# Quantum Biofortification / In-Situ Phytomining — independent evaluation

Reproducible evaluation of M. Mazgal, *Quantum Biofortification and In-Situ
Phytomining: Design of an Autonomous Closed-Loop Nanometallic Agricultural
Matrix* (Zenodo, 6 October 2026, DOI
[10.5281/zenodo.23174932](https://doi.org/10.5281/zenodo.23174932)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in
[`PAPER.cs.md`](PAPER.cs.md).

**One sentence of §4 states two densities that are 24 times apart.** At the
stated 30 cm plough depth, "1 pellet per 5 cm³" is 60 000 pellets/m², not the
2 500 the same sentence gives — and the mass budget, the 750-tonne requirement
and the $1 000 000 case study all rest on the 2 500, while the 5 cm³ is what the
"constant physical contact" requirement is based on. **§3.3 calls ¹³⁸La a stable
isotope**; it is a primordial radionuclide, half-life 1.03·10¹¹ years. The
premise of §3.3 fails for lanthanum before that matters, because **¹³⁹La —
99.91 % of all lanthanum — already has spin 7/2**, so there is nothing to select
for; and at natural isotopic composition the matrix raises the field's lanthanum
by **about a fifth** of what is already there while leaving the ¹³⁸La fraction
unchanged. The paper's own references invert three load-bearing claims: the
cited magnetic-isotope author measures **3–5× suppression** of DNA synthesis for
exactly the trio cited for acceleration and proposes them as a cytostatic.

Two findings go the other way, and §1 of the write-up sets them out first: the
30–50 % nitrogen-recovery premise is correct, and the added ¹³⁸La is four to five
orders of magnitude below the potassium-40 already in the soil, so calling it
stable is an error about the nuclide rather than a hazard in the proposal.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. Everything is arithmetic on the preprint's own parameters
and on published constants, because the deposit ships no code, no measurements
and no figures.

## Reproducing the results

```
./run_all.sh          # everything, about 1 second on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`density.py`](density.py) | the two densities of §4, which one the economics use, what honouring the other would cost, and what "constant physical contact" comes to | §§2, 4 |
| [`isotopes.py`](isotopes.py) | the spins the paper has right; ¹³⁸La's nuclear data; ¹³⁹La's spin; the added inventory against what the ploughed layer already holds; the enrichment alternative; the radiological comparison | §3.3 |
| [`economics.py`](economics.py) | the gold line against spot on the date of deposit, the return and its break-even discount rate, and how much leakage the "closed loop" can take | §4 |

Every constant is in [`constants.py`](constants.py) with a **provenance tag** —
`[P]` from the preprint, `[V]` verified against a named source, `[A]` an assumed
range that is swept rather than asserted — and no other script defines one.
Full output of one run: [`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| soil under 1 m² at the stated plough depth | — | 300 000 cm³ |
| "1 pellet per 5 cm³" | "approximately 2,500 pellets per 1 m²" | **60 000 pellets/m²** — the same sentence, **24× apart** |
| which figure the economics use | — | the 2 500, at exactly **1 g per pellet** |
| honouring the 5 cm³ instead | 750 t, $1 000 000 | **18 000 t, $24 000 000** |
| "constant physical contact" | required | mean spacing **4.93 cm**, root within 2.5 cm |
| ¹³⁸La | "stable isotope" (abstract, §3.3, keywords) | **primordial radionuclide**, T½ 1.03·10¹¹ y, β⁺ 65.5 % / β⁻ 34.5 % |
| ¹³⁸La nuclear spin | "I = 5" | **correct** |
| ¹³⁹La, 99.91 % of all lanthanum | — | spin **7/2** — non-zero, so nothing to select for |
| lanthanum added by 1 t La₂O₃ over 30 ha | "the most radical innovation" | 2.84 g/m² against **10.2–14.9 g/m² already present** → **+19 to +28 %** |
| ¹³⁸La fraction after the amendment | "precisely defined profile" | **unchanged at 0.0888 %** |
| ²⁵Mg already in the ploughed layer | — | **84–1260 g/m²** (10.00 % of all Mg) |
| ⁶⁷Zn already in the ploughed layer | — | 0.34–2.07 g/m² (4.10 % of all Zn) |
| feed needed for 1 t of enriched ¹³⁸La | not mentioned | **≈1 126 t** of natural lanthanum |
| added ¹³⁸La activity | — | 705 kBq total, **2.35 Bq/m²** |
| against soil potassium-40 | — | **4 to 5 orders of magnitude below** — not a hazard |
| gold line of the budget | $417 000 for 5 kg = $83.40/g | spot on the date of deposit **$134.03/g** → short by **$253 150** |
| simple payback | "permanent capital" | **40 years**; break-even only at ≤ **2.50 %/yr** in perpetuity |
| leakage the "closed loop" tolerates | assumed zero | **< 1.72 %/yr** to keep half the inventory to payback |
| 30–50 % nutrient uptake | claimed in §1 | **correct** for first-crop nitrogen recovery |
| Buchachenko, cited for accelerated DNA synthesis | "accelerate … DNA transcription" | **3–5× suppression**, proposed as an anti-cancer cytostatic |
| Reith et al., cited for gold blocking ROS | "entirely blocking" | gold **induces** oxidative stress; the cell exports it |
| Sheoran et al., cited for delivering metal | delivery into biomass | phytomining **removes** metal and smelts it |
| references resolving as printed | 6 given | **4 of 6**; Reith is 2009 PNAS 106(42) and Buchachenko's title is *Biochemistry* |

## Scope

The deposit is a four-page preprint under CC BY 4.0 with no code, no
measurements and no figures, so there is nothing to benchmark. §8 of the
write-up sets out the claims arithmetic cannot reach — "absolute structural
immunity", "entirely blocking cellular corrosion", "the theoretical blockade of
natural biological aging processes" — and says why they are not measured rather
than treating them as defects.

All six references were read for content in
[`reference-audit`](https://github.com/karagos01/reference-audit), which holds
the verbatim evidence and records how far each work could be read; the verdicts
are summarised in §6 here and not duplicated.

§9 sets out the limits. The `[A]` tags in `constants.py` mark values that could
not be checked against a primary source here and are therefore swept, with every
conclusion drawn from them computed across the whole range — two constants used
in an earlier draft were demoted to `[A]` on that basis. The spacing figures
assume a cubic lattice, which is a best case.

## Companion evaluations

- [`reference-audit`](https://github.com/karagos01/reference-audit) — whether all 69 citations in all 16 deposits say what they are cited for
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL tensor matrix architecture of October 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
