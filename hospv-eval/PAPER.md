# The right mechanism, the wrong row of the table

An independent evaluation of M. Mazgal, *HOS-PV 2.0: Exceeding the
Shockley-Queisser Limit via Chiral-Induced Spin Selectivity, Dexter-Sensitized
Singlet Fission, and Altermagnetic Carrier Extraction* (Zenodo, 14 October 2026,
DOI [10.5281/zenodo.23364732](https://doi.org/10.5281/zenodo.23364732)).

Every number below is produced by the scripts in this repository from the ASTM
G173-03 reference spectrum and from published measurements, with no GPU and no
network. One run of `./run_all.sh` is recorded in [`results.log`](results.log).

## 1. The mechanism is sound, and the limit really does move

The architecture's central claim is that a single junction can be made to
exceed the Shockley-Queisser limit by letting one absorber split high-energy
singlets into pairs of triplets and handing them to a second, narrow-gap
absorber that sets the voltage. That is correct, and this repository confirms it
from first principles rather than on the author's say-so.

The detailed-balance calculation in [`detailed_balance.py`](detailed_balance.py)
is built from the spectrum and the Planck law. Before it is pointed at the
preprint it reproduces three published values:

| model | measured here | published |
|---|---|---|
| Shockley-Queisser, one carrier per photon | **33.77 %** at 1.335 eV | 33.7 % at 1.34 eV |
| carrier multiplication, QY = floor(E/E_g) | **44.62 %** at 0.70 eV | 44.4 % at 0.70 eV |
| multiplication capped at two per photon | **42.09 %** at 0.94 eV | 42.0 % at 0.95 eV |

The second and third rows are from reference [5] of the preprint and from the
same group's companion report. All three land within 0.3 percentage points, and
the third lands within 0.1 points and 10 meV, which is what licenses everything
that follows.

Applied to the architecture — one electron per photon between 1.12 eV and
2.25 eV, two above 2.25 eV, all extracted at 1.12 eV — the same code gives:

| | limit |
|---|---|
| plain single gap at 1.12 eV | 33.48 % |
| Shockley-Queisser optimum, 1.34 eV | 33.76 % |
| **this architecture, at its own two energies** | **41.24 %** |

So the idea works. The architecture beats Shockley-Queisser by **7.5 percentage
points**, with a short-circuit current of 53.6 mA/cm² and an open-circuit
voltage of 0.883 V in the radiative limit. Exceeding the limit is not what is
wrong with this preprint.

Several other things in it are also right, and are worth saying plainly because
the rest of this document is critical:

* The wavelength conversions are exact: 2.25 eV → 551.0 nm, 1.12 eV →
  1107.0 nm, both as printed.
* `EQE_high = η_SF × η_DET × EQE_BHJ = 1.85 × 0.92 × 0.90 = 1.5318`, printed as
  153 %. Correct.
* `β_eff = β_L(1 − η_PB P²) = 1 − 0.95 × 0.85² = 0.3136`, printed as 0.314 and
  68.6 % suppression. Correct.
* `PCE = 52.3 × 0.81 × 0.840 / 100 = 0.3558`, printed as 35.58 %. Internally
  consistent arithmetic; it is the current entering it that fails.
* The claimed fill factor of 84.0 % is below the ideal-diode ceiling of
  **86.2 %** at V_oc = 0.81 V, so unlike the other headline numbers it is
  reachable as stated.
* The spin splitting attributed to the altermagnetic collector, ~0.8 eV, is the
  measured value for MnTe: angle-resolved photoemission reports 0.37 eV and
  0.80 eV in two independent studies.
* The symmetry argument of section 5.1 — that a collinear antiferromagnet whose
  sublattices are connected by inversion or translation has spin-degenerate
  bands, whereas one connected by rotation does not — is stated correctly, and
  reference [7] is the right citation for it.
* Reference [3], Rao et al. 2013, is correctly identified as the spin-kinetics
  measurement that establishes the triplet drain.

## 2. 45.9 % is the two-gap tandem row

The abstract claims the architecture "elevates the single-junction
thermodynamic limit to 45.9 %", citing reference [5]: M. C. Hanna and A. J.
Nozik, *J. Appl. Phys.* **100**, 074510 (2006).

The best this family of models can do, at any pair of energies whatsoever, with
doubling as perfect as singlet fission can be, is **42.09 %**. At the two
energies the preprint actually specifies it is **41.24 %**. So 45.9 % is not
merely optimistic: it is above the ceiling of the model it is drawn from, and no
choice of donor or acceptor reaches it.

Where it comes from is visible in the source. Reference [5]'s abstract reports:

| [5] reports | value |
|---|---|
| single gap, no multiplication | 33.7 % |
| single gap, with multiplication | 44.4 % |
| ideal **two-gap tandem**, without and with CM absorbers | **45.7 % → 47.7 %** |

45.9 % is not the single-junction row. It falls inside the two-gap tandem range.
And the single-junction value in the cited work is 44.4 % for *unlimited*
multiplication; for the doubling that singlet fission actually performs, the
same group reports 42.0 % — the number reproduced in §1 above.

This matters more than a mis-transcription usually would, because being a single
junction is the architecture's entire selling point. Section 1 argues against
III-V tandems on manufacturability grounds; the number imported to beat them is
a tandem number.

## 3. The photocurrent: one channel right, one over its own ceiling

Section 6.2 writes J_sc as two integrals, states a quantum efficiency for each
and reports a value for each. Both integrals are evaluated in
[`photocurrent.py`](photocurrent.py) against the real spectrum with the
preprint's own efficiencies:

| channel | published | measured |
|---|---|---|
| IR, 1.12–2.25 eV, at EQE = 0.85 | 28.5 | **28.89** |
| SF, above 2.25 eV, at EQE = 1.53 | 23.8 | **14.95** |
| total J_sc, mA/cm² | 52.3 | **43.83** |

The infrared channel is right to 1.3 %, which is within the accuracy of reading
a spectrum off a chart.

The high-energy channel is not. Photons above 2.25 eV carry **9.76 mA/cm²** of
charge if every single one of them yields one electron. Reaching 23.8 mA/cm²
therefore requires

    EQE_high = 23.8 / 9.76 = 244 %,

that is, **2.44 electrons per absorbed photon**. Singlet fission gives at most
two. The claim exceeds the ceiling of its own mechanism by 22 %, and exceeds the
153 % the same sentence states by 59 %.

The arithmetic is recoverable: 23.8 mA/cm² at EQE_high = 1.53 is the current of
all photons above **1.96 eV (634 nm)**, not above the 2.25 eV / 551 nm the same
sentence specifies — a shift of 294 meV. Only 9.8 mA/cm² of the AM1.5G spectrum
lies above 2.25 eV, and that is the quantity the architecture has to multiply.

Carried through, the published operating point becomes:

| | J_sc | PCE |
|---|---|---|
| as published | 52.30 | 35.58 % |
| with J_sc from the preprint's own efficiencies | **43.83** | **29.82 %** |
| with perfect fission, transfer and collection | 53.50 | 36.40 % |

There is a coincidence here worth pointing out, because it is the clearest
statement of what the architecture does and does not buy. A plain 1.12 eV
absorber with EQE = 1 and no fission at all collects **43.81 mA/cm²**. The whole
fission-plus-Dexter cascade, at the preprint's own quantum efficiencies, returns
**43.83 mA/cm²** — the same number to within 0.1 %. The multiplication pays for
the 0.85, the 0.92 and the 0.90, and nothing more. The architecture's real gain
over silicon is not in the current at all; it is that the current is collected at
a voltage set by a 1.12 eV gap while those collection losses are absorbed by the
doubling. That is a genuine and interesting result, and it is not the result the
preprint claims.

Two further checks on the operating point:

* **V_oc.** The radiative limit at E_g = 1.12 eV is **0.8782 V** for a plain
  gap and **0.8834 V** with the doubling. Section 6.2 states 0.90 V, 17 mV high.
  Its 0.81 V then follows from its own 0.90 V minus 0.09 V; from the measured
  limit it would be 0.793 V.
* **The non-radiative loss.** Moving ΔV_oc,nr from the 0.22 V section 6.2 calls
  typical to the 0.09 V it claims is, by the reciprocity relation
  ΔV_nr = −(kT/q) ln EQE_EL, a step in electroluminescence quantum efficiency
  from 1.9 × 10⁻⁴ to 3.0 × 10⁻², a **factor of 158**.

And for scale, how hard the claimed operating point is relative to its own
radiative limit:

| | fraction of limit |
|---|---|
| HOS-PV 2.0 against the measured limit | **86.3 %** |
| c-Si record against the Auger limit | 92.9 % |
| best OPV today against Shockley-Queisser | 59.3 % |

The projection asks a disordered organic blend to reach a larger fraction of its
radiative limit than crystalline silicon has managed in fifty years, starting
from the 59 % where organics sit today.

## 4. The spin mechanism: correct arithmetic, two inconsistent inputs

Section 4.1's expression and its worked value are right, as noted in §1. The
inputs are the problem, and both errors are instructive.

**η_PB = 0.95 is inconsistent with its own times, in the preprint's favour.**
The section defines η_PB = exp(−τ_ext/τ_s) and gives τ_ext = 20–80 ns and
τ_s = 5 µs in the same sentence. Those values give η_PB = 0.984 to 0.996, not
0.95 — and therefore a suppression of **72.0 %** rather than 68.6 %. The stated
0.95 corresponds to τ_ext = 256 ns. This correction improves the preprint's
result, and is recorded here for that reason.

**τ_ext itself is set by the mobility, and the preprint argues both ends of it.**
Section 4.1 defines τ_ext = d²/(2 µ V_int). With table 1's 220 nm active layer
the transit time is whatever the mobility makes it, and section 1 introduces
organic blends by their "low carrier mobilities" without giving a number. Swept
([`spin.py`](spin.py)):

| µ (cm²/Vs) | τ_ext | η_PB | β_eff/β_L | suppression |
|---|---|---|---|---|
| 1.0 × 10⁻⁴ | 3025 ns | 0.546 | 0.606 | **39.5 %** |
| 1.0 × 10⁻³ | 302 ns | 0.941 | 0.320 | 68.0 % |
| 1.0 × 10⁻² | 30 ns | 0.994 | 0.282 | **71.8 %** |

The quoted 20–80 ns requires µ = 1.5 × 10⁻² to 3.8 × 10⁻³ cm²/Vs, one to two
orders above a disordered bulk heterojunction and at or beyond the best ordered
organic films. At the bottom of the range the transit time is 3.0 µs, comparable
with the 5 µs spin lifetime rather than negligible against it, and the whole
effect falls to 39.5 %. The mechanism's margin, τ_ext ≪ τ_s, is real at high
mobility and gone at low mobility — and the preprint asserts the high end while
its introduction argues the low end.

**The suppression is measured against the wrong baseline.** Section 1 states
that uncorrelated encounters form 25 % singlet and 75 % triplet; section 4.1
blocks the triplet channel. If the triplet channel is blocked, what remains is
the singlet fraction, β_eff = 0.250 β_L. Section 4.1's chiral result is
0.314 β_L — the *larger* of the two. Unless β_L is read as the spin-blind
Langevin coefficient, in which case an ordinary achiral blend should already
show 0.250, the expression does not improve on the statistics it replaces. The
preprint's own reference [3] is the measurement of exactly that spin control in
achiral devices.

**P_CISS = tanh(ΔE/2kT) is a testable commitment.** Read as written, the
polarisation is a thermal population ratio, so a polarisation measured at 300 K
pins the splitting: 0.75 needs 50.0 meV, 0.85 needs 64.5 meV, 0.90 needs
75.7 meV. Holding 64.5 meV fixed, the same formula predicts the temperature
behaviour of the whole mechanism — and a solar cell does not run at 25 °C:

| T | P_CISS | suppression |
|---|---|---|
| 0 °C | 0.879 | 72.7 % |
| 25 °C | 0.850 | 68.0 % |
| 45 °C | 0.827 | 64.3 % |
| 59 °C | 0.810 | 61.8 % |
| 85 °C | 0.780 | 57.3 % |

This is a falsifiable prediction and a cleaner experimental signature than the
racemic-versus-homochiral comparison section 7 proposes, which it complements.

**ξ_SOC ∝ Z⁴ is the hydrogenic law, not the valence one.** Section 1 justifies
carbon's weak spin-orbit coupling with a Z⁴ scaling. Z⁴ is the fine-structure
scaling for an electron in a bare nuclear potential; the electrons that carry
spin in a conjugated polymer are screened valence p electrons. The exponent can
be measured, because the ground-term splitting of the halogens is one valence np
shell stepped down a column of the periodic table (NIST ASD):

| | Z | ²P₃⁄₂–²P₁⁄₂ (cm⁻¹) |
|---|---|---|
| F | 9 | 404.141 |
| Cl | 17 | 882.352 |
| Br | 35 | 3685.24 |
| I | 53 | 7602.976 |

A least-squares fit of ln(splitting) against ln Z gives an exponent of **1.69**
(worst residual 20 %, so the power law is itself only approximate) — below even
the Z² the review literature quotes for outermost electrons, and far from 4.
From carbon to lead the measured trend still gives a factor of 83, against 187
for Z² and 34 886 for Z⁴. Carbon's advantage is real on any of them. Only its
size, and the law quoted for it, are wrong.

## 5. The materials

**The fission donor fails the preprint's own ordering.** Section 2.1 requires
E(S₁) ≥ 2E(T₁). Section 2.2 specifies E(S₁) = 2.25 eV and E(T₁) = 1.15 eV, so
2E(T₁) = 2.30 eV and the condition **fails by 50 meV** — the fission the whole
architecture rests on is endothermic by 1.9 kT at 25 °C. The rest of the chain,
2E(T₁) ≥ 2E_g(IR), holds with 60 meV to spare.

Endothermic fission is not fatal in itself; tetracene is endothermic and still
efficient. But section 2.1 also demands 1/k_SF below 100 fs, and sub-100 fs
fission is what *exothermic* chromophores do. The two requirements pull in
opposite directions, and the squeeze is structural rather than a slip. The
ordering demands E(T₁) ≥ 1.12 eV *and* E(S₁) ≥ 2E(T₁) ≥ 2.24 eV simultaneously:

| | E(S₁) | E(T₁) | 2T₁−S₁ | T₁ ≥ 1.12? | S₁ ≥ 2T₁? |
|---|---|---|---|---|---|
| pentacene | 2.20 | 0.86 | −0.48 | **no** | yes |
| tetracene | 2.32 | 1.25 | +0.18 | yes | **no** |
| rubrene | 2.21 | 1.14 | +0.07 | yes | **no** |
| the preprint | 2.25 | 1.15 | +0.05 | yes | **no** |

Each of the three measured chromophores fails one of the two conditions, and so
do the preprint's own numbers. Pentacene, the one that fissions in 80 fs, has
triplets at 0.86 eV and cannot feed a 1.12 eV acceptor at all. Rubrene comes
closest and misses by 70 meV. Table 1's named donor, TIPS-tetracene, is a
tetracene: endothermic, picoseconds. The window is narrow rather than empty, and
nothing in the preprint is measured inside it.

**Layer 6 orders below the temperature the cell runs at.** The spin splitting
claimed for the altermagnetic collector is the published value (§1). What is not
stated is where it stops:

| | T (K) |
|---|---|
| MnTe Néel temperature, measured | **267 – 307** |
| standard test conditions | 298.15 |
| typical module NOCT | 318.15 |
| measured NOCT, thin-film module | 332.15 |
| IEC 61215 upper qualification | 358.15 |

A module in the field runs above MnTe's ordering temperature on both published
values. At the 332 K measured for a thin-film module under the IEC 61215 method
the collector is 25 to 65 K into its paramagnetic phase, where the spin
splitting layer 6 exists for is zero. Even standard test conditions sit at or
above the lower published value.

The alternative named first, RuO₂, has the opposite problem: its ordering
temperature is well above room temperature, but whether it is magnetically
ordered at all has been contested since 2024. Muon spin rotation and neutron
diffraction put the bulk moment below 1.4 × 10⁻⁴ µ_B/Ru, with the dissent coming
from thin films and surfaces — which is the form table 1 specifies, so for this
design the question is open rather than closed against it. Either way, the two
materials offered for layer 6 are the one whose magnetism is disputed and the one
that orders below the cell's operating temperature.

**Specific power is short by 3.4×.** Table 2 claims ≥ 10,000 W/kg. Table 1
gives every thickness except the back reflector's, which is swept over
100–200 nm, and the areal mass follows ([`materials.py`](materials.py)):

| layer | g/m² | share |
|---|---|---|
| 1 substrate, 50 µm PEN | 68.000 | 56.3 % |
| 7 encapsulation, 25 µm | 50.000 | 41.4 % |
| everything else | 2.84 | 2.3 % |
| **total** | **120.8** | |

At the claimed 35.6 % that is **2944 W/kg**, and across every corner of the
three swept assumptions 2815–3087 W/kg. The claim is short by a factor of
**3.4**. The 75 µm of polymer that does no physics is 97.7 % of the mass; the
functional stack is 2.84 g/m² and would on its own give over 100,000 W/kg.
Reaching 10,000 W/kg at the claimed efficiency means a total of 35.6 g/m², which
is about **19 µm** of packaging rather than 75 µm. The figure is reachable for a
free-standing ultrathin cell — which is where the 5,000–10,000 W/kg entries in
that column come from — but not for the stack in table 1.

**The high current tightens the series-resistance budget.** Holding the claimed
FF to within one point needs R_s below **0.155 Ω·cm²** at 52.3 mA/cm², against
0.189 Ω·cm² for the 42.8 mA/cm² silicon cell in the same table — 22 % tighter,
while adding a 1.5 nm chiral monolayer and a 1.2 nm MgO barrier in series that a
silicon cell does not have. Nothing here says that cannot be met; it is a
constraint the preprint does not state.

## 6. Form: this deposit against the series

Measured in [`census.py`](census.py), this is the first of the author's eighteen
Zenodo deposits that contains none of the vocabulary the other seventeen share:

| | count |
|---|---|
| tensor, Tensor Core | 0 |
| octonion, quaternion, sedenion, hypercomplex | 0 |
| non-associative, associator, zero divisor | 0 |
| causal, intensional | 0 |
| Maxwell | 0 |
| GPU, CUDA, RTX, clock cycle | 0 |
| Theory of Everything | 0 |
| Gemini | 0 |

Instead: spin 70, chiral 30, CISS 21, altermagnet 18, triplet 18, exciton 11,
singlet fission 10, Dexter 10, AM1.5G 9. The PDF header carries no unfilled
ORCID placeholder, which every earlier deposit does; no co-author is credited to
an AI; there are no self-citations; and all seven references are external, real,
and attached to claims they support — which, measured across the series in
[`reference-audit`](../reference-audit), is not the
usual case.

This is the most conventionally constructed deposit of the eighteen. Its central
error is of a different kind from the series' usual: not a claim with no source,
but a correctly cited source read off the wrong row.

## 7. The same quantity, twice

The findings in §§2–6 are of two kinds.  Some compare a claim with the outside
world: a spectrum, a measured chromophore, a Néel temperature, a column of the
periodic table.  Others never leave the document — a quantity is given one value
in one place and a different value in another, or a value is stated in a
sentence whose own other numbers imply a different one.
[`consistency.py`](consistency.py) collects the second kind, because it needs no
model to adjudicate and no source to trust: both values are the preprint's, and
so is the arithmetic between them.

| quantity | stated | implied by its own numbers | gap |
|---|---|---|---|
| absorption edge of the fission donor | 2.25 eV (551 nm), §2.2 | **1.96 eV (634 nm)**, from its own 23.8 mA/cm² at its own EQE_high, §6.2 | **294 meV** |
| E(S₁) of the donor | 2.25 eV, §2.2 | **at least 2.30 eV**, from E(S₁) ≥ 2E(T₁), §2.1 | 50 meV, 1.9 kT |
| electrons per absorbed photon | 1.53, written "153 %", §6.2 | **2.44**, from its own 23.8 mA/cm² over the 9.76 the spectrum carries above 2.25 eV | 59 %, and **22 % over fission's own ceiling of two** |
| τ_ext | 20–80 ns, §4.1 | **256 ns**, from its own η_PB = 0.95 through its own η_PB = exp(−τ_ext/τ_s) | ×3.2 to ×12.8 |
| η_PB | 0.95, §4.1 | **0.984–0.996**, from the two times in the same sentence | 2.5 points of suppression |
| carrier mobility | "low carrier mobilities", no number, §1 of the preprint | **3.8 × 10⁻³ to 1.5 × 10⁻² cm²/Vs**, from its own 20–80 ns through τ_ext = d²/(2μV) and table 1's 220 nm | one to two orders of magnitude |
| spin splitting the mechanism runs on | ~0.8 eV, table 1; 0.5–1.0 eV, §5.1 | **64.5 meV**, from its own P_CISS = 0.85 through its own P_CISS = tanh(ΔE/2kT) | **×12.4** |
| specific power | at least 10,000 W/kg, table 2 | **2944 W/kg**, from its own seven thicknesses at its own PCE | ×3.4 |

Two of the eight are in the preprint's favour, and are recorded for that reason
as §4 records them: either reading of the η_PB / τ_ext pair raises the
suppression the mechanism achieves.

Applying the same test to every other quantity the preprint states twice gives
the complement, which is worth as much as the table above:

| quantity | recomputed | as published |
|---|---|---|
| EQE_high = 1.85 × 0.92 × 0.90 | 1.5318 | 153 % (§6.2) |
| 1 − η_PB P_CISS² | 0.3136 | 0.314 (§4.1) |
| the suppression that follows | 68.6 % | 68.6 % (§4.1) |
| P_CISS of the worked example | 0.85 | inside 0.75–0.90 (§3.2) |
| splitting of table 1 | 0.8 eV | inside 0.5–1.0 eV (§5.1) |
| V_oc = 0.90 V − 0.09 V | 0.81 V | 0.81 V (§6.2) |
| PCE = J_sc V_oc FF / P_in | 35.58 % | 35.58 % (§6.2) |
| 2E(T₁) ≥ 2E_g(IR), the second link of the chain | 2.30 ≥ 2.24 eV | required by §2.2 |

Eight of eight. **Every arithmetic step the preprint performs, it performs
correctly.** Every formula is standard and correctly manipulated, every unit is
right, and the one product worked out in full — the PCE of §6.2 — is exact to
four digits.  What disagrees is never the algebra; it is always the numbers put
into it, and in six of the eight rows above the two numbers are in different
sections.  The document is locally sound and globally inconsistent.

**One row is an exclusion rather than an inconsistency.** The other seven could
each be repaired by choosing one of the two values and correcting the other.
The first cannot, because §2.2's own thermodynamic ordering

    E(S₁_D) ≥ 2E(T₁_D) ≥ 2E_CT ≥ 2E_g(IR)

fixes which of its two values is allowed.  2E_g(IR) = 2.24 eV, so the chain
forbids any donor whose S₁ lies below that, and the 1.96 eV edge its own
photocurrent needs is **284 meV below that floor**.  Read the other way, a donor
with E(S₁) = 1.96 eV may have E(T₁) at most 0.98 eV, which is 142 meV *below*
the 1.12 eV gap of the acceptor it is supposed to feed, so the Dexter step of
§2.2 would run uphill and the cascade would not exist.

Either the high-energy channel carries 14.95 mA/cm² and not 23.8, or the energy
cascade the whole architecture is built from is thermodynamically forbidden.
Nothing outside the preprint is needed to reach that.

## 8. What is not measured here

* The Dexter transfer rate. The expression in section 2.2 is the standard Dexter
  form; whether η_DET ≥ 0.90 is achievable at the required R_DA < 1 nm while
  keeping 5–10 nm donor domains, the competition section 7's Phase I identifies,
  is a morphology question and is not modelled.
* Whether CISS can polarise carriers without discarding the rejected spin
  population. Section 3.1 objects to electrode spin filters precisely because
  they reflect half the current; whether a bulk chiral interface avoids its own
  objection is a question about the mechanism, not a calculation, and is left
  open here. The same applies to spin conservation in the infrared channel,
  whose carriers come from singlet excitons and cannot form |↑↑⟩ pairs by the
  argument section 4.1 uses for the fission channel.
* The Thomas factor. The spin-orbit Hamiltonian in section 3.2 is written with
  a coefficient eℏ/2m²c²; the standard reduction of the Dirac equation gives
  eℏ/4m²c². This is a factor of two in a term whose magnitude is not used
  numerically anywhere in the preprint, so it changes nothing and is recorded
  only for completeness.
* The 1.2 nm MgO tunnel barrier, beyond the series-resistance budget in §5.
* Shunt resistance, trap densities and the low-irradiance regime of section 4.2.
* The sonoluminescence-style applications are absent from this deposit; unlike
  earlier ones it stays inside its field throughout.

## 9. Limits of this evaluation, and three errors found in it

The detailed-balance model is the standard one: radiative recombination only,
unity absorptivity above threshold, no series or shunt resistance, front-surface
emission with a perfect back reflector, and the quantum yield entering the
emission as well as the absorption. It therefore gives *ceilings*. That
strengthens the finding of §2, where a claim sits above the ceiling, and it
weakens nothing in §1, where the ceiling is reproduced against three published
values.

The three self-checks in §1 are in the repository for that reason, and they
earned their place: the first version of `detailed_balance.py` let the Bose
factor diverge when the chemical potential reached the photon energy, which
returned infinities and silently turned the efficiency scans into nonsense —
7 × 10¹² % at an "optimum" of 1.52 eV. The self-check table caught it on the
first run, because the Shockley-Queisser limit was not 33.7 %. The argument is
clipped to a small positive value now, and the reason is in a comment in the
code.

Two further errors in this evaluation, both caught by printed intermediate
values rather than by inspection:

* `materials.py` computed areal mass with a factor of 10³ where 1 g/cm³ over
  1 m of thickness needs 10⁶, giving a specific power of three million W/kg, a
  "shortfall factor 0.0" and a packaging budget of 10,588 µm. The layer-by-layer
  table is printed rather than only the total precisely so that this kind of
  error has somewhere to show up.
* `census.py` counted every numbered list in the body as a reference and
  reported 25 of them instead of 7. It now counts only after the last
  "References" heading.

A fourth change was not an error: the V_oc search was a scalar bisection and the
whole script took 2 min 21 s, which is replaced by three refinements of a
vectorised 64-point bracket and now takes 8 s. The numbers are unchanged.

The assumed values — mobility range, internal field, absorber volume fraction,
packaging densities, back-reflector thickness — are swept in
[`constants.py`](constants.py) rather than asserted, and every conclusion above
is stated across the whole of each range. The reference verdicts for the other
seventeen deposits are not repeated here; they live in
[`reference-audit`](../reference-audit).

---

*Code: MIT. This text: CC BY 4.0. Measurements by `karagos01`, 14 October 2026.*
