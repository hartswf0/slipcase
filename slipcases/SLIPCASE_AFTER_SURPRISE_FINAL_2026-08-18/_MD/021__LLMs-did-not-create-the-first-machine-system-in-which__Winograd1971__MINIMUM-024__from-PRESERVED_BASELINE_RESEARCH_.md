ZETTEL

ID:
MINIMUM-024

TITLE:
LLMs did not create the first machine system in which ordinary English commands changed a computational world.

SOURCE:
Terry Winograd — Procedures as a Representation for Data in a Computer Program for Understanding Natural Language — 1971 — MIT AI Technical Report 235. Later descriptions of the system document users manipulating its blocks world through English commands. 20

PASSAGE:
[PARAPHRASE]
SHRDLU accepted English interaction in a bounded blocks world, allowing commands to cause simulated actions such as moving and stacking objects. 21

RESEARCH OBJECT:
NATURAL-LANGUAGE OPERATIVITY predates LLMs.

LOCAL MOVE:
Winograd connects natural-language interpretation to a procedural world model and action repertoire.

SOURCE TERMS:
natural language
procedures
commands
blocks world
action

WHAT BECAME STRANGE:
The final paragraph says ambiguous cultural artifacts are “increasingly subjected to mechanical execution” as a historical novelty of generative models.

The relevant genealogy begins substantially earlier.

QUESTION:
What property of LLM prompting is historically new if natural-language machine control is not?

DEEPER QUESTION:
Is the novelty learned semantic breadth rather than linguistic executability?

MECHANISM:
SHRDLU:

English command
→ hand-engineered linguistic interpretation
→ procedural representation
→ blocks-world action.

LLM system:

natural-language context
→ learned model
→ distribution over continuations/actions
→ optional tool execution.

FORMAL SHIFT:
<BOUNDED HAND-SPECIFIED NL INTERPRETER>
→ <LEARNED OPEN-ENDED CONDITIONAL INTERPRETER>

SOURCE FORMALISM:
Winograd’s work uses procedural representations and a deliberately restricted simulated world.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Candidate historical novelty dimensions:

    DOMAIN BREADTH
    LEARNED INTERPRETATION
    ZERO/FEW-SHOT ADAPTATION
    STOCHASTIC GENERATION
    TOOL GENERALITY

not:

    FIRST NATURAL LANGUAGE → ACTION.

TENSION:
SHRDLU’s microworld and manually engineered ontology differ radically from foundation models trained over broad corpora.

MISSING:
A genealogy from SHRDLU through:
semantic parsing,
spoken-command systems,
robotics,
instruction-following models,
LLM agents.

BOUNDARY:
LLMs can still represent a profound historical shift without being the first machine-operative natural-language interface.

CITATION TRAIL:
SHRDLU.
LUNAR.
natural-language interfaces.
semantic parsing.
robot command grounding.

TEST:
Compare SHRDLU and a tool-enabled LLM along:

vocabulary size
ontology source
parser specification
environment
action repertoire
uncertainty
adaptation.

Locate novelty empirically.

PLATFORM:
[[generative-collapse]]

LINKS:
[[shrdlu]]
[[natural-language-operation-before-llms]]
[[prompt-genealogy]]

BIBTEX:
@techreport{Winograd1971,
  author      = {Winograd, Terry},
  title       = {Procedures as a Representation for Data in a Computer Program for Understanding Natural Language},
  institution = {MIT Artificial Intelligence Laboratory},
  number      = {AI-TR-235},
  year        = {1971}
}
