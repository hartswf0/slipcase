```text
ZETTEL

ID:
INGOLD-PROMPT-006

TITLE:
A CONSTRAINT MAY BE BETTER UNDERSTOOD AS THE HISTORY OF WHAT HAPPENED UNDER TEST THAN AS A STATIC ATTRIBUTE OF THE DESIRED OUTPUT.

SOURCE:
Tim Ingold — Making: Anthropology, Archaeology, Art and Architecture — 2013 — Chapter 2, “The Materials of Life,” pp. 30–31.

PASSAGE:
[QUOTE]
“The properties of materials … are not attributes but histories.”

[PARAPHRASE]
Ingold argues that practitioners know materials through histories of what they do under particular treatments and circumstances, rather than solely through fixed classifications or context-free attributes.

RESEARCH OBJECT:
CONSTRAINT AS HISTORY OF ENCOUNTERS.

LOCAL MOVE:
Ingold replaces THING → FIXED PROPERTY SET with THING → HISTORY OF RESPONSES UNDER CONDITIONS. This gives the paper’s “genealogy of constraints” a stronger technical interpretation.

SOURCE TERMS:
properties; attributes; histories; stories; treated; particular ways; engagement; becoming

WHAT BECAME STRANGE:
The constraint “NO DIRECT SIGHTLINE” is less informative than why it appeared, what failure exposed it, under what scenario, what change satisfied it, and what else changed. The history may be part of semantic content.

QUESTION:
Should a programming system store constraints as propositions or as histories of tested encounters?

DEEPER QUESTION:
Can two identical final invariants mean different things because they emerged from different failure histories?

MECHANISM:
An entity is subjected to operations and circumstances; behavior becomes perceptible; knowledge accumulates as history of responses; future action is informed by history.

FORMAL SHIFT:
<CONSTRAINT AS STATIC PREDICATE>
→ <CONSTRAINT + CONDITIONS + FAILURE HISTORY>
→ [RETEST UNDER NEW CONDITIONS]
→ <EVOLVING OPERATIONAL KNOWLEDGE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Instead of INVARIANT: roof_drains = true, store proposition, discovered_by test, prior_failure, conditions, correction, evidence, unresolved cases. The program becomes partly genealogical.

TENSION:
Conventional specification removes historical contingency; Ingold suggests knowing behavior may depend on preserving encounters through which a property became known. This supports the constraint-history thesis while making it more demanding than retaining chat logs.

MISSING:
A criterion for deciding how much genealogy matters operationally; preserving every event is unusable, so compression must retain causal relevance without collapsing history into bare propositions.

BOUNDARY:
Ingold is discussing materials, not requirements engineering. “Constraint as history” is an analogy and [OUR INFERENCE].

CITATION TRAIL:
[[THE PROMPT IS NOT THE PROGRAM]] → Ingold — material properties as histories → case-based reasoning → provenance systems → requirements rationale → design rationale → truth-maintenance → property-based testing.

TEST:
Take ten mature constraints; create FINAL PROPOSITION ONLY versus PROPOSITION + FAILURE + TEST + CORRECTION HISTORY; give both to a new agent modifying the artifact and measure regression prevention.

PLATFORM:
[[THE PROMPT IS NOT THE PROGRAM]]

LINKS:
[[THE PROMPT IS NOT THE PROGRAM]]
[[GENEALOGY OF CONSTRAINTS]]
[[CONSTRAINT HISTORY]]

BIBTEX:
@book{ingold2013making_histories,
  author = {Ingold, Tim},
  title = {Making: Anthropology, Archaeology, Art and Architecture},
  publisher = {Routledge},
  year = {2013},
  doi = {10.4324/9780203559055}
}
```
