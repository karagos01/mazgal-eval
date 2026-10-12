#!/usr/bin/env python3
"""Sec. 2.1: the band F_micro operates in, against the two things it is said to
act on.

  "F_micro(t): The high-frequency fractal modulation (kHz to MHz range)
   utilizing self-similarity to induce phonon-assisted tunneling and lower
   activation barriers at the solid-electrolyte interphase (SEI) and within the
   crystal lattice."                                              -- Sec. 2.1

Two tests.  The lattice modes it names are measured in the tens to hundreds of
wavenumbers, i.e. terahertz; and the band where a cell has any faradaic response
at all stops at about a kilohertz.  Both are ratios, so neither depends on a
modelling choice.
"""
from constants import (EIS_CHARGE_TRANSFER_BAND, F_MICRO_BAND, FOIL_THICKNESS_UM,
                       KT_EV_300, NA_MIGRATION_EV, NMC_RAMAN_CM1, RHO_AL, RHO_CU,
                       photon_ev, skin_depth_m, tag_report, wavenumber_to_hz)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. The band, and the lattice it is said to drive")
P()
P(f"  [P] F_micro                          {F_MICRO_BAND[0]:>12,.0f} - "
  f"{F_MICRO_BAND[1]:>12,.0f} Hz")
P()
P(f"  [V] Raman-active modes measured in a layered oxide cathode (NMC111):")
P(f"      {'wavenumber':>12s} {'frequency':>14s} {'quantum':>12s}")
for cm1 in NMC_RAMAN_CM1:
    f = wavenumber_to_hz(cm1)
    P(f"      {cm1:>9.0f} cm-1 {f / 1e12:>11.2f} THz {photon_ev(f) * 1000:>9.2f} meV")
P()
import math
lo = wavenumber_to_hz(min(NMC_RAMAN_CM1))
top, bot = F_MICRO_BAND[1], F_MICRO_BAND[0]
P(f"      the lowest measured mode is       {lo / 1e12:>12.2f} THz"
  f"  = {lo / 1e6:,.0f} MHz")
P(f"      the top of the F_micro band is    {top / 1e6:>12.0f} MHz")
P(f"      ratio at the top of the band      {lo / top:>12,.0f} x"
  f"   ({math.log10(lo / top):.1f} orders)")
P(f"      ratio at the bottom of the band   {lo / bot:>12,.0f} x"
  f"   ({math.log10(lo / bot):.1f} orders)")
P()
P("      So the band sits between six and ten orders of magnitude below the")
P("      slowest lattice vibration measured in this class of material.")
P("      'Phonon-assisted tunneling' at 1 MHz is not addressing a phonon;")
P("      there is no mode there to assist.")

P()
P("2. The same point in energy, which is the form that matters for tunneling")
P()
for f, label in ((F_MICRO_BAND[0], "1 kHz"), (F_MICRO_BAND[1], "1 MHz")):
    P(f"      h.f at {label:<6s}                     {photon_ev(f):>12.3e} eV")
P(f"      k.T at 300 K                      {KT_EV_300:>12.5f} eV")
P(f"        ratio, kT / h.f(1 MHz)          {KT_EV_300 / photon_ev(top):>12,.0f} x")
P()
P(f"  [V] sodium migration barrier          "
  f"{NA_MIGRATION_EV[0]:>12.2f} - {NA_MIGRATION_EV[1]:.2f} eV")
for ea in NA_MIGRATION_EV:
    P(f"        E_a / h.f(1 MHz) at {ea:.2f} eV      {ea / photon_ev(top):>12.3e}")
P()
P("      The stimulation quantum is about six million times smaller than the")
P("      ambient thermal energy the ions already have, and seven to eight")
P("      orders below the barrier it is meant to lower.  Whatever a kHz-to-MHz")
P("      field does to a cell, it does not do it one quantum at a time.")

P()
P("3. Where the cell has a faradaic response at all")
P()
P(f"  [V] charge-transfer semicircle        "
  f"{EIS_CHARGE_TRANSFER_BAND[0]:>12,.0f} - {EIS_CHARGE_TRANSFER_BAND[1]:,.0f} Hz")
P(f"  [P] F_micro band                      {F_MICRO_BAND[0]:>12,.0f} - "
  f"{F_MICRO_BAND[1]:,.0f} Hz")
overlap_lo = max(EIS_CHARGE_TRANSFER_BAND[0], F_MICRO_BAND[0])
overlap_hi = min(EIS_CHARGE_TRANSFER_BAND[1], F_MICRO_BAND[1])
overlap = max(0.0, overlap_hi - overlap_lo)
P(f"      overlap                           {overlap:>12,.0f} Hz")
P()
P("      The two bands meet at a point and do not overlap.  Above the")
P("      charge-transfer region the measured response of a cell is ohmic and")
P("      inductive, which means current in the F_micro band flows through the")
P("      double-layer capacitance and the series inductance rather than across")
P("      the interface.  Capacitive current transfers no ions; it dissipates in")
P("      the series resistance.  That is Joule heating, which is the loss Sec. 1")
P("      sets out to avoid.")

P()
P("4. The limitation Sec. 5 names, and the one it should have named")
P()
P("  [P] Sec. 5: \"MHz-range fractal signals injected into such geometries will")
P("      suffer from severe attenuation and skin-effect reflections.\"")
P()
P(f"      {'frequency':>12s} {'skin depth, Cu':>16s} {'skin depth, Al':>16s}")
for f in (1e3, 1e4, 1e5, 1e6, 1e7):
    P(f"      {f:>9,.0f} Hz {skin_depth_m(RHO_CU, f) * 1e6:>13.1f} um "
      f"{skin_depth_m(RHO_AL, f) * 1e6:>13.1f} um")
P()
P(f"      [A] current-collector foil is {FOIL_THICKNESS_UM[0]:.0f}-"
  f"{FOIL_THICKNESS_UM[1]:.0f} um thick")
d_al = skin_depth_m(RHO_AL, 1e6) * 1e6
P(f"      at 1 MHz the aluminium skin depth is {d_al:.0f} um, i.e. "
  f"{d_al / FOIL_THICKNESS_UM[1]:.1f}-{d_al / FOIL_THICKNESS_UM[0]:.1f}x")
P("      the foil thickness, so the current still fills the foil and skin")
P("      effect within it is not the binding limit at the stated frequencies.")
P()
P("      Sec. 5 reaches the right conclusion -- that MHz signals do not reach")
P("      the lattice in a wound cell -- from the wrong mechanism.  The binding")
P("      limit is the double-layer shunt measured in Sec. 3 above, and it")
P("      applies to a planar coin cell too, which is the geometry Sec. 5")
P("      prescribes as the fix.")
