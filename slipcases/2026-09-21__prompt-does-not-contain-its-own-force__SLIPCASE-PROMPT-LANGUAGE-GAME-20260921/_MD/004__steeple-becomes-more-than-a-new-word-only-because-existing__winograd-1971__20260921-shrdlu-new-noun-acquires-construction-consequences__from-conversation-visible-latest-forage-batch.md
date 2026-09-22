ZETTEL

ID:
20260921-shrdlu-new-noun-acquires-construction-consequences

TITLE:
“Steeple” Becomes More Than a New Word Only Because Existing Spatial Relations Can Make One

SOURCE:
Terry Winograd — Procedures as a Representation for Data in a Computer Program for Understanding Natural Language — 1971 — MIT AI Technical Report 235. ([dspace.mit.edu](https://dspace.mit.edu/entities/publication/3406b826-5a41-4b72-9430-7876c0d5405e?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Winograd’s system accepts information in English, reasons over its blocks world, remembers plans and actions, and can use newly supplied information in later deduction and manipulation. The well-known SHRDLU “steeple” case defines a steeple relationally as a small triangle on a tall rectangle, after which the term can be used in later questions and construction.

RESEARCH OBJECT:
A new linguistic category becoming operative because its definition composes already executable relations.

LOCAL MOVE:
The system does not acquire an entirely new primitive action when “steeple” is defined. It gains a new reusable relational pattern over pre-existing predicates and manipulation capabilities.

SOURCE TERMS:
information
deduction
context
world
plans
actions
properties
manipulate

WHAT BECAME STRANGE:
The apparent creativity of learning a new construct depends on an old substrate already knowing SMALL, TRIANGLE, ON, TALL, RECTANGLE, finding objects, and moving them. A new word can look like a new capability while mostly reorganizing existing capabilities.

QUESTION:
How much novelty in a user-defined prompt concept comes from the definition itself versus the executor’s pre-existing vocabulary of executable relations?

DEEPER QUESTION:
Can a system detect when a requested new concept is compositionally buildable from its existing world ontology and when the definition requires genuinely new primitives?

MECHANISM:
new category definition supplied
→ parse into known relations
→ store reusable relational schema
→ later category reference expands schema
→ planner searches / manipulates known object types
→ instance satisfies relation.

FORMAL SHIFT:
<NEW WORD>
→ <COMPOSITION OF EXISTING OPERATORS>
→ [STORE RELATIONAL SCHEMA]
→ <NEW REUSABLE CONSTRUCTION>

SOURCE FORMALISM:
Winograd describes SHRDLU as integrating syntactic analysis, semantic information, discourse context, world knowledge, deduction, plans, remembered actions, and executable manipulation. ([dspace.mit.edu](https://dspace.mit.edu/entities/publication/3406b826-5a41-4b72-9430-7876c0d5405e?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
novel_concept
=
new_composition(existing_predicates, existing_actions)
unless definition introduces an ungrounded primitive.

TENSION:
Modern generative models can produce plausible realizations of terms whose operational structure was never explicitly decomposed into symbolic predicates.

MISSING:
A test distinguishing compositional reuse from apparent concept acquisition produced by latent statistical associations.

BOUNDARY:
The SHRDLU world was deliberately small and symbolically defined; its compositional dependencies were unusually inspectable.

CITATION TRAIL:
[[20260921-shrdlu-definition-becomes-buildable-object]]
→ Winograd’s integrated world model
→ concept learning becomes a question about which primitive relations were already executable.

TEST:
Teach a world system two invented categories: one exactly composable from existing predicates and one requiring an unavailable relation such as FLEXES-WITHOUT-BREAKING. Ask it to classify, construct, repair, and explain instances of each.

PLATFORM:
[[genealogy-of-prompting]]

LINKS:
[[20260921-shrdlu-definition-becomes-buildable-object]]
[[SHRDLU]]
[[compositional-capability]]
[[operative-definition]]

BIBTEX:
@techreport{winograd1971procedures,
  author = {Winograd, Terry},
  title = {Procedures as a Representation for Data in a Computer Program for Understanding Natural Language},
  year = {1971},
  institution = {MIT Artificial Intelligence Laboratory},
  number = {AI-TR-235}
}
