#!/usr/bin/env python3
"""Every constant used in this repository, in one place, with its provenance.

No other script here defines a physical constant, so the provenance of every
number in PAPER.md can be checked by reading this file.

Each constant is tagged:

  [P]  a value taken from the preprint itself
  [V]  an external value verified against a named source while this repository
       was written, with the source given
  [A]  an ASSUMED range, not a cited constant.  Every result that depends on an
       [A] value is computed across the whole range and the conclusion is stated
       only where it holds across all of it.  These exist because the audit in
       the companion reference-audit repository found that citing a plausible
       figure from memory is exactly how a bibliography goes wrong, so anything
       that could not be checked here is swept instead of asserted.
"""

# ---------------------------------------------------------------------------
# [P] The preprint's own parameters
#     M. Mazgal, "Quantum Biofortification and In-Situ Phytomining",
#     Zenodo, 6 October 2026, DOI 10.5281/zenodo.23174932
# ---------------------------------------------------------------------------
PLOUGH_DEPTH_M   = 0.30        # [P] Sec. 4  "at a plowing depth of 30 cm"
PELLET_PER_CM3   = 5.0         # [P] Sec. 4  "1 pellet per 5 cm3 of soil"
PELLETS_PER_M2   = 2500.0      # [P] Sec. 4  "approximately 2,500 pellets per 1 m2"
MATRIX_T_PER_HA  = 25.0        # [P] Sec. 4  "25 tons of matrix per 1 hectare"
ESTATE_HA        = 30.0        # [P] Sec. 4  case study size
ESTATE_T         = 750.0       # [P] Sec. 4  "requires 750 tons of composite material"
LA2O3_T          = 1.0         # [P] Sec. 4  "1 ton of Lanthanum oxide"
GOLD_KG          = 5.0         # [P] Sec. 4  "5 kg of 24k dust (99.99% purity)"
CAPEX_USD        = 1_000_000.0 # [P] Sec. 4  "Estimated Total Cost"
CAPEX_GOLD_USD   = 417_000.0   # [P] Sec. 4  the gold line of the budget
ANNUAL_SAVING    = 25_000.0    # [P] Sec. 4  "annually consumes approximately $25,000"
NPK_UPTAKE       = (0.30, 0.50)  # [P] Sec. 1  "only 30% to 50% of the supplied nutrients"

# ---------------------------------------------------------------------------
# [V] Verified external values
# ---------------------------------------------------------------------------
# Nuclear data, en.wikipedia.org/wiki/Isotopes_of_lanthanum, quoting the
# isotope table; cross-checked against CIAAW for the abundance.
LA138_ABUNDANCE  = 8.881e-4    # [V] 8.881(71)e-4, i.e. 0.0888 %
LA138_HALFLIFE_Y = 1.03e11     # [V] 1.03(1)e11 years
LA138_SPIN       = 5           # [V] 5+   -- the preprint states I = 5, correctly
LA138_BRANCH     = {"beta+": 0.655, "beta-": 0.345}   # [V] to Ba-138 / Ce-138
LA138_STABLE     = False       # [V] a primordial RADIONUCLIDE, not a stable isotope
LA139_ABUNDANCE  = 0.9991119   # [V] 0.9991119(71)
LA139_SPIN       = 3.5         # [V] 7/2+  -- non-zero, which is the point
LA139_STABLE     = True        # [V]

# Nuclear spins and natural abundances of the other isotopes the preprint names,
# from WebElements / the Hebrew University NMR tables.
ODD_ISOTOPES = {
    # isotope: (spin, natural abundance, the element's role in the preprint)
    "Mg-25": (2.5,  0.1000, "chlorophyll, ATP synthase"),   # [V] I = 5/2, 10.00 %
    "Zn-67": (2.5,  0.0410, "zinc fingers"),                # [V] I = 5/2, 4.10 %
    "Ca-43": (3.5,  0.00135, "synaptic calcium"),           # [V] I = 7/2, 0.135 %
}

# Even-even ground states have I = 0.  This is a nuclear-structure theorem, not
# a measurement, and it is what makes the magnetic isotope effect possible at
# all: Mg-24/26, Zn-64/66/68/70 and Ca-40 are all spinless.
EVEN_EVEN_SPIN_IS_ZERO = True

# Atomic and molar masses, IUPAC 2021 standard atomic weights.
M_LA     = 138.905    # [V] g/mol
M_LA2O3  = 325.809    # [V] g/mol, La2O3
M_LA138  = 137.907    # [V] g/mol, the La-138 nuclide mass

