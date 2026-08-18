ZETTEL

ID:
Z-EDUPM-003

TITLE:
AN EARLY-WARNING SYSTEM SUCCEEDS WHEN ITS PREDICTION FAILS: EDUCATIONAL FORECASTING CAN BE AN ANTI-SETTLEMENT MACHINE.

SOURCE:
Manuela Ekowo and Iris Palmer — The Promise and Peril of Predictive Analytics in Higher Education: A Landscape Analysis — 2016 — New America.

SOURCE URL:
https://www.newamerica.org/insights/promise-and-peril-predictive-analytics-higher-education/

PASSAGE:
[PARAPHRASE] Colleges use predictive analytics to identify students needing additional support, steer students toward courses, and intervene with students predicted to be at risk of dropping out. The report also warns that profiling may discourage capable students from pursuing particular opportunities.

RESEARCH OBJECT:
A peculiar prediction whose purpose is to cause the predicted event not to happen.

LOCAL MOVE:
Ekowo and Palmer shift prediction from observation to intervention.

The forecast:
“this student may drop out”

is useful precisely because the institution can respond:
“then intervene so that they do not.”

SOURCE TERMS:
predictive analytics
early-alert tool
identify students
extra support
student success
profiling
steer
predictions
drop out

WHAT BECAME STRANGE:
Calibration becomes philosophically unstable when prediction triggers treatment.

If the model says:
P(dropout) = .80

and advising works,

the student stays.

Was the .80 prediction wrong?

Or was it correct enough to trigger the intervention that made itself false?

QUESTION:
How should an educational predictive system be evaluated when successful use destroys the observable event against which accuracy would normally be judged?

DEEPER QUESTION:
Is the university constructing predictions or counterfactual action triggers?

MECHANISM:
student data
→ risk estimate
→ risk classification
→ institutional intervention
→ changed conditions
→ changed outcome

The prediction enters the system it predicts.

FORMAL SHIFT:
<STUDENT TRAJECTORY>
→ <RISK SCORE>
→ [TRIGGER INTERVENTION]
→ <ALTERED TRAJECTORY>

SOURCE FORMALISM:
NONE.
The source describes applications and institutional examples rather than a formal causal model.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Without intervention:

X → P(Y = dropout | X)

With deployed prediction:

X
→ P(Y = dropout | X)
→ ACTION
→ X'
→ Y'

Therefore:

Y' ≠ outcome under no prediction.

TENSION:
Prediction markets generally reward forecasts that correctly settle against realized outcomes.

Early-warning systems may be most valuable when their forecasts provoke actions that prevent those outcomes from ever settling as predicted.

MISSING:
The untreated counterfactual:
What would have happened had the prediction not triggered intervention?

BOUNDARY:
Ekowo and Palmer do not themselves describe early-warning analytics as an “anti-settlement machine.” That is our inference from the intervention structure they document.

CITATION TRAIL:
Causal inference under treatment assignment.
Selective labels.
Performative prediction.
Algorithmic decision-making under feedback.
Early-warning intervention evaluations.
Self-fulfilling and self-defeating prophecy.

TEST:
Separate students around a risk-score threshold and measure:

predicted risk,
whether intervention occurred,
actual outcome,
and estimated untreated outcome.

Ask whether apparently “false positive” predictions are concentrated among successfully treated students.

PLATFORM:
[[EDUCATION AS PREDICTIVE INFRASTRUCTURE]]

LINKS:
[[Predictions That Want To Be Wrong]]
[[Intervention Destroys Settlement]]
[[Risk Scores Change Their Objects]]

BIBTEX:
@report{ekowo2016promise,
  author      = {Ekowo, Manuela and Palmer, Iris},
  title       = {The Promise and Peril of Predictive Analytics in Higher Education: A Landscape Analysis},
  institution = {New America},
  year        = {2016},
  month       = oct,
  url         = {https://www.newamerica.org/insights/promise-and-peril-predictive-analytics-higher-education/}
}