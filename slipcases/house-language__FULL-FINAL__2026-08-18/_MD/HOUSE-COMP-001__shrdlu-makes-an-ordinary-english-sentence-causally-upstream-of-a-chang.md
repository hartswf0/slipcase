ZETTEL

ID:
HOUSE-COMP-001

TITLE:
SHRDLU MAKES AN ORDINARY ENGLISH SENTENCE CAUSALLY UPSTREAM OF A CHANGED WORLD-STATE.

SOURCE:
Terry Winograd — Procedures as a Representation for Data in a Computer Program for Understanding Natural Language — 1971 — abstract and system description.

PASSAGE:
[QUOTE]
“The system answers questions, executes commands, and accepts information in normal English dialog.”

RESEARCH OBJECT:
NATURAL LANGUAGE AS AN EXECUTABLE INTERFACE TO A WORLD.

LOCAL MOVE:
Winograd does not merely classify or paraphrase English. SHRDLU interprets commands concerning objects in a constrained blocks world and executes actions that alter that represented environment.

SOURCE TERMS:
normal English; dialog; command; procedure; semantic information; context; discourse; blocks world

WHAT BECAME STRANGE:
A sentence can occupy the causal position normally associated with a programming command without itself looking like conventional program code. The system supplies intermediate interpretation.

QUESTION:
Is SHRDLU an early prototype of the architecture required by “The House That Words Built”—not because it builds houses, but because it demonstrates ordinary sentence → interpreted intention → procedure → altered world?

DEEPER QUESTION:
What additional representational layers become necessary when the “world” stops being a closed blocks simulation and becomes a materially resistant construction site?

MECHANISM:
Natural-language input is interpreted using grammar, semantic knowledge, discourse context, and knowledge of the modeled environment; interpretation can trigger procedures that alter blocks-world state.

FORMAL SHIFT:
<DESIRED CHANGE IN OBJECT RELATIONS>
→ <NORMAL ENGLISH COMMAND>
→ [INTERPRET + EXECUTE]
→ <CHANGED BLOCKS-WORLD STATE>

SOURCE FORMALISM:
A procedural AI architecture coupling linguistic analysis with a restricted representation of objects, relations, actions, and discourse state.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
UTTERANCE → PARSE → REFERENT RESOLUTION → WORLD MODEL → ACTION PLAN → EXECUTION → NEW WORLD STATE

TENSION:
The apparent flexibility of ordinary language depends on severe closure: objects, predicates, actions, and permissible relations are represented in advance.

MISSING:
Open-ended objects; unknown affordances; material tolerances; unmodeled consequences; multiple agents; conflicting goals; physical uncertainty; legal authority; irreversible failure.

BOUNDARY:
SHRDLU demonstrates natural-language control of a simulated microworld, not unrestricted NL understanding, physical fabrication, architectural design, or direct control of matter.

CITATION TRAIL:
Winograd — Understanding Natural Language — 1972; blocks-world AI; planning; grounded language; natural-language robot control.

TEST:
Hold a command constant while progressively expanding the world ontology; measure which categories, assumptions, procedures, and repair mechanisms must be added before the same sentence remains executable.

PLATFORM:
[[THE HOUSE THAT WORDS BUILT]]

LINKS:
[[HOUSE-COMP-000]]
[[MICROWORLD AS PRECONDITION]]
[[NATURAL LANGUAGE AS CONTROL SURFACE]]

BIBTEX:
@phdthesis{winograd1971procedures, author={Winograd, Terry}, title={Procedures as a Representation for Data in a Computer Program for Understanding Natural Language}, school={Massachusetts Institute of Technology}, year={1971}}
