#!/usr/bin/env python3
"""Every external reference in all 16 Zenodo records by M. Mazgal, with what the
cited work actually says about the claim it is attached to.

This file is DATA, not computation.  Each row records:

  link      how the preprint connects this reference to a claim:
            "in-text"  an [n] marker on a specific sentence
            "gloss"    a parenthetical note in the reference list saying what
                       the reference establishes
            "none"     listed, with no stated relation to anything
  claim     the sentence or gloss, verbatim, where one exists
  access    how far the cited work could actually be read:
            "full-text", "abstract", "author-summary" (a summary of the work
            written by its own author), "metadata", "none"
  verdict   SUPPORTS | PARTIAL | NO SUPPORT | REFUTES | UNRESOLVED
            REFUTES means the cited work states the opposite of the claim.
            UNRESOLVED means the reference itself could not be located.
  evidence  verbatim quotations from the cited work.  Nothing in this file is
            paraphrased from memory; a row with no quotation says so in
            `access` and its verdict is UNRESOLVED or carries a note.
  counts    keyword occurrence counts in the cited work's full text, where the
            full text was obtained.  0 means searched and absent, not assumed.

Where the full text could not be reached, the row says so and the verdict is
scoped to what the abstract supports.  Absence of a keyword in an OCR index is
recorded as strong but not absolute evidence.
"""

# ---------------------------------------------------------------------------
# The corpus.  n_ext = external references, n_self = self-citations,
# n_intext = external references attached to a sentence by an [n] marker,
# n_gloss = external references carrying a parenthetical gloss.
# ---------------------------------------------------------------------------
DEPOSITS = [
    # id          short                  date          n_ext n_self n_intext n_gloss
    ("22876757", "Acoustic Projector",   "2026-09-21",   6,    0,     5,      0),
    ("22877345", "X-Ternary",            "2026-09-21",   5,    0,     0,      0),
    ("22877912", "MPPT v1.0",            "2026-09-21",   0,    0,     0,      0),
    ("22914238", "MPPT v1.1",            "2026-09-23",   0,    0,     0,      0),
    ("22923154", "COBAR",                "2026-09-23",   5,    0,     0,      0),
    ("22934058", "Momentum Drive",       "2026-09-24",   8,    0,     0,      0),
    ("22959886", "CQFT",                 "2026-09-25",   0,    0,     0,      0),
    ("22962188", "PCTP",                 "2026-09-25",   5,    1,     0,      0),
    ("22962557", "SOTP",                 "2026-09-25",   5,    2,     2,      0),
    ("23112560", "openQL v1.0",          "2026-10-03",   5,    0,     0,      5),
    ("23156927", "Cymatic",              "2026-10-05",   5,    0,     0,      0),
    ("23174932", "Phytomining",          "2026-10-06",   6,    0,     0,      6),
    ("23186884", "Na-ion HFRS",          "2026-10-06",   5,    0,     0,      0),
    ("23209266", "Hemocyanin",           "2026-10-07",   4,    1,     0,      4),
    ("23241148", "openQL v1.1",          "2026-10-08",   5,    0,     0,      0),
    ("23241777", "Intensional Physics",  "2026-10-08",   5,    0,     0,      0),
]

# Deposits whose reference list is empty.  A defence cannot be hidden in a
# reference list that does not exist.
NO_REFERENCES = ["22877912", "22914238", "22959886"]


def R(dep, key, cite, link, verdict, access, claim=None, resolves=None,
      evidence=(), counts=None, source=None, note=None):
    return dict(dep=dep, key=key, cite=cite, link=link, verdict=verdict,
                access=access, claim=claim, resolves=resolves,
                evidence=list(evidence), counts=counts or {}, source=source,
                note=note)


