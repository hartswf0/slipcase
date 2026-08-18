ZETTEL

ID:
HL-20260817-08

TITLE:
SHRDLU’S ENGLISH ACTS ONLY BECAUSE THE WORLD HAS ALREADY BEEN PARTLY BUILT INTO THE INTERPRETER

SOURCE:
Terry Winograd, “Understanding Natural Language,” Cognitive Psychology 3, no. 1 (1972): 1–191. DOI: 10.1016/0010-0285(72)90002-3. SOURCE URL: https://doi.org/10.1016/0010-0285(72)90002-3

PASSAGE:
[QUOTE] “The system answers questions, executes commands, and accepts information in an interactive English dialog.”

[PARAPHRASE] Winograd describes an integrated system containing a parser, a recognition grammar of English, semantic-analysis programs, a general problem-solving system, and a detailed model of a particular domain. Knowledge is represented procedurally, and the system can remember and discuss plans and actions as well as carry them out.

RESEARCH OBJECT:
SHRDLU is often tempting evidence for a direct path from natural language to world change. The source gives a stricter account.

The English imperative is not itself the executable object. Its effect depends on an already formalized blocks world containing entities, relations, contextual knowledge, physical knowledge, procedures, goals, and available operations.

Natural language gains operational force by entering a preconstituted action-space.

For House Language, the key question is therefore not merely how to compile words into a house. It is what architectural ontology and action vocabulary must already exist before an utterance can change anything at all.

LOCAL MOVE:
For every apparently natural-language operation in a world-building system, trace:

UTTERANCE
PARSE
REFERENT
WORLD MODEL ENTITY
GOAL
AVAILABLE OPERATION
STATE TRANSITION
OUTPUT.

Then mark which terms were supplied by the user and which were already built into the interpreter.

SOURCE TERMS:
interactive English dialog
parser
recognition grammar
semantic analysis
general problem solving system
detailed model
particular domain
physical knowledge
context
procedures
plans
actions

WHAT BECAME STRANGE:
The apparent causal power of the sentence grows as the machinery beneath it becomes less visible.

“Put the block in the box” sounds like language directly moving a thing. But BLOCK, BOX, IN, PUT, possible grasp, spatial relation, current state, goal state, and action procedure must already be representable.

The visible world produced by the sentence depends on an invisible prior world encoded in the interpreter.

QUESTION:
When a prompt changes a computational house, which architectural decisions come from the utterance and which have already been made by the ontology, defaults, constraints, and action vocabulary of the system?

DEEPER QUESTION:
Does natural-language programming increase linguistic agency, or does it relocate authorship into interpreters whose preformalized worlds determine what language can cause?

MECHANISM:
UTTERANCE
→ syntactic analysis
→ semantic/contextual interpretation
→ reference into domain model
→ goal/problem solving
→ procedure
→ state transition
→ response.

FORMAL SHIFT:
FROM:

LANGUAGE
→ WORLD

TO:

LANGUAGE
→ INTERPRETATION
→ FORMALIZED DOMAIN
→ AVAILABLE OPERATION
→ STATE CHANGE.

SOURCE FORMALISM:
The source explicitly describes a parser, recognition grammar, semantic analysis, general problem solving, detailed domain model, contextual and physical knowledge, and procedural representation of knowledge.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT
+
DOMAIN ONTOLOGY
+
STATE
+
INTERPRETER
+
ACTION VOCABULARY
+
EXECUTOR
=
PERMITTED WORLD CHANGE.

TENSION:
READING A:
SHRDLU demonstrates language acquiring executable world-making power.

READING B:
The power is partly misattributed to language because the microworld has already been constructed so that utterances resolve into known entities and operations.

Both readings matter: the causal distance between utterance and action genuinely shortens, but only inside a deliberately formalized world.

MISSING:
A detailed trace of one published SHRDLU imperative through internal representation and planner procedures.

A comparison with a contemporary prompt-to-CAD or prompt-to-world system at the same level of implementation detail.

BOUNDARY:
SHRDLU does not demonstrate unrestricted English altering an open physical world. Its effectiveness depends on a restricted domain that can be represented computationally.

CITATION TRAIL:
[[HOUSE-LANGUAGE-001]]
→ Winograd
→ SHRDLU
→ detailed domain model
→ procedural knowledge
→ executable action
→ hidden prior world
→ compare with architectural world models

TEST:
Take one published SHRDLU command and one natural-language command in a current world-building system.

For each enumerate every concept or operation that must pre-exist in the implementation before the sentence can act.

Classify each as:

USER-SUPPLIED
INTERPRETER-SUPPLIED
WORLD-MODEL-SUPPLIED
DEFAULTED
INFERRED
UNDEFINED.

The zettel survives if apparently simple linguistic agency depends on substantial preformalized world structure in both systems.

PLATFORM:
HOUSE LANGUAGE / SHRDLU / NATURAL-LANGUAGE PROGRAMMING / WORLD MODEL

LINKS:
[[HOUSE-LANGUAGE-001]]
[[SHRDLU]]
[[WINOGRAD]]
[[WORLD-MODEL]]
[[EXECUTABLE-LANGUAGE]]
[[HIDDEN-INTERPRETER]]

BIBTEX:
@article{Winograd1972UnderstandingNaturalLanguage,
  author  = {Winograd, Terry},
  title   = {Understanding Natural Language},
  journal = {Cognitive Psychology},
  volume  = {3},
  number  = {1},
  pages   = {1--191},
  year    = {1972},
  doi     = {10.1016/0010-0285(72)90002-3},
  url     = {https://doi.org/10.1016/0010-0285(72)90002-3}
}
