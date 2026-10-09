# The defence in the references: an audit of all 69 citations in sixteen preprints

karagos01, October 2026

## Abstract

The author of sixteen Zenodo preprints has stated publicly that the defence of
his arguments is deliberately placed in the references rather than written in
the text, and that an analysis confined to the text will therefore miss it.
That is a testable claim. This audit tests it by reading what each cited work
actually says about the claim it is cited for, across all 69 external
references in all sixteen records, and by looking for support rather than only
for error.

The claim is partly vindicated. In two deposits the cited literature carries
support the preprints never spell out, and in one case a derivation better than
the preprint's own: Furey's thesis argues that causality and irreversible time
emerge from the bracketing of an algebraic expression, which is the conceptual
core of the whole "Causal" series; and Baez supplies both a real-matrix
encoding of octonion multiplication and a route to the number 12 through
sl(3,ℍ) acting on ℝ¹², remarking of that 12 that "this is no coincidence!"

It does not extend further, for three measured reasons. First, 47 of the 69
references are attached to no claim at all and three deposits have no reference
list, so for two thirds of the corpus there is no carrier a defence could use.
Second, where support was found, the same pages refute the mechanism it is
offered for: Furey, Dixon and Baez all resolve non-associativity by passing to
the associative algebra of left-multiplication operators, which is precisely
the manoeuvre the proposed architecture is premised on not making, and Adler's
central result is that the quaternionic units drop out of the S-matrix. Third,
fourteen claims are contradicted by their own cited sources in those sources'
own words, including the two that carry most weight in the agricultural and
biomedical deposits.

## 1. What this tests, and what it does not

The occasion for this audit was a specific and fair methodological criticism:
that verifying a reference exists is weaker than reading what it says, and that
an argument can live in a bibliography. Both halves are correct, and the first
describes a real weakness in the five earlier repositories in this series,
which checked existence and attribution more thoroughly than content.

So the question here is narrow and answerable: for each citation, does the work
cited say what it is cited for? Three things follow from the narrowness.

This is not an audit of whether the claims are true. A claim can be right with
a bad citation. Where the arithmetic has been done it is in the companion
repositories, and the numbers that do not depend on any reading of the
references are unchanged by anything here.

Where a work could not be read, the audit says so rather than guessing.
`audit.py` section 3 reports that 38 of 59 verdict rows rest on a full text;
the rest rest on an abstract, a contents listing, or — for two unreachable
books — on the same author's own papers and their own published summary of the
book, with the substitution named in each row's `source` field.

Finally, keyword absence is reported as a count, not an impression. A zero in
`refdata.py` means the term was searched for in the obtained text and is not
there. Where the text came from an OCR index, the row says so, and absence is
strong rather than absolute evidence.

## 2. Is there a carrier?

For a reference to defend a claim, the text has to attach it to that claim.
Counting the attachments is the first measurement, and it decides how much of
the corpus is testable at all.

| | count | share |
|---|---|---|
| external reference entries, 16 records | 69 | |
| attached to a sentence by an in-text marker | **7** | 10.1 % |
| carrying only a parenthetical gloss | 15 | 21.7 % |
| **with no stated relation to any claim** | **47** | **68.1 %** |
| self-citations | 4 | |

Two deposits cite an external work in their body text: the Acoustic Projector,
which marks five of its six -- Putland is listed but never cited -- and SOTP,
which marks two of five with `[3, 4]` on one sentence. Three deposits — MPPT v1.0, MPPT v1.1 and CQFT — have no reference
list at all, so there is nothing for a defence to be hidden in. Three more
gloss every reference with a note saying what it establishes, which is the most
directly testable form the claim can take, since the author states the mapping
himself.

That leaves 22 references across five deposits where the link is stated. Those
are where a hidden defence could be found, and they are where it was.

## 3. What the search for support found

Three findings are substantial, and the first is the strongest result in this
repository.

**Furey (2016), chapter 2**, cited in SOTP as `[3]`, argues exactly what the
"Causal" trilogy needs and never states:

> "Taking multiplication to be the propagation along an edge, and addition to
> be the joining of two edges at a vertex, it can be seen that this unevaluated
> algebraic expression gives a causal set."

> "In the case of an algebra, an event is a calculation. … an event can be seen
> to be irreversible, it cannot 'unhappen'. … Time, then, is simply a sequence
> of calculations, and is clearly irreversible."

