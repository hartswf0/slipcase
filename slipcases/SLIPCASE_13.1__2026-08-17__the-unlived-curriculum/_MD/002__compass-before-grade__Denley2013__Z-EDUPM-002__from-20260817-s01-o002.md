ZETTEL

ID:
Z-EDUPM-002

TITLE:
THE UNIVERSITY’S LITERAL PREDICTION ENGINE MAY SIT BEFORE THE GRADE: DEGREE COMPASS FORECASTS THE GRADE IN ORDER TO CHANGE THE COURSE A STUDENT TAKES.

SOURCE:
Tristan Denley — “Degree Compass: A Course Recommendation System” — 2013 — EDUCAUSE Review.

SOURCE URL:
https://er.educause.edu/articles/2013/9/degree-compass-a-course-recommendation-system

PASSAGE:
[PARAPHRASE] Degree Compass combines a student’s prior grades with grade histories from many other students, curricular requirements, sequencing, and course centrality. It ranks courses partly according to the grade the student is predicted to earn.

RESEARCH OBJECT:
A university can transform accumulated grades from retrospective evaluations into inputs for an individualized forecast that actively changes the student’s future trajectory.

LOCAL MOVE:
Denley turns transcript history into choice architecture.

The system does not merely say:
“You did well.”

It says:
“Given what people like you did before, this is where you should go next.”

SOURCE TERMS:
course recommendation system
predictive analytics
grade prediction model
individualized recommendations
degree requirements
course sequencing
student success
choice architecture

WHAT BECAME STRANGE:
The grade is not primarily the prediction.

The grade becomes training data for another machine that predicts the next grade.

A student therefore inhabits a recursive predictive loop:

PAST GRADES
→ PREDICTED FUTURE GRADE
→ COURSE RECOMMENDATION
→ COURSE TAKEN
→ NEW GRADE
→ FUTURE MODEL INPUT

QUESTION:
When a university predicts where a student will succeed and then routes the student toward that location, what exactly is being measured afterward: student aptitude, model accuracy, or the consequence of having followed the model?

DEEPER QUESTION:
At what point does predicting student success become producing the population distribution that later appears to validate the prediction?

MECHANISM:
Historic student-course outcomes are combined with an individual transcript.

Courses are ranked.

Predicted academic success contributes to the recommendation.

The recommendation enters advising and choice.

The resulting enrollment generates the next observation.

FORMAL SHIFT:
<PAST PERFORMANCE>
→ <PREDICTED COURSE PERFORMANCE>
→ [RANK / RECOMMEND]
→ <ALTERED COURSE CHOICE>
→ <NEW PERFORMANCE DATA>

SOURCE FORMALISM:
Degree Compass combines:
- transcript data,
- historical grade data,
- degree applicability,
- course sequencing,
- curricular centrality,
- predicted academic success.

The source describes a collaborative-filtering/predictive-modeling architecture but does not supply a complete executable specification in the article.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

RANK(student, course) =
    f(
      degree_requirement,
      curricular_centrality,
      sequence_fit,
      predicted_grade
    )

Then:

RANK
→ CHOICE
→ OUTCOME
→ TRAINING DATA

TENSION:
A prediction market ordinarily waits for an uncertain external event to settle.

Degree Compass inserts the prediction into the causal path leading to the event.

The prediction is therefore not merely epistemic. It is advisory and potentially performative.

MISSING:
A counterfactual record of what the same student would have achieved had the recommendation not been shown.

BOUNDARY:
The source establishes a predictive recommendation system, not evidence that Degree Compass inevitably creates self-fulfilling predictions or unjustly restricts students.

CITATION TRAIL:
Austin Peay / EDUCAUSE Degree Compass case study, 2012.
Ekowo & Palmer — predictive analytics in higher education.
Literature on recommender-system feedback loops.
Performative prediction / performative prediction models.
Algorithmic confounding caused by interventions.

TEST:
For students with two courses receiving similar predicted-success scores, randomly vary whether the recommendation is shown.

Compare:
choice,
grade,
persistence,
major trajectory,
and subsequent model predictions.

Ask whether the act of prediction changes the object predicted.

PLATFORM:
[[EDUCATION AS PREDICTIVE INFRASTRUCTURE]]

LINKS:
[[Performative Prediction]]
[[Algorithmic Advising]]
[[Grades Become Training Data]]

BIBTEX:
@misc{denley2013degreecompass,
  author       = {Denley, Tristan},
  title        = {Degree Compass: A Course Recommendation System},
  year         = {2013},
  month        = sep,
  publisher    = {EDUCAUSE Review},
  url          = {https://er.educause.edu/articles/2013/9/degree-compass-a-course-recommendation-system}
}