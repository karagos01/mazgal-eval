# The note B, divided by four: an evaluation of *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation*

karagos01, October 2026

## Abstract

M. Mazgal's *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation* (Zenodo,
5 October 2026) proposes a cylindrical photobioreactor that delivers 4500 W/m² in
50 µs pulses with a 4000 µs dark phase, synchronised to a 246.91 Hz acoustic wave
that is to hold stomata open, and then proposes to reproduce the acoustic half of
that at field scale by retuning the noise of wind turbines and high-voltage
transformers to 61.72 Hz through SCADA firmware. This is the first of the author's
eleven deposits with no hypercomplex algebra in it, and the first whose references
are almost all real and correctly cited.

The pulsed-light physics is sound in outline and the 4 ms dark interval is the
right order of magnitude for what the design needs. Everything above it is
measured here to fail, and to fail on arithmetic rather than on biology.

Both published frequencies are equal-tempered pitches: 246.91 Hz is B3 to within
0.22 cents and 61.72 Hz is B1 to within 0.43 cents, below the threshold at which a
trained listener can hear a difference. The optical period 50 µs + 4000 µs is
4.050 ms, which is 246.91 Hz — so the timing said to follow from Calvin-cycle
kinetics and the frequency said to follow from guard-cell mechanics are one number,
and that number is the note B. The division by four is justified as landing inside
the "empirically proven PAFT sensitive band"; measured against the band of the
review cited for it, 0.1–1 kHz, the division moves the frequency out of that band,
which 246.91 Hz was already inside.

At 1.2346 % duty the time-averaged irradiance is 55.6 W/m² = 256 µmol/m²/s, which
is 1.57× below the light-saturation point of lettuce and 5.5× below that of wheat —
so non-photochemical quenching, the loss the design exists to bypass, is barely
engaged in the regime the design creates. Dry matter per kilowatt-hour is invariant
under pulsing to 3.6·10⁻¹⁵ over an 81-fold range of duty cycle, because pulsing
divides the yield and the energy by the same factor; the claim to "redefine the
gram-per-watt limit of CEA" is a claim about the one quantity the scheme cannot
move. The 4 ms interval matches plastoquinol reoxidation at cytochrome *b₆f*
(2–20 ms), not the Calvin cycle it is attributed to (250–500 ms, 62–125× slower).

The field-scale half is further out. The blade-pass frequency of a three-bladed
turbine at 14 rpm is 0.700 Hz; 61.72 Hz would need 1234 rpm, Mach 18.8 at the blade
tip and 85 000 g of centripetal acceleration, and the paper proposes to reach it by
*braking*. Even granting the tone, the turbine's entire declared sound power of
105 dB re 1 pW falls 22.5 dB — a factor of 179 in power — short of the 70 dB at the
plant that the cited review's generators deliver from 30–60 m, rising to 33 dB at
1 km; and the loss is geometric spreading, not the atmospheric absorption the
frequency was chosen to minimise. As a phased array a wind farm has its elements
90–180 wavelengths apart where λ/2 is required. A transformer core locked to a
50 Hz grid emits lines at integer multiples of 50 Hz, and 61.72 Hz is not one of
them, so no firmware setting can place energy there; "asymmetric DC injection" is
half-cycle saturation, a damage mechanism. Finally, suppressing the midday stomatal
depression multiplies leaf transpiration by exactly 3.0× independent of vapour
pressure deficit, and costs 1.3–2.5× more water per unit carbon for every
saturating assimilation response — a cost the preprint states itself, for open
fields of winter wheat, sugar beet and potatoes.

Everything here is computed by four scripts with no network access and no GPU.
Every external constant is in `constants.py` with its source.

## 1. What is correct

More than in any previous deposit by this author, and it is worth being specific.

**There are no octonions and no Maxwell.** The pattern documented across the other
ten deposits — a correct algebraic fact with a theorem-excluded one attached, and a
historical attribution to Maxwell that appears exactly where octonions do — is
absent. Counted over the extracted text, "Maxwell" occurs 0 times, "octonion" 0,
"quaternion" 0, "hypercomplex" 0, "non-associative" 0, "tensor" 0 and "causal" 0.
The whole vocabulary is absent, not relabelled. Whatever else is wrong here is
wrong in a normal way.

