#!/usr/bin/env python3
"""openQL v1.0 -> v1.1: what changed, recorded.

Four of the six things the revision removes are claims the openql-eval
repository measured.  That coincidence is worth recording precisely, and worth
recording without a causal claim attached, because this repository has no way to
establish one: the revision carries no changelog and gives no reason for any
edit.

This script is a record, not a computation.  It is kept as a script so the list
appears in results.log beside the arithmetic rather than only in prose.
"""
from constants import (V10_CALLED_IT, V10_ORCID_PLACEHOLDER, V11_ADDED,
                       V11_ORCID_PLACEHOLDER, V11_REMOVED, tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()
P("      v1.0 is DOI 10.5281/zenodo.23112560, 3 October 2026.")
P("      v1.1 is DOI 10.5281/zenodo.23241148, 8 October 2026.")
P("      Both are reproduced by fetch.sh in the reference-audit repository.")
P()

P("1. Removed in v1.1")
P()
measured = 0
for label, quote, was_measured in V11_REMOVED:
    mark = "  <- measured in openql-eval" if was_measured else ""
    measured += 1 if was_measured else 0
    P(f"      - {label}{mark}")
    if quote:
        # wrap the quotation at a readable width
        words, line = quote.split(), "          \""
        for w in words:
            if len(line) + len(w) > 76:
                P(line)
                line = "           " + w
            else:
                line += (" " if line.strip() != '"' else "") + w
        P(line + "\"")
    P()
P(f"      {measured} of {len(V11_REMOVED)} removals are claims that openql-eval")
P("      measured and reported.  No causal claim is made: the revision has no")
P("      changelog, and the coincidence is the whole of the evidence.")

P()
P("2. Added in v1.1")
P()
for item in V11_ADDED:
    P(f"      + {item}")

P()
P("3. Unchanged in v1.1")
P()
P(f"      the update rule:  S(t+1) = sigma(W_PINN (x) S(t) + b)")
P(f"        v1.0 said it \"{V10_CALLED_IT}\"")
P("        v1.1 keeps the same wording; the companion IPC paper of the same")
P("        day strengthens it to \"a symplectic discrete Hamiltonian")
P("        operator\" -- see queries.py Sec. 5")
P()
P(f"      the ORCID placeholder in the PDF header, still unfilled:")
P(f"        v1.0  Author: Michal Mazgal {V10_ORCID_PLACEHOLDER}")
P(f"        v1.1  Author: Michal Mazgal {V11_ORCID_PLACEHOLDER}")
P()
P("      The placeholder was not filled in; it was regenerated in Czech.  The")
P("      author's real ORCID has been attached to the Zenodo record metadata")
P("      since 3 October, so the identifier exists and only the PDF template")
P("      is stale.")
P()
P("      Also unchanged: the abstract still says the architecture works \"By")
P("      transforming quaternion and octonion algebra into unified block")
P("      matrices\", while \"octonions\" has been dropped from the keywords.")
P("      The octonion half of that sentence is the one excluded by a theorem,")
P("      measured in openql-eval/octonion.py, and it is still in the abstract.")

P()
P("4. What the two deposits of 8 October are, relative to v1.0")
P()
P("      IPC (23241777) is openQL's Sec. 2, Sec. 4 and part of Sec. 5 restated")
P("      as a standalone paper, with four of its five references shared with")
P("      openQL and the fifth being Fitting's Stanford Encyclopedia entry on")
P("      intensional logic.  It contains no new architecture.  What is new is")
P("      the word 'symplectic' and the queries-per-millisecond figure, both")
P("      measured in queries.py.")
P()
P("      v1.1 (23241148) is v1.0 with the six removals above, the three")
P("      additions, and Sec. 6.1, which is the only substantively new section")
P("      in either deposit.  It is measured in bldc.py.")
P()
P("      One internal inconsistency between them is worth noting: openQL puts")
P("      12 dimensions in a 12x12 node built from three concatenated 4x4")
P("      quaternion blocks, while IPC Sec. 3 says the node is \"a 4x4 (for 12D")
P("      macroscopic physics)\" matrix -- 16 slots for 12 numbers, in a")
P("      different arrangement from the one openQL specifies for the same")
P("      layer.")
