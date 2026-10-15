#!/usr/bin/env python3
"""What the search FOR support actually found.

This audit was run because the author of these preprints stated publicly that
the defence of his arguments is deliberately placed in the references rather
than written in the text.  That is a testable claim, and testing it fairly
means looking for support, not only for errors.  A reference that genuinely
carries a claim is a more valuable finding here than one that does not.

The list below is what the search found, ranked by strength.  Each entry gives
the quotation, where it is, and the rider that limits it, because in most cases
the rider comes from the same pages as the support.

Entries are ranked by their position in the list; nothing here hard-codes a
number that the list itself does not determine.
"""

from refdata import DEPOSITS, NO_REFERENCES, REFS

P = print

FOUND = [
    dict(
        where="Furey (2016), arXiv:1611.09182, ch. 2  "
              "[cited in SOTP, Zenodo 22962557, as [3]]",
        supports="the conceptual core of the whole 'Causal' trilogy: that "
                 "causality and irreversible time arise from the structure of "
                 "an algebraic expression",
        quote=[
          "Taking multiplication to be the propagation along an edge, and "
          "addition to be the joining of two edges at a vertex, it can be seen "
          "that this unevaluated algebraic expression gives a causal set.",
          "In the case of an algebra, an event is a calculation. ... an event "
          "can be seen to be irreversible, it cannot 'unhappen'. ... Time, "
          "then, is simply a sequence of calculations, and is clearly "
          "irreversible.",
          "the octonions' non-associativity is not a impediment, but instead a "
          "gift, and that this misunderstood algebra is really at the heart of "
          "the standard model of particle physics.",
        ],
        rider="Furey's own next step is the rider. Her gauge apparatus lives "
              "in an ASSOCIATIVE algebra -- 'As the composition of maps is "
              "always associative, C(x)O-left is an associative algebra', "
              "faithfully representing Cl(6) -- and her causal-set claim is "
              "conjectured only for associative expressions: 'It is at this "
              "early stage only a conjecture that any (associative) algebraic "
              "expression gives a causal set.' So the motive is supported and "
              "the mechanism, the associator as a hardware observable, is not.",
        verdict="supports the motive, refutes the mechanism, from the same "
                "thesis",
    ),
    dict(
        where="Shockley & Queisser (1961), J. Appl. Phys. 32, 510, footnote 22  "
              "[cited in HOS-PV 2.0, Zenodo 23364732, as [1]]",
        supports="the premise the whole deposit rests on: that the 33.7% "
                 "limit is a one-pair-per-photon limit and carrier "
                 "multiplication lies outside it, which is the defence of "
                 "'exceeding the Shockley-Queisser limit' in the title",
        quote=[
          "Once a photon exceeds about three times the energy gap [E_g], the "
          "probability of producing two or more hole-electron pairs becomes "
          "appreciable",
          "the data can be well fitted up to quantum yields greater than two "
          "by assuming a threshold of only slightly more than [E_g] and "
          "assuming the energy divides equally between the photohole and the "
          "photoelectron. This effect would slightly increase the possible "
          "quantum efficiency; however, we shall not consider it further in "
          "this article.",
        ],
        rider="The authors of the limit excluded multiplication by choice, "
              "so exceeding it this way is legitimate and the deposit is "
              "right about that. The rider is the size of the gap: the same "
              "deposit's reference [5] puts a single junction with "
              "multiplication at 44.4%, not the 45.9% claimed, and 45.9% is "
              "inside that work's two-gap TANDEM range of 45.7-47.7%. The "
              "model rebuilt in hospv-eval reproduces 33.77%, 44.62% and "
              "42.09% for multiplication capped at two carriers per photon, "
              "which is what singlet fission does.",
        verdict="the best-hidden genuine defence in the corpus, in a footnote "
                "of a 1961 paper, for a claim that then overshoots it",
    ),
    dict(
        where="Baez (2002), arXiv:math/0105155, sec. 2.3 and 3.3  "
              "[cited in openQL v1.0, Zenodo 23112560, as [5]]",
        supports="a real-matrix encoding of octonion multiplication, and a "
                 "derivation of the number 12 better than either of the two "
                 "the preprint gives",
        quote=[
          "Left multiplication by any element a in K gives an operator "
          "L_a : K -> K, x -> ax. ... its matrix is block diagonal, built from "
          "2 x 2 blocks ... We thus obtain a representation of the Clifford "
          "algebra Cliff(Im(K)) on K.",
          "we define sl(m, K) to be the Lie algebra of operators on K^m "
          "generated by operators of this form. ... Note that multiplication "
          "in this group is given by composition of real-linear operators, "
          "which is associative even for K = O.",
          "Note that the numbers 9, 10, 12 and 16 are 8 more than the "
          "dimensions of R, C, H and O. As usual, this is no coincidence!",
        ],
        rider="The weak form of the claim is supported and the strong form is "
              "excluded: L_a o L_b != L_{ab}, so this is a representation of "
              "operators, not an isomorphism of algebras. The openql-eval "
              "repository already measures exactly this construction -- "
              "L_x L_y against L_{xy} gives 1.8e-15 for H and 29.5 "
              "(relative 2.76) for O -- but did not credit Baez with "
              "supplying it. For 12: sl(3,H) acts on H^3 ~ R^12 as real 12x12 "
              "operators and the magic square carries so(12) at (H,H). The "
              "preprint never points at this.",
        verdict="genuine support the preprint does not claim, and a better "
                "derivation than its own",
    ),
    dict(
        where="Moreno (1998), arXiv:q-alg/9710013, introduction  "
              "[cited in openOmega, Zenodo 23263528, as [3]]",
        supports="that non-zero elements whose product is exactly zero really "
                 "do exist in the sedenions, which is the mechanism the "
                 "deposit executes annihilation with",
        quote=[
          "for n >= 4 this norm-preserving formula is not true in general and "
          "this opens the possibility of the existence of zero divisors in "
          "A_n for n >= 4 i.e. x and y non-zero elements in A_n such that "
          "xy = 0 e.g. let x = e1 + e10 and y = e15 - e4 in R^16 = A_4",
        ],
        rider="Two riders out of the same two pages. The zero divisors exist "
              "BECAUSE ||xy|| = ||x|| ||y|| fails above dimension 8, so the "
              "norm is destroyed in exactly the operation the deposit "
              "performs 'with absolute energy conservation'. And Moreno's own "
              "item 2) disposes of the need for sedenions at all in the "
              "deposit's own matrix formulation: 'in an associative "
              "(alternative) context as in M_n(R) ... 0 != A is a zero "
              "divisor if and only if det A = 0'.",
        verdict="the example the openomega-eval repository found by brute "
                "search, up to the sign of y, was printed in the reference "
                "all along",
    ),
    dict(
        where="Adler (1995), via his own summary arXiv:hep-th/9607008, with "
              "Horwitz arXiv:quant-ph/9602001 and Baez & Huerta "
              "arXiv:1101.5690  [cited in PCTP, Zenodo 22962188, as [1]]",
        supports="the premise that the ordinary tensor product fails over the "
                 "quaternions -- a genuine, long-standing obstruction, and "
                 "Adler is the right citation for it",
        quote=[
          "The construction of a tensor product of quaternion modules ... has "
          "long been an obstacle in quaternionic theories, since there is an "
          "essential destruction of linearity, i.e., f q (x) g != "
          "(f (x) g)q, where q in H.",
          "the tensor product of quaternionic Hilbert spaces is not naturally "
          "a quaternionic Hilbert space.",
        ],
        rider="Adler's key result is fatal to the application: 'the S-matrix "
              "is always a complex matrix with no dependence on the "
              "quaternionic units j, k ... Hence the asymptotic dynamics for "
              "quaternionic quantum mechanics is always an effective complex "
              "theory', and 'noncommutative dynamics hides itself beneath "
              "effective complex quantum mechanical structures'. A processor "
              "whose output is measured cannot exhibit the "
              "non-commutativity it is built to execute.",
        verdict="supports the premise, refutes the device, from the same book",
    ),
    dict(
        where="Smejkal, Sinova & Jungwirth (2022), PRX 12, 040501, Table III  "
              "[cited in HOS-PV 2.0, Zenodo 23364732, as [7]]",
        supports="the altermagnetic collector, in the one place in this "
                 "corpus where a reference is stronger than the claim it "
                 "carries",
        quote=[
          "RuO2 ... TN 400 K ... Splitting 1400 meV ... dxy, P-2",
          "MnTe ... TN 310 K ... Splitting 1100 meV ... g-wave, B-4",
          "The electrical current then becomes spin-polarized when the bias "
          "is applied along the x or y-direction",
        ],
        rider="The deposit asks for 0.5-1.0 eV of spin splitting and the "
              "table gives 1.1-1.4 eV for the two materials it names. The "
              "riders are in the same row: MnTe is listed as g-wave, not the "
              "d-wave the sentence claims, its Neel temperature of 310 K is "
              "twelve kelvin above standard test conditions and below the "
              "318-332 K a module runs at, and the 'organic-inorganic "
              "altermagnetic perovskites' of the same sentence are not in the "
              "table, which has an inorganic perovskite oxide at 20 meV and "
              "an organic insulator below 50 meV.",
        verdict="supported, and the temperature that defeats it is in the "
                "same table",
    ),
    dict(
        where="Rao et al. (2013), arXiv:1303.2821  "
              "[cited in HOS-PV 2.0, Zenodo 23364732, as [3]]",
        supports="the triplet drain the architecture is built to close, and "
                 "the 25%/75% spin statistics of the sentences before the "
                 "marker, word for word",
        quote=[
          "recombination of spin-uncorrelated charges should lead to the "
          "formation of 1CT and 3CT states in a 1:3 ratio based on spin "
          "statistics",
          "We show that triplet exciton formation can be the major loss "
          "mechanism in OPVs.",
        ],
        rider="The cure is in the same paper and it is not chirality: "
              "'even when energetically favoured, the relaxation of 3CT to "
              "T1 can be strongly suppressed, via control over wavefunction "
              "delocalisation', and in the efficient blend 'no triplet "
              "formation is observed at room temperature'. The word 'chiral' "
              "occurs zero times in it. The claim's other half fares worse: "
              "'fill factor' occurs zero times, and the level ordering the "
              "deposit calls a V_oc degrader is 'required to maximise open "
              "circuit voltage' here.",
        verdict="supports the disease, reports an achiral cure for it",
    ),
    dict(
        where="Bi et al. (2011), DOI 10.1038/nphoton.2011.270  "
              "[cited in PCTP, Zenodo 22962188, as [4]]",
        supports="on-chip non-reciprocity, which is the element the preprint "
                 "needs in order to forbid back-propagation and enforce a "
                 "causal ordering",
        quote=[
          "we report the first monolithically integrated magneto-optical "
          "isolator on silicon. Using a non-reciprocal optical resonator ... "
          "we demonstrate unidirectional optical transmission with an "
          "isolation ratio up to 19.5 dB",
        ],
        rider="Non-reciprocity is S != S-transpose, not AB != BA. It does not "
              "produce non-commuting operators: Jones matrices are already "
              "non-commutative in the reciprocal case. And the numbers do not "
              "match -- the preprint claims better than 35 dB of reverse "
              "isolation against this source's 19.5 dB.",
        verdict="real hardware support for one element, not for the logic",
    ),
    dict(
        where="Lehmann et al. (2011), DOI 10.1016/j.soilbio.2011.04.022, "
              "abstract  [cited in Phytomining, Zenodo 23174932, as 3]",
        supports="biochar as a carrier for a bacterial inoculant, which is "
                 "the smart-pellet concept",
        quote=[
          "a significant number of early studies on biochar-type materials as "
          "soil amendments either for managing pathogens, as inoculant "
          "carriers or for manipulative experiments",
        ],
        rider="The same review contradicts the 'massive CEC' the preprint "
              "claims -- 'typically have initially low cation exchange "
              "capacities (CEC)' -- and reports nitrogen immobilisation "
              "'with resultant decreases in N uptake and growth of crops' and "
              "loss of mycorrhizal fungi where heavy-metal content is high.",
        verdict="real precedent for the delivery vehicle, not for its cargo",
    ),
    dict(
        where="Tesla (1894), US 512,340  "
              "[cited in COBAR, Zenodo 22923154, as [1]]",
        supports="the preprint's sentence on distributed capacitance in a "
                 "bifilar winding, which is the patent's own teaching",
        quote=[
          "Capacity secured in this particular way possesses an additional "
          "advantage in that it is evenly distributed, a consideration of the "
          "greatest importance in many cases.",
        ],
        rider="Two corrections against this audit's own prior assumption. The "
              "patent does NOT presuppose an iron core; it is explicitly "
              "agnostic ('any conductor'), so it can be cited neither for nor "
              "against coreless operation. And Tesla's aim is to cancel "
              "self-inductance so the coil behaves 'as though it possessed no "
              "self-induction', not to build a high-Q tank for force "
              "generation. Acoustic transduction: no mention in the patent.",
        verdict="supported, plus a correction to this audit rather than to the "
                "preprint",
    ),
]

