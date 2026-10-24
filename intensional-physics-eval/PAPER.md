# Half a claim: an evaluation of *Intensional Physics Computing* and openQL v1.1

karagos01, October 2026

## Abstract

Two deposits of 8 October 2026 are evaluated together because neither stands
alone: M. Mazgal, *Intensional Physics Computing: Generating Virtual Reality via
Multidimensional Tensor Core Queries* (DOI
[10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777)) restates
sections of openQL as a standalone paper, and *openQL / openOL … (Version 1.1)*
(DOI [10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148)) revises
the 3 October original.

**Half of the central new claim is correct, which is worth leading with.** IPC
§5 claims "millions of physical queries per millisecond" — 10⁹/s. For the 4×4
node §3 assigns to the 12D layer, the binding ceiling on the card the author's
own preprints specify is **1.46·10¹⁰ queries/s**, so the claim fits with 14.6×
of headroom. For the 112×112 node of the same sentence the ceiling is
**1.87·10⁷/s**, so it is off by **54×**. §5 makes the claim for both at once.

**But the rate is insufficient for the application it is quoted for.** §4 makes
ray marching the mechanism by which the scene exists at all, so the budget is
queries per pixel per frame: 10⁹/s buys **8.0 march steps per pixel** at 1080p60.
Volumetric ray marching normally wants 64–256, so the claimed rate is **4 to 32
times short** — before any step does physics. The paper's own rendering
reference, NeRF, needed 150–200 million queries per image at **30 seconds per
frame**; its query count agrees with this calculation, which is a point in the
architecture's favour, and its frame time is the opposite of "absolute
real-time".

**IPC also strengthens a claim that was already refuted.** §3 calls
σ(W_PINN ⊗ S(t) + b) "a symplectic discrete Hamiltonian operator", where openQL
v1.0 said only that it "preserves the Lie group symmetries". The expression is
unchanged. It was measured in `openql-eval/symplectic.py`: with σ = tanh a
harmonic oscillator drifts to 2·10⁻⁵ × E(0) over 10⁵ steps and a fitted pendulum
reaches 10.2 × E(0), while leapfrog holds 1.0000 × E(0) untrained. "Symplectic"
occurs in exactly one work cited by either preprint, and about the Freudenthal
space for E₇ rather than a time step.

**openQL v1.1 removes four claims this evaluation measured.** The derivation of
112, "Tensor Core load in the efficient 15-20% range", "the memory footprint of
a single node reaches tens of kilobytes" and "without requiring floating-point
correction loops" are all gone, along with all five reference glosses and the
keyword "octonions" — though the abstract still says the architecture works "By
transforming quaternion and octonion algebra into unified block matrices", which
is the half excluded by a theorem. The coincidence is recorded; no causal claim
is made, because the revision carries no changelog.

**Its one substantively new section is §6.1**, a BLDC motor case study claiming
"millions of organically mutated topologies per day" on a million-node grid.
That leaves **14 to 140 update sweeps** per candidate — roughly one multigrid
linear solve — for an objective that must cover the magnetostatic field, torque
ripple over an electrical cycle, position-dependent cogging, iron loss needing
B–H history, and a coupled thermal steady state. And the zero-branching
argument it rests on is correct but inverted: branchlessness means there is no
saving on empty space, which is a **2× to 100× penalty** against a sparse solver
on a mostly-air motor grid, not an advantage.

## 1. What is correct

**The 4×4 query rate is achievable**, with 14.6× of headroom on bandwidth. This
is the first numeric hardware claim in this series that the arithmetic supports
rather than contradicts, and it deserves to be said without qualification.

**NeRF's query count is the right order.** §4's model — a ray interrogating each
node it passes — implies roughly 10⁸ queries per image at useful sampling, and
NeRF measured 150–200 million. So the architecture's estimate of how much work a
volumetric frame takes is correct. What it gets wrong is the rate at which that
work can be done.

