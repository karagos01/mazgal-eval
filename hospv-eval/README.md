# HOS-PV 2.0 — independent evaluation

Reproducible evaluation of M. Mazgal, *HOS-PV 2.0: Exceeding the
Shockley-Queisser Limit via Chiral-Induced Spin Selectivity, Dexter-Sensitized
Singlet Fission, and Altermagnetic Carrier Extraction* (Zenodo, 14 October 2026,
DOI [10.5281/zenodo.23364732](https://doi.org/10.5281/zenodo.23364732)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**The mechanism is sound and the limit really does move, and this repository
confirms it from first principles.** A detailed-balance model is built here from
the ASTM G173-03 spectrum and the Planck law, and before being applied it
reproduces three published values: the Shockley-Queisser limit (**33.77 %** at
1.335 eV against 33.7 % at 1.34 eV), the carrier-multiplication limit of the
preprint's own reference [5] (**44.62 %** against 44.4 %), and the same group's
value for multiplication capped at two carriers per photon, which is what
singlet fission does (**42.09 %** at 0.94 eV against 42.0 % at 0.95 eV). The same
code then puts the architecture at **41.24 %**, which beats Shockley-Queisser by
**7.5 points**. Exceeding the limit is not what is wrong here.

**But 45.9 % is the two-gap tandem row of the paper it is cited from.** The best
this family of models can do at *any* pair of energies is 42.09 %, so no donor
or acceptor reaches 45.9 %. Reference [5]'s abstract gives 33.7 % for a single
gap without multiplication, **44.4 % for a single gap with it**, and
**45.7 %–47.7 % for an ideal two-gap tandem** — and 45.9 % falls in the tandem
range. Being a single junction is the architecture's entire selling point.

**And the high-energy channel is over the ceiling of its own mechanism.**
Photons above 2.25 eV carry only **9.76 mA/cm²** of charge at one electron each,
so the claimed 23.8 mA/cm² needs **2.44 electrons per absorbed photon**; singlet
fission gives at most two. With the preprint's own quantum efficiencies the
measured J_sc is **43.83 mA/cm²**, not 52.3, and the PCE **29.8 %**, not 35.6 %.
There is a coincidence in that number worth the whole exercise: a plain 1.12 eV
absorber with EQE = 1 and no fission at all collects **43.81 mA/cm²** — the same
figure to 0.1 %. The multiplication pays for the 0.85, the 0.92 and the 0.90 and
nothing more, and the architecture's real gain is that it collects silicon's
current at silicon's voltage while absorbing those losses.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. `data/ASTMG173.csv` is shipped and is checked against the
sha256 recorded in `constants.py` before any script uses it;
[`fetch_data.sh`](fetch_data.sh) re-derives it from the published pvlib wheel and
compares it byte for byte, re-queries the four NIST atomic levels, and extracts
the preprint's text for `census.py`.

## Reproducing the results

```
./run_all.sh          # everything, about ten seconds on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`spectrum.py`](spectrum.py) | the spectrum, its integral, the two photon thresholds, and the thermalisation/sub-bandgap census the introduction quotes | §1 |
| [`photocurrent.py`](photocurrent.py) | both channels of the J_sc integral against the preprint's own efficiencies; the ceiling of each; where the published number could come from; the efficiency recomputed; whether 220 nm can absorb both bands | §6.2 |
| [`detailed_balance.py`](detailed_balance.py) | the detailed-balance model, three self-checks, the architecture's own limit, the 45.9 % claim, V_oc, the implied electroluminescence yield and the fill-factor ceiling | §§2.2, 6.2 |
| [`spin.py`](spin.py) | the suppression formula, η_PB against its own times, the mobility sweep, the spin-statistical baseline, what tanh(ΔE/2kT) commits to, and the Z⁴ exponent measured against NIST data | §§3, 4 |
| [`materials.py`](materials.py) | the fission energy window against measured chromophores, the altermagnet's Néel temperature against the module's operating temperature, the specific power of table 1's stack, and the series-resistance budget | §§2.2, 5, table 1 |
| [`census.py`](census.py) | the vocabulary of the series, in this deposit | form |
| [`consistency.py`](consistency.py) | the quantities the preprint gives two values for, each recomputed from its own numbers, and the arithmetic steps that come out right | §§2, 4, 6.2, tables 1 and 2 |

Every value is in [`constants.py`](constants.py) with a **provenance tag** —
`[P]` from the preprint, `[V]` verified against a named source, `[A]` assumed and
swept — and no other script defines one. Full output of one run:
[`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| Shockley-Queisser limit, as a self-check | 33.7 % at 1.34 eV | **33.77 % at 1.335 eV** |
| reference [5]'s single-gap limit, as a self-check | 44.4 % at 0.70 eV | **44.62 %** |
| the same for doubling only, as a self-check | 42.0 % at 0.95 eV | **42.09 % at 0.94 eV** |
| this architecture at its own two energies | — | **41.24 %**, beating SQ by 7.5 points |
| the claimed limit | "45.9 %" | **above the 42.09 % ceiling of the model** |
| where 45.9 % is in reference [5] | cited as single-junction | the **two-gap tandem** range, 45.7–47.7 % |
| EQE_high = 1.85 × 0.92 × 0.90 | "153 %" | **1.5318, correct** |
| IR channel, 1.12–2.25 eV, at EQE 0.85 | 28.5 mA/cm² | **28.89, right to 1.3 %** |
| photons above 2.25 eV, one electron each | — | **9.76 mA/cm²** |
| SF channel, above 2.25 eV | 23.8 mA/cm² | **14.95** — the claim needs **2.44 e⁻/photon** |
| the threshold that would yield 23.8 | "above E(S₁) = 2.25 eV" | **1.96 eV / 634 nm**, a 294 meV shift |
| total J_sc | 52.3 mA/cm² | **43.83** |
| PCE | "35.58 %" | **29.82 %**; the arithmetic itself is consistent |
| plain 1.12 eV absorber, EQE = 1, no fission | — | **43.81 mA/cm²** — the cascade returns the same to 0.1 % |
| radiative-limit V_oc at 1.12 eV | "0.90 V" | **0.8834 V** with the doubling |
| ΔV_oc,nr from 0.22 V to 0.09 V | claimed | **×158 in electroluminescence yield**, 0.02 % → 3 % |
| fill factor | 84.0 % | ideal-diode ceiling **86.2 %** — reachable as stated |
| fraction of its own radiative limit | — | **86.3 %**, against 92.9 % for c-Si and 59.3 % for OPV today |
| β_eff = β_L(1 − η_PB P²) at 0.85, 0.95 | "0.314, 68.6 % suppression" | **correct as written** |
| η_PB from the τ values of the same sentence | "0.95" | **0.984–0.996**, so 72.0 % — in the preprint's favour |
| suppression over the mobility range | 68.6 % | **39.5 % to 71.8 %**; 20–80 ns needs µ = 3.8e-3 to 1.5e-2 cm²/Vs |
| the achiral spin-statistical baseline | — | **0.250 β_L**, below the chiral 0.314 β_L |
| splitting that P_CISS = 0.85 at 300 K implies | — | **64.5 meV**, and the suppression then falls to 57.3 % at 85 °C |
| ξ_SOC ∝ Z⁴ | asserted | **exponent 1.69** measured on the NIST halogen splittings |
| E(S₁) ≥ 2E(T₁) with the preprint's own 2.25 and 1.15 | "must satisfy" | **fails by 50 meV**; the fission is endothermic by 1.9 kT |
| chromophores satisfying E(T₁) ≥ 1.12 and E(S₁) ≥ 2E(T₁) | TIPS-tetracene, DPP | pentacene, tetracene and rubrene each fail one; **rubrene misses by 70 meV** |
| spin splitting of the altermagnetic collector | "~0.8 eV" | **0.37–0.80 eV measured for MnTe: correct** |
| MnTe Néel temperature against module temperature | not stated | **267–307 K** against 318–332 K in the field |
| specific power of table 1's stack | "≥ 10,000 W/kg" | **2944 W/kg**, 2815–3087 across the sweep: short by **3.4×** |
| mass that does no physics | — | **97.7 %** — 75 µm of polymer; 19 µm would be needed |
| R_s budget for one FF point at 52.3 mA/cm² | — | **0.155 Ω·cm²**, 22 % tighter than silicon's |
| the vocabulary of the other seventeen deposits | — | **zero occurrences**: no tensor, no hypercomplex, no causal, no GPU |
| ORCID placeholder, self-citations, AI co-author | — | **none** — the first deposit of the eighteen with all three |
| quantities given two values by the preprint itself | — | **8**, the widest a factor **12.4**, two of them in its favour |
| arithmetic steps it performs correctly | — | **8 of 8** — the algebra never fails, only the numbers put into it |

## Scope

The deposit is a short preprint under CC BY 4.0 with no code, no measurements and
no figures. §8 of the write-up sets out what is not measured here — the Dexter
morphology, whether a bulk chiral interface escapes the objection §3.1 raises
against electrode spin filters, spin conservation in the infrared channel, the
missing Thomas factor of two in §3.2's Hamiltonian, and the tunnel barrier
beyond its resistance budget — and says why, rather than treating them as
defects.

§9 sets out the limits. The detailed-balance model gives ceilings, which
strengthens the finding that a claim sits above one and weakens nothing in the
reproduction of three published values. It also records three errors found in
this evaluation: a divergent Bose factor that returned 7 × 10¹² % until the
self-check table caught it, an areal-mass unit wrong by 10³, and a reference
count that counted every numbered list in the body.

Measurements of the earlier deposits referred to here are not reproduced; the
reference verdicts live in
[`reference-audit`](../reference-audit).

## Companion evaluations

- [`reference-audit`](../reference-audit) — whether all 81 citations in all 18 deposits say what they are cited for
- [`openomega-eval`](../openomega-eval) — the openOmega matter-antimatter and sedenion proposal of October 2026
- [`intensional-physics-eval`](../intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026
- [`openql-eval`](../openql-eval) — the openQL / openOL tensor-matrix architecture
- [`phytomining-eval`](../phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026
- [`naion-hfrs-eval`](../naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`hemocyanin-eval`](../hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`cymatic-eval`](../cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`octonion-mppt-eval`](../octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](../xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](../causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026

## Licence

Code (all `*.py`, `run_all.sh` and `fetch_data.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
`data/ASTMG173.csv` is NREL's tabulation of ASTM G173-03 as distributed with
pvlib (BSD 3-clause); see [`data/README.md`](data/README.md).
