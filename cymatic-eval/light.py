"""The pulsed-light scheme: what average photon flux it produces, which
mechanism its dark interval matches, and whether pulsing can move grams per
kilowatt-hour.

Sections 4, 5 and 6 of PAPER.md.
"""
from constants import (E_PEAK, T_ON, T_OFF, DUTY, NPQ_LOSS, SAT_C3,
                       PAR_UMOL_PER_J, FULL_SUN_PPFD, LED_WALLPLUG,
                       KCAT_RUBISCO, PQ_REOX_MS, QUANTUM_YIELD, G_PER_MOL_CH2O,
                       LEAF_ABSORPT, PLANAR_LOSS)

bar = lambda c="=": print(c * 78)

bar()
print("1. THE DUTY CYCLE AND THE AVERAGE PHOTON FLUX")
bar()
e_avg = E_PEAK * DUTY
ppfd_peak = E_PEAK * PAR_UMOL_PER_J
ppfd_avg = e_avg * PAR_UMOL_PER_J
print(f"  duty cycle                 {DUTY*100:10.4f} %      (1 : {1/DUTY:.1f})")
print(f"  peak irradiance            {E_PEAK:10.1f} W/m^2  "
      f"= {ppfd_peak:9.0f} umol/m^2/s = {ppfd_peak/FULL_SUN_PPFD:6.2f} x full sun")
print(f"  time-averaged irradiance   {e_avg:10.1f} W/m^2  "
      f"= {ppfd_avg:9.0f} umol/m^2/s = {ppfd_avg/FULL_SUN_PPFD:6.2f} x full sun")
print()
print("  If the 4500 W/m^2 of Sec. 2.2 is total rather than PAR irradiance, the")
print("  photon flux is lower still; this takes the figure at its most favourable.")
bar("-")
print("  Carbon fixed over a day is set by the average flux, not the peak: the")
print("  pulse is 50 us and the Calvin cycle integrates over seconds.")
print(f"  C3 light saturation: {SAT_C3[0]:.0f} (lettuce) ..."
      f" {SAT_C3[1]:.0f} (wheat) umol/m^2/s")
print(f"  the average produced here is {SAT_C3[0]/ppfd_avg:.2f} x BELOW the lowest")
print(f"  of those and {SAT_C3[1]/ppfd_avg:.2f} x below the highest.")
print()
print("  NPQ is a saturation-regime loss.  At 256 umol/m^2/s a continuous-light")
print("  control is not light-saturated either, so it engages little NPQ: the")
print("  mechanism the design exists to bypass is not active in the regime the")
print("  design creates.  The comparison in Sec. 1 is against continuous")
print("  HIGH-intensity light, which this scheme does not deliver on average.")
bar("-")
print(f"  Ceiling on the gain even where NPQ is fully engaged: the preprint puts")
print(f"  the loss at up to {NPQ_LOSS*100:.0f} %, so recovering all of it is"
      f" 1/(1-{NPQ_LOSS:.1f}) = {1/(1-NPQ_LOSS):.2f} x.")
print("  Bounded, and bounded by a number the preprint supplies itself.")

bar()
print("2. WHICH TIMESCALE THE 4 ms DARK PHASE MATCHES")
bar()
t_rub = (1e3 / KCAT_RUBISCO[1], 1e3 / KCAT_RUBISCO[0])
print(f"  dark phase, Sec. 2.2                      {T_OFF*1e3:8.2f} ms")
print(f"  RuBisCO turnover 1/kcat, kcat ="
      f" {KCAT_RUBISCO[0]:.0f}-{KCAT_RUBISCO[1]:.0f} /s   "
      f"{t_rub[0]:6.0f} - {t_rub[1]:3.0f} ms   <- 'the Calvin cycle'")
print(f"  plastoquinol oxidation at cyt b6f         "
      f"{PQ_REOX_MS[0]:6.0f} - {PQ_REOX_MS[1]:3.0f} ms   <- the PQ pool")
print(f"  ratio of the Calvin figure to 4 ms:       "
      f"{t_rub[0]/(T_OFF*1e3):6.0f} - {t_rub[1]/(T_OFF*1e3):3.0f} x off")
print()
print("  4 ms is the right order for reoxidation of the plastoquinone pool, which")
print("  is exactly what Sec. 1 says the design must relieve.  The timing works.")
print("  The justification given for it names the Calvin cycle, which is two")
print("  orders of magnitude slower.  Right number, wrong mechanism.")

bar()
print("3. GRAMS PER KILOWATT-HOUR IS INVARIANT UNDER PULSING")
bar()


