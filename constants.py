#!/usr/bin/env python3
"""Every constant used in this repository, in one place, with its provenance.

No other script here defines a constant.

  [P]  a value taken from the preprint itself
  [V]  an external value verified against a named source, with the source given
  [A]  an ASSUMED range, swept rather than asserted
"""

# ---------------------------------------------------------------------------
# [P] The preprint's own parameters
#     M. Mazgal, "openOmega: Tensor Matrix Architecture for Matter-Antimatter
#     Symmetry in +/-12D, +/-112D, and +/-224D Spaces", Zenodo, 9 October 2026,
#     DOI 10.5281/zenodo.23263528
# ---------------------------------------------------------------------------
DIMS            = (12, 112, 224)   # [P] Sec. 2, the three layers
DOUBLED_FROM    = 112              # [P] Sec. 2 "An extreme matrix space created
                                   #     by dimensional doubling"
CLAIMS_SEDENION_BASIS = True       # [P] Sec. 4 "Sedenion architecture (which is
                                   #     the mathematical foundation of the
                                   #     -224D space)"
CLAIMS_CAYLEY_DICKSON = True       # [P] abstract "By introducing the
                                   #     Cayley-Dickson construction and the
                                   #     algebra of sedenions"
CLAIMS_ONE_CLOCK_CYCLE = True      # [P] Sec. 3 "natively in a single processor
                                   #     clock cycle"
CLAIMS_NO_BRANCH = True            # [P] Sec. 3 "requires no conditional script
                                   #     like 'if (collision) { delete_object }'"
CLAIMS_ENERGY_CONSERVED = True     # [P] abstract "annihilation with absolute
                                   #     energy conservation"
CLAIMS_224_OVER_16 = 14            # [P] Sec. 4 "The dimension 224 is a perfect
                                   #     multiple of 16 (224 / 16 = 14)"
CLAIMS_100_PCT_SATURATED = True    # [P] Sec. 4 "transforms into a 100%
                                   #     saturated quantum field simulator"
CLAIMS_STRING_THEORY = True        # [P] Sec. 2 "The positive 224D contains
                                   #     complete string theory and
                                   #     supersymmetry"
ORCID_PLACEHOLDER = "[ORCID: Zadejte-svuj-ORCID]"   # [P] header, still unfilled

# ---------------------------------------------------------------------------
# [V] Verified external values
# ---------------------------------------------------------------------------
# The Cayley-Dickson tower doubles at every step, so its dimensions are the
# powers of two.  Sedenions are the 16-dimensional member.  Zero divisors first
# appear there, and the reason is that norm multiplicativity fails:
#
#   G. Moreno, "The zero divisors of the Cayley-Dickson algebras over the real
#   numbers", Bol. Soc. Mat. Mexicana (3) 4(1), 13-28 (1998),
#   arXiv:q-alg/9710013 -- which is reference [3] of the preprint, and which
#   describes the zero divisors for dimension 16 and higher, norm
#   multiplicativity holding only up to dimension 8.
SEDENION_DIM        = 16    # [V]
CD_NORM_MULT_UP_TO  = 8     # [V] holds for R, C, H, O; fails from 16 up
MORENO_IS_APT       = True  # [V] the citation is correct and correctly attached

# Critical dimensions of string theory and M-theory.
STRING_CRITICAL_DIMS = (10, 26)   # [V] superstring 10, bosonic 26
M_THEORY_DIM         = 11         # [V]

# Dirac's hole theory.  P. A. M. Dirac, "A Theory of Electrons and Protons",
# Proc. R. Soc. Lond. A 126, 360-365 (1930) -- reference [1] of the preprint.
# Real, correctly cited, and superseded: the filled negative-energy sea was
# replaced by the antiparticle formalism of quantum field theory.
DIRAC_1930_IS_REAL   = True   # [V]
DIRAC_SEA_SUPERSEDED = True   # [V]

# The card the author's own preprints specify, from the NVIDIA catalogue.
GPU_NAME      = "RTX 3090"   # [V]
TENSOR_TFLOPS = 142e12       # [V] FLOP/s, fp16 tensor-core peak
CLOCK         = 1.70e9       # [V] Hz, boost
BANDWIDTH     = 936e9        # [V] bytes/s
VRAM          = 24 * 2**30   # [V] bytes
FP16_BYTES    = 2            # [V]

# Tensor-core MMA granularity.  "CUDA 9 allows us to program a basic
# matrix-multiply-and-accumulate on 16x16 matrices" -- Markidis, S. et al.,
# IPDPSW 522-531 (2018), DOI 10.1109/IPDPSW.2018.00091, reference [4] of the
# preprint.
WMMA_TILE = 16   # [V]

# Matrix multiplication is associative over any ring.  This is a theorem, not a
# measurement, and it is what forces the choice the preprint does not make:
# an MMA pipeline computes in an associative algebra.
MATMUL_IS_ASSOCIATIVE = True   # [V]

# ---------------------------------------------------------------------------
# [A] Assumed ranges, swept rather than asserted
# ---------------------------------------------------------------------------
ZD_TRIALS      = 200          # [A] random trials in the matrix zero-divisor test
ZD_TOLERANCE   = 1e-9         # [A] what counts as numerically zero
SEARCH_DEPTH   = 2            # [A] basis elements per operand in the sedenion
                              #     zero-divisor search
RNG_SEED       = 0            # [A] fixed so the run is reproducible
GRID_NODES     = 1_000_000    # [A] a fixed grid, so the step-rate table varies
                              #     with the layer instead of with the card
TOKAMAK_N_PER_M3 = 1e20       # [A] tokamak core number density, order of
                              #     magnitude only; carries no conclusion
                              #     beyond the order of the shortfall

# ---------------------------------------------------------------------------
# Derived, no new information
# ---------------------------------------------------------------------------
FLOP_PER_CYCLE = TENSOR_TFLOPS / CLOCK    # whole-GPU fp16 throughput


def cayley_dickson_dims(upto=512):
    d, out = 1, []
    while d <= upto:
        out.append(d)
        d *= 2
    return out


def node_bytes(dim):
    return dim * dim * FP16_BYTES


def matmul_flops(dim):
    return 2 * dim ** 3


def tag_report():
    """Counted from this file rather than written down."""
    import re
    import pathlib
    src = pathlib.Path(__file__).read_text()
    tagged = re.findall(r"^[A-Z_0-9]+\s*=.*?#\s*(\[[PVA]\])", src, re.M)
    return {
        "[P] from the preprint":               tagged.count("[P]"),
        "[V] verified against a named source": tagged.count("[V]"),
        "[A] assumed range or choice":         tagged.count("[A]"),
    }
