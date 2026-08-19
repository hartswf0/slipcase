ZETTEL

ID: FORAGE-PG-002

TITLE: The composition protocol licenses ordered sequences and flagged conflicts — it cannot merge claims

SOURCE: PROGRAMS/meta.json — <Operational Description>.THE COMPOSITION PROTOCOL; <Program Text>.=== COMPOSE ===; <Failure Description>.COMPOSITION_WITHOUT_AUDIT

PASSAGE: [QUOTE] "FOR EACH pair (<theory_A>, <theory_B>) in <diagnostic_suite>: [check-for-entity-conflict]: IF <theory_A> [names-entity] <E> AND <theory_B> [names-entity] <E> AND <theory_A.definition(E)> [contradicts] <theory_B.definition(E)> THEN [flag-conflict] and [require-operator-ruling]"; "[check-for-productive-tension]: IF <theory_A> [examines-different-aspect-of] <same-phenomenon> AS <theory_B> THEN [mark-complementary] and [compose-as-sequence]"; ordering rule: "ORDER <theory_set> by { dependency (prerequisites first), lineage (same lineage grouped), scope (broad to narrow) }".

RESEARCH OBJECT: What composition actually licenses in the Program of Programs: three and only three outcomes per theory pair — flag-and-escalate (contradiction), mark-complementary-and-sequence (tension), or silent coexistence (no shared entities). There is no fourth outcome that produces a merged claim.

LOCAL MOVE: Read the COMPOSE directive as a type signature rather than a workflow, and enumerate its codomain.

SOURCE TERMS: diagnostic_suite; entity-conflict; invariant-conflict; productive-tension; operator-ruling; composite_reading; ExplanationGate

WHAT BECAME STRANGE: The protocol's contradiction test requires a computable predicate contradicts(def_A(E), def_B(E)) over prose definitions — but meta.json's own Residual Human Theory declares "<when-two-theories-conflict-which-wins> cannot be automated." So the COMPOSE engine can detect conflicts it is constitutionally forbidden to resolve; composition is structurally an escalation machine.

QUESTION: Under this protocol, is a full-corpus deployment (CLAUDE.md's "DEPLOY ALL") even well-formed, given the actual entity conflicts documented in FORAGE-PG-006/007/008?

DEEPER QUESTION: Is a "composite reading" a conjunction, a sequence of lenses, or a polyphony? The protocol's answer — MERGE reports then HOLD at gate — leaves the logical status of the composite deliberately undefined, which may be the point.

MECHANISM: Pairwise O(n²) conflict audit before deployment; escalation of undecidables to the operator; monotone ordering heuristic (dependency → lineage → scope) that never reorders on content.

FORMAL SHIFT: From theories-as-propositions (which would compose by conjunction and explode on contradiction) to theories-as-instruments (which compose by sequencing and tolerate contradiction as flagged metadata).

SOURCE FORMALISM: Pseudocode COMPOSE directive with pairwise checks; operator notation for the three outcomes.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Composition is a partial monoid on suites: A ⊕ B defined iff conflict(A,B) has been adjudicated; ⊕ is associative on conflict-free subsets but adjudication is not — operator rulings on (A,B) then (AB,C) can differ from rulings on (B,C) then (A,BC). The corpus therefore lacks confluence: suite order is semantics, not presentation. The protocol half-admits this by making order a mandatory step.

TENSION: Rival reading 1: the protocol is paraconsistent by design — contradictions are quarantined per-pair so the suite never trivializes (no ex falso). Rival reading 2: the protocol merely defers inconsistency to the "composite reading" stage where MERGE has no defined semantics, i.e., the hard problem is moved, not solved. The text supports both: quarantine machinery is precise, merge machinery is one word ("MERGE <diagnostic_reports>").

MISSING: Any worked example of an operator ruling on a flagged conflict; a definition of MERGE; a notion of suite equivalence under reordering.

BOUNDARY: Applies to composing theories into diagnostic suites; does not govern composing two theories into a new theory (that is the separate MERGE directive with retirement of both originals).

CITATION TRAIL: meta.json COMPOSE ← CLAUDE.md COMPOSE directive and cross-reference table of nine "productive tension" pairs ← child theories' entity sets.

TEST: Run COMPOSE on {thick, tda} (both Geertzian): the entity <culture> receives contradictory definitions (instruction system vs. contested public world, see FORAGE-PG-006). Protocol-conformant output must be flag-conflict + require-operator-ruling; if an implementation returns "complementary," it has failed the protocol's own contradiction check.

PLATFORM: LLM session under PROGRAMS/CLAUDE.md; the check is executable as a structured prompt over two JSON files.

LINKS: [[FORAGE-PG-006]], [[FORAGE-PG-007]], [[FORAGE-PG-008]], [[FORAGE-PG-005]], [[FORAGE-PG-001]]

BIBTEX: @unpublished{meta2026program, title={META — The Program of Programs}, note={PROGRAMS/meta.json, version 1.0, OPERATION-DESCRIBE repository, unpublished}, year={2026}}
