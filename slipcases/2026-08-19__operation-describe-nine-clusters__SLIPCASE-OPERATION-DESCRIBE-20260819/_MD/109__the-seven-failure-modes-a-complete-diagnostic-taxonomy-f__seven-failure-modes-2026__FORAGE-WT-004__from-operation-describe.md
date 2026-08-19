ZETTEL

ID: FORAGE-WT-004

TITLE: The seven failure modes: a complete diagnostic taxonomy for how a worldtext dies

SOURCE: worldtext/syntheses/seven-failure-modes.md — whole file, esp. "Operating Principle", Modes 1–7, "The Failure Mode Index", "Deployment Protocol"

PASSAGE: [QUOTE] "These are the specific, named ways a worldtext directory breaks. They are not metaphors. They are diagnostic categories with tests, symptoms, and fixes." [QUOTE] "A worldtext that detects all seven is alive. A worldtext that detects none is dead."

RESEARCH OBJECT: A failure taxonomy for knowledge repositories, each mode equipped with definition, symptom, diagnostic test, fix, and source lineage: (1) Vermeer Problem, (2) Semantic Bleaching, (3) Dead Operations, (4) Broken Memex Trail, (5) Theory-Execution Gap, (6) Invisible Breakdown, (7) Operator as Product.

LOCAL MOVE: The file converts vague worry ("the wiki is decaying") into seven named, individually testable pathologies — a nosology — and then binds each to a scheduled instrument ("Run Modes 1–6 as part of every LINT pass. Run Mode 7 quarterly as part of the AUDIT verb.").

SOURCE TERMS: Vermeer Problem; semantic bleaching; dead operations; broken memex trail; theory-execution gap; invisible breakdown; operator as product; Fragile Expert phenotype; "failures are not errors. They are invitations to re-examine the commitment structure."

WHAT BECAME STRANGE: Mode 1 defines a failure that produces *excellent* output: [QUOTE] "Output is technically excellent, aesthetically coherent, and epistemically vacuous." Quality of prose is orthogonal to — and can mask — epistemic death. The best-looking worldtext may be the deadest.

QUESTION: Is the taxonomy actually complete (the file claims "the complete failure taxonomy"), or are there modes it structurally cannot see — e.g., a taxonomy-capture mode where the seven categories themselves bleach into ritual checklist?

DEEPER QUESTION: Modes 1–6 are artifact-side and Mode 7 is operator-side; is any failure taxonomy of a human-AI system forced to end in a self-referential mode (the classifier classifying its own classifier), and can that final mode ever have a non-circular diagnostic?

MECHANISM: Each mode carries an executable diagnostic. Mode 1: [QUOTE] "Change one noun in the description. If the description still works without cascading consequence, it is fluent but not adequate." Mode 2: count corpus occurrences, flag >100. Mode 3: check chronicle.md for evidence of each declared verb. Mode 4: random entity page, follow [source-id] chain to evidence/. Mode 5: compare cosmological claims to processed-source counts. Mode 6: check lint coverage of five decay classes. Mode 7: quarterly self-audit questions.

FORMAL SHIFT: From "quality assurance" as a single gradient to a discrete diagnosis space where each pathology has its own detector and its own repair — failure becomes typed.

SOURCE FORMALISM: The Failure Mode Index table mapping each mode to its detecting instrument: Vermeer→dse.json, Bleaching→tenne.json, Dead Operations→meta.json, Broken Trail→memex.json, Theory-Execution Gap→argue.json, Invisible Breakdown→dac.json, Operator as Product→thick.json. Plus two in-file empirical status claims: [QUOTE] "Current Status: 4 dead operations identified: crosslink, condense, expand, cluster_worlds" and [QUOTE] "The filesystem shows 93.6% of sources unprocessed."

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Failure modes as a partition of the complement of the invariant set: each mode M_i = a class of states s where LINT_i(s) fires; completeness claim = ⋃M_i ⊇ all reachable degraded states, which is unprovable without a model of the reachable state space.

TENSION: Mode 5 says the theory-execution gap "is not the failure — the invisibility of the gap is the failure," but the Index still lists the gap itself as a mode; the file oscillates between failure-as-state and failure-as-undetected-state. Also, the noun-swap test of Mode 1 duplicates the Salt Water Test at sentence scale — rival reading: Mode 1 is not a distinct pathology but the micro-form of failed propagation.

MISSING: Severity ordering among the seven; interaction effects (does bleaching accelerate trail-breaking?); base rates — how often each mode actually occurs in this repo beyond the two figures given; a protocol for retiring or splitting modes.

BOUNDARY: The taxonomy diagnoses a *directory* plus one operator; it says nothing about multi-operator worldtexts where failure can live in disagreement between operators' theories.

CITATION TRAIL: seven-failure-modes.md → dse.json/tenne.json/meta.json/memex.json/argue.json/dac.json/thick.json (evidence instruments) → Geertz (wink vs. twitch), Bush (associative trails), Naur via argue.json → operationalized as L1–L9 in worldtext-formal-engine.md.

TEST: Two checkable claims: (a) the four named dead operations (crosslink, condense, expand, cluster_worlds) should have no execution evidence in worldtext/chronicle.md — grep-verifiable; (b) 93.6% of sources unprocessed — countable against evidence/ vs worldtext/sources/.

PLATFORM: Any markdown knowledge repo with a chronicle and provenance tags; instruments named as JSON evidence files in this repo.

LINKS: [[FORAGE-WT-002]], [[FORAGE-WT-005]], [[FORAGE-WT-007]], [[FORAGE-WT-013]]

BIBTEX: @unpublished{seven-failure-modes-2026, title={The Seven Failure Modes of Worldtext}, note={worldtext/syntheses/seven-failure-modes.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
