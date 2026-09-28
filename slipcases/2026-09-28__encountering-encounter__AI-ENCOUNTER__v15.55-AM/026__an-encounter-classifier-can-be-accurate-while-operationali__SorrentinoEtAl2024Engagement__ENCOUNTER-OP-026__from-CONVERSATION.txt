ZETTEL

ID:
ENCOUNTER-OP-026

TITLE:
An encounter classifier can be accurate while operationalizing no stable encounter construct.

SOURCE:
Alessandra Sorrentino, Laura Fiorini, and Filippo Cavallo — “From the Definition to the Automatic Assessment of Engagement in Human–Robot Interaction: A Systematic Review” — 2024 — International Journal of Social Robotics 16, 1641–1663. ([doi.org](https://doi.org/10.1007/s12369-024-01146-w))

PASSAGE:
[PARAPHRASE] Six of the 28 reviewed studies supplied no explicit engagement definition; the literature frequently turned engagement into binary or multiclass classification, while the review found weak correspondence between conceptual components and extracted features. ([doi.org](https://doi.org/10.1007/s12369-024-01146-w))

RESEARCH OBJECT:
Operationalization can silently reverse direction: instead of theory determining indicators, available indicators begin determining what “encounter” means.

LOCAL MOVE:
The review audits the chain linking definition, annotation, feature extraction, and automatic prediction and finds conceptual instability propagating down that chain.

SOURCE TERMS:
engagement definition
annotation
ground truth
features
binary classification
multi-class classification
continuous state
cue-centric
automatic prediction

WHAT BECAME STRANGE:
A technically excellent encounter detector could simply learn annotators’ intuitions about politeness, duration, attention, or affect and then return those intuitions as if they constituted encounter.

QUESTION:
What construct-validity test should an “encounter” feature pass before entering a detector?

DEEPER QUESTION:
Should encounter even be represented by a single ground-truth label?

MECHANISM:
underspecified construct
→ annotation convention
→ proxy feature selection
→ classifier training
→ high prediction accuracy
→ proxy becomes mistaken for phenomenon.

FORMAL SHIFT:
<THEORETICAL CONSTRUCT>
→ <OPERATIONAL DEFINITION>
→ [ANNOTATION]
→ <FEATURES>
→ [MODEL]
→ <PREDICTION>

SOURCE FORMALISM:
The reviewed detection pipeline distinguishes:
DATA ANNOTATION
→ FEATURE EXTRACTION
→ AUTOMATIC PREDICTION.

Studies variously represent engagement as binary, multiclass, or continuous. ([doi.org](https://doi.org/10.1007/s12369-024-01146-w))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

INVALID SHORTCUT:
OBSERVABLE CUE → “ENCOUNTER”

REQUIRED CHAIN:
ENCOUNTER CLAIM
→ DIMENSION
→ OBSERVABLE SIGNATURE
→ ALTERNATIVE EXPLANATIONS
→ DISCRIMINANT TEST
→ MEASURE

TENSION:
[[ENCOUNTER-AI-016]] supplies structural encounter criteria, but converting those directly into labels would still leave “generative emergence” unmeasured.

MISSING:
Discriminant validity: variables that separate encounter from engagement, enjoyment, anthropomorphism, task success, conversation length, and mere linguistic fluency.

BOUNDARY:
The review concerns engagement in HRI, not human–LLM encounter specifically. Its methodological warning transfers more securely than any particular HRI feature set.

CITATION TRAIL:
[[ENCOUNTER-AI-016]]
→ Sorrentino et al. 2024
→ engagement construct validity
→ encounter annotation
→ discriminant validation.

TEST:
Give the same interaction corpus to annotators using four definitions:
ENGAGEMENT,
COLLABORATION,
CONVERSATION QUALITY,
ENCOUNTER.
Measure label overlap. Features that predict all four equally well are poor encounter-specific indicators.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-OP-024]]
[[Construct Validity]]
[[Encounter Detector]]

BIBTEX:
@article{SorrentinoEtAl2024Engagement,
  author = {Alessandra Sorrentino and Laura Fiorini and Filippo Cavallo},
  title = {From the Definition to the Automatic Assessment of Engagement in Human--Robot Interaction: A Systematic Review},
  journal = {International Journal of Social Robotics},
  year = {2024},
  volume = {16},
  pages = {1641--1663},
  doi = {10.1007/s12369-024-01146-w}
}