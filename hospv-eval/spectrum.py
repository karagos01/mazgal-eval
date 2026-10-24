"""The AM1.5G reference spectrum, and the loss census the introduction quotes.

Also the loader used by the other scripts.  Nothing here is specific to the
preprint except the last block, which checks the two loss percentages its
introduction attaches to the Shockley-Queisser optimum.
"""
import hashlib
import os

import numpy as np

import constants as C

HERE = os.path.dirname(os.path.abspath(__file__))


def load_spectrum(verify=True):
    """Return (photon energy in eV ascending, photon flux per m^2 per s per eV,
    integrated irradiance in W/m^2) for the ASTM G173-03 global tilt spectrum."""
    path = os.path.join(HERE, C.SPECTRUM_FILE)
    raw = open(path, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    if verify and digest != C.SPECTRUM_SHA256:
        raise SystemExit("data/ASTMG173.csv does not match the recorded sha256; "
                         "run ./fetch_data.sh to re-derive it")
    table = np.genfromtxt(path, delimiter=",", skip_header=2)
    wavelength = table[:, 0]                       # nm
    irradiance = table[:, 2]                       # W m^-2 nm^-1, global tilt
    power = np.trapezoid(irradiance, wavelength)   # W/m^2
    energy = C.HC_EV_NM / wavelength               # eV
    # per-nm photon flux, then change of variable to per-eV
    flux_nm = irradiance / (C.ELEMENTARY_CHARGE * energy)
    flux_ev = flux_nm * wavelength ** 2 / C.HC_EV_NM
    order = np.argsort(energy)
    return energy[order], flux_ev[order], power


def current_density(energy, flux, lo_ev, hi_ev=np.inf, weight=1.0):
    """Short-circuit current density in mA/cm^2 from photons in [lo, hi) eV."""
    mask = (energy >= lo_ev) & (energy < hi_ev)
    photons = np.trapezoid(flux[mask], energy[mask])
    return weight * C.ELEMENTARY_CHARGE * photons * 0.1    # A/m^2 -> mA/cm^2


def main():
    energy, flux, power = load_spectrum()
    print("=" * 78)
    print("ASTM G173-03 global tilt (AM1.5G)")
    print("=" * 78)
    print("  data file                      %s" % C.SPECTRUM_FILE)
    print("  sha256 matches constants.py    yes")
    print("  samples                        %d" % len(energy))
    print("  wavelength range               %.0f - %.0f nm"
          % (C.HC_EV_NM / energy[-1], C.HC_EV_NM / energy[0]))
    print("  integrated irradiance          %.3f W/m^2   (ASTM value %.1f)"
          % (power, C.SPECTRUM_IRRADIANCE_NOMINAL))
    print()
    print("  The preprint's two photon thresholds, from its own energies:")
    for label, value in (("E(S1) donor", C.E_S1_DONOR), ("E_g(IR)", C.E_GAP_IR)):
        print("    %-14s %.2f eV  ->  %7.1f nm" % (label, value,
                                                   C.HC_EV_NM / value))
    print("    the preprint writes 551 nm and 1107 nm: both correct")
    print()
    print("  Photon-flux ceilings, one electron per photon, EQE = 1:")
    tot = current_density(energy, flux, C.E_GAP_IR)
    lo = current_density(energy, flux, C.E_GAP_IR, C.E_S1_DONOR)
    hi = current_density(energy, flux, C.E_S1_DONOR)
    print("    all photons above 1.12 eV          %6.2f mA/cm^2" % tot)
    print("    1.12 - 2.25 eV (the IR channel)    %6.2f mA/cm^2" % lo)
    print("    above 2.25 eV (the SF channel)     %6.2f mA/cm^2" % hi)
    print()

    print("=" * 78)
    print("The loss census of section 1")
    print("=" * 78)
    print("  Section 1 attaches 'thermalisation about 30% of incident power' and")
    print("  'sub-bandgap transmission about 20%' to the SQ optimum E_g = 1.34 eV.")
    print()
    print("  %-10s %14s %16s %12s" % ("E_g (eV)", "sub-bandgap", "thermalisation",
                                      "left over"))
    for gap in (C.SQ_GAP_QUOTED, C.E_GAP_IR, C.E_S1_DONOR):
        below = np.trapezoid(np.where(energy < gap, flux * energy, 0.0), energy)
        above = np.trapezoid(np.where(energy >= gap, flux * (energy - gap), 0.0),
                             energy)
        below *= C.ELEMENTARY_CHARGE / power
        above *= C.ELEMENTARY_CHARGE / power
        print("  %-10.2f %13.1f%% %15.1f%% %11.1f%%"
              % (gap, 100 * below, 100 * above, 100 * (1 - below - above)))
    print()
    print("  The quoted pair, 30% thermalisation and 20% sub-bandgap, is the pair")
    print("  for E_g = 1.12 eV (31.7% and 19.2%), that is, for silicon.  At the")
    print("  1.34 eV the sentence names, the two are close to the other way")
    print("  round: 23.2% thermalisation against 29.9% sub-bandgap.  The")
    print("  conclusion the paragraph draws - that both losses are large and that")
    print("  a single gap cannot avoid either - is unaffected.")


if __name__ == "__main__":
    main()
