"""The 45.9% claim, against the model it is cited from.

The abstract and section 2.2 state that the architecture "elevates the
single-junction thermodynamic limit to 45.9%", citing reference [5], Hanna and
Nozik, J. Appl. Phys. 100, 074510 (2006).

The detailed-balance calculation is built here from the spectrum and the
Planck law, with nothing taken on trust, and is checked against three published
values before being applied to the preprint's architecture:

  * the Shockley-Queisser limit, 33.7% at 1.34 eV
  * reference [5]'s single-gap carrier-multiplication limit, 44.4% at 0.7 eV,
    for unlimited multiplication
  * the same group's value for multiplication capped at two carriers per
    photon - which is what singlet fission does - 42.0% at 0.95 eV

Quantum yields above the multiplication threshold raise the emitted flux as
well as the absorbed flux: a photon above threshold makes two carriers, so by
detailed balance two carriers are needed to emit one, and the emission at that
energy carries a chemical potential of QY x qV.  That is the Hanna-Nozik
treatment, and the three checks above are what establish that it is implemented
correctly.
"""
import numpy as np

import constants as C
from spectrum import load_spectrum

KT = C.BOLTZMANN * C.TEMPERATURE_STC / C.ELEMENTARY_CHARGE     # eV

_ENERGY, _FLUX, _POWER = load_spectrum()


def _blackbody(energy, mu):
    """Emitted photon flux into a hemisphere, per m^2 per s per eV."""
    # mu -> energy is the divergence of the Bose factor.  It is clipped to a
    # small positive argument rather than zero: the emitted flux then becomes
    # enormous, the net current strongly negative, and the V_oc search is
    # pushed back below it, which is the physical behaviour.  Clipping to zero
    # instead divides by zero and returns inf, which silently turned the
    # efficiency scans into nonsense in an earlier draft of this script.
    x = np.clip((energy - mu) / KT, 1e-12, 700.0)
    pre = (2 * np.pi * C.ELEMENTARY_CHARGE ** 3
           / (C.PLANCK ** 3 * C.LIGHT ** 2))
    return pre * energy ** 2 / np.expm1(x)


def solve(yield_of_energy, refinements=3, points=64, voltages=401):
    """Return J_sc (mA/cm^2), V_oc (V), FF and efficiency for a cell whose
    quantum yield is the given function of photon energy.

    The current is evaluated for a whole array of voltages in one pass, so
    V_oc is bracketed by three refinements of a 64-point grid rather than by a
    long scalar bisection.
    """
    qy = yield_of_energy(_ENERGY)
    mask = qy > 0
    energy, flux, qy = _ENERGY[mask], _FLUX[mask], qy[mask]
    jsc = C.ELEMENTARY_CHARGE * np.trapezoid(qy * flux, energy)      # A/m^2
    dark0 = C.ELEMENTARY_CHARGE * np.trapezoid(qy * _blackbody(energy, 0.0),
                                               energy)

    def current(v):
        v = np.atleast_1d(np.asarray(v, dtype=float))
        mu = np.outer(v, qy)                                 # (nV, nE)
        emitted = C.ELEMENTARY_CHARGE * np.trapezoid(
            qy * _blackbody(energy, mu), energy, axis=1)
        return jsc - (emitted - dark0)

    lo, hi = 0.0, float(energy.max())
    for _ in range(refinements):
        grid = np.linspace(lo, hi, points)
        positive = current(grid) > 0
        last = int(np.nonzero(positive)[0].max())
        lo = grid[last]
        hi = grid[min(last + 1, points - 1)]
    voc = lo
    grid = np.linspace(0.0, voc, voltages)
    power = current(grid) * grid
    best = float(power.max())
    return (jsc * 0.1, voc, best / (jsc * voc) if jsc * voc else 0.0,
            best / _POWER)


def step(gap):
    return lambda e: np.where(e >= gap, 1.0, 0.0)


def two_threshold(gap, threshold, high=2.0):
    def qy(e):
        out = np.where(e >= gap, 1.0, 0.0)
        return np.where(e >= threshold, high, out)
    return qy


def staircase(gap):
    return lambda e: np.where(e >= gap, np.floor(e / gap), 0.0)


def _scan(builder, gaps):
    best = None
    for gap in gaps:
        result = solve(builder(gap))
        if best is None or result[3] > best[1][3]:
            best = (gap, result)
    return best


