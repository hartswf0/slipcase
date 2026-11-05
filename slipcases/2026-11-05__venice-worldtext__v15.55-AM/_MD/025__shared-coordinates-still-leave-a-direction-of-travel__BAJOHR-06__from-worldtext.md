ZETTEL

ID: BAJOHR-06
TITLE: Shared coordinates still leave a direction of travel
SOURCE: Hannes Bajohr — “Operative Ekphrasis,” 2024, and Venice talk, 2025. Checked against Ramesh et al., “Hierarchical Text-Conditional Image Generation with CLIP Latents,” 2022.

PASSAGE: [QUOTE — supplied transcript] “language produces images.”
[PARAPHRASE] Bajohr distinguishes the prompt’s production of an image from the claim that shared latent representation destabilizes the identity of the two media.

RESEARCH OBJECT: The modality-specific operations that remain after text and image representations have been aligned.
LOCAL MOVE: Bajohr uses text-to-image generation to turn ekphrasis into an operation and then draws a stronger claim about what counts as text or image inside the system.
SOURCE TERMS: Operative ekphrasis, shared latent space, text caption, image embedding, prior, decoder.
WHAT BECAME STRANGE: In DALL·E 2, the shared CLIP space coexists with an explicitly directional generation pipeline. The prior predicts an image embedding conditioned on text, and the decoder produces pixels.
QUESTION: At which interface does the distinction between text and image weaken, and at which does the system require it?
MECHANISM: Alignment makes representations comparable. The prior maps caption information into a predicted image embedding. The decoder turns that embedding into a visual sample.
FORMAL SHIFT: <caption> → <text conditioning> → [predict image embedding and decode] → <image>.
SOURCE FORMALISM: Ramesh et al. specify the two-stage prior and decoder. The lecture supplies the aesthetic interpretation.
OUR FORMALIZATION: NONE.
TENSION: A. The collapse is local to an aligned representation. B. It extends to the operative substitutability of the two modalities.
MISSING: A substitution test at a specified architectural interface.
BOUNDARY: DALL·E 2 supplies one architectural case. The comparison leaves other multimodal architectures open.
CITATION TRAIL: Bajohr, Word & Image 40(2), doi:10.1080/02666286.2024.2330335. Then Ramesh et al., especially the separation of prior and decoder.
TEST: Inspect what the decoder accepts from the text and image encoders. Try substituting a caption embedding for an image embedding at that interface without an adapter. Separate input compatibility from preservation of the intended visual content.
PLATFORM: [[What travels between media]]
LINKS: [[BAJOHR-05]]

BIBTEX:
@misc{ramesh2022clip,
  author = {Ramesh, Aditya and Dhariwal, Prafulla and Nichol, Alex and Chu, Casey and Chen, Mark},
  title = {Hierarchical Text-Conditional Image Generation with {CLIP} Latents},
  year = {2022},
  eprint = {2204.06125},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2204.06125}
}
