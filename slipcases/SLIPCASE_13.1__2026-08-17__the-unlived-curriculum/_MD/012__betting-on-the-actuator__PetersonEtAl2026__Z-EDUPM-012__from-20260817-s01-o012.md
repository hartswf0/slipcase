ZETTEL

ID:
Z-EDUPM-012

TITLE:
A MARKET CAN CREATE THE EVENT IT BETS ON WHEN THE PERSON WHO CAN MAKE THE EVENT TRUE IS ALSO ALLOWED TO TRADE ON IT.

SOURCE:
Jack Peterson, Joseph Krug, Micah Zoltu, Austin K. Williams, and Stephanie Alexander — Augur: a Decentralized Oracle and Prediction Market Platform (v2.0) — 2026 — Section III.4, “Self-Referential Oracle Queries.”

PASSAGE:
[QUOTE] “Markets that trade on the future behavior of Augur’s oracle may have undesirable effects on the behavior of the oracle itself.”

RESEARCH OBJECT:
The self-referential prediction market: a forecast becomes an incentive attached to an actor capable of making the forecast come true.

LOCAL MOVE:
Augur considers markets about future behavior of its own reporters.

If a designated reporter can profit sufficiently from a particular market outcome, the market itself can alter the reporter's incentive to produce that outcome.

SOURCE TERMS:
self-referential oracle queries
designated reporter
perverse incentive
oracle
market
shares
behavior
finalization

WHAT BECAME STRANGE:
Prediction-market epistemology contains its own sabotage mechanism.

A wager does not merely aggregate beliefs when a bettor is also an actuator inside the event.

The information instrument becomes a control instrument.

This produces a new question for education.

Student evaluations,
public grade distributions,
acceptance-rate predictions,
department rankings,
job-placement dashboards,
and faculty performance forecasts

may cease to be passive descriptions whenever the people being measured can see them and act to change the settlement condition.

QUESTION:
Which educational forecasts accidentally create financial, reputational, or administrative incentives for the predicted actors to manufacture the predicted outcome?

DEEPER QUESTION:
At what point does a forecast stop being a sensor and become an actuator?

MECHANISM:
prediction instrument becomes visible
→ actor inside predicted event observes incentive
→ actor changes behavior
→ event probability changes
→ market / metric settles
→ produced outcome appears as evidence

FORMAL SHIFT:
<FORECAST OF ACTOR A>
→ [A OBSERVES / TRADES / IS REWARDED BY FORECAST]
→ <A CHANGES BEHAVIOR>
→ <FORECAST CHANGES ITS OWN SETTLEMENT EVENT>

SOURCE FORMALISM:
Augur provides the concrete example of a market concerning whether a designated reporter will fail to report.

A reporter could potentially purchase shares that make intentional non-reporting profitable enough to compensate for other losses.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Ordinary:

beliefs
→ price
→ event
→ settlement

Self-referential:

beliefs
→ price
→ INCENTIVE(actor)
→ actor changes event
→ settlement

The market has crossed from:

SENSOR

to:

SENSOR + ACTUATOR.

TENSION:
[[Z-EDUPM-003]] describes prediction changing its target through decision deployment.

[[Z-EDUPM-004]] describes markets settling externally specified future events.

Self-referential markets collapse these:

the prediction mechanism becomes one of the causal variables determining what it will later claim to have predicted.

MISSING:
An educational case where exposing a forecast can be experimentally shown to change behavior strongly enough to alter its own measured outcome.

BOUNDARY:
Augur demonstrates the possibility within its oracle architecture.

It does not establish that student evaluations, rankings, or educational dashboards exhibit the same incentive structure.

CITATION TRAIL:
[[Z-EDUPM-003]]
[[Z-EDUPM-004]]
→ Augur III.4
→ self-referential oracle query
→ prediction as incentive
→ prediction as actuator

Follow:
decision markets
Goodhart effects
Lucas critique
performative prediction
reflexivity
self-fulfilling prophecy

TEST:
Construct an educational forecast about an outcome controlled partly by the predicted actor.

Randomize whether the actor sees the forecast.

Compare:

behavior,
outcome,
forecast calibration.

If visibility changes the outcome distribution, the forecast is partly an actuator.

PLATFORM:
[[PREDICTION AS ACTUATION]]

LINKS:
[[Z-EDUPM-003]]
[[Z-EDUPM-004]]
[[Self-Referential Markets]]
[[Forecasts That Cause Their Settlement]]

BIBTEX:
@misc{peterson2026augur,
  author = {Peterson, Jack and Krug, Joseph and Zoltu, Micah and Williams, Austin K. and Alexander, Stephanie},
  title  = {Augur: a Decentralized Oracle and Prediction Market Platform (v2.0)},
  year   = {2026},
  note   = {arXiv:1501.01042}
}