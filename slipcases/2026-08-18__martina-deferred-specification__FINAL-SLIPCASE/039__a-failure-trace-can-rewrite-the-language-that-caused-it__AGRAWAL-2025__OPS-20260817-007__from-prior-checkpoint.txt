ZETTEL

ID:
OPS-20260817-007

TITLE:
A failure trace can rewrite the language that caused it.

SOURCE:
Lakshya A. Agrawal et al. — “GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning” — 2025; accepted ICLR 2026.
https://arxiv.org/abs/2507.19457

PASSAGE:
[PARAPHRASE]
GEPA examines execution trajectories, reflects on them in natural language, diagnoses problems, proposes prompt changes, tests those changes, and retains useful lessons.

RESEARCH OBJECT:
FAILURE BECOMES SOURCE MATERIAL FOR PROGRAM REVISION.

LOCAL MOVE:
[[MJ-MARTINA-004]] showed a human doing:

failure
→ discovery
→ add something to template.

GEPA formalizes a strikingly similar loop at the system level.

The execution history becomes input to the mechanism that rewrites the instructions for the next execution.

SOURCE TERMS:
“trajectories”
“reasoning”
“tool calls”
“tool outputs”
“reflects”
“diagnose”
“prompt updates”
“trial and error”

WHAT BECAME STRANGE:
The prompt is no longer simply upstream of execution.

Execution returns downstream evidence that flows backward and changes the prompt.

The program's failures edit its future language.

QUESTION:
Can the genealogy of prompt corrections be treated as part of the executable specification rather than discarded optimization history?

DEEPER QUESTION:
If a prompt is produced from accumulated reflections over prior failures, is the real program the final text or the lineage that generated it?

MECHANISM:
GEPA samples trajectories from an AI system, uses natural-language reflection to diagnose behavior and propose prompt updates, evaluates variants, and combines useful lessons during optimization.

FORMAL SHIFT:
FROM:
PROMPT
→ EXECUTION
→ OUTPUT

TO:
PROMPT_t
→ EXECUTION_t
→ TRACE_t
→ REFLECTION_t
→ PROMPT_t+1
→ EXECUTION_t+1.

SOURCE FORMALISM:
[PARAPHRASE]
GEPA uses:
system trajectories,
natural-language reflection,
prompt mutation/proposal,
evaluation,
Pareto-aware candidate selection.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SPEC_t+1
=
REVISE(
  SPEC_t,
  FAILURE_TRACE_t,
  SUCCESS_TRACE_t,
  METRIC
)

Therefore:

CURRENT_PROMPT
is a compressed residue of prior executions.

TENSION:
Optimizers typically care about producing a better current candidate, while research provenance may require retaining the failed variants and causal history that produced it.

MISSING:
A representation in which correction lineage remains queryable and executable rather than disappearing after optimization.

BOUNDARY:
GEPA's optimization procedure does not imply every revision corresponds to a true or human-legible specification improvement.

CITATION TRAIL:
[[MJ-MARTINA-004]]
→ Martina manually stores lessons from trial and error
→ GEPA operationalizes trace → reflection → prompt update
→ failure becomes instruction-generating evidence
→ specification becomes genealogical.

TEST:
Preserve every:
prompt version,
execution trace,
failure diagnosis,
proposed correction,
metric score.

Then remove the final prompt.

Attempt to reconstruct it only from the correction lineage.

If reconstruction is possible, test whether the lineage explains the system better than the final prompt alone.

PLATFORM:
GEPA; DSPy-compatible language-model programs

LINKS:
[[MJ-MARTINA-004]]
[[MJ-MARTINA-014-A-A]]
[[OPS-20260817-006]]

BIBTEX:
@misc{agrawal2025gepa,
  title = {GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning},
  author = {Agrawal, Lakshya A. and Tan, Shangyin and Soylu, Dilara and Ziems, Noah and Khare, Rishi and Opsahl-Ong, Krista and Singhvi, Arnav and Shandilya, Herumb and Ryan, Michael J. and Jiang, Meng and Potts, Christopher and Sen, Koushik and Dimakis, Alexandros G. and Stoica, Ion and Klein, Dan and Zaharia, Matei and Khattab, Omar},
  year = {2025},
  eprint = {2507.19457},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2507.19457}
}
