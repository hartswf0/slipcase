ZETTEL

ID: BAJOHR-01
TITLE: The author can carry a character across generations
SOURCE: Hannes Bajohr — “The Latent Space of Meaning and the Novel,” Venice, 2025, composition of (Berlin, Miami). Checked against Bajohr’s production note in Ensemble Park, 2024.

PASSAGE: [PARAPHRASE] The talk describes iterative sentence completion. In his production note, Bajohr recalls encountering a pregnancy elsewhere in the text, typing “Jawling pregnancies,” and generating an account of the creature’s reproductive cycle.

RESEARCH OBJECT: A manually reintroduced fact that makes two passages appear to belong to the same world.
LOCAL MOVE: The production note documents one intervention inside the completion process that the lecture describes at a higher level.
SOURCE TERMS: “Jawling pregnancies,” iterative sentence completion.
WHAT BECAME STRANGE: A few typed words can do more for continuity than hundreds of generated tokens.
QUESTION: Which apparent acts of character memory in the published novel came from information the author reintroduced?
MECHANISM: The author notices an earlier detail, selects it for reuse, and supplies it as text that conditions a new continuation.
FORMAL SHIFT: <earlier fictional fact> → <author-supplied phrase> → [condition another completion] → <possible continuity across passages>.
SOURCE FORMALISM: The production note reports generation in chunks of 200 tokens and supplies this intervention. It leaves the effective context for this run unspecified.
OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Annotate each recurrence with where its antecedent was available: active prefix, author-supplied cue, both, or unknown.
TENSION: A. The cue revived an association the model was already likely to develop. B. The cue supplied continuity that otherwise would have disappeared.
MISSING: The full prefix, rejected continuations, sampling settings, and exact checkpoint. The talk calls the model GPT-J, while the production note says GPT-J/GPT-NeoX.
BOUNDARY: One documented intervention establishes a route by which continuity can enter the book. Its frequency across the book remains open.
CITATION TRAIL: Compare the German edition, the English Ensemble Park excerpt, and any surviving generation records.
TEST: If the run can be reconstructed, sample matched continuations with and without the cue. Score preservation of the earlier pregnancy separately from mere reuse of the character’s name.
PLATFORM: [[Where fictional state lives]]
LINKS: [[BAJOHR-02]] [[BAJOHR-04]]

BIBTEX:
@article{bajohr2024berlinmiami,
  author = {Bajohr, Hannes},
  title = {{(Berlin, Miami)}},
  journal = {Ensemble Park},
  number = {1},
  year = {2024},
  url = {https://www.ensemblepark.com/issues/ensemble_park_1.pdf}
}
