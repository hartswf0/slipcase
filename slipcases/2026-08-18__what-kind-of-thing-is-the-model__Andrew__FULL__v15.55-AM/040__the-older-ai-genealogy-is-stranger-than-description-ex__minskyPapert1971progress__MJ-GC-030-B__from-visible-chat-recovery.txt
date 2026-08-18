ZETTEL

ID:
MJ-GC-030-B

TITLE:
The older AI genealogy is stranger than “description executes”: Minsky and Papert propose computation by changing descriptions of things, then describing the changes themselves.

SOURCE:
Marvin Minsky and Seymour Papert — “Progress Report on Artificial Intelligence” — MIT Artificial Intelligence Laboratory, AIM-252 — December 11, 1971.
URL: https://web.mit.edu/dxh/www/marvin/web.media.mit.edu/~minsky/papers/PR1971.html

PASSAGE:
[QUOTE]
“by operating on descriptions (instead of on the things themselves)”

[QUOTE]
“the description is itself a MODEL -- not merely a name”

[PARAPHRASE]
In their analogy procedure, Minsky and Papert distinguish descriptions of situations from higher-level descriptions of how those descriptions are changed. A transformation inferred from one pair of descriptions can then be applied to another description.

RESEARCH OBJECT:
DESCRIPTION-OF-DESCRIPTION-AS-EXECUTABLE-TRANSFORMATION.

LOCAL MOVE:
[[MJ-GC-030]] asked when description stops representing a world and begins operating on it.

Minsky and Papert introduce a stranger alternative:

perhaps computation need not operate on the world at all.

It can:
describe a world,
modify the description,
describe that modification,
then reuse the description-of-change as an operation on another description.

The operative object is not necessarily the represented thing.

It is the representation.

SOURCE TERMS:
“descriptions”
“change”
“MODEL”
“symbols”
“relations”
“procedure”
“description-handling mechanisms”

WHAT BECAME STRANGE:
A description can occupy at least three roles:

1. DESCRIPTION OF A THING.
2. STATE THAT CAN ITSELF BE CHANGED.
3. DESCRIPTION OF HOW ANOTHER DESCRIPTION CHANGED.

At level 3, description begins to resemble program.

QUESTION:
When a prompt describes not only a desired world but a transformation of a previous world, has it crossed from representation into procedural description?

DEEPER QUESTION:
Is the distinctive power of prompting that natural language can recursively describe:
objects,
world states,
changes,
and rules for producing further changes,
without visibly switching notation?

MECHANISM:
DESCRIPTION D_A
represents STATE A.

Modify D_A
until it represents STATE B.

Construct D_Δ
describing:
HOW D_A CHANGED.

Apply D_Δ
to DESCRIPTION D_C.

Produce:
D_C'.

Thus:

DESCRIPTION
→ TRANSFORMATION OF DESCRIPTION
→ DESCRIPTION OF TRANSFORMATION
→ REUSABLE TRANSFORMATION.

FORMAL SHIFT:
FROM:
DESCRIPTION
→ OPERATION ON WORLD

TO:
WORLD
→ DESCRIPTION
→ OPERATION ON DESCRIPTION
→ DESCRIPTION OF OPERATION
→ OPERATION ON NEW DESCRIPTION.

SOURCE FORMALISM:
The source gives a schematic analogy procedure:

Step 1:
construct descriptions for two figures.

Step 2:
change one description so it describes another figure.

Step 3:
construct a description of the change.

Step 4:
apply that description of change to the other description.

The authors then generalize toward “description-handling mechanisms.”

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

D(W₁) = representation of world/state W₁.

Δ:
D(W₁) → D(W₂).

META-DESCRIPTION:

D(Δ) = representation of transformation Δ.

Then:

EXECUTE(D(Δ), D(W₃))
→ D(W₄).

Recursive type:

DESCRIPTION<
  OBJECT |
  STATE |
  TRANSFORMATION<DESCRIPTION>
>.

TENSION:
Minsky and Papert explicitly emphasize symbolic, structured representations.

Contemporary prompts are surface natural-language strings interpreted by learned systems.

The formal similarity is provocative, but the computational substrates are radically different.

MISSING:
A modern technical source demonstrating whether language models or multimodal generative systems can reliably treat natural-language descriptions of transformations as reusable operators across novel represented states.

BOUNDARY:
This source does not establish a genealogy from 1971 description-handling research to contemporary prompting.

It establishes an earlier computational possibility:
representations can themselves become operands.

CITATION TRAIL:
[[MJ-GC-030]]
→ description enters an interaction loop
→ Minsky & Papert 1971
→ operate on descriptions rather than represented things
→ describe changes to descriptions
→ reuse those descriptions of change
→ description becomes recursively program-like.

TEST:
Give a generative system:

STATE A description,
STATE B description.

Ask it to produce only a reusable description of the transformation Δ from A→B.

Then provide novel STATE C and apply Δ without examples.

If the transformed C reliably preserves the abstract relation learned from A→B, the system is treating a description-of-change as something closer to a reusable operator than an isolated instruction.

PLATFORM:
MIT AI Laboratory / symbolic description-processing

LINKS:
[[MJ-GC-030]]
[[MJ-GC-023]]
[[MJ-GC-019]]

BIBTEX:
@techreport{minskyPapert1971progress,
  author={Minsky, Marvin and Papert, Seymour},
  title={Progress Report on Artificial Intelligence},
  institution={MIT Artificial Intelligence Laboratory},
  number={AIM-252},
  year={1971},
  url={https://web.mit.edu/dxh/www/marvin/web.media.mit.edu/~minsky/papers/PR1971.html}
}
