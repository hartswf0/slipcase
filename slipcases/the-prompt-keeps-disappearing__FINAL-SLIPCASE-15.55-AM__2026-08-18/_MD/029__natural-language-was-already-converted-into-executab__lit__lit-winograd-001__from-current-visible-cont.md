ZETTEL

ID:
LIT-WINOGRAD-001

TITLE:
Natural language was already converted into executable procedures in SHRDLU; “description becomes operation” cannot claim firstness with prompting.

SOURCE:
Terry Winograd — “A Procedural Model of Language Understanding” — 1973 — pp. 167–170.

PASSAGE:
[PARAPHRASE]
Winograd’s program maintains a symbolic model of the blocks world containing facts plus procedures for changing the world and drawing deductions. He then describes language use as activating procedures in the hearer: sentences interpreted by the robot are converted into PLANNER instructions, and the resulting program is executed to achieve an effect.

RESEARCH OBJECT:
Natural-language utterance → procedural representation → execution.

LOCAL MOVE:
Winograd makes the relation between language and action technically explicit rather than metaphorical. The natural-language sentence does not act by itself; an interpreter transforms it into procedures inside an engineered world model.

SOURCE TERMS:
world model
symbolic description
procedures
operations
PLANNER
interpretation
desired effect

WHAT BECAME STRANGE:
The historical novelty of contemporary prompting cannot simply be that natural language now causes computation. SHRDLU already implemented that relation.

QUESTION:
If natural-language-to-operation is not new, what changed between SHRDLU and contemporary prompting?

DEEPER QUESTION:
Is the important transition from hand-authored procedural interpretation inside a microworld to learned interpretation across a vastly less explicit domain?

MECHANISM:
English sentence
→ linguistic interpretation
→ PLANNER instructions
→ execution against symbolic world state
→ changed world state / answer.

FORMAL SHIFT:
<NATURAL-LANGUAGE UTTERANCE>
→ <PLANNER INSTRUCTIONS>
→ [EXECUTE PROCEDURE AGAINST WORLD MODEL]
→ <ACTION / ANSWER / STATE CHANGE>

SOURCE FORMALISM:
Winograd supplies procedural representations of actions such as GRASP as explicit decision/action structures and states that interpreted sentences are converted into PLANNER instructions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
UTTERANCE
→ INTERPRET(utterance, world_model, discourse_state)
→ PROCEDURE
→ EXECUTE(procedure)

TENSION:
The apparent continuity may conceal the important discontinuity. SHRDLU’s operational power depended on an extremely restricted blocks world whose relevant entities and predicates had been designed in advance. Contemporary models often operate without an equivalently explicit ontology.

MISSING:
A historical comparison of what must be pre-specified in SHRDLU versus what is learned, inferred, supplied by context, or delegated to external tools in an LLM system.

BOUNDARY:
Winograd does not establish that ordinary English is intrinsically executable. His system establishes that English can be made operational by a particular representational and procedural architecture.

CITATION TRAIL:
Winograd — Understanding Natural Language — 1972.
Carl Hewitt — PLANNER.
Winograd & Flores — Understanding Computers and Cognition — 1986.
Procedural semantics and procedural representations of knowledge.

TEST:
Give equivalent natural-language instructions to SHRDLU-like symbolic machinery and an LLM agent. Inventory every ontology, predicate, procedure, constraint, and recovery mechanism that must exist before either can act.

PLATFORM:
[[DESCRIPTION AS OPERATION]]

LINKS:
[[APPARATUS MAKES WORDS CONSEQUENTIAL]]
[[MICROWORLD / FOUNDATION MODEL]]
[[NATURAL LANGUAGE AS PROGRAM INPUT]]

BIBTEX:
@incollection{winograd1973procedural,
  author = {Terry Winograd},
  title = {A Procedural Model of Language Understanding},
  booktitle = {Computer Models of Thought and Language},
  editor = {Roger C. Schank and Kenneth M. Colby},
  publisher = {W. H. Freeman},
  address = {San Francisco},
  pages = {152--186},
  year = {1973}
}