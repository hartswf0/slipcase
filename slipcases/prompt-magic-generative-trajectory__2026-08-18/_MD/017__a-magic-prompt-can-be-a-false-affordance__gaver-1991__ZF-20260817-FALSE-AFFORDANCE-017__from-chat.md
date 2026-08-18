ZETTEL

ID:
ZF-20260817-FALSE-AFFORDANCE-017

TITLE:
A Magic Prompt Can Be a False Affordance

SOURCE:
William W. Gaver, “Technology Affordances,” Proceedings of CHI ’91, pp. 79–84, 1991.
https://doi.org/10.1145/108844.108856

PASSAGE:
[PARAPHRASE] For Gaver, a false affordance occurs when available information suggests an action that the environment does not actually support; a hidden affordance exists when an action is possible but information about it is unavailable or unnoticed.

RESEARCH OBJECT:
The “magic prompt” can be reframed without deciding in advance whether it is genuine or superstitious.

It is a PERCEIVED AFFORDANCE.

The practitioner believes:

THIS WORD LETS ME DO THAT.

But generative interfaces create at least three radically different cases:

PERCEPTIBLE AFFORDANCE:
the term reliably changes model behavior and the practitioner correctly perceives this.

HIDDEN AFFORDANCE:
the system can be controlled in some way the practitioner has not yet discovered.

FALSE AFFORDANCE:
the practitioner perceives control where no reliable control exists.

Prompt craft therefore involves discovering not merely vocabulary but the action possibilities of an invisible machine.

LOCAL MOVE:
Replace:

MAGIC TERM
versus
USELESS TERM

with:

PERCEPTIBLE AFFORDANCE
HIDDEN AFFORDANCE
FALSE AFFORDANCE
CONTEXT-CONDITIONAL AFFORDANCE.

SOURCE TERMS:
affordance
perceptible affordance
hidden affordance
false affordance
perceptual information
action
technology

WHAT BECAME STRANGE:
Opacity produces two opposite failures.

The practitioner can believe in a lever that does not exist.

But they can also fail to see a lever that does.

Prompt experimentation is therefore not merely optimization.

It is AFFORDANCE DISCOVERY under radically incomplete perceptual information.

QUESTION:
What information allows a practitioner to distinguish a real model affordance from a merely apparent one?

DEEPER QUESTION:
What would a generative interface look like if its actual controllable possibilities were perceptible rather than requiring users to reverse-engineer them through folklore?

MECHANISM:
SYSTEM HAS ACTION POSSIBILITY
+
USER HAS OR LACKS INFORMATION ABOUT POSSIBILITY

→ perceived control state.

The crucial distinction is between:

WHAT THE SYSTEM CAN DO

and:

WHAT THE INTERFACE LEADS THE USER TO THINK THEY CAN DO.

FORMAL SHIFT:
PROMPT TERM
→ EFFECT / NO EFFECT

becomes:

ACTUAL EFFECT POSSIBILITY
×
PERCEIVED EFFECT POSSIBILITY

yielding different classes of control.

SOURCE FORMALISM:
[PARAPHRASE]

Gaver separates:

existence of affordance

from:

perceptual information specifying affordance.

This produces categories including:

perceptible affordance
hidden affordance
false affordance.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

A(t,M) = whether intervention t affords useful control over model M

P_u(t,M) = whether user u perceives that control

Then:

A=1, P=1
→ PERCEPTIBLE CONTROL

A=1, P=0
→ HIDDEN CONTROL

A=0, P=1
→ FALSE CONTROL

A=0, P=0
→ CORRECT REJECTION.

For generative models, add:

A(t,M,c)

where c includes:

prompt context
seed
model version
parameters.

An apparently false affordance may instead be conditional on an unobserved c.

TENSION:
Calling prompt magic a false affordance is too easy.

Some strange linguistic interventions genuinely alter generation.

Conversely, calling every practitioner discovery an affordance is also too easy.

The research problem is precisely that users cannot directly inspect which category they inhabit.

MISSING:
An empirical affordance map of a generative model:

what actions are possible
which are documented
which are discoverable
which users perceive
which users falsely perceive
which change across versions.

BOUNDARY:
Gaver’s affordance theory concerns perception and action in technologies generally.

It does not claim that prompts are affordances or describe generative models.

That extension is ours.

CITATION TRAIL:
[[ZF-20260817-SUPERSTITION-VARIANCE-006]]
[[ZF-20260817-VOCABULARY-GAP-002]]
→ users cannot reliably infer which prompt elements matter
→ Gaver separates actual action possibilities from perceptual information about them
→ magic prompt becomes a problem of hidden versus false affordance
→ next edge: design interfaces that expose causal affordances without eliminating exploratory discovery

TEST:
Create a generative system whose actual prompt sensitivities are instrumented and known experimentally.

Ask users to map:

WHAT CAN I CONTROL?

Compare their perceived map against the measured map.

Classify each claimed prompt operation as:

PERCEPTIBLE
HIDDEN
FALSE
CONTEXT-CONDITIONAL.

Then alter the interface to expose:
effect previews
ablation
sensitivity indicators
or causal comparisons.

Test whether increased affordance visibility reduces superstition while preserving exploration.

PLATFORM:
human-computer interaction
generative interfaces
prompt systems

LINKS:
[[ZF-20260817-SUPERSTITION-VARIANCE-006]]
[[ZF-20260817-VOCABULARY-GAP-002]]
[[PROMPT-AFFORDANCE]]
[[FALSE-AFFORDANCE]]
[[HIDDEN-CONTROL]]
[[EXPLAINABLE-CREATIVE-INTERFACE]]

BIBTEX:
@inproceedings{gaver1991technology,
  author={Gaver, William W.},
  title={Technology Affordances},
  booktitle={Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
  pages={79--84},
  year={1991},
  doi={10.1145/108844.108856}
}
