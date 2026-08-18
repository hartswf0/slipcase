ZETTEL

ID:
SON-CONTROL-003

TITLE:
CONTROL in diffusion is divisible: seed controls reproducibility while guidance controls a fidelity–diversity tradeoff.

SOURCE:
Jonathan Ho & Tim Salimans — “Classifier-Free Diffusion Guidance” — 2022. URL: https://arxiv.org/abs/2207.12598
CompVis — Stable Diffusion reference implementation. URL: https://github.com/CompVis/stable-diffusion

PASSAGE:
[QUOTE]
Ho and Salimans describe guidance as a way to “trade off mode coverage and sample fidelity.”

RESEARCH OBJECT:
GENERATIVE CONTROL is not one variable.

It decomposes into different interventions over stochastic generation.

LOCAL MOVE:
The parent repeatedly places users between “having more control over [the AI]” and deliberately ceding control to discover unexpected outputs.

The technical machinery suggests that CONTROL must be split before it can be analyzed.

SOURCE TERMS:
classifier-free guidance
conditional
unconditional
score estimate
guidance
mode coverage
sample fidelity
seed
sampling

WHAT BECAME STRANGE:
The opposition between CONTROL and RANDOMNESS may be falsely binary.

A generation can simultaneously have:

fixed stochastic initialization
strong textual conditioning
high semantic adherence
unexpected local detail
multiple possible outputs

“More control” therefore requires naming which degree of freedom has been constrained.

QUESTION:
Which kinds of control were Midjourney super users actually learning to exercise?

DEEPER QUESTION:
Can prompt craft be decomposed into separate control dimensions whose effects can be experimentally distinguished?

MECHANISM:
Classifier-free guidance combines an unconditional prediction with the difference between conditional and unconditional predictions.

Stable Diffusion’s reference implementation additionally exposes a seed, sampler settings, number of steps, and guidance scale.

Thus different controls intervene at different points.

FORMAL SHIFT:
FROM:

CONTROL ←→ RANDOMNESS

TO:

CONTROL =
{
INITIALIZATION CONTROL,
CONDITION CONTROL,
GUIDANCE CONTROL,
SAMPLER CONTROL,
ITERATION CONTROL,
SELECTION CONTROL
}

RANDOMNESS operates inside this constrained system rather than simply opposing it.

SOURCE FORMALISM:
[QUOTE — SOURCE SYNTAX]

eps = eps(x, empty) + scale * (eps(x, cond) - eps(x, empty))

The Stable Diffusion reference script also exposes:

--seed
--scale
--ddim_steps
--n_samples

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OUTPUT =
GENERATE(
  seed,
  prompt,
  guidance,
  sampler,
  steps,
  model
)

USER_CONTROL =
ability to intentionally constrain one or more arguments while observing resulting variation.

CEDING_CONTROL =
deliberately leaving one or more arguments unconstrained or exploring their variation.

TENSION:
A user can increase semantic prompt adherence while decreasing diversity.

Therefore “more control” can destroy exactly the novelty that the user values.

The parent’s control/serendipity tension may be an actual technical tradeoff rather than merely an artistic attitude.

MISSING:
The exact sampling and guidance machinery used by Midjourney V3.

Whether Midjourney exposed equivalent hidden or explicit parameters.

Whether interviewees distinguished reproducibility from semantic adherence when saying “control.”

BOUNDARY:
Classifier-free guidance and Stable Diffusion parameters establish mechanisms available in one documented diffusion architecture.

They do not establish identical implementation in Midjourney.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ control versus ceding control
→ classifier-free guidance
→ fidelity/diversity tradeoff
→ Stable Diffusion seed/guidance/sampler controls
→ CONTROL splits into independently manipulable dimensions

TEST:
Use an open text-to-image diffusion model.

Hold model and prompt constant.

Run factorial comparisons varying only:

A. seed
B. guidance scale
C. sampling steps
D. prompt wording

Measure separately:

image-image variance
text-image similarity
human aesthetic preference
structural reproducibility

Determine which intervention corresponds most closely to interviewees’ language of “control.”

PLATFORM:
arXiv / GitHub

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]
[[SON-LATENT-002]]

BIBTEX:
@misc{ho2022classifierfree,
  title = {Classifier-Free Diffusion Guidance},
  author = {Jonathan Ho and Tim Salimans},
  year = {2022},
  eprint = {2207.12598},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2207.12598}
}

@misc{compvis_stablediffusion,
  author = {{CompVis}},
  title = {Stable Diffusion: A Latent Text-to-Image Diffusion Model},
  howpublished = {GitHub repository},
  url = {https://github.com/CompVis/stable-diffusion}
}
