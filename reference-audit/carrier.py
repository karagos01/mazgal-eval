#!/usr/bin/env python3
"""Is there a carrier for a defence hidden in the references?

The author of these preprints has stated publicly that the defence of his
arguments is deliberately placed in the references rather than written in the
text.  For a reference to defend a claim, the text has to attach it to that
claim.  This script counts, across all 18 Zenodo records, how many external
references have such an attachment at all.

Counts come from the extracted text of each deposit; fetch.sh reproduces the
texts from Zenodo and keywords.py re-derives the citation-marker counts from
them.
"""
from refdata import DEPOSITS, NO_REFERENCES

P = print

P("1. Per deposit")
P()
P(f"  {'record':10s} {'deposit':22s} {'ext':>4s} {'self':>5s} "
  f"{'in-text':>8s} {'gloss':>6s}  carrier for a hidden defence?")
P("  " + "-" * 86)
for rec, short, date, ext, slf, intext, gloss in DEPOSITS:
    if ext == 0:
        carrier = "none -- no reference list at all"
    elif intext:
        carrier = f"yes, {intext} reference(s) attached to a sentence"
    elif gloss:
        carrier = f"partial, {gloss} gloss(es) state what each establishes"
    else:
        carrier = "none -- nothing is attached to anything"
    P(f"  {rec:10s} {short:22s} {ext:4d} {slf:5d} {intext:8d} {gloss:6d}  "
      f"{carrier}")

ext = sum(d[3] for d in DEPOSITS)
slf = sum(d[4] for d in DEPOSITS)
intext = sum(d[5] for d in DEPOSITS)
gloss = sum(d[6] for d in DEPOSITS)
orphan = ext - intext - gloss

P("  " + "-" * 86)
P(f"  {'':10s} {'TOTAL':22s} {ext:4d} {slf:5d} {intext:8d} {gloss:6d}")

P()
P("2. The corpus as a whole")
P()
P(f"  Zenodo records                                      {len(DEPOSITS):>4d}")
P(f"  distinct works (openQL and MPPT each have two versions)  "
  f"{len(DEPOSITS) - 2:>2d}")
P(f"  external reference entries                          {ext:>4d}")
P(f"    attached to a sentence by an in-text marker       {intext:>4d}"
  f"   ({intext / ext:.1%})")
P(f"    carrying only a parenthetical gloss               {gloss:>4d}"
  f"   ({gloss / ext:.1%})")
P(f"    with no stated relation to any claim              {orphan:>4d}"
  f"   ({orphan / ext:.1%})")
P(f"  self-citations                                      {slf:>4d}")

P()
withrefs = [d for d in DEPOSITS if d[3] > 0]
cited = [d for d in withrefs if d[5] > 0]
glossed = [d for d in withrefs if d[6] > 0]
orphaned = [d for d in withrefs if d[5] == 0 and d[6] == 0]

P(f"  deposits with no reference list at all   "
  f"{len(NO_REFERENCES):>2d}   " + ", ".join(
      s for r, s, *_ in DEPOSITS if r in NO_REFERENCES))
P(f"  deposits citing a reference in the body  {len(cited):>2d}   "
  + ", ".join(d[1] for d in cited))
P(f"  deposits glossing every reference        {len(glossed):>2d}   "
  + ", ".join(d[1] for d in glossed))
P(f"  deposits with references but no link     {len(orphaned):>2d}   "
  + ", ".join(d[1] for d in orphaned))

P()
P("3. What that means for the claim being tested")
P()
P(f"  {len(NO_REFERENCES)} deposits have no references, so there is nothing "
  f"for a defence to hide in.")
P(f"  {len(orphaned)} deposits list {sum(d[3] for d in orphaned)} references "
  f"with no stated relation to any claim,")
partial = [d for d in withrefs if 0 < d[5] + d[6] < d[3]]
P(f"  and {orphan - sum(d[3] for d in orphaned)} more sit unlinked inside "
  f"deposits that link some of their references ("
  + ", ".join(f"{d[1]} {d[3] - d[5] - d[6]}" for d in partial) + ").")
P(f"  For those {orphan} a reader cannot tell which claim any of them would "
  f"defend.")
P(f"  That leaves {len(cited) + len(glossed)} deposits "
  f"({intext + gloss} references) where the link is stated and the")
P("  claim is therefore testable.  Those are audited in refdata.py.")
