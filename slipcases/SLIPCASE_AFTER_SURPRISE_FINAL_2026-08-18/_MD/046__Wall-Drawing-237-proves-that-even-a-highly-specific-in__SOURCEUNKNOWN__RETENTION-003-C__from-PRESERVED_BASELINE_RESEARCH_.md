ZETTEL

ID:
RETENTION-003-C

TITLE:
Wall Drawing 237 proves that even a highly specific instruction does not contain its own final geometry.

SOURCE:
Sol LeWitt — Wall Drawing 237, The location of a trapezoid — June 1974 — primary instruction and installation record preserved by MASS MoCA.

PASSAGE:
[PARAPHRASE]
The trapezoid is constructed through specified geometric relations using corners, side midpoints, and the center of the wall. The instructions tightly limit draftsman interpretation, yet the resulting geometry changes with the dimensions of the wall on which it is executed.

RESEARCH OBJECT:
ENVIRONMENT IS AN ARGUMENT OF THE INSTRUCTION.

LOCAL MOVE:
RETENTION-003 stores decisions in the description.

Wall Drawing 237 shows that the stored decision is incomplete until coupled to a particular world.

SOURCE TERMS:
location
trapezoid
midpoints
corners
center
architectural space
dimensions
relational

WHAT BECAME STRANGE:
The same instruction can be executed correctly twice and yield different visible geometry without anyone changing the instruction.

The wall participates in computation.

QUESTION:
Is the physical site part of the artwork’s input, its state, or its interpreter?

DEEPER QUESTION:
How should operative-description theory represent descriptions whose consequences emerge only when variables are supplied by the environment?

MECHANISM:
instruction
+
wall geometry
→ identify relevant architectural points
→ construct prescribed relations
→ resulting trapezoid.

FORMAL SHIFT:
<DESCRIPTION>
+
<ENVIRONMENT PARAMETERS>
→ [REALIZATION]
→ <SITE-SPECIFIC OUTPUT>

SOURCE FORMALISM:
The construction references geometrically defined points of the actual wall.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Instead of:

    Execute(p) = output

use:

    Execute(p, θ) = output

where:

    θ = architectural environment.

Thus:

    Execute(p, θ₁) ≠ Execute(p, θ₂)

while:

    p₁ = p₂.

TENSION:
Programming languages already behave this way whenever identical programs receive different inputs, environments, screen sizes, data, permissions, or hardware conditions.

The site-specific artwork may therefore be less exceptional computationally than aesthetically.

MISSING:
Which environmental variables count as legitimate parameters and which would invalidate the work.

BOUNDARY:
The instruction does not uniquely specify the physical artifact.

It specifies a relation between rule and site.

CITATION TRAIL:
[[RETENTION-003]]
→ deferred realization
→ Wall Drawing 237
→ same instruction, different walls
→ environment supplies unresolved variables
→ operative description becomes relational.

TEST:
Execute the geometric rule virtually on walls with:

1:1
2:1
5:1

aspect ratios.

Measure which geometric properties remain invariant and which vary.

Use the invariant set as a candidate description of work identity.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-003]]
[[environment-as-argument]]
[[wall-drawing-237]]
[[site-specific-execution]]
[[relational-description]]

BIBTEX:
NONE
