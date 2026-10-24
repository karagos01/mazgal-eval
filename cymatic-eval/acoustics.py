"""Whether a wind turbine or a grid transformer can emit 61.72 Hz at a level
that reaches a field, and whether a wind farm can be a phased array.

Sections 7 and 8 of PAPER.md.
"""
import numpy as np
from constants import (F_FIELD, C_SOUND, TURB_BLADES, TURB_RPM, TURB_RPM_RATED,
                       TURB_RADIUS, TURB_R_RATED, TURB_LW, TURB_LW_RATED,
                       PAFT_SPL, PAFT_SPL_RANGE, PAFT_R, FARM_SPACING_D,
                       ATM_ABS_63HZ, GRID_F, GRID_TOL)

bar = lambda c="=": print(c * 78)

# Hemispherical spreading over a reflecting ground plane: Lp = Lw - 10 log(2 pi r^2)
spread_db = lambda r: 10.0 * np.log10(2.0 * np.pi * r ** 2)
Lp = lambda Lw, r: Lw - spread_db(r)
Lw_for = lambda Lp_target, r: Lp_target + spread_db(r)

bar()
print("1. BLADE-PASS FREQUENCY AGAINST THE TARGET")
bar()
print(f"  {'rotor rpm':>10}  {'blade-pass Hz':>14}  {'harmonic of BPF at'}"
      f" {F_FIELD} Hz")
for rpm in [TURB_RPM[0], TURB_RPM_RATED, TURB_RPM[1]]:
    bpf = TURB_BLADES * rpm / 60.0
    print(f"  {rpm:10.1f}  {bpf:14.3f}  {F_FIELD/bpf:28.1f}")
print()
rpm_needed = F_FIELD * 60.0 / TURB_BLADES
print(f"  rotor speed for which BPF = {F_FIELD} Hz:  {rpm_needed:10.1f} rpm")
print(f"  rated rotor speed of the class:         {TURB_RPM_RATED:10.1f} rpm"
      f"   ({rpm_needed/TURB_RPM_RATED:.0f} x)")
bar("-")
omega = rpm_needed * 2.0 * np.pi / 60.0
print(f"  {'blade R':>8}  {'tip speed':>12}  {'Mach':>6}  {'tip accel':>12}"
      f"  {'in g':>10}")
for R in [TURB_RADIUS[0], TURB_R_RATED, TURB_RADIUS[1]]:
    v = omega * R
    a = omega ** 2 * R
    print(f"  {R:8.0f}  {v:9.0f} m/s  {v/C_SOUND:6.1f}  {a:9.0f} m/s2"
          f"  {a/9.81:10.0f}")
print()
print("  'RPM Lock: Electromagnetically braking the rotor via the grid inverter")
print("  forces the turbine to maintain exact rotational speeds ... ensuring a")
print(f"  phase-stable {F_FIELD} Hz emission' requires {rpm_needed:.0f} rpm at the")
print("  rotor.  Braking cannot raise a rotor speed, and the speed asked for is")
print("  supersonic at the blade tip.")
print()
print("  Taken instead as a harmonic of the blade pass, 61.72 Hz is near the 88th.")
print("  'Pitch Tuning' shifting noise by 'a fraction of a degree' moves broadband")
print("  stall noise, which has no line structure to place at a chosen frequency.")

bar()
print("2. THE LEVEL THAT REACHES THE FIELD")
bar()
print(f"  PAFT in the cited review works at {PAFT_SPL:.0f} dB SPL"
      f" (+/- 5) at {PAFT_R[0]:.0f}-{PAFT_R[1]:.0f} m.")
print(f"  Declared apparent sound power of a 2-3 MW turbine:"
      f" {TURB_LW[0]:.0f}-{TURB_LW[1]:.0f} dB re 1 pW"
      f" ({10**(TURB_LW_RATED/10)*1e-12*1e3:.1f} mW at"
      f" {TURB_LW_RATED:.0f} dB), broadband.")
print()
print(f"  {'r [m]':>7} {'turbine':>9} | {'Lw needed for 65':>16} {'70':>6}"
      f" {'75 dB':>6} | {'short at 70':>12} {'ratio':>9}")
for r in [100.0, 300.0, 500.0, 1000.0]:
    sp = Lp(TURB_LW_RATED, r)
    needs = [Lw_for(t, r) for t in (PAFT_SPL_RANGE[0], PAFT_SPL, PAFT_SPL_RANGE[1])]
    short = Lw_for(PAFT_SPL, r) - TURB_LW_RATED
    print(f"  {r:7.0f} {sp:6.1f} dB | {needs[0]:16.1f} {needs[1]:6.1f}"
          f" {needs[2]:6.1f} | {short:9.1f} dB {10**(short/10):8.0f} x")
