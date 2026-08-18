ZETTEL

ID:
Z-AIACS-006

TITLE:
The “minority prompt” makes bias correction a user operation.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[QUOTE]
Rivas develops a “minority prompt”: an instruction designed to counteract biases in model training databases.

RESEARCH OBJECT:
A structural representational problem is partially converted into extra linguistic work performed at generation time.

LOCAL MOVE:
The artist does not merely describe a desired image; he uses the prompt against the model's prior.

SOURCE TERMS:
“minority prompt”
“counteract”
“biases”
“instruction”
“activism”

WHAT BECAME STRANGE:
The same text box serves simultaneously as artistic description and corrective intervention against the system receiving the description.

QUESTION:
What kind of interface is a prompt box when some users must spend part of their description counteracting the model before they can describe what they want?

DEEPER QUESTION:
Does prompt-based correction relocate representational governance from model builders into the hands of individual users?

MECHANISM:
biased training distribution
→ undesired model prior
→ corrective linguistic intervention
→ altered generation distribution

FORMAL SHIFT:
<representational absence / bias>
→ <counter-instruction>
→ [PROMPT AGAINST PRIOR]
→ <otherwise less-likely representation>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DESIRED_GENERATION =
PROMPT(content)
+
PROMPT(counter-prior)

The second term exists because the default distribution is not neutral.

TENSION:
Prompting is celebrated as democratized creative skill, but this case suggests competence may include learning how to compensate for failures users did not create.

MISSING:
Comparative evidence measuring how much corrective prompting different desired identities, bodies, relationships, or cultural settings require.

BOUNDARY:
The paper gives one politically explicit strategy; it does not establish that all marginalized users experience the same corrective burden.

CITATION TRAIL:
Felipe Rivas San Martín; scholarship on “Un archivo queer inexistente”; work on representational harms and text-to-image prompting.

TEST:
Construct matched image requests differing only in the represented social relation. Measure how many corrective prompt operations are needed to produce comparable fidelity.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Minority Prompt]]
[[Corrective Description]]
[[Default Bias]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
