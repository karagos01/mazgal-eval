#!/usr/bin/env python3
"""Sec. 4: the densification arithmetic, and what the two halves of one sentence
cost if each is taken seriously.

The sentence, verbatim:

  "Densification to the level of 1 pellet per 5 cm3 of soil (at a plowing depth
   of 30 cm) equates to approximately 2,500 pellets per 1 m2, or 25 tons of
   matrix per 1 hectare."

It states a volumetric density, a count per square metre and a mass per hectare
as if they were the same claim.  They are not: the first is 24 times the second.
Everything downstream in the paper -- the 750-tonne material requirement, the
$1,000,000 budget, the whole case study -- rests on the second.  The motivation
for the first is the sentence just before it, that the root "must be in constant
physical contact with the nanomatrix", so the two are not interchangeable.
"""
from constants import (CAPEX_USD, ESTATE_HA, ESTATE_T, MATRIX_T_PER_HA,
                       PELLET_PER_CM3, PELLETS_PER_M2, PLOUGH_DEPTH_M,
                       SOIL_CM3_PER_M2)

P = print

P("1. The two densities in one sentence")
P()
P(f"  [P] plough depth                         {PLOUGH_DEPTH_M:>12.2f} m")
P(f"      soil volume under 1 m2               {SOIL_CM3_PER_M2:>12,.0f} cm3")
P()
implied = SOIL_CM3_PER_M2 / PELLET_PER_CM3
P(f"  [P] \"1 pellet per {PELLET_PER_CM3:.0f} cm3\" implies         "
  f"{implied:>12,.0f} pellets/m2")
P(f"  [P] \"approximately 2,500 pellets per 1 m2\"{PELLETS_PER_M2:>12,.0f} pellets/m2")
P(f"      ratio                                {implied / PELLETS_PER_M2:>12.1f} x")
P()
P(f"      2,500 pellets/m2 corresponds to 1 pellet per "
  f"{SOIL_CM3_PER_M2 / PELLETS_PER_M2:.0f} cm3, not 5.")

P()
P("2. Which of the two the rest of the paper uses")
P()
kg_per_m2 = MATRIX_T_PER_HA * 1000.0 / 10_000.0
P(f"  [P] 25 t/ha                              {kg_per_m2:>12.2f} kg/m2")
for n, label in ((PELLETS_PER_M2, "2,500/m2"), (implied, f"{implied:,.0f}/m2")):
    P(f"      mass per pellet at {label:<12s}      "
      f"{kg_per_m2 / n * 1000:>12.4f} g")
P()
P("      So the mass budget is self-consistent with 2,500 pellets of 1 g each,")
P("      which is a sensible pellet.  The 5 cm3 figure is the one that does not")
P("      fit, and the paper's economics are built on the 2,500.")

P()
P("3. What honouring the 5 cm3 figure would cost")
P()
g_per_pellet = kg_per_m2 / PELLETS_PER_M2 * 1000.0    # the paper's own 1 g
t_ha = implied * g_per_pellet / 1000.0 * 10_000.0 / 1000.0
P(f"      at the paper's own {g_per_pellet:.0f} g per pellet:")
P(f"        {'matrix':<14s} {t_ha:>14,.0f} t/ha      "
  f"paper: {MATRIX_T_PER_HA:>12,.0f} t/ha")
P(f"        {'for 30 ha':<14s} {t_ha * ESTATE_HA:>14,.0f} t         "
  f"paper: {ESTATE_T:>12,.0f} t")
P(f"        {'at the same $/t':<14s} "
  f"{'$' + format(t_ha * ESTATE_HA * CAPEX_USD / ESTATE_T, ',.0f'):>14s}"
  f"           paper: {'$' + format(CAPEX_USD, ',.0f'):>11s}")
P()
P("      i.e. the sentence's own premise, taken at face value, multiplies the")
P("      case study by 24 and the budget with it.  This is a single arithmetic")
P("      slip in one sentence, not a defect in the concept; what it costs the")
P("      paper is that the physical-contact requirement and the costed design")
P("      are not the same design.")

P()
P("4. What \"constant physical contact\" comes to at each density")
P()
P(f"  {'pellets/m2':>12s} {'per m3':>12s} {'mean spacing':>14s} "
  f"{'max distance to nearest':>24s}")
for n in (PELLETS_PER_M2, implied):
    per_m3 = n / PLOUGH_DEPTH_M
    spacing = (1.0 / per_m3) ** (1.0 / 3.0)
    P(f"  {n:>12,.0f} {per_m3:>12,.0f} {spacing * 100:>11.2f} cm "
      f"{spacing * 100 / 2:>21.2f} cm")
P()
P("      On a cubic lattice at the costed density a root is never more than")
P("      2.5 cm from a pellet, and at the stated density never more than 0.9 cm.")
P("      Neither is contact; both are a distance a root has to grow across, and")
P("      the paper gives no root-length density to compare them against.")

P()
P("5. The one figure in this section that checks out")
P()
P("  [P] Sec. 1: \"A plant is capable of assimilating only 30% to 50% of the")
P("      supplied nutrients in real-time\"")
P("  [V] \"Fertilizer N-recovery efficiency by the first crop is 30 to 50%\"")
P("      -- IFA, Nutrient/fertilizer use efficiency, ch. 1 (2014)")
P("      This is correct, and it is the premise the whole paper starts from.")
