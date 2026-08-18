ZETTEL

ID:
Z-EDUPM-019

TITLE:
WITH SELECTIVE LABELS, THE LEARNING PROBLEM MOVES FROM PREDICTION TO POLICY: SOME KNOWLEDGE REQUIRES DELIBERATE EXPLORATION.

SOURCE:
Niki Kilbertus, Manuel Gomez Rodriguez, Bernhard Schölkopf, Krikamol Muandet, and Isabel Valera — Fair Decisions Despite Imperfect Predictions — 2020 — AISTATS, PMLR 108, 277–287.

SOURCE URL:
https://proceedings.mlr.press/v108/kilbertus20a.html

PASSAGE:
[PARAPHRASE] With selective labels, optimizing a predictive model and applying a deterministic rule can be inferior to directly learning a stochastic decision policy. Exploring policies can reveal outcomes a deterministic policy never observes.

RESEARCH OBJECT:
Some missing counterfactuals cannot be recovered by a better predictor; the institution must change what it does in order to learn what its current policy prevents it from seeing.

LOCAL MOVE:
Kilbertus et al. shift the learning target from prediction to decision.

SOURCE TERMS:
selective labels
learning to predict
learning to decide
stochastic policy
exploration
utility
fairness

WHAT BECAME STRANGE:
Knowledge may require deliberately non-greedy action. A recommender that always chooses the apparent safest path can prevent itself from learning about excluded paths.

QUESTION:
What forms of educational exploration are necessary to learn about trajectories a recommender would otherwise suppress?

DEEPER QUESTION:
Who bears the cost of experiments required to make a decision system epistemically corrigible?

MECHANISM:
historical policy → selective observation → deterministic decision → same blind spot; exploring policy → varied decisions → new outcomes → policy learning

FORMAL SHIFT:
<SELECTIVELY LABELED HISTORY>
→ <DECISION POLICY>
→ [EXPLORE]
→ <NEW OUTCOMES>
→ <LEARN TO DECIDE>

SOURCE FORMALISM:
The paper optimizes stochastic decision policies under selective labels and fairness constraints, contrasting direct policy learning with prediction plus thresholding.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
If a policy gives an action zero probability for a population region, it may create no labels for that counterfactual action there. Exploration opens an observational channel but is not ethically free.

TENSION:
Exploration can improve learning while exposing people to actions not selected as the current estimated optimum.

MISSING:
A theory of legitimate educational exploration: consent, reversibility, risk limits, and distribution of burden.

BOUNDARY:
The source is not specifically about course recommendation; the application follows from the selective-label structure.

CITATION TRAIL:
[[Z-EDUPM-010]] → unlived outcomes → [[Z-EDUPM-013]] → recommendation produces observation → learning to decide

TEST:
Compare deterministic recommendation, bounded exploration, and direct policy learning; measure both knowledge gain and who bears exploratory cost.

PLATFORM:
[[THE UNLIVED CURRICULUM]]

LINKS:
[[Z-EDUPM-010]]
[[Z-EDUPM-013]]
[[Selective Labels]]
[[Ethical Exploration]]
[[Policy Learning]]

BIBTEX:
@InProceedings{pmlr-v108-kilbertus20a,
  title={Fair Decisions Despite Imperfect Predictions},
  author={Kilbertus, Niki and Rodriguez, Manuel Gomez and Sch{"o}lkopf, Bernhard and Muandet, Krikamol and Valera, Isabel},
  booktitle={Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics},
  pages={277--287}, year={2020}, volume={108},
  series={Proceedings of Machine Learning Research}, publisher={PMLR},
  url={https://proceedings.mlr.press/v108/kilbertus20a.html}
}