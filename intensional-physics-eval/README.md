# Intensional Physics Computing + openQL v1.1 — independent evaluation

Reproducible evaluation of the two deposits of 8 October 2026:
M. Mazgal, *Intensional Physics Computing: Generating Virtual Reality via
Multidimensional Tensor Core Queries* (DOI
[10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777)) and
*openQL / openOL … (Version 1.1)* (DOI
[10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148)), a revision
of the 3 October original. They are evaluated together because neither stands
alone.

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**Half of the central new claim is correct, which is worth leading with.** IPC
§5 claims "millions of physical queries per millisecond" — 10⁹/s. For the 4×4
node of §3 the binding ceiling on the card the author's own preprints specify is
**1.46·10¹⁰/s**, so it fits with **14.6× of headroom** — the first numeric
hardware claim in this series the arithmetic supports. For the 112×112 node of
the same sentence the ceiling is 1.87·10⁷/s, so it is off by **54×**.

**But the rate is insufficient for its own application.** §4 makes every ray
march step a query, so the budget is per pixel per frame: 10⁹/s buys **8.0 steps
per pixel** at 1080p60, against the 64–256 volumetric ray marching needs —
**4 to 32× short**, before any step does physics.

**openQL v1.1 removes four claims this evaluation measured**, along with all
five reference glosses and the keyword "octonions" — while the abstract still
transforms "quaternion and octonion algebra into unified block matrices". The
coincidence is recorded; no causal claim is made, because the revision has no
changelog. Its one new section, §6.1, claims "millions of topologies per day" on
a million-node grid, which leaves **14–140 update sweeps** per candidate for a
coupled multi-physics objective.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. Hardware figures are the catalogue specifications of the
RTX 3090 the preprints themselves name.

## Reproducing the results

```
./run_all.sh          # everything, about 1 second on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`queries.py`](queries.py) | the claimed query rate against compute and bandwidth ceilings for both node sizes; tile occupancy; the ray-marching budget; what NeRF cost; the symplectic wording | §§2–3 |
| [`bldc.py`](bldc.py) | what one topology evaluation costs, how many sweeps "millions per day" leaves, what zero-branching actually buys, and the skin-effect claim | §4 |
| [`versions.py`](versions.py) | the v1.0 → v1.1 diff, what was removed and added, and what stayed | §5 |

`versions.py` is a record rather than a computation, kept as a script so the
list appears in `results.log` beside the arithmetic. Every value is in
[`constants.py`](constants.py) with a **provenance tag** — `[P]` from the
preprints, `[V]` verified against a named source, `[A]` an assumed range that is
swept. Full output of one run: [`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| claimed query rate | "millions of physical queries per millisecond" | 10⁹/s |
| 4×4 node, binding ceiling | — | **1.46·10¹⁰/s — the claim fits, 14.6×** |
| 112×112 node, binding ceiling | same sentence | 1.87·10⁷/s — **off by 54×** |
| what binds in both cases | "natively processed by Tensor Cores" | memory bandwidth, not compute |
| 4×4 node in a 16×16 tensor-core tile | one node per MMA | **6.2 % occupancy** |
| 112×112 in the same tile | — | 100 % — 112 = 7 × 16 exactly |
| march steps the claimed rate buys at 1080p60 | "absolute real-time" | **8.0 per pixel** |
| what volumetric ray marching needs | — | 64–256 → the rate is **4–32× short** |
| NeRF, cited as the predecessor | "theoretical predecessor" | 150–200 M queries/image, **30 s/frame** |
| σ(W·S + b) in IPC §3 | "a **symplectic** discrete Hamiltonian operator" | openQL v1.0 said "preserves the Lie group symmetries"; the expression is unchanged and was refuted in `openql-eval` |
| "symplectic" in works cited by either preprint | — | **1**, and about the Freudenthal space for E₇ |
| v1.1 §6.1 grid state | "a million-node grid" | 274.7 MiB; one sweep 549.3 MiB = 0.615 ms |
| sweeps per candidate at "millions per day" | "circumvents this limit" | **14 to 140** — about one multigrid linear solve |
| what the objective must actually cover | — | field, torque ripple, cogging vs rotor angle, B–H iron loss, coupled thermal |
| zero-branching | the thing that circumvents the limit | true, but it is the loss of sparsity: **2× to 100×** penalty vs a sparse solver |
| "fractal-like winding patterns that minimize skin effect" | claimed | the established remedy subdivides conductors (Litz); a fractal boundary adds perimeter at fixed cross-section |
| claims removed in v1.1 that this evaluation measured | — | **4 of 6 removals** |
| ORCID placeholder in the PDF header | — | still unfilled, **regenerated in Czech** |
| 12D node shape | openQL: 12×12 from three 4×4 blocks | IPC §3: "a 4×4 (for 12D macroscopic physics)" |

## Scope

Neither deposit ships code, measurements or figures. §6 of the write-up sets out
what is not measured — the intensional-computing framing is a position about
representation, not a quantitative claim — and §7 the limits: the ceilings are
theoretical peaks, which strengthens the "exceeds the card" findings and weakens
the "fits" one, though 14.6× of headroom survives any plausible efficiency
factor.

The openQL v1.0 measurements referred to throughout are not reproduced here;
they live in [`openql-eval`](https://github.com/karagos01/openql-eval), and the
reference verdicts in
[`reference-audit`](https://github.com/karagos01/reference-audit).

## Companion evaluations

- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL v1.0 original that these two deposits restate and revise
- [`reference-audit`](https://github.com/karagos01/reference-audit) — whether all 81 citations in all 18 deposits say what they are cited for
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — the openOmega matter-antimatter and sedenion proposal of October 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — the HOS-PV 2.0 singlet-fission and spintronic photovoltaic proposal of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