Her abstract: "we argue that physical concepts such as particles, causality,
and irreversible time may result from the algebra acting on itself." She also
does obtain su(3)_c and u(1)_em from the complex octonions and calls
non-associativity "not a impediment, but instead a gift". SOTP's in-text
citation is substantively grounded, though "isomorphism" is loose: Furey works
with minimal left ideals and stabiliser subgroups, not an isomorphism of 𝕆 with
the gauge group.

**Baez (2002)**, cited in openQL v1.0 as `[5]` under a gloss about "12D/112D
spatial mappings" that fails on its face — "112" and "12-dimensional" do not
occur in Baez at all — nonetheless contains two things the preprint needs.
Section 2.3 gives real matrices for octonion multiplication through
left-multiplication operators, from which Baez derives a Clifford
representation. And section 3.3 gives sl(m,𝕂) acting on 𝕂^m, so that sl(3,ℍ) on
ℍ³ ≅ ℝ¹² is a set of real 12×12 operators, with so(12) sitting at (ℍ,ℍ) in his
magic square and his own remark that "the numbers 9, 10, 12 and 16 are 8 more
than the dimensions of ℝ, ℂ, ℍ and 𝕆. As usual, this is no coincidence!" That
is a better derivation of 12 than either of the two openQL offers, and the
preprint never points at it.

A weaker candidate for 112 also exists and should be recorded: 2 × 56, through
the 56-dimensional Freudenthal space for E₇, which Baez does equip with a
symplectic structure. He never writes 112, and that symplectic form is a
bilinear form preserved by E₇₍₋₂₅₎ rather than a property of an update step, so
this is a lead rather than a result.

**Adler (1995)**, cited in PCTP as `[1]`, supports the premise. The failure of
the ordinary tensor product over ℍ is real and long-standing — Horwitz: "there
is an essential destruction of linearity, i.e., f q ⊗ g ≠ (f ⊗ g)q"; Baez and
Huerta: "the tensor product of quaternionic Hilbert spaces is not naturally a
quaternionic Hilbert space."

Three smaller findings are in the author's favour and recorded in `hidden.py`:
Bi et al. genuinely demonstrate the monolithic on-chip non-reciprocity PCTP
needs to enforce an ordering; Lehmann's abstract genuinely supports biochar
"as inoculant carriers", which is the smart-pellet concept; and Tesla's patent
genuinely teaches the distributed capacitance COBAR claims from it.

## 4. The manoeuvre all three share

The three mathematicians cited for octonions each solve non-associativity the
same way, and each says so plainly:

> Furey: "As the composition of maps is always associative, ℂ⊗𝕆⃖ is an
> associative algebra" … "faithfully represents the 64-complex-dimensional
> Clifford algebra Cl(6)"

> Dixon: "𝕆_L ≃ ℝ(8) ≃ CL(0,6) … **(Note: 𝕆_L is trivially associative.)**"

> Baez: "multiplication in this group is given by composition of real-linear
> operators, **which is associative even for 𝕂 = 𝕆**"

Passing to the associative algebra of left-multiplication operators is exactly
the step the proposed architecture is premised on refusing, since its selling
point is a non-zero associator executed as a hardware observable. Furey adds
the rider in her own voice: "It is at this early stage only a conjecture that
any **(associative)** algebraic expression gives a causal set."

Adler's rider is of the same shape and equally decisive: "the S-matrix is
always a complex matrix with no dependence on the quaternionic units j, k …
Hence the asymptotic dynamics for quaternionic quantum mechanics is always an
effective complex theory", and "noncommutative dynamics hides itself beneath
effective complex quantum mechanical structures." A processor whose output is
measured cannot exhibit, in its in/out behaviour, the non-commutativity it
exists to execute.

So the hidden defence is real for the motivation of these papers and refutes
their mechanism, out of the same pages. This repository's existing companion
`openql-eval` already measured the boundary — left-multiplication operators
give 1.8·10⁻¹⁵ for ℍ and 29.5 for 𝕆 — but did not credit Baez with supplying
the construction. That attribution is a correction this audit owes the earlier
repository, not the preprint.

## 5. Glosses the cited work contradicts

Where the author states what a reference establishes, the statement can be
checked directly. Five of the fifteen glosses are contradicted by the work they
describe, and in three the contradiction is in the cited abstract.

**Raissi et al.**, glossed as the "basis for encoding physical laws into neural
weights", says: "the resulting pair u(t,x;W,b) and f(t,x;W,b) must satisfy the
Burgers equation **regardless of the choice of the weights W and bias b**." The
physics is in the loss function and in automatic differentiation with respect
to the input coordinates. "Symplectic" does not occur in the paper.

