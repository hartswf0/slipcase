ZETTEL

ID:
Z-EDUPM-016

TITLE:
A SUCCESSFUL INTERVENTION CAN MAKE ITS OWN RISK MODEL LOOK WRONG: POST-INTERVENTION LABELS ARE GENERATED UNDER THE POLICY THE MODEL CAUSED.

SOURCE:
James Liley, Samuel Emerson, Bilal Mateen, Catalina Vallejos, Louis Aslett, and Sebastian Vollmer — Model updating after interventions paradoxically introduces bias — 2021 — AISTATS, PMLR 130, 3916–3924.

SOURCE URL:
https://proceedings.mlr.press/v130/liley21a.html

PASSAGE:
[PARAPHRASE] When a predictive score guides interventions before an outcome is observed, successful intervention changes the data available for later model updating. A replacement model trained naively on those observations may learn the effect of the previous score rather than untreated risk.

RESEARCH OBJECT:
A prediction can be a victim of its own success: the more effectively it triggers prevention, the less its future training data resemble the untreated world in which the warning mattered.

LOCAL MOVE:
Liley et al. turn feedback into a model-updating problem. The old score becomes part of the data-generating process for the next score.

SOURCE TERMS:
prediction score
intervention
model updating
naive model replacement
counterfactual
bias
hold-out set
controlled interventions

WHAT BECAME STRANGE:
The label “nothing bad happened” can mean either there was little risk or that risk was real and intervention worked. Those observations look alike but imply opposite institutional lessons.

QUESTION:
Can a successful educational early-warning system erase from its retraining data the evidence that its intervention was necessary?

DEEPER QUESTION:
What institutional memory must survive so that prevention does not become indistinguishable from absence of risk?

MECHANISM:
features → risk score → intervention → changed outcome → post-intervention training set → replacement model

FORMAL SHIFT:
<UNTREATED RISK>
→ <DEPLOYED SCORE>
→ [TRIGGER INTERVENTION]
→ <POST-INTERVENTION OUTCOME>
→ [NAIVE RETRAINING]
→ <BIASED REPLACEMENT>

SOURCE FORMALISM:
The paper distinguishes the untreated outcome relation from the outcome distribution generated after a deployed score drives interventions; the untreated baseline can become counterfactual.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Y(0) = untreated outcome.
Y(A(R0(X))) = observed outcome after score-triggered action.
Training R1 on observed Y estimates a policy-conditioned outcome relation rather than simply Y(0).

TENSION:
This does not license treating every false positive as a successful rescue. The untreated counterfactual still has to be identified.

MISSING:
A recoverable untreated-risk estimate or design separating baseline risk from the effects of prior interventions.

BOUNDARY:
The source analyzes intervention-driven updating generally, not higher education specifically. The educational application is our inference.

CITATION TRAIL:
[[Z-EDUPM-003]] → self-defeating warning → Liley et al. 2021 → naive model replacement
[[Z-EDUPM-009]] → prediction changes its data-generating world → updating under intervention

TEST:
Compare naive post-intervention retraining with a holdout or explicit intervention model. Test whether apparent risk declines concentrate where intervention was effective.

PLATFORM:
[[EDUCATION AS PERFORMATIVE PREDICTION]]

LINKS:
[[Z-EDUPM-003]]
[[Z-EDUPM-009]]
[[Naive Model Replacement]]
[[Institutional Forgetting]]
[[Untreated Baseline]]

BIBTEX:
@InProceedings{pmlr-v130-liley21a,
  title={Model updating after interventions paradoxically introduces bias},
  author={Liley, James and Emerson, Samuel and Mateen, Bilal and Vallejos, Catalina and Aslett, Louis and Vollmer, Sebastian},
  booktitle={Proceedings of The 24th International Conference on Artificial Intelligence and Statistics},
  pages={3916--3924}, year={2021}, volume={130},
  series={Proceedings of Machine Learning Research}, publisher={PMLR},
  url={https://proceedings.mlr.press/v130/liley21a.html}
}