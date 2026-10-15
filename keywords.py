#!/usr/bin/env python3
"""Re-derive the citation-marker counts in carrier.py from the deposits
themselves, and run the vocabulary census across the corpus.

    ./fetch.sh corpus && python3 keywords.py corpus

Without a corpus directory this prints the values recorded when the audit was
run, marked as recorded rather than measured, so run_all.sh works offline.  With
one, every number is recomputed from the extracted text and compared against
the recorded value; any disagreement is flagged.
"""
import os
import re
import sys

P = print

# Recorded when the audit was run, 9 October 2026, and for the last two rows
# when they were added on 15 October 2026.  Each entry is
# (record, short name, external refs, in-text markers on external refs,
#  glosses, first line of the reference list in the extracted text).
RECORDED = [
    ("22876757", "acoustic-projector",  6, 5, 0, 204),
    ("22877345", "x-ternary",           5, 0, 0, 137),
    ("22877912", "mppt-v1.0",           0, 0, 0, None),
    ("22914238", "mppt-v1.1",           0, 0, 0, None),
    ("22923154", "cobar",               5, 0, 0,  99),
    ("22934058", "momentum-drive",      8, 0, 0, 189),
    ("22959886", "cqft",                0, 0, 0, None),
    ("22962188", "pctp",                5, 0, 0, 216),
    ("22962557", "sotp",                5, 2, 0, 224),
    ("23112560", "openql-v1.0",         5, 0, 5, 140),
    ("23156927", "cymatic",             5, 0, 0, 127),
    ("23174932", "phytomining",         6, 0, 6, 162),
    ("23186884", "na-ion-hfrs",         5, 0, 0, 127),
    ("23209266", "hemocyanin",          4, 0, 4, 122),
    ("23241148", "openql-v1.1",         5, 0, 0, 150),
    ("23241777", "intensional-physics", 5, 0, 0, 111),
    ("23263528", "openomega",            5, 0, 0, 103),
    ("23364732", "hospv",                7, 7, 0, 364),
]

# The vocabulary census this project has tracked across the series.  "causal"
# is the one that moved: it is zero for the first time in openQL / openOL v1.0
# of 3 October and stays zero in the seven deposits after it.  An earlier version
# of the cymatic-eval repository credited the cymatic deposit of 5 October with
# being first; this census corrected that, and the correction is recorded there.
VOCAB = ["maxwell", "octonion", "quaternion", "hypercomplex", "non-associative",
         "tensor", "causal", "intensional", "quantum", "fractal"]

GLOSS_RE = re.compile(
    r"\((?:Provides|Describes|Defines|Analysis|Validation|Foundational|"
    r"Theoretical|Underlying|Establishes|Details|Analyzes|Demonstrates|"
    r"Explains|The author)")


# Marker numbers that point at the author's own earlier deposits rather than at
# an external work.  SOTP's [1] and [2] are self-citations to CQFT and PCTP, so
# its body cites four markers but only two external references.
SELF_MARKERS = {"sotp": {1, 2}}


def body_markers(text, ref_start_line):
    """[n] markers in the body, i.e. before the reference list begins."""
    body = "\n".join(text.splitlines()[:ref_start_line])
    return re.findall(r"\[\d+(?:,\s*\d+)*\]", body)


def external_cited(text, ref_start_line, short):
    """Distinct reference numbers cited in the body that are not self-citations."""
    nums = set()
    for m in body_markers(text, ref_start_line):
        nums.update(int(n) for n in re.findall(r"\d+", m))
    return nums - SELF_MARKERS.get(short, set())


