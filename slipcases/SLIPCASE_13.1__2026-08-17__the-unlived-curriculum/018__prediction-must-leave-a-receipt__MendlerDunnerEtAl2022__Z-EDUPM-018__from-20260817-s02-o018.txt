ZETTEL

ID:
Z-EDUPM-018

TITLE:
A PREDICTION THAT CHANGES OUTCOMES MUST BE RECORDED AS PART OF THE CAUSAL HISTORY: OTHERWISE ITS EFFECT MAY BE UNIDENTIFIABLE.

SOURCE:
Celestine Mendler-Dünner, Frances Ding, and Yixin Wang — Anticipating Performativity by Predicting from Predictions — 2022 — Advances in Neural Information Processing Systems 35.

SOURCE URL:
https://proceedings.neurips.cc/paper_files/paper/2022/hash/ca09b375e8e2b2c789698c079a9fc51c-Abstract-Conference.html

PASSAGE:
[PARAPHRASE] When predictions affect outcomes, their causal effect may not be identifiable from ordinary feature-and-outcome data because the prediction is a deterministic function of features. The paper identifies conditions that restore identification and emphasizes recording deployed predictions.

RESEARCH OBJECT:
A consequential prediction becomes a treatment variable whose value must survive in the record if later analysis is to reconstruct its effect.

LOCAL MOVE:
Mendler-Dünner et al. make the deployed prediction itself part of the causal object.

SOURCE TERMS:
performativity
prediction
causal effect
identification
intervention
data collection
randomization
overparameterization

WHAT BECAME STRANGE:
Logging a score is not merely telemetry when the score changes advising or opportunity; forgetting it can erase the causal history that produced the outcome.

QUESTION:
Should institutions treat consequential predictions as intervention receipts linked to the outcomes they helped produce?

DEEPER QUESTION:
What is the minimum prediction/action provenance necessary for later causal audit without creating indefinite surveillance?

MECHANISM:
features → prediction → response/intervention → outcome; if prediction is not separately recorded, part of the pathway can be unidentified

FORMAL SHIFT:
<FEATURE RECORD>
→ <PREDICTION>
→ [DEPLOY]
→ <PERFORMATIVE RESPONSE>
→ <OUTCOME + PREDICTION RECEIPT>

SOURCE FORMALISM:
The paper treats deployed predictions as causal intervention variables and studies identification from data including features, outcomes, and predictions under specified conditions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Event record: (features, model version, score, displayed category, action, outcome), rather than only (features, outcome).

TENSION:
More logging can improve auditability while increasing surveillance and governance burdens.

MISSING:
A principled minimum-retention rule for causal evaluation.

BOUNDARY:
The source provides identification results, not an educational data-retention policy.

CITATION TRAIL:
[[Z-EDUPM-002]] → recommendation changes choice → [[Z-EDUPM-017]] → baseline depends on policy → predictions must remain observable

TEST:
Attempt the same causal evaluation with and without historic model version, score, recipient, and action fields. Record what becomes unidentified.

PLATFORM:
[[PREDICTION AS INTERVENTION POLICY]]

LINKS:
[[Z-EDUPM-002]]
[[Z-EDUPM-017]]
[[Prediction as Treatment]]
[[Logged Predictions as Causal Infrastructure]]
[[Data Collection for Performativity]]

BIBTEX:
@inproceedings{mendlerdunner2022anticipating,
  title={Anticipating Performativity by Predicting from Predictions},
  author={Mendler-D{"u}nner, Celestine and Ding, Frances and Wang, Yixin},
  booktitle={Advances in Neural Information Processing Systems},
  volume={35}, year={2022},
  url={https://proceedings.neurips.cc/paper_files/paper/2022/hash/ca09b375e8e2b2c789698c079a9fc51c-Abstract-Conference.html}
}