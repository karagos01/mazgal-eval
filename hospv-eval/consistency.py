#!/usr/bin/env python3
"""The same quantity twice: the preprint measured against itself.

The findings in the other scripts here are of two kinds.  Some compare a claim
with the outside world - a spectrum, a measured chromophore, a Neel temperature.
Others never leave the document: a quantity is given one value in one place and
a different value in another, or a value is stated in a sentence whose own other
numbers imply a different one.  Only the second kind is collected here, because
it needs no model to adjudicate and no source to trust.  Each row is recomputed
from constants.py and from the same functions the topical scripts use, so no
number is defined twice in this repository.

The test applied to a row is deliberately narrow: both values must come from the
preprint, and the arithmetic connecting them must be the preprint's own.  That
excludes the 45.9% claim of section 2.2, which needs reference [5] to settle,
and the 0.90 V radiative limit of section 6.2, which needs a detailed-balance
model; those are in detailed_balance.py.
"""
import numpy as np

import constants as C
from materials import stack
from photocurrent import threshold_for
from spectrum import current_density, load_spectrum
from spin import transit_time

KT_STC = C.BOLTZMANN * C.TEMPERATURE_STC / C.ELEMENTARY_CHARGE     # eV
W = 78


def item(n, title, rows, gap):
    print("  %d. %s" % (n, title))
    for where, value in rows:
        print("       %-18s %s" % (where, value))
    print("       %-18s %s" % ("disagreement", gap))
    print()


def mobility_for(tau):
    """Invert tau_ext = d^2 / (2 mu V) for mu, in cm^2/Vs."""
    d_cm = C.THICKNESS_ACTIVE * 100.0
    return d_cm ** 2 / (2 * tau * C.V_INTERNAL)