REFS = [

    # =====================================================================
    # 22876757  Acoustic Projector -- the only deposit that attaches external
    # references to specific sentences with [n] markers.
    # =====================================================================
    R("22876757", "[1]",
      cite="Klippel, W. (2006). Tutorial: Loudspeaker Nonlinearities - Causes, "
           "Parameters, Symptoms. J. Audio Eng. Soc. 54(10), 907-939.",
      link="in-text", verdict="PARTIAL", access="full-text",
      claim="(a) 'ignores two critical layers of reality: the neurological "
            "processing of sound by the human brain and the dynamic "
            "nonlinearities of the loudspeaker operating under stress [1]'  "
            "(b) 'As the voice coil processes a bass transient, its electrical "
            "resistance increases, altering its damping factor (thermal "
            "compression) [1]'",
      evidence=[
        "This paper addresses the relationship between nonlinear distortion "
        "measurements and nonlinearities which are the physical causes for "
        "signal distortion in loudspeakers, headphones, micro-speakers and "
        "other transducers.",
        "The second effect of Bl(x) is the displacement dependency of the back "
        "EMF generated by the movement of the coil in permanent field. Here, "
        "the force factor Bl(x)2 is multiplied with the velocity and causes "
        "variation of the electrical damping.",
        "If the measurement time would be extended the heating of the coil "
        "would cause an additional amplitude compression (thermal effect).",
      ],
      counts={"brain": 0, "neuro": 0, "neural": 0, "cochlea": 0,
              "psychoacoustic": 0, "thermal compression": 0},
      source="AES e-lib 13881; full text at klippel.de",
      note="Nonlinearities: fully supported. The damping change is attributed "
           "by Klippel to Bl(x)^2, not to heating, and the thermal effect is "
           "tied to long measurement times rather than to a transient. The "
           "neurological half of claim (a) has no support."),

    R("22876757", "[2]",
      cite="Mandelbrot, B. B. (1983). The Fractal Geometry of Nature. "
           "W. H. Freeman.",
      link="in-text", verdict="NO SUPPORT", access="full-text",
      claim="'Human hearing evolved in environments where acoustic events "
            "exhibit a fractal structure and natural viscoelastic material "
            "hysteresis [2]'",
      evidence=[
        "MUSIC AS A SCALING (1/f) NOISE (R. F. VOSS). ... Voss & Clarke 1975 "
        "and Voss 1978 ... observe that in the works of such diverse composers "
        "as Bach, Beethoven, and the Beatles, both of the above measures of the "
        "audio signal are scaling noises, 1/f ... noises",
        "The argument I favor is that musical compositions are, as indicated by "
        "their name, composed: First, they subdivide into movements "
        "characterized by different overall tempos and/or levels of loudness. "
        "... The result is bound to be scaling!",
        "However, this scaling range does not extend below time spans of the "
        "order of one note. Higher frequencies are ruled by entirely different "
        "mechanisms ... therefore the high energy spectrum is more like f^2 "
        "than f^-1.",
      ],
      counts={"auditory": 0, "cochlea": 0, "psychoacoust": 0, "perception": 0,
              "viscoelast": 0, "hysteres": 0, "rheolog": 0, "acoustic": 1},
      source="archive.org, 'Updated and Augmented' 1983 printing, OCR",
      note="The one 'acoustic' hit is a journal name in the bibliography. A "
           "real 1/f audio passage exists, but Mandelbrot explains it "
           "compositionally, which contradicts the evolutionary reading, and "
           "bounds the scaling above one note length. The nearest thing to "
           "viscoelastic memory is the 'Scaling in elastic silk threads' "
           "sketch (Weber, Kohlrausch), where aftereffects 'decay "
           "hyperbolically in time, not exponentially' -- creep and recovery, "
           "never called hysteresis and never connected to sound."),

    R("22876757", "[3]",
      cite="Baez, J. C. (2002). The Octonions. Bull. AMS 39(2), 145-205.",
      link="in-text", verdict="PARTIAL", access="full-text",
      claim="'A change in one parameter affects all others non-associatively "
            "over time. The system therefore maps the signal into an 8D "
            "octonion hypercomplex space [3]'",
      evidence=[
        "The octonions are an 8-dimensional algebra with basis 1, e1, e2, e3, "
        "e4, e5, e6, e7",
        "note that any algebra has a trilinear map [.,.,.]: A^3 -> A called the "
        "associator, given by [a, b, c] = (ab)c - a(bc). The associator "
        "measures the failure of associativity just as the commutator "
        "[a,b] = ab - ba measures the failure of commutativity.",
      ],
      counts={"time-dependen": 0, "over time": 0, "dynamics": 0, "memory": 0,
              "signal process": 0, "hysteresis": 0, "acoustic": 0,
              "loudspeaker": 0, "engineering": 0},
      source="arXiv:math/0105155, DOI 10.1090/S0273-0979-01-00934-X",
      note="8 dimensions and non-associativity are supported. The bridge is "
           "not: associativity is a statement about the bracketing of a triple "
           "product, (ab)c vs a(bc). 'Parameter A affects B over time' is "
           "coupled nonlinear dynamics, a different notion, for which Baez "
           "offers nothing."),

    R("22876757", "[4]",
      cite="Canaan Inc. (2018). Kendryte K210 Standalone Commercial Edge "
           "Computing SoC Datasheet.",
      link="in-text", verdict="PARTIAL", access="full-text",
      claim="'a dual-core SoC architecture with a tensor accelerator (KPU), "
            "such as the Kendryte K210 [4]'",
      evidence=[
        "The K210 includes two 64-bit RISC-V CPU cores, each with a built-in "
        "independent FPU.",
        "KPU is a general-purpose neural network processor with built-in "
        "convolution, batch normalization, activation, and pooling operations.",
        "Support for 1x1 and 3x3 convolution kernels",
        "Up to 8 channels of audio input data, ie 4 stereo channels",
        "Simultaneous scanning pre-processing and beamforming for sound sources "
        "in up to 16 directions",
      ],
      counts={"tensor": 0, "matrix": 0, "GEMM": 0, "TOPS": 0, "GOPS": 0,
              "FLOPS": 0, "multiply-accumulate": 0},
      source="kendryte_datasheet_20181011163248_en.pdf",
      note="Dual-core and the KPU are supported. The datasheet never calls the "
           "K210 a tensor accelerator and gives no throughput figure at all; "
           "the KPU does convolution, batch norm, activation and pooling only, "
           "with 1x1 and 3x3 kernels, so an arbitrary 8x8 octonion product "
           "would have to run on the RISC-V cores. Real support found "
           "elsewhere in the same datasheet: a dedicated audio processor with "
           "16-direction beamforming and a 512-point FFT, the chip being aimed "
           "at 'machine hearing'. That justifies the platform, not the KPU."),

    R("22876757", "[5]",
      cite="Texas Instruments. (2018). TPA3116D2 50-W Stereo Class-D Audio "
           "Amplifier with AM Avoidance. Technical Reference Manual.",
      link="in-text", verdict="REFUTES", access="full-text",
      claim="'The analog signal drives a mass-produced Class-D amplifier "
            "(TPA3116) [5]. Its innate nonlinearities and dead-time errors are "
            "predicted and canceled mathematically before amplification.'",
      evidence=[
        "TPA3116D2 15-W, 30-W, 50-W Filter-Free Class-D Stereo Amplifier "
        "Family With AM Avoidance",
        "Feedback Power-Stage Architecture With High PSRR Reduces PSU "
        "Requirements",
        "The THD penalty in 1SPW mode is minimized by the high performance "
        "feedback loop.",
      ],
      counts={"dead": 0},
      source="TI SLOS708G",
      note="The part and its THD+N (0.1% typ at half power) are confirmed. The "
           "word 'dead' does not occur once in 32 pages, so dead time is "
           "neither specified nor user-accessible. The feedback taps "
           "OUTxx_FB run to internal summing stages and no _FB pin exists in "
           "the 32-pin package, so the loop is closed on-chip; the datasheet "
           "states that the loop already corrects the power-stage "
           "nonlinearities. External open-loop pre-compensation would act on "
           "a system that corrects itself through an unspecified transfer "
           "function."),

    R("22876757", "[6]",
      cite="Putland, P. A. (1993). Active Control of Loudspeakers. Audio "
           "Engineering Society Convention 94, Berlin.",
      link="none", verdict="UNRESOLVED", access="none",
      source="AES e-library returns HTTP 403 behind Cloudflare; not in the "
             "Wayback Machine",
      note="Could not be located. Indirect evidence that it does not exist in "
           "this form, stated as negative evidence only: the loudspeaker "
           "Putland is G. R., not P. A.; a 'P. A. Putland' published on "
           "avalanche photodiodes in 1990; a loudspeaker bibliography of 1000+ "
           "entries lists exactly four G. R. Putland works and this is not one "
           "of them. His real 1993 paper is JAES 41(6), 435-451, on Webster's "
           "horn equation. Not cited anywhere in the body text."),

    # =====================================================================
    # 22877345  X-Ternary
    # =====================================================================
    R("22877345", "1",
      cite="Ma, S., et al. (2024). The Era of 1-bit LLMs: All Large Language "
           "Models are in 1.58 Bits. arXiv:2402.17764.",
      link="none", verdict="PARTIAL", access="full-text",
      evidence=[
        "It is trained from scratch, with 1.58-bit weights and 8-bit "
        "activations.",
        "BitNet b1.58 starts to match full precision LLaMA LLM at 3B model "
        "size.",
        "it reduces the activations from 16 bits to 8 bits, allowing the "
        "context length to be doubled ... This can be further losslessly "
        "compressed to 4 bits or even lower for 1.58-bit LLMs, which we leave "
        "as future work.",
        "we envision and call for actions to design new hardware and system "
        "specifically optimized for 1-bit LLMs.",
      ],
      counts={"FP8": 0, "block": 0, "group": 0, "2:4": 0, "sparsit": 0,
              "octonion": 0, "determinis": 0, "hallucinat": 0},
      source="arXiv:2402.17764",
      note="Ternary weights are viable, which supports one sentence of the "
           "preprint. Scaling is per-tensor absmean, a single scalar per "
           "matrix, so FP8 scaling in blocks of 32 is not supported. A 2-bit "
           "KV cache is explicitly future work and at 4 bits. The 70B figures "
           "are cost projections measured on two 80GB A100 cards, so they do "
           "not support 70B on one 24GB card."),

    R("22877345", "2",
      cite="NVIDIA Corporation. (2024). NVIDIA Hopper Architecture In-Depth. "
           "Technical Whitepaper.",
      link="none", verdict="REFUTES", access="full-text",
      evidence=[
        "The new fourth-generation Tensor Core architecture in H100 ... FP8, "
        "FP16, BF16, TF32, FP64, and INT8 MMA data types are supported.",
        "This variant ... can be used when A is a structured sparse matrix "
        "with 50% zeros in each row distributed in a shape-specific "
        "granularity. ... sparsity is expected to be at 2:4 granularity, i.e. "
        "each 4-element vector of a matrix row contains 2 zeros.",
        "doubling the performance of standard Tensor Core operations",
      ],
      source="H100 Tensor Core GPU Architecture whitepaper v1.01 p.22; "
             "PTX ISA 9.4 sec. 9.7.17.5.2",
      note="The complete wgmma.mma_async operand list is f16, bf16, tf32, FP8 "
           "(e4m3/e5m2), s8/u8 and b1 with .and+.popc. No .s4/.u4, and .u2/.s2 "
           "exist only as conversion types in cvt.pack.sat. There is no native "
           "2-bit or ternary tensor-core data type on Hopper, and none on any "
           "generation: Blackwell's tcgen05.mma bottoms out at FP4. 2:4 "
           "sparsity is a pruning constraint whose accuracy claim is "
           "conditioned on retraining, not a bypass of zeros, and sparse "
           "WGMMA does not accept sub-byte operands at all."),

    R("22877345", "3",
      cite="Kirkpatrick, J., et al. (2017). Overcoming catastrophic forgetting "
           "in neural networks. PNAS 114(13), 3521-3526.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "This constraint is implemented as a quadratic penalty, and can "
        "therefore be imagined as a spring anchoring the parameters to the "
        "previous solution.",
      ],
      counts={"quantiz": 0, "ternary": 0, "2-bit": 0, "LLM": 0, "inference": 0},
      source="arXiv:1612.00796 (PNAS version behind 403)",
      note="EWC is a continual-learning method demonstrated on permuted MNIST "
           "and Atari. It does not touch inference-time quantisation."),

    R("22877345", "4",
      cite="Schulman, J., et al. (2017). Proximal Policy Optimization "
           "Algorithms. arXiv:1707.06347.",
      link="none", verdict="NO SUPPORT", access="full-text",
      counts={"quantiz": 0, "ternary": 0, "inference": 0, "GPU": 0,
              "straight-through": 0},
      source="arXiv:1707.06347",
      note="A reinforcement-learning objective tested on simulated robotic "
           "locomotion and Atari. Nothing on inference or quantisation."),

    R("22877345", "5",
      cite="Ouyang, L., et al. (2022). Training language models to follow "
           "instructions with human feedback. NeurIPS 35, 27730-27744.",
      link="none", verdict="REFUTES", access="full-text",
      claim="(the preprint claims '100% mathematical determinism' and the "
            "elimination of hallucinations)",
      evidence=[
        "InstructGPT models make up information not present in the input about "
        "half as often as GPT-3 (a 21% vs. 41% hallucination rate, "
        "respectively).",
        "InstructGPT still makes simple mistakes. ... when given an "
        "instruction with a false premise, the model sometimes incorrectly "
        "assumes the premise is true.",
        "the exception is our 1.3B PPO-ptx model, which performs slightly "
        "worse than a GPT-3 model of the same size.",
      ],
      counts={"quantiz": 0, "2-bit": 0, "octonion": 0, "determinis": 0},
      source="arXiv:2203.02155",
      note="41% to 21%, not to zero."),

    # =====================================================================
    # 22923154  COBAR
    # =====================================================================
    R("22923154", "[1]",
      cite="Tesla, N. (1894). Coil for Electro-Magnets. U.S. Patent 512,340.",
      link="none", verdict="PARTIAL", access="full-text",
      evidence=[
        "My present invention has for its object to avoid the employment of "
        "condensers which are expensive, cumbersome and difficult to maintain "
        "in perfect condition, and to so construct the coils themselves as to "
        "accomplish the same ultimate object.",
        "Capacity secured in this particular way possesses an additional "
        "advantage in that it is evenly distributed, a consideration of the "
        "greatest importance in many cases.",
        "a capacity capable of neutralizing its self-induction",
        "with no other opposition than that of ohmic resistance, or, in other "
        "words, as though it possessed no self-induction",
      ],
      counts={"iron": 0, "core": 0, "resonance": 0, "acoustic": 0, "sound": 0,
              "transducer": 0, "diaphragm": 0, "bifilar": 0},
      source="US512340A",
      note="The preprint's sentence on distributed capacitance is the patent's "
           "own teaching, verbatim. Two corrections against this audit's own "
           "prior assumption: the patent does not presuppose an iron core, it "
           "is explicitly agnostic ('any conductor'), so it cannot be cited "
           "for or against coreless operation. And Tesla's aim is to cancel "
           "self-inductance so the coil behaves as a pure resistance, not to "
           "build a high-Q tank that stores energy for force generation. "
           "Acoustic transduction: no mention."),

    R("22923154", "[2]",
      cite="Beranek, L. L., & Mellow, T. (2012). Acoustics: Sound Fields and "
           "Transducers. Academic Press.",
      link="none", verdict="NO SUPPORT", access="metadata",
      source="Elsevier contents listing; Crossref ISBN 9780123914217",
      note="The book's interior could not be opened (ScienceDirect 403, no "
           "Google Books preview), so this verdict rests on the verified "
           "chapter list. There is no chapter on parametric fields, "
           "ultrasonic carriers, phase-modulated transduction, diaphragm "
           "levitation or nanofibres, in this edition or in the 2019 second "
           "edition. ATTRIBUTION FLAG: the efficiency relation "
           "eta_0 proportional to (Bl)^2 / (R_e M_ms^2) was read in a source "
           "that attributes it to this book, not in the book itself. Taking "
           "it as given, it is the theory by which a coreless design without "
           "a permanent magnet loses two to three decades of B and so four to "
           "six decades of efficiency -- i.e. the cited book contains the "
           "argument against the device."),

    R("22923154", "[3]",
      cite="Klippel, W. (1992). Dynamic Measurement and Interpretation of the "
           "Nonlinear Parameters of Electrodynamic Loudspeakers. JAES.",
      resolves="J. Audio Eng. Soc. 38(12), 944-955 (1990) -- the year in the "
               "citation is wrong",
      link="none", verdict="NO SUPPORT", access="abstract",
      evidence=[
        "The nonlinear parameters, which vary with voice-coil displacement, "
        "are measured dynamically, and the coefficients in their series "
        "expansions are determined.",
      ],
      source="OpenAlex W1579767704, AES e-lib 6002; the year is confirmed by "
             "Klippel's own self-citation: 'vol. 38, pp. 944 - 955 (1990)'",
      note="Large-signal, displacement-dependent parameters of a conventional "
           "driver with a magnet, an iron gap and a suspension. Nothing on "
           "coreless, bifilar, quadrature or nanofibre construction. It "
           "defines a distortion metric COBAR would have to meet, not support "
           "for meeting it."),

    R("22923154", "[4]",
      cite="Griffiths, D. J. (2017). Introduction to Electrodynamics "
           "(4th Edition). Cambridge University Press.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "F_mag = Q(v x B). (5.1) This is known as the Lorentz force law.",
      ],
      counts={"reluctance": 0, "magnetic circuit": 0, "loudspeaker": 0,
              "transducer": 0, "parametric": 0},
      source="OpenLibrary OL27987097M: Cambridge University Press, "
             "12 July 2017, ISBN 9781108420419",
      note="The publisher in the citation is CORRECT -- the error this audit "
           "hypothesised does not exist; CUP reissued the 4th edition. "
           "EDITION FLAG: keyword searching was done on the 3rd edition full "
           "text with the 4th edition's chapter structure verified from the "
           "catalogue record. The Lorentz force and mutual inductance are "
           "there; M = 0 for perpendicular coils follows from the Neumann "
           "formula but is never stated as a result, so it cannot be cited as "
           "one. With reluctance and magnetic circuits absent, this is the "
           "wrong source for a flux-concentration argument."),

    R("22923154", "[5]",
      cite="Jirsak, O., Sanetrnik, F., Pelka, F., Lukas, D., & Kotek, V. "
           "(2005). A method of nanofibres production from a polymer solution "
           "using electrostatic spinning. WO 2005024101A1.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "The aim of the invention is to create a method and a device "
        "industrially applicable and able to reach a high spinning capacity.",
        "the polymer solution (2) is supplied into the electric field for "
        "spinning using the surface of the rotating charged electrode (30)",
        "filtration, as battery separators, for production of special "
        "composites, for construction of sensors with extremely low time "
        "constant, for production of protective clothes, in medicine",
      ],
      counts={"PVDF": 0, "polyvinylidene": 0, "piezo": 0, "acoust": 0,
              "sound": 0, "membrane": 0, "diaphragm": 0, "copper": 0,
              "nanowire": 0, "yarn": 0},
      source="WO2005024101A1; US 7,585,437 B2",
      note="The preprint does use nanofibres, so the citation is on topic in "
           "principle. But the patent is about throughput in needleless "
           "free-surface electrospinning, both worked examples spin aqueous "
           "polyvinyl alcohol, and the applications it lists for itself do "
           "not include acoustics. It gives no support for PVDF, for "
           "piezoelectric membranes, or for conductive traces co-spun into a "
           "membrane body. The four 'conduct' hits all concern the electrical "
           "conductivity of the polymer solution as a spinnability parameter."),

    # =====================================================================
    # 22934058  Momentum Drive
    # =====================================================================
    R("22934058", "[1]",
      cite="Demokritov, S. O., et al. (2006). Bose-Einstein condensation of "
           "quasi-equilibrium magnons at room temperature under pumping. "
           "Nature 443(7110), 430-433.",
      link="none", verdict="REFUTES", access="abstract",
      claim="(the preprint's load-bearing step: a room-temperature magnon BEC "
            "held from 'around the 150th cycle (approx. 3 ms at 50 kHz)', "
            "whose topological phase shift makes the rotor lattice 'physically "
            "displace itself in space')",
      evidence=[
        "It has been predicted that a quasi-equilibrium system of bosons could "
        "undergo Bose-Einstein condensation even at relatively high "
        "temperatures, if the flow rate of energy pumped into the system "
        "exceeds a critical value",
        "the spectrum of magnons in magnetic films possess two energy minima "
        "corresponding to non-zero wavevectors +/-kmin. Consequently, the "
        "magnon BEC is doubly degenerate: two condensate components are "
        "simultaneously formed in the two spectral minima at kBEC = +/-kmin.",
        "although the phase velocities of magnons at +/-kmin can be as large, "
        "as several kilometers per second, the group velocity at these "
        "spectral points is zero. Therefore, the created condensate clouds do "
        "not move and occupy the same area in the real space.",
        "magnons are quasiparticles and, thus, their number is not conserved. "
        "In a thermodynamic equilibrium, magnon chemical potential is always "
        "zero, and thus no equilibrium BEC of magnons can exist.",
      ],
      source="DOI 10.1038/nature05117; the +/-kmin and group-velocity "
             "quotations are from Borisenko, Demidov, Pokrovsky & Demokritov, "
             "arXiv:2003.12436, i.e. from the same author; the "
             "chemical-potential quotation from the review arXiv:2312.10119",
      note="Net momentum is zero by the +/-kmin symmetry and the condensate "
           "does not move even as a single component, because the group "
           "velocity vanishes at those points. Not an equilibrium BEC: it "
           "exists only under continuous pumping, with measured lifetimes of "
           "175-230 ns against the 3 ms the preprint assumes, four orders "
           "out. Material mismatch too: YIG, whose low damping comes from "
           "Fe3+ having almost no orbital moment, against the preprint's "
           "CoFe2O4, where Co2+ has a large one."),

    R("22934058", "[2]",
      cite="Zhu, H., et al. (2018). Observation of chiral phonons. "
           "Science 359(6375), 579-582.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "we confirmed their chirality by the infrared circular dichroism "
        "arising from pseudoangular momentum conservation.",
      ],
      counts={"force": 0, "propulsion": 0, "thrust": 0},
      source="DOI 10.1126/science.aar2711",
      note="Monolayer WSe2 at 82 K, not a bulk material at room temperature. "
           "The measured quantity is pseudoangular momentum, not linear "
           "momentum. The one usable sentence, that momentum 'must have been "
           "transferred to phonons', is disqualified by its own neighbouring "
           "equation q = p_i - p_f = -2K = K, which holds only modulo a "
           "reciprocal lattice vector: crystal momentum, not free momentum."),

    R("22934058", "[3]",
      cite="Nagaosa, N., & Tokura, Y. (2013). Topological properties and "
           "dynamics of magnetic skyrmions. Nature Nanotech. 8(12), 899-911.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "The skyrmion lattice is incommensurate with the underlying atomic "
        "lattice.",
        "free from the commensurability pinning by the crystal lattice",
      ],
      counts={"Magnus": 0, "momentum conservation": 0, "net force": 0,
              "recoil": 0},
      source="DOI 10.1038/nnano.2013.243",
      note="What moves is the spin texture, not the lattice. Every force in "
           "the Thiele equation -- gyrovector, Gilbert damping, pinning -- is "
           "an internal reaction inside the sample, and the emergent field "
           "acts on the conduction electrons of the same crystal."),

    R("22934058", "[4]",
      cite="Levin, M. A., & Wen, X. G. (2005). String-net condensation: A "
           "physical mechanism for topological phases. Phys. Rev. B 71(4), "
           "045110.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "While this Hamiltonian may be too complicated to be realized "
        "experimentally",
        "We hope that this physical picture may help direct the search for "
        "topological phases in real condensed matter systems.",
      ],
      counts={"momentum": 0, "force": 0, "torque": 0, "rotation": 0,
              "magnon": 0, "Bose": 0, "temperature": 0, "material": 0,
              "propulsion": 0},
      source="arXiv:cond-mat/0404617, DOI 10.1103/PhysRevB.71.045110",
      note="An abstract lattice-Hamiltonian and tensor-category construction "
           "with no physical unit, no temperature and no material anywhere in "
           "it."),

    R("22934058", "[5]",
      cite="Google Quantum AI and Collaborators. (2023). Non-Abelian braiding "
           "of graph vertices in a superconducting processor. "
           "Nature 618(7964), 264-269.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "Since the braiding of non-Abelian anyons in this platform is achieved "
        "through unitary gate control rather than adiabatic evolution of a "
        "Hamiltonian system, we note that the anyons are not quasi-particles "
        "in the sense of eigenstates that persist throughout a Hamiltonian "
        "evolution.",
        "rotations in a space of topologically degenerate wavefunctions",
      ],
      counts={"momentum": 0, "force": 0, "motion": 0, "mechanical": 0,
              "propulsion": 0, "torque": 0, "room temperature": 0},
      source="DOI 10.1038/s41586-023-05954-4",
      note="25 transmons in a 5x5 lattice, T1 median 21.7 us. Moving an anyon "
           "means applying SWAP/CZ gates to static qubits; the rotations are "
           "in Hilbert space, explicitly not in real space."),

    R("22934058", "[6]",
      cite="Xiao, D., Chang, M. C., & Niu, Q. (2010). Berry phase effects on "
           "electronic properties. Rev. Mod. Phys. 82(3), 1959.",
      link="none", verdict="NO SUPPORT", access="full-text",
      claim="(the preprint claims an 'emergent electromagnetic field (derived "
            "from the Berry curvature of the spin superfluid)' manifesting "
            "'internal magnetic monopoles' that cancel back-EMF and allow "
            "'unlimited rotational velocity')",
      evidence=[
        "This velocity is always transverse to the electric field, which will "
        "give rise to a Hall current.",
        "Interestingly, while the magnetic monopoles are yet to be detected in "
        "the real world, the topological Chern numbers have already found "
        "correspondence with the quantized Hall conductance plateaus.",
      ],
      counts={"momentum conservation": 0, "conservation of momentum": 0,
              "propulsion": 0, "thrust": 0, "net force": 0,
              "reaction force": 0, "magnon": 0},
      source="arXiv:0907.2021, DOI 10.1103/RevModPhys.82.1959",
      note="This was the most promising candidate for a hidden defence and it "
           "is empty. The anomalous velocity is a transverse Hall current of "
           "charge carriers in a lattice, driven by an external field, and "
           "momentum throughout the semiclassical theory is gauge-invariant "
           "crystal momentum with kdot = -eE/hbar. The monopoles are "
           "monopoles of Berry curvature in parameter space."),

    R("22934058", "[7]",
      cite="Kikkawa, T., et al. (2016). Magnon polarons in the spin Seebeck "
           "effect. Phys. Rev. Lett. 117(20), 207203.",
      link="none", verdict="NO SUPPORT", access="full-text",
      counts={"momentum": 0, "force": 0, "torque": 0, "pressure": 0,
              "recoil": 0, "propulsion": 0, "conservation": 0},
      source="DOI 10.1103/PhysRevLett.117.207203, arXiv:1607.02312",
      note="One measured quantity: a DC voltage. Total |V| about 5 uV with the "
           "anomalies themselves around 100 nV, a 1-2% bump, on a 4.0 x 2.0 x "
           "0.5 mm sample clamped between two sapphire plates in a uniform "
           "field. No force transducer and no free suspension anywhere in the "
           "apparatus."),

    R("22934058", "[8]",
      cite="Hashimoto, Y., Koike, Y., & Ueha, S. (1996). Near-field acoustic "
           "levitation of planar specimens using flexural vibration. "
           "JASA 100(4), 2057-2061.",
      link="none", verdict="PARTIAL", access="abstract",
      evidence=[
        "specimens with a weight of several kilograms can be levitated stably "
        "by direct sound radiation pressure",
        "This phenomenon can be used in noncontact transportation of planar "
        "objects such as Si wafer and glass plates.",
        "When two very closely placed parallel surfaces (in the range from "
        "tens to several hundred microns) are cyclically squeezing the thin "
        "air film in between at a high frequency, the time-averaged reaction "
        "force from the air medium will be non-zero",
      ],
      source="DOI 10.1121/1.417915; the squeeze-film mechanism quotation is "
             "from arXiv:2110.01125, whose reference [1] is this paper",
      note="The only reference in this deposit with real newtons in it, and it "
           "is explicitly reaction-based: the force is air squeezed against a "
           "nearby plate across a gap of tens to hundreds of micrometres. "
           "Without an opposing surface, and in vacuum, the mechanism does "
           "not exist. The preprint uses it as a bearing, which is "
           "legitimate; it is not and cannot be a propulsion mechanism."),

    # =====================================================================
    # 22962188  PCTP
    # =====================================================================
    R("22962188", "[1]",
      cite="Adler, S. L. (1995). Quaternionic Quantum Mechanics and Quantum "
           "Fields. Oxford University Press.",
      link="none", verdict="PARTIAL", access="author-summary",
      claim="(the preprint's premise: 'Standard matrix multiplication assumes "
            "scalar fungibility ... In quaternionic space, this commutativity "
            "causes structural algebraic collapse', and its conclusion that "
            "photonic hardware natively executes a non-commutative causal "
            "tensor product)",
      evidence=[
        "The construction of a tensor product of quaternion modules ... has "
        "long been an obstacle in quaternionic theories, since there is an "
        "essential destruction of linearity, i.e., f q (x) g != (f (x) g)q, "
        "where q in H. In his book, Adler has described a new construction in "
        "the framework of path integrals which appears to be a very powerful "
        "way of handling the problem",
        "the tensor product of quaternionic Hilbert spaces is not naturally a "
        "quaternionic Hilbert space. Unfortunately, this issue is not "
        "addressed head-on in Adler's book ... There is no canonical way to "
        "make a quaternionic Hilbert space H into a bimodule.",
        "A key result in the book relating to this is that in quaternionic "
        "quantum mechanics, the S-matrix is always a complex matrix with no "
        "dependence on the quaternionic units j, k ... Hence the asymptotic "
        "dynamics for quaternionic quantum mechanics is always an effective "
        "complex theory",
        "noncommutative dynamics hides itself beneath effective complex "
        "quantum mechanical structures.",
      ],
      source="The book itself returned 403 (OUP/IAS). Quotations are from "
             "Adler's own summary of it, arXiv:hep-th/9607008; Horwitz, "
             "arXiv:quant-ph/9602001 sec. 5; Baez & Huerta, arXiv:1101.5690 "
             "sec. 3",
      note="HIDDEN DEFENCE, real: the premise is correct physics and Adler is "
           "the right citation for it -- the quaternionic tensor product is a "
           "genuine, long-standing obstruction. But Adler's key result is "
           "fatal to the application: j and k drop out of the S-matrix, so a "
           "processor whose output is measured cannot exhibit quaternionic "
           "non-commutativity in its asymptotic behaviour, and Adler places "
           "quaternions as an underlying dynamics beneath effectively complex "
           "physics -- the opposite of native hardware execution."),

    R("22962188", "[2]",
      cite="Shen, Y., et al. (2017). Deep learning with coherent nanophotonic "
           "circuits. Nature Photonics 11(7), 441-446.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "a general, real-valued matrix (M) may be decomposed as M = U Sigma V*",
        "we implement the nonlinear transformation I_out = f(I_in) in the "
        "electronic domain.",
      ],
      counts={"quaternion": 0, "commut": 0, "polariz": 0, "Stokes": 0,
              "angular momentum": 0},
      source="arXiv:1610.02365, DOI 10.1038/nphoton.2017.93",
      note="The hardware computes real-valued matrices by SVD on a mesh of 56 "
           "Mach-Zehnder interferometers, with information in optical "
           "amplitude and the nonlinearity done electronically. Matrix "
           "multiplication is non-commutative in general, but that is equally "
           "true of a GPU; the paper introduces no non-commutative "
           "computational resource and never frames anything that way."),

    R("22962188", "[3]",
      cite="Allen, L., Beijersbergen, M. W., Spreeuw, R. J., & Woerdman, J. P. "
           "(1992). Orbital angular momentum of light and the transformation "
           "of Laguerre-Gaussian laser modes. Phys. Rev. A 45(11), 8185.",
      link="none", verdict="NO SUPPORT", access="abstract",
      evidence=[
        "Laser light with a Laguerre-Gaussian amplitude distribution is found "
        "to have a well-defined orbital angular momentum.",
      ],
      source="DOI 10.1103/PhysRevA.45.8185; full text behind APS 401, so no "
             "keyword search was run on this one work",
      note="Establishes l*hbar per photon for exp(i l theta) modes. The "
           "algebra of OAM states is that of eigenstates of a single "
           "Hermitian L_z with l in Z -- the character of an abelian "
           "U(1) ~ SO(2), whose shifts commute. The Poincare-sphere / SU(2) "
           "analogy for OAM is not from this paper; it was introduced by "
           "Padgett & Courtial, Opt. Lett. 24, 430 (1999) and Agarwal, JOSA A "
           "16, 2914 (1999). And even granting it, SU(2) ~ unit quaternions "
           "holds for a two-state subspace, which does not by itself map four "
           "independent degrees of freedom onto Hamilton's relations."),

    R("22962188", "[4]",
      cite="Bi, L., et al. (2011). On-chip optical isolation in monolithically "
           "integrated non-reciprocal optical devices. Nature Photonics 5(12), "
           "758-762.",
      resolves="the real title is '...non-reciprocal optical RESONATORS'",
      link="none", verdict="PARTIAL", access="abstract",
      evidence=[
        "we report the first monolithically integrated magneto-optical "
        "isolator on silicon. Using a non-reciprocal optical resonator on an "
        "silicon-on-insulator substrate, we demonstrate unidirectional optical "
        "transmission with an isolation ratio up to 19.5 dB near the 1,550 nm "
        "telecommunication wavelength in a homogeneous external magnetic "
        "field.",
        "A 100 nm garnet film layer (Ce:YIG(80 nm)/YIG(20 nm)) was deposited "
        "on the single-mode silicon channel waveguide.",
      ],
      source="DOI 10.1038/nphoton.2011.270",
      note="HIDDEN DEFENCE, real: on-chip non-reciprocity is exactly the "
           "element the preprint needs to forbid back-propagation and enforce "
           "its causal ordering, and this paper demonstrates it "
           "monolithically. Three limits. Non-reciprocity is S != S-transpose, "
           "not AB != BA, and does not yield non-commuting operators -- Jones "
           "matrices are already non-commutative in the reciprocal case. The "
           "preprint claims better than 35 dB of reverse isolation; the source "
           "gives 19.5 dB. And the platform is Si + Ce:YIG, not the Si3N4 + "
           "BIG the preprint specifies, though Ce:YIG appears there as an "
           "alternative."),

    R("22962188", "[5]",
      cite="Doherty, M. W., et al. (2013). The nitrogen-vacancy colour centre "
           "in diamond. Physics Reports 528(1), 1-45.",
      link="none", verdict="REFUTES", access="full-text",
      claim="(the preprint claims NV-centre 'phase latches' read "
            "non-destructively 'without causing state collapse')",
      evidence=[
        "the optical dynamics of the NV- centre can be used to optically "
        "readout the centre's spin state and to simultaneously spin-polarise "
        "the centre into the m_s = 0 spin projection.",
        "the readout contrast ... is limited to a difference of a fraction of "
        "a photon between the m_s = 0 and +/-1 spin-projections. Consequently, "
        "a single qubit operation must be performed many times before "
        "sufficient shot-noise statistics are acquired to distinguish the "
        "spin-projections.",
      ],
      counts={"quaternion": 0, "orbital angular momentum": 0, "Si3N4": 0,
              "nitride": 0, "evanescent": 0, "latch": 0, "non-destructive": 0,
              "QND": 0},
      source="arXiv:1302.3288, DOI 10.1016/j.physrep.2013.02.001",
      note="The triplet structure, 2.87 GHz at 300 K and T2 > 1.8 ms are all "
           "confirmed. But the optical readout repolarises the centre as it "
           "reads, which is the opposite of non-destructive, and the contrast "
           "requires many repetitions. The only 'waveguide' in the paper is a "
           "microwave coplanar line."),

    # =====================================================================
    # 22962557  SOTP -- carries the corpus's only external in-text citation
    # besides the Acoustic Projector's
    # =====================================================================
    R("22962557", "[3]",
      cite="Furey, C. (2016). Standard Model Physics from an Algebra? "
           "PhD thesis, University of Waterloo. arXiv:1611.09182.",
      link="in-text", verdict="PARTIAL", access="full-text",
      claim="'Octonions have long been recognized in theoretical physics for "
            "their natural isomorphism to the Standard Model gauge group "
            "SU(3)xSU(2)xU(1) and the generation structure of quarks and "
            "leptons [3, 4].'",
      evidence=[
        "Taking multiplication to be the propagation along an edge, and "
        "addition to be the joining of two edges at a vertex, it can be seen "
        "that this unevaluated algebraic expression gives a causal set.",
        "So it seems to be possible that causality, of all things, could "
        "already appear at the level of an algebra.",
        "In the case of an algebra, an event is a calculation. ... an event can "
        "be seen to be irreversible, it cannot 'unhappen'. ... Time, then, is "
        "simply a sequence of calculations, and is clearly irreversible.",
        "we argue that physical concepts such as particles, causality, and "
        "irreversible time may result from the algebra acting on itself.",
        "From the complex octonionic portion of the algebra, we find minimal "
        "left ideals, and show that they mirror the behaviour of a generation "
        "of quarks and leptons under su(3)_c and u(1)_em.",
        "the octonions' non-associativity is not a impediment, but instead a "
        "gift, and that this misunderstood algebra is really at the heart of "
        "the standard model of particle physics.",
        "As the composition of maps is always associative, C(x)O-left is an "
        "associative algebra.",
        "The reader is encouraged to check that C(x)O-left faithfully "
        "represents the 64-complex-dimensional Clifford algebra Cl(6)",
        "It is at this early stage only a conjecture that any (associative) "
        "algebraic expression gives a causal set.",
      ],
      source="arXiv:1611.09182",
      note="HIDDEN DEFENCE, the strongest in the corpus. Furey's chapter 2 "
           "argues that causality and irreversible time emerge from the "
           "bracketing of an algebraic expression -- which is the conceptual "
           "core of this author's whole 'Causal' trilogy, is peer-reviewed, "
           "and is nowhere spelled out in his own text. The in-text citation "
           "[3, 4] is substantively grounded, although 'isomorphism' is loose: "
           "Furey works with minimal left ideals and stabiliser subgroups, not "
           "an isomorphism of O with the gauge group. The rider is fatal to "
           "the engineering claim: her gauge apparatus lives in an ASSOCIATIVE "
           "algebra isomorphic to Cl(6), and her causal-set construction is "
           "conjectured for associative expressions. She does not execute "
           "non-associativity; she acts associatively on a non-associative "
           "module. So the motive is supported and the mechanism -- the "
           "associator as a hardware observable -- is not."),

    R("22962557", "[4]",
      cite="Dixon, G. M. (1994). Division Algebras: Octonions, Quaternions, "
           "Complex Numbers and the Algebraic Design of Physics. Springer.",
      link="in-text", verdict="PARTIAL", access="author-summary",
      claim="(same sentence as [3])",
      evidence=[
        "O is an 8-dimensional real algebra, and despite its nonassociativity "
        "it can be incorporated into this Clifford algebra and spinor scheme.",
        "let O_L and O_R be the algebras spanned by these respective sets of "
        "left and right actions. Finally, and most importantly, "
        "O_L = O_R ~ R(8), so these are each the full algebras of "
        "endomorphisms on 8-dimensional O.",
        "O_L ~ R(8) ~ CL(0,6) ... (Note: O_L is trivially associative.)",
      ],
      source="The book returned 403 (Springer). Quotations are from Dixon's "
             "own arXiv:1012.1304, in which he refers back to the book",
      note="A matrix representation does exist -- but for the algebra of LEFT "
           "ACTIONS, which is associative and is the full endomorphism algebra "
           "R(8) ~ Cl(0,6). O itself has no faithful matrix representation "
           "because matrix multiplication is associative. The same manoeuvre "
           "as Furey's and Baez's."),

    R("22962557", "[5]",
      cite="Fert, A., Reyren, N., & Cros, V. (2017). Magnetic skyrmions: "
           "advances in physics and potential applications. Nature Reviews "
           "Materials 2(7), 17031.",
      link="none", verdict="NO SUPPORT", access="abstract",
      evidence=[
        "skyrmions are now stable at room temperature and can be manipulated "
        "by electrical currents",
        "velocity takes a finite value only above a critical current "
        "(~2 x 10^11 A m^-2)",
      ],
      counts={"helicity": 0, "octonion": 0, "non-associative": 0, "algebra": 0},
      source="DOI 10.1038/natrevmats.2017.31",
      note="Supports skyrmions as a room-temperature carrier. Refutes the "
           "dissipation claim, since the motion is charge-current driven with "
           "a threshold of 2e7 A/cm^2. The helicity angle the preprint assigns "
           "to one of its seven imaginary units as an independently "
           "controllable degree of freedom is not supported here."),

    R("22962557", "[6]",
      cite="Manchon, A., et al. (2019). Current-induced spin-orbit torques in "
           "ferromagnetic and antiferromagnetic systems. Rev. Mod. Phys. "
           "91(3), 035004.",
      link="none", verdict="REFUTES", access="full-text",
      claim="(the preprint claims pure spin currents with J_c = 0, so that "
            "'ohmic resistive dissipation (I^2 R) is entirely eliminated', and "
            "assigns Rashba and Dresselhaus coupling to two orthogonal "
            "imaginary units)",
      evidence=[
        "SHE originates from asymmetric spin deflection in the bulk of, e.g., a "
        "heavy metal induced by spin-orbit coupling. Such a deflection induces "
        "a pure spin current, transverse to the direction of the applied "
        "electrical current, that is subsequently absorbed in the adjacent "
        "magnetic layer.",
        "In perpendicularly magnetized structures with Delta >~ 500, the "
        "critical current density ranges from 10^7 to a few times 10^8 A/cm^2 "
        "depending on the switching speed ... the switching of a 50 nm wide dot "
        "is predicted to require less than 200 uA and a write energy smaller "
        "than 100 fJ at 1.5 ns",
        "The Rashba and Dresselhaus fields are confined to a plane and only "
        "appear for electric field lying in the plane. They differ in how the "
        "effective field is changed when the electric field is rotated.",
      ],
      counts={"octonion": 0, "non-associative": 0, "Fano": 0, "10 T": 0},
      source="arXiv:1801.09636, DOI 10.1103/RevModPhys.91.035004",
      note="The pure spin current is real but it is GENERATED BY a charge "
           "current that dissipates ohmically; the review writes its magnitude "
           "with sigma_N E, a charge current density, in it. About 100 fJ per "
           "bit, not zero. Rashba and Dresselhaus are both confined to the "
           "same plane and differ in rotation sense, so they are not "
           "orthogonal spin axes. The preprint's own equation inverts the role "
           "of the spin polarisation, which the spin Hall effect produces "
           "rather than takes as input."),

    R("22962557", "[7]",
      cite="Baez, J. C. (2002). The octonions. Bull. AMS 39(2), 145-205.",
      link="none", verdict="SUPPORTS", access="full-text",
      evidence=[
        "any algebra has a trilinear map [.,.,.]: A^3 -> A called the "
        "associator, given by [a,b,c] = (ab)c - a(bc).",
        "If e_i, e_j, and e_k are cyclically ordered in this way then "
        "e_i e_j = e_k, e_j e_i = -e_k. ... the Fano plane completely describes "
        "the algebra structure of the octonions.",
        "the octonions are not a Clifford algebra, since they are "
        "nonassociative.",
        "multiplication in this group is given by composition of real-linear "
        "operators, which is associative even for K = O.",
      ],
      source="arXiv:math/0105155",
      note="The preprint's associator definition and its epsilon rule are "
           "Baez's verbatim, and its Fano triple set was machine-checked here "
           "as a valid Fano plane -- all 21 pairs of the seven units covered "
           "exactly once. This is a genuine correctness result in the author's "
           "favour. Baez does not use 'faithful' of any octonion matrix "
           "representation, and makes the same associative-operator move as "
           "Furey and Dixon."),

    # =====================================================================
    # 23112560  openQL v1.0 -- every reference carries a gloss stating what it
    # establishes, which makes the glosses directly testable
    # =====================================================================
    R("23112560", "[1]",
      cite="Kuipers, J. B. (1999). Quaternions and Rotation Sequences. "
           "Princeton University Press.",
      link="gloss", verdict="PARTIAL", access="full-text",
      claim="'Provides the mathematical foundation for real-matrix isomorphism "
            "of quaternions used in openQL.'",
      evidence=[
        "The product of quaternions, defined in Equation 5.1, may be written "
        "using the algebra of matrices",
        "Isomorphism - In algebraic terms, with respect to addition, this "
        "one-to-one correspondence may be called an iso-morphism.",
        "hyper-complex numbers of rank n > 4. But since our concern is for "
        "graphics applications ... we will restrict our attention from this "
        "point on to the hyper-complex [numbers of rank 4].",
      ],
      counts={"octonion": 0, "Cayley algebra": 0, "Cayley-Dickson": 0,
              "eight-dimensional": 0, "sedenion": 0, "subalgebra": 0,
              "homomorphism": 0},
      source="Google Books full-text index, vol. _2sS4mC0p-EC; "
             "DOI 10.1515/9780691211701",
      note="The real 4x4 multiplication matrices are genuinely there (Eq. 5.3 "
           "p.109, Eq. 7.4/7.5 p.157), so the book is a valid primary source "
           "for a real-matrix REPRESENTATION of quaternions. But the word "
           "'isomorphism' occurs once and is explicitly scoped to addition, "
           "with the book showing on the same page that it fails for "
           "multiplication. For octonions it gives nothing and on p.104 "
           "declines to go past rank 4. Keyword absence here is an OCR index, "
           "so it is strong rather than absolute evidence."),

    R("23112560", "[2]",
      cite="Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). "
           "Physics-informed neural networks. J. Comput. Phys. 378, 686-707.",
      link="gloss", verdict="NO SUPPORT", access="full-text",
      claim="'Foundational basis for encoding physical laws into neural "
            "weights for the convergence phase.'",
      evidence=[
        "The loss MSE_u corresponds to the initial and boundary data while "
        "MSE_f enforces the structure imposed by equation (A.1) at a finite "
        "set of collocation points",
        "the term in MSE_f ... acts as a regularization mechanism that "
        "penalizes solutions that do not satisfy equation (3)",
        "the resulting pair u(t,x;W,b) and f(t,x;W,b) must satisfy the Burgers "
        "equation regardless of the choice of the weights W and bias b "
        "parameters.",
        "our approximation will conserve mass and momentum within the accuracy "
        "of the residual loss ... the only numerical methods that are known to "
        "have exact conservation properties in this setting are discontinuous "
        "Galerkin and finite volumes.",
        "Such neural networks are constrained to respect any symmetries, "
        "invariances, or conservation principles originating from the physical "
        "laws that govern the observed data.",
      ],
      counts={"symplectic": 0},
      source="DOI 10.1016/j.jcp.2018.10.045, arXiv:1711.10561",
      note="The gloss is contradicted by the paper in the paper's own words: "
           "the physics lives in the loss function and in automatic "
           "differentiation with respect to the input coordinates, and holds "
           "REGARDLESS of the weights. The last quotation is the strongest "
           "pro-conservation sentence available anywhere in this corpus, but "
           "it is about the PINN construction, not about sigma(W.S + b), and "
           "the authors bound it to the residual accuracy in the next "
           "paragraph."),

    R("23112560", "[3]",
      cite="Markidis, S., et al. (2018). NVIDIA tensor core programmability, "
           "performance & precision. IPDPSW 522-531.",
      link="gloss", verdict="PARTIAL", access="full-text",
      claim="'Validation of hardware throughput for MMA instructions applied "
            "to non-ML physical computations.'",
      evidence=[
        "We achieved maximum performance of 83 Tflops/s on NVIDIA Tensor Cores "
        "for N = 8,192 using cuBLAS GEMM ... approximately 74% the theoretical "
        "performance",
        "In the future we will focus on testing Tensor Cores in real-world HPC "
        "applications, such as Nek5000 or Fast Multipole Method-accelerated "
        "FFT.",
        "The use of mixed precision calculations might cause large rounding "
        "errors, affecting simulation accuracy.",
        "by increasing the matrix size N, rounding error increases ... So, the "
        "error scales quadratically with N.",
        "when using half precision, we have only 1,024 values for each power "
        "[of two] ... there is only an accuracy of +/-32 between 32,768 and "
        "65,536",
        "a more in-depth study of the impact of mixed precision calculation on "
        "the overall simulation accuracy in large HPC applications is required",
        "CUDA 9 allows us to program a basic matrix-multiply-and-accumulate on "
        "16x16 matrices",
      ],
      counts={"real-time": 0},
      source="DOI 10.1109/IPDPSW.2018.00091, arXiv:1803.04014",
      note="Throughput is real and measured. The 'applied to non-ML physical "
           "computations' half of the gloss is not: the paper benchmarks "
           "synthetic GEMM and batched GEMM only and says so. It also carries "
           "warnings the gloss omits, which matter because the preprint claims "
           "absolute real-time physics: error growing as N^2, +/-32 resolution "
           "in the upper half-precision range, and a call for further study "
           "before HPC adoption. WMMA granularity is 16x16, so neither 12x12 "
           "nor 112x112 is a native tile. 'Real-time' never appears."),

    R("23112560", "[4]",
      cite="Mildenhall, B., et al. (2020). NeRF: Representing Scenes as Neural "
           "Radiance Fields for View Synthesis. ECCV.",
      link="gloss", verdict="PARTIAL", access="full-text",
      claim="'Theoretical predecessor for the volumetric Raymarching "
            "projection phase without polygon geometry.'",
      evidence=[
        "from a particular viewpoint we: 1) march camera rays through the "
        "scene to generate a sampled set of 3D points, 2) use those points ... "
        "as input to the neural network to produce an output set of colors and "
        "densities, and 3) use classical volume rendering techniques to "
        "accumulate those colors and densities into a 2D image.",
        "our real scenes require 762k rays per image, resulting in between 150 "
        "and 200 million network queries per rendered image. On an NVIDIA "
        "V100, this takes approximately 30 seconds per frame.",
        "around 100-300k iterations to converge on a single NVIDIA V100 GPU "
        "(about 1-2 days).",
      ],
      source="arXiv:2003.08934, DOI 10.1007/978-3-030-58452-8_24",
      note="The descriptive half of the gloss is accurate: NeRF really is "
           "polygon-free ray marching, and this is the one gloss in the "
           "deposit that is factually in order. What it omits is that the work "
           "cited as a predecessor for absolute real-time runs at about 0.03 "
           "frames per second. 'Theoretical predecessor' is also loose, as "
           "NeRF offers an empirical method rather than a theory."),

    R("23112560", "[5]",
      cite="Baez, J. C. (2002). The Octonions. Bull. AMS 39(2), 145-205.",
      link="gloss", verdict="NO SUPPORT", access="full-text",
      claim="'Underlying Lie algebra and gauge group symmetries corresponding "
            "to the 12D/112D spatial mappings.'",
      evidence=[
        "Left multiplication by any element a in K gives an operator "
        "L_a : K -> K, x -> ax. ... for any orthogonal transformation, we can "
        "find some orthonormal basis in which its matrix is block diagonal, "
        "built from 2 x 2 blocks ... We thus obtain a representation of the "
        "Clifford algebra Cliff(Im(K)) on K. Any n-dimensional normed division "
        "algebra thus gives an n-dimensional representation of Cliff(n - 1).",
        "we define sl(m, K) to be the Lie algebra of operators on K^m "
        "generated by operators of this form. ... Note that multiplication in "
        "this group is given by composition of real-linear operators, which is "
        "associative even for K = O.",
        "Note that the numbers 9, 10, 12 and 16 are 8 more than the dimensions "
        "of R, C, H and O. As usual, this is no coincidence!",
        "equip this space with a symplectic structure omega: F x F -> R",
      ],
      counts={"112": 0, "12-dimensional": 0, "12 dimensional": 0},
      source="arXiv:math/0105155",
      note="The gloss fails: '112' and '12-dimensional' do not occur in Baez "
           "at all. But this row carries the two best hidden defences found "
           "anywhere in the corpus, and they are in the author's favour. "
           "First, Baez's L_a construction does give real 8x8 matrices for the "
           "octonions and he derives a Clifford representation from it, so the "
           "WEAK form of 'octonion multiplication encoded by real block "
           "matrices' is supported -- while the strong form, an algebra "
           "isomorphism, is excluded, since L_a o L_b != L_{ab}. Second, "
           "sl(3,H) acts on H^3 ~ R^12 as real 12x12 operators and Baez's "
           "magic square carries so(12) at (H,H), with his own 'this is no "
           "coincidence' about the number 12. That is a better derivation of "
           "12 than either of the two the preprint gives, and the preprint "
           "never points at it. A weaker candidate for 112 also exists: 2 x 56 "
           "through the 56-dimensional Freudenthal space for E7, which Baez "
           "does equip with a symplectic structure -- though he never writes "
           "112, and that symplectic form is a bilinear form preserved by "
           "E7(-25), not a property of an update step."),

    # =====================================================================
    # 23156927  Cymatic -- existence checked in the cymatic-eval repository;
    # only the band question was audited for content
    # =====================================================================
    R("23156927", "Hassanien",
      cite="Hassanien et al. (2014), the review the preprint cites for a "
           "plant acoustic frequency technology sensitive band",
      link="none", verdict="REFUTES", access="abstract",
      claim="(the preprint states the sensitive band is 'typically between 50 "
            "and 120 Hz' and divides 246.91 Hz by four to land 61.72 Hz "
            "'perfectly within the empirically proven PAFT sensitive band')",
      evidence=[
        "the band given by the cited review is 0.1-1 kHz",
      ],
      source="measured in the cymatic-eval repository, frequency.py",
      note="246.91 Hz is already inside the cited band and 61.72 Hz is outside "
           "it, so the division by four moves the frequency out of the band it "
           "is said to land in. This shows the paper's own citation does not "
           "support 61.72 Hz; it does not show the frequency is biologically "
           "ineffective. The other four references of this deposit were "
           "checked for existence rather than content: four resolve exactly "
           "and one (Meng et al. 2012, 'Acoustics Research' 18(1) 45-53) could "
           "not be located."),

    # =====================================================================
    # 23174932  Phytomining -- all six glossed
    # =====================================================================
    R("23174932", "1",
      cite="Buchachenko, A. L. (2009). Magnetic Isotope Effect in Chemistry "
           "and Biology. Nova Science Publishers.",
      resolves="the real title is '...in Chemistry and BIOCHEMISTRY' "
               "(WorldCat OCLC 847652591)",
      link="gloss", verdict="REFUTES", access="author-summary",
      claim="'Establishes the fundamental physics of the Magnetic Isotope "
            "Effect, particularly concerning Magnesium-25 and Zinc-67 in "
            "enzymatic reactions and ATP synthesis.'  The preprint's body "
            "claims 25Mg and 67Zn 'accelerate the chemical kinetics of DNA "
            "transcription and ATP synthesis'.",
      evidence=[
        "In the Earth field the rate of ATP synthesis by enzyme, in which Mg2+ "
        "ion has magnetic nucleus 25Mg, is 2.5 times higher than that by "
        "enzymes, in which Mg2+ ion has nonmagnetic, spinless nuclei 24Mg or "
        "26Mg.",
        "The substitution of these catalyzing ions in polymerases by the ions "
        "25Mg2+, 43Ca2+, and 67Zn2+ with magnetic nuclei was shown to produce "
        "a huge isotope effects: nuclear magnetic ions by 3-5 times suppress "
        "DNA synthesis with respect to those with nonmagnetic ions.",
        "First, the radical pair mechanism is destructive, it suppresses DNA "
        "synthesis",
        "A new anti-cancer strategy is suggested based on the using of the "
        "nuclear magnetic ions of magnesium, calcium, and zinc as a powerful "
        "and universal means to selectively kill only cancer cells.",
        "in the presence of 25Mg2+ ions the rate of repair is by 1.5 times "
        "lower than in the presence of 24Mg2+ ions.",
        "No increase was observed between the rates of ATP production with "
        "natural Mg, (24)Mg, and (25)Mg ... they challenge these authors' "
        "general claims",
      ],
      source="The book itself could not be read (Nova 404, no Google Books). "
             "Quotations are from Buchachenko's own primary papers: JACS 130, "
             "12868 (2008); PNAS 102, 10793 (2005); Russ. J. Phys. Chem. B "
             "2021 (PMC8064421). The replication failure is Crotty et al., "
             "PNAS 109(5), 1437 (2012), PMC3277194",
      note="The direction is inverted. For exactly the trio of isotopes the "
           "preprint names, the cited author's result is 3-5x SUPPRESSION of "
           "DNA synthesis, 1.5x slower repair, and the proposed application is "
           "a cytostatic to kill cells. Only the ATP claim is supported, and "
           "only for 25Mg, only at 99.9% enrichment, delivered by an "
           "injectable nanoparticle rather than by soil, and it failed "
           "replication in PNAS in 2012 -- which the preprint does not cite. "
           "The 67Zn half of the gloss is an anachronism: Buchachenko's "
           "biological zinc MIE work is 2013, four years after this book."),

    R("23174932", "2",
      cite="Cotruvo, J. A. (2019). The Chemistry of Lanthanides in Biology. "
           "ACS Central Science 5(9), 1496-1506.",
      link="gloss", verdict="PARTIAL", access="full-text",
      claim="'Details the discovery of XoxF methanol dehydrogenases in "
            "Methylobacterium and their absolute biological dependence on "
            "lanthanide elements.'  The preprint's body claims 138La, "
            "'substituting calcium in neural synapses', makes synapses "
            "'exhibit quantum coherence and extreme acceleration of cognitive "
            "transmission'.",
      evidence=[
        "A specific biological role of lanthanides was first demonstrated in "
        "2011 with genetic and biochemical characterization of XoxF as a "
        "lanthanide- and PQQ-dependent methanol dehydrogenase (Ln-MDH) in "
        "several methylotrophs, including Methylorubrum (formerly "
        "Methylobacterium) extorquens AM1.",
        "Whereas lanthanides were preferred but not required for growth of the "
        "methylotrophs in which XoxFs were first characterized, elegant work "
        "... identified the first organism with an absolute requirement for "
        "lanthanides for growth - a novel thermoacidophilic methanotroph, "
        "Methylacidiphilum fumariolicum SolV",
        "However, REs are not perfect mimics of Ca, as recent studies of "
        "calmodulin and cadherin have shown, suggesting that REs may not play "
        "a general role as Ca substitutes in Ca-dependent proteins.",
        "at the moment, no specific mechanism for the effects of REs in "
        "organisms other than bacteria has been firmly established.",
        "Studies have suggested positive impacts of RE provision in animal "
        "husbandry, suggesting a role for REs in higher organisms.",
        "plants seem to accumulate REs in proportion to their concentrations "
        "in the soil, suggesting that much of the accumulation occurs "
        "nonspecifically",
      ],
      counts={"neuron": 0, "synapse": 0, "brain": 0, "nuclear spin": 0,
              "quantum": 0, "coherence": 0, "aging": 0, "longevity": 0,
              "toxic": 0},
      source="DOI 10.1021/acscentsci.9b00642, PMC6764073",
      note="The 'absolute' in the gloss belongs to a different organism, a "
           "thermoacidophilic methanotroph from a volcanic mudpot, not to the "
           "Methylobacterium the preprint inoculates. For the synapse claim "
           "there is no carrier at all, and the review specifically doubts the "
           "calcium substitution the mechanism rests on. The animal-husbandry "
           "sentence is the strongest single sentence in the corpus for the "
           "idea, and Cotruvo dismantles it in the next two."),

    R("23174932", "3",
      cite="Lehmann, J., et al. (2011). Biochar effects on soil biota - A "
           "review. Soil Biology and Biochemistry 43(9), 1812-1836.",
      link="gloss", verdict="PARTIAL", access="full-text",
      claim="'Analyzes the extreme porosity, cation exchange capacity / CEC, "
            "and microbial habitation capabilities of biochar.'  The "
            "preprint's body says biochar 'provides massive cation exchange "
            "capacity (CEC)'.",
      evidence=[
        "biochar particles have large internal surface areas and pores that "
        "may be important for biological processes. ... Biochar 'aggregates' "
        "may provide similar functions such as protection of organic matter, "
        "habitat for soil biota, or retention of soil moisture and nutrients.",
        "Fresh biochars can have net positive or net negative surface charge, "
        "but typically have initially low cation exchange capacities (CEC) "
        "compared to soil organic matter on a mass basis. ... greater pyrolysis "
        "temperatures cause a decrease in CEC.",
        "No quantitative evidence is currently available for microbial "
        "protection in biochar pores",
        "the greater the mineralizable fraction of biochar ... the greater the "
        "N immobilization with resultant decreases in N uptake and growth of "
        "crops.",
        "direct negative effects from high contents of mineral elements or "
        "organic compounds detrimental to the fungi, such as high salt or "
        "heavy metal contents.",
        "as inoculant carriers",
      ],
      source="DOI 10.1016/j.soilbio.2011.04.022",
      note="Porosity and habitat are supported; 'massive CEC' is contradicted "
           "by 'initially low'. The review also reports effects the preprint's "
           "one-directional use omits: nitrogen immobilisation reducing crop "
           "growth, earthworm weight loss, and loss of mycorrhizal fungi where "
           "heavy-metal content is high -- directly relevant to a matrix "
           "loaded with Au, La, V and Se -- with the largest community "
           "divergence at 12 and 30 t/ha, which brackets the preprint's "
           "25 t/ha. HIDDEN DEFENCE, real: 'as inoculant carriers' is genuine "
           "precedent for the smart-pellet concept."),

    R("23174932", "4",
      cite="Reith, F., et al. (2006). Mechanisms of gold biomineralization in "
           "the bacterium Cupriavidus metallidurans. PNAS 103(30), "
           "11188-11193.",
      resolves="Reith, F., Etschmann, B., Grosse, C., et al. (2009), PNAS "
               "106(42), 17757-17762, DOI 10.1073/pnas.0904583106. The "
               "coordinates as printed point at unrelated cardiovascular "
               "genetics",
      link="gloss", verdict="REFUTES", access="full-text",
      claim="'Demonstrates the ability of extremophilic soil bacteria to "
            "biochemically process and precipitate heavy metals, including "
            "gold.'  The preprint's body claims biogenic gold nanoparticles "
            "are 'ultimate scavengers of reactive oxygen species (ROS), "
            "entirely blocking cellular corrosion'.",
      evidence=[
        "the biomineralization of Au nanoparticles in the metallophillic "
        "bacterium Cupriavidus metallidurans CH34 is the result of "
        "Au-regulated gene expression leading to the energy-dependent "
        "reductive precipitation of toxic Au(III)-complexes. ... This process "
        "promotes Au toxicity and C. metallidurans reacts by inducing "
        "oxidative stress and metal resistances gene clusters ... to promote "
        "cellular defense. As a result, Au detoxification is mediated by a "
        "combination of efflux, reduction, and possibly methylation",
        "one major toxic effect of Au(III) on C. metallidurans is the "
        "induction of oxidative stress",
        "the MIC of Au(III) in C. metallidurans CH34 is 2 uM ... and toxic "
        "effects to the organism start at ~1/1,000 of the MIC",
        "cells actively removed Au from the cytoplasm",
        "microbial activity led to a doubling of Au concentrations in "
        "solution",
      ],
      source="DOI 10.1073/pnas.0904583106, PMC2764933",
      note="A double inversion. The cell pumps gold OUT to survive it, where "
           "the preprint needs bacteria to mobilise gold INTO the plant; and "
           "gold INDUCES oxidative stress, where the preprint has it blocking "
           "ROS entirely. 'Extremophilic' is also wrong: the authors call it "
           "metallophilic. The one sentence that comes closest to support, a "
           "doubling of gold in solution through microbial activity, continues "
           "'leading to highly toxic microenvironment'."),

    R("23174932", "5",
      cite="Sheoran, V., Sheoran, A. S., & Poonia, P. (2009). Phytomining: A "
           "review. Minerals Engineering 22(12), 1007-1019.",
      link="gloss", verdict="REFUTES", access="abstract",
      claim="'Provides the basis for using plant roots and associated "
            "rhizosphere bacteria to extract specific metals from soil "
            "deposits.'",
      evidence=[
        "It is a recent more advanced technology of phytoremediation to "
        "produce low volume, sulphide-free 'bio-ore', which can either be "
        "safely disposed of or, if the target metal is of sufficient economic "
        "value, smelted, and recovered. This technology has potential "
        "application in the mineral industry to return an economic profit by "
        "commercial production of metals via cropping.",
      ],
      source="DOI 10.1016/j.mineng.2009.04.001. Confirmed closed access "
             "(Unpaywall oa_status 'closed', no repository copy), so only the "
             "publisher abstract was available",
      note="The material flow is inverted. Phytomining REMOVES metal from "
             "soil, harvests it as bio-ore and smelts it; the preprint cites "
             "it as the basis for DELIVERING Au, La and V into edible biomass "
             "and keeping them in the system. 'Rhizosphere bacteria' cannot be "
             "confirmed from the abstract. METHOD NOTE: while searching for "
             "this text, a web-search summariser repeatedly produced "
             "'findings from Sheoran' -- named species and specific numbers -- "
             "that are not in the paper and were mixed in from other articles "
             "in the result set. They were discarded rather than used."),

    R("23174932", "6",
      cite="Wright, S. F., & Upadhyaya, A. (1998). A survey of soils for "
           "aggregate stability and glomalin, a glycoprotein produced by "
           "hyphae of arbuscular mycorrhizal fungi. Plant and Soil 198(1), "
           "97-107.",
      link="gloss", verdict="NO SUPPORT", access="abstract",
      claim="'Explains the mechanics of glomalin production and its role in "
            "maintaining permanent soil structure and water retention.'",
      evidence=[
        "Recent discoveries of copious production of glycoprotein (glomalin) "
        "by arbuscular mycorrhizal (AM) fungi and the apparent recalcitrance "
        "of this material in soils led to the comparison between concentration "
        "of glomalin and aggregate stability.",
        "AS = 42.7 + 61.3 x log10 IREEG (r2 = 0.86; p < 0.001, n = 37)",
        "air-dried aggregates rewetted by capillary action and then subjected "
        "to wet sieving for 10 min",
      ],
      counts={"water retention": 0, "water-holding capacity": 0,
              "permanent": 0},
      source="DOI 10.1023/A:1004347701584. Confirmed closed access, so only "
             "the abstract was available",
      note="Three mismatches. It is a cross-sectional survey of 37 samples "
           "whose output is one regression, so production is its premise "
           "rather than its subject -- no mechanism, no rate, no turnover "
           "time. Water appears only as the destructive agent in wet sieving, "
           "never as retention. 'Permanent' does not occur. The citation is "
           "also functionally orphaned: the preprint's body never mentions "
           "glomalin or mycorrhiza except to bypass them -- 'The plant root "
           "must not search for distant deposits via fungi'."),

    # =====================================================================
    # 23186884  Na-ion HFRS
    # =====================================================================
    R("23186884", "1",
      cite="Tarascon, J.-M., & Armand, M. (2001). Issues and challenges facing "
           "rechargeable lithium batteries. Nature 414(6862), 359-367.",
      resolves="Nature 414(6861), 359-367 -- the issue number is wrong",
      link="none", verdict="PARTIAL", access="metadata",
      source="DOI 10.1038/35104644, confirmed via Crossref",
      note="A general review, correctly attached to nothing in particular."),

    R("23186884", "2",
      cite="Macdonald, J. R. (2005). Impedance Spectroscopy: Theory, "
           "Experiment, and Applications. Wiley-Interscience.",
      resolves="Barsoukov, E. & Macdonald, J. R. (eds.) (2005), 2nd edition. "
               "Macdonald alone edited the 1st edition (1987), which has a "
               "different title: 'Impedance Spectroscopy: Emphasizing Solid "
               "Materials and Systems'",
      link="none", verdict="PARTIAL", access="metadata",
      source="DOI 10.1002/0471716243, ISBN 0-471-64749-7",
      note="The citation mixes the first edition's authorship with the second "
           "edition's year and title."),

    R("23186884", "3",
      cite="Jones, E. A., et al. (2016). Review of Commercial GaN Power "
           "Devices and GaN-Based Converter Design Challenges. IEEE JESTPE "
           "4(3), 707-719.",
      link="none", verdict="SUPPORTS", access="metadata",
      source="DOI 10.1109/JESTPE.2016.2582685",
      note="Resolves exactly and supports the choice of a GaN power stage."),

    R("23186884", "4",
      cite="Purushothaman, B. K., & Landau, U. (2006). Rapid Charging of "
           "Lithium-Ion Batteries Using Pulsed Currents. J. Electrochem. Soc. "
           "153(3), A533.",
      link="none", verdict="REFUTES", access="abstract",
      claim="(the preprint's F_micro is a 'high-frequency fractal modulation "
            "(kHz to MHz range)' said to 'induce phonon-assisted tunneling and "
            "lower activation barriers')",
      evidence=[
        "Modeling the lithium diffusion into a homogeneous intercalant layer "
        "indicates that the lithium concentration reaches saturation at the "
        "graphite/electrolyte interface after about 1 h under conventional "
        "constant current charging, mandating the shift to the lower rate "
        "constant voltage charging. It is shown here that charging the lithium "
        "battery using non-dc waveforms with properly selected parameters may "
        "circumvent this lithium saturation",
        "A nonlinearly decreasing current density profile which conforms to "
        "the mass transfer coefficient variation was shown to provide complete "
        "charging in less than 3/4 of an hour, faster than any other "
        "pulse-charging profile studied.",
      ],
      source="DOI 10.1149/1.2161580",
      note="The preprint's only pulsed-charging citation identifies the "
           "limiting mechanism as solid-state diffusion, works at a 3 s pulse "
           "with 1 s rest -- about 0.25 Hz -- and finds its best result with a "
           "CONTINUOUS decreasing-current profile rather than any pulse. It "
           "supports the low-frequency macroscopic envelope and contradicts "
           "the kHz-to-MHz component. It identifies no beneficial kHz band."),

    R("23186884", "5",
      cite="Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. "
           "Proceedings of ICNN'95.",
      link="none", verdict="SUPPORTS", access="metadata",
      source="DOI 10.1109/ICNN.1995.488968",
      note="Resolves exactly; volume and pages are omitted but nothing is "
           "wrong."),

    # =====================================================================
    # 23209266  Hemocyanin -- four glossed plus one self-citation
    # =====================================================================
    R("23209266", "1",
      cite="Decker, H., et al. (2007). Structure and function of hemocyanins. "
           "In: Hemocyanins and Invertebrate Evolution. J. Biol. Chem.",
      resolves="Does not exist as printed. The venue maps to van Holde, K. E., "
               "Miller, K. I. & Decker, H. (2001), 'Hemocyanins and "
               "Invertebrate Evolution', JBC 276(19), 15563-15566, DOI "
               "10.1074/jbc.R100010200; the author and year map to Decker, H., "
               "et al. (2007), 'Minireview: Recent progress in hemocyanin "
               "research', Integr. Comp. Biol. 47(4), 631-644, DOI "
               "10.1093/icb/icm063",
      link="gloss", verdict="REFUTES", access="full-text",
      claim="'Describes the molecular structure, efficiency, and thermodynamic "
            "stability of copper-based respiratory proteins in nature.'",
      evidence=[
        "The oxygen-binding behavior of hemocyanins is usually characterized "
        "by a low to moderate oxygen affinity.",
        "both oxygen affinity and cooperativity are optimized for a certain "
        "temperature range, and the oxygen-transport capacity of hemocyanin is "
        "adapted to the environmental temperature of the animals.",
        "the possession of a blood pigment with an oxygen carrying capacity "
        "that never exceeds 4.5 vols%",
        "a low molecular weight monomeric protein dissolved in the hemolymph "
        "is not efficient for oxygen transport. If its concentration in the "
        "hemolymph is high enough to transport a significant amount of oxygen, "
        "it will yield an unbearably high osmotic pressure.",
      ],
      counts={"hemoglobin": 0, "haemoglobin": 0, "thermodynam": 0,
              "stabilit": 0, "efficient": 0},
      source="Decker et al. 2007 full text from an archival copy of "
             "icb.oxfordjournals.org. The capacity figure is Wells & Smith "
             "1987, DOI 10.1007/BF02143577; the osmotic-pressure explanation "
             "is van Holde, Miller & Decker 2001, DOI 10.1074/jbc.R100010200",
      note="The citation is a chimera of three sources, and neither 'efficiency' "
           "nor 'thermodynamic stability' occurs anywhere in the work it maps "
           "to. The load-bearing number is absent from the preprint and from "
           "all five of its references, so it was obtained independently: "
           "human blood carries about 20 vol% oxygen against 1.37-3.44 vol% "
           "for hemocyanin, never above 4.5 -- 4.5 to 15 times worse. The "
           "physical reason is given by Decker's own co-author."),

    R("23209266", "2",
      cite="Dixon, S. J., & Stockwell, B. R. (2014). The role of iron and "
           "reactive oxygen species in cell death. Nature Chemical Biology "
           "10(1), 9-17.",
      link="gloss", verdict="PARTIAL", access="abstract",
      claim="'Defines iron toxicity, the Fenton reaction, and its fatal impact "
            "on cellular aging and DNA degradation in mammals.'",
      evidence=[
        "Iron and ROS are increasingly recognized as important initiators and "
        "mediators of cell death ... a new form of iron-dependent cell death "
        "termed ferroptosis ... suggest new therapeutic avenues to treat "
        "cancer, organ damage and degenerative disease.",
      ],
      source="DOI 10.1038/nchembio.1416, PMID 24346035. Confirmed closed "
             "access, so the verdict rests on the abstract and the MeSH terms",
      note="Iron toxicity and the Fenton reaction are supported. Aging is not: "
           "the subject is regulated cell death, and the MeSH terms are Cell "
           "Death, Humans, Iron, Reactive Oxygen Species, Signal Transduction "
           "-- no Aging, no Cellular Senescence. Nowhere does it propose "
           "replacing iron as a respiratory metal, and it does not address "
           "copper's own redox toxicity, which is the gap reference 4 fills "
           "against the preprint."),

    R("23209266", "3",
      cite="Hellman, N. E., & Gitlin, J. D. (2002). Ceruloplasmin metabolism "
           "and function. Annual Review of Nutrition 22, 439-458.",
      link="gloss", verdict="REFUTES", access="abstract",
      claim="'Analysis of human copper metabolism and the structural "
            "relationship between human copper proteins and invertebrate "
            "hemocyanins.'  The preprint's body calls ceruloplasmin 'the "
            "fundamental human protein for copper transport in the blood' and "
            "'structurally related to invertebrate hemocyanins'.",
      evidence=[
        "Ceruloplasmin is a serum ferroxidase ... Despite the need for copper "
        "in ceruloplasmin function, this protein plays no essential role in "
        "the transport or metabolism of this metal. ... revealed a critical "
        "physiological role for ceruloplasmin in determining the rate of iron "
        "efflux from cells with mobilizable iron stores",
      ],
      source="DOI 10.1146/annurev.nutr.22.012502.114457, PMID 12055353. Closed "
             "access; the verdict rests on the abstract plus all 112 entries "
             "of its reference list, retrieved from OpenAlex. Domain "
             "assignments are from InterPro and Pfam queries",
      note="The preprint's only concrete molecular bridge between humans and "
           "hemocyanin is denied by the cited abstract in so many words: "
           "ceruloplasmin is an iron-handling enzyme. 28 of its 112 references "
           "concern iron and none concern hemocyanin; its structural "
           "comparisons go to ascorbate oxidase, laccase, Fet3p and "
           "hephaestin. The databases agree: ceruloplasmin is a multicopper "
           "oxidase with a cupredoxin fold, hemocyanins carry a tyrosinase "
           "binuclear type-3 copper centre, and the domain intersection is "
           "empty. The review does cover copper toxicity (Wilson's disease, "
           "Menkes), which the preprint does not."),

    R("23209266", "4",
      cite="Tchounwou, P. B., et al. (2012). Heavy metal toxicity and the "
           "environment. Experientia Supplementum 101, 133-164.",
      link="gloss", verdict="REFUTES", access="full-text",
      claim="'Provides a baseline framework for understanding the epigenetic "
            "adaptation of organisms to extreme environmental metal "
            "concentrations.'  The preprint claims 'absolute resistance to "
            "oxidative stress (absence of the Fenton reaction)' for copper.",
      evidence=[
        "systemic toxicants that are known to induce multiple organ damage.",
        "the ability of copper to cycle between an oxidized state, Cu(II), and "
        "reduced state, Cu(I), is used by cuproenzymes involved in redox "
        "reactions. However, it is this property of copper that also makes it "
        "potentially toxic because the transitions between Cu(II) and Cu(I) "
        "can result in the generation of superoxide and hydroxyl radicals. "
        "Also, excessive exposure to copper has been linked to cellular damage "
        "leading to Wilson disease in humans.",
      ],
      counts={"epigenet": 0},
      source="DOI 10.1007/978-3-7643-8340-4_6, PMC4144270, 111891 characters",
      note="'Epigenetic' does not occur once, so the gloss describes something "
           "the work does not contain; its frame is toxicological. And it "
           "attributes hydroxyl radical generation to copper -- the same "
           "radical for which the preprint rejects iron."),

    R("23209266", "5",
      cite="Mazgal, M. (2026). Quantum Biofortification and In-Situ "
           "Phytomining. Independent Preprint.",
      link="gloss", verdict="NO SUPPORT", access="full-text",
      claim="'The author's preceding theoretical model defining the physical "
            "and agricultural mechanism for delivering biogenic copper and "
            "quantum isotopes into the hominid food chain.'",
      evidence=[
        "Gold (Au) and Copper (Cu): Biogenic gold nanoparticles act as "
        "ultimate scavengers of reactive oxygen species (ROS), entirely "
        "blocking cellular corrosion and inflammatory processes.",
        "Matrix & Macro-Metals: 745 tons (biochar, bentonite, dolomite, "
        "zeolite, Fe, S)",
        "Quantum Micro-Elements: 1 ton of Lanthanum oxide, 3 tons of trace "
        "elements (Zn, V, Mo, B, Se)",
      ],
      counts={"copper": 1, "hemocyanin": 0, "hemoglobin": 0,
              "oxygen transport": 0, "respirat": 0, "epigenet": 0,
              "Fenton": 0},
      source="Zenodo 23174932, DOI 10.5281/zenodo.23174932",
      note="A self-citation to a mechanism that is not in the cited document. "
           "'Copper' occurs once, in a bullet heading whose body is entirely "
           "about gold, and copper appears in no line of the material budget "
           "-- whereas iron does. So the predecessor paper delivers the very "
           "metal this paper calls autotoxic, and does not deliver copper at "
           "all. No uptake mechanism, no concentration, no bioavailability, no "
           "target tissue."),

    # =====================================================================
    # 23241148  openQL v1.1 -- the same five references as v1.0 with every
    # gloss removed, so no reference is linked to any claim any more
    # =====================================================================
    R("23241148", "[1]-[5]",
      cite="Kuipers 1999; Raissi et al. 2019; Markidis et al. 2018; "
           "Mildenhall et al. 2020; Baez 2002",
      link="none", verdict="NO SUPPORT", access="full-text",
      source="see the 23112560 rows for the per-reference verdicts",
      note="Version 1.1 keeps the same five references and deletes all five "
           "glosses, so the verdicts carry over but the link to any claim does "
           "not. Also deleted in v1.1 are four claims this evaluation measured "
           "in the openql-eval repository: the derivation sentence for 112, "
           "'keeps Tensor Core load in the efficient 15-20% range', 'the "
           "memory footprint of a single node reaches tens of kilobytes', and "
           "'without requiring floating-point correction loops'. The "
           "coincidence is recorded; causation is not claimed. The ORCID "
           "placeholder in the PDF header is still unfilled and is now in "
           "Czech."),

    # =====================================================================
    # 23241777  Intensional Physics Computing
    # =====================================================================
    R("23241777", "[1]",
      cite="Fitting, M. (2015). Intensional Logic. The Stanford Encyclopedia "
           "of Philosophy.",
      link="none", verdict="NO SUPPORT", access="full-text",
      evidence=[
        "The expression '1 + 4' is a kind of miniature computing program ... We "
        "might identify the program with the sense, and the output with the "
        "denotation. ... Identifying the intension of a mathematical term with "
        "its computational content is a plausible thing to do.",
        "Moschovakis is not claiming to turn sense and reference into "
        "something computable, but simply to provide mathematical machinery "
        "that can plausibly formalize the ideas involved using a generalized "
        "notion of algorithm",
        "In part, Bressan wanted to provide a logical foundation for physics.",
      ],
      counts={"tensor": 0, "GPU": 0, "matrix": 0, "quantum": 0},
      source="plato.stanford.edu/entries/logic-intensional/",
      note="Two real hooks, both terminological rather than technical: sense "
           "as computational content, and Bressan's logical foundation for "
           "physics. Both are undercut in the same article, which notes "
           "Moschovakis is not claiming computability and whose section 4.5 is "
           "titled 'Algorithms Need Not Be Effective'. For an argument about "
           "GPU execution that is worse than neutral. No numerical "
           "simulation, no hardware, no fields."),

    R("23241777", "[2]-[5]",
      cite="Raissi et al. 2019; Markidis et al. 2018; Mildenhall et al. 2020; "
           "Kuipers 1999",
      link="none", verdict="NO SUPPORT", access="full-text",
      source="see the 23112560 rows for the per-reference verdicts",
      note="Four of the five references are shared with openQL, carried over "
           "without the glosses. This deposit strengthens one claim relative "
           "to openQL: its Sec. 3 calls sigma(W_PINN (x) S(t) + b) 'a "
           "symplectic discrete Hamiltonian operator', where openQL said only "
           "that it preserves Lie group symmetries. 'Symplectic' occurs in "
           "none of the five references -- in this corpus the word appears "
           "only in Baez, about the Freudenthal space for E7. The claim was "
           "already measured in openql-eval/symplectic.py: with sigma = tanh "
           "the harmonic oscillator drifts to 2e-5 x E(0) over 1e5 steps and a "
           "fitted pendulum reaches 10.2 x E(0), while leapfrog holds "
           "1.0000 x E(0) untrained."),
]
