ZETTEL

ID: PF-081

TITLE:
Double ablation could separate output dependence from architecture dependence.

SOURCE:
Xie et al. — Measuring Human Contribution in AI-Assisted Content Generation — 2026.

PASSAGE:
[PARAPHRASE] The paper argues that human contribution cannot be adequately inferred from generated output alone.

RESEARCH OBJECT:
A counterfactual experiment can remove different parts of a human-AI workflow separately.

LOCAL MOVE:
The source motivates looking beyond final output, but does not provide the proposed double ablation.

SOURCE TERMS:
human contribution; input; output; information.

WHAT BECAME STRANGE:
Two different questions hide inside “how much did AI matter?”:
Could the artifact survive without the machine output?
Could the capability survive without the human architecture?

QUESTION:
Can paired counterfactual removal distinguish machine textual contribution from human system contribution?

DEEPER QUESTION:
What if neither ablation is independently possible because the process is path-dependent?

MECHANISM:
<full workflow>
→ [remove AI outputs] / [remove human architecture]
→ <two counterfactual degradations>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Information-theoretic contribution.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ABLATE_OUTPUT and ABLATE_HUMAN_STRUCTURE.

TENSION:
Counterfactuals in iterative co-production may be ill-defined because later human actions depend on earlier machine outputs.

MISSING:
A causal design for path-dependent collaboration.

BOUNDARY:
The source does not endorse double ablation.

CITATION TRAIL:
Causal mediation; human-AI interaction experiments.

TEST:
Implement paired ablations on controlled chained-writing tasks and observe when counterfactual workflows become incoherent.

PLATFORM:
[[Double Ablation]]

LINKS:
[[Counterfactual]]
[[Human Contribution]]
[[AI Output]]

BIBTEX:
@inproceedings{xie2026humancontribution,
  author={Yueqi Xie and Tao Qi and Jingwei Yi and Xiyuan Yang and Ryan Whalen and Junming Huang and Qian Ding and Yu Xie and Xing Xie and Fangzhao Wu},
  title={Measuring Human Contribution in AI-Assisted Content Generation},
  booktitle={ACL},
  year={2026}
}