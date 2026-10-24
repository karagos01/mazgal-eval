#!/usr/bin/env python3
"""Sec. 2.2: the anomaly criterion, which names one quantity in its heading and
defines a different one in its body.

  "2.2 Anomaly Criterion (Negative Differential Resistance)
   The optimization process searches for a localized drop in differential
   impedance:  Z_diff = dV / dI
   The anomaly state is detected when an incremental increase in the integral
   power delivered by V(t) yields a sub-proportional thermal response (dT).
   This indicates the onset of coherent, low-friction ion intercalation."

Two things are checked.  Whether negative differential resistance and a
sub-proportional thermal response are the same statement, and whether the
criterion as written can distinguish the effect it is looking for from the cell
simply getting warmer -- a confound the preprint's own Sec. 5 identifies.
"""
import math

from constants import (K_B, E_CHARGE, PL2006_BEST_IS_CONTINUOUS, PL2006_PULSE_S,
                       PL2006_REST_S, R_I_ARRHENIUS_EV, T_AMBIENT_K, T_SWEEP_C,
                       tag_report)

P = print
KB_EV = K_B / E_CHARGE      # eV/K

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. The heading and the body describe different quantities")
P()
P("      heading:  Negative Differential Resistance")
P("      body:     Z_diff = dV/dI, and an anomaly when dT per unit power falls")
P()
P("      Negative differential resistance means dV/dI < 0.  For a cell under")
P("      charge at fixed state of charge, V = OCV(SoC) + I.R_i with R_i > 0,")
P("      so dV/dI = R_i > 0 always.  A cell cannot exhibit NDR in that sense;")
P("      the terminal voltage rises with current by construction.")
P()
P("      'Sub-proportional heat per unit power delivered' is a statement about")
P("      energy efficiency -- more of the input ended up stored rather than")
P("      dissipated.  That is a real and measurable thing, and it is not a sign")
P("      change in dV/dI.  The two are not the same criterion, and the section")
P("      gives no way to decide which one the optimiser is to search for.")
P()
P("      Also, dV/dI has units of ohms, so it is a differential RESISTANCE.")
P("      The text calls it a differential impedance, which is the complex")
P("      quantity measured against frequency, not against current.")

P()
P("2. Can the body's criterion be told apart from the cell warming up?")
P()
P("  [P] Sec. 5 identifies this confound itself:")
P("      \"Differentiating between standard thermal agitation (which naturally")
P("       lowers R_i as the cell heats up) and genuine electro-kinetic field")
P("       enhancement requires highly precise isothermal calorimetry\"")
P()
P("      Arrhenius, R_i(T) = R0.exp(E_a/kT), relative to 25 C:")
P(f"      [A] {'E_a':>6s}  " + "  ".join(f"{t:>6d} C" for t in T_SWEEP_C))
for ea in R_I_ARRHENIUS_EV:
    row = []
    ref = math.exp(ea / KB_EV / T_AMBIENT_K)
    for t in T_SWEEP_C:
        row.append(math.exp(ea / KB_EV / (t + 273.15)) / ref)
    P(f"      {ea:>6.2f}  " + "  ".join(f"{v:>8.3f}" for v in row))
P()
lo = min(math.exp(ea / KB_EV / (45 + 273.15)) / math.exp(ea / KB_EV / T_AMBIENT_K)
         for ea in R_I_ARRHENIUS_EV)
hi = max(math.exp(ea / KB_EV / (45 + 273.15)) / math.exp(ea / KB_EV / T_AMBIENT_K)
         for ea in R_I_ARRHENIUS_EV)
P(f"      A 20 K rise alone multiplies I^2.R heating at fixed current by")
P(f"      {lo:.2f} to {hi:.2f}, i.e. it cuts it by {1 / hi:.1f} to "
  f"{1 / lo:.1f} times.")
P()
P("      That is exactly the signature Sec. 2.2 looks for: push more power in,")
P("      get less heat out per unit of it.  So the criterion as written is")
P("      satisfied by a cell that is merely warming, across the whole swept")
P("      range of activation energies, with no electro-kinetic effect at all.")
P()
P("      Sec. 5 prescribes the right instrument -- isothermal calorimetry --")
P("      and that is to the paper's credit.  But Sec. 2.2 is the section that")
P("      defines the search objective, and as defined it is confounded.  The")
P("      optimiser would find warm cells.")

P()
P("3. What the paper's own pulsed-charging citation says instead")
P()
P("  [V] Purushothaman & Landau, J. Electrochem. Soc. 153(3) A533 (2006),")
P("      the preprint's only pulsed-charging reference:")
P()
P("      \"Modeling the lithium diffusion into a homogeneous intercalant layer")
P("       indicates that the lithium concentration reaches saturation at the")
P("       graphite/electrolyte interface after about 1 h under conventional")
P("       constant current charging\"")
P()
P(f"      the analysed protocol: {PL2006_PULSE_S:.0f} s on, "
  f"{PL2006_REST_S:.0f} s off")
duty = PL2006_PULSE_S / (PL2006_PULSE_S + PL2006_REST_S)
period = PL2006_PULSE_S + PL2006_REST_S
P(f"        duty cycle                        {duty:>12.0%}")
P(f"        repetition rate                   {1 / period:>12.2f} Hz")
P()
P("      \"A nonlinearly decreasing current density profile which conforms to")
P("       the mass transfer coefficient variation was shown to provide complete")
P("       charging in less than 3/4 of an hour, faster than any other")
P("       pulse-charging profile studied.\"")
P(f"        best result is a continuous profile:  {PL2006_BEST_IS_CONTINUOUS}")
P()
P("      So the limiting mechanism in the cited work is solid-state diffusion,")
P("      the beneficial timescale is a quarter of a hertz, and the best result")
P("      is not a pulse at all.  It supports W_macro, the low-frequency")
P("      envelope, and contradicts F_micro, which sits six orders of magnitude")
P("      above the band it identifies.  The paper cites no source that")
P("      identifies a beneficial kHz or MHz band, and the audit of all six of")
P("      its references found none -- see the reference-audit repository.")
