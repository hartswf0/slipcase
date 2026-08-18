ZETTEL

ID: PF-011

TITLE:
Output-only attribution loses upstream human information.

SOURCE:
Xie et al. — Measuring Human Contribution in AI-Assisted Content Generation — 2026.

PASSAGE:
[PARAPHRASE] The authors explicitly note that the same output may arise from inputs carrying very different degrees of human contribution, making output-only estimation lossy.

RESEARCH OBJECT:
Identical-looking text can have different production histories.

LOCAL MOVE:
The contribution model conditions on human input rather than inferring provenance only from the final artifact.

SOURCE TERMS:
human contribution; input; output; mutual information.

WHAT BECAME STRANGE:
The phrase “AI-generated text” may identify a production mechanism while remaining almost silent about human causal structure.

QUESTION:
How much upstream history is required to distinguish materially different production processes?

DEEPER QUESTION:
What human work remains invisible even when both input and output are preserved?

MECHANISM:
<human input>
→ <AI generation>
→ [compare information relation]
→ <contribution estimate>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Information-theoretic contribution metric.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
OUTPUT EQUIVALENCE ≠ PROCESS EQUIVALENCE.

TENSION:
Adding prompt text to the analysis still omits rejection, model choice, source curation, iteration, and validation.

MISSING:
An interaction graph rather than an input/output pair.

BOUNDARY:
The study does not invalidate the category “AI-generated”; it shows that category is insufficient for contribution estimation.

CITATION TRAIL:
CoAuthor; Humanly; W3C PROV.

TEST:
Construct indistinguishable final passages through radically different human-AI processes and ask whether evaluators can classify contribution from output alone.

PLATFORM:
[[Process Is Not Visible in Product]]

LINKS:
[[Output-Only Attribution]]
[[Human Contribution]]
[[Provenance Graph]]

BIBTEX:
@inproceedings{xie2026humancontribution,
  author={Yueqi Xie and Tao Qi and Jingwei Yi and Xiyuan Yang and Ryan Whalen and Junming Huang and Qian Ding and Yu Xie and Xing Xie and Fangzhao Wu},
  title={Measuring Human Contribution in AI-Assisted Content Generation},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},
  year={2026},
  pages={6168--6190}
}