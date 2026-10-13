# The right algebra for a property it does not need: an evaluation of *openOmega*

karagos01, October 2026

## Abstract

M. Mazgal, *openOmega: Tensor Matrix Architecture for Matter-Antimatter Symmetry
in ±12D, ±112D, and ±224D Spaces* (Zenodo, 9 October 2026, DOI
[10.5281/zenodo.23263528](https://doi.org/10.5281/zenodo.23263528)) extends the
openQL/openOL engine to antimatter. The Cayley-Dickson construction and the
sedenions are invoked to double the phase space to 224D and to add a "negative
mirror" half-plane holding the Dirac sea; the zero divisors of that algebra are
then to perform matter-antimatter annihilation natively — "The Tensor Core
simply multiplies both matrices. The result is a zero in the matter register and
the release of an absolute tensor vector into the energy register… natively in a
single processor clock cycle." The abstract calls it "a unified framework for a
Theory of Everything in computational physics".

**The algebra is right, and this repository confirms it from first principles
rather than taking it on trust.** The Cayley-Dickson tower is built here from
the reals; the construction reproduces the textbook classification exactly —
ℍ associative, 𝕆 non-associative but alternative, the sedenions neither — and
norm multiplicativity holds exactly up to dimension 8 and fails at 16, which is
precisely why zero divisors appear there. A sedenion zero divisor is then found
by search: **(e₁ + e₁₀) × (e₄ − e₁₅) = 0**, exactly. Moreno (1998), reference [3],
is the correct source for this and is correctly attached — alongside Furey in
SOTP, the best-chosen citation in the author's seventeen deposits.

**But the engine does not need the sedenions for the property it wants.** §3's
own equation is about *matrices*: "there exist non-zero matrices A (positron) and
B (electron)". Zero divisors are ordinary in every matrix algebra over a field —
[[1,0],[0,0]]·[[0,0],[0,1]] = 0 is the smallest case, and **200 of 200**
randomly constructed non-zero 224×224 real pairs multiply to zero here. The
property is free at every dimension, and the hardware is already in a matrix
algebra.

**The product cannot carry the energy away.** Measured: ‖A‖ = 34.1, ‖B‖ = 221.9,
‖A·B‖ = **4.1·10⁻¹³**. A zero product retains nothing of either operand, so
there is no quantity in it to release. To emit E = mc² the engine must read both
magnitudes *before* the multiply and then notice the register hit zero — which is
a comparison against zero, i.e. the `if (collision)` §3 says is not needed. The
branch is moved, not removed.

**224 is not in the Cayley-Dickson tower.** The tower is the powers of two;
sedenions are **16**-dimensional. 224 = 2 × 112, and 112 is not in the tower
either — nor does the series still offer a derivation for it, since openQL v1.1
deleted the sentence that gave one. So "Sedenion architecture (which is the
mathematical foundation of the −224D space)" does not connect.

**§4's hardware claim is correct and inherited.** 224/16 = 14 exactly, so the
node tiles the WMMA granularity at 100 % occupancy. But 112/16 = 7 exactly too —
doubling a multiple of 16 stays one — and a 224D node is **196 MMA operations**,
not one. On the card the author's own preprints specify, one 224×224 product is
**269 cycles of the entire GPU**, eight times worse than the 112D case the same
claim was made for.

**And the roofline result survives the doubling.** The matrix form and the state
it encodes have identical arithmetic intensity at every layer — 6.0, 56.0 and
112.0 FLOP/byte for both — while the matrix costs **d times** the traffic.
Encoding d numbers as a d×d matrix buys no arithmetic intensity at any d, which
is the measured sense in which "100 % saturated" is true and not useful: the
tiles are full and the card is waiting on memory.

## 1. What is correct

This deposit has more that holds up than most in the series, and the order here
reflects that.

**The sedenions have zero divisors, and the paper's reason is the right one.**
`zerodivisors.py` builds the Cayley-Dickson tower from the reals with
(a,b)(c,d) = (ac − d b̄, ā d + c b) and measures, at each dimension, whether
multiplication is commutative, associative, alternative, and norm-multiplicative:

| dim | commutative | associative | alternative | ‖xy‖ − ‖x‖‖y‖, relative |
|---|---|---|---|---|
| 1 | yes | yes | yes | 0 |
| 2 | yes | yes | yes | 1.5·10⁻¹⁶ |
| 4 (ℍ) | no | **yes** | yes | 0 |
| 8 (𝕆) | no | no | **yes** | 1.4·10⁻¹⁶ |
| 16 (sedenions) | no | no | **no** | **1.1·10⁻²** |

That is the textbook classification reproduced exactly, and it is the check that
the construction here is correct rather than merely plausible. Norm
multiplicativity failing at 16 is exactly Moreno's reason for zero divisors
appearing there, and a search then finds 168 zero-divisor pairs among the simple
combinations e_i ± e_j, the first being **(e₁ + e₁₀) × (e₄ − e₁₅) = 0** with
‖a·b‖ = 0 exactly.

**Reference [3] is excellent.** Moreno, *The zero divisors of the
Cayley-Dickson algebras over the real numbers*, Bol. Soc. Mat. Mexicana (3)
4(1), 13–28 (1998), arXiv:q-alg/9710013, is about exactly this: the zero
divisors for dimension 16 and higher, and the failure of norm multiplicativity
that permits them. Correctly chosen and correctly attached. In the reference
audit of this author's corpus only Furey's thesis in SOTP matched that standard.

**Reference [1] is real and correctly cited.** Dirac, *A Theory of Electrons and
Protons*, Proc. R. Soc. Lond. A 126, 360–365 (1930). The hole theory is a
historically important model, though it was superseded by the antiparticle
formalism of quantum field theory — citing it as the current physical picture of
the vacuum is a dated reading rather than a false one.

**224/16 = 14 exactly.** §4's alignment claim is arithmetically correct, and so
is the 100 % occupancy that follows from it. §2 below disputes what it buys, not
whether it holds.

**Phase conjugation is real.** Optical phase conjugation does produce a wave
that retraces its path through an aberrating medium, and it is routinely
described as time-reversed. The −12D layer's framing of it is not invented, even
though "active gravity shielding" in the same bullet is.

## 2. The algebra is not needed for the mechanism

§3 states the mechanism in terms of matrices:

> "in the 224D node of the openOmega engine, there exist non-zero matrices A
> (positron) and B (electron) for which the following holds: A×B=0"

> "This 'anomaly' is physically perfect. If matter and antimatter collide in the
> virtual grid of the engine, the computational core requires no conditional
> script like 'if (collision) { delete_object }'."

Zero divisors are not an anomaly in a matrix algebra; they are generic. Any two
singular matrices whose image and kernel line up multiply to zero. The smallest
example is

    [[1,0],[0,0]] · [[0,0],[0,1]] = [[0,0],[0,0]]

and at the paper's own dimension, `zerodivisors.py` constructs **200 out of 200**
non-zero 224×224 real pairs with A·B = 0, by choosing a random subspace
decomposition and putting im(B) inside ker(A).

So the property §3 reaches into the sedenions to obtain is one that every matrix
algebra over a field has, at every dimension, for free. Nothing about 224, and
nothing about Cayley-Dickson doubling, is required to get a non-zero pair whose
product vanishes.

This matters beyond elegance, because it changes what the section is claiming.
If zero divisors were exotic and confined to high-dimensional hypercomplex
algebras, then reaching 224D would be the enabling step. Since they are not, the
enabling step is absent — the engine could have done this at 2×2.

## 3. The product cannot carry the energy

§3 continues:

> "The Tensor Core simply multiplies both matrices. The result is a zero in the
> matter register and the release of an absolute tensor vector into the energy
> register. The engine executes pure, mathematically perfect E=mc²
> annihilation natively in a single processor clock cycle."

Measured on an aligned pair at 224×224:

| | value |
|---|---|
| ‖A‖_F | 34.1038 |
| ‖B‖_F | 221.8755 |
| ‖A·B‖_F | **4.06·10⁻¹³** |

The product retains nothing of either operand's magnitude — that is what being
zero means. There is no "absolute tensor vector" left in the result to release
into an energy register, because the result is the zero matrix.

To emit E = mc² the engine must therefore: read ‖A‖ and ‖B‖ before the multiply,
hold them somewhere, perform the multiply, and then **test whether the matter
register became zero** in order to know to add the stored magnitudes to the
energy register. That test is a comparison against zero — which is exactly the
`if (collision)` the section says is unnecessary. The branch is not eliminated;
it is moved from before the multiply to after it, and the bookkeeping it was
supposed to replace is still required.

Conservation also fails in the other direction. A zero product arises from *any*
aligned singular pair, so an engine that emits energy whenever a register reaches
zero emits it for every such pair, whether or not the two operands represented a
particle and its antiparticle. Distinguishing the physical case from the
numerical coincidence requires knowing what the matrices mean, which is more
bookkeeping again.

## 4. Where 224 comes from, and where the paper says it comes from

The abstract and §2 attribute 224 to the Cayley-Dickson construction and to
"dimensional doubling". `dimensions.py` checks:

| | in the Cayley-Dickson tower? |
|---|---|
| tower | 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 |
| sedenions, dimension 16 | **yes** |
| 12 | no |
| 112 | no |
| 224 | **no** |
| 448 | no |

Cayley-Dickson doubling takes an algebra of dimension n to one of dimension 2n
starting from 1, which gives the powers of two and nothing else. Multiplying an
arbitrary number by two is a different operation that shares the word. 224 =
2 × 112, and 112 is not in the tower either — and `openql-eval` recorded that
openQL v1.1 deleted the one sentence in the series that derived 112, without
replacing it. So 224 is a doubling of a number for which the series currently
offers no derivation at all.

The sedenions, meanwhile, are 16-dimensional. "Sedenion architecture (which is
the mathematical foundation of the −224D space)" therefore has nothing to
attach to: the algebra is real, its zero divisors are real, and the dimension it
lives in is 16, not 224.

