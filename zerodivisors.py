#!/usr/bin/env python3
"""The central mechanism of the preprint, built and measured.

  "When transitioning to 16D sedenion mathematics and beyond, algebra loses
   traditional rules, and so-called zero divisors emerge. ... in the 224D node
   of the openOmega engine, there exist non-zero matrices A (positron) and B
   (electron) for which the following holds:  A x B = 0
   ... The Tensor Core simply multiplies both matrices. The result is a zero in
   the matter register and the release of an absolute tensor vector into the
   energy register. The engine executes pure, mathematically perfect E=mc^2
   annihilation natively in a single processor clock cycle."   -- Sec. 3

Four things are measured.  The algebra claim, which is correct and is built here
from scratch rather than cited.  Whether sedenions are needed for the property
the engine wants, which they are not.  Whether the product can carry the energy
away, which it cannot.  And what the architecture would have to give up to use
the algebra it names.
"""
import numpy as np

from constants import (CD_NORM_MULT_UP_TO, MATMUL_IS_ASSOCIATIVE, MORENO_IS_APT,
                       RNG_SEED, SEDENION_DIM, ZD_TOLERANCE, ZD_TRIALS,
                       cayley_dickson_dims, tag_report)

P = print


# ---------------------------------------------------------------------------
# Cayley-Dickson doubling, built from the reals.  Elements are real vectors of
# length 2^k; a pair (a, b) represents a + b*l for the new imaginary unit l.
#
#   (a, b)(c, d) = (ac - d b*,  a* d + c b)
#   (a, b)*      = (a*, -b)
#
# with conjugation on the reals being the identity.
# ---------------------------------------------------------------------------
def conj(x):
    if len(x) == 1:
        return x.copy()
    h = len(x) // 2
    return np.concatenate([conj(x[:h]), -x[h:]])


def mul(x, y):
    if len(x) == 1:
        return x * y
    h = len(x) // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(d, conj(b)),
                           mul(conj(a), d) + mul(c, b)])


def basis(dim, i):
    e = np.zeros(dim)
    e[i] = 1.0
    return e


P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. The Cayley-Dickson tower, built here and checked")
P()
P(f"      dimensions in the tower: {cayley_dickson_dims(256)}")
P()
rng = np.random.default_rng(RNG_SEED)
P(f"      {'dim':>5s} {'commutative':>13s} {'associative':>13s} "
  f"{'alternative':>13s} {'|xy| = |x||y|':>15s}")
for dim in cayley_dickson_dims(SEDENION_DIM):
    xs = [rng.standard_normal(dim) for _ in range(3)]
    x, y, z = xs
    comm = np.abs(mul(x, y) - mul(y, x)).max()
    assoc = np.abs(mul(mul(x, y), z) - mul(x, mul(y, z))).max()
    # alternativity: the associator vanishes whenever two arguments coincide
    alt = max(np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max(),
              np.abs(mul(mul(y, x), x) - mul(y, mul(x, x))).max())
    norm = abs(np.linalg.norm(mul(x, y)) -
               np.linalg.norm(x) * np.linalg.norm(y))
    rel = norm / (np.linalg.norm(x) * np.linalg.norm(y))
    P(f"      {dim:>5d} {str(comm < 1e-9):>13s} {str(assoc < 1e-9):>13s} "
      f"{str(alt < 1e-9):>13s} {rel:>14.2e}")
P()
P(f"      Norm multiplicativity holds up to dimension {CD_NORM_MULT_UP_TO} and")
P("      fails at 16, which is exactly why zero divisors become possible there.")
P("      That is Moreno's result, and the preprint's reference [3] is the right")
P(f"      source for it: apt = {MORENO_IS_APT}.")

P()
P("2. A real sedenion zero divisor, found by search")
P()
P("      Searching pairs e_i +/- e_j for a product of zero:")
found = []
for i in range(1, SEDENION_DIM):
    for j in range(i + 1, SEDENION_DIM):
        a = basis(SEDENION_DIM, i) + basis(SEDENION_DIM, j)
        for k in range(1, SEDENION_DIM):
            for m in range(k + 1, SEDENION_DIM):
                for s in (+1.0, -1.0):
                    b = basis(SEDENION_DIM, k) + s * basis(SEDENION_DIM, m)
                    if np.abs(mul(a, b)).max() < ZD_TOLERANCE:
                        found.append((i, j, k, m, s))
