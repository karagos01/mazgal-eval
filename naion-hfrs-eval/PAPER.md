# The band with nothing in it: an evaluation of *Dual-Scale Waveform Optimization and HFRS*

karagos01, October 2026

## Abstract

M. Mazgal, *Dual-Scale Waveform Optimization and Hysteretic-Fractal Resonant
Stimulation (HFRS) for Minimizing Transport Resistance in Na-ion Lattices*
(Zenodo, 6 October 2026, DOI
[10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884)) proposes
charging sodium-ion cells with a superposition V(t) = W_macro(t) + F_micro(t),
where F_micro is a "high-frequency fractal modulation (kHz to MHz range)" said
to "induce phonon-assisted tunneling and lower activation barriers".

Three measurements, all ratios. The lowest Raman-active lattice mode measured in
a layered oxide cathode is 144 cm⁻¹, or **4.32 THz** — between **6.6 and 9.6
orders of magnitude** above the F_micro band, so there is no phonon in that band
to assist. In energy, hf at 1 MHz is 4.1·10⁻⁹ eV, **6.3 million times** below kT
at 300 K and seven to eight orders below the 0.10–0.64 eV sodium migration
barrier it is meant to lower. And the band where a cell has any faradaic
response at all is the charge-transfer semicircle at roughly 1 Hz–1 kHz, which
**does not overlap** F_micro: above it the measured response is ohmic and
inductive, so current flows through the double-layer capacitance and dissipates
in the series resistance. That is Joule heating, the loss §1 exists to avoid.

§2.2 names negative differential resistance in its heading and defines a
sub-proportional thermal response in its body; these are different quantities,
and for a charging cell dV/dI = R_i > 0 always. Worse, the criterion as written
is satisfied by a cell that is merely warming: Arrhenius with an apparent
activation energy of 0.20–0.50 eV cuts I²R heating by **1.6–3.0×** over a 20 K
rise. §5 identifies that confound itself and prescribes isothermal calorimetry,
which is to the paper's credit — but §2.2 is where the search objective is
defined, and as defined the optimiser would find warm cells.

§3's search is bounded by electrochemistry, not by GPUs: 8 cells at 1C give
**96 evaluations/day**, and the samples' whole useful life yields at most
**24 000** evaluations, which is the bottom of the range a particle swarm needs
on the "hyperdimensional" space §3 describes. §6 lists Gerber files, CUDA
kernels and DAQ logs as "Provided Data"; the deposit contains **one file**, the
four-page PDF.

Two findings go the other way. **§5 is the best-argued section in any of this
author's seventeen deposits** — it names two real confounds unprompted and
prescribes the right instruments for both. And its conclusion about MHz signals
is correct, though for a different reason than the skin effect it cites: at 1 MHz
the aluminium skin depth is 82 µm against a 12–20 µm foil.

## 1. What is correct

**§5 does the work a referee would do.** Verbatim: commercial wound cells
"present massive parasitic inductance and capacitance" so "Phase 1 of
experimental validation must strictly utilize planar coin-cell geometries"; and
"Differentiating between standard thermal agitation (which naturally lowers R_i
as the cell heats up) and genuine electro-kinetic field enhancement requires
highly precise isothermal calorimetry during the GPU-driven search phase." Both
are real confounds, both are stated without being asked, and both come with the
right remedy. Nothing else in this series does that.

**W_macro is a real and supported idea.** A low-frequency macroscopic envelope
that lets concentration gradients relax between pulses is exactly what the
paper's own pulsed-charging citation analyses, and it works there.

**The hardware is ordinary and buildable.** A GaN synchronous stage on an
insulated metal substrate with an STM32 or Zynq doing microsecond logging is a
normal power-electronics design. Nothing in §4 requires anything that does not
exist.

**The vocabulary is absent.** "Maxwell", "octonion", "quaternion",
"hypercomplex", "non-associative", "tensor" and "causal" all occur zero times.

## 2. There is no phonon in the band

§2.1 puts F_micro in the "kHz to MHz range" and says it induces
"phonon-assisted tunneling". Raman spectroscopy of a layered oxide cathode
measures bands at 144, 189 and 324 cm⁻¹ — 4.32, 5.67 and 9.71 THz. Layered
LiMO₂ crystallises in the α-NaFeO₂ structure, the same structural family as the
sodium layered cathodes at issue.

| | frequency | ratio to F_micro top (1 MHz) |
|---|---|---|
| lowest measured mode | 4.32 THz | **4 317 011×** (6.6 orders) |
| same, against 1 kHz | — | 4.3·10⁹× (9.6 orders) |

Nothing vibrates in the kHz–MHz band in this material, so there is no mode for
the modulation to couple to. The word "fractal" does not change that: a
self-similar waveform whose highest component is 1 MHz still has no power at
4 THz.

In energy the same gap reads more sharply, because that is the form tunneling
arguments take:

