ZETTEL

ID: FORAGE-WT-003

TITLE: The Salt Water Test: consequence propagation is the proof of coherence

SOURCE: worldtext/syntheses/worldtext-formal-engine.md — §IV "Consequence Propagation", §VII "Evaluation Criteria", §IX "Counter-Reading"; corroborated by worldtext/syntheses/vertical-axis.md — "The Drowned Parish Example"

PASSAGE: [QUOTE] "If the system produces only `Updated: \"salt water is profane\" → \"salt water is medicinal\"` and nothing else, it has failed. The consequence graph is the proof of coherence. No propagation = no worldtext." [QUOTE from vertical-axis.md] "Change \"salt water is profane\" to \"salt water is medicinal\" and watch the consequences propagate through the entire system. That propagation is the proof that Worldtext is operating."

RESEARCH OBJECT: A falsifiable acceptance test for world-coherence systems: modify exactly one invariant of a fictional world (the Drowned Parish) and measure whether the system enumerates downstream affected rules, entities, new violations, and repair actions.

LOCAL MOVE: Instead of defining coherence positively, the file defines it operationally by its response to perturbation — coherence is what propagates. A single-sentence edit becomes a probe of the entire causal fabric.

SOURCE TERMS: Salt Water Test; PROPAGATE; consequence_neighbors; affected set; repair_action {target, reason, suggested_fix}; Drowned Parish; INVARIANT/COMMITMENT/CULTURAL LOGIC/FAILURE MODE (the entry's four constraint kinds, per vertical-axis.md).

WHAT BECAME STRANGE: A theological proposition ("salt water is profane") functions as a load-bearing dependency for a blacksmith's work schedule, building height limits, and cartography law — religion is rendered as a dependency graph where doctrine has a build order.

QUESTION: What is the ground-truth affected set for a one-invariant change — who decides that "navigation is oral" depends on salt theology ("may lose rationale") but some other rule does not?

DEEPER QUESTION: Is the consequence relation in a fictional world discovered (implicit in the text, recoverable by any competent reader) or constructed (authored as consequence edges) — and if constructed, is the Salt Water Test testing the world or testing the diligence of whoever drew the edges?

MECHANISM: [QUOTE] "1. affected ← {R}; 2. frontier ← consequence_neighbors(R) in G; 3. while frontier ≠ ∅: node ← frontier.pop(); if node ∉ affected: affected ← affected ∪ {node}; frontier ← frontier ∪ consequence_neighbors(node); 4. For each node ∈ affected: run LINT({node}) with updated R; collect violations; 5. For each violation: generate repair_action" — BFS transitive closure over consequence edges, then localized re-lint.

FORMAL SHIFT: From coherence-as-static-consistency to coherence-as-perturbation-response: the unit of evaluation is not a state but a delta and its closure.

SOURCE FORMALISM: [QUOTE] "PROPAGATE(R: Rule, change: Δ) → { affected_rules: Set<Rule>, affected_entities: Set<Entity>, new_violations: Set<Violation>, repair_actions: List<Action> }". Pass condition [QUOTE]: "Changing one invariant produces ≥5 affected nodes and ≥2 violations." Expected output includes new violations "CONTRADICTION: \"blacksmith avoids salt\" conflicts with \"salt is medicinal\"" and "THIN_DESCRIPTION: \"healer\" entity lacks salt-medicine protocol".

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Salt Water Test as a benchmark tuple B = (W, δ, A*, V*) where W is a world spec, δ a single-invariant edit, A* the gold affected set, V* the gold violation set; system score = F1(A, A*) + F1(V, V*). A benchmark suite is a distribution over (W, δ) pairs with human-annotated closures.

TENSION: §IX flatly retracts the automation claim: [QUOTE] "The 'Salt Water Test' can be demonstrated manually; automating it requires semantic reasoning that remains an open research problem." So the file's central proof-procedure is, by its own counter-reading, currently a thought experiment. Rival readings: (a) the test is a benchmark awaiting implementation; (b) the test is a pedagogical fiction whose value is normative, not empirical.

MISSING: Ground-truth annotation protocol; inter-annotator agreement on affected sets; any worked example beyond the single Drowned Parish case; treatment of propagation through *entities* (the algorithm traverses consequence edges between rules, yet the expected output lists five affected entities).

BOUNDARY: The test measures closure over *declared* consequence edges; it cannot detect consequences the edge-author never encoded — the very consequences a reader of fiction supplies for free.

CITATION TRAIL: worldtext-formal-engine.md §IV → vertical-axis.md (Drowned Parish worldtext entry, the source world for the test) → seven-failure-modes.md Mode 1 (unpropagated edits = Vermeer-fluent emptiness).

TEST: Checkable empirical claim, stated in-file: the perturbation must yield ≥5 affected nodes and ≥2 violations. Run manually against the Drowned Parish entry with independent annotators; compare to the file's own expected YAML output.

PLATFORM: LLM-assisted manual demonstration today; automated version requires semantic entailment over natural-language rules (open problem, per §IX).

LINKS: [[FORAGE-WT-001]], [[FORAGE-WT-002]], [[FORAGE-WT-005]], [[FORAGE-WT-012]]

BIBTEX: @unpublished{worldtext-formal-engine-2026, title={Worldtext Formal Engine — Coherence-Preserving Repository Runtime}, note={worldtext/syntheses/worldtext-formal-engine.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}} ; @unpublished{vertical-axis-2026, title={The Vertical Axis — Worldtext as Hostile Extraction}, note={worldtext/syntheses/vertical-axis.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