P(f"      pairs found: {len(found)}")
if found:
    i, j, k, m, s = found[0]
    sign = "+" if s > 0 else "-"
    a = basis(SEDENION_DIM, i) + basis(SEDENION_DIM, j)
    b = basis(SEDENION_DIM, k) + s * basis(SEDENION_DIM, m)
    P(f"      example:  (e{i} + e{j}) x (e{k} {sign} e{m}) = 0")
    P(f"        |a| = {np.linalg.norm(a):.4f},  |b| = {np.linalg.norm(b):.4f},"
      f"  |a x b| = {np.linalg.norm(mul(a, b)):.2e}")
P()
P("      So the algebra claim of Sec. 3 is CORRECT.  Sedenions do have zero")
P("      divisors, they are constructible, and the paper's citation for them is")
P("      the right one.  This is the strongest part of the deposit and it is")
P("      confirmed here from first principles rather than taken on trust.")

P()
P("3. But the engine does not need sedenions for this")
P()
P("      The preprint's own equation is about MATRICES: \"there exist non-zero")
P("      matrices A (positron) and B (electron)\".  Zero divisors are ordinary")
P("      in any matrix algebra over a field.  The smallest example:")
A2 = np.array([[1.0, 0.0], [0.0, 0.0]])
B2 = np.array([[0.0, 0.0], [0.0, 1.0]])
P(f"        A = {A2.tolist()}   non-zero: {bool(A2.any())}")
P(f"        B = {B2.tolist()}   non-zero: {bool(B2.any())}")
P(f"        A @ B = {(A2 @ B2).tolist()}   zero: {not (A2 @ B2).any()}")
P()
n = 224
hits = 0
for _ in range(ZD_TRIALS):
    k = int(rng.integers(1, n))
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    # ker(A) contains span(Q[:, k:]);  im(B) lies inside span(Q[:, k:])
    A = rng.standard_normal((n, k)) @ Q[:, :k].T
    B = Q[:, k:] @ rng.standard_normal((n - k, n))
    if np.abs(A @ B).max() < ZD_TOLERANCE and A.any() and B.any():
        hits += 1
P(f"      non-zero {n}x{n} real pairs with A @ B = 0, out of {ZD_TRIALS} "
  f"trials: {hits}")
P()
P("      Any two singular matrices whose image and kernel line up multiply to")
P("      zero.  No exotic algebra is involved, and the property is available")
P("      at every dimension, not only at 224.  So the mechanism Sec. 3 reaches")
P("      for sedenions to obtain is one the hardware already has for free.")

P()
P("4. The product cannot carry the energy away")
P()
Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
A = rng.standard_normal((n, 5)) @ Q[:, :5].T
B = Q[:, 5:] @ rng.standard_normal((n - 5, n))
P(f"      ||A||_F     = {np.linalg.norm(A):>12.4f}")
P(f"      ||B||_F     = {np.linalg.norm(B):>12.4f}")
P(f"      ||A @ B||_F = {np.linalg.norm(A @ B):>12.4e}")
P()
P("      The product retains nothing of either operand's magnitude -- that is")
P("      what being zero means.  So \"the release of an absolute tensor vector")
P("      into the energy register\" cannot come from the product: there is no")
P("      quantity left in it to release.")
P()
P("      To emit E = mc^2 the engine has to read ||A|| and ||B|| BEFORE the")
P("      multiply, keep them somewhere, and then notice that the matter")
P("      register went to zero in order to know to add them to the energy")
P("      register.  Noticing that is a comparison against zero, i.e. exactly")
P("      the \"if (collision)\" that Sec. 3 says is not needed.  The branch is")
P("      not removed; it is moved from before the multiply to after it.")
P()
P("      And conservation runs the other way too: a zero product is reached by")
P("      any aligned singular pair, so an engine that emits energy whenever a")
P("      register hits zero emits it for every such pair, whether or not the")
P("      two operands were a particle and its antiparticle.")

P()
P("5. The choice the architecture does not make")
P()
P(f"      matrix multiplication is associative: {MATMUL_IS_ASSOCIATIVE}")
P("      sedenion multiplication is not (measured in Sec. 1 above)")
P()
P("      The architecture needs WMMA, which is matrix multiplication, and")
P("      matrix multiplication is associative over any ring.  The mechanism")
P("      needs the sedenions, which are not.  Both cannot hold at once, and")
P("      the preprint asserts them in consecutive sections: Sec. 3 says the")
P("      zero divisors come from sedenion mathematics, Sec. 4 says the node is")
P("      an array of 14 x 14 WMMA blocks.")
P()
P("      This is the same structural point openql-eval measured for the")
P("      octonions, where the span of the associators left 1 of 8 dimensions")
P("      surviving any matrix form.  The sedenions are a strictly larger")
P("      problem: they are not even alternative, as Sec. 1 shows.")
