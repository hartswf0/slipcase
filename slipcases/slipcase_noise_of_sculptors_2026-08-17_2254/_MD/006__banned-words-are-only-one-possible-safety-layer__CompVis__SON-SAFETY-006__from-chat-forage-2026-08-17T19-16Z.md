ZETTEL

ID:
SON-SAFETY-006

TITLE:
BANNED WORDS are only one possible safety layer; Stable Diffusion places a safety intervention after image generation.

SOURCE:
CompVis — Stable Diffusion reference implementation — 2022. URL: https://github.com/CompVis/stable-diffusion
CompVis — Stable Diffusion v1-4 Model Card. URL: https://huggingface.co/CompVis/stable-diffusion-v1-4

PASSAGE:
[QUOTE]
The reference sampler includes “a Safety Checker Module, to reduce the probability of explicit outputs.”

RESEARCH OBJECT:
SAFETY MODERATION must be decomposed by INTERVENTION POINT.

LOCAL MOVE:
The parent reports a Midjourney moderation mechanism in which words receive numeric NSFW values, prompts can be blocked, and escalating behavior can trigger timeouts or bans.

It also notes the contextual problem that terms such as “blood” can participate in both controversial and ordinary phrases.

The Stable Diffusion pipeline exposes a different possibility: image safety can also be evaluated after synthesis.

SOURCE TERMS:
Safety Checker Module
explicit outputs
text-to-image
prompt
CLIP text encoder
sampling
bias
misuse

WHAT BECAME STRANGE:
“THE NSFW ALGORITHM” may not be one algorithm.

Safety can intervene at several technically distinct locations:

training data
model training
prompt preprocessing
lexical blocking
generation
output classification
publication
account enforcement

A community may combine several simultaneously.

QUESTION:
At which exact computational layer did each Midjourney 2022 moderation mechanism operate?

DEEPER QUESTION:
What political and semantic consequences change when safety policy is attached to WORDS rather than generated IMAGES, model training data, user behavior, or publication?

MECHANISM:
The documented Stable Diffusion reference pipeline conditions generation on text embeddings and then incorporates a separate Safety Checker Module in the sampling pipeline.

The safety mechanism therefore need not operate by forbidding prompt vocabulary before generation.

FORMAL SHIFT:
FROM:

BANNED WORD
→ BLOCK

TO:

INPUT
→ INPUT MODERATION?
→ TEXT REPRESENTATION
→ GENERATION
→ OUTPUT MODERATION?
→ PUBLICATION
→ COMMUNITY MODERATION?
→ ACCOUNT SANCTION?

SOURCE FORMALISM:
[PARAPHRASE]

Stable Diffusion:

prompt
→ CLIP text embedding
→ conditioned latent diffusion
→ generated image
→ Safety Checker Module

The reference script separately exposes generation controls including seed and guidance.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SAFETY_SYSTEM =
{
TRAIN_FILTER,
INPUT_FILTER,
GENERATION_CONSTRAINT,
OUTPUT_CLASSIFIER,
VISIBILITY_FILTER,
BEHAVIOR_POLICY,
ACCOUNT_ENFORCEMENT
}

Each layer has a different error surface.

For lexical filtering:

FALSE_POSITIVE =
benign use of prohibited token blocked

FALSE_NEGATIVE =
harmful intent expressed without prohibited token

For output filtering:

FALSE_POSITIVE =
benign generated image classified unsafe

FALSE_NEGATIVE =
unsafe generated image classified safe

TENSION:
Lexical prohibition acts early and cheaply but struggles with polysemy, metaphor, identity terms, translation, misspelling, and circumvention.

Output classification can inspect what was actually generated but permits generation to occur before intervention and introduces its own classifier errors.

Neither layer solves moderation by itself.

MISSING:
Primary technical documentation for Midjourney’s 2022 NSFW scoring system.

Whether the numeric values reported by moderators applied to:

prompt tokens
user risk
generated imagery
bot heuristics
or combinations of these.

The relationship between automated filtering and moderator judgment.

BOUNDARY:
The Stable Diffusion safety checker is evidence that a different safety architecture existed in a neighboring text-to-image system.

It is not evidence that Midjourney used the same checker.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ hidden banned-word list
→ context failures
→ numeric NSFW values
→ Stable Diffusion reference safety pipeline
→ distinction between INPUT MODERATION and OUTPUT MODERATION
→ safety becomes a layered architecture problem

TEST:
Reconstruct the 2022 Midjourney moderation pipeline exclusively from contemporaneous primary evidence.

For every observed intervention, identify:

INPUT
STATE AVAILABLE
DECISION RULE
ACTION
HUMAN/MACHINE
TIMING

Classify each as:

PRE-GENERATION
IN-GENERATION
POST-GENERATION
POST-PUBLICATION
ACCOUNT-LEVEL

Do not use the phrase “NSFW algorithm” until these mechanisms have been separated.

PLATFORM:
GitHub / Hugging Face

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]
[[SON-GENEALOGY-001]]

BIBTEX:
@misc{compvis_stablediffusion,
  author = {{CompVis}},
  title = {Stable Diffusion: A Latent Text-to-Image Diffusion Model},
  howpublished = {GitHub repository},
  url = {https://github.com/CompVis/stable-diffusion}
}

@misc{compvis_sd14_modelcard,
  author = {{CompVis}},
  title = {Stable Diffusion v1-4 Model Card},
  howpublished = {Hugging Face},
  url = {https://huggingface.co/CompVis/stable-diffusion-v1-4}
}