# Claims checked against the cited works and supported by nothing in the corpus.
NO_CARRIER = [
    ("the associator executed as a hardware observable",
     "SOTP, PCTP; Furey, Dixon and Baez all pass to an associative algebra "
     "of left-multiplication operators instead"),
    ("2-bit or ternary tensor-core arithmetic",
     "X-Ternary; the Hopper whitepaper lists FP8, FP16, BF16, TF32, FP64 and "
     "INT8, and no generation has a sub-INT4 MMA type"),
    ("pure spin currents with zero ohmic dissipation",
     "SOTP; Manchon et al. derive the spin current from an applied charge "
     "current, at 1e7-1e8 A/cm^2 and about 100 fJ per bit"),
    ("non-destructive readout of an NV centre without state collapse",
     "PCTP; Doherty et al.: the optical readout 'simultaneously "
     "spin-polarise[s] the centre into the m_s = 0 spin projection'"),
    ("the elimination of hallucinations by determinism",
     "X-Ternary; InstructGPT reports 41% to 21%, and its 1.3B PPO-ptx model "
     "does worse than GPT-3 of the same size"),
    ("net momentum on a closed system",
     "Momentum Drive; the magnon BEC forms in both +/-k_min minima with zero "
     "group velocity, and the one reference with real forces is a squeeze-film "
     "reaction against a plate tens of micrometres away"),
    ("accelerated DNA transcription and repair from magnetic isotopes",
     "Phytomining; Buchachenko measures 3-5x SUPPRESSION of DNA synthesis for "
     "the same three isotopes and proposes them to kill cells"),
    ("biogenic gold as a scavenger of reactive oxygen species",
     "Phytomining; Reith et al.: gold INDUCES oxidative stress, and the cell "
     "exports it"),
    ("a structural relationship between ceruloplasmin and hemocyanin",
     "Hemocyanin; Hellman & Gitlin: ceruloplasmin 'plays no essential role in "
     "the transport or metabolism of' copper, and the domain intersection is "
     "empty"),
    ("a symplectic update step",
     "Intensional Physics Computing; 'symplectic' occurs in one work in the "
     "whole corpus, Baez, about the Freudenthal space for E7"),
    ("112 as a dimension",
     "openQL; '112' does not occur in Baez or Kuipers. The only '112' in the "
     "six works is Markidis's '112.7 Tflops/s theoretical peak' -- a "
     "throughput"),
    ("45.9% as a single-junction thermodynamic limit",
     "HOS-PV 2.0; the reference it is attached to gives 44.4% for a single "
     "gap with carrier multiplication and 45.7-47.7% for an ideal two-gap "
     "tandem, and the model rebuilt in hospv-eval caps doubling at 42.09%"),
    ("23.8 mA/cm2 collected above 2.25 eV",
     "HOS-PV 2.0; attached to no reference. The AM1.5G spectrum carries "
     "9.76 mA/cm2 above that energy at one electron per photon, so the "
     "figure needs 2.44 electrons per absorbed photon and fission gives two"),
    ("a carbon matrix that is spin-orbit weak and spin-selective at once",
     "HOS-PV 2.0; Naaman & Waldeck, cited for the CISS magnitudes, say the "
     "models 'all presume an unusually large spin-orbit coupling in chiral "
     "molecules for the effect to display the magnitudes seen in experiments'"),
    ("xi_SOC proportional to Z^4",
     "HOS-PV 2.0; attached to no reference, and a fit to the NIST ground-term "
     "splittings of F, Cl, Br and I gives an exponent of 1.69"),
    ("annihilation with absolute energy conservation",
     "openOmega; the zero divisors it runs on exist only because the norm is "
     "not multiplicative above dimension 8, which is what Moreno's cited "
     "paper is about"),
    ("the positron as a hole in the Dirac sea",
     "openOmega; the 1930 paper it cites identifies the holes as protons, and "
     "says a uniform sea is 'completely unobservable'"),
    ("coreless acoustic transduction efficiency",
     "COBAR; the cited Beranek & Mellow contains the relation by which a "
     "coreless design loses four to six decades of efficiency"),
    ("conductive nanofibres co-spun into a membrane",
     "COBAR; the Jirsak patent is about spinning throughput, spins aqueous "
     "PVA, and lists no acoustic application"),
]


