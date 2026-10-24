"""What holding stomata open through the midday depression costs in water.

Section 9 of PAPER.md.
"""
from constants import (GS_MORNING, GS_MIDDAY, VPD_MORNING, VPD_MIDDAY, P_ATM,
                       YIELD_CLAIM, F_FIELD)

# Half-saturation conductance in the illustrative A(g_s) below.  This is a
# chosen shape parameter, not a measured constant: assimilation saturates in
# stomatal conductance because CO2 supply stops being the limiting step.  The
# sensitivity table shows the conclusion does not depend on the value.
GS_HALF = 0.10

bar = lambda c="=": print(c * 78)

# Leaf-level transpiration, E = g_s * VPD / P (mol H2O per mol air, times g_s).
E = lambda gs, vpd: gs * vpd / P_ATM * 1e3     # mmol H2O /m^2/s

bar()
print("1. TRANSPIRATION ACROSS THE MIDDAY DEPRESSION")
bar()
print(f"  {'state':34s} {'g_s':>7} {'VPD':>7} {'E':>12}")
rows = [("morning, stomata open", GS_MORNING, VPD_MORNING),
        ("midday, natural depression", GS_MIDDAY, VPD_MIDDAY),
        ("midday, held open as proposed", GS_MORNING, VPD_MIDDAY)]
for lab, gs, vpd in rows:
    print(f"  {lab:34s} {gs:7.2f} {vpd:7.1f} {E(gs, vpd):8.2f} mmol/m^2/s")
print()
nat = E(GS_MIDDAY, VPD_MIDDAY)
forced = E(GS_MORNING, VPD_MIDDAY)
print(f"  The depression almost exactly cancels the rise in VPD: morning"
      f" {E(GS_MORNING, VPD_MORNING):.2f}")
print(f"  against natural midday {nat:.2f} mmol/m^2/s.  That is what the response is for.")
print(f"  Suppressing it multiplies midday transpiration by"
      f" {forced/nat:.1f} x, at the hour of peak demand.")
bar("-")
print("  Sensitivity: the factor is g_s(held) / g_s(depressed) and does not depend")
print("  on VPD at all, so it survives any choice of the midday VPD:")
print(f"  {'VPD kPa':>9}  {'natural':>14}  {'held open':>14}  {'factor':>8}")
for vpd in [2.0, 2.5, 3.0, 4.0, 5.0]:
    print(f"  {vpd:9.1f}  {E(GS_MIDDAY, vpd):9.2f} mmol  "
          f"{E(GS_MORNING, vpd):9.2f} mmol  {GS_MORNING/GS_MIDDAY:8.1f} x")

bar()
print("2. WHAT IS BOUGHT WITH IT")
bar()
# Water-use efficiency: A / E, with A set by the flux available at midday.
print("  Assimilation does rise when stomata reopen, but it saturates in CO2")
print("  while transpiration stays linear in g_s, so water-use efficiency falls.")
print(f"  A(g_s) = g_s / (g_s + K) with K = {GS_HALF:.2f} as an illustrative shape;")
print("  the value of K is chosen, not measured.")
print(f"  {'g_s':>6}  {'A (relative)':>13}  {'E mmol':>9}  {'A/E (relative)':>15}")
for gs in [0.10, 0.15, 0.20, 0.25, 0.30]:
    # Michaelis-type saturation of A in stomatal conductance
    a_rel = gs / (gs + GS_HALF)
    e = E(gs, VPD_MIDDAY)
    print(f"  {gs:6.2f}  {a_rel:13.3f}  {e:9.2f}  {a_rel/e*100:15.3f}")
print()
a_gain = lambda K: (GS_MORNING/(GS_MORNING+K)) / (GS_MIDDAY/(GS_MIDDAY+K))
print(f"  Tripling g_s from {GS_MIDDAY:.2f} to {GS_MORNING:.2f} multiplies")
print(f"  transpiration by {forced/nat:.1f} x regardless of K, and assimilation by:")
print(f"  {'K':>8}  {'A gain':>8}  {'water per gram of carbon':>26}")
for K in [0.03, 0.05, 0.10, 0.20, 0.50, 1e6]:
    lab = "linear" if K > 1e3 else f"{K:.2f}"
    print(f"  {lab:>8}  {a_gain(K):8.2f} x  {(forced/nat)/a_gain(K):24.2f} x")
print("  Only an exactly linear A(g_s) breaks even; every saturating shape costs")
print("  more water per unit carbon, which is the definition of the trade-off")
print("  the stomatal response exists to manage.")
print("  The preprint states the direction of this itself: 'evapotranspiration")
print("  rates will rise ... must be paired with continuous soil moisture")
print("  monitoring and sufficient irrigation buffers'.  That is correct, and it")
print("  is the cost rather than a caveat: the proposal is to defeat a drought")
print("  response in open fields of winter wheat, sugar beet and potatoes.")

bar()
print("3. THE YIELD CLAIM")
bar()
print(f"  claimed net biomass increase: {YIELD_CLAIM[0]*100:.0f}-{YIELD_CLAIM[1]*100:.0f} %")
print("  No derivation is given, and nothing in the paper links it to the")
print(f"  {F_FIELD} Hz stimulation, to a dose, to a duration or to a crop.")
print("  The cited PAFT review reports yield gains of 5.7 % (rice) to 37.1 %")
print("  (cucumber) at 70 dB and 30-60 m from a dedicated generator, so the")
print("  claimed range is plausible for that exposure.  What is not available is")
print("  that exposure: see acoustics.py.")
