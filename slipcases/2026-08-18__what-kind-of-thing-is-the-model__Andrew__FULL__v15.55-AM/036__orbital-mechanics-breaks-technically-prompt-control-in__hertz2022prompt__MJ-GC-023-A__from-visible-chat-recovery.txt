ZETTEL

ID:
MJ-GC-023-A

TITLE:
“Orbital mechanics” breaks technically: prompt control in diffusion is better modeled as token-pixel attention scheduled through time than as travel through a latent galaxy.

SOURCE:
Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, Daniel Cohen-Or — “Prompt-to-Prompt Image Editing with Cross Attention Control” — 2022.
URL: https://arxiv.org/abs/2208.01626

PASSAGE:
[PARAPHRASE]
Hertz et al. find that cross-attention maps connect prompt tokens to spatial regions of the generated image and critically affect generation. Their method can replace a word while preserving composition, introduce a new specification while retaining previous attention, and amplify or attenuate the effect of an individual word. Crucially, control can also depend on when attention information is injected during the diffusion process.

RESEARCH OBJECT:
PROMPT-CRAFT-AS-TEMPORAL-ATTENTION-CONTROL.

LOCAL MOVE:
[[MJ-GC-023]] imagined expert prompting as choosing a trajectory through unequal semantic gravity wells. Prompt-to-Prompt supplies actual machinery that both preserves and overturns that intuition.

The useful part survives:
words do exert unequal and manipulable effects.

The spatial mechanics do not survive intact.

For diffusion systems of this kind, a more technically grounded control object is:
which image regions attend to which prompt tokens, by how much, during which diffusion steps.

Prompt expertise may therefore resemble trajectory design only after “trajectory” is translated from movement through a semantic galaxy into intervention over an evolving attention process.

SOURCE TERMS:
“cross-attention maps”
“pixels”
“tokens”
“diffusion process”
“amplify”
“attenuate”
“semantic effect”

WHAT BECAME STRANGE:
The variable corresponding most closely to “orbital mechanics” may be TIME.

The same word need not exert one fixed semantic force throughout generation. Its influence can be mediated differently across stages of an iterative image-forming process.

The folk theory treats the prompt as a position.

The technical source makes prompting look more like a CONTROL SCHEDULE.

QUESTION:
Is expert prompt craft better understood as choosing semantic locations, or as indirectly manipulating when and where token-conditioned constraints enter an iterative generative process?

DEEPER QUESTION:
When users discover that certain prompt arrangements reliably preserve, destroy, or redirect image structure, are they learning an undocumented temporal control system without access to its internal attention maps?

MECHANISM:
TEXT TOKENS
→ cross-attention maps binding tokens to spatial image structure
→ attention participates across diffusion steps
→ image structure emerges.

CONTROL can intervene by:
REPLACE TOKEN
while preserving selected attention structure

or

ADD TOKEN
while allowing new attention to enter

or

REWEIGHT TOKEN EFFECT
→ strengthen / weaken semantic manifestation.

FORMAL SHIFT:
FROM:
PROMPT
→ POSITION IN SEMANTIC FIELD
→ TRAJECTORY
→ OUTPUT

TO:
PROMPT TOKENS
→ TOKEN↔PIXEL ATTENTION
→ ATTENTION THROUGH DIFFUSION TIME
→ STRUCTURE / ATTRIBUTE FORMATION
→ OUTPUT.

SOURCE FORMALISM:
[PARAPHRASE]
Prompt-to-Prompt operates on cross-attention maps inside a pretrained text-conditioned diffusion model.

The paper describes interventions including:
1. replacing a prompt token while injecting attention maps from the original generation,
2. adding words while preserving attention associated with previous tokens,
3. increasing or decreasing the semantic influence of selected words.

The authors explicitly treat cross-attention as a control handle connecting textual tokens with spatial image structure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

A(token, pixel, t)

represent the effective relation between prompt token, image location, and diffusion step t.

Then prompt “force” is not adequately represented as:

FORCE(token) = constant.

A better hypothesis is:

EFFECT(token)
= Σ_t Σ_pixel A(token, pixel, t)

subject to interactions with other tokens and the denoising state.

Prompt craft may therefore be approximated as:

LANGUAGE
→ INDIRECT ATTENTION PROGRAM
→ TEMPORAL IMAGE CONSTRUCTION.

TENSION:
The Midjourney interview concerns a proprietary system whose architecture is not established by this source.

Prompt-to-Prompt studies diffusion models and demonstrates a possible mechanism, not Midjourney's internal implementation.

The child's correction is therefore conceptual and technical, not a claim that Midjourney literally uses the same cross-attention machinery.

MISSING:
A way to infer from black-box outputs whether Midjourney prompt phenomena such as the “Mona Lisa black hole” behave like:
semantic embedding dominance,
cross-attention competition,
training-frequency priors,
or some other mechanism.

BOUNDARY:
Do not redescribe the interviewee's galaxy metaphor as secretly describing cross-attention.

Similarity of observable behavior is not identity of mechanism.

CITATION TRAIL:
[[MJ-GC-023]]
→ “orbital mechanics” as prompt trajectory
→ Hertz et al. 2022
→ token-pixel cross-attention can be intervened upon across diffusion
→ semantic navigation splits into SPATIAL, WEIGHT, and TEMPORAL control.

TEST:
Operationalize one “slingshot” prompt from [[MJ-GC-023]] in an open diffusion model.

Generate:
A
A + B
A + B + C

Then use Prompt-to-Prompt-style attention interventions to separately manipulate:
1. token identity,
2. token strength,
3. attention duration across diffusion steps.

Determine whether the behavior attributed to semantic “trajectory” can be reproduced by temporal or spatial attention control without invoking a latent-gravity explanation.

PLATFORM:
Text-conditioned diffusion models / Prompt-to-Prompt

LINKS:
[[MJ-GC-023]]
[[MJ-GC-019]]
[[MJ-GC-020]]
[[MJ-GC-022]]

BIBTEX:
@article{hertz2022prompt,
  title={Prompt-to-Prompt Image Editing with Cross Attention Control},
  author={Hertz, Amir and Mokady, Ron and Tenenbaum, Jay and Aberman, Kfir and Pritch, Yael and Cohen-Or, Daniel},
  journal={arXiv preprint arXiv:2208.01626},
  year={2022},
  url={https://arxiv.org/abs/2208.01626}
}
