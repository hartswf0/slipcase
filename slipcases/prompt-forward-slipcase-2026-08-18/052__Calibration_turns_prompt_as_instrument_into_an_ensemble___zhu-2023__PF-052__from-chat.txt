ZETTEL

ID: PF-052

TITLE:
Calibration turns “prompt as instrument” into an ensemble claim.

SOURCE:
Zhu et al. — PromptBench — 2023.

PASSAGE:
[PARAPHRASE] PromptBench evaluates prompt/model behavior across multiple tasks, models, prompt methods, and perturbations.

RESEARCH OBJECT:
A prompt cannot be calibrated independently of the environment in which its behavior is measured.

LOCAL MOVE:
The source creates standardized conditions for comparison.

SOURCE TERMS:
benchmark; model; prompt; adversarial; evaluation.

WHAT BECAME STRANGE:
The instrument may not be the prompt at all; it may be the complete execution envelope.

QUESTION:
What is the smallest execution envelope that must accompany a scholarly prompt?

DEEPER QUESTION:
How should prompt methods survive proprietary model updates that make exact replication impossible?

MECHANISM:
<prompt + model + task + parameters>
→ <execution>
→ [benchmark]
→ <performance profile>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Benchmark framework.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROMPT RECEIPT must include execution envelope, not text alone.

TENSION:
An overly complete envelope becomes burdensome and rapidly obsolete.

MISSING:
Standards for functional replication under model drift.

BOUNDARY:
Benchmark reproducibility and scholarly reproducibility are not identical.

CITATION TRAIL:
Model versioning; computational reproducibility.

TEST:
Re-run a prompt instrument across successive model versions and define what level of behavioral equivalence counts as replication.

PLATFORM:
[[Execution Envelope]]

LINKS:
[[Calibration]]
[[Model Drift]]
[[Prompt Receipt]]

BIBTEX:
@article{zhu2023promptbench,
  author={Kaijie Zhu and Qinlin Zhao and Hao Chen and Jindong Wang and Xing Xie},
  title={PromptBench: A Unified Library for Evaluation of Large Language Models},
  journal={arXiv preprint arXiv:2312.07910},
  year={2023}
}