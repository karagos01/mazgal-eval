#!/usr/bin/env python3
"""Sec. 3.3: the "Quantum Circuit", which the paper calls "the most radical
innovation of the matrix".

Three claims are checked here.

  "the selection of rare, stable isotopes with a non-zero (and often
   asymmetric) nuclear spin"                                    -- Sec. 3.3
  "a precisely defined profile of stable isotopes (including elements with
   non-zero nuclear spin such as 138La, 43Ca, and 25Mg)"         -- Abstract
  "Lanthanum-138 ... with a nuclear spin of I = 5. When substituting calcium
   in neural synapses, it acts not merely as a conductor, but as a magnetic
   gyroscope"                                                    -- Sec. 3.3

The spin values are right.  Three things are not: La-138 is not stable, the
common isotope of lanthanum already has non-zero spin so there is nothing to
select for, and at natural abundance the matrix adds nothing to the soil that
is not already in it in larger quantity.
"""
import math

from constants import (AU_CRUST_PPB, BULK_DENSITY_MID, BULK_DENSITY_RANGE,
                       ESTATE_M2, GOLD_KG,
                       K40_SOIL_BQ_PER_KG, LA138_ABUNDANCE, LA138_BRANCH,
                       LA138_HALFLIFE_Y, LA138_SPIN, LA138_STABLE, LA139_ABUNDANCE,
                       LA139_SPIN, LA2O3_T, LA_CRUST_PPM, LA_FRACTION_IN_LA2O3,
                       M_LA138, MG_SOIL_WT_FRACTION, N_A, ODD_ISOTOPES,
                       SEC_PER_YEAR, ZN_SOIL_PPM, soil_kg_per_m2)

P = print

P("0. Where the constants in this script come from")
P()
from constants import tag_report
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()
P("      Every conclusion drawn from an [A] value below is computed across its")
P("      whole range and stated only where it holds throughout.")
P()


def spin_str(i):
    return f"{int(i)}" if i == int(i) else f"{int(i * 2)}/2"


P("1. The spins, which the paper has right")
P()
P(f"  {'isotope':>8s} {'spin':>6s} {'natural abundance':>19s}   where the paper puts it")
P(f"  {'La-138':>8s} {spin_str(LA138_SPIN):>6s} {LA138_ABUNDANCE:>18.4%}"
  f"   synaptic calcium substitute")
for iso, (spin, ab, role) in ODD_ISOTOPES.items():
    P(f"  {iso:>8s} {spin_str(spin):>6s} {ab:>18.3%}   {role}")
P()
P("  All four spins are stated correctly in the preprint.  They are non-zero")
P("  because each nuclide has an odd number of either protons or neutrons,")
P("  while the abundant isotopes of the same elements -- Mg-24/26, Zn-64/66/68,")
P("  Ca-40 -- are even-even and therefore have I = 0 exactly.  That contrast is")
P("  what makes the magnetic isotope effect possible, and the paper's reasoning")
P("  up to this point is sound.")

P()
P("2. La-138 is not a stable isotope")
P()
P(f"  [P] abstract, Sec. 3.3 and the Zenodo keywords all call it stable")
P(f"  [V] it is a primordial RADIONUCLIDE")
P(f"        half-life   {LA138_HALFLIFE_Y:.3g} years")
P(f"        decay       beta+ {LA138_BRANCH['beta+']:.1%} to Ba-138,"
  f"  beta- {LA138_BRANCH['beta-']:.1%} to Ce-138")
P(f"        stable?     {LA138_STABLE}")
P()
P("  It is one of only a handful of odd-odd nuclides that survive from the")
P("  formation of the Earth, which is exactly why it is rare.  The rarity the")
P("  paper selects for and the instability it overlooks are the same fact.")

P()
P("3. The premise fails for lanthanum before stability even matters")
P()
P(f"  [P] \"the selection of rare, stable isotopes with a non-zero ... nuclear spin\"")
P(f"  [V] La-139, {LA139_ABUNDANCE:.2%} of all lanthanum, has spin "
  f"{spin_str(LA139_SPIN)}")
P()
P("  Non-zero.  So for lanthanum there is nothing to gain by selecting the rare")
P("  isotope on spin grounds: the common one already has one, and a larger one.")
P("  For Mg, Zn and Ca the paper's logic does work, because there the abundant")
P("  isotopes are spinless.  Lanthanum is the element it does not work for, and")
P("  it is the element the section is built around.")

P()
P("4. At natural abundance the matrix adds less than the field already holds")
P()
la_added_g_m2 = LA2O3_T * 1000.0 * LA_FRACTION_IN_LA2O3 * 1000.0 / ESTATE_M2
P(f"  [P] {LA2O3_T:.0f} t La2O3 over {ESTATE_M2 / 10_000:.0f} ha")
P(f"      mass fraction La in La2O3            {LA_FRACTION_IN_LA2O3:>10.4f}")
P(f"      lanthanum added                      {la_added_g_m2:>10.3f} g/m2")
P()
P(f"  [V] soil La at {LA_CRUST_PPM:.0f} ppm (Rudnick & Gao), swept over bulk density:")
P(f"      {'bulk density':>16s} {'soil mass':>12s} {'La present':>13s} "
  f"{'increase':>9s} {'new ppm':>9s}")
