ZETTEL

ID:
DEFAULT-IMAGES-CHI26-B

TITLE:
The paper observes default images in Midjourney, but it cannot yet locate the default inside the model.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] The authors explicitly state that they lack access to Midjourney’s training data and underlying model. They consider latent behavior and training-data gaps likely explanations but note that sampling mechanisms and possible prompt rewriting may also contribute. Because the proprietary system may intervene between input and output, the study cannot fully determine whether defaults originate in model behavior or platform design. fileciteturn1file7L440-L455

RESEARCH OBJECT:
“Default image” is securely established as an input-output phenomenon but not yet as a located internal mechanism.

The research object must therefore be split:

DEFAULT IMAGE AS OBSERVATION

versus

DEFAULT MECHANISM AS CAUSAL CLAIM.

LOCAL MOVE:
Downgrade “latent-space default” from established mechanism to candidate explanation.

SOURCE TERMS:
training data
latent model behavior
sampling mechanism
prompt rewriting
platform design decisions
black-box
causality

WHAT BECAME STRANGE:
The most visually obvious thing in the study may be the least causally localized.

A repeated motif appears to reveal the model’s interior, yet precisely because Midjourney is a black box, it might instead reveal an invisible transformation layer surrounding the model.

QUESTION:
Where does the fallback actually occur?

DEEPER QUESTION:
Could a system acquire recognizable “default images” even if its underlying generative model had no stable default regions, simply because a prompt-rewriting layer repeatedly maps unfamiliar inputs onto similar surrogate prompts?

MECHANISM:
Several mechanisms remain observationally compatible:

1. weak or absent training representation;
2. text-encoder collapse or proximity;
3. prompt rewriting;
4. conditioning failure;
5. sampling toward high-density visual regions;
6. memorization or over-training;
7. interactions among several of these.

FORMAL SHIFT:
FROM:

PROMPT
→ MODEL
→ DEFAULT IMAGE

TO:

PROMPT
→ UNKNOWN PLATFORM TRANSFORMATIONS
→ CONDITIONING REPRESENTATION
→ GENERATIVE PROCESS
→ SAMPLING
→ IMAGE.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Observed:

p₁, p₂, ... pₙ
→ visually convergent outputs.

But the actual system may be:

p
→ R(p)
→ E(R(p))
→ G(E(R(p)), s)
→ i

where:

R = unknown prompt rewrite / preprocessing
E = conditioning representation
G = image generator
s = sampling state.

Visual convergence therefore cannot identify whether convergence first occurred in R, E, or G.

TENSION:
The paper gives a substantive latent-space explanation earlier in its discussion, describing weakly guided sampling around generic visual patterns. fileciteturn1file9L561-L575

Its limitations section is more cautious and concedes that the proprietary pipeline prevents strong causal localization. fileciteturn1file7L443-L455

Both readings should be retained:

DEFAULTS-AS-LATENT-STRUCTURE

versus

DEFAULTS-AS-PIPELINE-PHENOMENON.

MISSING:
The actual transformed prompt received by the image model.

Internal text embeddings.

Conditioning traces.

Sampling implementation.

Training-data evidence for the allegedly unknown concepts.

BOUNDARY:
Black-box behavioral evidence can establish repeatable system behavior without establishing which internal component produced it.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ causal explanation in Section 2
→ causal qualification in limitations
→ unresolved model-versus-platform distinction
→ inspectable systems become necessary.

TEST:
Replicate default-image prompting in an open-weight TTI pipeline where every intermediate state can be logged.

Run four conditions:

raw prompt
→ encoder
→ generator

raw prompt
→ explicit LLM rewrite
→ encoder
→ generator

unknown prompt mapped to empty conditioning

unknown prompt mapped to nearest known semantic representation.

Compare whether recurrent motifs arise and determine the earliest stage at which otherwise unrelated inputs converge.

PLATFORM:
Midjourney as proprietary black-box system; comparative test requires inspectable TTI models.

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
