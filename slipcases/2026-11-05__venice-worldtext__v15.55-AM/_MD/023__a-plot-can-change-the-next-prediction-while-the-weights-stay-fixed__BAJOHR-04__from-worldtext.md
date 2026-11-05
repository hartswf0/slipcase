ZETTEL

ID: BAJOHR-04
TITLE: A plot can change the next prediction while the weights stay fixed
SOURCE: Hannes Bajohr — “The Latent Space of Meaning and the Novel,” Venice, 2025, discussion of the “frozen world state.”

PASSAGE: [QUOTE — supplied transcript] “no plot can leave a mark in the latent space once training is complete.”
[PARAPHRASE] Earlier in the talk, Bajohr describes token representations as dynamically computed in context.

RESEARCH OBJECT: The difference between a parameter update and a plot event continuing to constrain generation.
LOCAL MOVE: The talk uses the fixity of the trained system to explain why narrative change may be hard to sustain.
SOURCE TERMS: Frozen world state, contextual embeddings, trajectory.
WHAT BECAME STRANGE: The talk gives context the power to change what a token means, then makes the absence of permanent change do explanatory work about plot.
QUESTION: What has to persist for a fictional event to count as a change of world state?
MECHANISM: A generated or supplied event changes the available prefix. That prefix can change later predictions under the same trained parameters. Truncation, resetting the prefix, or failing to use the information can break the dependency.
FORMAL SHIFT: <event in prefix> → <context-conditioned representation> → [compute continuation] → <changed downstream possibilities>.
SOURCE FORMALISM: The talk describes next prediction and contextual representations. It supplies no run-level state trace.
OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Hold weights fixed. Change one prior event and measure how long its consequences alter later predictions.
TENSION: A. Coherence fails because the workflow loses access to a prior event. B. The event stays available, but the model fails to apply its consequences.
MISSING: The actual context retention and reset policy used for (Berlin, Miami).
BOUNDARY: A successful short-context intervention would establish a way for plot to affect generation. It would leave novel-length persistence open.
CITATION TRAIL: Bajohr’s production note in Ensemble Park. Compare Kenneth Li and colleagues’ “Emergent World Representations” for an intervention in a bounded game domain.
TEST: Run the same later scene after two prefixes in which a named character either survives or dies. Repeat with the decisive sentence in view, truncated, and restored through a neutral summary.
PLATFORM: [[Where fictional state lives]]
LINKS: [[BAJOHR-01]] [[BAJOHR-07]]

BIBTEX:
@misc{bajohr2025latent,
  author = {Bajohr, Hannes},
  title = {The Latent Space of Meaning and the Novel: World Models in {AI} and Literature},
  year = {2025},
  howpublished = {Talk at Chat Token Vector, Ca' Foscari University of Venice, June 12},
  url = {https://www.unive.it/web/en/14779/home}
}
