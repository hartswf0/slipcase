ZETTEL

ID: PF-002

TITLE:
Amount of interaction and amount of contribution are different variables.

SOURCE:
Xie et al. — Measuring Human Contribution in AI-Assisted Content Generation — 2026 — contribution framework.

PASSAGE:
[PARAPHRASE] Xie et al. model human contribution through information carried from human input into the resulting output rather than treating AI involvement as a binary property.

RESEARCH OBJECT:
Contribution can be continuous without being equivalent to interaction volume.

LOCAL MOVE:
The paper replaces AI-detection with an attempt to quantify how much human input conditions an output.

SOURCE TERMS:
human contribution; mutual information; self-information; AI-assisted content.

WHAT BECAME STRANGE:
A short input can theoretically carry more consequential information than a long input.

QUESTION:
Should AI scholarship distinguish interaction volume, informational influence, and intellectual judgment?

DEEPER QUESTION:
Can informational contribution capture choices such as rejection, source selection, or diagnosis that leave little lexical trace in the output?

MECHANISM:
<human input>
→ <conditional influence on output distribution>
→ [information-theoretic comparison]
→ <contribution score>

FORMAL SHIFT:
<human input>
→ <conditional output>
→ [measure information transmitted]
→ <estimated contribution>

SOURCE FORMALISM:
Human contribution is operationalized information-theoretically relative to output information.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
VOLUME ≠ INFLUENCE ≠ JUDGMENT.

TENSION:
A contribution measure may become more precise while still measuring the wrong kind of contribution for scholarship.

MISSING:
Selection, rejection, validation, and orchestration that do not survive as output text.

BOUNDARY:
The paper does not claim to measure scholarly authorship.

CITATION TRAIL:
Information theory of attribution; process-based writing analytics; provenance graphs.

TEST:
Construct pairs where a five-word prompt has high causal leverage and a thousand-word prompt has low leverage, then compare token-count and contribution metrics.

PLATFORM:
[[Contribution Without Token Counting]]

LINKS:
[[Human Contribution]]
[[Information Leverage]]
[[Interaction Volume]]

BIBTEX:
@inproceedings{xie2026humancontribution,
  author={Yueqi Xie and Tao Qi and Jingwei Yi and Xiyuan Yang and Ryan Whalen and Junming Huang and Qian Ding and Yu Xie and Xing Xie and Fangzhao Wu},
  title={Measuring Human Contribution in AI-Assisted Content Generation},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},
  year={2026},
  pages={6168--6190}
}