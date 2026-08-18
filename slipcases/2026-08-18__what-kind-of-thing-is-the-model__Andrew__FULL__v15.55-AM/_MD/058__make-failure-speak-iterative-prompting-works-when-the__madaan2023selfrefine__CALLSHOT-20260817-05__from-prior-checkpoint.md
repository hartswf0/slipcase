ZETTEL

ID:
CALLSHOT-20260817-05

TITLE:
MAKE FAILURE SPEAK — iterative prompting works when the failed artifact is converted into instructions for its own replacement.

SOURCE:
Aman Madaan et al. — “Self-Refine: Iterative Refinement with Self-Feedback” — 2023.
https://arxiv.org/abs/2303.17651

PASSAGE:
[PARAPHRASE]
Self-Refine first generates an output, then uses the same language model to produce feedback on that output, then supplies the output and feedback back to the model for refinement. This cycle is repeated without requiring additional model training.

RESEARCH OBJECT:
FAILURE-TO-INSTRUCTION-TRANSDUCTION.

LOCAL MOVE:
[[MJ-GC-005]] showed:

“that’s not what I asked for”
→ investigate the discrepancy.

Here discrepancy is operationalized.

Do not merely retry.

TURN THE DEFECT INTO LANGUAGE.

Feed that language into the next generation.

The failed output becomes raw material for a more precise specification.

SOURCE TERMS:
“initial output”
“feedback”
“refinement”
“iteratively”
“generator”
“refiner”
“feedback provider”

WHAT BECAME STRANGE:
The specification can be written after the artifact exists.

You may not know what instruction was missing until you see the failure that omission creates.

QUESTION:
What kinds of failure are legible enough that converting them into verbal feedback reliably improves the next generation?

DEEPER QUESTION:
Is the true programming unit of natural-language systems not instruction but:

PROVISIONAL ARTIFACT
→ DIAGNOSIS
→ NEW CONSTRAINT
→ REGENERATION?

MECHANISM:
GENERATE O₀

FEEDBACK:
F₀ = CRITIQUE(O₀)

REFINE:
O₁ = MODEL(O₀ + F₀)

repeat until stopping criterion.

FORMAL SHIFT:
FROM:
SPECIFICATION
→ ARTIFACT.

TO:
SPECIFICATION₀
→ ARTIFACT₀
→ FAILURE
→ SPECIFICATION₁
→ ARTIFACT₁.

SOURCE FORMALISM:
Self-Refine uses an iterative FEEDBACK → REFINE loop in which the same LLM can serve as generator, feedback provider, and refiner.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

FAILURE
becomes useful when:

DIAGNOSE(artifact)
→ CONSTRAINT_new.

Then:

SPEC_{t+1}
=
SPEC_t
∪ CONSTRAINT_new.

TENSION:
A model criticizing itself can reproduce the same blind spot that produced the original error.

Self-feedback is therefore not equivalent to independent verification.

MISSING:
A clear boundary between failures detectable from the artifact itself and failures requiring an external judge, simulator, compiler, user, or world.

BOUNDARY:
Self-refinement cannot repair an error the feedback process fails to recognize.

CITATION TRAIL:
[[MJ-GC-005]]
→ unexpected output changes intention
→ Self-Refine
→ output is inspected
→ failure is verbalized
→ verbalized failure becomes next instruction.

TEST:
For each failed AI artifact, do not manually rewrite the original prompt.

Instead produce exactly:

OBSERVED FAILURE:
WHY IT MATTERS:
NEW CONSTRAINT:

append the new constraint and regenerate.

Track whether accepted constraints accumulate into a reusable specification.

PLATFORM:
Large language models

LINKS:
[[MJ-GC-005]]
[[MJ-GC-030-B-B]]
[[CALLSHOT-20260817-04]]

BIBTEX:
@article{madaan2023selfrefine,
  title={Self-Refine: Iterative Refinement with Self-Feedback},
  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
  journal={arXiv preprint arXiv:2303.17651},
  year={2023},
  url={https://arxiv.org/abs/2303.17651}
}
