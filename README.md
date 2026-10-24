# Mazgal preprint corpus — independent evaluations

Twelve reproducible evaluations of the Zenodo deposits of M. Mazgal, covering
**all 18 records** (16 distinct works) published between September and October
2026, plus an audit of **all 81 external references** in them.

Each subdirectory is self-contained: it has its own `README.md` /
`README.cs.md`, its write-up in `PAPER.md` / `PAPER.cs.md`, its scripts, its
`requirements.txt`, its `run_all.sh` and the committed `results.log` of one run.
Each was published as a separate repository until 24 October 2026 and the full
commit history of all twelve is preserved here.

> Czech version: [`README.cs.md`](README.cs.md).

## The twelve evaluations

| | deposit | date | what the measurement found |
|---|---|---|---|
| [`octonion-mppt-eval`](octonion-mppt-eval) | *Intensional Maxwellian Formalism in Power Electronics* ([v1.0](https://doi.org/10.5281/zenodo.22877912), [v1.1](https://doi.org/10.5281/zenodo.22914238)) | 22 Sep | the associator the controller is built on is **identically zero** on exactly the seven Fano triples; `e0`, the component the published code computes, is identically zero for any input; 20 000 further configurations searched and **none beats Perturb & Observe** |
| [`xternary-eval`](xternary-eval) | *X-Ternary: A Deterministic Causal 2-Bit Inference Engine* ([22877345](https://doi.org/10.5281/zenodo.22877345)) | 22 Sep | 1.26 bit/weight stored in 2.25 — 20 % less information than BitNet b1.58 in 42 % more bits; 60 tok/s is above the named card's bandwidth ceiling; GPU float addition is **already non-associative for 31.9 %** of random triples, which is the non-determinism the paper cures by adding non-associativity; a ternary KV cache costs ×5 001 in perplexity |
| [`causal-trilogy-eval`](causal-trilogy-eval) | CQFT ([22959886](https://doi.org/10.5281/zenodo.22959886)), PCTP ([22962188](https://doi.org/10.5281/zenodo.22962188)), SOTP ([22962557](https://doi.org/10.5281/zenodo.22962557)) | 25 Sep | **the algebra is correct** — the oriented Fano plane of SOTP Eq. (3) is one of only 16 of 128 orientations that give a normed division algebra — and every defect is in the step from algebra to hardware |
| [`openql-eval`](openql-eval) | *openQL / openOL* ([23112560](https://doi.org/10.5281/zenodo.23112560)) | 3 Oct | the 4×4 matrix of §2.1 **is** the left regular representation of ℍ, to 1.8·10⁻¹⁵; the octonion half of the same sentence is **excluded by a theorem**, because matrix multiplication is associative and the homomorphism leaves 1 of 8 dimensions |
| [`cymatic-eval`](cymatic-eval) | *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation* ([23156927](https://doi.org/10.5281/zenodo.23156927)) | 5 Oct | **both frequencies the design rests on are the note B** (B3 to 0.22 cents, B1 to 0.43 cents); dry matter per kWh is invariant under pulsing to 3.6·10⁻¹⁵, which is the quantity §5 claims to redefine |
| [`naion-hfrs-eval`](naion-hfrs-eval) | *Dual-Scale Waveform Optimization and HFRS* ([23186884](https://doi.org/10.5281/zenodo.23186884)) | 6 Oct | **there is nothing in the band** — `F_micro` sits 6.6 to 9.6 orders of magnitude below the lowest Raman-active lattice mode, and does not overlap the faradaic band at all; but §5 is the **best-argued section in the corpus** |
| [`phytomining-eval`](phytomining-eval) | *Quantum Biofortification and In-Situ Phytomining* ([23174932](https://doi.org/10.5281/zenodo.23174932)) | 6 Oct | one sentence of §4 gives **two densities 24× apart**; §3.3 calls ¹³⁸La a stable isotope, and ¹³⁹La already has spin 7/2 so there is nothing to select for; the cited magnetic-isotope author measures **3–5× suppression** for exactly the trio cited for acceleration |
| [`hemocyanin-eval`](hemocyanin-eval) | *Copper-Based Hemocyanin Physiology in Hominids* ([23209266](https://doi.org/10.5281/zenodo.23209266)) | 7 Oct | hemocyanin carries **4.4 to 14.6× less** oxygen than human blood, so the proposal needs **7.3 L/min of cardiac output at rest** and **fails sitting still**; and vertebrates have no hemocyanin gene for the epigenetic switch to turn on |
| [`intensional-physics-eval`](intensional-physics-eval) | IPC ([23241777](https://doi.org/10.5281/zenodo.23241777)) + openQL v1.1 ([23241148](https://doi.org/10.5281/zenodo.23241148)) | 8 Oct | the **first numeric hardware claim the arithmetic supports** — 10⁹ queries/s against a 1.46·10¹⁰/s ceiling, 14.6× of headroom at the 4×4 node — 54× out at 112×112, and 4 to 32× short for the ray marching of its own §4 |
| [`openomega-eval`](openomega-eval) | *openOmega: ±12D, ±112D, ±224D* ([23263528](https://doi.org/10.5281/zenodo.23263528)) | 9 Oct | the algebra is right and is **verified here from first principles** — (e₁+e₁₀)×(e₄−e₁₅) = 0 exactly — but sedenions are not needed for it (200 of 200 random 224×224 pairs do the same), **no energy leaves a product of norm 4.1·10⁻¹³**, and the `if (collision)` moves rather than disappears |
| [`hospv-eval`](hospv-eval) | *HOS-PV 2.0* ([23364732](https://doi.org/10.5281/zenodo.23364732)) | 14 Oct | **the mechanism is sound and the limit really does move**: 41.24 % against Shockley-Queisser's 33.7 %, confirmed from the ASTM G173-03 spectrum after three published self-checks. But 45.9 % is the **two-gap tandem row** of the paper it is cited from, and the high-energy channel needs 2.44 e⁻/photon against singlet fission's ceiling of two |
| [`reference-audit`](reference-audit) | all 18 records, 81 references | 9 Oct | **14 of 81 references (17.3 %) are attached to a claim**, 15 carry only a gloss, **52 (64.2 %) have no stated relation to anything**, and three deposits have no bibliography at all. Verdicts: SUPPORTS 4, PARTIAL 25, NO SUPPORT 24, **REFUTES 15**, UNRESOLVED 1 |

## What the twelve measure together

**What is borrowed is mostly right. What is built fails at one seam, always the
same one: the step from algebra to hardware.** Hardware is associative, and
every machine in the corpus is built on non-associativity being physically
available.

| what was taken | where it died |
|---|---|
| the octonion associator as "a non-zero hardware observable" | identically zero on exactly the seven triples of the Fano plane the gate array is built from |
| 𝕆 → 12×12 real matrices | matrix multiplication is associative; 1 of 8 dimensions survives |
| sedenion zero divisors as annihilation | WMMA is associative and sedenions are not even alternative; ‖A·B‖ = 4.1·10⁻¹³ carries no energy |
| non-associativity as the cure for GPU non-determinism | the non-determinism **is** the non-associativity of float addition, 31.9 % of random triples |

Six things hold, and each evaluation leads with them: HOS-PV is a physically
real direction and the Shockley-Queisser limit does move (+7.5 points); IPC §5's
query rate passes the roofline at the small node; HFRS §5 reads like a referee's
report; the borrowed algebra gets steadily more correct across the series
(quaternions to 1.8·10⁻¹⁵, one of 16 valid Fano orientations, 168 sedenion zero
divisors); the author's own claim that the defence lives in the references is
confirmed in four deposits (Furey, Baez, Shockley & Queisser's footnote 22,
Moreno); and three premises outside the algebra are correct as stated.

Where support is genuine, the same pages refute the mechanism they are offered
for: Furey, Dixon and Baez all resolve non-associativity by moving into the
**associative** algebra of left-multiplication operators, which is the step the
proposed architecture is built on refusing, and the norm failure that creates
Moreno's zero divisors is the same thing that denies openOmega its "absolute
energy conservation".

## Running everything

Each subdirectory stands alone:

```
cd openomega-eval
python3 -m pip install -r requirements.txt
./run_all.sh
```

or, from here, every evaluation in sequence:

```
./run_all.sh            # about 25 minutes, almost all of it octonion-mppt-eval
```

Everything is pure CPU and needs no network, with two exceptions:
`octonion-mppt-eval` takes ~20 min and uses 16 processes, and `xternary-eval`
needs one CUDA GPU for all but `bits.py`. The union of all dependencies is in
the root [`requirements.txt`](requirements.txt); the per-directory files are
narrower and are what each `run_all.sh` expects.

Every value in every subdirectory is defined once, in that subdirectory's
`constants.py` where it has one, with a **provenance tag** — `[P]` from the
preprint, `[V]` verified against a named source, `[A]` assumed and swept.

## Licence

Code (all `*.py`, `*.sh`): MIT, see [`LICENSE`](LICENSE).
All `PAPER.md`, `PAPER.cs.md`, `README.md` and `README.cs.md`: CC BY 4.0.
`hospv-eval/data/ASTMG173.csv` is NREL's tabulation of ASTM G173-03 as
distributed with pvlib (BSD 3-clause); `xternary-eval/vendor/` keeps its
upstream licence.

The evaluated preprints are the work of their own author and are not included
here; they are open access under CC BY 4.0 at the DOIs above.
