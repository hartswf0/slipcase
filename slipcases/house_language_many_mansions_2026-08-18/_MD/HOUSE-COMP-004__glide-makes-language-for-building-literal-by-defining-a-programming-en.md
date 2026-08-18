ZETTEL

ID:
HOUSE-COMP-004

TITLE:
GLIDE MAKES “LANGUAGE FOR BUILDING” LITERAL BY DEFINING A PROGRAMMING ENVIRONMENT FOR REPRESENTING PHYSICAL SYSTEMS IN DESIGN-AND-CONSTRUCTION DETAIL.

SOURCE:
Charles M. Eastman and Max Henrion — “GLIDE: A Language for Design Information Systems” — SIGGRAPH — 1977 — pp. 24–33.

PASSAGE:
[QUOTE]
“GLIDE is intended to provide an efficient computer representation for physical systems in sufficient detail for their design and construction.”

RESEARCH OBJECT:
A DOMAIN-SPECIFIC PROGRAMMING LANGUAGE FOR PHYSICAL DESIGN INFORMATION.

LOCAL MOVE:
Eastman and Henrion move beyond storing a building description: the design-information environment becomes a LANGUAGE through which representations and operations over physical systems can be defined and manipulated.

SOURCE TERMS:
GLIDE; language; design information systems; computer representation; physical systems; design; construction; database; operations

WHAT BECAME STRANGE:
“The house built in language” can be literal: a building can exist as objects and operations inside a formal programming language before construction.

QUESTION:
Is GLIDE a better historical ancestor for prompt-to-building systems than philosophical accounts of language because it makes the representational transition operational?

DEEPER QUESTION:
What is gained when architectural description becomes programmable rather than merely machine-readable?

MECHANISM:
A language supplies abstractions for defining and manipulating structured representations of physical systems; representations support design operations and construction information.

FORMAL SHIFT:
<PHYSICAL SYSTEM>
→ <GLIDE REPRESENTATION>
→ [PROGRAMMATIC OPERATION]
→ <MODIFIED DESIGN INFORMATION>

SOURCE FORMALISM:
GLIDE is a programming-language environment for design information systems with structured representations and operations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
BUILDING_MODEL + PROGRAM → TRANSFORMED_BUILDING_MODEL.

TENSION:
GLIDE makes architectural information programmable but does not abolish the gap between information and construction: a wall object has not moved a physical wall.

MISSING:
Compilation from design object to fabrication instruction; machine control; physical feedback; construction sequencing; error correction; site sensing.

BOUNDARY:
GLIDE is not natural language, autonomous architecture, or a complete design-to-fabrication system.

CITATION TRAIL:
Eastman BDS; geometric modeling; solid modeling; CAD databases; BIM; parametric CAD; STEP; IFC; DesignScript; Grasshopper; building DSLs.

TEST:
Reconstruct one GLIDE operation and compare it with contemporary BIM/parametric CAD; identify what architectural knowledge migrated from HUMAN USER into LANGUAGE.

PLATFORM:
[[THE HOUSE THAT WORDS BUILT]]

LINKS:
[[HOUSE-COMP-003]]
[[BUILDING AS PROGRAM]]
[[DOMAIN SPECIFIC LANGUAGE]]

BIBTEX:
@inproceedings{eastman1977glide, author={Eastman, Charles M. and Henrion, Max}, title={GLIDE: A Language for Design Information Systems}, booktitle={Proceedings of the 4th Annual Conference on Computer Graphics and Interactive Techniques}, pages={24--33}, publisher={ACM}, year={1977}, doi={10.1145/563858.563863}}
