ZETTEL

ID: PF-035

TITLE:
Prompt templates can function as configuration even when written in natural language.

SOURCE:
StanfordHCI — genagents repository — 2024.

PASSAGE:
[PARAPHRASE] The simulation engine defines a prompt-template directory and invokes stored model-facing instructions as part of runtime behavior.

RESEARCH OBJECT:
Natural-language strings can occupy a configuration/code dependency position in software architecture.

LOCAL MOVE:
The repository operationalizes prompts as versionable resources.

SOURCE TERMS:
prompt_template; simulation_engine; LLM_PROMPT_DIR.

WHAT BECAME STRANGE:
“Natural language” and “configuration” are not mutually exclusive artifact categories.

QUESTION:
What makes a prompt configuration rather than conversation?

DEEPER QUESTION:
Should prompt templates inherit reproducibility expectations from source code when they control scientific simulations?

MECHANISM:
<stored prompt template>
→ <runtime loading>
→ [LLM call]
→ <simulation state change>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Repository/file architecture.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROMPT-AS-CONFIG iff versioned text is programmatically invoked in repeatable system operation.

TENSION:
A configuration file can be operationally indispensable while intellectually routine.

MISSING:
A criterion for novelty independent of runtime necessity.

BOUNDARY:
Filesystem location alone does not prove scholarly significance.

CITATION TRAIL:
Infrastructure-as-code; configuration management; prompt version control.

TEST:
Survey published LLM repositories for how prompts are stored, versioned, tested, and cited.

PLATFORM:
[[Natural Language as Configuration]]

LINKS:
[[Prompt Template]]
[[Configuration]]
[[Research Software]]

BIBTEX:
@misc{stanfordhci2024genagents,
  author={{StanfordHCI}},
  title={genagents},
  year={2024},
  howpublished={GitHub repository},
  url={https://github.com/joonspk-research/genagents}
}