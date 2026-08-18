ZETTEL

ID:
Z-EDUPM-010

TITLE:
THE UNLIVED CURRICULUM HAS NO LABELS: A RECOMMENDER CANNOT OBSERVE THE GRADES STUDENTS WOULD HAVE RECEIVED IN COURSES THEY NEVER TOOK.

SOURCE:
Jon Kleinberg, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, and Sendhil Mullainathan — “Human Decisions and Machine Predictions” — 2018 — Quarterly Journal of Economics 133(1), pp. 237–293.

PASSAGE:
[PARAPHRASE] In the bail setting, outcomes are observable for defendants judges release but not for those they detain; prior decisions therefore determine where labels exist.

RESEARCH OBJECT:
Selective labels: a prediction system is trained and evaluated on outcomes that earlier decisions permitted the world to reveal.

LOCAL MOVE:
Kleinberg et al. show that the missing-data problem is not random.

A prior decision determines whether the outcome that would evaluate the decision can ever become observable.

SOURCE TERMS:
human decisions
machine predictions
selective labels
counterfactual decision rules
prior judge decisions
observed outcomes
quasi-random assignment

WHAT BECAME STRANGE:
A transcript contains an enormous invisible negative space.

It records:

COURSES TAKEN
→ GRADES OBSERVED.

It does not record:

COURSES NOT TAKEN
→ GRADES THAT WOULD HAVE OCCURRED.

A recommender claiming to know which course a student should take therefore learns from a world in which almost every alternative educational trajectory is permanently unlabeled.

The missing object is the student's unlived curriculum.

QUESTION:
How can a course-recommendation model learn whether its rejected alternatives were actually worse when rejection prevents their outcomes from ever becoming data?

DEEPER QUESTION:
Does personalized education gradually destroy the counterfactual diversity required to know whether personalization works?

MECHANISM:
prior decision
→ one option selected
→ selected outcome becomes observable
→ rejected outcomes remain hidden
→ model trains on selectively revealed labels
→ future decisions repeat the selection structure

FORMAL SHIFT:
<POSSIBLE FUTURES {A,B,C,D}>
→ [CHOOSE B]
→ <OBSERVE Y_B>
→ <Y_A,Y_C,Y_D REMAIN UNOBSERVED>
→ [TRAIN]
→ <NEW CHOICE POLICY>

SOURCE FORMALISM:
The paper treats bail as a prediction-and-decision problem complicated because outcomes are observed only for defendants who are released.

It uses econometric strategies including quasi-random assignment to judges to construct decision counterfactuals.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For student s:

Potential grades:
G_s = {
  g(s,c₁),
  g(s,c₂),
  ...
  g(s,cₙ)
}

Observed transcript:

T_s = {g(s,c*) : c* actually taken}

For almost every c ≠ c*:

g(s,c) = UNOBSERVED

The recommendation system is therefore asked to rank precisely the values the institution usually prevents itself from observing.

TENSION:
[[Z-EDUPM-002]] asked whether recommendation produces the distribution that later validates it.

Selective labels sharpen the issue:

sometimes there is not even contrary evidence available to falsify the recommendation, because the alternative trajectory was never lived.

MISSING:
Counterfactual performance in courses not taken.

BOUNDARY:
Kleinberg et al. study judicial bail decisions, not course recommendation.

The selective-label structure transfers formally only if course choice actually determines whether the outcome needed to evaluate alternative recommendations is observed.

CITATION TRAIL:
[[Z-EDUPM-002]]
→ Kleinberg et al.
→ selectively observed outcomes
→ missing counterfactual labels
→ educational recommendation

Follow:
Lakkaraju et al. — The Selective Labels Problem
off-policy evaluation
contextual bandits
exploration versus exploitation
causal recommender systems

TEST:
Within a set of academically acceptable electives, randomly perturb which eligible course appears first in the recommendation interface.

Use that randomized exploration to estimate outcomes for trajectories the ordinary recommender would rarely expose.

Compare those results with the model's counterfactual grade predictions.

PLATFORM:
[[THE UNLIVED CURRICULUM]]

LINKS:
[[Z-EDUPM-002]]
[[Selective Labels]]
[[Counterfactual Education]]
[[Unlived Curriculum]]

BIBTEX:
@article{kleinberg2018human,
  author  = {Kleinberg, Jon and Lakkaraju, Himabindu and Leskovec, Jure and Ludwig, Jens and Mullainathan, Sendhil},
  title   = {Human Decisions and Machine Predictions},
  journal = {The Quarterly Journal of Economics},
  year    = {2018},
  volume  = {133},
  number  = {1},
  pages   = {237--293},
  doi     = {10.1093/qje/qjx032}
}