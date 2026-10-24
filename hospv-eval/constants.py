"""Every number used anywhere in this evaluation, with its provenance.

Provenance tags, one per constant:

  [P]  taken from the preprint under evaluation (M. Mazgal, HOS-PV 2.0,
       Zenodo 10.5281/zenodo.23364732, 14 October 2026)
  [V]  verified against a named external source, given inline
  [A]  assumed, or a choice of presentation.  Every [A] that could change a
       conclusion is swept over its stated range rather than asserted, and the
       conclusion is reported across the whole range.

No other script in this repository defines a physical constant.
"""

# ---------------------------------------------------------------- physics ----
# [V] CODATA 2018 / SI 2019 exact defining constants
PLANCK = 6.62607015e-34          # J s        [V] exact by SI definition
LIGHT = 2.99792458e8             # m/s        [V] exact by SI definition
ELEMENTARY_CHARGE = 1.602176634e-19  # C      [V] exact by SI definition
BOLTZMANN = 1.380649e-23         # J/K        [V] exact by SI definition
ELECTRON_MASS = 9.1093837015e-31 # kg         [V] CODATA 2018
# hc in eV nm, the conversion the preprint uses implicitly for its wavelengths
HC_EV_NM = 1239.841984           # eV nm      [V] = h c / e, from the above

# Cell temperature for all detailed-balance work.
TEMPERATURE_STC = 298.15         # K          [V] IEC 60904-3 standard test conditions

# ------------------------------------------------------- reference spectrum ---
# ASTM G173-03 global tilt (AM1.5G).  Shipped in data/ASTMG173.csv; fetch_data.sh
# re-derives the identical file from the pvlib distribution so that the copy
# here can be checked rather than trusted.
SPECTRUM_FILE = "data/ASTMG173.csv"
SPECTRUM_SHA256 = (                                  # [V] sha256 of the shipped file
    "91964ac23c0ec82dbbda4a7f160a5f5faf551dfe18ffae7e2446d74b57ee7859")
SPECTRUM_IRRADIANCE_NOMINAL = 1000.4   # W/m^2  [V] ASTM G173-03 integral of the
                                       # global tilt spectrum, 280-4000 nm

# ------------------------------------------------- the preprint's own values ---
# Abstract and section 6.2.
E_S1_DONOR = 2.25                # eV         [P] abstract, section 2.2
E_T1_DONOR = 1.15                # eV         [P] section 2.2
E_GAP_IR = 1.12                  # eV         [P] abstract, section 2.2
LAMBDA_DONOR_NM = 551.0          # nm         [P] section 2.2, "lambda <= 551 nm"
LAMBDA_IR_NM = 1107.0            # nm         [P] section 2.2, "lambda <= 1107 nm"

EQE_IR = 0.85                    # -          [P] section 6.2, 1.12-2.25 eV band
ETA_SF = 1.85                    # -          [P] section 6.2, triplets per singlet
ETA_DET = 0.92                   # -          [P] section 6.2, Dexter transfer
EQE_BHJ = 0.90                   # -          [P] section 6.2, above 2.25 eV
EQE_HIGH_CLAIMED = 1.53          # -          [P] section 6.2, "EQE_high = 153%"

JSC_IR_CLAIMED = 28.5            # mA/cm^2    [P] section 6.2
JSC_SF_CLAIMED = 23.8            # mA/cm^2    [P] section 6.2
JSC_CLAIMED = 52.3               # mA/cm^2    [P] abstract, section 6.2
JSC_CSI_TABLE = 42.8             # mA/cm^2    [P] table 2, c-Si record, for scale
VOC_CLAIMED = 0.81               # V          [P] abstract, section 6.2
VOC_RAD_CLAIMED = 0.90           # V          [P] section 6.2, "radiative limit"
FF_CLAIMED = 0.840               # -          [P] abstract, section 6.2
PCE_CLAIMED = 0.3558             # -          [P] section 6.2, "35.58%"
LIMIT_CLAIMED = 0.459            # -          [P] abstract, section 2.2, "45.9%"
SQ_LIMIT_QUOTED = 0.337          # -          [P] section 1, also the true value
SQ_GAP_QUOTED = 1.34             # eV         [P] section 1
LOSS_THERMALISATION_QUOTED = 0.30  # -        [P] section 1, "approximately 30%"
LOSS_SUBGAP_QUOTED = 0.20        # -         [P] section 1, "approximately 20%"

