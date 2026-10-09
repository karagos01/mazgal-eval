# Reference audit — do the citations say what they are cited for?

An audit of all **69 external references** in all **16 Zenodo records** by
M. Mazgal, reading what each cited work actually says about the claim it is
cited for.

The write-up is in [`PAPER.md`](PAPER.md), in Czech in
[`PAPER.cs.md`](PAPER.cs.md).

## Why this exists

The author of these preprints stated publicly that the defence of his arguments
is deliberately placed in the references rather than written in the text, and
that an analysis confined to the text will therefore miss it. That is a fair
methodological criticism and a testable claim: verifying that a reference exists
is weaker than reading what it says, and the five earlier repositories in this
series did more of the former than the latter.

So this audit looks for **support**, not only for error. A reference that
genuinely carries a claim is the more valuable finding here, and the ranked list
of what was found is in [`hidden.py`](hidden.py).

## The result

**The claim is partly vindicated, in two deposits.** Furey's thesis, cited in
SOTP, argues that causality and irreversible time emerge from the bracketing of
an algebraic expression — the conceptual core of the whole "Causal" series,
peer-reviewed, and nowhere stated in the preprints themselves. And Baez, cited
in openQL, supplies both a real-matrix encoding of octonion multiplication via
left-multiplication operators and a route to the number 12 through sl(3,ℍ)
acting on ℝ¹², with so(12) in his magic square and his own remark that "this is
no coincidence!" — a better derivation of 12 than either of the two openQL
gives. That is the author's point and it stands.

**It does not extend further, for three measured reasons.** 47 of the 69
references are attached to no claim at all and three deposits have no reference
list, so for two thirds of the corpus there is no carrier a defence could use.
Where support was found, the same pages refute the mechanism it is offered for:
Furey, Dixon and Baez each resolve non-associativity by passing to the
*associative* algebra of left-multiplication operators, which is exactly the
step the proposed architecture is premised on refusing. And fourteen claims are
contradicted by their own cited sources in those sources' own words.

## Requirements

```
python3 -m pip install -r requirements.txt   # numpy only
```

No GPU, no network for the audit itself. `fetch.sh` is the one script that needs
the network, and it only re-downloads the deposits so the citation-marker counts
can be recomputed from them.

## Reproducing the results

```
./run_all.sh                        # everything, offline, about 1 second
./fetch.sh corpus                   # optional: re-download the 16 deposits
python3 keywords.py corpus          #   then recompute the marker counts
```

| Script | What it does |
|---|---|
| [`refdata.py`](refdata.py) | the data: every reference, its verdict, the verbatim quotation the verdict rests on, and how far the cited work could be read |
| [`carrier.py`](carrier.py) | how many references are attached to any claim at all |
| [`audit.py`](audit.py) | verdict totals, access breakdown, keyword counts, citations that do not resolve as printed |
| [`hidden.py`](hidden.py) | the support that was found, ranked, with the rider that limits each |
| [`keywords.py`](keywords.py) | recomputes the citation-marker counts from the deposits; prints recorded values offline |
| [`fetch.sh`](fetch.sh) | downloads the 16 deposits from Zenodo and converts them to text |

Full output of one run: [`results.log`](results.log).

## Key numbers

| what | measured |
|---|---|
| Zenodo records audited | 16 (14 distinct works; openQL and MPPT have two versions each) |
| external reference entries | **69** |
| attached to a sentence by an in-text marker | **7 (10.1 %)** — only *Acoustic Projector* and SOTP |
| carrying only a parenthetical gloss | 15 (21.7 %) — openQL v1.0, Phytomining, Hemocyanin |
| **with no stated relation to any claim** | **47 (68.1 %)** |
| deposits with no reference list at all | **3** — MPPT v1.0, MPPT v1.1, CQFT |
| self-citations | 4, two of them listing "Mazgal, M., & Gemini AI" |
| verdict SUPPORTS | 3 |
| verdict PARTIAL | 18 |
| verdict NO SUPPORT | 23 |
| verdict REFUTES (the source states the opposite) | **14** |
| verdict UNRESOLVED (reference not located) | 1 |
| verdict rows resting on a full text | **38 of 59 (64 %)** |
| citations that do not resolve as printed | **7**, one of them a chimera of three sources |
| places where real support was found | **6**, ranked in `hidden.py` |
| claims with no carrier anywhere in the 69 | 13 |

