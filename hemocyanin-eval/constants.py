#!/usr/bin/env python3
"""Every constant used in this repository, in one place, with its provenance.

No other script here defines a physical or physiological constant.

  [P]  a value taken from the preprint itself
  [V]  an external value verified against a named source while this repository
       was written, with the source given
  [A]  an ASSUMED range, not a cited constant.  Every result that depends on an
       [A] value is computed across the whole range and the conclusion stated
       only where it holds throughout.
"""

# ---------------------------------------------------------------------------
# [P] The preprint's own claims
#     M. Mazgal, "Theoretical Framework for Copper-Based Hemocyanin Physiology
#     in Hominids", Zenodo, 7 October 2026, DOI 10.5281/zenodo.23209266
# ---------------------------------------------------------------------------
# The preprint gives no number for oxygen capacity, cardiac output, metabolic
# rate, copper dose, or anything else quantitative.  These record what it
# asserts, so the scripts can state what each assertion would require.
CLAIMS = {
    "pigment_switch":  "humans could carry copper-based hemocyanin instead of "
                       "iron-based haemoglobin",
    "iron_is_the_tax": "the Fenton reaction is the primary driver of cellular "
                       "corrosion, telomere shortening and biological ageing",
    "ceruloplasmin":   "ceruloplasmin is the fundamental human protein for "
                       "copper transport in the blood and is structurally "
                       "related to invertebrate hemocyanins",
    "epigenetic":      "the organism can epigenetically activate production of "
                       "hybrid copper transport proteins",
    "trigger":         "an isolated population fed for generations on biomass "
                       "from a metal-saturated soil matrix switches metabolism",
    "consequences":    "lifespans of hundreds of years, a superconducting "
                       "nervous system, thermoregulatory independence, a "
                       "biological quantum computer with La-138-doped synapses",
}
EPIGENETIC_WORD_COUNT = 8   # [P] occurrences of "epigenetic" in the text
METHYLATION_COUNT     = 0   # [P] occurrences of methylation
HISTONE_COUNT         = 0   # [P] occurrences of histone
CHROMATIN_COUNT       = 0   # [P] occurrences of chromatin
NUMERIC_DATA_ITEMS    = 0   # [P] measured quantities reported anywhere

# ---------------------------------------------------------------------------
# [V] Verified external values
# ---------------------------------------------------------------------------
# Oxygen-carrying capacity, volumes per cent (mL O2 per 100 mL of blood or
# haemolymph).  The preprint and all five of its references give no such figure,
# so these were obtained independently.
#
#   human arterial blood ~20 vol%
#     -- Collins, J.-A. et al., "Relating oxygen partial pressure, saturation
#        and content: the haemoglobin-oxygen dissociation curve", Breathe 11(3),
#        DOI 10.1183/20734735.001415
#   Cancer magister 3.44  -- Johansen et al. (1970), DOI 10.1007/BF00299532
#   Octopus dofleini 3.06 -- Lenfant & Johansen (1965),
#                            DOI 10.1152/ajplegacy.1965.209.5.991
#   Nautilus pompilius 2.30 +/- 0.57 -- Johansen (1978),
#                            DOI 10.1002/jez.1402050105
#   Octopus vulgaris 1.37 -- Oellermann et al. (2015),
#                            DOI 10.1186/s12983-015-0097-x
#   cephalopods in general: "never exceeds 4.5 vols%"
#     -- Wells & Smith (1987), DOI 10.1007/BF02143577
HB_HUMAN_VOL_PCT  = 20.0     # [V]
HCY_SPECIES_VOL_PCT = {      # [V]
    "Cancer magister":    3.44,
    "Octopus dofleini":   3.06,
    "Nautilus pompilius": 2.30,
    "Octopus vulgaris":   1.37,
}
HCY_CEPHALOPOD_CEILING = 4.5   # [V] "never exceeds 4.5 vols%"

# Why hemocyanin cannot simply be concentrated until it matches.  van Holde,
# K. E., Miller, K. I. & Decker, H., "Hemocyanins and Invertebrate Evolution",
# J. Biol. Chem. 276(19), 15563-15566 (2001), DOI 10.1074/jbc.R100010200 --
# which is also the paper the preprint's first citation garbles:
OSMOTIC_QUOTE = ("a low molecular weight monomeric protein dissolved in the "
                 "hemolymph is not efficient for oxygen transport. If its "
                 "concentration in the hemolymph is high enough to transport a "
                 "significant amount of oxygen, it will yield an unbearably "
                 "high osmotic pressure.")   # [V]

# Human resting oxygen consumption.  3.5 mL O2 per kg per minute is one
# metabolic equivalent (MET) by definition, the standard reference for resting
# metabolic rate -- Jetté, M., Sidney, K. & Blümchen, G., Clin. Cardiol. 13(8),
# 555-565 (1990), DOI 10.1002/clc.4960130809.
VO2_REST_ML_PER_KG_MIN = 3.5    # [V] = 1 MET
BODY_MASS_KG           = 70.0   # [V] reference adult

