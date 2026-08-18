ZETTEL

ID: PF-023

TITLE:
Prompt templates can occupy the same repository stratum as simulation code.

SOURCE:
StanfordHCI — genagents repository — 2024 — Repository Structure.

PASSAGE:
[PARAPHRASE] The repository identifies `simulation_engine/prompt_template/` as containing all LLM prompts used in the project and configures an `LLM_PROMPT_DIR` pointing to it.

RESEARCH OBJECT:
In an implemented generative system, prompts can be packaged as named architectural assets rather than disposable conversations.

LOCAL MOVE:
The repository gives prompts a concrete filesystem location inside the simulation engine.

SOURCE TERMS:
simulation_engine; prompt_template; LLM_PROMPT_DIR; prompts.

WHAT BECAME STRANGE:
Technical practice answers “where is the prompt?” materially: it has a directory.

QUESTION:
When does repository placement make a prompt part of the inspectable scientific apparatus?

DEEPER QUESTION:
Would deleting or changing the prompt directory alter claims of reproducibility enough that prompts should be treated as research artifacts?

MECHANISM:
<prompt templates>
→ <simulation engine resource>
→ [LLM calls]
→ <agent behavior>

FORMAL SHIFT:
<prompt text>
→ <versioned repository artifact>
→ [runtime invocation]
→ <simulation behavior>

SOURCE FORMALISM:
Repository architecture.

OUR FORMALIZATION:
NONE

TENSION:
Being executable source material does not by itself make an artifact intellectually novel or independently publishable.

MISSING:
Ablation or version history showing which prompt templates materially determine scientific findings.

BOUNDARY:
Repository inclusion establishes operational use, not authorship status.

CITATION TRAIL:
Generative Agents paper; repository commits; prompt-template diffs.

TEST:
Remove or systematically perturb prompt templates and measure which reported agent behaviors survive.

PLATFORM:
[[Prompt as Research Infrastructure]]

LINKS:
[[Generative Agents]]
[[Prompt Template]]
[[Executable Artifact]]

BIBTEX:
@misc{stanfordhci2024genagents,
  author={{StanfordHCI}},
  title={genagents},
  year={2024},
  howpublished={GitHub repository},
  url={https://github.com/joonspk-research/genagents}
}