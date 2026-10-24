#!/usr/bin/env python3
"""Sec. 3: the 8x8 computational swarm, and what limits it.

  "Topology: 1:1 mapping between a compute node (GPU) and a physical Na-ion cell
   sample."
  "Each GPU streams dynamically generated Direct Digital Synthesis (DDS) data to
   its cell. If any node detects a Z_diff anomaly, it broadcasts the parameter
   vector across a high-speed bus."
  "To find the optimal 'Key' in real physical time, a parallel data-mining
   architecture is proposed"                                        -- Sec. 3

The architecture is a search, so the thing to measure is how many candidate
waveforms it can actually evaluate.  Because every evaluation requires a real
charge-discharge on a real cell, the answer is set by electrochemistry and not
by the GPUs -- and the samples wear out while the search runs.
"""
from constants import (CELLS, C_RATES, COIN_CELL_LIFE, DDS_BITS, DDS_RATE_SA_S,
                       DEPOSIT_BYTES, DEPOSIT_FILES, GPU_COUNT, PDF_LICENCE,
                       PSO_EVALUATIONS, ZENODO_LICENCE, tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. Evaluations per day")
P()
P(f"  [P] cells, one per GPU                           {CELLS:>8d}")
P()
P(f"      [A] {'C-rate':>8s} {'charge+discharge':>18s} {'per day':>12s}")
for c in C_RATES:
    hours = 2.0 / c
    per_day = 24.0 / hours * CELLS
    P(f"          {c:>7.1f}C {hours:>15.1f} h {per_day:>12,.0f}")
P()
P("      One evaluation of a candidate waveform is at minimum one charge, and")
P("      a comparable discharge to return the cell to a known state.  Nothing")
P("      about the GPU changes that number.")

P()
P("2. The ceiling, which arrives before the search finishes")
P()
P(f"      [A] coin-cell useful life        {COIN_CELL_LIFE[0]:>6,d} - "
  f"{COIN_CELL_LIFE[1]:,d} cycles")
P(f"      evaluations available from {CELLS} cells, ever:")
for life in COIN_CELL_LIFE:
    total = CELLS * life
    days = total / (24.0 / 2.0 * CELLS)
    P(f"          {life:>6,d} cycles -> {total:>8,d} evaluations, "
      f"{days:>6.0f} days of continuous 1C cycling")
P()
P(f"      [A] particle swarm optimisation typically needs "
  f"{PSO_EVALUATIONS[0]:,.0f} - {PSO_EVALUATIONS[1]:,.0f}")
P("          evaluations on a 10-30 dimensional space, and Sec. 3 calls its own")
P("          parameter space 'hyperdimensional'.")
P()
best = CELLS * COIN_CELL_LIFE[1]
P(f"      So the whole lifetime budget of one set of samples, {best:,d}")
P(f"      evaluations, is at the bottom of the range a PSO run needs, and the")
P("      sample set is destroyed in reaching it.")

P()
P("3. The confound this creates, which the preprint does not mention")
P()
P("      The objective function is the cell's internal resistance, and internal")
P("      resistance rises with cycle count.  So the quantity being minimised")
P("      drifts upward over exactly the timescale of the search, in a direction")
P("      that depends on how many evaluations each cell has already served.")
P()
P("      A swarm that shares its best parameter vector across nodes -- which is")
P("      what Sec. 3 proposes -- shares it between cells of different age.  Any")
P("      apparent improvement found early is confounded with the samples being")
P("      newer, and Sec. 5's isothermal calorimetry does not address this one.")
P()
P("      Sec. 3's own answer, a 'Dynamic Key Trajectory parameterized by the")
P("      State of Charge', addresses drift within a cycle.  Ageing is drift")
P("      across cycles and is not parameterised by SoC.")

P()
P("4. What the GPUs are actually for")
P()
P(f"      [A] DDS stream per cell:")
for rate in DDS_RATE_SA_S:
    mbps = rate * DDS_BITS / 8 / 1e6
    P(f"          {rate / 1e6:>6.0f} MSa/s x {DDS_BITS} bit = {mbps:>7.0f} MB/s"
      f"   -> {mbps * CELLS:>8.0f} MB/s for {CELLS}")
P()
P("      That is a data-movement task. It needs bandwidth and determinism, not")
P("      floating-point throughput, and nothing in Sec. 3 describes a")
P("      computation that would occupy a GPU between evaluations that arrive")
P("      every two hours.")
P()
P("      Sec. 4 then says the opposite of Sec. 3 about where generation")
P("      happens:")
P("  [P] \"Microsecond-level current/voltage logging fed into a high-speed DSP")
P("      or FPGA (e.g. STM32/Zynq architectures) acting as the local generative")
P("      engine.\"")
P()
P("      If the local FPGA is the generative engine then the GPU is not")
P("      streaming the waveform, and the 1:1 GPU-to-cell mapping has no work")
P("      left to do. The two sections describe two different machines.")

P()
P("5. Sec. 6 against what the deposit contains")
P()
P("  [P] Sec. 6, \"Structure of Provided Data (Zenodo Repository)\":")
for d in ("/Hardware: Gerber, BOM, 3D STEP",
          "/Software: CUDA kernels, PSO synchronization scripts, DDS streaming code",
          "/Datasets: high-speed DAQ logs, isothermal calorimetry, voltage curves"):
    P(f"          {d}")
P()
P(f"      the deposit holds                      {DEPOSIT_FILES} file, "
  f"{DEPOSIT_BYTES:,d} bytes")
P("      which is the four-page PDF and nothing else.")
P()
P(f"  [P] the PDF header proposes:   {PDF_LICENCE}")
P(f"      the Zenodo record carries: {ZENODO_LICENCE} only")
P()
P("      The section is written in the present tense about data that is not")
P("      there. That is a stronger version of the same pattern as the cymatic")
P("      deposit's Sec. 6, which promises a GitHub repository in the future")
P("      tense and names none.")
