ZETTEL

ID:
MJ-GC-030-A

TITLE:
SHRDLU historicizes operative language but forces a split: language changes the world only after an utterance is interpreted against a deliberately bounded world model.

SOURCE:
Terry Winograd — “Understanding Natural Language” — Cognitive Psychology 3(1), 1972, pp. 1–191 — DOI: 10.1016/0010-0285(72)90002-3.
Publisher record: https://www.sciencedirect.com/science/article/pii/0010028572900023
1971 technical-report record: https://eric.ed.gov/?id=ED056543

PASSAGE:
[PARAPHRASE]
Winograd's SHRDLU conducted interactive English dialogue in a restricted blocks world. The system could answer questions, execute commands, and accept new information. Its architecture integrated syntactic analysis, semantic analysis, inference, a problem solver, and a detailed model of the domain under discussion.

RESEARCH OBJECT:
NATURAL-LANGUAGE-UTTERANCE-AS-WORLD-STATE-TRANSITION.

LOCAL MOVE:
[[MJ-GC-030]] proposed:

DESCRIPTION
→ GENERATION
→ INTERACTION STATE.

SHRDLU provides an earlier and more explicit operative-language architecture, but it introduces a crucial correction.

Natural language does not become action merely by being language.

Execution becomes possible because an utterance passes through machinery that determines:
what kind of utterance it is,
what objects it refers to,
what operation it denotes,
whether that operation is possible,
and how the represented world must change.

The operative force resides in the whole interpretation-execution system.

SOURCE TERMS:
“English”
“dialog”
“syntax”
“semantics”
“inference”
“commands”
“questions”
“information”
“domain”
“problem solving”

WHAT BECAME STRANGE:
“Language builds the house” becomes too simple.

Between sentence and house sits an executable theory of what exists, what words can denote, which relations are valid, and which state transitions are permitted.

The world must already be formalized enough to be changed by words.

QUESTION:
What hidden world model must exist before a natural-language description can become an operation?

DEEPER QUESTION:
When contemporary generative systems appear to let unrestricted prose “make worlds,” have they abolished the bounded micro-world—or merely hidden its operative ontology inside learned representations?

MECHANISM:
UTTERANCE
→ syntactic interpretation
→ semantic interpretation in context
→ reference resolution / inference
→ actionable representation
→ problem solver
→ permitted operation
→ BLOCKS-WORLD STATE CHANGE.

FORMAL SHIFT:
FROM:
WORDS
→ WORLD

TO:
WORDS
→ INTERPRETATION
→ DOMAIN MODEL
→ OPERATION
→ STATE TRANSITION
→ WORLD REPRESENTATION.

SOURCE FORMALISM:
[PARAPHRASE]
Winograd describes a system containing:
a parser,
a recognition grammar of English,
programs for semantic analysis,
and a general problem-solving system.

The program is supplied with a detailed model of the particular domain it discusses.

It handles utterances including questions, commands, and information in interactive English dialogue.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD = {
OBJECTS,
PROPERTIES,
RELATIONS,
LEGAL_OPERATIONS,
CURRENT_STATE
}.

INTERPRET(u, WORLD)
→ ACTION(a)
or QUERY(q)
or ASSERTION(p).

For command:

if PRECONDITIONS(a, WORLD):
    WORLD' = EXECUTE(a, WORLD).

The sentence does not itself move the block.

The interpreted operation does.

TENSION:
[[MJ-GC-030]] blurs description and command because real-time generative prompting can make descriptive language produce perceptual artifacts.

SHRDLU insists on a stronger distinction between linguistic forms and executable acts.

Yet contemporary text-to-image systems complicate that distinction because an apparently descriptive noun phrase can itself initiate a generative procedure.

MISSING:
A precise comparison between SHRDLU's explicit symbolic world model and the implicit learned representations through which diffusion systems condition generation.

BOUNDARY:
SHRDLU's success depends on an intentionally narrow blocks world.

It does not demonstrate general natural-language control of arbitrary reality.

CITATION TRAIL:
[[MJ-GC-030]]
→ real-time dungeon description becomes visualization
→ Winograd 1971/1972
→ English utterances mapped through syntax, semantics, inference, and domain knowledge into commands
→ operative description requires executable world machinery
→ question shifts from “Can words build worlds?” to “What world must already exist for words to operate?”

TEST:
Represent one generative tabletop interaction in SHRDLU-like terms.

For the utterance:
“a ruined tower rises beyond the river”

identify:
OBJECTS
PROPERTIES
RELATIONS
ASSERTIONS
OPERATIONS
STATE CHANGES.

Then ask which generated details cannot be derived from the utterance or prior world state.

Those residual details identify where generative systems exceed command execution by synthesizing unspecified world content.

PLATFORM:
SHRDLU / blocks-world natural-language interaction

LINKS:
[[MJ-GC-030]]
[[MJ-GC-026]]
[[MJ-GC-025]]

BIBTEX:
@article{winograd1972understanding,
  author={Winograd, Terry},
  title={Understanding Natural Language},
  journal={Cognitive Psychology},
  volume={3},
  number={1},
  pages={1--191},
  year={1972},
  doi={10.1016/0010-0285(72)90002-3}
}