**"Negative dimensions" are a labelling, not a space.** Dimension is a
cardinality — the number of coordinates needed to specify a point — so there is
no vector space of dimension −224 over any field. What §2 describes, a mirror
copy of the state holding the antiparticle sector, is an ordinary construction,
and it is *more* dimensions:

| layer | positive | mirror | total state |
|---|---|---|---|
| ±12 | 12 | 12 | 24 |
| ±112 | 112 | 112 | 224 |
| ±224 | 224 | 224 | **448** |

The largest layer is a 448-dimensional state, which is what the hardware must
hold and move, and §5 below is computed on that figure. There is a mild irony
in the arithmetic: ±112 already totals 224.

**The dimensions the cited physics uses are different numbers.** §2 says "The
positive 224D contains complete string theory and supersymmetry". The critical
dimensions are 10 for superstring theory and 26 for the bosonic string, with
M-theory at 11, and they are fixed by anomaly cancellation rather than chosen.
224 is none of them, and the section offers no embedding or compactification
relating the two. Recorded as unsupported rather than refuted: there is no
construction here to check.

## 5. What it costs on the hardware it specifies

**"a single processor clock cycle".** The RTX 3090 the author's own preprints
name does 83 529 fp16 FLOP per cycle across the whole card.

| node | FLOP per product | cycles of the entire GPU |
|---|---|---|
| 12×12 | 3 456 | 0.04 |
| 112×112 | 2 809 856 | 33.6 |
| 224×224 | 22 478 848 | **269.1** |