**Zero-branching is a real property of MMA pipelines.** "Computing empty space
takes the exact same nanosecond fraction as computing a highly complex,
asymmetric copper coil" is true. §4 below disputes what it buys, not whether it
holds.

**The intensional/extensional distinction is a real one in logic**, and the
analogy to storing rules rather than enumerated state is legitimate as framing.
Signed distance fields and procedural generation occupy that space already,
which is a precedent the paper could have claimed.

**112 = 7 × 16 exactly**, so a 112×112 node tiles the tensor-core 16×16
granularity at 100 % occupancy. That is a coincidence rather than a design
choice, since the paper derives 112 elsewhere and not from the hardware, but it
is true.

## 2. The query rate, both ways

IPC §5: "the hardware stops rendering hollow shells and begins acting as a
particle micro-accelerator, evaluating millions of physical queries per
millisecond". Taking "millions per millisecond" at its floor, that is 10⁹
queries per second. §3 defines two node sizes: 4×4 for "12D macroscopic
physics" and 112×112 for "quantum-level physics".

| node | per MMA | compute ceiling | bandwidth ceiling | binding | vs the claim |
|---|---|---|---|---|---|
| 4×4 | 32 B, 128 FLOP | 1.11·10¹² /s | 1.46·10¹⁰ /s | bandwidth | **14.62× — fits** |
| 112×112 | 25 088 B, 2.81·10⁶ FLOP | 5.05·10⁷ /s | 1.87·10⁷ /s | bandwidth | **0.02× — exceeds** |

Both are bandwidth-bound, which is the same conclusion `openql-eval/roofline.py`
reached for this architecture by a different route. The small node fits
comfortably; the large one is off by 54×. The sentence asserts the rate for the
architecture as a whole, so half of it is right.

One caveat in the paper's favour and one against. Against: a 4×4 node occupies
one sixteenth of a 16×16 tile, so the compute ceiling above is optimistic unless
many nodes are packed per tile — possible, but a different algorithm from the
one-node-one-MMA model §3 describes. In favour: for 112 the tiling is exact.

## 3. The rate is insufficient for its own application

§4 is explicit that querying is how the scene is observed: "When a virtual
camera casts a photon (a ray) into the tensor grid, the photon travels through
the matrices and interrogates them. At each step, the ray asks the local node".
So each march step is a query, and the budget that matters is per pixel per
frame.

| march steps/pixel | queries/s needed | vs the claim |
|---|---|---|
| 32 | 3.98·10⁹ | 3.98× |
| 64 | 7.96·10⁹ | 7.96× |
| 128 | 1.59·10¹⁰ | 15.93× |
| 256 | 3.19·10¹⁰ | 31.85× |

The claimed rate buys **8.0 march steps per pixel** at 1080p60. Volumetric ray
marching through a participating medium normally wants 64–256 samples along each
ray, and with 8 the result is severe banding on any gradient. And that is before
a step does any physics, reads the ray state, or writes a result — the ceiling
computed in §2 assumes nothing is touched but the node itself.

So the rate is simultaneously achievable in the abstract and four to thirty-two
times short of the purpose it is quoted for. The honest reading is that the
number is not wrong, it is answering a different question from the one §4 poses.

NeRF makes the same point from the other side: 150–200 million network queries
per image, 30 seconds per frame on a V100, 1–2 days to train. Cited in both
preprints as the "theoretical predecessor" for real-time volumetric synthesis,
it ran at 0.03 frames per second.

## 4. openQL v1.1 §6.1, the only new section

§6.1 claims that a genetic algorithm over the 12D engine "circumvents"
combinatorial explosion and can "simulate millions of organically mutated
topologies per day" on a million-node grid.

A 12×12 fp16 node is 288 B, so the grid's state is 274.7 MiB and one update
sweep moves 549.3 MiB — 0.615 ms at 936 GB/s, bandwidth-bound. That gives:

