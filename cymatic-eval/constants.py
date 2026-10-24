"""Every constant used anywhere in this repository, in one place.

Values marked [P] are read off the evaluated preprint; everything else carries
its source.  No script defines a physical constant of its own, so that the
provenance of each number in PAPER.md can be checked by reading this file.
"""

# ---------------------------------------------------------------- the preprint
# M. Mazgal, "Cymatic Stomatal Stimulation and Pulsed Optical Assimilation:
# Scaling from Cybernetic Bioreactors to Industrial-Scale Acoustic Modulation",
# Zenodo, 5 October 2026, DOI 10.5281/zenodo.23156927.
F_REACTOR   = 246.91        # [P] Sec. 2.3  cymatic frequency in the bioreactor, Hz
F_FIELD     = 61.72         # [P] Sec. 3    "4th subharmonic" for open field, Hz
BAND_P      = (50.0, 120.0) # [P] Sec. 3    band the preprint calls PAFT-sensitive, Hz
E_PEAK      = 4500.0        # [P] Sec. 2.2  peak irradiance, W/m^2
T_ON        = 50e-6         # [P] Sec. 2.2  pulse duration, s
T_OFF       = 4000e-6       # [P] Sec. 2.2  dark phase, s
NPQ_LOSS    = 0.60          # [P] Sec. 1    "dissipating up to 60% of absorbed photons"
PLANAR_LOSS = (0.40, 0.50)  # [P] Sec. 2.1  claimed loss of 2D planar LED arrays
YIELD_CLAIM = (0.15, 0.18)  # [P] Sec. 5    claimed net biomass increase

# ------------------------------------------------------------------- radiometry
# PAR photon flux per unit PAR energy; the standard figure for solar PAR and
# for white LEDs alike.  Spectral basis: McCree 1971, Agric. Meteorol. 9, 191.
PAR_UMOL_PER_J = 4.6        # umol photons / J, white LED and solar PAR alike
# Full sun, clear sky, overhead: ~1000 W/m^2 total, ~2000 umol/m^2/s PAR.
FULL_SUN_PPFD  = 2000.0     # umol/m^2/s
LED_WALLPLUG   = 0.50       # photon output / electrical input, good white LED

# ------------------------------------------------------------------ plant physiology
# Light saturation point of C3 leaves: lettuce at the low end, wheat at the high
# end.  Taiz & Zeiger, Plant Physiology; Farquhar & Sharkey 1982.
SAT_C3         = (400.0, 1400.0)   # umol/m^2/s
# RuBisCO carboxylation turnover number, wheat.  von Caemmerer 2000.
KCAT_RUBISCO   = (2.0, 4.0)        # s^-1 per catalytic site, range
# Plastoquinol oxidation at cytochrome b6f, the rate-limiting step of linear
# electron transport.  Haehnel 1984, Annu. Rev. Plant Physiol. 35, 659-693.
PQ_REOX_MS     = (2.0, 20.0)       # ms
# Maximum quantum yield of CO2 assimilation in a canopy, realistic.
QUANTUM_YIELD  = 0.05              # mol CO2 / mol photons
G_PER_MOL_CH2O = 30.0              # g dry matter per mol fixed CO2 (CH2O)
# PAR absorptance of a single green leaf.  McCree 1971.
LEAF_ABSORPT   = (0.84, 0.90)
# Stomatal conductance to water vapour, well-watered C3 crop, and the midday
# depression.  Farquhar & Sharkey 1982.
GS_MORNING     = 0.30              # mol H2O /m^2/s
GS_MIDDAY      = 0.10              # mol H2O /m^2/s, depressed
VPD_MORNING    = 1.0               # kPa
VPD_MIDDAY     = 3.0               # kPa
P_ATM          = 101.3             # kPa

# ------------------------------------------------------------------- acoustics
C_SOUND        = 343.0             # m/s, 20 C
# Hassanien, Hou, Li & Li 2014, J. Integr. Agric. 13(2) 335-348 -- the review the
# preprint cites.  Working band and level of PAFT generators.
PAFT_BAND      = (100.0, 1000.0)   # Hz
PAFT_SPL       = 70.0              # dB SPL at the plant
PAFT_SPL_RANGE = (65.0, 75.0)      # dB, the +/- 5 of the same review
PAFT_R         = (30.0, 60.0)      # m, generator-to-plant distance in that work
# Wind turbines, 2-3 MW class.  Oerlemans, Sijtsma & Mendez Lopez 2007;
# IEC 61400-11 declared apparent sound power levels.
TURB_BLADES    = 3
TURB_RPM       = (9.0, 18.0)       # rpm, operating range
TURB_RPM_RATED = 14.0              # rpm
TURB_RADIUS    = (40.0, 60.0)      # m, blade radius
TURB_R_RATED   = 50.0              # m
TURB_LW        = (100.0, 110.0)    # dB re 1 pW, declared apparent sound power
TURB_LW_RATED  = 105.0             # dB re 1 pW
# Wind-farm turbine spacing, in rotor diameters.
FARM_SPACING_D = (5.0, 10.0)
# Atmospheric absorption at 63 Hz, 10-20 C, 50-80 % RH.  ISO 9613-1.
ATM_ABS_63HZ   = 0.1               # dB per km

# ------------------------------------------------------------------------ grid
GRID_F         = 50.0              # Hz, continental Europe
# Magnetostriction in a transformer core is excited at twice the line frequency
# and its harmonics, because the strain depends on |B|.
GRID_TOL       = 0.05              # Hz, ENTSO-E continental synchronous area

# ------------------------------------------------------------------- utilities
DUTY   = T_ON / (T_ON + T_OFF)
PERIOD = T_ON + T_OFF
A4     = 440.0                     # Hz, equal temperament reference
