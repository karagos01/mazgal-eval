#!/usr/bin/env python3
"""What a +/-224D node costs on the card the author's own preprints specify.

  "The engine executes pure, mathematically perfect E=mc^2 annihilation
   natively in a single processor clock cycle."                 -- Sec. 3
  "At this specific resolution (224D), the silicon architecture of graphics
   cards transforms into a 100% saturated quantum field simulator."
                                                                -- Sec. 4
  "Fusion Reactor (Tokamak) Simulation: Computing exact plasma behavior down to
   annihilation losses."                                        -- Sec. 5

Reference figures are the RTX 3090 catalogue specifications: 142 TFLOP/s fp16
on the tensor cores, 936 GB/s, 1.70 GHz boost, 24 GiB.  No GPU is needed to run
this; it is arithmetic on published specifications.
"""
import math

from constants import (BANDWIDTH, CLOCK, DIMS, FLOP_PER_CYCLE, FP16_BYTES,
                       GPU_NAME, GRID_NODES, TENSOR_TFLOPS, TOKAMAK_N_PER_M3,
                       VRAM, matmul_flops, node_bytes, tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()
P(f"      hardware: {GPU_NAME}, {TENSOR_TFLOPS / 1e12:.0f} TFLOP/s fp16 "
  f"tensor, {BANDWIDTH / 1e9:.0f} GB/s, {CLOCK / 1e9:.2f} GHz, "
  f"{VRAM / 2**30:.0f} GiB")
P()

P('1. "a single processor clock cycle"')
P()
P(f"      whole-GPU fp16 throughput      {FLOP_PER_CYCLE:>14,.0f} FLOP/cycle")
P()
P(f"      {'node':>10s} {'FLOP per product':>18s} "
  f"{'cycles of the WHOLE GPU':>25s}")
for d in DIMS:
    fl = matmul_flops(d)
    P(f"      {f'{d}x{d}':>10s} {fl:>18,d} {fl / FLOP_PER_CYCLE:>24.2f}")
P()
big = matmul_flops(max(DIMS)) / FLOP_PER_CYCLE
mid = matmul_flops(112) / FLOP_PER_CYCLE
P(f"      So one annihilation at 224D is {big:.0f} cycles of the entire card,")
P(f"      not one, and {big / mid:.0f}x worse than the 112D case openQL made the")
P("      same claim for -- which is what cubing the dimension does.")
P()
P("      The claim is also of a kind the hardware cannot satisfy in principle:")
P("      a WMMA instruction has a latency of several cycles, a 224D node is")
P("      196 of them, and the operands have to be fetched first, which is the")
P("      next section.")

P()
P("2. What a +/-224D node costs to hold")
P()
P(f"      {'layer':>10s} {'one node':>12s} {'with mirror':>14s} "
  f"{'pairs in VRAM':>15s}")
for d in DIMS:
    nb = node_bytes(d)
    pair = 2 * nb
    P(f"      {'+/-' + str(d):>10s} {nb / 1024:>9.1f} KiB "
      f"{pair / 1024:>11.1f} KiB {VRAM / pair:>15,.0f}")
P()
d = max(DIMS)
resident = VRAM / (2 * node_bytes(d))
side = round(resident ** (1 / 3))
P(f"      At the +/-224D layer the card holds {resident:,.0f} node pairs, a cube")
P(f"      {side} nodes on a side, state only -- nothing left for the rule")
P("      matrices, the ray state or an output image.")
P()
per_mm3 = TOKAMAK_N_PER_M3 * 1e-9
P("      Against Sec. 5's tokamak application, at one node per particle:")
P(f"        nodes the card holds                   {resident:>14,.0f}")
P(f"        [A] particles in 1 mm^3 at 1e20 m^-3   {per_mm3:>14,.0f}")
P(f"        shortfall                              {per_mm3 / resident:>14,.0f}x"
  f"   ({math.log10(per_mm3 / resident):.1f} orders)")
P()
P("      So the grid is about six orders of magnitude short of a single cubic")
P("      millimetre of plasma.  The density is an order-of-magnitude figure and")
P("      carries nothing here beyond the order of the shortfall.")

P()
P("3. The step rate the bandwidth allows, for a fixed grid")
P()
P("      A table over a card filled to capacity would be degenerate: filling")
P("      the card and sweeping it once is about two VRAM passes whatever the")
P("      node size, so every layer would return the same number by")
P("      construction.  The grid is therefore held fixed and the layer varied,")
P("      which is what makes the cost of the doubling visible.")
P()
P(f"      [A] grid {GRID_NODES:,d} node pairs")
P()
P(f"      {'layer':>10s} {'state':>14s} {'bytes per sweep':>18s} "
  f"{'sweeps/s':>10s} {'fits in VRAM':>13s}")
for d in DIMS:
    pair = 2 * node_bytes(d)
    state = GRID_NODES * pair
    per_step = 2 * state                 # read the grid, write it back
    P(f"      {'+/-' + str(d):>10s} {state / 2**30:>11.2f} GiB "
      f"{per_step / 2**30:>15.2f} GiB {BANDWIDTH / per_step:>10.2f} "
      f"{str(state <= VRAM):>13s}")
P()
pair112, pair224 = 2 * node_bytes(112), 2 * node_bytes(224)
P(f"      112D -> 224D multiplies the traffic per sweep by "
  f"{pair224 / pair112:.0f}x.")
P()
P("      A million-node grid does not fit on the card at either of the two")
P("      upper layers.  For the largest grid that does fit at +/-224D:")
fit = VRAM / pair224
P(f"        node pairs                             {fit:>14,.0f}")
P(f"        bytes per sweep                        "
  f"{2 * fit * pair224 / 2**30:>11.2f} GiB")
P(f"        sweeps/s                               "
  f"{BANDWIDTH / (2 * fit * pair224):>14.2f}")
P("      i.e. about 18 Hz for a 50-node cube.  Real time is 60.")

P()
P("4. The roofline, which the doubling does not move")
P()
P(f"      {'layer':>10s} {'state':>9s} {'matrix':>11s} {'overhead':>9s} "
  f"{'W@s FLOP/B':>12s} {'W@S FLOP/B':>12s}")
for d in DIMS:
    state = d * FP16_BYTES               # the d potentials the node encodes
    nb = node_bytes(d)                   # the dxd matrix that encodes them
    mv = (2 * d ** 2) / (2 * state)      # matrix-vector on the state
    mm = matmul_flops(d) / (2 * nb)      # matrix-matrix on the node
    P(f"      {'+/-' + str(d):>10s} {state:>6,d} B {nb:>8,d} B "
      f"{nb / state:>8.0f}x {mv:>12.1f} {mm:>12.1f}")
P()
P("      The last two columns are equal at every layer, which is the result")
P("      openql-eval measured for 112 and which survives the doubling: the")
P("      matrix form sits at exactly the same point on the roofline as the")
P("      state it encodes, while costing d times the traffic and d times the")
P("      arithmetic.  Encoding d numbers as a d x d matrix buys no arithmetic")
P("      intensity at any d.")
P()
P("      Which is the measured sense in which Sec. 4's \"100% saturated\" is")
P("      true and not useful.  The tiles are full -- that is what 224/16 = 14")
P("      exactly buys -- and the card is waiting on memory regardless.")

P()
P("5. What the doubling costs, relative to openQL")
P()
a, b = 112, 224
P(f"      {'quantity':>24s} {'112D':>14s} {'224D':>14s} {'ratio':>8s}")
for label, x, y in [("node footprint, bytes", node_bytes(a), node_bytes(b)),
                    ("with the mirror, bytes", 2 * node_bytes(a),
                     2 * node_bytes(b)),
                    ("FLOP per product", matmul_flops(a), matmul_flops(b)),
                    ("WMMA tiles per node", (a // 16) ** 2, (b // 16) ** 2)]:
    P(f"      {label:>24s} {x:>14,d} {y:>14,d} {y / x:>7.0f}x")
P()
P("      So the step from openQL to openOmega is 4x the memory per node, 8x")
P("      the arithmetic and 4x the tiles, before the mirror doubles the memory")
P("      again.  Sec. 4 presents it as costless because the alignment is")
P("      preserved; alignment is about waste inside a tile, not about how many")
P("      tiles there are.")
