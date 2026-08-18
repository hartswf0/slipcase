ZETTEL

ID:
WORKWORDS-PROMPT-003

TITLE:
What a prompt leaves unsaid can function like borrowed code supplied by the model.

SOURCE:
Chenyang Yang, Yike Shi, Qianou Ma, Michael Xieyang Liu, Christian Kästner, and Tongshuang Wu — “What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts” — 2025 — arXiv:2505.13360

PASSAGE:
[PARAPHRASE] Yang et al. systematically study requirements omitted from prompts. Models sometimes satisfy unspecified requirements anyway, but those behaviors are substantially less stable across prompt and model changes.

[PARAPHRASE] More surprisingly, explicitly adding every known requirement does not solve the problem. As more requirements are placed together in one prompt, instruction-following performance can decline. The authors therefore explore optimizing not only how requirements are written but which requirements should be stated at all.

RESEARCH OBJECT:
A PROMPT IS PARTLY MADE OF WHAT IT DOES NOT SAY.

Unspecified behavior is not empty.

It is temporarily supplied by:

model priors,
post-training,
context,
task conventions,
and accidental defaults.

The operative artifact is therefore larger than its written text.

LOCAL MOVE:
Replace:

THICK PROMPT = MORE SPECIFICATION = MORE CONTROL

with:

PROMPT DESIGN = SELECTIVE DISTRIBUTION OF EXPLICIT AND IMPLICIT CONTROL.

SOURCE TERMS:
underspecification
requirements
specified requirements
unspecified requirements
behavioral stability
requirement-aware prompt optimization
conditional requirements

WHAT BECAME STRANGE:
Writing another instruction can make an instruction already present less likely to be followed.

Specification is not monotonically additive.

More words can produce less control.

QUESTION:
What should a prompt deliberately leave unstated?

DEEPER QUESTION:
Can omission itself become a designed computational resource rather than an accidental deficiency?

MECHANISM:
Requirements compete for finite instruction-following capacity.

Some omitted requirements are already reliably supplied by model behavior.

Others are supplied only contingently.

Therefore an effective prompt can require choosing:

which requirements must be textualized

and

which may safely remain delegated to the model.

FORMAL SHIFT:
FROM:

PROMPT QUALITY ∝ AMOUNT SPECIFIED

TO:

PROMPT QUALITY
= selection of an effective subset of requirements
under model-specific interaction constraints.

SOURCE FORMALISM:
The authors represent candidate requirements as a binary vector:

r = (r1,...,rn) ∈ {0,1}^n

where a requirement is specified or unspecified.

Their requirement-selection optimizer seeks:

r* = argmax f(r),

where f evaluates system performance under that configuration.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let total operative specification be:

S_total =
S_written
+
S_model
+
S_context
+
S_examples
+
S_interface.

A prompt edit changes only one component:

ΔS_written.

But execution depends on interactions among all five.

Therefore:

more(S_written)

does not imply:

more(control).

TENSION:
Software-engineering language frames underspecification largely as a reliability problem.

For creative prompt practice, controlled underspecification may instead be productive.

The same gap can be:

BUG
or
GENERATIVE APERTURE.

The distinction depends on the purpose of the work.

MISSING:
A theory distinguishing:

dangerous omission,
redundant specification,
productive ambiguity,
delegated convention,
and deliberate openness.

BOUNDARY:
The source evaluates application prompts against articulated requirements. Creative writing, image generation, speculative design, and artistic prompting may value output variation differently.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-A]]
→ known terms compete with unknown terms
→ Yang et al.
→ explicit requirements themselves compete
→ more description can reduce obedience
→ next edge: productive underspecification and controlled ambiguity as prompt craft.

TEST:
Begin with a successful long prompt.

Extract every apparent requirement.

Generate systematic ablations.

For each requirement measure:

performance when explicit,
performance when absent,
variance when absent,
interference with other requirements.

Classify each clause as:

NECESSARY
REDUNDANT
INTERFERING
STABILIZING
GENERATIVE-OPENING.

PLATFORM:
LLM-powered applications; requirements-aware prompt optimization.

LINKS:
[[DEFAULT-IMAGES-CHI26-A]]

BIBTEX:
@article{Yang2025PromptsDontSay,
  author = {Yang, Chenyang and Shi, Yike and Ma, Qianou and Liu, Michael Xieyang and K{\"a}stner, Christian and Wu, Tongshuang},
  title = {What Prompts Don't Say: Understanding and Managing Underspecification in LLM Prompts},
  year = {2025},
  url = {https://arxiv.org/abs/2505.13360}
}
