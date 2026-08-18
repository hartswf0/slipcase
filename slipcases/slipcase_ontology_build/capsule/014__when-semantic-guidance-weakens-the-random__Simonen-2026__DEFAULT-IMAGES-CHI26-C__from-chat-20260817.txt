ZETTEL

ID:
DEFAULT-IMAGES-CHI26-C

TITLE:
When semantic guidance weakens, the random seed stops looking like mere variation and begins choosing among meanings the prompt failed to determine.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] Changing the seed while keeping the prompt fixed often produced different default images that shared only partial motifs. The authors therefore used a fixed seed to make recurrent defaults easier to observe. fileciteturn1file8L512-L519

[PARAPHRASE] In the real-world dataset, where seeds varied, the researchers did not encounter the same canonical defaults found in the fixed-seed manual experiment; they report that seed-driven variation makes real-world detection substantially more difficult. fileciteturn1file2L137-L150

RESEARCH OBJECT:
Seed variation is not merely nuisance noise around one stable default.

Under weak semantic conditioning, it may determine which of several recurrent motifs becomes visible.

The object “the default image for prompt P” may therefore be incorrectly specified.

A more adequate object may be:

the distribution of fallback motifs for P under sampling states S.

LOCAL MOVE:
Replace DEFAULT IMAGE with DEFAULT DISTRIBUTION when reasoning across seeds.

SOURCE TERMS:
seed value
stochastic sampling
variation
default-image motif
many-to-many relationship
fixed seed

WHAT BECAME STRANGE:
A canonical default can be partly manufactured by experimental control.

Fixing the seed reveals recurrence, but it may also tempt the observer to treat one member of a sampling-dependent family as the model’s unique response to semantic failure.

QUESTION:
When a prompt supplies little semantic constraint, how much of the resulting image is determined by the prompt and how much by the sampling trajectory?

DEEPER QUESTION:
Does semantic underspecification increase the causal power of supposedly “random” generation parameters?

MECHANISM:
Weak prompt guidance leaves a wider set of possible generation trajectories available.

Changing the seed alters the sampled trajectory and can expose different recurrent motifs.

With stronger semantic constraints, the prompt may restrict this space more strongly.

FORMAL SHIFT:
FROM:

seed = cosmetic variation parameter

TO:

seed × conditioning-strength
= determinant of which fallback basin becomes visible.

SOURCE FORMALISM:
The manual experiment fixed:

model = 6.1
aspect ratio = 1
stylize = 0
chaos = 0
weird = 0
seed = 123456.

The authors then separately varied seed values in their sensitivity analysis. fileciteturn0file0L460-L483

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let semantic constraint strength be C(p).

Generated output:

i = G(p,s).

Hypothesis:

as C(p) ↓

∂i / ∂s ↑.

That is:

the weaker the prompt’s effective semantic constraint,
the greater the output variance attributable to sampling state.

Default behavior should therefore be modeled as:

D(p) = distribution {G(p,s₁), G(p,s₂), ... G(p,sₙ)}

rather than:

D(p) = one canonical image.

TENSION:
Fixed seeds are methodologically useful because they expose cross-prompt recurrence.

But a phenomenon visible primarily under fixed seeds could exaggerate the stability of the “default image” as a natural object.

The real-world dataset simultaneously supports default behavior and complicates the canonical-image conception.

MISSING:
A systematic factorial study crossing:

prompt semantic familiarity
prompt specificity
seed
model version

with enough samples to estimate variance components.

BOUNDARY:
The study's seed ablation is intentionally small-scale.

It establishes sensitivity but not a general quantitative law relating semantic weakness to seed influence.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ fixed-seed manual experiment
→ seed ablation
→ real-world random-seed dataset
→ canonical defaults disappear into motif variation
→ default image becomes a distributional object.

TEST:
Choose prompt classes spanning highly recognized to strongly unknown.

For each prompt generate N outputs over the same N seeds.

Estimate:

within-prompt / across-seed visual variance

and

across-prompt / within-seed visual convergence.

If unknown prompts show unusually high seed-dependent motif switching while still converging across prompts at particular seeds, the default phenomenon is jointly determined by semantic weakness and sampling state.

PLATFORM:
Midjourney v6.1 manual experiments and multi-version observational dataset.

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
