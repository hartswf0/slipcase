ZETTEL

ID:
DEFAULT-IMAGES-CHI26-E

TITLE:
Default-image detection reverses ordinary prompt evaluation: the signal is visual similarity where linguistic similarity is absent.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — CHI ’26 — 2026 — https://doi.org/10.1145/3772318.3790681

PASSAGE:
[PARAPHRASE] The authors identify candidates by first clustering visually similar outputs with CLIP embeddings and then eliminating clusters whose associated prompts share too much lexical or semantic similarity. Their lexical filter excludes clusters when a word occurs in at least half of the associated prompts; their semantic filter removes clusters whose average prompt-embedding similarity exceeds 0.3. fileciteturn0file0L590-L647

RESEARCH OBJECT:
The paper turns default-image detection into a relational anomaly.

Neither a strange image nor a misunderstood prompt is sufficient.

The phenomenon appears only when two relations disagree:

IMAGE RELATION:
these outputs are unusually alike.

PROMPT RELATION:
the instructions producing them are unusually unlike.

LOCAL MOVE:
Move from judging single prompt-output pairs to detecting contradictions between two similarity spaces.

SOURCE TERMS:
CLIP
cosine similarity
agglomerative hierarchical clustering
lexical overlap
semantic similarity
sentence transformers
default-image cluster

WHAT BECAME STRANGE:
The failure is invisible in either modality alone.

Looking only at the images, the cluster may appear coherent.

Looking only at the prompts, nothing may connect them.

The anomaly exists in the mismatch between representational spaces.

QUESTION:
What other generative failure modes become detectable only by comparing the topology of input space with the topology of output space?

DEEPER QUESTION:
Can generative-system behavior be mapped as systematic distortions between neighborhoods in instruction space and neighborhoods in artifact space?

MECHANISM:
The method searches for output neighborhoods that collapse inputs which are distant in language space.

A candidate default cluster therefore represents a local many-to-one distortion between prompt semantics and generated-image semantics.

FORMAL SHIFT:
FROM:

evaluate:

prompt ↔ its image

TO:

compare:

relations among prompts
↔
relations among outputs.

SOURCE FORMALISM:
The source computes CLIP ViT-L/14 embeddings for images and uses agglomerative hierarchical clustering with a cosine-distance threshold of 0.1, followed by cluster merging based on centroid similarity at 0.9.

For a cluster with M prompts and vocabulary V, it defines lexical overlap as:

L = max_{w∈V} freq(w) / M

and excludes the cluster if:

L ≥ 0.5.

It then calculates average pairwise semantic similarity among prompt embeddings using all-MiniLM-L6-v2 and excludes clusters with semantic similarity > 0.3. fileciteturn0file0L590-L647

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

d_P(pᵢ,pⱼ) = distance between prompts

d_I(iᵢ,iⱼ) = distance between outputs.

A default-like collapse occurs where:

d_P(pᵢ,pⱼ) >> 0

while:

d_I(G(pᵢ),G(pⱼ)) ≈ 0.

More generally define representational distortion:

Δᵢⱼ = d_P(pᵢ,pⱼ) - d_I(G(pᵢ),G(pⱼ)).

Large positive Δ indicates linguistic distinctions being collapsed in output space.

Large negative Δ would indicate the inverse phenomenon:

similar instructions producing unexpectedly divergent artifacts.

TENSION:
The method depends on representation models to decide both visual similarity and semantic dissimilarity.

A cluster can therefore be classified as a generative-model failure partly because CLIP and a sentence-transformer impose their own similarity geometries.

The detector's ontology is not independent of other learned models.

MISSING:
Human validation of prompt semantic distance at scale.

Sensitivity analysis across image and text embedding models.

A principled rather than visually tuned choice of thresholds.

Analysis of the inverse anomaly: semantically close prompts producing systematically distant outputs.

BOUNDARY:
This procedure detects candidate clusters under operational similarity thresholds.

It does not prove that every resulting cluster shares one internal causal mechanism.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-ROOT]]
→ computational detection method
→ image-space convergence + prompt-space divergence
→ relational rather than pairwise failure
→ possibility of mapping distortions between instruction space and output space.

TEST:
Construct two neighborhood graphs over the same dataset:

G_P = nearest-neighbor graph of prompts

G_I = nearest-neighbor graph of generated images.

Measure edges present in G_I but absent in G_P and edges present in G_P but absent in G_I.

Cluster these topology disagreements.

Determine whether default images are one member of a larger taxonomy of cross-space distortions.

PLATFORM:
Midjourney dataset; CLIP ViT-L/14; all-MiniLM-L6-v2; agglomerative hierarchical clustering.

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