**Hellman & Gitlin**, glossed for "human copper transport" and a "structural
relationship … to invertebrate hemocyanins", opens: "Ceruloplasmin is a serum
ferroxidase … **Despite the need for copper in ceruloplasmin function, this
protein plays no essential role in the transport or metabolism of this
metal.**" Twenty-eight of its 112 references concern iron and none concern
hemocyanin; its structural comparisons go to ascorbate oxidase, laccase, Fet3p
and hephaestin. Domain databases agree: ceruloplasmin is a multicopper oxidase
with a cupredoxin fold, hemocyanins carry a tyrosinase binuclear type-3 copper
centre, and the intersection is empty. This is the preprint's only concrete
molecular bridge between humans and hemocyanin.

**Tchounwou et al.**, glossed for "epigenetic adaptation", contains the string
"epigenet" zero times, and attributes to copper "the generation of superoxide
and **hydroxyl radicals**" — the same radical for which the preprint rejects
iron.

**Wright & Upadhyaya**, glossed for the "mechanics of glomalin production" and
"water retention", is a cross-sectional survey of 37 samples whose output is a
single regression; production is its premise, water appears only as the
destructive agent in wet sieving, and "permanent" does not occur. The citation
is also orphaned: the preprint mentions mycorrhiza only to bypass it — "The
plant root must not 'search' for distant deposits via fungi."

**Decker et al. (2007)** does not resolve as printed at all. It is a chimera:
the venue maps to van Holde, Miller & Decker (2001) in JBC, the author and year
to Decker et al. (2007) in *Integrative and Comparative Biology*. Neither
"efficiency" nor "thermodynamic stability" — the two words the gloss claims —
occurs in the work it maps to, which instead reports "a low to moderate oxygen
affinity".

## 6. Refutations in the sources' own words

Fourteen rows carry the verdict REFUTES, meaning the cited work states the
opposite of the claim. Six are worth setting out.

**Buchachenko, on magnetic isotopes.** The phytomining preprint claims ²⁵Mg and
⁶⁷Zn "accelerate the chemical kinetics of DNA transcription and ATP synthesis".
The cited author's result for exactly the trio of isotopes the preprint names:

> "The substitution of these catalyzing ions in polymerases by the ions ²⁵Mg²⁺,
> ⁴³Ca²⁺, and ⁶⁷Zn²⁺ with magnetic nuclei was shown to produce a huge isotope
> effects: nuclear magnetic ions **by 3–5 times suppress DNA synthesis**"

> "A new **anti-cancer strategy** is suggested based on the using of the nuclear
> magnetic ions of magnesium, calcium, and zinc as a powerful and universal
> means to **selectively kill** only cancer cells."

Repair is also slower, by 1.5×. Only the ATP claim survives, and only for ²⁵Mg
at 99.9 % enrichment delivered by an injectable nanoparticle — and it failed
replication in PNAS in 2012, which the preprint does not cite. The ⁶⁷Zn half of
the gloss is an anachronism: Buchachenko's biological zinc work is from 2013,
four years after the cited 2009 book.

**Reith et al., on gold.** The preprint has biogenic gold nanoparticles
"entirely blocking" reactive oxygen species. The source: "Au detoxification is
mediated by a combination of **efflux**, reduction, and possibly methylation",
and "one major toxic effect of Au(III) … is the **induction of oxidative
stress**", with a minimum inhibitory concentration of 2 µM. The cell exports
gold to survive it, and gold induces the very species the preprint has it
scavenging.

**NVIDIA, on 2-bit arithmetic.** The whitepaper: "FP8, FP16, BF16, TF32, FP64,
and INT8 MMA data types are supported." The complete `wgmma.mma_async` operand
list adds only `b1` with `.and`+`.popc`; `.s4`/`.u4` are absent and `.u2`/`.s2`
exist only as conversion types. There is no native 2-bit or ternary
tensor-core type on Hopper and none on any generation.

**Manchon et al., on dissipation.** SOTP claims pure spin currents eliminate
I²R entirely. The review: a pure spin current is induced "transverse to the
direction of **the applied electrical current**", at 10⁷–10⁸ A/cm² and about
100 fJ per bit. It also places Rashba and Dresselhaus fields in the same plane,
differing in rotation sense, so they are not the orthogonal spin axes the
preprint assigns them to.

