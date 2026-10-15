# The defence in the references: an audit of all 81 citations in eighteen preprints

karagos01, October 2026

## Abstract

The author of eighteen Zenodo preprints has stated publicly that the defence of
his arguments is deliberately placed in the references rather than written in
the text, and that an analysis confined to the text will therefore miss it.
That is a testable claim. This audit tests it by reading what each cited work
actually says about the claim it is cited for, across all 81 external
references in all eighteen records, and by looking for support rather than only
for error.

The claim is partly vindicated. In four deposits the cited literature carries
support the preprints never spell out, and in one case a derivation better than
the preprint's own: Furey's thesis argues that causality and irreversible time
emerge from the bracketing of an algebraic expression, which is the conceptual
core of the whole "Causal" series; Baez supplies both a real-matrix encoding of
octonion multiplication and a route to the number 12 through sl(3,ℍ) acting on
ℝ¹², remarking of that 12 that "this is no coincidence!"; Shockley and
Queisser's own footnote 22 names carrier multiplication and sets it aside,
which is the defence of HOS-PV 2.0's title; and Moreno prints the sedenion
zero-divisor pair openOmega's mechanism needs.

It does not extend further, for three measured reasons. First, 52 of the 81
references are attached to no claim at all and three deposits have no reference
list, so for two thirds of the corpus there is no carrier a defence could use.
Second, where support was found, the same pages refute the mechanism it is
offered for: Furey, Dixon and Baez all resolve non-associativity by passing to
the associative algebra of left-multiplication operators, which is precisely
the manoeuvre the proposed architecture is premised on not making, and Adler's
central result is that the quaternionic units drop out of the S-matrix. Third,
fourteen claims are contradicted by their own cited sources in those sources'
own words, including the two that carry most weight in the agricultural and
biomedical deposits and the efficiency figure in the title of the newest one.

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
`audit.py` section 3 reports that 43 of 69 verdict rows rest on a full text;
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
| external reference entries, 18 records | 81 | |
| attached to a sentence by an in-text marker | **14** | 17.3 % |
| carrying only a parenthetical gloss | 15 | 18.5 % |
| **with no stated relation to any claim** | **52** | **64.2 %** |
| self-citations | 4 | |

Three deposits cite an external work in their body text: the Acoustic
Projector, which marks five of its six -- Putland is listed but never cited --
SOTP, which marks two of five with `[3, 4]` on one sentence, and HOS-PV 2.0 of
14 October, which marks **all seven of its seven**, the first deposit in the
corpus to leave no reference unattached. Three deposits — MPPT v1.0, MPPT v1.1
and CQFT — have no reference
list at all, so there is nothing for a defence to be hidden in. Three more
gloss every reference with a note saying what it establishes, which is the most
directly testable form the claim can take, since the author states the mapping
himself.

That leaves 29 references across six deposits where the link is stated. Those
are where a hidden defence could be found, and they are where it was.

## 3. What the search for support found

Five findings are substantial, and the first is the strongest result in this
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

**Shockley & Queisser (1961)**, cited in HOS-PV 2.0 as `[1]`, defends that
deposit's title from a footnote. The claim the deposit is built on is that a
single junction can exceed 33.7 % because singlet fission puts two carriers in
the circuit for one photon. Footnote 22 of the paper that set the limit:

> "Once a photon exceeds about three times the energy gap [E_g], the
> probability of producing two or more hole-electron pairs becomes
> appreciable"

> "the data can be well fitted up to quantum yields greater than two … This
> effect would slightly increase the possible quantum efficiency; however, **we
> shall not consider it further in this article**."

The authors of the limit excluded multiplication by choice, so exceeding it
this way is legitimate, and the deposit is right about that without ever saying
where the permission comes from. The rider is the size of the gap, and it is in
the same deposit's reference [5]: a single junction with multiplication is
44.4 %, not the 45.9 % claimed, and 45.9 % sits inside that work's two-gap
tandem range.

**Moreno (1998)**, cited in openOmega as `[3]`, prints the mechanism that
deposit runs on. Its annihilation step needs two non-zero sedenions whose
product is exactly zero, and the introduction of the cited paper gives one:

> "for n ≥ 4 this norm-preserving formula is not true in general and this opens
> the possibility of the existence of zero divisors in A_n for n ≥ 4 i.e. x and
> y non-zero elements in A_n such that xy = 0 e.g. let **x = e₁ + e₁₀ and
> y = e₁₅ − e₄** in ℝ¹⁶ = A₄"

That is the pair the companion repository `openomega-eval` found by brute-force
search over the basis combinations — it reports (e₁ + e₁₀) × (e₄ − e₁₅) = 0,
the same pair with the sign of y flipped — printed in the reference all along. Two
riders come out of the same two pages. The zero divisors exist *because*
‖xy‖ = ‖x‖‖y‖ fails above dimension 8, so the norm is destroyed in the one
operation the deposit performs "with absolute energy conservation". And
Moreno's own item 2) removes the need for sedenions in the deposit's own matrix
formulation: "in an associative (alternative) context as in M_n(ℝ) … 0 ≠ A is a
zero divisor if and only if det A = 0."

Five smaller findings are in the author's favour and recorded in `hidden.py`:
Bi et al. genuinely demonstrate the monolithic on-chip non-reciprocity PCTP
needs to enforce an ordering; Lehmann's abstract genuinely supports biochar
"as inoculant carriers", which is the smart-pellet concept; Tesla's patent
genuinely teaches the distributed capacitance COBAR claims from it; Šmejkal,
Sinova and Jungwirth's Table III gives HOS-PV 2.0's altermagnetic collector
**more** spin splitting than the deposit asks for, 1.1–1.4 eV against a claimed
0.5–1.0 eV; and Rao et al. support the triplet drain the same deposit is built
to close, in the words of the sentences that precede the marker.

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

