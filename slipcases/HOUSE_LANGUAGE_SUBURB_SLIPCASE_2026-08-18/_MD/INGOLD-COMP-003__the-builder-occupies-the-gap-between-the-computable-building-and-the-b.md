```text
ZETTEL

ID:
INGOLD-COMP-003

TITLE:
THE BUILDER OCCUPIES THE GAP BETWEEN THE COMPUTABLE BUILDING AND THE BUILDING THAT WEATHER, MATERIALS, AND USE KEEP CHANGING.

SOURCE:
Tim Ingold — Making: Anthropology, Archaeology, Art and Architecture — 2013 — Chapter 4, “On Building a House,” pp. 47–48.

PASSAGE:
[PARAPHRASE]
Ingold contrasts the architect’s expectation of a completed stable realization with builders who repeatedly encounter unanticipated conditions, recalcitrant materials, and necessary improvisations; completion is at best a legal fiction.

RESEARCH OBJECT:
THE RUNTIME ENVIRONMENT OF A BUILDING.

LOCAL MOVE:
Ingold shifts from DESIGN → CORRECT REALIZATION to practical negotiation of discrepancies between intended form and unfolding circumstances.

SOURCE TERMS:
design; construction; process; plan; improvise; materials; completion; growth; decay; regeneration

WHAT BECAME STRANGE:
Programming offers a rival vocabulary: a building has something resembling a RUNTIME. A representation may compile while the actual environment introduces states it did not anticipate.

QUESTION:
What is the architectural equivalent of a runtime exception?

DEEPER QUESTION:
Could a sentence-to-wall language ever be sufficiently expressive to handle conditions that do not exist until execution has begun?

MECHANISM:
Prior representation constrains intended form; construction exposes it to variable materials, changing environment, unanticipated events, and local judgement; builders revise action to continue.

FORMAL SHIFT:
<PRE-EXISTENT DESIGN>
→ <CONSTRUCTION SITUATION>
→ [IMPROVISE UNDER UNANTICIPATED CONDITIONS]
→ <NEVER-QUITE-FINAL BUILDING>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
DESIGN = SOURCE; CONSTRUCTION SITE = RUNTIME; UNMODELED CONDITION = EXCEPTION; CRAFT JUDGEMENT = RUNTIME HANDLER; MODIFICATION = PATCH; MAINTENANCE = CONTINUED EXECUTION.

TENSION:
[[HOUSE-COMP-003]] and [[HOUSE-COMP-004]] follow increasingly complete building descriptions; Ingold asks whether representational completeness reduces contingency or reclassifies more events as deviations.

MISSING:
Empirical evidence from BIM-to-field workflows: what is automatic, what generates RFIs, what is improvised, what returns to the model.

BOUNDARY:
A construction site is not literally a software runtime; the analogy matters only if it identifies concrete represented/material state differences.

CITATION TRAIL:
[[HOUSE-COMP-003]] → Ingold → Stewart Brand → Lucy Suchman → BIM field coordination → digital twins → construction robotics.

TEST:
Recover every deviation between MODEL STATE and AS-BUILT STATE for one wall; identify detector, decider, representation, correction, and whether change propagated back to model.

PLATFORM:
[[THE HOUSE THAT WORDS BUILT]]

LINKS:
[[HOUSE-COMP-000]]
[[HOUSE-COMP-003]]
[[HOUSE-COMP-004]]
[[ARCHITECTURAL RUNTIME]]

BIBTEX:
@book{ingold2013making_runtime,
  author = {Ingold, Tim},
  title = {Making: Anthropology, Archaeology, Art and Architecture},
  publisher = {Routledge},
  year = {2013},
  doi = {10.4324/9780203559055}
}
```
