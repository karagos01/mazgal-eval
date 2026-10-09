#!/usr/bin/env python3
"""The verdicts: for each reference whose link to a claim is stated, does the
cited work say what it is cited for?

Nothing here is a computation.  The verdicts and their evidence live in
refdata.py, each with the verbatim quotation it rests on and a record of how
far the cited work could actually be read.  This script tabulates them and
shows how much of the audit rests on a full text rather than an abstract.
"""
from collections import Counter

from refdata import DEPOSITS, REFS

P = print
SHORT = {r: s for r, s, *_ in DEPOSITS}
ORDER = ["SUPPORTS", "PARTIAL", "NO SUPPORT", "REFUTES", "UNRESOLVED"]
MEANING = {
    "SUPPORTS":   "the cited work says what it is cited for",
    "PARTIAL":    "part of the claim is supported, part is not",
    "NO SUPPORT": "the cited work does not address the claim",
    "REFUTES":    "the cited work states the opposite",
    "UNRESOLVED": "the reference itself could not be located",
}
ACCESS = {
    "full-text":      "full text of the cited work obtained",
    "abstract":       "abstract only; the full text was paywalled or absent",
    "author-summary": "the work itself was unreachable; a summary of it "
                      "written by its own author was used",
    "metadata":       "metadata and contents listing only",
    "none":           "could not be reached at all",
}

P("1. Verdicts, by deposit")
P()
for rec, short, *_ in DEPOSITS:
    rows = [r for r in REFS if r["dep"] == rec]
    if not rows:
        P(f"  {short:22s} -- no reference list")
        continue
    P(f"  {short}  ({rec})")
    for r in rows:
        flag = {"in-text": "^", "gloss": "~", "none": " "}[r["link"]]
        P(f"    {flag} {r['key']:10s} {r['verdict']:<11s} "
          f"[{r['access']:<14s}] {r['cite'][:58]}")
        if r["resolves"]:
            P(f"      -> resolves to: {r['resolves'][:84]}")
    P()
P("  ^ attached to a sentence in the body    ~ carries a gloss in the list")

P()
P("2. Totals")
P()
v = Counter(r["verdict"] for r in REFS)
tot = sum(v.values())
for k in ORDER:
    P(f"  {k:<11s} {v[k]:>3d}  {v[k] / tot:>5.1%}   {MEANING[k]}")
P(f"  {'':11s} {tot:>3d}         rows (some cover several references)")

P()
P("3. How far the cited works could be read")
P()
a = Counter(r["access"] for r in REFS)
for k in ["full-text", "abstract", "author-summary", "metadata", "none"]:
    if a[k]:
        P(f"  {k:<15s} {a[k]:>3d}   {ACCESS[k]}")
P()
P(f"  rows resting on a full text: {a['full-text']}/{tot} "
  f"({a['full-text'] / tot:.0%})")
P("  Every row that does not rest on a full text says so, and its verdict is")
P("  scoped to what the abstract or the contents listing supports.  Where a")
P("  book was unreachable, quotations come from the same author's own papers")
P("  or from their own summary of the book, and the source field says which.")

P()
P("4. Keyword counts, where a full text was obtained")
P()
P("  0 means the term was searched for and is absent, not that it was")
P("  assumed absent.  Counts on an OCR index are strong, not absolute.")
P()
for r in REFS:
    if not r["counts"]:
        continue
    zeros = [k for k, n in r["counts"].items() if n == 0]
    nonzero = {k: n for k, n in r["counts"].items() if n}
    P(f"  {SHORT[r['dep']]:20s} {r['key']:10s} {r['cite'].split('(')[0][:34]}")
    if zeros:
        P(f"      absent: {', '.join(zeros)}")
    if nonzero:
        P(f"      present: "
          + ", ".join(f"{k} x{n}" for k, n in nonzero.items()))

P()
P("5. Citations that do not resolve as printed")
P()
for r in REFS:
    if r["resolves"]:
        P(f"  {SHORT[r['dep']]:20s} {r['key']:10s} {r['cite'][:52]}")
        P(f"      {r['resolves']}")
        P()
unresolved = [r for r in REFS if r["verdict"] == "UNRESOLVED"]
for r in unresolved:
    P(f"  {SHORT[r['dep']]:20s} {r['key']:10s} NOT LOCATED: {r['cite'][:48]}")
    P(f"      {r['source']}")
P()
P("  'Not located' is negative evidence: it means the reference could not be")
P("  found, which is weaker than showing it does not exist.")