def main(corpus=None):
    live = bool(corpus and os.path.isdir(corpus))

    P("1. Citation markers in the body text")
    P()
    if not live:
        P("  No corpus directory given, so these are the values recorded when")
        P("  the audit was run, not measured now.  Run ./fetch.sh first to")
        P("  recompute them.")
        P()
        P(f"  {'deposit':22s} {'ext':>4s} {'in-text':>8s} {'gloss':>6s}")
        for _, short, ext, intext, gloss, _ in RECORDED:
            P(f"  {short:22s} {ext:4d} {intext:8d} {gloss:6d}")
    else:
        P(f"  {'deposit':22s} {'markers':>8s} {'self':>5s} {'external':>9s}"
          f"  {'recorded':>9s}  check")
        bad = 0
        for rec, short, ext, intext, gloss, start in RECORDED:
            path = os.path.join(corpus, short + ".txt")
            if not os.path.exists(path):
                P(f"  {short:22s} {'(missing)':>8s}")
                continue
            text = open(path, encoding="utf-8", errors="replace").read()
            if start is None:
                n, nx = len(re.findall(r"\[\d+\]", text)), set()
            else:
                n = len(body_markers(text, start))
                nx = external_cited(text, start, short)
            nself = len(SELF_MARKERS.get(short, set()))
            ok = "ok" if len(nx) == intext else "MISMATCH"
            if ok != "ok":
                bad += 1
            P(f"  {short:22s} {n:8d} {nself:5d} {len(nx):9d}  {intext:9d}  {ok}")
        P()
        P(f"  mismatches: {bad}")
        P("  'markers' counts [n] occurrences in the body, so a repeated marker")
        P("  and a '[3, 4]' pair both show up there; 'external' counts the")
        P("  distinct reference numbers cited that are not self-citations, which")
        P("  is what carrier.py tabulates.  SOTP cites four markers and two")
        P("  external references: [1] and [2] are its own CQFT and PCTP.")
        P("  A mismatch means a deposit on Zenodo has changed since the audit,")
        P("  or that a count here needs correcting.")

    P()
    P("2. Reference-list glosses")
    P()
    if not live:
        P("  recorded: openql-v1.0 5, phytomining 6, hemocyanin 4, rest 0")
    else:
        for rec, short, ext, intext, gloss, start in RECORDED:
            path = os.path.join(corpus, short + ".txt")
            if not os.path.exists(path) or start is None:
                continue
            tail = "\n".join(
                open(path, encoding="utf-8", errors="replace")
                .read().splitlines()[start:])
            n = len(GLOSS_RE.findall(tail))
            mark = "" if n == gloss else "   MISMATCH"
            P(f"  {short:22s} {n:3d}  (recorded {gloss}){mark}")

    P()
    P("3. Vocabulary census across the corpus")
    P()
    if not live:
        P("  Needs the corpus; run ./fetch.sh.  Recorded result: maxwell,")
        P("  octonion, quaternion, hypercomplex, non-associative and causal are")
        P("  all zero in the cymatic, phytomining, na-ion and hemocyanin")
        P("  deposits.  'causal' first reaches zero one deposit earlier than")
        P("  that, in openQL / openOL v1.0 of 3 October, which still carries")
        P("  'Maxwell' twice and 'quaternion' seven times.  The two deposits of")
        P("  8 October reintroduce 'tensor' and 'intensional' but not the")
        P("  hypercomplex vocabulary, except that openQL v1.1 keeps 'octonion'")
        P("  in its abstract while dropping it from its keywords.  openOmega")
        P("  of 9 October brings back 'tensor' 10 times and 'octonion' once")
        P("  with 'causal' still at zero, and HOS-PV 2.0 of 14 October is")
        P("  zero in nine of the ten columns -- its only hit is 'quantum', 9")
        P("  times -- the first deposit without 'tensor' since 7 October.")
        return
    P(f"  {'deposit':22s} " + " ".join(f"{k[:9]:>9s}" for k in VOCAB))
    for rec, short, *_ in RECORDED:
        path = os.path.join(corpus, short + ".txt")
        if not os.path.exists(path):
            continue
        t = open(path, encoding="utf-8", errors="replace").read().lower()
        P(f"  {short:22s} "
          + " ".join(f"{len(re.findall(k, t)):9d}" for k in VOCAB))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
