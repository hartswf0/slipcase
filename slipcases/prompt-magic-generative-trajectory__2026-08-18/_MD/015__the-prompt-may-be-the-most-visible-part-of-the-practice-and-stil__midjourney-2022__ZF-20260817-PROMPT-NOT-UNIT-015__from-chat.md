ZETTEL

ID:
ZF-20260817-PROMPT-NOT-UNIT-015

TITLE:
The Prompt May Be the Most Visible Part of the Practice and Still Not Be Its Unit

SOURCE:
[PRIMARY ARCHIVE] Midjourney research archive supplied by user.
SOURCE URL: local:_RESOURCES/Midjourney_prompt_magic_archive_2022.md

Historical parameter notes document seed, negative prompting, image weights, stylize, quality, chaos, model version, and other controls beyond ordinary descriptive prose.

[AUTHORITATIVE TECHNICAL SOURCE] Midjourney, “Parameter List.”
https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List

PASSAGE:
[PRIMARY ARCHIVE]

“How does the ‘magical prompt’ compare with other forms of creative production with MJ such as ‘V Rolling’?”

“A stumbling, wandering, accidental approach to creating with MJ”

“Is there a difference between prompt craft and prompt magic?”

“How do approaches to prompt craft account for the latent space of possibilities in the algorithm?”

RESEARCH OBJECT:
The archive keeps trying to escape the prompt.

That may be its deepest finding.

Each time “prompting” seems to stabilize as the creative act, another operation appears:

ROLL
WEIGHT
SEED
REMIX
VARIATE
SHORTEN
OBSERVE
SELECT
ABANDON
FOLLOW
RELEARN
SURRENDER.

The prompt remains culturally central because it is legible.

It is a sentence.
It can be screenshotted.
It can be shared.
It looks like authorship.

But the actual practice is a trajectory through state.

The research object may therefore not be:

PROMPT.

It may be:

SESSION.

LOCAL MOVE:
Replace the unit:

PROMPT

with:

GENERATIVE TRAJECTORY.

SOURCE TERMS:
prompt craft
prompt magic
V Rolling
wandering
latent space
seed
weight
stylize
chaos
version
remix
exploration

WHAT BECAME STRANGE:
The object easiest to quote may be the wrong object to study.

A final prompt can erase the history that produced it.

It does not show:

the failed prompts
the abandoned directions
the rolls
the moments of surprise
the parameter changes
the copied phrases
the model version
the selected seed
the discarded outputs
the point where the artist’s goal changed.

The prompt is a residue of a process.

QUESTION:
What evidence disappears when AI-art research treats the final prompt as the creative object?

DEEPER QUESTION:
What is the minimal complete unit of generative practice?

A string?

A prompt-output pair?

A branching session?

A human-model history?

A socially embedded trajectory across model versions?

MECHANISM:
INITIAL INTENTION
→ PROMPT₀
→ OUTPUT SET₀
→ JUDGMENT
→ REROLL / EDIT / WEIGHT / REMIX / SELECT
→ OUTPUT SET₁
→ CHANGED INTENTION
→ ...
→ STOP.

The desired artifact and the specification co-develop.

FORMAL SHIFT:
FORAGE:

PROMPT → OUTPUT

becomes:

STATE₀
→ ACTION₀
→ STATE₁
→ OBSERVATION₁
→ REVISED GOAL₁
→ ACTION₁
→ ...
→ ARTIFACT.

SOURCE FORMALISM:
[PARAPHRASE] Midjourney’s interface exposes many controls in addition to prompt text, including model version and other generation parameters.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A generative session S:

S = {
  M₀,
  I₀,
  a₀,
  x₀,
  J₀,
  M₁,
  I₁,
  a₁,
  x₁,
  J₁,
  ...
}

where:

M = model state/version
I = current intention
a = user operation
x = generated state/output
J = human judgment

Crucially:

Iₜ₊₁ ≠ Iₜ

may occur because:

xₜ

reveals a possibility the user could not specify at t₀.

Thus the specification is endogenous to execution.

TENSION:
Prompt-centered theory has an enormous practical advantage:

the prompt is recordable.

Trajectory-centered theory is messier but may be more faithful.

The danger is methodological convenience masquerading as ontology.

MISSING:
Lossless session traces.

Most published AI artworks preserve:
final image
sometimes final prompt.

They rarely preserve the operational genealogy that would make the creative process analyzable.

BOUNDARY:
Some generative tasks really are one-shot.

The claim is not that prompts never matter.

It is that prompt-centric analysis must demonstrate rather than assume that the prompt is the operative unit.

CITATION TRAIL:
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
[[ZF-20260817-REROLL-OPERATOR-009]]
[[ZF-20260817-STYLIZE-AGENCY-DIAL-010]]
[[ZF-20260817-DOCUMENTARY-MODE-012]]
→ prompt fails to specify execution
→ reroll adds sampling
→ stylize adds intentional delegation
→ documentary mode adds situated observation
→ archive repeatedly asks how these modes differ
→ new object: GENERATIVE TRAJECTORY
→ next edge: define a portable execution trace for generative authorship

TEST:
Instrument a generative interface to record every:

prompt
parameter
model version
seed
generation
variation
selection
deletion
reference image
elapsed interval
user note.

After completing a work, compare three representations:

A. FINAL IMAGE
B. FINAL PROMPT + IMAGE
C. FULL TRAJECTORY

Give each to independent researchers and ask them to infer:
artist intention
creative strategy
skill
degree of model contribution
moment of conceptual change.

Measure what becomes visible only in C.

PLATFORM:
Midjourney
generative interfaces
prompt-based systems
iterative creation

LINKS:
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
[[ZF-20260817-REROLL-OPERATOR-009]]
[[ZF-20260817-STYLIZE-AGENCY-DIAL-010]]
[[ZF-20260817-DOCUMENTARY-MODE-012]]
[[PROMPT-IS-NOT-THE-PROGRAM]]
[[GENERATIVE-TRAJECTORY]]
[[DEFERRED-FORMALIZATION]]
[[THEORY-OF-THE-PROGRAM]]

BIBTEX:
@misc{midjourneyParameters,
  author={{Midjourney}},
  title={Parameter List},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List}
}
