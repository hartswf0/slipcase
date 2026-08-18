ZETTEL

ID:
DEFAULT-IMAGES-CHI26-F

TITLE:
When a model lacks a word, it does not leave a hole where that culture should be; it fills the hole with something it already knows how to picture.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] The researchers deliberately include native Finnish and Tagalog terms among realistic prompts likely to challenge Midjourney because of low training-data coverage. They use haveibeentrained.com as an imperfect proxy for whether candidate terms are represented in large image-caption datasets. fileciteturn1file6L412-L428

[PARAPHRASE] The authors argue that defaults can reveal insufficient coverage of low-resource languages and potentially indicate deficiencies in training-data diversity. fileciteturn1file9L596-L605

RESEARCH OBJECT:
Linguistic underrepresentation does not merely reduce linguistic performance.

In a text-to-image system compelled to return an image, lexical absence can become visual substitution.

The missing representation is covered over by imagery drawn from better-established regions of the system.

LOCAL MOVE:
Reframe low-resource-language failure from:

MODEL CANNOT REPRESENT X

to:

MODEL CANNOT REPRESENT X
AND THEREFORE REPRESENTS Y.

The second clause is the new research object.

SOURCE TERMS:
low-resource languages
Finnish
Tagalog
training-data coverage
default images
dataset diversity
unknown inputs

WHAT BECAME STRANGE:
A blank, refusal, or explicit unknown would preserve evidence of absence.

A default image instead supplies a culturally unrequested positive representation.

The system's ignorance becomes substitution.

QUESTION:
When culturally or linguistically underrepresented concepts fail to condition generation, what visual priors replace them?

DEEPER QUESTION:
Are supposedly universal generative aesthetics partly the visible residue of what the model does whenever the world's less-represented vocabularies cease to exert control?

MECHANISM:
A term with weak learned visual association supplies little semantic guidance.

Generation then depends more heavily on learned recurrent visual structure.

The output can therefore inherit common motifs unrelated to the culturally specific requested concept.

FORMAL SHIFT:
FROM:

representation bias
= some concepts are generated less accurately

TO:

representation bias
= loss of requested semantic control
+
systematic occupation of the vacated output space by other priors.

SOURCE FORMALISM:
The paper creates six prompt categories.

A4 specifically contains low-resource-language words:

A4.1 Finnish
A4.2 Tagalog.

Candidate prompts are selected partly by checking apparent underrepresentation in large image-caption datasets through haveibeentrained.com. fileciteturn0file0L431-L459

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For concept c in language ℓ:

representation strength = R(c,ℓ).

If:

R(c,ℓ) < τ,

then the system does not output NULL.

Instead:

G(c,ℓ)
→ fallback distribution F_m.

The politically and culturally relevant object is therefore not only:

error(c,ℓ)

but:

substitute(c,ℓ) = dominant motifs sampled when R(c,ℓ) is weak.

TENSION:
The paper uses low-resource-language prompts as one experimental category and proposes bias research as a future direction.

It does not establish that every observed Tagalog or Finnish default is caused by linguistic underrepresentation, nor does its black-box design expose Midjourney’s actual training set.

Low resource in an external dataset proxy is not proof of absence from Midjourney training.

MISSING:
Direct training-data evidence.

Cross-language matched concepts.

Comparison of transliteration, translation, paraphrase, and native-language prompting.

Analysis of which demographic, cultural, geographic, and aesthetic motifs occupy the fallback distribution.

BOUNDARY:
The paper establishes a useful probe and an observed association, not a causal theorem that low-resource language status itself produces default images.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ A4 Finnish / Tagalog prompts
→ default images under weak recognition
→ authors' proposed study of “raw” demographic, cultural, and aesthetic biases
→ substitution becomes the unresolved object.

TEST:
Build concept-equivalent prompt sets across languages.

For each concept:

native low-resource term
translation into high-resource language
descriptive paraphrase in low-resource language
descriptive paraphrase in high-resource language.

Fix model parameters and sample many seeds.

Measure:

concept fidelity
default-image frequency
fallback motif distribution.

The key discriminating evidence is not merely whether one language fails more often, but whether its failures systematically converge on particular visual motifs absent from the requested concept.

PLATFORM:
Midjourney; comparative multilingual TTI evaluation.

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
