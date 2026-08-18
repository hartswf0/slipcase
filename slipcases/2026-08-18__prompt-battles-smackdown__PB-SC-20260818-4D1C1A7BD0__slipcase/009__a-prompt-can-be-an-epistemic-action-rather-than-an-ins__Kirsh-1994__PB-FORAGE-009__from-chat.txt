ZETTEL

ID:
PB-FORAGE-009

TITLE:
A prompt can be an epistemic action rather than an instruction.

SOURCE:
David Kirsh and Paul Maglio — On Distinguishing Epistemic from Pragmatic Action — 1994 — Cognitive Science 18(4):513–549.

PASSAGE:
[PARAPHRASE]
Kirsh and Maglio distinguish pragmatic actions, which move an actor physically closer to a goal, from epistemic actions, which alter the world in order to make information easier to obtain or computation easier to perform. Their Tetris studies show players rotating pieces not merely to place them but to simplify perceptual and cognitive work.

RESEARCH OBJECT:
The Prompt Pilot may not fundamentally be issuing better instructions.

The Pilot may be performing epistemic actions on a conversational environment.

A prompt can be useful even when its completion is unusable as a final answer if that completion changes what can be seen, discriminated, represented, or asked next.

LOCAL MOVE:
Stop scoring every prompt by the quality of its immediate completion.

Ask what cognitive work the prompt makes unnecessary or newly possible.

SOURCE TERMS:
epistemic action
pragmatic action
Tetris cognition
problem-solving
hidden information
computation
action in the world

WHAT BECAME STRANGE:
A prompt that “fails” as a request may succeed as an epistemic probe.

Likewise, an apparently wasteful prompt may be the analogue of rotating a Tetris piece merely to see whether it fits.

The completion is then not the product.

It is a temporary external state used for thinking.

QUESTION:
How many prompts in a successful Prompt Battle are actually epistemic actions whose purpose is to transform the problem rather than obtain the answer?

DEEPER QUESTION:
If prompting skill consists partly in constructing external states that reduce uncertainty, is the fundamental unit of prompting still the prompt-completion pair?

MECHANISM:
An uncertain problem is partially externalized.

The operator performs an action on the external representation.

The resulting state exposes information that was previously difficult to compute internally.

That information changes the next action.

The sequence can therefore improve cognition without any single action resembling a direct solution step.

FORMAL SHIFT:
<UNCERTAIN TASK>
→ <EXTERNAL CONVERSATIONAL STATE>
→ [EPISTEMIC PROMPT]
→ <NEWLY VISIBLE DISTINCTION>
→ [NEXT ACTION]
→ <REVISED PROBLEM STATE>

SOURCE FORMALISM:
Kirsh and Maglio distinguish:

pragmatic action
→ changes the world to advance physical task completion

epistemic action
→ changes the world to improve cognition by exposing or simplifying information.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

S_t = current conversational/problem state
p_t = prompt action
o_t = resulting completion

A pragmatic prompt is evaluated mainly by:

Utility(o_t, goal)

An epistemic prompt may instead be evaluated by:

ΔI = InformationAvailable(S_{t+1}) - InformationAvailable(S_t)

or by reduction in the search required for the next move.

Thus:

low final-output value
≠
low prompting value.

TENSION:
Prompt engineering usually describes prompts as specifications intended to cause desired outputs.

Epistemic action suggests another class of prompt whose purpose is to alter the operator’s own cognitive situation.

The same interaction can therefore be tool use and inquiry at once.

MISSING:
A way to distinguish empirically among:

answer-seeking prompts
state-setting prompts
diagnostic prompts
contrast-producing prompts
representation-changing prompts
purely performative prompts.

BOUNDARY:
Kirsh and Maglio studied embodied action in Tetris, not language-model prompting.

The claim that prompting can instantiate epistemic action is [OUR INFERENCE], not their claim.

CITATION TRAIL:
[[PB-FORAGE-003]]
→ Kirsh and Maglio on epistemic action
→ Clark and Chalmers on spread of epistemic credit
→ test whether successful prompting trajectories contain actions whose value exists only in later moves.

TEST:
Take expert Prompt Battle transcripts.

For every prompt, hide all later turns from independent raters and ask whether the immediate completion advances the nominal task.

Then reveal the subsequent trajectory.

Identify prompts whose apparent value rises only after later turns.

Compare experts and novices on the frequency and placement of these delayed-value actions.

If expert advantage concentrates there, prompting expertise may consist substantially in epistemic action rather than better instruction writing.

PLATFORM:
[[Prompting as Interactive Cognition]]

LINKS:
[[PB-FORAGE-003]]
[[Epistemic Prompt]]
[[Prompt Trajectory]]
[[Externalized Search]]

BIBTEX:
@article{kirsh1994distinguishing,
  title={On Distinguishing Epistemic from Pragmatic Action},
  author={Kirsh, David and Maglio, Paul},
  journal={Cognitive Science},
  volume={18},
  number={4},
  pages={513--549},
  year={1994},
  doi={10.1207/s15516709cog1804_1}
}