DVOC_NR_ACHIRAL = 0.22           # V          [P] section 6.2, typical NFA blend
DVOC_NR_CLAIMED = 0.09           # V          [P] section 6.2, claimed for HOS-PV

P_CISS = 0.85                    # -          [P] section 4.1, worked example
P_CISS_RANGE = (0.75, 0.90)      # -          [P] section 3.2, reported range
ETA_PB_CLAIMED = 0.95            # -          [P] section 4.1, worked example
TAU_SPIN = 5.0e-6                # s          [P] section 4.1, spin-lattice time
TAU_EXT_QUOTED = (20e-9, 80e-9)  # s          [P] section 4.1, transit time
SUPPRESSION_CLAIMED = 0.686      # -          [P] section 4.1, "suppressed by 68.6%"
SOC_EXPONENT_CLAIMED = 4.0       # -          [P] section 1, "xi_SOC proportional to Z^4"
Z_CARBON = 6                     # -          [P] section 1, also simply true

ALPHA_ABSORPTION = 1.0e5         # 1/cm       [P] section 1, "alpha ~ 10^5 cm^-1"
SPIN_SPLIT_CLAIMED = (0.5, 1.0)  # eV         [P] section 5.1, altermagnet splitting
SPIN_SPLIT_TABLE = 0.8           # eV         [P] table 1, layer 6

SPECIFIC_POWER_CLAIMED = 10000.0 # W/kg       [P] table 2, "at least 10,000"
SPECIFIC_POWER_CSI = 450.0       # W/kg       [P] table 2, crystalline silicon
PCE_OPV_TODAY = (0.19, 0.20)     # -          [P] section 1, state of the art OPV
PCE_CSI_RECORD = 0.273           # -          [P] table 2, c-Si record
LIMIT_CSI_AUGER = 0.294          # -          [P] table 2, Auger limit of silicon

# Table 1, the seven-layer stack.  Thicknesses are [P]; the back reflector is the
# one layer whose thickness the table does not give.
THICKNESS_SUBSTRATE = 50e-6      # m          [P] table 1, layer 1
THICKNESS_ITO = 100e-9           # m          [P] table 1, layer 2
THICKNESS_CSAM = 1.5e-9          # m          [P] table 1, layer 3
THICKNESS_ACTIVE = 220e-9        # m          [P] table 1, layer 4
THICKNESS_MGO = 1.2e-9           # m          [P] table 1, layer 5
THICKNESS_ALTERMAGNET = 40e-9    # m          [P] table 1, layer 6
THICKNESS_ENCAPSULATION = 25e-6  # m          [P] table 1, layer 7
THICKNESS_REFLECTOR_RANGE = (100e-9, 200e-9)  # m   [A] table 1 names an
                                 # "Ag/Al optical back-reflector" without a
                                 # thickness; this range is swept.

# ---------------------------------------------------- verified external data ---
# Reference [5] of the preprint, cited for the 45.9% figure:
# M. C. Hanna and A. J. Nozik, J. Appl. Phys. 100, 074510 (2006).
HN_SINGLE_GAP_NO_CM = 0.337      # -          [V] [5] abstract: single gap, no
                                 # carrier multiplication
HN_SINGLE_GAP_MAX_CM = 0.444     # -          [V] [5] abstract: single gap with
                                 # carrier multiplication, maximum multiplication
HN_TANDEM_RANGE = (0.457, 0.477) # -          [V] [5] abstract: ideal two-gap
                                 # tandem, without and with CM absorbers
# Same group, NREL/CP-590-38992 (Nov 2005), reporting the M = 2 case explicitly:
# "from 42.0% at Eg = 0.95 eV to 44.4% at Eg = 0.7 eV".
HN_M2_EFFICIENCY = 0.420         # -          [V] NREL/CP-590-38992, M = 2
HN_M2_GAP = 0.95                 # eV         [V] NREL/CP-590-38992, M = 2
HN_MMAX_GAP = 0.70               # eV         [V] NREL/CP-590-38992, M = max

# Singlet fission energetics of the chromophores the literature has measured.
# (name, E(S1) eV, E(T1) eV, source tag)
SF_CHROMOPHORES = (             # [V] see sources in PAPER.md section 5
    ("pentacene", 2.20, 0.86, "T1 experimental; S1 monomer 2.1-2.3 eV"),
    ("tetracene", 2.32, 1.25, "2*T1 lies about 0.2 eV above S1"),
    ("rubrene", 2.21, 1.14, "crystalline, adiabatic T1; dE_SF = -0.07 eV"),
)
SF_PENTACENE_TIME = 80e-15       # s          [V] sub-100 fs fission in pentacene
                                 # is the standard exothermic benchmark
