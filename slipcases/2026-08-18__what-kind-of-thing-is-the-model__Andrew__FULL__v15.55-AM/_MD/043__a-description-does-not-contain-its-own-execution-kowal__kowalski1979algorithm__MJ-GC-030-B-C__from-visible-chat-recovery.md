ZETTEL

ID:
MJ-GC-030-B-C

TITLE:
A description does not contain its own execution: Kowalski separates what an algorithm means from how that meaning is used.

SOURCE:
Robert Kowalski — “Algorithm = Logic + Control” — Communications of the ACM 22(7) — 1979 — pp. 424–436.
Author-hosted PDF: https://www.doc.ic.ac.uk/~rak/papers/algorithm%20%3D%20logic%20%2B%20control.pdf

PASSAGE:
[QUOTE]
“Different ways of using the same definition give rise to different algorithms.”

[PARAPHRASE]
Kowalski decomposes an algorithm into a logic component L, representing the knowledge or definitions used to solve a problem, and a control component C, specifying how those definitions are used. He writes the decomposition as A = L + C. The same logical definition can be used bottom-up or top-down, producing different algorithmic behavior.

RESEARCH OBJECT:
DESCRIPTION-PLUS-CONTROL-EQUALS-EXECUTION.

LOCAL MOVE:
[[MJ-GC-030-B]] made a description of transformation appear program-like.

Kowalski introduces a necessary interruption:

A DESCRIPTION IS NOT YET ITS EXECUTION.

The same logical content can support different procedures depending on the control regime applied to it.

The missing machinery in “description becomes operation” may therefore be CONTROL.

SOURCE TERMS:
“logic component”
“control component”
“problem-solving strategies”
“meaning”
“top-down”
“bottom-up”
“A = L + C”
“controlled deduction”

WHAT BECAME STRANGE:
Two algorithms can share the same declared knowledge.

What changes is not WHAT THE DESCRIPTION MEANS.

What changes is HOW THE MACHINE TRAVERSES IT.

A program can therefore be partly absent from the representation visible to the user.

QUESTION:
What is the control component of a natural-language prompt system?

DEEPER QUESTION:
Does prompting feel as though words themselves execute because the platform hides the enormous control machinery that turns the same linguistic representation into a particular sequence of computational operations?

MECHANISM:
Kowalski:

LOGIC L
= domain knowledge / definitions.

CONTROL C
= strategy determining how L is used.

ALGORITHM:

A = L + C.

Same L:

L + C₁ → A₁
L + C₂ → A₂.

FORMAL SHIFT:
FROM:
DESCRIPTION
→ OPERATION

TO:
DESCRIPTION
+ CONTROL REGIME
→ OPERATION.

SOURCE FORMALISM:
Kowalski explicitly writes:

A = L + C.

He contrasts top-down and bottom-up uses of the same logical definitions and argues that control can alter algorithmic behavior while leaving the logic component unchanged.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For generative prompting:

VISIBLE DESCRIPTION = P.

HIDDEN / PARTLY EXPOSED CONTROL may include:

MODEL
DECODING / SAMPLING
ATTENTION DYNAMICS
TOOL ROUTING
CONTEXT ORDERING
SYSTEM-LEVEL INSTRUCTIONS
RANDOM INITIAL STATE.

Then:

BEHAVIOR
≠ P alone.

Hypothesis:

BEHAVIOR
= INTERPRET(P, C).

The list of possible control components is our analogy, not Kowalski's formalism.

TENSION:
Kowalski argues that the logic component determines algorithmic meaning while control changes how it is used.

In contemporary learned systems, changing decoding or representation can sometimes change not merely efficiency but the apparent semantics of the output.

The clean logic/control separation may therefore break.

MISSING:
A principled decomposition of a generative model into:
content-preserving control variables
versus
variables that actually change effective semantics.

BOUNDARY:
Kowalski's formal analysis concerns predicate logic, Horn clauses, and algorithm design.

It is not a historical theory of language-model prompting.

CITATION TRAIL:
[[MJ-GC-030-B]]
→ description of transformation as reusable operation
→ Kowalski 1979
→ same definition supports different algorithms under different control
→ description alone is insufficient
→ operative language requires an interpreter/control regime.

TEST:
Hold one prompt or declarative task description fixed.

Systematically vary only execution controls that plausibly preserve intended content:

random seed,
sampling strategy,
search procedure,
inference schedule.

Measure whether outputs differ only in route/efficiency or also in effective meaning.

The point at which meaning changes marks where Kowalski's logic/control separation fails for generative systems.

PLATFORM:
Logic programming / generative-system analogy

LINKS:
[[MJ-GC-030-B]]
[[MJ-GC-030-A]]
[[MJ-GC-011-A]]
[[MJ-GC-023-A]]

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
