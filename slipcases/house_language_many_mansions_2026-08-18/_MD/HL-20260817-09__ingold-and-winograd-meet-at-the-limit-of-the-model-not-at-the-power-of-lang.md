ZETTEL

ID:
HL-20260817-09

TITLE:
INGOLD AND WINOGRAD MEET AT THE LIMIT OF THE MODEL, NOT AT THE POWER OF LANGUAGE

SOURCE:
Terry Winograd, “Understanding Natural Language,” Cognitive Psychology 3, no. 1 (1972): 1–191. SOURCE URL: https://doi.org/10.1016/0010-0285(72)90002-3

Tim Ingold, “On Building a House,” Chapter 4 of Making: Anthropology, Archaeology, Art and Architecture (Routledge, 2013), especially pp. 48, 54–57. SOURCE URL: https://doi.org/10.4324/9780203559055

David Turnbull, “The Ad Hoc Collective Work of Building Gothic Cathedrals with Templates, String, and Geometry,” Science, Technology, & Human Values 18, no. 3 (1993): 315–340. SOURCE URL: https://doi.org/10.1177/016224399301800304

PASSAGE:
[PARAPHRASE — WINOGRAD] SHRDLU can act because language interpretation is integrated with a detailed model of a restricted domain and procedural knowledge.

[QUOTE — INGOLD] “Builders, in practice if not in principle, inhabit this kink.”

[QUOTE — INGOLD, reporting Turnbull] The design argument can “attribute powers to rules they cannot have.”

RESEARCH OBJECT:
The productive opposition between Winograd and Ingold is not language versus materiality.

It is the status of the model.

Winograd demonstrates that natural-language action becomes possible when a domain is sufficiently formalized for language to resolve into operations. Ingold and Turnbull show why actual building cannot simply be explained as the execution of a complete prior formalization: materials, weather, workmanship, local practices, and unfinished states continually generate consequential conditions.

Put together, they define a boundary condition for House Language:

FORMALIZE ENOUGH TO ACT.
DO NOT FORMALIZE SO COMPLETELY THAT THE MODEL IS MISTAKEN FOR THE WORLD.

LOCAL MOVE:
Every House Language implementation must expose two explicit interfaces:

ACTION INTERFACE:
what the model knows how to change.

SURPRISE INTERFACE:
how evidence not anticipated by the model can alter its representation, constraints, or next action.

A system with only the first is a microworld executor.
A system with only the second cannot reliably act.

SOURCE TERMS:
detailed model
particular domain
procedures
kink
workmanship
rules
algorithms
situation at hand
improvisation
constructive geometry

WHAT BECAME STRANGE:
The strongest system may be neither fully formal nor proudly informal.

It may require a deliberately incomplete formalism plus a disciplined procedure for admitting consequences that the formalism failed to anticipate.

QUESTION:
What is the optimal boundary between preformalized action-space and open-ended situated correction in a language-driven world-building system?

DEEPER QUESTION:
Can a computational system treat its own ontology as revisable during execution without losing the invariants that make execution possible?

MECHANISM:
WINOGRAD SIDE:
formal domain
→ interpretable command
→ executable operation.

INGOLD SIDE:
operation
→ unanticipated world response
→ skilled attention
→ local revision.

COMBINED:
MODEL_t
→ LANGUAGE
→ ACTION
→ WORLD/ARTIFACT EVIDENCE
→ REVISE MODEL_t+1
→ ACTION.

FORMAL SHIFT:
FROM:

FORMALIZATION versus SITUATION

TO:

FORMALIZATION
↔
SITUATED REVISION.

SOURCE FORMALISM:
Winograd provides an explicit computational architecture with a detailed domain model and procedures.

Ingold provides no computational formalism; his chapter describes practical building, constructive geometry, improvisation, and the limits of treating skilled practice as rule execution.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ACTIONABLE MODEL M_t

command c_t
→ operation a_t
→ evidence e_t

if e_t fits M_t:
continue.

if e_t exposes missing variable, false relation, or failed assumption:
M_t → M_t+1
before continuing.

TENSION:
READING A:
Every surprise can ultimately be absorbed into a richer formal model.

READING B:
The attempt to pre-enumerate all possible surprise recreates the error Ingold and Turnbull criticize by treating situated practice as latent algorithmic output.

MISSING:
Empirical comparison between a closed prompt-to-world system and one that can revise its world model after perceptual inspection.

A principled stopping rule for when to expand the ontology versus make a local exception.

BOUNDARY:
The zettel does not claim that formalization and situated action are mutually exclusive. Its argument depends on their coupling.

CITATION TRAIL:
[[HOUSE-LANGUAGE-001]]
→ SHRDLU detailed model
→ Ingold builder inhabits kink
→ Turnbull rules cannot explain workmanship
→ ABIDING render-look-revise
→ actionable incomplete model
→ surprise interface

TEST:
Implement the same small world-building task in two systems.

SYSTEM A:
fixed ontology and action vocabulary; failures may only select another existing action.

SYSTEM B:
identical initial ontology, but inspection can add a new constraint, relation, or state variable.

Introduce one unmodeled condition.

Compare whether B can repair the failure without silently violating prior invariants.

PLATFORM:
HOUSE LANGUAGE / MODEL LIMITS / SITUATED EXECUTION / REVISABLE ONTOLOGY

LINKS:
[[HOUSE-LANGUAGE-001]]
[[HL-20260817-03]]
[[HL-20260817-08]]
[[INGOLD]]
[[WINOGRAD]]
[[TURNBULL]]
[[SURPRISE-INTERFACE]]

BIBTEX:
@article{Winograd1972UnderstandingNaturalLanguage,
  author  = {Winograd, Terry},
  title   = {Understanding Natural Language},
  journal = {Cognitive Psychology},
  volume  = {3},
  number  = {1},
  pages   = {1--191},
  year    = {1972},
  doi     = {10.1016/0010-0285(72)90002-3}
}

@book{Ingold2013Making,
  author    = {Ingold, Tim},
  title     = {Making: Anthropology, Archaeology, Art and Architecture},
  publisher = {Routledge},
  year      = {2013},
  doi       = {10.4324/9780203559055}
}

@article{Turnbull1993AdHoc,
  author  = {Turnbull, David},
  title   = {The Ad Hoc Collective Work of Building Gothic Cathedrals with Templates, String, and Geometry},
  journal = {Science, Technology, \& Human Values},
  volume  = {18},
  number  = {3},
  pages   = {315--340},
  year    = {1993},
  doi     = {10.1177/016224399301800304}
}
