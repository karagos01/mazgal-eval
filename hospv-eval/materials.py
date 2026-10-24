"""Sections 2.2 and 5, and table 1: whether the materials exist.

Three claims here are about matter rather than about arithmetic, and each can be
checked against measured values: the energy window the fission donor has to sit
in, the magnetic ordering temperature of the altermagnetic collector, and the
specific power of the stack table 1 specifies.
"""
import numpy as np

import constants as C
from photocurrent import recomputed

KT_STC = C.BOLTZMANN * C.TEMPERATURE_STC / C.ELEMENTARY_CHARGE     # eV


def stack(org, enc, ref):
    """Areal mass of table 1's seven layers, in g/m^2."""
    layers = (
        ("1 substrate, PEN", C.THICKNESS_SUBSTRATE, C.DENSITY_PEN),
        ("2 ITO anode", C.THICKNESS_ITO, C.DENSITY_ITO),
        ("3 c-SAM hole layer", C.THICKNESS_CSAM, org),
        ("4 active layer", C.THICKNESS_ACTIVE, org),
        ("5 MgO tunnel barrier", C.THICKNESS_MGO, C.DENSITY_MGO),
        ("6 altermagnet, RuO2", C.THICKNESS_ALTERMAGNET, C.DENSITY_RUO2),
        ("6 back reflector, Ag", ref, C.DENSITY_AG),
        ("7 encapsulation", C.THICKNESS_ENCAPSULATION, enc),
    )
    # thickness in m, density in g/cm^3; 1 m x 1 g/cm^3 = 1e6 g/m^2.
    # An earlier draft of this script used 1e3 here, and printed a
    # 10,588 um substrate and a shortfall "factor 0.0" before the unit was
    # found - which is why the layer-by-layer table below is printed at all
    # rather than only the total.
    return [(name, 1.0e6 * thickness * density) for name, thickness, density
            in layers]


