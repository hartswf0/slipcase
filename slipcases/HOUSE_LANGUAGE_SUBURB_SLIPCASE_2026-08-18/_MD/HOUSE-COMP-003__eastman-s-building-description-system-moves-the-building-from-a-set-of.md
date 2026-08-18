```text
ZETTEL

ID:
HOUSE-COMP-003

TITLE:
EASTMAN’S BUILDING DESCRIPTION SYSTEM MOVES THE BUILDING FROM A SET OF DRAWINGS INTO A COMPUTABLE DATA STRUCTURE.

SOURCE:
Charles Eastman, David Fisher, Gilles Lafue, Joseph Lividini, Douglas Stoker, and Christos Yessios — An Outline of the Building Description System — 1974 — Research Report 50.

PASSAGE:
[QUOTE]
“A building is considered as the spatial composition of a set of parts.”

RESEARCH OBJECT:
THE BUILDING AS A COMPUTATIONAL OBJECT.

LOCAL MOVE:
Eastman begins from the problem that drawings are the description of record yet are redundant, inconsistent, and separated from numerical analysis. BDS proposes a computer-based description detailed enough for design, construction, and operation.

SOURCE TERMS:
description of record; building description; parts; spaces; database; attributes; interactive graphic language; design; construction; operation

WHAT BECAME STRANGE:
Before a computer can “build” anything, the building must first become something the computer can represent: HOUSE → DATA STRUCTURE.

QUESTION:
Was the decisive computational transformation of architecture not automation of drawing but invention of the BUILDING AS DATABASE?

DEEPER QUESTION:
Which properties of a building had to become explicit entities, relations, and attributes before architectural operations could become programmable?

MECHANISM:
A building is decomposed into elements and spaces; geometry, relationships, properties, and connections are stored in a common representation on which operations can query, edit, compose, analyze, and regenerate views.

FORMAL SHIFT:
<BUILDING>
→ <DATABASE OF PARTS + SPACES + RELATIONS + PROPERTIES>
→ [EDIT / SORT / ANALYZE / COMPOSE]
→ <UPDATED BUILDING DESCRIPTION / DERIVED REPRESENTATIONS>

SOURCE FORMALISM:
BDS includes a building database, element descriptions, spaces, attributes, component libraries, an interactive graphic language, and operations over arrangements.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
BUILDING = {ELEMENTS, SPACES, GEOMETRY, RELATIONS, PROPERTIES}; UPDATE(MODEL) → propagate consequences.

TENSION:
The House That Words Built foregrounds linguistic input; Eastman suggests decisive infrastructure lies one layer later: BUILDING must become computationally addressable.

MISSING:
Construction sequence; craft knowledge; material tolerances; site improvisation; labor; supply chains; code interpretation; ownership; responsibility.

BOUNDARY:
BDS does not eliminate drawings, automatically fabricate buildings, or accept unrestricted natural-language specifications.

CITATION TRAIL:
Eastman 1976; Eastman/Henrion GLIDE; BIM histories; product modeling; STEP; IFC; parametric building models.

TEST:
Compare the ontology of BDS with a contemporary BIM schema; identify which categories were added before increasingly downstream construction operations became computable.

PLATFORM:
[[THE HOUSE THAT WORDS BUILT]]

LINKS:
[[HOUSE-COMP-000]]
[[BUILDING AS DATA STRUCTURE]]
[[COMPUTABLE HOUSE]]

BIBTEX:
@techreport{eastman1974bds, author={Eastman, Charles and Fisher, David and Lafue, Gilles and Lividini, Joseph and Stoker, Douglas and Yessios, Christos}, title={An Outline of the Building Description System}, institution={Institute of Physical Planning, Carnegie-Mellon University}, number={Research Report 50}, year={1974}}
```
