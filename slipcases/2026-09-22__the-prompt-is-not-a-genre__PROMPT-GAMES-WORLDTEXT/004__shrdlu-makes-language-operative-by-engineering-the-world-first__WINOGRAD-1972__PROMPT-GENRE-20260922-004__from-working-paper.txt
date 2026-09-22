ZETTEL

ID:
PROMPT-GENRE-20260922-004

TITLE:
SHRDLU makes language operative by engineering the world first

SOURCE:
Terry Winograd, "Understanding Natural Language," Cognitive Psychology 3(1), 1972.

SOURCE URL:
https://www.sciencedirect.com/science/article/pii/0010028572900023

PASSAGE:
[PARAPHRASE]\nWinograd's system answers questions, executes commands, and accepts information in English within a deliberately modeled blocks-world domain.

RESEARCH OBJECT:
[OUR INFERENCE]\nRELIABLE NATURAL-LANGUAGE ACTION CAN DEPEND ON PRIOR WORLD CLOSURE.

LOCAL MOVE:
Use SHRDLU as the opposite pole from general-purpose chat: narrow world, strong reference.

SOURCE TERMS:
microworld; blocks world; language understanding; planning

WHAT BECAME STRANGE:
The apparent naturalness of the command depends on an unusually explicit ontology, planner, memory, and action space.

QUESTION:
How much world engineering is hidden behind a short successful command?

DEEPER QUESTION:
What is the modern equivalent of the blocks world when prompts act over files, code, CAD, or physical tools?

MECHANISM:
A bounded domain limits candidate referents and legal actions, making ambiguity and consequence tractable.

FORMAL SHIFT:
ENGINEER_WORLD_FIRST -> COMPACT_OPERATIVE_LANGUAGE.

SOURCE FORMALISM:
[PARAPHRASE]\nThe language system is tied to a detailed model of the domain it discusses.

OUR FORMALIZATION:
Prompt = compact address into ontology + planner + memory + action space.

TENSION:
Closure buys reliability by excluding the open-ended background of ordinary human activity.

MISSING:
Comparative map from contemporary tool schemas and sandboxes to classic microworld closure.

BOUNDARY:
SHRDLU's domain is deliberately narrow; its success should not be generalized to unrestricted natural language.

CITATION TRAIL:
Winograd -> blocks world -> grounded command -> world-first prompting.

TEST:
Vary domain closure while holding command wording constant; measure reference and action failures.

PLATFORM:
SHRDLU; grounded language; world models

LINKS:
[[PROMPT-GENRE-20260922-005]]
[[PROMPT-GENRE-20260922-012]]

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
