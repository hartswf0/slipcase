ZETTEL

ID: PF-058

TITLE:
Capability claims are always indexed to a benchmark and system envelope.

SOURCE:
Khattab et al. — DSPy — 2023.

PASSAGE:
[PARAPHRASE] DSPy compiles language-model pipelines to optimize specified metrics across tasks and demonstrates performance improvements in evaluated settings.

RESEARCH OBJECT:
“Creates a capability” is incomplete without saying for which system, task, metric, and baseline.

LOCAL MOVE:
The source makes capability comparative and metric-bound.

SOURCE TERMS:
metric; compiler; pipeline; optimization; performance.

WHAT BECAME STRANGE:
A capability can disappear when the benchmark, model, or baseline changes.

QUESTION:
What evidence is required before calling a prompt-generated behavior a scholarly capability rather than a local performance gain?

DEEPER QUESTION:
How general must a capability be to count as an independent contribution?

MECHANISM:
<program/prompt pipeline>
→ <task/model>
→ [optimize/evaluate]
→ <metric improvement>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Metric-driven compilation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
CAPABILITY = comparative relation, not intrinsic property.

TENSION:
The aphorism calls capability “hardest evidence,” but capability claims can be benchmark artifacts.

MISSING:
Transfer and baseline robustness.

BOUNDARY:
DSPy results do not license general claims about any individual prompt.

CITATION TRAIL:
Benchmark validity; out-of-distribution evaluation.

TEST:
Require every claimed prompt capability to survive at least two models, tasks, and baseline prompt families.

PLATFORM:
[[Capability Is Indexed]]

LINKS:
[[DSPy]]
[[Capability]]
[[Benchmark]]

BIBTEX:
@article{khattab2023dspy,
  author={Omar Khattab and Arnav Singhvi and Paridhi Maheshwari and Zhiyuan Zhang and Keshav Santhanam and others},
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  journal={arXiv preprint arXiv:2310.03714},
  year={2023}
}