ZETTEL

ID:
DEFAULT-IMAGES-CHI26-F-1

TITLE:
A single Unicode character can behave like a culture vector even when it appears inside a semantically irrelevant word.

SOURCE:
Lukas Struppek, Dominik Hintersdorf, Felix Friedrich, Manuel Brack, Patrick Schramowski, and Kristian Kersting — “Exploiting Cultural Biases via Homoglyphs in Text-to-Image Synthesis” — Journal of Artificial Intelligence Research 78 — 2023 — https://arxiv.org/abs/2209.08891

PASSAGE:
[PARAPHRASE] Struppek et al. replace single Latin characters with visually similar characters from non-Latin scripts inside otherwise ordinary prompts. These tiny changes can shift generated architecture, food, environments, and depictions of people toward visual characteristics statistically associated with the substituted script. Their experiments identify the text encoder as the primary mechanism. They further construct embedding-space directions from the difference between Latin and non-Latin character embeddings and show that adding such directions to ordinary prompt embeddings can reproduce similar cultural shifts without changing the visible prompt.

RESEARCH OBJECT:
Low-resource language behavior is not only about missing words.

A text-to-image model may assign powerful visual consequences below the level of the word.

A single character can carry a learned cultural direction strong enough to reorganize an image.

LOCAL MOVE:
Move from:

LANGUAGE COVERAGE
→ whether the model recognizes a word

to:

SCRIPT GEOMETRY
→ how individual characters move the prompt representation through learned cultural space.

SOURCE TERMS:
homoglyphs
non-Latin characters
text encoder
cultural biases
embedding space
cultural directions
Unicode scripts

WHAT BECAME STRANGE:
A character placed in an article or preposition—a character with essentially no intended cultural proposition—can alter clothing, architecture, faces, colors, or scenery.

The smallest visible unit of writing can exert more visual control than the sentence says it should have.

QUESTION:
Do low-resource-language default images arise only from weak semantic coverage, or can script-level embedding directions actively push weak prompts toward particular fallback motifs?

DEEPER QUESTION:
When the intended semantics of a prompt are weak, does orthography itself become an unintended control language for the generator?

MECHANISM:
The source locates the effect primarily in the text encoder.

Characters from different scripts occupy distinguishable regions of embedding space.

The authors compute embedding differences between Latin and non-Latin characters and use those differences as directions that can shift an ordinary text embedding toward outputs displaying corresponding learned cultural associations.

FORMAL SHIFT:
FROM:

CHARACTER
→ part of WORD
→ lexical meaning

TO:

CHARACTER
→ EMBEDDING DISPLACEMENT
→ visual-cultural conditioning

even when lexical meaning is effectively unchanged.

SOURCE FORMALISM:
The source defines encoder-based embedding manipulations and computes directions from the difference between representations associated with Latin and non-Latin characters.

Those directions are added to normal prompt embeddings to test whether the image generator reproduces the cultural shift observed with actual homoglyph substitutions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

E(p) = text embedding of prompt p

and let h replace one Latin character with a homoglyph.

Define:

v_h = E(p ⊕ h) - E(p).

The source's result motivates treating v_h as a learned script-associated direction.

Then:

G(E(p) + v_h)
≠
G(E(p))

even when:

human_semantics(p ⊕ h)
≈
human_semantics(p).

For weak prompt semantics:

||semantic_control(p)|| ↓

the relative influence of:

||v_h||

may become disproportionately large.

TENSION:
The authors use terms such as cultural bias and cultural direction, but the mappings are model-dependent.

The same character can acquire different associations in different systems because training histories differ.

A Unicode character therefore does not possess one inherent culture.

The model has learned a statistical association between script and visual patterns.

MISSING:
The interaction between character-level directions and default-image attractors.

Specifically:

Does adding one script character to a prompt known to trigger Lady-Birdhead or another recurrent default suppress that default, select another default, or culturally transform the same motif?

BOUNDARY:
The demonstrated mechanism concerns DALL-E 2, Stable Diffusion, and related encoder architectures investigated by the authors.

It is not direct evidence about Midjourney's hidden text encoder.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-F]]
→ low-resource terms produce default substitutions
→ Struppek et al. character-level cultural steering
→ linguistic failure splits into ABSENCE and ORTHOGRAPHIC FORCE
→ default imagery may depend on what weak text fails to say AND what its script accidentally says.

TEST:
Take a fixed set of default-triggering nonce and low-resource prompts.

Create minimally different variants by replacing one visually similar character with homoglyphs from several scripts.

Fix model parameters and seeds.

Measure:

default-motif identity
default frequency
CLIP/image embedding shift
human-rated cultural attributes.

Then reproduce each observed effect by directly adding the corresponding character-derived embedding direction in an open model.

If the same motif shift can be produced without changing the visible text, the operative mechanism is embedding geometry rather than lexical interpretation.

PLATFORM:
DALL-E 2; Stable Diffusion; CLIP-based text encoders.

LINKS:
[[DEFAULT-IMAGES-CHI26-F]]

BIBTEX:
@article{Struppek2023Homoglyphs,
  author = {Struppek, Lukas and Hintersdorf, Dominik and Friedrich, Felix and Brack, Manuel and Schramowski, Patrick and Kersting, Kristian},
  title = {Exploiting Cultural Biases via Homoglyphs in Text-to-Image Synthesis},
  journal = {Journal of Artificial Intelligence Research},
  volume = {78},
  pages = {1017--1068},
  year = {2023},
  url = {https://arxiv.org/abs/2209.08891}
}
