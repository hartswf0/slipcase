ZETTEL

ID:
DEFAULT-IMAGES-CHI26-E-1

TITLE:
The instrument used to detect default-image convergence has a convergence pathology of its own: CLIP produces hubs.

SOURCE:
Neil Chowdhury, Franklin Wang, Sumedh Shenoy, Douwe Kiela, Sarah Schwettmann, and Tristan Thrush — “Nearest Neighbor Normalization Improves Multimodal Retrieval” — 2024 — https://arxiv.org/abs/2410.24114

PASSAGE:
[PARAPHRASE] Chowdhury et al. study contrastive multimodal embedding models including CLIP and identify “hubness”: some candidates become nearest neighbors for disproportionately many unrelated queries. In their COCO text-to-image retrieval experiments, a base CLIP model contains numerous hub images that match more than one hundred captions. Correcting candidate-specific similarity bias substantially changes retrieval performance.

RESEARCH OBJECT:
The default-image study operationalizes recurrence through CLIP embedding similarity.

But CLIP's own geometry is not neutral.

It contains regions and examples that are systematically too close to many otherwise distinct queries.

This creates a measurement opposition:

GENERATOR COLLAPSE

versus

EMBEDDING-SPACE HUBNESS.

LOCAL MOVE:
Turn the detector back on itself.

Before interpreting a dense visual cluster as a property of Midjourney, ask whether some portion of the cluster density is created or amplified by the representation used to measure similarity.

SOURCE TERMS:
hubness
contrastive retrieval
CLIP
cosine similarity
nearest neighbor
hub images
Nearest Neighbor Normalization

WHAT BECAME STRANGE:
The experiment looks for images that are “too similar to too many things.”

The measuring instrument is itself documented to contain items that are “too similar to too many things.”

The anomaly and its detector therefore share a formal shape.

QUESTION:
Would the same Midjourney default-image clusters survive if visual similarity were measured in embedding spaces that do not share CLIP's hub structure?

DEEPER QUESTION:
How do we distinguish a generative attractor from an observational attractor created by the metric used to see it?

MECHANISM:
Contrastive embedding spaces can develop hubs: points receiving anomalously high similarity scores from many inputs.

Chowdhury et al. estimate candidate-specific bias from nearby reference queries and subtract that bias during retrieval, reducing hub domination.

The result demonstrates that raw cosine similarity in CLIP can contain systematic neighborhood distortion.

FORMAL SHIFT:
FROM:

CLIP_SIMILARITY(i₁,i₂)
≈ perceptual similarity

TO:

CLIP_SIMILARITY
= perceptual/semantic structure
+
embedding geometry
+
possible hub bias.

SOURCE FORMALISM:
For retrieval query q and candidate r, the source begins from:

s(q,r) = q · r

and estimates candidate-specific hub bias using its nearest reference queries.

It then computes a normalized score:

s_D(q,r) = s(q,r) - b(r).

The method explicitly treats some candidates as having systematic similarity offsets.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Parent detector:

DEFAULT_CANDIDATE
if

d_CLIP(i_a,i_b) small
while
d_TEXT(p_a,p_b) large.

But suppose an image embedding h has hubness H(h):

H(h) = number / density of unrelated neighbors for which h appears anomalously close.

Then observed convergence may contain two components:

C_observed
=
C_generator
+
C_metric.

The required test is therefore invariance:

cluster_default
should persist under multiple independent visual metrics.

TENSION:
The new source demonstrates hubness specifically in contrastive image-text retrieval.

Simonen et al. use CLIP image embeddings for image-image clustering.

These are related but not identical operations.

Therefore this source does NOT establish that the published default-image clusters are artifacts.

It establishes a serious measurement question that the parent method has not yet eliminated.

MISSING:
Re-clustering the 757,728-image dataset with independent representations such as:

DINO-family visual embeddings
LPIPS
SSIM / MS-SSIM
other vision encoders
human similarity judgments.

Also missing:

hubness statistics for the exact CLIP image-image embedding space and dataset used in the default-image study.

BOUNDARY:
Hubness in CLIP retrieval cannot by itself invalidate the default-image phenomenon.

The manual affinity-diagramming results and recurrent motifs provide evidence independent of large-scale CLIP clustering.

The issue principally pressures the scale and membership of automatically detected clusters.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-E]]
→ CLIP-based output-space convergence detector
→ contrastive-embedding hubness literature
→ detector itself contains preferential neighborhoods
→ generative collapse must be separated from measurement collapse.

TEST:
Re-run the exact default-image discovery pipeline with at least four independently trained visual representations.

For every candidate cluster calculate:

cluster persistence
membership agreement
centroid stability
human-rated visual coherence.

Then estimate each image's hubness under each representation.

A default-image cluster survives the opposition only if its recurrence remains after:

changing representation,
hub-normalizing similarity,
and human verification.

PLATFORM:
CLIP and other multimodal embedding models; Midjourney default-image detection pipeline.

LINKS:
[[DEFAULT-IMAGES-CHI26-E]]

BIBTEX:
@article{Chowdhury2024NNN,
  author = {Chowdhury, Neil and Wang, Franklin and Shenoy, Sumedh and Kiela, Douwe and Schwettmann, Sarah and Thrush, Tristan},
  title = {Nearest Neighbor Normalization Improves Multimodal Retrieval},
  journal = {arXiv preprint arXiv:2410.24114},
  year = {2024},
  url = {https://arxiv.org/abs/2410.24114}
}