def main():
    energy, flux, _power = load_spectrum()
    eqe_high = C.ETA_SF * C.ETA_DET * C.EQE_BHJ

    # --- the quantities each of the disagreements rests on ---------------
    edge_ev, edge_nm = threshold_for(energy, flux, C.JSC_SF_CLAIMED / eqe_high)
    chain_floor = 2 * C.E_GAP_IR                   # section 2.2's own ordering
    first_link = 2 * C.E_T1_DONOR
    jsc_high = current_density(energy, flux, C.E_S1_DONOR)
    per_photon = C.JSC_SF_CLAIMED / jsc_high
    tau_for_claim = -np.log(C.ETA_PB_CLAIMED) * C.TAU_SPIN
    eta_from_taus = tuple(np.exp(-t / C.TAU_SPIN) for t in C.TAU_EXT_QUOTED)
    mu_needed = tuple(mobility_for(t) for t in C.TAU_EXT_QUOTED)
    split_from_p = 2 * KT_STC * np.arctanh(C.P_CISS)
    areal_mass = sum(m for _n, m in stack(1.2, 2.0, 150e-9))
    specific_power = C.PCE_CLAIMED * 1000.0 / (areal_mass / 1000.0)

    print("=" * W)
    print("Quantities the preprint gives two values for")
    print("=" * W)
    print("  Both values in every row are the preprint's own, and so is the")
    print("  arithmetic between them.")
    print()

    item(1, "The absorption edge of the fission donor",
         [("section 2.2", "%.2f eV (%.0f nm), stated"
           % (C.E_S1_DONOR, C.LAMBDA_DONOR_NM)),
          ("section 6.2", "%.2f eV (%.0f nm), the edge its own %.1f mA/cm^2"
           % (edge_ev, edge_nm, C.JSC_SF_CLAIMED)),
          ("", "needs at its own EQE_high = %.2f" % eqe_high)],
         "%.0f meV" % (1000 * (C.E_S1_DONOR - edge_ev)))

    item(2, "E(S1) of the donor",
         [("section 2.2", "%.2f eV, stated" % C.E_S1_DONOR),
          ("section 2.1", "at least %.2f eV, required by E(S1) >= 2 E(T1)"
           % first_link)],
         "%.0f meV, so the fission is endothermic by %.1f kT"
         % (1000 * (first_link - C.E_S1_DONOR),
            (first_link - C.E_S1_DONOR) / KT_STC))

    item(3, "Electrons per absorbed photon above the edge",
         [("section 6.2", "%.2f, stated as EQE_high = %.0f%%"
           % (eqe_high, 100 * eqe_high)),
          ("section 6.2", "%.2f, required by its own %.1f mA/cm^2 over the"
           % (per_photon, C.JSC_SF_CLAIMED)),
          ("", "%.2f mA/cm^2 the spectrum carries above %.2f eV"
           % (jsc_high, C.E_S1_DONOR))],
         "%.0f%%, and %.0f%% over fission's own ceiling of two"
         % (100 * (per_photon / eqe_high - 1), 100 * (per_photon / 2 - 1)))

    item(4, "tau_ext, the extraction transit time",
         [("section 4.1", "%.0f to %.0f ns, stated"
           % (1e9 * C.TAU_EXT_QUOTED[0], 1e9 * C.TAU_EXT_QUOTED[1])),
          ("section 4.1", "%.0f ns, required by its own eta_PB = %.2f through"
           % (1e9 * tau_for_claim, C.ETA_PB_CLAIMED)),
          ("", "its own eta_PB = exp(-tau_ext / tau_s), tau_s = %.0f us"
           % (1e6 * C.TAU_SPIN))],
         "a factor %.1f to %.1f, in the preprint's favour"
         % (tau_for_claim / C.TAU_EXT_QUOTED[1],
            tau_for_claim / C.TAU_EXT_QUOTED[0]))

    item(5, "eta_PB, the same inconsistency read the other way",
         [("section 4.1", "%.2f, stated" % C.ETA_PB_CLAIMED),
          ("section 4.1", "%.4f to %.4f, from the two times in the same"
           % (eta_from_taus[1], eta_from_taus[0])),
          ("", "sentence; the suppression is then %.1f%%, not %.1f%%"
           % (100 * eta_from_taus[1] * C.P_CISS ** 2,
              100 * C.SUPPRESSION_CLAIMED))],
         "%.1f points of suppression, in the preprint's favour"
         % (100 * (eta_from_taus[1] * C.P_CISS ** 2 - C.SUPPRESSION_CLAIMED)))

    item(6, "Carrier mobility of the active layer",
         [("section 1", "\"low carrier mobilities\", no number, used to"),
          ("", "introduce the recombination problem"),
          ("section 4.1", "%.1e to %.1e cm^2/Vs, required by the %.0f to"
           % (mu_needed[1], mu_needed[0], 1e9 * C.TAU_EXT_QUOTED[0])),
          ("", "%.0f ns above through tau_ext = d^2/(2 mu V) and"
           % (1e9 * C.TAU_EXT_QUOTED[1])),
          ("", "table 1's %.0f nm" % (1e9 * C.THICKNESS_ACTIVE))],
         "one to two orders of magnitude, against itself")

    item(7, "Spin splitting the mechanism runs on",
         [("table 1, layer 6", "~%.1f eV, and %.1f to %.1f eV in section 5.1"
           % (C.SPIN_SPLIT_TABLE, C.SPIN_SPLIT_CLAIMED[0],
              C.SPIN_SPLIT_CLAIMED[1])),
          ("section 4.1", "%.1f meV, required by its own P_CISS = %.2f through"
           % (1000 * split_from_p, C.P_CISS)),
          ("", "its own P_CISS = tanh(dE / 2kT) at %.2f K"
           % C.TEMPERATURE_STC)],
         "a factor %.1f" % (C.SPIN_SPLIT_TABLE / split_from_p))

    item(8, "Specific power of the cell",
         [("table 2", "at least %.0f W/kg, stated" % C.SPECIFIC_POWER_CLAIMED),
          ("table 1", "%.0f W/kg, from its own seven thicknesses at its own"
           % specific_power),
          ("", "PCE of %.2f%%, %.1f g/m^2 of stack"
           % (100 * C.PCE_CLAIMED, areal_mass))],
         "a factor %.1f" % (C.SPECIFIC_POWER_CLAIMED / specific_power))

    print("=" * W)
    print("What holds")
    print("=" * W)
    print("  The same test applied to every other quantity that appears twice.")
    print("  Each of these is a single expression evaluated inside one")
    print("  sentence, and each comes out right:")
    print()
    checks = [
        ("EQE_high = %.2f x %.2f x %.2f" % (C.ETA_SF, C.ETA_DET, C.EQE_BHJ),
         "%.4f" % eqe_high, "%.0f%% (6.2)" % (100 * C.EQE_HIGH_CLAIMED),
         abs(eqe_high - C.EQE_HIGH_CLAIMED) < 0.005),
        ("1 - eta_PB P_CISS^2",
         "%.4f" % (1 - C.ETA_PB_CLAIMED * C.P_CISS ** 2),
         "0.314 (4.1)", abs((1 - C.ETA_PB_CLAIMED * C.P_CISS ** 2)
                                     - 0.314) < 0.0005),
        ("the suppression that follows",
         "%.1f%%" % (100 * C.ETA_PB_CLAIMED * C.P_CISS ** 2),
         "%.1f%% (4.1)" % (100 * C.SUPPRESSION_CLAIMED),
         abs(C.ETA_PB_CLAIMED * C.P_CISS ** 2
             - C.SUPPRESSION_CLAIMED) < 0.0005),
        ("P_CISS of the worked example", "%.2f" % C.P_CISS,
         "%.2f-%.2f (3.2)" % C.P_CISS_RANGE,
         C.P_CISS_RANGE[0] <= C.P_CISS <= C.P_CISS_RANGE[1]),
        ("splitting of table 1", "%.1f eV" % C.SPIN_SPLIT_TABLE,
         "%.1f-%.1f eV (5.1)" % C.SPIN_SPLIT_CLAIMED,
         C.SPIN_SPLIT_CLAIMED[0] <= C.SPIN_SPLIT_TABLE
         <= C.SPIN_SPLIT_CLAIMED[1]),
        ("V_oc = %.2f V - %.2f V" % (C.VOC_RAD_CLAIMED, C.DVOC_NR_CLAIMED),
         "%.2f V" % (C.VOC_RAD_CLAIMED - C.DVOC_NR_CLAIMED),
         "%.2f V (6.2)" % C.VOC_CLAIMED,
         abs(C.VOC_RAD_CLAIMED - C.DVOC_NR_CLAIMED - C.VOC_CLAIMED) < 0.005),
        # J_sc in mA/cm^2 times V is mW/cm^2, and P_in = 100 mW/cm^2, so the
        # product is already the efficiency in percent.
        ("PCE = J_sc V_oc FF / P_in",
         "%.2f%%" % (C.JSC_CLAIMED * C.VOC_CLAIMED * C.FF_CLAIMED),
         "%.2f%% (6.2)" % (100 * C.PCE_CLAIMED),
         abs(C.JSC_CLAIMED * C.VOC_CLAIMED * C.FF_CLAIMED
             - 100 * C.PCE_CLAIMED) < 0.005),
        ("2 E(T1) >= 2 E_g(IR), the second link",
         "%.2f >= %.2f eV" % (first_link, chain_floor),
         "required by 2.2", first_link >= chain_floor),
    ]
    print("  %-37s %12s  %-16s %s"
          % ("quantity", "recomputed", "as published", "check"))
    print("  " + "-" * (W - 4))
    for name, got, published, ok in checks:
        print("  %-37s %12s  %-16s %s"
              % (name, got, published, "ok" if ok else "MISMATCH"))
    print()
    held = sum(1 for check in checks if check[3])
    print("  %d of %d hold.  Every arithmetic step the preprint performs it"
          % (held, len(checks)))
    print("  performs correctly.  What disagrees is never the algebra; it is")
    print("  always the numbers put into it.")
    print()

    print("=" * W)
    print("Row 1 is not an inconsistency but an exclusion")
    print("=" * W)
    print("  The other seven rows could each be repaired by choosing one of")
    print("  the two values.  Row 1 cannot, because section 2.2's own")
    print("  thermodynamic ordering fixes which value is allowed:")
    print()
    print("      E(S1_D) >= 2 E(T1_D) >= 2 E_CT >= 2 E_g(IR)")
    print()
    print("  2 E_g(IR) = %.2f eV, so the chain forbids any donor whose S1 lies"
          % chain_floor)
    print("  below that.  The edge its photocurrent needs is %.2f eV, which is"
          % edge_ev)
    print("  %.0f meV below the floor." % (1000 * (chain_floor - edge_ev)))
    print()
    print("  Read the other way, a donor with E(S1) = %.2f eV may have at most"
          % edge_ev)
    print("  E(T1) = %.2f eV, and that is %.0f meV *below* the %.2f eV gap of"
          % (edge_ev / 2, 1000 * (C.E_GAP_IR - edge_ev / 2), C.E_GAP_IR))
    print("  the acceptor it is supposed to feed, so the Dexter step of")
    print("  section 2.2 would run uphill and the cascade would not exist.")
    print()
    print("  So the two values are mutually exclusive rather than merely")
    print("  different: either the high-energy channel carries %.2f mA/cm^2"
          % (jsc_high * eqe_high))
    print("  and not %.1f, or the energy cascade the architecture is built"
          % C.JSC_SF_CLAIMED)
    print("  from is thermodynamically forbidden.  Nothing outside the")
    print("  preprint is needed to reach that.")


if __name__ == "__main__":
    main()