## Audited deposits

| record | DOI | short |
|---|---|---|
| 22876757 | [10.5281/zenodo.22876757](https://doi.org/10.5281/zenodo.22876757) | Acoustic Projector |
| 22877345 | [10.5281/zenodo.22877345](https://doi.org/10.5281/zenodo.22877345) | X-Ternary |
| 22877912 | [10.5281/zenodo.22877912](https://doi.org/10.5281/zenodo.22877912) | MPPT v1.0 |
| 22914238 | [10.5281/zenodo.22914238](https://doi.org/10.5281/zenodo.22914238) | MPPT v1.1 |
| 22923154 | [10.5281/zenodo.22923154](https://doi.org/10.5281/zenodo.22923154) | COBAR |
| 22934058 | [10.5281/zenodo.22934058](https://doi.org/10.5281/zenodo.22934058) | Topological Momentum Drive |
| 22959886 | [10.5281/zenodo.22959886](https://doi.org/10.5281/zenodo.22959886) | CQFT |
| 22962188 | [10.5281/zenodo.22962188](https://doi.org/10.5281/zenodo.22962188) | PCTP |
| 22962557 | [10.5281/zenodo.22962557](https://doi.org/10.5281/zenodo.22962557) | SOTP |
| 23112560 | [10.5281/zenodo.23112560](https://doi.org/10.5281/zenodo.23112560) | openQL / openOL v1.0 |
| 23156927 | [10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927) | Cymatic stomatal stimulation |
| 23174932 | [10.5281/zenodo.23174932](https://doi.org/10.5281/zenodo.23174932) | Quantum Biofortification / Phytomining |
| 23186884 | [10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884) | Na-ion HFRS |
| 23209266 | [10.5281/zenodo.23209266](https://doi.org/10.5281/zenodo.23209266) | Hemocyanin physiology |
| 23241148 | [10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148) | openQL / openOL v1.1 |
| 23241777 | [10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777) | Intensional Physics Computing |

## Scope

This is not an audit of whether the claims are true — a claim can be right with
a bad citation. Where the arithmetic has been done it is in the companion
repositories below, and nothing here changes it.

Section 8 of `PAPER.md` sets out the limits. 21 of 59 verdict rows do not rest
on a full text and each says which substitute was used; two books were
unreachable and were replaced by their own authors' papers and published
summaries; one reference could not be located at all, which is negative
evidence rather than proof of absence. Keyword counts are reported as counts: a
zero means the term was searched for and is absent.

Three corrections this audit owes elsewhere are recorded in it. Tesla's patent
does *not* presuppose an iron core, contrary to this audit's own starting
assumption, and the Griffiths citation is correct — the error hypothesised here
does not exist. `openql-eval` already measured Baez's left-multiplication
construction without crediting him with supplying it. And the vocabulary census
in `keywords.py`, run over all sixteen records rather than ten, disproved a
priority claim in `cymatic-eval`: "causal" first reached zero in openQL v1.0 of
3 October, and all seven tracked terms are absent from COBAR of 23 September and
the Momentum Drive of 24 September, so the vocabulary comes in two interleaved
groups rather than disappearing over time. That correction is now recorded in
`cymatic-eval` §1.

## Companion evaluations

- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — the octonion two-layer/associator template and the Maxwell attribution census
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — the 2-bit LLM inference engine
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — the CQFT / PCTP / SOTP trilogy of September 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — the openQL / openOL tensor matrix architecture of October 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — the cymatic stomatal stimulation and pulsed light proposal of October 2026

## Licence

Code (all `*.py`, `run_all.sh`, `fetch.sh`): MIT, see `LICENSE`.
`PAPER.md` and `PAPER.cs.md`: CC BY 4.0.
Quotations from third-party works are short excerpts used for criticism and
review, each attributed to its source in `refdata.py`.