# Hemocyanin is a type-3 binuclear copper protein: one O2 per two Cu, in a
# subunit of the order of 75 kDa; haemoglobin carries four O2 per 64.5 kDa
# tetramer.  Both figures are standard but were not verified against a primary
# source here, so the mass-efficiency comparison below is tagged [A].

# Ceruloplasmin is a ferroxidase, not a copper transporter.  Hellman, N. E. &
# Gitlin, J. D., Annu. Rev. Nutr. 22, 439-458 (2002),
# DOI 10.1146/annurev.nutr.22.012502.114457, abstract, verbatim:
CERULOPLASMIN_QUOTE = ("Ceruloplasmin is a serum ferroxidase ... Despite the "
                       "need for copper in ceruloplasmin function, this protein "
                       "plays no essential role in the transport or metabolism "
                       "of this metal.")   # [V]

# Domain assignments, from InterPro and Pfam queries.  The intersection between
# the ceruloplasmin and hemocyanin families is empty.
CERULOPLASMIN_FAMILY = "multicopper oxidase, cupredoxin fold (IPR045087)"  # [V]
HEMOCYANIN_FAMILY    = "hemocyanin/hexamerin + tyrosinase binuclear type-3 "\
                       "copper centre (IPR013788)"                          # [V]
VERTEBRATE_HEMOCYANIN_GENES = 0   # [V] IPR013788 in Vertebrata (taxon 7742)
                                  #     returns no entries; likewise Chordata
HUMAN_TYROSINASE_DOMAIN_GENES = ("TYR", "TYRP1", "DCT")   # [V] PF00264 in human
TYRP1_ACTIVE_SITE_METAL = "zinc"  # [V] "the active site contains two zinc
                                  #     ions... Because zinc ions, in contrast
                                  #     to copper ions, are not redox-active"
                                  #     -- Lai et al., Int. J. Mol. Sci. 21(3),
                                  #     915 (2020), DOI 10.3390/ijms21030915

# Copper's own redox toxicity, from the preprint's own fourth reference.
# Tchounwou, P. B. et al., Experientia Supplementum 101, 133-164 (2012),
# DOI 10.1007/978-3-7643-8340-4_6, verbatim:
COPPER_TOXICITY_QUOTE = ("it is this property of copper that also makes it "
                         "potentially toxic because the transitions between "
                         "Cu(II) and Cu(I) can result in the generation of "
                         "superoxide and hydroxyl radicals.")   # [V]
TCHOUNWOU_EPIGENETIC_COUNT = 0   # [V] occurrences of "epigenet" in that work

# Pigment replacement does occur in nature, and runs the other way.  Peña, J. J.
# & Adema, C. M., PLoS ONE 11, e0168665 (2016),
# DOI 10.1371/journal.pone.0168665, and Lieb, B. et al., PNAS 103, 12011 (2006),
# DOI 10.1073/pnas.0601861103.
PLANORBID_QUOTE = ("snails of the family Planorbidae are unique among "
                   "gastropods in that they have replaced the ancestral (blue) "
                   "hemocyanin as an oxygen-carrier with secondarily evolved "
                   "hemoglobin")   # [V]
PLANORBID_REASON = ("B. glabrata hemoglobin evolved from pulmonate myoglobin, "
                    "possibly to replace a less-efficient hemocyanin")  # [V]
HEMOCYANIN_NOT_REGAINED = ("Once lost, hemocyanin was not regained.")   # [V]
                    # Burmester, T., Integr. Comp. Biol. 55(5) (2015),
                    # DOI 10.1093/icb/icv079

# What squid pay for their metabolic rate.  O'Dor, R. K. & Webber, D. M.,
# J. Exp. Biol. 160, 93-112 (1991), DOI 10.1242/jeb.160.1.93.
SQUID_CONSTRAINT_QUOTE = ("The constraint on power output in squids is clearly "
                          "not oxygen uptake, but oxygen transport in the "
                          "blood")   # [V]

# ---------------------------------------------------------------------------
# [A] Assumed ranges, swept rather than asserted
# ---------------------------------------------------------------------------
CARDIAC_OUTPUT_REST_L_MIN = (4.0, 6.0)   # [A] L/min, resting adult
O2_EXTRACTION_FRACTION    = (0.25, 0.75) # [A] fraction of arterial O2 content
                                         #     actually unloaded per pass
VO2_MAX_MULTIPLE          = (8.0, 20.0)  # [A] VO2max as a multiple of resting
HB_TETRAMER_KDA           = 64.5         # [A] 4 O2 per tetramer
HCY_PER_O2_KDA            = (50.0, 100.0)  # [A] protein mass per O2 site

# ---------------------------------------------------------------------------
# Derived, no new information
# ---------------------------------------------------------------------------
VO2_REST_ML_MIN = VO2_REST_ML_PER_KG_MIN * BODY_MASS_KG   # mL O2/min at rest


def required_avo2_vol_pct(vo2_ml_min, cardiac_output_l_min):
    """Arteriovenous oxygen difference a given flow must deliver, in vol%."""
    return vo2_ml_min / (cardiac_output_l_min * 1000.0) * 100.0


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