def yield_per_kwh(ppfd, npq_fraction, quantum_yield=QUANTUM_YIELD):
    """Dry matter per electrical energy, for a canopy at a given average PPFD."""
    co2 = ppfd * quantum_yield * (1.0 - npq_fraction)        # umol CO2 /m^2/s
    dry = co2 * 1e-6 * G_PER_MOL_CH2O * 86400.0              # g /m^2/day
    el = ppfd / PAR_UMOL_PER_J / LED_WALLPLUG                # W/m^2 electrical
    return dry, el, dry / (el * 24.0 / 1000.0)


print(f"  {'scheme':50s} {'g/m^2/d':>9} {'W/m^2':>8} {'g/kWh':>8}")
rows = [
    ("pulsed, 1.23 % duty, NPQ fully bypassed", ppfd_avg, 0.0),
    ("continuous at the same average flux, no NPQ", ppfd_avg, 0.0),
    ("the same, if NPQ cost the published 60 % here", ppfd_avg, NPQ_LOSS),
    ("continuous at full sun, NPQ at the published 60 %", FULL_SUN_PPFD, NPQ_LOSS),
]
for lab, ppfd, npq in rows:
    dry, el, gk = yield_per_kwh(ppfd, npq)
    print(f"  {lab:50s} {dry:9.1f} {el:8.1f} {gk:8.2f}")
print()
print("  Rows 1 and 2 are identical because pulsing divides the dry matter and")
print("  the electrical input by the same duty cycle.  The ratio cannot move.")
print("  Row 3 is hypothetical: at 256 umol/m^2/s there is little NPQ to pay.")
bar("-")
print("  The invariance is structural, so it must survive varying the duty cycle")
print("  while the peak stays at 4500 W/m^2.  Rows past light saturation are")
print("  marked (*): there the linear quantum-yield model no longer holds, and")
print("  the real g/kWh would FALL, never rise.")
print(f"  {'duty %':>8}  {'avg umol/m^2/s':>15}  {'g/m^2/d':>9}  {'W/m^2':>8}"
      f"  {'g/kWh':>8}")
for d in [DUTY, 0.05, 0.10, 0.25, 1.0]:
    p = E_PEAK * d * PAR_UMOL_PER_J
    dry, el, gk = yield_per_kwh(p, 0.0)
    flag = " (*)" if p > SAT_C3[1] else ""
    print(f"  {d*100:8.3f}  {p:15.0f}  {dry:9.1f}  {el:8.1f}  {gk:8.2f}{flag}")
vals = [yield_per_kwh(E_PEAK * d * PAR_UMOL_PER_J, 0.0)[2]
        for d in [DUTY, 0.05, 0.10, 0.25, 1.0]]
print(f"  spread of g/kWh across an {1/DUTY:.0f}-fold range of duty cycle:"
      f" {max(vals)-min(vals):.3e}  (floating point only)")
bar("-")
print("  g/kWh does depend on the quantum yield, and on nothing else in the")
print("  design.  Doubling the assumed yield doubles it exactly:")
print(f"  {'quantum yield':>14}  {'g/kWh':>8}  {'ratio to the first row':>24}")
base = None
for qy in [0.02, 0.04, 0.05, 0.08, 0.125]:
    gk = yield_per_kwh(ppfd_avg, 0.0, qy)[2]
    base = gk if base is None else base
    print(f"  {qy:14.3f}  {gk:8.2f}  {gk/base:24.4f}")
print()
print("  So the only lever on energy efficiency is the quantum yield, and the")
print("  most that bypassing NPQ can add to it is the 2.50 x ceiling of Sec. 1")
print("  above -- in a regime where, as measured, NPQ is barely engaged.")
print("  Sec. 5 claims the reactor 'redefines the gram-per-watt limit of CEA'.")
print("  Commercial vertical farming already sits at roughly 5-10 g dry per kWh.")

bar()
print("4. THE 100 % PHOTON CAPTURE CLAIM")
bar()
print(f"  Sec. 2.1: planar arrays lose "
      f"{PLANAR_LOSS[0]*100:.0f}-{PLANAR_LOSS[1]*100:.0f} %, the cylinder lets")
print("  'photon capture efficiency approach the theoretical maximum of 100%'.")
print(f"  PAR absorptance of a single green leaf: "
      f"{LEAF_ABSORPT[0]:.2f} - {LEAF_ABSORPT[1]:.2f}")
print(f"  so a photon striking one leaf once is absorbed with probability"
      f" <= {LEAF_ABSORPT[1]:.2f}.")
print("  A closed reflective cavity can exceed that by multiple passes, so 100 %")
print("  is not excluded outright -- but the bound is then set by the reflectance")
print("  of the enclosure wall, which is where the LEDs are.  This is recorded as")
print("  an unquantified claim rather than as a defect.")
