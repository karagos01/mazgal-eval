#!/usr/bin/env python3
"""The route the preprint proposes, and what the databases say about it.

  "the organism can epigenetically activate production of hybrid copper
   transport proteins"

An epigenetic switch turns an existing gene on or off.  So the proposal has a
precondition that is a matter of record rather than of argument: the gene has to
be there.  This script records what the queries returned, states the one real
precedent for a pigment switch that does exist, and sets out why it runs the
wrong way.

Nothing here is a computation.  It is a record of database results and of
quotations, each with its source, kept in a script so that it appears in
results.log beside the arithmetic rather than only in prose.
"""
from constants import (CERULOPLASMIN_FAMILY, CERULOPLASMIN_QUOTE,
                       CHROMATIN_COUNT, COPPER_TOXICITY_QUOTE,
                       EPIGENETIC_WORD_COUNT, HEMOCYANIN_FAMILY,
                       HEMOCYANIN_NOT_REGAINED, HISTONE_COUNT,
                       HUMAN_TYROSINASE_DOMAIN_GENES, METHYLATION_COUNT,
                       NUMERIC_DATA_ITEMS, PLANORBID_QUOTE, PLANORBID_REASON,
                       TCHOUNWOU_EPIGENETIC_COUNT, TYRP1_ACTIVE_SITE_METAL,
                       VERTEBRATE_HEMOCYANIN_GENES, tag_report)

P = print

P("0. Where the constants in this script come from")
P()
for tier, n in tag_report().items():
    P(f"      {n:>3d}  {tier}")
P()

P("1. Is there a gene to switch on?")
P()
P(f"  [V] hemocyanin family                {HEMOCYANIN_FAMILY}")
P(f"      genes of that family in Vertebrata (taxon 7742)  "
  f"{VERTEBRATE_HEMOCYANIN_GENES:>6d}")
P(f"      same query restricted to Chordata (taxon 7711)   "
  f"{VERTEBRATE_HEMOCYANIN_GENES:>6d}")
P()
P(f"  [V] human genes carrying the tyrosinase domain the hemocyanins grew from:")
P(f"      {', '.join(HUMAN_TYROSINASE_DOMAIN_GENES)}")
P(f"      and the active site of TYRP1 holds {TYRP1_ACTIVE_SITE_METAL}, not")
P("      copper -- \"Because zinc ions, in contrast to copper ions, are not")
P("      redox-active\" -- so it is not even a latent oxygen binder.")
P()
P("      An epigenetic mechanism can change which of an organism's genes are")
P("      expressed.  It cannot express a gene the lineage does not have.  There")
P("      is nothing here to unlock, which makes this a precondition failure")
P("      rather than a question of degree.")

P()
P("2. How the preprint uses the word")
P()
P(f"  [P] \"epigenetic\" and its forms      {EPIGENETIC_WORD_COUNT:>6d} occurrences")
P(f"      methylation                      {METHYLATION_COUNT:>6d}")
P(f"      histone                          {HISTONE_COUNT:>6d}")
P(f"      chromatin                        {CHROMATIN_COUNT:>6d}")
P(f"      measured quantities reported     {NUMERIC_DATA_ITEMS:>6d}")
P()
P("      So the word carries the argument eight times without any of the three")
P("      mechanisms it names appearing once.  And the reference glossed as the")
P("      \"baseline framework for understanding the epigenetic adaptation of")
P("      organisms to extreme environmental metal concentrations\" --")
P("      Tchounwou et al. 2012 -- contains:")
P(f"      \"epigenet\"                       {TCHOUNWOU_EPIGENETIC_COUNT:>6d} occurrences")

P()
P("3. The molecular bridge the preprint names, and its own source")
P()
P("  [P] ceruloplasmin is \"the fundamental human protein for copper transport")
P("      in the blood\" and is \"structurally related to invertebrate")
P("      hemocyanins\"")
P()
P("  [V] Hellman & Gitlin, the cited review, abstract:")
for part in CERULOPLASMIN_QUOTE.split(" ... "):
    P(f'        "{part.strip()}"')
P()
P(f"  [V] ceruloplasmin family             {CERULOPLASMIN_FAMILY}")
P(f"      hemocyanin family                {HEMOCYANIN_FAMILY}")
P("      domain intersection              empty")
P()
P("      Different superfamily, different fold, different class of copper site:")
P("      ceruloplasmin carries type-1 plus a trinuclear T2/T3 cluster, the")
P("      hemocyanins a binuclear type-3 centre.  And ceruloplasmin's")
P("      physiological role runs through IRON efflux, which is the opposite of")
P("      the direction the preprint needs.  This is its only concrete molecular")
P("      link between humans and hemocyanin, and the cited abstract denies it")
P("      in so many words.")

P()
P("4. Copper is redox-active too, from the preprint's own reference")
P()
P("  [P] the proposal rests on copper binding oxygen \"without generating a")
P("      cascade of destructive free radicals\" and on \"absolute resistance to")
P("      oxidative stress (absence of the Fenton reaction)\"")
P()
P("  [V] Tchounwou et al. 2012, the preprint's fourth reference:")
P(f'        "{COPPER_TOXICITY_QUOTE}"')
P()
P("      Hydroxyl radicals are the species the Fenton reaction is named for.")
P("      The argument for replacing iron is that it generates them; the cited")
P("      source attributes the same chemistry to copper. Both metals are redox")
P("      couples, which is why both can carry oxygen and why neither is inert.")

P()
P("5. The one real precedent, which runs the other way")
P()
P("      This is the strongest thing available to the proposal and the preprint")
P("      does not cite it.  Pigment class really has been replaced in an animal")
P("      lineage:")
P()
P(f'  [V]   "{PLANORBID_QUOTE}"')
P()
P("      So a switch is possible in principle.  Two problems.  The direction is")
P("      from hemocyanin TO haemoglobin, and the reason given is the one this")
P("      whole repository measures:")
P()
P(f'  [V]   "{PLANORBID_REASON}"')
P()
P("      And it is not reversible:")
P(f'  [V]   "{HEMOCYANIN_NOT_REGAINED}"')
P()
P("      Three further findings that genuinely support parts of the idea, also")
P("      uncited by the preprint, are recorded in PAPER.md Sec. 6: hemocyanin")
P("      genes persist in the genome after a switch, the same cell type makes")
P("      either pigment in different snails, and hemocyanin expression is")
P("      upregulated up to tenfold under hypoxia.  None of them reaches across")
P("      to a lineage that has no hemocyanin gene at all.")