bar("-")
print("  Sensitivity to the declared sound power, shortfall at 300 m and 70 dB:")
print(f"  {'turbine Lw':>12}  {'shortfall':>10}  {'power ratio':>12}")
for lw in [TURB_LW[0], TURB_LW_RATED, TURB_LW[1]]:
    sh = Lw_for(PAFT_SPL, 300.0) - lw
    print(f"  {lw:9.0f} dB  {sh:7.1f} dB  {10**(sh/10):12.0f} x")
print()
print(f"  Atmospheric absorption at 63 Hz is about {ATM_ABS_63HZ} dB/km"
      f" (ISO 9613-1), so over")
print(f"  1 km it costs {ATM_ABS_63HZ:.1f} dB against the"
      f" {spread_db(1000.0)-spread_db(60.0):.0f} dB of geometric spreading from 60 m")
print("  to 1 km.  Sec. 3 is right that a low frequency travels with 'minimal")
print("  atmospheric attenuation' -- and that is not the loss that matters.")
print("  Choosing the frequency addresses the negligible term.")
print()
print("  All of the above compares the turbine's whole broadband output against")
print("  a requirement in one narrow band, so the real shortfall is larger.")

bar()
print("3. A WIND FARM AS A PHASED ARRAY")
bar()
lam = C_SOUND / F_FIELD
print(f"  wavelength at {F_FIELD} Hz:                 {lam:8.2f} m")
print(f"  element spacing for a grating-lobe-free array (lambda/2): {lam/2:6.2f} m")
rotor_d = 2 * TURB_R_RATED
print(f"  actual spacing in a wind farm,"
      f" {FARM_SPACING_D[0]:.0f}-{FARM_SPACING_D[1]:.0f} rotor diameters:")
for k in FARM_SPACING_D:
    d = k * rotor_d
    print(f"    {k:4.0f} D = {d:7.0f} m = {d/lam:8.1f} wavelengths"
          f"  ({d/(lam/2):.0f} x the limit)")
print()
# phase stability: hold the blade-pass phase to lambda/10 of path difference
dt = (lam / 10.0) / C_SOUND
rev = 60.0 / TURB_RPM_RATED
print(f"  To hold a phase error below lambda/10, the timing of the blade pass")
print(f"  must be stable to {dt*1e3:.2f} ms.  One revolution at"
      f" {TURB_RPM_RATED:.0f} rpm takes {rev:.2f} s,")
print(f"  so that is {dt/rev*360:.3f} degrees of rotor angle, held against gusts,")
print("  across every turbine in the farm simultaneously.")

bar()
print("4. THE TRANSFORMER")
bar()
print(f"  line frequency                     {GRID_F:8.2f} Hz"
      f"  (+/- {GRID_TOL} Hz, ENTSO-E)")
print("  Magnetostrictive strain follows |B|, so the core is excited at 2f:")
print(f"    {', '.join(f'{2*GRID_F*k:.0f}' for k in range(1, 5))} Hz")
print("  A DC bias saturates alternate half cycles, which adds the odd lines:")
print(f"    {', '.join(f'{GRID_F*k:.0f}' for k in range(1, 7))} Hz")
print(f"  target                             {F_FIELD:8.2f} Hz"
      f"  = {F_FIELD/GRID_F:.4f} x f_line")
best = min(range(1, 41), key=lambda k: abs(GRID_F * k - F_FIELD))
print(f"  nearest line available             {GRID_F*best:8.2f} Hz"
      f"  (off by {abs(GRID_F*best - F_FIELD):.2f} Hz)")
print()
print(f"  Every line a grid-locked core can emit is an integer multiple of"
      f" {GRID_F:.0f} Hz.")
print(f"  {F_FIELD} Hz is not one, and no firmware setting creates a spectral line")
print("  at a frequency the excitation does not contain.  Producing it needs an")
print("  independent source at that frequency -- which is a loudspeaker, not a")
print("  'smart-grid inverter modulation'.")
print()
print("  Separately, 'asymmetric DC injection' is half-cycle saturation: the")
print("  geomagnetically-induced-current failure mode, which raises magnetizing")
print("  current, losses, hot-spot temperature and noise.  It is a damage")
print("  mechanism, and grid codes limit injected DC to around 1 A for exactly")
print("  that reason.")
