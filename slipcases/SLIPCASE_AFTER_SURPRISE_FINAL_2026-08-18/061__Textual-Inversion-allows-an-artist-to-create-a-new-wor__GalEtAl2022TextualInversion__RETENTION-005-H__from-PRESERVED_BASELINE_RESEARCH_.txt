ZETTEL

ID:
RETENTION-005-H

TITLE:
Textual Inversion allows an artist to create a new “word” whose meaning is a learned visual concept.

SOURCE:
Rinon Gal et al. — “An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion” — 2022.

PASSAGE:
[PARAPHRASE]
From a few user-provided images, Textual Inversion learns a new embedding-space token representing a concept; that token can then be composed into ordinary prompts.

RESEARCH OBJECT:
PROMPTING CAN INCLUDE AUTHORING THE VOCABULARY OF THE PROMPT.

LOCAL MOVE:
The artist can intervene in the model-language relation itself by manufacturing a new operative sign.

SOURCE TERMS:
new words
embedding space
user-provided concept
frozen model
personalization
composition

WHAT BECAME STRANGE:
The visible token may have almost no ordinary linguistic meaning. Its operative content lives in a learned vector produced from selected examples.

QUESTION:
Where is the creative intervention located: in the source images, their selection, the learned embedding, the token name, the surrounding sentence, or the generated output?

DEEPER QUESTION:
Can an embedding function as a private artistic vocabulary—a sign whose semantics consists principally in how a machine responds to it?

MECHANISM:
select example images X → optimize embedding v* → bind token τ* → compose τ* in prompt → frozen generator interprets v* → new outputs.

FORMAL SHIFT:
<USE EXISTING LANGUAGE> → [LEARN NEW SIGN] → <EXTEND OPERATIVE VOCABULARY> → [COMPOSE] → <GENERATION>

SOURCE FORMALISM:
The method learns a token embedding for a user-provided concept while keeping the underlying text-to-image model frozen.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Ordinary: τ_i → fixed E(τ_i). Textual inversion: X → optimize v* → bind τ*↦v* → use τ* compositionally.

TENSION:
The learned vector is heavily determined by the optimization algorithm and pretrained model geometry.

MISSING:
Legal analysis of user-trained prompt tokens or embeddings as authorship contributions.

BOUNDARY:
“Prompt” ceases to mean ordinary natural-language expression once its vocabulary can contain learned model-specific artifacts.

CITATION TRAIL:
[[RETENTION-005]] → prompt as artistic intervention → Textual Inversion → user creates operative word → prompt craft expands into model-language design.

TEST:
Create two embeddings from different curated image sets for the same named concept. Use identical surrounding text and measure stable output differences attributable to example selection.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[textual-inversion]]
[[operative-vocabulary]]
[[prompt-language]]
[[learned-sign]]

BIBTEX:
@article{GalEtAl2022TextualInversion, author={Gal, Rinon and others}, title={An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion}, journal={arXiv preprint arXiv:2208.01618}, year={2022}}
