ZETTEL

ID: CALVINO-004

TITLE:
The foundational combinatorial calculation contains a numerical error.

SOURCE:
Paolo Alessandrini — "La matematica di Italo Calvino" — Archimede 3 (2023), p. 160.

PASSAGE:
[PARAPHRASE]
Alessandrini identifies an arithmetic mistake in Calvino's calculation of the possible crime configurations. The combinatorial expression is correct; the printed numerical result is not.

RESEARCH OBJECT:
A discrepancy between the formal specification of a possibility space and its stated cardinality.

LOCAL MOVE:
Alessandrini separates the mathematical structure of the crime problem from the numerical result attributed to it.

SOURCE TERMS:
"disposizioni con ripetizione"; "coppie ordinate";
"schemi"; "12 alla dodicesima potenza."

WHAT BECAME STRANGE:
A story concerned with the computational mastery of possibility contains an error in its most conspicuous calculation.

QUESTION:
Does the error matter only as arithmetic, or does it expose a broader ambiguity between the mathematical possibility space and the actual narrative problem?

DEEPER QUESTION:
How much of the apparent rigor of computational literature survives when we audit its representations instead of accepting its stated numbers?

MECHANISM:
Four distinct people produce twelve possible ordered, nonreflexive pairs. Twelve independently assigned actions therefore produce 12^12 assignments.

FORMAL SHIFT:
4 characters
→ 4 × 3 ordered pairs
→ 12 choices for each of 12 actions
→ 12^12 assignments.

SOURCE FORMALISM:
12^12 = 8,916,100,448,256

Printed in Calvino:
8,874,296,672,256

Difference:
41,803,776,000

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

The initial search space assumes:
1. Exactly twelve action occurrences.
2. One ordered character pair per action.
3. No self-directed actions.
4. Independent assignment before compatibility constraints.

The counting rule does not establish that all these assignments represent narratable stories.

TENSION:
The equation counts assignments, not distinct plots under interpretation, causal equivalence, or narrative redundancy.

MISSING:
Evidence identifying the origin of the arithmetic mistake; a specification of when two assignments should count as the same narrative.

BOUNDARY:
The error does not invalidate the combinatorial construction itself or establish a general failure of computational approaches to literature.

CITATION TRAIL:
Alessandrini (2023), p. 160.
Calvino, "The Burning of the Abominable House" (1995 translation), p. 157.
Braffort (1997), section 2.

TEST:
Reproduce the count, then calculate how it changes under explicit restrictions on reciprocal relations, character mortality, duplicated motives, and permutation equivalence. Compare the different meanings of "possible story."

PLATFORM:
[[Formal Audits of Computational Literature]]

LINKS:
[[CALVINO-003]]
[[CALVINO-005]]

BIBTEX:
@article{alessandrini2023matematica,
  author  = {Alessandrini, Paolo},
  title   = {La matematica di Italo Calvino},
  journal = {Archimede},
  number  = {3},
  year    = {2023},
  pages   = {157--163},
  url     = {https://riviste.mondadorieducation.it/archimede/wp-content/uploads/sites/2/2023/12/0060.ARCH3_23_ARch_Cultura_Alessandrini_157_163.pdf}
}
