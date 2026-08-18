ZETTEL

ID:
DEFAULT-IMAGES-CHI26-D

TITLE:
A model version may have a visual failure signature: what it draws when it cannot tell what you asked for.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] Midjourney v6.0 and v6.1 produced very similar defaults for the same prompts, while older versions such as v5.1 and v5.2 showed a more surreal or abstract aesthetic with recurring motifs including floating objects and human portraits intertwined with plants or animals. fileciteturn1file8L541-L548

[PARAPHRASE] The paper therefore proposes that each model version has its own set of default images and that these defaults change as models and their learned visual patterns change. fileciteturn1file0L37-L56

RESEARCH OBJECT:
A model can potentially be characterized not only by what it generates when it understands a request, but by what it generates when semantic guidance collapses.

Failure outputs may constitute a version-specific behavioral fingerprint.

LOCAL MOVE:
Treat failure morphology as a model characteristic rather than merely defective output.

SOURCE TERMS:
model-specific default images
model version
training data
default motifs
model signature
visual patterns

WHAT BECAME STRANGE:
Benchmarks usually ask models questions they are expected to answer.

Default-image probing asks the inverse question:

What does this model do when there is almost nothing meaningful for it to obey?

The answer may distinguish models unusually well.

QUESTION:
Are default-image distributions stable enough to identify a model family or version from outputs alone?

DEEPER QUESTION:
Would a genealogy of generative models be visible in the evolution of their failure motifs even when their successful outputs increasingly converge in quality?

MECHANISM:
Changes in training data, architecture, text-image representation, tuning, or sampling may change the high-probability imagery reached under weak conditioning.

The paper establishes version-associated differences but cannot attribute those differences to a particular internal change.

FORMAL SHIFT:
FROM:

MODEL CAPABILITY PROFILE
= performance on known tasks

TO:

MODEL BEHAVIOR PROFILE
= performance on known tasks
+
morphology of failure under unknown inputs.

SOURCE FORMALISM:
The paper's Postulate P2 states that model versions possess different sets of default images.

Its version ablation compares the same prompt across Midjourney releases and visually inspects recurring motifs. fileciteturn1file0L37-L38

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For model version m define a fallback distribution:

F_m = P(image features | semantic guidance ≈ 0, model=m).

Model fingerprinting asks whether:

distance(F_m1, F_m2)

is sufficiently large that an unknown output set can be classified by model/version.

TENSION:
The paper suggests model-specific defaults may reflect training data.

But version changes can also include architecture, prompt processing, fine-tuning, safety layers, aesthetic tuning, or sampling changes.

A model signature is not automatically a training-data signature.

MISSING:
Controlled comparisons where only one component changes at a time.

Longitudinal default-image datasets spanning closely spaced model releases.

Evidence separating version identification from seed, style, personalization, and interface effects.

BOUNDARY:
The paper demonstrates differences among Midjourney releases; it does not establish forensic identification accuracy or uniqueness across unrelated TTI systems.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ model-version ablation
→ Postulate P2
→ default images as model signatures
→ unresolved question of whether failure distributions preserve model genealogy.

TEST:
Build a blind classification benchmark.

For each model/version:

1. select the same large set of low-recognition prompts;
2. sample many seeds;
3. remove obvious metadata;
4. extract visual embeddings;
5. train a classifier on fallback-output distributions;
6. test on unseen prompts and seeds.

Then compare fingerprint accuracy from unknown-input outputs against accuracy from ordinary prompt outputs.

PLATFORM:
Midjourney versions 1–6.1; proposed extension across TTI systems.

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
