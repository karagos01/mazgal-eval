# openOmega — independent evaluation

Reproducible evaluation of M. Mazgal, *openOmega: Tensor Matrix Architecture for
Matter-Antimatter Symmetry in ±12D, ±112D, and ±224D Spaces* (Zenodo, 9 October
2026, DOI
[10.5281/zenodo.23263528](https://doi.org/10.5281/zenodo.23263528)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**The algebra is right, and this repository confirms it from first principles.**
The Cayley-Dickson tower is built here from the reals; the construction
reproduces the textbook classification exactly — ℍ associative, 𝕆 non-associative
but alternative, the sedenions neither — and norm multiplicativity holds to
dimension 8 and fails at 16, which is precisely why zero divisors appear there.
A sedenion zero divisor is then found by search: **(e₁ + e₁₀) × (e₄ − e₁₅) = 0**,
exactly. Moreno (1998), reference [3], is the correct source and is correctly
attached — alongside Furey in SOTP, the best-chosen citation in the author's
seventeen deposits.

**But the engine does not need the sedenions for the property it wants.** §3's
own equation is about *matrices*, and zero divisors are ordinary in every matrix
algebra over a field: [[1,0],[0,0]]·[[0,0],[0,1]] = 0 is the smallest case, and
**200 of 200** randomly constructed non-zero 224×224 real pairs multiply to zero
here. **And the product cannot carry the energy away** — ‖A‖ = 34.1,
‖B‖ = 221.9, ‖A·B‖ = **4.1·10⁻¹³**. To emit E = mc² the engine must read both
magnitudes before the multiply and then test the register against zero, which is
the `if (collision)` §3 says is unnecessary: the branch is moved, not removed.

**224 is not in the Cayley-Dickson tower** (it is the powers of two; sedenions
are 16-dimensional), **one 224×224 product is 269 cycles of the entire GPU** and
not one, and **the roofline result survives the doubling** — matrix form and
encoded state have identical arithmetic intensity at every layer while the
matrix costs d× the traffic.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. The algebra is built from scratch; the hardware figures are
catalogue specifications of the RTX 3090 the preprint's own series names.

## Reproducing the results

```
./run_all.sh          # everything, about 20 seconds on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`dimensions.py`](dimensions.py) | whether 224 is in the Cayley-Dickson tower; the multiple-of-16 claim, tiles and occupancy; "negative dimensions" as a cardinality; the critical dimensions the cited physics uses | §4 |
| [`zerodivisors.py`](zerodivisors.py) | the Cayley-Dickson tower built from the reals and checked against the textbook classification; a sedenion zero divisor found by search; zero divisors in matrix algebras; whether the product conserves energy; the associativity the architecture needs | §§1–3, 6 |
| [`hardware.py`](hardware.py) | the "single clock cycle" claim; node footprint and resident nodes; the step rate for a fixed grid; the roofline; what the doubling costs relative to openQL | §5 |

Every value is in [`constants.py`](constants.py) with a **provenance tag** —
`[P]` from the preprint, `[V]` verified against a named source, `[A]` an assumed
value or a choice of presentation — and no other script defines one. Full output
of one run: [`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| sedenions have zero divisors | "so-called zero divisors emerge" | **correct** — 168 pairs found among e_i ± e_j |
| the first one found | — | **(e₁ + e₁₀) × (e₄ − e₁₅) = 0**, exactly |
| why they appear at 16 and not below | — | norm multiplicativity exact to dim 8, **1.1·10⁻²** at 16 |
| the construction's own check | — | ℍ associative, 𝕆 alternative, sedenions neither — textbook classification reproduced |
| reference [3], Moreno 1998 | cited for the zero divisors | **apt and correctly attached** |
| are zero divisors exotic? | "This 'anomaly'" | no — **200 of 200** non-zero 224×224 real pairs with A·B = 0 |
| smallest example of the same property | — | [[1,0],[0,0]] · [[0,0],[0,1]] = 0 |
| does the product carry the energy? | "release of an absolute tensor vector into the energy register" | ‖A‖ = 34.1, ‖B‖ = 221.9, **‖A·B‖ = 4.1·10⁻¹³** |
| is the branch removed? | "requires no conditional script like `if (collision)`" | no — testing the register against zero **is** that branch |
| 224 in the Cayley-Dickson tower | "By introducing the Cayley-Dickson construction" | **no** — the tower is 1, 2, 4, 8, 16, 32, … |
| dimension of the sedenions | "the mathematical foundation of the −224D space" | **16** |
| where 224 does come from | "dimensional doubling" | 2 × 112, and 112 has no surviving derivation in the series |
| 224 / 16 | "a perfect multiple of 16 (224 ÷ 16 = 14)" | **correct**, 14 exactly, 100 % tile occupancy |
| 112 / 16 | — | 7 exactly too — the alignment is **inherited**, not gained |
| MMA operations per 224D node | "a single processor clock cycle" | **196 tiles** |
| cycles for one 224×224 product | "a single processor clock cycle" | **269.1 cycles of the entire GPU** |
| the same at 112D | openQL made the identical claim | 33.6 — so 224 is **8× worse** |
| ±224D node with its mirror | — | **196.0 KiB**; 128 397 pairs fit in 24 GiB, a 50-node cube |
| against §5's tokamak, 1 mm³ at 10²⁰ m⁻³ | "exact plasma behavior" | short by **778 834×** (5.9 orders) |
| a million-node grid at ±224D | — | 186.9 GiB — **does not fit on the card** |
| largest grid that does fit, sweep rate | — | **18.2 Hz**; real time is 60 |
| matrix form vs the state it encodes | "natively processed by Tensor Cores" | identical FLOP/byte at every layer: 6.0, 56.0, **112.0** |
| cost of the step from openQL | presented as costless | **4×** memory, **8×** arithmetic, **4×** tiles, then the mirror doubles memory again |
| "negative dimensions" | ±12D, ±112D, ±224D | dimension is a cardinality; the largest layer is a **448**-dimensional state |
| 224 vs the critical dimensions | "contains complete string theory" | superstring 10, bosonic 26, M-theory 11 — **none is 224** |
| what the architecture needs vs what the mechanism needs | asserted in consecutive sections | WMMA is **associative**; the sedenions are not even alternative |
| hypercomplex vocabulary | — | returns after six deposits: octonion 1, **sedenion 5**; "causal" still 0 |
| "Theory of Everything" | in the abstract | first occurrence in the series |

## Scope

The deposit is a short preprint under CC BY 4.0 with no code, no measurements
and no figures. §7 of the write-up sets out what is not measured — the Theory of
Everything claim, the phase-conjugate radar, the sonoluminescence and dark-matter
applications — and says why, rather than treating them as defects.

§8 sets out the limits. The Cayley-Dickson construction uses one of several sign
conventions; a different one permutes which particular pairs are zero divisors
but not the dimension at which they appear, which is why the classification
table is included as the check. An earlier draft of this repository had a wrong
formula for the second component, and that table caught it by making the
quaternions non-associative. An earlier draft also had a degenerate step-rate
table, filled to card capacity, where every layer returned the same number by
construction; it is now computed over a fixed grid instead.

The openQL measurements referred to throughout are not reproduced here; they
live in [`openql-eval`](../openql-eval), and the
reference verdicts in
[`reference-audit`](../reference-audit).

## Companion evaluations

- [`openql-eval`](../openql-eval) — the openQL / openOL original this deposit extends
- [`intensional-physics-eval`](../intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026
- [`reference-audit`](../reference-audit) — whether all 81 citations in all 18 deposits say what they are cited for
- [`phytomining-eval`](../phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026
- [`naion-hfrs-eval`](../naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`hemocyanin-eval`](../hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`octonion-mppt-eval`](../octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](../xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](../causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`cymatic-eval`](../cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`hospv-eval`](../hospv-eval) — the HOS-PV 2.0 singlet-fission and spintronic photovoltaic proposal of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