| | value |
|---|---|
| hf at 1 MHz | 4.136·10⁻⁹ eV |
| kT at 300 K | 0.02585 eV |
| ratio | **6 250 986×** |
| Na migration barrier | 0.10–0.64 eV |
| E_a / hf(1 MHz) | 2.4·10⁷ to 1.5·10⁸ |

The quantum of the proposed stimulation is six million times smaller than the
thermal energy the ions already have. An ion at room temperature is being
battered by kT continuously; a field quantum nine orders below that does not
assist it over a barrier eight orders above it.

A fair caveat: a strong *classical* field can of course move ions, through the
drift term, and that is what any charger does. The claim being measured here is
the specific mechanistic one — phonon assistance and barrier lowering — and it
is that claim the ratios refute, not the idea that an AC component does
something.

## 3. The band has no faradaic response either

Even setting the lattice aside, the cell itself does not respond faradaically
where F_micro operates. In impedance spectroscopy the charge-transfer process
appears as a semicircle spanning roughly **1 Hz to 1 kHz**; above about 1 kHz the
measured response is ohmic resistance plus inductance — electrolyte, collectors,
connectors and leads.

F_micro is specified as 10³–10⁶ Hz. The two bands meet at a point and their
overlap is **zero**. So in the whole of F_micro's range, current entering the
cell flows through the double-layer capacitance in parallel with the
charge-transfer branch, and through the series inductance — it charges and
discharges an interface without crossing it. Capacitive current intercalates no
sodium. What it does do is dissipate in the series resistance, which is I²R
heating: the exact loss §1 opens by identifying as the thing to eliminate.

This is the finding that survives §5's own fix. §5 prescribes planar coin cells
to remove the jelly-roll parasitics, and that is the right move for the
inductance — but the double-layer shunt is a property of the electrode
interface, not of the winding geometry, so it is present in a coin cell too.

## 4. §2.2 defines two different criteria, and the one it defines is confounded

The heading says "Anomaly Criterion (Negative Differential Resistance)". The
body says Z_diff = dV/dI and defines the anomaly as an "incremental increase in
the integral power delivered by V(t)" yielding a "sub-proportional thermal
response".

These are not the same statement. NDR means dV/dI < 0. For a cell under charge
at fixed state of charge, V = OCV(SoC) + I·R_i with R_i > 0, so dV/dI = R_i > 0
unconditionally — the quantity in the heading cannot occur. Sub-proportional
heat per unit power is an efficiency statement, which can. The section gives no
way to tell which the optimiser is searching for. (dV/dI also has units of ohms,
so it is a differential *resistance*; "differential impedance" is the complex
quantity measured against frequency.)

And the criterion the body does define is satisfied by the cell warming up.
Internal resistance falls with temperature; with an apparent activation energy
of 0.20–0.50 eV, a 20 K rise multiplies I²R heating at fixed current by 0.61
down to 0.29 — a **1.6× to 3.0×** reduction in heat per unit current, which is
precisely the signature §2.2 reads as "the onset of coherent, low-friction ion
intercalation".

**§5 names this confound itself**, which is why this is a criticism of §2.2 and
not of the paper's awareness. But §2.2 is where the objective function lives,
and an eight-cell swarm optimising that objective would converge on whatever
combination of parameters warms the cells fastest.

## 5. The search is bounded by electrochemistry, and the samples die first

§3 maps one GPU to one physical cell and proposes to "find the optimal 'Key' in
real physical time". One evaluation of a candidate waveform is at minimum one
charge plus a discharge to return the cell to a known state:

| C-rate | charge+discharge | evaluations/day on 8 cells |
|---|---|---|
| C/2 | 4.0 h | 48 |
| 1C | 2.0 h | **96** |
| 2C | 1.0 h | 192 |

Against that, a coin cell is useful as a test vehicle for perhaps 500–3000
cycles, so one set of eight yields **4 000 to 24 000 evaluations ever**, reached
after 42 to 250 days of continuous cycling. Particle swarm optimisation on a
10–30 dimensional space typically wants 10⁴–10⁵ evaluations, and §3 calls its own
space "hyperdimensional". The whole lifetime budget of the apparatus is at the
bottom of that range.

There is also a confound §3 does not mention, and §5's calorimetry does not
reach. The objective function is internal resistance, and internal resistance
rises with cycle count. So the quantity being minimised drifts upward over
exactly the timescale of the search, by an amount that depends on how many
evaluations each cell has already served. A swarm that broadcasts its best
parameter vector between nodes is comparing cells of different age, and any
improvement found early is confounded with the samples being newer. §3's answer
— a "Dynamic Key Trajectory parameterized by the State of Charge" — handles
drift within a cycle; ageing is drift across cycles and is not a function of
SoC.

Finally, §3 and §4 describe different machines. §3 has each GPU streaming DDS
data to its cell; at 10–100 MSa/s and 16 bits that is 20–200 MB/s per cell, a
data-movement task with no floating-point content and nothing to occupy a GPU
between evaluations two hours apart. §4 then says the local "DSP or FPGA (e.g.
STM32/Zynq architectures)" is "acting as the local generative engine" — in which
case the GPU is not generating the waveform and the 1:1 mapping has no work.

