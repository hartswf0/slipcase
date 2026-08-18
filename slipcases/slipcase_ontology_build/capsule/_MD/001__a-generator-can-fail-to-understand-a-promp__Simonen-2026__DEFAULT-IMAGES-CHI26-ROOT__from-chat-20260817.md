ZETTEL

ID:
DEFAULT-IMAGES-CHI26-ROOT

TITLE:
A generator can fail to understand a prompt without failing to generate: semantic failure can appear as a polished image.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] The authors define “default images” as visually similar images produced from different and unrelated prompts when a text-to-image system does not recognize or cannot strongly visualize its input. The system still returns an image, so failure appears as a plausible visual artifact rather than an explicit error. fileciteturn1file1L90-L109

[PARAPHRASE] Their large-scale study analyzes 189,432 prompts and 757,728 images and finds default-image behavior in real Midjourney usage, not merely in prompts deliberately constructed by the researchers. fileciteturn1file1L77-L89

RESEARCH OBJECT:
The research object is not merely “bad prompt adherence.” It is a specific class of silent execution failure:

the system accepts an input
→ cannot strongly ground some of it
→ nevertheless must produce an output
→ falls into recurrent visual configurations
→ returns those configurations as if generation had succeeded.

The visible image therefore conceals an important distinction between successful execution and successful interpretation.

LOCAL MOVE:
Split GENERATION SUCCESS from SEMANTIC SUCCESS.

A text-to-image interface can report success at the level of computation while failing at the level of reference.

SOURCE TERMS:
default images
unknown inputs
unrecognized prompts
latent space
generic visual patterns
known concepts
stochastic sampling
model vocabulary
prompt engineering

WHAT BECAME STRANGE:
The absence of understanding does not produce absence.

It produces imagery.

The system’s “I do not know” may therefore have a positive visual form: women, birds, vegetation, floating objects, surreal landscapes, or other recurrent motifs.

QUESTION:
What kind of computational object is a default image: a fallback, an attractor, a memorized region, an interface artifact, or merely an empirical pattern that does not yet warrant any of those causal interpretations?

DEEPER QUESTION:
What other generative systems convert semantic uncertainty into plausible positive output instead of exposing uncertainty as an error state?

MECHANISM:
[PARAPHRASE] The paper proposes that weak or unknown semantic guidance leaves generation more dependent on learned generic or frequent visual patterns, while stochastic sampling determines which particular recurring motif appears. fileciteturn1file9L561-L575

FORMAL SHIFT:
FROM:

unknown input
→ generation failure

TO:

unknown input
→ successful execution
→ recurrent fallback-like output
→ hidden semantic failure.

SOURCE FORMALISM:
The paper operationally identifies a default image through the conjunction of:

visually similar outputs
+
dissimilar input prompts.

Its large-scale method first clusters images by visual similarity and then removes clusters whose prompts are too lexically or semantically similar. fileciteturn0file0L590-L647

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

G(p, s, m) → i

where:
p = prompt
s = sampling state / seed
m = model or model version
i = generated image

Ordinary semantic convergence:

similar(p₁,p₂) high
→ similar(G(p₁),G(p₂)) high

Default-image candidate:

similar(p₁,p₂) low
AND
similar(G(p₁),G(p₂)) high.

The anomaly is therefore not simply image repetition.

It is:

LINGUISTIC DIVERGENCE
+
VISUAL CONVERGENCE.

TENSION:
The paper sometimes explains the phenomenon in terms of latent-space structure and training-data gaps, but later acknowledges that Midjourney is a proprietary pipeline whose prompt rewriting or other platform mechanisms are not observable.

The empirical phenomenon is stronger than the proposed causal explanation.

MISSING:
A causal decomposition separating:

training-data coverage
text encoding
prompt rewriting
cross-attention or equivalent conditioning
sampling
model priors
platform-level processing.

BOUNDARY:
The empirical study concerns Midjourney and does not establish that identical mechanisms generate superficially similar behavior in Stable Diffusion, Flux, Imagen, Janus, video generators, or other architectures.

CITATION TRAIL:
Simonen et al. 2026
→ definition of default images
→ ablation studies
→ large-scale visual-convergence / prompt-divergence detection
→ causal-opacity limitation
→ unresolved question: where in the generation pipeline does semantic failure become a recurrent positive image?

TEST:
Hold prompts, model version, and sampling conditions under experimental control in an inspectable open-weight model.

Create graded semantic perturbations from well-represented term → rare term → low-resource-language term → corrupted term → random token.

Measure where visual outputs cease following the requested concept and begin converging across unrelated prompts.

Then inspect text embeddings, cross-attention/conditioning signals, and denoising trajectories to determine where convergence first appears.

PLATFORM:
Midjourney; CHI 2026 empirical study.

LINKS:
NONE

BIBTEX:
@inproceedings{Simonen2026DefaultImages,
  author = {Simonen, Hannu and Kiviniemi, Atte and Johnston, Hannah and Barranha, Helena and Oppenlaender, Jonas},
  title = {An Exploration of Default Images in Text-to-Image Generation},
  booktitle = {Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems},
  year = {2026},
  doi = {10.1145/3772318.3790681},
  url = {https://doi.org/10.1145/3772318.3790681}
}
