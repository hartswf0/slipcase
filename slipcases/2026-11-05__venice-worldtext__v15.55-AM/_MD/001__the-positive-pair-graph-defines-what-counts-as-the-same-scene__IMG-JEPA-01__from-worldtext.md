ZETTEL

ID: IMG-JEPA-01

TITLE:
The positive-pair graph defines what counts as the same scene

SOURCE:
Randall Balestriero and Yann LeCun — Proving and Improving the Platonic Representation Hypothesis with JEPAs — 2026 — §§2.1–2.3, Figure 3, §7

PASSAGE:
[PARAPHRASE] In the spectral setting, the learned directions come from the graph that positive pairs draw on world states. Exact agreement requires shared positives and uniqueness up to rotation. When the graphs differ, the bound depends on their mismatch and on the spectral gap.

RESEARCH OBJECT:
The rule for pairing observations as a prior about which differences matter.

LOCAL MOVE:
The proof rewrites each modality’s learning objective on the same state space.

SOURCE TERMS:
Positive-pair distribution, world kernel, injective rendering, spectral gap.

WHAT BECAME STRANGE:
[OUR INFERENCE] On Flickr, descriptions are grouped by photograph. The photograph supplies an address for the scene before the text encoder learns anything. Grouping by photographed event instead would change the learning problem.

QUESTION:
What does an imagetext experiment take as its unit of sameness: the image, the depicted event, or the relation a reader is asked to notice?

DEEPER QUESTION:
Can two descriptions of different images form a better pair for studying composition than two descriptions of the same image?

MECHANISM:
Changing the pair rule changes the graph. Under the paper’s spectral objective, this can change which distinctions survive in the leading embedding directions.

FORMAL SHIFT:
<Observations> → <weighted edges between states> → [spectral embedding] → <geometry of learned similarities>

SOURCE FORMALISM:
Kπ = D^(-1/2) Π D^(-1/2), where Π represents the positive-pair distribution and D = diag(p). With second-order anti-collapse and a spectral gap, the solution is determined by the leading nonconstant eigenspace, up to rotation.

OUR FORMALIZATION:
NONE

TENSION:
The proof requires a specified relation among states. In imagetext analysis, deciding whether two views depict the same event can itself be an interpretive judgment.

MISSING:
A test that varies the grouping rule while holding the actual images and texts fixed.

BOUNDARY:
The spectral result supplies a sufficient condition for alignment under its assumptions. The paper leaves uniqueness under LeJEPA’s full-distribution constraint open.

CITATION TRAIL:
Laplacian eigenmaps and spectral contrastive learning, both cited in §2.1.

TEST:
Take one staged dispute photographed from several angles and a second dispute staged with the same blocking. Compare grouping by image ID, event ID, and blocking. Hold out one camera angle. Ask which grouping retrieves the same event and which retrieves the same composition.

PLATFORM:
[[Imagetext as a Unit of Analysis]]

LINKS:
[[Positive Pair Provenance]]
[[Scene Identity]]
[[Composition Across Images]]

BIBTEX:
@misc{balestriero2026platonic,
  author = {Balestriero, Randall and LeCun, Yann},
  title = {Proving and Improving the Platonic Representation Hypothesis with {JEPAs}},
  year = {2026},
  eprint = {2610.39302},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/html/2610.39302v1}
}