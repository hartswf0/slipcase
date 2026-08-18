ZETTEL

ID:
RETENTION-005-R-A

TITLE:
A prompt trajectory records not only the artist learning the image but the artist learning to speak the model’s preferences.

SOURCE:
Shachar Don-Yehiya, Leshem Choshen, and Omri Abend — “Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney” — EMNLP 2023.

PASSAGE:
[PARAPHRASE]
The authors observe prompt convergence and evidence for two processes: users discover omitted details of their intended image and adapt language toward model-preferred patterns.

RESEARCH OBJECT:
PROMPT TRAJECTORIES MIX INTENTION REFINEMENT WITH MODEL ACCOMMODATION.

LOCAL MOVE:
A revision can mean I KNOW BETTER WHAT I WANT or I KNOW BETTER WHAT THE MODEL REWARDS.

SOURCE TERMS:
iterative prompting
model feedback
human learning
model preferences
convergence
user intention

WHAT BECAME STRANGE:
The same prompt change may move toward intention or toward generator preference.

QUESTION:
Can a prompt history distinguish intention refinement from accommodation to model bias?

DEEPER QUESTION:
When repeated interaction changes the maker’s vocabulary and perhaps what they want, which side is steering which?

MECHANISM:
H0+M→p0→y0; user update contains Δintent+Δmodel-adaptation; over time H itself may shift.

FORMAL SHIFT:
<PROMPT TRAJECTORY = HUMAN CONTROL RECORD> → <HUMAN–MODEL CO-ADAPTATION TRACE>

SOURCE FORMALISM:
The paper analyzes sequential Midjourney prompt changes and tests missing-detail versus model-adaptation explanations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Δp_t=Δp_t^intent+Δp_t^accommodation+ε_t.

TENSION:
Learning medium affordances is ordinary craft; accommodation does not automatically diminish authorship.

MISSING:
A method separating productive medium-learning from convergence suppressing original intentions.

BOUNDARY:
A rich trajectory proves interaction and learning, not unilateral steering.

CITATION TRAIL:
[[RETENTION-005-R]] → prompt trajectory → iterative prompting data → co-adaptation.

TEST:
Elicit target features independently before model use and classify subsequent prompt changes as restoring intention, discovering intention, or model accommodation.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-R]]
[[co-adaptation]]
[[model-preference]]
[[iterative-prompting]]

BIBTEX:
NONE
