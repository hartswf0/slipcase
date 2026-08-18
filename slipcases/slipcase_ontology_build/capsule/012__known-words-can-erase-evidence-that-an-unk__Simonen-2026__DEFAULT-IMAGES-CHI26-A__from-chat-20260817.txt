ZETTEL

ID:
DEFAULT-IMAGES-CHI26-A

TITLE:
Known words can erase evidence that an unknown word was never understood.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] In an ablation study, short prompts containing unknown terms produced recognizable default images. When the same unknown terms were placed inside longer prompts containing words Midjourney recognized, the system generated imagery from the recognized words and the outputs ceased resembling the canonical defaults. fileciteturn1file8L525-L532

[PARAPHRASE] Elsewhere the authors describe known concepts as acting like “magnets” that overshadow unknown concepts and move generation toward imagery associated with what the model recognizes. fileciteturn1file9L577-L586

RESEARCH OBJECT:
An unknown token does not necessarily cause visible failure.

Surrounding recognized terms can provide enough semantic guidance for generation to look successful while the unknown portion of the request contributes little or nothing identifiable to the output.

Default images may therefore expose only one extreme of a larger phenomenon:

SILENT PARTIAL INTERPRETATION.

LOCAL MOVE:
Move from asking:

“Did the model understand the prompt?”

to:

“Which parts of the prompt acquired causal control over the image?”

SOURCE TERMS:
known concepts
unknown terms
larger prompts
prompt specificity
default images
semantic guidance
magnets

WHAT BECAME STRANGE:
Adding more descriptive information can make a generator appear more competent while making failure harder to see.

A rich prompt may conceal ignorance better than a sparse prompt.

QUESTION:
Does prompt composition behave less like satisfying a set of requested constraints and more like competition among semantic signals of unequal strength?

DEEPER QUESTION:
Can a prompt contain ten apparently meaningful instructions while only two or three actually control generation?

MECHANISM:
Recognized terms provide strong visual conditioning.

When semantic guidance from recognized terms is strong enough, the generator can produce a coherent image without visibly resolving unknown terms.

The unknown component is therefore masked by successful rendering of its neighbors.

FORMAL SHIFT:
FROM:

PROMPT
= collection of jointly executed descriptions

TO:

PROMPT
= field of unequally effective conditioning signals.

SOURCE FORMALISM:
The source does not provide an equation for semantic dominance.

Its evidence comes from an ablation:

unknown-triggering short prompt
→ default image

same unknown material + recognized terms in larger prompt
→ imagery associated with recognized terms rather than the default motif. fileciteturn1file8L525-L532

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Prompt:

p = {t₁, t₂, ... tₙ}

Assign each term an effective visual control strength:

c(tᵢ).

Naive compositional model:

IMAGE ≈ satisfy(t₁ ∧ t₂ ∧ ... ∧ tₙ)

Alternative competitive model:

IMAGE ≈ G(argmax / weighted interaction of c(tᵢ)).

An unknown term may have:

c(t_unknown) ≈ 0

while recognized neighbors have:

c(t_known) >> 0.

The image can therefore look strongly prompt-conditioned even though one requested concept has disappeared computationally.

TENSION:
One reading is simple lexical dominance: recognized words overpower an unknown word.

Another is that Midjourney may preprocess or rewrite the entire prompt, making apparent token-level competition an artifact of an unseen intermediary.

The current evidence does not distinguish these mechanisms.

MISSING:
Token-level or phrase-level causal intervention.

The study does not show precisely which prompt segments altered which image features, nor whether Midjourney rewrote the prompts internally.

BOUNDARY:
The finding comes from limited Midjourney ablations and should not yet be generalized into a universal law of prompt composition.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ Section 5.2.3
→ known concepts suppress visible default behavior
→ semantic failure can survive inside apparently successful generation
→ question of token-level causal control.

TEST:
Construct minimal prompt pairs while fixing seed and all generation parameters.

For each unknown term U and recognized term K, compare:

U
K
U + K
K + U
U inside a syntactic modifier of K
K inside a syntactic modifier of U.

Then causally remove each term and measure changes in generated objects and image embeddings.

A term counts as operationally interpreted only if its removal produces a reproducible, concept-specific change.

PLATFORM:
Midjourney v6-series ablation study.

LINKS:
[[DEFAULT-IMAGES-CHI26-ROOT]]

BIBTEX:
@inproceedings{Simonen2026DefaultImages,
  author = {Simonen, Hannu and Kiviniemi, Atte and Johnston, Hannah and Barranha, Helena and Oppenlaender, Jonas},
  title = {An Exploration of Default Images in Text-to-Image Generation},
  booktitle = {Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems},
  year = {2026},
  doi = {10.1145/3772318.3790681},
  url = {https://doi.org/10.1145/3772318.3790681}
}
