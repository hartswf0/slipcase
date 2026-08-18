ZETTEL

ID:
DEFAULT-IMAGES-CHI26-C-1

TITLE:
The random seed is not empty: blocks of Gaussian noise already have preferences for what they will become.

SOURCE:
Jiafeng Mao, Xueting Wang, and Kiyoharu Aizawa — “Guided Image Synthesis via Initial Image Editing in Diffusion Model” — 2023 — https://arxiv.org/abs/2305.03382

PASSAGE:
[PARAPHRASE] Mao et al. experimentally manipulate the initial latent noise of Stable Diffusion and find that local blocks of the initial noise exhibit preferences for generating particular kinds of content. Altering a local block changes the corresponding region of the final image while often preserving other regions. They further report that these generation preferences depend more strongly on the values contained in a block than on the block’s original position.

RESEARCH OBJECT:
The seed is not merely the dice roll that selects among otherwise equivalent images.

The initial noise contains structure that interacts with the model so predictably that pieces of it can be moved and edited to steer what appears later.

The “random” beginning of generation therefore already contains unequal futures.

LOCAL MOVE:
Replace:

SEED = source of arbitrary variation

with:

SEED = structured initial condition with differential generative affordances.

SOURCE TERMS:
initial noise
initial latent image
content preference
pixel blocks
guided image synthesis
Stable Diffusion
layout-to-image

WHAT BECAME STRANGE:
Before the prompt has finished becoming an image, different pieces of supposedly meaningless noise are already better candidates for becoming different things.

Randomness is not neutral with respect to the learned generator.

The seed may be a proto-image without looking anything like an image.

QUESTION:
Are the recurring motifs called “default images” partly selected by latent regions of the initial noise that are unusually compatible with those motifs?

DEEPER QUESTION:
When linguistic conditioning becomes weak, does generation reveal a hidden visual disposition already latent in the starting noise-model pair?

MECHANISM:
The source demonstrates that changing local values in initial latent noise can predictably alter corresponding generated content.

The operative object is therefore not noise alone but:

INITIAL NOISE
×
TRAINED DENOISER.

Certain noise configurations interact with the learned model in ways that make some outcomes easier to realize than others.

FORMAL SHIFT:
FROM:

PROMPT determines semantics
+
SEED supplies stochastic variation

TO:

PROMPT supplies semantic pressure
+
SEED supplies structured generative predispositions
+
DENOISING resolves their interaction.

SOURCE FORMALISM:
The authors manipulate blocks within the initial latent and evaluate how those interventions alter corresponding output regions.

Their experiments treat the initial latent itself as an actionable control surface for generation rather than an immutable random starting point.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

z₀ = initial Gaussian latent
p = prompt
G = trained diffusion generator.

Ordinary framing:

I = G(z₀,p)

with z₀ treated as semantically neutral randomness.

Alternative:

z₀ contains local generation affordances:

A(z₀,r,c)

= propensity for region r of z₀, under G, to develop toward content c.

Then:

weak semantic guidance from p
→ greater relative influence of A(z₀,r,c).

Default imagery may therefore be jointly selected by:

MODEL PRIOR
×
NOISE AFFORDANCE
×
WEAK PROMPT CONTROL.

TENSION:
Calling the initial noise “semantic” would overstate the source.

The experiments demonstrate content preferences conditional on a trained generator.

They do not show that Gaussian values intrinsically contain birds, buildings, faces, or other concepts independently of the model.

The content is relational:

NOISE × MODEL,

not simply hidden inside the noise.

MISSING:
Whether the same latent block retains a content preference across:

different prompts
different seeds around a local neighborhood
different model checkpoints
different diffusion architectures.

Also missing is whether default-image motifs correspond disproportionately to especially large basins of compatible initial noise.

BOUNDARY:
The source studies Stable Diffusion and controlled latent manipulation.

It does not demonstrate that Midjourney uses equivalent initial latents or that its default images originate in seed structure.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-C]]
→ seed changes which default motif appears
→ initial-noise manipulation literature
→ noise blocks exhibit content preferences
→ “random variation” becomes structured initial condition
→ next edge: map default motifs backward into initial-noise regions.

TEST:
For an open diffusion model, first discover prompts that produce default-like recurrent motifs.

Then sample a large seed set.

Label resulting motif class for each seed.

For seeds strongly associated with one motif:

swap local latent blocks into seeds associated with another motif.

If motif probability moves with transferred blocks, identify which initial-noise regions exert causal control.

Then repeat with progressively stronger known prompt concepts.

Prediction:

the stronger the semantic prompt constraint,
the less visible the latent block’s prior preference should become.

PLATFORM:
Stable Diffusion; initial-latent intervention.

LINKS:
[[DEFAULT-IMAGES-CHI26-C]]

BIBTEX:
@article{Mao2023InitialImageEditing,
  author = {Mao, Jiafeng and Wang, Xueting and Aizawa, Kiyoharu},
  title = {Guided Image Synthesis via Initial Image Editing in Diffusion Model},
  journal = {arXiv preprint arXiv:2305.03382},
  year = {2023},
  url = {https://arxiv.org/abs/2305.03382}
}
