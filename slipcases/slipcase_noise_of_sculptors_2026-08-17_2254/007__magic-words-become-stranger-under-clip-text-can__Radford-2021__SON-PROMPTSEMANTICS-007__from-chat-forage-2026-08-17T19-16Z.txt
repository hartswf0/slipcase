ZETTEL

ID:
SON-PROMPTSEMANTICS-007

TITLE:
“MAGIC WORDS” become stranger under CLIP: text can control images because language has been trained as a reference system for learned visual concepts.

SOURCE:
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger & Ilya Sutskever — “Learning Transferable Visual Models From Natural Language Supervision” — 2021. URL: https://arxiv.org/abs/2103.00020

PASSAGE:
[QUOTE]
After training, the authors say “natural language is used to reference learned visual concepts.”

RESEARCH OBJECT:
PROMPTING can operate because language has become an address system over learned visual regularities.

LOCAL MOVE:
The parent observes a culture in which prompt phrases acquire reputations as “magic words,” users hoard prompts as trade secrets, and expert knowledge circulates through repeated empirical discovery.

CLIP shifts the underlying question.

The strange thing is not merely that particular words work.

It is that a statistical training procedure can transform ordinary language into an interface for referencing visual representations learned from hundreds of millions of image/text pairings.

SOURCE TERMS:
natural language supervision
image
text
pair
text encoder
image encoder
representation
visual concepts
zero-shot transfer

WHAT BECAME STRANGE:
The prompt looks linguistically familiar to the human while functioning computationally inside a learned representational system.

This creates a double life for words.

For the user:

“castle”
is a word with cultural, architectural, and narrative meanings.

For the model:

“castle”
participates in a learned numerical representation produced by statistical relationships among text and images.

Prompt craft happens in the gap between those two systems.

QUESTION:
When users learn prompt craft, are they learning to describe images better or learning the idiosyncratic translation rules of a learned text–image representation?

DEEPER QUESTION:
When ordinary language becomes an executable conditioning interface, what remains of ordinary linguistic meaning and what becomes model-specific operational meaning?

MECHANISM:
CLIP jointly trains text and image encoders using large numbers of paired images and captions.

Natural-language descriptions can then reference learned visual concepts through the resulting representation.

Text-conditioned image generators can use representations of that kind as conditioning information.

FORMAL SHIFT:
FROM:

WORD
→ HUMAN MEANING
→ REQUEST

TO:

WORD
→ TOKENIZED TEXT
→ LEARNED TEXT REPRESENTATION
↔ LEARNED VISUAL REGULARITIES
→ CONDITIONING SIGNAL

SOURCE FORMALISM:
[PARAPHRASE]

CLIP learns image and text representations by training on matching image-text pairs and uses the text encoder to reference learned visual concepts at inference.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

HUMAN_LANGUAGE(p)
≠
MODEL_OPERATION(p)

Instead:

p
→ TEXT_ENCODER
→ embedding c

and the operational effect of p depends on the learned geometry surrounding c.

Therefore two phrases that seem semantically similar to a speaker may not be operationally equivalent for the model.

Conversely, strange phrases may become operationally powerful despite weak ordinary-language motivation.

TENSION:
This helps explain “magic words” without proving that every reported magic word reflects stable model structure.

A discovered phrase might instead be:

a reproducible representational effect
a prompt interaction
a training-data artifact
a stochastic coincidence
a version-specific behavior
or user superstition.

MISSING:
Controlled replications of the magical prompts reported by Midjourney users.

Prompt/output histories across model versions.

The exact text representation used by Midjourney V3.

BOUNDARY:
CLIP establishes a concrete mechanism by which natural language can reference learned visual concepts.

It does not establish that Midjourney V3 used precisely OpenAI CLIP or identical embeddings.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ magical prompts / prompt trade secrets
→ CLIP
→ natural language becomes reference to learned visual concepts
→ prompt craft becomes translation between HUMAN SEMANTICS and MODEL-OPERATIONAL SEMANTICS

TEST:
Collect claimed “magic words” from the parent interviews.

For each phrase construct:

literal paraphrases
synonyms
word-order variants
nonsense controls
token deletions

Run each across:

multiple seeds
multiple model versions
multiple text-to-image architectures

A real representational effect should show reproducible structure.

A stochastic anecdote should collapse under replication.

A platform-specific magic word should survive only within one architecture or version.

PLATFORM:
arXiv

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]
[[SON-WORDPOWER-004]]
[[SON-IEC-005]]

BIBTEX:
@misc{radford2021learning,
  title = {Learning Transferable Visual Models From Natural Language Supervision},
  author = {Alec Radford and Jong Wook Kim and Chris Hallacy and Aditya Ramesh and Gabriel Goh and Sandhini Agarwal and Girish Sastry and Amanda Askell and Pamela Mishkin and Jack Clark and Gretchen Krueger and Ilya Sutskever},
  year = {2021},
  eprint = {2103.00020},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  url = {https://arxiv.org/abs/2103.00020}
}
