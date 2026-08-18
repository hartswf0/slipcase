ZETTEL

ID:
OPS-20260817-005

TITLE:
A schema calls the shot by making some next words impossible.

SOURCE:
OpenAI — “Introducing Structured Outputs in the API” — August 6, 2024.
https://openai.com/index/introducing-structured-outputs-in-the-api/

PASSAGE:
[QUOTE]
“Our approach is based on a technique known as constrained sampling or constrained decoding.”

RESEARCH OBJECT:
CONSTRAINT CAN ACT BELOW THE LEVEL OF INSTRUCTION FOLLOWING.

LOCAL MOVE:
[[MJ-MARTINA-021-A-A]] used Goodman to ask whether a prompt can determine its own compliance class.

Structured Outputs produces a different object: the developer supplies a JSON Schema and decoding is constrained so structurally invalid continuations can be excluded.

SOURCE TERMS:
“Structured Outputs”
“JSON Schema”
“strict”
“constrained sampling”
“constrained decoding”
“valid tokens”

WHAT BECAME STRANGE:
“Return exactly this structure” can exist in two radically different forms.

FORM 1:
natural-language instruction that the model may violate.

FORM 2:
a decoding constraint under which invalid structural continuations are not available.

The same apparent command has moved from semantics into the mechanics of generation.

QUESTION:
When should a requirement be represented as meaning and when should it be represented as grammar?

DEEPER QUESTION:
Is the new frontier of prompting the extraction of invariants from prose into machine-enforced representational constraints?

MECHANISM:
OpenAI describes Structured Outputs as combining model training with constrained decoding so generated structures match developer-supplied JSON Schemas.

FORMAL SHIFT:
FROM:
PROMPT:
“Always output objects with fields A, B, C.”

TO:
SCHEMA:
required = [A,B,C]

DECODER:
disallow structurally invalid token continuations.

SOURCE FORMALISM:
JSON Schema
+
strict mode
+
constrained decoding.

The source also states that structural correctness does not guarantee correctness of the values inside the structure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OUTPUT_SPACE_default
=
all token sequences

OUTPUT_SPACE_schema
=
{ x | x satisfies structural schema S }

Therefore:

S
does not merely REQUEST a property.

S changes the available output state space.

TENSION:
Structural validity is not semantic validity.

A perfectly schema-valid object can contain a wrong date, false claim, or incorrect operation.

MISSING:
A layered account distinguishing:
syntactic invariant,
semantic invariant,
world-state invariant,
and task-success invariant.

BOUNDARY:
Constrained decoding controls representational form, not truth or successful action.

CITATION TRAIL:
[[MJ-MARTINA-021-A-A]]
→ Goodman: script versus score
→ Structured Outputs creates determinacy for one dimension of compliance
→ some prompt requirements become grammars
→ investigate what remains outside grammar.

TEST:
Take twenty requirements currently written in prose.

For each classify:
STRUCTURAL
SEMANTIC
RELATIONAL
TEMPORAL
WORLD-STATE.

Move every structural requirement into a schema.

Measure:
format failures,
semantic failures,
prompt length,
retry count.

Then identify the remaining clauses that cannot be compiled into schema.

PLATFORM:
OpenAI API; Structured Outputs; JSON Schema

LINKS:
[[MJ-MARTINA-021-A-A]]
[[MJ-MARTINA-013-A]]

BIBTEX:
@misc{openai2024structuredoutputs,
  author = {{OpenAI}},
  title = {Introducing Structured Outputs in the API},
  year = {2024},
  month = {8},
  day = {6},
  url = {https://openai.com/index/introducing-structured-outputs-in-the-api/}
}
