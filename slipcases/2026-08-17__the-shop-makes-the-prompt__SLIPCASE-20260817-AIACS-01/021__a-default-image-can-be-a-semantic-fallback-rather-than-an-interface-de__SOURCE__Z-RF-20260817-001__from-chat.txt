ZETTEL

ID:
Z-RF-20260817-001

TITLE:
A default image can be a semantic fallback rather than an interface default.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — arXiv:2505.09166, v6 revised 25 January 2026.

PASSAGE:
[PARAPHRASE]
Text-to-image systems are designed to return an image even when a prompt contains unknown terms. Simonen et al. call one resulting failure mode “default images”: visually similar images appearing across otherwise unrelated prompts. Their expanded study analyzes more than 750,000 Midjourney images.

RESEARCH OBJECT:
“Default” splits into at least two different mechanisms: a setting selected before interaction and a recurrent output produced when textual conditioning provides insufficient discriminating information.

LOCAL MOVE:
The source operationalizes a phenomenon that [[Z-AIACS-004]] treated more broadly as a hidden prior. It shows that recognizable defaults can be detected in outputs without first locating an explicit UI setting.

SOURCE TERMS:
“default images”
“unknown terms”
“unrelated prompts”
“text-to-image generation”
“user satisfaction”

WHAT BECAME STRANGE:
A model does not need a blank prompt to expose its defaults. A sufficiently unrecognized or weakly discriminating prompt can act like a probe that reveals what the system does when language stops steering it.

QUESTION:
What exactly is being exposed by a default image: training-data frequency, model architecture, alignment, aesthetic tuning, prompt preprocessing, or some interaction among them?

DEEPER QUESTION:
Could deliberately bad prompts be a better instrument for studying a generative model than carefully optimized prompts?

MECHANISM:
poorly discriminating / unknown textual input
→ insufficient prompt-specific guidance
→ generation still must proceed
→ recurrent visual attractor
→ similar images across unrelated prompts

FORMAL SHIFT:
<weakly recognized prompt>
→ <conditioning signal>
→ [GENERATE DESPITE LOW SEMANTIC SPECIFICITY]
→ <default-like output cluster>

SOURCE FORMALISM:
The study searches for consistent visual similarity across outputs associated with unrelated prompts and expands the investigation computationally to more than 750,000 Midjourney images.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DEFAULT_STRENGTH(p, m)
≈ similarity(
    G_m(p),
    outputs generated from semantically unrelated prompts
  )

The key comparison is not blank prompt versus filled prompt.
It is semantic difference in input versus visual difference in output.

TENSION:
[[Z-AIACS-004]] treated defaults primarily as pre-prompt platform configuration. Simonen et al. reveal a different class of default that emerges through the model’s response to weak or unknown conditioning. Both may exist, but they should not share one causal label.

MISSING:
A decomposition of default images across model weights, model versions, prompt preprocessing, system-level instructions, sampler configuration, and interface behavior.

BOUNDARY:
The study establishes recurrent default images in Midjourney. It does not establish which internal component is causally responsible for each default.

CITATION TRAIL:
[[Z-AIACS-004]]
→ Simonen et al., “An Exploration of Default Images in Text-to-Image Generation”
→ default as observable fallback behavior rather than merely preset configuration
→ locate the layer that produces the fallback

TEST:
Construct semantically unrelated nonsense, rare-word, vague, and ordinary prompts. Run the identical prompt set through multiple model versions and, where possible, multiple interfaces to the same underlying model. If default clusters follow the model version rather than the interface, the causal locus moves downward in the stack.

PLATFORM:
[[Default Images]]

LINKS:
[[Z-AIACS-004]]
[[Model Priors]]
[[Semantic Failure]]
[[Generative Attractors]]

BIBTEX:
@misc{SimonenEtAl2025DefaultImages,
  author = {Hannu Simonen and Atte Kiviniemi and Hannah Johnston and Helena Barranha and Jonas Oppenlaender},
  title = {An Exploration of Default Images in Text-to-Image Generation},
  year = {2025},
  eprint = {2505.09166},
  archivePrefix = {arXiv},
  primaryClass = {cs.HC},
  doi = {10.48550/arXiv.2505.09166}
}
