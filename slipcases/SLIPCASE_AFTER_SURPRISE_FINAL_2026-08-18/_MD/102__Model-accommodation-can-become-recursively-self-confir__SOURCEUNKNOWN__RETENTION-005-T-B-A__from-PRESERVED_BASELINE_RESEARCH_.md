ZETTEL

ID:
RETENTION-005-T-B-A

TITLE:
Model accommodation can become recursively self-confirming if accommodated user prompts are later reused as training data.

SOURCE:
Shachar Don-Yehiya, Leshem Choshen, and Omri Abend — “Human Learning by Model Feedback” — EMNLP 2023.

PASSAGE:
[PARAPHRASE]
The study finds users adapt toward model-preferred language and raises concern that interaction data reused for training may already encode accommodation to the model.

RESEARCH OBJECT:
MODEL PREFERENCE CAN WRITE ITSELF INTO FUTURE DATA.

LOCAL MOVE:
Build feedback loop MODEL PREFERENCE → USER ADAPTATION → LOGGED LANGUAGE → FUTURE TRAINING → STRONGER PREFERENCE.

SOURCE TERMS:
model feedback
model preferences
human adaptation
iterative prompting
training data
language convergence

WHAT BECAME STRANGE:
What later appears to be natural user preference may partly be a fossil of earlier model pressure.

QUESTION:
Can interaction logs become counterfeit evidence of what users independently wanted?

DEEPER QUESTION:
When model-shaped behavior feeds back into development, how can one recover the counterfactual user distribution before accommodation?

MECHANISM:
M_t favors l → users discover l works → logs accumulate l → M_{t+1} trains/optimizes on logs → l strengthens.

FORMAL SHIFT:
<MODEL BIAS> → <USER ACCOMMODATION> → <TRAINING DATA> → <MODEL BIAS REINFORCEMENT>

SOURCE FORMALISM:
The paper observes prompt convergence and raises reuse of interaction data as a concern.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
P_logged=Adapt(P_independent_intent,M); retraining on P_logged creates M→AdaptUsers(M)→Data(M)→M′.

TENSION:
The completed retraining loop is a research hypothesis, not demonstrated by the source.

MISSING:
Longitudinal evidence linking user accommodation to subsequent model updates.

BOUNDARY:
Model-shaped user data should not automatically be treated as exogenous evidence of preference.

CITATION TRAIL:
[[RETENTION-005-T-B]] → model accommodation → logs → potential self-confirming preference loop.

TEST:
Train successor model on fresh independent descriptions versus M1-adapted interaction prompts and compare strengthening of M1-specific traits.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-T-B]]
[[self-confirming-preference]]
[[model-induced-language]]
[[counterfeit-consensus]]
[[feedback-loop]]

BIBTEX:
NONE