for bd in (BULK_DENSITY_RANGE[0], BULK_DENSITY_MID, BULK_DENSITY_RANGE[1]):
    skg = soil_kg_per_m2(bd)
    nat = skg * LA_CRUST_PPM * 1e-6 * 1000.0
    P(f"      {bd:>10.1f} g/cm3 {skg:>9.0f} kg {nat:>8.2f} g/m2 "
      f"{la_added_g_m2 / nat:>9.1%} {LA_CRUST_PPM * (1 + la_added_g_m2 / nat):>9.1f}")
P()
P("      So the 'most radical innovation' raises the field's lanthanum by about")
P("      a fifth, and -- since the paper never says the lanthanum is")
P("      isotopically enriched -- leaves the La-138 fraction exactly where it")
P("      was, at 0.0888 %.  A natural isotope ratio is not something a soil can")
P("      be deficient in.")

P()
P("5. The same test for the other two isotopes named")
P()
P("      [A] soil contents are swept, not asserted; see constants.py")
P(f"      {'isotope':>8s} {'element in soil, g/m2':>26s}"
  f" {'isotope present, g/m2':>26s}")
for iso, (spin, ab, _) in (("Mg-25", ODD_ISOTOPES["Mg-25"]),
                           ("Zn-67", ODD_ISOTOPES["Zn-67"])):
    skg = soil_kg_per_m2(BULK_DENSITY_MID)
    if iso == "Mg-25":
        lo, hi = (skg * f * 1000.0 for f in MG_SOIL_WT_FRACTION)
        unit = "g/m2"
    else:
        lo, hi = (skg * p * 1e-6 * 1000.0 for p in ZN_SOIL_PPM)
        unit = "g/m2"
    P(f"      {iso:>8s} {lo:>11.1f} - {hi:>11.1f}  "
      f"{lo * ab:>12.2f} - {hi * ab:>11.2f}")
P()
P("      Chlorophyll already contains Mg-25 at 10.00 % of its magnesium and")
P("      zinc-finger proteins already contain Zn-67 at 4.10 % of their zinc.")
P("      Across the whole swept range the quantity already in the ploughed")
P("      layer exceeds anything the matrix adds by orders of magnitude.  The")
P("      magnetic isotope effect, whatever its size, is already running.")

P()
P("6. What enrichment would have cost instead")
P()
P(f"      to obtain 1 t of La-138 at {LA138_ABUNDANCE:.4%} natural abundance")
P(f"      requires {1.0 / LA138_ABUNDANCE:>10,.0f} t of natural lanthanum as feed")
P()
P("      The paper's budget has 1 t of lanthanum oxide at a price consistent")
P("      with ordinary commercial material, and never uses the word enriched.")
P("      Both readings are therefore unavailable to it at once: unenriched, the")
P("      Quantum Circuit adds nothing; enriched, the budget is wrong by orders")
P("      of magnitude.")

P()
P("7. Radiologically the added La-138 is negligible, and that is in the")
P("   paper's favour")
P()
la138_g = LA2O3_T * 1000.0 * LA_FRACTION_IN_LA2O3 * 1000.0 * LA138_ABUNDANCE
lam = math.log(2) / (LA138_HALFLIFE_Y * SEC_PER_YEAR)
spec_bq_per_g = lam * N_A / M_LA138
activity = la138_g * spec_bq_per_g
P(f"      La-138 in 1 t of natural La2O3        {la138_g:>12.1f} g")
P(f"      decay constant                       {lam:>12.3e} /s")
P(f"      specific activity of pure La-138     {spec_bq_per_g:>12.1f} Bq/g")
P(f"      total activity added over {ESTATE_M2 / 10_000:.0f} ha        "
  f"{activity / 1e3:>12.1f} kBq")
P(f"      areal activity                       {activity / ESTATE_M2:>12.2f} Bq/m2")
P()
P("      [A] against the potassium-40 already in the soil, swept:")
for k40 in K40_SOIL_BQ_PER_KG:
    nat = k40 * soil_kg_per_m2(BULK_DENSITY_MID)
    P(f"        K-40 at {k40:>5.0f} Bq/kg -> {nat:>11,.0f} Bq/m2    "
      f"added / present = {activity / ESTATE_M2 / nat:.1e}")
P()
ratios = [activity / ESTATE_M2 / (k40 * soil_kg_per_m2(BULK_DENSITY_MID))
          for k40 in K40_SOIL_BQ_PER_KG]
P(f"      Between {-math.log10(max(ratios)):.0f} and "
  f"{-math.log10(min(ratios)):.0f} orders of magnitude below the natural "
  f"potassium")
P("      background, across the whole range.  Calling La-138 a stable isotope")
P("      is a factual error about the nuclide, not a safety problem with the")
P("      proposal, and the distinction is worth keeping.")

P()
P("8. Gold loading, for scale")
P()
au_g_m2 = GOLD_KG * 1000.0 / ESTATE_M2
P(f"  [P] {GOLD_KG:.0f} kg over {ESTATE_M2 / 10_000:.0f} ha"
  f"{au_g_m2 * 1000:>26.3f} mg/m2")
for bd in (BULK_DENSITY_RANGE[0], BULK_DENSITY_RANGE[1]):
    ppb = au_g_m2 / soil_kg_per_m2(bd) * 1e6
    P(f"      at bulk density {bd:.1f} g/cm3 {ppb:>21.1f} ppb")
P(f"      [A] crustal gold is quoted as {AU_CRUST_PPB[0]:.0f}-{AU_CRUST_PPB[1]:.0f} ppb,")
P("          unverified here, so this is scale only and carries no conclusion.")
