ZETTEL

ID:
SHOT-20260817-03

TITLE:
2026-08-17 — A shot becomes stronger when its legal shape exists before its content.

SOURCE:
OpenAI — “Structured model outputs” — OpenAI API documentation — accessed 2026-08-17.
SOURCE URL: https://developers.openai.com/api/docs/guides/structured-outputs

PASSAGE:
[QUOTE]
“only Structured Outputs ensure schema adherence.”

RESEARCH OBJECT:
SCHEMA AS POSSIBILITY SPACE.

LOCAL MOVE:
[[MJ-2022-003]] made the prompt strange by locating an invisible representation beneath ordinary words.

[[SHOT-20260817-02]] makes instruction location strange by distributing rules among tools.

Structured Outputs adds yet another operation:

the human can declare the class of legal answers before the model chooses the answer.

A prompt no longer needs to say only:

“Give me the answer.”

or even:

“Give me exactly these fields.”

It can pair semantic intent with a machine-enforced structural type.

SOURCE TERMS:
“Structured Outputs”
“JSON Schema”
“schema adherence”
“strict”
“response format”
“function calling”

WHAT BECAME STRANGE:
The user can constrain the model through a language that is not primarily addressed to the model as prose.

The schema is a shot call whose force comes from making certain output shapes unavailable.

QUESTION:
How much prompt prose should disappear once the same constraint can be represented structurally?

DEEPER QUESTION:
Are schemas functioning as the first widely deployed type system for natural-language programming?

MECHANISM:
User specifies semantic goal.

User specifies legal structural representation.

Generation occurs inside that structural space.

Downstream operation consumes the resulting typed object.

FORMAL SHIFT:
REQUEST
→ FREE TEXT
→ PARSE
→ REPAIR

becomes

REQUEST
+
SCHEMA
→ TYPED OBJECT
→ NEXT OPERATION

SOURCE FORMALISM:
[PARAPHRASE]

OpenAI distinguishes ordinary JSON production from Structured Outputs that adhere to a supplied schema.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SHOT =
SEMANTIC INTENT
∩
STRUCTURAL TYPE

Example:

semantic:
“choose the next operation”

structural:
{
  operation: enum,
  target: string,
  confidence: number
}

The model cannot answer by wandering outside the declared representational space.

TENSION:
Structural correctness does not establish semantic correctness.

A perfectly legal object can still call the wrong operation.

This pushes the lineage directly toward [[SHOT-20260817-06]]:

TYPE CHECK
is not
ACTION REVIEW.

And toward [[SHOT-20260817-09]]:

SCHEMA VALIDITY
is not
SPECIFICATION VALIDITY.

MISSING:
A layer for expressing semantic invariants beyond shape.

Examples:

end_date must follow start_date
refund amount cannot exceed payment
deleted object must exist
child zettel must contain parent link
citation must support quoted proposition.

BOUNDARY:
Structured Outputs constrains supported structural properties.

It does not guarantee truth, good judgment, or correct external execution.

CITATION TRAIL:
[[MJ-2022-003]]
→ words become machine representation
→ [[SHOT-20260817-02]]
→ rules gain local scope
→ Structured Outputs
→ output receives type
→ [[SHOT-20260817-09]]
→ typed specification can itself be semantically linted
→ [[SHOT-20260817-06]]
→ valid action can still require review

TEST:
On 2026-08-17, collect recurring prose instructions such as:

“return exactly”
“do not add fields”
“always include”
“choose one of”
“use this order.”

Translate them into schema constraints where possible.

Measure which prose rules can disappear entirely and which still require semantic instruction.

PLATFORM:
OpenAI Structured Outputs
Function calling
Typed agent interfaces

LINKS:
[[MJ-2022-003]]
[[SHOT-20260817-02]]
[[SHOT-20260817-06]]
[[SHOT-20260817-09]]

BIBTEX:
NONE
