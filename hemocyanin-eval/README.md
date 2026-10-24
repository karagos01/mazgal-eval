# Copper-Based Hemocyanin Physiology in Hominids — independent evaluation

Reproducible evaluation of M. Mazgal, *Theoretical Framework for Copper-Based
Hemocyanin Physiology in Hominids* (Zenodo, 7 October 2026, DOI
[10.5281/zenodo.23209266](https://doi.org/10.5281/zenodo.23209266)).

The write-up is in [`PAPER.md`](PAPER.md), in Czech in [`PAPER.cs.md`](PAPER.cs.md).

**The number that decides it is in neither the preprint nor any of its five
references**, so it was obtained independently. Human arterial blood carries
about **20 vol%** oxygen; hemocyanin carries 1.37–3.44 vol% in measured species
and "never exceeds 4.5 vols%" in cephalopods — **4.4 to 14.6 times less**. And
it cannot be concentrated to close the gap, for the reason given by a co-author
of the paper the preprint's first citation garbles: dissolved in haemolymph at
transport-sufficient concentration it "will yield an unbearably high osmotic
pressure".

The consequence is arithmetic. A 70 kg adult at rest needs 245 mL O₂/min, which
at 4–6 L/min of cardiac output means a 4.1–6.1 vol% arteriovenous difference —
reproducing the ~5 vol% actually measured, so the calculation is calibrated.
With hemocyanin at the published ceiling and a generous 75 % extraction the same
person needs **7.3 L/min at rest**, and at a measured *Octopus vulgaris*
capacity **24–72 L/min**, against a maximal human cardiac output of about
20–25 L/min. **The proposal fails sitting still.**

The genetic route fails on a precondition: an epigenetic switch turns an
existing gene on, and **vertebrates have no hemocyanin gene** — InterPro
IPR013788 returns nothing in Vertebrata or Chordata.

One finding goes the other way and §6 of the write-up gives it prominently.
**A pigment-class switch really has happened** — Planorbid snails replaced
ancestral hemocyanin with haemoglobin. The preprint does not cite it, it runs
the opposite way, and the published reason is "possibly to replace a
less-efficient hemocyanin".

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network. The deposit reports no measured quantity of any kind, so
every value here is either verified from the literature or an assumed range that
is swept.

## Reproducing the results

```
./run_all.sh          # everything, about 1 second on any CPU
```

| Script | What it computes | Section |
|---|---|---|
| [`oxygen.py`](oxygen.py) | oxygen-carrying capacity against human blood; what a resting human metabolism requires of the circulation; the same requirement met with hemocyanin at swept extraction; exertion; why squid are not a counterexample; protein mass per O₂ | §§2–4 |
| [`genetics.py`](genetics.py) | whether there is a gene to switch on; how the preprint uses "epigenetic"; the ceruloplasmin bridge against its own cited abstract; copper's own redox toxicity; the one real pigment-switch precedent | §§5–6 |

`genetics.py` is a record of database results and quotations rather than a
computation, kept as a script so that it appears in `results.log` beside the
arithmetic. Every value is in [`constants.py`](constants.py) with a **provenance
tag** — `[P]` from the preprint, `[V]` verified against a named source, `[A]` an
assumed range that is swept rather than asserted. Full output of one run:
[`results.log`](results.log).

## Key numbers

| what | published | measured / computed |
|---|---|---|
| oxygen capacity of the proposed pigment | "highly efficient and thermodynamically stable" | **4.4–14.6× below human blood** |
| human arterial blood | — | 20.00 vol% |
| *Cancer magister* / *O. dofleini* / *Nautilus* / *O. vulgaris* | — | 3.44 / 3.06 / 2.30 / 1.37 vol% |
| cephalopod ceiling | — | "never exceeds **4.5 vols%**" |
| why it cannot be concentrated | — | "unbearably high osmotic pressure" — from the preprint's own garbled citation |
| resting oxygen consumption, 70 kg | not given | 245 mL O₂/min (1 MET) |
| a-v difference that requires | not given | **4.1–6.1 vol%** — reproduces the ~5 measured |
| cardiac output needed, hemocyanin at the ceiling, 75 % extraction | not given | **7.3 L/min at rest** |
| same at measured *O. vulgaris* capacity | not given | **24–72 L/min** vs ~20–25 maximal |
| same at 8× and 20× resting metabolism | "thermoregulatory independence" | 58 and **145 L/min** |
| what limits squid, the best counterexample | — | "not oxygen uptake, but **oxygen transport in the blood**" |
| hemocyanin genes in Vertebrata / Chordata | "latent genes" | **0 / 0** |
| human tyrosinase-domain genes | — | TYR, TYRP1, DCT; TYRP1's active site holds **zinc** |
| ceruloplasmin | "fundamental human protein for copper transport" | a **ferroxidase**; "plays no essential role in the transport or metabolism of this metal" |
| ceruloplasmin ∩ hemocyanin domains | "structurally related" | **empty** — cupredoxin fold vs tyrosinase binuclear type-3 |
| copper's redox behaviour, per the preprint's own ref. | "absence of the Fenton reaction" | "generation of superoxide and **hydroxyl radicals**" |
| "epigenetic" in the preprint | the mechanism of the whole switch | **8 occurrences**; methylation, histone, chromatin: **0 each** |
| "epigenet" in the reference glossed for epigenetic adaptation | — | **0** |
| measured quantities reported anywhere in the preprint | — | **0** |
| the real pigment-switch precedent | not cited | hemocyanin → haemoglobin, "possibly to replace a less-efficient hemocyanin"; "Once lost, hemocyanin was not regained" |

## Scope

The deposit is a short preprint under CC BY 4.0 with no code, no measurements
and no figures. §7 of the write-up sets out what is not measured here — the
claims about centuries-long lifespans, a superconducting nervous system and a
biological quantum computer — and says why, rather than treating them as
defects. It also records that this deposit and its predecessor are the two
places in this author's seventeen where the proposal is an intervention on
people.

§8 sets out the limits. The extraction fraction is the softest assumption and is
swept to 75 %, which is well above the human resting figure, so the calculation
is already generous to the proposal and still fails at rest. A negative database
result is weaker than a proof of absence and the claim is scoped to what the
annotation shows.

All five references were read for content in
[`reference-audit`](https://github.com/karagos01/reference-audit), which holds
the verbatim evidence; §§5–6 summarise and do not duplicate it.

## Companion evaluations

- [`reference-audit`](https://github.com/karagos01/reference-audit) — whether all 81 citations in all 18 deposits say what they are cited for
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — the quantum biofortification and in-situ phytomining matrix of October 2026, which this deposit self-cites
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — the dual-scale waveform and HFRS charging proposal of October 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL tensor matrix architecture of October 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing and openQL v1.1 of October 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — the openOmega matter-antimatter and sedenion proposal of October 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — the HOS-PV 2.0 singlet-fission and spintronic photovoltaic proposal of October 2026

## Licence

Code (all `*.py` and `run_all.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
