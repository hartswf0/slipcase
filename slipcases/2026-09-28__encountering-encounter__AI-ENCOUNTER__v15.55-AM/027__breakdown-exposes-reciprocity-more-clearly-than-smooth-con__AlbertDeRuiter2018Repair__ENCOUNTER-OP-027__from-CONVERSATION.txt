ZETTEL

ID:
ENCOUNTER-OP-027

TITLE:
Breakdown exposes reciprocity more clearly than smooth conversation does.

SOURCE:
Saul Albert and J. P. de Ruiter — “Repair: The Interface Between Interaction and Cognition” — 2018 — Topics in Cognitive Science 10(2), 279–313. ([doi.org](https://doi.org/10.1111/tops.12339))

PASSAGE:
[PARAPHRASE] Conversation analysis distinguishes who initiates repair from who resolves it, yielding four combinations of self/other initiation and self/other repair. ([doi.org](https://doi.org/10.1111/tops.12339))

RESEARCH OBJECT:
Repair transforms “mutual understanding” from an invisible mental-state claim into observable sequential work performed when interaction encounters trouble.

LOCAL MOVE:
Albert and de Ruiter make misunderstanding analytically productive. Trouble reveals who notices divergence, who marks it, who supplies a candidate correction, and whether coordinated action can resume.

SOURCE TERMS:
repair
trouble-source
self-initiation
other-initiation
self-repair
other-repair
understanding
progressivity
intersubjectivity

WHAT BECAME STRANGE:
Smooth dialogue supplies weak evidence of reciprocity because both parties can continue while misunderstanding one another. A breakdown generates an interactional probe of the relation.

QUESTION:
Who carries the burden of keeping a human–AI encounter intelligible when shared progress breaks?

DEEPER QUESTION:
Does a stronger encounter require both participants to detect trouble, or only the coupled system to recover from it?

MECHANISM:
trouble-source
→ trouble detection
→ repair initiation
→ candidate repair
→ acceptance/rejection
→ resumed or failed progress.

FORMAL SHIFT:
<APPARENTLY SMOOTH EXCHANGE>
→ <ENGINEERED TROUBLE>
→ [REPAIR SEQUENCE]
→ <OBSERVABLE COORDINATION STRUCTURE>

SOURCE FORMALISM:
Four-way repair taxonomy:
SISR = self-initiated self-repair
SIOR = self-initiated other-repair
OISR = other-initiated self-repair
OIOR = other-initiated other-repair. ([doi.org](https://doi.org/10.1111/tops.12339))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For human–AI interaction:

INITIATOR ∈ {HUMAN, AI}
RESOLVER ∈ {HUMAN, AI}

Measure:
TROUBLE_OPPORTUNITIES
REPAIR_INITIATION_RATE
AI_INITIATION_RATE
HUMAN_INITIATION_RATE
REPAIR_SUCCESS
REPAIR_LATENCY
REPEATED_TROUBLE
REPAIR_BURDEN_ASYMMETRY

TENSION:
A language model may generate linguistically appropriate repair forms without representing the misunderstanding that generated them.

MISSING:
A criterion distinguishing substantive trouble detection from generic clarification behavior.

BOUNDARY:
Conversation-analysis repair categories describe observable sequential organization. They do not by themselves establish equivalent cognitive processes across humans and AI.

CITATION TRAIL:
[[ENCOUNTER-006]]
[[ENCOUNTER-AI-021]]
→ Albert and de Ruiter 2018
→ Pütz and Esposito 2024
→ controlled ambiguity probes
→ repair symmetry as encounter signature.

TEST:
Seed ambiguous reference, contradictory assumptions, under-specification, and mistaken premises into otherwise identical conversations. Code who first detects each trouble and who performs the work required to recover. Compare human-human and human-LLM baselines.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-006]]
[[ENCOUNTER-AI-021]]
[[Repair]]
[[Encounter Breakdown Test]]

BIBTEX:
@article{AlbertDeRuiter2018Repair,
  author = {Saul Albert and J. P. de Ruiter},
  title = {Repair: The Interface Between Interaction and Cognition},
  journal = {Topics in Cognitive Science},
  year = {2018},
  volume = {10},
  number = {2},
  pages = {279--313},
  doi = {10.1111/tops.12339}
}