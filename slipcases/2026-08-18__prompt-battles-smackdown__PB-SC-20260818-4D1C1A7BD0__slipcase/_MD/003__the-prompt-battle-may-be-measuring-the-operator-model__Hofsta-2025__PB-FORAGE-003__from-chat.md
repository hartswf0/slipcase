ZETTEL

ID:
PB-FORAGE-003

TITLE:
The Prompt Battle may be measuring the operator-model pair rather than the model.

SOURCE:
Hofstätter et al. — The Elicitation Game: Evaluating Capability Elicitation Techniques — 2025 — arXiv:2502.02180.

PASSAGE:
[PARAPHRASE]
Capability measurement depends on the procedure used to elicit capability; prompting can reveal some hidden capabilities while stronger interventions reveal others.

RESEARCH OBJECT:
PB_PRIME quietly introduces a new experimental organism:

    MODEL
    +
    SYSTEM BUILDER
    +
    PROMPT PILOT.

Once these roles exist, “AI performance” is no longer an attribute of the AI alone.

LOCAL MOVE:
Treat prompting expertise as an experimental treatment, not nuisance variance.

SOURCE TERMS:
elicitation technique
latent capability
prompting
capability evaluation

WHAT BECAME STRANGE:
PB_PRIME separately proposes:

    a System Builder who defines the sandbox and constraints,
    a Prompt Pilot who steers within it,
    participant expertise classification,
    “epistemic camp” identification,
    scoring for sophisticated prompting.

Then it repeatedly speaks as though the resulting completion revealed “what AI can do.”

QUESTION:
Whose capability is being measured when expert prompting improves model performance?

DEEPER QUESTION:
Is there even a context-free capability of an interactive generative model worth estimating, or is the useful object an elicitation frontier indexed by operator competence?

MECHANISM:
The human chooses interventions based on previous outputs.

Therefore the prompt sequence is a policy:

    π_h(history) → next intervention.

Different humans implement different policies over the same model.

Performance therefore emerges from the coupled trajectory.

FORMAL SHIFT:
<MODEL>
→ <MODEL + OPERATOR POLICY + HISTORY>
→ [ITERATIVE ELICITATION]
→ <OBSERVED CAPABILITY FRONTIER>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Observed performance:

    Y = F(M, S, π_h, H, J)

where:

    M   = model
    S   = system configuration
    π_h = human prompting policy
    H   = interaction history
    J   = judgment procedure

A model comparison that changes π_h is confounded.

A prompter comparison holding M fixed is an HCI experiment.

A battle in which both co-adapt is an experiment on the coupled system.

TENSION:
The System Builder / Prompt Pilot split is initially presented as a competition mechanic.

It may be the archive’s most consequential methodological invention because it makes orchestration experimentally visible.

MISSING:
Crossed measurements of:

    model × System Builder × Prompt Pilot × flag.

Without these, exceptional performance can be credited to the wrong actor.

BOUNDARY:
This does not imply that models have no independently measurable properties. It means interactive capability claims must specify the elicitation procedure that generated them.

CITATION TRAIL:
Interactive machine learning.
Mixed-initiative interaction.
Machine teaching.
Capability elicitation.

TEST:
Run a crossed tournament:

    4 models
    × 8 Prompt Pilots
    × 4 System Builders
    × identical frozen flags.

Rotate every human across every model.

Estimate variance attributable to:

    model
    pilot
    system
    model × pilot interaction.

Then ask whether rankings survive operator rotation.

PLATFORM:
[[Human Model Systems]]

LINKS:
[[Prompt Pilot]]
[[System Builder]]
[[Elicitation Frontier]]

BIBTEX:
@article{hofstatter2025elicitation,
  title={The Elicitation Game: Evaluating Capability Elicitation Techniques},
  author={Hofst{\"a}tter, Felix and van der Weij, Teun and Teoh, Jayden and Djoneva, Rada and Bartsch, Henning and Ward, Francis Rhys},
  journal={arXiv preprint arXiv:2502.02180},
  year={2025},
  doi={10.48550/arXiv.2502.02180}
}
