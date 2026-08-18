ZETTEL

ID:
CALLSHOT-20260817-02

TITLE:
BAN THE WRONG NEXT MOVE — a schema controls AI by making illegal continuations impossible rather than by persuading the model not to produce them.

SOURCE:
OpenAI — “Introducing Structured Outputs in the API” — August 6, 2024.
https://openai.com/index/introducing-structured-outputs-in-the-api/

PASSAGE:
[PARAPHRASE]
OpenAI describes Structured Outputs as using constrained decoding in addition to model training. A supplied JSON Schema is converted into a grammar; after every generated token, the inference system determines which tokens remain legal and masks invalid alternatives so their sampling probability becomes zero.

RESEARCH OBJECT:
NEGATIVE-SPACE-PROGRAMMING.

LOCAL MOVE:
[[MJ-GC-030-B-C]] asked what CONTROL must be added to a description before it becomes reliable execution.

This supplies one concrete answer.

Do not keep telling the model:

“please follow this format.”

Alter the possibility space so malformed moves cannot occur.

This is a major pragmatic distinction:

PROMPTING asks.

CONSTRAINED DECODING forbids.

SOURCE TERMS:
“JSON Schema”
“constrained decoding”
“context-free grammar”
“valid tokens”
“mask”
“probability”
“0”

WHAT BECAME STRANGE:
The specification controls generation through absences.

The schema does not need to specify the desired sentence.

It specifies a language of legal sentences.

Everything outside that language disappears from the model’s available next moves.

The user calls the shot partly by making certain futures nonexistent.

QUESTION:
Which prompt requirements should remain persuasive natural-language instructions, and which should be compiled into hard generative constraints?

DEEPER QUESTION:
Is the strongest form of natural-language programming actually hybrid programming, where prose supplies intention but formal grammars define the reachable state space?

MECHANISM:
SCHEMA
→ compile to grammar
→ inspect generated prefix
→ calculate valid next tokens
→ mask invalid tokens
→ sample only from legal continuation set.

FORMAL SHIFT:
FROM:
“OUTPUT JSON.”

TO:
NEXT_TOKEN ∈ LEGAL(schema, prefix).

SOURCE FORMALISM:
OpenAI describes converting the supplied JSON Schema into a context-free grammar and dynamically restricting valid tokens at every sampling step.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT:
what should happen.

SCHEMA:
what forms are allowed.

DECODER:
which next states remain reachable.

CALL_SHOT
=
INTENTION
+
REACHABILITY CONSTRAINT.

TENSION:
Schema validity is not semantic correctness.

A perfectly schema-conforming answer may contain false values, wrong choices, or bad reasoning. OpenAI explicitly notes that Structured Outputs does not prevent errors inside valid fields.

MISSING:
A taxonomy separating:
FORM CONSTRAINTS,
DOMAIN CONSTRAINTS,
STATE CONSTRAINTS,
SEMANTIC CONSTRAINTS,
WORLD CONSTRAINTS.

BOUNDARY:
Hard output grammar controls representational legality, not truth.

CITATION TRAIL:
[[MJ-GC-030-B-C]]
→ description + control
→ structured output
→ grammar removes illegal next tokens
→ “calling the shot” becomes construction of the possibility space.

TEST:
Take ten requirements normally written as prompt prose.

For each ask:

CAN FAILURE BE MADE UNREPRESENTABLE?

If yes, translate it into a schema/grammar/typed constraint.

Compare reliability against instruction-only prompting.

PLATFORM:
OpenAI API / constrained decoding

LINKS:
[[MJ-GC-030-B-C]]
[[MJ-GC-030-B-B]]
[[CALLSHOT-20260817-01]]

BIBTEX:
@misc{openai2024structured,
  author={{OpenAI}},
  title={Introducing Structured Outputs in the API},
  year={2024},
  url={https://openai.com/index/introducing-structured-outputs-in-the-api/}
}
