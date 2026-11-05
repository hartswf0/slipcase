ZETTEL

ID:
IMG-JEPA-02-A

TITLE:
Caption density begins with a rule about what to keep

SOURCE:
Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola — The Platonic Representation Hypothesis — 2024 — Appendix E

PASSAGE:
[QUOTE] “especially information from the start of the original description.”
[QUOTE] “the alignment score also improves as caption length increases.”

RESEARCH OBJECT:
The ordering of details in the parent description as a variable in caption-density experiments.

LOCAL MOVE:
The authors vary the requested word budget for summaries of an existing description. Their prompt also gives early details priority.

SOURCE TERMS:
Caption density, granularity, salient visual information, alignment score.

WHAT BECAME STRANGE:
[OUR INFERENCE] A longer summary may align better partly because it restores details previously excluded by an instruction that privileges the beginning. The caption’s order can determine which parts of the image become available for alignment.

QUESTION:
At a fixed word budget, does moving a visible detail to the beginning of the source description change whether that detail contributes to measured alignment?

DEEPER QUESTION:
If two equally accurate captions rank different aspects of one image as salient, which caption should a critic prefer?

MECHANISM:
A text-only model compresses a description under a word budget and a positional preference. The alignment measurement happens downstream of that selection.

FORMAL SHIFT:
<Ordered full description> → <word budget and priority instruction> → [summarization] → <caption used for alignment measurement>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
NONE

TENSION:
[OUR INFERENCE] The length effect could reflect broader coverage of the image, or recovery of particular details systematically excluded at shorter budgets. Both could be present.

MISSING:
An order intervention that keeps the image, source propositions, and word budget fixed.

BOUNDARY:
Appendix E’s reported length effect does not isolate the effect of ordering or of the instruction to favor the beginning.

CITATION TRAIL:
[[IMG-JEPA-02]] → Huh et al., Appendix E → Urbanek et al.’s Densely Captioned Images dataset and its description hierarchy.

TEST:
Swap the first and last blocks of each description without changing any wording. Run the same short and long summary prompts on both orders. Compare which propositions survive and whether changes in visual coverage track the alignment score.

PLATFORM:
[[Thick Prompting as Method]]

LINKS:
[[IMG-JEPA-02]]
[[Caption Order]]
[[Salience in Imagetext]]

BIBTEX:
@misc{huh2024platonic,
  author = {Huh, Minyoung and Cheung, Brian and Wang, Tongzhou and Isola, Phillip},
  title = {The Platonic Representation Hypothesis},
  year = {2024},
  eprint = {2405.07987},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/html/2405.07987}
}