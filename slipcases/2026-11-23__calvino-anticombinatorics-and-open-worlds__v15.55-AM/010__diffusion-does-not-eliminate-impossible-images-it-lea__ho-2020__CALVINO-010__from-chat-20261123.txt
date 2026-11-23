ZETTEL

ID: CALVINO-010

TITLE:
Diffusion does not eliminate impossible images; it learns how to transform noisy states.

SOURCE:
Jonathan Ho, Ajay Jain, and Pieter Abbeel — "Denoising Diffusion Probabilistic Models" — 2020, sections 2–3, Algorithms 1–2.

PASSAGE:
[PARAPHRASE]
The model is trained using a forward noising process and learns parameters for a reverse generative process. Sampling begins from a Gaussian noise state and proceeds through learned transitions toward a final image.

RESEARCH OBJECT:
The difference between rejection over symbolic candidates and learned reverse dynamics over continuous representations.

LOCAL MOVE:
Ho and colleagues specify a probabilistic generative procedure with a training objective and a reverse sampling algorithm.

SOURCE TERMS:
"forward process"; "reverse process";
"variational bound"; "denoising score matching";
"sampling."

WHAT BECAME STRANGE:
A noisy image is not literally an archive of fully formed candidate images awaiting elimination.

QUESTION:
What exactly is being reduced during diffusion sampling: uncertainty, entropy, noise, admissible possibilities, or distance from a learned distribution?

DEEPER QUESTION:
If an image model progressively produces visual detail without reasoning over explicit spatial objects, what warrants treating its result as an inferred narrative world?

MECHANISM:
The model estimates a reverse transition distribution from noisy examples. Sampling applies these learned transitions, often incorporating additional randomness.

FORMAL SHIFT:
Training images
→ progressively noised training states
→ [learn reverse transitions]
→ generative sampling from noise.

SOURCE FORMALISM:
Forward process q.
Learned reverse process p_theta.
Initial sampling state x_T ~ N(0,I).
Repeated transitions toward x_0.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Calvino-style search:
Candidates → exclusions → surviving candidates.

Diffusion:
Noise state → learned transition → next state.

The second process is not a sequence of logical rejections of complete hypothetical images.

TENSION:
Diffusion can produce a visually coherent scene without representing its causal history, object permanence, or consistency with other scenes.

MISSING:
An explicit representation of shared fictional locations, object identity, viewpoint, temporal continuity, and narrative event relations.

BOUNDARY:
This analysis concerns the DDPM mechanism. It does not describe every image-generation architecture or establish that learned models cannot be combined with explicit constraints.

CITATION TRAIL:
Ho, Jain, and Abbeel (2020).
Ho and Salimans, "Classifier-Free Diffusion Guidance" (2022).
Research on scene graphs, multiview generation, and world consistency.

TEST:
Generate multiple views of a purportedly shared place. Check spatial and semantic consistency independently of visual realism. Then introduce explicit world-state constraints and compare the results.

PLATFORM:
[[Generative Models Versus Narrative Reconstruction]]

LINKS:
[[CALVINO-003]]
[[CALVINO-009]]
[[CALVINO-016]]

BIBTEX:
@inproceedings{ho2020denoising,
  author    = {Ho, Jonathan and Jain, Ajay and Abbeel, Pieter},
  title     = {Denoising Diffusion Probabilistic Models},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2020},
  eprint    = {2006.11239},
  archivePrefix = {arXiv},
  url       = {https://arxiv.org/abs/2006.11239}
}
