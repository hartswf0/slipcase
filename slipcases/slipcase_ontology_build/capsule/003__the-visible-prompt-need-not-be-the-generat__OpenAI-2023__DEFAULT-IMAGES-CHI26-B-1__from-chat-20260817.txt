ZETTEL

ID:
DEFAULT-IMAGES-CHI26-B-1

TITLE:
The visible prompt need not be the generator's prompt: an invisible writer can stand between the user and the image model.

SOURCE:
OpenAI — “DALL·E 3” — 2023 — https://openai.com/index/dall-e-3/

PASSAGE:
[PARAPHRASE] OpenAI describes DALL·E 3 as being integrated with ChatGPT such that a user's initial idea is automatically converted into a tailored, more detailed prompt before image generation. The deployed interaction therefore contains an explicit text-transformation stage between what the user says and what the image generator is conditioned on.

RESEARCH OBJECT:
The uncertainty raised in the Midjourney default-image paper is not merely hypothetical system architecture.

At least one major deployed text-to-image pipeline openly inserts another generative language model between:

USER DESCRIPTION

and

IMAGE GENERATOR.

The prompt is therefore potentially a compiled artifact.

LOCAL MOVE:
Distinguish:

USER PROMPT

from:

EXECUTED PROMPT.

SOURCE TERMS:
ChatGPT
tailored prompts
detailed prompts
DALL-E 3
prompt refinement
image generation

WHAT BECAME STRANGE:
A researcher may believe they are probing an image model with nonsense.

But if an upstream language model rewrites nonsense before image generation, the experiment is actually probing:

HOW THE LANGUAGE MODEL INTERPRETS NONSENSE
+
HOW THE IMAGE MODEL INTERPRETS THE LANGUAGE MODEL'S INTERPRETATION.

The “default image” could be downstream of a hidden act of translation.

QUESTION:
Does Midjourney pass unknown strings directly into its image-conditioning stack, or does an unseen preprocessing model rewrite, expand, normalize, classify, or otherwise transform them first?

DEEPER QUESTION:
If several unrelated user prompts are transformed by an upstream model into similar internal descriptions, could apparent image-space defaulting occur even when the image generator itself responds perfectly to its actual inputs?

MECHANISM:
The documented DALL-E 3 pipeline establishes the architecture:

user idea
→ ChatGPT-generated detailed prompt
→ DALL-E 3 generation.

In such a pipeline, convergence can occur before image synthesis.

Two dissimilar user inputs:

u₁ ≠ u₂

can become similar after rewriting:

R(u₁) ≈ R(u₂).

A downstream generator may then rationally produce similar images.

FORMAL SHIFT:
FROM:

USER TEXT
→ IMAGE MODEL
→ IMAGE

TO:

USER TEXT
→ PROMPT TRANSFORMER
→ EXECUTED TEXT
→ IMAGE MODEL
→ IMAGE.

SOURCE FORMALISM:
OpenAI describes ChatGPT as automatically generating tailored, detailed prompts for DALL-E 3 from the user's initial idea.

No mathematical formalism is provided on the source page.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

u = user-visible prompt
R = hidden or visible prompt transformation
G = image generator.

Observed system:

S(u) = G(R(u)).

A default-like convergence can therefore have at least two causal locations:

REWRITE COLLAPSE:

d(u₁,u₂) high
but
d(R(u₁),R(u₂)) low

or

GENERATOR COLLAPSE:

d(R(u₁),R(u₂)) high
but
d(G(R(u₁)),G(R(u₂))) low.

Without R(u), black-box observation cannot distinguish them.

TENSION:
OpenAI's documentation proves this architecture for DALL-E 3.

It does NOT prove that Midjourney uses an analogous prompt rewriter.

Simonen et al. correctly preserve this as an unresolved possibility rather than a demonstrated Midjourney mechanism.

MISSING:
The exact text or conditioning object Midjourney's image generator receives.

The crucial missing observables are:

user prompt u
transformed prompt R(u)
text embedding E(R(u))
generated image G(E(R(u))).

Without at least one intermediate representation, causal localization remains underdetermined.

BOUNDARY:
Evidence from DALL-E 3 establishes architectural possibility and deployed precedent, not Midjourney provenance.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B]]
→ Midjourney causal opacity
→ possibility of prompt rewriting
→ DALL-E 3 provides documented deployed precedent
→ default image splits into PRE-GENERATION COLLAPSE versus GENERATIVE COLLAPSE.

TEST:
Build an experimental pipeline with an inspectable prompt-rewriting LLM before an open diffusion model.

Feed it the same rare names, corrupted words, low-resource words, URLs, glitch tokens, and abbreviations used by Simonen et al.

Measure pairwise distances at three stages:

USER INPUT
R(USER INPUT)
GENERATED IMAGE.

Then compare three conditions:

no rewriting
generic LLM rewriting
rewriter trained to elaborate unknown inputs.

If visually convergent defaults emerge primarily when R maps unrelated inputs onto similar descriptions, then default-like behavior can be manufactured upstream of the image model.

PLATFORM:
DALL-E 3 + ChatGPT as documented example; proposed comparison with Midjourney and inspectable pipelines.

LINKS:
[[DEFAULT-IMAGES-CHI26-B]]

BIBTEX:
@misc{OpenAI2023DALLE3,
  author = {{OpenAI}},
  title = {DALL-E 3},
  year = {2023},
  url = {https://openai.com/index/dall-e-3/}
}
