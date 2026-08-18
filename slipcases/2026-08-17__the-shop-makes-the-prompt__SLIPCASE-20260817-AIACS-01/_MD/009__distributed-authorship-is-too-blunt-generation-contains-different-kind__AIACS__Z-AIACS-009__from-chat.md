ZETTEL

ID:
Z-AIACS-009

TITLE:
“Distributed authorship” is too blunt; generation contains different kinds of control.

SOURCE:
AI Art as a Cultural System — A03 and A07 — pp. 2, 7–8.

PASSAGE:
[PARAPHRASE]
The paper calls AI creation hybrid or distributed because humans select prompts or training inputs while the apparatus produces outcomes beyond direct control.

RESEARCH OBJECT:
Authorship may need to be decomposed into operations before it can be distributed.

LOCAL MOVE:
The paper asks whether credit belongs to prompt writers, model builders, or machines.

SOURCE TERMS:
“hybrid authorship”
“distributed”
“prompt”
“training sets”
“machine's creators”
“credit”

WHAT BECAME STRANGE:
“Who authored it?” may be malformed if different parties control different transformations.

QUESTION:
Which operations in generative production are actually being bundled together under the word authorship?

DEEPER QUESTION:
Would disputes about AI authorship become clearer if credit attached to operations rather than persons?

MECHANISM:
corpus construction
→ model design/training
→ interface/default configuration
→ prompting
→ generation
→ selection
→ editing
→ circulation

Different actors intervene at different transitions.

FORMAL SHIFT:
<production chain>
→ <actor-operation assignments>
→ [COLLAPSE]
→ <single authorship question>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

AUTHORSHIP_STACK = {
  dataset_authority,
  model_authority,
  parameter_authority,
  descriptive_authority,
  selection_authority,
  transformation_authority,
  publication_authority
}

TENSION:
The paper recognizes distributed agency but returns repeatedly to singular nouns: “artist,” “machine,” “creator,” “author.”

MISSING:
A vocabulary distinguishing forms of creative control without assuming they are interchangeable.

BOUNDARY:
The proposed stack is analytical reconstruction, not source syntax.

CITATION TRAIL:
Flusser on apparatus; work on distributed authorship; legal and philosophical analyses distinguishing conception, execution, selection, and control.

TEST:
Describe one finished AI artwork only as an operation ledger. Then ask where alternative theories of authorship place the decisive threshold.

PLATFORM:
[[Authorship After Generation]]

LINKS:
[[Operation Ledger]]
[[Agency Stack]]
[[Prompt Is Not the Whole Program]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A03 and A07}
}