# Physical constants, SI 2019 definitions.
N_A      = 6.02214076e23   # [V] /mol
SEC_PER_YEAR = 3.15576e7   # [V] s, Julian year

# Upper continental crust lanthanum.  Rudnick, R. L. & Gao, S., "Composition of
# the Continental Crust", Treatise on Geochemistry (2003; 2nd ed. 2014,
# DOI 10.1016/B978-0-08-095975-7.00301-6).
LA_CRUST_PPM = 31.0       # [V] mg/kg

# Spot gold on the day the preprint was deposited, 6 October 2026, Kitco.
GOLD_USD_PER_OZ = 4168.80      # [V]
TROY_OZ_G       = 31.1034768   # [V] g

# Nitrogen recovery by the first crop, which is what the preprint's Sec. 1
# figure refers to.  "Fertilizer N-recovery efficiency by the first crop is
# 30 to 50%" -- IFA, Nutrient/fertilizer use efficiency, ch. 1 (2014).
N_RECOVERY_FIRST_CROP = (0.30, 0.50)   # [V]

# ---------------------------------------------------------------------------
# [A] Assumed ranges, swept rather than asserted
# ---------------------------------------------------------------------------
# Bulk density of arable topsoil.  Every mass-per-area result scales with this,
# so it is swept rather than fixed.
BULK_DENSITY_RANGE = (1.1, 1.6)    # [A] g/cm3
BULK_DENSITY_MID   = 1.4           # [A] g/cm3, used only for display

# Soil magnesium and zinc content.  Could not be verified against a primary
# source while writing this, so they are ranges and every conclusion drawn from
# them is checked across the whole range.  Magnesium is a major soil element at
# the percent level; zinc is a trace element at tens of ppm.
MG_SOIL_WT_FRACTION = (0.002, 0.030)   # [A] 0.2 % to 3 % Mg by mass
ZN_SOIL_PPM         = (20.0, 120.0)    # [A] mg/kg

# Crustal gold, for scale only.  Commonly quoted as 1-4 ppb; not verified here,
# so the comparison is given as a range and carries no weight in any conclusion.
AU_CRUST_PPB = (1.0, 4.0)          # [A]

# Potassium-40 activity concentration in soil, for the radiological comparison.
# Typically 100-700 Bq/kg; not verified here, so the comparison is given across
# the range.  The conclusion -- that the added La-138 is negligible against it --
# holds at every point by four to five orders of magnitude.
K40_SOIL_BQ_PER_KG = (100.0, 700.0)   # [A]

# Discount rates for the ROI sensitivity.  A choice of presentation, not data.
DISCOUNT_RATES = (0.00, 0.01, 0.02, 0.025, 0.03, 0.05, 0.07)   # [A]

# Annual fractional loss of the metal inventory from the "closed loop".  A swept
# parameter: the preprint assumes it is exactly zero.
LOOP_LOSS_RATES = (0.001, 0.005, 0.01, 0.02, 0.05, 0.10)       # [A]

# ---------------------------------------------------------------------------
# Derived, no new information
# ---------------------------------------------------------------------------
SOIL_CM3_PER_M2 = PLOUGH_DEPTH_M * 100 * 100 * 100   # cm3 under 1 m2
ESTATE_M2       = ESTATE_HA * 10_000.0
LA_FRACTION_IN_LA2O3 = 2 * M_LA / M_LA2O3            # mass fraction of La


def soil_kg_per_m2(bulk_density):
    """Mass of the ploughed layer under one square metre, kg."""
    return PLOUGH_DEPTH_M * 1e6 * bulk_density / 1000.0


def tag_report():
    """How many constants rest on each provenance tier.

    Counted from this file rather than written down, so the figure cannot drift
    away from the tags it describes.
    """
    import re
    import pathlib
    src = pathlib.Path(__file__).read_text()
    # a tagged constant is an assignment, or a dict entry, carrying a tag in a
    # trailing comment
    tagged = re.findall(r"^(?:[A-Z_0-9]+\s*=|\s+\"[\w-]+\":).*?#\s*(\[[PVA]\])",
                        src, re.M)
    return {
        "[P] from the preprint":              tagged.count("[P]"),
        "[V] verified against a named source": tagged.count("[V]"),
        "[A] assumed range, swept":            tagged.count("[A]"),
    }
