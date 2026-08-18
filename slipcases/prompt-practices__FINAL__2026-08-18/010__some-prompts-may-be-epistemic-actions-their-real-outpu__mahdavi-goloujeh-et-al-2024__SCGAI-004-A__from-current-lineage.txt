ZETTEL

ID:
SCGAI-004-A

TITLE:
Some prompts may be epistemic actions: their real output is knowledge about the machine.

SOURCE:
David Kirsh and Paul Maglio — “On Distinguishing Epistemic from Pragmatic Action” — Cognitive Science 18(4) — 1994 — pp. 513–549 — https://doi.org/10.1207/s15516709cog1804_1

PASSAGE:
[QUOTE] Kirsh and Maglio distinguish “epistemic actions—actions performed to uncover information that is hidden or hard to compute mentally.” (p. 513)

RESEARCH OBJECT:
[OUR INFERENCE] A generation can be instrumentally poor yet epistemically successful if its observable consequence teaches the user which variable matters. Some prompts seek knowledge about the model rather than an artifact.

LOCAL MOVE:
Split PROMPTING into PRAGMATIC PROMPTING and EPISTEMIC PROMPTING.

SOURCE TERMS:
pragmatic action; epistemic action; hidden information; external action; computational state

WHAT BECAME STRANGE:
A visibly failed generation can be a completely successful prompt. Artifact quality and prompt success can diverge.

QUESTION:
How much prompt practice seeks artifacts, and how much seeks information about the model?

DEEPER QUESTION:
Is the generative model partly an epistemic instrument through which users think by perturbing a hidden system and inspecting returns?

MECHANISM:
uncertainty → external action → perceptible consequence → newly available information; in prompting: hypothesis → prompt perturbation → generation → observation → belief update.

FORMAL SHIFT:
PROMPT: INSTRUCTION → OUTPUT splits into PRAGMATIC: INSTRUCTION → DESIRED OUTPUT and EPISTEMIC: HYPOTHESIS → INTERVENTION → OUTPUT-AS-EVIDENCE → UPDATED BELIEF.

SOURCE FORMALISM:
Kirsh and Maglio distinguish pragmatic actions that advance an external task and epistemic actions that transform the environment to expose information or reduce computation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
p+Δ → M → y; B_t → observe(y|p+Δ) → B_(t+1); utility may include information gain, not only output quality.

TENSION:
Tetris exposes a comparatively stable environment; generative systems may be stochastic, hidden, versioned, personalized, moderated, or silently updated, making evidence unstable.

MISSING:
Behavioral evidence distinguishing artifact-seeking executions from information-seeking executions in real prompt logs.

BOUNDARY:
Kirsh and Maglio do not discuss AI prompting; epistemic prompting is [OUR INFERENCE].

CITATION TRAIL:
[[SCGAI-004]] → community “experiments” → what is an experimental prompt doing? → Kirsh & Maglio 1994 → epistemic/pragmatic action.

TEST:
Record expert sessions with think-aloud; identify executions users keep because they learned something despite disliking the artifact.

PLATFORM:
Generative AI prompting / MidJourney / LLMs / image models

LINKS:
[[SCGAI-004]]
[[SCGAI-002]]

BIBTEX:
@article{kirsh1994distinguishing, author={Kirsh, David and Maglio, Paul}, title={On Distinguishing Epistemic from Pragmatic Action}, journal={Cognitive Science}, volume={18}, number={4}, pages={513--549}, year={1994}, doi={10.1207/s15516709cog1804_1}, url={https://doi.org/10.1207/s15516709cog1804_1}}
