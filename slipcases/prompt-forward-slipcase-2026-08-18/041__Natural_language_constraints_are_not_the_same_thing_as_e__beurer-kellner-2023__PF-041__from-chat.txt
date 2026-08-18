ZETTEL

ID: PF-041

TITLE:
Natural-language constraints are not the same thing as executable constraints.

SOURCE:
Beurer-Kellner, Fischer, and Vechev — Prompting Is Programming — 2023.

PASSAGE:
[PARAPHRASE] LMQL provides programmatic constraints over generated output rather than relying entirely on the model to honor prose instructions.

RESEARCH OBJECT:
“Rails” can be soft instructions or hard(er) decoding/program constraints.

LOCAL MOVE:
The source splits constraint into at least two mechanisms.

SOURCE TERMS:
constraints; control flow; decoding; query language.

WHAT BECAME STRANGE:
A prompt that says “do not invent citations” and a program that prevents outputs violating a condition should not share one undifferentiated category.

QUESTION:
What kinds of constraint can prompt-forward scholarship claim to impose?

DEEPER QUESTION:
Does the scholarly contribution lie in writing a desired condition or in constructing machinery that enforces it?

MECHANISM:
<desired rule>
→ either <natural-language instruction> or <programmatic constraint>
→ [model execution]
→ <different reliability>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
LMQL constraints.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SOFT CONSTRAINT / EXECUTABLE CONSTRAINT.

TENSION:
The “prompt as rails” metaphor exaggerates enforcement when constraints remain probabilistic.

MISSING:
Constraint taxonomy tied to reliability.

BOUNDARY:
LMQL constraints themselves can still depend on model behavior and implementation.

CITATION TRAIL:
DSPy Assertions; constrained decoding.

TEST:
Implement the same prohibition as prose, LMQL constraint, and post-generation validator; compare failure rates.

PLATFORM:
[[Constraint Is Not One Operation]]

LINKS:
[[Soft Constraint]]
[[Hard Constraint]]
[[Prompt Reliability]]

BIBTEX:
@inproceedings{beurerkellner2023lmql,
  author={Luca Beurer-Kellner and Marc Fischer and Martin Vechev},
  title={Prompting Is Programming: A Query Language for Large Language Models},
  booktitle={PLDI},
  year={2023}
}