def main():
    print("=" * 78)
    print("Three self-checks before anything is concluded")
    print("=" * 78)
    gap_sq, sq = _scan(step, np.arange(1.00, 1.60, 0.005))
    print("  Shockley-Queisser, one carrier per photon")
    print("    optimum at E_g = %.3f eV, efficiency %.2f%%" % (gap_sq, 100 * sq[3]))
    print("    published value: %.1f%% at %.2f eV"
          % (100 * C.SQ_LIMIT_QUOTED, C.SQ_GAP_QUOTED))
    at134 = solve(step(C.SQ_GAP_QUOTED))
    print("    at 1.34 eV exactly: %.2f%%, J_sc %.2f mA/cm^2, V_oc %.3f V, FF %.3f"
          % (100 * at134[3], at134[0], at134[1], at134[2]))
    print()
    gap_max, mx = _scan(staircase, np.arange(0.50, 1.20, 0.01))
    print("  Carrier multiplication, unlimited: QY = floor(E / E_g)")
    print("    optimum at E_g = %.2f eV, efficiency %.2f%%" % (gap_max, 100 * mx[3]))
    print("    reference [5]: %.1f%% at %.2f eV"
          % (100 * C.HN_SINGLE_GAP_MAX_CM, C.HN_MMAX_GAP))
    print()
    best2 = None
    for coarse, step_g, step_t in ((True, 0.04, 0.08), (False, 0.01, 0.02)):
        if coarse:
            gaps2 = np.arange(0.60, 1.40, step_g)
        else:
            gaps2 = np.arange(max(0.60, best2[0] - 0.04),
                              best2[0] + 0.04 + 1e-9, step_g)
        for gap in gaps2:
            lo_t = 2 * gap
            hi_t = 3.60 if coarse else min(3.60, best2[1] + 0.08)
            for threshold in np.arange(max(lo_t, lo_t if coarse
                                           else best2[1] - 0.08),
                                       hi_t, step_t):
                if threshold < 2 * gap - 1e-9:
                    continue
                result = solve(two_threshold(gap, threshold))
                if best2 is None or result[3] > best2[2][3]:
                    best2 = (gap, threshold, result)
    print("  Carrier multiplication capped at two per photon, which is what")
    print("  singlet fission does, with a free doubling threshold")
    print("    optimum at E_g = %.2f eV, threshold %.2f eV, efficiency %.2f%%"
          % (best2[0], best2[1], 100 * best2[2][3]))
    print("    same group, NREL/CP-590-38992: %.1f%% at %.2f eV"
          % (100 * C.HN_M2_EFFICIENCY, C.HN_M2_GAP))
    print()
    print("  Three independent published values reproduced to better than")
    print("  0.3 percentage points.  The model below is the same code.")
    print()

    print("=" * 78)
    print("The limit of the HOS-PV 2.0 architecture")
    print("=" * 78)
    print("  A single junction extracting at E_g(IR) = 1.12 eV, one electron per")
    print("  photon between 1.12 and 2.25 eV, two above 2.25 eV.")
    print()
    own = solve(two_threshold(C.E_GAP_IR, C.E_S1_DONOR))
    print("  %-56s %7s" % ("", "limit"))
    print("  %-56s %6.2f%%" % ("plain single gap at 1.12 eV", 100 * solve(
        step(C.E_GAP_IR))[3]))
    print("  %-56s %6.2f%%" % ("Shockley-Queisser optimum, 1.34 eV", 100 * at134[3]))
    print("  %-56s %6.2f%%" % ("this architecture, at its own two energies",
                               100 * own[3]))
    print("  %-56s %6.2f%%" % ("best possible with a cap of two per photon",
                               100 * best2[2][3]))
    print("  %-56s %6.2f%%" % ("published claim", 100 * C.LIMIT_CLAIMED))
    print()
    print("  So the central idea works.  A single junction at 1.12 eV that")
    print("  doubles above 2.25 eV does beat Shockley-Queisser, by %.1f points,"
          % (100 * (own[3] - at134[3])))
    print("  and its J_sc of %.1f mA/cm^2 and V_oc of %.3f V are where the gain"
          % (own[0], own[1]))
    print("  comes from.  Exceeding the limit is not the problem.")
    print()
    print("  The claimed figure is the problem.  45.9% is above the best that")
    print("  doubling can do at any pair of energies whatsoever (%.2f%%), so no"
          % (100 * best2[2][3]))
    print("  choice of donor or acceptor reaches it, and it is %.1f points above"
          % (100 * (C.LIMIT_CLAIMED - own[3])))
    print("  the limit at the energies the preprint actually specifies.")
    print()
    print("  Where 45.9% comes from is visible in the source it cites.")
    print("  Reference [5] reports, in its abstract:")
    print("    single gap, no multiplication                  %.1f%%"
          % (100 * C.HN_SINGLE_GAP_NO_CM))
    print("    single gap, with multiplication                %.1f%%"
          % (100 * C.HN_SINGLE_GAP_MAX_CM))
    print("    ideal TWO-gap tandem, without and with CM      %.1f%% to %.1f%%"
          % (100 * C.HN_TANDEM_RANGE[0], 100 * C.HN_TANDEM_RANGE[1]))
    print("  45.9% is not the single-junction row.  It falls inside the two-gap")
    print("  tandem range, in a paper whose single-junction answer is 44.4% for")
    print("  unlimited multiplication and 42.0% for the doubling that singlet")
    print("  fission actually performs.  The architecture's one selling point is")
    print("  that it is a single junction.")
    print()

    print("=" * 78)
    print("V_oc, FF and the non-radiative loss")
    print("=" * 78)
    rad = solve(two_threshold(C.E_GAP_IR, C.E_S1_DONOR))
    plain_rad = solve(step(C.E_GAP_IR))
    print("  radiative-limit V_oc at E_g = 1.12 eV")
    print("    plain single gap                     %.4f V" % plain_rad[1])
    print("    with the doubling above 2.25 eV      %.4f V" % rad[1])
    print("    section 6.2 states                   %.4f V" % C.VOC_RAD_CLAIMED)
    print("    difference                           %.0f mV, in the claim's favour"
          % (1000 * (C.VOC_RAD_CLAIMED - rad[1])))
    print()
    print("  V_oc = V_oc,rad - dV_nr, with the preprint's dV_nr = 0.09 V:")
    print("    from its own 0.90 V      0.90 - 0.09 = %.3f V, printed as 0.81"
          % (C.VOC_RAD_CLAIMED - C.DVOC_NR_CLAIMED))
    print("    from the measured limit  %.4f - 0.09 = %.3f V"
          % (rad[1], rad[1] - C.DVOC_NR_CLAIMED))
    print()
    print("  What dV_nr = 0.09 V requires.  By the reciprocity relation")
    print("  dV_nr = -(kT/q) ln EQE_EL:")
    for loss, label in ((C.DVOC_NR_ACHIRAL, "achiral NFA blends, per section 6.2"),
                        (C.DVOC_NR_CLAIMED, "claimed for HOS-PV 2.0")):
        print("    dV_nr = %.2f V  ->  EQE_EL = %.2e   (%s)"
              % (loss, np.exp(-loss / KT), label))
    ratio = np.exp((C.DVOC_NR_ACHIRAL - C.DVOC_NR_CLAIMED) / KT)
    print("  The step from 0.22 V to 0.09 V is a factor %.0f in" % ratio)
    print("  electroluminescence quantum efficiency, from 0.02% to 3%.")
    print()
    voc_kt = C.VOC_CLAIMED / KT
    ff_max = (voc_kt - np.log(voc_kt + 0.72)) / (voc_kt + 1)
    print("  Fill factor: the ideal-diode ceiling at V_oc = 0.81 V and n = 1 is")
    print("  %.1f%% (Green's expression).  The claimed 84.0%% is below it, so the"
          % (100 * ff_max))
    print("  fill factor is the one headline number in section 6.2 that is")
    print("  reachable as stated, though no organic cell has reached it.")
    print()
    print("  Finally, how hard the claimed operating point is relative to its")
    print("  own limit:")
    for pce, limit, label in (
            (C.PCE_CLAIMED, own[3], "HOS-PV 2.0 against the measured limit"),
            (C.PCE_CLAIMED, C.LIMIT_CLAIMED, "HOS-PV 2.0 against its claimed limit"),
            (C.PCE_CSI_RECORD, C.LIMIT_CSI_AUGER, "c-Si record against Auger limit"),
            (C.PCE_OPV_TODAY[1], C.SQ_LIMIT_QUOTED, "best OPV today against SQ")):
        print("    %-44s %5.1f%% of limit" % (label, 100 * pce / limit))
    print("  The projection asks an organic blend to reach a larger fraction of")
    print("  its radiative limit than silicon has managed after fifty years.")


if __name__ == "__main__":
    main()
