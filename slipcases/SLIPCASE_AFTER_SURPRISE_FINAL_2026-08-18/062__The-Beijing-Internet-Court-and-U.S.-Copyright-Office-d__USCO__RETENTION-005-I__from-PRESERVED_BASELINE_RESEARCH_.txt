ZETTEL

ID:
RETENTION-005-I

TITLE:
The Beijing Internet Court and U.S. Copyright Office draw nearly opposite inferences from prompt variation.

SOURCE:
Beijing Internet Court — Li v. Liu — 2023; U.S. Copyright Office — Copyright and Artificial Intelligence, Part 2 — 2025.

PASSAGE:
[PARAPHRASE]
The Beijing court treated changes in prompts or parameters that produced different images as evidence of personalized choice. The U.S. analysis emphasizes output variation under the same prompt as evidence that users do not determine expressive form.

RESEARCH OBJECT:
VARIABILITY CAN BE READ AS EVIDENCE FOR CONTROL OR AGAINST CONTROL.

LOCAL MOVE:
The jurisdictions intervene on different variables: SAME PROMPT → DIFFERENT OUTPUT versus DIFFERENT PROMPT/PARAMETERS → DIFFERENT OUTPUT.

SOURCE TERMS:
prompt words
parameters
selection
arrangement
personal judgment
originality
different pictures

WHAT BECAME STRANGE:
A system can have high uncontrolled variance and high sensitivity to intentional intervention at the same time.

QUESTION:
Which experiment is more relevant to authorship: repeatability under fixed input, or responsiveness to intentional changes in input?

DEEPER QUESTION:
Should control require LOW NOISE, HIGH INTERVENTION EFFECT, or some combination of both?

MECHANISM:
Noise = Var(Y|P=p). Control sensitivity = ΔE[Y | do(P=p1) versus do(P=p2)].

FORMAL SHIFT:
<CONTROL AS REPEATABILITY> → <CONTROL AS SIGNAL-TO-NOISE OF INTENTIONAL INTERVENTION>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
For feature f, C_f = effect of intended intervention on f / uncontrolled variance of f.

TENSION:
The legal systems, factual records, and tools differ; this is not a controlled cross-jurisdiction experiment.

MISSING:
A legal framework explicitly separating intervention sensitivity from output repeatability.

BOUNDARY:
Do not summarize the disagreement as CHINA PRO-AI versus U.S. ANTI-AI. The deeper issue is what counts as evidence of expressive causation.

CITATION TRAIL:
[[RETENTION-005]] → U.S. same-input variance → Beijing changed-input variance → two causal tests → signal versus noise.

TEST:
Measure repeated outputs under identical prompt and outputs after controlled prompt changes. Estimate intentional effect against noisy baseline.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[li-v-liu]]
[[comparative-copyright]]
[[control-vs-variance]]
[[causal-intervention]]

BIBTEX:
NONE
