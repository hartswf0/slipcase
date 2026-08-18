ZETTEL

ID:
CALLSHOT-FIELD-008

TITLE:
A SCHEMA DOES NOT PERSUADE THE MODEL TO OBEY: IT CAN REMOVE ILLEGAL NEXT TOKENS FROM THE POSSIBILITY SPACE.

SOURCE:
OpenAI, “Introducing Structured Outputs in the API,” 2024-08-06. SOURCE URL: https://openai.com/index/introducing-structured-outputs-in-the-api/

PASSAGE:
[QUOTE]
“only tokens that would be valid according to the supplied schema”

RESEARCH OBJECT:
SPECIFICATION CAN MOVE FROM SEMANTIC INSTRUCTION INTO THE TOKEN-GENERATION MECHANISM.

LOCAL MOVE:
OpenAI describes converting a supplied JSON Schema into a grammar used for constrained decoding. Structural requirements can therefore become hard possibility boundaries rather than prose requests.

SOURCE TERMS:
“Structured Outputs” · “JSON Schema” · “constrained decoding” · “context-free grammar” · “valid tokens”

WHAT BECAME STRANGE:
A requirement discovered through prompting can eventually cease to be a prompt instruction at all.

QUESTION:
Which instructions should remain semantic language, and which should be compiled into schemas, code, permissions, or tests?

DEEPER QUESTION:
Is reliable natural-language programming partly a process of moving stabilized invariants out of prose and into mechanically enforced layers?

MECHANISM:
SCHEMA → GRAMMAR → PREFIX-DEPENDENT VALID TOKEN SET → MASK INVALID TOKENS → SAMPLE VALID STRUCTURE.

FORMAL SHIFT:
PLEASE FOLLOW RULE R → OUTPUT LANGUAGE IS RESTRICTED TO L(R).

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI describes dynamic constrained decoding that masks tokens inconsistent with the supplied schema after each generated token.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
P'(t|c,s)=0 if t violates schema s; otherwise renormalize over valid tokens.

TENSION:
Structural validity does not guarantee semantic truth. A schema-valid object can still contain wrong facts or wrong decisions.

MISSING:
A general method for deciding when a correction has matured enough to migrate from prose to machinery.

BOUNDARY:
Structured Outputs enforce supported structural constraints, not arbitrary semantic properties.

CITATION TRAIL:
[[CALLSHOT-20260817-02]] → schema as possibility boundary → [[CALLSHOT-FIELD-013]] tests as another migration target.

TEST:
Extract all structural instructions from a production prompt into a strict schema. Compare violations, semantic errors, retries, token cost, and maintainability.

PLATFORM:
OpenAI API · Structured Outputs · constrained decoding

LINKS:
[[CALLSHOT-20260817-02]] [[CALLSHOT-FIELD-007]] [[CALLSHOT-FIELD-013]]

BIBTEX:
@misc{OpenAIStructuredOutputs2024, author={{OpenAI}}, title={Introducing Structured Outputs in the API}, year={2024}, month=aug, url={https://openai.com/index/introducing-structured-outputs-in-the-api/}}