def main():
    P("1. Support found, ranked")
    P()
    for i, f in enumerate(FOUND, 1):
        P(f"  [{i}] {f['where']}")
        P(f"      supports: {f['supports']}")
        for q in f["quote"]:
            P(f'        "{q}"')
        P(f"      rider: {f['rider']}")
        P(f"      -> {f['verdict']}")
        P()

    P("2. The pattern in the algebra deposits")
    P()
    P("  Furey, Dixon and Baez all resolve the non-associativity problem the")
    P("  same way, by moving to the associative algebra of left-multiplication")
    P("  operators:")
    P()
    P('    Furey:  "As the composition of maps is always associative,')
    P('             C(x)O-left is an associative algebra"')
    P('    Dixon:  "O_L ~ R(8) ~ CL(0,6) ... (Note: O_L is trivially')
    P('             associative.)"')
    P('    Baez:   "multiplication in this group is given by composition of')
    P('             real-linear operators, which is associative even for')
    P('             K = O"')
    P()
    P("  That manoeuvre is exactly the one the architecture is premised on not")
    P("  making.  So the hidden defence exists for the motivation of these")
    P("  papers and is refuted for their mechanism, out of the same pages.")

    P()
    n_ext = sum(d[3] for d in DEPOSITS)
    P(f"3. Claims with no carrier anywhere in the {n_ext} references")
    P()
    for claim, why in NO_CARRIER:
        P(f"  - {claim}")
        P(f"      {why}")

    P()
    P("4. Scoring the claim that was tested")
    P()
    P(f"  support found and substantial          {len(FOUND)} places")
    P(f"  claims with no carrier in any reference {len(NO_CARRIER)}")
    P()
    orphan = n_ext - sum(d[5] + d[6] for d in DEPOSITS)
    P("  The claim is partly vindicated.  In openQL and SOTP the cited")
    P("  literature does carry support the preprints never spell out, and in")
    P("  one case a better derivation than the preprint's own.  That is the")
    P(f"  author's point and it stands.  It does not extend to the {orphan} "
      f"references attached to")
    P(f"  nothing, to the {len(NO_REFERENCES)} deposits with no references, "
      f"or to the claims above, which the")
    P("  cited works contradict in their own words.")
    P()
    hospv = [r for r in REFS if r["dep"] == "23364732"]
    part = sum(1 for r in hospv if r["verdict"] == "PARTIAL")
    P("  HOS-PV 2.0 of 14 October is where the claim comes closest to being")
    P("  simply true.  It is the first deposit in which every external "
      "reference is")
    P(f"  attached to a sentence, all {len(hospv)} of them, and {part} of the "
      f"{len(hospv)} carry part of what")
    P("  they are cited for rather than none of it.  Three of the entries "
      "above come")
    P("  from it.  Its two largest problems are in its references too: 45.9% "
      "is the")
    P("  tandem row of the paper it is taken from, and the altermagnet's Neel")
    P("  temperature is in the table it is cited from.")


if __name__ == "__main__":
    main()
