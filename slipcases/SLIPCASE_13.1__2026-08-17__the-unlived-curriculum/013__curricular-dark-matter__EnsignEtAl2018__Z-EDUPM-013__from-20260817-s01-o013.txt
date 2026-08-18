ZETTEL

ID:
Z-EDUPM-013

TITLE:
A PREDICTIVE SYSTEM CAN MISTAKE WHERE IT LOOKS FOR WHAT EXISTS: DEPLOYMENT CREATES “DISCOVERED” DATA THAT THEN JUSTIFY MORE DEPLOYMENT.

SOURCE:
Danielle Ensign, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger, and Suresh Venkatasubramanian — “Runaway Feedback Loops in Predictive Policing” — 2018 — Proceedings of the 1st Conference on Fairness, Accountability and Transparency, pp. 160–171.

PASSAGE:
[PARAPHRASE] Predictive policing repeatedly uses discovered crime data to update deployment; the authors show how this can repeatedly redirect police toward the same locations regardless of underlying crime rates.

RESEARCH OBJECT:
Observation is exposure-dependent.

The system sees more evidence where its previous prediction sent observers.

LOCAL MOVE:
Ensign et al. distinguish incidents that are independently reported from incidents discovered through police deployment.

That distinction makes the observational machinery itself a causal variable in the dataset.

SOURCE TERMS:
runaway feedback loops
predictive policing
discovered incidents
reported incidents
allocation
true crime rate
feedback
inputs

WHAT BECAME STRANGE:
A recommender may not merely have selective labels.

It may actively manufacture unequal quantities of evidence.

If course A is recommended repeatedly:

more students enter A
→ more outcomes from A exist
→ more data describe A
→ model knows A better
→ uncertainty around A falls
→ A can become safer to recommend.

Meanwhile course B becomes statistically dark.

The recommendation system could gradually confuse:

WE HAVE MORE EVIDENCE ABOUT THIS PATH

with:

THIS PATH IS BETTER.

QUESTION:
Can educational personalization create epistemic rich-get-richer effects in which frequently recommended pathways become increasingly data-rich while neglected pathways disappear from the model's knowable world?

DEEPER QUESTION:
Does algorithmic advising eventually construct “main roads” through a curriculum simply because prior recommendations made those roads easiest to observe?

MECHANISM:
initial prediction
→ allocation of attention / people
→ increased observation at selected location
→ selected-location data dominate update
→ prediction strengthens
→ increased allocation

FORMAL SHIFT:
<PREDICTED HIGH-VALUE REGION>
→ [DEPLOY OBSERVATION THERE]
→ <MORE DISCOVERED EVENTS THERE>
→ [UPDATE MODEL]
→ <REGION APPEARS EVEN MORE IMPORTANT>

SOURCE FORMALISM:
Ensign et al. mathematically model a repeated allocation-and-update process.

They distinguish:

reported incidents

from:

discovered incidents generated through deployment.

They show that reported incidents can attenuate runaway feedback but need not eliminate it.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For course c:

ObservedData(c,t+1)
=
NaturallyObserved(c)
+
Exposure(c,t) × DiscoverableOutcome(c)

Recommendation(c,t)
→ Exposure(c,t+1)

Therefore:

recommendation
→ exposure
→ observations
→ recommendation.

TENSION:
[[Z-EDUPM-002]] focused on recommendations changing student trajectories.

This source forces a more technical distinction:

the model may change not only outcomes but the LOCATION AND DENSITY OF OBSERVATION.

MISSING:
Evidence about whether educational recommender systems normalize, explore, or otherwise correct for recommendation-dependent exposure.

BOUNDARY:
Predictive policing is not educational advising.

Crime discovery and course performance differ substantively.

Only the feedback architecture is being transferred as a hypothesis.

CITATION TRAIL:
[[Z-EDUPM-002]]
→ Ensign et al.
→ discovered versus independently reported events
→ allocation-generated data
→ recommendation-generated curriculum visibility

Follow:
exposure bias in recommender systems
bandit exploration
positivity violations
feedback loops in ranking systems

TEST:
For every course in a recommender system, estimate:

recommendation exposure,
enrollment following exposure,
number of observed outcomes,
prediction confidence,
future recommendation frequency.

Test whether early exposure predicts later recommendation after controlling for measured student-course fit.

PLATFORM:
[[CURRICULAR FEEDBACK ECOLOGY]]

LINKS:
[[Z-EDUPM-002]]
[[Runaway Feedback]]
[[Curricular Dark Matter]]
[[Recommendation Produces Observation]]

BIBTEX:
@inproceedings{ensign2018runaway,
  title     = {Runaway Feedback Loops in Predictive Policing},
  author    = {Ensign, Danielle and Friedler, Sorelle A. and Neville, Scott and Scheidegger, Carlos and Venkatasubramanian, Suresh},
  booktitle = {Proceedings of the 1st Conference on Fairness, Accountability and Transparency},
  pages     = {160--171},
  year      = {2018},
  volume    = {81},
  series    = {Proceedings of Machine Learning Research},
  publisher = {PMLR}
}