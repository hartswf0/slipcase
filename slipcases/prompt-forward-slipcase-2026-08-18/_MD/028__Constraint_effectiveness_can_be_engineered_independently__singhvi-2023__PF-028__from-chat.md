ZETTEL

ID: PF-028

TITLE:
Constraint effectiveness can be engineered independently of authorship status.

SOURCE:
Singhvi et al. — DSPy Assertions — 2023.

PASSAGE:
[PARAPHRASE] DSPy Assertions lets developers state computational constraints on language-model outputs and use failures to trigger self-refinement.

RESEARCH OBJECT:
A linguistic constraint can have measurable engineering value without resolving who authored the resulting expression.

LOCAL MOVE:
The paper makes prompt-like constraints components of a performance-improving pipeline.

SOURCE TERMS:
assertions; computational constraints; self-refinement; pipeline.

WHAT BECAME STRANGE:
The more consequential an instruction becomes computationally, the less useful sentence-level authorship may become as the sole contribution measure.

QUESTION:
Should capability-producing constraints be evaluated as software/method contributions even when copyright authorship remains weak?

DEEPER QUESTION:
What kinds of scholarly credit attach to constraints that reliably alter behavior but do not determine expression?

MECHANISM:
<constraint>
→ <model output>
→ [assert / fail / refine]
→ <greater rule compliance>

FORMAL SHIFT:
<constraint text>
→ <executable assertion>
→ [check and regenerate]
→ <controlled behavior>

SOURCE FORMALISM:
DSPy Assertions.

OUR FORMALIZATION:
NONE

TENSION:
Effectiveness is evidence of causal contribution, not automatically of novelty or intellectual significance.

MISSING:
Criteria for scholarly originality of behavioral constraints.

BOUNDARY:
The paper evaluates pipeline performance, not authorship.

CITATION TRAIL:
Software contribution; specification languages; copyright report.

TEST:
Compare scholarly evaluation of a novel assertion architecture with evaluation of the prose it causes a model to emit.

PLATFORM:
[[Capability Without Expressive Authorship]]

LINKS:
[[DSPy Assertions]]
[[Constraint]]
[[Scholarly Credit]]

BIBTEX:
@article{singhvi2023assertions,
  author={Arnav Singhvi and Manish Shetty and Shangyin Tan and Christopher Potts and Koushik Sen and Matei Zaharia and Omar Khattab},
  title={DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines},
  journal={arXiv preprint arXiv:2312.13382},
  year={2023}
}