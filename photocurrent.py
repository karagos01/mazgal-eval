"""Section 6.2: the photocurrent integral, channel by channel.

Section 6.2 writes J_sc as the sum of a direct infrared channel and a
singlet-fission-multiplied high-energy channel, states the quantum efficiencies
it uses for each, and reports a number for each.  Both integrals are evaluated
here against the ASTM G173-03 spectrum, with the preprint's own efficiencies.
"""
import numpy as np

import constants as C
from spectrum import current_density, load_spectrum


def threshold_for(energy, flux, target_ma):
    """The photon energy above which the one-electron current equals target_ma.
    Returns (eV, nm)."""
    grid = np.arange(1.0, 3.0, 0.002)
    for threshold in grid:
        if current_density(energy, flux, threshold) < target_ma:
            return threshold, C.HC_EV_NM / threshold
    return float("nan"), float("nan")


def recomputed():
    """J_sc (mA/cm^2) and PCE from the preprint's own quantum efficiencies and
    the reference spectrum, with its V_oc and FF left untouched.  Imported by
    materials.py so that the figure is defined in one place only."""
    energy, flux, _power = load_spectrum()
    eqe_high = C.ETA_SF * C.ETA_DET * C.EQE_BHJ
    jsc = (current_density(energy, flux, C.E_GAP_IR, C.E_S1_DONOR) * C.EQE_IR
           + current_density(energy, flux, C.E_S1_DONOR) * eqe_high)
    return jsc, jsc * C.VOC_CLAIMED * C.FF_CLAIMED / 100.0


