ZETTEL

ID:
STRATEGY-001

TITLE:
Partial evaluation introduces a second control problem: deciding which computation happens now and which becomes future code.

SOURCE:
Neil D. Jones, Carsten K. Gomard, and Peter Sestoft — Partial Evaluation and Automatic Program Generation — 1993 — §§1.1, 4.3–4.4.

PASSAGE:
[PARAPHRASE]
Partial evaluation performs a mixture of execution and code generation. The specializer must decide which available values to exploit immediately and which transitions to compress or residualize; Jones and collaborators treat these decisions as a specialization strategy.

RESEARCH OBJECT:
STRATEGY does not merely choose among possible runtime transitions.

It can choose the TEMPORAL LOCATION OF THE TRANSITION:

NOW
or
LATER AS GENERATED CODE.

LOCAL MOVE:
The parent split transition relation from strategy.

Partial evaluation adds another axis:

EXECUTE
versus
RESIDUALIZE.

SOURCE TERMS:
strategy
specialization
static
dynamic
code generation
mixed computation
binding time

WHAT BECAME STRANGE:
A computation can change ontological appearance without changing semantics.

What is an EXECUTED TRANSITION during specialization in one staging regime may appear as PROGRAM TEXT awaiting execution in another.

QUESTION:
Is the description/operation boundary partly a binding-time boundary?

DEEPER QUESTION:
Could “operative description” be recursively defined as computation deferred into representation?

MECHANISM:
specializer observes expression/transition τ.

If dependent only on static information:

    execute τ now.

If dependent on dynamic information:

    emit representation of τ
    into residual program
    for execution later.

FORMAL SHIFT:
<OPERATION>
→ {
    [EXECUTE NOW] → <VALUE>,
    [RESIDUALIZE] → <DESCRIPTION OF FUTURE OPERATION>
  }

SOURCE FORMALISM:
Jones et al. characterize partial evaluation as mixed computation and distinguish static versus dynamic computation according to binding time.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Introduce stage index k:

    Op_k

may produce:

    Value_k

or:

    Code_{k+1}(Op).

Thus:

    operation at stage k
    → description at stage k+1
    → operation at stage k+1.

TENSION:
Residual code is not merely deferred execution history; specialization may simplify, duplicate, eliminate, or restructure computations.

MISSING:
A formal criterion for when an operation and its residual description count as THE SAME operation across stages.

BOUNDARY:
The description/operation distinction can reverse recursively under staging.

CITATION TRAIL:
[[UPTAKE-002]]
→ transition relation versus strategy
→ partial-evaluation strategy
→ execute versus residualize
→ operation becomes future description.

[[UPTAKE-003]]
→ operative description
→ binding-time engineering
→ recursive description/operation alternation.

TEST:
Take one expression in a staged program.

Run three binding-time assignments so that the same logical calculation occurs:

A. during specialization,
B. in residual code,
C. partly in both.

Trace exactly when it is DESCRIPTION and when it is OPERATION.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-002]]
[[UPTAKE-003]]
[[binding-time]]
[[mixed-computation]]
[[recursive-operativity]]

BIBTEX:
@book{JonesGomardSestoft1993,
  author    = {Jones, Neil D. and Gomard, Carsten K. and Sestoft, Peter},
  title     = {Partial Evaluation and Automatic Program Generation},
  publisher = {Prentice Hall},
  year      = {1993}
}
