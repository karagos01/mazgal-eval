#!/usr/bin/env python3
"""Every constant used in this repository, in one place, with its provenance.

No other script here defines a constant.

  [P]  a value taken from one of the two preprints
  [V]  an external value verified against a named source, with the source given
  [A]  an ASSUMED range, swept rather than asserted
"""

# ---------------------------------------------------------------------------
# [P] The two deposits of 8 October 2026
#
#   IPC  = "Intensional Physics Computing: Generating Virtual Reality via
#           Multidimensional Tensor Core Queries", DOI 10.5281/zenodo.23241777
#   v1.1 = "openQL / openOL: Tensor Matrix Architecture ... (Version 1.1)",
#           DOI 10.5281/zenodo.23241148, a revision of 10.5281/zenodo.23112560
# ---------------------------------------------------------------------------
IPC_QUERIES_PER_MS = 1e6      # [P] IPC Sec. 5 "evaluating millions of physical
                              #     queries per millisecond"
IPC_NODE_DIMS      = (4, 112) # [P] IPC Sec. 3 "a 4x4 (for 12D macroscopic
                              #     physics) or 112x112 (for quantum-level
                              #     physics) block matrix"
V11_TOPOLOGIES_PER_DAY = 1e6  # [P] v1.1 Sec. 6.1 "simulate millions of
                              #     organically mutated topologies per day"
V11_GRID_NODES     = 1_000_000  # [P] v1.1 Sec. 6.1 "a million-node grid"
V11_NODE_DIM       = 12       # [P] v1.1 Sec. 3.1, the 12D macroscopic layer
V11_VOLTAGE        = 48.0     # [P] v1.1 Sec. 6.1 "voltage limit (e.g. 48V)"

# The update rule, identical in both and in openQL v1.0, now with a stronger
# word attached:  S(t+1) = sigma(W_PINN (x) S(t) + b)
IPC_CALLS_IT_SYMPLECTIC = True   # [P] IPC Sec. 3 "a symplectic discrete
                                 #     Hamiltonian operator"
V10_CALLED_IT = "preserves the Lie group symmetries"   # [P] openQL v1.0 Sec. 2.3

# What v1.1 removed relative to v1.0.  Four of the six are claims measured in
# the openql-eval repository; the coincidence is recorded, causation is not
# claimed.
V11_REMOVED = [
    ("the derivation of 112",
     "The dimensionality of 112 in openOL is derived from the necessary "
     "degrees of freedom to encapsulate the macroscopic 12D gauge groups "
     "alongside the microstate variables of crystallography, spin "
     "configurations, and valence orbital interactions", True),
    ("the tensor-core load figure",
     "keeps Tensor Core load in the efficient 15-20% range when simulating "
     "environments with millions of nodes", True),
    ("the node footprint",
     "the memory footprint of a single node reaches tens of kilobytes", True),
    ("the correction-loop clause",
     "without requiring floating-point correction loops", True),
    ("all five reference glosses", "", False),
    ("the keywords 'octonions' and 'dimensional reduction'", "", False),
]
V11_ADDED = [
    "Sec. 2, extensional vs intensional computing, imported from the MPPT "
    "papers",
    "Sec. 6.1, the BLDC motor case study measured in bldc.py",
    "fractal-like winding patterns that minimize skin effect",
]
V10_ORCID_PLACEHOLDER = "[ORCID: enter-your-orcid]"      # [P] v1.0 header
V11_ORCID_PLACEHOLDER = "[ORCID: Zadejte-svuj-ORCID]"    # [P] v1.1 header,
                                                         #     still unfilled,
                                                         #     now in Czech

# ---------------------------------------------------------------------------
# [V] Verified external values
# ---------------------------------------------------------------------------
# The card the author's own preprints specify, from the NVIDIA catalogue.
GPU_NAME   = "RTX 3090"       # [V]
BANDWIDTH  = 936e9            # [V] bytes/s, catalogue read bandwidth
TENSOR_TFLOPS = 142e12        # [V] FLOP/s, fp16 tensor-core peak
CLOCK      = 1.70e9           # [V] Hz, boost
VRAM       = 24 * 2**30       # [V] bytes
FP16_BYTES = 2                # [V]

# Tensor-core MMA granularity.  "CUDA 9 allows us to program a basic
# matrix-multiply-and-accumulate on 16x16 matrices" -- Markidis, S. et al.,
# "NVIDIA tensor core programmability, performance & precision", IPDPSW 522-531
# (2018), DOI 10.1109/IPDPSW.2018.00091, which is reference [3] of both
# preprints.
WMMA_TILE = 16                # [V]

# From the same reference, the warnings its gloss omits.
MARKIDIS_PEAK_TFLOPS = 83e12  # [V] "maximum performance of 83 Tflops/s"
MARKIDIS_ERROR_SCALING = "the error scales quadratically with N"   # [V]
MARKIDIS_HALF_PRECISION_GAP = 32   # [V] "only an accuracy of +/-32 between
                                   #     32,768 and 65,536"
MARKIDIS_REALTIME_COUNT = 0   # [V] occurrences of "real-time" in that paper

# NeRF, reference [4] of both preprints, on what volumetric ray marching costs.
# Mildenhall, B. et al., ECCV (2020), arXiv:2003.08934.
NERF_QUERIES_PER_IMAGE = (150e6, 200e6)   # [V] "between 150 and 200 million
                                          #     network queries per rendered
                                          #     image"
NERF_SECONDS_PER_FRAME = 30.0             # [V] "approximately 30 seconds per
                                          #     frame" on a V100

# "Symplectic" appears in exactly one work cited by either preprint, and not in
# connection with an update step: Baez, "The Octonions", Bull. AMS 39(2), on the
# 56-dimensional Freudenthal space for E7.
SYMPLECTIC_IN_REFERENCES = 1   # [V]

# ---------------------------------------------------------------------------
# [A] Assumed ranges, swept rather than asserted
# ---------------------------------------------------------------------------
SCREEN = (1920, 1080)          # [A] a 1080p target
FRAME_RATE = 60.0              # [A] Hz
MARCH_STEPS = (32, 64, 128, 256)   # [A] samples per pixel for volumetric
                                   #     ray marching
GRID_EMPTY_FRACTION = (0.5, 0.7, 0.9, 0.99)   # [A] for the sparsity comparison
SWEEPS_PER_SOLVE = (14, 140)   # [A] the range the v1.1 claim implies; see
                               #     bldc.py, which derives rather than assumes
                               #     it

# ---------------------------------------------------------------------------
# Derived, no new information
# ---------------------------------------------------------------------------
PIXELS = SCREEN[0] * SCREEN[1]


def node_bytes(dim):
    return dim * dim * FP16_BYTES


def mma_flops(dim):
    """One matrix-matrix product of a dim x dim node against a rule matrix."""
    return 2 * dim ** 3


def tag_report():
    """Counted from this file rather than written down."""
    import re
    import pathlib
    src = pathlib.Path(__file__).read_text()
    tagged = re.findall(r"^[A-Z_0-9]+\s*=.*?#\s*(\[[PVA]\])", src, re.M)
    return {
        "[P] from the preprints":              tagged.count("[P]"),
        "[V] verified against a named source": tagged.count("[V]"),
        "[A] assumed range, swept":            tagged.count("[A]"),
    }