## 6. §6 describes data that is not in the deposit

§6 is headed "Structure of Provided Data (Zenodo Repository)" and lists, in the
present tense, `/Hardware` with "Gerber, BOM, 3D STEP", `/Software` with "CUDA
kernels for the distributed arbitrary waveform search, PSO synchronization
scripts, and DDS streaming code", and `/Datasets` with "High-speed Data
Acquisition (DAQ) logs comparing isothermal calorimetry and voltage curves".

The deposit contains one file: the four-page PDF, 97 786 bytes. The PDF header
also proposes "CC BY 4.0 for text and data, CERN-OHL-S for hardware"; the Zenodo
record carries CC BY 4.0 only.

This is the same pattern as the cymatic deposit's §6, which promises a GitHub
repository and names none — but in the future tense. Here the data is described
as provided.

## 7. What the paper's own citation says instead

Purushothaman & Landau (2006), the preprint's only pulsed-charging reference,
identifies the limiting mechanism as **solid-state diffusion**: lithium
concentration "reaches saturation at the graphite/electrolyte interface after
about 1 h under conventional constant current charging". Its analysed protocol
is a **3 s pulse with 1 s rest** — 75 % duty, 0.25 Hz. And its best result is not
a pulse at all: "A nonlinearly decreasing current density profile … was shown to
provide complete charging in less than 3/4 of an hour, faster than any other
pulse-charging profile studied."

So the one source cited for pulsing supports W_macro, at a quarter of a hertz,
and prefers a continuous ramp to any pulse. It identifies no beneficial kHz
band, and the content audit of all six of this deposit's references in
[`reference-audit`](../reference-audit) found none that
does. Two further citation slips are recorded there: Tarascon & Armand is Nature
414(**6861**), and "Macdonald (2005)" is Barsoukov & Macdonald as editors of the
second edition, Macdonald alone having edited a differently titled first edition
in 1987.

## 8. Limitations

No cell was built, charged or measured. Everything here is arithmetic on the
preprint's own parameters and on published values, because the deposit ships no
code, no measurements and no figures.

Provenance is tagged in `constants.py`: `[P]` the preprint's own values, `[V]`
verified against a named source, `[A]` an assumed range swept rather than
asserted. Coin-cell life, foil thickness, the Arrhenius activation energy, the
PSO evaluation budget and the DDS sample rate are all `[A]`, and every
conclusion drawn from them is computed across the whole range.

The Raman figures are from a lithium NMC cathode, not a sodium one. They are
used because layered LiMO₂ and the sodium layered oxides share the α-NaFeO₂
structure, so the mode frequencies are the right order; a sodium-specific
measurement would shift them by tens of per cent and not by six orders of
magnitude, which is the size of the gap at issue.

The EIS band is quoted as "approximately 1 Hz to 1 kHz", which is where the
charge-transfer semicircle is conventionally found. Real cells vary with
chemistry, temperature and state of charge, and a cell with unusually fast
kinetics would push the corner higher. It would have to move it three orders of
magnitude to reach the top of F_micro.

The §4 claim that a measured apparent activation energy for R_i reflects a
single process is a simplification; R_i aggregates electrolyte conductivity, SEI
transport and charge transfer, each with its own temperature dependence. The
swept range is meant to cover that, and the conclusion — that warming alone
produces the signature — holds across all of it.

## 9. Data and code availability

`constants.py` holds every constant with its provenance tag and source, and no
other script defines one. `frequency.py`, `anomaly.py` and `throughput.py`
reproduce §§2–6. `run_all.sh` runs everything offline in about a second;
`results.log` is the output of one run. Reference verdicts are not duplicated
here — they live with their evidence in
[`reference-audit`](../reference-audit).

## References

The evaluated preprint: M. Mazgal, *Dual-Scale Waveform Optimization and
Hysteretic-Fractal Resonant Stimulation (HFRS) for Minimizing Transport
Resistance in Na-ion Lattices*, Zenodo, 6 October 2026, DOI
10.5281/zenodo.23186884, CC BY 4.0.

External sources are cited in `constants.py` beside the values they support:
Raman and Infrared Spectroscopy of Materials for Lithium-Ion Batteries,
*Int. J. Mol. Sci.* 26(24), 11879 (2025), DOI 10.3390/ijms262411879, for the
cathode lattice modes; the NaFeO₂ and NaFePO₄ migration-barrier literature,
including *Materials* 12(19), 3243 (2019), DOI 10.3390/ma12193243; standard EIS
practice for the charge-transfer band; CRC resistivities; the SI 2019 defining
constants; and Purushothaman, B. K. & Landau, U., *J. Electrochem. Soc.* 153(3),
A533 (2006), DOI 10.1149/1.2161580. Quotations are short excerpts used for
criticism and review.