Fifteen rows carry the verdict REFUTES, meaning the cited work states the
opposite of the claim. Seven are worth setting out.

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

**Hanna & Nozik, on 45.9 %.** HOS-PV 2.0's abstract and its section 2.2 both
claim that the architecture raises the single-junction limit "from 33.7 % (SQ
limit) to 45.9 %", with this reference attached. The reference is the right
one — detailed balance under 1 sun AM1.5G, with singlet fission as a
multiplication absorber — and its abstract gives a different number for exactly
that configuration:

> "for single gap photovoltaic (PV) devices the maximum efficiency increases
> from 33.7 % for cells with no carrier multiplication to **44.4 %** for cells
> with carrier multiplication"

> "the maximum efficiency of an ideal two gap tandem PV device increases from
> **45.7 % to 47.7 %**"

45.9 % falls in the tandem range, and being a single junction is the
architecture's entire selling point. The companion repository `hospv-eval`
rebuilds the model from the ASTM G173-03 spectrum and reproduces all three of
that group's published values — 33.77 %, 44.62 %, and 42.09 % at 0.94 eV for
multiplication capped at two carriers per photon, which is what singlet fission
does, against their published 42.0 % at 0.95 eV. 45.9 % is above that ceiling
at any pair of energies.

## 7. What is correct

Four verdicts are SUPPORTS, and two further findings should be stated plainly
because they correct this audit rather than the preprints.

SOTP's seven Fano triples were machine-checked here and form a **valid Fano
plane**: all 21 pairs of the seven imaginary units are covered exactly once.
Its associator definition and its ε rule are Baez's verbatim. Jones et al. and
Kennedy & Eberhart resolve exactly and support what they are cited beside, and
Moreno is about exactly the zero divisors openOmega is built on.

HOS-PV 2.0 is the cleanest deposit in the corpus by every formal measure taken
here. All seven of its references are real, all seven resolve exactly as
printed, all seven are attached to a sentence, none is a self-citation, there
is no AI co-author and no unfilled ORCID placeholder — the first deposit of the
eighteen with all of those at once. Six of its seven carry part of what they
are cited for. Its problems are of a different kind from the rest of the
corpus: not invented references, but the wrong row of a table in a real one.

Tesla's patent does **not** presuppose an iron core — it is explicitly agnostic
("any conductor") — so it can be cited neither for nor against coreless
operation; the assumption to the contrary was this audit's, not the preprint's.
And the Griffiths citation is correct: Cambridge University Press did reissue
the fourth edition in 2017, ISBN 9781108420419, so the error hypothesised here
does not exist.

A third correction belongs to an earlier repository in this series rather than
to a preprint. Running the vocabulary census in `keywords.py` over all eighteen
records, instead of the ten available when `cymatic-eval` was written,
disproved a priority claim made there: "causal" first reaches zero in openQL
v1.0 of 3 October, and all seven tracked terms are absent from COBAR of
23 September and the Topological Momentum Drive of 24 September, both of which
make engineering claims. Seven of the eighteen records carry none of the
hypercomplex vocabulary and eleven carry it heavily, and the two groups
alternate rather than succeed one another, so there is no trend to read. The counts themselves were
right; the claim to priority built on them was an artefact of comparing against
part of the corpus. It is now corrected in `cymatic-eval` §1.

## 8. Limitations

The audit was first run on 9 October 2026 over sixteen records. openOmega was
deposited that same day and HOS-PV 2.0 five days later; both were added on
15 October by the same procedure, and `keywords.py` re-derived the
citation-marker counts of all eighteen from the deposits themselves with no
mismatch against the values recorded in October.

Twenty-six of 69 verdict rows do not rest on a full text, and each says which
substitute was used. Two books were unreachable: Adler's, replaced by his own
published summary plus two primary reviews, and Dixon's, replaced by his own
arXiv lecture referring back to it. Beranek & Mellow's interior could not be
opened, so that verdict rests on a verified chapter list; the efficiency
relation attributed to it was read in a secondary source and is flagged as such
in `refdata.py`. Sheoran et al. and Wright & Upadhyaya are confirmed closed
access. Keyword searching for Griffiths was done on the third edition with the
fourth edition's structure verified from a catalogue record. Of the seven rows
added for HOS-PV 2.0, three rest on an abstract: Shockley & Queisser, of which
only pp. 510–512 could be obtained, as an OCR'd court exhibit; Dediu et al.,
paywalled with no repository copy; and Naaman & Waldeck, supplemented by the
same authors' open-access perspective, which is where the 85 % figure is. Smith
& Michl's 2010 review is paywalled and was replaced by the same two authors'
2013 Annual Review, so no keyword counts are recorded for that row.

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
tabulate it; `fetch.sh` reproduces the eighteen deposits from Zenodo and
`keywords.py` recomputes the citation-marker counts from them. `run_all.sh`
runs everything offline in about a second; `results.log` is the output of one
run.

## References

The eighteen audited deposits are listed with their DOIs in `README.md`. Every
work quoted in this write-up is cited in full in `refdata.py`, with a DOI or a
URL and a note on how it was obtained. Quotations are short excerpts used for
criticism and review.
