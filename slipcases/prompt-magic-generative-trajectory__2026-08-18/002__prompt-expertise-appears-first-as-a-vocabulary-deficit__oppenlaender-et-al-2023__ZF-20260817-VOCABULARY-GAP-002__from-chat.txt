ZETTEL

ID:
ZF-20260817-VOCABULARY-GAP-002

TITLE:
Prompt Expertise Appears First as a Vocabulary Deficit

SOURCE:
Jonas Oppenlaender, Rhema Linder, and Johanna Silvennoinen, “Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering” (2023; revised 2024).
https://arxiv.org/abs/2303.13534

PASSAGE:
[PARAPHRASE] Across three studies, participants could judge prompt quality and construct descriptive prompts, but lacked the style-specific vocabulary needed for effective prompting. The authors interpret this as evidence that prompt engineering is non-intuitive and acquired through practice and learning.

RESEARCH OBJECT:
Millière says artistic prompting requires “a unique vision” plus knowledge of the right words.

The experiment separates those two capacities.

A person may recognize a better result and know roughly what they want while remaining unable to produce the linguistic intervention that causes the model to approach it.

The bottleneck is therefore not necessarily imagination.

It can be lexical access.

This creates an unusual creative situation:

the person can possess evaluative competence before generative control.

They can know:

NOT THAT.

They may even know:

THAT IS CLOSER.

Yet they cannot formulate the operation that moves the system from one to the other.

LOCAL MOVE:
Split “creative skill” into at least three capacities:

1. envisioning
2. evaluating
3. intervening

Do not treat them as one faculty.

SOURCE TERMS:
prompt quality
descriptive prompts
style-specific vocabulary
creative skill
non-intuitive skill
practice
learning

WHAT BECAME STRANGE:
A person can be visually competent but prompt-incompetent.

Prompting therefore introduces a translation bottleneck between aesthetic judgment and executable intervention.

The skilled eye does not automatically possess the skilled sentence.

QUESTION:
What exactly has someone learned when they become a better prompter if their underlying aesthetic judgment was already present?

DEEPER QUESTION:
Is prompt literacy a new artistic competence, or is it an interface tax imposed between an already competent human judgment and an opaque generative system?

MECHANISM:
[PARAPHRASE] Participants were asked to discern prompt quality, compose prompts, and refine prompts. Performance suggested that recognizing quality was easier than possessing the specialized vocabulary required for effective generation.

FORMAL SHIFT:
ARTISTIC INTENTION
→ PROMPT
→ IMAGE

must be split into:

INTENTION
→ EVALUATIVE MODEL
→ AVAILABLE VOCABULARY
→ INTERVENTION
→ GENERATED CANDIDATE
→ EVALUATION
→ REVISION

SOURCE FORMALISM:
[PARAPHRASE]

Three empirical tasks:

discern prompt quality
→ write prompts
→ refine prompts

The study treats performance differences among these tasks as evidence relevant to whether prompting is intuitive or acquired.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

V = desired visual state
J(x) = human judgment of candidate x
L = available intervention vocabulary
G(p) = model output under prompt p

A user may have:

J(G(p₂)) > J(G(p₁))

without knowing any:

δp ∈ L

such that:

J(G(p₁ + δp)) > J(G(p₁))

Thus:

ABILITY TO RECOGNIZE IMPROVEMENT
≠
ABILITY TO PRODUCE THE CONTROL SIGNAL

TENSION:
If specialized vocabulary must be learned, prompting looks like genuine expertise.

But if the vocabulary exists only because the interface poorly exposes controllable variables, the same evidence can be read in reverse:

the expertise may be compensation for a bad control surface.

Skill and interface friction are observationally entangled.

MISSING:
The experiment does not by itself establish whether the learned skill is durable after changes in models or interfaces.

Nor does it establish whether richer controls would eliminate the observed vocabulary advantage.

BOUNDARY:
The findings establish differences in prompt-related performance under the studied conditions. They do not establish that natural-language prompting will remain a stable creative profession or enduring artistic medium.

CITATION TRAIL:
[[MILLIERE-2022-WIRED-AI-CURATION]]
→ claim that interesting AI art requires skill and intentionality
→ Oppenlaender, Linder, Silvennoinen: evaluative ability can outrun style-specific prompt vocabulary
→ unresolved edge: distinguish NEW CREATIVE SKILL from INTERFACE-INDUCED COMPENSATORY SKILL

TEST:
Give expert visual artists with no prompting experience the same target-image tasks through three interfaces:

A. text prompt only
B. direct visual controls
C. multimodal reference + iterative editing

Hold model capability constant.

Measure:
iterations to target
semantic vocabulary required
subjective control
transfer to a second model

If the “prompt expertise” gap collapses under B or C, much of the measured skill belongs to the interface rather than the artistic task.

PLATFORM:
text-to-image generation
crowdsourced prompting experiments
human-computer interaction

LINKS:
[[MILLIERE-2022-WIRED-AI-CURATION]]
[[EVALUATION-PRECEDES-CONTROL]]
[[PROMPTING-AS-INTERFACE-TAX]]
[[DEFERRED-FORMALIZATION]]

BIBTEX:
@article{oppenlaender2023prompting,
  title={Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering},
  author={Oppenlaender, Jonas and Linder, Rhema and Silvennoinen, Johanna},
  journal={arXiv preprint arXiv:2303.13534},
  year={2023},
  url={https://arxiv.org/abs/2303.13534}
}
