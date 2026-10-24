"""Sections 3 and 4: the CISS polarisation and the Pauli spin blockade.

Section 4.1 gives a closed expression for the suppression of bimolecular
recombination,

    beta_eff = beta_L (1 - eta_PB P_CISS^2),   eta_PB = exp(-tau_ext / tau_s),

works it for P_CISS = 0.85 and eta_PB = 0.95, and reports 68.6% suppression.
Every quantity in that expression is given elsewhere in the same section, so the
whole chain can be closed with the preprint's own numbers.
"""
import numpy as np

import constants as C

KT_STC = C.BOLTZMANN * C.TEMPERATURE_STC / C.ELEMENTARY_CHARGE     # eV


def suppression(polarisation, eta_pb):
    return eta_pb * polarisation ** 2


def transit_time(mobility_cm2, thickness_m=C.THICKNESS_ACTIVE,
                 field_volts=C.V_INTERNAL):
    """tau_ext = d^2 / (2 mu V), with mu in cm^2/Vs and d in m."""
    d_cm = thickness_m * 100.0
    return d_cm ** 2 / (2 * mobility_cm2 * field_volts)


def main():
    print("=" * 78)
    print("The published arithmetic of section 4.1")
    print("=" * 78)
    s = suppression(C.P_CISS, C.ETA_PB_CLAIMED)
    print("  1 - eta_PB P^2 = 1 - %.2f x %.2f^2 = %.4f"
          % (C.ETA_PB_CLAIMED, C.P_CISS, 1 - s))
    print("  section 4.1 states beta_eff = 0.314 beta_L and 68.6% suppression")
    print("  measured: beta_eff = %.4f beta_L, suppression %.2f%%"
          % (1 - s, 100 * s))
    print("  correct as written.")
    print()

    print("=" * 78)
    print("eta_PB against the two times the same section gives for it")
    print("=" * 78)
    print("  eta_PB = exp(-tau_ext / tau_s), with tau_s = %.0f us and"
          % (1e6 * C.TAU_SPIN))
    print("  tau_ext = 20 to 80 ns, both from section 4.1 itself.")
    print()
    print("  %-12s %10s %16s %14s" % ("tau_ext", "eta_PB", "beta_eff/beta_L",
                                      "suppression"))
    for tau in C.TAU_EXT_QUOTED:
        eta = np.exp(-tau / C.TAU_SPIN)
        print("  %7.0f ns  %10.4f %16.4f %13.1f%%"
              % (1e9 * tau, eta, 1 - suppression(C.P_CISS, eta),
                 100 * suppression(C.P_CISS, eta)))
    needed = -np.log(C.ETA_PB_CLAIMED) * C.TAU_SPIN
    print()
    print("  The stated eta_PB = 0.95 corresponds to tau_ext = %.0f ns, not to"
          % (1e9 * needed))
    print("  the 20-80 ns the same sentence gives.  The error is in the")
    print("  preprint's own disfavour: its own times give eta_PB = 0.984 to")
    print("  0.996 and a suppression of %.1f%% rather than 68.6%%, so the"
          % (100 * suppression(C.P_CISS, np.exp(-C.TAU_EXT_QUOTED[0]
                                                / C.TAU_SPIN))))
    print("  conclusion of section 4.1 survives this correction and improves.")
    print()

    print("=" * 78)
    print("But tau_ext follows from the mobility, which is the weak point")
    print("=" * 78)
    print("  Section 4.1 defines tau_ext = d^2 / (2 mu V_int).  With the 220 nm")
    print("  active layer of table 1 and V_int = %.1f V, the transit time is set"
          % C.V_INTERNAL)
    print("  by the mobility - and section 1 introduces organic blends as having")
    print("  'low carrier mobilities' without giving a value.")
    print()
    print("  %-14s %11s %10s %16s %14s"
          % ("mu (cm^2/Vs)", "tau_ext", "eta_PB", "beta_eff/beta_L",
             "suppression"))
    lo, hi = C.MOBILITY_RANGE
    for mobility in np.logspace(np.log10(lo), np.log10(hi), 5):
        tau = transit_time(mobility)
        eta = np.exp(-tau / C.TAU_SPIN)
        print("  %-14.1e %8.0f ns %10.4f %16.4f %13.1f%%"
              % (mobility, 1e9 * tau, eta, 1 - suppression(C.P_CISS, eta),
                 100 * suppression(C.P_CISS, eta)))
    print()
    tau_lo = transit_time(lo)
    print("  At the bottom of the range, where a disordered blend actually sits,")
    print("  the transit time is %.1f us, comparable with the %.0f us spin"
          % (1e6 * tau_lo, 1e6 * C.TAU_SPIN))
    print("  lifetime rather than negligible against it, and the suppression")
    print("  falls to %.1f%%.  The 20-80 ns quoted in section 4.1 needs"
          % (100 * suppression(C.P_CISS, np.exp(-tau_lo / C.TAU_SPIN))))
    for tau in C.TAU_EXT_QUOTED:
        mu_needed = (C.THICKNESS_ACTIVE * 100.0) ** 2 / (2 * tau * C.V_INTERNAL)
        print("    tau_ext = %3.0f ns  ->  mu = %.1e cm^2/Vs"
              % (1e9 * tau, mu_needed))
    print("  which is one to two orders above a disordered bulk heterojunction")
    print("  and at or beyond the best ordered organic films.  So the")
    print("  mechanism's margin, tau_ext << tau_s, is real at high mobility and")
    print("  gone at low mobility, and the preprint asserts the high end while")
    print("  its introduction argues the low end.")
    print()

    print("=" * 78)
    print("The spin statistics the suppression is measured against")
    print("=" * 78)
    print("  Section 1 states that uncorrelated encounters form 25% singlet and")
    print("  75% triplet, and section 4.1 blocks the triplet channel.  If the")
    print("  triplet channel is blocked, what is left is the singlet fraction:")
    print("    achiral device, spin statistics alone      beta_eff = 0.250 beta_L")
    print("    section 4.1, chiral, P = 0.85              beta_eff = %.3f beta_L"
          % (1 - s))
    print("  The chiral result is the larger of the two.  Unless beta_L is read")
    print("  as the spin-blind Langevin coefficient - in which case an ordinary")
    print("  achiral blend should already show 0.250 - the expression as written")
    print("  does not improve on the statistics it replaces.  Reference [3],")
    print("  Rao et al. 2013, which the preprint cites for the triplet drain, is")
    print("  precisely the measurement of this spin control in achiral blends.")
    print()

    print("=" * 78)
    print("What P_CISS = tanh(dE / 2kT) commits the design to")
    print("=" * 78)
    print("  Read as written, the polarisation is a thermal population ratio, so")
    print("  a polarisation measured at 300 K fixes the splitting:")
    print()
    print("  %-14s %18s" % ("P_CISS", "required dE (meV)"))
    for pol in (C.P_CISS_RANGE[0], C.P_CISS, C.P_CISS_RANGE[1]):
        print("  %-14.2f %15.1f" % (pol, 1000 * 2 * KT_STC * np.arctanh(pol)))
    print()
    de = 2 * KT_STC * np.arctanh(C.P_CISS)
    print("  Holding that splitting fixed at %.1f meV, the same formula then"
          % (1000 * de))
    print("  predicts how the whole mechanism behaves with temperature - and a")
    print("  solar cell does not run at 25 C:")
    print()
    print("  %-12s %10s %16s %14s" % ("T (degC)", "P_CISS", "beta_eff/beta_L",
                                      "suppression"))
    for celsius in C.TEMPERATURE_SWEEP_C:
        kt = C.BOLTZMANN * (273.15 + celsius) / C.ELEMENTARY_CHARGE
        pol = np.tanh(de / (2 * kt))
        eta = np.exp(-transit_time(1e-3) / C.TAU_SPIN)
        print("  %-12.0f %10.3f %16.4f %13.1f%%"
              % (celsius, pol, 1 - suppression(pol, eta),
                 100 * suppression(pol, eta)))
    print()
    print("  This is a prediction, and a testable one: the suppression weakens")
    print("  as the module heats up and strengthens in the cold.  Section 4.2")
    print("  claims the opposite advantage, better low-irradiance winter")
    print("  behaviour, for unrelated reasons; this is the cleaner signature.")
    print()

    print("=" * 78)
    print("xi_SOC proportional to Z^4")
    print("=" * 78)
    print("  Section 1 justifies the weak spin-orbit coupling of carbon with")
    print("  'xi_SOC proportional to Z^4'.  Z^4 is the hydrogenic fine-structure")
    print("  scaling, for an electron in a bare nuclear potential.  The")
    print("  electrons that carry spin in a conjugated polymer are valence p")
    print("  electrons, screened, and the exponent can be measured: the ground")
    print("  term splitting of the halogens is exactly one valence np shell")
    print("  stepped down one column of the periodic table.")
    print()
    z = np.array([row[0] for row in C.HALOGEN_SOC], dtype=float)
    split = np.array([row[1] for row in C.HALOGEN_SOC])
    print("  %-8s %-6s %18s" % ("element", "Z", "2P(3/2)-2P(1/2) (1/cm)"))
    for (zz, ss), name in zip(C.HALOGEN_SOC, ("F", "Cl", "Br", "I")):
        print("  %-8s %-6d %18.3f" % (name, zz, ss))
    slope, intercept = np.polyfit(np.log(z), np.log(split), 1)
    residual = np.exp(intercept) * z ** slope / split
    print()
    print("  least-squares fit of ln(splitting) against ln(Z):")
    print("    measured exponent          %.2f" % slope)
    print("    claimed in section 1       %.1f" % C.SOC_EXPONENT_CLAIMED)
    print("    valence scaling in the review literature  %.1f"
          % C.SOC_EXPONENT_VALENCE)
    print("    worst fit residual         %.0f%%" % (100 * abs(residual - 1).max()))
    print()
    print("  So the exponent is %.2f, below even the Z^2 the review literature"
          % slope)
    print("  gives for outermost electrons, and far from 4.  It does not change")
    print("  the conclusion: from carbon to lead the measured trend still gives")
    for exponent, label in ((slope, "measured"), (C.SOC_EXPONENT_VALENCE, "Z^2"),
                            (C.SOC_EXPONENT_CLAIMED, "Z^4 as claimed")):
        print("    %-16s factor %9.0f between Z = 6 and Z = 82"
              % (label, (82.0 / C.Z_CARBON) ** exponent))
    print("  Carbon's advantage is real whichever exponent is used.  Only the")
    print("  size of it, and the law quoted for it, are wrong.")


if __name__ == "__main__":
    main()
