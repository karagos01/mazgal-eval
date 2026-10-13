#!/usr/bin/env python3
"""Where 224 comes from, and where the paper says it comes from.

  "By introducing the Cayley-Dickson construction and the algebra of sedenions,
   the engine expands the phase space from 12D and 112D to a full 224D"
                                                            -- abstract
  "+/-224D (Grand Unification): An extreme matrix space created by dimensional
   doubling."                                                -- Sec. 2
  "Sedenion architecture (which is the mathematical foundation of the -224D
   space) requires no software intermediary steps."          -- Sec. 4
  "The dimension 224 is a perfect multiple of 16 (224 / 16 = 14). Therefore, the
   224D state node is not a hardware burden but a perfectly aligned array of
   14 x 14 instruction blocks."                              -- Sec. 4

The multiple-of-16 claim is checked and is correct.  The Cayley-Dickson claim
is checked against the construction built in zerodivisors.py and is not.
"""
from constants import (CLAIMS_224_OVER_16, DIMS, DOUBLED_FROM, M_THEORY_DIM,
                       SEDENION_DIM, STRING_CRITICAL_DIMS, WMMA_TILE,
                       cayley_dickson_dims, tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. Is 224 in the Cayley-Dickson tower?")
P()
tower = cayley_dickson_dims(512)
P(f"      the tower doubles at every step: {tower}")
P(f"      sedenions, the algebra the paper names: dimension {SEDENION_DIM}"
  f"   in the tower: {SEDENION_DIM in tower}")
P()
for d in DIMS + (2 * max(DIMS),):
    P(f"      {d:>4d} in the tower: {str(d in tower):>5s}")
P()
P(f"      224 = 2 x {DOUBLED_FROM} = {2 * DOUBLED_FROM}, and "
  f"{DOUBLED_FROM} is itself not in the tower.")
P()
P("      So the doubling the paper invokes is not Cayley-Dickson doubling.")
P("      Cayley-Dickson doubling takes an algebra of dimension n to one of")
P("      dimension 2n starting from 1, which gives the powers of two and")
P("      nothing else; 112 and 224 are not among them.  Multiplying an")
P("      arbitrary number by two is a different operation that happens to")
P("      share the word.")
P()
P("      And the sedenions are 16-dimensional, so \"Sedenion architecture")
P("      (which is the mathematical foundation of the -224D space)\" does not")
P("      connect: nothing in the sedenions has 224 of anything.  The algebra")
P("      is real, its zero divisors are real (zerodivisors.py Sec. 1-2), and")
P("      the dimension it lives in is 16.")
P()
P("      Where 112 came from was already measured in openql-eval: the openQL")
P("      v1.0 sentence that derived it was deleted in v1.1 without being")
P("      replaced, so 224 is a doubling of a number the series no longer")
P("      offers a derivation for.")

P()
P("2. The multiple-of-16 claim, which is correct")
P()
P(f"      [V] WMMA tile granularity: {WMMA_TILE} x {WMMA_TILE}")
P()
P(f"      {'dim':>5s} {'/16':>8s} {'exact':>7s} {'tiles':>8s} "
  f"{'MMA ops per node':>18s} {'occupancy':>11s}")
for d in DIMS:
    tiles = -(-d // WMMA_TILE)
    occ = (d * d) / (tiles * WMMA_TILE) ** 2
    P(f"      {d:>5d} {d / WMMA_TILE:>8.3f} {str(d % WMMA_TILE == 0):>7s} "
      f"{tiles:>4d}x{tiles:<3d} {tiles * tiles:>18d} {occ:>10.2%}")
P()
P(f"      224 / 16 = {CLAIMS_224_OVER_16} exactly, so Sec. 4 is right about")
P("      the alignment and right that it is not a hardware burden in the")
P("      sense of wasted lanes.  The 100 % saturation claim is also correct")
P("      as an occupancy statement.")
P()
P("      Two things the section does not say.  112 / 16 = 7 is exact too, so")
P("      the alignment is inherited rather than gained -- doubling a multiple")
P("      of 16 stays a multiple of 16, for any such number.  And a 224D node")
P(f"      is {14 * 14} MMA operations, not one: the tiles are the unit the")
P("      hardware executes, and there are 196 of them per node.")
P()
P(f"      The 12D layer is the one that never tiled: 12 / 16 = 0.75, so a")
P("      12x12 node fills 56.25 % of a single tile.  That layer is carried")
P("      unchanged from openQL and the alignment argument does not cover it.")

P()
P("3. \"Negative dimensions\"")
P()
P("      [P] Sec. 2 divides space into \"positive (matter) and negative")
P("          (vacuum/antimatter) intensional nodes\" at +/-12D, +/-112D, +/-224D")
P()
P("      Dimension is a cardinality: the number of coordinates needed to")
P("      specify a point.  There is no vector space of dimension -224 over any")
P("      field, because there is no set with -224 elements in a basis.")
P()
P("      What the paper describes -- a mirror copy of the state space holding")
P("      the antiparticle sector -- is a perfectly ordinary construction, and")
P("      it is MORE dimensions, not negative ones:")
P()
P(f"      {'layer':>10s} {'positive':>10s} {'mirror':>8s} {'total state':>13s}")
for d in DIMS:
    P(f"      {'+/-' + str(d):>10s} {d:>10d} {d:>8d} {2 * d:>13d}")
P(f"      {'all three':>10s} {sum(DIMS):>10d} {sum(DIMS):>8d} "
  f"{2 * sum(DIMS):>13d}")
P()
P("      So the engine's largest layer is a 448-dimensional state, which is")
P("      what the hardware has to hold and move.  Calling half of it negative")
P("      is a labelling of the two halves, not a property of the space, and")
P("      the costs in hardware.py are computed on the real figure.")

P()
P("4. The dimensions the cited physics actually uses")
P()
P("      [P] Sec. 2: \"The positive 224D contains complete string theory and")
P("          supersymmetry (all possible vibrations of matter).\"")
P()
P(f"      [V] critical dimension, superstring theory      "
  f"{STRING_CRITICAL_DIMS[0]:>4d}")
P(f"      [V] critical dimension, bosonic string theory   "
  f"{STRING_CRITICAL_DIMS[1]:>4d}")
P(f"      [V] M-theory                                    {M_THEORY_DIM:>4d}")
P(f"      [P] the layer said to contain it                {max(DIMS):>4d}")
P()
for d in STRING_CRITICAL_DIMS + (M_THEORY_DIM,):
    P(f"          224 == {d:>2d}:  {224 == d}")
P()
P("      The critical dimensions are not free parameters; they are fixed by")
P("      anomaly cancellation.  224 is not one of them, and the section gives")
P("      no embedding, compactification or other relation between the two")
P("      numbers.  This is recorded as an unsupported claim rather than a")
P("      measured defect: there is no construction here to check.")
