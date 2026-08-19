ZETTEL

ID: FORAGE-PG-005

TITLE: cyber.json is titled "Agential Cybernetic Media" — the corpus's redundancy rule (>80% overlap → merge or retire) is armed against its own cybernetic lineage

SOURCE: PROGRAMS/cyber.json — ProgramTheory title, entities, Theory-Code Mapping; PROGRAMS/agential.json — program_theory id, core_entities, theoretical_lineage; PROGRAMS/meta.json — REGISTER STEP R2, LAW 3 (CLAUDE.md)

PASSAGE: [QUOTE cyber.json] '<ProgramTheory title="Agential Cybernetic Media" version="2.0" ...>' with entities including "<AgentialCut> <Boundary> ... <FeedbackLoop> <CyberneticSystem> ... <RequisiteVariety> <Metis> <Legibility>" and types "<Metis> := the Scottian defense against flattening". [QUOTE agential.json] '<program_theory id="agential-worlds-cybernetic-cuts" version="2.0">' with core_entities "<agential_cut/> <phenomenon/> <cybernetic_circuit/> ... <legibility_regime/> <metis/>" and lineage nodes Barad, Bateson, Second_Order_Cybernetics, Flusser, Scott. [QUOTE meta.json] "STEP R2: [check-corpus-redundancy] ... IF overlap > 80%: FLAG <redundancy> and [require-operator-ruling]".

RESEARCH OBJECT: The pair (cyber.json, agential.json): two registered theories drawing on the same five-author lineage (Barad, Bateson, Flusser, Scott, second-order cybernetics), sharing the cut/circuit/metis/legibility entity core, the same central maxim (ethics begins at the cut), and near-identical failure modes (LegibilityCollapse/metis_erasure, BlackBoxFunctionaryMode/fluent_black_box, RelationalErasure/human_centering_evasion).

LOCAL MOVE: Apply the corpus's own R2 redundancy check to one pair, estimating entity-set overlap by named-concept matching rather than trusting the manifest's claim that they are distinct ("cybernetic media ↔ agential cuts" listed as productive tension).

SOURCE TERMS: AgentialCut / agential_cut; Metis; RequisiteVariety; FunctionaryMode; cut visibility; ethics of mattering; no-addition-without-subtraction; >80% overlap

WHAT BECAME STRANGE: The corpus manifest assigns them different theses ("Apparatus cuts determine what becomes determinate" vs "AI is a world-making participant, not a tool") but the files themselves each assert both theses: cyber.json's invariants include "<AIApparatus> [is] <WorldMakingParticipant>" AND the cut machinery; agential.json's invariants include cut-ethics AND "<AI_output> is a <world_making_event>". The differentiation exists in the manifest layer, not the theory layer.

QUESTION: What is the actual overlap coefficient of the two entity sets under reasonable synonym identification, and does it cross 0.8?

DEEPER QUESTION: Is redundancy in a theory corpus a defect at all? Two near-isomorphic theories differing in output type (cyber → reclassification rules; agential → design_interventions and responsibility_maps) may be one theory at two deployment temperatures — which would argue for meta to add a notion of "aspect" or "profile" instead of merge-or-retire.

MECHANISM: R2's overlap check plus LAW 3 ("If it overlaps >80% with an existing theory, it must merge or the existing theory must retire") — a hard rule with no aspect exemption.

FORMAL SHIFT: From informal "these two feel similar" to a corpus-governance rule with a numeric threshold, revealing that the threshold was specified but the measurement procedure (how to count entities as identical across naming conventions) was not.

SOURCE FORMALISM: Entity lists in two different XML dialects (CamelCase in cyber, snake_case in agential); meta's REGISTER pseudocode.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Map both entity sets through a normalization ν (case-fold, strip underscores, synonym table {apparatus≈AIApparatus, cut≈AgentialCut, ...}). Jaccard(ν(E_cyber), ν(E_agential)) on core concepts ≈ 0.55–0.7 by our count; overlap of failure-mode semantics is higher (≥ 5 of 7 map 1-to-1). Whether R2 fires depends entirely on ν — the rule's teeth are in the unspecified normalizer.

TENSION: Manifest says productive tension (compose them); R2 arithmetic plausibly says redundancy (merge or retire one). These trigger different directives with irreversible consequences (MERGE retires both originals). Rival reading: the pair is the corpus testing its own merge machinery — the known_duplicate note about td.json (byte-for-byte duplicate of mot.json, "candidate for retirement") shows the corpus already tolerates known redundancy without acting.

MISSING: The measurement procedure for entity overlap; an operator ruling on this pair; the td.json file itself (named in the manifest as a duplicate but absent from the directory — retired silently or never existed).

BOUNDARY: Overlap analysis here covers entities and failure modes; program texts differ genuinely (cyber's main_loop vs agential's analyze() pipeline), so a merge would lose neither's operative machinery but would lose their difference in address (media theory vs design practice).

CITATION TRAIL: Barad, Meeting the Universe Halfway; Bateson, Steps to an Ecology of Mind; Flusser, Towards a Philosophy of Photography; Scott, Seeing Like a State; Beer (requisite variety via Ashby) → both files → meta.json cross_references "cyber.json ↔ agential.json".

TEST: Implement ν three ways (strict string match, embedding similarity at cosine ≥ 0.8, human synonym table); compute Jaccard under each; report whether the R2 threshold's verdict is stable across normalizers. If not, LAW 3 is unenforceable as written.

PLATFORM: Any scripting environment; optionally embeddings for the similarity variant.

LINKS: [[FORAGE-PG-002]], [[FORAGE-PG-003]], [[FORAGE-PG-007]], [[FORAGE-PG-014]]

BIBTEX: @unpublished{cyber2026agential, title={Agential Cybernetic Media}, note={PROGRAMS/cyber.json, version 2.0, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @unpublished{agential2026worlds, title={agential-worlds-cybernetic-cuts}, note={PROGRAMS/agential.json, version 2.0, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @book{barad2007meeting, author={Barad, Karen}, title={Meeting the Universe Halfway}, publisher={Duke University Press}, year={2007}} @book{scott1998seeing, author={Scott, James C.}, title={Seeing Like a State}, publisher={Yale University Press}, year={1998}}