> **Correction, 9 October 2026.** This section first said that "causal" was at zero
> here "for the first time in eleven deposits". That was wrong twice over, and a
> census run over all sixteen records in the companion
> [`reference-audit`](https://github.com/karagos01/reference-audit) repository is
> what caught it.
>
> "causal" was already 0 in openQL / openOL v1.0 of 3 October, two days before
> this deposit. And all seven of the terms counted above are 0 in **COBAR**
> (23 September) and in the **Topological Momentum Drive** (24 September), both of
> which make engineering claims — so this deposit is neither the first with
> "causal" at zero nor the first without the hypercomplex vocabulary.
>
> The correct reading is not a development over time but two interleaved groups.
> Six of the sixteen records carry none of these terms — COBAR, Momentum Drive,
> this one, Phytomining, Na-ion HFRS and Hemocyanin — while the other ten carry
> them heavily, and the two groups alternate rather than succeed one another. The
> counts for this deposit are unchanged; what was wrong was the claim to priority
> built on them, and it was an artefact of comparing against ten deposits instead
> of all of them.

**The bibliography is real.** Four of the five references resolve exactly as
printed: Müller, Li & Niyogi 2001 in *Plant Physiology* 125(4) 1558–1566; Hassanien,
Hou, Li & Li 2014 in the *Journal of Integrative Agriculture* 13(2) 335–348;
Oerlemans, Sijtsma & Méndez López 2007 in the *Journal of Sound and Vibration*
299(4–5) 869–883; Farquhar & Sharkey 1982 in the *Annual Review of Plant
Physiology* 33 317–345. All four are the right source for the claim they are
attached to. The fifth is discussed in §10.

**Pulsed light can genuinely bypass NPQ.** This is not fringe. Energy-dependent
quenching (qE) is induced over seconds to minutes via lumenal acidification; a
50 µs pulse is far too short for it to develop, so a train of microsecond pulses
really can deliver photons at an instantaneous rate that would trigger quenching
under continuous light without triggering it. The mechanism named in §1 of the
preprint — plastoquinone pool oversaturation — is also the right mechanism to
relieve.

**The 4 ms dark interval is a well-chosen number.** It is the right order for the
pool to reoxidise (§5). The justification given for it is wrong, but the number is
not.

**Low frequencies do propagate with little absorption.** §3 says the 61.72 Hz
subharmonic "experiences minimal atmospheric attenuation over long distances". At
63 Hz, ISO 9613-1 gives about 0.1 dB/km. That is correct.

**Sound does affect stomata.** PAFT is a real if contested literature, the cited
review is a reasonable entry point into it, and the reported yield gains there
(5.7 % for rice to 37.1 % for cucumber) bracket the 15–18 % the preprint claims.

**The micro-scale hardware is ordinary and buildable.** An STM32 driving GaN
half-bridges and an I²S audio chain, with capacitor banks for a 1.2 % duty peak, is
a normal embedded design. At 4500 W/m² peak and 1.2346 % duty the average optical
load is 55.6 W/m², so about 111 W/m² electrical at 50 % wall-plug efficiency —
undemanding. Nothing in the bioreactor is hard to build.

What follows is where the measurements disagree with the paper.

## 2. Both published frequencies are the note B

Two frequencies carry the design: 246.91 Hz in the reactor (§2.3) and 61.72 Hz in
the field (§3). The first is said to have been "synthesized to maximize localized
guard cell vibration"; the second to have been "calculated" as the fourth
subharmonic.

`frequency.py` compares each to the equal-tempered chromatic scale on A4 = 440 Hz:

| published | nearest 12-TET pitch | exact | error | cents |
|---|---|---|---|---|
| 246.910 Hz, §2.3 reactor | **B3** | 246.942 Hz | −0.032 Hz | **−0.22** |
| 61.720 Hz, §3 field | **B1** | 61.735 Hz | −0.015 Hz | **−0.43** |

A cent is a hundredth of a semitone, and the smallest pitch difference a trained
listener can resolve is around 5 cents. Both numbers are the note B as a guitar
tuner would set it, to within a fifth of the limit of human pitch discrimination.
That the field frequency is two octaves below the reactor frequency is not an
independent fact: B1 is B3 divided by four by construction.

Then the optical timing:

| | |
|---|---|
| pulse, §2.2 | 50 µs |
| dark phase, §2.2 | 4000 µs |
| period | 4.050 ms |
| repetition rate | **246.91 Hz** |
| cymatic frequency, §2.3 | **246.91 Hz** |
| difference | 3.6·10⁻³ Hz, 1.5·10⁻⁵ relative |

§2.2 derives the optical gating from "the enzymatic turnover rate of the Calvin
cycle". §2.3 derives the acoustic frequency from guard-cell mechanics. They agree
to one part in 10⁵, which is the rounding of 246.91 Hz to two decimals. They are
not two parameters that happen to be commensurate; they are one parameter stated
twice with two different derivations, and §2.3's "synchronizes the acoustic pressure
waves with the optical pulses at a microsecond resolution" is then trivially
satisfiable because there is nothing to synchronise.

This matters beyond tidiness. If the optical period were set by electron-transport
kinetics it would be a biological quantity with a defensible value. If it is set by
a musical pitch, then the one number that the whole micro-scale design rests on has
no biological derivation at all, and the agreement in §2.3 is an artefact of
choosing the same note twice.

## 3. The cited band excludes the frequency derived to fit it

§3 states that plant mechanoreceptors respond to low-frequency vibration "typically
between 50 and 120 Hz", and divides 246.91 Hz by four so that the result "falls
perfectly within the empirically proven PAFT sensitive band".

The review cited for PAFT is Hassanien et al. 2014. The band in that work is
**0.1–1 kHz**, at **70 ± 5 dB** SPL, delivered from 30–60 m by a dedicated
generator.

| frequency | inside the preprint's 50–120 Hz | inside the cited 100–1000 Hz |
|---|---|---|
| 246.91 Hz, reactor | no | **yes** |
| 61.72 Hz, field | yes | **no** |

So the derivation runs backwards. The reactor frequency was already inside the band
the cited review supports; dividing by four takes it out. The band stated in §3 is
not the band of the source §3 relies on, and the division is justified by the
mismatch.

Nothing here says 61.72 Hz cannot work — only that the paper's own citation does
not support it, and that the stated reason for choosing it is the opposite of what
the citation says.

## 4. The duty cycle puts the average below the regime the design targets

§2.2 replaces continuous light with "extreme-intensity photon bursts (4500 W/m²)"
of 50 µs followed by 4000 µs of darkness, and claims this "completely bypass[es]
the NPQ trigger". §2.1 adds that the cylindrical geometry lets "photon capture
efficiency approach the theoretical maximum of 100%".

`light.py` computes what that delivers:

| | |
|---|---|
| duty cycle | **1.2346 %** (1 : 81.0) |
| peak irradiance | 4500 W/m² = 20 700 µmol/m²/s = **10.35× full sun** |
| time-averaged irradiance | **55.6 W/m² = 256 µmol/m²/s = 0.13× full sun** |

at 4.6 µmol/J, the standard PAR conversion. If the 4500 W/m² is total rather than
PAR irradiance, the photon flux is lower still; this takes the figure at its most
favourable.

Carbon fixed over a day is set by the average flux, not the peak: the pulse lasts
50 µs and carboxylation integrates over hundreds of milliseconds. And the average
produced here is below light saturation for every C3 crop:

| | µmol/m²/s | ratio to the average delivered |
|---|---|---|
| light saturation, lettuce | 400 | 1.57× above |
| light saturation, wheat | 1400 | 5.48× above |
| **this scheme, averaged** | **256** | — |

This inverts the argument. NPQ is a saturation-regime loss: it exists because
absorbed photons exceed what carboxylation can consume. At 256 µmol/m²/s a plant
under *continuous* light of the same average intensity is not light-saturated
either, and so engages little quenching. The mechanism the design is built to
bypass is not strongly active in the regime the design creates. §1 compares against
"continuous high-intensity irradiation", which this scheme does not deliver on
average — it delivers 13 % of full sun.

And even where NPQ is fully engaged, the gain is bounded by a number the preprint
supplies itself: §1 puts the loss at "up to 60% of absorbed photons", so recovering
all of it is a factor of 1/(1−0.6) = **2.50×**. Bounded, and far from "redefining"
a limit.

On the 100 % photon capture claim: PAR absorptance of a single green leaf is
0.84–0.90, so one pass cannot exceed that. A closed reflective enclosure can do
better by multiple passes, so 100 % is not excluded outright — but the ceiling is
then set by the reflectance of the enclosure wall, which is where the LEDs are, and
no reflectance is given. This is recorded as an unquantified claim, not a defect.

## 5. The 4 ms dark interval matches a different mechanism than the one named

§2.2: "The burst duration is tightly constrained to 50 µs, followed by a 4000 µs
dark phase. This temporal gating perfectly matches the enzymatic turnover rate of
the Calvin cycle, preventing PQ pool saturation."

| process | timescale | source |
|---|---|---|
| dark phase, §2.2 | **4.00 ms** | the preprint |
| RuBisCO turnover, 1/k_cat at k_cat = 2–4 s⁻¹ | **250–500 ms** | von Caemmerer 2000 |
| plastoquinol oxidation at cytochrome *b₆f* | **2–20 ms** | Haehnel 1984 |

The Calvin cycle is **62–125× slower** than the interval chosen. The interval is,
however, the right order for reoxidation of the plastoquinone pool — which is
precisely what §1 identifies as the thing that must be relieved, and what the
second half of the same sentence says the gating achieves.

So the engineering is right and the citation inside the sentence is wrong. This is a
smaller defect than the others and would be a copy-edit in a journal, but it is
worth separating from §4: the dark interval is defensible, the average flux it
produces is not.

## 6. Grams per kilowatt-hour is invariant under pulsing

§5: "the cybernetic bioreactor achieves conversion ratios that redefine the
gram-per-watt limit of CEA". That figure of merit is dry matter per unit electrical
energy, and `light.py` shows the design cannot move it.

| scheme | g/m²/day | W/m² | **g/kWh** |
|---|---|---|---|
| pulsed, 1.23 % duty, NPQ fully bypassed | 33.1 | 111.1 | **12.42** |
| continuous at the same average flux, no NPQ | 33.1 | 111.1 | **12.42** |
| the same, if NPQ cost the published 60 % here | 13.2 | 111.1 | 4.97 |
| continuous at full sun, NPQ at the published 60 % | 103.7 | 869.6 | 4.97 |

Rows 1 and 2 are identical, and they are identical structurally rather than
numerically: pulsing divides the dry matter and the electrical input by the same
duty cycle, so their ratio is fixed. Sweeping the duty cycle over its whole range
at constant peak confirms it:

| duty % | avg µmol/m²/s | g/m²/day | W/m² | g/kWh |
|---|---|---|---|---|
| 1.235 | 256 | 33.1 | 111.1 | 12.42 |
| 5.000 | 1035 | 134.1 | 450.0 | 12.42 |
| 10.000 | 2070 | 268.3 | 900.0 | 12.42 (*) |
| 25.000 | 5175 | 670.7 | 2250.0 | 12.42 (*) |
| 100.000 | 20700 | 2682.7 | 9000.0 | 12.42 (*) |

(*) past light saturation, where the linear quantum-yield model overstates the
yield — so the real g/kWh there would fall, never rise. The spread across an
81-fold range of duty cycle is **3.6·10⁻¹⁵**, i.e. floating point.

Yield per unit area rises with duty cycle. Yield per unit *energy* does not change
at all. The only lever on it in this model is the quantum yield, which scales
g/kWh exactly linearly (0.02 → 4.97, 0.04 → 9.94, 0.08 → 19.87 g/kWh), and the
most that bypassing NPQ can contribute to that is the 2.50× ceiling of §4 — in a
regime where, as measured, NPQ is barely engaged.

The absolute figure, 12.42 g dry matter per kWh under assumptions chosen to favour
the design, lands inside the 5–10 g/kWh range where commercial vertical farming
already operates. There is nothing to redefine, and pulsing is the wrong lever for
the quantity named.

This is the same shape of defect as the roofline result in the companion evaluation
of *openQL / openOL*: a restructuring that multiplies a cost and leaves the ratio
it is advertised to improve exactly where it was.

## 7. A wind turbine cannot emit 61.72 Hz, and could not be heard if it did

§4.1 proposes turning turbines into "phased acoustic arrays" by SCADA changes:
"Pitch Tuning" to shift "the blade-pass frequency noise to the target subharmonic",
and "RPM Lock: Electromagnetically braking the rotor via the grid inverter forces
the turbine to maintain exact rotational speeds irrespective of wind gusts, ensuring
a phase-stable 61.72 Hz emission."

**The frequency.** Blade-pass frequency is blades × rpm / 60:

| rotor rpm | blade-pass frequency | 61.72 Hz as a harmonic of it |
|---|---|---|
| 9.0 | 0.450 Hz | 137th |
| 14.0 (rated) | **0.700 Hz** | **88th** |
| 18.0 | 0.900 Hz | 69th |

To put the blade pass itself at 61.72 Hz the rotor must turn at **1234.4 rpm**,
88× rated:

| blade radius | tip speed | Mach | tip acceleration |
|---|---|---|---|
| 40 m | 5171 m/s | 15.1 | 68 133 g |
| 50 m | **6463 m/s** | **18.8** | **85 167 g** |
| 60 m | 7756 m/s | 22.6 | 102 200 g |

The sentence asks for this by *braking*, which cannot raise a rotor speed. Taken
instead as the 88th harmonic of the blade pass, there is no mechanism offered to put
energy there; and "Pitch Tuning: Dynamically adjusting the blade pitch by a fraction
of a degree induces controlled boundary-layer separation (micro-stall)" describes
broadband stall noise, which has no line structure to place at a chosen frequency.

**The level.** The cited review's PAFT generators deliver 70 ± 5 dB SPL at the plant
from 30–60 m. A 2–3 MW turbine's declared apparent sound power is 100–110 dB re
1 pW — 31.6 mW of acoustic power at 105 dB, broadband. Under hemispherical
spreading over a reflecting ground plane:

| distance | turbine SPL | L_w needed for 70 dB | shortfall | in power |
|---|---|---|---|---|
| 100 m | 57.0 dB | 118.0 dB | 13.0 dB | 20× |
| 300 m | 47.5 dB | 127.5 dB | **22.5 dB** | **179×** |
| 500 m | 43.0 dB | 132.0 dB | 27.0 dB | 497× |
| 1000 m | 37.0 dB | 138.0 dB | **33.0 dB** | **1987×** |

The model gives 47.5 dB at 300 m, against the 40–45 dB(A) typically measured at
that distance from a turbine of this class, so it is calibrated and if anything
generous to the proposal. Varying the declared sound power across the whole class changes
the 300 m shortfall from 17.5 dB (57×) at 110 dB re 1 pW to 27.5 dB (565×) at
100 dB. The conclusion does not depend on the choice.

And this compares the turbine's **entire broadband output** against a requirement in
one narrow band, so the real shortfall is larger than the table says.

**The loss mechanism is the wrong one.** §3 chose the low frequency partly because
it "experiences minimal atmospheric attenuation over long distances", which is
correct: about 0.1 dB/km at 63 Hz. But from 60 m to 1 km geometric spreading costs
24 dB and absorption costs 0.1 dB. The frequency choice optimises the term that
contributes a quarter of one percent of the loss.

**The array.** At 61.72 Hz, λ = 5.56 m, so grating-lobe-free beam forming needs
elements within 2.78 m of each other. Wind-farm spacing is 5–10 rotor diameters:

| spacing | distance | in wavelengths | versus λ/2 |
|---|---|---|---|
| 5 D | 500 m | 90.0 | 180× too far |
| 10 D | 1000 m | 179.9 | 360× too far |

Separately, holding a phase error below λ/10 across such an array requires the
blade-pass timing to be stable to 1.62 ms. One revolution at 14 rpm takes 4.29 s, so
that is **0.136° of rotor angle**, held against gusts, simultaneously on every
turbine in the farm. "Irrespective of wind gusts" is the hard part of the sentence,
not the easy one.

## 8. A grid-locked transformer core has no 61.72 Hz line

§4.2: "High-voltage transformers naturally emit magnetostriction hum. Through
asymmetric DC injection or smart-grid inverter modulation, this hum can be tuned to
precisely 61.72 Hz, turning substations into stationary acoustic stimulators."

Magnetostrictive strain depends on |B|, so a core on a 50 Hz line is excited at
twice the line frequency and its harmonics: 100, 200, 300, 400 Hz. A DC bias
saturates alternate half cycles and adds the odd lines: 50, 150, 250 Hz. Every line
a grid-locked core can emit is an integer multiple of **50 Hz**.

| | |
|---|---|
| line frequency | 50.00 Hz, ± 0.05 Hz (ENTSO-E continental area) |
| target | **61.72 Hz** = 1.2344 × f_line |
| nearest available line | 50.00 Hz, off by **11.72 Hz** |

61.72 Hz is not a harmonic, a subharmonic or an intermodulation product of 50 Hz.
No firmware setting creates a spectral line at a frequency the excitation does not
contain; producing one requires an independent source at that frequency, which is a
loudspeaker and not "smart-grid inverter modulation". The word "precisely" in the
quoted sentence is doing the opposite of the work it looks like it is doing: it is
precision about a frequency the mechanism cannot reach at all.

Separately, "asymmetric DC injection" is half-cycle saturation — the
geomagnetically-induced-current failure mode, which raises magnetizing current,
losses, hot-spot temperature and audible noise. Grid codes limit injected DC to
around 1 A for that reason. It is a damage mechanism, not a tuning control, and
proposing it for substations on the public network is a proposal to degrade grid
assets.

## 9. The hydrological sign

§5 is candid about direction: "Because the acoustic stimulation artificially
maintains stomatal aperture, evapotranspiration rates will rise. Therefore,
large-scale deployment must be paired with continuous soil moisture monitoring and
sufficient irrigation buffers."

`water.py` puts a size on it. Leaf transpiration is E = g_s · VPD / P:

| state | g_s mol/m²/s | VPD kPa | E mmol/m²/s |
|---|---|---|---|
| morning, stomata open | 0.30 | 1.0 | 2.96 |
| midday, natural depression | 0.10 | 3.0 | **2.96** |
| midday, held open as proposed | 0.30 | 3.0 | **8.88** |

The depression almost exactly cancels the rise in vapour pressure deficit — that is
what the response is for. Suppressing it multiplies midday transpiration by
**3.0×**, and the factor is g_s(held)/g_s(depressed), independent of VPD, so it
survives any choice of the midday value (2.0 to 5.0 kPa all give 3.0×).

Assimilation also rises, but it saturates in stomatal conductance while
transpiration stays linear in it, so water per unit carbon rises for every
saturating response shape:

| half-saturation K | assimilation gain | water per unit carbon |
|---|---|---|
| 0.03 | 1.18× | **2.54×** |
| 0.10 | 1.50× | **2.00×** |
| 0.50 | 2.25× | 1.33× |
| linear (no saturation) | 3.00× | 1.00× |

Only an exactly linear response breaks even, and assimilation is not linear in
conductance. K is a chosen shape parameter here, not a measured constant; the point
is that the sign does not depend on it.

§1 of the preprint states the biology correctly: midday closure, "while this
prevents lethal dehydration, abruptly halts CO₂ assimilation". The proposal is then
to defeat that mechanism across open fields of winter wheat, sugar beet and
potatoes — the crops and the latitude where soil water, not light, is the binding
constraint, and in the hours when it binds hardest. The irrigation buffer is not a
deployment detail; it is the proposal.

The claimed 15–18 % biomass increase is asserted with no derivation and no link to
a dose, a duration, a frequency or a crop. The range is plausible *for the exposure
in the cited review* — and that exposure is what §7 shows is not available.

## 10. References and presentation

Four of the five references resolve exactly as printed and are the right source for
their claim (§1). The fifth does not:

> Meng, Q. W., et al. (2012). Plant acoustics: sound-induced stomatal opening and
> the underlying mechanotransduction pathway. *Acoustics Research*, 18(1), 45-53.

No article with that title could be located, and no journal under that name appears
in the indexes searched. Work by Meng and colleagues from 2012 on plant acoustic
frequency technology does exist and is cited in the PAFT literature, but in *Hubei
Agricultural Sciences*. The author and year appear to be real and the title,
journal, volume and pages not. This is the reference that is load-bearing for the
only quantitative biological claim in §3 — the mechanoreceptor band — which is also
the claim §3 states at variance with the review it does cite correctly (§3 above).

On presentation: the Zenodo record carries the author's real ORCID,
0009-0000-6842-2187. The deposit is a four-page preprint under CC BY 4.0 with no
accompanying code, no measurements and no figures; §6 states that hardware topology,
STM32 firmware and CAD models "will be maintained in an open-source GitHub
repository associated with this publication", and no repository is named or linked.

## 11. Limitations

This is arithmetic on published parameters, not an experiment. Specifically:

- **No plants were grown.** §§4–6 and 9 are a radiation and gas-exchange budget with
  standard constants, not a measurement of yield. A real bioreactor could differ
  from the budget in either direction; what the budget constrains is the ratio in
  §6, which is structural.
- **The quantum yield 0.05 mol CO₂/mol photons and the LED wall-plug efficiency
  0.50 are assumptions.** §6 shows the invariance does not depend on either, and the
  absolute g/kWh figure does; it is stated as one figure under stated assumptions.
- **The acoustic model is hemispherical spreading over a reflecting plane** with no
  ground effect, atmospheric refraction, wind shear or turbine directivity. It
  gives 47.5 dB at 300 m against 40–45 dB(A) measured, and the shortfalls are
  13–33 dB, far outside what those refinements move.
- **The transformer argument is spectral, not experimental.** It says a grid-locked
  excitation has no 61.72 Hz component, not that a substation cannot be made to emit
  61.72 Hz by other means.
- **61.72 Hz is not claimed to be biologically ineffective.** §3 of this write-up
  shows the preprint's own citation does not support it; that is a different claim
  from showing the frequency does not work.
- **The pitch coincidence in §2 is a fact about the numbers, not about the author's
  intent.** What it establishes is that the one parameter the micro-scale design
  rests on has no biological derivation in the paper, not why.
- **Reference checking is negative evidence.** §10 reports that an article could not
  be located, which is weaker than showing it does not exist.

## 12. Data and code availability

Everything in this write-up is produced by `frequency.py`, `light.py`,
`acoustics.py` and `water.py` in this repository; `./run_all.sh` reproduces all of
it in about two seconds on any CPU, with no network access and no GPU. Every
external constant, with its source, is in `constants.py`, and no script defines a
physical constant of its own. The full output of one run is in `results.log`.

The evaluated preprint is open access at
[10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927) under CC BY 4.0
and is not reproduced here.

## References

1. M. Mazgal, *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation:
   Scaling from Cybernetic Bioreactors to Industrial-Scale Acoustic Modulation*,
   Zenodo, 5 October 2026. DOI
   [10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927).
2. R. H. Hassanien, T. Z. Hou, Y. F. Li, B. M. Li, *Advances in Effects of Sound
   Waves on Plants*, Journal of Integrative Agriculture **13**(2) (2014) 335–348.
3. P. Müller, X.-P. Li, K. K. Niyogi, *Non-photochemical quenching. A response to
   excess light energy*, Plant Physiology **125**(4) (2001) 1558–1566.
4. G. D. Farquhar, T. D. Sharkey, *Stomatal conductance and photosynthesis*, Annual
   Review of Plant Physiology **33** (1982) 317–345.
5. S. Oerlemans, P. Sijtsma, B. Méndez López, *Location and quantification of noise
   sources on a wind turbine*, Journal of Sound and Vibration **299**(4–5) (2007)
   869–883.
6. K. J. McCree, *The action spectrum, absorptance and quantum yield of
   photosynthesis in crop plants*, Agricultural Meteorology **9** (1971) 191–216.
7. W. Haehnel, *Photosynthetic electron transport in higher plants*, Annual Review
   of Plant Physiology **35** (1984) 659–693.
8. S. von Caemmerer, *Biochemical Models of Leaf Photosynthesis*, CSIRO Publishing,
   2000.
9. ISO 9613-1:1993, *Acoustics — Attenuation of sound during propagation outdoors —
   Part 1: Calculation of the absorption of sound by the atmosphere*.
10. IEC 61400-11, *Wind turbines — Part 11: Acoustic noise measurement techniques*.
11. Companion evaluations of the same author's other deposits:
    [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval),
    [`xternary-eval`](https://github.com/karagos01/xternary-eval),
    [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval),
    [`openql-eval`](https://github.com/karagos01/openql-eval).
