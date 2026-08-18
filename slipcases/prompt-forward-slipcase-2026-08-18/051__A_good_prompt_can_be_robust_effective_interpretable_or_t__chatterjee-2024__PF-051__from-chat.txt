ZETTEL

ID: PF-051

TITLE:
A good prompt can be robust, effective, interpretable, or transferable—and these need not coincide.

SOURCE:
Chatterjee et al. — POSIX — 2024.

PASSAGE:
[PARAPHRASE] POSIX isolates sensitivity to intent-preserving changes, demonstrating that prompt performance can depend strongly on superficial formulation.

RESEARCH OBJECT:
“Prompt quality” is multidimensional.

LOCAL MOVE:
The source turns one hidden dimension—surface-form sensitivity—into a measurable property.

SOURCE TERMS:
prompt sensitivity; intent-preserving; robustness.

WHAT BECAME STRANGE:
The key that opens one lock reliably may fail after the lock receives a software update.

QUESTION:
What dimensions belong in a scholarly prompt-quality profile?

DEEPER QUESTION:
Can a prompt be methodologically strong if it is effective but brittle?

MECHANISM:
<prompt variants>
→ <same intended task>
→ [model execution]
→ <performance variance>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
POSIX.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
QUALITY = effectiveness × robustness × transferability × inspectability.

TENSION:
Optimizing all dimensions simultaneously may be impossible.

MISSING:
Empirically justified dimensions and tradeoffs.

BOUNDARY:
POSIX measures sensitivity, not overall prompt quality.

CITATION TRAIL:
PromptBench; reliability engineering; instrument calibration.

TEST:
Evaluate a set of famous prompts along independent quality dimensions and inspect rank reversals.

PLATFORM:
[[Prompt Quality Is a Vector]]

LINKS:
[[Robustness]]
[[Prompt Quality]]
[[Transferability]]

BIBTEX:
@inproceedings{chatterjee2024posix,
  author={Anwoy Chatterjee and H. S. V. N. S. Kowndinya Renduchintala and Sumit Bhatia and Tanmoy Chakraborty},
  title={POSIX: A Prompt Sensitivity Index For Large Language Models},
  booktitle={Findings of EMNLP 2024},
  year={2024}
}