#!/usr/bin/env python3
"""openQL v1.1 Sec. 6.1, the one section that is new in the revision.

  "Applying blind brute-force to a million-node grid yields an insurmountable
   combinatorial explosion. However, employing an evolutionary genetic algorithm
   over the 12D openQL engine circumvents this limit due to the hardware's
   zero-branching nature."
  "Because Tensor Cores execute MMA instructions without conditional branching,
   computing empty space takes the exact same nanosecond fraction as computing a
   highly complex, asymmetric copper coil. By defining only the spatial volume
   and voltage limit (e.g. 48V), the engine can simulate millions of organically
   mutated topologies per day."

Two things are computed: how many update sweeps of the grid "millions per day"
leaves per candidate topology, and what the zero-branching argument actually
buys, which is the opposite of what the section claims for it.
"""
from constants import (BANDWIDTH, FP16_BYTES, GRID_EMPTY_FRACTION, V11_GRID_NODES,
                       V11_NODE_DIM, V11_TOPOLOGIES_PER_DAY, V11_VOLTAGE, VRAM,
                       node_bytes, tag_report)

P = print
SECONDS_PER_DAY = 86400.0

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. What one evaluation costs")
P()
nb = node_bytes(V11_NODE_DIM)
state = V11_GRID_NODES * nb
sweep = 2 * state           # read the whole grid, write it back
P(f"  [P] {V11_NODE_DIM}x{V11_NODE_DIM} fp16 node                  "
  f"{nb:>14,d} B")
P(f"  [P] million-node grid, state only       {state / 2**20:>14,.1f} MiB")
P(f"      fits in {VRAM / 2**30:.0f} GiB                        "
  f"{VRAM / state:>14,.0f} such grids")
P(f"      one full update sweep moves         {sweep / 2**20:>14,.1f} MiB")
P(f"      time for one sweep at {BANDWIDTH / 1e9:.0f} GB/s       "
  f"{sweep / BANDWIDTH * 1e3:>14.3f} ms")
P()
P("      This is a bandwidth bound, not a FLOP bound, so it is the floor on")
P("      what a sweep can cost however the arithmetic is arranged.")

P()
P("2. How many sweeps \"millions per day\" leaves")
P()
P(f"      {'topologies/day':>16s} {'time each':>14s} {'sweeps affordable':>19s}")
for target in (V11_TOPOLOGIES_PER_DAY, 2e6, 5e6, 10e6):
    t = SECONDS_PER_DAY / target
    P(f"      {target:>16,.0f} {t * 1e3:>11.3f} ms "
      f"{t * BANDWIDTH / sweep:>18.1f}")
P()
lo = SECONDS_PER_DAY / 10e6 * BANDWIDTH / sweep
hi = SECONDS_PER_DAY / V11_TOPOLOGIES_PER_DAY * BANDWIDTH / sweep
P(f"      So the claim requires a converged field solution in {lo:.0f} to")
P(f"      {hi:.0f} sweeps of the whole grid, depending on how many millions")
P("      is meant.")
P()
P("      For scale: a multigrid Poisson solve on a 100^3 grid is in that")
P("      range for ONE linear solve.  And the objective function Sec. 6.1")
P("      describes is not one linear solve -- it has to evaluate, at minimum:")
for item in ("the magnetostatic field of the proposed winding",
             "the resulting torque and its ripple over a full electrical cycle",
             "cogging torque, which is a function of rotor position",
             "iron loss, which needs the B-H history at every node",
             "the thermal steady state, which needs the loss field as input"):
    P(f"        - {item}")
P()
P("      Each of those is at least one solve, several are coupled, and the")
P("      position-dependent ones need the field recomputed at many rotor")
P("      angles.  The budget is one solve's worth of sweeps for all of it.")

P()
P("3. What the zero-branching argument actually buys")
P()
P("  [P] \"computing empty space takes the exact same nanosecond fraction as")
P("      computing a highly complex, asymmetric copper coil\"")
P()
P("      This is TRUE, and it is the one part of the argument that survives")
P("      intact.  An MMA pipeline does not skip work, so cost is independent")
P("      of content.  But that is a statement that there is no SAVING on empty")
P("      space, not that there is a speed advantage -- and a conventional")
P("      solver's main economy on a motor grid is precisely that most of the")
P("      volume is air:")
P()
P(f"      {'grid empty':>12s} {'sparse solver does':>20s} {'dense does':>12s} "
  f"{'penalty':>10s}")
for frac in GRID_EMPTY_FRACTION:
    P(f"      {frac:>11.0%} {1 - frac:>19.1%} {1.0:>11.0%} "
      f"{1 / (1 - frac):>9.1f}x")
P()
P("      So zero-branching is the price of the architecture, not its")
P("      advantage.  Sec. 6.1 presents the absence of a saving as the thing")
P("      that \"circumvents\" the combinatorial limit.")

P()
P("4. And the combinatorial claim is not about the grid at all")
P()
P("  [P] \"Applying blind brute-force to a million-node grid yields an")
P("      insurmountable combinatorial explosion.\"")
P()
P("      The explosion is in the SEARCH SPACE of topologies, not in the cost")
P("      of evaluating one.  A genetic algorithm addresses it by evaluating")
P("      few candidates well, so what it needs is a cheap, accurate objective")
P("      -- which is what Sec. 2 computes the budget for.  Making each")
P("      evaluation branchless does not reduce the number of candidates, and")
P("      the number of candidates is the quantity called insurmountable.")
P()
P(f"      [P] the stated inputs are a spatial volume and \"{V11_VOLTAGE:.0f}V\",")
P("      with no stated parameterisation of the winding, so the dimension of")
P("      the search space is not given and cannot be checked here.")

P()
P("5. The one new physical claim in Sec. 6.1")
P()
P("  [P] \"fractal-like winding patterns that minimize skin effect\"")
P()
P("      Skin effect is current crowding toward a conductor's surface, and the")
P("      established remedy is to SUBDIVIDE the conductor into strands thinner")
P("      than the skin depth and transpose them, which is Litz wire.  A")
P("      fractal boundary increases surface area at fixed cross-section, which")
P("      is the opposite move: more perimeter for the same copper means more")
P("      of the conductor sits in the high-current-density region.")
P()
P("      Fractal and space-filling geometries do have real uses in RF")
P("      antennas, where a long electrical path in a small volume is wanted.")
P("      That is a different objective from minimising AC resistance in a")
P("      motor winding, and Sec. 6.1 gives no mechanism linking the two.")
P("      This is recorded as an unsupported claim rather than a measured")
P("      defect: no skin-effect calculation is attempted here, because the")
P("      section specifies no winding geometry to compute one for.")
