"""Where the two frequencies of the preprint come from, and whether the band it
cites contains them.

Sections 2 and 3 of PAPER.md.
"""
import numpy as np
from constants import (A4, F_REACTOR, F_FIELD, BAND_P, PAFT_BAND, PAFT_R,
                       PAFT_SPL, T_ON, T_OFF, PERIOD, C_SOUND)

bar = lambda c="=": print(c * 78)
note = lambda n: A4 * 2.0 ** (n / 12.0)

bar()
print("1. NEAREST EQUAL-TEMPERED PITCH TO EACH PUBLISHED FREQUENCY")
bar()
print(f"  {'published':>22}  {'nearest 12-TET':>16}  {'exact':>10}  "
      f"{'error':>10}  {'cents':>8}")
for f, where in [(F_REACTOR, "Sec. 2.3, reactor"), (F_FIELD, "Sec. 3, field")]:
    # semitones from A4, rounded to the nearest
    n = int(round(12.0 * np.log2(f / A4)))
    exact = note(n)
    cents = 1200.0 * np.log2(f / exact)
    midi = 69 + n   # scientific pitch notation
    sci = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"][midi % 12]
    sci_oct = midi // 12 - 1
    print(f"  {f:10.3f} Hz {where:>22}  {sci}{sci_oct:<14}  {exact:10.3f}  "
          f"{f - exact:+10.3f}  {cents:+8.2f}")
print()
print("  A cent is 1/100 of a semitone; the just-noticeable pitch difference for")
print("  a trained listener is about 5 cents.  Both published frequencies are")
print("  inside that, i.e. they are the note B as a tuner would set it.")

bar()
print("2. THE OPTICAL TIMING IS THE SAME NUMBER")
bar()
f_pulse = 1.0 / PERIOD
print(f"  pulse               {T_ON*1e6:10.1f} us")
print(f"  dark phase          {T_OFF*1e6:10.1f} us")
print(f"  period              {PERIOD*1e3:10.3f} ms")
print(f"  repetition rate     {f_pulse:10.2f} Hz")
print(f"  cymatic frequency   {F_REACTOR:10.2f} Hz")
print(f"  difference          {abs(f_pulse - F_REACTOR):10.2e} Hz"
      f"   ({abs(f_pulse-F_REACTOR)/F_REACTOR:.1e} relative)")
print()
print("  Sec. 2.2 derives the optical timing from 'the enzymatic turnover rate of")
print("  the Calvin cycle'.  Sec. 2.3 derives the acoustic frequency from guard")
print("  cell mechanics.  Measured, they agree to 1.5 parts in 100 000, which is")
print("  the rounding of 246.91 Hz to two decimals -- they are one number, and")
print("  that number is B3.")

bar()
print("3. THE SUBHARMONIC")
bar()
print(f"  F_reactor / F_field = {F_REACTOR / F_FIELD:.5f}")
print(f"  f/4 is the 4th subharmonic, two octaves down -- the naming is correct.")
print(f"  wavelength at {F_FIELD} Hz:  {C_SOUND / F_FIELD:.2f} m")
print(f"  wavelength at {F_REACTOR} Hz: {C_SOUND / F_REACTOR:.3f} m")

bar()
print("4. THE BAND")
bar()
inb = lambda f, b: b[0] <= f <= b[1]
print(f"  band asserted by the preprint, Sec. 3:        "
      f"{BAND_P[0]:7.1f} - {BAND_P[1]:7.1f} Hz")
print(f"  band of the review it cites (Hassanien 2014): "
      f"{PAFT_BAND[0]:7.1f} - {PAFT_BAND[1]:7.1f} Hz")
print(f"    that review's working level: {PAFT_SPL:.0f} dB SPL at"
      f" {PAFT_R[0]:.0f}-{PAFT_R[1]:.0f} m")
print()
print(f"  {'frequency':>18}  {'in preprint band':>18}  {'in cited band':>15}")
for f, lab in [(F_REACTOR, "reactor 246.91 Hz"), (F_FIELD, "field    61.72 Hz")]:
    print(f"  {lab:>18}  {str(inb(f, BAND_P)):>18}  {str(inb(f, PAFT_BAND)):>15}")
print()
print("  Sec. 3 divides by four so that the result 'falls perfectly within the")
print("  empirically proven PAFT sensitive band'.  Measured against the band of")
print("  the review it cites for that claim, the division does the opposite:")
print("  246.91 Hz was inside, 61.72 Hz is below it.")