| topologies/day | time each | sweeps affordable |
|---|---|---|
| 1 000 000 | 86.400 ms | 140.4 |
| 5 000 000 | 17.280 ms | 28.1 |
| 10 000 000 | 8.640 ms | 14.0 |

So 14 to 140 sweeps of the whole grid per candidate design. A multigrid Poisson
solve on 100³ is in that range for **one** linear solve. The objective §6.1
describes is not one linear solve; to rank motor topologies it must evaluate at
minimum the magnetostatic field of the winding, the torque and its ripple over a
full electrical cycle, cogging torque as a function of rotor position, iron loss
requiring the B–H history at every node, and a thermal steady state that takes
the loss field as input. Several are coupled and the position-dependent ones
need the field recomputed at many rotor angles. The whole of that has one
solve's worth of sweeps.

**And the zero-branching argument is inverted.** It is true that an MMA pipeline
costs the same for air as for copper. But that is the statement that there is no
saving on empty space, and a conventional solver's main economy on a motor grid
is exactly that most of the volume is air:

| grid empty | sparse solver does | dense does | penalty |
|---|---|---|---|
| 50 % | 50 % | 100 % | 2.0× |
| 90 % | 10 % | 100 % | 10.0× |
| 99 % | 1 % | 100 % | 100.0× |

Branchlessness is the price of the architecture, not its advantage, and §6.1
presents the absence of a saving as the thing that circumvents the limit.

A third point: the explosion §6.1 names is in the search space of topologies,
not in the cost of one evaluation. A genetic algorithm addresses that by
evaluating few candidates well, so what it needs is a cheap accurate objective —
which is what the sweep budget above constrains. Making each evaluation
branchless does not reduce the number of candidates, and the number of
candidates is the quantity called insurmountable. The section states the inputs
as a spatial volume and a 48 V limit, with no parameterisation of the winding,
so the dimension of that space is not given and cannot be checked.

§6.1's one new physical claim is "fractal-like winding patterns that minimize
skin effect". Skin effect is current crowding toward a conductor's surface, and
the established remedy is to subdivide the conductor into strands thinner than
the skin depth and transpose them — Litz wire. A fractal boundary increases
perimeter at fixed cross-section, which puts more of the copper in the
high-current-density region. Fractal geometries have real uses in RF antennas,
where a long electrical path in a small volume is the goal; that is a different
objective, and §6.1 gives no mechanism linking them. This is recorded as
unsupported rather than measured, because the section specifies no winding
geometry to compute against.

## 5. The version diff, and what it does and does not show

Six things are removed in v1.1, and four of them are claims `openql-eval`
measured:

- the derivation of 112 — "derived from the necessary degrees of freedom to
  encapsulate the macroscopic 12D gauge groups alongside the microstate
  variables of crystallography, spin configurations, and valence orbital
  interactions" ← measured
- "keeps Tensor Core load in the efficient 15-20% range when simulating
  environments with millions of nodes" ← measured
- "the memory footprint of a single node reaches tens of kilobytes" ← measured
- "without requiring floating-point correction loops" ← measured
- all five reference glosses
- the keywords "octonions" and "dimensional reduction"

The coincidence is the whole of the evidence. The revision carries no changelog
and gives no reason for any edit, so no causal claim is made here and none
should be read in.

Two things are notably unchanged. The abstract still says the architecture works
"By transforming quaternion and octonion algebra into unified block matrices",
while "octonions" has been dropped from the keywords — and the octonion half of
that sentence is the one excluded by a theorem, measured in
`openql-eval/octonion.py`. And the ORCID placeholder in the PDF header is still
unfilled: v1.0 had `[ORCID: enter-your-orcid]`, v1.1 has `[ORCID:
Zadejte-svůj-ORCID]`. It was not filled in; it was regenerated in Czech. The
author's real ORCID has been in the Zenodo record metadata since 3 October, so
the identifier exists and only the PDF template is stale.

