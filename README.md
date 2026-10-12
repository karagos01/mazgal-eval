# Dual-Scale Waveform Optimization / HFRS — independent evaluation

Reproducible evaluation of M. Mazgal, *Dual-Scale Waveform Optimization and
Hysteretic-Fractal Resonant Stimulation (HFRS) for Minimizing Transport
Resistance in Na-ion Lattices* (Zenodo, 6 October 2026, DOI
[10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**There is nothing in the band.** `F_micro` is specified as "kHz to MHz" and
said to "induce phonon-assisted tunneling"; the lowest Raman-active lattice mode
measured in a layered oxide cathode is 144 cm⁻¹ = **4.32 THz**, between **6.6
and 9.6 orders of magnitude** above it. In energy, hf at 1 MHz is **6.3 million
times** below kT at 300 K and seven to eight orders below the 0.10–0.64 eV sodium
migration barrier. And the band where a cell has any faradaic response — the
charge-transfer semicircle at ~1 Hz–1 kHz — **does not overlap `F_micro` at
all**, so current there flows through the double-layer capacitance and
dissipates in the series resistance, which is the Joule heating §1 exists to
avoid.

**But §5 is the best-argued section in any of this author's seventeen
deposits**, and §1 of the write-up says so first: it names the jelly-roll
parasitics and the thermal-versus-kinetic confound unprompted, and prescribes
planar coin cells and isothermal calorimetry. That is what a referee would have
written.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. Everything is arithmetic on the preprint's own parameters
and on published values, because the deposit ships no code, no measurements and
no figures.

## Reproducing the results

```
./run_all.sh          # everything, about 1 second on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`frequency.py`](frequency.py) | the `F_micro` band against measured lattice modes, against kT and the migration barrier, against the charge-transfer band, and the skin depth §5 invokes | §§2–3 |
| [`anomaly.py`](anomaly.py) | the §2.2 heading against its body, whether its criterion survives the cell warming, and what the paper's own pulsed-charging citation found | §4, §7 |
| [`throughput.py`](throughput.py) | evaluations per day, the sample-lifetime ceiling, the ageing confound, the DDS data rate, and §6 against the deposit's contents | §§5–6 |

Every constant is in [`constants.py`](constants.py) with a **provenance tag** —
`[P]` from the preprint, `[V]` verified against a named source, `[A]` an assumed
range that is swept rather than asserted — and no other script defines one.
Full output of one run: [`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| `F_micro` band | "kHz to MHz range" | 10³–10⁶ Hz |
| lowest measured lattice mode in a layered oxide cathode | "phonon-assisted tunneling" | 144 cm⁻¹ = **4.32 THz** |
| gap at the top of the band | — | **4 317 011×** (6.6 orders) |
| gap at the bottom of the band | — | 4.3·10⁹× (9.6 orders) |
| hf at 1 MHz | — | 4.136·10⁻⁹ eV |
| kT at 300 K | — | 0.02585 eV → **6 250 986×** larger |
| Na migration barrier | "lower activation barriers" | 0.10–0.64 eV → **2.4·10⁷ to 1.5·10⁸×** the quantum |
| charge-transfer band in EIS | — | ~1 Hz – 1 kHz |
| overlap with `F_micro` | — | **0 Hz** |
| what flows in that band instead | "coherent ion intercalation" | double-layer displacement current, dissipating as I²R |
| §2.2 heading vs body | "Negative Differential Resistance" | dV/dI = R_i > 0 always for a charging cell; the body defines an efficiency criterion instead |
| I²R heating over a 20 K rise | — | falls **1.6–3.0×**, which is the signature §2.2 reads as the anomaly |
| aluminium skin depth at 1 MHz | "skin-effect reflections" | **82 µm** against a 12–20 µm foil — the right conclusion, wrong mechanism |
| evaluations/day, 8 cells at 1C | "in real physical time" | **96** |
| evaluations available from one sample set | — | **4 000–24 000 ever**, after 42–250 days |
| what PSO typically needs | "hyperdimensional" space | 10⁴–10⁵ |
| DDS stream per cell | GPU-generated | 20–200 MB/s — data movement, no floating point |
| §3 vs §4 on where generation happens | GPU / "local generative engine" | the two sections describe different machines |
| §6 "Structure of Provided Data" | /Hardware, /Software, /Datasets | **1 file, 97 786 bytes** — the PDF |
| licence | "CERN-OHL-S for hardware" in the PDF | record carries CC BY 4.0 only |
| the paper's only pulsed-charging citation | cited beside `F_micro` | identifies solid-state diffusion, **0.25 Hz**, and prefers a **continuous** ramp |
| hypercomplex vocabulary | — | Maxwell, octonion, quaternion, hypercomplex, non-associative, tensor, causal: **all 0** |

## Scope

The deposit is a four-page preprint under CC BY 4.0 with no code, no
measurements and no figures, so there is nothing to benchmark. §8 of the
write-up sets out the limits: the Raman figures are from a lithium NMC cathode
rather than a sodium one, used because both crystallise in the α-NaFeO₂
structure, and a sodium-specific measurement would move them by tens of per cent
and not by the six orders of magnitude at issue. The `[A]` tags mark values that
could not be checked against a primary source here and are therefore swept.

All six references were read for content in
[`reference-audit`](https://github.com/karagos01/reference-audit), which holds
the verbatim evidence; §7 summarises what the pulsed-charging citation actually
says and does not duplicate the rest.

## Companion evaluations

- [`reference-audit`](https://github.com/karagos01/reference-audit) — whether all 69 citations in all 16 deposits say what they are cited for
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL tensor matrix architecture of October 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
