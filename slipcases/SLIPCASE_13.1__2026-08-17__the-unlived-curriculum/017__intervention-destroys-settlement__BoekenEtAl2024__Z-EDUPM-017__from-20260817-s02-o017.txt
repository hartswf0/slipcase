ZETTEL

ID:
Z-EDUPM-017

TITLE:
AFTER AN ALARM CHANGES ACTION, OBSERVED OUTCOMES NO LONGER ESTIMATE BASELINE RISK: RETRAINING MUST CROSS A CAUSAL DOMAIN SHIFT.

SOURCE:
Philip Boeken, Onno Zoeter, and Joris M. Mooij — Evaluating and Correcting Performative Effects of Decision Support Systems via Causal Domain Shift — 2024 — CLeaR, PMLR 236, 551–569.

SOURCE URL:
https://proceedings.mlr.press/v236/boeken24a.html

PASSAGE:
[PARAPHRASE] In an alarm-type decision support system, effective action induced by an earlier model changes later outcomes. Naively retraining on those data can underestimate risk. The authors model deployment as causal domain shift and target performance under a baseline policy.

RESEARCH OBJECT:
The relevant settlement condition after deployment is policy-indexed: outcome under the deployed intervention is not the same object as baseline risk.

LOCAL MOVE:
Boeken et al. replace the vague idea of feedback with an explicit causal cross-domain problem.

SOURCE TERMS:
decision support system
performative effects
causal domain shift
alarm
baseline policy
risk
sample selection

WHAT BECAME STRANGE:
“Accuracy after deployment” can compare quantities produced under different policies as if they came from one unchanged world.

QUESTION:
What should count as settlement for an educational warning once the warning has altered the policy under which the outcome is generated?

DEEPER QUESTION:
Should intervention-coupled predictors be evaluated as policies rather than isolated estimators?

MECHANISM:
model → alarm → intervention policy → shifted outcome distribution → retraining under old policy → underestimated baseline risk

FORMAL SHIFT:
<BASELINE DOMAIN>
→ <DEPLOYED DECISION SUPPORT>
→ [CHANGE ACTION]
→ <SHIFTED DOMAIN>
→ [RETRAIN]
→ <POLICY-CONDITIONED ESTIMATE>

SOURCE FORMALISM:
The paper represents deployment as causal domain shift and distinguishes a target under a baseline policy from observations under the deployed policy.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Evaluation needs Risk(M | policy), not only Risk(M), because policy changes which outcomes become observable.

TENSION:
Recovering a baseline requires identification assumptions. “Correct the feedback” can overstate what the available data permit.

MISSING:
In educational deployments: explicit mappings from scores to interventions and a defensible baseline policy.

BOUNDARY:
The source studies decision support systems generally; it does not prove that a particular university system satisfies its assumptions.

CITATION TRAIL:
[[Z-EDUPM-003]] → anti-settlement problem → [[Z-EDUPM-016]] → intervention-conditioned labels → Boeken et al. 2024

TEST:
Write the actual intervention policy triggered by each risk state, then test whether post-deployment retraining changes when evaluation targets a no-alert or baseline policy.

PLATFORM:
[[PREDICTION AS INTERVENTION POLICY]]

LINKS:
[[Z-EDUPM-003]]
[[Z-EDUPM-016]]
[[Baseline Policy]]
[[Performative Bias]]
[[Causal Domain Shift]]

BIBTEX:
@InProceedings{pmlr-v236-boeken24a,
  title={Evaluating and Correcting Performative Effects of Decision Support Systems via Causal Domain Shift},
  author={Boeken, Philip and Zoeter, Onno and Mooij, Joris},
  booktitle={Proceedings of the Third Conference on Causal Learning and Reasoning},
  pages={551--569}, year={2024}, volume={236},
  series={Proceedings of Machine Learning Research}, publisher={PMLR},
  url={https://proceedings.mlr.press/v236/boeken24a.html}
}