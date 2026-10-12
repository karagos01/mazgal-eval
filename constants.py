#!/usr/bin/env python3
"""Every constant used in this repository, in one place, with its provenance.

No other script here defines a physical constant.

  [P]  a value taken from the preprint itself
  [V]  an external value verified against a named source while this repository
       was written, with the source given
  [A]  an ASSUMED range, not a cited constant.  Every result that depends on an
       [A] value is computed across the whole range and the conclusion stated
       only where it holds throughout.
"""

# ---------------------------------------------------------------------------
# [P] The preprint's own parameters
#     M. Mazgal, "Dual-Scale Waveform Optimization and Hysteretic-Fractal
#     Resonant Stimulation (HFRS) for Minimizing Transport Resistance in Na-ion
#     Lattices", Zenodo, 6 October 2026, DOI 10.5281/zenodo.23186884
# ---------------------------------------------------------------------------
F_MICRO_BAND  = (1e3, 1e6)   # [P] Sec. 2.1  "high-frequency fractal modulation
                             #               (kHz to MHz range)"
GPU_COUNT     = 8            # [P] Sec. 3    "The 8x8 Computational Swarm"
CELLS         = 8            # [P] Sec. 3    "1:1 mapping between a compute node
                             #               (GPU) and a physical Na-ion cell"
DEPOSIT_FILES = 1            # [P] Sec. 6 promises /Hardware, /Software and
                             #     /Datasets; the deposit holds one file
DEPOSIT_BYTES = 97_786       # [P] the PDF, which is all of it
PDF_LICENCE   = "CC BY 4.0 for text and data, CERN-OHL-S for hardware"  # [P] header
ZENODO_LICENCE = "cc-by-4.0"  # [P] what the record actually carries

# ---------------------------------------------------------------------------
# [V] Verified external values
# ---------------------------------------------------------------------------
# SI 2019 defining constants and derived quantities.
H_PLANCK = 6.62607015e-34    # [V] J s
E_CHARGE = 1.602176634e-19   # [V] C
K_B      = 1.380649e-23      # [V] J/K
C_LIGHT_CM = 2.99792458e10   # [V] cm/s, for wavenumber -> frequency
MU_0     = 1.25663706212e-6  # [V] H/m

# Raman-active lattice modes measured in a layered oxide cathode.  "aged NMC111
# cathode materials show Raman bands at 144, 189, and 324 cm-1 attributed to
# vibrational modes" -- Raman and Infrared Spectroscopy of Materials for
# Lithium-Ion Batteries, Int. J. Mol. Sci. 26(24), 11879 (2025),
# DOI 10.3390/ijms262411879.  Layered LiMO2 crystallises in the alpha-NaFeO2
# structure, which is the same structural family as the Na-ion layered cathodes
# the preprint targets.
NMC_RAMAN_CM1 = (144.0, 189.0, 324.0)   # [V] cm-1

# Sodium migration activation energies.  NaFePO4 maricite: "Na ions ... migrate
# via a 3D conduction pathway with low activation barriers of 0.10-0.17 eV";
# classical MD "approximately 0.2 eV".  alpha-NaFeO2: "local Na hops ... with a
# migration energy of 0.64 eV" -- Defect Chemistry, Sodium Diffusion and Doping
# Behaviour in NaFeO2 Polymorphs, Materials 12(19), 3243 (2019),
# DOI 10.3390/ma12193243, and the NaFePO4 literature cited there.
NA_MIGRATION_EV = (0.10, 0.64)   # [V] eV, across the materials above

# Where a cell actually has a faradaic response.  "Charge transfer resistance and
# double-layer capacitance at the interfacial layers between the electrolyte
# solution and electrode surfaces form a characteristic semicircle above the
# x-axis, over approximately the 1 Hz to 1 kHz range", and above 1 kHz the
# response "represent[s] the ohmic resistance and inductive effects".
EIS_CHARGE_TRANSFER_BAND = (1.0, 1e3)   # [V] Hz

# Resistivities at 20 C, CRC.
RHO_CU = 1.68e-8    # [V] ohm m
RHO_AL = 2.65e-8    # [V] ohm m

# What the preprint's only pulsed-charging citation actually found.
# Purushothaman, B. K. & Landau, U., J. Electrochem. Soc. 153(3), A533 (2006),
# DOI 10.1149/1.2161580: the limit is solid-state lithium diffusion, the
# analysed protocol is a 3 s pulse with 1 s rest, and the best result in the
# paper is a continuous profile, not a pulse at all.
PL2006_PULSE_S = 3.0    # [V] s on
PL2006_REST_S  = 1.0    # [V] s off
PL2006_BEST_IS_CONTINUOUS = True   # [V] "A nonlinearly decreasing current
                                   #     density profile ... faster than any
                                   #     other pulse-charging profile studied"

# ---------------------------------------------------------------------------
# [A] Assumed ranges, swept rather than asserted
# ---------------------------------------------------------------------------
FOIL_THICKNESS_UM = (6.0, 20.0)   # [A] Cu anode 6-10, Al cathode 12-20 um
COIN_CELL_LIFE    = (500, 3000)   # [A] cycles before capacity fade ends the
                                  #     usefulness of a sample as a test vehicle
C_RATES           = (0.5, 1.0, 2.0)   # [A] for the throughput table
R_I_ARRHENIUS_EV  = (0.20, 0.50)  # [A] apparent activation energy of the
                                  #     cell's internal resistance
PSO_EVALUATIONS   = (1e4, 1e5)    # [A] typical budget for particle swarm
                                  #     optimisation on a 10-30 dimensional space
DDS_RATE_SA_S     = (1e7, 1e8)    # [A] sample rate the GPU would stream
DDS_BITS          = 16            # [A] bits per sample
T_AMBIENT_K       = 298.15        # [A] K, reference for the Arrhenius sweep
T_SWEEP_C         = (25, 35, 45, 55)  # [A] degrees C

# ---------------------------------------------------------------------------
# Derived, no new information
# ---------------------------------------------------------------------------
KT_EV_300 = K_B * 300.0 / E_CHARGE      # thermal energy at 300 K, eV


def wavenumber_to_hz(cm1):
    return C_LIGHT_CM * cm1


def photon_ev(f_hz):
    return H_PLANCK * f_hz / E_CHARGE


def skin_depth_m(rho, f_hz):
    import math
    return math.sqrt(rho / (math.pi * f_hz * MU_0))


def tag_report():
    """Counted from this file rather than written down."""
    import re
    import pathlib
    src = pathlib.Path(__file__).read_text()
    tagged = re.findall(r"^[A-Z_0-9]+\s*=.*?#\s*(\[[PVA]\])", src, re.M)
    return {
        "[P] from the preprint":               tagged.count("[P]"),
        "[V] verified against a named source": tagged.count("[V]"),
        "[A] assumed range, swept":            tagged.count("[A]"),
    }
