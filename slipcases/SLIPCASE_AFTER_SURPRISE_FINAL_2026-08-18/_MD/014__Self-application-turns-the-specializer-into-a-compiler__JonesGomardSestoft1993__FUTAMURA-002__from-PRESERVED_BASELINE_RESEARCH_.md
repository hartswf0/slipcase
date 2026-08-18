ZETTEL

ID:
FUTAMURA-002

TITLE:
Self-application turns the specializer into a compiler and then into a compiler generator.

SOURCE:
Neil D. Jones, Carsten K. Gomard, and Peter Sestoft — Partial Evaluation and Automatic Program Generation — 1993 — §§1.5.2–1.5.3, §4.3.2.

PASSAGE:
[PARAPHRASE]
When a self-applicable partial evaluator is specialized with respect to an interpreter, the residual program is a compiler for the interpreter’s source language. When the partial evaluator is specialized with respect to itself, the residual artifact is a compiler generator.

RESEARCH OBJECT:
PROGRAMMING ROLES can emerge from self-application rather than from distinct primitive machinery.

LOCAL MOVE:
The parent’s rules-of-rule-change problem acquires a concrete computational mechanism.

The machine that transforms programs can itself become its own input.

SOURCE TERMS:
self-application
partial evaluator
compiler
compiler generator
Futamura projection
mix

WHAT BECAME STRANGE:
One program text, `mix`, can participate as:

EXECUTING SPECIALIZER
INPUT PROGRAM
COMPILER CONSTRUCTOR
and
MATERIAL FOR COMPILER-GENERATOR CONSTRUCTION.

QUESTION:
Are interpreter, compiler, and compiler-generator different kinds of object or different fixed arguments of a sufficiently general higher-order operator?

DEEPER QUESTION:
Does self-application imply that computational role is fundamentally relational rather than syntactic?

MECHANISM:
First:

    target = mix(int, source)

Second:

    compiler = mix(mix, int)

Third:

    cogen = mix(mix, mix).

FORMAL SHIFT:
<SPECIALIZER>
→ [SELF-APPLICATION + FIXED INTERPRETER]
→ <COMPILER>
→ [SELF-APPLICATION AGAIN]
→ <COMPILER GENERATOR>

SOURCE FORMALISM:
Jones et al. give the equations:

    target   = [[mix]] [int, source]
    compiler = [[mix]] [mix, int]
    cogen    = [[mix]] [mix, mix]

as the Futamura projections.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Role may be modeled as:

    Role(object, argument-position, stage)

rather than:

    TypeOfThing(object).

The same underlying program can move among meta-level roles depending on where it is supplied.

TENSION:
Type constraints and language boundaries still restrict which self-applications are valid.

Not every specializer is self-applicable.

MISSING:
What structural properties make self-application possible without semantic collapse or nontermination?

BOUNDARY:
Meta-level status can be generated operationally through staging rather than residing intrinsically in an artifact.

CITATION TRAIL:
[[METASTABLE-001]]
→ rules of rule-change
→ self-applicable partial evaluator
→ compiler and compiler-generator generation
→ meta-role as executable staging relation.

[[REFLECT-001]]
→ language implementation as program
→ specializer applied to itself
→ programmable implementation generation.

TEST:
For each occurrence of `mix` in the three Futamura equations label it:

EXECUTED PROGRAM
STATIC INPUT
GENERATED OUTPUT.

If the same artifact occupies all three positions, reject any ontology assigning those roles intrinsically.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[METASTABLE-001]]
[[REFLECT-001]]
[[self-application]]
[[futamura-projections]]
[[meta-role]]

BIBTEX:
@book{JonesGomardSestoft1993,
  author    = {Jones, Neil D. and Gomard, Carsten K. and Sestoft, Peter},
  title     = {Partial Evaluation and Automatic Program Generation},
  publisher = {Prentice Hall},
  year      = {1993}
}
