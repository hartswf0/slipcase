ZETTEL

ID: FORAGE-ZP-002

TITLE: Bajohr's operative ekphrasis: the text/image collapse is computational, not metaphorical

SOURCE: Z-Port/final-draft-v4.md ("Operative Ekphrasis and the Imagetext"); Z-Port/portugal-version.md ("Operative ekphrasis and the Imagetext"); Z-Port/final-draft-v2.md §1; Z-Port/deep-research-report (14).md (Thesis bin)

PASSAGE: [QUOTE] "Hannes Bajohr was among the first literary theorists to note that the prompting of an AI image generated constituted a new form of ekphrasis. (Bajohr 2024; see also Meyer 2023) Bajohr coined the term 'operative ekphrasis' to describe the unique capacity that gen AI systems bring to the practice." (final-draft-v4.md) [QUOTE] "As Bajohr emphasizes, the process of creating these models collapses in important ways the distinction between text and image, and it is this collapse that makes operative ekphrasis possible." (final-draft-v4.md) [QUOTE] "In the multidimensional latent space of a diffusion model, words and images are mapped into the same mathematical vectors." (final-draft-v2.md §1) [PARAPHRASE] The deep-research-report stresses that Bajohr's abstract claims multimodal AI forces ekphrastic relations to be understood as performative rather than representational, because the text/image distinction collapses operationally inside the model.

RESEARCH OBJECT: Bajohr's concept "operative ekphrasis" (Word & Image 40(2), 2024) as the paper's hinge: the moment textual description becomes computationally executable. The mechanism cited is training: captions and images are encoded into one weight set, so after training "it is impossible to say which particular values constitute the text and which the images; the representations of text and images are everywhere in the latent manifold" (v4).

LOCAL MOVE: Import a single recent concept from German media theory and make it the pivot between the classical rhetoric genealogy (Webb) and the machine-learning genealogy (Ha & Schmidhuber), so the paper's novelty claim ("worldtext") can present itself as the *next* step after Bajohr rather than a competitor to him.

SOURCE TERMS: operative ekphrasis; collapse of the text/image distinction; latent space; latent manifold; performative vs representational; executable description

WHAT BECAME STRANGE: Description, the paradigmatically secondary act (after the object), becomes causally primary (before the object). The caption — training metadata — turns out to be the load-bearing interface of the whole generative stack.

QUESTION: Does "collapse" accurately describe joint embedding — or do text and image remain operationally distinguishable (separate encoders, cross-attention) so that the collapse is a property of Bajohr's rhetoric rather than the architecture?

DEEPER QUESTION: If the collapse is real, is ekphrasis still the right ancestral category — or has the word/image *relation* (rivalry, translation, desire) that defined ekphrasis simply ceased to exist, leaving nothing for "ekphrasis" to name?

MECHANISM: Tokenization of both captions and images into a single weighted-matrix system during training; diffusion at inference "repeatedly refines the image out of an initial pattern of noise" — probabilistic in outcome, deterministic in procedure (v4).

FORMAL SHIFT: Ekphrasis moves from a semiotic relation between two sign systems to an operation within one vector space; the semiotic gap becomes a geometric distance.

SOURCE FORMALISM: Bajohr's operative/representational distinction; v4's characterization of the latent space as literally imagetext ("Imagetext as both image and text is an appropriate description of the latent space of an image generation model").

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Traditional ekphrasis: text T refers to image I, relation R(T,I) interpretive. Operative ekphrasis: generation function G with shared embedding E, I = G(E(T)); R is replaced by execution. Worldtext extends: W = G'(E(T), S, P) where S = system-prompt stack, P = procedural rules.

TENSION: READING A: operative ekphrasis is radically new — a rupture in the history of the sign (v2's "literal, computational execution"). READING B (v4): it is "both familiar and radically new," continuous with the rhetorical tradition, and the computer scientists produced it accidentally — the interface "happened to enact this literary practice." Novelty vs. uncanny recurrence.

MISSING: No draft engages Bajohr's own arguments in detail beyond the abstract-level claim; the actual article's internal distinctions (e.g., how Bajohr treats earlier digital image manipulation) are summarized in one sentence in v4 and absent elsewhere.

BOUNDARY: Applies to multimodal generative models trained on captioned images; the drafts explicitly exclude "traditional computer manipulation of images" (v4) from operative ekphrasis.

CITATION TRAIL: Bajohr 2024, Word & Image 40(2):77–90, doi:10.1080/02666286.2024.2330335 → Meyer 2023 → Mitchell 1994 → Liu & Chilton 2023 (prompting as probing latent space) → Almeda et al. 2024.

TEST: Check whether text and image embeddings in a production diffusion model are actually inseparable in the weights (vs. architecturally separated encoders); if separable, the "collapse" claim needs restating as alignment rather than fusion.

PLATFORM: Text-to-image diffusion systems (DALL-E, Midjourney, Stable Diffusion, Gemini image generation) as discussed in the drafts.

LINKS: [[FORAGE-ZP-001]], [[FORAGE-ZP-005]], [[FORAGE-ZP-003]], [[FORAGE-ZP-010]]

BIBTEX: @article{bajohr2024operative, author = {Bajohr, Hannes}, title = {Operative Ekphrasis: The Collapse of the Text/Image Distinction in Multimodal AI}, journal = {Word \& Image}, volume = {40}, number = {2}, pages = {77--90}, year = {2024}, doi = {10.1080/02666286.2024.2330335}}
