ZETTEL

ID:
FORAGE-WINFIELD-BLACKMORE-003

TITLE:
A STORY BECOMES EXECUTABLE WHEN ANOTHER BODY CAN RUN ITS COUNTERFACTUAL

SOURCE:
Alan F. T. Winfield and Susan Blackmore — Experiments in Artificial Culture: from noisy imitation to storytelling robots — 2022 — §3 Storybots

SOURCE URL:
https://arxiv.org/abs/2106.11754

PASSAGE:
[PARAPHRASE]
A Storybot can simulate a possible action and its consequences without executing it, convert that imagined sequence into speech, and transmit it to another robot.

The listener converts the spoken sequence back into actions and substitutes them into its own internal simulation machinery.

RESEARCH OBJECT:
The story is not executable merely because it contains instructions.

It becomes executable because speaker and listener share machinery capable of mapping narration back into a runnable counterfactual.

LOCAL MOVE:
Winfield and Blackmore move from imitation of observed behavior to transmission of behavior that never occurred.

Language carries a counterfactual trajectory from one internal simulator into another.

SOURCE TERMS:
Consequence Engine
what-if
storytelling
narrativises
internal model
simulate
imagine
conspecifics

WHAT BECAME STRANGE:
A description can transmit an event that has never happened.

QUESTION:
What has to be shared between two systems for words to become runnable?

DEEPER QUESTION:
Is linguistic executability located in the sentence, or in the compatibility between the worlds that speaker and listener know how to simulate?

MECHANISM:
ROBOT A:

possible action
→ internal simulation
→ predicted consequence
→ narration

ROBOT B:

narration
→ interpreted action sequence
→ substitution into internal "what-if" machinery
→ simulation
→ evaluated imagined consequence

FORMAL SHIFT:
<COUNTERFACTUAL WORLD-TRAJECTORY>
→ <LINGUISTIC DESCRIPTION>
→ [INTERPRET / SUBSTITUTE]
→ <RE-EXECUTED COUNTERFACTUAL WORLD-TRAJECTORY>

SOURCE FORMALISM:
The Consequence Engine performs a generate-and-test loop over possible next actions, simulating their anticipated consequences before action selection.

The Storybot proposal reuses this machinery by substituting a heard, interpreted sequence for an internally generated candidate sequence.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For description D to be operational between A and B:

encode_A(simulation_A) → D

decode_B(D) → candidate_B

run_B(candidate_B) → simulation_B

Executability therefore requires not merely D but sufficient compatibility between encode_A, decode_B, and B's world model.

TENSION:
Natural-language programming is often described as though language itself became executable.

The Storybot architecture suggests a stricter claim:

language becomes operational only because substantial interpretive and simulation machinery already exists on both sides of the utterance.

MISSING:
A theory of semantic mismatch.

What happens when A and B:
have different bodies,
different action vocabularies,
different world models,
different causal assumptions,
or different meanings for the same description?

BOUNDARY:
The Storybots are deliberately designed conspecific robots sharing closely related internal machinery.

This does not establish arbitrary natural-language executability between heterogeneous systems.

That restriction is the important clue.

CITATION TRAIL:
Winfield's Consequence Engine work.
Simulation theory of cognition.
Dennett's generate-and-test tower.
Communication between heterogeneous agents.
Executable specifications.
Programming by demonstration and instruction.

TEST:
Create two Storybot-like simulators whose internal world models can be varied independently.

Transmit the same counterfactual description while progressively changing:

body geometry,
action vocabulary,
object ontology,
causal rules.

Record the first point at which the listener can still parse the words but can no longer run the described world.

PLATFORM:
[[winfield_blackmore_2022_artificial_culture.platform3]]

LINKS:
[[description-requires-a-machine-that-can-obey]]
[[the-prompt-is-not-the-program]]
[[the-house-that-words-build]]

BIBTEX:
@article{winfield2022artificialculture,
  title={Experiments in Artificial Culture: from noisy imitation to storytelling robots},
  author={Winfield, Alan F. T. and Blackmore, Susan},
  journal={Philosophical Transactions of the Royal Society B: Biological Sciences},
  volume={377},
  number={1843},
  year={2022},
  url={https://arxiv.org/abs/2106.11754}
}
