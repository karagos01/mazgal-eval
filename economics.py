#!/usr/bin/env python3
"""Sec. 4: the capital budget, the return, and the "intergenerational closed
loop".

  "In contrast, the $1,000,000 investment into the hyper-saturation model
   represents permanent capital. ... If all manure and biological waste is
   composted and returned to the soil, the total amount of gold, lanthanum, and
   quantum isotopes in the system remains constant. This constitutes an
   intergenerational closed loop."

Three things are computed: the gold line against the spot price on the day the
preprint was deposited, the return against the saving the paper itself claims,
and how much annual leakage the closed loop can take before the inventory it is
supposed to preserve is gone.
"""
import math

from constants import (ANNUAL_SAVING, CAPEX_GOLD_USD, CAPEX_USD, DISCOUNT_RATES,
                       ESTATE_HA, GOLD_KG, GOLD_USD_PER_OZ, LOOP_LOSS_RATES,
                       TROY_OZ_G)

P = print

P("1. The gold line against the spot price on the date of deposit")
P()
spot_g = GOLD_USD_PER_OZ / TROY_OZ_G
implied_g = CAPEX_GOLD_USD / (GOLD_KG * 1000.0)
P(f"  [V] {'spot, 6 October 2026':<30s} ${GOLD_USD_PER_OZ:>10,.2f}/troy oz"
  f"  = ${spot_g:>6.2f}/g")
P(f"  [P] {f'${CAPEX_GOLD_USD:,.0f} for {GOLD_KG:.0f} kg implies':<30s} "
  f"${implied_g * TROY_OZ_G:>10,.2f}/troy oz  = ${implied_g:>6.2f}/g")
P()
at_spot = GOLD_KG * 1000.0 * spot_g
P(f"      {f'{GOLD_KG:.0f} kg at spot':<32s} ${at_spot:>12,.0f}")
P(f"      {'shortfall in that one line':<32s} ${at_spot - CAPEX_GOLD_USD:>12,.0f}"
  f"   ({at_spot / CAPEX_GOLD_USD:.2f} x)")
P(f"      {'total capex restated':<32s} "
  f"${CAPEX_USD - CAPEX_GOLD_USD + at_spot:>12,.0f}")
P()
P("      The implied price is roughly what gold cost two years before the")
P("      preprint was written, so this reads as a stale figure rather than an")
P("      error of method.  It moves the headline total by a quarter.")

P()
P("2. The return, on the paper's own numbers")
P()
P(f"  [P] {'capital expenditure':<32s} ${CAPEX_USD:>12,.0f}")
P(f"  [P] {'annual saving':<32s} ${ANNUAL_SAVING:>12,.0f}")
P(f"      {'simple payback, undiscounted':<32s} "
  f"{CAPEX_USD / ANNUAL_SAVING:>13.0f} years")
P(f"      {'capex per hectare':<32s} ${CAPEX_USD / ESTATE_HA:>12,.0f} /ha")
P()
P(f"      break-even discount rate in perpetuity "
  f"{ANNUAL_SAVING / CAPEX_USD:>7.2%} per year")
P()
P(f"      [A] {'rate':>6s} {'PV of the saving':>20s} {'NPV':>16s}")
for r in DISCOUNT_RATES:
    if r == 0.0:
        P(f"          {r:>5.1%} {'unbounded':>20s} {'unbounded':>16s}")
        continue
    pv = ANNUAL_SAVING / r
    P(f"          {r:>5.1%} ${pv:>19,.0f} ${pv - CAPEX_USD:>15,.0f}")
P()
P("      The investment is positive only at a real discount rate at or below")
P("      2.5 % held in perpetuity.  The paper calls it 'permanent capital',")
P("      which is the right frame for the claim -- but the claim then needs the")
P("      inventory to actually be permanent, which is the next section.")

P()
P("3. How much leakage the closed loop can take")
P()
P("      The loop is only closed if the metals return.  Phytomining works by")
P("      concentrating metal into harvested biomass, and biomass leaves the")
P("      field, so the return fraction is the whole question.  The paper assumes")
P("      it is exactly 1.")
P()
P(f"      [A] {'annual loss':>12s} {'half the inventory gone in':>28s}")
for f in LOOP_LOSS_RATES:
    half = math.log(2) / -math.log(1 - f)
    P(f"          {f:>11.1%} {half:>24.1f} years")
P()
payback = CAPEX_USD / ANNUAL_SAVING
max_loss = 1 - 0.5 ** (1 / payback)
P(f"      For more than half the inventory to survive to the {payback:.0f}-year")
P(f"      payback, the annual loss has to stay below {max_loss:.2%}.")
P()
P("      That is a demanding number for an open field: it has to cover harvest")
P("      removal net of returned manure, leaching, erosion and runoff, all at")
P("      once.  The paper gives no figure for any of them, so this is a bound")
P("      on what the claim requires rather than a measurement of what happens.")

P()
P("4. What the comparison omits")
P()
P(f"  [P] the saving is 'synthetic fertilizers, pesticides, and associated")
P("      diesel fuel' at $25,000/yr for 30 ha")
P()
P("      Not costed anywhere in the paper, and each would move the result:")
for item in ("replacement of the pellet matrix as biochar mineralises",
             "the yield difference, positive or negative, which is never measured",
             "the cost of monitoring metal levels in food crops",
             "any regulatory cost of putting 5 kg of gold and 1 t of lanthanum "
             "oxide into farmland"):
    P(f"        - {item}")
P()
P("      The first matters most to the 'permanent capital' claim: biochar is")
P("      the carrier for everything else, and the cited Lehmann review treats")
P("      its persistence in soil as an open question rather than a given.")