SF_RATE_REQUIRED = 100e-15       # s          [P] section 2.1, "1 / k_SF below 100 fs"

# Altermagnets named in table 1, layer 6.
NEEL_MNTE_RANGE = (267.0, 307.0) # K          [V] Lee et al., Phys. Rev. Lett.
                                 # 132, 036702 (2024): 267 K; Osumi et al., Phys.
                                 # Rev. B 109, 115102 (2024): 307 K
SPIN_SPLIT_MNTE_RANGE = (0.37, 0.80)  # eV    [V] same two papers: up to 370 meV
                                 # and 0.8 eV respectively
# Module operating temperature, IEC 61215 nominal operating cell temperature.
NOCT_TYPICAL_C = (45.0, 47.0)    # degC       [V] typical reported NOCT values
NOCT_THIN_FILM_MEASURED_C = 59.0 # degC       [V] outdoor NOCT measured for a
                                 # thin-film module (Shah Alam, IEC 61215 method)

# NIST Atomic Spectra Database, ground term 2P(3/2) - 2P(1/2) splitting of the
# halogens: the valence np shell down one column of the periodic table, which is
# the comparison the Z^4 claim is being used for.  fetch_data.sh re-queries these.
HALOGEN_SOC = (                  # (Z, splitting in cm^-1)  [V] NIST ASD
    (9, 404.141),                # F I   2s2.2p5
    (17, 882.3515),              # Cl I  3s2.3p5
    (35, 3685.24),               # Br I  4s2.4p5
    (53, 7602.9762),             # I I   5s2.5p5
)
SOC_EXPONENT_VALENCE = 2.0       # -          [V] Landau-Lifshitz scaling for the
                                 # outermost electrons, as quoted in the
                                 # altermagnetism/SOC review literature

# Mass densities, g/cm^3.
DENSITY_PEN = 1.36               # [V] poly(ethylene naphthalate), bulk
DENSITY_ITO = 7.14               # [V] indium tin oxide, bulk
DENSITY_MGO = 3.58               # [V] magnesium oxide, bulk
DENSITY_RUO2 = 6.97              # [V] ruthenium dioxide, bulk
DENSITY_AG = 10.49               # [V] silver, bulk
DENSITY_ORGANIC_RANGE = (1.0, 1.4)   # [A] conjugated-polymer blends; swept
DENSITY_ENCAPSULATION_RANGE = (1.8, 2.2)  # [A] ALD alumina plus fluoropolymer
                                 # stack, area-averaged; swept

# -------------------------------------------------------------- assumptions ---
MOBILITY_RANGE = (1e-4, 1e-2)    # cm^2/Vs    [A] the preprint states "low carrier
                                 # mobilities" for disordered OPV without a
                                 # number; this range covers disordered blends at
                                 # the bottom and the best ordered films at the
                                 # top, and is swept
V_INTERNAL = 0.8                 # V          [A] internal field driving extraction
                                 # in tau_ext = d^2 / (2 mu V); swept +-25%
ACCEPTOR_VOLUME_FRACTION = (0.3, 0.7)  # -    [A] split of the 220 nm active layer
                                 # between the two absorbers; swept
TEMPERATURE_SWEEP_C = (0.0, 25.0, 45.0, 59.0, 85.0)  # degC  [A] presentation:
                                 # winter, STC, typical NOCT, measured thin-film
                                 # NOCT, and the IEC 61215 qualification ceiling


def tag_report(path=__file__):
    """Count the provenance tags in this file, by reading the file itself."""
    import collections
    import re
    counts = collections.Counter()
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.lstrip().startswith('"""') or line.lstrip().startswith("#  "):
                pass
            for tag in re.findall(r"\[([PVA])\]", line):
                counts[tag] += 1
    # The docstring explains the three tags and must not be counted.
    for tag in "PVA":
        counts[tag] -= 1
    return counts


if __name__ == "__main__":
    counts = tag_report()
    print("provenance tags in constants.py")
    for tag, label in (("P", "from the preprint"),
                       ("V", "verified against a named source"),
                       ("A", "assumed, and swept")):
        print("  [%s] %-34s %3d" % (tag, label, counts[tag]))
