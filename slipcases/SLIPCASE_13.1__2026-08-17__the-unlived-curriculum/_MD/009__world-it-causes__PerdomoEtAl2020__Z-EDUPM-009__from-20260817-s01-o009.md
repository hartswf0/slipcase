ZETTEL

ID:
Z-EDUPM-009

TITLE:
A MODEL CAN BECOME CALIBRATED TO THE WORLD IT CAUSES RATHER THAN THE WORLD IT CLAIMS TO DESCRIBE.

SOURCE:
Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt — “Performative Prediction” — 2020 — Proceedings of the 37th International Conference on Machine Learning, pp. 7599–7609.

PASSAGE:
[QUOTE] “When predictions support decisions they may influence the outcome they aim to predict.”

RESEARCH OBJECT:
Performative stability: prediction can reach an equilibrium with the distribution produced by deploying the prediction itself.

LOCAL MOVE:
Perdomo et al. replace the ordinary assumption that predictions encounter a fixed target distribution with a setting in which deployment changes that distribution.

The strange object is not merely biased prediction.

It is a predictor whose apparent empirical world is partly downstream of itself.

SOURCE TERMS:
performative prediction
distribution shift
performative stability
retraining
strategic classification
risk minimization
future outcomes

WHAT BECAME STRANGE:
An educational risk system could become increasingly well calibrated while becoming decreasingly informative about the world that would exist without the system.

Suppose:

MODEL predicts student is unlikely to succeed in course X
→ advisor redirects student away from X
→ student never takes X
→ future population taking X contains fewer predicted low-success students
→ observed outcomes increasingly resemble model expectations.

The model can become stable by reorganizing its environment.

QUESTION:
When educational predictions become performatively stable, what exactly has stabilized: knowledge about students, institutional routing behavior, or a new student population produced by the predictions?

DEEPER QUESTION:
Could “model improvement” sometimes mean increasing agreement between an institution and the world the institution has successfully forced into existence?

MECHANISM:
historical population
→ prediction
→ decision
→ changed behavior / allocation
→ changed population
→ retraining
→ new prediction

FORMAL SHIFT:
<PREDICTION ABOUT DISTRIBUTION D>
→ [DEPLOY]
→ <D BECOMES D(θ)>
→ [RETRAIN]
→ <PREDICTOR STABILIZES AGAINST ITS INDUCED DISTRIBUTION>

SOURCE FORMALISM:
The paper introduces a performative prediction framework in which deploying model parameters can induce a new data distribution.

It introduces the equilibrium notion of performative stability and studies conditions under which repeated retraining converges toward such a point.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Ordinary prediction:

θ_t
→ predict Y under D

Performative prediction:

θ_t
→ ACTION(θ_t)
→ D(θ_t)
→ DATA_t+1
→ θ_t+1

A stable θ* need not recover an intervention-free D₀.

It can instead satisfy:

θ*
→ D(θ*)
→ θ*

TENSION:
[[Z-EDUPM-003]] framed educational intervention as potentially making a correct prediction appear false.

Performative stability exposes the mirror-image danger:

intervention can also make a model appear increasingly correct because the deployment changes the target toward the model.

MISSING:
The distribution of educational trajectories that would have existed without predictive intervention.

BOUNDARY:
Perdomo et al. develop a general machine-learning framework, not an empirical study of university advising.

Applying performative stability to educational recommendation remains an inference requiring direct evidence.

CITATION TRAIL:
[[Z-EDUPM-003]]
→ Perdomo et al., performative prediction
→ performative stability
→ educational routing as distribution-producing intervention

Follow:
strategic classification
performative power
causal prediction under intervention
dynamic algorithmic decision systems

TEST:
Take a deployed student-risk or course-recommendation system with repeated retraining.

For successive model generations record:

prediction distributions,
interventions,
course choices,
student outcomes,
population composition.

Then compare observed calibration with an experimentally maintained non-intervention or randomized-exploration population.

Ask whether apparent improvement disappears when deployment effects are removed.

PLATFORM:
[[EDUCATION AS PERFORMATIVE PREDICTION]]

LINKS:
[[Z-EDUPM-003]]
[[Performative Stability]]
[[Predictions That Manufacture Their Evidence]]

BIBTEX:
@inproceedings{perdomo2020performative,
  title     = {Performative Prediction},
  author    = {Perdomo, Juan and Zrnic, Tijana and Mendler-D{"u}nner, Celestine and Hardt, Moritz},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning},
  pages     = {7599--7609},
  year      = {2020},
  volume    = {119},
  series    = {Proceedings of Machine Learning Research},
  publisher = {PMLR}
}