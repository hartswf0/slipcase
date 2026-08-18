ZETTEL

ID:
MJ-GC-030-B-D

TITLE:
A logical description has no fixed input or output: the same relation can test a fact or run backward to discover the missing entity.

SOURCE:
Robert Kowalski — “Algorithm = Logic + Control” — Communications of the ACM 22(7) — 1979 — pp. 424–436.
Author-hosted PDF: https://www.doc.ic.ac.uk/~rak/papers/algorithm%20%3D%20logic%20%2B%20control.pdf

PASSAGE:
[PARAPHRASE]
In Kowalski's procedural interpretation of Horn clauses, the input-output arguments of a procedure are not permanently fixed. A relation used to test whether something is true can also be invoked with unknown variables in order to discover values for which the relation holds.

RESEARCH OBJECT:
REVERSIBLE-DESCRIPTION.

LOCAL MOVE:
[[MJ-GC-030-B-C]] separated description from control.

Kowalski contains a second, stranger consequence.

A conventional function points one way:

INPUT
→ OUTPUT.

A logical relation need not.

The same declaration can answer:

IS ZEUS AN ANCESTOR OF X?

or:

WHO IS ZEUS AN ANCESTOR OF?

The description remains the same.

The unknown moves.

SOURCE TERMS:
“input-output arguments”
“not fixed”
“procedure call”
“relationship”
“find individuals”
“variables”
“substitution”

WHAT BECAME STRANGE:
Execution direction is not necessarily written into the description.

The query determines which part of the relation is treated as known and which becomes something to discover.

The “program” changes direction without rewriting the underlying relation.

QUESTION:
What would it mean to design prompt languages around relations rather than commands?

DEEPER QUESTION:
Could generative interaction become more powerful if descriptions were treated as reversible constraint structures from which users could ask the system to solve for any missing component?

MECHANISM:
RELATION:

R(x,y).

Possible uses:

given x,y:
TEST R(x,y).

given x:
SOLVE y such that R(x,y).

given y:
SOLVE x such that R(x,y).

same declared relation,
different query binding.

FORMAL SHIFT:
FROM:
PROGRAM:
INPUT → OUTPUT

TO:
DESCRIPTION:
RELATION(X₁,...,Xₙ)

QUERY:
bind any subset

→ solve remaining variables.

SOURCE FORMALISM:
Kowalski states that input-output arguments are not fixed and depend on the procedure call.

A procedure capable of testing a relation among known individuals can also be used to find individuals for whom that relationship holds.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

HOUSE relation:

HOUSE(
site,
structure,
materials,
climate,
cost,
geometry
).

Conventional generator:

site + requirements
→ geometry.

Relational generator:

site + geometry
→ infer materials?

geometry + cost
→ infer feasible structure?

structure + climate
→ infer site constraints?

The description becomes a constraint field rather than a one-directional prompt.

TENSION:
Logic programming can support relational reversibility because relations and proof procedures possess explicit formal semantics.

Natural-language generative systems often hallucinate plausible missing values rather than solve logically constrained variables.

The resemblance could therefore be superficial unless constraints are externally checked.

MISSING:
A prompt or representation language that combines natural-language expressiveness with enforceable relational constraints and genuinely reversible querying.

BOUNDARY:
Do not infer that arbitrary Prolog relations are efficiently executable in every direction.

Kowalski's paper itself emphasizes that control strategy and representation strongly affect computational behavior and efficiency.

CITATION TRAIL:
[[MJ-GC-030-B]]
→ descriptions of transformations
→ [[MJ-GC-030-B-C]]
→ description requires control
→ Kowalski's procedural interpretation
→ input/output roles are query-dependent
→ description can be operational without possessing a single execution direction.

TEST:
Choose a domain with machine-checkable constraints.

Represent one design problem as a relation rather than a function.

Run at least four query directions by withholding different variables.

Compare:

logical relation engine,
LLM natural-language prompting,
LLM + constraint checker.

Determine where natural language behaves relationally and where it merely invents a plausible inverse.

PLATFORM:
Logic programming / relational computation

LINKS:
[[MJ-GC-030-B]]
[[MJ-GC-030-B-C]]
[[MJ-GC-030-A]]

BIBTEX:
@article{kowalski1979algorithm,
  title={Algorithm = Logic + Control},
  author={Kowalski, Robert},
  journal={Communications of the ACM},
  volume={22},
  number={7},
  pages={424--436},
  year={1979},
  doi={10.1145/359131.359136},
  url={https://www.doc.ic.ac.uk/~rak/papers/algorithm%20%3D%20logic%20%2B%20control.pdf}
}
