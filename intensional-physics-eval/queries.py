#!/usr/bin/env python3
"""IPC Sec. 5: "evaluating millions of physical queries per millisecond".

That is a rate, so it can be put against the two ceilings any GPU has -- its
arithmetic throughput and its memory bandwidth -- for each of the two node sizes
Sec. 3 defines.  The answer is interesting in both directions: for the small
node the claim fits with room to spare, and for the large one it is off by a
factor of 54.

Then the same rate is put against the application it is claimed for.  Sec. 4
makes ray marching the mechanism by which the scene is observed at all, so the
budget that matters is queries per pixel per frame, and there the claimed rate
is several times too small.
"""
from constants import (BANDWIDTH, FRAME_RATE, GPU_NAME, IPC_CALLS_IT_SYMPLECTIC,
                       IPC_NODE_DIMS, IPC_QUERIES_PER_MS, MARCH_STEPS,
                       NERF_QUERIES_PER_IMAGE, NERF_SECONDS_PER_FRAME, PIXELS,
                       SCREEN, SYMPLECTIC_IN_REFERENCES, TENSOR_TFLOPS,
                       V10_CALLED_IT, WMMA_TILE, mma_flops, node_bytes,
                       tag_report)

P = print
CLAIMED = IPC_QUERIES_PER_MS * 1000.0   # queries per second

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()
P(f"      Hardware figures are the {GPU_NAME} the author's own preprints")
P("      specify, from the catalogue.  No GPU is needed to run this.")
P()

P("1. The claimed rate against the card, for each node size")
P()
P(f"  [P] \"millions of physical queries per millisecond\" = "
  f"{CLAIMED:,.0f} /s and up")
P()
for dim in IPC_NODE_DIMS:
    nb, fl = node_bytes(dim), mma_flops(dim)
    comp = TENSOR_TFLOPS / fl
    band = BANDWIDTH / (2 * nb)          # read the node, write it back
    limit = min(comp, band)
    which = "bandwidth" if band < comp else "compute"
    P(f"      {dim}x{dim} node  ({nb:,} B, {fl:,} FLOP per MMA)")
    P(f"        compute ceiling            {comp:>18,.0f} queries/s")
    P(f"        bandwidth ceiling          {band:>18,.0f} queries/s")
    P(f"        binding                    {limit:>18,.0f} queries/s   "
      f"({which})")
    P(f"        vs the claim               {limit / CLAIMED:>18.2f} x   "
      + ("the claim FITS" if limit >= CLAIMED else "the claim EXCEEDS the card"))
    P()
P("      So the claim is true for the 4x4 node with 14x of headroom, and")
P("      false by 54x for the 112x112 node, and Sec. 5 makes it for both at")
P("      once.  Worth stating plainly: half of this claim is correct.")

P()
P("2. But the node sizes do not match the hardware's tile")
P()
P(f"  [V] tensor-core MMA granularity      {WMMA_TILE}x{WMMA_TILE}")
for dim in IPC_NODE_DIMS:
    tiles = -(-dim // WMMA_TILE)          # ceiling division
    occupancy = (dim * dim) / (tiles * WMMA_TILE) ** 2
    P(f"      {dim:>3d}x{dim:<3d} node needs {tiles}x{tiles} tile(s), "
      f"occupancy {occupancy:>6.1%}")
P()
P("      A 4x4 node fills one sixteenth of a 16x16 tile, so the compute")
P("      ceiling above is optimistic by that factor unless many nodes are")
P("      packed into one tile -- which is possible, but is a different")
P("      algorithm from the one-node-one-MMA model Sec. 3 describes.  112 is")
P("      also not a multiple of 16, so it needs 7x7 tiles at 100% only by")
P("      coincidence of 112 = 7 x 16.  That one is exact.")

P()
P("3. The rate against the application it is claimed for")
P()
P("  [P] IPC Sec. 4: a cast ray \"interrogates\" the local node at each step,")
P("      so every march step is a query.")
P()
P(f"      [A] target {SCREEN[0]}x{SCREEN[1]} at {FRAME_RATE:.0f} Hz "
  f"= {PIXELS * FRAME_RATE:,.0f} pixel-frames/s")
P()
P(f"      {'steps/pixel':>12s} {'queries/s needed':>20s} {'vs the claim':>14s}")
for steps in MARCH_STEPS:
    need = PIXELS * steps * FRAME_RATE
    P(f"      {steps:>12d} {need:>20,.0f} {need / CLAIMED:>13.2f}x")
P()
P(f"      the claimed rate buys           "
  f"{CLAIMED / FRAME_RATE / PIXELS:>8.1f} march steps per pixel")
P()
P("      Volumetric ray marching normally wants 64 to 256 samples per pixel,")
P("      so the claimed rate is 4 to 32 times short of its own application --")
P("      and that is before any of those steps does physics, writes a result,")
P("      or reads the ray state.  The rate is simultaneously achievable in the")
P("      abstract and insufficient for the purpose it is quoted for.")

P()
P("4. What the paper's own rendering reference cost")
P()
P(f"  [V] NeRF, reference [4] of both preprints:")
P(f"      queries per rendered image     "
  f"{NERF_QUERIES_PER_IMAGE[0] / 1e6:>8.0f} - "
  f"{NERF_QUERIES_PER_IMAGE[1] / 1e6:.0f} million")
P(f"      time per frame on a V100       {NERF_SECONDS_PER_FRAME:>8.1f} s"
  f"   = {1 / NERF_SECONDS_PER_FRAME:.3f} frames/s")
P()
P("      So the work cited as the predecessor for \"absolute real-time\"")
P("      volumetric synthesis ran at about 0.03 frames per second.  Its query")
P("      count per image is in the same range this script computes as")
P("      necessary, which is a point in the preprint's favour: the")
P("      architecture's estimate of how much work a frame takes is right.")
P("      What it gets wrong is how fast that work can be done.")

P()
P("5. The word that got stronger between versions")
P()
P(f"  [P] openQL v1.0 Sec. 2.3 said the update \"{V10_CALLED_IT}\"")
P(f"  [P] IPC Sec. 3 calls it \"a symplectic discrete Hamiltonian operator\""
  f"   {IPC_CALLS_IT_SYMPLECTIC}")
P()
P("      The expression is unchanged:  S(t+1) = sigma(W_PINN (x) S(t) + b)")
P()
P(f"  [V] \"symplectic\" occurs in {SYMPLECTIC_IN_REFERENCES} work cited by")
P("      either preprint -- Baez, about the 56-dimensional Freudenthal space")
P("      for E7 -- and not in connection with a time step.")
P()
P("      This claim was already measured in openql-eval/symplectic.py and the")
P("      numbers are reproduced there, not here, to avoid duplicating a")
P("      measurement: with sigma = tanh a harmonic oscillator drifts to")
P("      2e-5 x E(0) over 1e5 steps, and a W fitted to exact pendulum data")
P("      reaches 10.2 x E(0), while leapfrog holds 1.0000 x E(0) untrained.")
P("      A nonlinearity applied after an affine map is not a symplectic map;")
P("      stating it more strongly in a later paper does not change that.")
