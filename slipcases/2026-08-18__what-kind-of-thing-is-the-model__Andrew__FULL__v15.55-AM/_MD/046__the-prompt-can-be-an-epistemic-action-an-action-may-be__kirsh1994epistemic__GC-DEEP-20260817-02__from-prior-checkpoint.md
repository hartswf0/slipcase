ZETTEL

ID:
GC-DEEP-20260817-02

TITLE:
THE PROMPT CAN BE AN EPISTEMIC ACTION — an action may be valuable because it exposes information rather than directly advancing the goal.

SOURCE:
David Kirsh and Paul Maglio — “On Distinguishing Epistemic from Pragmatic Action” — Cognitive Science 18(4), 1994, 513–549. SOURCE URL: https://doi.org/10.1207/s15516709cog1804_1

PASSAGE:
[QUOTE]
“actions performed to uncover information that is hidden or hard to compute mentally.”

[PARAPHRASE]
Kirsh and Maglio distinguish epistemic actions from pragmatic actions: some actions change the world mainly to simplify cognition or reveal information, rather than to move directly toward the external goal.

RESEARCH OBJECT:
EPISTEMIC-ACTION-AS-PROMPT-FUNCTION.

LOCAL MOVE:
[[GC-DEEP-20260817-01]] describes prompts that are issued to discover model boundaries. Kirsh and Maglio provide a prior distinction that makes this behavior legible without reducing it to failed task execution. The prompt-output event can be useful because it externalizes a question whose answer is difficult to compute in advance.

SOURCE TERMS:
“epistemic action”
“pragmatic action”
“uncover information”
“hidden”
“hard to compute mentally”

WHAT BECAME STRANGE:
The “wasted” generation—the strange image, the test phrase, the seed probe—may be the cognitively efficient move. What looks superfluous under a goal-only model can be central under an inquiry model.

QUESTION:
Which prompting moves look inefficient if judged only by closeness to a target but become rational when judged by information gained?

DEEPER QUESTION:
Can prompt interfaces be evaluated by how cheaply they support epistemic action, not only by final-output quality?

MECHANISM:
UNKNOWN RELATION
→ external action
→ perceptible consequence
→ reduced uncertainty
→ better later action.

FORMAL SHIFT:
FROM: generation as production cost.
TO: generation as cognitive instrumentation.

SOURCE FORMALISM:
Kirsh and Maglio distinguish pragmatic actions that move an agent physically closer to a goal from epistemic actions that reveal or simplify information needed for cognition.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

VALUE(prompt) = ARTIFACT_PROGRESS + INFORMATION_GAIN.

A prompt with low ARTIFACT_PROGRESS may still be expert behavior when INFORMATION_GAIN is high.

TENSION:
A model output can be epistemically informative while also misleading the user about underlying mechanism. Information gain about observable regularity is not the same as causal understanding.

MISSING:
Measures of information gain suitable for stochastic generative interaction.

BOUNDARY:
Kirsh and Maglio studied Tetris actions, not generative AI. This child applies their functional distinction by analogy, not historical influence.

CITATION TRAIL:
[[GC-DEEP-20260817-01]] → exploratory prompts
→ Kirsh & Maglio 1994
→ distinguish acting-to-learn from acting-to-achieve
→ prompt exploration becomes a recognizable class of epistemic action.

TEST:
Compare two interfaces for the same model: one optimized for producing polished outputs, one optimized for rapid controlled probes and comparison. Measure how quickly users build accurate capability maps.

PLATFORM:
Cognitive science / generative AI interpretation

LINKS:
[[GC-DEEP-20260817-01]]
[[MJ-GC-004]]
[[MJ-GC-005]]
[[MJ-GC-006]]

BIBTEX:
@article{kirsh1994epistemic,
  author={Kirsh, David and Maglio, Paul},
  title={On Distinguishing Epistemic from Pragmatic Action},
  journal={Cognitive Science},
  volume={18},
  number={4},
  pages={513--549},
  year={1994},
  doi={10.1207/s15516709cog1804_1},
  url={https://doi.org/10.1207/s15516709cog1804_1}
}
