ZETTEL

ID: PF-010

TITLE:
A prompt becomes instrument-like only when its calibration conditions are specified.

SOURCE:
Zhu et al. — PromptBench: A Unified Library for Evaluation of Large Language Models — 2023.

PASSAGE:
[PARAPHRASE] PromptBench provides common tasks, models, prompt-construction methods, adversarial tests, and evaluation procedures for examining model behavior under prompts.

RESEARCH OBJECT:
Instrumentality requires more than repeated success; it requires a known test environment.

LOCAL MOVE:
PromptBench turns prompting into comparative evaluation rather than isolated anecdote.

SOURCE TERMS:
evaluation; prompts; adversarial attack; benchmark; robustness.

WHAT BECAME STRANGE:
The “prompt as microscope” analogy imports calibration obligations that ordinary prompt practice rarely satisfies.

QUESTION:
What would constitute calibration documentation for a prompt used as a scholarly instrument?

DEEPER QUESTION:
Is the instrument the prompt, or the prompt + model + parameters + context + evaluation protocol?

MECHANISM:
<prompt>
→ <benchmark/model configuration>
→ [execute/evaluate]
→ <performance profile>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Benchmark framework.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
INSTRUMENT = P + M + CONTEXT + METRIC + VERSION.

TENSION:
Treating prompts as autonomous instruments may obscure dependence on proprietary and changing model infrastructure.

MISSING:
Calibration certificates for scholarly prompt instruments.

BOUNDARY:
PromptBench benchmarks LLMs; it does not claim prompts are scientific instruments.

CITATION TRAIL:
Metrology; experimental apparatus; model cards; software environments.

TEST:
Attempt to reproduce a prompt-based scholarly result after changing each member of the proposed instrument tuple individually.

PLATFORM:
[[Prompt Instrumentation]]

LINKS:
[[Calibration]]
[[PromptBench]]
[[Model-Prompt Ensemble]]

BIBTEX:
@article{zhu2023promptbench,
  author={Kaijie Zhu and Qinlin Zhao and Hao Chen and Jindong Wang and Xing Xie},
  title={PromptBench: A Unified Library for Evaluation of Large Language Models},
  journal={arXiv preprint arXiv:2312.07910},
  year={2023}
}