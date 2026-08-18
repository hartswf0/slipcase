ZETTEL

ID:
MINIMUM-029

TITLE:
Even self-reference and recursion-theorem constructions do not require Turing completeness.

SOURCE:
Neil D. Jones — “A Swiss Pocket Knife for Computability” — 2013 — §§2.5–3.3.

PASSAGE:
[PARAPHRASE]
Jones shows that the concrete program transformations used for the examined Second Recursion Theorem constructions can be implemented in a tiny flow-chart language with assignments and list operations but no tests or loops. He explicitly notes that this tiny language is not Turing-complete and that its programs run in constant time under the stated data-structure cost assumptions.

RESEARCH OBJECT:
SELF-REFERENCE is not evidence of UNIVERSAL COMPUTATIONAL POWER.

LOCAL MOVE:
The destructive minimum loses another candidate discriminator.

Not only ordinary programming but even significant reflective constructions can survive below Turing completeness.

SOURCE TERMS:
tiny
Second Recursion Theorem
constant time
program specialization
not Turing-complete
program generation

WHAT BECAME STRANGE:
Features commonly taken as signatures of deep computational reflexivity can occur inside a language too weak to compute arbitrary recursive functions.

QUESTION:
Which expressive power is actually required for program self-reference?

DEEPER QUESTION:
Can reflective or operative descriptions be formally weak while remaining structurally self-referential?

MECHANISM:
tiny program
→ finite data-structure manipulations
→ generate specialized/self-referential program representation

without:
loops
tests
general recursion
Turing completeness.

FORMAL SHIFT:
<SELF-REFERENCE>
↛
<TURING COMPLETENESS>

SOURCE FORMALISM:
Jones’ `tiny` programs use assignments, sequencing, constants, and list operators such as `hd`, `tl`, and `cons`, with no tests or loops.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Separate dimensions:

    COMPUTATIONAL UNIVERSALITY
    REFLECTIVE CAPABILITY
    PROGRAM GENERATION
    EXECUTABILITY.

None should be inferred from another without proof.

TENSION:
The surrounding acceptable programming system used to state the general recursion theorem is stronger than the tiny concrete transformation language used for these constructions.

MISSING:
The exact minimum expressive basis for:
quotation,
specialization,
self-reproduction,
and semantic self-modification
considered separately.

BOUNDARY:
Reflection is not a proxy for Turing completeness.

CITATION TRAIL:
[[METASTABLE-001]]
→ semantic self-modification
→ Kleene SRT implementations
→ non-Turing-complete tiny language
→ separate meta-capacity from universal computation.

TEST:
Build a capability matrix across:

finite-state machine
tiny Jones language
simply typed lambda calculus
Scheme
Maude.

Test independently for:
self-reproduction,
program-as-data,
specialization,
interpreter definition,
semantic modification,
Turing completeness.

PLATFORM:
[[destructive-minimum]]

LINKS:
[[METASTABLE-001]]
[[turing-completeness]]
[[reflection-without-universality]]
[[destructive-minimum]]

BIBTEX:
@article{Jones2013PocketKnife,
  author  = {Jones, Neil D.},
  title   = {A Swiss Pocket Knife for Computability},
  journal = {Electronic Proceedings in Theoretical Computer Science},
  volume  = {129},
  pages   = {1--17},
  year    = {2013},
  doi     = {10.4204/EPTCS.129.1}
}