def main():
    print("=" * 78)
    print("The energy ordering of section 2.2, with the preprint's own numbers")
    print("=" * 78)
    print("  Section 2.1 requires   E(S1) >= 2 E(T1)")
    print("  Section 2.2 requires   E(S1) >= 2 E(T1) >= 2 E_CT >= 2 E_g(IR)")
    print("  Section 2.2 specifies  E(S1) = %.2f eV, E(T1) = %.2f eV,"
          % (C.E_S1_DONOR, C.E_T1_DONOR))
    print("                         E_g(IR) = %.2f eV" % C.E_GAP_IR)
    print()
    drive = 2 * C.E_T1_DONOR - C.E_S1_DONOR
    print("  2 E(T1) = %.2f eV against E(S1) = %.2f eV:"
          % (2 * C.E_T1_DONOR, C.E_S1_DONOR))
    print("    the first link fails by %.0f meV.  The fission the architecture"
          % (1000 * drive))
    print("    rests on is endothermic by %.0f meV, which is %.1f kT at 25 C,"
          % (1000 * drive, drive / KT_STC))
    print("    not exothermic as section 2.1 requires.")
    print("  2 E(T1) = %.2f eV against 2 E_g(IR) = %.2f eV:"
          % (2 * C.E_T1_DONOR, 2 * C.E_GAP_IR))
    print("    this link holds, with %.0f meV to spare."
          % (1000 * (2 * C.E_T1_DONOR - 2 * C.E_GAP_IR)))
    print()
    print("  Endothermic fission is not fatal - tetracene is endothermic and")
    print("  still efficient - but section 2.1 also demands 1/k_SF below 100 fs")
    print("  to outrun singlet decay, and sub-100 fs fission is what exothermic")
    print("  chromophores do.  The two requirements pull opposite ways.")
    print()
    print("  What the ordering demands of a real chromophore:")
    print("    E(T1) >= E_g(IR) = %.2f eV   and   E(S1) >= 2 E(T1) >= %.2f eV"
          % (C.E_GAP_IR, 2 * C.E_GAP_IR))
    print()
    print("  %-12s %8s %8s %10s %12s %12s"
          % ("chromophore", "E(S1)", "E(T1)", "2T1-S1", "T1 >= 1.12?",
             "S1 >= 2 T1?"))
    for name, s1, t1, _note in C.SF_CHROMOPHORES:
        print("  %-12s %8.2f %8.2f %10.2f %12s %12s"
              % (name, s1, t1, 2 * t1 - s1,
                 "yes" if t1 >= C.E_GAP_IR else "no",
                 "yes" if s1 >= 2 * t1 else "no"))
    print("  %-12s %8.2f %8.2f %10.2f %12s %12s"
          % ("the preprint", C.E_S1_DONOR, C.E_T1_DONOR, drive,
             "yes" if C.E_T1_DONOR >= C.E_GAP_IR else "no",
             "yes" if C.E_S1_DONOR >= 2 * C.E_T1_DONOR else "no"))
    print()
    print("  Each of the three measured chromophores fails one of the two")
    print("  conditions, and so do the preprint's own numbers.  Pentacene, the")
    print("  one that fissions in 80 fs, has E(T1) = 0.86 eV: it cannot feed a")
    print("  1.12 eV acceptor at all, because its triplets lie below the gap.")
    print("  Rubrene comes closest and misses by %.0f meV.  Table 1's named"
          % (1000 * (2 * 1.14 - 2.21)))
    print("  donor, TIPS-tetracene, is a tetracene: endothermic, picoseconds.")
    print("  The window is narrow rather than empty, and nothing in the")
    print("  preprint is measured inside it.")
    print()

    print("=" * 78)
    print("Layer 6: the altermagnetic collector")
    print("=" * 78)
    print("  Table 1 specifies oriented RuO2(101) or MnTe, 40 nm, with a spin")
    print("  splitting of ~%.1f eV; section 5.1 says %.1f-%.1f eV."
          % (C.SPIN_SPLIT_TABLE, C.SPIN_SPLIT_CLAIMED[0], C.SPIN_SPLIT_CLAIMED[1]))
    print()
    print("  The splitting is right.  Angle-resolved photoemission on MnTe")
    print("  measures %.2f eV and %.2f eV in two independent studies, so the"
          % C.SPIN_SPLIT_MNTE_RANGE)
    print("  0.8 eV in table 1 is the published number for the material named.")
    print("  Reference [7], Smejkal, Sinova and Jungwirth, Phys. Rev. X 12,")
    print("  040501 (2022), is the right citation for altermagnetism, correctly")
    print("  attached, and the symmetry argument in section 5.1 - rotation")
    print("  rather than translation or inversion, hence spin-split bands where")
    print("  a collinear antiferromagnet has none - is stated correctly.")
    print()
    print("  What is not stated is the temperature at which it stops.")
    print()
    print("  %-30s %12s" % ("", "T (K)"))
    print("  %-30s %9.0f - %.0f" % ("MnTe Neel temperature, measured",
                                    C.NEEL_MNTE_RANGE[0], C.NEEL_MNTE_RANGE[1]))
    print("  %-30s %12.2f" % ("standard test conditions", C.TEMPERATURE_STC))
    for celsius in C.TEMPERATURE_SWEEP_C[2:]:
        label = {45.0: "typical module NOCT",
                 59.0: "measured NOCT, thin film",
                 85.0: "IEC 61215 upper qualification"}[celsius]
        print("  %-30s %12.2f" % (label, 273.15 + celsius))
    print()
    hottest = 273.15 + C.TEMPERATURE_SWEEP_C[-2]
    print("  A module in the field runs above MnTe's ordering temperature on")
    print("  both published values.  At the %.0f K measured for a thin-film"
          % hottest)
    print("  module under the IEC 61215 method, the collector is %.0f to %.0f K"
          % (hottest - C.NEEL_MNTE_RANGE[1], hottest - C.NEEL_MNTE_RANGE[0]))
    print("  into its paramagnetic phase, where the spin splitting that layer 6")
    print("  exists for is zero.  Even standard test conditions, %.2f K, sit"
          % C.TEMPERATURE_STC)
    print("  at or above the lower published value.")
    print()
    print("  The alternative named first, RuO2, has the opposite problem: its")
    print("  ordering temperature is well above room temperature, but whether")
    print("  it is magnetically ordered at all has been contested since 2024.")
    print("  Muon spin rotation and neutron diffraction put the bulk moment")
    print("  below 1.4e-4 muB/Ru, with the dissent coming from thin films and")
    print("  surfaces - which is the form table 1 specifies, so the question is")
    print("  open rather than closed against it.  Either way, the two materials")
    print("  offered for layer 6 are the one whose magnetism is disputed and")
    print("  the one that orders below the cell's operating temperature.")
    print()

    print("=" * 78)
    print("Table 2: specific power of at least 10,000 W/kg")
    print("=" * 78)
    lo_org, hi_org = C.DENSITY_ORGANIC_RANGE
    lo_enc, hi_enc = C.DENSITY_ENCAPSULATION_RANGE
    lo_ref, hi_ref = C.THICKNESS_REFLECTOR_RANGE

    rows = stack(1.2, 2.0, 150e-9)
    total = sum(mass for _name, mass in rows)
    print("  Layer by layer, at mid-range for the three assumed values:")
    print()
    print("  %-26s %12s %10s" % ("layer", "g/m^2", "share"))
    for name, mass in rows:
        print("  %-26s %12.3f %9.1f%%" % (name, mass, 100 * mass / total))
    print("  %-26s %12.3f" % ("total", total))
    print()
    packaging = rows[0][1] + rows[-1][1]
    print("  The 50 um substrate and the 25 um encapsulation are %.1f%% of the"
          % (100 * packaging / total))
    print("  mass and do no physics.  Everything that does - the two absorbers,")
    print("  the electrodes, the barrier and the altermagnet - is %.2f g/m^2."
          % (total - packaging))
    print()
    print("  Specific power, across the full range of the three assumptions:")
    print()
    print("  %-30s %12s %14s" % ("", "g/m^2", "W/kg"))
    extremes = []
    for org in (lo_org, hi_org):
        for enc in (lo_enc, hi_enc):
            for ref in (lo_ref, hi_ref):
                extremes.append(sum(m for _n, m in stack(org, enc, ref)))
    _jsc_recomputed, pce_recomputed = recomputed()
    for label, mass, pce in (
            ("lightest case, PCE as claimed", min(extremes), C.PCE_CLAIMED),
            ("heaviest case, PCE as claimed", max(extremes), C.PCE_CLAIMED),
            ("mid case, PCE as claimed", total, C.PCE_CLAIMED),
            ("mid case, PCE recomputed", total, pce_recomputed)):
        power = pce * 1000.0                                   # W/m^2 at 1 sun
        print("  %-30s %12.1f %14.0f" % (label, mass, power / (mass / 1000.0)))
    print("  %-30s %12s %14.0f" % ("claimed in table 2", "-",
                                   C.SPECIFIC_POWER_CLAIMED))
    print()
    shortfall = C.SPECIFIC_POWER_CLAIMED / (C.PCE_CLAIMED * 1000.0
                                            / (total / 1000.0))
    print("  The claim is short by a factor %.1f at every corner of the sweep."
          % shortfall)
    budget = C.PCE_CLAIMED * 1000.0 / C.SPECIFIC_POWER_CLAIMED * 1000.0
    print("  To reach 10,000 W/kg at the claimed %.1f%% the whole cell must"
          % (100 * C.PCE_CLAIMED))
    print("  weigh %.1f g/m^2.  The functional stack already weighs %.2f g/m^2,"
          % (budget, total - packaging))
    print("  so the packaging budget is %.1f g/m^2 against the %.1f g/m^2 that"
          % (budget - (total - packaging), packaging))
    print("  table 1's 75 um of polymer actually weighs.")
    # 1 g/m^2 of a material of density 1 g/cm^3 is exactly 1 um thick, so the
    # packaging budget in g/m^2 divided by its density in g/cm^3 is its
    # thickness in um directly.
    mean_density = 0.5 * (C.DENSITY_PEN + sum(C.DENSITY_ENCAPSULATION_RANGE) / 2)
    thin = (budget - (total - packaging)) / mean_density
    print("  At a mean packaging density of %.2f g/cm^3 that is %.0f um of"
          % (mean_density, thin))
    print("  polymer in total, against the %.0f um of table 1.  The claim"
          % (1e6 * (C.THICKNESS_SUBSTRATE + C.THICKNESS_ENCAPSULATION)))
    print("  is reachable for a free-standing ultrathin cell, which is where")
    print("  the 5,000-10,000 W/kg figures in that column come from; it is not")
    print("  reachable for the stack in table 1.")
    print()

    print("=" * 78)
    print("What 52.3 mA/cm^2 costs the rest of the stack")
    print("=" * 78)
    print("  A higher current makes every series resistance matter more.  The")
    print("  fill-factor loss from series resistance is about")
    print("  dFF/FF = R_s J_sc / V_oc, so the budget for layers 2, 3 and 5")
    print("  together, to hold the claimed FF to within one point, is:")
    print()
    print("  %-22s %18s %18s" % ("J_sc (mA/cm^2)", "R_s for 1 point",
                                 "R_s for 5 points"))
    for jsc in (C.JSC_CSI_TABLE, C.JSC_CLAIMED):
        one = 0.01 * C.VOC_CLAIMED / (jsc * 1e-3)
        five = 0.05 * C.VOC_CLAIMED / (jsc * 1e-3)
        print("  %-22.1f %8.3f ohm.cm^2 %8.3f ohm.cm^2" % (jsc, one, five))
    print()
    print("  The 42.8 mA/cm^2 row is the silicon cell in table 2, for scale.")
    print("  The whole stack above the absorber - a 100 nm ITO film, a 1.5 nm")
    print("  chiral monolayer and a 1.2 nm MgO tunnel barrier in series - has")
    print("  to come in under %.2f ohm.cm^2.  Nothing here says it cannot; the"
          % (0.01 * C.VOC_CLAIMED / (C.JSC_CLAIMED * 1e-3)))
    print("  point is that the claimed current tightens that budget by a")
    print("  further %.0f%% relative to a silicon cell, while adding two layers"
          % (100 * (C.JSC_CLAIMED / C.JSC_CSI_TABLE - 1)))
    print("  in series that a silicon cell does not have.")


if __name__ == "__main__":
    main()
