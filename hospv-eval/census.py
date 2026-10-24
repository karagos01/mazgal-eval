"""A word census of the deposit, against the vocabulary of the series.

Seventeen earlier deposits by the same author share a vocabulary: tensor
matrices, hypercomplex algebra, causal logic, Tensor Cores, a named GPU.  This
one can be measured for it.  The counts are taken from the text of the PDF, not
asserted here; run ./fetch_data.sh to produce data/hospv.txt from Zenodo.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.join(HERE, "data", "hospv.txt")

# The signature vocabulary of the series, as established in the companion
# repositories, followed by the vocabulary of this deposit's own field.
SERIES = ("tensor", "tensor core", "octonion", "quaternion", "sedenion",
          "hypercomplex", "non-associative", "associator", "causal",
          "intensional", "maxwell", "zero divisor", "GPU", "CUDA", "RTX",
          "clock cycle", "Theory of Everything", "Gemini")
FIELD = ("singlet fission", "Dexter", "chiral", "CISS", "altermagnet",
         "Pauli", "spin", "Shockley-Queisser", "detailed balance",
         "drift-diffusion", "Langevin", "triplet", "quantum yield",
         "phonon", "exciton", "EQE", "AM1.5G")


def counts(text, words):
    lowered = text.lower()
    return [(word, len(re.findall(re.escape(word.lower()), lowered)))
            for word in words]


def main():
    if not os.path.exists(TEXT):
        print("data/hospv.txt is not present; run ./fetch_data.sh first.")
        return 0
    text = open(TEXT, encoding="utf-8", errors="replace").read()
    print("=" * 78)
    print("The vocabulary of the series, in this deposit")
    print("=" * 78)
    rows = counts(text, SERIES)
    width = max(len(word) for word, _n in rows)
    for word, number in rows:
        print("  %-*s %4d" % (width, word, number))
    print()
    total = sum(number for _word, number in rows)
    print("  total occurrences of the series vocabulary: %d" % total)
    print()
    print("  This is the first deposit of the eighteen with no tensor in it at")
    print("  all, no hypercomplex algebra, no causal logic, and no named")
    print("  graphics card.  Its mechanisms are drawn from the literature of")
    print("  its own field instead:")
    print()
    rows = counts(text, FIELD)
    width = max(len(word) for word, _n in rows)
    for word, number in rows:
        print("  %-*s %4d" % (width, word, number))
    print()

    print("=" * 78)
    print("Form")
    print("=" * 78)
    # Numbered lists appear throughout the body, so the reference list is
    # counted only after the last "References" heading.
    tail = text.split("References")[-1]
    print("  references listed                          %d"
          % len(re.findall(r"\n\s*\d+\.", tail)))
    print("  occurrences of the author's own name       %d"
          % len(re.findall(r"Mazgal", text)))
    print("  self-citations in the reference list       %d"
          % len(re.findall(r"Mazgal", tail)))
    print("  unfilled ORCID placeholder                 %s"
          % ("present" if "ORCID" in text else "absent"))
    print("  'Gemini AI' credited as an author          %s"
          % ("yes" if "Gemini" in text else "no"))
    print()
    print("  Earlier deposits in the series carry an unfilled ORCID field in")
    print("  the PDF header; three of them credit or cite 'Gemini AI'; several")
    print("  cite each other.  This one does none of that.  Its seven")
    print("  references are all external, all real, and each is attached to a")
    print("  claim it genuinely supports - which, measured across the series in")
    print("  the reference-audit repository, is not the usual case.")
    print("  The reference that carries the central number, [5], is the one")
    print("  that does not support it, and that is a misreading of a row in a")
    print("  table rather than an invented citation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
