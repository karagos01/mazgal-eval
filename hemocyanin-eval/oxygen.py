#!/usr/bin/env python3
"""The number the preprint does not give, and what it decides.

The proposal is that humans carry copper-based hemocyanin in place of
iron-based haemoglobin.  Whether that can work is settled by one quantity --
how much oxygen a given volume of the fluid carries -- and neither the preprint
nor any of its five references states it.  So it was obtained independently and
the consequence is computed here.

The test is not whether hemocyanin is a worse pigment in the abstract.  It is
whether a circulation carrying hemocyanin can deliver a human resting metabolic
rate at all.
"""
from constants import (BODY_MASS_KG, CARDIAC_OUTPUT_REST_L_MIN,
                       HB_HUMAN_VOL_PCT, HB_TETRAMER_KDA,
                       HCY_CEPHALOPOD_CEILING, HCY_PER_O2_KDA,
                       HCY_SPECIES_VOL_PCT, O2_EXTRACTION_FRACTION,
                       OSMOTIC_QUOTE, SQUID_CONSTRAINT_QUOTE,
                       VO2_MAX_MULTIPLE, VO2_REST_ML_MIN,
                       VO2_REST_ML_PER_KG_MIN, required_avo2_vol_pct,
                       tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()
P("      The preprint reports no measured quantity of any kind, so every")
P("      number below is either [V] from the literature or [A] and swept.")
P()

P("1. Oxygen-carrying capacity")
P()
P(f"      {'fluid':<24s} {'vol%':>8s}   {'vs human':>9s}")
P(f"      {'human arterial blood':<24s} {HB_HUMAN_VOL_PCT:>8.2f}   "
  f"{'1.00x':>9s}")
for sp, v in HCY_SPECIES_VOL_PCT.items():
    P(f"      {sp:<24s} {v:>8.2f}   {HB_HUMAN_VOL_PCT / v:>8.1f}x")
P(f"      {'cephalopod ceiling':<24s} {HCY_CEPHALOPOD_CEILING:>8.2f}   "
  f"{HB_HUMAN_VOL_PCT / HCY_CEPHALOPOD_CEILING:>8.1f}x")
P()
worst = max(HB_HUMAN_VOL_PCT / v for v in HCY_SPECIES_VOL_PCT.values())
best = HB_HUMAN_VOL_PCT / HCY_CEPHALOPOD_CEILING
P(f"      So hemocyanin carries {best:.1f} to {worst:.1f} times less oxygen per")
P("      unit volume than human blood, taking the most generous published")
P("      ceiling at one end and a measured octopus at the other.")
P()
P("      And it cannot be fixed by concentrating it.  From the paper the")
P("      preprint's own first citation garbles:")
P()
for line in OSMOTIC_QUOTE.split(". "):
    P(f'        "{line.strip()}"')
P()
P("      Haemoglobin evades that by being packed inside erythrocytes, where it")
P("      is osmotically invisible.  Hemocyanin is dissolved in the haemolymph,")
P("      so its concentration is capped by colloid osmotic pressure and")
P("      viscosity.  The capacity gap is structural, not a matter of degree.")

P()
P("2. What a human resting metabolism requires of the circulation")
P()
P(f"  [V] resting oxygen consumption      {VO2_REST_ML_PER_KG_MIN:>8.1f} "
  f"mL O2/kg/min  (1 MET)")
P(f"      for a {BODY_MASS_KG:.0f} kg adult               "
  f"{VO2_REST_ML_MIN:>8.1f} mL O2/min")
P()
P(f"      [A] cardiac output at rest      "
  f"{CARDIAC_OUTPUT_REST_L_MIN[0]:.1f} - {CARDIAC_OUTPUT_REST_L_MIN[1]:.1f} L/min")
P()
P(f"      {'cardiac output':>16s} {'a-v difference required':>26s}")
for co in CARDIAC_OUTPUT_REST_L_MIN:
    P(f"      {co:>13.1f} L/min {required_avo2_vol_pct(VO2_REST_ML_MIN, co):>21.2f} vol%")
P()
P("      For reference, human arterial blood is 20 vol% and venous blood about")
P("      15, so the measured arteriovenous difference at rest is about 5 vol% --")
P("      which is what this calculation reproduces.  The arithmetic is")
P("      therefore calibrated against the system it describes.")

P()
P("3. The same requirement, met with hemocyanin")
P()
P("      Extraction cannot be complete: unloading needs a partial-pressure")
P("      gradient, so some oxygen always returns in the venous fluid.")
P()
P(f"      [A] extraction fraction         "
  f"{O2_EXTRACTION_FRACTION[0]:.0%} - {O2_EXTRACTION_FRACTION[1]:.0%}")
P()
P(f"      {'capacity':>10s} {'extraction':>11s} {'delivered':>11s} "
  f"{'cardiac output needed':>23s} {'vs human':>10s}")
for cap_label, cap in (("ceiling", HCY_CEPHALOPOD_CEILING),
                       ("O. vulgaris", HCY_SPECIES_VOL_PCT["Octopus vulgaris"])):
    for ex in O2_EXTRACTION_FRACTION:
        delivered = cap * ex                      # vol% actually unloaded
        co_needed = VO2_REST_ML_MIN / (delivered / 100.0) / 1000.0  # L/min
        ref = VO2_REST_ML_MIN / (HB_HUMAN_VOL_PCT * ex / 100.0) / 1000.0
        P(f"      {cap:>7.2f}   {ex:>10.0%} {delivered:>8.2f} vol% "
          f"{co_needed:>18.1f} L/min {co_needed / ref:>9.1f}x")
P()
cap, ex = HCY_CEPHALOPOD_CEILING, max(O2_EXTRACTION_FRACTION)
best_co = VO2_REST_ML_MIN / (cap * ex / 100.0) / 1000.0
oct_cap = HCY_SPECIES_VOL_PCT["Octopus vulgaris"]
oct_lo = VO2_REST_ML_MIN / (oct_cap * max(O2_EXTRACTION_FRACTION) / 100.0) / 1000.0
oct_hi = VO2_REST_ML_MIN / (oct_cap * min(O2_EXTRACTION_FRACTION) / 100.0) / 1000.0
P(f"      At the published cephalopod ceiling and a generous {ex:.0%} extraction")
P(f"      a resting human needs {best_co:.1f} L/min of cardiac output, above the")
P(f"      normal resting range; at the measured O. vulgaris capacity it is")
P(f"      {oct_lo:.0f} to {oct_hi:.0f} L/min, against a maximal human cardiac")
P("      output of roughly 20-25 L/min in a trained athlete.")
P()
P("      So the proposal fails at rest, before any activity is considered.")

P()
P("4. And activity is where it fails by more")
P()
P(f"      [A] VO2max as a multiple of resting   "
  f"{VO2_MAX_MULTIPLE[0]:.0f} - {VO2_MAX_MULTIPLE[1]:.0f} x")
P()
P(f"      {'exertion':>10s} {'VO2':>12s} "
  f"{'cardiac output with hemocyanin at the ceiling':>46s}")
for mult in (1.0,) + VO2_MAX_MULTIPLE:
    vo2 = VO2_REST_ML_MIN * mult
    co = vo2 / (HCY_CEPHALOPOD_CEILING * 0.75 / 100.0) / 1000.0
    label = "rest" if mult == 1.0 else f"{mult:.0f}x rest"
    P(f"      {label:>10s} {vo2:>9.0f} mL/min {co:>40.0f} L/min")
P()
P("      The preprint claims thermoregulatory independence and a lifespan of")
P("      centuries for an organism whose oxygen delivery cannot support it")
P("      sitting still.")

P()
P("5. Why the animals that do use hemocyanin are not a counterexample")
P()
P("      Squid reach mass-specific metabolic rates comparable to mammals, which")
P("      is the strongest argument available for the preprint and is worth")
P("      stating.  They do it by moving far more fluid, and the cost is named")
P("      by the people who measured it:")
P()
P(f'        "{SQUID_CONSTRAINT_QUOTE}"')
P()
P("      -- i.e. the limit on a squid is precisely the quantity the preprint")
P("      proposes to adopt.  They also run a Bohr effect of -1.2 to -2.3")
P("      against the human -0.35 to -0.5, venous saturations around 14 %, and")
P("      effectively no aerobic scope.  The largest hemocyanin animal, the")
P("      colossal squid, is an ambush predator with a metabolic rate orders")
P("      below an active squid of the same clade.")

P()
P("6. Protein mass per oxygen carried, for the mechanism behind the gap")
P()
P(f"      [A] haemoglobin: 4 O2 per {HB_TETRAMER_KDA:.1f} kDa tetramer "
  f"= {HB_TETRAMER_KDA / 4:>5.1f} kDa per O2")
P(f"      [A] hemocyanin:  1 O2 per binuclear site, "
  f"{HCY_PER_O2_KDA[0]:.0f}-{HCY_PER_O2_KDA[1]:.0f} kDa per O2")
lo = HCY_PER_O2_KDA[0] / (HB_TETRAMER_KDA / 4)
hi = HCY_PER_O2_KDA[1] / (HB_TETRAMER_KDA / 4)
P(f"      ratio                              {lo:>5.1f} - {hi:.1f} x the "
  f"protein mass per O2")
P()
P("      That bracket, 3 to 6 times, is the same size as the measured capacity")
P("      gap of 4.4 to 14.6 times, which is what one would expect if the")
P("      difference is largely stoichiometric and partly osmotic.  Both figures")
P("      here are [A] and this section is an explanation of the gap rather than")
P("      evidence for it; the capacity measurements in Sec. 1 are the evidence.")
