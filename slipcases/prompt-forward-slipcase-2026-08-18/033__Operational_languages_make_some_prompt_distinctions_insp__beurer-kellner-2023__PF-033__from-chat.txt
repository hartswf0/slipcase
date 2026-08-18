ZETTEL

ID: PF-033

TITLE:
Operational languages make some prompt distinctions inspectable before governance judges them.

SOURCE:
Beurer-Kellner, Fischer, and Vechev — Prompting Is Programming — 2023.

PASSAGE:
[PARAPHRASE] LMQL externalizes model constraints and control flow as explicit program structures.

RESEARCH OBJECT:
Some formerly implicit prompt operations can be represented as inspectable computational objects.

LOCAL MOVE:
The language makes constraints first-class enough to be executed and analyzed.

SOURCE TERMS:
constraints; control flow; query; language-model programming.

WHAT BECAME STRANGE:
“Run the prompt before classifying it” becomes stronger when the operation itself can be represented rather than inferred from prose.

QUESTION:
Could governance reason about explicit operational roles instead of estimating AI involvement from narrative disclosure?

DEEPER QUESTION:
Would this unfairly privilege technically formalizable prompting over ordinary-language work?

MECHANISM:
<implicit intention>
→ <explicit constraint/program>
→ [execute]
→ <observable role>

FORMAL SHIFT:
<intention>
→ <LMQL program>
→ [constrained generation]
→ <behavior>

SOURCE FORMALISM:
LMQL.

OUR FORMALIZATION:
NONE

TENSION:
Formalizability is not identical to scholarly importance.

MISSING:
An operational vocabulary usable for non-programmer prompting.

BOUNDARY:
LMQL cannot classify all prompt use.

CITATION TRAIL:
DSPy signatures; workflow DSLs; research-method reporting.

TEST:
Encode the same prompt workflow once as free prose and once in LMQL, then compare what evaluators can infer about contribution.

PLATFORM:
[[Operational Object Language]]

LINKS:
[[LMQL]]
[[Explicit Constraint]]
[[Governance]]

BIBTEX:
@inproceedings{beurerkellner2023lmql,
  author={Luca Beurer-Kellner and Marc Fischer and Martin Vechev},
  title={Prompting Is Programming: A Query Language for Large Language Models},
  booktitle={PLDI},
  year={2023}
}