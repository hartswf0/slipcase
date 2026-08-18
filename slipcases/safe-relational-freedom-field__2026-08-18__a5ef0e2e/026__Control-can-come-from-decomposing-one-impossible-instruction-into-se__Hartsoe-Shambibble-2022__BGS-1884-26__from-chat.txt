ZETTEL

ID:
BGS-1884-26

TITLE:
Control can come from decomposing one impossible instruction into several partially independent ones

SOURCE:
Shambibble — interview with Watson Hartsoe — October 22, 2022 — 58:41–1:04:33. fileciteturn3file1L213-L235

PASSAGE:
[PARAPHRASE]
For an orc woman with green skin and white hair, Shambibble separates the desired attributes into multiple prompts that share “orc woman” as common ground while assigning hair and skin color separately. He reports that the decomposition produced the intended combination more reliably than one undifferentiated prompt. fileciteturn3file1L221-L231

RESEARCH OBJECT:
Authorship may lie neither in the words nor in choosing an output but in decomposing a representational problem into independently steerable subproblems.

LOCAL MOVE:
The practitioner discovers a structural operation:

shared invariant + separated constraints.

SOURCE TERMS:
common ground
agree
split them off
green skin
white hair
overlapping
break up your prompt
influence

WHAT BECAME STRANGE:
A description and a control program can contain almost the same words while doing different things because the words have been partitioned differently.

QUESTION:
Can the structure imposed on instructions itself constitute expressive determination even when the generator realizes every visible pixel?

DEEPER QUESTION:
Is decomposition a form of authorship because it decides which expressive variables must cohere and which may vary independently?

MECHANISM:
single coupled representation
→ attribute interference
→ identify shared invariant
→ split conflicting constraints
→ independent generative influence
→ recombination around common subject

FORMAL SHIFT:
<UNDIVIDED DESCRIPTION>
→ <SHARED INVARIANT + SEPARATE CONSTRAINTS>
→ [PARALLEL STEERING]
→ <RECOMBINED EXPRESSION>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Desired object:

ORC_WOMAN
with:
HAIR = WHITE
SKIN = GREEN

Instead of:

f(ORC, WHITE, GREEN)

construct:

f₁(ORC_WOMAN, WHITE_HAIR)
f₂(ORC_WOMAN, GREEN_SKIN)

with invariant:

I = ORC_WOMAN

The human authors a dependency structure among constraints.

TENSION:
[[BGS-1884-18]] asks what interface properties convert instructions into expressive operations.

This example suggests a candidate answer: the ability to address relations among variables, not merely name desired properties.

MISSING:
Evidence that the decomposition actually maps to separable internal operations rather than merely changing surface probabilities through an opaque mechanism.

BOUNDARY:
Shambibble explicitly describes the mechanism provisionally—“hopefully,” “I think”—and lacks access to the diffusion process needed to verify which component acts first. fileciteturn3file1L221-L223

CITATION TRAIL:
[[BGS-1884-18]]
[[BGS-1884-19]]
→ multi-prompt “common ground”
→ constraint decomposition
→ investigate variable addressability as a dimension of authorial control

TEST:
Create target images requiring attributes that normally bleed across one another.

Compare:

single prompt
repetition
weighting
structural decomposition

Measure not aesthetic quality but independent control of each requested variable.

PLATFORM:
[[Constraint Decomposition]]

LINKS:
[[BGS-1884-18]]
[[BGS-1884-19]]
[[Control Semantics]]
[[Variable Addressability]]
[[Common Ground Prompting]]

BIBTEX:
@misc{HartsoeShambibble2022,
  author = {Hartsoe, Watson and Shambibble},
  title = {Interview on Midjourney Prompt Craft},
  year = {2022},
  month = {10},
  note = {Interview conducted October 22, 2022}
}
