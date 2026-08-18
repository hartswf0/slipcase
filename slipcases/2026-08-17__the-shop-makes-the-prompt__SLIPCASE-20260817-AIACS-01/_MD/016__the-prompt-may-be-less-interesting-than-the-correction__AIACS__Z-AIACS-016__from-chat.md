ZETTEL

ID:
Z-AIACS-016

TITLE:
The prompt may be less interesting than the correction.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[PARAPHRASE]
Prompt expertise develops through practice, copying, experimentation, model-specific vocabulary, and strategies for counteracting model tendencies.

RESEARCH OBJECT:
The informative unit of prompting may be the sequence of failures and repairs rather than the successful final text.

LOCAL MOVE:
The paper describes iteration socially but still treats “the prompt” as a visible artifact.

SOURCE TERMS:
“learned through practice”
“improved”
“style-specific vocabulary”
“iterating”
“try adding”
“prompt formula”

WHAT BECAME STRANGE:
A finished prompt hides the observations that made each phrase necessary.

QUESTION:
If prompt competence is learned through response to outputs, why treat the final prompt as the creative object rather than the trajectory of corrections that produced it?

DEEPER QUESTION:
Does generative authorship reside in a feedback history?

MECHANISM:
description_0
→ output_0
→ noticed failure_0
→ correction_1
→ output_1
→ noticed failure_1
→ correction_2
→ …

FORMAL SHIFT:
<desired artifact>
→ <provisional description>
→ [GENERATE / INSPECT / CORRECT]
→ <progressively specified artifact>

SOURCE FORMALISM:
The source describes iterative prompt modification but provides no explicit loop formalism.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P_0 → G(P_0) → ERROR_0
P_1 = P_0 + correction(ERROR_0)
P_1 → G(P_1) → ERROR_1
...

The specification grows from encountered failure.

TENSION:
Prompt guides preserve successful incantations; learning actually occurs through unstable encounters between wording and outputs.

MISSING:
Prompt histories, rejected generations, and correction sequences.

BOUNDARY:
The source supports iteration but does not claim the loop rather than the final prompt is the proper unit of authorship.

CITATION TRAIL:
Prompt-engineering process studies; interface logs; version histories; creative process research; studies retaining rejected generations.

TEST:
Archive complete generation histories from expert and novice users. Compare final prompts with the sequence of constraints discovered through failures.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Deferred Formalization]]
[[Failure Becomes Specification]]
[[Prompt History]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