So one annihilation is 269 cycles of the whole card, and eight times worse than
the 112D case openQL made the identical claim for — which is what cubing the
dimension does. A 224D node is also 196 WMMA instructions, each with a latency
of several cycles, before the operands are fetched.

**Footprint.** A 224×224 fp16 node is 98.0 KiB, and with its mirror 196.0 KiB.
Twenty-four gibibytes holds **128 397** node pairs, state only — a cube 50 nodes
on a side, with nothing left for rule matrices, ray state or an output image.
Against §5's tokamak application at one node per particle, a cubic millimetre of
plasma at 10²⁰ m⁻³ contains 10¹¹ particles, so the grid is short by a factor of
**778 834**, about six orders of magnitude, for one cubic millimetre.

**Step rate.** For a fixed million-node grid, ±224D needs 186.9 GiB of state and
373.8 GiB per sweep — it does not fit on the card at all, and neither does
±112D. The largest grid that does fit at ±224D sweeps at **18.2 Hz**; real time
is 60.

(A table over a card filled to capacity would have been degenerate here: filling
the card and sweeping it once is about two VRAM passes whatever the node size, so
every layer would return the same number by construction. The grid is held fixed
and the layer varied instead, which is what makes the cost of the doubling
visible. An earlier draft of this repository had the degenerate version.)

**The roofline, which the doubling does not move.**

| layer | state | matrix | overhead | W·s FLOP/byte | W·S FLOP/byte |
|---|---|---|---|---|---|
| ±12 | 24 B | 288 B | 12× | 6.0 | 6.0 |
| ±112 | 224 B | 25 088 B | 112× | 56.0 | 56.0 |
| ±224 | 448 B | 100 352 B | 224× | **112.0** | **112.0** |

The last two columns are equal at every layer. That is the result `openql-eval`
measured for 112, and it survives the doubling: the matrix form sits at exactly
the same point on the roofline as the state it encodes, while costing d times the
traffic and d times the arithmetic. Encoding d numbers as a d×d matrix buys no
arithmetic intensity at any d.

This is the measured sense in which §4's "100 % saturated quantum field
simulator" is true and not useful. The tiles are full — that is what 224/16 = 14
exactly buys — and the card is waiting on memory regardless.