def main():
    energy, flux, power = load_spectrum()
    eqe_high = C.ETA_SF * C.ETA_DET * C.EQE_BHJ

    print("=" * 78)
    print("The multiplication factor of the high-energy channel")
    print("=" * 78)
    print("  eta_SF x eta_DET x EQE_BHJ = %.2f x %.2f x %.2f = %.4f"
          % (C.ETA_SF, C.ETA_DET, C.EQE_BHJ, eqe_high))
    print("  section 6.2 calls this EQE_high = 153% in the blue-green: correct")
    print()

    print("=" * 78)
    print("The two channels of section 6.2")
    print("=" * 78)
    ceil_ir = current_density(energy, flux, C.E_GAP_IR, C.E_S1_DONOR)
    ceil_sf = current_density(energy, flux, C.E_S1_DONOR)
    j_ir = ceil_ir * C.EQE_IR
    j_sf = ceil_sf * eqe_high
    print("  %-46s %9s %9s" % ("", "measured", "claimed"))
    print("  %-46s %8.2f  %8.2f" % ("IR channel, 1.12-2.25 eV, at EQE = 0.85",
                                    j_ir, C.JSC_IR_CLAIMED))
    print("  %-46s %8.2f  %8.2f" % ("SF channel, above 2.25 eV, at EQE = 1.53",
                                    j_sf, C.JSC_SF_CLAIMED))
    print("  %-46s %8.2f  %8.2f" % ("total J_sc, mA/cm^2",
                                    j_ir + j_sf, C.JSC_CLAIMED))
    print()
    print("  The infrared channel is right: 28.5 claimed against %.2f measured,"
          % j_ir)
    print("  an error of %.1f%%, which is within the accuracy of reading a"
          % (100 * abs(j_ir - C.JSC_IR_CLAIMED) / j_ir))
    print("  spectrum off a chart.")
    print()
    print("  The high-energy channel is not.  Photons above 2.25 eV carry")
    print("  %.2f mA/cm^2 of charge if every one of them makes exactly one"
          % ceil_sf)
    print("  electron.  The claimed 23.8 mA/cm^2 therefore needs")
    print("    EQE_high = 23.8 / %.2f = %.0f%%" % (ceil_sf,
                                                   100 * C.JSC_SF_CLAIMED / ceil_sf))
    print("  that is, %.2f electrons per absorbed photon."
          % (C.JSC_SF_CLAIMED / ceil_sf))
    print("  Singlet fission gives at most two.  The claim exceeds the ceiling of")
    print("  its own mechanism by %.0f%%, and exceeds the 153%% it states by %.0f%%."
          % (100 * (C.JSC_SF_CLAIMED / ceil_sf / 2.0 - 1),
             100 * (C.JSC_SF_CLAIMED / ceil_sf / eqe_high - 1)))
    print()
    print("  Where the number could come from: 23.8 mA/cm^2 at EQE_high = 1.53")
    print("  is the current of all photons above %.2f eV, that is above %.0f nm,"
          % threshold_for(energy, flux, C.JSC_SF_CLAIMED / eqe_high))
    print("  rather than above the 2.25 eV / 551 nm the same sentence")
    print("  specifies - a shift of %.0f meV."
          % (1000 * (C.E_S1_DONOR
                     - threshold_for(energy, flux,
                                      C.JSC_SF_CLAIMED / eqe_high)[0])))
    print()

    print("=" * 78)
    print("What the architecture's current can be")
    print("=" * 78)
    rows = (
        ("the preprint's own efficiencies", C.EQE_IR, eqe_high),
        ("perfect transfer and collection, eta_SF = 1.85", 1.0, C.ETA_SF),
        ("perfect everything, two triplets per singlet", 1.0, 2.0),
    )
    for label, w_ir, w_sf in rows:
        total = ceil_ir * w_ir + ceil_sf * w_sf
        print("  %-48s %6.2f mA/cm^2" % (label, total))
    plain = current_density(energy, flux, C.E_GAP_IR)
    print()
    print("  For comparison, a plain 1.12 eV absorber with EQE = 1 and no fission")
    print("  at all collects %.2f mA/cm^2." % plain)
    print("  With the preprint's own quantum efficiencies the whole")
    print("  fission-plus-Dexter cascade returns %.2f mA/cm^2, which is the same"
          % (ceil_ir * C.EQE_IR + ceil_sf * eqe_high))
    print("  number to within %.1f%%: the multiplication pays for the 0.85, 0.92"
          % (100 * abs(ceil_ir * C.EQE_IR + ceil_sf * eqe_high - plain) / plain))
    print("  and 0.90 and nothing more.  The gain over silicon in this")
    print("  architecture is not in the current; it is in collecting that current")
    print("  at a voltage set by the 1.12 eV gap while the 0.85 and 0.90 losses")
    print("  are absorbed by the doubling.")
    print()

    print("=" * 78)
    print("Section 6.2's efficiency, recomputed")
    print("=" * 78)
    measured = ceil_ir * C.EQE_IR + ceil_sf * eqe_high
    print("  %-52s %6s %8s" % ("", "J_sc", "PCE"))
    print("  %-52s %6.2f %7.2f%%"
          % ("as published", C.JSC_CLAIMED,
             100 * C.JSC_CLAIMED * C.VOC_CLAIMED * C.FF_CLAIMED / 100.0))
    print("  %-52s %6.2f %7.2f%%"
          % ("with J_sc from the preprint's own efficiencies", measured,
             100 * measured * C.VOC_CLAIMED * C.FF_CLAIMED / 100.0))
    print("  %-52s %6.2f %7.2f%%"
          % ("with perfect fission, transfer and collection",
             ceil_ir + 2 * ceil_sf,
             100 * (ceil_ir + 2 * ceil_sf) * C.VOC_CLAIMED * C.FF_CLAIMED / 100.0))
    print()
    print("  The published arithmetic is internally consistent:")
    print("    52.3 x 0.81 x 0.840 / 100 = %.4f, printed as 35.58%%"
          % (C.JSC_CLAIMED * C.VOC_CLAIMED * C.FF_CLAIMED / 100.0))
    print("  It is the current entering it that the spectrum does not support.")
    print()

    print("=" * 78)
    print("Can 220 nm of active layer absorb both bands?")
    print("=" * 78)
    print("  Section 1 gives alpha ~ 1e5 /cm for organic absorbers; table 1 gives")
    print("  a single 220 nm active layer holding both the fission donor and the")
    print("  infrared acceptor, with a back reflector behind it.  Each absorber")
    print("  therefore sees only its own share of the thickness.")
    print()
    print("  %-10s %12s %14s %16s" % ("acceptor", "its path", "single pass",
                                      "with reflector"))
    lo, hi = C.ACCEPTOR_VOLUME_FRACTION
    for frac in np.linspace(lo, hi, 5):
        path = frac * C.THICKNESS_ACTIVE * 100.0          # cm
        one = 1 - np.exp(-C.ALPHA_ABSORPTION * path)
        two = 1 - np.exp(-2 * C.ALPHA_ABSORPTION * path)
        print("  %-10.0f%% %10.0f nm %13.1f%% %15.1f%%"
              % (100 * frac, 1e9 * frac * C.THICKNESS_ACTIVE, 100 * one, 100 * two))
    print()
    for target, label in ((C.EQE_IR, "the 0.85 the infrared channel assumes"),
                          (C.EQE_BHJ, "the 0.90 the fission channel assumes")):
        path = 0.5 * C.THICKNESS_ACTIVE * 100.0
        need = -np.log(1 - target) / (2 * path)
        print("  To reach %s at an even 50:50 split," % label)
        print("  double pass, needs alpha >= %.2e /cm over the whole band." % need)
    print()
    print("  At the peak of an organic absorption band 1e5 /cm is ordinary, so")
    print("  both numbers are reachable there.  The requirement is that alpha")
    print("  stay near its peak across 1.12-2.25 eV for the acceptor, a 556 nm")
    print("  wide window ending at its own absorption edge, where alpha of any")
    print("  real absorber falls away.  This is not quantified here; it is")
    print("  flagged as the assumption the 0.85 rests on.")


if __name__ == "__main__":
    main()
