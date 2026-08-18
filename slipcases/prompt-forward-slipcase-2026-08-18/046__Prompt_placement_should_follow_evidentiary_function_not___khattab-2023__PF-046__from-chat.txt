ZETTEL

ID: PF-046

TITLE:
Prompt placement should follow evidentiary function, not a universal appendix rule.

SOURCE:
Khattab et al. — DSPy — 2023.

PASSAGE:
[PARAPHRASE] DSPy treats model-facing specifications as programmable components of language-model pipelines.

RESEARCH OBJECT:
A prompt can occupy source-code-like, methodological, evidentiary, or illustrative roles.

LOCAL MOVE:
The paper makes prompts operational components rather than merely documentation.

SOURCE TERMS:
module; pipeline; declarative; compiler.

WHAT BECAME STRANGE:
“Put your prompts in the appendix” assumes prompts are supplementary evidence before asking what role they perform.

QUESTION:
Where should a prompt appear when the paper's contribution is the prompt program itself?

DEEPER QUESTION:
Can publication structure be determined by dependency: if the claim cannot be understood or reproduced without the prompt, must it move into the main scholarly object?

MECHANISM:
<prompt artifact>
→ <claim dependency>
→ [assess role]
→ <main text / methods / code / supplement>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
DSPy modules and pipeline representation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PLACEMENT = f(claim dependence, reproducibility role, artifact scale).

TENSION:
Main-text inclusion of large prompts can destroy readability.

MISSING:
Publication conventions for prompt artifacts.

BOUNDARY:
DSPy does not prescribe article layout.

CITATION TRAIL:
Artifact-evaluation policies; supplementary-material standards; literate programming.

TEST:
Analyze fifty prompt-centric papers and classify where load-bearing prompts are published and whether replication is possible.

PLATFORM:
[[Prompt Placement by Function]]

LINKS:
[[Appendix]]
[[Research Artifact]]
[[Reproducibility]]

BIBTEX:
@article{khattab2023dspy,
  author={Omar Khattab and Arnav Singhvi and Paridhi Maheshwari and Zhiyuan Zhang and Keshav Santhanam and others},
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  journal={arXiv preprint arXiv:2310.03714},
  year={2023}
}