**The cost of the step from openQL:** 4× the memory per node, 8× the arithmetic,
4× the tiles, before the mirror doubles the memory again. §4 presents it as
costless because the alignment is preserved; alignment is about waste inside a
tile, not about how many tiles there are.

## 6. The choice the architecture does not make

The architecture needs WMMA, which is matrix multiplication, and matrix
multiplication is associative over any ring. The mechanism needs the sedenions,
which §1 measures as neither associative nor even alternative. Both cannot hold
at once, and the preprint asserts them in consecutive sections: §3 derives the
zero divisors from sedenion mathematics, §4 describes the node as an array of
14 × 14 WMMA blocks.

This is the same structural point `openql-eval` measured for the octonions,
where the associators of the author's own multiplication table spanned the whole
imaginary part and left 1 of 8 dimensions surviving any matrix form. The
sedenions are a strictly larger version of the problem.

The reference audit found that the three mathematicians this author cites for
hypercomplex algebra — Furey, Dixon and Baez — all resolve this by passing to the
*associative* algebra of left-multiplication operators, and each says so
explicitly. That manoeuvre is available here too, and it is the thing that would
make the architecture coherent; it would also dissolve the mechanism, because an
associative operator algebra is a matrix algebra, where §2's point applies and
the sedenions are not doing any work.

## 7. What is not measured here

"A unified framework for a Theory of Everything in computational physics" is not
a quantitative claim and nothing here adjudicates it. Nor are the §5
applications: phase-conjugate radar "with zero reflection delay",
sonoluminescence "via vacuum field collapse in the −112D layer", or dark matter
simulated as "manifestations of tensor curvature that do not interact with the
positive spectrum but exert gravitational force". None is stated with a
quantity, so there is nothing to check.

Two observations about the series rather than the physics. This is the first
deposit to use the phrase "Theory of Everything". And the hypercomplex
vocabulary returns after a six-deposit gap: "octonion" appears once and
"sedenion" five times, while "causal" remains at zero, where it has been since
openQL v1.0 of 3 October.

## 8. Limitations

No GPU was used. Hardware figures are catalogue specifications and the ceilings
are theoretical peaks; a real implementation reaches some fraction of them, which
strengthens the cost findings and does not affect the ratios.

Provenance is tagged in `constants.py`: `[P]` from the preprint, `[V]` verified
against a named source, `[A]` an assumed value or a choice of presentation. The
grid size, the tokamak density, the random seed and the numerical zero tolerance
are `[A]`; the tokamak density carries nothing beyond the order of the
shortfall.

The Cayley-Dickson construction here uses one of several sign conventions for
the doubling product. A different convention permutes the basis and changes
which particular pairs are zero divisors, but not the dimension at which they
appear or the classification table in §1 — which is why that table is included:
it is the check that the convention implemented is a correct one. An earlier
draft used a wrong formula for the second component and the table caught it, by
making the quaternions non-associative.

The 224×224 zero-divisor construction is exact up to floating point; ‖A·B‖ of
order 10⁻¹³ against operand norms of order 10² is zero to about fifteen digits,
not analytically zero. The 2×2 example and the sedenion example are exact.

## 9. Data and code availability

`constants.py` holds every value with its provenance tag and source, and no
other script defines one. `dimensions.py` reproduces §4, `zerodivisors.py` §§1–3
and §6, `hardware.py` §5. `run_all.sh` runs everything offline in about twenty
seconds; `results.log` is the output of one run. The openQL measurements
referred to throughout are not reproduced here — they live in
[`openql-eval`](https://github.com/karagos01/openql-eval), and the reference
verdicts in
[`reference-audit`](https://github.com/karagos01/reference-audit).

## References

The evaluated preprint: M. Mazgal, *openOmega: Tensor Matrix Architecture for
Matter-Antimatter Symmetry in ±12D, ±112D, and ±224D Spaces*, Zenodo, 9 October
2026, DOI 10.5281/zenodo.23263528, CC BY 4.0.

External sources are cited in `constants.py` beside the values they support:
G. Moreno, *The zero divisors of the Cayley-Dickson algebras over the real
numbers*, Bol. Soc. Mat. Mexicana (3) 4(1), 13–28 (1998), arXiv:q-alg/9710013;
P. A. M. Dirac, *A Theory of Electrons and Protons*, Proc. R. Soc. Lond. A 126,
360–365 (1930); S. Markidis et al., IPDPSW 522–531 (2018), DOI
10.1109/IPDPSW.2018.00091, for the WMMA tile granularity; and the NVIDIA
RTX 3090 catalogue specifications. Quotations are short excerpts used for
criticism and review.
