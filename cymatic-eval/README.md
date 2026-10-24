# Cymatic stomatal stimulation — independent evaluation

Reproducible evaluation of M. Mazgal, *Cymatic Stomatal Stimulation and Pulsed
Optical Assimilation: Scaling from Cybernetic Bioreactors to Industrial-Scale
Acoustic Modulation* (Zenodo, 5 October 2026, DOI
[10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**Both frequencies the design rests on are the note B.** 246.91 Hz is equal-tempered
B3 to within 0.22 cents, 61.72 Hz is B1 to within 0.43 cents, and the optical period
50 µs + 4000 µs is 4.050 ms = 246.91 Hz — so the timing derived from Calvin-cycle
kinetics and the frequency derived from guard-cell mechanics are one number. At
1.2346 % duty the average irradiance is 256 µmol/m²/s, below light saturation for
every C3 crop, so the quenching the design bypasses is barely engaged in the regime
it creates; and dry matter per kilowatt-hour is invariant under pulsing to
3.6·10⁻¹⁵, which is the quantity §5 claims to redefine. At field scale a
three-bladed turbine's blade-pass frequency is 0.700 Hz where 61.72 Hz is wanted,
its whole broadband output is 22.5 dB short of the level the cited review works at,
and a 50 Hz transformer core has no 61.72 Hz line to tune.

None of the author's hypercomplex vocabulary appears in this deposit, and it is
the first with an almost entirely real bibliography; §1 of the write-up sets out
what is correct before anything else. (§1 carried a correction on 9 October: it
had claimed priority for the vocabulary being absent, which a census over all
sixteen records in [`reference-audit`](https://github.com/karagos01/reference-audit)
disproved -- COBAR and the Momentum Drive of September have none of those terms
either.)

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. Everything is arithmetic on the preprint's own parameters and
on published constants, because the deposit ships no code, no measurements and no
figures.

## Reproducing the results

```
./run_all.sh          # everything, about 2 seconds on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| `frequency.py` | nearest equal-tempered pitch to each published frequency; the optical period against the acoustic one; the cited band against the derived subharmonic | §§2–3 |
| `light.py` | duty cycle and time-averaged photon flux against C3 light saturation; the dark interval against RuBisCO and the PQ pool; invariance of g/kWh | §§4–6 |
| `acoustics.py` | blade-pass frequency, the rotor speed and tip Mach the target needs, the sound-power budget at 100–1000 m, wind-farm spacing as a phased array, transformer harmonics | §§7–8 |
| `water.py` | transpiration across the midday depression, and water per unit carbon | §9 |

Every external constant is in [`constants.py`](constants.py) with its source, and
no script defines a physical constant of its own. Full output of one run:
[`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| 246.91 Hz, "synthesized to maximize localized guard cell vibration" | — | **B3**, −0.22 cents |
| 61.72 Hz, "calculated" subharmonic | — | **B1**, −0.43 cents |
| optical period 50 µs + 4000 µs | from "the Calvin cycle" | **246.91 Hz** — the same number as the acoustic one, to 1.5·10⁻⁵ |
| PAFT sensitive band | "typically between 50 and 120 Hz" | cited review gives **0.1–1 kHz**; the division by 4 leaves it |
| time-averaged irradiance | "extreme-intensity photon bursts (4500 W/m²)" | **55.6 W/m² = 256 µmol/m²/s**, 0.13× full sun |
| that average against C3 light saturation | bypasses NPQ | **1.57× below** lettuce, 5.48× below wheat |
| ceiling on bypassing NPQ | "up to 60%" dissipated | **2.50×**, from the paper's own figure |
| dark phase vs the mechanism named | "perfectly matches … the Calvin cycle" | Calvin **250–500 ms**, 62–125× off; PQ pool **2–20 ms** |
| g/kWh over an 81-fold range of duty cycle | "redefine the gram-per-watt limit of CEA" | spread **3.6·10⁻¹⁵** — invariant |
| g/kWh, assumptions favouring the design | redefined | **12.42**, inside the commercial 5–10 range |
| blade-pass frequency, 3 blades at 14 rpm | retunable to 61.72 Hz | **0.700 Hz** — 61.72 Hz is the 88th harmonic |
| rotor speed for a 61.72 Hz blade pass | reached by "electromagnetically braking" | **1234 rpm**, Mach **18.8** at the tip, **85 167 g** |
| turbine sound power vs 70 dB at the plant | "large-scale agricultural acoustic stimulators" | short **22.5 dB (179×)** at 300 m, **33.0 dB (1987×)** at 1 km |
| the loss the frequency choice addresses | "minimal atmospheric attenuation" | correct, and it is **0.1 dB** against **24 dB** of spreading |
| wind farm as a phased array | "phased acoustic arrays" | elements **90–180 λ** apart where λ/2 is needed; 0.136° of rotor angle |
| transformer lines available on a 50 Hz grid | "tuned to precisely 61.72 Hz" | integer multiples of **50 Hz**; nearest is 11.72 Hz away |
| "asymmetric DC injection" | a tuning control | half-cycle saturation — the geomagnetic-current damage mode |
| midday transpiration if stomata are held open | "evapotranspiration rates will rise" | **3.0×**, independent of VPD |
| water per unit carbon | — | **1.3–2.5×** for every saturating assimilation response |
| 15–18 % biomass increase | claimed | asserted, with no link to dose, duration, frequency or crop |
| references | 5 given | **4 of 5** resolve exactly; the 5th could not be located (§10) |

## Scope

The deposit is a four-page preprint under CC BY 4.0 with no accompanying code, no
measurements and no figures, so there is no implementation to test; §6 of it says
hardware topology, STM32 firmware and CAD models "will be maintained in an
open-source GitHub repository", and names none. The limits of what is computed here
are set out in §11 of the write-up — no plants were grown, and the acoustic model is
hemispherical spreading, calibrated against the 40–45 dB(A) measured at 300 m.

## Companion evaluations

- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL tensor matrix architecture of October 2026
- [`reference-audit`](https://github.com/karagos01/reference-audit) — whether all 81 citations in all 18 deposits say what they are cited for
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — the copper-based hemocyanin physiology proposal of October 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — the openOmega matter-antimatter and sedenion proposal of October 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — the HOS-PV 2.0 singlet-fission and spintronic photovoltaic proposal of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
