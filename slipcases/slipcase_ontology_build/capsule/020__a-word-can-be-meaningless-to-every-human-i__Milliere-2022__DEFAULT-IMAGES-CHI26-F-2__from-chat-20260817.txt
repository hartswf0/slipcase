ZETTEL

ID:
DEFAULT-IMAGES-CHI26-F-2

TITLE:
A word can be meaningless to every human in the room and still be densely meaningful to the image model.

SOURCE:
Raphaël Millière — “Adversarial Attacks on Image Generation With Made-Up Words” — 2022 — https://arxiv.org/abs/2208.04135

PASSAGE:
[PARAPHRASE] Millière constructs “macaronic” nonce words by combining fragments associated with the same concept across several languages. Fragments drawn from German, Italian, French, and Spanish words for birds can be recombined into strings with no conventional lexical meaning yet still reliably elicit bird imagery from DALL-E 2. Other manufactured strings target insects, butterflies, lizards, rabbits, cliffs, airplanes, firefighters, education, and emotional concepts. Some of these fabricated prompts transfer to DALL-E mini despite substantial architectural and tokenizer differences.

[PARAPHRASE] Millière also challenges the stronger claim that DALL-E 2 possesses a mysterious autonomous “hidden vocabulary.” Some apparently magical strings may instead work because subword tokenization preserves fragments associated with real words and visual concepts.

RESEARCH OBJECT:
“Unknown input” is not a property of the visible string.

It is a relation between the visible string and the model's tokenization-plus-representation machinery.

A prompt can fail every human lexical test while activating an unusually coherent model concept.

LOCAL MOVE:
Split:

NON-WORD

from:

SEMANTICALLY EMPTY FOR THE MODEL.

They are not equivalent.

SOURCE TERMS:
macaronic prompting
nonce strings
lexical hybridization
subword units
BPE tokenization
multilingual data
evocative prompting

WHAT BECAME STRANGE:
The system's vocabulary need not line up with any human vocabulary.

There can be strings that no speaker uses, no dictionary contains, and no author intended—yet the model treats them as effective instructions.

The machine does not merely have gaps between known words.

It has semantic corridors cutting diagonally through pieces of many languages.

QUESTION:
How many “unknown” prompts in the default-image study are actually unknown to the model, rather than unusual surfaces composed of familiar subword fragments with competing or weak visual associations?

DEEPER QUESTION:
Is a model's operative prompt language better described as a geometry over subword fragments than as a vocabulary of human words?

MECHANISM:
Subword tokenization decomposes strings into units that may have acquired visual associations during multilingual training.

Millière deliberately combines fragments from several translations of the same target concept.

The resulting nonce string is meaningless according to ordinary lexical semantics but can concentrate multiple learned subword associations toward one visual concept.

FORMAL SHIFT:
FROM:

WORD ∈ VOCABULARY
→ understood

WORD ∉ VOCABULARY
→ unknown

TO:

STRING
→ TOKENIZATION
→ set / sequence of learned subword associations
→ visual conditioning strength.

SOURCE FORMALISM:
The source constructs artificial lexical hybrids from fragments of words sharing a visual referent across multiple languages.

For example, fragments from translations of “birds” are recombined into novel strings and tested as image-generation prompts.

The method is experimental rather than a formal programming language, but its operative chain is explicit:

MULTILINGUAL SOURCE WORDS
→ SUBWORD FRAGMENTS
→ HYBRID NONCE STRING
→ IMAGE GENERATION.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For visible prompt string s:

T(s) = {τ₁, τ₂, ... τₙ}

where T is tokenizer decomposition.

Human lexical validity:

H(s) ∈ {word, non-word}

does not determine model semantic strength.

Define:

C(s,c) = aggregate conditioning strength of T(s) toward concept c.

Then it is possible that:

H(s) = non-word

while:

C(s,bird) >> 0.

Conversely, a legitimate low-resource word may satisfy:

H(s) = word

while:

C(s,intended concept) ≈ 0.

TENSION:
Daras and Dimakis described some gibberish behavior as a possible “hidden vocabulary.”

Millière argues this framing may be misleading because token overlap, BPE decomposition, multilingual associations, and morphological resemblance offer more ordinary mechanisms.

The strange behavior survives.

Its ontology changes:

not SECRET WORDS,

but MISALIGNED LEXICAL GEOMETRY.

MISSING:
Tokenizer-level analysis of Simonen et al.'s six default-triggering prompt classes.

For each purportedly unknown input, we do not yet know:

its token decomposition,
training frequency of those pieces,
visual neighbors of each piece,
or whether several pieces exert mutually cancelling conditioning.

BOUNDARY:
Macaronic prompting is deliberately constructed and does not show that ordinary nonce strings generally possess reliable semantics.

Many nonsense strings remain unstable or ineffective.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-F]]
→ model fills unrecognized language with default imagery
→ Daras and Dimakis hidden-vocabulary anomaly
→ Millière's tokenizer/subword opposition
→ unknown-to-human ≠ unknown-to-model
→ default-image research needs a model-relative definition of UNKNOWN.

TEST:
Take every prompt in Simonen et al.'s A1–A6 sets.

For an open model:

1. record tokenizer decomposition;
2. estimate each token's nearest lexical and visual neighbors;
3. calculate token frequency and multilingual overlap;
4. compare these properties with probability of default-like output.

Then generate matched controls:

human non-words with high coherent subword association,
human words with weak model association,
random strings with no coherent association.

If default behavior tracks representation strength rather than wordhood, replace the category UNKNOWN INPUT with MODEL-RELATIVE CONDITIONING DEFICIT.

PLATFORM:
DALL-E 2; DALL-E mini; subword-tokenized text-to-image systems.

LINKS:
[[DEFAULT-IMAGES-CHI26-F]]

BIBTEX:
@article{Milliere2022MadeUpWords,
  author = {Milli{\`e}re, Rapha{\"e}l},
  title = {Adversarial Attacks on Image Generation With Made-Up Words},
  journal = {arXiv preprint arXiv:2208.04135},
  year = {2022},
  url = {https://arxiv.org/abs/2208.04135}
}