One inconsistency between the two deposits of the same day: openQL puts 12
dimensions in a 12×12 node built from three concatenated 4×4 quaternion blocks,
while IPC §3 describes the node for the same layer as "a 4×4 (for 12D
macroscopic physics)" matrix — 16 slots for 12 numbers, in a different
arrangement from the one openQL specifies.

## 6. What is not measured here

The intensional-computing framing of IPC §§1–2 and §4 is a philosophical
position about representation, not a quantitative claim, and nothing here
adjudicates it. Storing rules and generating state on demand is a real
technique with real precedents.

The claim that CPUs "fail at this task because they rely on branching logic" is
not measured either, though two things are worth noting about its form: CPUs
have SIMD and branchless code too, and a ray marcher is inherently branchy at
the point of ray termination — which is why §4's own design hands off between
CUDA cores and tensor cores, a handoff that is a branch.

The five references of IPC were read for content in
[`reference-audit`](https://github.com/karagos01/reference-audit); four are
shared with openQL and the fifth is Fitting's Stanford Encyclopedia entry on
intensional logic, in which "tensor", "GPU", "matrix" and "quantum" each occur
zero times, and whose §4.5 is titled "Algorithms Need Not Be Effective".

## 7. Limitations

No GPU was used. Hardware figures are the catalogue specifications of the
RTX 3090 the author's own preprints name, and the ceilings computed are
theoretical peaks — a real implementation reaches some fraction of them, which
makes the "exceeds the card" findings stronger and the "fits" finding weaker.
The 14.6× headroom on the 4×4 node is large enough to survive any plausible
efficiency factor.

Provenance is tagged in `constants.py`: `[P]` from the preprints, `[V]` verified
against a named source, `[A]` an assumed range swept rather than asserted. The
screen resolution, frame rate, march-step count and empty-grid fraction are all
`[A]`.

The march-step range of 64–256 is the softest assumption. Techniques exist to
cut it — empty-space skipping, adaptive sampling, importance sampling — but
empty-space skipping is precisely what §6.1's zero-branching design gives up, so
the architecture has fewer of those options than a conventional renderer, not
more.

The sweep count in §4 is derived from the claim rather than assumed, and the
comparison to a multigrid solve is an order-of-magnitude statement; the
conclusion is that one solve's budget must cover a multi-physics objective, and
that does not turn on the exact constant.

## 8. Data and code availability

`constants.py` holds every value with its provenance tag and source, and no
other script defines one. `queries.py` reproduces §§2–3 and the symplectic note,
`bldc.py` §4, and `versions.py` §5; `versions.py` is a record rather than a
computation, kept as a script so it appears in `results.log`. `run_all.sh` runs
everything offline in about a second.

The openQL v1.0 measurements referred to throughout are not reproduced here.
They live in [`openql-eval`](https://github.com/karagos01/openql-eval), and the
reference verdicts live in
[`reference-audit`](https://github.com/karagos01/reference-audit).

## References

The evaluated preprints: M. Mazgal, *Intensional Physics Computing*, Zenodo,
8 October 2026, DOI 10.5281/zenodo.23241777; and *openQL / openOL: Tensor Matrix
Architecture for Unified Simulation of Physical Fields in 12D and 112D via GPU
Tensor Cores (Version 1.1)*, Zenodo, 8 October 2026, DOI
10.5281/zenodo.23241148. Both CC BY 4.0.

External sources are cited in `constants.py` beside the values they support: the
NVIDIA RTX 3090 catalogue specifications; Markidis, S. et al., IPDPSW 522–531
(2018), DOI 10.1109/IPDPSW.2018.00091, for the WMMA tile granularity and the
precision warnings; and Mildenhall, B. et al., ECCV (2020), arXiv:2003.08934,
for NeRF's query count and frame time. Quotations are short excerpts used for
criticism and review.
