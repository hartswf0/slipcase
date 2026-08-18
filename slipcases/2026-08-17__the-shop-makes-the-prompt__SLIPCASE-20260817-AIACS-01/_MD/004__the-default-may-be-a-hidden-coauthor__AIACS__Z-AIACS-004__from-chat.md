ZETTEL

ID:
Z-AIACS-004

TITLE:
The default may be a hidden coauthor.

SOURCE:
AI Art as a Cultural System — A03, A07, A08 — pp. 2–3, 7, 9.

PASSAGE:
[PARAPHRASE]
The paper repeatedly says that algorithms, interfaces, training data, platform tendencies, and defaults constrain what users produce.

RESEARCH OBJECT:
Creative decisions can be made before the artist types anything.

LOCAL MOVE:
The source treats apparatus constraints as contributors to aesthetic form but never isolates the special role of defaults.

SOURCE TERMS:
“affordances”
“constraints”
“default biases”
“platforms”
“user interface”
“nudges”

WHAT BECAME STRANGE:
The prompt receives authorship attention precisely because it is visible, while defaults may determine far more while remaining invisible.

QUESTION:
How much of a generated image has already been decided by the platform before the user's description arrives?

DEEPER QUESTION:
Is prompting partly the experience of selecting within a world whose strongest aesthetic decisions have already been silently made?

MECHANISM:
training distribution
+ model architecture
+ safety rules
+ sampler
+ system prompt
+ interface defaults
→ prior output space

user prompt
→ local perturbation of that prior

FORMAL SHIFT:
<platform configuration>
→ <default possibility distribution>
→ [PROMPT]
→ <conditioned output>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OUTPUT = GENERATOR(DEFAULTS, PROMPT)

The critical variable may be:

Δprompt = distance(output_with_prompt, output_under_default)

rather than merely inspecting the prompt text.

TENSION:
Prompt culture foregrounds linguistic virtuosity, while apparatus theory suggests much causal force resides elsewhere.

MISSING:
The source does not enumerate actual defaults or establish their relative contribution.

BOUNDARY:
“Hidden coauthor” is our inference about causal significance, not source terminology.

CITATION TRAIL:
Platform documentation, model cards, UI histories, sampler defaults, internal system instructions where available, and studies of default effects in interface design.

TEST:
Generate systematically with blank, minimal, ordinary, and highly specified prompts while changing one hidden/default parameter at a time.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Default Images]]
[[Invisible Authorship]]
[[Prompt as Perturbation]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A03, A07, and A08}
}