**Demokritov, on magnon condensates.** The momentum drive needs a
room-temperature magnon BEC held for milliseconds whose phase shift displaces
the rotor lattice. From the same author's later work: "the magnon BEC is doubly
degenerate: two condensate components are simultaneously formed in the two
spectral minima at k_BEC = ±k_min", and "the group velocity at these spectral
points is zero. Therefore, **the created condensate clouds do not move**." Net
momentum is zero by symmetry, measured lifetimes are 175–230 ns against the
3 ms assumed, and no equilibrium magnon BEC can exist at all because the
chemical potential vanishes in equilibrium.

**Purushothaman & Landau, on pulsed charging.** The Na-ion preprint's only
pulsed-charging citation identifies solid-state diffusion as the limit, works
at a 3 s pulse with 1 s rest — about 0.25 Hz — and finds its best result with a
**continuous** decreasing-current profile rather than any pulse. It supports the
low-frequency envelope and contradicts the kHz-to-MHz component it is cited
beside.

## 7. What is correct

Three verdicts are SUPPORTS, and two further findings should be stated plainly
because they correct this audit rather than the preprints.

SOTP's seven Fano triples were machine-checked here and form a **valid Fano
plane**: all 21 pairs of the seven imaginary units are covered exactly once.
Its associator definition and its ε rule are Baez's verbatim. Jones et al. and
Kennedy & Eberhart resolve exactly and support what they are cited beside.

Tesla's patent does **not** presuppose an iron core — it is explicitly agnostic
("any conductor") — so it can be cited neither for nor against coreless
operation; the assumption to the contrary was this audit's, not the preprint's.
And the Griffiths citation is correct: Cambridge University Press did reissue
the fourth edition in 2017, ISBN 9781108420419, so the error hypothesised here
does not exist.

A third correction belongs to an earlier repository in this series rather than
to a preprint. Running the vocabulary census in `keywords.py` over all sixteen
records, instead of the ten available when `cymatic-eval` was written,
disproved a priority claim made there: "causal" first reaches zero in openQL
v1.0 of 3 October, and all seven tracked terms are absent from COBAR of
23 September and the Topological Momentum Drive of 24 September, both of which
make engineering claims. Six of the sixteen records carry none of the
vocabulary and ten carry it heavily, and the two groups alternate rather than
succeed one another, so there is no trend to read. The counts themselves were
right; the claim to priority built on them was an artefact of comparing against
part of the corpus. It is now corrected in `cymatic-eval` §1.

## 8. Limitations

Twenty-one of 59 verdict rows do not rest on a full text, and each says which
substitute was used. Two books were unreachable: Adler's, replaced by his own
published summary plus two primary reviews, and Dixon's, replaced by his own
arXiv lecture referring back to it. Beranek & Mellow's interior could not be
opened, so that verdict rests on a verified chapter list; the efficiency
relation attributed to it was read in a secondary source and is flagged as such
in `refdata.py`. Sheoran et al. and Wright & Upadhyaya are confirmed closed
access. Keyword searching for Griffiths was done on the third edition with the
fourth edition's structure verified from a catalogue record.

One reference, Putland (1993), could not be located; the AES e-library is
behind Cloudflare and not archived. The indirect evidence against it is strong
but it is negative evidence, which is weaker than showing a work does not
exist.

The cymatic deposit's five references were checked for existence in the
companion repository and only one for content, so that deposit is
under-audited relative to the rest.

Finally, a failure mode worth recording because it is the one being discussed.
While searching for the Sheoran text, a web-search summariser repeatedly
produced "findings from Sheoran" — named species, specific numbers — that are
not in that paper and were mixed in from other articles in the result set. They
were discarded and the row was marked as resting on the abstract. The same
discipline is why two references were dropped from an earlier repository in
this series rather than cited from memory.

## 9. Data and code availability

`refdata.py` holds every verdict with its verbatim evidence, its source, and
how far the cited work could be read. `carrier.py`, `audit.py` and `hidden.py`
tabulate it; `fetch.sh` reproduces the sixteen deposits from Zenodo and
`keywords.py` recomputes the citation-marker counts from them. `run_all.sh`
runs everything offline in about a second; `results.log` is the output of one
run.

## References

The sixteen audited deposits are listed with their DOIs in `README.md`. Every
work quoted in this write-up is cited in full in `refdata.py`, with a DOI or a
URL and a note on how it was obtained. Quotations are short excerpts used for
criticism and review.
