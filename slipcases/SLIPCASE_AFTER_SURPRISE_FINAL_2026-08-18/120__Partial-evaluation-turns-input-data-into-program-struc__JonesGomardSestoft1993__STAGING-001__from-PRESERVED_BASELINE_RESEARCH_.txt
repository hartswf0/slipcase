ZETTEL

ID:
STAGING-001

TITLE:
Partial evaluation turns input data into program structure without changing the computed result.

SOURCE:
Neil D. Jones, Carsten K. Gomard, and Peter Sestoft — Partial Evaluation and Automatic Program Generation — 1993 — Chapter 1, §§1.1–1.1.2.

PASSAGE:
[PARAPHRASE]
A partial evaluator receives a program together with part of that program’s input and produces a residual program. Running the residual program on the remaining input yields the same result as running the original program on all inputs. The authors explicitly note that the residual program is first produced as data and subsequently treated as code.

RESEARCH OBJECT:
PROGRAM and INPUT are not permanently assigned ontological categories.

Information can cross the boundary:

DATA
→ SPECIALIZATION
→ PROGRAM STRUCTURE

while preserving extensional behavior.

LOCAL MOVE:
The parent’s COUNTERFACTUAL CONTROL criterion still presupposes a stable distinction between the representation that controls behavior and the input on which that behavior operates.

Partial evaluation makes that partition movable.

SOURCE TERMS:
partial evaluation
program specialization
static input
dynamic input
residual program
binding time

WHAT BECAME STRANGE:
A value that begins as ordinary input can disappear from the runtime input interface because its consequences have been compiled into a new program.

QUESTION:
Is PROGRAM ROLE fundamentally a binding-time distinction between information fixed now and information supplied later?

DEEPER QUESTION:
If arbitrary inputs can be promoted into residual code through specialization, what remains of an intrinsic program/input boundary?

MECHANISM:
program p
+
static input s
→ partial evaluator mix
→ residual program p_s

then:

p_s
+
dynamic input d
→ output

with the same result as:

p(s,d).

FORMAL SHIFT:
<PROGRAM p + DATA s>
→ [SPECIALIZE]
→ <PROGRAM p_s>
→ [LATER INPUT d]
→ <OUTPUT>

SOURCE FORMALISM:
The source gives the specialization equation:

    [[p]] [s,d]
      =
    [[ [[mix]] [p,s] ]] d

where:

    [[mix]] [p,s]

is the specialized program.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Define a staging partition:

    Inputs(p) = Static × Dynamic

Then:

    Specialize(p,s) = p_s

such that:

    Beh(p,s,d) = Beh(p_s,d).

The same semantic information carried by s at one stage is carried by program structure at the next.

TENSION:
The distinction has not vanished completely.

The specializer still requires a designated subject program p and recognizes s as data during specialization.

MISSING:
What determines the admissible staging partition?

Can EVERY behaviorally relevant input be residualized into program structure?

BOUNDARY:
Partial evaluation makes program/data role transformable without making the distinction meaningless at each individual stage.

CITATION TRAIL:
[[UPTAKE-003]]
→ counterfactual-control criterion
→ Jones, Gomard, Sestoft on partial evaluation
→ static input becomes residual program
→ program role as staged information.

TEST:
Take one two-input program p(a,b).

Produce:

    p_a(b)

by specializing on a.

Then reverse which argument is static:

    p_b(a).

Compare what counts as PROGRAM STRUCTURE and INPUT DATA in the two residual systems while holding the original denotation fixed.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-003]]
[[program-role]]
[[binding-time]]
[[program-data-boundary]]

BIBTEX:
@book{JonesGomardSestoft1993,
  author    = {Jones, Neil D. and Gomard, Carsten K. and Sestoft, Peter},
  title     = {Partial Evaluation and Automatic Program Generation},
  publisher = {Prentice Hall},
  year      = {1993}
}
